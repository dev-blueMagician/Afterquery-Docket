---
name: docket-local-ids-vs-platform-doc-numbers
description: "Local Dnn ids follow extract_text's alphabetical file order and can differ from the task page's 'Doc N' numbers; form fields (reasoning citations, saved passages) must use the platform numbers."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-04
  originSessionId: 0b3fd638-83b1-473b-8a9e-6c645eb2ec12
  modified: 2026-10-04T15:25:45.060Z
---

## Current rule

`tools/extract_text.py` numbers documents D01, D02, ... in alphabetical order of file name. The
task page numbers them "Doc 1", "Doc 2", ... in its own order, so the two can differ.

- At intake from a capture, compare `text/manifest.json` with the capture's "### Doc N ·
  <file>" headings. Record the mapping in each doc-map Source line and in `notes/session.md`.
- Anything typed into the form uses the platform number. That covers the reasoning field's
  "Doc N" citations, because the form checks each step's numbers against the document it
  names ([[docket-form-automated-checks]]), and the passages saved for each document.
- Local files keep Dnn ids: `documents:`, evidence lines and the floor. State the mapping in
  the question's `## Lever checks`.
- When ids coincide (alphabetical order happens to match), nothing changes, but check anyway.

**Why:** a reasoning step citing a local id that means another platform document points the
form's number check at the wrong document. A passage attached to the wrong document fails
"every necessary document needs at least one quote".

**How to apply:** check the mapping at `/docket-new`; write hand-over reasoning with platform
numbers; list passages to save by platform number.

## Evidence and history

- 2026-10-04 (aq-docket-trial-07): mismatch found at extraction. D01 = Doc 3, D03 = Doc 1,
  D04 = Doc 5, D05 = Doc 4; D02, D06 and D07 coincided. q01 and q02 reasoning was written with
  platform numbers and checked by an emulation of the form's number rule. No form report on
  this yet; one bundle. A tool change (recording the platform number in the manifest) would
  remove the manual step.
