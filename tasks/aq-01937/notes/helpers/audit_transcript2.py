"""Audit a blind role's subagent transcript: every tool call must stay inside its packet.

usage: python audit_transcript2.py <agent_id> <allowed_packet_dir | NONE>
Like aq-01543's audit_transcript.py, plus one benign case made explicit: a Read of the harness's
persisted overflow file tool-results/<tool_use_id>.txt is accepted when that id is one of this
same agent's own Grep/Glob calls whose path is inside the packet (the file then holds only
packet-derived search output). Every such case is listed. Exit 1 on any other violation.
"""
import json
import re
import sys
from pathlib import Path, PureWindowsPath

PROJECT = Path("C:/Users/Administrator/.claude/projects/d--Projects-Projects-AfterQuery-Docket-10-7")
agent, allowed = sys.argv[1], sys.argv[2]
allowed_norm = None if allowed == "NONE" else str(PureWindowsPath(allowed)).lower().rstrip("\\")
found = sorted(PROJECT.glob(f"*/subagents/agent-{agent}.jsonl"))
if len(found) != 1:
    raise SystemExit(f"expected one transcript for agent {agent}, found {len(found)}")
blocks = []
for line in found[0].read_bytes().decode("utf-8").splitlines():
    try:
        rec = json.loads(line)
    except ValueError:
        continue
    msg = rec.get("message") or {}
    content = msg.get("content") if isinstance(msg, dict) else None
    if isinstance(content, list):
        blocks += [b for b in content if isinstance(b, dict) and b.get("type") == "tool_use"]


def inside(value: str) -> bool:
    norm = str(PureWindowsPath(value)).lower().rstrip("\\")
    return allowed_norm is not None and (norm == allowed_norm or norm.startswith(allowed_norm + "\\"))


own_search_ids = {b.get("id", "") for b in blocks
                  if b.get("name") in ("Grep", "Glob") and inside((b.get("input") or {}).get("path", ""))}
calls, violations, benign, paths = [], [], [], set()
for b in blocks:
    name, inp = b.get("name"), b.get("input") or {}
    calls.append(name)
    if name == "SubagentHandback":
        continue
    if allowed_norm is None:
        violations.append(f"{name} {json.dumps(inp)[:200]}")
        continue
    for key in ("file_path", "path"):
        value = inp.get(key)
        if isinstance(value, str) and value:
            paths.add(value)
            if inside(value):
                continue
            m = re.search(r"tool-results[\\/](toolu_[A-Za-z0-9]+)\.txt$", value)
            if name == "Read" and m and m.group(1) in own_search_ids:
                benign.append(f"Read of own overflowed search output {m.group(1)}")
                continue
            violations.append(f"{name} {key}={value}")
    if name in ("Grep", "Glob") and not inp.get("path"):
        violations.append(f"{name} without explicit path: {json.dumps(inp)[:200]}")
    if name not in ("Read", "Grep", "Glob"):
        violations.append(f"unexpected tool {name}")
print(f"agent {agent}: {len(calls)} tool calls {sorted(set(calls))}")
for item in benign:
    print("  benign:", item)
if violations:
    print("VIOLATIONS:")
    for v in violations:
        print("  ", v)
    sys.exit(1)
print("clean: all tool paths inside the packet" + (" (plus own overflow reads)" if benign else ""))
