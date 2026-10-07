---
name: docket-platform-guide-newer-than-instruction
description: "The platform guide captured 2026-10-04 (sections dated Oct 1-3) is newer than instruction.md - rule 10 (ask about the world, not the set), 20-45 word aim with a warning over 60, task shapes, send-back reasons, full AI-use section; the floor and gate card still follow the older text."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-04
  originSessionId: 58fa60e0-67c1-4288-96e5-e9a1cc580e0a
  modified: 2026-10-05T02:19:54.654Z
---

## Current rule

Until synchronization of `instruction.md` and `tools/check_questions.py` is complete,
check questions against the newer platform guide as well. Claude Opus 5.5 handles these checks
without waiting for a user decision on routine work. The full guide text is no longer in
the workspace (see history, 2026-10-04); this note's summary is the working copy until the user
saves the guide again. The differences that change a check:

- Rule 10, "Ask about the world, not about the set": the answer is a fact about what the
  documents describe, not about the documents. The question may not count or quantify documents
  ("in exactly two of the documents", "cited in both") or refer to "this bundle", "this set" or
  "this collection". The answer may not be a document, a reference to one (file name, exhibit or
  docket number) or the name of whoever wrote one. A standard or regulation is a fine answer.
  The guide's task shapes add: avoid questions that only ask who cites whom or which authors or
  journals appear.
- Length: the guide says aim for 20-45 words. The form's quality checks (captured 2026-10-04,
  `reference/platform-quality-checks.md`) say "Aim as short as it can be and stay exact; warns
  above 60, blocks above 80. Shorter is never a fault", and need 8 or more words. The floor
  follows the form.
- "Difficulty belongs in the documents, not in the question": applying any counting rule must
  take looking, not judgment.
- Common send-back reasons: a gold computed from rounded inputs when the document states the
  figure; a description that fits more than one thing; two asks with one answer; too long;
  period or terms not pinned; thin reasoning or missing evidence ("Every necessary document
  needs at least one quote").

**Why:** `question-review` and the gate card read `instruction.md`. Without this note, a check
would pass a 70-word question, or one about the set, that the platform sends back.

**How to apply:** in every `/docket-check` and review, apply rule 10 and the 60-word warning by
hand. The gate card now explicitly references these additional checks, but the mechanical
floor remains incomplete. Once the guide and floor are synchronized, update this note.

## Evidence and history

- 2026-10-04: found while starting aq-docket-trial-01. The capture's guide has ten rules; the
  workspace copy has nine. The difference was recorded for later synchronization.
- 2026-10-04: aligned commands and workflow with autonomous Opus 5.5 ownership and made
  the gate's newer-guide checks explicit. The local guide and floor have not been synchronized.
- 2026-10-04 (aq-docket-trial-05): same finding (no "## Guide" in any of the seven captures);
  the pointer had already been corrected by a parallel session. Rule 10 and the 20-45 word aim
  were applied to trial-05 from this summary.
- 2026-10-04 (aq-docket-trial-04): same finding (contents link only); trial-04 checks applied
  this summary by hand.
- 2026-10-04 (aq-docket-trial-06 intake): `AQ-DOCKET-TRIAL-01_2026-10-04_0449.md` still lists
  "Guide · Project Docket: Question-Writing Guide" in its contents, but the section is gone (the
  file ends inside Doc 6), and no other trial capture (01-07) holds the guide. The AI-use
  section's exact wording cannot be rechecked locally; ask the user for a fresh capture if a
  decision turns on it.
