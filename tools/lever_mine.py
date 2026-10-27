"""Mechanical candidates for the platform guide's quiet levers in one extracted Docket bundle.

Usage:
  python tools/docket_agent.py mine tasks/<slug>          write notes/mine.md and print a summary
  python tools/lever_mine.py tasks/<slug> [--stdout]      the same, or print the Markdown instead

The guide's Hard advice (2026-10-16, section 5, "Where solvers fail") says strong solvers read every
page, so a fact the documents state plainly gets found; what they reliably miss is what the documents
never say directly. Its method for finding those slips: "compare every quote of the same passage across
documents, every spelling of each name, each figure against its earlier versions, and each summary
against the rest of the document." A script can make those comparisons over text/Dnn.txt, so this one
does, and lists where to look under the levers each comparison serves. It proposes no question, judges
no reading and runs no model. Every candidate needs its passages read in full before it becomes a hook
in notes/hooks.md, and most never will. Line numbers are text/Dnn.txt line numbers.
"""
from __future__ import annotations

import argparse
import calendar
import difflib
import hashlib
import json
import re
import sys
import time
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import check_questions as cq

VERSION = 1
SHINGLE = 8          # words in a seed: long enough to skip stock phrases, short enough for a re-quote
MAX_OCCURRENCES = 8  # a seed printed more often than this across the bundle is boilerplate
MIN_MATCH = 20       # words two passages must share around their edits to count as one passage
MAX_EDIT = 12        # an edit longer than this on either side ends the shared passage
GAP = MAX_EDIT + SHINGLE + 4  # seeds this close on one diagonal belong to one passage
MARGIN = 2 * MAX_EDIT  # words aligned beyond the outermost seeds, where an edit stops a seed from forming
ANCHOR = 4             # a shared passage starts and ends with at least this many equal words
QUIET_EDITS = 4      # a passage with more edits is a recurring template, reported only as a count
SELF_GAP = 150       # words apart before two passages of one document count as a repeat
CONTEXT = 6          # words of context printed on each side of an edit
LIMITS = {"passages": 40, "per_pair": 6, "parallels": 25, "restated": 80, "per_doc": 8, "rows": 30, "names": 30}

WORD = re.compile(r"[A-Za-z0-9$%£€][A-Za-z0-9$%£€.,'’/&-]*")
PAGE_MARK = re.compile(r"^=== page \d+ ===$")
HEADER = re.compile(r"^# D\d{2,3} \|")
MONTHS = {name.lower(): number for number, name in enumerate(calendar.month_name) if name}
MONTHS.update({name.lower(): number for number, name in enumerate(calendar.month_abbr) if name})
MONTHS["sept"] = 9
PERIOD_WORDS = set(MONTHS) | set("first second third fourth q1 q2 q3 q4 h1 h2 fy three six nine twelve "
                                 "quarter quarters half year years month months".split())
QUALIFIERS = set("not no never none nor except unless only excluding including without may might could "
                 "would should must shall likely unlikely all any each every some most least approximately "
                 "about nearly over under".split())


def norm_word(raw: str) -> str:
    """One printed word as the comparisons see it: case, curly quotes and trailing punctuation dropped, and
    hyphens inside words removed ("non-residents" re-quoted as "nonresidents" is the same word)."""
    word = unicodedata.normalize("NFKC", raw).translate(cq.QUOTES).lower().rstrip(".,'/-&")
    if not any(ch.isdigit() for ch in word):
        word = word.replace("-", "")
    return word


@dataclass
class Doc:
    doc_id: str
    lines: list[str]
    words: list[str] = field(default_factory=list)    # normalised words
    raw: list[str] = field(default_factory=list)      # the same words as printed
    line_of: list[int] = field(default_factory=list)  # text/Dnn.txt line number of each word

    def is_prose(self, number: int) -> bool:
        line = self.lines[number - 1]
        return len(line) >= 80 and "|" not in line and "\t" not in line

    def snippet(self, number: int, start: int, end: int, width: int = 90) -> str:
        line = self.lines[number - 1]
        left, right = max(0, start - width), min(len(line), end + width)
        text = " ".join(line[left:right].split())
        return ("..." if left else "") + text + ("..." if right < len(line) else "")


def load(bundle: cq.Bundle) -> list[Doc]:
    docs = []
    for doc_id in sorted(bundle.live_ids()):
        path = bundle.path / "text" / f"{doc_id}.txt"
        if not path.is_file() or path.is_symlink():
            continue
        lines = cq.read_text(path).split("\n")
        doc = Doc(doc_id, lines)
        for number, line in enumerate(lines, 1):
            if (number == 1 and HEADER.match(line)) or PAGE_MARK.match(line.strip()):
                continue
            for match in WORD.finditer(line):
                word = norm_word(match.group(0))
                if word:
                    doc.words.append(word)
                    doc.raw.append(match.group(0))
                    doc.line_of.append(number)
        docs.append(doc)
    return docs


def prose_hits(doc: Doc, pattern: re.Pattern, limit: int, prose_only: bool = True) -> list[dict]:
    hits = []
    for number, line in enumerate(doc.lines, 1):
        if prose_only and not doc.is_prose(number):
            continue
        for match in pattern.finditer(line):
            hits.append({"doc": doc.doc_id, "line": number, "match": " ".join(match.group(0).split()),
                         "snippet": doc.snippet(number, match.start(), match.end())})
            break
        if len(hits) >= limit:
            break
    return hits


# 1. The same passage in two places with a few words or figures changed.

@dataclass
class Edit:
    kind: str  # figure, qualifier, wording; period, numbering and spelling edits score nothing
    left: str
    right: str
    before: str
    after: str
    line_a: int
    line_b: int
    size: int = 1  # words on the longer side

    @property
    def score(self) -> float:
        """Short edits are the quiet ones: one inserted clause or one changed figure in a long shared passage."""
        weight = {"figure": 3, "qualifier": 3, "wording": 2 if not (self.left and self.right) else 1}
        return weight.get(self.kind, 0) * (1 if self.size <= 3 else 0.5 if self.size <= 6 else 0.25)


