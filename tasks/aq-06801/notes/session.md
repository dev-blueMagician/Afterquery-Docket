# Current bundle checkpoint

- Goal and user constraints: user (2026-10-18): "no slot for Easy or Medium Tier for this bundle, we should
  target high. do your best." Hard target; sketches first, screened, every fair sketch handed over.
- Verification target / measured platform tier: hard / none passed. User (2026-10-18) on i01-i04: "all too easy".
  q01 rev 0 (i05) Run 1, Oct 18 8:55 PM, Version 75bed4: Low — · Medium — · High 3/3 · Too easy (extra run granted);
  capture verdicts/AQ-06801_difficulty_2026-10-18_2104.txt; feedback-index F1; ledger row 83.
- Prepared run / tested_sha256: q01 rev 0, runs/q01-r0-v2-59a088bb...-platform, tested_sha256 59a088bb2fbff1bdcbe6b8998f5344f69228d4707227531d69a89e32e6e1ebdc
- Bundle slug / documents (ids) / extraction warnings: aq-06801, 7 docs complete (capture AQ-06801_2026-10-18_1547.txt);
  D01=Doc 6, D02=Doc 7, D03=Doc 5, D04=Doc 4, D05=Doc 1, D06=Doc 3, D07=Doc 2. D02 segment table shifts prior-year cells.
- Phase: q01 measured Too easy at High (2026-10-18); redesign or release, user's choice.
- Questions: q01 checked rev 0; floor 0 FAIL / 5 WARN (strong-screen, origin, units, two expected Doc 5 form-number false alarms); Checks not captured.
- Screen results (blind-solver claude-opus-5-5 max): i01-i05 all 3/3 right (15 of 15); ledger rows 56-59, 83.
- Mechanisms tried: derived fiscal Q4 + FY rebuild + look-alike line (i01); derived Q2 as selector (i02); footnote
  rule on unreported half-years (i03); trailing window + 10-Q prose input (i04); value printed nowhere recovered by a
  10-Q-only rule, with a mislabeled look-alike line (i05). Solvers read releases fully, search the 10-Q, derive
  every missing period, find every reconciling identity and name each lure.
- Bundle limits: no restated figures; no definition change with a numeric effect (Iridium OEBITDA relabel has none
  in 2025; net-debt wording follows a nil revolver); no 2025/2026 like-for-like base outside one document.
- Reserve: h15 (APIC overlap 111.1, lure 115.0) unscreened; its post-October allocation is inferred, not stated.
- Decisions and constraints: i01/i04/i05 cite figures past character 20,000 (expected form false alarms).
  i05's wording changed once before screening ("embedded derivative liability attached to" -> "derivative liability
  that Comtech split out of") after the screen flagged "embedded" as leading to the settling passage.
- Changed files: sketches/i05.md (new, screened), hooks.md (h14, h15), ideas.md, ../../../notes/hard-runs.md.
- Five-candidate trial / timing: not enrolled; unmeasured (peer held the single timer) -> coverage partial.
- Next action and blocker, if any: user decides: release the bundle, or screen reserve h15 (APIC overlap) as a new stack.
  q01 stays at status checked with its fail record; no rewording (Too easy at High replaces the stack).
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5); blind-solver role pinned to claude-opus-5-5, effort max.
- Optional diagnostic if needed: none
