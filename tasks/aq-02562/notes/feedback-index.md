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
| F1 / aq-02562 / q01 | form quick test 2026-10-09; rev 0, 9d38952d... assumed (panel not pasted; quick test sees question and answer) | difficulty / every decisive rule keyword-reachable from the question ("general partnership", "$900,000", "all from farming" settling MASC's exception in the same sentence) | user chat: "q01 too easy for quick test" (questions/q01.md Feedback log) | rev 1 (6b96b593...): partner's income 70% crops + seed sold to farmers, decided by D02's 66.66% production-inputs clause; gold unchanged | resolved by observed platform result: rev 1 measured In band, Hard (F2) |
| F2 / aq-02562 / q01 | difficulty Run 1, Version 9f31eb, 2026-10-10 12:57 AM; rev 1, 6b96b593... (question and gold verbatim; Document check left out Docs 2 and 7) | difficulty pass + "may be too vague" advisory ($1,500,000: MASC's exception carried into ASCF, the high model citing D07's 7 CFR 1400 subpart F reference) | [verdicts/AQ-02562_difficulty_2026-10-10_0137.txt](../verdicts/AQ-02562_difficulty_2026-10-10_0137.txt): "In band — Hard tier", Low 0/5 · Medium 0/5 · High 1/5, "You can submit now." | gold kept: D07 prints the bar without exception twice (L148, L365); D02 alone prints it (L274-275); advisory non-blocking | resolved: q01 ready at Hard (above the Medium target); residual reviewer risk stated to the user |
| F3 / aq-02562 / q01 | Submit, 2026-10-10, rev 1 (failure modes are outside the fingerprint) | form / failure mode 1 "Look-alike measure" refused: "not a similar-metric confusion where a solver takes a sibling line item" | user screenshot (questions/q01.md Feedback log) | modes reduced to the measured scope trap (Wrong jurisdiction or scope / Misapplies a rule or premise), reason 49 words | resolved: user 2026-10-10 "accepted after pasting"; q01 submitted, accepted_tier: Hard Tier (reviewer acceptance not yet observed) |

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
- Candidate rows used: 0 / 5 (2026-10-09: `efficiency promote` for aq-02562 i01 -> q01 refused, "All five
  prospective promotion slots are already enrolled"; its timed sketch sessions 8a926bac and edbb23b8 stay
  unpromoted work in the shared ledger)

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
