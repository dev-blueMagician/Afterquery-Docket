---
name: docket-windows-text-io
description: "This host defaults to cp1252 and PowerShell redirects add a BOM and CRLF; scripts read and write UTF-8 bytes, files are made with Write/Edit, and evidence is quoted from text/Dnn.txt."
metadata:
  node_type: memory
  type: reference
  updated: 2026-10-01
  originSessionId: 98bac4b9-cec9-45e6-af00-b85e64f88959
  modified: 2026-10-05T17:49:35.237Z
---

## Current rule

- Python on this Windows host defaults to cp1252. Scripts read text with
  `read_bytes().decode("utf-8")` and write with `write_bytes(text.encode("utf-8"))`, which also
  keeps LF newlines. `Path.read_text()` without an encoding mis-decodes non-ASCII characters.
- Never create or edit files with PowerShell `>`, `Out-File` or `Set-Content`: they add a BOM
  and CRLF. Use the Write and Edit tools.
- Quote evidence from `text/Dnn.txt`, not from a PDF viewer or a page read visually:
  `check_questions.py` looks quotes up in the extracted, NFKC-normalised text.
- In the Bash tool, a heredoc whose body contains a backtick fails before running ("unexpected
  EOF while looking for matching"), even with a quoted delimiter such as <<'EOF'. Write such
  content (raw agent returns, Markdown with code spans) with the Write or Edit tool instead.

**Why:** the Kepler workspaces (packaging preflight, 2026-08) and Minerva (patch export,
2026-09) both lost time to these encoding and newline faults on this machine.

**How to apply:** new tools under `tools/` follow the byte-level pattern of
`tools/extract_text.py`; run `python tools/test_docket_tools.py` after changing any tool.

## Evidence and history

- 2026-10-01: seeded from Kepler's `WORKFLOW.md` packaging notes and Minerva's
  `minerva-patch-export` memory.
- 2026-10-05 (aq-00745): two Bash heredoc appends of raw solver returns failed with "unexpected
  EOF while looking for matching" because the returns contained backticks; nothing was written,
  and the same content went in through Write/Edit. Heredocs without backticks worked.
