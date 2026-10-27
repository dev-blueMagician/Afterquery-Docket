"""Summarise a saved Docket difficulty-check capture: runs, tiers and what every attempt committed to.

Usage: python tools/verdict_summary.py <capture.txt> [--q tasks/<slug>/questions/qNN.md] [--run N] [--full]

The capture (plain text, 2026-10 page layout) holds a "RUN HISTORY" with one block per run: a ruled
header "Run N · <result> · <note>", a line "<date> · Version <id> · Low a/b · Medium a/b · High a/b",
"What changed before this run: ...", "Your answer: ...", then the sections "Closed-book check",
"Low model", "Medium model", "High model" and "Document check" (each underlined with "="). A section
lists attempts, "Attempt <label> · <grade>" underlined with "-", each with "Docs:", the platform's
"Final answer:" pick, optional "How it got there:" / "Where it left your evidence:" lines, a
"Full answer" block and a "Reasoning" block.

The platform's "Final answer" pick is often a stray fragment, and its "Where it left your evidence"
line can misdescribe the attempt (aq-02564 Run 2), so this tool also prints the value each attempt's
own Full answer commits to: its "Answer:" line, else its last \\boxed{...}, else the last line with a
figure near the end. That is a reading aid; the platform's grade is the result. With --q the tool
counts verbatim quotes of the question file's wording in each run and compares "Your answer" with its
gold, the evidence for binding a run to a revision. It reads the capture only and writes nothing.

A committed value is not a route. The summary therefore prints each attempt's line span in the
capture and whether its Reasoning block was loaded when the page was saved, and it opens with a
warning when any was not. Name a wrong attempt's route only after reading that span: on aq-02749 q02 a
6 that equalled a list-length subtraction and a 9 called a "miscount" were both a misread of one
State's list, visible only in the Reasoning (two of the first capture's blocks still read "Loading").

With --q the summary also prints, per attempt, how much of each Evidence quote in the question file the
attempt's Full answer and Reasoning echo: the share of the quote's five-word runs that recur, and a note
when the last third of a long quote does not recur at all. It separates "never reached the deciding
clause" from "read it and set it aside": on aq-03736 q01 four wrong attempts echoed the head of one
phase-in sentence and none of its closing exception, while the page's own note called all four a wrong
phase. A paraphrase scores low, so a low share is a pointer to the span, not proof the passage went unread.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DOT = "·"
RUN = re.compile(r"^Run (\d+) " + DOT + r" (.+)$")
ATTEMPT = re.compile(r"^Attempt (.+?) " + DOT + r" (.+)$")
SECTIONS = ("Closed-book check", "Low model", "Medium model", "High model", "Document check")
FIELDS = {"Docs:": "docs", "Final answer:": "final", "How it got there:": "how",
          "Where it left your evidence:": "where"}
ANSWER_LINE = re.compile(r"^(?:short answer|answer|final answer)\s*[:\-]", re.I)
BOXED = re.compile(r"\\boxed\{((?:[^{}]|\{[^{}]*\})*)\}")
TAIL = 8  # a Full answer states its total near the end when it has no "Answer:" line
LIST_ITEM = re.compile(r"^(?:[-*•]|\d{1,2}[.)])\s+\S")  # a bullet or numbered line of a list answer
ITEM_WIDTH = 70  # characters kept of each list item, so several items fit on the summary line
NOT_LOADED = "Loading the reasoning"  # the page's placeholder for a Reasoning block it had not fetched yet
EVIDENCE_ROW = re.compile(r'^- (D\d+) \((.*?)\) \[[^\]]*\]: "(.*)"\s*$')
RUN_WORDS = 5    # words in a run: long enough that the source's own wording has to recur, not a stray phrase
LONG_QUOTE = 12  # runs; below this a quote has no meaningful "last third"


def _rule(line: str, char: str) -> bool:
    stripped = line.strip()
    return len(stripped) >= 5 and set(stripped) == {char}


def _underlined(lines: list[str], i: int, char: str) -> bool:
    return i + 1 < len(lines) and _rule(lines[i + 1], char)


def committed(full: list[str]) -> str:
    """The value an attempt's Full answer commits to, as a reading aid (see the module text)."""
    body = [line.strip() for line in full if line.strip() and not _rule(line, "-")]
    if not body:
        return ""
    for at, line in enumerate(body):
        if ANSWER_LINE.match(line):
            if re.search(r"\d", line):
                return line
            # An "Answer:" sentence without a figure: its total follows ("Total distribution bill: $1,000/month").
            for later in body[at + 1:]:
                if re.search(r"total", later, re.I) and re.search(r"\$\s?\d", later) and len(later) < 300:
                    return later
            break
    boxed = BOXED.findall("\n".join(body))
    if boxed:
        value = re.sub(r"\\text\{([^{}]*)\}", r"\1", boxed[-1].replace("{,}", ",").replace("\\$", "$"))
        return "boxed: " + " ".join(value.split())
    # A list answer that ends in bullets or numbered lines commits to the whole list, not to its last line
    # (aq-03950 q02: nine two-name answers each showed only their second name here and on the page).
    items: list[str] = []
    end = len(body)
    if end >= 3 and not LIST_ITEM.match(body[-1]) and not re.search(r"\d", body[-1]):
        end -= 1  # a closing remark with no figure after the list ("No other witness had a role there.")
    for line in reversed(body[:end]):
        if not LIST_ITEM.match(line):
            break
        items.append(line if len(line) <= ITEM_WIDTH else line[:ITEM_WIDTH - 1].rstrip() + "…")
    if len(items) >= 2 and not any("$" in item for item in items):
        return " | ".join(reversed(items))
    tail = body[-TAIL:]
    for line in reversed(tail):
        if "$" in line or (re.search(r"\d", line) and re.search(r"=|total", line, re.I)):
            return line
    for line in reversed(tail):
        if re.search(r"\d", line):
            return line
    return body[-1]


