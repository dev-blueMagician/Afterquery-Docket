"""Build renumbered removal-probe packets for one aq-01937 question (copied from aq-01543 helpers).

usage: python build_probe.py <bundle_dir> <run_name> <question_file_text> <slot>=<left_out_id>[+<id>...] [...]
Each slot (solver-1, solver-2, shortcut) gets docs/ and text/ without the left-out document,
ids renumbered contiguously D01..Dnn in the original alphabetical order, the header line of each
text file rewritten to its new id, and a fresh manifest.json. Then the run is bound to the read guard.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

bundle = Path(sys.argv[1]).resolve()
run_name = sys.argv[2]
question = Path(sys.argv[3]).read_bytes()
slots = dict(arg.split("=", 1) for arg in sys.argv[4:])

root = bundle.parent.parent
sys.path.insert(0, str(root / "tools"))
import docket_agent  # noqa: E402

manifest = json.loads((bundle / "text" / "manifest.json").read_bytes())
run = bundle / "runs" / run_name
if run.exists():
    raise SystemExit(f"run exists: {run}")
run.mkdir(parents=True)
report = {}
for slot, left_out in slots.items():
    assert slot in {"solver-1", "solver-2", "shortcut"}, slot
    left_out_set = set(left_out.split("+"))
    assert left_out_set <= set(manifest), left_out
    packet = run / slot
    (packet / "docs").mkdir(parents=True)
    (packet / "text").mkdir()
    (packet / "question.txt").write_bytes(question)
    new_manifest = {}
    mapping = {}
    n = 0
    for old_id in sorted(manifest):
        if old_id in left_out_set:
            continue
        n += 1
        new_id = f"D{n:02d}"
        entry = dict(manifest[old_id])
        src = bundle / entry["source"]
        shutil.copyfile(src, packet / entry["source"])
        text = (bundle / "text" / f"{old_id}.txt").read_bytes().decode("utf-8")
        first, rest = text.split("\n", 1)
        assert first.startswith(f"# {old_id} | "), first
        text = f"# {new_id} | " + first.split(" | ", 1)[1] + "\n" + rest
        (packet / "text" / f"{new_id}.txt").write_bytes(text.encode("utf-8"))
        new_manifest[new_id] = entry
        mapping[old_id] = new_id
    (packet / "text" / "manifest.json").write_bytes(
        (json.dumps(new_manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    report[slot] = {"left_out": left_out, "documents": n, "mapping": mapping}
(run / "probe-map.json").write_bytes((json.dumps(report, indent=2) + "\n").encode("utf-8"))
bound = docket_agent.bind_scope(root, bundle.name, run_name)
print(json.dumps({"run": str(run), "slots": {k: v["left_out"] for k, v in report.items()},
                  "bound_first": [f"{e['bundle']}/{e['run']}" for e in bound[:3]]}, indent=2))
