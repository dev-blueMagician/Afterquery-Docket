# Current bundle checkpoint

- Goal and user constraints: user 2026-10-06: "set target difficulty as at least Medium ... start work from the scratch again on Trial 7 ... only one attempt, once after reach result, you need to check carefully again". Rebuilt from scratch.
- Verification target / measured platform tier: medium (High also satisfies) / pending; no platform access here.
- Current candidate: q01 rev 1, status draft (kept below checked because both reviews rate difficulty below the medium target). Run q01-r1-v2-4a4bfbeb...ac22, tested_sha256 4a4bfbeb920197262965674b8c510f44dc34182ae7098a90425a9d5b05acac22; source_gaps_sha256 12d3693f...c3c5.
- q01 rev 1 records: blind A match, B match (high); closed-book misses (+7.4%, -5.6%); audit clear; second review ready (difficulty easy: too easy 45%, Easy 40%, Medium 10%, High 3%, too hard 2%); source assessment unaffected (all seven gap labels, six dimensions). Rev 0 (0f1cbdad...f148): same outcomes; review revise only for the cross-line quote and decoy quotes (fixed in rev 1); removal probes: without D05 +6.0%/-8.2%, without D04 +10.4%/-5.5% (both needed).
- Floor: 0 FAIL, 1 WARN (origin claude; export takes user only; form asks "I wrote this question myself").
- Bundle: D01=Doc 3, D02=Doc 2, D03=Doc 1, D04=Doc 5, D05=Doc 4, D06=Doc 6, D07=Doc 7. Gaps: pre-date header + 34-char tail per doc (located by markers).
- Round 1 finding: no fair Medium mechanism (author B: 25 non-time-series links, none viable; author A: time-series best Easy; both reviews agree). i06 (prose-conflict decoy) screened: matched but the solver listed the prose route as a reading (two-answer risk). i02 screened: match 53.9%, closed-book ~51% (miss).
- Hand-over: notes/quicktest-round1.md (S1 q01 rev 1; S2 i02; S3 i06 flagged; S4 i04 optional). Form placement: D05 quotes -> Doc 4, D04 quotes -> Doc 5.
- Rounds used: 1 sketch round; q01 revised once (evidence).
- Next action: user decision. Quick-test the batch; if q01 survives, it can go to the difficulty check; if "Too easy", Medium is not fairly reachable here (accept Easy with q01, or try round 2 / i06 with its risk). If Easy accepted, bump q01 to difficulty_target easy (new fingerprint, fresh checks) before export.
- Runtime: Claude Code, Opus 5.5 max; fresh isolated subagents.
