"""The task form's reasoning number check, emulated for the floor, the hand-over and the sketch screen.

Under the Step-by-step reasoning box the form reads every number in every step. When it cannot place
one it shows, in orange, "Step N: Doc X doesn't mention Y. Check the document number." or, in a step
citing no document, "Step N: Which document says Y? Add 'Doc N'." Such a line used to reveal real
reasoning mistakes, so the floor FAILs every number a rewording could fix: a wrong Doc, a result
reused in a one-document step, a restated or unexempted result. A figure the cited document really
states, in words or past the form's read depth, inside a passage quoted as evidence is an expected
false alarm instead (user, 2026-10-09, on aq-02505 q01: "this time, it is not your fault"): a WARN
to mention with the hand-over.

Rules reconstructed from the user's form screenshots (dated evidence in
.claude/memory/docket-form-automated-checks.md):
- A step cites the documents named in its head, before the first colon: "Calculation (Doc 2 and Doc 6):".
  A range is read as its first document ("Docs 10 to 13" as Doc 10, aq-01960 q02), so write "Doc N"
  for each document; the range's own numbers are not read as figures (that Step 9 passed).
- A number passes when a cited document prints it in digits within the text the form reads; when it is
  the exact result straight after "=" of the step's first bare "a op b" (a "%" result passes when it
  rounds correctly; "gross profit = 3.15 × 60.7% = 1.91205" passed, aq-01960 q02 rev 1); or, in a step
  citing two or more documents, when an earlier step wrote the identical string. A step citing one
  document accepts no earlier result (aq-02102 q01). A result typed as a percentage ("= 15.6 per cent",
  "in %: a op b = r") is stored as "15.6%" (aq-02157 q01). A second calculation in the same step is
  not evaluated (aq-00949 q03).
- A step that spells a number out loses the exemption for its calculation's result. "twelve 30-day months
  ...: 12 × 30 + 5 = 365" drew "Step 4: Docs 2 and 6 don't mention 365" (aq-02626 q03, user screenshot
  2026-10-10), and the one earlier unexplained flag was "Twelve months ended June 30, 2026: 1,942 + 1,999
  = 3,941" (aq-01321 q02 Step 9). The next step of aq-02626 q03, "365 × 3 + 1 = 1,096" with no number
  word, drew no line. So a number word of ten or more in a calculation step is a FAIL here (inferred from
  those two steps, not a stated platform rule), and a chain mixing operators is only a WARN.
- Words are not digits: list totals printed only as "One hundred and seven entities" were flagged as
  107 and 187 (aq-02505 q01), while a single digit spelled out early ("five") passed.
- Deep text: digits at characters 80,370 and about 84,000 were flagged; the deepest observed pass is
  character 19,581 (aq-02157).

This is an emulation, not the platform's code. It reproduces the recorded flags and is stricter where
the form's behaviour is unobserved: a number printed only between SAFE_DEPTH and READ_DEPTH is a WARN.
"""
from __future__ import annotations

import re
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from typing import NamedTuple

OBSERVED_PASS = 19_581  # deepest character position of a printed number the form has passed
SAFE_DEPTH = 20_000
READ_DEPTH = 60_000  # assumed read limit; the form flagged printed digits near characters 80,000 and 84,000

OPERAND = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|\d+(?:\.\d+)?%?"
TOKEN = re.compile(r"(?<![\w.,])-?\d{1,3}(?:,\d{3})+(?:\.\d+)?%?(?![\d,])|(?<![\w.,])-?\d+(?:[.,]\d+)?%?(?!\d)")
# One bare "a op b = r", or a longer chain without brackets: the form took "3.15 × 60.7% = 1.91205" and
# "1.91205 + 1.9608 + 2.03077 + 2.17074 = 8.07436" (aq-01960 q02). Groups: first operand, the rest, result.
CALC = re.compile(r"(?<![\w.,%)(])(-?(?:" + OPERAND + r"))((?:\s*[-+*/−×x]\s*(?:" + OPERAND + r"))+)\s*=\s*(-?(?:"
                  + OPERAND + r"))")
OPERATION = re.compile(r"\s*([-+*/−×x])\s*(" + OPERAND + r")")
PERCENT_OF = re.compile(r"(?<![\w.,])(\d+(?:\.\d+)?)%\s+of\s+(" + OPERAND + r")(?:\s*[A-Za-z]+)?\s*=\s*("
                        + OPERAND + r")")
