"""Form reasoning-check emulation v2: v1's number rule plus result verification.

A result straight after "=" is exempt only if the a-op-b just before it recomputes to within
REL_TOL (relative). The form shows one flag per step, so only the first flag per step prints.
usage: python form_check_v2.py <bundle_dir> <reasoning.txt> DocN=Dnn [...]
"""
import json, re, sys
from pathlib import Path

REL_TOL = 0.001
bundle = Path(sys.argv[1]); reasoning = Path(sys.argv[2]).read_text(encoding="utf-8")
doc_map = dict(a.split("=", 1) for a in sys.argv[3:])
manifest = json.loads((bundle / "text" / "manifest.json").read_text(encoding="utf-8"))
docs = {int(k[3:]): (bundle / manifest[v]["source"]).read_text(encoding="utf-8") for k, v in doc_map.items()}
N = r"\d[\d,]*(?:\.\d+)?%?"
NUM = re.compile(r"(?<![\w.,])" + N)
CALC = re.compile(r"(" + N + r")\s*(of|[-+/x*])\s*(" + N + r")[^=\d]*=\s*(" + N + r")")
val = lambda s: float(s.rstrip("%").replace(",", ""))

def checked_results(body):
    ok, bad = set(), {}
    for m in CALC.finditer(body):
        a, op, b, r = m.groups()
        x, y = val(a), val(b)
        exact = {"of": x / 100 * y if a.endswith("%") else x * y, "-": x - y, "+": x + y,
                 "*": x * y, "x": x * y, "/": x / y * (100 if r.endswith("%") else 1)}[op]
        err = abs(val(r) - exact) / abs(exact)
        (ok.add(r) if err <= REL_TOL else bad.__setitem__(r, f"{exact:.4f}, off {err:.3%}"))
    plain = {m.rstrip(",.") for m in re.findall(r"=\s*(" + N + r")", body)}
    return (plain - set(bad)) | ok, bad

earlier = set()
for block in [b.strip() for b in re.split(r"\n\s*\n", reasoning) if b.strip()]:
    label = (re.match(r"(Step \d+|Decoy)", block) or [block[:12]])[0]
    cited = sorted({int(n) for n in re.findall(r"\bDocs? (\d+)", block)} |
                   {int(n) for n in re.findall(r"\band (\d+)\b", block.split(":", 1)[0])})
    body = re.sub(r"\b(?:Step|Docs?) \d+", " ", block)
    body = re.sub(r"\band \d+\b", " ", body) if cited else body
    results, bad = checked_results(body)
    for raw in NUM.findall(body):
        num = raw.rstrip(",.")
        if num in results:
            continue
        pool = [docs[d] for d in cited] if cited else list(docs.values())
        if any(num in t for t in pool) or num in earlier:
            continue
        why = f"  [result recomputes to {bad[num]}]" if num in bad else ""
        names = " and ".join(map(str, cited))
        print(f"{label}: Doc{'s' if len(cited) > 1 else ''} {names} don't mention {num}.{why}")
        break
    earlier |= results
