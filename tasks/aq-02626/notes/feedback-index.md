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
| P1 / aq-02626 / q01 (sketch i01) | form quick test 2026-10-10; wording taken as q01 rev 0 (3532a741..., assumed, panel not pasted) | difficulty / two parallel State comment rules applied to one stated case; each rule beside its label | user chat: "both turned out to be too easy for quick test" (questions/q01.md Feedback log) | none: dropping the stated conditions would leave the gold undetermined | historical: q01 dropped, hook h13 closed, i05 dropped untested |
| P2 / aq-02626 / q02 (sketch i03) | form quick test 2026-10-10; wording taken as q02 rev 0 (eaf8ef1c..., assumed, panel not pasted) | difficulty / awarded-vs-anticipated total plus a facility count read off a permit list | same user message (questions/q02.md Feedback log) | none | historical: q02 dropped, hook h14 closed, i04 dropped untested |
| P3 / aq-02626 / i02 -> q03 | form quick test 2026-10-10; sketch wording = q03 rev 0's question, answer "1,271 days" (panel not pasted) | survived (no panel text) / stale amendment list in the Wyoming proposal | user chat: "i02 i06 survived, rest of them not tested" (questions/q03.md Feedback log) | q03 rev 0 adopts the wording unchanged (49d32dc6...) | open: difficulty run pending; survival is a first screen only |
| P4 / aq-02626 / i06 -> q04 | form quick test 2026-10-10 (survived, no panel); then difficulty check Run 1, Version d686ca (current), Oct 10, 2026, 4:30 AM; rev 0, tested_sha256 c18fded5... (question, gold and marked documents verified from the capture; other boxes not captured) | difficulty / approved-list status across templated proposals: "In band — Easy tier", Low 3/5, Medium and High not run; Document check needed Docs 3 and 4; closed-book needed the documents | [verdicts/AQ-02626_difficulty_2026-10-10_0806.txt](../verdicts/AQ-02626_difficulty_2026-10-10_0806.txt); platform summaries: 2 wrong low attempts "included Wyoming as a qualifying state" (43, 40); Coach section not in the capture | none: the Alabama decoy caught no attempt and three low attempts read the lists cleanly; no dependency change found (questions/q04.md Feedback log) | resolved by observed platform result: Easy, below the medium target, no Easy slot; q04 held, not submitted; quick-test survival again overstated difficulty |
| P5 / aq-02626 / q03 | task form, reasoning number check, 2026-10-10; box held the user's reworded rev 0 reasoning (49d32dc6... in substance; Step 4's text not in the screenshot) | form / a calculation step that spelled a number out ("twelve") and chained mixed operators lost its result exemption: "Step 4: Docs 2 and 6 don't mention 365. Check the document number." | user screenshot and chat "q03 has an issue" (questions/q03.md Feedback log) | rev 2 (f3d04aef...): Steps 4-9 are single two-operand calculations with no number written as a word; question, answer, documents, evidence unchanged; tools/form_numbers.py now FAILs a number word of ten or more in a calculation step and WARNs on a mixed chain | repaired/platform pending: paste notes/handover-q03.md, confirm no orange line, then run the difficulty check (P3 still open) |
| P6 / aq-02626 / q05 (sketch i07) | form quick test 2026-10-10; wording taken as q05 rev 0 (15e8c0cd..., assumed, panel not pasted) | difficulty / publication-to-deadline day counts summed over five proposals; the printed 60-day label did not hold the easier solver | user chat: "q05 is too easy to quick test" (questions/q05.md Feedback log) | none | historical: q05 dropped, hook h23 closed |
| P7 / aq-02626 / q03 | difficulty check Run 2, Version 564142, Oct 10, 2026, 10:02 AM; rev 2 (f3d04aef...; question and gold verified from the later capture's run history) | difficulty / stale amendment list in the Wyoming proposal plus a long day count: Too easy, Low 5/5, every low attempt 1,271 ([verdicts/AQ-02626_difficulty_2026-10-10_1132.txt](../verdicts/AQ-02626_difficulty_2026-10-10_1132.txt)) | user chat: "q03 too easy after final checks" (questions/q03.md Feedback log); supersedes P3's pending run | none: a pin-free wording would make 812 defensible | historical: q03 dropped, hook h15 closed; quick-test survival again did not carry |
| P8 / aq-02626 / i08 -> q06 | form quick test 2026-10-10; sketch wording = q06 rev 0's question, short answer "16" (panel not pasted) | survived (no panel text) / five permit-duration statements with look-alike wording | same user message (questions/q06.md Feedback log) | q06 rev 0 adopts the question unchanged; gold written "16 landfills" (8b7ea010...) | open: difficulty run pending; survival is a first screen only |
| P9 / aq-02626 / i09 | form quick test 2026-10-10; sketch wording (notes/sketches/i09.md) | difficulty / the same duration sentences as one stated 25-year case: too easy | same user message | none | historical: i09 dropped |
| P10 / aq-02626 / q06 | difficulty check Run 3, Version 8bf6fe (current), Oct 10, 2026, 10:52 AM; rev 0 (8b7ea010...; question and gold verified from the capture) | difficulty / five permit-duration statements with look-alike wording: "Too easy", Low 4/5; the one miss left Wyoming out (13); Coach: reword the condition away from the source's "no expiration" wording, and add a second condition (States that have actually issued permits) ([verdicts/AQ-02626_difficulty_2026-10-10_1132.txt](../verdicts/AQ-02626_difficulty_2026-10-10_1132.txt)) | user chat: "q06 too easy after difficulty check" (questions/q06.md Feedback log); supersedes P8's pending run | none yet: the held repair (i10) failed its quick test (P11); the Coach's variant is vetted as fair (Virginia 7 + Wisconsin 6 = 13) and offered as a free quick test, sketch i13 | q06 dropped at rev 0; i13 quick test pending at the user's choice; release still recommended |
| P11 / aq-02626 / i10 | form quick test 2026-10-10; sketch wording (notes/ideas.md i10, answer 50) | difficulty / q06's filter with Wisconsin's landfill-only scope added: too easy | same user message | none | historical: i10 dropped |

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
