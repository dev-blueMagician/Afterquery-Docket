# Current bundle checkpoint

- Goal and user constraints (2026-10-06): restart Trial 1 from scratch; one submission attempt;
  re-check carefully after reaching a result. Target was at least Medium; after both write-ups
  failed the quick test the user relaxed it: "actually in trial, it's okay if accept in even Low
  tier" (Easy accepted).
- Verification target / measured platform tier: easy / pending.
- Prepared runs (source_gaps none): q03 rev 2 987c25e32fae91ba826f09cae16d35fdb76513d4807bdb0b4345130b165bbd51
  (re-bound 2026-10-06 for round-3 sketch solves); q01 rev 0 604695ceac0f43ad3983b6d199cb01e630307ff984d5d6eb7cc8a23ae6b28336.
- Bundle: capture AQ-DOCKET-TRIAL-01_2026-10-06_0110.md, D01-D06 = platform Doc 1-6, complete.
- Platform quick tests: 2 of 10 used, both "Too easy — solver got it" (q03, q01; Feedback logs).
  Coach analyses: notes/feedback-coach-2026-10-06.md ("One lookup plus one operation is usually
  solved"; use three or more dependent steps, scattered pieces, restated figures).
- Questions: q03 rev 2 and q01 rev 0 checked but too easy (keep as records); q02 dropped.
- Phase: round 3 sketches (notes/ideas.md, notes/sketches/i10-i15). Blind solves matched i10
  16,879, i11 17,312, i12 3, i13/i14 0.0002 and 248,685 (all high); closed-book unknown for i10,
  i11, i13; i12 dropped (closed-book recalled the chapter page ranges). Returns:
  runs/sketch-round3/returns.md. Hand-over: notes/quicktest-round3.md (S1 i11, S2 i15, S3 i10).
- q04 rev 0 (user: "QA like Trial 2's q01 or Trial 6's q02"): run ced2e12b09a10904dcce43687b70c32c04f9668e1b03291d9458fc7ced840014;
  gold 11.0 percentage points (14,638 / 33,538 minus 979 / 3000); A/B match high, audit clear,
  closed-book unknown, removal probes 10.0 (no D02) and 22.4 (no D05). Review: ready (local),
  difficulty easy marginal, Too easy about 65%. Status checked.
- q05 (sibling without q04's signposts; both shares against all genes with expression data):
  rev 0 (two decimals, 2.70) all checks passed but 2.6967 sat 0.0017 above 2.695 (coarse early
  rounding gives 2.67); rev 1 asks one decimal, gold 2.7 times, run f73ebf6033c08e869c72efe94c2f14f2323d143643c92c3524ee7c573107f6e4:
  A/B match high, audit clear, closed-book unknown, probes 11.3 and 3.0 miss; quotes verified
  against the capture. Review ready (local), Easy marginal: Too easy ~50%, Easy ~40%, Low 0/5 ~10%;
  status checked. Hand-over notes/handover-q05.md (preferred over q04). Submit at most one of q04,
  q05 and sketch i10 (same inputs).
- Next action: the user quick-tests the batch (3 of the 8 remaining); record verdicts verbatim;
  suggest "Harder variations" on q01/q03 as a second source; write up only sketches the low model
  misses, then removal probes, full checks and a second careful check before the one submission.
- Runtime: Claude Code, claude-opus-5-5; blind-solver (scope hook), closed-book-solver,
  shortcut-auditor, question-review.
