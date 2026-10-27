"""Prepare Docket platform snapshots and report recorded validation without model calls.

Usage:
  python tools/docket_agent.py mine tasks/<slug>
  python tools/docket_agent.py screen tasks/<slug> --idea iNN
  python tools/docket_agent.py packet tasks/<slug> --idea iNN | --q qNN
  python tools/docket_agent.py record-screen tasks/<slug> --idea iNN | --q qNN --results right,wrong,right --note TEXT
  python tools/docket_agent.py prepare tasks/<slug> --q qNN
  python tools/docket_agent.py prepare tasks/<slug> --q qNN --local-checks
  python tools/docket_agent.py report tasks/<slug> --q qNN
  python tools/docket_agent.py record-checks tasks/<slug> --q qNN --capture PATH --revision N --tested-sha256 HASH
  python tools/docket_agent.py replay
  python tools/docket_agent.py efficiency report

mine writes notes/mine.md: where passages, names and figures differ across the bundle's documents, by
the guide's levers (tools/lever_mine.py). It is navigation for hook-finding, not a question or a judgement.
screen checks a short notes/sketches/iNN.md before full components/reasoning are written.
It checks structure and cited inputs, not uniqueness, calculation correctness or difficulty. For a Hard
target it also reads the sketch's '## Lever stack' (two or more levers, each with its quoted trap and
settling passage and its own wrong answer; three or more steps; a decoy) and warns when a rare word of the
question sits in a settling passage.
packet makes one isolated document packet for the strong-solver screen of a Hard target (three
fresh blind solves of the exact sentence) and binds the read guard; record-screen appends the
author's judgement of those solves, bound to the sentence and corpus. It invokes no model.
prepare freezes form fields and one copy of the corpus for platform validation. Optional
--local-checks creates isolated diagnostic packets and binds their read guard instead.
Neither mode invokes models or fabricates checks. Local diagnostics are not prerequisites.
report distinguishes local records, actual recorded platform verdict and mechanical readiness.
replay audits historical platform-tested questions read-only; it is not a new platform test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path

import agent_scope
import check_questions as cq
import form_numbers as fn
import lever_mine
import platform_checks as pc

ROOT = Path(__file__).resolve().parent.parent
PACKETS = ("solver-1", "solver-2", "shortcut")
BINDING_TTL_SECONDS = 12 * 3600
MAX_BINDINGS = 16


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def question_path(bundle: Path, qid: str) -> Path:
    if not re.fullmatch(r"q\d{2,3}", qid):
        raise ValueError("Question id must be qNN (two or three digits).")
    bundle = bundle.resolve()
    if bundle.parent.name != "tasks" or bundle.name == cq.TEMPLATE:
        raise ValueError("Use a named tasks/<slug> bundle, not the template.")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", bundle.name):
        raise ValueError("Bundle slug must contain only letters, digits, hyphens and underscores.")
    path = bundle / "questions" / f"{qid}.md"
    if not path.is_file() or path.is_symlink() or path.resolve().parent != bundle / "questions":
        raise ValueError(f"Missing or unsafe question file: {path}")
    return path


def source_gaps(bundle: Path) -> list[str]:
    """Known omissions only: absence of a marker is not proof of source completeness."""
    return cq.source_completeness(cq.Bundle(bundle))


def with_retry(action, attempts: int = 20, delay: float = 0.5) -> None:
    """Windows briefly locks fresh files and directories (indexing, antivirus); retry the move."""
    for attempt in range(attempts):
        try:
            action()
            return
        except PermissionError:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)


@contextmanager
def scope_lock(lock: Path, timeout: float = 15.0, stale: float = 60.0):
    """Serialise read-modify-write of the shared binding between concurrent prepares."""
    deadline = time.time() + timeout
    while True:
        try:
            os.close(os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            break
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > stale:
                    lock.unlink()
                    continue
            except OSError:
                pass
            if time.time() > deadline:
                raise ValueError("Scope binding is locked by another prepare; run prepare again.") from None
            time.sleep(0.1)
    try:
        yield
    finally:
        try:
            lock.unlink()
        except OSError:
            pass


def bind_scope(root: Path, slug: str, run_name: str, now: float | None = None) -> list[dict]:
    """Add one prepared run to the shared read guard without evicting other active runs.

    Concurrent sessions each prepare their own runs; overwriting a single binding would deny
    reads to solvers still working on another run. Entries whose run directory is gone or that
    are older than BINDING_TTL_SECONDS are dropped. Packets hold only documents and the question,
    so several bound runs widen document access, never key access.
    """
    binding = root / ".claude" / "solver-scope.json"
    binding.parent.mkdir(exist_ok=True)
    if not binding.parent.resolve().is_relative_to(root.resolve()):
        raise ValueError("Scope binding directory must stay inside the workspace.")
    if binding.is_symlink():
        raise ValueError("Linked scope binding is not supported.")
    now = int(time.time() if now is None else now)
    with scope_lock(binding.with_name("solver-scope.lock")):
        try:
            current = json.loads(binding.read_bytes())
            entries = current["runs"] if isinstance(current, dict) and "runs" in current else [current]
            if not isinstance(entries, list):
                entries = []
        except (OSError, ValueError, KeyError, TypeError):
            entries = []
        kept = []
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            other, other_run = entry.get("bundle"), entry.get("run")
            bound = entry.get("bound_at", now)  # a legacy schema 1 entry counts as bound now
            if (not (agent_scope.safe_name(other) and agent_scope.safe_name(other_run))
                    or (other, other_run) == (slug, run_name)
                    or not isinstance(bound, int) or now - bound > BINDING_TTL_SECONDS
                    or not (root / "tasks" / other / "runs" / other_run).is_dir()):
                continue
            kept.append({"bundle": other, "run": other_run, "bound_at": bound})
        entries = ([{"bundle": slug, "run": run_name, "bound_at": now}] + kept)[:MAX_BINDINGS]
        staging = binding.with_name(f"solver-scope.{os.getpid()}.tmp")
        staging.write_bytes(json_bytes({"schema": 2, "runs": entries}))
        with_retry(lambda: os.replace(staging, binding))
    return entries


PERIOD_LABEL = re.compile(r"\b(?:first|second)[- ]half\b|\bhalf[- ]year(?:ly)?\b|\bfull[- ]year\b|\binterim\b"
                          r"|\byear[- ]end\b", re.I)
REPORT_NOUN = r"(?:results?|reports?|updates?|accounts|statements?|announcements?)"


def period_label_notes(question: str, corpus) -> list[str]:
    """Period words in the question that a document also prints as a reporting label ("half-year results").
    A solver can take the period the label reports on: on aq-03120 (2026-10-12) "its last completed financial
    half-year" failed the difficulty gate (the high model read the interim period), and "first-half results"
    as the dating event was blocked twice by the form's "One defensible answer" check."""
    notes = []
    for word in sorted({re.sub(r"[- ]", "-", m.group(0).lower()) for m in PERIOD_LABEL.finditer(question)}):
        pattern = re.compile(r"\b" + re.escape(word).replace(r"\-", "[- ]") + r"\s+" + REPORT_NOUN + r"\b", re.I)
        for doc_id in corpus.live_ids():
            hit = pattern.search(corpus.page_text(doc_id))
            if hit:
                notes.append(f'the question says "{word}" and {doc_id} prints "{hit.group(0)}": a solver can take the '
                             "period that label reports on, not the one meant (aq-03120: gate failed, form blocked). "
                             'Name the period by its structure, such as "the half of its financial year that ..."')
                break
    return notes


