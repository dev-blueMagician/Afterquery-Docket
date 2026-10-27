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
| f1 / aq-02157 / q01 | form state matching rev 1's question and gold (screenshot; reasoning box not shown) / rev 1 / 68b124f4... | form / precision advisory | runs/q01-r1-form-2026-10-08/form-screenshot-1.png: Gold answer box, orange: "Say the rounding (e.g. 'to one decimal place')." No length warning at 24 words. | rev 2 dfcb6b76...: question states "to one decimal place" (28 words); reasoning drops number-glued commas (v7 flags them) | repaired; platform pending |
| f2 / aq-02157 / q04 (cause revised under f4: position in the document, not the comma or £) | form state of rev 0 with the user's own rewording of Step 6 ("1.5028/6.9572=21.6%") / rev 0 / eac6be22... | form / reasoning number check | runs/q04-r0-form-2026-10-08/form-screenshot-2.png: "Step 1: Doc 2 doesn't mention £8.46. Check the document number." "Step 2: Doc 4 doesn't mention 122,. Check the document number." | rev 1 3bcdfbc8...: Steps 1-2 write amounts as "8.46 pounds" etc. and drop paragraph numbers; notes/helpers/form_check_v7.py reproduces both flags | repaired; platform pending |
| f3 / aq-02157 / q01 | rev 2 question/gold with user-reworded reasoning (text not captured; identity unresolved) | form / reasoning number check | runs/q01-r2-form-2026-10-08/form-screenshot-3.png: six "doesn't mention" flags (Steps 1, 2, 3, 4, 6, 13) on numbers printed only in Doc 3's and Doc 1's bulleted lists, and 15.6 | rev 3 fd3491df...: source numbers written once as "14.8 per cent" so later operands repeat the same strings; v8 predicted one flag each in Steps 1-2 (bulleted lists unread), which f5 disproved: Steps 1-5 now pass | resolved by the rev 3 form result (f5); Step 13 continues under f5 |
| f4 / aq-02157 / q04 | rev 1 with user-reworded Steps 5-6 (identity unresolved) | form / reasoning number check | runs/q04-r1-form-2026-10-08/form-screenshot-4.png: "Step 1: Doc 2 doesn't mention 8.46." "Step 2: Doc 4 doesn't mention 262.90." (f2's currency fix did not clear Step 1) | unchanged rev 1; both numbers printed far into the two longest documents; reported as checker false positives | open: ask whether these flags block Submit |
| f5 / aq-02157 / q01 | rev 3 with light user rewording of Steps 12-13 (identity close, unverified) | form / reasoning number check | runs/q01-r3-form-2026-10-08/form-screenshot-5.png: only "Step 13: Docs 3 and 1 don't mention 15.6." | rev 4 8d7023ee...: Steps 8, 10, 12 read "..., in per cent: 14.0 + 1.6 = 15.6 (the highest of the four)", so no "per cent" follows a reused result (every reused result so far was followed by "percentage points" or "pounds"); notes/helpers/form_check_v9.py reproduces rev 3's flag and clears rev 4; f3's list blind spot refuted (Steps 1-2 passed) | superseded by f6: the user's rev 4 wording ("in %:" before the expression) drew the same flag |
| f6 / aq-02157 / q01 | rev 4 with user rewording (Steps 8, 10, 12 "The rate for ... in 2030 in %: a op b = r (...)"; heads "(Step 8 & 10, Doc 3 and Doc 1)"; full text not captured, identity unresolved) | form / reasoning number check (same mechanism as f5, recurring) | runs/q01-r4-form-2026-10-09/form-screenshot-6.png: only "Step 5: Docs 3 and 1 don't mention 15.6." (no step numbered 5 holds 15.6; label unexplained) | rev 5 31ee6be2...: no subtraction of percentage-typed results; Step 13 2022 gap 14.0 - 13.9 = 0.1, Step 14 widening 1.6 + 7.2 = 8.8, Step 15 0.1 + 8.8 = 8.9, all "percentage points" (the aq-01543 q01 cure); notes/helpers/form_check_v10.py reproduces the flagged number for rev 3 and the user's rev 4 and clears rev 5 | repaired by restructure; platform pending: paste Steps 13-15 with numbers and "percentage points" unchanged; if any flag remains, copy the whole box text into the chat |
| f7 / aq-02157 / q04 | difficulty Run 1, "Version 37205a" (2026-10-08 18:52): the user's paraphrase of rev 1's question, quoted verbatim by every solver ("...increased from the pack insert impact assessment to the smoke free consultation?"), gold 21.6%; matches no local revision, not bound to 3bcdfbc8... | unsupported gold under the tested wording: the paraphrase dropped "response", so its literal endpoint is Doc 1's £7.87 (13.1%), not Doc 2's £8.46; High attempt 4: "the question says \"smoke free consultation\" not \"smoke free consultation response.\" So it should be Document 1." Difficulty observation: every Medium and High attempt computed Doc 4's MET floor (£6.9572) correctly | [verdict 19:19](../verdicts/AQ-02157_difficulty_2026-10-08_1919.txt); [re-capture 01:13, same run](../verdicts/AQ-02157_difficulty_2026-10-09_0113.txt): "Too hard", "Low 0/5 (1 not scored) · Medium 0/5 · High 0/5", "This question may be too vague: several solvers agreed on an answer that is not your gold \"21.6%\"..." | rev 2 7a76404e...: "to the government's response to the smokefree consultation" (saved rev 1 already said "smokefree consultation response"; rev 2 makes the referent survive paraphrase) | superseded by f8: the user's paraphrase of rev 2 kept the response wording but changed the asked quantity to an increase (Run 2) |
| f8 / aq-02157 / q04 | difficulty Run 2, "Version 0ef4f7" (2026-10-09 02:00): the user's paraphrase of rev 2, quoted verbatim by the solvers ("What is the increase in the minimum excise duty on a pack of 20 cigarettes, to one decimal place, from the pack insert impact assessment to the government's response to the smoke-free consultation?"), gold still 21.6%; not bound to 7a76404e... | unsupported gold under the tested wording (f7's paraphrase mechanism again, on the asked quantity): "increase" asks an amount; literal answer £1.5. Traces: High 5/5 £1.5 (MET £6.96 vs £8.46); Medium 0.5 x3 (£7.98 look-alike), 1.5, 0.9 (Doc 1's £7.87 as the response); Low 5/5 £0.6 (Doc 1's £7.87 as the start). Coach advice (name the MET, point to the table) not followed: it read 0/15 as unsolvable | [verdict 02:13](../verdicts/AQ-02157_difficulty_2026-10-09_0213.txt): "Too hard", "Low 0/5 · Medium 0/5 · High 0/5", "3 of 15 gave the same wrong answer: “0.5”", "may be too vague ... The solvers answered \"0.5\", ... **£0.6** ..."; "8 of 10 runs left · 7 of 50 runs used in the last 24 h (all tasks)" | rev 3 7790f824...: the Run 2 question word for word (origin user+claude), gold £1.5 (8.46 - 6.9572 = 1.5028), Step 6 states the rounding in words, FM3 = wrong-document link (£0.6) | resolved by the observed platform result: Run 3 on rev 3 passed In band — Medium tier (f9) |
| f9 / aq-02157 / q04 | difficulty Run 3, "Version 407f61" (2026-10-09 02:56): question = rev 3 word for word (closed-book quote L100), gold £1.5; platform diff from 0ef4f7 "answer: removed “21.6%”; added “£1.5”"; bound to rev 3 7790f824... (pasted reasoning/evidence not captured, not used by the measurement) | difficulty: pass at target | [verdict 03:42](../verdicts/AQ-02157_difficulty_2026-10-09_0342.txt): "In band — Medium tier", "Low 0/5 · Medium 2/5 · High —", "You can submit now.", "+$20 Medium+ bonus if accepted"; advisory "may be too vague" lists only trap answers (0.5 = £7.98 look-alike, £0.6 = consultation start) | rev 3 unchanged; status ready | resolved: difficulty at target. Submission, platform Checks and acceptance are the user's next steps and remain unrecorded |

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

- Summary: accepted TODO / enrolled TODO; known authoring minutes TODO; timing complete TODO
  of TODO; acceptance outcomes pending TODO; revisions TODO; ambiguity/necessity returns TODO.
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
