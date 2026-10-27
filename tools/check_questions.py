"""Mechanical floor for Docket questions, plus bundle status and the submission sheet.

Usage:
  python tools/check_questions.py tasks/<slug> [--q q01 q02 ...]  check questions; exit 1 on any FAIL
  python tools/check_questions.py tasks/<slug> --handover [--q ...] write notes/handover-qNN.md: every form field
  python tools/check_questions.py tasks/<slug> --json [--q ...] write questions/qNN.json: form input values only
  python tools/check_questions.py tasks/<slug> --export          write dist/<slug>.md from ready questions
  python tools/check_questions.py --status                        every bundle's questions by status
  python tools/check_questions.py --hook                          PostToolUse hook for question files

It checks what a script can: fields, lengths, tags, documents, evidence quotes found verbatim
in text/, the wording traps instruction.md names, and the task form's mechanical quality checks
(captured 2026-10-04, .claude/memory/reference/platform-quality-checks.md): 1-10 answer
components, each a piece of the answer with a tagged quote of 12+ contiguous characters; no
semicolon in the answer; 8-80 words; no answer part in the question. Since 2026-10-07 the form
also needs 1-3 "Targeted failure modes" (each a trap and a cause from fixed lists; since 2026-10-08
one shared "Why these are traps" reason of at most 50 words, not three boxes per mode) and gives
each necessary document a role; '## Targeted failure modes' and the optional '## Necessary
documents' hold them. The form's reasoning number check is emulated by tools/form_numbers.py: a
number a step's cited documents cannot be shown to print FAILs ("Step 1: Doc 2 doesn't mention 107."),
unless the document states it, in words or deep, in an evidence quote (an expected false alarm, WARN).
--handover prints every form field in the form's
order, with the task page's Doc numbers. It cannot tell whether a question has
one answer, is fair, or is hard. Status ready requires an explicit platform pass at the
requested difficulty, bound to the revision and full submission/corpus fingerprint.
Optional local checks remain diagnostics: positive results are not prerequisites, stale
records never demand reruns, and current concrete adverse evidence still blocks readiness.
New questions declare 'difficulty_target: easy|medium|hard'; targetless questions retain
the legacy Hard target. Tier counts show which tests ran, never whether they passed.
A clean run is a floor, not a pass. The question format is tasks/template-task/questions/q00.md.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from collections import Counter
from pathlib import Path

import form_numbers as fn
import platform_checks as pc

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = "template-task"
STATUSES = {"template", "draft", "checked", "ready", "submitted", "accepted", "rejected", "dropped"}
ORIGINS = {"user", "claude", "user+claude", "gpt", "user+gpt", "codex", "user+codex"}
ANSWER_TYPES = {"number", "name", "date", "yes-no", "count", "list", "ordered-list"}
TAGS = {"cross-document join", "temporal alignment", "unit normalization", "conditional filter",
        "entity resolution", "aggregation"}
LEVERS = {"mentions it vs does it", "scatter the pieces", "bury one list item late",
          "same series, right edition", "who belongs where", "exact table vs rounded prose",
          "does the hedge apply", "match, then exclude", "ordered answers",
          "calculate across documents", "state the rounding",
          # The platform guide of 2026-10-15/16 (section 5's lever table and "More traps to add"), saved
          # verbatim in .claude/memory/reference/platform-guide-2026-10-16.md.
          "restated figures", "ask for a precision the document doesn't print",
          "ask about a period no document reports on its own", "like for like across a definition change",
          "summary vs detail", "quiet edit in a re-quoted passage", "second mention, different words",
          "claimed but never discussed", "short references", "look-alike metric",
          "footnotes and prose can change how a table is read"}
# Wording the guide of 2026-10-16 names as giving the trap away ("skip words like 'actually' or 'originally'";
# send-back pitfall 5: "spelling out the trap in the question ('not rounded percentages', 'one of them isn't
# internally consistent')").
HINT_WORDS = re.compile(r"\b(?:actually|originally|really|in fact|truly|true figure|correct(?:ed)? figure|"
                        r"not rounded|unrounded|internally (?:in)?consistent|inconsistent|discrepan\w*|typo|misprint|"
                        r"mistake)\b", re.I)
# Send-back pitfall 1 (the most common): a period or case picked through another fact. Fine when the selector
# is the analysis ("in the quarter its gross margin was lowest"), not when it is an unrelated hop.
SELECTOR = re.compile(r"\b(?:quarter|year|month|half|period|week|day)s?\b(?:\s+[\w'’-]+){0,3}?\s+"
                      r"(?:in which|when|during which)\b", re.I)
# Send-back reason 8: "the most recent release", "the latest report" must point at exactly the gold's document.
LITERAL = re.compile(r"\b(?:latest|most recent|newest|last|previous|prior|earlier|earliest|first|initial|original)\s+"
                     r"(?:published |available |reported |quarterly |annual |earnings |interim )?(?:release|report|"
                     r"edition|filing|estimate|forecast|outlook|update|statement|submission|letter|version|"
                     r"announcement|guidance|projection|circular)s?\b", re.I)
# Send-back pitfall 5: the gold is the bare value only ("no 'about', no 'increase of', no labels in brackets").
GOLD_WORDS = re.compile(r"\b(?:about|approximately|approx|around|roughly|nearly|almost|"
                        r"an? (?:increase|decrease|rise|fall|drop|decline) of|"
                        r"(?:increased|decreased|rose|fell|dropped|declined|up|down) by)\b", re.I)
# The task form's own option lists (value: label), as saved in the task page on 2026-10-07.
FAILURE_TRAPS = {
    "wrong_company_in_bundle": "Look-alike company",
    "wrong_jurisdiction_or_scope": "Wrong jurisdiction or scope",
    "entity_type_mismatch": "Wrong kind of entity",
    "fiscal_calendar_offset": "Fiscal vs calendar period",
    "trailing_window_assembly": "Trailing-period total",
    "historical_data_in_current_report": "Older figure inside a newer report",
    "out_of_scope_period_exclusion": "Out-of-range period",
    "wrong_year_or_edition": "Wrong year or edition",
    "superseded_or_latest_deadline": "Superseded date or version",
    "similar_metric_confusion": "Look-alike measure",
    "subset_vs_total": "Part vs total",
    "unit_or_basis_mismatch": "Unit or basis",
    "cross_document_entity_linking": "Linking across documents",
    "recording_or_format_convention": "Document convention",
    "derived_or_computed_metric": "Figure that must be computed",
}
FAILURE_CAUSES = {
    "wrong_entity_or_scope": "Picks the wrong entity or section",
    "wrong_period_or_anchor": "Uses the wrong period or date",
    "metric_substitution": "Takes the wrong line item",
    "rule_or_premise_misapplication": "Misapplies a rule or premise",
    "computation_or_arithmetic_error": "Calculation slip",
    "set_boundary_membership_error": "Wrong members in a list",
    "output_form_or_presentation_error": "Right content, wrong form",
    "precision_rounding_or_sign_error": "Rounding, scale or sign",
}
# A failure mode's labelled fields, in the form's order. Since 2026-10-08 the form follows them with
# one shared box for all modes, "Why these are traps", which blocks Submit above 50 words; its counter
# matched whitespace-separated words (an old 95-word box read "95 / 50 words").
FAILURE_FIELDS = {"trap": "Trap", "cause": "How a careless solver fails"}
FAILURE_REASON = "Why these are traps"
FAILURE_REASON_WORDS = 50
# Since 2026-10-09 Submit reads the shared reason against each pick's own definition and the chosen cause
# (aq-02208 q02, user screenshot): "Figure that must be computed" is "computing a metric by subtracting one
# period from another (full year minus first half)", and "Part vs total" needs a careless solver who "would
# mistake a headline total or different part" for the asked figure. A pick whose question (period trap) or
# reason (part trap) shows no cue of its definition gets a WARN. Other traps' definitions are not captured yet.
TRAP_DEFINITION_CUES = {
    "Figure that must be computed": (
        "a figure derived by subtracting one period from another (full year minus first half)",
        r"\b(quarters?|half|halves|months?|years?|fiscal|annual|year-to-date|ytd|full-year|nine-month|six-month)\b",
        "question"),
    "Part vs total": (
        "a headline total or a different part taken for the asked figure",
        r"\b(totals?|whole|parts?|subtotals?|subsets?|segments?|overall|combined|aggregate|entire)\b",
        "reason"),
}
# The 2026-10-07 form's three boxes per mode. The floor still reads them so it can flag a file
# that has not been rewritten to the shared reason.
LEGACY_FAILURE_BOXES = {"where": "Where the trap sits", "wrong": "The wrong answer a careless solver gives",
                        "why": "Why the correct answer avoids it"}
DOC_ROLES = ("Answer component", "Exclusion / condition source", "Used to identify")
FORM_TAGS = ("Cross-document join", "Temporal alignment", "Unit normalization", "Conditional filter",
             "Entity resolution", "Aggregation")
FROZEN = {"submitted", "accepted", "rejected"}
OUTCOMES = {"match", "wrong-lever", "ambiguous", "not-answerable", "solver-error"}
DIFFICULTIES = {"easy": 1, "medium": 2, "hard": 3}
TIER_ALIASES = {"low": "easy", "easy": "easy", "medium": "medium", "high": "hard", "hard": "hard"}
NUMBER_WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
COUNT = re.compile(r"(\d+|" + "|".join(NUMBER_WORDS) + r")( [a-z-]+)?")
STOCK = ("delve", "worth noting", "it is important to note", "it's important to note", "in conclusion",
         "in summary", "a testament to", "plays a crucial role", "plays a pivotal role", "in the realm of",
         "navigate the complexities", "tapestry")
WHICH_ITEMS = re.compile(r"^(which|list|name|identify)\b|\bwhich (of|one|two|three|four|five|six)\b|"
                         r"\b(list|name|identify) (every|each|all)\b")
STOP = set("""about above after again against also among and another any are because been before
being below between both but by can could did does doing down during each either from further
had has have having here how into its itself just more most much must not now only other our out
over own same should some such than that the their them then there these they this those through
under until upon very was were what when where which while who whom whose why will with within
would your give given state stated report reported list name total""".split())
QUOTES = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
                        "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
                        "‐": "-", "‑": "-", "–": "-", "—": "-", "−": "-"})


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("­", "").translate(QUOTES).lower()
    text = re.sub(r"=== page \d+ ===", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def dehyphen(text: str) -> str:
    return re.sub(r"(\w)- (\w)", r"\1\2", text)


def depipe(text: str) -> str:
    """Drop Markdown table pipes: a complete capture renders formerly hidden tables as pipe rows,
    while the platform's own text shows the same cells space-separated."""
    return re.sub(r"\s+", " ", text.replace("|", " ")).strip()


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9$%][a-z0-9$%.'/-]*", norm(text))


def content_words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z'-]{3,}", norm(text)) if w not in STOP}


def items(field: str) -> list[str]:
    return [part.strip() for part in re.split(r"[;\n]", field) if part.strip()]


def gold_extra(answer: str, question: str) -> str | None:
    """Words or a bracket in the gold that the question does not ask for (send-back pitfall 5). A bracket the
    question's own format asks for ("Name (level)", "marking those that ...") is fine."""
    found = GOLD_WORDS.search(norm(answer))
    if found:
        return f"'{found.group(0)}'"
    if "(" in answer and not re.search(r"bracket|parenthes|\(|in the form|mark(?:ing|ed)?\b|asterisk|\btag",
                                       norm(question)):
        return "a bracketed note"
    return None


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n")


def long_path(path: Path) -> Path:
    """Windows extended-length form of a path, so files past 260 characters stay readable.

    A prepared snapshot nests the platform's document names under a run folder named by the full
    fingerprint; on aq-04797 (2026-10-14) that came to 265-284 characters with LongPathsEnabled 0,
    and Path.rglob/is_file silently skipped the documents, so prepare refused its own snapshot.
    Elsewhere, and for a path already in that form, the absolute path is returned unchanged.
    """
    text = str(path.absolute())
    if os.name != "nt" or text.startswith("\\\\?\\"):
        return Path(text)
    if text.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + text[2:])
    return Path("\\\\?\\" + text)


def parse(path: Path) -> tuple[dict, dict]:
    """Front matter (flat key: value lines) and ## sections, keys lower-cased; comments dropped."""
    raw = read_text(path)
    meta: dict[str, str] = {}
    match = re.match(r"\A---\n(.*?)\n---\n", raw, re.S)
    if match:
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip().lower()] = value.strip()
        raw = raw[match.end():]
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    sections: dict[str, list[str]] = {}
    current = None
    for line in raw.split("\n"):
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1).strip().lower()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return meta, {key: "\n".join(lines).strip() for key, lines in sections.items()}