def sentence_notes(question: str, answer: str) -> list[str]:
    """Wording notes the full floor raises only after promotion, surfaced while the sentence is still a sketch.

    A quick-test survivor's sentence goes onto the form word for word, so whatever the floor or the form's
    advisories will ask of it has to be settled before the quick test. aq-03707 q03 (2026-10-13): ", if any,"
    was added between the quick test and the difficulty run because the floor first warned at promotion.
    aq-04112 q03 (same day): an order phrase was changed the same way and the changed sentence failed its
    quick test. The patterns mirror check_questions.py; this is a prompt to decide, not a verdict.
    """
    q, a = cq.norm(question), cq.norm(answer)
    notes = []
    tail = (" Settle it in the sketch now: a quick-test survivor's sentence goes onto the form word for word "
            "(aq-03707 q03, aq-04112 q03)")
    several = len([part for part in re.split(r",|\band\b", a) if part.strip()]) > 1
    # The floor also counts a list answer (answer_type: list), which a sketch does not declare: a "which"
    # after an opening phrase ("Relative to nominal capacity, which cells ...") escaped this note on
    # aq-04797 i05 (2026-10-14) and the floor raised it only at promotion. Named items in the answer stand in.
    named_items = len([part for part in re.split(r",|\band\b", a) if re.search(r"[a-z]", part)]) > 1
    which_items = bool(cq.WHICH_ITEMS.search(q)) or (named_items and bool(re.search(r"\bwhich\b|\blist\b", q)))
    if which_items and not re.search(r"\bif any\b|\bnone\b|\bif no\b|\bzero\b", q):
        notes.append("the sentence asks which items and does not say what to answer when nothing qualifies "
                     "('which ..., if any, ...'); the floor and the form's 'Answer format stated' advisory ask "
                     "for it." + tail)
    if which_items and several and not re.search(r"\border\b|rank|chronolog|sequence|ascending|descending"
                                                 r"|alphabetical", q):
        notes.append("the answer lists several items and the sentence gives no order ('alphabetically', "
                     "'in date order'); the floor and the form's 'Answer format stated' advisory ask for one." + tail)
    if re.search(r"\d\.\d|%|percent", a) and not re.search(
            r"decimal|nearest|round|significant figure|whole number|whole percent|tenth|hundredth", q):
        notes.append("the answer is a rate or decimal and the sentence states no precision; the floor warns "
                     "'precision' at promotion. Decide now whether the sentence states it or the figure is exact "
                     "as printed." + tail)
    if re.search(r"(?:^|[,;:(?]\s*)(?:counting|including|whether or not)\b", q) or re.search(
            r"\b(?:anywhere|wherever)\b", q):
        notes.append("the sentence carries a cue ('counting', 'including', 'whether or not', 'anywhere' or "
                     "'wherever'); the floor warns 'cue' at promotion. Name the set or the evidence by its "
                     "structure instead." + tail)
    # The platform guide of 2026-10-15/16 (sections 5 and 7), which the floor mirrors at promotion.
    hint = cq.HINT_WORDS.search(q)
    if hint:
        notes.append(f"the sentence says '{hint.group(0)}', which points at the trap; the guide says to skip words "
                     "like 'actually' or 'originally' and not to spell out the trap (send-back pitfall 5). Let the "
                     "documents carry it." + tail)
    extra = cq.gold_extra(answer, question)
    if extra:
        notes.append(f"the gold carries {extra} that the question does not ask for; the gold is the bare value in "
                     "the asked format (send-back pitfall 5). Two quick tests read as survivals with an explanatory "
                     "parenthesis and failed with the bare answer (ledger rows 24, 26)." + tail)
    if cq.SELECTOR.search(q):
        notes.append("the sentence picks its period or case through another fact: fine when the selector is part of "
                     "the analysis (the company's own best quarter), a send-back when it is an unrelated hop "
                     "(pitfall 1, the most common)." + tail)
    literal = cq.LITERAL.search(q)
    if literal:
        notes.append(f"'{literal.group(0)}': read only the words and confirm they point at exactly the document and "
                     "period the gold uses (send-back reason 8)." + tail)
    if len(question.split()) > 45:
        notes.append(f"the sentence has {len(question.split())} words; the guide aims for 20-45 (send-back reason 4)."
                     + tail)
    return notes


