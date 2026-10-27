# Current bundle checkpoint

- Goal and user constraints (2026-10-08): "let's work on AQ-DOCKET-TRIAL-06_2026-10-06_0111. there is no slot
  for Easy Tier for this bundle, we should target medium and high. do you best." An Easy pass is unusable here.
- Verification target / measured platform tier: medium (hard where a design supports it) / pending for both.
- Workflow: v3 (platform validation) since about 17:30 on 2026-10-08: author arithmetic, one preflight,
  full hand-over; local model diagnostics only for a concrete issue; no local tier guesses.
- Bundle: rebuilt 2026-10-08 from template + capture (earlier folder deleted before this session; git HEAD
  30c3f7e). 6 of 6 documents in full, intake/manifest byte-identical to the earlier intake, no capture gaps.
  Source omissions inside originals: D05 footnote texts/figures/App. V, VII; D02 App. III-IV, Figure 1 map.
- q01 rev 1 CHECKED, tested_sha256 ef9968f1ef348fa65cca898ddda45762caf08bfef0bd39275b2dbc971b332c1d
  (snapshot runs/q01-r1-v2-ef9968f1...-platform). Share of privately insured credit unions in the states
  whose bank regulators GAO interviewed about OCC's 2004 rules (CA, GA, NY, NC, ID, IA -> CA 22, ID 20) that
  got at least one 2003 visit: 17/42 = 40.5%. Traps: 21 California sites = 17 credit unions (Table 1
  note b) -> 50.0%; Idaho dropped -> 77.3%. Rev 0 diagnostics (history): A/B match, closed-book misses,
  probes without Doc 2 / Doc 5 miss, audit clear, review revise (format) -> fixed in rev 1.
- q02 rev 0 CHECKED, tested_sha256 41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1
  (snapshot runs/q02-r0-v2-41de64e9...-platform; 2026-10-06 raw returns copied from git beside it).
  Credit unions at end-2002 (9,688 + 214 = 9,902) minus banks Sept 30, 2005 (7,541) = 2,361. Traps: two
  uninsured credit unions only in fn 8 / App. I -> 2,359; federally insured only -> 2,147. Stated risk:
  Doc 5 removal check if the platform model recalls exactly 7,541 banks.
- Rejected: single-state California bridges i01-i01d (no-Doc-5 probes forced the gold at p 0.2-0.4 by
  design intent or recall); authors' sketches (5.36 per national bank; 35 settlement states; 33.3%).
- Hand-overs: notes/handover-q01.md, notes/handover-q02.md (whole form, 0 FAIL, WARN origin only).
- Platform quick tests used: 0 of 10 per the capture (2026-10-06). One practice submission: submit one.
- Next: user quick-tests / runs the platform difficulty check; record platform words under
  `## Platform validation` against the matching fingerprint.
- Runtime: Claude Code, claude-opus-5-5 (max). An API weekly-limit error stopped one reviewer launch
  (resets Oct 10, 6am Asia/Tokyo per the error); the retry completed.