@dataclass
class Passage:
    doc_a: str
    doc_b: str
    line_a: tuple[int, int]
    line_b: tuple[int, int]
    matched: int
    edits: list[Edit]
    spread: int = 2         # documents that print the passage's opening words
    other_period: bool = False  # the two sides' lines name different periods ("three" vs "six months ended")

    @property
    def periodic(self) -> bool:
        """The two sides report different periods (a date changed, or their lines name different periods)."""
        return self.other_period or any(edit.kind == "period" for edit in self.edits)

    def effective(self, edit: Edit) -> float:
        """A figure that changes along with the period is expected, so it scores nothing; a changed word in the
        same passage still counts (Wyndham: "Rooms grew 4%" became "Global Rooms grew 3%, or 4% excluding Revo")."""
        return 0 if self.periodic and edit.kind == "figure" else edit.score

    @property
    def template(self) -> bool:
        """A passage with many changes, a table row whose figures all differ, or one whose only changes are a
        date, an item number or figures that move with the period, is a recurring frame (a results sentence
        rolled forward, a re-quoted consultation question); only its count is reported. A passage that adds
        or drops a qualifier ("excluding Revo,") is kept however much else changed."""
        kinds = [edit.kind for edit in self.edits]
        kept = "qualifier" in kinds and len(self.edits) <= 3 * QUIET_EDITS
        return ((len(self.edits) > QUIET_EDITS or kinds.count("figure") >= 3) and not kept
                or not any(self.effective(edit) > 0 for edit in self.edits))

    @property
    def score(self) -> float:
        """The best edit counts fully and the rest by half (two points at most, so a rewritten passage does
        not outrank one quiet edit), plus a bonus for a long shared passage and for a passage two documents
        share (the guide's re-quote). A passage four or more documents print (a consultation's own question,
        a boilerplate notice) counts by half."""
        scores = sorted((self.effective(edit) for edit in self.edits), reverse=True)
        points = ((scores[0] if scores else 0) + min(sum(scores[1:]) / 2, 2) + min(self.matched, 80) / 40
                  + (1 if self.doc_a != self.doc_b else 0))
        return points / 2 if self.spread >= 4 else points


def is_period_edit(words: list[str]) -> bool:
    """A date or period roll-forward ("March 31, 2026" for "June 30, 2026"; "six" months for "three")."""
    if not words:
        return False
    named = any(word in PERIOD_WORDS for word in words)
    for word in words:
        if word in PERIOD_WORDS or re.fullmatch(r"(?:19|20)\d\d(?:[-/](?:\d\d|(?:19|20)\d\d))?,?", word):
            continue
        if named and re.fullmatch(r"\d{1,2},?", word) and int(word.rstrip(",")) <= 31:
            continue
        return False
    return True


def edit_kind(left: list[str], right: list[str]) -> str:
    words = left + right
    if is_period_edit(words):
        return "period"
    if left and right and "".join(left) == "".join(right):
        return "spelling"  # a word the extraction split ("sophis cated")
    if len(left) == len(right) == 1 and not any(ch.isdigit() for ch in left[0] + right[0]):
        a, b = sorted((left[0].replace("/", ""), right[0].replace("/", "")), key=len)
        if b.startswith(a[:max(5, len(a) - 2)]):
            return "spelling"  # "financial" re-quoted as "financially", "client/s" as "clients"
    figures = [word for word in words if any(ch.isdigit() for ch in word)]
    if figures and all(re.fullmatch(r"(?:q\.?)?\d{1,3}[.)]?", word) for word in figures) and all(
            len(word) <= 4 or word in {"page", "pages"} for word in words if word not in figures):
        return "numbering"  # a renumbered question or list item, or a page number
    if figures:
        return "figure"
    if len(words) <= 6 and any(word in QUALIFIERS for word in words):
        return "qualifier"
    return "wording"


def seeds(docs: list[Doc]) -> tuple[dict[tuple[int, int], list[tuple[int, int]]], dict[tuple[str, ...], int]]:
    """Pairs of positions sharing a SHINGLE-word run, by document pair, and how many documents print each run."""
    index: dict[tuple[str, ...], list[tuple[int, int]]] = defaultdict(list)
    for number, doc in enumerate(docs):
        for i in range(len(doc.words) - SHINGLE + 1):
            index[tuple(doc.words[i:i + SHINGLE])].append((number, i))
    pairs: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    spread: dict[tuple[str, ...], int] = {}
    for key, spots in index.items():
        if len(spots) < 2:
            continue
        spread[key] = len({number for number, _ in spots})
        if len(spots) > MAX_OCCURRENCES:
            continue
        for x, first in enumerate(spots):
            for second in spots[x + 1:]:
                (da, ia), (db, ib) = sorted((first, second))
                if da == db and ib - ia < SELF_GAP:
                    continue
                pairs[(da, db)].append((ia, ib))
    return pairs, spread


def chain(spots: list[tuple[int, int]]) -> list[list[int]]:
    """Group seeds lying on nearly one diagonal into passages: [start_a, end_a, start_b, end_b, diagonal]."""
    done, live = [], []
    for ia, ib in sorted(set(spots)):
        diagonal = ib - ia
        for block in live:
            if (ia <= block[1] + GAP and abs(diagonal - block[4]) <= MAX_EDIT
                    and block[2] - GAP <= ib <= block[3] + GAP):
                block[1], block[3], block[4] = max(block[1], ia), max(block[3], ib), diagonal
                break
        else:
            live.append([ia, ia, ib, ib, diagonal])
        still = []
        for block in live:
            (done if block[1] + GAP < ia else still).append(block)
        live = still
    return done + live


