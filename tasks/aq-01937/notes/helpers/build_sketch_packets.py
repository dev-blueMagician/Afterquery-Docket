"""Build document-only sketch packets (no question file, no key) for aq-01937 sketch screens.

usage: python build_sketch_packets.py <bundle_dir> <run_name>
Creates runs/<run_name>/{solver-1,solver-2,shortcut}/ with byte copies of docs/ and text/
(manifest included), then binds the run to the shared read guard. The caller passes each
question in the solver prompt; nothing else about the candidate is written into the run.
"""
import json
import shutil
import sys
from pathlib import Path

bundle = Path(sys.argv[1]).resolve()
run_name = sys.argv[2]
root = bundle.parent.parent
sys.path.insert(0, str(root / "tools"))
import docket_agent  # noqa: E402

run = bundle / "runs" / run_name
if run.exists():
    raise SystemExit(f"run exists: {run}")
for slot in ("solver-1", "solver-2", "shortcut"):
    packet = run / slot
    for folder in ("docs", "text"):
        src = bundle / folder
        dst = packet / folder
        dst.mkdir(parents=True)
        for path in sorted(src.iterdir()):
            if path.is_file() and path.name != ".gitkeep":
                shutil.copyfile(path, dst / path.name)
bound = docket_agent.bind_scope(root, bundle.name, run_name)
print(json.dumps({"run": str(run), "bound_first": [f"{e['bundle']}/{e['run']}" for e in bound[:3]],
                  "bound_count": len(bound)}, indent=2))
