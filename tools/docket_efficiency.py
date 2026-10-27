"""Record prospective Docket authoring measurements without running validations.

One ledger follows the next five distinct promoted candidates across bundles. Timers
measure only explicit start/stop intervals: stop before platform waits; discard an
accidentally open interval instead of estimating it. Supplied usage and platform
receipts are evidence, never inferred from local checks or difficulty labels.

Usage: python tools/docket_efficiency.py COMMAND [--ledger PATH] [command options]
Commands: init, start, stop, promote, record, report. Run COMMAND --help for options.
The public functions accept a ledger Path and raise ValueError for invalid records.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import uuid


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LEDGER = ROOT / "notes" / "efficiency.json"
TRIAL_SIZE = 5
PHASES = ("sketch", "draft", "revision")
STAGES = ("quality", "difficulty", "review")
COVERAGES = ("complete", "partial", "unknown")
OUTCOMES = ("accepted", "rejected", "pending", "retired_before_submission")


def utc_now() -> datetime:
    """Clock seam for deterministic tests; production always records current UTC."""
    return datetime.now(timezone.utc)


def _timestamp() -> str:
    now = utc_now()
    if not isinstance(now, datetime) or now.tzinfo is None:
        raise ValueError("The timer clock must return an aware datetime.")
    return now.astimezone(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _date(value: object) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("Ledger timestamps must be explicit UTC strings ending in Z.")
    try:
        result = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        raise ValueError("Invalid ledger timestamp.") from None
    if result.utcoffset().total_seconds() != 0:
        raise ValueError("Ledger timestamps must be UTC.")
    return result


def _keys(value: object, expected: set[str], label: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise ValueError(f"Invalid {label} fields; expected: {', '.join(sorted(expected))}.")


def _integer(value: object, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{label} must be an integer >= {minimum} (not a boolean).")
    return value


def _identifier(value: object, label: str, pattern: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(pattern, value):
        raise ValueError(f"Invalid {label}.")
    return value


def _identity(bundle: object, candidate: object) -> tuple[str, str]:
    return (
        _identifier(bundle, "bundle slug", r"[A-Za-z0-9][A-Za-z0-9_-]{0,127}"),
        _identifier(candidate, "candidate id (iNN)", r"i\d{2,3}"),
    )


def _choice(value: object, choices: tuple[str, ...], label: str) -> None:
    if not isinstance(value, str) or value not in choices:
        raise ValueError(f"{label} must be one of: {', '.join(choices)}.")


def _validate_event(event: object) -> None:
    if not isinstance(event, dict):
        raise ValueError("An event must be a JSON object.")
    kind = event.get("kind")
    specific = {
        "usage": {"total_tokens"},
        "platform_attempt": {"attempt_id", "stage", "revision", "tested_sha256"},
        "revision": {"revision", "tested_sha256"},
        "outcome": {"outcome"},
        "coverage": {"timing", "tokens"},
    }
    if not isinstance(kind, str) or kind not in specific:
        raise ValueError("Unknown event kind.")
    _keys(event, {"kind", "event_id", "bundle", "candidate", "source"} | specific[kind], "event")
    _identity(event["bundle"], event["candidate"])
    _identifier(event["event_id"], "event_id", r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,199}")
    if not isinstance(event["source"], str) or not event["source"].strip():
        raise ValueError("Every event needs a nonempty evidence source.")
    if kind == "usage":
        _integer(event["total_tokens"], "total_tokens")
    if kind in ("revision", "platform_attempt"):
        _integer(event["revision"], "revision")
        _identifier(event["tested_sha256"], "tested_sha256 (64 hex characters)", r"[a-fA-F0-9]{64}")
    if kind == "platform_attempt":
        _identifier(event["attempt_id"], "attempt_id", r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,199}")
        _choice(event["stage"], STAGES, "stage")
    if kind == "outcome":
        _choice(event["outcome"], OUTCOMES, "outcome")
    if kind == "coverage":
        _choice(event["timing"], COVERAGES, "timing coverage")
        _choice(event["tokens"], COVERAGES, "token coverage")


def _candidate(state: dict, bundle: str, candidate: str) -> dict | None:
    return next((item for item in state["candidates"]
                 if (item["bundle"], item["candidate"]) == (bundle, candidate)), None)


def _ensure_candidate(state: dict, bundle: str, candidate: str, stamp: str) -> dict:
    item = _candidate(state, bundle, candidate)
    if item is None:
        item = {"bundle": bundle, "candidate": candidate, "created_at": stamp, "promotion": None}
        state["candidates"].append(item)
    return item


def _for_candidate(items: list[dict], bundle: str, candidate: str) -> list[dict]:
    return [item for item in items if (item["bundle"], item["candidate"]) == (bundle, candidate)]


def _basis(state: dict, bundle: str, candidate: str) -> dict:
    return {
        "session_ids": [s["session_id"] for s in _for_candidate(state["sessions"], bundle, candidate)],
        "usage_event_ids": [r["event"]["event_id"] for r in state["events"]
                            if r["event"]["kind"] == "usage"
                            and (r["event"]["bundle"], r["event"]["candidate"]) == (bundle, candidate)],
        "revision_keys": sorted({f"{r['event']['revision']}:{r['event']['tested_sha256'].lower()}"
                                 for r in state["events"] if r["event"]["kind"] == "revision"
                                 and (r["event"]["bundle"], r["event"]["candidate"]) == (bundle, candidate)}),
    }


def _check_event_history(state: dict, event: dict) -> None:
    """Check a new receipt against earlier observations, without inventing events."""
    bundle, candidate = event["bundle"], event["candidate"]
    earlier = [r["event"] for r in state["events"]
               if (r["event"]["bundle"], r["event"]["candidate"]) == (bundle, candidate)]
    kind = event["kind"]
    for old in earlier:
        if kind in ("revision", "platform_attempt") and old["kind"] in ("revision", "platform_attempt"):
            if old["revision"] == event["revision"] and old["tested_sha256"].lower() != event["tested_sha256"].lower():
                raise ValueError("A recorded revision cannot be reused with a different hash.")
        if kind == old["kind"] == "platform_attempt":
            if (old["stage"], old["attempt_id"]) == (event["stage"], event["attempt_id"]):
                if (old["revision"], old["tested_sha256"].lower()) != (event["revision"], event["tested_sha256"].lower()):
                    raise ValueError("A platform attempt identity cannot be reused for different content.")
    if kind == "outcome" and event["outcome"] == "retired_before_submission":
        if any((old["kind"] == "platform_attempt" and old["stage"] == "review")
               or (old["kind"] == "outcome" and old["outcome"] in ("accepted", "rejected"))
               for old in earlier):
            raise ValueError("Retirement before submission conflicts with an observed review/submission outcome.")
    if kind == "coverage":
        sessions = _for_candidate(state["sessions"], bundle, candidate)
        if event["timing"] == "complete" and (not sessions or any(
                s["ended_at"] is None or s["discarded"] for s in sessions)):
            raise ValueError("Complete timing requires measured, closed sessions and no discarded intervals.")
        if event["tokens"] == "complete" and not any(old["kind"] == "usage" for old in earlier):
            raise ValueError("Complete token coverage requires a usage receipt, including explicit zero if applicable.")


def _validate_state(state: object) -> None:
    _keys(state, {"schema_version", "trial_size", "created_at", "candidates", "sessions", "events"}, "ledger")
    if type(state["schema_version"]) is not int or state["schema_version"] != 1:
        raise ValueError("Unsupported efficiency ledger schema.")
    if type(state["trial_size"]) is not int or state["trial_size"] != TRIAL_SIZE:
        raise ValueError("This prospective trial has exactly five promotion slots.")
    _date(state["created_at"])
    for name in ("candidates", "sessions", "events"):
        if not isinstance(state[name], list):
            raise ValueError(f"Ledger {name} must be a list.")
    identities, slots, qids = set(), set(), set()
    for item in state["candidates"]:
        _keys(item, {"bundle", "candidate", "created_at", "promotion"}, "candidate")
        identity = _identity(item["bundle"], item["candidate"])
        if identity in identities:
            raise ValueError("Duplicate candidate identity.")
        identities.add(identity)
        _date(item["created_at"])
        promotion = item["promotion"]
        if promotion is not None:
            _keys(promotion, {"qid", "slot", "baseline_revision", "promoted_at"}, "promotion")
            _identifier(promotion["qid"], "question id (qNN)", r"q\d{2,3}")
            _integer(promotion["slot"], "slot", 1)
            _integer(promotion["baseline_revision"], "baseline_revision")
            _date(promotion["promoted_at"])
            qkey = (item["bundle"], promotion["qid"])
            if promotion["slot"] in slots or qkey in qids:
                raise ValueError("Duplicate promotion slot or question identity.")
            slots.add(promotion["slot"])
            qids.add(qkey)
    if len(slots) > TRIAL_SIZE or slots != set(range(1, len(slots) + 1)):
        raise ValueError("Promotion slots must be consecutive and limited to five.")
    session_ids, opened, intervals = set(), 0, []
    for session in state["sessions"]:
        _keys(session, {"session_id", "bundle", "candidate", "phase", "started_at", "ended_at", "discarded"}, "session")
        sid = _identifier(session["session_id"], "session_id", r"[a-f0-9]{32}")
        if sid in session_ids:
            raise ValueError("Duplicate timer session.")
        session_ids.add(sid)
        if _identity(session["bundle"], session["candidate"]) not in identities:
            raise ValueError("Timer references a missing candidate.")
        _choice(session["phase"], PHASES, "phase")
        started = _date(session["started_at"])
        if type(session["discarded"]) is not bool:
            raise ValueError("discarded must be a boolean.")
        if session["ended_at"] is None:
            opened += 1
            if session["discarded"]:
                raise ValueError("An open timer cannot already be discarded.")
            ended = datetime.max.replace(tzinfo=timezone.utc)
        else:
            ended = _date(session["ended_at"])
            if ended < started:
                raise ValueError("Timer ends before it starts.")
        intervals.append((started, ended))
    if opened > 1:
        raise ValueError("Only one timer may be active globally.")
    intervals.sort()
    for previous, following in zip(intervals, intervals[1:]):
        if following[0] < previous[1]:
            raise ValueError("Authoring timer intervals cannot overlap.")
    seen_ids, history = set(), {**state, "events": []}
    for receipt in state["events"]:
        _keys(receipt, {"event", "recorded_at", "coverage_basis"}, "receipt")
        event = receipt["event"]
        _validate_event(event)
        _date(receipt["recorded_at"])
        if (event["bundle"], event["candidate"]) not in identities:
            raise ValueError("Receipt references a missing candidate.")
        if event["event_id"] in seen_ids:
            raise ValueError("Duplicate stored event id.")
        seen_ids.add(event["event_id"])
        # Historical complete coverage is allowed to become stale after later work.
        if event["kind"] != "coverage":
            _check_event_history(history, event)
            if receipt["coverage_basis"] is not None:
                raise ValueError("Only coverage receipts have a coverage basis.")
        else:
            basis = receipt["coverage_basis"]
            _keys(basis, {"session_ids", "usage_event_ids", "revision_keys"}, "coverage basis")
            current = _basis(history, event["bundle"], event["candidate"])
            for key in basis:
                values = basis[key]
                if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
                    raise ValueError("Coverage basis must contain identifier lists.")
                if len(values) != len(set(values)) or not set(values).issubset(current[key]):
                    raise ValueError("Coverage refers to missing or unrelated measurements.")
            covered = [s for s in state["sessions"] if s["session_id"] in basis["session_ids"]]
            if event["timing"] == "complete" and (not covered or any(
                    s["ended_at"] is None or s["discarded"] for s in covered)):
                raise ValueError("Invalid complete timing attestation.")
            if event["tokens"] == "complete" and not basis["usage_event_ids"]:
                raise ValueError("Invalid complete token attestation.")
        history["events"].append(receipt)


def _no_constant(value: str) -> None:
    raise ValueError(f"Non-finite JSON number is not allowed: {value}.")


def _read(path: Path) -> dict:
    if path.is_symlink():
        raise ValueError("The ledger must not be a symbolic link.")
    try:
        state = json.loads(path.read_text(encoding="utf-8"), parse_constant=_no_constant)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read efficiency ledger: {exc}") from None
    _validate_state(state)
    return state


@contextmanager
def _lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_name(path.name + ".lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise ValueError(f"Efficiency ledger is locked: {lock}. Retry after the other writer finishes.") from None
    os.close(fd)
    try:
        yield
    finally:
        lock.unlink()


def _write(path: Path, state: dict) -> None:
    _validate_state(state)
    if path.is_symlink():
        raise ValueError("The ledger must not be a symbolic link.")
    text = json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"
    descriptor, name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def init(ledger: Path = DEFAULT_LEDGER) -> dict:
    """Create an empty prospective trial; an existing valid ledger is unchanged."""
    path = Path(ledger).absolute()
    with _lock(path):
        if path.exists() or path.is_symlink():
            return _read(path)
        state = {"schema_version": 1, "trial_size": TRIAL_SIZE, "created_at": _timestamp(),
                 "candidates": [], "sessions": [], "events": []}
        _write(path, state)
        return state


def start(ledger: Path, bundle: str, candidate: str, phase: str) -> dict:
    """Start measured active authoring, creating a prospect without enrolling it."""
    _identity(bundle, candidate)
    _choice(phase, PHASES, "phase")
    path = Path(ledger).absolute()
    with _lock(path):
        state = _read(path)
        if any(s["ended_at"] is None for s in state["sessions"]):
            raise ValueError("A timer is already active; stop it before starting another.")
        stamp = _timestamp()
        _ensure_candidate(state, bundle, candidate, stamp)
        session = {"session_id": uuid.uuid4().hex, "bundle": bundle, "candidate": candidate,
                   "phase": phase, "started_at": stamp, "ended_at": None, "discarded": False}
        state["sessions"].append(session)
        _write(path, state)
        return session


def stop(ledger: Path, session_id: str, discard: bool = False) -> dict:
    """Stop a timer; discard preserves a lost interval but excludes its duration."""
    _identifier(session_id, "session_id", r"[a-f0-9]{32}")
    if type(discard) is not bool:
        raise ValueError("discard must be a boolean.")
    path = Path(ledger).absolute()
    with _lock(path):
        state = _read(path)
        session = next((s for s in state["sessions"] if s["session_id"] == session_id), None)
        if session is None:
            raise ValueError("Unknown timer session.")
        if session["ended_at"] is not None:
            if session["discarded"] != discard:
                raise ValueError("A completed timer cannot be changed to or from discarded.")
            return session
        session["ended_at"] = _timestamp()
        session["discarded"] = discard
        _write(path, state)
        return session


def promote(ledger: Path, bundle: str, candidate: str, qid: str, revision: int = 0) -> dict:
    """Enroll a newly promoted candidate once; resume/revision reuses its slot."""
    _identity(bundle, candidate)
    _identifier(qid, "question id (qNN)", r"q\d{2,3}")
    _integer(revision, "revision")
    path = Path(ledger).absolute()
    with _lock(path):
        state = _read(path)
        item = _candidate(state, bundle, candidate)
        if item is not None and item["promotion"] is not None:
            if item["promotion"]["qid"] != qid:
                raise ValueError("This candidate is already enrolled under a different question.")
            if revision < item["promotion"]["baseline_revision"]:
                raise ValueError("A resumed revision cannot precede the promotion baseline.")
            return item
        enrolled = [c for c in state["candidates"] if c["promotion"] is not None]
        if any(c["bundle"] == bundle and c["promotion"]["qid"] == qid for c in enrolled):
            raise ValueError("This question is already enrolled under another candidate.")
        if len(enrolled) >= TRIAL_SIZE:
            raise ValueError("All five prospective promotion slots are already enrolled.")
        stamp = _timestamp()
        item = _ensure_candidate(state, bundle, candidate, stamp)
        item["promotion"] = {"qid": qid, "slot": len(enrolled) + 1,
                             "baseline_revision": revision, "promoted_at": stamp}
        _write(path, state)
        return item


def record(ledger: Path, event: dict) -> dict:
    """Append a supplied observation; exact event-id replays are idempotent."""
    _validate_event(event)
    # Copy caller-owned data before storing or returning it.
    event = json.loads(json.dumps(event, allow_nan=False))
    if "tested_sha256" in event:
        event["tested_sha256"] = event["tested_sha256"].lower()
    path = Path(ledger).absolute()
    with _lock(path):
        state = _read(path)
        for receipt in state["events"]:
            if receipt["event"]["event_id"] == event["event_id"]:
                if receipt["event"] != event:
                    raise ValueError("Conflicting reuse of an event_id.")
                return {"recorded": False, "event": event}
        _check_event_history(state, event)
        stamp = _timestamp()
        _ensure_candidate(state, event["bundle"], event["candidate"], stamp)
        basis = _basis(state, event["bundle"], event["candidate"]) if event["kind"] == "coverage" else None
        state["events"].append({"event": event, "recorded_at": stamp, "coverage_basis": basis})
        _write(path, state)
        return {"recorded": True, "event": event}


def _candidate_report(state: dict, item: dict) -> dict:
    bundle, candidate = item["bundle"], item["candidate"]
    sessions = _for_candidate(state["sessions"], bundle, candidate)
    receipts = [r for r in state["events"]
                if (r["event"]["bundle"], r["event"]["candidate"]) == (bundle, candidate)]
    events = [r["event"] for r in receipts]
    measured = [s for s in sessions if s["ended_at"] is not None and not s["discarded"]]
    phase_seconds = {phase: round(sum((_date(s["ended_at"]) - _date(s["started_at"])).total_seconds()
                                     for s in measured if s["phase"] == phase), 6) for phase in PHASES}
    usages = [e for e in events if e["kind"] == "usage"]
    coverage = next((r for r in reversed(receipts) if r["event"]["kind"] == "coverage"), None)
    timing = "partial" if sessions else "unknown"
    tokens = "partial" if usages else "unknown"
    if coverage:
        timing, tokens = coverage["event"]["timing"], coverage["event"]["tokens"]
        basis = _basis(state, bundle, candidate)
        work_changed = any(basis[key] != coverage["coverage_basis"][key]
                           for key in ("session_ids", "revision_keys"))
        if timing == "complete" and (work_changed or any(
                s["ended_at"] is None or s["discarded"] for s in sessions)):
            timing = "partial"
        if tokens == "complete" and (work_changed or basis["usage_event_ids"] != coverage["coverage_basis"]["usage_event_ids"]):
            tokens = "partial"
    if any(s["discarded"] for s in sessions):
        timing = "partial"
    attempts = {(e["stage"], e["attempt_id"]) for e in events if e["kind"] == "platform_attempt"}
    promotion = item["promotion"]
    baseline = promotion["baseline_revision"] if promotion else None
    revisions = {e["revision"] for e in events if e["kind"] == "revision"
                 and (baseline is None or e["revision"] > baseline)}
    outcome = next((e["outcome"] for e in reversed(events) if e["kind"] == "outcome"), "pending")
    # A subsequent observed review means a formerly retired prospect has resumed.
    if outcome == "retired_before_submission":
        last_retirement = max(i for i, e in enumerate(events) if e["kind"] == "outcome")
        if any(e["kind"] == "platform_attempt" and e["stage"] == "review" for e in events[last_retirement + 1:]):
            outcome = "pending"
    return {"bundle": bundle, "candidate": candidate,
            "qid": promotion["qid"] if promotion else None,
            "slot": promotion["slot"] if promotion else None, "baseline_revision": baseline,
            "authoring_seconds": round(sum(phase_seconds.values()), 6), "phase_seconds": phase_seconds,
            "measured_sessions": len(measured), "discarded_sessions": sum(s["discarded"] for s in sessions),
            "open_sessions": sum(s["ended_at"] is None for s in sessions),
            "reported_tokens": sum(e["total_tokens"] for e in usages) if usages else None,
            "timing_coverage": timing, "token_coverage": tokens,
            "platform_attempts": len(attempts),
            "platform_stage_attempts": {stage: sum(s == stage for s, _ in attempts) for stage in STAGES},
            "revision_rounds": len(revisions), "outcome": outcome}


def _aggregate(rows: list[dict]) -> dict:
    def coverage(field: str) -> str:
        values = [row[field] for row in rows]
        if values and all(value == "complete" for value in values):
            return "complete"
        return "unknown" if not values or all(value == "unknown" for value in values) else "partial"

    tokens = [r["reported_tokens"] for r in rows if r["reported_tokens"] is not None]
    return {"authoring_seconds": round(sum(r["authoring_seconds"] for r in rows), 6),
            "phase_seconds": {p: round(sum(r["phase_seconds"][p] for r in rows), 6) for p in PHASES},
            "measured_sessions": sum(r["measured_sessions"] for r in rows),
            "discarded_sessions": sum(r["discarded_sessions"] for r in rows),
            "open_sessions": sum(r["open_sessions"] for r in rows),
            "reported_tokens": sum(tokens) if tokens else None,
            "timing_coverage": coverage("timing_coverage"), "token_coverage": coverage("token_coverage"),
            "platform_attempts": sum(r["platform_attempts"] for r in rows),
            "platform_stage_attempts": {s: sum(r["platform_stage_attempts"][s] for r in rows) for s in STAGES},
            "revision_rounds": sum(r["revision_rounds"] for r in rows)}


def report(ledger: Path = DEFAULT_LEDGER) -> dict:
    """Read measured facts only; no timer, question, preflight, or model is run."""
    state = _read(Path(ledger).absolute())
    rows = [_candidate_report(state, item) for item in state["candidates"]]
    enrolled = sorted((r for r in rows if r["slot"] is not None), key=lambda r: r["slot"])
    unpromoted = sorted((r for r in rows if r["slot"] is None), key=lambda r: (r["bundle"], r["candidate"]))
    trial = _aggregate(enrolled)
    trial.update({"enrolled": len(enrolled), "target": TRIAL_SIZE,
                  "accepted": sum(r["outcome"] == "accepted" for r in enrolled),
                  "settled": sum(r["outcome"] != "pending" for r in enrolled)})
    reasons = []
    if len(enrolled) != TRIAL_SIZE:
        reasons.append("The five-candidate cohort is not fully enrolled.")
    if trial["timing_coverage"] != "complete":
        reasons.append("Authoring timing coverage is not complete for every enrolled candidate.")
    if trial["settled"] != TRIAL_SIZE:
        reasons.append("Not all five enrolled candidates have an explicit settled outcome.")
    if trial["authoring_seconds"] <= 0:
        reasons.append("The measured authoring denominator must be positive.")
    trial["rate_unavailable_reasons"] = reasons
    trial["accepted_per_authoring_hour"] = (trial["accepted"] * 3600 / trial["authoring_seconds"]
                                             if not reasons else None)

    def largest(values: dict) -> list[str]:
        maximum = max(values.values(), default=0)
        return [key for key, value in values.items() if maximum > 0 and value == maximum]

    return {"measurement_note": "Durations and tokens are known measured sums, not estimates of unmeasured work. "
                                "Open/discarded intervals are excluded. Unpromoted work is outside the trial. "
                                "Coverage and outcome records are supplied observations, not validation or acceptance certification.",
            "candidates": enrolled, "unpromoted_candidates": unpromoted, "trial": trial,
            "unpromoted": _aggregate(unpromoted),
            "active_session": next((s for s in state["sessions"] if s["ended_at"] is None), None),
            "largest_measured": {"phases": largest(trial["phase_seconds"]),
                                 "platform_stages": largest(trial["platform_stage_attempts"]),
                                 "revision_work": {"authoring_seconds": trial["phase_seconds"]["revision"],
                                                   "revision_rounds": trial["revision_rounds"]}}}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "start", "stop", "promote", "record", "report"):
        sub = commands.add_parser(name)
        # Permit --ledger before or after the command without overriding a supplied path.
        sub.add_argument("--ledger", type=Path, default=argparse.SUPPRESS)
        if name in ("start", "promote"):
            sub.add_argument("--bundle", required=True)
            sub.add_argument("--candidate", required=True)
        if name == "start":
            sub.add_argument("--phase", required=True, choices=PHASES)
        elif name == "stop":
            sub.add_argument("--session", required=True)
            sub.add_argument("--discard", action="store_true")
        elif name == "promote":
            sub.add_argument("--q", required=True)
            sub.add_argument("--revision", type=int, default=0)
        elif name == "record":
            sub.add_argument("--event", required=True, type=Path, help="One supplied event as JSON.")
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            result = init(args.ledger)
        elif args.command == "start":
            result = start(args.ledger, args.bundle, args.candidate, args.phase)
        elif args.command == "stop":
            result = stop(args.ledger, args.session, args.discard)
        elif args.command == "promote":
            result = promote(args.ledger, args.bundle, args.candidate, args.q, args.revision)
        elif args.command == "record":
            event = json.loads(args.event.read_text(encoding="utf-8"), parse_constant=_no_constant)
            result = record(args.ledger, event)
        else:
            result = report(args.ledger)
    except (ValueError, OSError) as exc:
        print(f"Efficiency ledger error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
