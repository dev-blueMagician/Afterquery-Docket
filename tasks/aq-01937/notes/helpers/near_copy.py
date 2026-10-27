"""Compare one question's wording with every workspace question (Original question near-copy risk).

usage: python near_copy.py <workspace_root> <question_file>
Prints the five highest difflib token ratios and the longest shared token run for each.
Restructure when a ratio exceeds about 0.4, a shared run is 6+ tokens, or a closing sentence repeats.
"""
import difflib
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
target = Path(sys.argv[2]).resolve()


def question_of(path: Path) -> str:
    text = path.read_bytes().decode("utf-8", "replace")
    match = re.search(r"^## Question\s*\n(.*?)(?=^## )", text, re.S | re.M)
    return match.group(1).strip() if match else ""


def toks(text: str) -> list[str]:
    return re.findall(r"[a-z0-9$%.,']+", text.lower())


mine = toks(question_of(target))
rows = []
for path in root.glob("tasks/*/questions/q*.md"):
    if path.resolve() == target:
        continue
    other = toks(question_of(path))
    if not other:
        continue
    sm = difflib.SequenceMatcher(None, mine, other)
    run = max((b.size for b in sm.get_matching_blocks()), default=0)
    rows.append((sm.ratio(), run, str(path.relative_to(root))))
for ratio, run, name in sorted(rows, reverse=True)[:5]:
    print(f"{ratio:.2f} run={run} {name}")
print("longest runs:", sorted(rows, key=lambda r: -r[1])[:3])
