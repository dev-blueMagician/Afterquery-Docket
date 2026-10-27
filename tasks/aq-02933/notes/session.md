# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.

- Goal and user constraints: aq-02933, 7 Federal Register texts. User, 2026-10-11 and 2026-10-12: no Easy slot, "target medium and high" (final; do not re-raise). After the Medium submission the user asked whether a Hard-tier question can still be made. Runs: the page showed "10 of 15 runs left" after Run 5.
- Verification target / measured tier: medium / q04 rev 5 "In band — Medium tier" (Low 0/5, Medium 1/5), submitted by the user 2026-10-12. Acceptance not yet observed.
- Submitted: q04 rev 5, tested_sha256 d6a2c4caa1dabf3c2476fb3ac9602a0955e49a4b9163ef10885a0d80467603a4, Version 162781. File frozen (status submitted, accepted_tier: Medium Tier). Later observations go to notes/feedback-q04.md, never to questions/q04.md.
- Documents: D01-D07 complete. Local ids differ from the page: D05 = Doc 6 (HHA notice), D06 = Doc 5 (hospice notice).
- Phase: feedback recorded; round 4 (Hard target) found no fair design on a separator other than q04's; decision returned to the user.
- Questions (origin claude):
  - q04 rev 5, submitted: "Across every State whose 2019 hospice total appears in CMS's hospice notice, leaving California out, what percentage of those hospices were in States CMS names for home health agencies sharing an address? Two decimal places." Gold 67.45%.
  - q03 (315 providers): Easy, Low 1/5; decides on the same Georgia sentence as q04. Not going forward.
  - q05: dropped (quick test too easy; route unread).
  - q01 (57.7%) shares q04's two passages: closed. q02 (383 enrollees, Docs 3 and 5) and sketch i01 (144.8, Texas per year): untested, on passages q04 does not use; stated sentences plus arithmetic.
- What five runs showed: the only item the stronger solvers missed is Georgia's prose total beside Table 1 (high model: 0 of 5 with no scope, 1 of 3 with the scope named). Every attempt at every level matched the Doc 6 list; the low model assembled split pairs and counted prose lists.
- Hard target, round 4 (2026-10-12): no write-up. Other late members carry no number that changes an answer (Ohio in the oversight list and in both co-location passages; Nevada's 188). Ohio's nested minimum (70 HHAs at nine addresses) is one-document. Scope-rule scenarios rest on hedged clauses or plain sentences. A second question deciding on Georgia's sentence would share the submitted q04's answer path and was not written. Details in notes/ideas.md.
- Lessons folded into memory (2026-10-12): docket-local-solver-calibration (measured Medium recipe 7), docket-start-from-measured-misses (step 7), docket-form-vague-block, WORKFLOW section 6 item 5; user-level note docket-fix-the-reading-not-the-cue.
- Feedback index: notes/feedback-index.md rows F1-F10. Raw: verdicts/ (five captures), notes/platform-feedback/ (rev 0, rev 3, rev 4 screenshots). Routes table and retrospective: notes/feedback-q04.md.
- Rounds: sketch rounds 3 of 3 used, plus round 4 at the user's request; hooks h1-h14 in notes/hooks.md.
- Efficiency ledger: ../../notes/efficiency.json; trial slots full, nothing enrolled; no timer open.
- Next action: the user's choice. If a reviewer returns q04, log the panel word for word in notes/feedback-q04.md first. If the user wants a free screen, q02's hand-over exists (notes/handover-q02.md); a quick test says only whether the easier solver reaches it. Do not write a second question on Georgia's sentence unless the user asks for it knowing it shares q04's deciding step.
- Runtime/model/effort: Claude Code, claude-opus-5-5, sessions of 2026-10-11 and 2026-10-12.
- Optional diagnostic: none run.
