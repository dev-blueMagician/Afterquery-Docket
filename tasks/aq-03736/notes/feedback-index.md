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
| aq-03736-q01-F1 | Version 420741 / rev 0 / c845f26d... (question quoted word for word, gold equal, documents 3 and 1 left out in the Document check) | difficulty: one tier below target. One unpointed step (the exception closing D02 Article 37(1)(b)) held four of five low attempts; every pointed step was cleared by all five | [capture](../verdicts/AQ-03736_difficulty_2026-10-13_1002.txt): "In band — Easy tier", Low 1/5; user: "easy tier. but slots full for easy." | rev 0 unchanged; failure mode re-picked to the observed route (outside the fingerprint); routes in [q01](../questions/q01.md) Lever checks and Feedback log | historical for Medium: q01 held, no repair run (no second unpointed step outside the same sentence). Next: q02, then sketches i06 and i07 |
| aq-03736-q02-F1 | Run 2, Oct 13, 2026, 2:31 PM (version id not shown) / rev 0 / 0316bb7a... (question and gold shown word for word in the screenshots) | necessity: the answer is reached without Doc 3. In the documents: the gold equals every guidance item the proposal calls optional, so Doc 3 only confirms it. Difficulty: Low 2/5 | five user screenshots in chat, no saved page: "A marked document may not be needed ... without document 3"; "Low model 2/5 right"; rule-10 advisory on "in any order"; routes unread | q02 rev 0 unchanged and dropped; platform "What to change" items and the reviewer note not adopted; record in [q02](../questions/q02.md) | redesign: hook h1 closed. Next: quick tests of i07 and i09; i10 held |
| aq-03736-q01-F2 | Run 3, Version 6bde93 / rev 1 / 1355d693... (question quoted word for word, gold equal, "What changed" lists the rev 1 phrases) | difficulty: too easy at the Medium level, where the check began (Low not run). The exception that held the low solver in Run 1 was quoted by every medium attempt whose text is recorded; the one miss is the second reading of the proposal's first deadline (30 April 2028) | [capture](../verdicts/AQ-03736_difficulty_2026-10-13_1925.txt): "Too easy", Medium 5/6, "three solvers try up to 3 times each. Ready when at least two get it wrong twice and one gets it right twice"; Coach remedy not adopted | rev 1 unchanged and dropped; record in [q01](../questions/q01.md) | redesign: hook h15 closed after two measured versions. Next: i04, the last fair untested sketch |

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

- Summary for this bundle (2026-10-13): nothing enrolled here. The trial's five slots were already used by
  earlier bundles (workspace owner index), so aq-03736's candidates are tracked as unpromoted. Known
  authoring time: one sketch interval for i01 (31 minutes); the rest untimed, coverage partial. No platform
  attempts, revisions or returns yet.
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
