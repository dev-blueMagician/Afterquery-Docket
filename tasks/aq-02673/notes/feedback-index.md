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
| f1 / aq-02673 / q04 | Version d599f9, difficulty Run 1 (Oct 10, 2026, 3:09 PM) / rev 0 / 0819d70f... (bound by the question quoted verbatim 13 times and "Your answer: 168.84 mt") | ambiguity + difficulty: "Too hard", Low 0/5 · Medium 0/5 · High 0/5; all 15 attempts 193.84 (baseline quota difference); the question left to the documents the rule that a bycatch allocation drawn from the western TAC counts | [capture](../verdicts/AQ-02673_difficulty_2026-10-10_1520.txt); platform: "This question may be too vague: several solvers agreed on an answer that is not your gold"; Coach: reword to the baseline quota difference (not adopted: one-document lookup, gold would become 193.84) | rev 1 / ca7d711e...: rev 0's sentence plus "counting any longline bycatch allocation drawn from that TAC"; gold and documents unchanged; [q04.md](../questions/q04.md) Feedback log, [hand-over](handover-q04.md) | resolved for rev 0's mechanism by rev 1's clause (no solver result on it beyond f2); see f2 |
| f2 / aq-02673 / q04 | quick test, platform version not shown / rev 1 as handed over (ca7d711e...), identity unverified: no capture, typed question not shown | difficulty: too easy at the quick test (user report); author's inference, no trace: rev 1's clause named the bycatch allocation and the origin test, which is the whole inference | user's words, 2026-10-10 15:43: "q04 too easy to pass quick test"; no panel, counts or Coach text supplied; logged in [q04.md](../questions/q04.md) Feedback log | q04 rev 2 / 50ca7237...: clause replaced by "in total"; alternate [q05](../questions/q05.md) rev 0 / 0d9155dd...: "whatever fishery the tonnage was reserved for"; gold and documents unchanged; hand-overs [q04](handover-q04.md), [q05](handover-q05.md) | resolved by observed platform results f3 and f4 (both midpoints were then run in the difficulty check) |
| f3 / aq-02673 / q04 | Version 5d3970, difficulty Run 2 (Oct 10, 2026, 4:01 PM) / q04 rev 2 / 50ca7237... (bound by the platform's change list, 20 verbatim quotes of the question and the gold) | difficulty: "Between levels", Low 0/5 · Medium 0/5 · High 4/5; "in total" was enough for the high model only; low and medium stayed on 193.84 | [capture](../verdicts/AQ-02673_difficulty_2026-10-10_1633.txt); "Too hard for the medium model but too easy for the high model"; Coach "Make it harder" | no further edit; q04 dropped as superseded by q05 (same question, the wording that passed) | historical |
| f4 / aq-02673 / q05 | Version 1ee802 (current at capture), difficulty Run 3 (Oct 10, 2026, 5:42 PM) / q05 rev 0 / 0d9155dd... (bound by the platform's change list, 21 verbatim quotes, the gold, and the Document check leaving out Doc 3 and Doc 6) | difficulty: "In band — Medium tier", Low 0/5 · Medium 1/5, at target; Document check: Doc 3 and Doc 6 each needed; closed-book needed the documents; "may be too vague" advisory shown beside "You can submit now" | [capture](../verdicts/AQ-02673_difficulty_2026-10-10_1832.txt); wrong answers 193.84 (4 of 10) and 231.34 (5 of 10), the two declared failure modes | q05 status ready, [hand-over](handover-q05.md); the user's message labels the two files the other way round, the captures decide | resolved by observed platform result; next: Submit (the page's current content is the passing version); then record submission |

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
