"""Record supplied platform Checks captures; never run validators or certify authorship.

The caller explicitly attests which prepared revision/fingerprint the capture tested.
The ledger preserves imports in order, raw bytes, and hash-linked entries. This is an
audit trail, not a signature from the platform or proof of submission acceptance.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path


CHECKS = {
    "Question, answer & components": "block",
    "Reasoning tags": "block",
    "Solution explanation": "block",
    "Necessary documents": "block",
    "Verbatim evidence": "block",
    "Necessary documents cited": "block",
    "Component coverage": "block",
    "Question length": "advisory",
    "Answer length": "advisory",
    "Answer not given away": "block",
    "Short answer": "block",
    "Components match the answer": "block",
    "Answer parts can be told apart": "block",
    "Restricted names": "block",
    "Original question": "block",
    "Sibling question": "advisory",
    "Writing style": "advisory",
    "Label for items in only one document": "advisory",
    "Answer format stated": "advisory",
    "Partial answers": "advisory",
    "Asks about the world, not the set": "advisory",
    "Question length spread": "advisory",
    "Question in your own words": "block",
    "Reasoning in your own words": "block",
    "One defensible answer": "block",
    "Needs two or more documents": "block",
    "Reasoning reaches the answer": "block",
    "Evidence supports its component": "advisory",
    "Question does not hint the answer": "advisory",
    "No single passage gives the answer": "advisory",
    "Left-out items do not qualify": "advisory",
    "Answer matches a stated figure": "advisory",
    "Each description fits one thing": "advisory",
    "Answer covers every ask": "block",
    "Needs the documents": "block",
    "Question mix": "advisory",
    "List contract": "advisory",
    "Which period": "advisory",
    "Not a duplicate": "block",
}
STATUSES = ("passed", "warning", "failed", "could_not_check", "pending", "unknown")


def _json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _identity(qid: str, revision: int, fingerprint: str) -> None:
    if not isinstance(qid, str) or not re.fullmatch(r"q\d{2,}", qid):
        raise ValueError("Question ID must be q followed by at least two digits.")
    if type(revision) is not int or revision < 0:
        raise ValueError("Revision must be a nonnegative integer.")
    if not isinstance(fingerprint, str) or not re.fullmatch(r"[0-9a-f]{64}", fingerprint):
        raise ValueError("tested_sha256 must be a lowercase SHA-256 fingerprint.")


def _unlinked(path: Path) -> Path:
    path = path.absolute()
    for part in (path, *path.parents):
        if part.is_symlink() or getattr(part, "is_junction", lambda: False)():
            raise ValueError(f"Linked path is not supported: {part}")
    return path


def _inside(bundle: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or rel.drive or ".." in rel.parts or not rel.parts:
        raise ValueError("Artifact path must be relative to the bundle.")
    path = _unlinked(bundle / rel)
    if not path.resolve().is_relative_to(bundle.resolve()):
        raise ValueError("Artifact path escapes its bundle.")
    return path


def _unknown() -> dict:
    return {name: {"status": "unknown", "kind": kind, "detail": "Not captured."}
            for name, kind in CHECKS.items()}


def parse_capture(text: str) -> dict:
    """Parse the full named Checks section, ignoring duplicate attention summaries.

    Recognized statuses must lead the result field; explanatory words such as
    'warning, never a block' never override the reported Passed status.
    """
    checks, errors, seen = _unknown(), [], set()
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line.strip().casefold() == "checks"]
    start = starts[0] + 1 if starts else 0
    in_footer = False
    blockers = []
    for line in lines[start:]:
        stripped = line.strip()
        if re.match(r"(?:\d+\.\s*)?Step\s+\d", stripped, re.I):
            in_footer = True
        if re.match(r"Still needed before you can submit\s*:", stripped, re.I):
            in_footer = True
            blockers.append(stripped)
        if in_footer:
            if re.match(r"[-*]\s+", stripped):
                blockers.append(re.sub(r"^[-*]\s+", "", stripped))
            continue
        row = re.match(r"^[-*]\s+([^:]+):\s*(.*)$", stripped)
        if not row:
            continue
        name, detail = row.groups()
        name = name.strip()
        if name not in CHECKS:
            errors.append(f"Unrecognized check: {name}")
            continue
        if name in seen:
            errors.append(f"Duplicate check: {name}")
            checks[name].update(status="unknown", detail="Duplicate results in capture.")
            continue
        seen.add(name)
        normalized = detail.replace("\u2019", "'")
        match = re.match(r"^(Passed|Warning|Failed|Blocked|Couldn't check|Could not check|"
                         r"Not started|Pending|Running|In progress|Needs review|Review|Unknown)(?=$|[^A-Za-z])",
                         normalized, re.I)
        value = match.group(1).casefold() if match else "unknown"
        status = {"passed": "passed", "warning": "warning", "failed": "failed",
                  "blocked": "failed", "couldn't check": "could_not_check",
                  "could not check": "could_not_check", "not started": "pending",
                  "pending": "pending", "running": "pending", "in progress": "pending",
                  "needs review": "pending", "review": "pending",
                  "unknown": "unknown"}[value]
        if not match:
            errors.append(f"Unrecognized result for {name}")
        checks[name].update(status=status, detail=detail)
        # Only explicit status metadata can make an admin review nonblocking.
        # The stock description about short reasoning is not such a result.
        header = re.split(r"\s+[\u2013\u2014]\s+|\s+--\s+", detail, maxsplit=1)[0]
        if name.endswith("in your own words") and re.search(
                r"(?:^|[\u00b7|])\s*(?:advisory|nonblocking|non-blocking)\b", header, re.I):
            checks[name]["kind"] = "advisory"
    missing = [name for name in CHECKS if name not in seen]
    if missing:
        errors.append("Missing checks: " + "; ".join(missing))
    stale = bool(re.search(r"Docket has been updated|Reload this page|checks? may not have run|"
                           r"(?:checks?|results?) (?:are|may be|might be) stale", text, re.I))
    # Capture-time labels are preserved as labels, not misrepresented as execution times.
    observed = re.search(r"^(?:Saved|Captured):\s*(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(?::\d{2})?)",
                         text, re.M | re.I)
    captured_at = None
    if observed:
        try:
            captured_at = dt.datetime.fromisoformat(observed.group(1)).isoformat()
        except ValueError:
            errors.append("Invalid capture date.")
    return {"checks": checks, "counts": {status: sum(row["status"] == status for row in checks.values())
                                          for status in STATUSES},
            "stale": stale, "captured_at": captured_at, "capture_blockers": blockers,
            "errors": errors}


def _snapshot(bundle: Path, qid: str, revision: int, fingerprint: str, relative: str | None = None) -> Path:
    # Deferred import permits check_questions to expose this ledger in its handover.
    import check_questions as cq

    runs = _inside(bundle, "runs")
    candidates = ([ _inside(bundle, relative) ] if relative else
                  [runs / f"{qid}-r{revision}-v2-{fingerprint}{suffix}" / "snapshot.json"
                   for suffix in ("-platform", "")])
    for candidate in candidates:
        candidate = _unlinked(candidate)
        if not candidate.exists():
            continue
        if not candidate.resolve().is_relative_to(runs.resolve()):
            raise ValueError("Snapshot must be in runs/.")
        snap = json.loads(candidate.read_bytes())
        if (snap.get("schema") != 2 or snap.get("question_id") != qid
                or snap.get("revision") != revision or snap.get("tested_sha256") != fingerprint
                or snap.get("bundle") != bundle.name):
            raise ValueError("Prepared snapshot identity differs from the supplied binding.")
        names = ("solver-1", "solver-2", "shortcut", "closed-book") if snap.get("local_checks", True) else ("corpus",)
        payload = snap["corpus_sha256"]
        if not isinstance(payload, dict) or not payload:
            raise ValueError("Prepared snapshot has no corpus manifest.")
        for name in names:
            packet = _unlinked(candidate.parent / name)
            files = cq.long_path(packet)  # long document names can pass 260 characters here
            expected = {"question.txt"} | (set(payload) if name != "closed-book" else set())
            actual = {file.relative_to(files).as_posix() for file in files.rglob("*") if file.is_file()}
            if actual != expected or any(_unlinked(file) != file.absolute() for file in files.rglob("*")):
                raise ValueError("Prepared packet is incomplete or changed.")
            if (files / "question.txt").read_bytes() != (snap["sections"]["question"] + "\n").encode("utf-8"):
                raise ValueError("Prepared question differs from snapshot.")
            if name == "closed-book":
                continue
            for rel, digest in payload.items():
                _inside(packet, rel)  # refuses absolute, escaping or linked paths
                if _hash((files / rel).read_bytes()) != digest:
                    raise ValueError("Prepared corpus hash mismatch.")
            if cq.submission_sha256(snap["metadata"], snap["sections"], cq.Bundle(files)) != fingerprint:
                raise ValueError("Prepared content fingerprint mismatch.")
        if cq.submission_sha256(snap["metadata"], snap["sections"]) != snap.get("form_sha256"):
            raise ValueError("Prepared form fingerprint mismatch.")
        return candidate
    raise ValueError("No matching prepared snapshot; run prepare for the intended content first.")


def _load_ledger(path: Path) -> list[dict]:
    if not path.exists():
        return []
    ledger = json.loads(_unlinked(path).read_bytes())
    if not isinstance(ledger, dict) or ledger.get("schema") != 1 or not isinstance(ledger.get("records"), list):
        raise ValueError("Malformed platform Checks ledger.")
    previous = None
    for entry in ledger["records"]:
        if not isinstance(entry, dict):
            raise ValueError("Malformed platform Checks record.")
        content = {key: value for key, value in entry.items() if key != "record_sha256"}
        if entry.get("previous_sha256") != previous or entry.get("record_sha256") != _hash(_json(content)):
            raise ValueError("Platform Checks record integrity mismatch.")
        previous = entry["record_sha256"]
    return ledger["records"]


def record_capture(bundle: Path, qid: str, capture: Path, revision: int, tested_sha256: str) -> dict:
    """Append an explicitly author-bound capture; preserve failures and partial returns."""
    _identity(qid, revision, tested_sha256)
    bundle = _unlinked(bundle).resolve(strict=True)
    snapshot = _snapshot(bundle, qid, revision, tested_sha256)
    raw = _unlinked(capture).read_bytes()
    parsed = parse_capture(raw.decode("utf-8-sig"))
    notes = _inside(bundle, "notes")
    notes.mkdir(exist_ok=True)
    ledger_path = _inside(bundle, f"notes/platform-checks-{qid}.json")
    lock = _inside(bundle, f"notes/.platform-checks-{qid}.lock")
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError("Platform Checks ledger is being written; retry after that write finishes.") from None
    os.close(descriptor)
    try:
        records = _load_ledger(ledger_path)
        capture_dir = _inside(bundle, f"notes/platform-checks/{qid}")
        capture_dir.mkdir(parents=True, exist_ok=True)
        raw_path = _inside(bundle, f"notes/platform-checks/{qid}/{_hash(raw)}.txt")
        if raw_path.exists():
            if raw_path.read_bytes() != raw:
                raise ValueError("Stored capture bytes have changed.")
        else:
            with raw_path.open("xb") as stream:
                stream.write(raw)
        entry = {"question_id": qid, "revision": revision, "tested_sha256": tested_sha256,
                 "binding": "author-supplied; not inferred from capture title",
                 "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                 "capture_path": raw_path.relative_to(bundle).as_posix(), "capture_sha256": _hash(raw),
                 "snapshot_path": snapshot.relative_to(bundle).as_posix(),
                 "snapshot_sha256": _hash(snapshot.read_bytes()),
                 "captured_at": parsed["captured_at"],
                 "previous_sha256": records[-1]["record_sha256"] if records else None}
        entry["record_sha256"] = _hash(_json(entry))
        fd, temporary = tempfile.mkstemp(prefix=f".platform-checks-{qid}-", suffix=".tmp", dir=notes)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(_json({"schema": 1, "records": [*records, entry]}) + b"\n")
            os.replace(temporary, ledger_path)
        finally:
            Path(temporary).unlink(missing_ok=True)
        return {**entry, "parsed": parsed}
    finally:
        lock.unlink()


def summary(bundle: Path, qid: str, revision: int, fingerprint: str) -> dict:
    """Read verified evidence. Never fall back from a newer failure/unknown to a pass."""
    result = {**parse_capture(""), "current": False, "blocking_clearance": "unknown",
              "all_checks_passed": False, "advisory_issues": [], "record_count": 0,
              "latest_record": None}
    result["errors"] = []
    try:
        _identity(qid, revision, fingerprint)
        bundle = _unlinked(bundle).resolve(strict=True)
        records = _load_ledger(_inside(bundle, f"notes/platform-checks-{qid}.json"))
        result["record_count"] = len(records)
        if not records:
            result["errors"] = ["No platform Checks capture recorded."]
            return result
        parsed_history = []
        for entry in records:
            _identity(entry["question_id"], entry["revision"], entry["tested_sha256"])
            if entry["question_id"] != qid or entry.get("binding") != "author-supplied; not inferred from capture title":
                raise ValueError("Invalid author-supplied capture binding.")
            raw = _inside(bundle, entry["capture_path"]).read_bytes()
            if _hash(raw) != entry["capture_sha256"]:
                raise ValueError("Stored capture integrity mismatch.")
            parsed = parse_capture(raw.decode("utf-8-sig"))
            if parsed["captured_at"] != entry["captured_at"]:
                raise ValueError("Stored capture date mismatch.")
            parsed_history.append(parsed)
        latest = records[-1]
        result.update(parsed_history[-1], latest_record=latest)
        result["advisory_issues"] = [name for name, row in result["checks"].items()
                                     if row["kind"] == "advisory" and row["status"] != "passed"]
        current = latest["revision"] == revision and latest["tested_sha256"] == fingerprint
        result["current"] = current
        snapshot = _snapshot(bundle, qid, latest["revision"], latest["tested_sha256"], latest["snapshot_path"])
        if _hash(snapshot.read_bytes()) != latest["snapshot_sha256"]:
            raise ValueError("Stored snapshot integrity mismatch.")
        if not current:
            result["blocking_clearance"] = "stale"
            return result
        newest_date = result["captured_at"]
        prior_dates = [item["captured_at"] for item in parsed_history[:-1] if item["captured_at"]]
        if newest_date and prior_dates and newest_date < max(prior_dates):
            result["errors"].append("Latest import is an older capture; it cannot replace newer evidence.")
        elif not newest_date and any(item["capture_blockers"] or any(
                row["kind"] == "block" and row["status"] != "passed" for row in item["checks"].values())
                for item in parsed_history[:-1]):
            result["errors"].append("Undated capture cannot establish that prior blocking results were resolved.")
        if result["stale"]:
            result["blocking_clearance"] = "stale"
        elif result["capture_blockers"] or any(row["kind"] == "block" and row["status"] in {"failed", "warning"}
                                               for row in result["checks"].values()):
            result["blocking_clearance"] = "blocked"
        elif result["errors"] or any(row["kind"] == "block" and row["status"] != "passed"
                                      for row in result["checks"].values()):
            result["blocking_clearance"] = "unknown"
        else:
            result["blocking_clearance"] = "clear"
            result["all_checks_passed"] = result["counts"]["passed"] == len(CHECKS)
    except (OSError, KeyError, TypeError, ValueError) as error:
        result["errors"].append(str(error))
        result["blocking_clearance"] = "unknown"
        result["all_checks_passed"] = False
    return result