def passages(docs: list[Doc]) -> tuple[list[Passage], dict[tuple[str, str], int]]:
    """Shared passages with small edits, and how many identical shared passages each pair of documents has."""
    found: list[Passage] = []
    identical: dict[tuple[str, str], int] = defaultdict(int)
    pairs, spread = seeds(docs)
    for (da, db), spots in sorted(pairs.items()):
        a, b = docs[da], docs[db]
        for block in chain(spots):
            if da == db and block[2] < block[1] + SHINGLE:
                continue  # a passage overlapping its own repeat is one passage, not two
            sa, ea = max(0, block[0] - MARGIN), min(len(a.words), block[1] + SHINGLE + MARGIN)
            sb, eb = max(0, block[2] - MARGIN), min(len(b.words), block[3] + SHINGLE + MARGIN)
            if da == db and sb < ea:
                sb = ea = (block[1] + SHINGLE + block[2]) // 2  # the two copies' margins meet halfway
            ops = difflib.SequenceMatcher(None, a.words[sa:ea], b.words[sb:eb], autojunk=False).get_opcodes()
            segment: list[tuple] = []
            for op in ops + [("break", 0, 0, 0, 0)]:
                tag, i1, i2, j1, j2 = op
                if tag == "equal" or (tag != "break" and i2 - i1 <= MAX_EDIT and j2 - j1 <= MAX_EDIT):
                    segment.append(op)
                    continue
                # Trim to where the two texts run together: an edge whose equal run is shorter than ANCHOR is
                # where the passages diverge (a letterhead, a re-quoted question followed by different answers).
                while segment and (segment[-1][0] != "equal" or segment[-1][2] - segment[-1][1] < ANCHOR):
                    segment.pop()
                while segment and (segment[0][0] != "equal" or segment[0][2] - segment[0][1] < ANCHOR):
                    segment.pop(0)
                matched = sum(o[2] - o[1] for o in segment if o[0] == "equal")
                if segment and matched >= MIN_MATCH:
                    found_passage = build(a, b, sa, sb, segment, matched)
                    opening = tuple(a.words[sa + segment[0][1]:sa + segment[0][1] + SHINGLE])
                    found_passage.spread = spread.get(opening, 2)
                    if found_passage.edits:
                        found.append(found_passage)
                    else:
                        identical[(a.doc_id, b.doc_id)] += 1
                segment = []
    return found, dict(identical)


def build(a: Doc, b: Doc, sa: int, sb: int, segment: list[tuple], matched: int) -> Passage:
    edits = []
    for tag, i1, i2, j1, j2 in segment:
        if tag == "equal":
            continue
        left, right = a.words[sa + i1:sa + i2], b.words[sb + j1:sb + j2]
        if left == right:
            continue
        before = " ".join(a.raw[max(sa + segment[0][1], sa + i1 - CONTEXT):sa + i1])
        after = " ".join(a.raw[sa + i2:min(sa + segment[-1][2], sa + i2 + CONTEXT)])
        edits.append(Edit(edit_kind(left, right), " ".join(a.raw[sa + i1:sa + i2]),
                          " ".join(b.raw[sb + j1:sb + j2]), before, after,
                          a.line_of[min(sa + i1, len(a.line_of) - 1)], b.line_of[min(sb + j1, len(b.line_of) - 1)],
                          max(len(left), len(right))))
    first_a, last_a = sa + segment[0][1], sa + segment[-1][2] - 1
    first_b, last_b = sb + segment[0][3], sb + segment[-1][4] - 1
    lines_a, lines_b = (a.line_of[first_a], a.line_of[last_a]), (b.line_of[first_b], b.line_of[last_b])
    spans_a = {span for n in range(lines_a[0], lines_a[1] + 1) for span in spans_in(a.lines[n - 1])}
    spans_b = {span for n in range(lines_b[0], lines_b[1] + 1) for span in spans_in(b.lines[n - 1])}
    return Passage(a.doc_id, b.doc_id, lines_a, lines_b, matched, edits,
                   other_period=bool(spans_a and spans_b and spans_a != spans_b))


# 2. Parallel sentences in different words: two documents state the same rule or fact in their own wording,
#    and one carries an exception, condition or qualifier the other lacks (aq-02562, Hard: the MASC rule's
#    "unless ... average adjusted gross farm income is at least ..." against the ASCF rule's plain cap).

SENTENCE = re.compile(r"(?<=[.;])\s+(?=[A-Z(\"“])")
CONTENT = re.compile(r"[a-z][a-z'-]{3,}|\$?\d[\d,]*(?:\.\d+)?%?")
STRONG_MARKERS = ("unless", "except", "excluding", "provided that", "other than", "notwithstanding",
                  "does not apply", "only if", "no longer")
MARKERS = STRONG_MARKERS + ("only", "not", "including", "may", "must", "at least", "at most", "up to",
                            "more than", "less than")
PARALLEL = {"min_words": 12, "rare": 40, "shared": 6, "low": 0.35, "high": 0.9}


@dataclass
class Sentence:
    doc_id: str
    line: int
    text: str
    words: frozenset

    def markers(self) -> set[str]:
        low = " " + " ".join(norm_word(w) for w in self.text.split()) + " "
        return {m for m in MARKERS if f" {m} " in low}


def sentences(docs: list[Doc]) -> list[Sentence]:
    found = []
    for doc in docs:
        for number, line in enumerate(doc.lines, 1):
            if not doc.is_prose(number) and len(line) < 120:
                continue
            for part in SENTENCE.split(line):
                words = frozenset(w for w in (norm_word(m.group(0)) for m in CONTENT.finditer(part.lower()))
                                  if w not in cq.STOP)
                if len(words) >= PARALLEL["min_words"]:
                    found.append(Sentence(doc.doc_id, number, " ".join(part.split()), words))
    return found


