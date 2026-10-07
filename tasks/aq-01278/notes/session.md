# Current bundle checkpoint

- Goal and user constraints: user, 2026-10-06: "work on AQ-01278_2026-10-06_1140. you should do
  difficulty_target to at least medium." 2026-10-07: the form now requires Targeted failure modes, and
  every hand-over carries all form fields (check_questions.py --handover -> notes/handover-qNN.md).
  Page (2026-10-07): slots Hard 0/2, Medium 0/3, Easy 0/1, "In review: Medium 1", 8 submissions and
  6 of 8 difficulty runs left.
- Verification target / measured platform tier: medium / Run 2 (version a75c90, consistent with rev
  3/4): "In band — Medium tier", Low 0/5 · Medium 1/5 · High —, "passes on the current content"; the
  same saved page calls it "for an earlier version", so it is recorded as unknown (task page,
  2026-10-07, runs/q02-platform-a75c90/). Version 4093c3, a wording no local revision had (corrected
  2026-10-07), was submitted and returned "Revision requested" (notes/feedback-q02.md).
- Prepared run / tested_sha256: q02 rev 4, runs/q02-r4-v2-f8d502af...; tested_sha256
  f8d502af3abf9790a43a7a1b8c0be58613a857813b7af5921d0b1a8ad2ccaa40 (q01 rev 1: 3ebf025f...)
- Bundle: aq-01278, PEER corporate filings, 10 docs, Q1-Q2 2026 releases of four P&C insurers.
  Local id = platform Doc: D01=Doc 5, D02=Doc 10, D03=Doc 6 (Allstate Q1, Q2, Q1 supplement);
  D04=Doc 4, D05=Doc 9 (Chubb Q1, Q2); D06=Doc 1, D07=Doc 7 (Progressive March, June);
  D08=Doc 2, D09=Doc 8, D10=Doc 3 (Travelers Q1, Q2, Q1 supplement). --handover maps them.
- Intake: split from the plain-text capture; no gaps; text/Dnn.txt equals docs/ line for line. Map
  complete (notes/doc-map.md, all ranges read).
- Phase: q02 resubmission hand-over (notes/handover-q02.md, every field).
- Questions: q01 checked rev 1 (Travelers worldwide personal auto NWP 2Q25->2Q26, -10.41%): A and B
  match, closed-book miss, audit clear, review ready (easy); no failure modes yet (floor WARN), so it
  is not hand-over complete. q02 checked rev 4 (Chubb NA commercial plus agriculture, Q2 -1.3%):
  A/B match, closed-book +2.3% miss, audit clear, reviews rev 2-4 ready (medium, marginal; logged
  2026-10-07 from raw returns), Run 2 recorded as unknown against f8d502af. At capture the form's
  evidence (8 rows) and tags (2) differed from rev 4; the reasoning box was not saved. One failure
  mode, outside the fingerprint: Part vs total / Misapplies a rule or premise (-2.3%, 9 of 10 Run 2
  attempts). The independent review on 2026-10-07 verified the gold and the hand-over and had the records
  corrected and a second, unobserved mode (-1.4%) withdrawn. Its re-check closed every finding.
- Decisions: Q2 editions print six-month/YTD columns; Q1 editions needed only for March 31 values,
  Q1-only prose, Q1 supplements and Chubb's Q1 segment figures. Progressive component ratios do
  not rebuild from dollars (avoid). Keep Doc 4 and Doc 9 as Answer component (the passing run's
  ticks). solver-scope.json caps at 16 runs (peers warned).
- Rounds used: 2 sketch rounds (i01-i14); q01 revisions 1 of 2; q02 rev 4 (platform-driven).
- Next action: the user pastes every field of notes/handover-q02.md, replacing the reasoning, all
  evidence rows (10) and the tags (4), and adds failure mode 1. They press "Re-run failed" ("Needs the
  documents" could not run), then read the difficulty panel. If it shows the pass as current, they
  submit. If it asks for a new run, they run it on exactly this content (6 of 8 left). Either way they
  send the page; then record the result, set q02 submitted and freeze it. Other slots are open; never
  pair i13 with q02.
- Runtime: Claude Code (VS Code), claude-opus-5-5; fresh agents per role.