DOC_NUMBER = re.compile(r"(?<![\w.,])\d{1,3}(?:,\d{3})+(?:\.\d+)?(?![\d,])|(?<![\w.,])\d+(?:[.,]\d+)?(?![\d])")
SCALES = [Decimal(1000) ** k for k in range(-3, 4)]
SMALL = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
         "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
        "ninety": 90}
SCALE_WORDS = {"hundred": 100, "thousand": 1000, "million": 10 ** 6, "billion": 10 ** 9}
_WORD = "|".join(sorted([*SMALL, *TENS, *SCALE_WORDS], key=len, reverse=True))
SPELLED = re.compile(rf"\b(?:{_WORD})(?:(?:\s+and\s+|[\s-]+)(?:{_WORD}))*\b", re.I)
# "Step 3", "Steps 2, 4 and 6", "Doc 2", "Docs 10 to 13": references, not figures.
_LIST = r"\d+(?:(?:\s*,\s*|\s+and\s+|\s+to\s+)\d+)*"
REFERENCE = re.compile(rf"\b(?:Steps?|Docs?) {_LIST}")
NEW_STEP = re.compile(r"(?:Step\s+\d+\b|\d+[.:)]\s)")


class Flag(NamedTuple):
    level: str            # FAIL: the form will flag it; WARN: printed at a depth the form may not read
    step: str             # "Step 3"
    number: str           # as written in the step
    cited: tuple          # the step's task-page Doc numbers
    form: str             # the form's own wording
    why: str              # what the local check found, and the fix


def dec(token: str) -> Decimal:
    """'21,335.206' -> 21335.206; a lone comma before 1-2 or 4+ digits is a decimal comma: '28,46' -> 28.46."""
    t = token.rstrip("%")
    if re.fullmatch(r"-?\d{1,3}(?:,\d{3})+(?:\.\d+)?", t):
        return Decimal(t.replace(",", ""))
    return Decimal(t.replace(",", "."))


def places(token: str) -> int:
    t = token.rstrip("%")
    return len(t.split(".")[1]) if "." in t else 0


def evaluate(a: str, op: str, b: str) -> float | None:
    """The value of 'a op b' as the form computes it (floats; 'b%' after + or - is a share of a)."""
    x = float(dec(a)) / (100 if a.endswith("%") else 1)
    y = float(dec(b)) / (100 if b.endswith("%") else 1)
    if op in "+-−" and b.endswith("%"):
        y = x * y
    if op in "-−":
        return x - y
    if op == "+":
        return x + y
    if op in "*×x":
        return x * y
    return x / y if y else None


def evaluate_chain(first: str, rest: str) -> float | None:
    """'a op b' as evaluate(); a longer chain of plain numbers with * and / before + and -. A chain
    holding a percentage is left unevaluated (only the two-operand percent rule is observed)."""
    operations = OPERATION.findall(rest)
    if len(operations) == 1:
        return evaluate(first, *operations[0])
    if first.endswith("%") or any(b.endswith("%") for _, b in operations):
        return None
    total, sign, term = 0.0, 1, float(dec(first))
    for op, b in operations:
        y = float(dec(b))
        if op in "*×x":
            term *= y
        elif op == "/":
            if not y:
                return None
            term /= y
        else:
            total, sign, term = total + sign * term, (-1 if op in "-−" else 1), y
    return total + sign * term


def mixed_chain(rest: str) -> bool:
    """A chain of three or more operands that mixes operators ('a × b + c'): one passed on the form and
    one was flagged in a step that also spelled a number out (aq-02626 q03 Steps 5 and 4)."""
    kinds = {"*" if op in "*×x" else "-" if op in "-−" else op for op, _ in OPERATION.findall(rest)}
    return len(kinds) > 1


def number_words(text: str) -> list[str]:
    """Numbers of ten or more that a step spells out ('twelve', 'thirty'). Both steps whose exact
    result the form flagged held one (aq-01321 q02 Step 9, aq-02626 q03 Step 4)."""
    return [m.group(0) for m in SPELLED.finditer(text) if (words_value(m.group(0)) or 0) >= 10]


