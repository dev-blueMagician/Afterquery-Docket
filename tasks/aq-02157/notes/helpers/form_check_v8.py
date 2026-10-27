"""SUPERSEDED by form_check_v9.py (2026-10-08): q01 rev 3's Steps 1-2 passed live, so the bulleted-list blind spot below
is refuted; v9 also stores a result written "= r per cent" as "r%" (q01 rev 3's Step 13 flag on 15.6).

Form reasoning-check emulation v8 (aq-02157, 2026-10-08), from aq-02102's v6 (v7's comma/currency rules dropped).

Model fitted to every recorded live result (aq-02157 q01 rev 2 and q04 revs 0-1, aq-02102 q01 rev 1, aq-01543 q01,
aq-01960 q02): the checker uses the task page's Doc numbering; it does not read document lines that start with "-"
(bulleted list items: "-  14.8% in Scotland" was "not mentioned" in Doc 3) nor text far into long documents (Doc 2
"£8.46" at character 80,370 and Doc 4 "122." / "£262.90" at about 84,000 were "not mentioned"; numbers up to 19,581
were read; the cutoff lies somewhere between). A step citing two or more documents accepts any number already
mentioned in an earlier step as the identical string (q04 rev 1 Steps 3 and 5 reused "347.86" and "8.46" from Steps
1-2; q01's "13.8" after an earlier "13.8%" was flagged); a step citing one document accepts none (aq-02102 Step 10).
Glued commas ("paragraph 3.7,", "= 1,295,") and currency signs ("$3.15") passed live, so v7's rules for them are gone.
usage: python form_check_v8.py <bundle_dir> <reasoning.txt> DocN=Dnn [...] [--hide-lists] [--truncate N]
Defaults: --hide-lists on, --truncate 60000 (an assumption inside the observed 19,581-80,370 range).
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
        results.extend(m.group(0) for m in TOKEN.finditer(body))  # v8: every earlier mention, as the same string
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
    hide = "--no-hide-lists" not in args
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
