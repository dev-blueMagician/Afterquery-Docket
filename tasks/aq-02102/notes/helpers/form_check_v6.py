"""Form reasoning-check emulation v6 (aq-02102, 2026-10-08), from the aq-01937 copy of v5.

New in v6, from the form flag on aq-02102 q01 rev 1 ("Step 10: Doc 4 doesn't mention 112. Check the document
number."): a step that cites exactly one document accepts only numbers that document prints (plus the step's own
verified "=" result); an earlier step's result does not count there. In the same paste, steps citing "Doc 2 and
Doc 4" used the same earlier results (112, 117) without a flag, and so did aq-00949 q05 rev 0 Step 3 ("Doc 1 and
Doc 7"). Uncited steps keep v5's rule (earlier results allowed). One observation; treat it as a working rule.

aq-01937 copy (2026-10-08): the first operand may carry a unary minus ("-66 / 401 = -16.5%"), as mathjs
parses it; otherwise unchanged from tasks/aq-01543/notes/helpers/form_check_v5.py.

Form reasoning-check emulation v5 (2026-10-08, after the form flagged q01 rev 7 Step 6 and q03 rev 3 Step 6).

v4 let a rounded "a% of b" result pass. The form then flagged "56.2% of 37,963 GWh = 21,335.2 GWh" (q01 rev 7)
and "75.1% of 44,303 GWh = 33,271.6 GWh" (q03 rev 3) while it kept passing q01 Step 3's
"41.6% of 37,963 GWh = 15,792.6 GWh" (five pastes). No tolerance separates them (21,335.2 is the closer one), so
the form does not evaluate "of" at all. mathjs, whose percent rule reproduces the q01 rev 3-5 flags
(parse.js parseAddSubtract: "a - b%" is a - a*b%), has no "of" operator. v5 encodes:
- One calculation per step, the first "a op b = r" with op + - * / and no words or brackets between the
  operands and "=" (units go after the result). "%" operands follow mathjs: "x%" is x/100, and "a + b%" /
  "a - b%" mean a + a*b% / a - a*b%.
- A result written with "%" passes when the value x 100 rounds to it; any other result must equal the value
  (relative 1e-9): "6,536 / 717 = 9.116" fails.
- Every other number must be in a cited document (substring, or the same significant digits at another scale:
  "28,460" against Doc 1's "28,46"; Doc 16's "44 303" is the two numbers 44 and 303), or be an earlier "=" token
  (same token, "%" included; a flagged result still counts as earlier).
- "a% of b = c" passes only when one cited document prints both "a%" and b and c is a x b / 100 rounded to c's
  decimals (q01 Step 3: Doc 1 prints "41.6%" and "37,963"). Inputs from two documents fail (q01 rev 7: Doc 2
  prints "56.2%"; Doc 1 prints 37,963 and "$56.2 million", which did not help), and so does a derived base
  (q03 rev 3: Doc 16 prints "75.1 %" and "44 303", not 44,303).
- A paragraph without "Step N" (a Decoy line) belongs to the step above it. One flag per step: the first.
usage: python form_check_v5.py <bundle_dir> <reasoning.txt> DocN=Dnn [...]
"""
import json
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

TOKEN = re.compile(r"(?<![\w.,])-?\d{1,3}(?:,\d{3})+(?:\.\d+)?%?(?![\d,])|(?<![\w.,])-?\d+(?:[.,]\d+)?%?(?!\d)")
OPERAND = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|\d+(?:\.\d+)?%?"
CALC = re.compile(r"(?<![\w.,%)(])(-?(?:" + OPERAND + r"))\s*([-+*/−])\s*(" + OPERAND + r")\s*=\s*(-?(?:" + OPERAND + r"))")
PERCENT_OF = re.compile(r"(?<![\w.,])(\d+(?:\.\d+)?)%\s+of\s+(" + OPERAND + r")(?:\s*[A-Za-z]+)?\s*=\s*(" + OPERAND + r")")


def dec(token: str) -> Decimal:
    """'21,335.206' -> 21335.206; a lone comma before 1-2 or 4+ digits is a decimal comma: '28,46' -> 28.46."""
    t = token.rstrip("%")
    if re.fullmatch(r"-?\d{1,3}(?:,\d{3})+(?:\.\d+)?", t):
        return Decimal(t.replace(",", ""))
    return Decimal(t.replace(",", "."))


def places(token: str) -> int:
    t = token.rstrip("%")
    return len(t.split(".")[1]) if "." in t else 0