def parallels(docs: list[Doc]) -> list[dict]:
    """Sentence pairs in different documents sharing most of their content words without being copies,
    ranked first where an exception or qualifier word sits in one sentence only."""
    items = sentences(docs)
    frequency: dict[str, int] = defaultdict(int)
    for item in items:
        for word in item.words:
            frequency[word] += 1
    postings: dict[str, list[int]] = defaultdict(list)
    for number, item in enumerate(items):
        for word in item.words:
            if frequency[word] <= PARALLEL["rare"]:
                postings[word].append(number)
    found, seen = [], set()
    for number, item in enumerate(items):
        shared: dict[int, int] = defaultdict(int)
        for word in item.words:
            for other in postings.get(word, ()):
                if other > number and items[other].doc_id != item.doc_id:
                    shared[other] += 1
        for other, count in shared.items():
            if count < PARALLEL["shared"]:
                continue
            mate = items[other]
            similarity = len(item.words & mate.words) / len(item.words | mate.words)
            if not PARALLEL["low"] <= similarity < PARALLEL["high"]:
                continue
            key = (item.doc_id, item.line, mate.doc_id, mate.line)
            if key in seen:
                continue
            seen.add(key)
            only_a, only_b = item.markers() - mate.markers(), mate.markers() - item.markers()
            strong = sum(m in STRONG_MARKERS for m in only_a | only_b)
            found.append({"doc_a": item.doc_id, "line_a": item.line, "doc_b": mate.doc_id, "line_b": mate.line,
                          "similarity": round(similarity, 2), "markers_a": sorted(only_a), "markers_b": sorted(only_b),
                          "text_a": item.text[:240], "text_b": mate.text[:240],
                          "score": min(strong, 2) * 3 + min(len(only_a | only_b) - strong, 2) + similarity})
    # A sentence with a parallel in three or more other documents is boilerplate (a Federal Register rule's
    # Executive Order 12866 paragraph), so it counts by half.
    mates: dict[tuple[str, int], set[str]] = defaultdict(set)
    for item in found:
        mates[(item["doc_a"], item["line_a"])].add(item["doc_b"])
        mates[(item["doc_b"], item["line_b"])].add(item["doc_a"])
    for item in found:
        if max(len(mates[(item["doc_a"], item["line_a"])]), len(mates[(item["doc_b"], item["line_b"])])) >= 3:
            item["score"] /= 2
    found.sort(key=lambda f: (-f["score"], f["doc_a"], f["line_a"], f["doc_b"], f["line_b"]))
    return found[:LIMITS["parallels"]]


# 3. Statements that a figure, table or definition was restated, recast, revised or redefined.

RESTATED = [
    ("restated or recast", re.compile(
        r"\b(?:recast(?:ed)?|(?<!amended and )restat(?:ed|ement|ements|ing)(?! (?:senior |unsecured |revolving )*"
        r"(?:credit |loan |employment )?(?:agreement|certificate|bylaws|charter|articles|plan|indenture)s?\b)|"
        r"re-presented|reclassifi(?:ed|cation|cations)|"
        r"conform(?:ed)? (?:to|with) (?:the )?current(?:[- ]period| year)? presentation|"
        r"discontinued operations?)\b", re.I)),
    ("previously reported", re.compile(
        r"\b(?:as )?previously (?:reported|presented|announced|published|estimated|forecast|projected)\b",
        re.I)),
    ("definition or basis changed", re.compile(
        r"\b(?:(?:new|updated|revised|amended|changed?|modified) (?:definition|methodology|basis|presentation|"
        r"calculation|measure)|no longer (?:includes?|excludes?|reports?|presents?|adjusts?|reflects?)|"
        r"(?:now|instead) (?:defines?|excludes?|includes?|presents?|reports?|calculates?)|"
        r"beginning (?:with|in) (?:the )?(?:first|second|third|fourth|fiscal|q[1-4]|20\d\d))\b", re.I)),
    ("estimate or guidance revised", re.compile(
        r"\b(?:revised (?:upward|downward|up|down|from|to)|(?:raised|lowered|narrowed|widened|reaffirm(?:ed|s)?|"
        r"updated|increased|decreased|cut|trimmed) (?:its |our |the )?(?:full[- ]year |annual |20\d\d )?"
        r"(?:guidance|outlook|forecast|estimate|projection)s?|(?:first|latest|previous|prior|initial) "
        r"(?:forecast|estimate|projection)s?)\b", re.I)),
]


def restatements(docs: list[Doc]) -> list[dict]:
    hits = []
    for doc in docs:
        mine = []
        for number, line in enumerate(doc.lines, 1):
            for label, pattern in RESTATED:
                match = pattern.search(line)
                if match:
                    mine.append({"doc": doc.doc_id, "line": number, "kind": label,
                                 "snippet": doc.snippet(number, match.start(), match.end(), 110)})
                    break
        hits.extend(mine[:LIMITS["per_doc"] + 4])
    return hits[:LIMITS["restated"]]


# 4. Periods printed only cumulatively: a quarter no document reports on its own.

SPAN = re.compile(r"\b(three|six|nine|twelve|3|6|9|12)[- ]months?\s+(?:period\s+)?ended\s+([A-Za-z]{3,9})\.?\s+(\d{1,2})",
                  re.I)
YEAR_END = re.compile(r"\b(?:fiscal\s+)?years?\s+ended\s+([A-Za-z]{3,9})\.?\s+(\d{1,2})", re.I)
QUARTER_END = re.compile(r"\bquarters?\s+ended\s+([A-Za-z]{3,9})\.?\s+(\d{1,2})", re.I)
SPAN_MONTHS = {"three": 3, "six": 6, "nine": 9, "twelve": 12, "3": 3, "6": 6, "9": 9, "12": 12}
CASH = re.compile(r"\b(?:cash flows?|cash (?:provided|used|generated)|operating cash|free cash flow|capital expenditures?|"
                  r"repurchases? of (?:common )?(?:stock|shares)|share repurchases?|dividends paid|purchases of property)\b",
                  re.I)


def spans_in(line: str) -> list[tuple[int, int]]:
    """(months, month of the period end) for each period phrase in a line."""
    found = []
    for match in SPAN.finditer(line):
        month = MONTHS.get(match.group(2).lower())
        if month:
            found.append((SPAN_MONTHS[match.group(1).lower()], month))
    for pattern, months in ((YEAR_END, 12), (QUARTER_END, 3)):
        for match in pattern.finditer(line):
            month = MONTHS.get(match.group(1).lower())
            if month:
                found.append((months, month))
    return found


def periods(docs: list[Doc]) -> dict:
    printed: dict[tuple[int, int], set[str]] = defaultdict(set)
    cash_only: list[dict] = []
    for doc in docs:
        cash_spans: set[tuple[int, int]] = set()
        first_cash = None
        recent: list[tuple[int, list[tuple[int, int]]]] = []
        for number, line in enumerate(doc.lines, 1):
            here = spans_in(line)
            for span in here:
                printed[span].add(doc.doc_id)
            if here:
                recent.append((number, here))
            if CASH.search(line):
                near = here or next((spans for at, spans in reversed(recent) if number - at <= 25), [])
                if near:
                    cash_spans.update(near)
                    first_cash = first_cash or number
        if cash_spans and not any(months == 3 for months, _ in cash_spans):
            cash_only.append({"doc": doc.doc_id, "line": first_cash,
                              "spans": sorted({f"{months} months ended {calendar.month_name[month]}"
                                               for months, month in cash_spans})})
    derived = []
    for (months, month), where in sorted(printed.items()):
        if months == 3 or (3, month) in printed:
            continue
        earlier = (month - 3 - 1) % 12 + 1
        prior = (months - 3, earlier)
        source = sorted(printed.get(prior, set())) if months > 3 else []
        derived.append({"quarter_end": calendar.month_name[month], "cumulative": f"{months} months",
                        "documents": sorted(where),
                        "less": (f"{months - 3} months ended {calendar.month_name[earlier]}"
                                 + (f" ({', '.join(source)})" if source else " (not printed in the bundle)"))
                        if months > 3 else ""})
    return {"derived": derived, "cash_only": cash_only}


