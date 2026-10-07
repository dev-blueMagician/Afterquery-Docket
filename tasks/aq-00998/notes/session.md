# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal: user 2026-10-05 "work on AQ-00998_2026-10-06_0256" (complete capture, tables visible).
  At least an Easy platform pass; no platform test/submission without user authorization.
- Target / measured: easy / PASSED by q05 rev 4 (platform Run 3, "In band — Easy tier", Low 3/5,
  2026-10-06 下午1:29, version c8271d). Gate text: "Ready when 1–3 attempts at a level are right".
- Bundle: Chevron releases 4Q23-2Q26 (D01-D06, D08-D12) + Hess completion (D07); D01-D12 =
  Doc 1-12. Complete capture, no gaps. Old folder deleted 2026-10-05 12:36:31 (rebuilt).
- Platform results (2026-10-06, user):
  - q03 rev 1 (62f3d14a...) difficulty check Run 1 "Too easy", Low 5/5 (raw output in
    runs/q03-r1.../results/platform-difficulty-check-run1.md); quick test had passed.
  - q01, q02, q04: quick test too easy (user report, no verbatim output).
  - All four now status dropped (records kept). Runs left on the platform page: 7 of 8
    difficulty checks; quick tests about 6 of 10 (user used 4).
- Lesson: event-defined quarters with a printed month/quarter plus labelled cells are too easy
  for the low model even with same-release decoys; quick-test pass is not a difficulty pass.
- Round 3 (checked 2026-10-06; raw returns and reviews in runs/<run>/results/):
  - q05 rev 3 (6259dd66...): PLATFORM Run 2 (version 35d6a9) "Low model 2/5 right" (in window)
    but "A marked document may not be needed ... without document 10"; gate failed (D11's
    rounded 4Q25 ROCE 5.4% at face value gives 10.8707 = gold at two decimals).
  - q05 rev 4 READY, tested_sha256 17565b4d...: three decimals = 10.869%. Platform Run 3: In band
    Easy, Low 3/5, closed-book needed docs, document check needed Doc 10 (10.871 without it) and
    Doc 12. User may submit; not yet reported submitted. Once submitted it is frozen.
  - q06 rev 1 CHECKED, tested_sha256 29d185e7...: 2Q 2025, 4Q 2025. HELD: once q05 is in review
    it holds the only Easy slot (slots Hard 0/2, Medium 0/3, Easy 0/1), and the high-model
    document check would likely rebuild items from cash-flow columns (D08, D09, D10, D12) and call
    exclusion-only releases not needed. Not run on the platform.
- Platform page: 5 of 8 difficulty runs left; 9 submissions left on this document set.
- Held/rejected author round 3: i16 (fairness inference), i17, i18.
- Next: user submits q05 (record submission; freeze). Further work on this bundle would target
  Medium or Hard slots (new sketches); q06 stays held unless redesigned.
- Runtime: Claude Code (VS Code), Opus 5.5 max; fresh role agents via Agent tool.
