# Current bundle checkpoint

- Goal and user constraints: user 2026-10-18 "let's work on AQ-06708_2026-10-18_1544. there is no slot for Easy or
  Medium Tier for this bundle, we should target high. do your best." Page: "Hard 0/5 · Medium closed · Easy 0/0";
  quick tests 0 of 20; 8 submissions left; clock "13h 17m left ... Expires at Mon 5:01 AM" as saved 15:44.
- Verification target / measured platform tier: hard / q01 rev 0 Run 1: Too easy, High 3/6 (A 0/3, B 3/3), extra run granted.
- Prepared run / tested_sha256: q01 rev 0 a99e6e2df0d8fafe14e925317c9b550ce4c4096c2f1e59a147fd40e2c0c0c65d (runs/q01-r0-v2-a99e6e2d...-platform).
- Bundle slug / documents / extraction warnings: aq-06708; Pinterest and Snap filings, capture complete (7 of 7 in
  full, no gap markers). D01 = Doc 2 Pinterest Q1 2026 release; D02 = Doc 4 Pinterest Q1 2026 10-Q; D03 = Doc 1
  Pinterest Q2 2026 release; D04 = Doc 3 Pinterest Q4/FY2025 release; D05 = Doc 6 Snap Q1 2026; D06 = Doc 5 Snap Q2
  2026; D07 = Doc 7 Snap Q4/FY2025. Repeat check: no earlier Pinterest or Snap bundle (captures, tasks, 10.6, 10.7).
- Phase: rounds 1-3 screened (i01-i06, each local 3/3); quick tests of all six: "all too easy" (user, 10-18,
  twice); round 4 (user "go on"): i07, i08 lists, local 3/3, quick tests too easy; round 5: i09 (3M move), local 3/3; handed over. notes/doc-map.md (releases read in full; 10-Q l.1-1340 and l.2155-2394 read, risk factors searched).
- Questions: q01 (from i09, quick test survived 10-19): checked, floor 0 FAIL / 5 WARN answered; handover-q01.md.
- Decisions and constraints: no restated or quietly edited figures in the bundle (mine.md; Snap's tables agree
  across D05-D07). Pinterest Q3 2025 and Q1-Q3 2025 FX exist only as FY less Q4 less H1. Snap's constant-currency
  figures exist only in D06 (2025 quarters backfilled). Pinterest's releases omit their "About non-GAAP" section.
- Candidate families tried: h1 currency lift (i01 $12 million), h2 earliest 2025 operating-profit quarter
  (i02 29.2%), h10 Snap growth excluding Other Revenue (i03 -2), h11 SBC reconciliation-line growth (i04 33.2),
  h12 convertible dilution at 150% (i05 2.59%), h3 Snap restructuring ex SBC/D&A (i06 $42M). Held h5-h7; rejected h4, h8, h9, h13.
- Changed files: notes/doc-map.md, hooks.md, ideas.md, calc-hooks.py, sketches/i01-i04.md, session.md, mine.md,
  intake.json; runs/i01-screen-8d903db3c7cf366c, i02-screen-afcc8d3eeb9fefc2, i03-screen-0e4b36d88e45a350,
  i04-screen-25fc316dc723fbf4, i05-screen-c1301d06ef1c8e91, i06-screen-a07a510cd253c3d5; ledger rows 106-114 (renumbered 10-19 after a collision with other sessions' rows 53-105); runs/i07-, i08-screen-*.
- Revision rounds used / open platform feedback: 5 sketch rounds / FB-01 (verdicts/AQ-06708_difficulty_2026-10-18_2146.txt):
  difficulty run locked until the full Checks pass, 0 runs, no result.
- Active feedback index: notes/feedback-index.md (FB-01 resolved; FB-02 redesign: i10 screened 3/3, quick test failed 10-19).
- Five-candidate trial: not enrolled.
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / i01, i03 / none (sessions
  81146b4a, 57a46717, 88381ff3, 8fa9eb57 stopped before solver waits; intake and reading before 23:36Z untimed: coverage partial; i09 untimed).
- Next action: user runs the full Checks on q01 and saves them (verdicts/); clear any blocking row (own-words risk,
  aq-05747); then the difficulty run, saved before Submit. Captures: tasks/aq-06708/verdicts/. Trial slots full.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5); blind-solver role effort max.
- Optional diagnostic if needed: none.
