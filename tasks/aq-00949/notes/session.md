# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user 2026-10-05 (after q04's Easy pass): "set target difficulty as at
  least Medium [tier] and start work from the scratch again. This is for trial task, we have only
  one attempt, once after reach result, you need to check carefully again." New work on this bundle
  targets difficulty_target: medium (Medium or High pass; Easy no longer counts here).
- Measured so far: q01/q02 too easy (quick test), q03 too easy (Low 5/5), q04 rev 2 Easy (Low
  3/5, ambiguous wording) then rev 5 too easy (Low 5/5). Difficulty-check runs: 5 of 8 left.
- q04 dropped 2026-10-06 (rev 5 Run 4 "Too easy", 3 of 5 quoted D01's "$5.2 billion" yet used
  5,175). User: "find another, set difficulty_target to at least medium"; q05 cross-referenced.
- Source: complete capture AQ-00949_2026-10-06_0251.md; no gaps; local D01-D07 = platform Doc 1-7.
- Round 4 (2026-10-05, fresh full re-read of D01, D03, D07 and the edition-unique parts of D02,
  D04-D06; caller origin: claude). Structural findings:
  - No forecast, outlook or guidance edition anywhere (series grep: none; D03 defers guidance to
    after closing; D01's 2020 plan has no 2020 actuals). Every Medium/High pass so far (aq-00964 q01,
    aq-00745 q09) used an event reported beside its own later outlook; that material is absent.
  - No same-period figure is restated except the 2026 PRM fold-in. Every 2025 value repeats in D06
    and D07; walks are rebuildable from later per-Boe tables; D07 explains the FCF definition change.
  - Robustly unique facts: D01 (Dec 31, 2019 balances, 2020 plan), D03 (deal terms, dividend dates,
    $4.08 rate), D07 (2Q26, H1 2026, June 30, 2026), D05 (Sep 30, 2025 PRM split). Encino-quarter
    anchors (2Q25) are guessable from the series' 2Q25 Encino costs, so D03 fails the removal test
    unless the anchor is a dividend date (4Q25, duplicated in D06/D07).
  - Feasible mechanisms were already measured Easy or too easy here (q01-q04).
- Round 4 sketches i07-i10 (ideas.md): user quick-tested all four, each "Survived — worth writing
  up" (screenshot saved in q05's run results). Chosen: i07 (only sketch whose two documents both
  survive the removal test; i09/i10 anchors are inferable or guessable).
- q05 (i07 = platform draft 1; target medium). Rev 0 (6d615228...) reviewed revise / easy. User
  chose to submit it anyway (2026-10-06). Form flagged rev 0 steps 1-2 ("Doc 1 doesn't mention
  5,175", "Doc 7 doesn't mention 7,926": figures after a quoted label). Rev 1 (ba6b4f23...):
  plain "current and long-term debt of 5,175"; A/B match, audit clear, closed-book misses;
  review running. Form reaction to rev 1 pending from the user.
- q06 rev 0 (from i09; target medium): YoY volume effect by EOG's bridge method, $0.94; D03 + D07;
  tested_sha256 7adb1a8d.... A/B match, audit clear, closed-book misses (recalled May 30, 2025);
  review revise / easy: Doc 3 removal risk high (date public and implied by 2Q25 Encino costs),
  $0.95 via daily-rate volumes, q02-family bridge. Status checked.
- User chose "stay here". Long shot q07 (i11; dividends declared over the four quarters after
  the Oct 17, 2025 record-date dividend's declaration quarter -> $3.06, decoy $4.08) DROPPED:
  A/B match, audit clear, but the closed-book run reached $3.06 from recall. The 1Q24->2Q26
  bridge-method idea fails one-clear-answer (printed 46.73 vs derived 46.74 flips $0.72/$0.71).
  Recommended stopping here; awaiting the user's decision.
- Questions: q01-q04, q07 dropped; q05, q06 checked (rev 0, both revise: easy; other session).
- Runtime: Claude Code (VS Code), Opus 5.5 max; fresh Agent subagents for checks.
