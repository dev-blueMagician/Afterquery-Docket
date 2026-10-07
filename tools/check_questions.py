"""Mechanical floor for Docket questions, plus bundle status and the submission sheet.

Usage:
  python tools/check_questions.py tasks/<slug> [--q q01 q02 ...]  check questions; exit 1 on any FAIL
  python tools/check_questions.py tasks/<slug> --handover [--q ...] write notes/handover-qNN.md: every form field
  python tools/check_questions.py tasks/<slug> --export          write dist/<slug>.md from ready questions
  python tools/check_questions.py --status                        every bundle's questions by status
  python tools/check_questions.py --hook                          PostToolUse hook for question files

It checks what a script can: fields, lengths, tags, documents, evidence quotes found verbatim
in text/, the wording traps instruction.md names, and the task form's mechanical quality checks
(captured 2026-10-04, .claude/memory/reference/platform-quality-checks.md): 1-10 answer
components, each a piece of the answer with a tagged quote of 12+ contiguous characters; no
semicolon in the answer; 8-80 words; no answer part in the question. Since 2026-10-07 the form
also needs 1-3 "Targeted failure modes" (a trap and a cause from fixed lists, three boxes of 150+
words together) and gives each necessary document a role; '## Targeted failure modes' and the
optional '## Necessary documents' hold them. --handover prints every form field in the form's
order, with the task page's Doc numbers. It cannot tell whether a question has
one answer, is fair, or is hard; the blind solves, the closed-book solve and the review decide
that. For status ready it confirms two matching blind solves, a closed-book miss, a local
review, and an explicit platform pass at the requested difficulty. New questions declare
'difficulty_target: easy|medium|hard'; their records and shortcut audit bind to both the
revision and a submission/corpus fingerprint. Questions without a target retain the legacy
Hard/maximum difficulty gate. Tier counts show which tests ran, never whether they passed.
A clean run is a floor, not a pass. The question format is tasks/template-task/questions/q00.md.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

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
          "calculate across documents", "state the rounding"}
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
# A failure mode's labelled fields, in the form's order; the last three are its text boxes.
FAILURE_FIELDS = {"trap": "Trap", "cause": "How a careless solver fails", "where": "Where the trap sits",
                  "wrong": "The wrong answer a careless solver gives", "why": "Why the correct answer avoids it"}
FAILURE_BOXES = ("where", "wrong", "why")
FAILURE_WORDS = 150
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


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n")


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


def quote_found(quote: str, haystacks: list[str]) -> bool:
    parts = [norm(p) for p in re.split(r"\s*\[?(?:\.\.\.|…)\]?\s*", quote) if p.strip()]
    for hay in haystacks:
        if all(p in hay for p in parts):
            return True
        flat = dehyphen(hay)
        if all(dehyphen(p) in flat for p in parts):
            return True
        bare = depipe(hay)
        if all(depipe(p) in bare for p in parts):
            return True
    return False


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
        text_dir = bundle.path / "text"
        manifest = text_dir / "manifest.json"
        intake = bundle.path / "notes" / "intake.json"
        docs_dir = bundle.path / "docs"
        payload["corpus"] = {
            "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest() if manifest.exists() else None,
            "intake_sha256": hashlib.sha256(intake.read_bytes()).hexdigest() if intake.exists() else None,
            "documents": [(path.relative_to(docs_dir).as_posix(), hashlib.sha256(path.read_bytes()).hexdigest())
                          for path in sorted(docs_dir.rglob("*")) if path.is_file()
                          and not (path.name == ".gitkeep" and path.stat().st_size == 0)],
            "texts": [(path.name, hashlib.sha256(path.read_bytes()).hexdigest())
                      for path in sorted(text_dir.glob("*.txt"))],
        }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


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
    """Check the explicit reviewer record, without treating its prose as a proven fact.

    Each known gap needs an explanation for all six impacts. The independent reviewer
    must establish those claims from evidence; passing this schema alone proves nothing.
    """
    current = []
    for line in section.splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        fields, _, duplicate = record_fields(line)
        if fields.get("rev", "") == str(revision):
            current.append((fields, duplicate))
    if not current:
        return ["known gaps need this revision's independent '## Source assessment' record"]
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
    if not fields.get("reviewer", "").strip():
        errors.append("source assessment needs an independent reviewer identity")

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
    """Check records, one per bulleted line, oldest first, each with its revision ('rev: N'; None
    on older lines). From '## Blind solve': a blind solve (the line has 'outcome:') or a
    closed-book solve ('closed-book', 'result:'). From '## Review' (review=True): the verdict and
    the difficulty rating."""
    found = []
    for line in section.splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        fields, cells, duplicate = record_fields(line)
        low_fields = {key: norm(value) for key, value in fields.items()}
        revision = fields.get("rev", "")
        record: dict = {"rev": int(revision) if re.fullmatch(r"\d+", revision) else None,
                        "tested_sha256": low_fields.get("tested_sha256", ""), "duplicate_fields": duplicate}
        if review:
            if "verdict" not in fields:
                continue
            record.update(kind="review", verdict=low_fields["verdict"],
                          difficulty=low_fields.get("difficulty", ""))
        else:
            markers = {norm(cell) for cell in cells if ":" not in cell}
            if markers & {"platform quick test", "platform difficulty check"}:
                record.update(kind="quick-test", result=low_fields.get("result", ""),
                              platform_verdict=low_fields.get("platform_verdict", ""),
                              passed_tier=low_fields.get("passed_tier", ""),
                              reached=sorted(observed_tiers(fields.get("tiers", ""))),
                              feedback=fields.get("feedback", ""))
            elif "closed-book solve" in markers:
                record.update(kind="closed-book", result=low_fields.get("result", ""))
            elif "outcome" in fields:
                record.update(kind="blind", outcome=low_fields["outcome"], solver=low_fields.get("solver", ""))
            else:
                continue
        found.append(record)
    return found


def answer_items(answer: str, is_list: bool) -> list[str]:
    parts = items(re.sub(r"^\s*[-*]\s*", "", answer, flags=re.M))
    if is_list and len(parts) == 1:
        parts = [p.strip() for p in re.split(r",|\s+and\s+", parts[0]) if p.strip()]
    return parts


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


def failure_modes(section: str) -> list[dict[str, str]]:
    """'## Targeted failure modes': one '### ...' block per trap, holding the form's five labelled
    fields ('Trap: ...', 'How a careless solver fails: ...', then the three boxes). A box's text runs
    on over the following lines until the next label or block."""
    label = re.compile(r"^\s*(?:[-*]\s*)?(" + "|".join(re.escape(v) for v in FAILURE_FIELDS.values())
                       + r")\s*:\s*(.*)$", re.I)
    blocks: list[dict[str, list[str]]] = []
    key = None
    for line in section.splitlines():
        if re.match(r"^###\s", line):
            blocks.append({"heading": [line.lstrip("#").strip()]})
            key = None
            continue
        match = label.match(line)
        if match and blocks:
            key = next(k for k, v in FAILURE_FIELDS.items() if v.lower() == match.group(1).lower())
            blocks[-1][key] = [match.group(2).strip()]
        elif blocks and key:
            blocks[-1][key].append(line.rstrip())
    return [{key: "\n".join(lines).strip() for key, lines in block.items()} for block in blocks]


def failure_words(mode: dict[str, str]) -> tuple[int, int]:
    """Words across a failure mode's three boxes, all of them and those holding a letter."""
    words = [w for key in FAILURE_BOXES for w in mode.get(key, "").split()]
    return len(words), sum(1 for w in words if re.search(r"[A-Za-z]", w))


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
    targeted = "difficulty_target" in meta
    target = meta.get("difficulty_target", "hard").lower()
    if status not in STATUSES:
        fail("status", f"status '{status}' is not one of {sorted(STATUSES)}")
    if status in {"template", "dropped"}:
        return meta, sec, found
    if target not in DIFFICULTIES:
        fail("difficulty-target", "difficulty_target must be easy, medium or hard")

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
    if ";" in answer:
        fail("short-answer", "the answer has a semicolon, which the form refuses; separate parts with commas or 'and'")
    if len(answer) > 250:
        fail("short-answer", f"answer is {len(answer)} characters; the limit is 250")
    if is_list:
        if len(parts) > 12:
            fail("short-answer", f"answer lists {len(parts)} items; the limit is 12")
        for part in parts:
            if len(part.split()) > 10:
                warn("answer-length", f"list item '{part[:40]}' is over 10 words")
    elif len(answer.split()) > 10:
        fail("short-answer", f"answer has {len(answer.split())} words; a short answer is up to 10 words")
    if re.search(r"\b(because|due to|which means|so that)\b", a_norm) or (
            answer.rstrip().endswith(".") and len(answer.split()) > 4):
        warn("short-answer", "the answer reads like a sentence or an explanation; give the value")
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
        for number in re.findall(r"\d+(?:[.,]\d+)*", a_norm):
            if not any(number in value for value in normed.values()):
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
    for lever in items(meta.get("levers", "")):
        if re.sub(r"\s*\(most effective\)|\?", "", lever.lower()).strip() not in LEVERS:
            warn("levers", f"'{lever}' is not one of the guide's levers (separate them with semicolons)")

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

    # The form's Targeted failure modes (2026-10-07): 1-3 traps from its list, each once, with how a
    # careless solver fails and three boxes of 150+ words together. Submit stays blocked without them.
    if status not in FROZEN:
        modes_text = sec.get("targeted failure modes", "")
        if not modes_text or "TODO" in modes_text:
            (fail if status == "ready" else warn)(
                "failure-modes", "no complete '## Targeted failure modes'; the form blocks Submit until 1-3 traps "
                                 "are filled in, each proved in Lever checks with the wrong answer it gives")
        else:
            modes = failure_modes(modes_text)
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
                if form_choice(mode.get("cause", ""), FAILURE_CAUSES) is None:
                    fail("failure-modes", f"failure mode {number}: '{FAILURE_FIELDS['cause']}' must be one of: "
                                          + ", ".join(FAILURE_CAUSES.values()))
                empty = [f"'{FAILURE_FIELDS[key]}'" for key in FAILURE_BOXES if not mode.get(key)]
                if empty:
                    fail("failure-modes", f"failure mode {number}: empty box {', '.join(empty)}")
                total, lettered = failure_words(mode)
                if total < FAILURE_WORDS:
                    fail("failure-modes", f"failure mode {number} has {total} words across its three boxes; the "
                                          f"form needs at least {FAILURE_WORDS}")
                elif lettered < FAILURE_WORDS:
                    warn("failure-modes", f"failure mode {number}: only {lettered} of its {total} words hold a letter; "
                                          "leave a margin in case the form's counter skips bare figures")

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
        warn("format", "a list answer: say the order, or 'in any order' (form: answer format stated)")
    if (which_items or is_list) and not re.search(r"\bif any\b|\bnone\b|\bif no\b|\bzero\b", q_norm):
        warn("format", "say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' "
                       "(form: answer format stated)")
    if is_list and len(parts) > 3:
        names = "|".join([str(len(parts))] + [w for w, n in NUMBER_WORDS.items() if n == len(parts)])
        if not re.search(rf"\b({names})\b", q_norm):
            warn("list-contract", f"the answer lists {len(parts)} items; say how many to expect, or ask for one "
                                  "value (form: list contract)")
    least = re.search(r"\bat least (\d+|" + "|".join(NUMBER_WORDS) + r")\b", q_norm)
    if least:
        wanted = int(least.group(1)) if least.group(1).isdigit() else NUMBER_WORDS[least.group(1)]
        if len(parts) > wanted:
            warn("partial", f"'at least {least.group(1)}' with {len(parts)} answer items marks a correct partial "
                            "answer wrong (form: partial answers)")
    if re.search(r"\b(this|the) (bundle|document set|set of documents|collection of documents)\b"
                 r"|\bhow many (of the )?documents\b|\bwhich (of the )?documents?\b"
                 r"|\b(both|all|each|exactly \w+) (of the )?documents\b|\bcited (in|by) both\b", q_norm):
        warn("world", "the question is about the documents, not what they describe (rule 10)")
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
        if targeted:
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
                        warn("source-completeness", "corpus remains incomplete; independent review assessed "
                             "this candidate as unaffected: " + ", ".join(gaps))
            elif not (bundle.path / "notes" / "intake.json").exists():
                warn("source-completeness", "capture provenance is unavailable; confirm original source completeness")
        if any(level == "FAIL" for level, _, _ in found):
            fail("status", "ready with a FAIL; set it back to draft")
        solves = [r for r in records(sec.get("blind solve", "")) if r["rev"] == revision]
        reviews = [r for r in records(sec.get("review", ""), review=True) if r["rev"] == revision]
        audits = [r for r in records(sec.get("shortcut audit", ""), review=True) if r["rev"] == revision]
        if any(r["duplicate_fields"] for r in solves + reviews + audits):
            fail("status", "check records must not contain duplicate fields")
        if targeted:
            for label, candidates in (("blind solve", [r for r in solves if r["kind"] == "blind"]),
                                      ("closed-book solve", [r for r in solves if r["kind"] == "closed-book"]),
                                      ("platform check", [r for r in solves if r["kind"] == "quick-test"]),
                                      ("review", reviews), ("shortcut audit", audits)):
                if candidates and candidates[-1]["tested_sha256"] != digest:
                    fail("status", f"latest {label} is not bound to this submission and corpus; "
                                   "record the current tested_sha256 after rerunning it")
            solves = [r for r in solves if r["tested_sha256"] == digest]
            reviews = [r for r in reviews if r["tested_sha256"] == digest]
            audits = [r for r in audits if r["tested_sha256"] == digest]
            if not audits or audits[-1]["verdict"] != "clear":
                fail("status", "ready needs a shortcut audit of this revision and fingerprint with 'verdict: clear'")
        blind = [r["outcome"] for r in solves if r["kind"] == "blind" and r["outcome"] != "solver-error"]
        closed = [r["result"] for r in solves if r["kind"] == "closed-book"]
        quick = [r for r in solves if r["kind"] == "quick-test"]
        if not solves:
            fail("status", f"ready needs this revision's check records (lines tagged 'rev: {revision}') "
                           "in '## Blind solve'; run /docket-check")
        else:
            if set(blind) - OUTCOMES:
                fail("status", f"unknown blind-solve outcome {sorted(set(blind) - OUTCOMES)}; use {sorted(OUTCOMES)}")
            if set(blind) & {"ambiguous", "not-answerable"}:
                fail("status", "ready with an ambiguous or not-answerable blind solve of this revision; "
                               "fix fairness first (rule 4)")
            if blind.count("match") < 2:
                fail("status", "ready needs two matching blind solves of this revision; lever misses and solver "
                               "errors do not validate the gold answer")
            if targeted:
                matching_solvers = {r["solver"] for r in solves if r["kind"] == "blind"
                                    and r["outcome"] == "match" and r["solver"]}
                if len(matching_solvers) < 2:
                    fail("status", "ready needs matching records from two distinct nonempty solver identities "
                                   "('solver: A' and 'solver: B') launched in fresh contexts")
            if not closed or closed[-1] != "misses":
                fail("status", "ready needs a closed-book solve of this revision with 'result: misses' (rule 1)")
            if not quick:
                fail("status", "ready needs an explicit platform difficulty verdict for this revision")
            else:
                platform = quick[-1]
                passed_tier = platform["passed_tier"]
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
        if not reviews or reviews[-1]["verdict"] != "ready":
            fail("status", f"ready needs a review of this revision (rev: {revision}) whose last verdict is ready")
        elif targeted:
            predicted = reviews[-1]["difficulty"]
            rating = "hard" if predicted == "maximum" else predicted
            if DIFFICULTIES.get(rating, 0) < DIFFICULTIES.get(target, 4):
                fail("status", f"ready needs the local review's difficulty prediction at or above {target}")
        elif reviews[-1]["difficulty"] != "maximum":
            fail("status", "legacy ready needs a maximum difficulty review; declare difficulty_target for the "
                           "current Easy, Medium or Hard policy")
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
          "A floor, not a pass: uniqueness, fairness and difficulty need the solves and the review.")
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
    modes = failure_modes(modes_text) if modes_text and "TODO" not in modes_text else []
    if not modes:
        out.append("### Targeted failure modes\n\nMISSING: write 1-3 in the question file's "
                   "'## Targeted failure modes'. The form blocks Submit without them.")
    else:
        blocks = []
        for n, mode in enumerate(modes, 1):
            total, _ = failure_words(mode)
            trap = form_choice(mode.get("trap", ""), FAILURE_TRAPS) or mode.get("trap", "?")
            cause = form_choice(mode.get("cause", ""), FAILURE_CAUSES) or mode.get("cause", "?")
            blocks.append(f"#### Failure mode {n}\n\nTrap: {trap}\n\n{FAILURE_FIELDS['cause']}: {cause}\n\n"
                          + "\n\n".join(f"{FAILURE_FIELDS[key]}:\n\n{fenced(unwrapped(mode.get(key, '')))}"
                                        for key in FAILURE_BOXES)
                          + f"\n\n({total} words across the three boxes; the form needs at least {FAILURE_WORDS}.)")
        out.append("### Targeted failure modes\n\n" + "\n\n".join(blocks))
    return "\n\n".join(out) + "\n"


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
        if origin.lower() != "user":
            head.append(f"- Authorship: origin {origin}. The form's authorship and AI-use statements are the "
                        "user's to make; the export sheet takes origin user only.")
        if status == "draft":
            head.append("- DRAFT: not locally checked. Use it for a quick test or a look at the form only.")
        if fails:
            head.append("- NOT READY TO PASTE: fix every FAIL first.")
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
            "you to tick yourself. The floor, blind solve and review cover the rule checks; looking at every "
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
    if args.export and args.handover:
        parser.error("choose --export or --handover")
    if args.handover:
        return handover(args.bundle, args.q)
    return export(args.bundle) if args.export else check_bundle(args.bundle, args.q)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
