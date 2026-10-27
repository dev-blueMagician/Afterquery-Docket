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
| F1 / aq-05177 / q01 | Checks page saved 2026-10-14 22:18; identity not bound (no question text in capture; gold matches rev 0 26b60f03...); stale reload notice | ambiguity / both form solvers answered the formation sentence's single partner, "Providence Health System"; the second member (Cedars-Sinai) is shown only in a later call's passing "three-way joint venture" | [capture](../verdicts/AQ-05177_checks_2026-10-14_2218.txt); One defensible answer Failed (blocking); Left-out items Warning (advisory) | rev 1 = sketch i07, scope "Judging by RadNet's 2024 earnings calls together" (precedent aq-03170 q01 rev 4); local screen 3/3 right; prepared 4e45cb12..., 0 FAIL / 3 WARN | redesign / hook dropped: rev 1 quick test "too easy for quick test" (user, 2026-10-15); q01 status dropped, not submitted |
| F2 / aq-05177 / q02 | Checks screenshots 2026-10-15; question, gold, components, evidence = rev 0 as handed over; reasoning user-rewritten (not bound to ff159cfc...) | form / One defensible answer Passed; Answer matches a stated figure Failed (year digits read as figures); Partial answers warning ("at least one"); Evidence supports its component warning (exclusion and cross-component quotes) | [screenshots](platform-feedback/) q02-checks-2026-10-15-1..4.png | rev 1 = sketch i08 ("change any guidance range"; answer "May, November"; evidence re-mapped); local screen 3/3 right; prepared 4ef235de..., 0 FAIL / 4 WARN (explained) | difficulty: Run 1 (10-15, Version 5bc90a, gold = rev 1) "Low — · Medium — · High 3/3" Too easy ([capture](../verdicts/AQ-05177_difficulty_2026-10-15_1202.txt)); routes unread / hook dropped, q02 status dropped, not submitted |
| F3 / aq-05177 / q03 | Run 2, Oct 15 5:18 PM, Version ecf6e0; question quoted verbatim, answer = gold of rev 0 (366930...) | difficulty / "Low — · Medium — · High 3/3" Too easy (extra run); routes unread; Coach: the scope phrase pointed at Doc 4's eRAD carve-out | [capture](../verdicts/AQ-05177_difficulty_2026-10-15_2111.txt) | rev 0 unchanged; Platform validation record (fail) | hook dropped, q03 status dropped, not submitted |
| F4 / aq-05177 / q04 | quick test of rev 0 (bare answer "3 guidance ranges"), user 10-15 | difficulty (quick test, easier solver) / failed; the earlier survival was graded against my longer answer text | user chat: "both failed in quick test" | rev 0 unchanged | dropped, not submitted |
| F5 / aq-05177 / q05 | quick test of rev 0 (bare answer "-$3 million"), user 10-15 | difficulty (quick test, easier solver) / failed; the earlier survival was graded against my longer answer text | user chat: "both failed in quick test" | rev 0 unchanged | dropped, not submitted |

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
