# Current bundle checkpoint

- Goal and user constraints: AQ-03169, ten responses to the CMA's October 2018 audit-market invitation to comment. User,
  2026-10-12: "there is no slot for Easy Tier for this bundle, we should target medium and high". Never offer an Easy submission.
- Verification target / measured platform tier: medium (hard accepted by the user's brief) / q02 rev 4 "In band — Hard
  tier", Low 0/5, Medium 1/7, High 3/6 (Run 5, Version 96eed6).
- Prepared run / tested_sha256: runs/q02-r4-v2-d020902e...-platform / d020902e0730964355141dead5c422d48c0e1dd9d4d701792905a190834511c1
  (history: rev 3 3503e8d3..., rev 2 829dae3a..., rev 1 d110aa2b..., rev 0 7234f7b7..., q01 revs 0-2).
- Bundle slug / documents / extraction warnings: aq-03169 / D01-D10 = Doc 1-Doc 10 / none; capture page notice only
  ("Docket has been updated. Reload this page ..."). D01 is OCR text with letter errors; D02's charts are unusable.
- Phase: submitted. q02 is frozen: questions/q02.md stays byte for byte at rev 4 (saved status checked); everything
  later goes to notes/feedback-q02.md.
- Questions: q02 (i06) rev 4, submitted by the user at Hard on 2026-10-13 (user chat). observed_platform_status:
  unknown (no acceptance or rejection seen). Platform history: Run 2 rev 0 Easy (P6); rev 1 form "Short answer" Failed
  (P7); Run 3 rev 2 Between levels (P8); Run 4 rev 3 Answer not supported (P9); Run 5 rev 4 Hard (P10).
  q01 (i01) dropped at rev 2: Run 1 "Answerable without the documents"; quick test too easy (P4).
- Decisions and constraints: every gold is base-free. A lone small whole number is never the whole gold (P1). Respondent
  names and counts stay out of answers (rule 10).
- Candidate families tried: round 1 cap arithmetic: too easy. Round 2: i06 = two-table filter, members split between
  Grant Thornton's annex table and its reply. Scope ladder on one gold: "say anywhere in its response" Between levels;
  "does Grant Thornton say" not supported (high model stayed in the table); "does Grant Thornton's response say" Hard.
  Low rarely finds the annex; medium skips tendering reform in Deloitte's table. i07, i08 untested.
- Changed files since the last checkpoint: notes/feedback-q02.md (new), feedback-index.md (P10), ideas.md, hooks.md,
  runs/event-i06-difficulty-run5.json, runs/event-i06-outcome.json. Workspace: tools/check_questions.py (`cue` WARN on
  "anywhere"/"wherever", new `short-answer` WARN), tools/test_docket_tools.py, WORKFLOW.md section 6 item 5, memory
  notes docket-local-solver-calibration, docket-start-from-measured-misses, docket-form-automated-checks.
- Revision rounds used / open platform feedback: q02 4, q01 2 (dropped) / none open; P10 awaits the acceptance outcome.
- Active feedback index: notes/feedback-index.md, rows P1-P10; frozen-question note notes/feedback-q02.md.
- Five-candidate trial: not enrolled; platform attempts run1:4e4850, run2:3beb81, run3:2277b0, run4:86b24a and
  run5:96eed6 and the outcome "pending" for i06 are in the shared ledger.
- Efficiency ledger / candidate / timer: ../../../notes/efficiency.json / aq-03169 i06 / none running. Rev 2 was
  untimed; intake and the full read were not timed; this feedback turn was not timed.
- Next action and blocker: none owed. When the platform accepts or rejects q02, record it in notes/feedback-q02.md and
  as an outcome event. "10 of 15 runs left" if the user wants a second question (i07, i08 or a new hook; never Easy).
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5), VS Code extension session, 2026-10-13.
- Optional diagnostic if needed: none run (no local solves, probes or reviews; none requested).