class Bundle:
    """A bundle's manifest and normalised document texts, loaded on demand."""

    def __init__(self, path: Path):
        self.path = path
        manifest = path / "text" / "manifest.json"
        self.manifest = json.loads(read_text(manifest)) if manifest.exists() else {}
        self._texts: dict[str, list[str]] = {}
        self._page_texts: dict[str, str] = {}

    def page_text(self, doc_id: str) -> str:
        """A document's text as the task page shows it, case and spacing kept, for the form's number
        check and its character positions: the extraction header and PDF page markers are dropped."""
        if doc_id not in self._page_texts:
            file = self.path / "text" / f"{doc_id}.txt"
            text = read_text(file) if file.exists() else ""
            text = re.sub(r"\A# D\d{2,3} \|[^\n]*\n\n", "", text)
            self._page_texts[doc_id] = re.sub(r"(?m)^=== page \d+ ===\n", "", text)
        return self._page_texts[doc_id]

    def texts(self, doc_id: str) -> list[str]:
        if doc_id not in self._texts:
            found = []
            for name in (f"{doc_id}.txt", f"{doc_id}.layout.txt"):
                file = self.path / "text" / name
                if file.exists():
                    found.append(norm(read_text(file)))
            self._texts[doc_id] = found
        return self._texts[doc_id]

    def live_ids(self) -> list[str]:
        return [doc_id for doc_id, entry in self.manifest.items() if not entry.get("missing")]

    def questions(self) -> list[Path]:
        folder = self.path / "questions"
        return sorted(folder.glob("q*.md")) if folder.is_dir() else []


def verbatim_found(quote: str, haystacks: list[str]) -> bool:
    """True when the whole quote, dots included, occurs contiguously in a document.

    Federal Register timetables print dot leaders ("End of Extended Comment Period...... 04/05/24");
    such a quote is one passage, not passages joined by an ellipsis.
    """
    whole = norm(quote)
    return any(whole in hay or dehyphen(whole) in dehyphen(hay) or depipe(whole) in depipe(hay)
               for hay in haystacks)


def quote_found(quote: str, haystacks: list[str], pipes: bool = True) -> bool:
    """With pipes=False only the literal (or de-hyphenated) passage counts, not the pipe-free form."""
    parts = [norm(p) for p in re.split(r"\s*\[?(?:\.\.\.|…)\]?\s*", quote) if p.strip()]
    for hay in haystacks:
        if all(p in hay for p in parts):
            return True
        flat = dehyphen(hay)
        if all(dehyphen(p) in flat for p in parts):
            return True
        if not pipes:
            continue
        bare = depipe(hay)
        if all(depipe(p) in bare for p in parts):
            return True
    return False


# A table row the document itself writes in Markdown ("|Capital expenditures|(434,416)|(1,337,719)|" under a
# "|---|---|---|" rule) is part of the page's own text. Captures that lay out the page text (docket-capture v4,
# plain .txt) keep those pipes, while the older Markdown captures drew their own spaced "| --- |" rows. The form
# matches the page text, so it rejected every pipe-free quote of such rows (aq-06840 q01 and q02 rev 0, user
# screenshots 2026-10-18: "Quote 2 does not appear word for word in document 5").
NATIVE_PIPE_RULE = re.compile(r"(?m)^\|(?:-{3,}\|)+[ 	]*$")


def native_pipe_rows(page_text: str) -> bool:
    return bool(NATIVE_PIPE_RULE.search(page_text))


def submission_sha256(meta: dict, sec: dict, bundle: Bundle | None = None) -> str:
    """Bind checks to the exact submission and, when provided, the extracted corpus.

    Revision and workflow status are deliberately absent: recording a check or changing
    status does not change the tested submission. Wording, evidence, required documents,
    tags, target, and source-text bytes do. Canonical JSON keeps this portable across paths.
    The form's document roles ('## Necessary documents') count only when written, so a file
    without them keeps its earlier fingerprint. Targeted failure modes are the reviewer's
    reading of the traps, outside what solvers see, and stay out like Lever checks.
    """
    payload: dict = {
        "metadata": {key: meta.get(key, "").strip() for key in
                     ("documents", "tags", "difficulty_target", "asks", "answer_type")},
        "sections": {key: sec.get(key, "").strip() for key in
                     ("question", "answer", "components", "reasoning", "evidence")},
    }
    if sec.get("necessary documents", "").strip():
        payload["sections"]["necessary documents"] = sec["necessary documents"].strip()
    if bundle is not None:
        payload["corpus"] = corpus_identity(bundle)
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def corpus_identity(bundle: Bundle) -> dict:
    """The source bytes a check saw: manifest, intake record, originals and extracted texts."""
    text_dir = bundle.path / "text"
    manifest = text_dir / "manifest.json"
    intake = bundle.path / "notes" / "intake.json"
    docs_dir = bundle.path / "docs"
    return {
        "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest() if manifest.exists() else None,
        "intake_sha256": hashlib.sha256(intake.read_bytes()).hexdigest() if intake.exists() else None,
        "documents": [(path.relative_to(docs_dir).as_posix(), hashlib.sha256(path.read_bytes()).hexdigest())
                      for path in sorted(docs_dir.rglob("*")) if path.is_file()
                      and not (path.name == ".gitkeep" and path.stat().st_size == 0)],
        "texts": [(path.name, hashlib.sha256(path.read_bytes()).hexdigest())
                  for path in sorted(text_dir.glob("*.txt"))],
    }


SCREEN_SECTION = "strong-solver screen"
SCREEN_SOLVES = 3
SCREEN_RECORD = re.compile(r"\bscreen_sha256: ([a-f0-9]{64})\b.*?\bright: (\d+)/(\d+)\b")


def screen_sha256(question: str, bundle: Bundle) -> str:
    """Bind a strong-solver screen to the sentence the solvers saw and the documents they read.

    Only the question's words count (whitespace collapsed), so a sentence carried word for word from
    its sketch into a question file keeps its screen; any other change to the sentence or the corpus
    needs a new one. The gold stays outside: the solvers never see it.
    """
    payload = {"question": " ".join(question.split()), "corpus": corpus_identity(bundle)}
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def screen_records(bundle: Bundle, digest: str) -> list[dict]:
    """Strong-solver screen records bound to digest, from the bundle's sketches and question files."""
    sketches = bundle.path / "notes" / "sketches"
    paths = (sorted(sketches.glob("i*.md")) if sketches.is_dir() else []) + bundle.questions()
    found = []
    for path in paths:
        try:
            _, sec = parse(path)
        except (OSError, UnicodeDecodeError):
            continue
        for line in sec.get(SCREEN_SECTION, "").splitlines():
            match = SCREEN_RECORD.search(line)
            if match and match.group(1) == digest:
                found.append({"source": path.name, "right": int(match.group(2)),
                              "solves": int(match.group(3)), "line": line.strip()})
    return found


def screen_findings(question: str, bundle: Bundle) -> tuple[list[str], list[str]]:
    """Failures and warnings for a live Hard target: with Easy and Medium full the platform's check starts
    at the High model, so every Hard sentence gets three fresh strong solves before a run. On 2026-10-14,
    14 of 14 such runs failed, 13 of them "High 3/3", with no strong solve before any of them. The screen
    ranks and never withholds: an all-right screen warns, and the user decides whether to run it (aq-05049,
    2026-10-14: withholding four 3/3 sketches drew "you even didn't give me any questions")."""
    records = screen_records(bundle, screen_sha256(question, bundle))
    if not records:
        return ["no strong-solver screen on this exact sentence and corpus. The Hard check starts at the High "
                "model: run `docket_agent.py packet`, three fresh blind solves and `record-screen` before a "
                "difficulty run (.claude/memory/reference/hard-playbook.md)"], []
    if any(r["solves"] >= SCREEN_SOLVES and r["right"] == r["solves"] for r in records):
        return [], ["the strong solver was right in every fresh solve of this exact sentence: likely Too easy at "
                    "High. Say so with the hand-over; the user decides whether to run it. Never reword or "
                    "re-screen the sentence to find a miss"]
    if all(r["right"] == 0 for r in records):
        return [], ["every fresh strong solve of this sentence missed: the High check fails when every attempt "
                    "is wrong. Read each miss; a second reading or an unsupported gold must be fixed first"]
    return [], []


def record_fields(line: str) -> tuple[dict[str, str], list[str], bool]:
    """Read pipe-separated record fields without interpreting words in quoted feedback."""
    cells = [cell.strip() for cell in re.sub(r"^\s*[-*]\s+", "", line).split("|")]
    bound_record = any(re.match(r"^tested_sha256:\s*", cell, re.I) for cell in cells)
    fields: dict[str, str] = {}
    duplicate = False
    structural_cells = []
    for index, cell in enumerate(cells):
        structural_cells.append(cell)
        match = re.match(r"^([a-z_][a-z0-9_ -]*):\s*(.*?)\s*$", cell, re.I)
        if match:
            key, value = match.groups()
            key = key.lower()
            duplicate = duplicate or key in fields
            fields[key] = value
            if key in {"feedback", "findings", "readings"} or (key == "answer" and bound_record):
                # The final verbatim field can itself contain the record delimiter. Never
                # let quoted platform text inject typed fields or hide a later rejection.
                fields[key] = " | ".join([value] + cells[index + 1:])
                break
    return fields, structural_cells, duplicate


def observed_tiers(tier_line: str) -> set[str]:
    """A count proves execution only; there is no locally invented pass threshold."""
    reached = set()
    for tier, correct, attempts in re.findall(r"\b(low|easy|medium|high|hard)\s+(\d+)\s*/\s*(\d+)\b",
                                             norm(tier_line)):
        if 0 <= int(correct) <= int(attempts) and int(attempts) > 0:
            reached.add(TIER_ALIASES[tier])
    return reached


def source_gap_details(bundle: Bundle) -> list[dict[str, str]]:
    """Identify known omissions and their scope; absent capture provenance stays unknown.

    Identities include the recorded range/size where available. They are review inputs,
    never a claim that unmarked text is complete or that an omitted passage is irrelevant.
    """
    gaps: dict[str, dict[str, str]] = {}

    def add(identity: str, doc_id: str = "", kind: str = "unknown") -> None:
        gaps[identity] = {"identity": identity, "document": doc_id, "kind": kind}

    source_ids = {str(entry.get("source", "")).replace("\\", "/"): doc_id
                  for doc_id, entry in bundle.manifest.items() if entry.get("source")}
    for doc_id, entry in bundle.manifest.items():
        if entry.get("missing") or entry.get("method") == "unsupported":
            add(f"{doc_id}: missing or unsupported document", doc_id, "unavailable-document")
        elif not (bundle.path / "text" / f"{doc_id}.txt").is_file():
            add(f"{doc_id}: missing extracted text", doc_id, "missing-text")
        source = entry.get("source")
        if not source or not (bundle.path / source).is_file():
            add(f"{doc_id}: missing original source", doc_id, "missing-original")
    intake = bundle.path / "notes" / "intake.json"
    if intake.exists():
        try:
            data = json.loads(read_text(intake))
            if not isinstance(data, dict) or not isinstance(data.get("documents"), list):
                raise ValueError("invalid document provenance")
            for doc in data["documents"]:
                if not isinstance(doc, dict):
                    raise ValueError("invalid document provenance")
                count = doc.get("gap_characters", 0)
                if not isinstance(count, int) or isinstance(count, bool) or count < 0:
                    raise ValueError("invalid capture gap count")
                source = str(doc.get("source", "captured document")).replace("\\", "/")
                doc_id = source_ids.get(source, "")
                if doc.get("incomplete") or count > 0:
                    detail = f"{count:,} omitted characters" if count else "unlocated omitted range"
                    if doc.get("note"):
                        detail += "; " + str(doc["note"]).strip()
                    add(f"{source}: incomplete capture ({detail})", doc_id, "capture-gap")
                if doc.get("matches_capture") is False:
                    add(f"{source}: source differs from captured bytes", doc_id, "capture-mismatch")
        except (OSError, ValueError, KeyError, TypeError):
            add("invalid notes/intake.json provenance")
    for path in sorted((bundle.path / "text").glob("*.txt")):
        for line_number, line in enumerate(read_text(path).splitlines(), 1):
            for match in re.finditer(
                    r"\[(?:…|\.\.\.)\s+([\d,]+) characters not shown on the page\s+(?:…|\.\.\.)\]", line):
                doc_id = path.name.split(".", 1)[0]
                if doc_id not in bundle.manifest:
                    doc_id = ""
                add(f"{path.name}: line {line_number}, column {match.start() + 1}, "
                    f"{match.group(1)} omitted characters",
                    doc_id, "text-gap")
    return [gaps[identity] for identity in sorted(gaps)]


def source_completeness(bundle: Bundle) -> list[str]:
    """Canonical known-gap identities used by snapshots, reports and scoped review."""
    return [gap["identity"] for gap in source_gap_details(bundle)]


