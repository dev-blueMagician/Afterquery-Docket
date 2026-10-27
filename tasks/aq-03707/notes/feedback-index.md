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
| aq-03707-q01-F1 / aq-03707 / q01 | form quick test, version not shown / rev 0 (assumed) / unbound (prepared 31dbf177... is not attached: no panel) | difficulty / easier solver reached the gold; route unread | user chat 2026-10-13, verbatim "too easy for quick test"; [q01 Feedback log](../questions/q01.md) | q01 dropped; hook h1 and sibling i01b closed, no repair | historical / round 2 sketches on another mechanism |
| aq-03707-q02-P1 / aq-03707 / q02 (sketch i03) | form quick test, version not shown / rev 0 (assumed) / unbound | difficulty (preliminary) / survived the quick test; no attempt text | user chat 2026-10-13, verbatim "i03 survived"; [q02 Feedback log](../questions/q02.md) | q02 rev 0 checked, tested_sha256 d85e2911... | platform pending / form Checks, then one difficulty run |
| aq-03707-q02-F1 / aq-03707 / q02 | form Checks, "5 hr ago" on 2026-10-13 / rev 0 (Question box equals rev 0 word for word; other fields not shown) / not bound | form / "Question in your own words" Failed: the box holds Claude's sentence | [screenshots and transcription](platform-feedback/q02-rev0-checks-2026-10-13.txt) | no repair by Claude; the user writes the sentence, which becomes rev 1 (origin user+claude) after a check against 22.2% | historical (q02 dropped) / rev 1 (the user's wording B, close to rev 0) failed the same row again (user chat 2026-10-13, no screenshot); next: the user's sentence on wording A's structure with its three content defects repaired, checked against 22.2% as rev 2 |
| aq-03707-q02-F2 / aq-03707 / q02 | same screenshots / rev 0 / not bound | form (advisory) / "Each description fits one thing": gross profit margin and EBITDAR margin both fit the description | [transcription](platform-feedback/q02-rev0-checks-2026-10-13.txt) | no repair: two kinds by design, one computable; "One defensible answer" passed (same row was left on aq-03557 q01, which then measured Medium) | advisory, no repair |
| aq-03707-q02-D1 / aq-03707 / q02 | difficulty Run 1, Version 3a92ac / rev 2 / f87a8c37... (question and gold verified in the capture) | difficulty / Between levels: Low 0/5, Medium 4/7; the single unpointed step (Doc 8 para 4.19, cost-of-goods share) decided every recorded attempt | [capture](../verdicts/AQ-03707_difficulty_2026-10-13_1256.txt); [read-out](feedback-q02.md) | no repair found inside hook h13; q02 dropped | redesign / quick-test i02 |
| aq-03707-q03-P1 / aq-03707 / q03 (sketch i05) | form quick test, version not shown / rev 0 (assumed) / unbound | difficulty (preliminary) / survived the quick test; no attempt text | user chat 2026-10-13, verbatim "i05 survived"; [q03 Feedback log](../questions/q03.md) | q03 rev 0 checked, tested_sha256 d5a12a0c... (", if any," added after the quick test) | platform pending / the user's wording, Checks, one difficulty run |
| aq-03707-q03-D1 / aq-03707 / q03 | difficulty Run 2, Version 752eb7 / rev 0 / d5a12a0c... (question and gold verified in the capture) | difficulty / Between levels: "Too hard for the medium model but too easy for the high model", Low 0/5 (2 not scored), Medium 1/7, High 3/3; Doc 5's aside reached by no low or recorded medium attempt; two low attempts read "a submission" as one submission | [capture](../verdicts/AQ-03707_difficulty_2026-10-13_1607.txt); [read-out](feedback-q03.md) | rev 1 (d2e05dac...): membership test restated as "any submission ... describes as a four-player supermarket market"; one failure mode kept | resolved by observed platform result (Run 3 on rev 1) |
| aq-03707-q03-D2 / aq-03707 / q03 | difficulty Run 3, Version 994c72 / rev 1 / d2e05dac... (change list, question, gold and removed documents verified in the capture) | difficulty / "In band — Medium tier", Low — · Medium 2/6 · High —; Document check: documents 3, 5 and 8 each needed | [capture](../verdicts/AQ-03707_difficulty_2026-10-13_1933.txt); [read-out](feedback-q03.md); user chat "Successfully submitted as a medium tier" | q03 frozen as submitted (accepted_tier: Medium Tier); the one declared mode matches every observed wrong answer | resolved by observed platform result / reviewer outcome pending |

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

- Summary: this bundle has no row in the trial (all five slots were already enrolled elsewhere); see the workspace owner index.
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
