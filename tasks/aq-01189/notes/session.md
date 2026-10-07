# Current bundle checkpoint

- Goal and user constraints: user 2026-10-05: "set target difficulty as at least Medium" and start
  AQ-01189; after reaching a result, check carefully again. Slots open: Hard 0/2, Medium 0/3,
  Easy 0/1 (capture L157-161); Medium or High tier qualifies, "Too hard" does not.
- Verification target / measured platform tier: medium / pending (8 of 8 difficulty runs left,
  0 of 10 quick tests used; Claude took no platform action).
- Prepared runs: q01 rev 0 tested_sha256 4f49c8dd057866863e7d56d99a0d8fd480d1dd1a37da4b261ee9d10c52b14c16;
  q02 rev 0 tested_sha256 596fc28dbf685c815794744aecfbea07a6e9f457c77b6b1911a3aa6df90f29f1; no source gaps.
- Bundle: D01 = Doc 3 BHP 9M Mar-26 (22 Apr 2026); D02 = Doc 4 BHP FY26 (16 Jul 2026);
  D03 = Doc 1 FCX 1Q26 (23 Apr 2026); D04 = Doc 2 FCX 2Q26 (23 Jul 2026). Capture complete; map
  complete; all tables are pipe rows (prose/single-cell quotes only).
- Phase: both questions locally checked; handed over for platform full checks + difficulty check.
- Questions:
  q01 checked (FCX edition bridge: May 2026 Cerro Verde stake -> April outlook; 1H SA sales 493 /
  1.05 bn = 47.0%; decoy 49.3%). A/B match, closed-book miss, audit clear, review ready medium (marginal).
  q02 checked (BHP edition bridge + operated filter: guidance on 2 Apr 2026 Carajás completion =
  pre-22 Apr ranges; gold Pampa Norte (Spence), NSW Energy Coal; decoy {NSWEC}). Same record set.
  Both reviews: main risk an Easy placement; same mechanism family (correlated risk).
- Open unknowns: form handling of q01's two-document steps 5-6; whether "in any order" clears the
  format advisory; platform model checks and removal test.
- Decisions: split_capture.py heading regex extended (+test); suites 26/19 OK (rechecked at hand-over).
- Candidate families: h1/h6 promoted; i03 (cross-company calendar), i05 (exact vs rounded) held as
  fallbacks; i04 dropped; h2/h3 FCX siblings held.
- Revision rounds used / open platform feedback: 0 / none.
- Next action: user pastes fields, runs full checks and difficulty check; record verbatim results
  (docket-feedback); if Easy/Too easy, design a different source relationship rather than rewording.
- Runtime: Claude Code, Opus 5.5 max; fresh subagents (omitClaudeMd roles) for blind checks.
