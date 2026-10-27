"""Form reasoning-check emulation v10 (aq-02157, 2026-10-09), from v9 after q01 rev 4's live result.

Change from v9 (user screenshot runs/q01-r4-form-2026-10-09/form-screenshot-6.png, rev 4 as the user reworded it, Steps 8,
10 and 12 reading "The rate for ... in 2030 in %: a op b = r (...)"): 15.6 was flagged again ("Step 5: Docs 3 and 1 don't
mention 15.6."), so a result is typed as a percentage, and stored as "r%", also when the step describes it as one before
the expression ("in %:", "in per cent:"), not only when "per cent" or "%" follows it. A "%" attached to an operand does
not type the result (aq-01960 q02: "3.15 x 60.7% = 1.91205" was reused as 1.91205 unflagged). Same lesson as aq-01543
q01 revs 2-5: do not subtract percentage-typed results; restructure so reused results are plain or "percentage points".
Not explained: the label "Step 5" (no step so numbered held 15.6; the full pasted text was not captured).

v9 notes, kept:
Changes from v8, both from the user's screenshot of q01 rev 3 (runs/q01-r3-form-2026-10-08/form-screenshot-5.png),
whose only flag was "Step 13: Docs 3 and 1 don't mention 15.6.":
- Bulleted lists are read. Rev 3's Steps 1-2 passed with rates printed only in the dash-led lists of Doc 3 and Doc 1, so
  v8's list blind spot is refuted; --hide-lists is kept only to replay the refuted model.
- A result written "= r per cent" (or "= r%") is stored for later steps as "r%", so a later plain operand r does not match
  it. Results followed by other words ("= 1.6 percentage points", "= 6.9572 pounds") were reused without a flag. A
  number merely mentioned with "per cent" ("14.8 per cent" in a source-fact step) is still stored as the plain string.
Unchanged: the page's Doc numbering; deep text unread (Doc 2 "8.46" at character 80,370, Doc 4 "262.90" near 84,000;
truncation length assumed 60,000); a step citing two or more documents accepts any earlier mention as the identical
string, a step citing one document accepts none (aq-02102 Step 10).
Not explained: rev 2's flags on "14.8%" (Step 1) and "12.7%" (Step 2) and on plain 13.8, 14.8 and 14.1 (Steps 3, 4, 6)
while plain 12.7, 14.0 and 13.9 passed (Steps 3, 5, 10); the user had reworded that version and its full text was not
captured.
usage: python form_check_v10.py <bundle_dir> <reasoning.txt> DocN=Dnn [...] [--hide-lists] [--truncate N]
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
        percent_results = set()
        head_end = body.find(":")
        described = body[head_end + 1:calc.start(1)] if calc and head_end < calc.start(1) else ""
        typed = re.search(r"(?<![\d.])%|\bper\s?cent\b|\bpercent\b", described)  # v10: "in %: a op b = r"
        for m in re.finditer(r"=\s*(-?(?:" + OPERAND + r"))(\s*(?:per\s?cent\b|percent\b))?", body):
            r = m.group(1)
            if (m.group(2) or (typed and calc and m.start(1) == calc.start(4))) and not r.endswith("%"):
                percent_results.add(m.start(1))  # v9: '= 15.6 per cent' is stored as '15.6%'
                results.append(r + "%")
            else:
                results.append(r)
        results.extend(m.group(0) for m in TOKEN.finditer(body) if m.start() not in percent_results)
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


def blind(text: str, hide_lists: bool, truncate) -> str:
    if truncate:
        text = text[:truncate]
    if hide_lists:
        text = "\n".join(line for line in text.split("\n") if not line.lstrip().startswith("-"))
    return text


if __name__ == "__main__":
    args = sys.argv[1:]
    hide = "--hide-lists" in args  # v9: lists are read
    trunc = 60000
    if "--truncate" in args:
        k = args.index("--truncate")
        trunc = int(args[k + 1]) or None
        del args[k:k + 2]
    args = [a for a in args if a not in ("--hide-lists", "--no-hide-lists")]
    bundle = Path(args[0])
    reasoning_text = Path(args[1]).read_text(encoding="utf-8")
    manifest = json.loads((bundle / "text" / "manifest.json").read_text(encoding="utf-8"))
    doc_texts = {int(k[3:]): blind((bundle / manifest[v]["source"]).read_text(encoding="utf-8", errors="replace"), hide, trunc)
                 for k, v in (a.split("=", 1) for a in args[2:])}
    for line in check(reasoning_text, doc_texts):
        print(line)
