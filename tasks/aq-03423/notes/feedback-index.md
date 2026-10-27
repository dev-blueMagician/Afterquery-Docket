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
| aq-03423-q01-F1 / aq-03423 / q01 | Quick test of the sketch wording; no page version given. Local rev 0, 5f25fda0... (identity presumed: the user had only this wording) | difficulty / printed look-alike figure plus a subtraction | User message 2026-10-12, verbatim: "both too easy for quick test". No panel text, capture or trace | questions/q01.md Feedback log; status dropped | redesign: hook h1 retired; no difficulty run spent |
| aq-03423-q02-F1 / aq-03423 / q02 | Quick test of the sketch wording; no page version given. Local rev 0, 6258b1cf... (identity presumed) | difficulty / four-step calculation with a time-limited offer | Same user message. No panel text, capture or trace | questions/q02.md Feedback log; status dropped | redesign: hook h2 retired; no difficulty run spent |
| aq-03423-r2-F1 / aq-03423 / sketches i06, i07, i09, i10 | Quick test of the round 2 sketch wordings (notes/sketches/); no page version given | difficulty / derived base, sign against a table, split ranking | User message 2026-10-12, verbatim: "only last one survived". No panel text, capture or trace | notes/ideas.md round 2 table | redesign: hooks h11, h12, h13 retired |
| aq-03423-q03-Q1 / aq-03423 / q03 | Quick test of sketch i08's wording ("set out and answer"); no page version given | quick-test survival, not a tier | Same user message: the last of the five survived. Solver's answer not supplied | questions/q03.md rev 0, c8f4b9e8..., wording tightened to "set out to answer" | closed: superseded by aq-03423-q03-D1 |
| aq-03423-q03-D1 / aq-03423 / q03 | Run 1, Oct 12, 2026, 5:16 PM, Version 3ccb8e (current) / rev 0 / c8f4b9e8... (attempts quote the question word for word; "Your answer" equals the gold; other fields not shown) | difficulty / the medium solver tabulates three lists that share printed question numbers; the low solver mixes up documents | [capture](../verdicts/AQ-03423_difficulty_2026-10-12_1737.txt) (sha256 8054ce79e6653a58c0425ed2e2f2e35010657010992d9e1743808aca1467598b; copy beside the snapshot): "Between levels", Low 0/5 · Medium 5/5, closed-book "Needed the documents ✓" | questions/q03.md Platform validation and Feedback log (routes of all ten attempts); no wording repair exists | redesign: q03 dropped, hook h6 retired; replaced by q04 |
| aq-03423-q04-F1 / aq-03423 / q04 | Quick test of rev 0's wording; no page version given. Local rev 0, beb2e1e0... (identity presumed) | difficulty / the kind-clause ("only another submitter reports") points at the other submissions, where Doc 7 states Trustpower's offers plainly | User message 2026-10-12, verbatim: "too easy for quick test". No panel text, capture or solver answer | questions/q04.md Feedback log; rev 1, 7946e5eb..., replaces the clause with "Judging by all the submissions ... together" (gold, evidence, documents unchanged) | redesign not available: rev 1 and the no-rule wording both quick-test "too easy" (user, 2026-10-12: "both are too easy"; no panel); q04 dropped, hook h14 retired; release recommended |

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

- Summary: this bundle's candidates (i01 -> q01, i02 -> q02) are not enrolled in the trial; the owner index is
  the workspace notes/feedback-index.md. Authoring minutes unmeasured (a peer session's timer was open in the
  shared ledger when work began on 2026-10-12); acceptance outcomes pending; revisions 0; ambiguity/necessity
  returns none yet.
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
