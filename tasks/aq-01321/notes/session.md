# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user (2026-10-06) "work on AQ-01321 ... difficulty_target to at least
  medium". Platform slots: Hard 0/2 · Medium 0/3 · Easy 0/1; 9 submissions, 8 difficulty runs,
  10 quick tests left (capture 11:39). Medium or Hard pass needed.
- Verification target / measured platform tier: medium / pending (no platform access here).
- Bundle: aq-01321, 12 earnings-release exhibits (ADI, Microchip, TI, onsemi; three each); capture
  .txt (split_capture.py extended); complete, no gaps; doc-map complete.
  Local id -> platform Doc: D01-D03 = 1-3 (ADI); D04 = 6, D05 = 4, D06 = 5 (MCHP); D07 = 11, D08 = 12,
  D09 = 10 (ON); D10 = 8, D11 = 9, D12 = 7 (TXN).
- Phase: HANDED OVER for quick tests (2026-10-06). Batch order: q02, q01, i05, i08, i03.
- q02 rev 1 CHECKED (f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456): TI twelve
  months to June 30, 2026, (R&D + SG&A) / revenue, two decimals; docs Doc 7, 8, 9. A/B match, audit
  clear, closed-book miss, removal probes (no Doc 7 / no Doc 8) forced the rounded-prose route; review
  ready, difficulty easy (Medium ~12%, High ~3%). Form risk: 7 of 11 quotes pipe-free (L220 spans an
  empty cell): Save passage.
- q01 rev 1 CHECKED (a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba): Microchip
  inventory reduction from the end-of-calendar-2024 peak by the close of FQ1 FY27, one decimal; docs
  Doc 5, 6. Review ready, difficulty easy (Medium ~9%). Form risk: Doc 6 row quote pipe-free.
- Sketches (blind match + closed-book miss each): i05 combined revenue of quarters ended Apr 1-Jun
  30, 2026 ($B, one decimal); i08 onsemi buybacks / LTM FCF (one decimal; D09 removal risk); i03
  onsemi Q2 ranges below midpoint. i04 = q01 as % (never with q01). i06 dropped (closed-book reach).
- Decisions: no same-period forecast editions; within-company timing anchors all tied; recall of
  headline actuals reaches late April 2026 (memory updated; golds kept out of memory).
- Next action (user): quick-test the batch; paste verbatim results; run a difficulty check only on a
  survivor, after saving passages for pipe-row quotes; record results with docket-feedback.
- Runtime: Claude Code, Opus 5.5; blind-solver/shortcut-auditor (scope hook; re-run prepare to
  re-bind, MAX_BINDINGS 16 shared), closed-book (no tools), question-review.
