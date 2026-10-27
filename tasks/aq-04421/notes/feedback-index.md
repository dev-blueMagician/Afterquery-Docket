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
| P1 / aq-04421 / sketch i01 | quick test, 2026-10-13; notes/sketches/i01.md wording by the user's label, tested text not captured | difficulty (draft screen) / the easier solver reached the Entity List rule's two UAE firms unprompted | user message "i01 failed, i04 survived, others not tested" (no panel) | none: sketch dropped, h13 closed | closed |
| P2 / aq-04421 / q01 (sketch i04) | quick test, 2026-10-13; notes/sketches/i04.md wording by the user's label, tested text not captured | difficulty (draft screen) / survived | same user message | q01 rev 0 (76650096...) = that question and answer word for word | survived the quick test; full Checks passed (user report, 2026-10-14, no capture); ten difficulty attempts on version 4fcc5d ended "Did not finish" or "Checker unavailable", none counted; an eleventh run started and was counted; result pending (questions/q01.md Feedback log) |
| P3 / aq-04421 / q01 | difficulty Run 16, Version fa81d1, 2026-10-14 9:32 AM; "Your answer" = rev 0 gold, question not quoted, page says documents or necessary ticks changed before the run: binding to rev 0 (76650096...) not established | difficulty / Too easy at the high level: Low — · Medium — · High 3/3; the page's notes say a near-verbatim road-name match (Feila / Fei La, Guoshoujing) | verdicts/AQ-04421_difficulty_2026-10-14_0942.txt (attempt texts not recorded; routes unread) | sketch i05: same join over entries added or corrected, adding the member whose road is split across D03's interleaved columns (Hexin Xingtong, Bi Bo Road) | i05 survived its quick test (user, 2026-10-14) and became q01 rev 1 (ea2e57cc...); rev 1 measured Too easy, High 3/3 (P4) |
| P4 / aq-04421 / q01 rev 1 | difficulty Run 17, Version 511a2b, 2026-10-14 10:26 AM; question quoted word for word and "Your answer" = rev 1 gold; ticks not captured (binding to ea2e57cc... incomplete) | difficulty / Too easy at the high level again: Low — · Medium — · High 3/3; the page's notes: "matched the three roads verbatim", split Bi Bo Road included | verdicts/AQ-04421_difficulty_2026-10-14_1033.txt (attempt texts not recorded; routes unread) | none: same failure on the repaired version, h14 closed; round-3 search found no other fair hook for the high model (notes/hooks.md) | closed; next action is the user's choice between the two untested low sketches and release |

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