def reasoning_state(attempt: dict) -> str:
    """'loaded', 'not loaded' (the page still showed its placeholder when it was saved) or 'none'."""
    body = [line for line in attempt.get("reasoning", []) if line.strip() and not _rule(line, "-")]
    if not body:
        return "none"
    return "not loaded" if any(NOT_LOADED in line for line in body) else "loaded"


def bare_answer(attempt: dict) -> bool:
    """A Full answer that is only a value: the route to it is in the Reasoning block alone."""
    body = [line.strip() for line in attempt["full"] if line.strip() and not _rule(line, "-")]
    return len(body) <= 2 and sum(len(line.split()) for line in body) <= 8


def parse(text: str) -> dict:
    """{'head': [...], 'runs': [{number, title, tiers, changed, your_answer, start, end, sections}]}."""
    lines = text.split("\n")
    head: list[str] = []
    runs: list[dict] = []
    run = section = attempt = None
    mode = None
    opened: list[dict] = []  # the attempt still being read; closed with its last 1-based line

    def close(at: int) -> None:
        while opened:
            opened.pop()["end"] = at

    for i, line in enumerate(lines):
        found = RUN.match(line)
        if found and i > 0 and _rule(lines[i - 1], "-") and i + 2 < len(lines) and _rule(lines[i + 2], "-"):
            close(i - 1)
            if run is not None:
                run["end"] = i - 1
            run = {"number": int(found.group(1)), "title": line.strip(), "tiers": lines[i + 1].strip(),
                   "changed": "", "your_answer": "", "start": i, "end": len(lines), "sections": []}
            runs.append(run)
            section = attempt = mode = None
            continue
        if run is None:
            if re.search(r"tier|model: \d+ of \d+|runs left|^Saved:|Attempts read:|may be too vague|"
                         r"may not be needed|difficulty check (?:finished|passes)", line):
                head.append(line.strip())
            continue
        if line in SECTIONS and _underlined(lines, i, "="):
            close(i)
            section = {"name": line, "attempts": []}
            run["sections"].append(section)
            attempt = mode = None
            continue
        found = ATTEMPT.match(line)
        if found and section is not None and _underlined(lines, i, "-"):
            close(i)
            attempt = {"label": found.group(1), "grade": found.group(2).strip(), "docs": "", "final": "",
                       "how": "", "where": "", "full": [], "reasoning": [], "line": i + 1, "end": len(lines)}
            opened.append(attempt)
            section["attempts"].append(attempt)
            mode = None
            continue
        if attempt is None:
            if line.startswith("What changed before this run:"):
                run["changed"] = line.split(":", 1)[1].strip()
            elif line.startswith("Your answer:"):
                run["your_answer"] = line.split(":", 1)[1].strip()
            continue
        if line.strip() == "Full answer" and _underlined(lines, i, "-"):
            mode = "full"
        elif line.strip() == "Reasoning" and _underlined(lines, i, "-"):
            mode = "reasoning"
        elif mode == "full":
            attempt["full"].append(line)
        elif mode == "reasoning":
            attempt["reasoning"].append(line)
        elif mode is None:
            for label, key in FIELDS.items():
                if line.startswith(label):
                    attempt[key] = line[len(label):].strip()
    for item in runs:
        item["text"] = "\n".join(lines[item["start"]:item["end"]])
    return {"head": head, "runs": runs}


def question_fields(path: Path) -> tuple[str, str]:
    """The exact question and gold answer of a question file."""
    text = path.read_text(encoding="utf-8")

    def section(name: str) -> str:
        found = re.search(r"^## " + re.escape(name) + r"\s*\n+(.+?)\n\s*(?:\n|$)", text, re.S | re.M)
        return found.group(1).strip() if found else ""
    return section("Question"), section("Answer")


