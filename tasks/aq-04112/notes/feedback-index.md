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
| r1 / aq-04112 / q01 (sketch i01) | Form quick test, 2026-10-13. Wording not captured: the sketch sentence as handed over, or the user's rewording. Not bound to e2a10d7d... | difficulty (preliminary screen) / a cost built from a table's unit costs beside its printed total and rounded rate | User chat, verbatim: "i02, i01 survived. others not tested". No panel, no trace. Logged in [q01.md](../questions/q01.md) Feedback log. | q01 rev 0, the sketch sentence unchanged. No fix needed. | resolved by r10. |
| r2 / aq-04112 / q02 (sketch i02) | Form quick test, 2026-10-13. Wording not captured, as r1. Not bound to 4e6e6e74... | difficulty (preliminary screen) / a threshold derived from a rule beside its printed unreduced figure | Same user message as r1. Logged in [q02.md](../questions/q02.md) Feedback log. | q02 rev 0, the sketch sentence unchanged. No fix needed. | resolved by observed platform result: see r3. |
| r3 / aq-04112 / q02 | Difficulty Run 1, Oct 13, 2026, 4:05 PM, Version 402a46 (current). Bound to rev 0, 4e6e6e74..., for question and answer (question quoted word for word, gold equal); no Document check ran. | difficulty / every step reached from the question's premise; one wrong answer in five, from a reading of the question's own phrase | [capture](../verdicts/AQ-04112_difficulty_2026-10-13_1701.txt): "The difficulty check finished: Too easy." "Low model: 4 of 5 attempts right". "Too easy, so you got an extra run." Closed-book: "Needed the documents". Routes in [q02.md](../questions/q02.md) Feedback log. | q02 dropped, no repair (no unpointed step to build on). Lesson applied to q01 before its first run (rev 1). | resolved: hook h2 closed. Next: q01 rev 1 run; quick tests of i06, i07, i03. |
| r4 / aq-04112 / q03 (sketch i06) and sketch i07 | Form quick tests, 2026-10-13. Wordings not captured: the sketch sentences as handed over, or the user's rewordings. Not bound to 98b7ef02... | difficulty (preliminary screen) / a three-name list across two hearings; i07 named the paperwork, i06 names no trade | User chat, verbatim: "i06 survived, i07 failed". No panel, no trace. Logged in [q03.md](../questions/q03.md) Feedback log and sketches/i07.md. | q03 rev 0 (opening reworded, surname order); i07 dropped. | superseded by r5. |
| r5 / aq-04112 / q03 rev 0 | Form quick test, 2026-10-13, on rev 0's reworded sentence (assumed as handed over; no panel). Not bound to 98b7ef02... | difficulty (preliminary screen) + author error / a quick-test survivor's sentence was changed at write-up and the changed sentence failed | User chat, verbatim: "why is q3 different from i06? Anyway, q3 failed to pass quick test. Idiot". Logged in [q03.md](../questions/q03.md) Feedback log. | q03 rev 1 (draft): the sketch i06 sentence and answer restored word for word. | resolved by r6. |
| r6 / aq-04112 / q03 rev 1, q01 rev 1, sketch i03 | Form quick tests, 2026-10-13, on the three sentences given word for word in the preceding message (no panels; not bound to fingerprints). | difficulty (preliminary screen) | User chat, verbatim: "i06, q01 survived, i03 failed". Logged in [q03.md](../questions/q03.md) and [q01.md](../questions/q01.md) Feedback logs and sketches/i03.md. | q03 rev 1 and q01 rev 1, sentences unchanged; i03 dropped. | q03: resolved by r7. q01 rev 1: resolved by r10. |
| r7 / aq-04112 / q03 rev 1 | Difficulty Run 2, Oct 13, 2026, 8:21 PM, Version baa047 (current). Bound to rev 1, 2b2b333b..., for question and answer (change list and three full quotes of the question; gold equal); no Document check ran. | difficulty / a three-name list whose members each carry the asked property word beside a number: found by a solver that goes through both transcripts | [capture](../verdicts/AQ-04112_difficulty_2026-10-13_2122.txt): "The difficulty check finished: Too easy." "Medium model: 4 of 6 attempts right". Tiers "Low — · Medium 4/6 · High —": the check started at the medium level. "Too easy, so you got an extra run." Closed-book: "Needed the documents". Routes in [q03.md](../questions/q03.md) Feedback log; medium 3 and 6 unrecorded. | q03 dropped, no repair (coach's suggestions are a paraphrase and more look-alikes, both of a cleared kind). | resolved: hook h14 closed. Next: q01 rev 1 run (form unchanged); sketch i10 for a quick test (i09 was rejected before a file was written). |
| r8 / aq-04112 / q04 (sketch i10) | Form quick test, 2026-10-14, on the sketch sentence and answer given word for word in the preceding message (no panel; not bound to ca843e5c...). | difficulty (preliminary screen) / a two-list match whose asked property has no keyword; one member named only by a short form | User chat, verbatim: "survived". Logged in [q04.md](../questions/q04.md) Feedback log and sketches/i10.md. | q04 rev 0, sentence and answer unchanged; checked, 0 FAIL, 1 WARN, fingerprint ca843e5c... | resolved by r9. |
| r9 / aq-04112 / q04 rev 0 | Difficulty Run 3, Oct 14, 2026, 9:13 AM, Version daf97b (current). Bound to rev 0, ca843e5c..., for question and answer (the change list rebuilds the question word for word; gold equal); no attempt text, no Document check shown. | difficulty / a two-list difference plus a name search: done in full by the high model | [capture](../verdicts/AQ-04112_difficulty_2026-10-14_0915.txt): "The difficulty check finished: Too easy." "- High model: 3 of 3 attempts right". Tiers "Low — · Medium — · High 3/3": the check went straight to the high model. Note on attempt 2: the lists "pre-compute the set difference, leaving only a literal string match". Closed-book: "Needed the documents". Coach not loaded. | q04 dropped, no repair (no attempt missed, so no step held). | resolved: hook h16 closed. Next: q01 rev 1 run (form unchanged), expected at the high level; then report options. |
| r10 / aq-04112 / q01 rev 1 | Difficulty Run 4, Oct 14, 2026, 9:32 AM, Version cfc84c (current). Bound to rev 1, e21fa8ca..., for question and answer (closed-book quotes the question word for word; change list agrees; gold equal); no attempt text, no Document check shown. | difficulty / a table-built cost whose one unscaled line held nobody | [capture](../verdicts/AQ-04112_difficulty_2026-10-14_0937.txt): "Too easy" "- High model: 3 of 3 attempts right". Tiers "Low — · Medium — · High 3/3": straight to the high model. Notes: "including the one-off sponsor fee"; "the table's printed 50-worker total also allows direct scaling". Closed-book: "Needed the documents" (£97,500). Coach: drop the signposting; ask the one-off part separately or use another head count. | q01 dropped, no repair (no step held; the Coach's suggestions are a paraphrase and a cue). | resolved: hook h1 closed. Every candidate measured below target; options reported to the user. |

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

- Summary: q01 (i01) and q02 (i02) were promoted on 2026-10-13 after their quick tests; enrolment status is
  in the bundle's session note. Earlier state: no promoted candidate (five sketches), nothing enrolled; the
  workspace trial's five slots were already taken when sister bundles tried to enrol the same day. One sketch
  interval for i01 is timed in ../../../notes/efficiency.json; it was started after the documents had been
  read, so timing coverage is partial. No platform result, no revision, no ambiguity or necessity return.
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
