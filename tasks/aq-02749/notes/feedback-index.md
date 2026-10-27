# Feedback index

Keep concise rows linking raw returns, current fixes and status. Raw platform words stay in
the linked artifacts/feedback notes; this index does not replace exact-content records.
Never edit submitted/accepted question files to maintain it.

## Active issues

Triage each exact tested version once. Key by bundle/question + platform version + issue;
record revision/fingerprint when established. Distinguish platform observations from the
author's inference. Categories: ambiguity, necessity, unsupported gold, form, difficulty,
identity. One mechanism per row is enough; use short phrases and links, not essays.

| Issue id / bundle / question | Tested platform version / rev / fingerprint | Category / mechanism | Raw feedback links / platform observation | Current version / author comparison or fix link | Status / next action |
| --- | --- | --- | --- | --- | --- |
| P1 / aq-02749 / q01 (sketch i01) | form quick test 2026-10-10; wording taken as q01 rev 0 (1ce4f588..., assumed, panel not pasted) | difficulty / one scenario total over three State procedures, four cells each following a different stated rule, with two classification steps and a zero cell | user chat: "both of them too easy to pass quick test" (questions/q01.md Feedback log) | none: dropping the stated conditions would leave the total undetermined | historical: q01 dropped, hook h25 closed |
| P2 / aq-02749 / i02 | form quick test 2026-10-10; sketch wording (notes/sketches/i02.md, answer 33 days; panel not pasted) | difficulty / one State rule applied to five federal hearing and deadline pairs | same user message | none | historical: i02 dropped, hook h26 closed |
| P3 / aq-02749 / i03, i04 -> q02 | form quick tests 2026-10-10; sketch wordings (notes/sketches/i03.md, i04.md, answer "10 amendments" each; panels not pasted) | survived (no panel text) / approval matrix over four itemised lists and one proposal with none | user chat: "by the way, i03, i04 both of them survived"; same message: "after checking difficulty, it blocks easy tier. So we must target at medium or hard." | q02 rev 0 adopts i04's wording unchanged (8f894659...); i03 held as the sibling | resolved by observed platform result (P4) |
| P4 / aq-02749 / q02 | difficulty check Run 1, Version 94672c (current), Oct 11, 2026, 10:34 AM; rev 0, tested_sha256 8f894659... (question, gold and marked documents verified from the capture; other boxes not captured) | difficulty / approval matrix over four itemised lists with Wyoming's grouped item counted in every entry: "In band — Medium tier", Low 0/5 (0, 0, 0, 0, "One"), Medium 3/5 (misses 9 and 6); Document check needed Docs 5, 6 and 2; closed-book needed the documents | [verdicts/AQ-02749_difficulty_2026-10-11_1128.txt](../verdicts/AQ-02749_difficulty_2026-10-11_1128.txt); user chat: "submitted as medium tier. Check the verdict and improve your performance"; the same run captured again with every Reasoning block loaded: [verdicts/AQ-02749_difficulty_2026-10-12_0028.txt](../verdicts/AQ-02749_difficulty_2026-10-12_0028.txt) (re-sent artifact, no new run), user chat 2026-10-12: "plz check arrived verdicts, find out what you missed and improve your performance" | none needed in the question; the first reading of the routes was wrong for both medium misses and incomplete for the low ones, corrected 2026-10-12 in [feedback-q02.md](feedback-q02.md) | resolved by observed platform result: Medium, at target; q02 submitted; then returned by the reviewer (P5) |
| P5 / aq-02749 / q02 | platform review, "Revision requested", second send-back, screenshot 2026-10-12; tested content: the submitted form (rev 0's question, gold and Docs 2, 5, 6; reasoning reworded before submission, not captured); the first send-back was not supplied | necessity + unsupported gold (evidence) + form (wording) / Docs 3 and 4 unticked and unquoted although the count depends on Virginia and Louisiana approving all twenty; no quote for the "more prescriptive" amendments; Step 2 said three entries where the list has five; Steps 6 and 7 unclear | [verdicts/AQ-02749_revision-requested_2026-10-12.png](../verdicts/AQ-02749_revision-requested_2026-10-12.png); panel verbatim in [feedback-q02.md](feedback-q02.md); reviewer: "The gold answer (10) is correct and both traps land, so no change to the question or answer is needed." | rev 1 (1b42e10a...): Docs 3 and 4 ticked as "Exclusion / condition source" with reviewer notes; fifteen quotes added; Steps 2, 4, 6, 7 reworded as asked; question, answer, component, tags and failure modes unchanged | repaired; rev 1's own difficulty result failed the gate (P6), so rev 2 carries these changes forward |
| P6 / aq-02749 / q02 | difficulty check Run 2, Version 54eee2 (current), Oct 13, 2026, 12:56 AM; rev 1, tested_sha256 1b42e10a... (question and gold verified from the capture; "What changed before this run: the documents or the documents marked necessary changed") | difficulty / the same question and answer as Run 1, re-measured after the ticks changed: "Between levels", Low 0/5 (0, 0, 0, 3, 0), Medium 4/5 (one miss read only the more prescriptive list; one right attempt has no text recorded); High not run; no Document check in this run | [verdicts/AQ-02749_difficulty_2026-10-13_0712.txt](../verdicts/AQ-02749_difficulty_2026-10-13_0712.txt); page: "Too hard for the low model but too easy for the medium model. Make it a little harder"; Coach: define the term in the question (not taken: it names both lists; its account of the low attempts is contradicted by their Full answers); user chat 2026-10-13: "plz check arrived verdicts by using your feedback skill and fix" | rev 2 (f8ddf50d...): a second parallel count, "and how many in all five?", gold "10, 12"; five of six recorded right medium attempts never used the second list, which that count needs; rev 1's reviewer changes kept (questions/q02.md Lever checks) | resolved by observed platform result: Run 3 counts Low 0/5, Medium 2/6 (P7) |
| P7 / aq-02749 / q02 | difficulty check Run 3, Version e40592 (current), Oct 13, 2026, 10:41 AM; rev 2, tested_sha256 f8ddf50d... (question and gold verified from screenshots and the page's change list; other boxes not shown) | necessity / the high model reached the answer without Doc 3 and without Doc 4, the two documents the reviewer asked to be ticked as "Exclusion / condition source": "A marked document may not be needed", gate does not pass, Submit blocked. Counts: Low 0/5, Medium 2/6. Advisory Warnings only: "Left-out items do not qualify" (the gold's digits 12 and 10 matched a date in Doc 1, a page number in Doc 2 and a date in Doc 4) and "Each description fits one thing" ("all five" and the amendments phrase match prose in several proposals) | screenshots verdicts/AQ-02749_form_2026-10-13_run3_question-gold.png, _checks.png, _difficulty.png, _history.png; Coach ("Make it depend on the marked documents") says high attempts 2 and 5 reached the gold without Document 2, which the gate's own banner does not say (it names 3 and 4 only): unverified, no text capture | none in the content; the one-line reviewer note for the difficulty check handed over (questions/q02.md Feedback log) | resubmitted 2026-10-13 with the one-line note (user chat: "submitted with that note. Let's wait for the result"); submitted at the Medium tier (user, same day: "oh, it was medium tier"); Run 3 text capture not supplied, routes unread; page then showed "Review Ready" with the 2026-10-12 panel re-shown (verdicts/AQ-02749_review-ready_2026-10-13.png: same artifact as P5, no new return); review outcome pending |

Statuses may be unresolved identity, open, repaired/platform pending, resolved by observed
platform result, historical, or redesign. A local repair is not a platform pass. Preserve
prior raw feedback and fixes through links when updating a row.

- Re-sent screenshots of the same version/issue link to the same row, with no new failure or
  return count. Compare the tested content with the current draft before changing it.
- Unknown versions get distinct receipt ids and stay unresolved. Do not group unrelated
  returns under a shared `unknown` key; merge only with evidence of the same tested version
  and issue, or an identical re-sent artifact. Never infer a current fingerprint from a qNN.
- Make one focused repair for a mechanism. If the same failure is demonstrated on that
  repaired exact version, redesign the hook; stale/duplicate/unknown feedback does not show
  recurrence. No automatic local model validation follows intake or repair.

## Next five newly promoted candidates

Use one owner index for the five-candidate trial, including if it spans bundles; link it from
other bundle sessions. Add each newly promoted candidate once. Resume/revision keeps its row;
a genuinely new hook promoted as a new candidate gets a new row. Do not enroll old candidates
retrospectively or reset the count when changing bundles. Stop enrolling after five.

- Trial owner index / start: [workspace owner](../../../notes/feedback-index.md); start recorded in the shared ledger
- Candidate rows used: 0 / 5

| Slot / bundle / candidate | Promoted date / question link | Actual authoring minutes / timing coverage | Reported tokens / coverage | Distinct platform attempts | Revision rounds | Ambiguity / necessity returns | Observed acceptance / raw link |
| --- | --- | --- | --- | --- | --- | --- | --- |

Record actual active candidate authoring/revision minutes as work happens, including any
already timed sketch work; exclude idle/platform waiting. Keep brief dated increments in the
minutes cell or a linked session note and mark coverage complete or partial/unknown. Never
estimate missed time afterward. A promotion does not make unrecorded earlier work known.
Revision rounds count distinct edits after first promotion, not duplicate screenshots or
resumptions. Count each distinct platform return once per applicable ambiguity/necessity
category, linked to its issue row; unknown identity stays uncounted/pending until resolved.
Acceptance records the actual platform observation (accepted, rejected or pending) with its
raw link; a difficulty pass or local repair is not acceptance. A candidate retired before any
submission is recorded as not submitted/retired: zero acceptances, no platform verdict claimed.
Retirement after submission does not settle a pending platform outcome.

- Summary: not enrolled (the workspace trial of five candidates is full, per aq-02626's 2026-10-10 checkpoint);
  no rows, no timer and no measured minutes for this bundle.
- Accepted questions per known authoring hour: pending. Once all five have complete timing
  and settled outcomes (including retired before submission), compute accepted count / (total recorded minutes / 60), including
  time spent on unsuccessful candidates. No rate claim while either is incomplete or the
  denominator is zero; report known counts/minutes without treating partial time as a total.

## Measured events

Use the single workspace `notes/efficiency.json` ledger; this table links its report, rather than
maintaining a second set of totals. Start/stop timers and promote candidates through
`python tools/docket_agent.py efficiency` (WORKFLOW section 11). Keep stable candidate IDs across
work sessions and revisions. Do not enroll pre-existing questions or reconstruct their history.

For `record --event PATH`, save a JSON object with `kind`, a stable `event_id`, the bundle slug in
`bundle`, the tracked `candidate`, and `source` pointing to the actual trace/return/session evidence.
Add the fields below. Illustrative field names are a contract, not recorded measurements.

| Kind | Additional fields |
| --- | --- |
| `usage` | `total_tokens`: nonnegative integer reported by the runtime/API |
| `platform_attempt` | `attempt_id`: identified platform run; `stage`: `quality`, `difficulty` or `review`; `revision`: nonnegative integer; `tested_sha256`: verified prepared fingerprint |
| `revision` | `revision`: actual post-promotion revision number; `tested_sha256`: content fingerprint |
| `outcome` | `outcome`: `accepted`, `rejected`, `pending` or `retired_before_submission` |
| `coverage` | `timing` and `tokens`: each `complete`, `partial` or `unknown`; source explains coverage |

One usage event represents one non-overlapping reported usage interval/request; use its stable
receipt ID and do not record overlapping session and request totals. Missing usage stays unknown;
zero requires a reported zero. Do not substitute document-token counts or estimates. Repeated event
IDs with the same data are harmless; conflicting reuse is rejected. Duplicate identified runs or
revision snapshots do not increase counts. Keep unresolved run identity in feedback notes until known.

The `source` records provenance, not an independent verification of the supplied value. Acceptance
must be an observed platform outcome, not inferred from a difficulty pass. Confirm timing/token
coverage only when the measured records cover the relevant work; future work needs reconfirmation.
Stop timers before waits and turn end; discard an interrupted interval whose active time is unknown.
Unpromoted work and incomplete coverage remain visible. No metric triggers new model validation.
