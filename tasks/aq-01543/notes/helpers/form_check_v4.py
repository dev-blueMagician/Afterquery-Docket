"""Form reasoning-check emulation v4 (2026-10-08, after the form flagged q01 rev 5, q02 rev 1 and q03 rev 1).

v3's rule (percentages as fractions) failed: the form flagged "56.2% - 33.37% = 22.83%" too. v4 encodes the
rule that fits every form message on record (q01 revs 2-5, q02 rev 1, q03 rev 1) and every accepted step:
- A number passes if a cited document mentions it (substring, or the same significant digits at another
  scale: "28,460" against Doc 1's "28,46"), if an earlier step wrote it after "=" (same token, "%" included),
  or if it is the result of the step's own calculation and that calculation checks out.
- Only simple calculations are evaluated: "a op b", and "a% of b" with the "%" attached. An identity with no
  operator ("44 303 GWh = 44.303 TWh"), a spaced "75.1 %", brackets or two operators are not.
- Percent arithmetic follows the mathjs convention: "a - b%" means a - a*b/100, so "56.2% - 33.37%" is
  0.3745, not 0.2283, and no notation of a percentage-point difference of two "%" operands checks out.
- A result written with "%" passes when the computed value x 100 rounds to it ("12,667.4 / 37,963 =
  33.37%"); so does a percent-of result ("41.6% of 37,963 = 15,792.6"). Any other result must be exact:
  "6,536 / 717 = 9.116" fails (9.11576...).
- A paragraph without "Step N" (a Decoy line) belongs to the step above it. One flag per step: the first.
usage: python form_check_v4.py <bundle_dir> <reasoning.txt> DocN=Dnn [...] [--strict]
--strict applies the alternative the q01 rev 6 review found equally consistent with the seven messages (with a
display cap of two messages): a calculation counts only straight after a colon, arithmetic is in floats, and a
result may be rounded only when written to two decimals or fewer; longer results must be float-exact.
"""
import json
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

TOKEN = re.compile(r"(?<![\w.,])-?\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|(?<![\w.,])-?\d+(?:\.\d+)?%?")
OPERAND = r"-?\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|-?\d+(?:\.\d+)?%?"
UNIT = r"(?:\s*[A-Za-z]+)?"
CALC = re.compile(r"(?<![\w.,%)])(" + OPERAND + r")" + UNIT + r"\s*(of|[-+/x*×−])\s*(" + OPERAND + r")"
                  + UNIT + r"\s*=\s*(" + OPERAND + r")")
GREEDY = re.compile(r"\d[\d,.]*\d|\d")


def dec(token: str) -> Decimal:
    return Decimal(token.rstrip("%").replace(",", ""))


def digits(text: str) -> str:
    """Significant digits: '28,460' -> '2846', '0.303' -> '303', '44 303' is two numbers."""
    return re.sub(r"\D", "", text).strip("0")


def evaluate(a: str, op: str, b: str):
    """Value of a simple calculation as the form evaluates it, or None if it does not evaluate one."""
    x, y = dec(a), dec(b)
    if op == "of":
        return x / 100 * y if a.endswith("%") and not b.endswith("%") else None
    if a.endswith("%"):
        x = x / 100
    if b.endswith("%"):
        if op in "-+−":  # mathjs: a - b% = a - a*b/100
            return x - x * y / 100 if op in "-−" else x + x * y / 100
        y = y / 100
    if op in "-−":
        return x - y
    if op == "+":
        return x + y
    if op in "x*×":
        return x * y
    return x / y if y else None


def result_ok(value, a: str, op: str, r: str, strict: bool = False) -> bool:
    if value is None:
        return False
    if strict:  # the review's alternative: float arithmetic; rounding allowed only up to two decimals
        places = len(r.rstrip("%").split(".")[1]) if "." in r else 0
        v = float(value) * (100 if r.endswith("%") else 1)
        w = float(dec(r))
        return round(v, places) == w if places <= 2 else v == w
    places = len(r.rstrip("%").split(".")[1]) if "." in r else 0
    quantum = Decimal(1).scaleb(-places)
    if r.endswith("%"):
        return (value * 100).quantize(quantum, ROUND_HALF_UP) == dec(r)
    if op == "of":
        return value.quantize(quantum, ROUND_HALF_UP) == dec(r)
    return abs(value - dec(r)) <= Decimal("1e-9") * max(Decimal(1), abs(dec(r)))


def check(reasoning: str, docs: dict, strict: bool = False) -> list:
    doc_digits = {n: {digits(t) for t in GREEDY.findall(text)} for n, text in docs.items()}
    steps = []
    for para in [p.strip() for p in re.split(r"\n\s*\n", reasoning) if p.strip()]:
        if re.match(r"Step \d+", para) or not steps:
            steps.append(para)
        else:
            steps[-1] += "\n" + para
    messages, earlier = [], set()
    for step in steps:
        label = (re.match(r"Step \d+", step) or [step[:10]])[0]
        head = re.split(r":", step, maxsplit=1)[0]
        cited = list(dict.fromkeys(int(n) for n in re.findall(r"\bDocs? (\d+)", head)))
        body = re.sub(r"\b(?:Step|Docs?) \d+", " ", step)
        verified, results = set(), []
        for m in CALC.finditer(body):
            a, op, b, r = m.groups()
            results.append(r)
            if strict and not body[:m.start()].rstrip().endswith(":"):
                continue
            if result_ok(evaluate(a, op, b), a, op, r, strict):
                verified.add((m.start(4), r))
        for m in re.finditer(r"=\s*(" + OPERAND + r")", body):
            results.append(m.group(1))
        flagged = None
        for m in TOKEN.finditer(body):
            tok = m.group(0)
            if (m.start(), tok) in verified or tok in earlier:
                continue
            plain = tok.rstrip("%")
            if any(plain in docs[d] for d in cited) or any(digits(plain) in doc_digits[d] for d in cited):
                continue
            flagged = tok
            break
        if flagged:
            names = " and ".join(map(str, cited))
            verb = "don't" if len(cited) > 1 else "doesn't"
            messages.append(f"{label}: Doc{'s' if len(cited) > 1 else ''} {names} {verb} mention {flagged}.")
        earlier |= set(results)
    return messages


if __name__ == "__main__":
    bundle = Path(sys.argv[1])
    reasoning_text = Path(sys.argv[2]).read_text(encoding="utf-8")
    manifest = json.loads((bundle / "text" / "manifest.json").read_text(encoding="utf-8"))
    doc_texts = {int(k[3:]): (bundle / manifest[v]["source"]).read_text(encoding="utf-8")
                 for k, v in (a.split("=", 1) for a in sys.argv[3:] if a != "--strict")}
    for line in check(reasoning_text, doc_texts, strict="--strict" in sys.argv):
        print(line)
