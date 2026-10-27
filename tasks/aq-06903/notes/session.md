# Current bundle checkpoint

- Goal and user constraints: user 2026-10-18: "there is no slot for Easy or Medium Tier for this
  bundle, we should target high. do your best." Repeat of aq-01189 (same four documents); user
  chose "Proceed, Hard" after the repeat check (2026-10-18).
- Verification target / measured platform tier: hard / pending (7 of 20 quick tests used, all failed).
- Prepared run / tested_sha256: none (sketch phase; no question file).
- Bundle slug / documents (ids) / extraction warnings: aq-06903; D01 = Doc 3 BHP 9M Mar-26,
  D02 = Doc 4 BHP FY26, D03 = Doc 1 FCX 1Q26, D04 = Doc 2 FCX 2Q26; capture complete (capture
  page carried a "Docket has been updated. Reload this page" notice); no gaps.
- Phase: STOPPED (user, 2026-10-19: "Stop on this bundle"). Two rounds, seven Hard designs (i01-i07),
  every one local 3/3 and every one failed its quick test (ledger rows 97-101, 104-105). Nothing written up.
  Round 1 quick tests 2026-10-19: all five failed (user: "all failed"). Earlier: sketches handed over (round 1). Strong-solver screen 2026-10-19: i01-i05 all 3/3 right
  (15 of 15, high confidence); records in sketches/iNN.md, raw returns in runs/iNN-screen-*/returns,
  ledger rows 97-101 (notes/hard-runs.md).
- Questions: none yet.
- Decisions and constraints: no restated figures in the bundle (mechanical checks); aq-01189's
  edition-bridge hooks not reused; kt vs lb comparisons excluded (no conversion printed).
- Candidate families tried: h1-h5 (round 1, all failed quick tests); h10, h11 (round 2); h6, h7 held; h8, h9 rejected.
- Changed files since the last checkpoint: notes/doc-map.md, hooks.md, ideas.md,
  sketches/i01-i05.md, runs/i01-i05 screen packets.
- Revision rounds used / open platform feedback: 0 / none.
- Active feedback index / issue ids / current fix: none.
- Five-candidate trial owner index / candidate row: not enrolled (no promotion yet).
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / i01 /
  stopped at hand-over (second interval).
- Next action and blocker, if any: none. If this bundle is claimed again, the repeat check should
  show this record. Unused leftovers: i06 on net income (23), a gold-ounce version of i07, BHP Q4
  FY26 exploration expensed share (84.2%); all variants of kinds that failed here.
- Runtime/model/effort: Claude Code, Opus 5.5 (claude-opus-5-5); blind-solver role pinned to
  claude-opus-5-5, effort max, omitClaudeMd.
- Optional diagnostic if needed: none.
