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
| f1 / aq-02208 / q01 | quick test on rev 2, d58f4220... (assumed pasted as handed over; no screenshot) | difficulty / silent-drop list diff (Doc 2 proposal vs Doc 4 final lists) solved by the easier solver | user report in chat, 2026-10-08: "q01 too easy, i11 survived" | q01 Feedback log; no repair (hook retired) | resolved by observed result: dropped |
| f2 / aq-02208 / i11 -> q02 | quick test on sketch i11 (question as handed over in chat; pasted answer string not seen; sketch, no fingerprint) | difficulty / count of transmitter-characteristic items across editions (17 - 12 = 5); Doc 4's discussion names three of the five additions | same user report: "i11 survived" | q02 rev 0 checked, d21d6533... ([questions/q02.md](../questions/q02.md)); removal probes miss (no Doc 2: 3 at p 0.75; no Doc 4: not answerable) | resolved by observed result: difficulty check passed at Easy (user, 2026-10-09: "Passed difficult check as Easy tier"; binding assumed, see q02 Platform validation); below the Medium target; user submitting at Easy |
| f3 / aq-02208 / q02 | Submit attempt after the Easy pass, rev 0, d21d6533... (assumed) | form / targeted failure modes: "Figure that must be computed" and "Part vs total" judged not to fit their definitions | [screenshot](platform-feedback/q02-submit-failed-failure-modes-2026-10-09.png); verbatim text in q02 Feedback log | modes replaced: Look-alike measure / Takes the wrong line item; Linking across documents / Picks the wrong entity or section; 49-word reason; outside the fingerprint | resolved by observed result: Submit passed with option 1 (user, 2026-10-09: "Passed with your first option"); q02 submitted at Easy |

### Verdict review, 2026-10-09 (user: "check arrived verdicts ... find out what you missed out and improve")

Platform observations (user reports) against the author's predictions; lessons in memory as noted.

| Verdict | Predicted | Observed | What was missed | Lesson / where |
| --- | --- | --- | --- | --- |
| q01 quick test (f1) | lead Medium candidate; three traps (prose "none", moved items, suborbital) | "too easy" | memory already measured two-list diffs as low-model-solvable (trial-07 q05, aq-02102 q02, aq-02086 q03) and the FCC author repeated it; the "none" trap rested on a probe lacking Doc 2, which measures necessity only; orphan items are found by searching each proposed item | docket-removal-probe-required (2026-10-09 entry) |
| i11 quick test (f2) | optional numeric fallback | survived | numeric shape was the stronger lead (user preference) but was offered second | lead with the numeric when one exists |
| q02 difficulty (f2) | survivor, so Medium possible | "Easy tier" | one quick-test miss is one attempt; the letter-count route reaches the gold directly | docket-local-solver-calibration (2026-10-09 entry) |
| q02 Submit (f3) | form floor clean | blocked: modes did not fit trap definitions | picked labels by name; declared an unobserved per-station trap against the note's own rule | platform-quality-checks, question-gate Q15 |
| q02 Submit retry (f3) | option 1 (two measured modes) | passed; submitted at Easy | none | accepted labels recorded in platform-quality-checks |

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