def result_ok(value: float | None, r: str) -> bool:
    """A plain result must be exact (float noise allowed); a '%' result must round correctly."""
    if value is None:
        return False
    if r.endswith("%"):
        q = Decimal(1).scaleb(-places(r))
        return Decimal(repr(value * 100)).quantize(q, ROUND_HALF_UP) == dec(r)
    w = float(dec(r))
    return abs(value - w) <= 1e-9 * max(1.0, abs(w))


def printed(text: str) -> dict[Decimal, int]:
    """Each value a document prints in digits, with the character position of its first printing.
    '37,963' -> 37963; '28,46' -> 28.46 (decimal comma); '44 303' is the two numbers 44 and 303."""
    found: dict[Decimal, int] = {}
    for m in DOC_NUMBER.finditer(text):
        t = m.group(0)
        thousands = re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", t)
        found.setdefault(Decimal(t.replace(",", "") if thousands else t.replace(",", ".")), m.start())
    return found


def words_value(phrase: str) -> int | None:
    """'One hundred and eighty-seven' -> 187; None for a bare scale word ('million' after digits)."""
    words = [w for w in re.findall(r"[a-z]+", phrase.lower()) if w != "and"]
    if not any(w in SMALL or w in TENS for w in words):
        return None
    total = current = 0
    for w in words:
        if w in SMALL:
            current += SMALL[w]
        elif w in TENS:
            current += TENS[w]
        elif w == "hundred":
            current = (current or 1) * 100
        else:
            total += (current or 1) * SCALE_WORDS[w]
            current = 0
    return total + current


def spelled_out(text: str) -> dict[int, tuple[int, str]]:
    """Each value a document spells out in words, with its first position and wording."""
    found: dict[int, tuple[int, str]] = {}
    for m in SPELLED.finditer(text):
        value = words_value(m.group(0))
        if value is not None:
            found.setdefault(value, (m.start(), m.group(0)))
    return found


def where(token: str, cited, digits: dict[int, dict[Decimal, int]]) -> tuple[int, int] | None:
    """(position, Doc) of the earliest printing of the token's value in a cited document. A number
    without '%' may also be a printed value times a power of 1,000 (a unit conversion: '28,460' GWh
    against '28,46' TWh); a factor of 10 does not count (aq-00949 q04: '53.2%' against '532')."""
    try:
        v = abs(dec(token))
    except InvalidOperation:
        return None
    scales = [Decimal(1)] if token.endswith("%") else SCALES
    hits = [(digits[d][v / s], d) for d in cited if d in digits for s in scales if v / s in digits[d]]
    return min(hits) if hits else None


def steps(reasoning: str) -> list[tuple[str, str]]:
    """(label, text) per step: a line opening with 'Step N' or 'N.' starts one; other lines continue it."""
    found: list[list[str]] = []
    for line in (ln.strip() for ln in reasoning.splitlines()):
        if not line:
            continue
        if NEW_STEP.match(line) or not found:
            found.append([line])
        else:
            found[-1].append(line)
    out = []
    for n, lines in enumerate(found, 1):
        text = "\n".join(lines)
        number = re.match(r"(?:Step\s+)?(\d+)", text)
        out.append((f"Step {number.group(1) if number else n}", text))
    return out


def doc_list(numbers) -> str:
    names = [str(n) for n in numbers]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def form_message(label: str, cited: tuple, token: str) -> str:
    if not cited:
        return f"{label}: Which document says {token}? Add 'Doc N'."
    if len(cited) == 1:
        return f"{label}: Doc {cited[0]} doesn't mention {token}."
    return f"{label}: Docs {doc_list(cited)} don't mention {token}."


