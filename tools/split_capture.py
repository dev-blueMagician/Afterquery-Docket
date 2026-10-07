"""Split a saved Docket task-page capture (Markdown or plain text) into the bundle's document files.

Usage: python tools/split_capture.py <capture.md|capture.txt> tasks/<slug> [--force]

The Markdown capture has a "## Documents" section holding one "### Doc N · <file name>" block per
document, or "### Doc N · <YYYY-MM-DD> · <file name>" when the page shows the document's date (a
bold title, a "<n> tokens · <n> characters" line, an optional "> **Incomplete:** ..." note, then
the document's text). The plain-text capture (2026-10-06 on) has a DOCUMENTS section between two
"=" rules; each document starts with a header between two "-" rules: "Doc N · [<type> · ]
[<YYYY-MM-DD> · ]<file name>", a title line and the size line. Its text keeps the document's own
characters, with no Markdown escapes, so a body's "-----" page rules and "# # #" lines stay as
they are. Each document's text is written to tasks/<slug>/docs/<file name> as UTF-8 with LF
newlines, exactly as captured. The bundle overview, the form's drafts and the guide are not
documents and are left out. Run tools/extract_text.py on the bundle afterwards.

The report gives each document's platform size, repeats the capture's "Incomplete" notes, and
lists each "[... N characters not shown on the page ...]" marker the capture left where text was
missing (in the first bundle, whole table bodies), with its line in docs/<file name> and whether
the markers account for the whole shortfall. That text is not in the bundle's files, so check it
on the platform before relying on it. Sizes never match exactly: the platform counts UTF-16 code
units and the capture normalises whitespace. A file already in docs/ with other content is left
alone unless --force is given. notes/intake.json saves warnings, source/capture hashes and prior
capture history; a newly supplied complete capture refreshes current completeness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

DOT = "·"
# The file name is a heading's last field. Pages may put descriptive fields before it: a date
# ("Doc 1 · 2026-04-15 · <file>"), a filing type and date ("Doc 1 · 8-K · 2026-04-23 · <file>"),
# a type alone ("Doc 4 · 8-K · <file>") or a type and fiscal year ("Doc 1 · 8-K · fy2025 · <file>").
DOC_HEADING = re.compile(r"^### Doc (\d+) " + DOT + r" (.+?)\s*$")
TXT_HEADING = re.compile(r"^Doc (\d+) " + DOT + r" (.+?)\s*$")
# The page may append more " · ..." fields, such as "2/2 quotes found" once passages are saved.
SIZE_LINE = re.compile(r"^([\d,]+) tokens " + DOT + r" ([\d,]+) characters(?: " + DOT + r" [^\n]*)?\s*$")
INCOMPLETE = re.compile(r"^> \*\*Incomplete:\*\*\s*(.+?)\s*$")
TXT_INCOMPLETE = re.compile(r"^(?:> )?(?:\*\*)?Incomplete:(?:\*\*)?\s*(.+?)\s*$")
SHORTFALL = re.compile(r"only ([\d,]+) of ([\d,]+) characters")
GAP_MARKER = re.compile(r"\[(?:…|\.\.\.) ([\d,]+) characters not shown on the page (?:…|\.\.\.)\]")
SAFE_NAME = re.compile(r"^[\w][\w.\-]*$")
# Plain-text capture: a section title sits between two "=" rules; a document header between two
# "-" rules. Bodies may hold shorter rules ("-----" page breaks) and stay untouched.
BANNER = re.compile(r"^={40,}\s*$")
RULE = re.compile(r"^-{40,}\s*$")
SECTION_TITLE = re.compile(r"^[A-Z][A-Z ]*[A-Z]\s*$")


def to_int(text: str) -> int:
    return int(text.replace(",", ""))


def gap_lines(doc: dict) -> list[str]:
    """Report lines for the capture's gap markers in one document, against its Incomplete note."""
    gaps = [(n, to_int(m.group(1))) for n, line in enumerate(doc["body"].split("\n"), 1)
            for m in GAP_MARKER.finditer(line)]
    match = SHORTFALL.search(doc["note"] or "")
    short = to_int(match.group(2)) - to_int(match.group(1)) if match else None
    if not gaps:
        return ["      no gap markers: the missing characters are not marked in the text"] if short else []
    total = sum(size for _, size in gaps)
    if short is None:
        cover = "no Incomplete note"
    elif total == short:
        cover = "all of the shortfall"
    else:
        cover = f"the note says {short:,} short"
    where = ", ".join(str(n) for n, _ in gaps)
    plural = "s" if len(gaps) > 1 else ""
    return [f"      {len(gaps)} gap marker{plural} ({total:,} characters, {cover}) at line{plural} {where}"]


