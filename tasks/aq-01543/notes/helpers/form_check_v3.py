"""Form reasoning-check emulation v3: v2 plus percentages read as fractions.

Working rule (aq-01543 q01, form messages on rev 2, 3 and 4, 2026-10-08): the form reads "56.2%" as 0.562.
A result straight after "=" is exempt only if the a-op-b just before it recomputes to that result within
REL_TOL, with every "%" operand and "%" result divided by 100. So "41.6% of 37,963 = 15,792.6" (0.416 x
37,963) and "12,667.4 / 37,963 = 33.37%" (0.3337) pass, while "56.2% - 33.37% = 22.83" fails (0.2283 is not
22.83) and "56.2% - 33.37% = 22.83%" passes. The form shows one flag per step: only the first prints.
usage: python form_check_v3.py <bundle_dir> <reasoning.txt> DocN=Dnn [...]
"""
import json
import re
import sys
from pathlib import Path

REL_TOL = 0.001
bundle = Path(sys.argv[1])
reasoning = Path(sys.argv[2]).read_text(encoding="utf-8")
doc_map = dict(a.split("=", 1) for a in sys.argv[3:])
manifest = json.loads((bundle / "text" / "manifest.json").read_text(encoding="utf-8"))
docs = {int(k[3:]): (bundle / manifest[v]["source"]).read_text(encoding="utf-8") for k, v in doc_map.items()}
N = r"-?\d[\d,]*(?:\.\d+)?%?"
NUM = re.compile(r"(?<![\w.,])" + N)
CALC = re.compile(r"(" + N + r")\s*(of|[-+/x*])\s*(" + N + r")[^=\d]*=\s*(" + N + r")")


def val(s: str) -> float:
    x = float(s.rstrip("%").replace(",", ""))
    return x / 100 if s.endswith("%") else x


def checked_results(body):
    ok, bad = set(), {}
    for m in CALC.finditer(body):
        a, op, b, r = m.groups()
        x, y = val(a), val(b)
        exact = {"of": x * y, "-": x - y, "+": x + y, "*": x * y, "x": x * y, "/": x / y}[op]
        err = abs(val(r) - exact) / abs(exact) if exact else abs(val(r))
        if err <= REL_TOL:
            ok.add(r)
        else:
            bad[r] = f"{exact:.6g}, off {err:.3%}"
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