def diagnose(token: str, position: int, body: str, calc, cited: tuple, earlier: set[str],
             digits: dict, words: dict, quotes: dict[int, list[str]]) -> tuple[str, bool]:
    """Why the number cannot be placed and the fix, and whether the flag is an expected false alarm
    (the cited document states it, in words or deep, in a passage quoted as evidence)."""
    if not cited:
        return ("this step names no document, so a new number needs one: cite the Doc that prints it in the "
                "step's head, or only reuse an earlier step's value as the identical string"), False
    if len(cited) == 1 and token in earlier:
        return ("a step citing one document accepts no earlier step's result (aq-02102 q01): cite every "
                "contributing document in the head, as 'Calculation (Doc 2 and Doc 6):'"), False
    deep = where(token, cited, digits)
    if deep:
        if where(token, [deep[1]], {deep[1]: printed(" ".join(quotes.get(deep[1], [])))}):
            return (f"expected false alarm: Doc {deep[1]} prints it at character {deep[0]:,}, past the "
                    f"{READ_DEPTH:,} characters the form is taken to read, in a passage quoted as evidence; no "
                    "wording clears it, so say so with the hand-over"), True
        return (f"Doc {deep[1]} prints it only at character {deep[0]:,}, past the {READ_DEPTH:,} characters the form "
                "is taken to read (it flagged printed numbers near characters 80,000 and 84,000): use an input "
                "printed earlier, or quote this passage as evidence if it is the source (the flag is then an "
                "expected false alarm)"), False
    value = abs(dec(token))
    if value == value.to_integral_value() and not token.endswith("%"):
        spelled = sorted((words[d][int(value)], d) for d in cited if int(value) in words.get(d, {}))
        quoted = [d for (_, d) in spelled if any(int(value) in spelled_out(q) for q in quotes.get(d, []))]
        if quoted:
            at, phrase = words[quoted[0]][int(value)]
            return (f'expected false alarm: Doc {quoted[0]} states it only in words ("{phrase}", character '
                    f"{at:,}) in a passage quoted as evidence, and the form matches digits (aq-02505 q01); no "
                    "wording clears it, so say so with the hand-over"), True
        if spelled:
            (at, phrase), d = spelled[0]
            return (f'Doc {d} prints it only in words ("{phrase}", character {at:,}), and the form matches '
                    "digits: if that passage is the source, quote it as evidence (the flag is then an expected "
                    "false alarm); otherwise cite the document that prints it"), False
    if calc and position == calc.start(3) and number_words(body):
        return (f'the step spells a number out ("{number_words(body)[0]}"), and the form then did not exempt the '
                "calculation's result (aq-01321 q02 Step 9 'Twelve months ended ...', aq-02626 q03 Step 4 'twelve "
                "30-day months'): write the step's numbers in digits or leave the word out"), False
    if calc and position > calc.end(3):
        return ("it restates or extends the step's result after the calculation, so the form reads it as a "
                "document figure: give the result once, straight after '='"), False
    if "=" in body[:position]:
        return ("it follows '=' but is not the exact result of the step's first bare calculation (unit words "
                "inside the expression, brackets, a second calculation in the step, or a rounded or "
                "non-terminating result): one bare calculation per step, with its exact result straight after "
                "'='"), False
    if token + "%" in earlier:
        return ("an earlier result typed as a percentage is not reusable as a plain number (aq-02157 q01): "
                "route the steps through plain or percentage-point quantities"), False
    others = sorted(d for d in digits if d not in cited and (hit := where(token, [d], digits)) and hit[0] < READ_DEPTH)
    if others:
        return (f"Doc {doc_list(others)} prints it; if that is where it comes from, cite that document "
                "(the check does not prove the match is the same fact)"), False
    return "no cited document prints it: cite the document that does, or derive it in a calculation step", False


