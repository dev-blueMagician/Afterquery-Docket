# Current bundle checkpoint

- Goal and user constraints: user (2026-10-18): "there is no slot for Easy or Medium Tier for this bundle, we
  should target high. do your best." Hard target; sketches first, screened, every fair sketch handed over.
- Verification target / measured platform tier: hard / q01 rev 1 Run 1 (Oct 18 9:57 PM, Version 5b4cb3): Answer not
  supported, Low — · Medium — · High 0/6; verdicts/AQ-06840_difficulty_2026-10-18_2247.txt; 14 of 15 runs left.
  q02 rev 2 not run yet.
- Prepared run / tested_sha256: q02 rev 2 03d88618b883af065f9ad34d566d624faa8e2551e92714f0fca72720987f8d9d (current);
  q01 rev 1 0ceca174... (failed Run 1); q02 rev 0 and rev 1 (0b8ca66d...) never run.
- Bundle slug / documents (ids) / extraction warnings: aq-06840, 8 docs complete (capture
  AQ-06840_2026-10-18_1806.txt); D05=Doc 1 (Q3 24), D07=Doc 2 (Q4/FY 24), D01=Doc 3 (Q1 25), D03=Doc 4 (Q2 25),
  D06=Doc 5 (Q3 25), D08=Doc 6 (Q4/FY 25), D02=Doc 7 (Q1 26), D04=Doc 8 (Q2 26). Not a repeat bundle.
- Phase: q02 rev 2 handed over as the full form (2026-10-19): i07's sentence word for word after the user's quick
  test ("i07 survived"); 0 FAIL, 12 WARN. i06 (q01's repair): quick-test result not reported; q01 stays rev 1.
- Questions: q01 checked rev 1 (gold 711.8; failed Run 1, "basis" read as the FCF definition, F1); q02 checked rev 2
  (gold 767; "Using the most recently published figures", F2). Evidence quotes table rows with their pipes, each
  checked against the capture's own text (rev 0's pipe-free quotes were rejected by the form, F0). One mode each:
  Superseded date or version / Picks the wrong entity or section (q01 717.8, q02 765).
- Screen results (blind-solver claude-opus-5-5 max): every sketch 3/3 (ledger rows 75-79, 102-103): i01, i05, i03,
  i04, i02 (superseded by i05: one-decimal rounding hazard), i06, i07; all "local 3/3: likely Too easy at High".
- Decisions and constraints: the bundle's one quiet relationship is the mid-2025 cash-flow presentation revision
  (9M 2024 in D06, FY 2024 in D08, Q1 2025 in D02, no notes; D03 l.324 notes H1 2024). Solvers find it through the
  FX-forward investing line and the releases' own prose. Inputs sit past character 20,000 in D02, D03, D04, D06,
  D08: expected form-number false alarms (q02 rev 2: seven).
- Candidate families tried: restated cash flow (i01/i06, i02/i05/i07, i03); Ketjen refining exit charges (i04).
  Reserve h3, h4 share the caught revision; other hooks are lookups (hooks.md).
- Changed files since the last checkpoint: questions/q02.md (+ .json), notes/handover-q02.md, sketches/i07.md,
  ideas.md, feedback-index.md, session.md; ../../../notes/hard-runs.md rows 79, 102, 103.
- Revision rounds used / open platform feedback: one repair each (q01 via i06, untested; q02 rev 2) / F1, F2 open.
- Five-candidate trial owner index / candidate row / timed minutes this session: not enrolled; timing partial.
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / i05 / none. Timer 17b31094
  (05:34-10:59 UTC) spans the user's quick-test wait, so it is not active time; a completed timer cannot be discarded.
- Next action and blocker, if any: Checks of 2026-10-19 ran on a mixed form (q01 rev 1 fields + q02 rev 2 reasoning;
  F3). User puts every q02 rev 2 field (notes/handover-q02.md) in one form, keeps one Q2-vs-Q2 question on the bundle,
  re-runs Checks, saves the page and sends the capture before Submit; then record the run (ledger row 103, F2).
  If i06 survived a quick test, write it up as q01 rev 2. Platform results since batch review 3: rows 71, 75, 83;
  review due after two more.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5); blind-solver role pinned to claude-opus-5-5, effort max.
- Optional diagnostic if needed: none
