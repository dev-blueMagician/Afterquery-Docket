# Current bundle checkpoint

Working memory for resuming aq-03635; never submitted. Updated 2026-10-13 (round 2 all too easy; release advised).

- Goal and user constraints: user, 2026-10-12: "there is no slot for Easy Tier for this bundle, we should
  target medium and high. do your best." Easy is not usable: never offer it or re-ask.
- Verification target / measured platform tier: medium (Hard welcome) / none at target. Only in-band result:
  q03 rev 0, Run 1 (Version 0d7da7), "In band — Easy tier", Low 2/5, not submitted. 14 of 15 runs left.
- Prepared runs (history): q03 rev 1 e45f6430... (blocked on the form), q03 rev 0 003d8a3d... (Easy, kept in
  runs/q03-r0-v2-003d8a3d...-platform), q02 9be1dc93... (dropped), q01 ff49c0d6... (untested, same hook).
- Bundle / documents / extraction: eleven papers from the NZ Commerce Commission's 2019 retail fuel market
  study. Local -> Doc: D09 = 1, D01 = 2, D03 = 3, D04 = 4, D06 = 5, D07 = 6, D08 = 7, D10 = 8, D11 = 9, D02 = 10,
  D05 = 11. No gaps. Not a repeat bundle. Family: aq-03120, aq-03423, aq-03557, aq-02940, aq-03066.
- Phase: sketching closed after two rounds; decision returned to the user (release advised).
- Everything tested (quick tests are the user's chat reports, no panels):
  - Hook h1 (Doc 9 + Doc 1, Z's return against the reasonable-return range): i06 / q02 yearly peak, quick
    test too easy; i07 / q03 rev 0, quick test survived, Run 1 Easy (Low 2/5: three low attempts kept their
    own mean of the year-end balances, 3.7; two and the strongest solver took the printed 2,085 on the
    wording match); q03 rev 1 with the label words removed, form "One defensible answer" Failed (4.4 and
    3.7). Named it is Easy, un-named it is vague; no step between. q03 dropped.
  - Other pairs, all quick-test too easy ("all are too easy for quick test", 2026-10-13): i05 (47 sites,
    Doc 10 + Doc 6), i08 (26 sites, Doc 10 + Doc 4 + Doc 8), i09 (41 days, Doc 11 + Doc 1), i02 (28.65
    cents, Doc 1 + Doc 2).
- Untested and not offered: q01 (61.9%), i01, i03b (same step as q03), i04 (date arithmetic like i09).
- Search coverage: all eleven documents read in full by the caller; two independent author runs; hooks
  h1-h14 in notes/hooks.md, each closed or dropped with its reason.
- Feedback index: notes/feedback-index.md rows aq-03635-q03-D1 (Run 1) and -A1 (rev 1 blocked). Raw:
  verdicts/AQ-03635_difficulty_2026-10-13_0103.txt, notes/platform-feedback/q03-rev1-checks-2026-10-13-*.png.
  Lessons in .claude/memory/docket-local-solver-calibration.md (Current rule, three 2026-10-13 entries).
- Efficiency ledger ../../../notes/efficiency.json: candidate i07, one difficulty attempt, one revision,
  outcome retired before submission; five trial slots full (unpromoted); no timer running.
- Next action: user decides. Advised: release the bundle (no fair medium or hard design found; 14 runs and
  some quick tests unspent). If the user wants another round, it needs a new mechanism, not a rewording.
- Runtime/model/effort: Claude Opus 5.5 in the VS Code extension.
- Optional diagnostic: none.
