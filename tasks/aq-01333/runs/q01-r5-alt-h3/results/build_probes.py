"""Build removal-probe packets for aq-01333 q01 rev 5 from the frozen rev 5 solver-1 packet.

solver-1: every document except D01 (Doc 4, Q1 FY26 release); solver-2: every document except D05
(Doc 6, Q3 FY26 release). Remaining ids are renumbered contiguously (text header line and manifest
keys rewritten); docs/ bytes and the rest of each text file stay byte-identical; question.txt is a
byte copy. Then the run is bound to the read guard with docket_agent.bind_scope.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(r"D:\Agents\Docket")
sys.path.insert(0, str(ROOT / "tools"))
import docket_agent  # noqa: E402

SLUG = "aq-01333"
RUN = "q01-r5-alt-h3"
SRC = ROOT / "tasks" / SLUG / "runs" / "q01-r5-v2-f6b3318d49235652e301180a068020df2e8835966fcbc2df3c8dfaaa84710c1c" / "solver-1"
DEST = ROOT / "tasks" / SLUG / "runs" / RUN
PLAN = {"solver-1": "D01", "solver-2": "D05"}

if DEST.exists():
    raise SystemExit(f"{DEST} already exists; not overwriting")

manifest = json.loads((SRC / "text" / "manifest.json").read_bytes())
for packet, removed in PLAN.items():
    out = DEST / packet
    (out / "docs").mkdir(parents=True)
    (out / "text").mkdir(parents=True)
    kept = [d for d in sorted(manifest) if d != removed]
    new_manifest = {}
    for n, old in enumerate(kept, 1):
        new = f"D{n:02d}"
        entry = manifest[old]
        new_manifest[new] = entry
        src_doc = SRC / entry["source"]
        shutil.copyfile(src_doc, out / entry["source"])
        data = (SRC / "text" / f"{old}.txt").read_bytes()
        head, sep, rest = data.partition(b"\n")
        expected = f"# {old} | {entry['source']}".encode("utf-8")
        if head.rstrip(b"\r") != expected:
            raise SystemExit(f"unexpected header in {old}.txt: {head[:120]!r}")
        if old.encode() in rest:
            raise SystemExit(f"{old} appears inside the body of {old}.txt; renumbering would leave it")
        new_head = head.replace(f"# {old} |".encode(), f"# {new} |".encode(), 1)
        (out / "text" / f"{new}.txt").write_bytes(new_head + sep + rest)
        print(f"{packet}: {old} -> {new}  {entry['source'].split('/')[-1]}")
    (out / "text" / "manifest.json").write_bytes(
        (json.dumps(new_manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    shutil.copyfile(SRC / "question.txt", out / "question.txt")
    removed_src = manifest[removed]["source"].split("/")[-1]
    print(f"{packet}: left out {removed} ({removed_src})")

(DEST / "results").mkdir()
entries = docket_agent.bind_scope(ROOT, SLUG, RUN)
print("bound runs now:", len(entries))
for e in entries:
    print("  ", e["bundle"], e["run"], e["bound_at"])