# 5. A row label printed in two documents with nearly equal but different values.

NUMBER = re.compile(r"\(?-?\$?\s?\d[\d,]*(?:\.\d+)?\)?%?")
GENERIC = {"total", "other", "net", "change", "percent change", "% change", "subtotal", "amount", "total other"}


def parse_value(text: str) -> tuple[float, bool] | None:
    raw = text.replace("$", "").replace(" ", "")
    negative = raw.startswith("(") and raw.rstrip("%").endswith(")") or raw.startswith("-")
    digits = raw.strip("()%-").replace(",", "")
    if not re.fullmatch(r"\d+(?:\.\d+)?", digits):
        return None
    if "." not in digits and "," not in raw and (len(digits) == 4 and 1990 <= int(digits) <= 2040 or int(digits) < 10):
        return None
    value = float(digits)
    return (-value if negative else value), raw.endswith("%")


def show(value: tuple[float, bool]) -> str:
    return f"{value[0]:,.10g}" + ("%" if value[1] else "")


def row(line: str) -> tuple[str, list[tuple[float, bool]]] | None:
    cells = [cell for cell in re.split(r"\s*\|\s*|\t+", line) if cell.strip()]
    if len(cells) >= 2 and re.search(r"[A-Za-z]{3}", cells[0]):
        label, rest = cells[0], " ".join(cells[1:])
    else:
        match = re.match(r"^\s*([A-Za-z][^\d$()]{5,80}?)\s*[$(]?\s*\d", line)
        if not match:
            return None
        label, rest = match.group(1), line[match.end(1):]
    if len(re.findall(r"[A-Za-z]", rest)) > 0.3 * max(1, len(rest.replace(" ", ""))):
        return None
    label = re.sub(r"\(\d\)|\([a-z]\)|\*|\$", " ", label.lower())
    label = " ".join(re.sub(r"[^a-z0-9%&' -]", " ", label).split())
    values = [value for value in (parse_value(m.group(0)) for m in NUMBER.finditer(rest)) if value]
    if len(label) < 8 or label in GENERIC or len(values) < 2:
        return None
    return label, values


def rows(docs: list[Doc]) -> list[dict]:
    """Shared labels whose values differ slightly, between two documents that also print some identical
    values under other shared labels (so they share a period, and an unchanged row would match)."""
    index: dict[str, dict[str, tuple[int, list[tuple[float, bool]]]]] = defaultdict(dict)
    for doc in docs:
        for number, line in enumerate(doc.lines, 1):
            parsed = row(line)
            if parsed:
                first, values = index[parsed[0]].get(doc.doc_id, (number, []))
                index[parsed[0]][doc.doc_id] = (first, values + parsed[1])
    pairs: dict[tuple[str, str], dict[str, list]] = defaultdict(lambda: {"exact": [], "near": []})
    for label, entries in index.items():
        ids = sorted(entries)
        for x, first in enumerate(ids):
            for second in ids[x + 1:]:
                (la, va), (lb, vb) = entries[first], entries[second]
                exact = {v for v in va if v in vb and (abs(v[0]) >= 100 or v[0] != int(v[0]))}
                near = [(p, q) for p in va for q in vb if p[1] == q[1] and p[0] != q[0] and p[0] * q[0] > 0
                        and abs(p[0] - q[0]) / max(abs(p[0]), abs(q[0])) <= 0.15]
                if exact:
                    pairs[(first, second)]["exact"].append(label)
                elif near:
                    pairs[(first, second)]["near"].append({"label": label, "line_a": la, "line_b": lb,
                                                           "values_a": [show(v) for v in va],
                                                           "values_b": [show(v) for v in vb]})
    found = []
    for (first, second), seen in sorted(pairs.items()):
        if len(seen["exact"]) >= 3 and seen["near"]:
            for item in seen["near"][:LIMITS["per_pair"]]:
                found.append({"doc_a": first, "doc_b": second, "shared_exact": len(seen["exact"]), **item})
    return found[:LIMITS["rows"]]


# 6. One thing under two names: an abbreviation defined in one document and used bare in another, and
#    spelling variants of one name across documents.

ABBR = re.compile(r"((?:The\s+)?[A-Z][A-Za-z&'’.-]*(?:\s+(?:of|and|for|the|on|in|to|&|[A-Z][A-Za-z&'’.-]*)){1,8})"
                  r"\s+\(\s*(?:the\s+)?[\"“']?([A-Z][A-Za-z0-9&.-]{1,11})[\"”']?\s*\)")
NAME = re.compile(r"\b[A-Z][A-Za-z'’]+(?:(?: |-)(?:(?:of|and|for|the|&) )?[A-Z][A-Za-z'’]+){0,5}\b")


def expansion_for(short: str, phrase: str) -> str | None:
    """The shortest tail of the phrase whose initials spell the abbreviation: "Prospectuses and Product
    Disclosure Statements (PDS)" is "Product Disclosure Statements"; small words may count ("CAMAC")."""
    letters = "".join(ch for ch in short if ch.isupper())
    words = re.sub(r"(?:'s|’s)$", "", phrase).split()
    if len(letters) < 2:
        return None
    for start in range(len(words) - 1, -1, -1):
        tail = words[start:]
        if tail[0][0].isupper() and letters in {"".join(w[0].upper() for w in tail if w[0].isupper()),
                                                 "".join(w[0].upper() for w in tail if w[0].isalpha())}:
            return " ".join(tail)
    return None