def check(reasoning: str, docs: dict[int, str], quotes: dict[int, list[str]] | None = None) -> list[Flag]:
    """Every number the form is predicted to flag, step by step. docs maps the task page's Doc
    numbers to their text as the page shows it (no extraction header or page markers); quotes maps
    them to the question's evidence quotes. A figure the cited document really states, in words or
    past the form's read depth, inside a quoted passage is an expected false alarm: a WARN."""
    quotes = quotes or {}
    digits = {n: printed(text) for n, text in docs.items()}
    words = {n: spelled_out(text) for n, text in docs.items()}
    flags: list[Flag] = []
    earlier: set[str] = set()
    for label, step in steps(reasoning):
        head = step.split(":", 1)[0]
        cited = tuple(dict.fromkeys(int(n) for n in re.findall(r"\bDocs? (\d+)", head)))
        if re.search(r"\bDocs \d", head):
            flags.append(Flag("WARN", label, "", cited, f"{label}: cites documents as 'Docs ...'.",
                              "the form read 'Docs 10 to 13' as Doc 10 alone (aq-01960 q02); write each one as "
                              "'Doc N', as in 'Calculation (Doc 2 and Doc 6):'"))
        body = REFERENCE.sub(" ", re.sub(r"^\d+[.:)]", " ", step))
        verified: set[int] = set()
        calc = next(CALC.finditer(body), None)
        if calc and not number_words(body) and result_ok(evaluate_chain(calc.group(1), calc.group(2)), calc.group(3)):
            verified.add(calc.start(3))
            if mixed_chain(calc.group(2)):
                flags.append(Flag("WARN", label, calc.group(3), cited, f"{label}: a chain that mixes operators.",
                                  "one such chain passed on the form and one was flagged in a step that also "
                                  "spelled a number out (aq-02626 q03 Steps 5 and 4): prefer one two-operand "
                                  "calculation per step"))
        for m in PERCENT_OF.finditer(body):
            a, b, c = m.groups()
            same_doc = any(re.search(r"(?<![\d.,])" + re.escape(a) + r"%", docs[d][:READ_DEPTH]) and
                           re.search(r"(?<![\d.,])" + re.escape(b) + r"(?![\d]|[.,]\d)", docs[d][:READ_DEPTH])
                           for d in cited if d in docs)
            if same_doc and (dec(a) / 100 * dec(b)).quantize(Decimal(1).scaleb(-places(c)), ROUND_HALF_UP) == dec(c):
                verified.add(m.start(3))
        # A result typed as a percentage, by "per cent" after it or "in %:" before its expression, is
        # stored as "r%"; a later plain r does not match it.
        head_end = body.find(":")
        described = body[head_end + 1:calc.start(1)] if calc and head_end < calc.start(1) else ""
        typed = re.search(r"(?<![\d.])%|\bper\s?cent\b|\bpercent\b", described)
        results, typed_at = [], set()
        for m in re.finditer(r"=\s*(-?(?:" + OPERAND + r"))(\s*(?:per\s?cent\b|percent\b))?", body):
            r = m.group(1)
            if (m.group(2) or (typed and calc and m.start(1) == calc.start(3))) and not r.endswith("%"):
                typed_at.add(m.start(1))
                results.append(r + "%")
            else:
                results.append(r)
        results.extend(m.group(0) for m in TOKEN.finditer(body) if m.start() not in typed_at)
        seen: set[str] = set()
        for m in TOKEN.finditer(body):
            token = m.group(0)
            if m.start() in verified or (len(cited) != 1 and token in earlier) or token in seen:
                continue
            seen.add(token)
            hit = where(token, cited, digits)
            if hit and hit[0] < SAFE_DEPTH:
                continue
            if hit and hit[0] < READ_DEPTH:
                flags.append(Flag("WARN", label, token, cited, form_message(label, cited, token),
                                  f"Doc {hit[1]} prints it first at character {hit[0]:,}, past the deepest observed "
                                  f"pass ({OBSERVED_PASS:,}); the form flagged printed numbers near character "
                                  "80,000, so it may flag this one: prefer an input printed earlier"))
                continue
            if re.fullmatch(r"\d", token) and any(
                    int(token) in words.get(d, {}) and words[d][int(token)][0] < READ_DEPTH for d in cited):
                continue  # a single digit spelled out within the read text passed ("five", aq-02505 q01)
            why, false_alarm = diagnose(token, m.start(), body, calc, cited, earlier, digits, words, quotes)
            flags.append(Flag("WARN" if false_alarm else "FAIL", label, token, cited,
                              form_message(label, cited, token), why))
        earlier |= set(results)
    return flags


def input_notes(quote: str, text: str) -> list[str]:
    """Sketch-time warnings for one input quote against its document's page text: a number of 10 or
    more that the quote states only in words, and digits the document prints first past SAFE_DEPTH."""
    digits = printed(text)
    notes = []
    for m in SPELLED.finditer(quote):
        value = words_value(m.group(0))
        if value is not None and value >= 10 and (Decimal(value) not in digits or digits[Decimal(value)] >= READ_DEPTH):
            notes.append(f'the quote states {value} only in words ("{m.group(0)}"): a reasoning step citing this '
                         f"document for {value} draws \"Doc N doesn't mention {value}\" on the form (aq-02505 q01), a "
                         "false alarm no wording clears; prefer an input printed in digits, or keep this quote as "
                         "evidence and mention the flag with the hand-over")
    for m in TOKEN.finditer(quote):
        hit = where(m.group(0), [0], {0: digits})
        if hit and hit[0] >= SAFE_DEPTH:
            notes.append(f"the quoted {m.group(0)} is printed first at character {hit[0]:,}; the form has passed "
                         f"printed numbers only up to character {OBSERVED_PASS:,} and flagged them near 80,000")
    return notes
