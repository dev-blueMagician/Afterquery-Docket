# aq-01333 q01 platform feedback

Platform question: q01 rev 4 as submitted on 2026-10-07. The difficulty check passed at the Easy tier
(user report; fingerprint d148e751cf7ef42418e3e374f6672649b90314806aee7be83f80462311cf9964). The form at
submission had Doc 4 and Doc 6 as "Answer component" and Doc 5 as "Exclusion / condition source" with the
reviewer note. The form's evidence rows were not in the local order. The reviewer calls the Doc 5 completion
quote "Evidence row 3" and Doc 6's "In May 2026 ..." quote "your own evidence row 4". The form's row 3 held the
longer quote "HPE also notes that the divestiture of its stake in H3C Technologies Co., Limited was completed
on May 28".

## 2026-10-07, platform review: Revision requested (screenshot supplied by the user)

Source: screenshot of the Edit Task AQ-01333 page, saved as
runs/q01-r4-v2-d148e751.../results/platform-review-revision-requested.png. Transcribed verbatim:

> Revision requested
> - Remove Doc 5 from the necessary documents, leaving Doc 4 and Doc 6, and delete the author's note. Go to Necessary documents
> - Drop evidence row 3. Rewrite step 2 along these lines: "Doc 6 dates the sale to May 2026. Doc 4 (March 9, 2026) is the latest full-year forecast issued before May 2026, so its range of $2.30 to $2.50 was in force." Go to Evidence
>
> The question and gold (58.3%) are correct, so nothing there needs to change. Doc 5 isn't necessary, though: the check reached 58.3% without it, because Doc 6 already dates the sale to May 2026 ("In May 2026, the Company sold the remaining equity interest in H3C"), and that places it after Doc 4's March forecast. Please unmark Doc 5, delete the note, drop its evidence row, and rely on Doc 6 for the sale timing in step 2.
>
> Issues the reviewer found
>
> Other · Other
> Necessary documents: Doc 5 is marked as an "Exclusion / condition source", but the answer doesn't depend on it. The document check reached the gold without it ("Without document 5 — 58.3%"). The sale date isn't unique to Doc 5: Doc 6 says "In May 2026, the Company sold the remaining equity interest in H3C" (your own evidence row 4), which places the sale after Doc 4's March 9 forecast. Doc 5's role in the note is only to rule out its own June 1 range ($3.35 to $3.45), and without Doc 5 that range doesn't exist to rule out. So the note doesn't make Doc 5 necessary.
>
> Evidence · Wrong / missing evidence
> Evidence row 3 and explanation step 2 rely on Doc 5 ("HPE also notes that the divestiture of its stake in H3C Technologies Co., Limited was completed on May 28"), but Doc 6's quote "In May 2026, the Company sold the remaining equity interest in H3C" already establishes when the sale happened.

observed_platform_status: revision requested (not accepted, not rejected).

Assessment:
- The reviewer accepts the question and the gold. The request covers only the document marks, the note,
  one evidence row and explanation step 2.
- The finding matches local evidence. The rev 0-3 reviews named D01 + D05 (Doc 4 + Doc 6) as the smallest
  set. The rev 4 review found that without D03, D05 l.644 "In May 2026" still selects March and gives
  58.3%, so Doc 5 is not needed for the value.
- Rev 4 had ticked Doc 5 because the platform's printed rule counts a document as needed "when it is the
  only document naming an item you marked it as excluding". The reviewer read that rule narrowly. A
  document that rules out only its own item is not made necessary by the exclusion role, because without
  the document there is nothing to rule out.
- Consequence: an edition trap's decoy-carrying release stays unticked when another necessary document
  dates the event. That was the rev 0-3 practice.
- The tier result is unaffected: what solvers see (question plus bundle) is unchanged.

## 2026-10-07, the user's form while revising (screenshot)

User: "how to fix?" with a screenshot of the form, saved as
runs/q01-r4-v2-d148e751.../results/form-evidence2-not-verbatim.png. It shows "Evidence 2" marked "NOT
VERBATIM". The Document field reads "Doc 6 · 8-K · fy2026 · hewlett-packard-enterprise-company-q3-f…" and
Proves component reads "1. 58.3%". The box holds the reviewer's suggested step-2 sentence.