def abbreviations(docs: list[Doc]) -> list[dict]:
    defined: dict[str, tuple[str, str, int]] = {}
    for doc in docs:
        for number, line in enumerate(doc.lines, 1):
            for match in ABBR.finditer(line):
                short = match.group(2)
                expansion = expansion_for(short, " ".join(match.group(1).split()))
                if expansion and short.lower() != expansion.lower():
                    defined.setdefault(short, (expansion, doc.doc_id, number))
    texts = {doc.doc_id: " ".join(doc.lines) for doc in docs}
    lowered = {doc_id: " ".join(text.lower().split()) for doc_id, text in texts.items()}
    found = []
    for short, (expansion, where, number) in sorted(defined.items()):
        short_re = re.compile(r"(?<![A-Za-z0-9])" + re.escape(short) + r"(?![A-Za-z0-9])")
        full = " ".join(expansion.lower().split())
        short_only = [d for d in texts if short_re.search(texts[d]) and full not in lowered[d]]
        full_only = [d for d in texts if full in lowered[d] and not short_re.search(texts[d])]
        if short_only:
            found.append({"short": short, "full": expansion, "defined": f"{where} l.{number}",
                          "short_only": sorted(short_only), "full_only": sorted(full_only)})
    return found[:LIMITS["names"]]


def name_variants(docs: list[Doc]) -> list[dict]:
    forms: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for doc in docs:
        for line in doc.lines:
            for match in NAME.finditer(line.translate(cq.QUOTES)):
                form = " ".join(match.group(0).split())
                key = re.sub(r"[^a-z0-9]", "", form.lower().replace("&", "and"))
                if len(key) >= 6:
                    forms[key][form.lower()].add(doc.doc_id)
    found = []
    for key, variants in sorted(forms.items()):
        if len(variants) < 2 or not any(" " in v or "-" in v for v in variants):
            continue
        spread = {doc for docs_ in variants.values() for doc in docs_}
        if len(spread) < 2:
            continue
        found.append({"variants": {form: sorted(where) for form, where in sorted(variants.items())}})
    return found[:LIMITS["names"]]


# 7-10. Rounded figures in prose, notes that change how a table is read, counts stated in prose, and
#       summary figures the rest of the document never prints.

ROUNDED = re.compile(r"\b(?:approximately|approx\.|about|around|roughly|nearly|almost|more than|over|less than|under|"
                     r"close to|just over|just under|up to|at least|in excess of)\s+(?:(?:US|A|NZ|C)?\$\d[\d,]*(?:\.\d+)?"
                     r"(?:\s*(?:million|billion|trillion|thousand|bn|mn|m|k)\b)?|\d[\d,]*(?:\.\d+)?\s*(?:%|percent\b|"
                     r"per cent\b|million\b|billion\b|trillion\b))"
                     r"|(?:US|A|NZ|C)?\$\d{1,3}(?:\.\d)?\s+(?:billion|trillion)\b", re.I)
# Table notes and footnotes as financial and statistical documents mark them; a numbered list item or a
# consultation question ("3. Should certain assets be excluded ...") is not one.
NOTE_LINE = re.compile(r"^\s*(?:\(\d{1,2}\)|\[\d{1,2}\]|\d{1,2}/\s|[*†‡§]+\s?|\([a-z]\)\s|notes?\s*\d*\s*[:.]|"
                       r"sources?\s*:)", re.I)
READING = re.compile(r"\b(?:marketing year|begins|beginning|cumulative|year[- ]to[- ]date|excludes|excluding|excluded|"
                     r"includes|including|included|restated|recast|reclassified|pro forma|readily determinable|"
                     r"not comparable|net of|gross of|on an? [a-z-]+ basis|reflects|only)\b", re.I)
COUNTED = re.compile(r"\b(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|twenty|"
                     r"\d{1,3})\s+(?:[a-z-]+\s+)?(?:people|persons|individuals|members|respondents|submitters|submissions|"
                     r"cases|countries|states|firms|companies|organi[sz]ations|entities|projects|recipients|stores|hotels|"
                     r"sites|studies|papers|rulings|findings|recommendations|deaths|injuries|workers|employees|commenters|"
                     r"comments|letters|claims|plaintiffs|defendants|patients|participants|banks|funds|schemes|programs|"
                     r"programmes|agencies|councils|jurisdictions|properties|facilities|plants|mines)\b", re.I)
# A summary in the guide's sense (headline, highlights, key findings, conclusion); a filing's "Overview" is
# only its opening section, and its figures are rarely repeated, so it is left out.
SUMMARY_HEAD = re.compile(r"^\s*(?:#+\s*)?(?:executive summary|summary(?: of [a-z ]+)?|(?:financial |key )?highlights?|"
                          r"key (?:points|findings|messages|takeaways)|conclusions?|abstract|in brief|at a glance)\s*:?\s*$",
                          re.I)
FIGURE = re.compile(r"(?:US|A|NZ|C)?\$\d[\d,]*(?:\.\d+)?(?:\s*(?:million|billion|trillion|bn|m)\b)?"
                    r"|\d[\d,]*(?:\.\d+)?\s*(?:%|percent\b|per cent\b|million\b|billion\b|trillion\b)")
HEADING = re.compile(r"^\s*(?:#+\s*)?[A-Z][A-Za-z ,&'’()/-]{2,60}$")  # a short line without digits or a full stop


def notes(doc: Doc) -> list[dict]:
    hits = []
    for number, line in enumerate(doc.lines, 1):
        if len(line) <= 600 and NOTE_LINE.match(line):
            match = READING.search(line)
            if match:
                hits.append({"doc": doc.doc_id, "line": number,
                             "snippet": doc.snippet(number, match.start(), match.end(), 140)})
        if len(hits) >= LIMITS["per_doc"]:
            break
    return hits


