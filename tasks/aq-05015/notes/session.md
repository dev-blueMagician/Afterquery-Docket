# Current bundle checkpoint

- Goal and user constraints: user 2026-10-14 "no slot for Easy Tier ... target medium and high. do
  your best." Page (15:26): "Still open on this set: Hard", "Hard 0/5 · Medium closed · Easy 0/0".
  Target hard. Workspace rules changed 19:19 (CLAUDE.md, WORKFLOW 4, hard-playbook.md): every Hard
  sketch gets a three-solver strong-solver screen before it is offered; every fair sketch goes to the
  user with its result; the user decides.
- Verification target / measured platform tier: hard / none yet (no difficulty run).
- Prepared: q01 rev 0 tested_sha256 a92b895d...b092 (runs/q01-r0-v2-a92b895d...-platform); q02 rev 0
  daf1d452...a660 (runs/q02-r0-v2-daf1d452...-platform). Both checked, floor 0 FAIL.
- Bundle: aq-05015 Valero, D01 2021 tender offer; D02-D08 releases Q4 2024-Q2 2026. Dnn = Doc n.
  Capture complete. New bundle (no earlier Valero bundle).
- Phase: quick test (user 2026-10-14): i03, i05 survived, i04 failed. q01 (i03) and q02 (i05) written
  up word for word, prepared, full hand-overs given; difficulty runs pending (user's choice).
- Round 1: i01/i02 (h1 silent cost-of-materials reclassification) quick test "too easy" (user, one
  report for both); family closed (playbook: unpinned rests on an unstated inclusion, pinned is a
  rebuilt number).
- Round 2: i03 (h9 West Coast opex per barrel Q3 -> Q4 2025, -$1.3, lure +$0.8 printed adjusted
  rows) screen 3/3 right, ranked last, ledger row 12. i04 (h4 DGD 2025 capex vs outlook, $50M) and
  i05 (h7 2025 non-sustaining capital, $203M) screens 3/3 each (ledger rows 14, 15). All three offered,
  ranked last; no sketch in this bundle has drawn a local miss.
- Hooks without a sketch: h3 (2025 notes retired since 2021, 1,210; recall risk on issue sizes), h6
  (West Coast margin per barrel over the closure, weighting), h2/h10 (fail delete-and-guess), h5
  (necessity routes), h8 (renamed caption). None is of a playbook kind with a Hard result.
- Arithmetic: notes/calc-h1.py, calc-h9.py, calc-h4-h7.py.
- Five-candidate trial: full; efficiency timer not running (sketch timing this turn not measured).
- Next action: user runs q01 and/or q02 (Checks first: "One defensible answer"); record each verdict
  (question file + ledger rows 12/15) and decide that question's next action. Unsketched: h3, h6.
- Runtime/model/effort: Claude Opus 5.5, Claude Code (VS Code); screens: blind-solver
  (claude-opus-5-5, effort max), fresh contexts.