def evaluate(a: str, op: str, b: str):
    """mathjs value of 'a op b' (floats), or None."""
    x = float(dec(a)) / (100 if a.endswith("%") else 1)
    y = float(dec(b)) / (100 if b.endswith("%") else 1)
    if op in "+-−" and b.endswith("%"):
        y = x * y
    if op in "-−":
        return x - y
    if op == "+":
        return x + y
    if op == "*":
        return x * y
    return x / y if y else None


def result_ok(value, r: str) -> bool:
    if value is None:
        return False
    if r.endswith("%"):
        q = Decimal(1).scaleb(-places(r))
        return Decimal(repr(value * 100)).quantize(q, ROUND_HALF_UP) == dec(r)
    w = float(dec(r))
    return abs(value - w) <= 1e-9 * max(1.0, abs(w))


DOC_NUMBER = re.compile(r"(?<![\w.,])\d{1,3}(?:,\d{3})+(?:\.\d+)?(?![\d,])|(?<![\w.,])\d+(?:[.,]\d+)?(?![\d])")
SCALES = [Decimal(1000) ** k for k in range(-3, 4)]


def doc_values(text: str) -> set:
    """Numbers a document prints, by value: '37,963' -> 37963; a lone comma before 1-2 or 4+ digits is a decimal
    comma ('28,46' -> 28.46, '3,3264' -> 3.3264); '44 303' is the two numbers 44 and 303."""
    values = set()
    for t in DOC_NUMBER.findall(text):
        if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", t):
            values.add(Decimal(t.replace(",", "")))
        else:
            values.add(Decimal(t.replace(",", ".")))
    return values


def mentioned(tok: str, cited, doc_vals) -> bool:
    """A step number is mentioned when a cited document prints the same value; a number without "%" may also be
    a printed value times a power of 1,000 (unit conversions: '28,460' GWh against Doc 1's '28,46' TWh). A
    factor of 10 does not count (aq-00949 q04: '53.2%' was flagged although Doc 7 prints '532')."""
    v = abs(dec(tok))
    scales = [Decimal(1)] if tok.endswith("%") else SCALES
    return any((v / s) in doc_vals[d] for d in cited for s in scales)


def check(reasoning: str, docs: dict) -> list:
    doc_vals = {n: doc_values(text) for n, text in docs.items()}
    steps = []
    for line in [ln.strip() for ln in reasoning.splitlines() if ln.strip()]:
        if re.match(r"(?:Step\s+)?\d+[.:)]\s", line) or not steps:
            steps.append(line)
        else:
            steps[-1] += "\n" + line
    messages, earlier = [], set()
    for step in steps:
        number = re.match(r"(?:Step\s+)?(\d+)", step)
        label = f"Step {number.group(1)}" if number else step[:10]
        head = re.split(r":", step, maxsplit=1)[0]
        cited = list(dict.fromkeys(int(n) for n in re.findall(r"\bDocs? (\d+)", head)))
        body = re.sub(r"\b(?:Step|Docs?) \d+|^\d+[.:)]", " ", step)
        verified, results = set(), []
        first_eq = body.find("=")
        calc = next((m for m in CALC.finditer(body) if m.start(4) > first_eq >= m.end(3)), None)
        if calc and result_ok(evaluate(*calc.group(1, 2, 3)), calc.group(4)):
            verified.add(calc.start(4))
        for m in PERCENT_OF.finditer(body):
            a, b, c = m.groups()
            same_doc = any(re.search(r"(?<![\d.,])" + re.escape(a) + r"%", docs[d])
                           and re.search(r"(?<![\d.,])" + re.escape(b) + r"(?![\d]|[.,]\d)", docs[d]) for d in cited)
            value = dec(a) / 100 * dec(b)
            if same_doc and value.quantize(Decimal(1).scaleb(-places(c)), ROUND_HALF_UP) == dec(c):
                verified.add(m.start(3))
        for m in re.finditer(r"=\s*(-?(?:" + OPERAND + r"))", body):
            results.append(m.group(1))
        flagged = None
        for m in TOKEN.finditer(body):
            tok = m.group(0)
            earlier_ok = len(cited) != 1  # v6: one-document steps do not accept earlier results
            if m.start() in verified or (earlier_ok and tok in earlier) or mentioned(tok, cited, doc_vals):
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
                 for k, v in (a.split("=", 1) for a in sys.argv[3:])}
    for line in check(reasoning_text, doc_texts):
        print(line)