def summary_only(doc: Doc) -> list[dict]:
    """Figures a summary, highlights or conclusion section states that the rest of the document never prints."""
    hits = []
    for number, line in enumerate(doc.lines, 1):
        if not SUMMARY_HEAD.match(line):
            continue
        end = min(len(doc.lines), number + 30)
        end = next((at - 1 for at in range(number + 1, end + 1) if HEADING.match(doc.lines[at - 1])), end)
        region = range(number + 1, end + 1)
        rest = "\n".join(doc.lines[:number - 1] + doc.lines[end:])
        for at in region:
            if not doc.is_prose(at) and not doc.lines[at - 1].lstrip().startswith(("-", "•", "*")):
                continue
            unprinted = []
            for match in FIGURE.finditer(doc.lines[at - 1]):
                core = re.search(r"\d[\d,]*(?:\.\d+)?", match.group(0)).group(0)
                if not re.search(r"(?<![\d.,])" + re.escape(core) + r"(?![\d]|[.,]\d)", rest):
                    unprinted.append(" ".join(match.group(0).split()))
            if unprinted:
                hits.append({"doc": doc.doc_id, "line": at, "figure": ", ".join(unprinted),
                             "snippet": " ".join(doc.lines[at - 1].split())[:220]})
            if len(hits) >= LIMITS["per_doc"]:
                return hits
    return hits


