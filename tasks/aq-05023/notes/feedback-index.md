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
| aq-05023-checks-2142 / aq-05023 / q01 (form state mixed) | Checks page saved 2026-10-14 21:42; unbound: question and answer "4.3" are q01's, but the component "$143 million", the evidence (Doc 1's June 2026 row) and the necessary-document ticks (Doc 1 standalone) are q02's; matches neither q01 rev 0 (dfdc826c) nor q02 rev 0 (919597bd); page also said "Docket has been updated. Reload this page" | form / paste mix, plus one advisory | [checks/AQ-05023_checks_2026-10-14_2142.txt](../checks/AQ-05023_checks_2026-10-14_2142.txt): 35 passed, 4 need attention: Components match the answer (Failed), Needs two or more documents (Failed, Doc 1 not needed), Evidence supports its component (Warning, advisory: 2026 repurchase quotes "irrelevant to CY 2025"), Sibling question (Warning, advisory: wording shared with another question on the bundle). "One defensible answer" and "Reasoning reaches the answer" last ran 45 min earlier, on q02's content | q01 rev 1 (f2fd7aaa...830f): evidence-only change removing 2026 remaining-authorization quotes from the alternative documents (the advisory's mechanism); the two Failed rows are paste fixes (component 4.3; Doc 3 ticked with Doc 1, Doc 4 and Doc 2 in its "or" box). Sibling advisory left: the shared wording is q01 vs q02, and both sentences are screened and quick-tested | historical: superseded by the difficulty run on q01 (row below); Checks for rev 1 were never captured |
| aq-05023-q01-run1 / aq-05023 / q01 | Run 1, Oct 14, 2026 10:18 PM, Version c9917a; bound by question and answer ("Your answer: 4.3"; Coach quotes q01's phrases); evidence and ticks not captured; precedes rev 1's snapshot (22:48), same question/answer/documents as rev 0 and rev 1 | difficulty / High-level clear of the two roll-forwards | [verdicts/AQ-05023_difficulty_2026-10-14_2252.txt](../verdicts/AQ-05023_difficulty_2026-10-14_2252.txt): "Too easy", Low — · Medium — · High 3/3, refunded; closed-book 2.0 (needed the documents); routes unread (no attempt text) | none: a High-level Too easy closes the hook (hard-playbook section 7); Coach items 1 (rewording) and 2 (basis pin; misdescribes the Q4 step as a share-count estimate) not adopted, see q01 Feedback log | historical (hook closed); q02 then also ran (row below) |
| aq-05023-q02-run2 / aq-05023 / q02 | Run 2, Oct 15, 2026 9:05 AM, Version 0aa132; bound by question (quoted word for word) and answer "$143 million"; no necessary-document change listed; evidence and ticks not captured | difficulty / High-level clear of the Q4 2025 buyback rebuild | [verdicts/AQ-05023_difficulty_2026-10-15_0909.txt](../verdicts/AQ-05023_difficulty_2026-10-15_0909.txt): "Too easy", Low — · Medium — · High 3/3, refunded; closed-book recall guess $100 million (needed the documents); routes unread (no attempt text) | none: a High-level Too easy closes the hook; Coach items 1-3 not adopted (rewording; unstated excise/fee basis; cleared Q4 step or table sweep), see q02 Feedback log | historical (hook closed); bundle: no fair sketch without a result |

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
