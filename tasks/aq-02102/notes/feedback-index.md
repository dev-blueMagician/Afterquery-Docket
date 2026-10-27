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
| F1 / aq-02102 / q01 | form paste of rev 1 (8b03da09...; user-reworded Step 15) | form / reasoning number check | [screenshot](platform-feedback/q01-rev1-reasoning-flag-2026-10-08.png): "Step 10: Doc 4 doesn't mention 112. Check the document number." | rev 2 (96e6a6cd...) deletes the one-document share steps; emulator [v6](helpers/form_check_v6.py) reproduces the flag and clears rev 2 | repaired, platform pending: re-paste reasoning, then quick test |
| F2 / aq-02102 / q02 | quick test of rev 1 question + answer (identical to rev 0) | difficulty / union match-then-exclude list | [screenshot](platform-feedback/q02-rev1-quick-test-2026-10-08.png): "Too easy — solver got it" | no fair repair of the same mechanism | redesign: q02 dropped |
| F3 / aq-02102 / q01 | quick test of rev 2 question + answer (= rev 1) | difficulty / stated-condition convention trap | user message "q01 is too easy to pass quick test" | untied rev 0 wording reopens a second reading (Doc 4 Table 2 107) | redesign: q01 dropped, family h1 closed |

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
- Candidate rows used: not enrolled. All five slots were already filled when aq-02102 started (2026-10-08:
  aq-01960 i01/i02, aq-02028 i01, aq-01937 i14/i15); sketch time for i01 is still timed in notes/efficiency.json.

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
