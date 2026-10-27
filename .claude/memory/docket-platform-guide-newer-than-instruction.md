---
name: docket-platform-guide-newer-than-instruction
description: "The platform guide is newer than instruction.md: sections 4-7 of 2026-10-15/16 are saved verbatim in reference/platform-guide-2026-10-16.md (Hard definition, stacked levers, Hard shapes, Hard bank, send-back pitfalls); older summaries of 2026-10-04 (rule 10, 20-45 words) and 2026-10-15 (levers) below."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-04
  originSessionId: 58fa60e0-67c1-4288-96e5-e9a1cc580e0a
  modified: 2026-10-05T02:19:54.654Z
---

## 2026-10-17: the guide's sections 4-7 saved verbatim

The user pasted the platform guide's sections 4-7 (last updated Oct 15-16, 2026), saved verbatim in
[reference/platform-guide-2026-10-16.md](reference/platform-guide-2026-10-16.md). It governs where it differs
from this note's summaries below. What changed a check or a design:

- Hard is defined: "each of the two Hard solvers gets it wrong at least once in its three runs".
- "One lever is rarely enough"; Hard questions "stack two or more levers"; four Hard shapes (A-D);
  "Where solvers fail" and the method to find slips ("compare every quote of the same passage across
  documents, every spelling of each name, each figure against its earlier versions, and each summary
  against the rest of the document"), now `docket_agent.py mine`.
- An accepted Hard bank of eight questions, each with two or three levers stacked.
- Send-back pitfalls: contrived selectors (the most common), two questions in one, riddle chains,
  judgement conditions, golds that punish a right answer (bare value only); reason 8, read literally.
- The floor now lists the newer levers and warns on hint words, gold extras, selectors and "the latest
  report"; the design rules are in `reference/hard-playbook.md` (batch review 3).

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

## Section 4 levers, as summarised 2026-10-15

Source: the user pasted a summary of the platform guide's Section 4, "How to make a question harder"
(aq-04466, 2026-10-15). It is a summary, not the guide's words; the user found no "L1-L4" labels or
"harder variations" in the guide (the Coach had cited them). Levers beyond `instruction.md`'s list:

- Restated figures (marked most effective): an earlier period's figure on the basis a named later release uses.
- A precision the document does not print, computed from raw lines ("do not round intermediate values").
- A period no document reports on its own (a quarter backed out of a full year).
- Like for like across a definition change.
- Summary vs detail: a detail that corrects the document's own headline or summary.
- Quiet edit in a re-quoted passage: one word differs between two quotations of the same passage.
- Second mention, different words: the mention that matters uses other wording, a label or another section.
- Claimed but never discussed: a summary cites something the text never covers.
- Short references: "Id.", "the same case", "the Company", abbreviations.
- Footnotes and prose that change how a table is read.
- Calculate across documents: "three or more dependent steps usually trip solvers up".
- Combine two levers: "One lever usually lands Easy; two together land Medium or Hard."

Still marked most effective: Mentions it vs does it. The local guide's other two "most effective"
marks (the hedge; match, then exclude) are not marked in this summary.