def source_gaps_sha256(gaps: list[str]) -> str:
    """Bind a source assessment to the exact set of known omissions."""
    canonical = json.dumps(sorted(set(gaps)), ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def source_assessment_errors(section: str, revision: int, digest: str, gaps: list[str]) -> list[str]:
    """Check a concrete author/source or platform assessment without proving its prose.

    Each known gap needs evidence for all six impacts. No local model role is required;
    passing this schema alone proves neither the claims nor source completeness.
    """
    current = []
    for line in section.splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        fields, _, duplicate = record_fields(line)
        if fields.get("rev", "") == str(revision):
            current.append((fields, duplicate))
    if not current:
        return ["known gaps need this revision's evidence-based '## Source assessment' record"]
    fields, duplicate = current[-1]
    errors = []
    if duplicate:
        errors.append("source assessment must not contain duplicate fields")
    if fields.get("tested_sha256", "").lower() != digest:
        errors.append("latest source assessment does not match this submission and corpus fingerprint")
    if fields.get("source_gaps_sha256", "").lower() != source_gaps_sha256(gaps):
        errors.append("latest source assessment does not match the exact known-gap fingerprint")
    if norm(fields.get("verdict", "")) != "unaffected":
        errors.append("source assessment must explicitly conclude 'verdict: unaffected'")
    if not any(fields.get(key, "").strip() for key in ("assessor", "reviewer", "author")):
        errors.append("source assessment needs an assessor, reviewer or author identity")

    def unique_object(pairs: list[tuple[str, object]]) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate findings key")
            result[key] = value
        return result

    try:
        findings = json.loads(fields.get("findings", ""), object_pairs_hook=unique_object)
    except (TypeError, ValueError):
        errors.append("source assessment findings must be a JSON object with unique known-gap keys")
        return errors
    if not isinstance(findings, dict) or set(findings) != set(gaps):
        errors.append("source assessment findings must enumerate every exact known gap, without extras")
        return errors
    scopes = {"premises", "gold", "exclusions", "uniqueness", "necessity", "shortcut"}
    placeholders = {"none", "unaffected", "irrelevant", "n/a", "not applicable", "no impact", "todo"}
    for gap, explanation in findings.items():
        if not isinstance(explanation, dict) or set(explanation) != scopes:
            errors.append(f"source assessment for {gap} needs all six impact explanations")
            continue
        if any(not isinstance(value, str) or len(value.strip()) < 12
               or norm(value) in placeholders or "todo" in norm(value)
               for value in explanation.values()):
            errors.append(f"source assessment for {gap} needs concrete evidence-based text in each scope")
    return errors


def feedback_contradicts_pass(feedback: str, passed_tier: str) -> bool:
    """Fail closed on contradictions or unfinished checks at the claimed passed tier.

    'Easy passed; Medium too easy' supports an Easy pass. An unscoped rejection or a
    failure at the claimed tier or an earlier ladder tier contradicts that claim.
    """
    low = norm(feedback)
    for clause in re.split(r"[.;|,]|\bbut\b", low):
        tiers = {TIER_ALIASES[tier] for tier in re.findall(r"(?<!too )\b(low|easy|medium|high|hard)\b", clause)}
        if tiers and all(DIFFICULTIES[tier] > DIFFICULTIES.get(passed_tier, 0) for tier in tiers):
            continue
        if re.search(r"\btoo easy\b|\bfailed\b|\brejected\b|\bdid not pass\b|\bdidn't pass\b|\bnot passed\b|\bno pass\b", clause):
            return True
        if re.search(r"\bpending\b|\brunning\b|\bqueued\b|\bin progress\b|\bnot (?:yet )?started\b|"
                     r"\bnot (?:yet )?(?:run|tested|finished|completed)\b|\bawaiting (?:results?|verification|verdict)\b|"
                     r"\bno (?:result|verdict)(?: yet)?\b", clause):
            return True
    return False


def records(section: str, review: bool = False) -> list[dict]:
    """Parse optional local checks or platform results, preserving terminal raw feedback.

    Platform records belong in '## Platform validation'; historical '## Blind solve'
    records remain supported. Review/audit records use review=True. Parsing a record
    asserts neither its authenticity nor that its check is required.
    """
    found = []
    for line in section.splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        fields, cells, duplicate = record_fields(line)
        low_fields = {key: norm(value) for key, value in fields.items()}
        revision = fields.get("rev", "")
        date = cells[0] if cells and re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[0]) else ""
        if date:
            try:
                datetime.date.fromisoformat(date)
            except ValueError:
                date = ""
        record: dict = {"date": date, "rev": int(revision) if re.fullmatch(r"\d+", revision) else None,
                        "tested_sha256": low_fields.get("tested_sha256", ""), "duplicate_fields": duplicate}
        if review:
            if "verdict" not in fields:
                continue
            record.update(kind="review", verdict=low_fields["verdict"],
                          difficulty=low_fields.get("difficulty", ""), findings=fields.get("findings", ""))
        else:
            markers = {norm(cell) for cell in cells if ":" not in cell}
            if markers & {"platform quick test", "platform difficulty check", "platform validation"}:
                record.update(kind="quick-test", result=low_fields.get("result", ""),
                              platform_verdict=low_fields.get("platform_verdict", ""),
                              passed_tier=low_fields.get("passed_tier", ""),
                              reached=sorted(observed_tiers(fields.get("tiers", ""))),
                              feedback=fields.get("feedback", ""))
            elif "closed-book solve" in markers:
                record.update(kind="closed-book", result=low_fields.get("result", ""))
            elif "removal probe" in markers:
                record.update(kind="removal", result=low_fields.get("result", ""),
                              left_out=fields.get("left_out", ""))
            elif "outcome" in fields:
                record.update(kind="blind", outcome=low_fields["outcome"], solver=low_fields.get("solver", ""))
            else:
                continue
        found.append(record)
    return found


def platform_records(sec: dict) -> list[dict]:
    """Merge old/new platform history by ISO date, retaining line order for ties.

    For equal dates the dedicated section follows the legacy section. Undated/invalid
    dates sort last so a dated pass cannot hide a failure of unknown chronology.
    Callers must still select the revision and validate the latest record's fingerprint;
    filtering stale records first could hide a later failure.
    """
    found = [record for section in ("blind solve", "platform validation")
             for record in records(sec.get(section, "")) if record["kind"] == "quick-test"]
    return sorted(found, key=lambda record: record["date"] or "9999-99-99")


def local_issue_resolved(section: str, revision: int, digest: str, issue: str) -> bool:
    """Optional author/source adjudication of a current adverse diagnostic; no model rerun.

    A '## Local resolution' bullet uses rev, tested_sha256, assessor (or author/reviewer),
    issue (the exact diagnostic label), verdict: resolved, and terminal findings describing
    the concrete resolution. The latest record for that issue controls. This validates
    binding and attribution, not the truth of the explanation; keep the original return.
    """
    matching = []
    for line in section.splitlines():
        if re.match(r"^\s*[-*]\s", line):
            fields, _, duplicate = record_fields(line)
            if fields.get("rev") == str(revision) and norm(fields.get("issue", "")) == issue:
                matching.append((fields, duplicate))
    if not matching:
        return False
    fields, duplicate = matching[-1]
    return (not duplicate and fields.get("tested_sha256", "").lower() == digest
            and norm(fields.get("verdict", "")) == "resolved"
            and any(fields.get(key, "").strip() for key in ("assessor", "author", "reviewer"))
            and bool(fields.get("findings", "").strip()))


def answer_items(answer: str, is_list: bool) -> list[str]:
    if is_list:
        return list_answer_items(answer)[0]
    parts = items(re.sub(r"^\s*[-*]\s*", "", answer, flags=re.M))
    return parts


