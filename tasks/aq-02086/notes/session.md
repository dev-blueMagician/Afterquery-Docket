# Current bundle checkpoint

- Goal and user constraints: AQ-02086 (capture AQ-02086_2026-10-08_1226.txt). User 2026-10-08: "there is
  no slot for Easy Tier for this bundle, we should target medium and high. do your best." Page: Hard 0/2 ·
  Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests, 8 of 8 difficulty runs.
- Verification target / measured platform tier: medium (hard where supported) / pending.
- Prepared runs: q01 r0 6ba84dab (dropped); q02 r0 8cb0c5f5 (blocked), r1 43468c16 (dropped); q03 r0 28a06f79; q04 r0 ac7582aa.
- Bundle: 5 UK housing-policy documents, complete (intake.json). D01=Doc 4, D02=Doc 1, D03=Doc 2,
  D04=Doc 3, D05=Doc 5. No extraction warnings.
- Phase: stopped after round 3 (WORKFLOW section 6). q01-q04 all dropped: quick tests "too easy" (F1, F3, F4, F5);
  q02 rev 0 was form-blocked (F2). Quick tests used: 4 of 10 (q02 rev 0 stopped at the free form check).
- Questions: q05 checked rev 0 (48cea5c5...7479): relative shrink of the private-minus-social non-decency gap
  2010-2020 (Doc 4 + Doc 1) = 53.5%; decoys 10% (2021/2023) -> 36.0%, 39% (2001). q01-q04 dropped.
- Decisions: numeric first (user preference); i02 BRE per-home cost parked (repeating decimal vs the
  form's exact-result check); h2 projection rejected (two readings); h3 universe fixed by "annexed".
- Candidate families / shortcut routes / completeness: see notes/hooks.md; full corpus.
- Changed files: notes/doc-map.md, hooks.md, ideas.md, sketches/i01-i02, questions/q01-q02 (+json),
  notes/handover-q01.md, handover-q02.md, runs/q01-r0..., runs/q02-r0....
- Revision rounds used / open platform feedback: 3 rounds / none open (F1-F5 historical).
- Active feedback index: notes/feedback-index.md (F1-F5).
- Five-candidate trial: not enrolled (trial already holds 5 of 5 candidates); no timer run.
- Efficiency ledger / candidate ID / active timer ID: ../../../notes/efficiency.json / none / none.
- Next action: user runs the free form check and a quick test on q05; a difficulty run only if it survives.
- Runtime/model/effort: Claude Opus 5.5 (claude-opus-5-5), max effort, VS Code extension.
- Optional diagnostic: none requested.
