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
| P1 / aq-02564 / q01 (sketch i01) | form quick test 2026-10-09; wording identical to q01 rev 0 (d584a570..., assumed, panel not pasted) | difficulty (draft screen) / plain fee statements in two passages per notice; "total ... than under the existing programs" directs the solver to the Distribution Fee; footnote 12's decoy shows its own scope | user chat: "q01, i02 too easy for quick test" (questions/q01.md Feedback log) | none: dropping "total" or the baseline makes fn 12's $400 defensible | historical: q01 dropped, hook h1 closed |
| P2 / aq-02564 / i02 sketch | form quick test 2026-10-09; notes/sketches/i02.md wording, gold $1,475 (assumed, panel not pasted) | difficulty (draft screen) / host-pays and per-firm count rules stated in the same paragraph as the fees | same user message | none: sketch dropped | closed; hook h2 closed |
| P3 / aq-02564 / i03 sketch | form quick test 2026-10-10; notes/sketches/i03.md wording (host 2,000 users), gold $1,250 (sketch_sha256 227816bb..., assumed, panel not pasted) | difficulty (draft screen) / survived: host loses its credit when its only subscriber passes the 10,000 cap | user chat: "i03 survived" | q02 rev 0 = same wording with host 5,000 users, gold $1,625 (form number check: 2,000 is printed in neither notice) | survived the quick test; q02 rev 0 measured Easy (P4) |
| P4 / aq-02564 / q02 | difficulty Run 1, Version be6014 = rev 0 (b9ad2a2a...), bound by the quoted question, gold $1,625 and the two documents left out | difficulty / "In band — Easy tier", Low 2/5: all five low attempts made the eligibility inference; three left the host's user fees unpriced ("$1,000 ... plus ... user fees"), two priced them from footnote 12; the declared trap caught no one | verdicts/AQ-02564_difficulty_2026-10-10_0227.txt (Document check: both documents needed; closed-book missed; no Coach panel) | rev 1: the two notices applied as two programs (second subscriber; one on EDGX Top only, one over BYX's cap but within EDGX's), gold $2,375 | resolved by observed platform result (P5) |
| P5 / aq-02564 / q02 | difficulty Run 2, Version 8ce393 = rev 1 (27f12de0...), bound by the quoted question (8 quotes), gold $2,375, the platform's question/answer diff from Run 1 and the two documents left out | difficulty / "In band — Medium tier", Low 0/5 · Medium 3/5: low misses $875 x3 (hosted subscribers' set fees left off the host's bill), $1,750 (user fees unpriced), $2,125 (BYX credit kept); medium misses $1,750 and $2,387.50 | verdicts/AQ-02564_difficulty_2026-10-10_0356.txt (both documents needed; closed-book missed; no advisory) | none needed; q02 frozen as submitted (accepted_tier: Medium Tier), later observations in notes/feedback-q02.md | resolved at target; submitted by the user 2026-10-10; acceptance not observed |

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