LEVER_LINE = re.compile(r"^\s*[-*]\s*L(\d{1,2})\s*:\s*(.+)$")
STACK_QUOTE = re.compile(r"\b(D\d{2,3})\b[^\"“\n|]*[\"“]([^\"”\n]+)[\"”]")
STEP_LINE = re.compile(r"^\s*\d{1,2}[.)]\s+\S")


def lever_stack(section: str) -> dict:
    """A sketch's '## Lever stack': its levers (name, trap, settles, missed gives), numbered steps and decoy."""
    levers, steps, decoy, shape = [], 0, "", ""
    for line in section.splitlines():
        lever = LEVER_LINE.match(line)
        if lever:
            parts = [part.strip() for part in lever.group(2).split("|")]
            fields = {"number": int(lever.group(1)), "name": parts[0]}
            for part in parts[1:]:
                key, _, value = part.partition(":")
                fields[key.strip().lower()] = value.strip()
            levers.append(fields)
        elif STEP_LINE.match(line):
            steps += 1
        elif re.match(r"^\s*decoy\s*:", line, re.I):
            decoy = line.split(":", 1)[1].strip()
        elif re.match(r"^\s*shape\s*:", line, re.I):
            shape = line.split(":", 1)[1].strip()
    return {"levers": levers, "steps": steps, "decoy": decoy, "shape": shape}


