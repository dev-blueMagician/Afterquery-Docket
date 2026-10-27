"""Print exact spans (repr) around literal search strings in originals and text/ for quoting.

usage: python find_quotes.py <bundle_dir> <file> <literal> [<literal> ...]
<file> is a path relative to the bundle (docs/... or text/Dnn.txt). Each literal is searched
verbatim; the line holding each hit is printed with repr() so tabs and non-ASCII are visible.
"""
import sys
from pathlib import Path

bundle = Path(sys.argv[1])
text = (bundle / sys.argv[2]).read_bytes().decode("utf-8")
for literal in sys.argv[3:]:
    start = 0
    hits = 0
    while True:
        i = text.find(literal, start)
        if i < 0:
            break
        hits += 1
        line_start = text.rfind("\n", 0, i) + 1
        line_end = text.find("\n", i)
        line_no = text.count("\n", 0, i) + 1
        line = text[line_start:line_end if line_end >= 0 else len(text)]
        print(f"L{line_no}: {line[:400]!r}")
        start = i + 1
    if not hits:
        print(f"NOT FOUND: {literal!r}")
