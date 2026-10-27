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
| r1 / aq-03993 / q01 (sketch i01) | Form quick test, 2026-10-13. Wording not captured: rev 0's sentence as handed over, or the user's rewording of it. Not bound to f2eb49e7... | difficulty (preliminary screen) / a part only Doc 4 separates from Doc 1's headline total | User chat, verbatim: "i01 survived, others not tested". No panel, no trace. Logged in [q01.md](../questions/q01.md) Feedback log. | q01 rev 0, unchanged. No fix needed. | historical: superseded by r2 (the run was on rev 0's sentence). |
| r2 / aq-03993 / q01 | Difficulty Run 1, Oct 13, 2026, 2:26 PM, Version fb9504. Rev 0, f2eb49e7... (bound for question and answer: the capture quotes both; other fields not shown). | difficulty / one unprompted look in Doc 4 for the grant share. Low never opened Doc 4; two of three medium solvers never left Doc 1; the third found it once in three; high three in three. | [capture](../verdicts/AQ-03993_difficulty_2026-10-13_1438.txt): "Between levels", Low 0/5 · Medium 1/7 · High 3/3, "Too hard for the medium model but too easy for the high model". Closed-book "Needed the documents ✓" (answered 158 and £100,000 from recall). Routes in [q01.md](../questions/q01.md) Feedback log. Not recorded on the page: medium 2 and 6, high 1-3. | q01 rev 1, 6ae7c9c5...: one ask ("how much grant money ... pay out, on average, to each project it funded"), gold "About £50,000"; trap, documents and evidence unchanged. Coach's "pin the basis" wording not taken (reasons in the Feedback log). | historical: rev 1 measured in r3. |
| r3 / aq-03993 / q01 | Difficulty Run 2, Oct 13, 2026, 3:21 PM, Version 2a5462. Rev 1, 6ae7c9c5... (bound for question and answer: the page's change list is rev 0 to rev 1, the question is quoted nine times). | difficulty / same mechanism as r2, demonstrated again on the repaired version: nobody below the strongest solver opens Doc 4. | [capture](../verdicts/AQ-03993_difficulty_2026-10-13_1539.txt): "Between levels", Low 0/5 · Medium 0/6 · High 3/3. Closed-book "Needed the documents ✓". Routes in [q01.md](../questions/q01.md) Feedback log. Not recorded: medium 3 and 6, high 1-3. | No rev 2 yet. Rev 1 changed the wording, not the dependency. Untried fair wording of the hook: sketch i05 (evidence named). New hook: sketch i04. | redesign: quick-test i04, i05, i02, i03 (free); write up a survivor. No further run on q01 as worded. |
| r4 / aq-03993 / q02 (sketch i04) | Form quick test, 2026-10-13. Wording not captured: the sketch's sentence ("... List them in any order.") or the user's rewording. Not bound to a fingerprint. | difficulty (preliminary screen) / three witnesses whose own organisation employs the reporters, among partners, the funder and membership bodies | User chat, verbatim: "i04 survived". No panel, no trace. Logged in [q02.md](../questions/q02.md) Feedback log. | q02 rev 0, 9d531399... (tail changed to surname order; nothing else). | historical: rev 0 measured in r5. |
| r5 / aq-03993 / q02 | Difficulty Run 3, Oct 13, 2026, 5:17 PM, Version f86c5c. Rev 0, 9d531399... (bound for question and answer: change list and three full quotes). | difficulty / one clause in a witness's own answer (Floyd, Doc 4 Q255). Low never found it; one medium solver never, one twice in three, one twice (unrecorded). Look-alikes cleared by every recorded medium attempt. | [capture](../verdicts/AQ-03993_difficulty_2026-10-13_1739.txt): "Between levels", Low 0/5 · Medium 4/7, "Too hard for the low model but too easy for the medium model". Closed-book "Needed the documents ✓". Routes in [q02.md](../questions/q02.md) Feedback log. Not recorded: medium 3 and 4 (right). | q02 rev 1, dd07a6e7...: asked as a total, "How many BBC-funded local democracy reporters does the evidence place on the staff of organisations that sent a witness ...", gold "77 reporters"; ticks corrected to Doc 1 and Doc 4; mode Part vs total (75). | historical: rev 1 measured in r6. |
| r6 / aq-03993 / q02 | Difficulty Run 4, Oct 13, 2026, 7:39 PM, Version 7a3c0c (current). Rev 1, dd07a6e7... (bound for question, answer and necessary documents: change list rev 0 to rev 1, question quoted twenty times, document check on Doc 4 and Doc 1). | difficulty / the same clause (Floyd, Doc 4 Q255), asked as a total against Doc 1's complete-looking 75. By wording: one medium solver right twice, one wrong twice (never found the clause), the unrecorded one wrong twice. | [capture](../verdicts/AQ-03993_difficulty_2026-10-13_2056.txt): "In band — Medium tier", Low — · Medium 2/6 · High —, "The difficulty check passes on the current content." Closed-book "Needed the documents ✓" ("About 30"). Document check: "Reached your answer ✓", "Needed document 4 ✓" twice (75), "Needed document 1 ✓" twice (2). Routes in [feedback-q02.md](feedback-q02.md). Not recorded: medium 3 and 6 (wrong). | q02 rev 1, frozen (status submitted, accepted_tier: Medium Tier, file sha256 0ce53607...). User chat: "Successfully submitted as a medium tier." Submitted form and Checks not captured. | resolved by observed platform result (difficulty pass at Medium on the same content). Acceptance not observed: later observations go to [feedback-q02.md](feedback-q02.md) only. |

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

- Summary: aq-03993 is not enrolled. The workspace trial's five promotion slots were already taken
  (`efficiency promote` refused q01 on 2026-10-13: "All five prospective promotion slots are already
  enrolled"). One sketch interval for i01 was timed in ../../../notes/efficiency.json (about 7 minutes,
  started after the documents had been read, so timing coverage is partial; later work was untimed because a
  peer session's timer was active). Outside the trial, for the record: four difficulty runs (rows r2, r3, r5,
  r6), two revisions (q01 rev 1, q02 rev 1), no ambiguity or necessity return from the platform, q02
  submitted at Medium on 2026-10-13, acceptance pending.
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
