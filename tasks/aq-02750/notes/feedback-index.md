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
| F1 / aq-02750 / q01 | quick test, platform version unknown / rev 0 / 7460e560... | difficulty / edition trap with a dated event | user chat 2026-10-10: "three of them too easy to pass quick test" (no panel; taken as q01-q03); questions/q01.md Feedback log | rev 1 (a1955795...): event dated only by a footnoted memo | historical: rev 1 also too easy (F4) |
| F2 / aq-02750 / q02 | quick test, platform version unknown / rev 0 / ca492376... | difficulty / edition trap plus printed deadline | same chat report; questions/q02.md Feedback log | rev 1 (7a3b70a9...): status cue removed | historical: rev 1 also too easy (F5) |
| F3 / aq-02750 / q03 | quick test, platform version unknown / rev 0 / d85c297f... | difficulty / three-document deadline gap | same chat report; questions/q03.md Feedback log | none: dropped | historical |
| F4 / aq-02750 / q01 | quick test, platform version unknown / rev 1 / a1955795... | difficulty / same edition trap, footnote-dated event | user chat 2026-10-10: "q01 q02 too easy to pass quick test. i08 survived. rest not tested" (no panel); questions/q01.md Feedback log | none: hook h1 retired, q01 dropped | redesign (done: q04) |
| F5 / aq-02750 / q02 | quick test, platform version unknown / rev 1 / 7a3b70a9... | difficulty / same edition trap, no status cue | same chat report; questions/q02.md Feedback log | none: hook h2 retired, q02 dropped | redesign (done: q04) |
| F6 / aq-02750 / i08 -> q04 | quick test of the sketch (question and answer only), platform version unknown | difficulty / asymmetric rules across two procedures | same chat report: "i08 survived"; questions/q04.md Feedback log | q04 rev 0 (3e6180a6...), wording unchanged | historical: Run 1 Between levels (F7) |
| F7 / aq-02750 / q04 | difficulty Run 1, Version b8861d / rev 0 / 3e6180a6... (question and answer verified word for word; no Document check ran, so ticked documents not shown) | difficulty / the method rule stopped the low model 5 of 5 and the medium model 0 of 5 | verdicts/AQ-02750_difficulty_2026-10-10_2058.txt: "Between levels", "Low 0/5 · Medium 5/5 · High —"; low attempts all 91, medium all 61; questions/q04.md Platform validation and Feedback log | rev 1 (d8855b69...): rule side kept; one batch per order arriving 19 days after issue (derived dates against three printed deadlines), gold 52 | historical: rev 1 too easy at the quick test (F8) |
| F8 / aq-02750 / q04 | quick test, platform version unknown / rev 1 / d8855b69... | difficulty / the easier solver cleared the method rule and the derived dates in one draw | user chat 2026-10-11: "too easy to pass quick test" (no panel; taken as q04 rev 1); questions/q04.md Feedback log | rev 2 (72a22cb5...): the valid letters on the June order restored; order batches timed from the prior order's comment close; gold 70 | historical: the report was difficulty Run 2 (F9); rev 2 measured in Run 3 (F10) |
| F9 / aq-02750 / q04 | difficulty Run 2, Version 0e525b / rev 1 / d8855b69... (identity resolved 2026-10-11 by the capture's change note and "Your answer: 52 comments"; no Document check ran) | difficulty / the low model cleared the method rule and three derived dates 4 of 5 | verdicts/AQ-02750_difficulty_2026-10-11_1820.txt: "Run 2 · Too easy · Earlier version — does not count", "Low 4/5 · Medium — · High —"; first seen in verdicts/AQ-02750_form_2026-10-11_screenshot.png and the user's chat "too easy to pass quick test" (F8, same run); questions/q04.md Platform validation and Feedback log | rev 2 (72a22cb5...): valid letters on the June order restored | historical: rev 2 measured in Run 3 (F10) |
| F10 / aq-02750 / q04 | difficulty Run 3, Version bd63c0 / rev 2 / 72a22cb5... (question quoted in full, answer 70, documents 4-7 left out in turn) | necessity / Docs 5 and 7: no batch fell between the 15-day fallback date and the printed deadline of the June or August order, so the high model reached 70 without either | verdicts/AQ-02750_difficulty_2026-10-11_1820.txt: "A marked document may not be needed", "Your answer can still be reached without documents 5 and 7.", "Low 3/5 · Medium — · High —"; without Doc 4: 52 twice; without Doc 6: 51 twice; questions/q04.md Platform validation and Feedback log | rev 3 (a89df736...): lag of 18 days from each order's issue date, so the June and July batches each land between fallback and printed deadline; August order and Doc 7 dropped; documents D04-D06; gold 89 | resolved by observed platform result: Run 4, Version b97466, "In band — Easy tier", Low 2/5, Docs 4, 5 and 6 each needed twice (verdicts/AQ-02750_difficulty_2026-10-11_2048.txt); below the medium target, see F11 |
| F11 / aq-02750 / q04 | difficulty Run 4, Version b97466 / rev 3 / a89df736... | premise (author's finding from the traces; the platform passed the version) / the question states comment receipts as fact; Doc 6 L43 and Doc 7 L41 record five comments on the June order and none on the July order | verdicts/AQ-02750_difficulty_2026-10-11_2048.txt: low attempt 1 "CDC's official record for that order's comment period (closed July 31) shows no comments received"; platform note on attempt 2 "pulled in unrelated comment counts from Doc 7"; questions/q04.md Lever checks (Premise) | q04 unchanged, an edit would void Run 4; q05 rev 0 (6881cae3...) is the same question as a supposition, target easy | historical: no Easy slot left (user, 2026-10-11), so neither q04's Easy pass nor q05 can be used |
| F12 / aq-02750 / q05 | quick test, platform version unknown / taken as q05 rev 0 (6881cae3...), identity unresolved | difficulty / the easier solver reached the gold in one draw | user chat 2026-10-11: "too easy for quick test" (no panel); questions/q05.md Feedback log | q05 unchanged: target easy, and q04 rev 3 (same question as fact) measured Low 2/5 in Run 4, so one correct draw is not a failure of this target | historical: confirmed a quick test of q05 (user, 2026-10-11); q05 dropped, no Easy slot left; redesign as sketch i11 (Docs 2 and 3), quick test pending |
| F13 / aq-02750 / q06 | platform Checks, partial screenshots 2026-10-11 23:46 / rev 0 / d105c21d... (identity by the quoted wording) | form / blocking "Components match the answer": the answer's "8" of "8 CFR" in no component; advisories: answer-protocol tail "in any order", "No single passage", "Each description fits one thing" | verdicts/AQ-02750_checks_2026-10-11_2346_q06_a.png, verdicts/AQ-02750_checks_2026-10-11_2346_q06_b.png; questions/q06.md Feedback log | rev 1: component 1 "8 CFR 1003.42"; tail removed; two advisories answered in Lever checks | historical: rev 1 handed over; then quick-test too easy (F14) |
| F14 / aq-02750 / q06 | quick test, platform version unknown / taken as rev 1 (b6ec9851...), identity unresolved | difficulty / the easier solver reached the six-section list in one draw; route unread (no trace) | user chat 2026-10-12: "too easy for quick test" (no panel); questions/q06.md Feedback log | none: q06 dropped, hook h13 closed | historical / stop rule reached: release recommended |

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
- Candidate rows used: 0 / 5 from this bundle; the workspace trial was already full (five slots enrolled before 2026-10-10), so aq-02750 candidates i01 and i06 are timed as unpromoted work only

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

- Summary: no aq-02750 candidate is enrolled in the five-candidate trial; see the workspace owner index for totals.
