# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal: user 2026-10-05 "work on AQ-00964_2026-10-05_2031" (/docket-new). At least an Easy
  platform pass; no platform submission without user authorization. User is at UTC+8 (records
  after midnight there are dated 2026-10-06).
- Target / measured: easy / MET by q01: platform difficulty check Run 1 (version 353aaf)
  "In band — Medium tier", Low 0/5 · Medium 1/5 · High —, "The difficulty check passes on the
  current content." Difficulty-check runs: 7 of 8 left. Quick tests 0 of 10.
- Rules: WORKFLOW v2.1; per-label Source assessment (151 labels, gap hash 482e178f...4b19).
- Bundle: American Tower releases; D01-D07 = Doc 1-7; D02-D07 clipped only inside tables.
- Phase: q01 ready; other candidates await platform checks.
- Questions (origin claude, easy; floor 0 FAIL):
  - q01 READY (cd873980): platform pass at Medium; second v2.1 review ready; Source assessment
    record (expanded mechanically from the reviewer's group map; raw in runs/q01.../results/).
    Frozen by the platform's version rule: do not edit question/answer/documents. Not submitted;
    submission and the "I wrote this question myself" item are the user's decision.
  - q06 checked (6b54fb71): New Site cutoff -> $12M; same shape as q01. Next platform candidate.
  - q04 (aedaeb4b), q05 (6dc6f72e), q02 (197a9f06) checked, unmeasured; q02/q05 need rev 1
    reasoning fixes (uncited calculation steps), q04 a reasoning phrase fix, before final checks.
  - q07 checked (02a32835): held (cut D05 row may move the gold). q03 dropped.
- Lessons filed: calibration note (first pass mechanism), redesign-v2 history, MEMORY index,
  GPT port L2; earlier q03 (estimation) and q07 (cut row) notes.
- Next: user decides on submitting q01; on request, run q06 on the platform, record verbatim via
  /docket-feedback; optional round 2 reusing the passing mechanism (dated event in a later
  release selecting an earlier forecast edition) on other events.
- Runtime: Claude Code (VS Code), Opus 5.5 max effort; fresh role agents via Agent tool.
