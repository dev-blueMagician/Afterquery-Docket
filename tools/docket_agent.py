"""Prepare isolated Docket checks and report measured readiness without claiming model success.

Usage:
  python tools/docket_agent.py screen tasks/<slug> --idea iNN
  python tools/docket_agent.py prepare tasks/<slug> --q qNN
  python tools/docket_agent.py report tasks/<slug> --q qNN
  python tools/docket_agent.py replay

screen checks a short notes/sketches/iNN.md before full components/reasoning are written.
It checks structure and cited inputs, not uniqueness, calculation correctness or difficulty.
prepare freezes form fields and document bytes, creates question-only solver/shortcut packets,
and binds the read guard to that bundle/run. It never invokes models or fabricates checks.
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


def screen(bundle: Path, idea: str) -> dict:
    """Read-only lightweight sketch screen. It does not generate independent check records."""
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
    if len(cited) < 2:
        failures.append("Identify supported input facts from at least two distinct documents.")
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


def prepare(bundle: Path, qid: str) -> dict:
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
    run_name = f"{qid}-r{revision}-v2-{fingerprint}"
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
                "source_gaps": source_gaps(bundle),
                "independence": "One fresh context per packet. No writer history or shared memory."}
    snapshot["source_gaps_sha256"] = cq.source_gaps_sha256(snapshot["source_gaps"])
    question_bytes = (sec["question"] + "\n").encode("utf-8")
    if not run.exists():
        with tempfile.TemporaryDirectory(prefix="prepare-", dir=runs) as staging_name:
            staging = Path(staging_name)
            for name in PACKETS:
                packet = staging / name
                packet.mkdir()
                (packet / "question.txt").write_bytes(question_bytes)
                for file in files:
                    target = packet / file.relative_to(bundle)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(file, target)
            closed = staging / "closed-book"
            closed.mkdir()
            (closed / "question.txt").write_bytes(question_bytes)
            (staging / "snapshot.json").write_bytes(json_bytes(snapshot))
            # Do not freeze a mixed snapshot if documents changed during preparation.
            for name in PACKETS:
                for rel, digest in payload.items():
                    if hashlib.sha256((staging / name / rel).read_bytes()).hexdigest() != digest:
                        raise ValueError("Corpus changed while preparing; run prepare again.")
            if cq.submission_sha256(*cq.parse(path), cq.Bundle(bundle)) != fingerprint:
                raise ValueError("Question or corpus changed while preparing; run prepare again.")
            with_retry(lambda: staging.rename(run))
    validate_snapshot(run, fingerprint, payload, question_bytes, form_hash, snapshot["source_gaps"])
    bound = bind_scope(bundle.parent.parent, bundle.name, run_name)
    return {"run": str(run), "tested_sha256": fingerprint,
            "packets": {name: str(run / name) for name in (*PACKETS, "closed-book")},
            "bound_runs": [f"{entry['bundle']}/{entry['run']}" for entry in bound],
            "source_gaps": snapshot["source_gaps"],
            "source_gaps_sha256": snapshot["source_gaps_sha256"],
            "next": "Launch fresh independent checks. Record actual returns; then review. Platform pending."}


def validate_snapshot(run: Path, fingerprint: str, payload: dict, question_bytes: bytes,
                      form_hash: str, gaps: list[str]) -> None:
    if run.is_symlink():
        raise ValueError("Linked run directory is not supported.")
    try:
        existing = json.loads((run / "snapshot.json").read_bytes())
        if (existing.get("schema") != 2 or existing["tested_sha256"] != fingerprint
                or existing["corpus_sha256"] != payload):
            raise ValueError("Snapshot metadata differs.")
        if (existing.get("source_gaps") != gaps or
                existing.get("source_gaps_sha256") != cq.source_gaps_sha256(gaps)):
            raise ValueError("Frozen source-gap metadata changed.")
        if (existing["form_sha256"] != form_hash or
                cq.submission_sha256(existing["metadata"], existing["sections"]) != form_hash):
            raise ValueError("Frozen submission fields changed.")
        for name in (*PACKETS, "closed-book"):
            packet = run / name
            if packet.is_symlink() or not packet.resolve().is_relative_to(run.resolve()):
                raise ValueError(f"Linked {name} packet.")
            expected = {"question.txt"} | (set(payload) if name in PACKETS else set())
            actual = {str(file.relative_to(packet)).replace("\\", "/")
                      for file in packet.rglob("*") if file.is_file()}
            if actual != expected or any(file.is_symlink() for file in packet.rglob("*")):
                raise ValueError(f"Unexpected files or links in {name} packet.")
            if (packet / "question.txt").read_bytes() != question_bytes:
                raise ValueError(f"Question changed in {name} packet.")
            if name in PACKETS:
                for rel, digest in payload.items():
                    if hashlib.sha256((packet / rel).read_bytes()).hexdigest() != digest:
                        raise ValueError(f"Corpus changed in {name} packet.")
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise ValueError(f"Prepared snapshot is incomplete or modified; refusing reuse: {error}") from error


def report(bundle: Path, qid: str) -> dict:
    bundle = bundle.resolve()
    meta, sec, findings = cq.check(question_path(bundle, qid), cq.Bundle(bundle))
    fingerprint = cq.submission_sha256(meta, sec, cq.Bundle(bundle))
    revision = int(meta.get("revision", "0"))
    checks = [record for record in cq.records(sec.get("blind solve", ""))
              if record["rev"] == revision]
    # Always surface the latest record, including failure/pending/stale evidence. A previous
    # passing record must never hide a later failure on the same revision.
    platform = [record for record in checks if record["kind"] == "quick-test"]
    latest = platform[-1] if platform else None
    gaps = source_gaps(bundle)
    return {"bundle": bundle.name, "question_id": qid, "status": meta.get("status"),
            "difficulty_target": meta.get("difficulty_target", "hard (legacy)"),
            "tested_sha256": fingerprint, "current_revision_records": checks,
            "latest_platform_record": latest, "source_gaps": gaps,
            "source_gaps_sha256": cq.source_gaps_sha256(gaps),
            "mechanical_failures": [message for level, _, message in findings if level == "FAIL"],
            "warnings": [message for level, _, message in findings if level == "WARN"],
            "claim": "Records are observations, not proof of independence or platform authenticity."
                         " A clean floor alone does not establish a tier pass."}


def replay(root: Path = ROOT) -> dict:
    rows = []
    for path in sorted((root / "tasks").glob("*/questions/q*.md")):
        meta, sec = cq.parse(path)
        platforms = [r for r in cq.records(sec.get("blind solve", "")) if r["kind"] == "quick-test"]
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
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=("screen", "prepare", "report", "replay"))
    parser.add_argument("bundle", nargs="?", type=Path)
    parser.add_argument("--q", dest="qid")
    parser.add_argument("--idea")
    args = parser.parse_args(argv)
    try:
        if args.command == "replay":
            if args.bundle or args.qid or args.idea:
                raise ValueError("replay takes no bundle or question arguments.")
            result = replay()
        else:
            if args.bundle is None:
                raise ValueError("screen/prepare/report require tasks/<slug>.")
            if not args.bundle.resolve().is_relative_to(ROOT / "tasks"):
                raise ValueError("Bundle must be inside this workspace's tasks directory.")
            if args.command == "screen":
                if args.idea is None or args.qid is not None:
                    raise ValueError("screen requires --idea iNN, without --q.")
                result = screen(args.bundle, args.idea)
            else:
                if args.qid is None or args.idea is not None:
                    raise ValueError("prepare/report require --q qNN, without --idea.")
                result = prepare(args.bundle, args.qid) if args.command == "prepare" else report(args.bundle, args.qid)
        print(json_bytes(result).decode("utf-8"), end="")
        return 1 if args.command == "screen" and result["failures"] else 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"docket_agent.py: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