def list_answer_items(answer: str) -> tuple[list[str], bool]:
    """Parse visible list boundaries, independently of evidence components.

    Bullet/numbered lines explicitly delimit items. Inline lists use top-level commas;
    quoted/bracketed names, thousands, month-name dates and common company suffixes stay
    together. Plain line breaks may be wrapping. Bare 'and' can be part of an entity name,
    so it is not a separator and returns uncertainty instead of a made-up item count.
    This is a formatting heuristic, not semantic entity recognition: ambiguous names
    should use quoted items or one bullet per item; the platform judges their meaning.
    """
    lines = [line.strip() for line in answer.splitlines() if line.strip()]
    marked = [re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)(.+)$", line) for line in lines]
    if marked and marked[0]:
        listed: list[str] = []
        for line, match in zip(lines, marked):
            if match:
                listed.append(match.group(1).strip())
            else:
                listed[-1] += " " + line
        return listed, False
    text = " ".join(lines)
    protected: set[int] = set()
    months = (r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
              r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?")
    for pattern in (r"(?<![\d,])\d{1,3}(?:,\d{3})+(?!\d)",
                    rf"\b(?:{months})\.?\s+\d{{1,2}},\s*\d{{4}}\b",
                    rf"\b\d{{1,2}}\s+(?:{months})\.?,\s*\d{{4}}\b",
                    r",\s*(?:Inc|Ltd|LLC|Corp|Co|L\.L\.C)\b\.?",):
        for match in re.finditer(pattern, text, re.I):
            protected.update(range(match.start(), match.end()))
    stack: list[str] = []
    quote = ""
    separators = []
    visible = []
    malformed = False
    for index, char in enumerate(text):
        if quote:
            if char == quote:
                quote = ""
            visible.append(" ")
            continue
        if char in {'"', '\u201c', '\u2018'}:
            quote = {'\u201c': '\u201d', '\u2018': '\u2019'}.get(char, char)
            visible.append(" ")
            continue
        if char in "([{":
            stack.append({"(": ")", "[": "]", "{": "}"}[char])
        elif char in ")]}":
            if not stack or stack.pop() != char:
                malformed = True
        if char in ",;" and not stack and index not in protected:
            separators.append(index)
        visible.append(char if not stack and index not in protected else " ")
    if quote or stack or malformed:
        return [text] if text else [], True
    starts, ends = [0] + [index + 1 for index in separators], separators + [len(text)]
    parts = [re.sub(r"^and\s+", "", text[start:end].strip(), flags=re.I) if start else text[start:end].strip()
             for start, end in zip(starts, ends)]
    # An Oxford-comma ', and' is a list boundary; other conjunctions are unresolved.
    unclear = bool(re.search(r"\band\b", re.sub(r"[,;]\s*and\s+", ", ", "".join(visible), flags=re.I)))
    return [part for part in parts if part], unclear


def components(section: str) -> tuple[dict[str, str], list[str]]:
    """'## Components' lines '- c1: <value>' -> ({'c1': value}, [lines that do not parse])."""
    found: dict[str, str] = {}
    bad = []
    for line in section.splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        match = re.match(r"^\s*[-*]\s*(c\d{1,2})\s*:\s*(.+?)\s*$", line, re.I)
        if match:
            found[match.group(1).lower()] = match.group(2)
        else:
            bad.append(line.strip())
    return found, bad


def form_choice(value: str, choices: dict[str, str]) -> str | None:
    """One of the form's options, given by its label or its value; None when it is neither."""
    key = norm(value).strip(" .")
    return next((label for slug, label in choices.items() if key in {norm(label), slug}), None)


def failure_section(section: str) -> tuple[list[dict[str, str]], str]:
    """'## Targeted failure modes': one '### Failure mode N' block per trap holding 'Trap: ...' and
    'How a careless solver fails: ...' (one line each: the form's dropdowns), then the shared reason,
    written as a 'Why these are traps:' line or a '### Why these are traps' heading, whose text runs on
    until the next heading. Old per-mode boxes, whose text ran on until the next label, are kept under
    their keys so the floor can flag them. Returns the modes and the reason."""
    labels = {**FAILURE_FIELDS, **LEGACY_FAILURE_BOXES}
    label = re.compile(r"^\s*(?:[-*]\s*)?(" + "|".join(re.escape(v) for v in labels.values())
                       + r")\s*:\s*(.*)$", re.I)
    reason_start = re.compile(r"^\s*(?:#{3,}\s*|[-*]\s*)?" + re.escape(FAILURE_REASON)
                              + r"\b[^:\n]*?(?::\s*(.*))?$", re.I)
    blocks: list[dict[str, list[str]]] = []
    reason: list[str] = []
    key, in_reason = None, False
    for line in section.splitlines():
        start = reason_start.match(line)
        if start:
            in_reason, key = True, None
            reason = [(start.group(1) or "").strip()]
        elif re.match(r"^###\s", line):
            in_reason, key = False, None
            blocks.append({"heading": [line.lstrip("#").strip()]})
        elif in_reason:
            reason.append(line.rstrip())
        else:
            match = label.match(line)
            if match and blocks:
                key = next(k for k, v in labels.items() if v.lower() == match.group(1).lower())
                blocks[-1][key] = [match.group(2).strip()]
            elif blocks and key in LEGACY_FAILURE_BOXES:
                blocks[-1][key].append(line.rstrip())
    modes = [{key: "\n".join(lines).strip() for key, lines in block.items()} for block in blocks]
    return modes, "\n".join(reason).strip()


def failure_modes(section: str) -> list[dict[str, str]]:
    """The '### Failure mode N' blocks of '## Targeted failure modes' (see failure_section)."""
    return failure_section(section)[0]


def reason_words(text: str) -> int:
    """Words in the shared reason as the form's counter reads them: whitespace-separated runs."""
    return len(text.split())


def necessary_documents(section: str) -> tuple[list[dict], list[str]]:
    """'## Necessary documents' lines: '- D04: Answer component', '- D03: Exclusion / condition
    source | note: <the form's reviewer note>' or '- D04 or D09: Used to identify' (alternatives
    the form groups with "or...")."""
    groups, bad = [], []
    for line in section.splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        match = re.match(r"^\s*[-*]\s*(D\d{2,3}(?:\s+or\s+D\d{2,3})*)\s*:\s*([^|]+?)\s*"
                         r"(?:\|\s*note\s*:\s*(.+?))?\s*$", line, re.I)
        if not match:
            bad.append(line.strip())
            continue
        role = next((r for r in DOC_ROLES if norm(r) == norm(match.group(2))), None)
        groups.append({"ids": re.findall(r"D\d{2,3}", match.group(1)), "role": role,
                       "role_text": match.group(2).strip(), "note": (match.group(3) or "").strip()})
    return groups, bad


def check(path: Path, bundle: Bundle) -> tuple[dict, dict, list[tuple[str, str, str]]]:
    meta, sec = parse(path)
    found: list[tuple[str, str, str]] = []

    def fail(code: str, message: str) -> None:
        found.append(("FAIL", code, message))

    def warn(code: str, message: str) -> None:
        found.append(("WARN", code, message))

    status = meta.get("status", "").lower()
    target = meta.get("difficulty_target", "hard").lower()
    if status not in STATUSES:
        fail("status", f"status '{status}' is not one of {sorted(STATUSES)}")
    if status in {"template", "dropped"}:
        return meta, sec, found
    if target not in DIFFICULTIES:
        fail("difficulty-target", "difficulty_target must be easy, medium or hard")
    # Explicit field only: a targetless legacy file defaults to hard above and is not live Hard work.
    if meta.get("difficulty_target", "").strip().lower() == "hard" and status in {"draft", "checked"}:
        screen_fails, screen_warns = screen_findings(sec.get("question", ""), bundle)
        for message in screen_fails:
            fail("strong-screen", message)
        for message in screen_warns:
            warn("strong-screen", message)

    for key in ("id", "status", "origin", "asks", "answer_type", "documents", "tags"):
        if not meta.get(key):
            fail("fields", f"front matter needs '{key}'")
    for name in ("question", "answer", "components", "reasoning", "evidence"):
        text = sec.get(name, "")
        if not text or "TODO" in text:
            fail("fields", f"'## {name.capitalize()}' is missing, empty or still has TODO")
    question, answer, reasoning = sec.get("question", ""), sec.get("answer", ""), sec.get("reasoning", "")
    q_norm, a_norm = norm(question), norm(answer)
    origin = meta.get("origin", "").lower()
    if origin not in ORIGINS:
        warn("origin", f"origin should be one of {sorted(ORIGINS)}")
    elif origin != "user":
        warn("origin", "the form asks you to tick; export takes origin: user only")

    # Requirements and the form's quality checks: lengths and asks.
    words = len(question.split())
    if words > 80:
        fail("question-length", f"question has {words} words; the form blocks above 80")
    elif words > 60:
        warn("question-length", f"question has {words} words; the form warns above 60 (as short as it can be "
                                "and stay exact)")
    elif words < 8:
        fail("question-length", f"question has {words} words; the form needs 8 or more")
    kinds = {k.strip().lower() for k in re.split(r"[;,]", meta.get("answer_type", "")) if k.strip()}
    if kinds - ANSWER_TYPES:
        fail("fields", f"answer_type {sorted(kinds - ANSWER_TYPES)} not in {sorted(ANSWER_TYPES)}")
    is_list = bool(kinds & {"list", "ordered-list"})
    comps, unparsed = components(sec.get("components", ""))
    parts = list(comps.values()) or answer_items(answer, is_list)
    list_parts, unclear_list = list_answer_items(answer) if is_list else ([], False)
    if ";" in answer:
        fail("short-answer", "the answer has a semicolon, which the form refuses; separate parts with commas or 'and'")
    if len(answer) > 250:
        fail("short-answer", f"answer is {len(answer)} characters; the limit is 250")
    if is_list:
        if unclear_list:
            warn("list-items", "cannot determine every list boundary from the answer; use comma-separated quoted items or "
                               "one bullet per item, then review the item count on the platform")
        if not unclear_list and len(list_parts) > 12:
            fail("short-answer", f"answer lists {len(list_parts)} items; the limit is 12")
        for part in list_parts if not unclear_list else []:
            if len(part.split()) > 10:
                warn("answer-length", f"list item '{part[:40]}' is over 10 words")
    elif len(answer.split()) > 10:
        fail("short-answer", f"answer has {len(answer.split())} words; a short answer is up to 10 words")
    if re.search(r"\b(because|due to|which means|so that)\b", a_norm) or (
            answer.rstrip().endswith(".") and len(answer.split()) > 4):
        warn("short-answer", "the answer reads like a sentence or an explanation; give the value")
    extra = gold_extra(answer, question)
    if extra:
        warn("gold-extra", f"the gold carries {extra} that the question does not ask for; give the bare value in the "
                           "asked format (send-back pitfall 5, guide of 2026-10-15; ledger rows 24 and 26: quick tests "
                           "read as survivals with an explanatory parenthesis and failed with the bare answer)")
    if re.fullmatch(r"[-+]?[\d.,]+", answer.strip()):
        warn("units", "the answer is a bare number; give its units (form: 'short and checkable, with units')")
    if kinds == {"yes-no"}:
        warn("guessable", "a bare yes/no can be guessed half the time, so it cannot reach maximum difficulty; "
                          "ask for a count, list, name or value, or a yes/no with a named item (gate Q13, D7)")
    asks = meta.get("asks", "")
    if asks not in {"1", "2"}:
        fail("asks", "asks must be 1, or 2 parallel asks at most")
    marks = question.count("?")
    if marks >= 3:
        fail("asks", f"{marks} question marks; one ask is best, two parallel asks at most")
    elif marks == 2 and asks == "1":
        warn("asks", "two question marks but asks: 1")

    # The form's component checks: 1-10 distinct pieces of the answer that cover every number and
    # every ask, with a separator between parts.
    normed = {cid: norm(value) for cid, value in comps.items()}
    if unparsed:
        fail("components", f"cannot parse '{unparsed[0][:60]}'; use - c1: <a value or name from the answer>")
    if not 1 <= len(comps) <= 10:
        fail("components", f"{len(comps)} components; the form needs 1-10, each a piece of the answer")
    if len(set(normed.values())) < len(normed):
        fail("components", "two components are the same; components must be distinct")
    for cid, value in normed.items():
        if value not in a_norm:
            fail("components", f"{cid} '{comps[cid]}' is not a piece of the answer (a value or a name from it)")
    if comps:
        # Whole numbers, as the form compares them: "8" in "8 CFR 1208.13" is not covered by "1208.13"
        # (form, aq-02750 q06, 2026-10-11: "Your answer includes 8, but no component contains it").
        covered = {n for value in normed.values() for n in re.findall(r"\d+(?:[.,]\d+)*", value)}
        for number in re.findall(r"\d+(?:[.,]\d+)*", a_norm):
            if number not in covered:
                fail("components", f"the number {number} in the answer is in no component")
        if asks in {"1", "2"} and len(comps) < int(asks):
            fail("components", f"{len(comps)} component for {asks} asks; the answer must cover every ask")
    spans = sorted((a_norm.find(v), a_norm.find(v) + len(v), cid) for cid, v in normed.items() if v and v in a_norm)
    for (_, end, first), (start, _, second) in zip(spans, spans[1:]):
        if start >= end and not a_norm[end:start].strip():
            fail("components", f"nothing separates {first} from {second} in the answer; a grader must tell "
                               "the parts apart")

    # Rule 2: at least two necessary documents that exist. The form gives each ticked document a
    # role and groups documents that carry the same fact as alternatives ("Doc 4 or Doc 9").
    documents = re.findall(r"\bD\d{2,3}\b", meta.get("documents", ""))
    groups = [[doc_id] for doc_id in dict.fromkeys(documents)]
    roles_text = sec.get("necessary documents", "")
    if roles_text:
        parsed, bad = necessary_documents(roles_text)
        for line in bad:
            fail("documents", f"cannot parse '{line[:60]}'; use - D04: Answer component (or Used to identify, or "
                              "Exclusion / condition source | note: ...), alternatives joined by 'or'")
        if sorted(d for group in parsed for d in group["ids"]) != sorted(set(documents)):
            fail("documents", "'## Necessary documents' must list each front-matter document exactly once")
        for group in parsed:
            name = " or ".join(group["ids"])
            if group["role"] is None:
                fail("documents", f"{name}: '{group['role_text']}' is not one of the form's roles "
                                  f"({', '.join(DOC_ROLES)})")
            elif group["role"] == "Exclusion / condition source":
                note = group["note"]
                if len(re.findall(r"[A-Za-z0-9]", note)) < 20 or len(set(re.findall(r"[a-z]+", note.lower()))) < 3:
                    warn("documents", f"{name}: an exclusion source needs the form's reviewer note (20+ letters or "
                                      "digits, 3+ different words) saying what it rules out")
                warn("documents", f"{name}: exclusion role; a platform reviewer accepted it only for a document "
                                  "ruling out an item that exists without it, not for its own decoy (aq-01333 q01)")
        if parsed and not bad:
            groups = [group["ids"] for group in parsed]
    if len(groups) < 2:
        fail("documents", "list at least two necessary documents (rule 2)")
    elif len(set(documents)) > 4:
        warn("documents", f"{len(set(documents))} documents listed; the form's reasoning usually covers 2-4, "
                          "only those the answer relies on")
    if not bundle.manifest:
        fail("documents", "text/manifest.json is missing; run tools/extract_text.py on the bundle")
    for doc_id in documents:
        entry = bundle.manifest.get(doc_id)
        if bundle.manifest and (entry is None or entry.get("missing")):
            fail("documents", f"{doc_id} is not a live document in text/manifest.json")

    # Reasoning tags and levers.
    tags = [t.lower() for t in items(meta.get("tags", ""))]
    unknown = [t for t in tags if t not in TAGS]
    if unknown:
        fail("tags", f"unknown tags {unknown}; use the guide's six, separated by semicolons")
    if len(set(tags) - set(unknown)) < 2:
        fail("tags", "at least two reasoning tags")
    declared = items(meta.get("levers", ""))
    for lever in declared:
        if norm(re.sub(r"\s*\(most effective\)|\?", "", lever)).strip() not in LEVERS:
            warn("levers", f"'{lever}' is not one of the guide's levers (separate them with semicolons)")
    if meta.get("difficulty_target", "").strip().lower() == "hard" and status in {"draft", "checked"} and len(
            declared) < 2:
        warn("levers", f"{len(declared)} lever(s) declared for a Hard target; the guide (2026-10-16): 'One lever "
                       "usually lands Easy; two together land Medium or Hard'. Stack two or three on the path to the "
                       "answer (playbook section 4) and list them in 'levers:'")

    # Rule 9a and the form's evidence checks: every quote is 12+ characters of one passage, found
    # verbatim in the document it cites, and attached to a component; every component has a quote
    # (one bare count may go uncited).
    cited, covered = set(), set()
    for line in sec.get("evidence", "").splitlines():
        if not re.match(r"^\s*[-*]\s", line) or "TODO" in line:
            continue
        match = re.match(r'^\s*[-*]\s*(D\d{2,3})\b(.*?):\s*["“](.+)["”]\s*$', line)
        if not match:
            fail("evidence", f"cannot parse '{line.strip()[:60]}'; use - Dnn (where) [c1]: \"exact quote\"")
            continue
        doc_id, where, quote = match.groups()
        cited.add(doc_id)
        tag = re.search(r"\[\s*(c\d{1,2}(?:\s*,\s*c\d{1,2})*)\s*\]", where, re.I)
        if not tag:
            fail("components", f"the {doc_id} quote is attached to no component; add [c1] before the colon")
        else:
            for cid in re.findall(r"c\d{1,2}", tag.group(1).lower()):
                if cid not in comps:
                    fail("components", f"the {doc_id} quote names {cid}, which '## Components' does not list")
                covered.add(cid)
        haystacks = bundle.texts(doc_id)
        if re.search(r"\.\.\.|…", quote) and not verbatim_found(quote, haystacks):
            fail("evidence", f"the {doc_id} quote joins passages with an ellipsis; attach each passage as its own quote")
        elif len(quote.strip()) < 12:
            fail("evidence", f"the {doc_id} quote \"{quote}\" is under 12 characters; the form needs 12 or more")
        elif not haystacks:
            warn("evidence", f"{doc_id} has no extracted text; its quote cannot be verified")
        elif not quote_found(quote, haystacks):
            fail("evidence", f"{doc_id} quote not found verbatim: \"{quote[:70]}\"")
        elif native_pipe_rows(bundle.page_text(doc_id)) and not quote_found(quote, haystacks, pipes=False):
            # A submitted or accepted question is frozen (never edited), so its old quotes are reported, not failed.
            (warn if status in FROZEN else fail)(
                             "evidence", f"{doc_id} quote matches only with the table pipes removed, but this document's own text "
                             f"keeps them, and the form rejects such a quote (aq-06840, 2026-10-18): copy the row as "
                             f"the document prints it, pipes included: \"{quote[:70]}\"")
    uncited = [cid for cid in comps if cid not in covered]
    if len(uncited) > 1 or (uncited and not COUNT.fullmatch(normed[uncited[0]])):
        fail("components", f"no evidence quote for {', '.join(uncited)}; every component needs one "
                           "(one bare count may go uncited)")
    for group in groups:
        if not any(doc_id in cited for doc_id in group):
            fail("evidence", f"{' or '.join(group)} is listed as necessary but has no evidence quote")
        elif not all(doc_id in cited for doc_id in group):
            warn("evidence", f"alternatives {' or '.join(group)}: quote each one; the form's 'Necessary documents "
                             "cited' check may want a quote from every ticked document")
    for doc_id in sorted(cited - set(documents)):
        warn("evidence", f"{doc_id} is quoted but not listed as necessary; if the answer needs it, list it")

    # The form's reasoning number check (tools/form_numbers.py): each number in a step must be printed,
    # in digits, in a document the step cites, or be the step's exact "=" result, or (in a step citing
    # two or more documents) repeat an earlier step's string. The form shows each miss in orange under
    # the reasoning box ("Step 1: Doc 2 doesn't mention 107."). A miss a rewording could fix is a FAIL
    # and blocks a clean hand-over; a figure the cited document states in words or deep, inside an
    # evidence quote, is an expected false alarm and a WARN (user, 2026-10-09). A ready question was
    # measured with its reasoning as it stands, and an edit voids that pass, so there it is reported only.
    if status not in FROZEN and reasoning and "TODO" not in reasoning:
        pages = platform_numbers(bundle)
        if not pages:
            warn("form-numbers", "notes/intake.json gives no task-page Doc numbers, so the form's reasoning "
                                 "number check could not run; check every step's numbers by hand")
        else:
            page_texts = {pages[doc_id]: bundle.page_text(doc_id) for doc_id in bundle.live_ids() if doc_id in pages}
            page_quotes: dict[int, list[str]] = {}
            for doc_id, _, _, quote in evidence_rows(sec.get("evidence", "")):
                if doc_id in pages:
                    page_quotes.setdefault(pages[doc_id], []).append(quote)
            for flag in fn.check(reasoning, page_texts, page_quotes):
                if flag.level == "FAIL" and status != "ready":
                    fail("form-numbers", f"{flag.form} {flag.why}")
                else:
                    warn("form-numbers", f"{flag.form} {flag.why}" + (
                        " (ready: the platform measured this reasoning; an edit needs a new difficulty result)"
                        if flag.level == "FAIL" else ""))
            # A step that names a document relies on it. Platform reviewers returned aq-01333 q01 and aq-02749
            # q02 because the explanation leaned on a document that was not marked necessary: the Document check
            # (answer unchanged without it) is a narrower test than the reviewer's (every document the count or
            # condition depends on is ticked and quoted). The exclusion role with its note covers that case.
            ticked = {pages[doc_id] for doc_id in documents if doc_id in pages}
            named = {int(number)
                     for found in re.finditer(r"\bDocs?\s+(\d+(?:(?:\s*,\s*|\s+and\s+|\s+or\s+)\d+)*)", reasoning)
                     for number in re.findall(r"\d+", found.group(1))}
            for number in sorted(named - ticked):
                warn("documents", f"the reasoning names Doc {number}, which is not ticked as necessary: tick it "
                                  "(\"Exclusion / condition source\" with the note and a quote when it only rules "
                                  "something out) or take the statement out; reviewers returned aq-01333 q01 and "
                                  "aq-02749 q02 for an explanation that relied on an unmarked document")

    # The form's Targeted failure modes: 1-3 traps from its list, each once, each with how a careless
    # solver fails (2026-10-07), then one shared "Why these are traps" reason of at most 50 words
    # (2026-10-08, replacing three boxes per mode). Submit stays blocked without them or above 50 words.
    if status not in FROZEN:
        modes_text = sec.get("targeted failure modes", "")
        if not modes_text or "TODO" in modes_text:
            (fail if status == "ready" else warn)(
                "failure-modes", "no complete '## Targeted failure modes'; the form blocks Submit until 1-3 traps "
                                 "and one shared reason are filled in, each trap proved in Lever checks with the "
                                 "wrong answer it gives")
        else:
            modes, reason = failure_section(modes_text)
            if not 1 <= len(modes) <= 3:
                fail("failure-modes", f"{len(modes)} failure modes; the form takes 1 to 3, one "
                                      "'### Failure mode N' block each")
            seen = set()
            for number, mode in enumerate(modes, 1):
                trap = form_choice(mode.get("trap", ""), FAILURE_TRAPS)
                if trap is None:
                    fail("failure-modes", f"failure mode {number}: trap '{mode.get('trap', '')}' is not one of the "
                                          "form's: " + ", ".join(FAILURE_TRAPS.values()))
                elif trap in seen:
                    fail("failure-modes", f"failure mode {number} repeats '{trap}'; the form takes each trap once")
                else:
                    seen.add(trap)
                    cue = TRAP_DEFINITION_CUES.get(trap)
                    if cue and not re.search(cue[1], q_norm if cue[2] == "question" else reason, re.I):
                        warn("failure-modes", f"failure mode {number}: Submit checks '{trap}' against its definition, "
                                              f"{cue[0]}; the {cue[2]} shows no such cue, so pick the trap whose "
                                              "definition fits the wrong route (aq-02208 q02 was blocked)")
                if form_choice(mode.get("cause", ""), FAILURE_CAUSES) is None:
                    fail("failure-modes", f"failure mode {number}: '{FAILURE_FIELDS['cause']}' must be one of: "
                                          + ", ".join(FAILURE_CAUSES.values()))
                old = [f"'{LEGACY_FAILURE_BOXES[key]}'" for key in LEGACY_FAILURE_BOXES if key in mode]
                if old:
                    fail("failure-modes", f"failure mode {number} still has the old per-mode box(es) {', '.join(old)}; "
                                          f"the form now has one shared '{FAILURE_REASON}' box for all modes, at most "
                                          f"{FAILURE_REASON_WORDS} words")
            words = reason_words(reason)
            if not reason:
                fail("failure-modes", f"no '{FAILURE_REASON}:' reason; the form needs one short reason for all picks "
                                      f"(where the trap sits, the wrong answer, why the gold avoids it), at most "
                                      f"{FAILURE_REASON_WORDS} words")
            elif words > FAILURE_REASON_WORDS:
                fail("failure-modes", f"'{FAILURE_REASON}' has {words} words; the form blocks Submit above "
                                      f"{FAILURE_REASON_WORDS}")
            elif not re.search(r"\bDocs? \d+", reason):
                warn("failure-modes", f"'{FAILURE_REASON}' names no Doc N; the form asks where each trap sits "
                                      "(the document and passage)")

    # Rule 7: self-contained wording.
    if re.search(r"\.(pdf|html?|docx?|txt|xlsx?|csv|xml)\b", q_norm):
        fail("self-contained", "the question names a file; name what it needs instead (rule 7)")
    if re.search(r"\b(page|pages|p\.|pp\.)\s*\d+", q_norm):
        fail("self-contained", "the question points at a page number (rule 7)")
    if re.search(r"\bD\d{2,3}\b", question) or re.search(r"\b(document|doc|file|attachment)\s*#?\s*\d+\b", q_norm):
        fail("self-contained", "the question points at a document by id or number (rule 7)")
    for entry in bundle.manifest.values():
        stem = norm(Path(entry["source"]).stem)
        if len(stem) >= 6 and stem in q_norm:
            fail("self-contained", f"the question contains the file name '{stem}' (rule 7)")

    # Rule 5 and common mistakes: essays, judgment calls, unsigned superlatives.
    if re.match(r"(explain|describe|summari[sz]e|discuss|why)\b", q_norm) or re.search(
            r"explain why|describe how|in your own words", q_norm):
        fail("essay", "asks for an explanation; answers must be short and checkable (rule 5)")
    elif re.search(r"\b(explain|summari[sz]e|discuss|elaborate|justify)\b|\bwhy\b", q_norm):
        warn("essay", "explanation wording; make sure the answer is still a short checkable item")
    judgement = re.findall(r"most relevant|most important|most significant|most strongly|most closely"
                           r"|most aligned|most appropriate|most likely|\bbest\b|\bworst\b", q_norm)
    if judgement:
        warn("judgment", f"judgment wording {judgement}; two careful readers may disagree")
    if re.search(r"\b(largest|biggest|greatest|smallest|most|least)\s+(\w+\s+)?(change|difference|move|swing"
                 r"|shift|variance|deviation)\b", q_norm) and not re.search(
            r"absolute|increase|decrease|rise|gain|drop|decline|fall|positive|negative|upward|downward", q_norm):
        warn("superlative", "unsigned superlative; say 'in absolute size' or 'largest increase'")

    # Rule 9: pinned periods, units and precision.
    if re.search(r"\b(margin|rate|share|yield|ratio|proportion)s?\b", q_norm) and re.search(
            r"how much|by how|difference|change|higher|lower|increase|decrease|grow|grew|rise|rose|fall|fell"
            r"|gap", q_norm) and not re.search(
            r"percentage point|basis point|relative|percent change|percentage change|absolute|in percent", q_norm):
        warn("points-or-percent", "comparing a rate: say 'percentage points' or 'percent (relative)'")
    if re.search(r"\b(q[1-4]|quarter|quarters|fy\s?'?\d{2,4}|h[12])\b", q_norm) and not re.search(
            r"\b(fiscal|calendar|ended|ending)\b", q_norm):
        warn("period", "names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; "
                       "confirm the period is pinned (rule 9b)")
    if re.search(r"\d\.\d|%|percent", a_norm) and not re.search(
            r"decimal|nearest|round|significant figure|whole number|whole percent|tenth|hundredth", q_norm):
        warn("precision", "the answer is a rate or decimal; state the precision in the question")

    # Rule 8 and the form's "answer not given away": neither the answer nor any part of it appears
    # in the question.
    if len(a_norm) >= 2 and a_norm not in {"yes", "no"} and a_norm in q_norm:
        fail("giveaway", "the question contains the answer (rule 8)")
    else:
        for part in parts:
            p = norm(part)
            if len(p) >= 2 and p not in {"yes", "no", "none"} and re.search(
                    rf"(?<![a-z0-9]){re.escape(p)}(?![a-z0-9])", q_norm):
                fail("giveaway", f"answer part '{part}' appears in the question; the form blocks any part (rule 8)")

    # Section 4: which-items questions need a named decoy.
    which_items = bool(WHICH_ITEMS.search(q_norm))
    if which_items and "decoy" not in reasoning.lower():
        fail("decoy", "a which-items question needs a decoy named in the reasoning ('Decoy: ...')")

    # The form's advisory format checks: the order of a list, what to answer when nothing
    # qualifies, how many items a long list has, and no "at least N" over a longer answer.
    if is_list and not re.search(r"\border\b|rank|first|earliest|latest|chronolog|sequence|ascending|descending"
                                 r"|lowest|highest|alphabetical", q_norm):
        warn("format", "a list answer: say the order, e.g. 'alphabetically' or 'in date order' (form: answer "
                       "format stated; 'in any order' clears this check but draws the rule-10 advisory)")
    elif is_list and not re.search(r"\border\b|rank|chronolog|sequence|ascending|descending|alphabetical", q_norm):
        # aq-03170 q01 rev 1: "Earliest second letter first." cleared this floor and the form still warned
        # ("the question does not say what order to give them in"); "List them alphabetically." cleared both.
        warn("format", "a list answer whose only order word is 'first', 'earliest', 'latest', 'lowest' or 'highest': "
                       "the form did not read \"Earliest second letter first.\" as an order (aq-03170 q01); use "
                       "the check's own words ('alphabetically', 'in date order')")
    # A clause telling the solver what to count is a cue, even when it reads like a fairness rule. Measured:
    # "Counting co-signed letters" Between levels (aq-03570); "including letters only others mention" Medium
    # where the same question naming only the evidence ("Judging by all these letters together") was Hard
    # (aq-03170 q01); "including any whose attempt only another submitter reports" quick-test too easy
    # (aq-03423). Name the set or the evidence by its structure and leave the counting to the solver.
    if re.search(r"(?:^|[,;:(?]\s*)(?:counting|including|whether or not)\b", q_norm):
        warn("cue", "a clause beginning 'counting', 'including' or 'whether or not' tells the solver what to "
                    "look for; name the set or the evidence by its structure instead (aq-03170 q01: the clause "
                    "measured Medium, the structural wording Hard)")
    # A completeness word does the same job as a clause. Measured on one list with a member outside a
    # complete-looking table (aq-03169 q02): "say anywhere in its response" Between levels (Medium 4/5); the
    # scope dropped altogether, "Answer not supported" (the high model stayed in the table, 0 of 3); the scope
    # named with no search word, "does Grant Thornton's response say", Hard. Same ladder on aq-02933
    # ("Wherever": Between levels; "appears in CMS's hospice notice": Medium).
    if re.search(r"\b(?:anywhere|wherever)\b", q_norm):
        warn("cue", "'anywhere' or 'wherever' tells the solver to keep searching (aq-03169 q02, aq-02933 q04: "
                    "Between levels); name the document or section set the members are drawn from, and do not "
                    "drop the scope either (dropped: the high model answered from the table only)")
    # The platform guide of 2026-10-15/16: no word that points at the trap, no contrived selector, and words like
    # "the latest release" that point at exactly the gold's document (sections 5 and 7).
    hint = HINT_WORDS.search(q_norm)
    if hint:
        warn("hint", f"'{hint.group(0)}' points at the trap; the guide says to skip words like 'actually' or "
                     "'originally' and not to spell the trap out (send-back pitfall 5)")
    if SELECTOR.search(q_norm):
        warn("selector", "the period or case is picked through another fact: keep it only if the selector is the "
                         "analysis (the company's own best or worst quarter); otherwise name the period (send-back "
                         "pitfall 1, the most common)")
    literal = LITERAL.search(q_norm)
    if literal:
        warn("literal", f"'{literal.group(0)}': read only the words and confirm they point at exactly the document "
                        "and period the gold uses (send-back reason 8)")
    # A list gold written as labelled sentences ("Less concentration: a, b, c. Lower audit quality: d, e")
    # failed the form's blocking "Short answer" check: it splits on commas, so a label and a sentence break
    # fold into the neighbouring items (aq-03169 q02 rev 1). One comma list, a short tag in brackets per item.
    if is_list and (re.search(r"[A-Za-z]:\s", answer) or re.search(r"[a-z]{3}\.\s+[A-Z]", answer)):
        warn("short-answer", "the list answer carries a colon label or a sentence break; the form's blocking "
                             "'Short answer' check failed that shape (aq-03169 q02 rev 1): write one comma list "
                             "and tag items in brackets when two asks share it")
    # The form reads an ordinal before a document part as a pointer to the answer: "second letter" drew
    # "points to where the answer is ... name the thing you mean instead" (aq-03170 q01 rev 1).
    pointer = re.search(r"\b(first|second|third|fourth|fifth|last)\s+(letter|paragraph|table|section|footnote|"
                        r"sentence|page|row|column|mention)\b", q_norm)
    if pointer:
        warn("pointer", f"'{pointer.group(0)}' reads as a pointer to where the answer sits (the form flagged "
                        "'second letter' on aq-03170 q01); name the thing itself")
    if (which_items or is_list) and not re.search(r"\bif any\b|\bnone\b|\bif no\b|\bzero\b", q_norm):
        warn("format", "say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' "
                       "(form: answer format stated)")
    if is_list and not unclear_list and len(list_parts) > 3:
        names = "|".join([str(len(list_parts))] + [w for w, n in NUMBER_WORDS.items() if n == len(list_parts)])
        if not re.search(rf"\b({names})\b", q_norm):
            warn("list-contract", f"the answer lists {len(list_parts)} items; say how many to expect, or ask for one "
                                  "value (form: list contract)")
    least = re.search(r"\bat least (\d+|" + "|".join(NUMBER_WORDS) + r")\b", q_norm)
    if least:
        wanted = int(least.group(1)) if least.group(1).isdigit() else NUMBER_WORDS[least.group(1)]
        item_count = len(list_parts) if is_list else len(parts)
        if not unclear_list and item_count > wanted:
            warn("partial", f"'at least {least.group(1)}' with {item_count} answer items marks a correct partial "
                            "answer wrong (form: partial answers)")
    if re.search(r"\b(this|the) (bundle|document set|set of documents|collection of documents)\b"
                 r"|\bhow many (of the )?documents\b|\bwhich (of the )?documents?\b"
                 r"|\b(both|all|each|exactly \w+) (of the )?documents\b|\bcited (in|by) both\b", q_norm):
        warn("world", "the question is about the documents, not what they describe (rule 10)")
    # aq-03736 q02 (2026-10-13): the form's "Asks about the world, not the set" advisory flagged the tail
    # "List the items in any order." as "an answer-protocol tail". "List them alphabetically." (aq-03170 q01)
    # cleared "Answer format stated" and is not known to draw this line.
    if re.search(r"\bin any order\b", q_norm):
        warn("world", "'in any order' drew the form's rule-10 advisory as an answer-protocol tail (aq-03736 q02); "
                      "give a natural order instead ('alphabetically', 'in date order'), or ask for one value")
    for name, text in (("question", question), ("reasoning", reasoning)):
        if re.search(r"[—–]|(?<!-)--(?!-)", text):
            warn("style", f"the {name} has an em or en dash; the form flags them (writing style)")
        stock = [phrase for phrase in STOCK if phrase in norm(text)]
        if stock:
            warn("style", f"stock phrasing in the {name}: {stock} (writing style)")

    # Requirements: no rulebooks.
    if re.search(r"universe:|step 1|step one|exactly the phrase|the following phrases", q_norm) or len(
            re.findall(r"\b(excluding|except|other than|not counting|apart from)\b", q_norm)) >= 3:
        warn("rulebook", "setup, procedure or string of exclusions; ask something simpler")

    # Rule 3: not a keyword search.
    q_tokens = tokens(question)
    grams = {" ".join(q_tokens[i:i + 8]) for i in range(len(q_tokens) - 7)}
    q_words = content_words(question)
    answer_parts = [norm(p) for p in parts if len(norm(p)) >= 3] or ([a_norm] if len(a_norm) >= 3 else [])
    for doc_id in bundle.live_ids():
        for hay in bundle.texts(doc_id)[:1]:
            flat = " " + " ".join(tokens(hay)) + " "
            copied = next((g for g in grams if f" {g} " in flat), None)
            if copied:
                warn("copied-phrasing", f"8 words copied from {doc_id}: '{copied}'; paraphrase (rule 3)")
            if not answer_parts or len(q_words) < 4:
                continue
            first = answer_parts[0]
            for hit in re.finditer(re.escape(first), hay):
                window = hay[max(0, hit.start() - 600): hit.end() + 600]
                share = len(q_words & content_words(window)) / len(q_words)
                if all(p in window for p in answer_parts) and (share >= 0.6 or len(answer_parts) >= 2):
                    snippet = hay[max(0, hit.start() - 70): hit.end() + 70].strip()
                    warn("single-passage", f"one passage of {doc_id} holds the answer"
                         + (" with most of the question's words" if share >= 0.6 else "")
                         + f": '...{snippet}...' (rules 2-3)")
                    break

    # The form's sibling check: no other live question on this bundle asks for the same fact, gives
    # this answer away, or shares this wording.
    runs = {" ".join(q_tokens[i:i + 6]) for i in range(len(q_tokens) - 5)}
    for other in bundle.questions():
        if other.resolve() == path.resolve():
            continue
        o_meta, o_sec = parse(other)
        o_question, o_answer = o_sec.get("question", ""), norm(o_sec.get("answer", ""))
        if o_meta.get("status", "").lower() in {"template", "dropped"} or not o_question or "TODO" in o_question:
            continue
        o_tokens = tokens(o_question)
        shared = runs & {" ".join(o_tokens[i:i + 6]) for i in range(len(o_tokens) - 5)}
        if len(o_answer) >= 4 and o_answer == a_norm:
            warn("sibling", f"{other.stem} has the same answer; do the two ask for the same fact?")
        elif len(o_answer) >= 4 and re.search(rf"(?<![a-z0-9]){re.escape(o_answer)}(?![a-z0-9])", q_norm):
            warn("sibling", f"the question contains {other.stem}'s answer")
        if shared:
            warn("sibling", f"six words shared with {other.stem}: '{sorted(shared)[0]}'")

    # Workflow gates.
    try:
        if int(meta.get("revision", "0")) > 2:
            warn("revision", "more than two revision rounds; replace an ineffective question family or record why "
                             "new evidence justifies another revision")
    except ValueError:
        warn("revision", "revision should be a number")
    if status == "ready":
        try:
            revision = int(meta.get("revision", "0"))
        except ValueError:
            revision = -1
        digest = submission_sha256(meta, sec, bundle)
        gap_details = source_gap_details(bundle)
        gaps = [gap["identity"] for gap in gap_details]
        if gaps:
            necessary = set(documents) | cited
            unavailable = {"unavailable-document", "missing-text", "missing-original"}
            unwaivable = [gap["identity"] for gap in gap_details if not gap["document"]
                          or (gap["document"] in necessary and gap["kind"] in unavailable)]
            if unwaivable:
                fail("source-completeness", "ready cannot waive missing necessary/cited sources or "
                     "unscoped provenance gaps: " + ", ".join(unwaivable))
            else:
                errors = source_assessment_errors(sec.get("source assessment", ""), revision, digest, gaps)
                for error in errors:
                    fail("source-completeness", error)
                if errors:
                    fail("source-completeness", "known source gaps remain unassessed: " + ", ".join(gaps))
                else:
                    warn("source-completeness", "corpus remains incomplete; source assessment found "
                         "this candidate unaffected: " + ", ".join(gaps))
        elif not (bundle.path / "notes" / "intake.json").exists():
            warn("source-completeness", "capture provenance is unavailable; confirm original source completeness")
        if any(level == "FAIL" for level, _, _ in found):
            fail("status", "ready with a FAIL; set it back to draft")

        # Local checks are optional historical diagnostics. Only exact-content adverse
        # evidence can block readiness; missing, stale or low-rated local checks cannot.
        stale_local = False

        def adverse_local(issue: str, message: str) -> None:
            if local_issue_resolved(sec.get("local resolution", ""), revision, digest, issue):
                warn("local-diagnostic", f"{issue}: adverse history retained with a current attributed resolution")
            else:
                fail("status", message + f"; retain the return and resolve '{issue}' from source or platform "
                     "evidence in '## Local resolution' (no local model rerun required)")

        for section, is_review in (("blind solve", False), ("review", True), ("shortcut audit", True)):
            local = [r for r in records(sec.get(section, ""), review=is_review) if r["kind"] != "quick-test"]
            current = [r for r in local if r["rev"] == revision and r["tested_sha256"] == digest]
            stale_local = stale_local or len(current) < len(local)
            for record in current:
                if record["duplicate_fields"]:
                    fail("status", f"current {section} record contains duplicate fields; reconcile the raw evidence")
                if record["kind"] == "blind":
                    if record["outcome"] not in OUTCOMES:
                        fail("status", f"unknown current blind-solve outcome {record['outcome']!r}; use {sorted(OUTCOMES)}")
                    elif record["outcome"] in {"ambiguous", "not-answerable"}:
                        adverse_local(f"blind: {record['outcome']}",
                                      "current local evidence reports an ambiguous or not-answerable question")
                elif record["kind"] in {"closed-book", "removal"} and record["result"] == "reaches":
                    adverse_local(f"{record['kind']}: reaches", f"current {record['kind']} result reaches the "
                                  "gold and reports a document-necessity failure")
                elif is_review:
                    if record["verdict"] in {"shortcut", "ambiguous", "not-answerable", "unsupported", "rejected"}:
                        adverse_local(f"{section}: {record['verdict']}",
                                      f"current {section} reports {record['verdict']}")
                    elif record["verdict"] not in {"ready", "clear"}:
                        warn("local-diagnostic", f"current {section} verdict {record['verdict']!r}: "
                             f"{record['findings'] or 'no findings recorded'}. Inspect this diagnostic; local tier "
                             "predictions are not readiness requirements")
        if stale_local:
            warn("local-history", "stale or unbound optional local records retained as history; no local rerun required")

        quick = [r for r in platform_records(sec) if r["rev"] == revision]
        if not quick:
            fail("status", "ready needs an explicit platform difficulty verdict for this revision in "
                 "'## Platform validation' (legacy '## Blind solve' is also read)")
        else:
            platform = quick[-1]
            passed_tier = platform["passed_tier"]
            if not platform["date"]:
                fail("status", "platform result needs its actual calendar date in YYYY-MM-DD format")
            if platform["duplicate_fields"]:
                fail("status", "platform record must not contain duplicate fields")
            if platform["tested_sha256"] != digest:
                fail("status", "latest platform check is not bound to this submission and corpus; "
                     "a new platform result is required for the current fingerprint")
            if platform["platform_verdict"] != "pass":
                fail("status", "ready needs 'platform_verdict: pass'; a local rating or tier count is no pass")
            if not platform["feedback"].strip():
                fail("status", "ready needs the platform's verbatim verdict in 'feedback:'")
            elif feedback_contradicts_pass(platform["feedback"], passed_tier):
                fail("status", "platform feedback contradicts the recorded pass; resolve the verdict before ready")
            if platform["result"] in {"solved", "failed", "rejected"}:
                fail("status", "platform result contradicts the recorded pass")
            if passed_tier not in DIFFICULTIES or DIFFICULTIES.get(passed_tier, 0) < DIFFICULTIES.get(target, 4):
                fail("status", f"ready needs an explicit passed_tier at or above {target}")
            elif passed_tier not in platform["reached"]:
                fail("status", "passed_tier did not run according to the verbatim tier line; record the observed "
                     "tier counts without inferring success")
    return meta, sec, found


def check_bundle(bundle_path: Path, only: list[str] | None = None) -> int:
    bundle = Bundle(bundle_path)
    files = [p for p in bundle.questions() if not only or p.stem in only]
    if not files:
        print(f"No question files under {bundle_path / 'questions'}"
              + (f" matching {only}" if only else "") + ".")
        return 1 if only else 0
    totals = Counter()
    for path in files:
        meta, _, found = check(path, bundle)
        counts = Counter(level for level, _, _ in found)
        totals.update(counts)
        label = f"{path.stem:<6} {meta.get('status', '?'):<9}"
        if meta.get("status") in {"template", "dropped"}:
            print(f"{label} skipped")
            continue
        print(f"{label} {counts['FAIL']} FAIL, {counts['WARN']} WARN")
        for level, code, message in found:
            print(f"    {level} {code}: {message}")
    print(f"\n{len(files)} question file(s): {totals['FAIL']} FAIL, {totals['WARN']} WARN. "
          "A mechanical floor, not a platform pass: validation happens on the platform.")
    return 1 if totals["FAIL"] else 0


def status_all(root: Path = ROOT) -> int:
    rows = []
    for folder in sorted((root / "tasks").iterdir()):
        if not folder.is_dir() or folder.name == TEMPLATE:
            continue
        bundle = Bundle(folder)
        statuses = Counter(parse(p)[0].get("status", "?") for p in bundle.questions())
        session = folder / "notes" / "session.md"
        phase = ""
        if session.exists():
            match = re.search(r"^- Phase[^:]*:\s*(.+)$", read_text(session), re.M)
            phase = match.group(1).strip() if match else ""
        summary = ", ".join(f"{n} {s}" for s, n in sorted(statuses.items())) or "no questions"
        rows.append(f"{folder.name:<32} {len(bundle.live_ids()):>3} docs  {summary}  | phase: {phase[:40]}")
    print("\n".join(rows) if rows else "No bundles under tasks/ yet.")
    return 0


def platform_numbers(bundle: Bundle) -> dict[str, int]:
    """Local Dnn id -> the task page's 'Doc N', from notes/intake.json (the capture's own numbering).
    Ids follow sorted file names and often differ from the page's numbers."""
    try:
        documents = json.loads(read_text(bundle.path / "notes" / "intake.json")).get("documents", [])
        numbers = {str(doc["source"]).replace("\\", "/"): doc["number"] for doc in documents
                   if isinstance(doc, dict) and isinstance(doc.get("number"), int) and doc.get("source")}
    except (OSError, ValueError, AttributeError, TypeError, KeyError):
        return {}
    found = {}
    for doc_id, entry in bundle.manifest.items():
        source = str(entry.get("source", "")).replace("\\", "/")
        if source in numbers:
            found[doc_id] = numbers[source]
    return found


def evidence_rows(section: str) -> list[tuple[str, str, list[str], str]]:
    """Parsed '## Evidence' lines as (document id, location note, component ids, quote)."""
    rows = []
    for line in section.splitlines():
        match = re.match(r'^\s*[-*]\s*(D\d{2,3})\b(.*?):\s*["“](.+)["”]\s*$', line)
        if not match or "TODO" in line:
            continue
        doc_id, where, quote = match.groups()
        tag = re.search(r"\[\s*(c\d{1,2}(?:\s*,\s*c\d{1,2})*)\s*\]", where, re.I)
        ids = re.findall(r"c\d{1,2}", tag.group(1).lower()) if tag else []
        rows.append((doc_id, re.sub(r"\[[^\]]*\]", "", where).strip().strip("()").strip(), ids, quote))
    return rows


def fenced(text: str) -> str:
    """A box's exact text, fenced so Markdown neither renders nor reflows it."""
    mark = "```"
    while mark in text:
        mark += "`"
    return f"{mark}text\n{text.strip()}\n{mark}"


def unwrapped(text: str) -> str:
    """Join a file's wrapped lines into paragraphs, so a pasted box has no break mid-sentence. The
    reasoning keeps its lines: the form reads them as steps."""
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return "\n\n".join(" ".join(line.strip() for line in p.splitlines() if line.strip()) for p in paragraphs)


def form_fields(meta: dict, sec: dict, bundle: Bundle) -> str:
    """Every task-form field of one question in the form's order (Edit Task page, 2026-10-07):
    Question, Number of asks, Gold answer, Step-by-step reasoning, Answer components, Evidence,
    Necessary documents, Reasoning tags, Targeted failure modes. Local ids become Doc numbers."""
    numbers = platform_numbers(bundle)

    def doc(doc_id: str) -> str:
        name = Path(bundle.manifest.get(doc_id, {}).get("source", "?")).name
        return f"Doc {numbers[doc_id]} ({name})" if doc_id in numbers else f"{doc_id} ({name}; page number unknown)"

    comps, _ = components(sec.get("components", ""))
    index = {cid: n for n, cid in enumerate(comps, 1)}
    asks = meta.get("asks", "?")
    out = ["### Question\n\n" + fenced(unwrapped(sec.get("question", ""))),
           "### Number of asks\n\n" + ("1 ask" if asks == "1" else f"{asks} asks"),
           "### Gold answer\n\n" + fenced(unwrapped(sec.get("answer", ""))),
           "### Step-by-step reasoning\n\n" + fenced(sec.get("reasoning", "")),
           "### Answer components\n\n" + "\n\n".join(f"Component {n}\n\n{fenced(comps[cid])}"
                                                     for cid, n in index.items())]
    # The form attaches each quote to one component, so a quote tagged [c1, c2] is two rows.
    rows = [(doc_id, where, cid, quote) for doc_id, where, ids, quote in evidence_rows(sec.get("evidence", ""))
            for cid in ids or ["?"]]
    out.append("### Evidence\n\n" + "\n\n".join(
        f"Evidence {n}: document {doc(doc_id)}, proves component "
        + (f"{index[cid]}. {comps[cid]}" if cid in index else f"{cid} (not listed)")
        + (f" (local note: {where})" if where else "") + "\n\n" + fenced(unwrapped(quote))
        for n, (doc_id, where, cid, quote) in enumerate(rows, 1)))

    documents = list(dict.fromkeys(re.findall(r"\bD\d{2,3}\b", meta.get("documents", ""))))
    parsed, bad = necessary_documents(sec.get("necessary documents", ""))
    if not parsed or bad:
        parsed = [{"ids": [doc_id], "role": "Answer component", "role_text": "Answer component", "note": ""}
                  for doc_id in documents]
    lines = []
    for group in parsed:
        role = group["role"] or group["role_text"]
        first, rest = group["ids"][0], group["ids"][1:]
        line = f"- Tick {doc(first)}, role: {role}"
        if rest:
            line += (f"; also tick {', '.join(doc(d) for d in rest)} and choose it in {doc(first).split(' (')[0]}'s "
                     "\"or...\" box")
        lines.append(line)
        if group["note"]:
            lines.append("\n  Reviewer note:\n\n" + fenced(unwrapped(group["note"])))
    others = sorted((d for d in bundle.live_ids() if d not in documents), key=lambda d: (numbers.get(d, 999), d))
    lines.append("\nLeave unticked: " + (", ".join(doc(d) for d in others) or "none"))
    out.append("### Necessary documents\n\n" + "\n".join(lines))

    tags = {norm(tag) for tag in items(meta.get("tags", ""))}
    out.append("### Reasoning tags\n\nTick: " + ", ".join(t for t in FORM_TAGS if norm(t) in tags)
               + "\n\nLeave unticked: " + (", ".join(t for t in FORM_TAGS if norm(t) not in tags) or "none"))

    modes_text = sec.get("targeted failure modes", "")
    modes, reason = failure_section(modes_text) if modes_text and "TODO" not in modes_text else ([], "")
    if not modes:
        out.append("### Targeted failure modes\n\nMISSING: write 1-3 in the question file's "
                   "'## Targeted failure modes'. The form blocks Submit without them.")
    else:
        blocks = []
        for n, mode in enumerate(modes, 1):
            trap = form_choice(mode.get("trap", ""), FAILURE_TRAPS) or mode.get("trap", "?")
            cause = form_choice(mode.get("cause", ""), FAILURE_CAUSES) or mode.get("cause", "?")
            blocks.append(f"#### Failure mode {n}\n\nTrap: {trap}\n\n{FAILURE_FIELDS['cause']}: {cause}")
        heading = f"#### {FAILURE_REASON} (at most {FAILURE_REASON_WORDS} words)\n\n"
        if reason:
            text = unwrapped(reason)
            blocks.append(heading + fenced(text) + f"\n\n({reason_words(text)} / {FAILURE_REASON_WORDS} words.)")
        else:
            blocks.append(heading + f"MISSING: write '{FAILURE_REASON}:' in the question file. "
                                    "The form blocks Submit without it.")
        out.append("### Targeted failure modes\n\n" + "\n\n".join(blocks))
    return "\n\n".join(out) + "\n"


def form_payload(meta: dict, sec: dict, bundle: Bundle) -> dict:
    """Only form input values, with display labels and one-based platform references.

    Serialize existing content without validation runs or a readiness claim. Reject missing
    fields and ambiguous mappings rather than produce a partial automation payload.
    """
    def required(value: str, field: str) -> str:
        if not value.strip() or "TODO" in value:
            raise ValueError(f"Missing {field} input")
        return value.strip()

    question = unwrapped(required(sec.get("question", ""), "question"))
    answer = unwrapped(required(sec.get("answer", ""), "gold answer"))
    reasoning = required(sec.get("reasoning", ""), "step-by-step reasoning")
    if meta.get("asks") not in {"1", "2"}:
        raise ValueError("Number of asks must be 1 or 2")
    comps, bad = components(sec.get("components", ""))
    component_lines = [line for line in sec.get("components", "").splitlines() if line.strip()]
    if bad or not 1 <= len(comps) <= 10 or len(component_lines) != len(comps):
        raise ValueError("Answer components are missing, duplicated or unparseable")
    values = [required(value, "answer component") for value in comps.values()]
    index = {cid: n for n, cid in enumerate(comps, 1)}
    numbers = platform_numbers(bundle)
    if len(set(numbers.values())) != len(numbers):
        raise ValueError("Ambiguous platform document numbers in notes/intake.json")

    def number(doc_id: str) -> int:
        value = numbers.get(doc_id)
        if type(value) is not int or value < 1 or bundle.manifest.get(doc_id, {}).get("missing"):
            raise ValueError(f"Missing platform document number for {doc_id}; check notes/intake.json")
        return value

    rows = evidence_rows(sec.get("evidence", ""))
    evidence_lines = [line for line in sec.get("evidence", "").splitlines() if line.strip()]
    if not rows or len(rows) != len(evidence_lines):
        raise ValueError("Evidence is missing or unparseable")
    evidence = []
    for doc_id, _, ids, quote in rows:
        if not ids or any(cid not in index for cid in ids):
            raise ValueError("Evidence refers to an unknown or missing answer component")
        evidence.extend({"document_number": number(doc_id), "component_number": index[cid],
                         "quote": unwrapped(required(quote, "evidence quote"))} for cid in ids)
    doc_text = meta.get("documents", "")
    documents = re.findall(r"\bD\d{2,3}\b", doc_text)
    if (not documents or len(set(documents)) != len(documents)
            or re.sub(r"\bD\d{2,3}\b", "", doc_text).strip(" ,;\t\n")):
        raise ValueError("Necessary document selections are missing, duplicated or unparseable")
    roles_text = sec.get("necessary documents", "")
    groups, bad = necessary_documents(roles_text)
    if roles_text.strip():
        if bad or not groups or sorted(d for group in groups for d in group["ids"]) != sorted(documents):
            raise ValueError("Necessary document roles do not match the selections")
    else:
        groups = [{"ids": [doc_id], "role": "Answer component", "note": ""} for doc_id in documents]
    necessary = []
    for group in groups:
        if group["role"] not in DOC_ROLES:
            raise ValueError("Unknown necessary document role")
        necessary.append({"document_numbers": [number(doc_id) for doc_id in group["ids"]],
                          "role": group["role"], "reviewer_note": unwrapped(group["note"])})
    tags = {norm(tag) for tag in items(meta.get("tags", ""))}
    if len(tags) < 2 or tags - {norm(tag) for tag in FORM_TAGS}:
        raise ValueError("Reasoning tags are missing or unknown")
    modes, reason = failure_section(sec.get("targeted failure modes", ""))
    if not 1 <= len(modes) <= 3:
        raise ValueError("Missing targeted failure modes; expected 1-3")
    failures = []
    for mode in modes:
        trap = form_choice(mode.get("trap", ""), FAILURE_TRAPS)
        cause = form_choice(mode.get("cause", ""), FAILURE_CAUSES)
        if trap is None or cause is None:
            raise ValueError("Unknown targeted failure mode trap or cause")
        if any(key in mode for key in LEGACY_FAILURE_BOXES):
            raise ValueError("Targeted failure modes still use the old per-mode boxes; write one shared reason")
        failures.append({"trap": trap, "how_a_careless_solver_fails": cause})
    why = unwrapped(required(reason, "targeted failure modes reason"))
    if reason_words(why) > FAILURE_REASON_WORDS:
        raise ValueError(f"Targeted failure modes reason exceeds {FAILURE_REASON_WORDS} words")
    return {"question": question, "number_of_asks": int(meta["asks"]), "gold_answer": answer,
            "step_by_step_reasoning": reasoning, "answer_components": values, "evidence": evidence,
            "necessary_documents": necessary,
            "reasoning_tags": [tag for tag in FORM_TAGS if norm(tag) in tags],
            "targeted_failure_modes": failures, "why_these_are_traps": why}


def write_json_inputs(bundle: Bundle, path: Path, meta: dict, sec: dict) -> Path:
    """Write a UTF-8 JSON sidecar atomically; preserve the authored Markdown bytes."""
    folder = bundle.path / "questions"
    out = path.with_suffix(".json")
    if (not re.fullmatch(r"q\d{2,}", path.stem) or path.resolve().parent != folder.resolve()
            or folder.is_symlink() or getattr(folder, "is_junction", lambda: False)()
            or out.is_symlink()):
        raise ValueError("JSON output must be an unlinked questions/qNN.json in the bundle")
    data = (json.dumps(form_payload(meta, sec, bundle), ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.stem}-", suffix=".json.tmp", dir=folder)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
        os.replace(temporary, out)
    finally:
        Path(temporary).unlink(missing_ok=True)
    return out


def json_inputs(bundle_path: Path, only: list[str] | None = None) -> int:
    """Serialize requested input values; no mechanical/semantic question validation."""
    bundle = Bundle(bundle_path)
    files = [path for path in bundle.questions() if not only or path.stem in only]
    written, failed = 0, False
    for path in files:
        meta, sec = parse(path)
        if meta.get("status") in {"template", "dropped"} or (not only and meta.get("status") in FROZEN):
            continue
        try:
            out = write_json_inputs(bundle, path, meta, sec)
            print(f"Wrote {out.as_posix()}: form input values only.")
            written += 1
        except (ValueError, OSError) as error:
            print(f"{path.stem}: JSON not written; any existing sidecar is unchanged: {error}")
            failed = True
    if not written and not failed:
        print("No selected questions eligible for JSON input serialization.")
    return int(failed or not written)


def handover(bundle_path: Path, only: list[str] | None = None) -> int:
    """Write notes/handover-qNN.md: every form field of a live question, ready to paste. Any origin
    is handed over with its authorship stated; it is never a submission. Exit 1 on any FAIL."""
    bundle = Bundle(bundle_path)
    files = [p for p in bundle.questions() if not only or p.stem in only]
    if not files:
        print(f"No question files under {bundle_path / 'questions'}" + (f" matching {only}" if only else "") + ".")
        return 1
    numbers = platform_numbers(bundle)
    worst = 0
    for path in files:
        meta, sec, found = check(path, bundle)
        status = meta.get("status", "?")
        if status in {"template", "dropped"} | FROZEN:
            print(f"{path.stem}: status {status}; no hand-over (frozen or not live)")
            continue
        fails = [f"{code}: {message}" for level, code, message in found if level == "FAIL"]
        warns = [f"{code}: {message}" for level, code, message in found if level == "WARN"]
        ids = sorted(set(re.findall(r"\bD\d{2,3}\b", meta.get("documents", "")))
                     | {row[0] for row in evidence_rows(sec.get("evidence", ""))})
        mapping = ", ".join(f"{d} = Doc {numbers[d]}" if d in numbers else f"{d} = unknown" for d in ids)
        origin = meta.get("origin", "?")
        head = [f"# {bundle.path.name} {path.stem} hand-over", "",
                f"Generated {datetime.date.today().isoformat()} by `python tools/check_questions.py "
                f"tasks/{bundle.path.name} --handover --q {path.stem}` from questions/{path.stem}.md. Regenerate it "
                "after any edit. It is not a submission.", "",
                f"- Status {status}, revision {meta.get('revision', '?')}, difficulty_target "
                f"{meta.get('difficulty_target', 'hard (legacy)')}, origin {origin}.",
                f"- tested_sha256 {submission_sha256(meta, sec, bundle)}: question, number of asks, answer, answer "
                "type, components, reasoning, evidence, documents"
                + (", their roles" if sec.get("necessary documents", "").strip() else "")
                + ", tags, target and corpus. Targeted failure modes are outside it"
                + ("." if sec.get("necessary documents", "").strip()
                   else ", and so are the default Answer component roles shown below."),
                f"- Local ids and the task page's numbers: {mapping}.",
                f"- Floor: {len(fails)} FAIL, {len(warns)} WARN."]
        head += [f"  - FAIL {item}" for item in fails] + [f"  - WARN {item}" for item in warns]
        try:
            revision = int(meta.get("revision", "-1"))
        except ValueError:
            revision = -1
        quality = pc.summary(bundle.path, path.stem, revision, submission_sha256(meta, sec, bundle))
        cleared = status == "ready" and not fails and quality["blocking_clearance"] == "clear"
        head.append(f"- Recorded platform Checks: {quality['blocking_clearance']}; "
                    f"{quality['counts'].get('passed', 0)}/39 passed in the latest capture. "
                    f"Submission clearance recorded: {'yes' if cleared else 'no'}. "
                    "Difficulty readiness and Checks clearance are separate; neither is acceptance.")
        head += [f"  - Checks: {message}" for message in quality["errors"] + quality["capture_blockers"]]
        for name, result in quality["checks"].items():
            if result["status"] not in {"passed", "unknown"}:
                head.append(f"  - {name}: {result['status']} ({result['kind']}).")
        if origin.lower() != "user":
            head.append(f"- Authorship: origin {origin}. The form's authorship and AI-use statements are the "
                        "user's to make; the export sheet takes origin user only.")
        if status == "draft":
            head.append("- DRAFT: not locally checked. Use it for a quick test or a look at the form only.")
        if fails:
            head.append("- NOT READY TO PASTE: fix every FAIL first.")
            head.append("- JSON inputs not refreshed because the mechanical floor failed.")
        else:
            try:
                json_path = write_json_inputs(bundle, path, meta, sec)
                head.append(f"- Form input JSON: questions/{json_path.name} (input values only).")
                print(f"Wrote {json_path.as_posix()}: form input values only.")
            except (ValueError, OSError) as error:
                message = f"JSON not written; any existing sidecar is unchanged: {error}"
                head.append(f"- {message}")
                print(f"{path.stem}: {message}")
        head += ["", "Paste each block into the form field of the same name, replacing what the field holds. Copy "
                 "only the text inside each box. On the platform, an edit to the question, answer or necessary "
                 "documents needs a new difficulty result.", ""]
        out = bundle.path / "notes" / f"handover-{path.stem}.md"
        out.parent.mkdir(exist_ok=True)
        out.write_bytes(("\n".join(head) + "\n" + form_fields(meta, sec, bundle)).encode("utf-8"))
        print(f"Wrote {out.as_posix()}: {path.stem} {status} rev {meta.get('revision', '?')}, "
              f"{len(fails)} FAIL, {len(warns)} WARN")
        worst = max(worst, 1 if fails else 0)
    return worst


def export(bundle_path: Path, root: Path = ROOT) -> int:
    bundle = Bundle(bundle_path)
    blocks, skipped = [], []
    for path in bundle.questions():
        meta, sec, found = check(path, bundle)
        fails = [f"{code}: {message}" for level, code, message in found if level == "FAIL"]
        if meta.get("origin", "").lower() != "user" and meta.get("status") != "template":
            fails.append("origin is not 'user'; the form asks you to tick")
        if meta.get("status") != "ready" or fails:
            if meta.get("status") != "template":
                skipped.append(f"{path.stem} ({meta.get('status', '?')}{'; ' + fails[0] if fails else ''})")
            continue
        blocks.append(f"## {path.stem}\n\n" + form_fields(meta, sec, bundle))
    if not blocks:
        print("Nothing to export: no question is ready with a clean floor.")
        print("\n".join(f"  skipped {s}" for s in skipped))
        return 1
    slug = bundle_path.resolve().name
    out = root / "dist" / f"{slug}.md"
    out.parent.mkdir(exist_ok=True)
    head = (f"# {slug} - submission sheet\n\nGenerated {datetime.date.today().isoformat()} by "
            f"tools/check_questions.py from tasks/{slug}/questions/. Ready questions only, each field "
            "exactly as checked and in the form's order. Paste each field into the task form, replacing what it "
            "holds, and attach each evidence passage to its component.\n\nConfirm any statements the form asks "
            "you to tick yourself. The floor checks form mechanics and the platform validates the question; looking at every "
            "document and figure, re-doing the calculation from the evidence alone, and having written the "
            "question are yours to confirm.\n")
    out.write_bytes(("\n---\n\n".join([head] + blocks)).encode("utf-8"))
    print(f"Wrote {out.relative_to(root).as_posix()}: {len(blocks)} question(s).")
    if skipped:
        print("\n".join(f"  skipped {s}" for s in skipped))
    return 0


def hook() -> int:
    """PostToolUse on Edit|Write|MultiEdit: check an edited question file and hand problems back
    as context. Never blocks."""
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, OSError):
        return 0
    raw = str((data.get("tool_input") or {}).get("file_path", "")).replace("\\", "/")
    match = re.search(r"(?:^|/)tasks/([^/]+)/questions/(q[^/]*)\.md$", raw)
    if not match or match.group(1) == TEMPLATE:
        return 0
    path = Path(raw)
    if not path.is_absolute():
        path = Path(data.get("cwd") or ROOT) / path
    if not path.exists():
        return 0
    try:
        meta, _, found = check(path, Bundle(path.parent.parent))
    except Exception as error:  # a hook must never break the edit
        note = f"check_questions.py could not check {match.group(2)}: {error}"
    else:
        if not found:
            return 0
        lines = [f"{level} {code}: {message}" for level, code, message in found]
        note = (f"check_questions.py on {match.group(1)}/{match.group(2)} (status {meta.get('status', '?')}):\n  "
                + "\n  ".join(lines[:25]) + ("\n  ..." if len(lines) > 25 else ""))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": note}}))
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", nargs="?", type=Path, help="tasks/<slug>")
    parser.add_argument("--q", nargs="+", metavar="QID", help="check only these question ids")
    parser.add_argument("--export", action="store_true", help="write dist/<slug>.md from ready questions")
    parser.add_argument("--json", dest="json_inputs", action="store_true",
                        help="write questions/qNN.json with form input values only, without validation")
    parser.add_argument("--handover", action="store_true",
                        help="write notes/handover-qNN.md with every form field, in the form's order")
    parser.add_argument("--status", action="store_true", help="list every bundle's questions by status")
    parser.add_argument("--hook", action="store_true", help="run as a PostToolUse hook")
    args = parser.parse_args(argv)
    if args.hook:
        return hook()
    if args.status:
        return status_all()
    if not args.bundle:
        parser.error("give a bundle (tasks/<slug>) or --status")
    if not args.bundle.is_dir():
        parser.error(f"{args.bundle} is not a directory")
    if sum((args.export, args.handover, args.json_inputs)) > 1:
        parser.error("choose --export, --handover or --json")
    if args.json_inputs:
        return json_inputs(args.bundle, args.q)
    if args.handover:
        return handover(args.bundle, args.q)
    return export(args.bundle) if args.export else check_bundle(args.bundle, args.q)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