def corpus_sha256(bundle: cq.Bundle) -> str:
    canonical = json.dumps(cq.corpus_identity(bundle), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def mine(bundle_path: Path) -> dict:
    bundle = cq.Bundle(bundle_path.resolve())
    if not bundle.manifest:
        raise ValueError("Extract the bundle first: text/manifest.json is missing.")
    docs = load(bundle)
    found, identical = passages(docs)
    quiet = sorted((p for p in found if not p.template), key=lambda p: (-p.score, p.doc_a, p.doc_b, p.line_a))
    per_pair: dict[tuple[str, str], int] = defaultdict(int)
    kept = []
    for passage in quiet:
        if per_pair[(passage.doc_a, passage.doc_b)] < LIMITS["per_pair"]:
            per_pair[(passage.doc_a, passage.doc_b)] += 1
            kept.append(passage)
        if len(kept) >= LIMITS["passages"]:
            break
    templates: dict[tuple[str, str], int] = defaultdict(int)
    for passage in found:
        if passage.template:
            templates[(passage.doc_a, passage.doc_b)] += 1
    return {
        "bundle": bundle.path.name, "corpus_sha256": corpus_sha256(bundle), "documents": [d.doc_id for d in docs],
        "passages": kept, "quiet_total": len(quiet), "templates": dict(templates), "identical": identical,
        "parallels": parallels(docs), "restated": restatements(docs), "periods": periods(docs), "rows": rows(docs),
        "abbreviations": abbreviations(docs), "names": name_variants(docs),
        "rounded": [hit for doc in docs for hit in prose_hits(doc, ROUNDED, LIMITS["per_doc"])],
        "notes": [hit for doc in docs for hit in notes(doc)],
        "counts": [hit for doc in docs for hit in prose_hits(doc, COUNTED, LIMITS["per_doc"] // 2 + 1)],
        "summary_only": [hit for doc in docs for hit in summary_only(doc)],
    }


def pair_name(a: str, b: str) -> str:
    return f"within {a}" if a == b else f"{a} and {b}"


def quoted(text: str) -> str:
    return text.replace("`", "'")


def markdown(result: dict, today: str | None = None) -> str:
    out = [f"# {result['bundle']} - lever candidates (mechanical)", "",
           f"Generated by `tools/lever_mine.py` v{VERSION} on {today or time.strftime('%Y-%m-%d')} from text/ "
           f"(corpus sha256 {result['corpus_sha256'][:16]}); rerun after any re-extraction. Navigation only: each "
           "line says where two passages, names or figures differ, never that a question works. Read the passages "
           "in full before a candidate becomes a hook (notes/hooks.md); design by the playbook's section 4, which "
           "stacks two or three such levers on the path to one answer. Line numbers are text/Dnn.txt lines.", ""]

    out += ["## 1. Same passage, a few words or figures changed", "",
            "Levers: quiet edit in a re-quoted passage; a figure that quietly changes from one report to the next; "
            "an exception or qualifier present in only one of two parallel rules. Edits are shown as "
            "[first document: words | second document: words].", ""]
    if not result["passages"]:
        out.append("- none found")
    for passage in result["passages"]:
        place = (f"{passage.doc_a} l.{passage.line_a[0]}-{passage.line_a[1]} and "
                 f"{passage.doc_b} l.{passage.line_b[0]}-{passage.line_b[1]}")
        out.append(f"- {place} ({passage.matched} words shared, {len(passage.edits)} "
                   f"edit{'s' if len(passage.edits) != 1 else ''})")
        shown = passage.edits if len(passage.edits) <= QUIET_EDITS else [
            edit for edit in passage.edits if edit.kind == "qualifier" or passage.effective(edit) >= 3][:QUIET_EDITS]
        for edit in shown:
            out.append(f"  - {edit.kind}: ...{quoted(edit.before)} [{passage.doc_a}: {quoted(edit.left) or '-'} | "
                       f"{passage.doc_b}: {quoted(edit.right) or '-'}] {quoted(edit.after)}...")
        if len(shown) < len(passage.edits):
            out.append(f"  - ({len(passage.edits) - len(shown)} other edits in this passage)")
    if result["quiet_total"] > len(result["passages"]):
        out.append(f"- ({result['quiet_total'] - len(result['passages'])} more ranked lower)")
    if result["templates"]:
        out += ["", "Recurring frames (a passage reprinted for another period or with many changes), by pair: "
                + ", ".join(f"{pair_name(a, b)} {n}" for (a, b), n in sorted(result["templates"].items())) + "."]
    if result["identical"]:
        out += ["", "Identical shared passages (20+ words; a repeated fact can make a document unnecessary), by "
                "pair: " + ", ".join(f"{pair_name(a, b)} {n}" for (a, b), n in sorted(result["identical"].items()))
                + "."]

    out += ["", "## 2. One rule or fact in two documents' own words", "",
            "Levers: an exception in one of two parallel rules (aq-02562, Hard); second mention, different words. "
            "Pairs share most content words without being copies; those where an exception or qualifier word "
            "sits in one sentence only come first.", ""]
    for item in result["parallels"]:
        marks = "; ".join(f"only {doc} says {', '.join(repr(m) for m in item[key])}"
                          for doc, key in ((item["doc_a"], "markers_a"), (item["doc_b"], "markers_b")) if item[key])
        out.append(f"- {item['doc_a']} l.{item['line_a']} and {item['doc_b']} l.{item['line_b']} (similarity "
                   f"{item['similarity']})" + (f": {marks}" if marks else ""))
        out.append(f"  - {item['doc_a']}: \"{quoted(item['text_a'])}\"")
        out.append(f"  - {item['doc_b']}: \"{quoted(item['text_b'])}\"")
    if not result["parallels"]:
        out.append("- none found")

    out += ["", "## 3. Restated, recast, revised or redefined", "",
            "Levers: restated figures (most effective); like for like across a definition change; same series, "
            "right edition; first forecast against latest estimate.", ""]
    out += [f"- {h['doc']} l.{h['line']} ({h['kind']}): \"{quoted(h['snippet'])}\"" for h in result["restated"]] \
        or ["- none found"]

    out += ["", "## 4. Periods printed only cumulatively", "",
            "Lever: ask about a period no document reports on its own (a quarter backed out of a longer period). "
            "The guide's Hard bank uses it to select a case as well as to compute.", ""]
    for item in result["periods"]["derived"]:
        out.append(f"- The quarter ending {item['quarter_end']} is never printed as three months: "
                   f"{item['cumulative']} in {', '.join(item['documents'])}"
                   + (f", less {item['less']}." if item["less"] else "."))
    for item in result["periods"]["cash_only"]:
        out.append(f"- {item['doc']} (from l.{item['line']}): cash-flow, buyback or capex lines appear only for "
                   f"{'; '.join(item['spans'])}, never three months.")
    if not result["periods"]["derived"] and not result["periods"]["cash_only"]:
        out.append("- none found")

    out += ["", "## 5. One row label, nearly equal values in two documents", "",
            "Lever: restated or revised figures. Each pair also prints identical values under several other "
            "shared labels, so the two documents likely share a period; an unchanged row would match. Confirm "
            "the columns before relying on it.", ""]
    for item in result["rows"]:
        out.append(f"- \"{item['label']}\": {item['doc_a']} l.{item['line_a']} [{', '.join(item['values_a'])}] vs "
                   f"{item['doc_b']} l.{item['line_b']} [{', '.join(item['values_b'])}] ({item['shared_exact']} "
                   "other shared labels match exactly)")
    if not result["rows"]:
        out.append("- none found")

    out += ["", "## 6. One thing under two names", "",
            "Levers: second mention, different words; short references; entity resolution (a reader must know "
            "the two names are one thing, or that two look-alikes are not).", ""]
    for item in result["abbreviations"]:
        out.append(f"- {item['short']} = {item['full']} (defined {item['defined']}): only \"{item['short']}\" in "
                   f"{', '.join(item['short_only'])}" + (f"; only the full name in {', '.join(item['full_only'])}"
                                                         if item["full_only"] else ""))
    for item in result["names"]:
        out.append("- " + "; ".join(f"\"{form}\" ({', '.join(where)})" for form, where in item["variants"].items()))
    if not result["abbreviations"] and not result["names"]:
        out.append("- none found")

    sections = [
        ("7. Rounded figures in prose", "Levers: ask for a precision the document doesn't print; exact table vs "
         "rounded prose. The rounded figure is the decoy; the exact one must come from table lines.", "rounded"),
        ("8. Notes that change how a table is read", "Lever: a footnote or note that shifts which column is which "
         "period, says a line is cumulative, or narrows what a line covers. The explanation must cite it.", "notes"),
        ("9. Counts stated in prose", "Lever: summary vs detail (a stated count that an enumeration, footnote or "
         "table elsewhere corrects). Compare each with the items it counts.", "counts"),
        ("10. Summary figures the rest of the document never prints", "Levers: summary vs detail; claimed but never "
         "discussed; a rounded headline beside the exact figure (the figures listed appear nowhere else in that "
         "document).", "summary_only"),
    ]
    for title, lever, key in sections:
        out += ["", f"## {title}", "", lever, ""]
        out += [f"- {h['doc']} l.{h['line']}" + (f" ({h['figure']})" if h.get("figure") else "")
                + f": \"{quoted(h['snippet'])}\"" for h in result[key]] or ["- none found"]
    return "\n".join(out) + "\n"


def summary(result: dict, path: Path | None) -> dict:
    return {"bundle": result["bundle"], "file": str(path) if path else None,
            "corpus_sha256": result["corpus_sha256"],
            "counts": {"passages": len(result["passages"]), "passages_ranked_lower": result["quiet_total"] - len(
                result["passages"]), "parallels": len(result["parallels"]), "restated": len(result["restated"]),
                "derived_periods": len(result["periods"]["derived"]),
                "cash_only": len(result["periods"]["cash_only"]), "rows": len(result["rows"]),
                "abbreviations": len(result["abbreviations"]), "names": len(result["names"]),
                "rounded": len(result["rounded"]), "notes": len(result["notes"]), "counts": len(result["counts"]),
                "summary_only": len(result["summary_only"])},
            "claim": "Mechanical comparisons only: where passages, names and figures differ. No question, reading, "
                     "model or difficulty judgement."}


def bundle_dir(path: Path) -> Path:
    bundle = path.resolve()
    if (bundle.parent.name != "tasks" or bundle.name == cq.TEMPLATE
            or not re.fullmatch(r"[A-Za-z0-9_-]+", bundle.name)):
        raise ValueError("Use a named tasks/<slug> bundle, not the template.")
    return bundle


def write(path: Path, today: str | None = None) -> dict:
    bundle = bundle_dir(path)
    notes_dir = bundle / "notes"
    if notes_dir.is_symlink() or (notes_dir.exists() and not notes_dir.resolve().is_relative_to(bundle)):
        raise ValueError("Linked notes directory is not supported.")
    notes_dir.mkdir(exist_ok=True)
    result = mine(bundle)
    target = notes_dir / "mine.md"
    if target.is_symlink():
        raise ValueError("Linked notes/mine.md is not supported.")
    target.write_bytes(markdown(result, today).encode("utf-8"))
    return summary(result, target)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--stdout", action="store_true", help="print the Markdown instead of writing notes/mine.md")
    args = parser.parse_args(argv)
    try:
        if args.stdout:
            print(markdown(mine(bundle_dir(args.bundle))), end="")
        else:
            print(json.dumps(write(args.bundle), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as error:
        print(f"lever_mine.py: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
