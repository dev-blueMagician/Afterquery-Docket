# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal (user, 2026-10-08): "remove q01 ~ 07 and work again ... there is no slot for Easy Tier for
  this bundle, we should target medium and high. do you best." Targets: difficulty_target medium
  (a Medium or High pass). Standing rule: one removal probe per ticked document before any hand-over
  or platform run (memory docket-removal-probe-required).
- q01-q07 moved unchanged to archive/round1-q01-q07/ (README there lists each outcome). New
  questions start at q08 so the old ids stay unambiguous in records and memory.
- Platform page (2026-10-08): 4 of 8 difficulty runs left; slots Hard 0/2, Medium 0/3, Easy 0/1
  ("In review: Easy 1"); 8 submissions left. Quick tests (one low-model attempt, "Survived" or "Too
  easy") are separate from the runs; 2 of 10 used on 2026-10-06, then 4 in round 4, so about 4 left.
- Source: complete capture AQ-00949_2026-10-06_0251.md; no gaps; local D01-D07 = platform Doc 1-7.
- Structural limits (rounds 1-5, re-confirmed in round 6): 2024 quarters repeat in D02/D04/D05, 2025
  quarters in D06/D07; no outlook or restated figures (only the 2026 PRM fold-in and relabels).
  Individually necessary facts: D01 (2019 balances, 2020 plan), D03 (deal terms; dates inferable from
  the series' Encino costs), D05 (Sep 30, 2025 PRM split, Bapco), D06 (1Q26 Bahrain-only note), D07
  (2Q26, June 30, 2026). The platform passed q04 on a D01 input (end-2019 debt), so D01 + D07 is the
  best-proven pair. Lookup-plus-arithmetic designs measured Easy or Too easy here.
- Round 6 (ideas.md): new family, reasoning on a leverage ratio, with D07's printed total
  capitalization as the systematic shortcut.
  - i12: additional net debt, equity fixed, to lift the June 30, 2026 net debt-to-total-cap ratio to
    the end-2019 ratio from reported net debt and equity -> $1,615M (shortcut $1,410M; printed 13%
    $1,742M; ratio rounded first $1,616M).
  - i13 (sibling): signed total-debt change on the GAAP ratio -> -$306M (shortcut -$247M; 19% -$452M).
  - i14: net debt rise Jun 30, 2025 ((980)) to Jun 30, 2026 (3,019) beyond D03's $3.5B debt plan ->
    $499M (sign slip -$1,461M; borrowings route $527M).
  - Screens (raw: runs/sketch-r6-a4/results/, runs/sketch-r6-b9/results/): each full-bundle solve
    matched with high confidence; each closed-book missed (no June 2026 data; recalled the 2019 and
    deal inputs exactly); each probe "not answerable" unforced, the gold forced from memory (p 0.6 /
    0.6 / 0.75): a stated recall risk, not a probe failure.
- User 2026-10-08: "prepare both" -> i12 = q08 (71912869...), i14 = q09 (3d35521f...), rev 0, status
  checked, hand-overs notes/handover-q08.md and -q09.md. Both: A/B match, audit clear, closed-book
  misses, probe without D07 misses, probe without D01/D03 "not answerable" but gold forced from
  memory (p 0.5 / 0.65). Reviews: revise, difficulty easy (q08 rough guess Too easy ~45%, Easy ~40%,
  Medium <=10%; q09 Easy or Too easy). Advice to user: quick-test both before any difficulty run;
  "Too easy" = retire the design. i13 (sibling of q08) still held.
- Runtime: Claude Code (VS Code), Opus 5.5 max; fresh Agent subagents for checks. Subagents see the
  harness git status, which lists the archived runs' deleted file names (a probe can see that the
  removed document's file exists; this makes local probes more conservative, not less).
