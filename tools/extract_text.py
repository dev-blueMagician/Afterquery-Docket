"""Extract the text of a Docket bundle's documents so agents can grep and quote them.

Usage: python tools/extract_text.py tasks/<slug> [--force]

Reads every file under tasks/<slug>/docs/ and writes tasks/<slug>/text/Dnn.txt, one per
document, with "=== page N ===" markers for PDFs, plus text/manifest.json mapping each id
to its source file. A PDF also gets Dnn.layout.txt (pdftotext -layout), which keeps table
rows on one line. Ids are stable: a rerun keeps existing ids, re-extracts only files whose
bytes changed (all of them with --force), and gives new files the next free id.

Text is NFKC-normalised UTF-8 with LF newlines. check_questions.py looks evidence quotes up
in these files, so copy quotes from them, not from a PDF viewer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

TEXT_SUFFIXES = {".txt", ".md", ".csv", ".tsv", ".json"}
HTML_SUFFIXES = {".html", ".htm", ".xhtml"}
THIN_PAGE_CHARS = 200  # a PDF page with less text than this is probably a scan or a chart
BLOCK_TAGS = ["p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section",
              "article", "header", "footer", "pre", "blockquote", "dt", "dd", "ul", "ol", "title"]


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("­", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def decode(data: bytes) -> str:
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def pdf_pages(path: Path) -> tuple[list[str], str]:
    try:
        import pymupdf
        with pymupdf.open(path) as doc:
            return [page.get_text("text") for page in doc], "pymupdf"
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        return [page.extract_text() or "" for page in PdfReader(path).pages], "pypdf"
    except ImportError:
        pass
    return pdftotext(path, layout=False).split("\f"), "pdftotext"


def pdftotext(path: Path, layout: bool) -> str:
    args = ["pdftotext", "-enc", "UTF-8"] + (["-layout"] if layout else []) + [str(path), "-"]
    return subprocess.run(args, capture_output=True, check=True).stdout.decode("utf-8", "replace")


def html_text(data: bytes, parser: str) -> str:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data, parser)
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    for row in soup.find_all("tr"):
        cells = [cell.get_text(" ", strip=True) for cell in row.find_all(["td", "th"])]
        row.replace_with(soup.new_string(" | ".join(cells) + "\n"))
    for tag in soup.find_all(BLOCK_TAGS):
        tag.insert_after("\n")
    text = soup.get_text("" if parser != "xml" else "\n")
    return "\n".join(re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n"))


def docx_text(path: Path) -> str:
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    document = Document(path)
    lines = []
    for child in document.element.body.iterchildren():
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "p":
            lines.append(Paragraph(child, document).text)
        elif tag == "tbl":
            for row in Table(child, document).rows:
                lines.append(" | ".join(cell.text.strip() for cell in row.cells))
    return "\n".join(lines)


def extract(path: Path) -> dict:
    """Return {method, pages, body, layout, thin_pages} for one document, or method 'unsupported'."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        pages, method = pdf_pages(path)
        thin = [n for n, page in enumerate(pages, 1) if len(page.strip()) < THIN_PAGE_CHARS]
        body = "\n".join(f"=== page {n} ===\n{page.strip()}\n" for n, page in enumerate(pages, 1))
        layout = None
        if shutil.which("pdftotext"):
            layout_pages = pdftotext(path, layout=True).split("\f")
            layout = "\n".join(f"=== page {n} ===\n{page.rstrip()}\n"
                               for n, page in enumerate(layout_pages, 1) if n <= len(pages))
        return {"method": method, "pages": len(pages), "body": body, "layout": layout, "thin_pages": thin}
    if suffix in HTML_SUFFIXES:
        return {"method": "html", "pages": None, "body": html_text(path.read_bytes(), "lxml")}
    if suffix == ".xml":
        return {"method": "xml", "pages": None, "body": html_text(path.read_bytes(), "xml")}
    if suffix == ".docx":
        return {"method": "docx", "pages": None, "body": docx_text(path)}
    if suffix in TEXT_SUFFIXES:
        return {"method": "text", "pages": None, "body": decode(path.read_bytes())}
    return {"method": "unsupported", "pages": None, "body": None}


def write_text(path: Path, text: str) -> None:
    path.write_bytes(text.encode("utf-8"))  # bytes keep LF on Windows


def run(bundle: Path, force: bool = False) -> list[str]:
    """Extract every document of the bundle; return report lines."""
    docs, text_dir = bundle / "docs", bundle / "text"
    if not docs.is_dir():
        raise SystemExit(f"{docs} does not exist; copy the bundle's documents there first.")
    text_dir.mkdir(exist_ok=True)
    manifest_path = text_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes().decode("utf-8")) if manifest_path.exists() else {}
    by_source = {entry["source"]: doc_id for doc_id, entry in manifest.items()}
    sources = sorted(p for p in docs.rglob("*")
                     if p.is_file() and not any(part.startswith(".") for part in p.relative_to(docs).parts))
    next_number = max((int(k[1:]) for k in manifest), default=0) + 1
    report, seen = [], set()
    for source in sources:
        rel = source.relative_to(bundle).as_posix()
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        doc_id = by_source.get(rel)
        if doc_id is None:
            doc_id, next_number = f"D{next_number:02d}", next_number + 1
        seen.add(doc_id)
        old = manifest.get(doc_id, {})
        unchanged = (old.get("sha256") == digest and not old.get("missing")
                     and (old.get("method") == "unsupported" or (text_dir / f"{doc_id}.txt").exists()))
        if unchanged and not force:
            entry, note = old, "unchanged"
        else:
            result = extract(source)
            entry = {"source": rel, "sha256": digest, "method": result["method"]}
            if result["body"] is None:
                note = "UNSUPPORTED - read it visually or convert it to PDF/HTML/DOCX/TXT"
            else:
                body = normalise(result["body"])
                header = f"# {doc_id} | {rel}" + (f" | {result['pages']} pages" if result["pages"] else "")
                write_text(text_dir / f"{doc_id}.txt", f"{header}\n\n{body}")
                entry.update({"pages": result["pages"], "chars": len(body)})
                if result.get("layout"):
                    write_text(text_dir / f"{doc_id}.layout.txt", f"{header} | layout\n\n{normalise(result['layout'])}")
                    entry["layout"] = f"text/{doc_id}.layout.txt"
                if result.get("thin_pages"):
                    entry["thin_pages"] = result["thin_pages"]
                note = "extracted"
        manifest[doc_id] = entry
        pages = f"{entry['pages']:>4} pp" if entry.get("pages") else "   - pp"
        chars = f"{entry.get('chars', 0):>9,} chars"
        line = f"{doc_id}  {pages}  {chars}  {entry['method']:<11} {entry['source']}  [{note}]"
        if entry.get("thin_pages"):
            line += f"\n      little or no text on pages {entry['thin_pages']}: scans or charts; read them visually"
        report.append(line)
    for doc_id, entry in manifest.items():
        if doc_id not in seen and not entry.get("missing"):
            entry["missing"] = True
            report.append(f"{doc_id}  source {entry['source']} is gone; id retired, text kept")
    write_text(manifest_path, json.dumps(dict(sorted(manifest.items())), indent=2, ensure_ascii=False) + "\n")
    return report


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", type=Path, help="tasks/<slug>")
    parser.add_argument("--force", action="store_true", help="re-extract unchanged documents too")
    args = parser.parse_args(argv)
    report = run(args.bundle, args.force)
    print("\n".join(report) if report else f"No documents under {args.bundle / 'docs'}.")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
