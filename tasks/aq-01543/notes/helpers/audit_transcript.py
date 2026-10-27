"""Audit a blind role's subagent transcript: every tool call must stay inside its packet.

usage: python audit_transcript.py <agent_id> <allowed_packet_dir | NONE>
Prints tool-call counts, every distinct path/pattern used, and any violation. Exit 1 on violation.
"""
import json
import sys
from pathlib import Path, PureWindowsPath

PROJECT = Path("C:/Users/Administrator/.claude/projects/d--Projects-Projects-AfterQuery-Docket-10-7")
agent, allowed = sys.argv[1], sys.argv[2]
allowed_norm = None if allowed == "NONE" else str(PureWindowsPath(allowed)).lower().rstrip("\\")
# Any session's subagents/ folder, so the helper survives a restart (new session id).
found = sorted(PROJECT.glob(f"*/subagents/agent-{agent}.jsonl"))
if len(found) != 1:
    raise SystemExit(f"expected one transcript for agent {agent}, found {len(found)}")
path = found[0]
calls, violations, paths = [], [], set()
for line in path.read_bytes().decode("utf-8").splitlines():
    try:
        rec = json.loads(line)
    except ValueError:
        continue
    msg = rec.get("message") or {}
    content = msg.get("content") if isinstance(msg, dict) else None
    if not isinstance(content, list):
        continue
    for block in content:
        if not isinstance(block, dict) or block.get("type") != "tool_use":
            continue
        name, inp = block.get("name"), block.get("input") or {}
        calls.append(name)
        if name == "SubagentHandback":
            continue
        if allowed_norm is None:
            violations.append(f"{name} {json.dumps(inp)[:200]}")
            continue
        for key in ("file_path", "path"):
            value = inp.get(key)
            if isinstance(value, str) and value:
                norm = str(PureWindowsPath(value)).lower().rstrip("\\")
                paths.add(value)
                if not (norm == allowed_norm or norm.startswith(allowed_norm + "\\")):
                    violations.append(f"{name} {key}={value}")
        if name in ("Grep", "Glob") and not (inp.get("path")):
            violations.append(f"{name} without explicit path: {json.dumps(inp)[:200]}")
        if name not in ("Read", "Grep", "Glob"):
            violations.append(f"unexpected tool {name}")
print(f"agent {agent}: {len(calls)} tool calls {sorted(set(calls))}")
rel = sorted({p.lower().replace(allowed_norm, "<packet>") if allowed_norm else p for p in paths})
for p in rel:
    print("  ", p)
if violations:
    print("VIOLATIONS:")
    for v in violations:
        print("  ", v)
    sys.exit(1)
print("clean: all tool paths inside the packet")
