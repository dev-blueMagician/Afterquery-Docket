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
| r1 / aq-01937 / q02 | form quick test (easier solver), user report 2026-10-08; tested wording not supplied; rev 1 (53dd017c...) assumed, unverified | difficulty: quick test "too easy" (gold reached) | user report "q02 and q03 are too eash to pass quick test" ([q02 Feedback log](../questions/q02.md)); no panel supplied | no repair: renamed-caption mapping is stated by Doc 9's note (local inference) | dropped; replaced by round-3 hooks ([ideas](ideas.md)) |
| r2 / aq-01937 / q03 | same report; rev 1 (993076f2...) assumed, unverified | difficulty: quick test "too easy" (gold reached) | same user report ([q03 Feedback log](../questions/q03.md)) | no repair: second failure of the Doc 9 reclassification family | dropped; redesign with other documents and mechanisms |
| r3 / aq-01937 / q01 (user named "q02") | Targeted failure modes box on the form, user screenshot 2026-10-08; the box held q01 rev 3's old FM1 "Where the trap sits" text (95 words, AUM) | form: the form now has one shared "Why these are traps" box, at most 50 words; Submit blocked: "95 / 50 words — shorten it to submit" | screenshot in session (traps "Part vs total"/"Takes the wrong line item" and "Linking across documents"/"Misapplies a rule or premise") | q01 failure modes rewritten as one 47-word reason, same traps and causes (outside the fingerprint, rev 3 unchanged); floor, handover and JSON updated to the new form | repaired, platform pending: paste the new reason from [handover-q01](handover-q01.md) |
| r4 / aq-01937 / q01 | platform difficulty check Run 1, 2026-10-08 12:30 PM, version d017fd; question and gold verbatim = revs 1-3; reasoning/evidence/ticks not captured, no hash | difficulty: Too hard (Low 0/5 · Medium 0/5 · High 0/5) with "may be too vague" note; all 15 attempts took total AUM, 22.69% | [verdicts/AQ-01937_difficulty_2026-10-08_1238.txt](../verdicts/AQ-01937_difficulty_2026-10-08_1238.txt) | rev 4: question says the asked assets are not all of reported AUM; gold 22.40%, documents and inputs unchanged ([q01](../questions/q01.md)) | repaired (rev 4), platform pending; re-captured 13:59 ([verdicts/AQ-01937_difficulty_2026-10-08_1359.txt](../verdicts/AQ-01937_difficulty_2026-10-08_1359.txt)), same Run 1 now "for an earlier version", not a new result |
| r5 / aq-01937 / q01 | form quick test, user report 2026-10-08; tested wording not supplied; rev 4 (84dca06a...) assumed, unverified | difficulty: quick test "too easy" (gold reached) | user report "q01 and q04 is too easy to pass quick test" ([q01 Feedback log](../questions/q01.md)) | rev 5: midpoint wording "actually the investment manager" between rev 3 (Too hard) and rev 4 (too easy); last step for this family | repaired, platform pending |
| r6 / aq-01937 / q04 | same report; rev 1 (8bf47c84...) assumed, unverified | difficulty: quick test "too easy" (gold reached) | same user report ([q04 Feedback log](../questions/q04.md)) | no repair: labelled inputs and a short identity; decoy disarmed in its own sentence | dropped |
| r7 / aq-01937 / q05 | user report "q05 is too hard"; no q05 text in the attached capture ([verdicts/AQ-01937_difficulty_2026-10-08_1359.txt](../verdicts/AQ-01937_difficulty_2026-10-08_1359.txt) holds only q01's stale Run 1); tested version unknown | difficulty (identity unresolved) | user report only | rev 2: "published before it launched" removes the reading that points at the launch release's own figure | repaired, platform pending; re-checked after the user said both files were verdicts: the 13:59 file is q01's Run 1 only, no q05 capture exists; ask for a capture saved after q05's own run |

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
- Candidate rows used: 2 / 5 in this bundle (workspace ledger slots 4 and 5; slots 1-2 are aq-01960, slot 3 aq-02028). q01-q03 were promoted before enrollment and are not tracked.

| Slot / bundle / candidate | Promoted date / question link | Actual authoring minutes / timing coverage | Reported tokens / coverage | Distinct platform attempts | Revision rounds | Ambiguity / necessity returns | Observed acceptance / raw link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 / aq-01937 / i14 | 2026-10-08 / [q04](../questions/q04.md) | 3.7 measured (sketch 2.7, draft 1.1, ledger); partial: the round-3 hook search before 15:11Z was untimed and covered i14 and i15 together | unknown / no runtime usage report | 0 identified | 1 (rev 1, reasoning reformatted for the form's number check before hand-over) | 0 / 0 | retired before submission (dropped 2026-10-08 after the quick test was too easy, r6) |
| 5 / aq-01937 / i15 | 2026-10-08 / [q05](../questions/q05.md) | 6.0 measured (draft, ledger; it also covered q04's rev 1); partial: its sketch work sits in the untimed search and in i14's sketch interval | unknown / no runtime usage report | 0 identified | 2 (rev 1 reasoning format; rev 2 "published before it launched" after the user's "too hard" report, r7) | 0 / 0 | pending |

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