def evidence_rows(path: Path) -> list[tuple[str, str]]:
    """(label, quote) for each row of a question file's Evidence section, in the form's order."""
    text = path.read_text(encoding="utf-8")
    found = re.search(r"^## Evidence\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    rows = []
    for line in (found.group(1).split("\n") if found else []):
        row = EVIDENCE_ROW.match(line.strip())
        if row:
            rows.append((f"{row.group(1)} {row.group(2)}", row.group(3)))
    return rows


def _words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _runs(words: list[str], size: int) -> list[tuple[str, ...]]:
    return [tuple(words[i:i + size]) for i in range(len(words) - size + 1)]


def echo(quote: str, attempt_text: str) -> tuple[int, bool]:
    """Share (0-100) of a quote's five-word runs that recur in an attempt, and whether its last third recurs."""
    words = _words(quote)
    size = min(RUN_WORDS, len(words))
    runs = _runs(words, size)
    if not runs:
        return 0, False
    seen = set(_runs(_words(attempt_text), size))
    hits = [run in seen for run in runs]
    return round(100 * sum(hits) / len(hits)), any(hits[len(hits) - max(1, len(hits) // 3):])


def echo_line(evidence: list[tuple[str, str]], attempt: dict) -> str:
    """'E1 100% · E2 0% · E3 40%, end not echoed' for one attempt, E-numbers in the Evidence section's order."""
    text = "\n".join(attempt["full"] + attempt["reasoning"])
    parts = []
    for number, (_, quote) in enumerate(evidence, 1):
        share, tail = echo(quote, text)
        long = len(_runs(_words(quote), RUN_WORDS)) >= LONG_QUOTE
        parts.append(f"E{number} {share}%" + (", end not echoed" if share and long and not tail else ""))
    return f" {DOT} ".join(parts)


def _short(value: str, limit: int) -> str:
    value = " ".join(value.split())
    return value if len(value) <= limit else value[: limit - 1] + "…"


def render(parsed: dict, question: str = "", gold: str = "", only_run: int | None = None,
           full: bool = False, width: int = 200, evidence: list[tuple[str, str]] | None = None) -> str:
    out = list(dict.fromkeys(parsed["head"]))
    if evidence:
        out.append("Evidence rows: " + "; ".join(f"E{n} {label}" for n, (label, _) in enumerate(evidence, 1))
                   + f". 'evidence echoed' is the share of each quote's {RUN_WORDS}-word runs that recur in an "
                   "attempt's Full answer and Reasoning; a paraphrase scores low, so read the span before "
                   "calling a passage unread.")
    unread = [f"Run {run['number']} {section['name']} {attempt['label']}"
              for run in parsed["runs"] if only_run is None or run["number"] == only_run
              for section in run["sections"] for attempt in section["attempts"]
              if reasoning_state(attempt) == "not loaded"]
    if unread:
        out.append(f"Reasoning not loaded for {len(unread)} attempt(s): {'; '.join(unread)}. Their routes are unread: "
                   "open each attempt on the page and capture again before naming a route.")
    for run in parsed["runs"]:
        if only_run is not None and run["number"] != only_run:
            continue
        out += ["", run["title"], "  " + run["tiers"]]
        if run["changed"]:
            out.append("  Changed: " + _short(run["changed"], width * 2))
        out.append("  Your answer: " + (run["your_answer"] or "(not found)"))
        if question:
            quotes = run["text"].count(question)
            match = "yes" if gold and run["your_answer"] == gold else "no"
            out.append(f"  Identity: question quoted verbatim {quotes} time(s) in this run; "
                       f"\"Your answer\" equals the file's gold ({gold}): {match}")
        for section in run["sections"]:
            grades = [a["grade"] for a in section["attempts"]]
            right = sum(1 for g in grades if g.startswith("Right"))
            tally = f" ({right} of {len(grades)} right)" if section["name"].endswith("model") else ""
            out.append(f"  {section['name']}{tally}")
            for attempt in section["attempts"]:
                out.append(f"    {attempt['label']} {DOT} {attempt['grade']} | docs {attempt['docs'] or '-'}")
                out.append("      committed: " + _short(committed(attempt["full"]) or "(no Full answer)", width))
                if attempt["where"]:
                    out.append("      platform note: " + _short(attempt["where"], width))
                trace = f"      trace: lines {attempt['line']}-{attempt['end']}, reasoning {reasoning_state(attempt)}"
                if attempt["grade"].startswith("Wrong") and bare_answer(attempt):
                    trace += "; the Full answer is a bare value, so its route is only in the Reasoning block"
                out.append(trace)
                if evidence and reasoning_state(attempt) != "not loaded":
                    out.append("      evidence echoed: " + echo_line(evidence, attempt))
                if full:
                    out += ["      | " + line for line in attempt["full"] if line.strip() and not _rule(line, "-")]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("capture", type=Path, help="saved difficulty-check capture (.txt)")
    parser.add_argument("--q", type=Path, help="question file whose wording and gold bind the run")
    parser.add_argument("--run", type=int, help="show only this run number")
    parser.add_argument("--full", action="store_true", help="print each attempt's Full answer")
    args = parser.parse_args(argv)
    parsed = parse(args.capture.read_text(encoding="utf-8"))
    if not parsed["runs"]:
        print("No run blocks found: is this a difficulty-check capture?")
        return 1
    question, gold = question_fields(args.q) if args.q else ("", "")
    evidence = evidence_rows(args.q) if args.q else None
    print(render(parsed, question, gold, args.run, args.full, evidence=evidence))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
