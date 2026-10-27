"""PreToolUse guard for the blind-solver agent: it may read only a bundle's documents.

Hooked from blind-solver and shortcut-auditor as
    python "$CLAUDE_PROJECT_DIR/tools/agent_scope.py" blind-solver
Run tools/docket_agent.py prepare with --local-checks for an optional diagnostic: it adds its
bundle/run to .claude/solver-scope.json. Default platform preparation does not bind a scope.
The binding may hold several active runs (schema 2) so that concurrent sessions do not evict
each other's solvers; the legacy single-run form (schema 1) is still honoured.
Allows only prepared packet documents. Closed-book agents cannot use tools.
This guards tool paths; fresh agent context is also required to prevent prompt leakage.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path, PurePath, PureWindowsPath

ROOT = Path(__file__).resolve().parent.parent
READABLE = {"text", "docs"}
TOOLS = {"Read", "Grep", "Glob"}


def safe_name(value: object) -> bool:
    return (isinstance(value, str) and bool(value) and
            all(char.isalnum() or char in "-_" for char in value))


def bindings(scope: object) -> list[tuple[str, str]]:
    """Active (bundle, run) pairs from a schema 1 or schema 2 binding; raise if malformed."""
    if not isinstance(scope, dict):
        raise ValueError("binding is not an object")
    entries = scope["runs"] if "runs" in scope else [scope]
    if not isinstance(entries, list) or not entries:
        raise ValueError("no active runs")
    pairs = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("run entry is not an object")
        slug, run = entry["bundle"], entry["run"]
        if not (safe_name(slug) and safe_name(run)):
            raise ValueError("unsafe bundle or run binding")
        pairs.append((slug, run))
    return pairs


def check(role: str, data: dict, root: Path = ROOT) -> str | None:
    """Return a denial reason, or None to allow."""
    if role == "closed-book-solver":
        return "The closed-book solver has no document, search, memory or execution access."
    if role != "blind-solver":
        return f"agent_scope.py has no rule for role '{role}'."
    if not isinstance(data, dict) or not isinstance(data.get("tool_input"), dict):
        return "Invalid scope request: expected an object with tool_input fields."
    tool = data.get("tool_name")
    if tool not in TOOLS:
        return "The blind solver may only Read, Grep and Glob the bundle's documents."
    try:
        active = bindings(json.loads((root / ".claude" / "solver-scope.json").read_bytes()))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        return f"No valid solver scope: run docket_agent.py prepare with --local-checks first ({error})."
    args = data["tool_input"]
    pattern = args.get("pattern", "") if tool == "Glob" else args.get("glob", "")
    if not isinstance(pattern, str):
        return "Invalid glob: expected a string."
    patterns = (PurePath(pattern), PureWindowsPath(pattern))
    if pattern and any(p.drive or p.root or ".." in p.parts for p in patterns):
        return "Use a relative glob without '..' inside tasks/<slug>/text/ or docs/."
    raw = args.get("file_path") or args.get("path")
    if not isinstance(raw, str) or not raw:
        return "Pass an explicit path: tasks/<slug>/text/ (or docs/), not the workspace root."
    path = (Path(data.get("cwd") or root) / raw).resolve()
    try:
        parts = path.relative_to((root / "tasks").resolve()).parts
    except ValueError:
        parts = ()
    if (len(parts) >= 5 and (parts[0], parts[2]) in active and parts[1] == "runs"
            and parts[3] in {"solver-1", "solver-2", "shortcut"}
            and parts[4].lower() in READABLE):
        return None
    bound = ", ".join(f"{slug}/{run}" for slug, run in active)
    return f"Outside the active bundle/run documents: {raw}. Bound to {bound}."


def main() -> int:
    try:
        reason = check(sys.argv[1], json.loads(sys.stdin.read()))
    except (ValueError, OSError, KeyError, IndexError, TypeError, AttributeError) as error:
        reason = f"Scope check failed closed: {error}"
    if reason:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                          "permissionDecision": "deny", "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
