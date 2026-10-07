# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user (2026-10-06) "work on AQ-01321 ... difficulty_target to at least
  medium". Platform slots at capture: Hard 0/2 · Medium 0/3 · Easy 0/1; 9 submissions, 8 difficulty
  runs, 10 quick tests (counts now lower; not re-captured).
- Verification target / measured platform tier: medium / q02 platform version passed at Easy (user
  report 2026-10-06, tier line not supplied); no Medium result yet.
- Bundle: aq-01321, 12 earnings-release exhibits (ADI, Microchip, TI, onsemi; three each); capture
  .txt (split_capture.py extended); complete, no gaps; doc-map complete.
  Local id -> platform Doc: D01-D03 = 1-3 (ADI); D04 = 6, D05 = 4, D06 = 5 (MCHP); D07 = 11, D08 = 12,
  D09 = 10 (ON); D10 = 8, D11 = 9, D12 = 7 (TXN).
- q02 SUBMITTED and FROZEN (2026-10-07, user: "set q02 status as submitted and set accepted_tier as
  Easy Tier"); frontmatter status: submitted, accepted_tier: Easy Tier; fingerprint unchanged
  (f1d2a9bc...). Platform: the user's reworded version was blocked as "too vague" (both form solvers
  took the rounded $3.9 billion route); the narrowed version passed at Easy (user report). Exact
  submitted text not supplied (identity gap logged); later findings go to notes/feedback-q02.md.
  New questions must not repeat q02's fact (TI twelve-month R&D + SG&A ratio) or its path.
- q01 rev 1 CHECKED (a82bd87c...): Microchip inventory reduction from the end-of-calendar-2024 peak by
  the close of FQ1 FY27; stale "now" figure in the March-quarter release. Reviews Easy-leaning, but the
  q02 form check shows platform solvers take stated figures that match the wording, so q01's pull may be
  stronger than estimated (risk both ways: Medium, or a "too vague" block).
- Sketches: i05 (quarters ended Apr 1-Jun 30, 2026, combined revenue), i08 (onsemi buybacks / LTM
  FCF; D09 removal risk), i03 (onsemi ranges below midpoint); i04 = q01 as % (never with q01); i06
  dropped.
- Lessons saved: memory (form-checks Step 9 flag; one-clear-answer vagueness; calibration; recall to
  late April 2026); golds kept out of memory.
- Next action (user): optionally paste q02's exact submitted text and tier line (for feedback-q02.md);
  quick-test q01 (then i05, i08) for Medium; difficulty check only after a quick-test survival and a
  clean "One defensible answer" check.
- Runtime: Claude Code, Opus 5.5; blind-solver/shortcut-auditor (scope hook; re-run prepare to
  re-bind, MAX_BINDINGS 16 shared), closed-book (no tools), question-review.
