# Current bundle checkpoint

- Goal and user constraints: user, 2026-10-06: "work on AQ-01278_2026-10-06_1140. you should do
  difficulty_target to at least medium." Page slots: Hard 0/2, Medium 0/3, Easy 0/1; 9 submissions,
  8 difficulty runs, 10 quick tests left (capture 2026-10-06 11:40).
- Verification target / measured platform tier: medium / pending (no platform result)
- Prepared run / tested_sha256: q01 rev 1, runs/q01-r1-v2-3ebf025f...; tested_sha256
  3ebf025f20297efd4410fb17acafb57aae015cdf862448ef10f9c9e68639def3 (rev 0 run 318df468... is history)
- Bundle: aq-01278, PEER corporate filings, 10 docs, Q1-Q2 2026 releases of four P&C insurers.
  Local id = platform Doc: D01=Doc 5, D02=Doc 10, D03=Doc 6 (Allstate Q1, Q2, Q1 supplement);
  D04=Doc 4, D05=Doc 9 (Chubb Q1, Q2); D06=Doc 1, D07=Doc 7 (Progressive March, June);
  D08=Doc 2, D09=Doc 8, D10=Doc 3 (Travelers Q1, Q2, Q1 supplement). Cite Doc N in form fields.
- Intake: split from the plain-text capture with docket-e1's new .txt parser; no gaps; text/Dnn.txt
  equals docs/ line for line. Map complete (notes/doc-map.md, all ranges read).
- Phase: quick-test batch handed to the user (notes/quicktest-batch-1.md: q01, i03, i05, i06, q02);
  q01 checked; q02 rev 1 draft awaiting evidence re-copy.
- Questions: q01 checked rev 1 (Travelers worldwide personal auto NWP 2Q25->2Q26, -10.41%): floor
  0 FAIL / 2 WARN explained; A and B match; closed-book unknown (miss); audit clear; removal probes
  -10.37% (no D09) and -5.59% (no D10), both misses. Rev 0 review: revise, difficulty easy
  (cue defused the decoy; one-decimal removal coincidences; Step 6 uncited; "its"). Rev 1 review: ready,
  difficulty easy (Medium+ ~13-15%); status checked. q02 draft rev 0 (Chubb NA commercial on the Q1
  2.8% basis, Q2 -1.3%, run 8065adb6...): A and B match, audit clear, closed-book +2.4% miss, probes
  -2.3% (no D04) / +2.0% (no D05); rev 0 review revise (reasoning/evidence only; easy-marginal,
  Medium+ ~18%). q02 now draft rev 1 (317625d3...: "percentage change", split step, decoy step);
  final checks wait for the Save-passage evidence re-copy.
- Decisions: Q2 editions print six-month/YTD columns; Q1 editions needed only for March 31 values,
  Q1-only prose, Q1 supplements and Chubb's Q1 segment figures. Progressive component ratios do
  not rebuild from dollars (avoid). solver-scope.json caps at 16 runs (peers warned).
- Rounds used: 2 sketch rounds (i01-i14); q01 revisions used: 1 of 2; q02 none.
- Next action: record q02 review; await user's quick-test panel lines; for survivors, Save passage
  re-copy of pipe-row quotes, re-prepare, rerun bound checks, then difficulty run.
- Runtime: Claude Code (VS Code), claude-opus-5-5; fresh agents per role.