def rare_words(question: str, corpus) -> set[str]:
    """The question's content words that at most a third of the documents print: the words a search follows."""
    ids = corpus.live_ids()
    rare = set()
    for word in cq.content_words(question):
        pattern = re.compile(r"(?<![a-z0-9])" + re.escape(word) + r"(?![a-z0-9])")
        if sum(1 for doc_id in ids if any(pattern.search(text) for text in corpus.texts(doc_id))) <= max(1, len(ids) // 3):
            rare.add(word)
    return rare


def stack_findings(sec: dict, question: str, answer: str, corpus) -> tuple[list[str], list[str]]:
    """Hard-target checks on the sketch's lever stack (playbook section 4; guide of 2026-10-16: "One lever usually
    lands Easy; two together land Medium or Hard"). Quotes must be found; the rest are prompts, not verdicts."""
    failures, warnings = [], []
    text = sec.get("lever stack", "")
    stack = lever_stack(text)
    levers = stack["levers"]
    if not levers or "TODO" in text:
        return [], ["Lever stack: '## Lever stack' is missing or unfinished. Name two or three levers on the path to "
                    "the answer, each with its trap, its settling passage and the wrong answer missing it gives, then "
                    "the steps and the decoy (playbook section 4): from 2026-10-14 to 16, 46 screened sentences were "
                    "right in 138 of 138 local solves, and all eight screened runs came back Too easy at High."]
    if len(levers) < 2:
        warnings.append("Lever stack: one lever. The guide (2026-10-16): 'One lever usually lands Easy; two together "
                        "land Medium or Hard'; its Hard bank stacks two or three.")
    misses: dict[str, int] = {}
    rare = rare_words(question, corpus)
    for lever in levers:
        label = f"Lever stack L{lever['number']}"
        name = cq.norm(re.sub(r"\s*\(most effective\)|\?", "", lever["name"])).strip()
        if name not in cq.LEVERS:
            warnings.append(f"{label}: '{lever['name']}' is not one of the guide's levers (check_questions.LEVERS).")
        for field in ("trap", "settles"):
            quote = STACK_QUOTE.search(lever.get(field, ""))
            if not quote:
                warnings.append(f"{label}: no quoted {field} passage; write {field}: D0N \"exact words\".")
                continue
            doc_id, words = quote.groups()
            if doc_id not in corpus.live_ids() or not cq.quote_found(words, corpus.texts(doc_id)):
                failures.append(f"{label}: the {field} quote is not in {doc_id}'s extracted text.")
            elif field == "settles":
                pointed = sorted(word for word in rare if word in cq.content_words(words))
                if pointed:
                    warnings.append(f"{label}: the question's rare word(s) {', '.join(pointed)} also sit in the "
                                    "settling passage, so a search lands on it (playbook 4; rows 2, 21, 25, 31-33). "
                                    "Name that part by structure, or let the words lead to the trap instead.")
        miss = cq.norm(lever.get("missed gives", ""))
        if not miss:
            warnings.append(f"{label}: no 'missed gives:' answer; a lever is one only if missing it changes the answer.")
        elif miss == cq.norm(answer):
            warnings.append(f"{label}: missing it gives the gold, so it changes nothing.")
        elif miss in misses:
            warnings.append(f"{label} and L{misses[miss]}: missing either gives the same wrong answer, so they test one "
                            "step; make the second lever change the answer differently.")
        else:
            misses[miss] = lever["number"]
    if stack["steps"] < 3:
        warnings.append(f"Lever stack: {stack['steps']} numbered step(s). The guide: one lookup plus one operation is "
                        "usually solved; three or more dependent steps usually aren't.")
    if not stack["decoy"]:
        warnings.append("Lever stack: no 'Decoy:' line. The guide: 'If you can't name one, the question is probably "
                        "too easy.'")
    return failures, warnings


def sketch_path(bundle: Path, idea: str) -> Path:
    bundle = bundle.resolve()
    if (bundle.parent.name != "tasks" or bundle.name == cq.TEMPLATE or
            not re.fullmatch(r"[A-Za-z0-9_-]+", bundle.name)):
        raise ValueError("Use a named tasks/<slug> bundle.")
    if not re.fullmatch(r"i\d{2,3}", idea):
        raise ValueError("Idea id must be iNN (two or three digits).")
    path = bundle / "notes" / "sketches" / f"{idea}.md"
    if (not path.is_file() or path.is_symlink() or
            path.resolve().parent != bundle / "notes" / "sketches"):
        raise ValueError(f"Missing or unsafe sketch file: {path}")
    return path


def screen(bundle: Path, idea: str) -> dict:
    """Read-only lightweight sketch screen. It does not generate independent check records."""
    bundle = bundle.resolve()
    path = sketch_path(bundle, idea)
    meta, sec = cq.parse(path)
    corpus = cq.Bundle(bundle)
    failures, warnings = [], []
    question, answer = sec.get("question", ""), sec.get("answer", "")
    if not question or "TODO" in question or not 8 <= len(question.split()) <= 80:
        failures.append("Question must contain 8-80 words and no TODO placeholder.")
    elif len(question.split()) > 60:
        warnings.append("Question is over the current form's 60-word advisory limit.")
    if not answer or "TODO" in answer or len(answer) > 250 or ";" in answer:
        failures.append("Provide a provisional short gold answer within 250 characters, no semicolon.")
    target = meta.get("difficulty_target", "easy")
    if target not in {"easy", "medium", "hard"}:
        failures.append("difficulty_target must be easy, medium or hard.")
    if not corpus.manifest:
        failures.append("Extract the bundle before screening evidence inputs.")
    cited = set()
    for line in sec.get("evidence", "").splitlines():
        if not re.match(r"^\s*[-*]\s", line):
            continue
        match = re.fullmatch(r'\s*[-*]\s*(D\d{2,3})\s*(?:\([^\n]*\))?\s*'
                             r'(?:\[[^\n]*\])?\s*:\s*["“](.*)["”]\s*', line)
        if not match:
            failures.append("Sketch evidence must be a cited document passage with a quoted input.")
            continue
        doc_id, quote = match.groups()
        if doc_id not in corpus.live_ids():
            failures.append(f"{doc_id}: unknown or missing document.")
        elif len(quote) < 12 or not cq.quote_found(quote, corpus.texts(doc_id)):
            failures.append(f"{doc_id}: input quote must be 12+ characters found in extracted text.")
        else:
            cited.add(doc_id)
            # The form's reasoning number check reads digits near the start of a document only.
            warnings.extend(f"{doc_id}: {note}." for note in fn.input_notes(quote, corpus.page_text(doc_id)))
    if len(cited) < 2:
        failures.append("Identify supported input facts from at least two distinct documents.")
    if corpus.manifest and question:
        warnings.extend(f"{note}." for note in period_label_notes(question, corpus))
    if question and answer and "TODO" not in question:
        warnings.extend(f"{note}." for note in sentence_notes(question, answer))
    if target == "hard" and question and "TODO" not in question:
        if corpus.manifest:
            stack_fails, stack_warns = stack_findings(sec, question, answer, corpus)
            failures.extend(stack_fails)
            warnings.extend(stack_warns)
        screen_fails, screen_warns = cq.screen_findings(question, corpus)
        failures.extend(f"Strong-solver screen: {message}." for message in screen_fails
                        if "no strong-solver screen" not in message)
        warnings.extend(f"Strong-solver screen: {message}." for message in screen_warns)
        if any("no strong-solver screen" in message for message in screen_fails):
            warnings.append("Strong-solver screen: not run yet on this sentence. Before offering it, run "
                            f"`docket_agent.py packet tasks/{bundle.name} --idea {idea}`, three fresh blind solves "
                            "and `record-screen`.")
    intended = set(re.findall(r"\bD\d{2,3}\b", meta.get("documents", "")))
    if intended and intended != cited:
        failures.append("Listed documents must match the cited sketch input sources.")
    gaps = source_gaps(bundle)
    if gaps:
        warnings.append("Known source gaps need candidate-specific impact review before readiness.")
    return {"bundle": bundle.name, "idea": idea, "difficulty_target": target,
            "question": question, "answer": answer, "supported_input_documents": sorted(cited),
            "sketch_sha256": cq.submission_sha256(meta, sec, corpus),
            "source_gaps": gaps, "source_gaps_sha256": cq.source_gaps_sha256(gaps),
            "failures": failures, "warnings": warnings,
            "eligible_for_full_writeup": not failures,
            "claim": "Mechanical sketch screen only. Necessity, uniqueness, calculations and platform"
                     " difficulty require the later checks. No independent or platform test was run."}


def corpus_files(bundle: Path) -> list[Path]:
    manifest_path = bundle / "text" / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError("Extract the bundle first: text/manifest.json is missing.")
    manifest = cq.Bundle(bundle).manifest
    allowed = {"text/manifest.json"}
    for doc_id, entry in manifest.items():
        if not re.fullmatch(r"D\d{2,3}", doc_id) or not isinstance(entry, dict):
            raise ValueError("Invalid extraction manifest.")
        if not entry.get("missing"):
            source = entry.get("source", "")
            if not isinstance(source, str) or not source.startswith("docs/"):
                raise ValueError("Manifest sources must be inside docs/.")
            source_path = bundle / source
            if not source_path.resolve().is_relative_to((bundle / "docs").resolve()):
                raise ValueError("Manifest source escapes docs/.")
            allowed.add(source_path.relative_to(bundle).as_posix())
            allowed.update({f"text/{doc_id}.txt", f"text/{doc_id}.layout.txt"})
    files = []
    for folder in ("docs", "text"):
        base = bundle / folder
        if not base.is_dir() or base.is_symlink() or not base.resolve().is_relative_to(bundle.resolve()):
            raise ValueError(f"Missing or linked corpus directory: {base}")
        for path in sorted(base.rglob("*")):
            if path.is_symlink() or not path.resolve().is_relative_to(base.resolve()):
                raise ValueError(f"Linked corpus paths are not supported: {path}")
            if path.is_file():
                if path.name == ".gitkeep" and path.stat().st_size == 0:
                    continue
                if path.relative_to(bundle).as_posix() not in allowed:
                    raise ValueError(f"Unexpected corpus file; extract originals before preparing: {path}")
                files.append(path)
    return files


def prepare(bundle: Path, qid: str, *, local_checks: bool = False) -> dict:
    bundle = bundle.resolve()
    path = question_path(bundle, qid)
    files = corpus_files(bundle)
    meta, sec, findings = cq.check(path, cq.Bundle(bundle))
    if meta.get("status") in {"submitted", "accepted"}:
        raise ValueError("Submitted/accepted questions are frozen. Use report for a read-only audit.")
    if meta.get("difficulty_target") not in {"easy", "medium", "hard"}:
        raise ValueError("Set explicit difficulty_target: easy|medium|hard before a new check.")
    failures = [f"{code}: {message}" for level, code, message in findings if level == "FAIL"]
    if failures:
        raise ValueError("Fix the mechanical floor before preparing checks: " + "; ".join(failures))
    try:
        revision = int(meta["revision"])
        if revision < 0:
            raise ValueError()
    except (KeyError, ValueError):
        raise ValueError("Set a nonnegative integer revision.") from None
    fingerprint = cq.submission_sha256(meta, sec, cq.Bundle(bundle))
    form_hash = cq.submission_sha256(meta, sec)
    run_name = f"{qid}-r{revision}-v2-{fingerprint}" + ("" if local_checks else "-platform")
    runs = bundle / "runs"
    if runs.is_symlink() or not runs.resolve().is_relative_to(bundle):
        raise ValueError("Linked runs directory is not supported.")
    runs.mkdir(exist_ok=True)
    run = runs / run_name
    payload = {str(file.relative_to(bundle)).replace("\\", "/"):
               hashlib.sha256(file.read_bytes()).hexdigest() for file in files}
    snapshot = {"schema": 2, "bundle": bundle.name, "question_id": qid, "revision": revision,
                "difficulty_target": meta["difficulty_target"], "tested_sha256": fingerprint,
                "form_sha256": form_hash,
                "metadata": meta, "sections": sec, "corpus_sha256": payload,
                "source_gaps": source_gaps(bundle), "local_checks": local_checks}
    if local_checks:
        snapshot["independence"] = "One fresh context per packet. No writer history or shared memory."
    snapshot["source_gaps_sha256"] = cq.source_gaps_sha256(snapshot["source_gaps"])
    question_bytes = (sec["question"] + "\n").encode("utf-8")
    packet_names = (*PACKETS, "closed-book") if local_checks else ("corpus",)
    if not run.exists():
        with tempfile.TemporaryDirectory(prefix="prepare-", dir=runs) as staging_name:
            staging = Path(staging_name)
            for name in packet_names:
                packet = staging / name
                packet.mkdir()
                (packet / "question.txt").write_bytes(question_bytes)
                if name == "closed-book":
                    continue
                for file in files:
                    target = cq.long_path(packet) / file.relative_to(bundle)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(cq.long_path(file), target)
            (staging / "snapshot.json").write_bytes(json_bytes(snapshot))
            # Do not freeze a mixed snapshot if documents changed during preparation.
            for name in packet_names:
                if name == "closed-book":
                    continue
                for rel, digest in payload.items():
                    if hashlib.sha256((cq.long_path(staging / name) / rel).read_bytes()).hexdigest() != digest:
                        raise ValueError("Corpus changed while preparing; run prepare again.")
            if cq.submission_sha256(*cq.parse(path), cq.Bundle(bundle)) != fingerprint:
                raise ValueError("Question or corpus changed while preparing; run prepare again.")
            with_retry(lambda: staging.rename(run))
    validate_snapshot(run, fingerprint, payload, question_bytes, form_hash, snapshot["source_gaps"],
                      local_checks=local_checks)
    bound = bind_scope(bundle.parent.parent, bundle.name, run_name) if local_checks else []
    return {"run": str(run), "tested_sha256": fingerprint,
            "local_checks": local_checks,
            "corpus": str(run / "corpus") if not local_checks else None,
            "packets": {name: str(run / name) for name in packet_names} if local_checks else {},
            "bound_runs": [f"{entry['bundle']}/{entry['run']}" for entry in bound],
            "source_gaps": snapshot["source_gaps"],
            "source_gaps_sha256": snapshot["source_gaps_sha256"],
            "next": ("Optional diagnostic packets prepared; run only the requested or issue-specific checks."
                     if local_checks else "Generate the complete handover and use platform validation.")
                    + " Record actual platform feedback against this fingerprint; validation remains pending."}


def validate_snapshot(run: Path, fingerprint: str, payload: dict, question_bytes: bytes,
                      form_hash: str, gaps: list[str], *, local_checks: bool = True) -> None:
    if run.is_symlink():
        raise ValueError("Linked run directory is not supported.")
    try:
        existing = json.loads((run / "snapshot.json").read_bytes())
        if (existing.get("schema") != 2 or existing["tested_sha256"] != fingerprint
                or existing["corpus_sha256"] != payload
                or existing.get("local_checks", True) != local_checks):
            raise ValueError("Snapshot metadata differs.")
        if (existing.get("source_gaps") != gaps or
                existing.get("source_gaps_sha256") != cq.source_gaps_sha256(gaps)):
            raise ValueError("Frozen source-gap metadata changed.")
        if (existing["form_sha256"] != form_hash or
                cq.submission_sha256(existing["metadata"], existing["sections"]) != form_hash):
            raise ValueError("Frozen submission fields changed.")
        for name in ((*PACKETS, "closed-book") if local_checks else ("corpus",)):
            packet = run / name
            if packet.is_symlink() or not packet.resolve().is_relative_to(run.resolve()):
                raise ValueError(f"Linked {name} packet.")
            files = cq.long_path(packet)  # long document names can pass 260 characters here
            expected = {"question.txt"} | (set(payload) if name != "closed-book" else set())
            actual = {file.relative_to(files).as_posix() for file in files.rglob("*") if file.is_file()}
            if actual != expected or any(file.is_symlink() for file in files.rglob("*")):
                raise ValueError(f"Unexpected files or links in {name} packet.")
            if (files / "question.txt").read_bytes() != question_bytes:
                raise ValueError(f"Question changed in {name} packet.")
            if name != "closed-book":
                for rel, digest in payload.items():
                    if hashlib.sha256((files / rel).read_bytes()).hexdigest() != digest:
                        raise ValueError(f"Corpus changed in {name} packet.")
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise ValueError(f"Prepared snapshot is incomplete or modified; refusing reuse: {error}") from error


SCREEN_RESULTS = ("right", "wrong", "contaminated")


def screen_source(bundle: Path, idea: str | None, qid: str | None) -> Path:
    """The sketch or question file whose exact sentence a strong-solver screen measures."""
    if (idea is None) == (qid is None):
        raise ValueError("Give exactly one of --idea iNN or --q qNN.")
    return sketch_path(bundle, idea) if idea is not None else question_path(bundle, qid)


def screen_sentence(path: Path) -> str:
    question = " ".join(cq.parse(path)[1].get("question", "").split())
    if not question or "TODO" in question:
        raise ValueError(f"{path.name} has no finished question sentence to screen.")
    return question


def screen_packet(bundle: Path, *, idea: str | None = None, qid: str | None = None) -> dict:
    """One isolated document packet for three fresh strong solves of a sketch's or question's exact sentence.

    The packet holds the documents and the sentence only: no gold, notes or other questions. It needs no
    question file, so a sketch is screened before the user spends a quick test or a run. The read guard is
    bound as for --local-checks; every solver reads the same packet in its own fresh context.
    """
    bundle = bundle.resolve()
    path = screen_source(bundle, idea, qid)
    question = screen_sentence(path)
    files = corpus_files(bundle)
    digest = cq.screen_sha256(question, cq.Bundle(bundle))
    payload = {str(file.relative_to(bundle)).replace("\\", "/"):
               hashlib.sha256(file.read_bytes()).hexdigest() for file in files}
    runs = bundle / "runs"
    if runs.is_symlink() or not runs.resolve().is_relative_to(bundle):
        raise ValueError("Linked runs directory is not supported.")
    runs.mkdir(exist_ok=True)
    run_name = f"{path.stem}-screen-{digest[:16]}"
    run = runs / run_name
    question_bytes = (question + "\n").encode("utf-8")
    if not run.exists():
        with tempfile.TemporaryDirectory(prefix="screen-", dir=runs) as staging_name:
            staging = Path(staging_name)
            packet = staging / "solver-1"
            packet.mkdir()
            (packet / "question.txt").write_bytes(question_bytes)
            for file in files:
                target = cq.long_path(packet) / file.relative_to(bundle)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(cq.long_path(file), target)
            (staging / "screen.json").write_bytes(json_bytes({
                "schema": 1, "bundle": bundle.name, "source": path.relative_to(bundle).as_posix(),
                "question": question, "screen_sha256": digest, "corpus_sha256": payload,
                "independence": "One fresh context per solve; the packet holds documents and the sentence only."}))
            for rel, sha in payload.items():
                if hashlib.sha256((cq.long_path(packet) / rel).read_bytes()).hexdigest() != sha:
                    raise ValueError("Corpus changed while preparing; run packet again.")
            if cq.screen_sha256(screen_sentence(path), cq.Bundle(bundle)) != digest:
                raise ValueError("Sentence or corpus changed while preparing; run packet again.")
            with_retry(lambda: staging.rename(run))
    try:
        saved = json.loads((run / "screen.json").read_bytes())
        packet = cq.long_path(run / "solver-1")
        actual = {file.relative_to(packet).as_posix() for file in packet.rglob("*") if file.is_file()}
        if (saved.get("screen_sha256") != digest or saved.get("corpus_sha256") != payload
                or actual != {"question.txt"} | set(payload)
                or (packet / "question.txt").read_bytes() != question_bytes
                or any(hashlib.sha256((packet / rel).read_bytes()).hexdigest() != sha
                       for rel, sha in payload.items())):
            raise ValueError("packet differs from the sentence and corpus it was made for")
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise ValueError(f"Screen packet is incomplete or modified; refusing reuse: {error}") from error
    bound = bind_scope(bundle.parent.parent, bundle.name, run_name)
    return {"run": str(run), "packet": str(run / "solver-1"), "question": question, "screen_sha256": digest,
            "bound_runs": [f"{entry['bundle']}/{entry['run']}" for entry in bound],
            "next": (f"Launch {cq.SCREEN_SOLVES} blind-solver agents, each fresh and given only the workspace root, "
                     "this packet path and the exact question. Judge each answer against the gold yourself, read "
                     f"every miss, then run record-screen with --{'idea' if idea else 'q'} {idea or qid}.")}


def solver_model(root: Path = ROOT) -> str:
    """The blind-solver role's pinned model and effort, as the record states what ran."""
    try:
        head = cq.read_text(root / ".claude" / "agents" / "blind-solver.md").split("---")[1]
    except (OSError, IndexError):
        return "model unknown"
    fields = dict(re.findall(r"(?m)^(model|effort):\s*(\S+)", head))
    return f"{fields.get('model', 'model unknown')}, effort {fields.get('effort', 'unknown')}"


def append_to_section(path: Path, heading: str, line: str) -> None:
    """Append one record line at the end of a ## section, creating the section at the end of the file."""
    text = path.read_bytes().decode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.replace("\r\n", "\n").split("\n")
    start = next((i for i, row in enumerate(lines)
                  if re.fullmatch(r"##\s+" + re.escape(heading) + r"\s*", row, re.I)), None)
    if start is None:
        while lines and not lines[-1].strip():
            lines.pop()
        lines += ["", f"## {heading}", "", line, ""]
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        insert = end
        while insert > start + 1 and not lines[insert - 1].strip():
            insert -= 1
        lines[insert:insert] = [line] if insert > start + 1 else ["", line]
    path.write_bytes(newline.join(lines).encode("utf-8"))


def record_screen(bundle: Path, *, results: list[str], note: str, idea: str | None = None,
                  qid: str | None = None, today: str | None = None) -> dict:
    """Append a strong-solver screen record, bound to the exact sentence and corpus a packet was made for.

    The author judges each solve against the gold and reads every miss; this records that judgement. A
    screen can only reject a sentence: it never predicts or establishes a platform tier.
    """
    bundle = bundle.resolve()
    path = screen_source(bundle, idea, qid)
    if cq.parse(path)[0].get("status", "").lower() in cq.FROZEN:
        raise ValueError("Submitted/accepted questions are frozen; log findings in notes/feedback-qNN.md.")
    question = screen_sentence(path)
    digest = cq.screen_sha256(question, cq.Bundle(bundle))
    try:
        saved = json.loads((bundle / "runs" / f"{path.stem}-screen-{digest[:16]}" / "screen.json").read_bytes())
    except (OSError, ValueError):
        saved = {}
    if saved.get("screen_sha256") != digest:
        raise ValueError("No packet for this exact sentence and corpus: run packet first. The sentence or the "
                         "documents changed since the packet was made, or it was never made.")
    results = [item.strip().lower() for item in results if item.strip()]
    if any(item not in SCREEN_RESULTS for item in results):
        raise ValueError("Each result must be right, wrong or contaminated.")
    valid = [item for item in results if item != "contaminated"]
    if len(valid) != cq.SCREEN_SOLVES:
        raise ValueError(f"Record exactly {cq.SCREEN_SOLVES} uncontaminated fresh solves; replace a contaminated "
                         "one with another fresh solve.")
    note = " ".join(note.split())
    if not note or "|" in note:
        raise ValueError("Give a one-line note without '|': the step each miss took, from its own text.")
    right = valid.count("right")
    decision = ("reject" if right == len(valid) else "check the gold and readings" if right == 0
                else "may offer")
    line = (f"- {today or time.strftime('%Y-%m-%d')} | screen_sha256: {digest} | solver: blind-solver "
            f"({solver_model()}), {len(results)} fresh contexts | results: {', '.join(results)} | "
            f"right: {right}/{len(valid)} | decision: {decision} | note: {note}")
    append_to_section(path, "Strong-solver screen", line)
    return {"file": path.relative_to(bundle).as_posix(), "line": line, "decision": decision,
            "claim": "A local screen can only reject a sentence. It never predicts or establishes a platform tier."}


def report(bundle: Path, qid: str) -> dict:
    bundle = bundle.resolve()
    meta, sec, findings = cq.check(question_path(bundle, qid), cq.Bundle(bundle))
    fingerprint = cq.submission_sha256(meta, sec, cq.Bundle(bundle))
    revision = int(meta.get("revision", "0"))
    checks = [record for record in cq.records(sec.get("blind solve", ""))
              if record["rev"] == revision and record["kind"] != "quick-test"]
    # Always surface the latest record, including failure/pending/stale evidence. A previous
    # passing record must never hide a later failure on the same revision.
    platform = [record for record in cq.platform_records(sec) if record["rev"] == revision]
    checks += platform
    latest = platform[-1] if platform else None
    gaps = source_gaps(bundle)
    quality = pc.summary(bundle, qid, revision, fingerprint)
    failures = [message for level, _, message in findings if level == "FAIL"]
    return {"bundle": bundle.name, "question_id": qid, "status": meta.get("status"),
            "difficulty_target": meta.get("difficulty_target", "hard (legacy)"),
            "tested_sha256": fingerprint, "current_revision_records": checks,
            "latest_platform_record": latest,
            "latest_platform_record_current": bool(latest and latest["tested_sha256"] == fingerprint),
            "quality_checks": quality,
            "submission_clearance_recorded": (meta.get("status") == "ready" and not failures
                                               and quality["blocking_clearance"] == "clear"),
            "source_gaps": gaps,
            "source_gaps_sha256": cq.source_gaps_sha256(gaps),
            "mechanical_failures": failures,
            "warnings": [message for level, _, message in findings if level == "WARN"],
            "claim": "Records are observations, not proof of independence or platform authenticity."
                         " A clean floor alone does not establish a tier pass; difficulty readiness"
                         " and recorded Checks clearance are separate. Neither establishes acceptance."}


def replay(root: Path = ROOT) -> dict:
    rows = []
    for path in sorted((root / "tasks").glob("*/questions/q*.md")):
        meta, sec = cq.parse(path)
        platforms = cq.platform_records(sec)
        if not platforms:
            continue
        _, _, findings = cq.check(path, cq.Bundle(path.parent.parent))
        row = {"bundle": path.parent.parent.name, "question_id": path.stem,
               "status": meta.get("status"), "platform_records": platforms,
               "ready_gate_failures": []}
        # A shadow file lets the real readiness checker replay rejected/draft records without
        # changing a historical question, its sources, or its revision.
        with tempfile.TemporaryDirectory(prefix="docket-replay-") as name:
            shadow = Path(name) / path.name
            text = cq.read_text(path)
            shadow.write_bytes(re.sub(r"(?m)^status:.*$", "status: ready", text, count=1).encode("utf-8"))
            _, _, shadow_findings = cq.check(shadow, cq.Bundle(path.parent.parent))
            row["ready_gate_failures"] = [message for level, code, message in shadow_findings
                                          if level == "FAIL" and code == "status"]
        row["mechanical_failures"] = sum(level == "FAIL" for level, _, _ in findings)
        rows.append(row)
    return {"kind": "historical replay; no new model or platform checks", "questions": rows,
            "count": len(rows)}


def main(argv: list[str]) -> int:
    if argv and argv[0] == "efficiency":
        from docket_efficiency import main as efficiency_main
        return efficiency_main(argv[1:])
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=("mine", "screen", "packet", "record-screen", "prepare", "report",
                                            "record-checks", "replay", "efficiency"))
    parser.add_argument("bundle", nargs="?", type=Path)
    parser.add_argument("--q", dest="qid")
    parser.add_argument("--idea")
    parser.add_argument("--results", help="record-screen: comma-separated right|wrong|contaminated, one per solve")
    parser.add_argument("--note", help="record-screen: one line on the step each miss took, from its own text")
    parser.add_argument("--local-checks", action="store_true",
                        help="prepare optional isolated local diagnostics instead of a platform snapshot")
    parser.add_argument("--capture", type=Path, help="saved platform Checks capture; no platform calls")
    parser.add_argument("--revision", type=int, help="verified revision tested by the captured Checks")
    parser.add_argument("--tested-sha256", help="verified prepared fingerprint tested by the capture")
    args = parser.parse_args(argv)
    try:
        if args.local_checks and args.command != "prepare":
            raise ValueError("--local-checks is only available with prepare.")
        capture_args = (args.capture, args.revision, args.tested_sha256)
        if args.command != "record-checks" and any(value is not None for value in capture_args):
            raise ValueError("--capture/--revision/--tested-sha256 are only available with record-checks.")
        if args.command != "record-screen" and (args.results is not None or args.note is not None):
            raise ValueError("--results/--note are only available with record-screen.")
        if args.command == "mine":
            if args.bundle is None or not args.bundle.resolve().is_relative_to(ROOT / "tasks"):
                raise ValueError("mine requires a tasks/<slug> bundle inside this workspace.")
            if args.qid or args.idea:
                raise ValueError("mine takes the bundle only, without --q or --idea.")
            print(json_bytes(lever_mine.write(args.bundle)).decode("utf-8"), end="")
            return 0
        if args.command in {"packet", "record-screen"}:
            if args.bundle is None or not args.bundle.resolve().is_relative_to(ROOT / "tasks"):
                raise ValueError("packet/record-screen require a tasks/<slug> bundle inside this workspace.")
            if args.command == "packet":
                result = screen_packet(args.bundle, idea=args.idea, qid=args.qid)
            else:
                if args.results is None or args.note is None:
                    raise ValueError("record-screen requires --results and --note.")
                result = record_screen(args.bundle, results=args.results.split(","), note=args.note,
                                       idea=args.idea, qid=args.qid)
            print(json_bytes(result).decode("utf-8"), end="")
            return 0
        if args.command == "replay":
            if args.bundle or args.qid or args.idea:
                raise ValueError("replay takes no bundle or question arguments.")
            result = replay()
        else:
            if args.bundle is None:
                raise ValueError("screen/prepare/report/record-checks require tasks/<slug>.")
            if not args.bundle.resolve().is_relative_to(ROOT / "tasks"):
                raise ValueError("Bundle must be inside this workspace's tasks directory.")
            if args.command == "screen":
                if args.idea is None or args.qid is not None:
                    raise ValueError("screen requires --idea iNN, without --q.")
                result = screen(args.bundle, args.idea)
            else:
                if args.qid is None or args.idea is not None:
                    raise ValueError("prepare/report/record-checks require --q qNN, without --idea.")
                if args.command == "record-checks":
                    if any(value is None for value in capture_args):
                        raise ValueError("record-checks requires --capture, --revision and --tested-sha256; "
                                         "verify the captured version before binding it to a snapshot.")
                    question_path(args.bundle.resolve(), args.qid)
                    result = pc.record_capture(args.bundle.resolve(), args.qid, args.capture,
                                               args.revision, args.tested_sha256)
                else:
                    result = (prepare(args.bundle, args.qid, local_checks=args.local_checks)
                              if args.command == "prepare" else report(args.bundle, args.qid))
        print(json_bytes(result).decode("utf-8"), end="")
        return 1 if args.command == "screen" and result["failures"] else 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"docket_agent.py: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
