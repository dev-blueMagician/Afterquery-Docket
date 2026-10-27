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
| F1 / aq-02933 / q03 | Version 1acbee, Run 1, Oct 11, 2026, 1:51 PM / rev 0 / 04ea99cc6f0ab842020f6be6133faafa412ba69dc288b323c0a3e147fdb1f55e (question quoted verbatim, gold and ticked documents match) | difficulty / below target: "In band — Easy tier", Low 1/5, Medium and High not run. Traces: four low attempts answered 367 by leaving Georgia out; none took the declared Nevada trap. | [capture](../verdicts/AQ-02933_difficulty_2026-10-11_1708.txt); page also showed a "Docket has been updated. Reload this page" notice; its "Where it left your evidence" line (Nevada's 138 as the base) contradicts the attempts' own answers | q03 unchanged at rev 0, record in [q03.md](../questions/q03.md). No repair inside the hook (one deciding step); separator carried into [q04.md](../questions/q04.md) rev 0 with a second membership step | resolved by observed platform result for q03 (Easy, not used: no Easy slot per the user); q04 platform pending |
| F2 / aq-02933 / q04 | version id not shown; rows quote rev 0's descriptions and answer (rev 0, 74803f0890b9d5d2e8c022a94836ca5232216317a4f4adb6a01c8bd1befcc665); reasoning box not visible | ambiguity (blocking) / "One defensible answer" Failed: rev 0's "does not name" condition left California's status open and California's 1,130 decides the total (373 on the other reading). Three advisories: No single passage, Answer matches a stated figure, Each description fits one thing | [screenshot](platform-feedback/q04-r0-checks-2026-10-11.png), [transcription](platform-feedback/q04-r0-checks-2026-10-11.md) | [q04.md](../questions/q04.md) rev 1 (58404d44bda7696f039e5bcfbc524472cb947f6fa1f713c361dc817fba5664b2): California left out in the question, ask is the named States' share, 67.45%. The two set-description and one-document-figures advisories may warn again | resolved for the form block by rev 1 (it reached a difficulty run); see F3 |
| F3 / aq-02933 / q04 | Version f40b71, Run 2, Oct 11, 2026, 8:25 PM / rev 1 / 58404d44bda7696f039e5bcfbc524472cb947f6fa1f713c361dc817fba5664b2 (the run's change list, the quoted question and the gold match rev 1) | difficulty / "Too hard", Low 0/5, Medium 0/5, High 0/5; page advisory "may be too vague". Traces: fifteen of fifteen answered 83.57% (773 / 925), taking the 2019 totals from Table 1 alone; all fifteen found Texas and Nevada in Doc 6; three medium attempts quoted Georgia's sentence and still left it out | [capture](../verdicts/AQ-02933_difficulty_2026-10-11_2048.txt); Coach suggested rewording the shared-address clause, which no attempt misread | [q04.md](../questions/q04.md) rev 2 (45f54e261663216380ca99c92b32c838cf2a6904deaecc5ccb38bc0cb56ddcee): adds "tabulated or only in text"; gold, reasoning, evidence unchanged; failure mode re-declared from the observed 83.57%. Separate new hook: [q05.md](../questions/q05.md) | resolved by observed platform result on rev 2; see F4 |
| F4 / aq-02933 / q04 | Version 25d15f, Run 3, Oct 11, 2026, 11:47 PM / rev 2 / 45f54e261663216380ca99c92b32c838cf2a6904deaecc5ccb38bc0cb56ddcee (change list equals rev 2's edit; question and gold match) | difficulty / below target: "In band — Easy tier", Low 3/5, Medium and High not run; Document check both needed. Traces: three low attempts 67.45%, two still 83.57% (Table 1 only) | [capture](../verdicts/AQ-02933_difficulty_2026-10-12_0055.txt) | [q04.md](../questions/q04.md) unchanged at rev 2; hook retired at Medium (Easy on q03's frame, Too hard without the rule, Easy with it). Next candidate [q05.md](../questions/q05.md) rev 1 | resolved by observed platform result (Easy, not used: no Easy slot per the user); q05 then quick-test too easy, see F5 |
| F5 / aq-02933 / q05 | quick test, version not shown / taken as rev 1 (bbe7f74d7a88fcac490b8d166ee3fe2a14a9ccae0f0869a088021a27ca497269) on the user's report | difficulty / quick test "too easy": the easier solver reached 13 in one draw; route unread (no trace) | user chat, 2026-10-12, "too easy for quick test"; no artifact | [q05.md](../questions/q05.md) status dropped, no repair | closed; q05 has no successor (see F6 for the one remaining candidate) |
| F6 / aq-02933 / q04 | quick test, version not shown / wording offered 2026-10-12, now rev 3 (d7b969d85c309fab832e8a06cc5a74874ff45f863739b28066fbccd21da3372d) on the user's report | difficulty / quick test "survived": the easier solver missed in one draw; route unread (no trace) | user chat, 2026-10-12, "quick test survived"; no artifact | [q04.md](../questions/q04.md) rev 3: the tested wording, everything else as rev 2 | resolved by observed platform result (Between levels); see F8 |
| F7 / aq-02933 / q04 | version not shown; taken as rev 3 on timing only (d7b969d85c309fab832e8a06cc5a74874ff45f863739b28066fbccd21da3372d) | form / two checks did not run ("Could not run this check — retry": Needs the documents; Each description fits one thing) and one advisory warning (No single passage: "Doc 5 on its own may give enough to compute the answer") | [screenshot](platform-feedback/q04-r3-checks-2026-10-12.png), [transcription](platform-feedback/q04-r3-checks-2026-10-12.md) | [q04.md](../questions/q04.md) rev 3 unchanged: reload the page and re-run the two checks; the advisory is the one rev 0 drew, and rev 2's Document check found both documents needed | closed: the difficulty run went ahead (see F8) |
| F8 / aq-02933 / q04 | Version 1c833c, Run 4, Oct 12, 2026, 2:42 PM / rev 3 / d7b969d85c309fab832e8a06cc5a74874ff45f863739b28066fbccd21da3372d (change list equals rev 3's edit; question and gold match) | difficulty / "Between levels", Low 0/5, Medium 4/5, High not run. Traces: every low attempt read "Wherever" as Table 1 (83.57%, one 83.62%); four medium attempts stopped on the word, re-read Doc 5 and added Georgia (67.45); one medium read it as Table 1 | [capture](../verdicts/AQ-02933_difficulty_2026-10-12_1451.txt); Coach: no specific change suggested | [q04.md](../questions/q04.md) rev 4: "Across every State with a 2019 hospice total from CMS" in place of "Wherever CMS gives a State's 2019 hospice total"; nothing else changed | rev 4 blocked by the form before any run; see F9 |
| F9 / aq-02933 / q04 | form Checks, version id not shown / rev 4 / ffe35caffb43c548c81855a6535f26d8e5134f879384086fc33b691a1db58b60 (Question box shows rev 4 word for word; message quotes the gold) | ambiguity, blocking / "One defensible answer" Failed: "two independent solvers ... did not reach your gold "67.45%". Both answered "83.57%"" (the Table 1-only figure; solver reasoning not shown). "Each description fits one thing": could not run, retry | [list](platform-feedback/q04-r4-checks-2026-10-12-list.png), [question box](platform-feedback/q04-r4-checks-2026-10-12-question.png), [transcription](platform-feedback/q04-r4-checks-2026-10-12.md) | [q04.md](../questions/q04.md) rev 5: scope named, "whose 2019 hospice total appears in CMS's hospice notice"; "it names" to "CMS names"; nothing else changed | resolved: rev 5 ran and was submitted (see F10); its Checks panel was not captured |
| F10 / aq-02933 / q04 | Version 162781, Run 5, Oct 12, 2026, 6:26 PM / rev 5 / d6a2c4caa1dabf3c2476fb3ac9602a0955e49a4b9163ef10885a0d80467603a4 (change list gives rev 5's question; quoted 16 times; gold matches) | difficulty / "In band — Medium tier", Low 0/5, Medium 1/5; document check: one of three every-document attempts reached, both documents needed; non-blocking "may be too vague" | [capture](../verdicts/AQ-02933_difficulty_2026-10-12_1903.txt) | [q04.md](../questions/q04.md) rev 5, unchanged | passed at target; submitted by the user 2026-10-12 (chat); frozen, later notes in [feedback-q04.md](feedback-q04.md) |

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