Cause: the step-2 rewrite belongs to the Solution explanation. An evidence box accepts only text copied
word for word from the selected document. The review panel's "Go to Evidence" link sits beside the
step-2 bullet (it refers to dropping row 3), which invited pasting the sentence into Evidence row 2.

Response: the rev 5 fields were handed over in labelled blocks (see q01.md rev 5):
- evidence: exactly five Doc 4/Doc 6 rows, with every Doc 5 row deleted;
- necessary documents: Doc 4 and Doc 6 as "Answer component", Doc 5 unticked and the note deleted;
- explanation: the reviewer's step 2 verbatim; Step 3 shortened because Step 2 now names the range;
- Step 1's quote: the period moved outside the quotation marks, because only Doc 5 prints the sentence
  with a period;
- decoy line: rephrased to use only Doc 5's own date, with no reference to the completion.

Verified before hand-over:
- all five quotes occur once, word for word, in text/;
- every number in each step is printed in a document the step names, or follows "=";
- (3.80 - 2.40) / 2.40 = 58.333% -> 58.3%.

## 2026-10-07, form: Targeted failure modes (two screenshots)

The user asked "which one should I select?" about a new required form section, saved as
runs/q01-r5-v2-f6b3318d.../results/form-targeted-failure-modes.png and -options.png. The form's text:
"Before you submit, name the 1 to 3 traps your question sets for a careless solver, and how that solver
goes wrong. Pick only traps your question really sets: the reviewer reads your reasons." It also shows
"Declare at least one before you submit (at most 3)."

Recommended:
- "Wrong year or edition": Doc 5's June 1 range, which gives 11.8%.
- "Superseded date or version": Doc 3's December 2025 range, which gives 61.7%.

The reasons for both are in q01.md Lever checks (Revision 5).

Resubmission and any new difficulty result: pending (user).

## 2026-10-08, the same panel sent again (screenshot, no message)

The user sent a new screenshot of the Edit Task AQ-01333 page, saved as
runs/q01-r4-v2-d148e751.../results/platform-review-revision-requested-2026-10-08.png. Its "Revision requested"
panel is word for word the one transcribed above: both bullets, the summary paragraph and both reviewer issues.
This capture also shows a line below the panel that the cropped 2026-10-07 capture does not:

> Still open on this set: Hard, Medium, Easy.

It is a standing line of the task page. The 2026-10-06 capture already had it (AQ-01333_2026-10-06_1150.txt
L172), above "Question slots" and "Hard 0/2 · Medium 0/3 · Easy 0/1" (L174-177).

Reading:
- The page still shows the rev 4 return. No newer review result is visible.
- Each tier still has at least one open slot. Easy has a single slot, so it is unfilled while q01 is returned.
  The line does not show whether any Hard or Medium slot is taken.

Response:
- Rev 5's local fields were checked again against the panel, field by field. Doc 5 is not a listed document, and
  no note is written. No Doc 5 evidence row remains (five Doc 4/Doc 6 rows). Step 2 is the reviewer's sentence,
  character for character. The question and gold are unchanged, as the reviewer asked. The form must be set to
  match; its current state is not visible here.
- Two items were still open, and both are now done:
  - The form's Targeted failure modes. The section existed at the 2026-10-07 hand-over and two traps were
    recommended in chat, but nothing had been written into q01.md. It is now written with one trap: Wrong year or
    edition (Doc 5's June range, 11.8%). The December trap is withdrawn (q01.md Lever checks).
  - The removal probes the user required on 2026-10-08, run on the rev 5 fingerprint, one per ticked document
    (results under Blind solve in q01.md). Both miss.
- An independent review of these additions (fresh question-review agent, raw:
  runs/q01-r5-v2-f6b3318d.../results/review-additions-2026-10-08.md) gave these verdicts: probes pass, hand-over
  matches, failure mode "revise" for one overclaim, records "not accurate" (minor). The overclaim was that the
  boxes called Doc 5 "the release that reports the sale", when Doc 6 reports it too. The overclaim and the record
  errors were fixed the same day.
- The whole form was handed over again from `check_questions.py --handover` (notes/handover-q01.md).
- The platform needs a new difficulty result before resubmission. Rev 5 unticks Doc 5, and the run history says
  "any edit to the question, answer or necessary documents needs a new result".
