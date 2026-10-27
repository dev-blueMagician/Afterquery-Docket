---
name: docket-explanation-leans-only-on-ticked-quoted-documents
description: "A platform reviewer's test for necessary documents and evidence is wider than the Document check: every document or claim the explanation leans on must be ticked and quoted before hand-over"
metadata:
  type: feedback
  updated: 2026-10-12
---

## Current rule

Before any hand-over, walk the reasoning sentence by sentence and answer three things for each claim:

1. Which document supports it? If the step names a document, that document is ticked. A document that only
   establishes a condition or rules out an alternative (a State that might also have lacked the item, a list that
   shows nothing else qualifies) takes the form's "Exclusion / condition source" role with its reviewer note, saying
   what it rules out. Never write that a document is "not needed" inside a step that uses it.
2. Is there a verbatim quote for it under Evidence? Every State, entity or list the count depends on has at least one
   quote, and so does every side claim ("the other amendments are approved in no State").
3. Does the sentence describe the source exactly? Give a list's real size when taking part of it ("3 of the 5
   entries"), and say in the final step which items are excluded and why.

The platform's Document check asks only whether the answer changes when a ticked document is removed. It is the
narrower test. Leaving a document unticked because the check would call it "not needed" passes the gate and fails the
review.

**Why:** aq-02749 q02 passed at Medium and was returned by the platform reviewer on 2026-10-12 (second send-back;
panel verbatim in tasks/aq-02749/notes/feedback-q02.md): "The gold answer (10) is correct and both traps land ...
Please add Docs 3 and 4 as necessary documents, add the supporting quotes, and fix the wording in Steps 2, 4, 6 and
7." Rev 0's Step 4 used Virginia's and Louisiana's lists (Docs 3 and 4) and the "more prescriptive" amendments with no
tick and no quote, and its Step 2 said a five-entry list "holds three more". The same reviewer point was already in
the workspace notes from aq-01333 q01 ("the explanation and evidence not rely on the unmarked document"); I had filed
it under edition traps and did not apply it to a count whose condition rests on two more documents.

**How to apply:** `tools/check_questions.py` now WARNs when the reasoning names a Doc that is not ticked; treat that
WARN as blocking. Adding a tick changes the necessary documents and needs a new difficulty result, so settle the ticks
before the first run, not after a pass. In the hand-over, list the sentences the user must keep word for word when
rewording (the reviewer quoted reworded sentences that were less exact than the hand-over's). When the user reports a
send-back, ask for the panel itself: the first send-back on this question never reached the workspace and the second
arrived with "None of the changes requested in the previous send-back were applied". My reading, not the reviewer's
words: the three-question walk above.

## Evidence and history

- 2026-10-12, aq-02749 q02 rev 1: Docs 3 and 4 ticked as "Exclusion / condition source" (note: each rules out its
  State as a third one lacking a version), fifteen quotes added, Steps 2, 4, 6, 7 reworded as asked; question, answer
  and failure modes unchanged. New difficulty result pending. See [[docket-series-editions-necessity]] for when the
  exclusion role is not accepted (a document that rules out only its own content) and
  [[docket-accepted-question-is-finished]] for the revise-in-place procedure.

- 2026-10-13, aq-02749 q02 rev 1: the cost of settling ticks late. Ticking Docs 3 and 4 made a new version, and
  Run 2 measured the unchanged question and answer again: "Between levels", Low 0/5 · Medium 4/5, where Run 1
  had been Medium at 3/5 (tasks/aq-02749/verdicts/AQ-02749_difficulty_2026-10-13_0712.txt). The solver task was
  identical; the earlier pass no longer counted and the gate blocked resubmission. Rev 2 had to change the
  question (a second parallel count) to get a new result. A pass on a version whose ticks a reviewer would not
  accept is not a result to keep.

## Open case: the form refuses the tick (aq-03170 q01, 2026-10-12)

A three-name list in which two names each come from one document alone. Ticked as "Answer component", those two
documents drew the form's blocking check "Needs two or more documents": "You marked documents 3, 13 as necessary, but
the answer does not need them. Unmark them, or change the question so they are needed." They were unticked and kept
as evidence rows; the steps still name them. The question then passed at Hard and was submitted in that state, which
is the pattern reviewers returned on aq-01333 q01 and aq-02749 q02. Outcome at review, 2026-10-13: returned. "Question and gold are sound ... The only fix is tagging Docs 3 and 13,
which each uniquely support an answer item; then re-run the checks." and "both are in evidence and each changes
the answer if removed, so both must be tagged" (panel in tasks/aq-03170/notes/feedback-q01.md). So the
reviewer's rule overrides the form's check: a document that is the only source of an answer item stays ticked,
and a form check that refuses the tick is taken to the reviewer or an admin, never settled by unticking. The
untick cost a passed Hard result: rev 5 restores the ticks and needs a new difficulty run. That run (Run 3,
2026-10-13) measured Medium on a set whose Medium slots were full, with the question unchanged and the page's gate
changed in between. A forced re-run is a new measurement, not a formality: settle the marks by the sole-source
rule before the first difficulty run, and say so to the user before a returned question goes back to a run. Before the next difficulty run on such a list, try the tick with the
"Exclusion / condition source" role and its reviewer note (the form says a note sends the check to the reviewer
instead of blocking), and tell the user plainly which ticks the form refused. Author's reading, not platform words.