def checked_name(number: str, fields: str) -> str:
    """The heading's file name (its last field), refused if it could leave docs/."""
    name = fields.split(f" {DOT} ")[-1].strip()
    if not SAFE_NAME.match(name) or ".." in name:
        raise ValueError(f"Doc {number}: unsafe file name {name!r}")
    return name


def trimmed(block: list[str]) -> list[str]:
    body = list(block)
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return body


def parse_capture(text: str) -> list[dict]:
    """Return one dict per document: number, name, title, stated_chars, note, body."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if any(line.strip() == "## Documents" for line in lines):
        return parse_markdown(lines)
    banner = next((i for i in range(1, len(lines) - 1) if lines[i].strip() == "DOCUMENTS"
                   and BANNER.match(lines[i - 1]) and BANNER.match(lines[i + 1])), None)
    if banner is None:
        raise ValueError("no '## Documents' section or DOCUMENTS banner; is this a saved Docket task page?")
    return parse_text(lines, banner + 2)


def parse_markdown(lines: list[str]) -> list[dict]:
    start = next(i for i, line in enumerate(lines) if line.strip() == "## Documents")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    heads = [i for i in range(start + 1, end) if DOC_HEADING.match(lines[i])]
    if not heads:
        raise ValueError("the '## Documents' section has no '### Doc N · <file>' blocks")
    documents = []
    for k, head in enumerate(heads):
        block = lines[head + 1: heads[k + 1] if k + 1 < len(heads) else end]
        number, fields = DOC_HEADING.match(lines[head]).groups()
        name = checked_name(number, fields)
        title, stated, note, body_start = None, None, None, 0
        for j, line in enumerate(block[:12]):
            if title is None and re.fullmatch(r"\*\*(.+)\*\*", line.strip()):
                title = line.strip()[2:-2]
                body_start = j + 1
            elif SIZE_LINE.match(line):
                stated = to_int(SIZE_LINE.match(line).group(2))
                body_start = j + 1
            elif INCOMPLETE.match(line):
                note = INCOMPLETE.match(line).group(1)
                body_start = j + 1
            elif line.strip() and stated is not None:
                break
        body = trimmed(block[body_start:])
        if not body:
            raise ValueError(f"Doc {number} ({name}) has no text in the capture")
        documents.append({"number": int(number), "name": name, "title": title, "stated_chars": stated,
                          "note": note, "body": "\n".join(body) + "\n"})
    return documents


def parse_text(lines: list[str], start: int) -> list[dict]:
    """Documents of a plain-text capture, from the line after the DOCUMENTS banner."""
    end = next((i for i in range(start, len(lines) - 2) if BANNER.match(lines[i])
                and SECTION_TITLE.match(lines[i + 1]) and BANNER.match(lines[i + 2])), len(lines))
    heads = []  # (opening rule, closing rule) of each document header
    i = start
    while i < end - 1:
        if RULE.match(lines[i]) and TXT_HEADING.match(lines[i + 1]):
            close = next((j for j in range(i + 2, min(i + 8, end)) if RULE.match(lines[j])), None)
            if close is not None and any(SIZE_LINE.match(lines[j]) for j in range(i + 2, close)):
                heads.append((i, close))
                i = close + 1
                continue
        i += 1
    if not heads:
        raise ValueError("the DOCUMENTS section has no 'Doc N · <file>' headers between rules")
    documents = []
    for k, (head, close) in enumerate(heads):
        number, fields = TXT_HEADING.match(lines[head + 1]).groups()
        name = checked_name(number, fields)
        title, stated, note = None, None, None
        for line in lines[head + 2: close]:
            if SIZE_LINE.match(line):
                stated = to_int(SIZE_LINE.match(line).group(2))
            elif TXT_INCOMPLETE.match(line):
                note = TXT_INCOMPLETE.match(line).group(1)
            elif title is None and line.strip():
                title = line.strip()
        body = trimmed(lines[close + 1: heads[k + 1][0] if k + 1 < len(heads) else end])
        if not body:
            raise ValueError(f"Doc {number} ({name}) has no text in the capture")
        documents.append({"number": int(number), "name": name, "title": title, "stated_chars": stated,
                          "note": note, "body": "\n".join(body) + "\n"})
    numbers = [doc["number"] for doc in documents]
    if numbers != sorted(set(numbers)):
        raise ValueError(f"document numbers out of order or repeated: {numbers}")
    return documents


def run(capture: Path, bundle: Path, force: bool = False) -> list[str]:
    """Write each captured document to bundle/docs/; return report lines."""
    documents = parse_capture(capture.read_bytes().decode("utf-8-sig"))
    docs = bundle / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    report = []
    for doc in documents:
        target = docs / doc["name"]
        data = doc["body"].encode("utf-8")
        if target.exists() and target.read_bytes() == data:
            state = "unchanged"
        elif target.exists() and not force:
            state = "EXISTS with other content; left alone (use --force to replace)"
        else:
            state = "replaced" if target.exists() else "written"
            target.write_bytes(data)  # bytes keep LF on Windows
        stated = f"{doc['stated_chars']:,} chars" if doc["stated_chars"] else "size not stated"
        line = f"Doc {doc['number']}  {doc['name']}  {stated}  [{state}]"
        if doc["note"]:
            line += f"\n      INCOMPLETE in the capture: {doc['note']}"
        report.append("\n".join([line] + gap_lines(doc)))
    # Keep the warnings after the console output is gone. The document body intentionally
    # excludes capture UI metadata, so extraction alone cannot recover an Incomplete note.
    intake = {"schema": 1, "capture_sha256": hashlib.sha256(capture.read_bytes()).hexdigest(),
              "documents": []}
    for doc in documents:
        target = docs / doc["name"]
        captured_hash = hashlib.sha256(doc["body"].encode("utf-8")).hexdigest()
        source_hash = hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else None
        intake["documents"].append({
            "number": doc["number"], "source": f"docs/{doc['name']}",
            "captured_sha256": captured_hash, "source_sha256": source_hash,
            "incomplete": bool(doc["note"]), "note": doc["note"],
            "gap_characters": sum(to_int(m.group(1)) for m in GAP_MARKER.finditer(doc["body"])),
            "matches_capture": source_hash == captured_hash})
    notes = bundle / "notes"
    notes.mkdir(parents=True, exist_ok=True)
    intake_path = notes / "intake.json"
    if intake_path.exists():
        # A fresh complete capture can replace a clipped intake. Keep the original warning
        # as history without treating a corrected, newly hashed corpus as clipped forever.
        previous = json.loads(intake_path.read_bytes())
        history = previous.get("history", [])
        prior = {key: previous.get(key) for key in ("capture_sha256", "documents")}
        current = {key: intake[key] for key in ("capture_sha256", "documents")}
        if prior != current:
            history = history + [prior]
        if history:
            intake["history"] = history
    intake_path.write_bytes((json.dumps(intake, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return report


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("capture", type=Path, help="the saved task page (.md or .txt)")
    parser.add_argument("bundle", type=Path, help="tasks/<slug>")
    parser.add_argument("--force", action="store_true", help="replace docs/ files whose content differs")
    args = parser.parse_args(argv)
    try:
        report = run(args.capture, args.bundle, args.force)
    except ValueError as error:
        print(f"split_capture.py: {error}")
        return 1
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
