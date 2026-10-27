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
| r1 / aq-01960 / none | None: intake capture of the empty task page (no question fields, "Quick tests used: 0 of 10", "0 runs") | identity: no question version tested, no verdict | [AQ-01960_2026-10-08_0416.txt](../../../AQ-01960_2026-10-08_0416.txt) "There is no difficulty result on the current content yet"; slots "Hard 0/2 · Medium 0/3 · Easy 0/1" | q01 rev 0 (838418ad...) and q02 rev 0 (16aba9f9...) written after it; nothing to compare or repair | historical (checked 2026-10-08 for arrived verdicts: none); next: platform form checks and difficulty run on q01 |
| r2 / aq-01960 / q01 | form quick test (easier solver); tested wording not supplied, rev 0 (838418ad...) assumed but unverified | difficulty: quick test "too easy" (solver reached the gold) | user report 2026-10-08 "q01 is too easy for a quick test" ([q01 Feedback log](../questions/q01.md)) | no repair: a single labelled quarter has no dependency left to tighten | dropped; q02 continues; i03 (different mechanism) offered for a quick test |
| r3 / aq-01960 / q02 | form full checks on rev 0 reasoning as pasted with the user's edits (Steps 8, 12-14); exact text not supplied | form: reasoning number check, "Step 2: Doc 10 doesn't mention $1.91205 billion" (also Steps 4, 6) and "Step 8: Doc 13 doesn't mention 0.6072" | user screenshot 2026-10-08 ([q02 Feedback log](../questions/q02.md)) | rev 1 (bd77669b...): plain operands as printed and plain results after "=" in Steps 2, 4, 6, 8; user's passing wording in Steps 9, 12-14 | repaired: rev 1 cleared Steps 2, 4, 6, 8 on the form (user screenshot, 2026-10-08); see r4 |
| r4 / aq-01960 / q02 | form full checks on rev 1 reasoning as pasted (bd77669b...; Steps 12-13 visible) | form: "Step 13: Which document says 8,074.36 million? Add 'Doc N'." | user screenshot 2026-10-08 ([q02 Feedback log](../questions/q02.md)) | rev 2 (6c540b33...): Step 13 cites "Docs 10 to 13" like Step 9 | superseded by r5 (rev 2's citation did not clear Step 13) |
| r5 / aq-01960 / q02 | form full checks on rev 2 reasoning as pasted (6c540b33...; user wording "result from Step 9") | form: "Step 12: Which document says 8,324.416 million? Add 'Doc N'." and "Step 13: Doc 10 doesn't mention 8,074.36 million. Check the document number." | user screenshot 2026-10-08 ([q02 Feedback log](../questions/q02.md)) | rev 3 (34bf7b1e...): conversion steps removed; one cross-unit subtraction ends the reasoning; failure modes in the 2026-10-08 layout | historical: q02 dropped after its quick test (r6) |
| r6 / aq-01960 / q02 | form quick test (easier solver); question and answer identical across revs 0-3, tested text not supplied | difficulty: quick test "too easy" | user report 2026-10-08 "both of q02 and i03 are too easy to pass quick test" | none: second failure of the guidance-implied gross profit family (after r2) | dropped; family retired |
| r7 / aq-01960 / i03 (sketch) | form quick test of the i03 question and answer as handed over (unverified) | difficulty: quick test "too easy" | same user report | none: the decoy's own quarter label disarms the edition trap | dropped; round 3 sketch i04 (grouped fiscal-year figure) offered |

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
- Candidate rows used: 2 / 5 in this bundle (workspace ledger slots 1 and 2; slot 3 is aq-02028, another session)

| Slot / bundle / candidate | Promoted date / question link | Actual authoring minutes / timing coverage | Reported tokens / coverage | Distinct platform attempts | Revision rounds | Ambiguity / necessity returns | Observed acceptance / raw link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 / aq-01960 / i01 | 2026-10-08 / [q01](../questions/q01.md) | 30.5 measured (sketch 27.8, draft 2.7); partial: a 34-min interval spanning the session break was discarded, scaffold/mapping untimed, i02 sketching interleaved in i01's sketch interval | unknown / no runtime usage report | 0 identified (quick test reported, no run id) | 0 | 0 / 0 | retired before submission (dropped 2026-10-08, r2) |
| 2 / aq-01960 / i02 | 2026-10-08 / [q02](../questions/q02.md) | 3.8 measured (draft) plus revision time in the ledger; partial: its sketch work sits inside i01's interval | unknown / no runtime usage report | 0 identified (quick test reported, no run id) | 3 (revs 1-3, form reasoning-format warnings only, r3-r5) | 0 / 0 | retired before submission (dropped 2026-10-08, r6) |

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
