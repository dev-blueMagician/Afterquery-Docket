# Current bundle checkpoint

- Goal and user constraints (2026-10-06): restart Trial 6 from scratch; target at least Medium tier;
  one submission attempt; after reaching a result, re-check it carefully before hand-over (done).
- Verification target / measured platform tier: medium / pending (no platform access here).
- Bundle: capture AQ-DOCKET-TRIAL-06_2026-10-06_0111.md (6 of 6 in full, no gap markers, hashes
  match; quick tests used 0 of 10 per capture). D01-D06 = platform Doc 1-6. Six unrelated GAO
  products 2001-2007. prepare reports no source_gaps.
- Notes: doc-map.md (merged, full coverage), hooks.md, ideas.md (i01-i03, i06-i08), handover-q01.md
  (labelled form fields, verified identical to the checked revision).
- PRIMARY: q01 CHECKED rev 0, tested_sha256 41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1.
  "How many more credit unions did the United States have at the end of 2002 than it had banks on
  September 30, 2005?" Gold "2,361 more credit unions" (9,688 + 214 = 9,902; 1,846 + 5,695 = 7,541).
  Docs 2 and 5. Trap inside Doc 2: 9,688 (overview figure) or 9,900 (98% + 2% sentences) instead of
  9,902 (two uninsured credit unions in fn 8 and App I 1179). A/B match, closed-book 2,148, audit
  ambiguous then clear (replacement), removal probes need both docs, review ready, SECOND CHECK
  ready with no blocking issues. Tier estimate: Easy ~45%, Medium ~40%, High ~10%.
  Risks: Easy; reviewer may call 2002-vs-2005 contrived; Doc 5 recall (7,541) 10-20%.
- q02 DROPPED rev 0 (Idaho share 9.8%): 9.4% defensible because Doc 2 uses "lacking federal deposit
  insurance" for privately insured credit unions; no-D05 probe hit the gold (Indiana 21/214 = Idaho).
- ROUND 2 (user, 2026-10-06: "make QA like Trial 2's q01 or Trial 6's q02"):
  q03 CHECKED rev 0 (f9e852afbaf20d2cb7a2c3fe6bcf7b4c60fa144a8c5e23aca81e3efe630f4ddf): q01's hook as
  a two-decimal percentage, 31.31% (decoy 31.28%). A/B match, closed-book 28.49%, both audits clear
  of shortcuts but both answered 31.28% (never read D02 1179), review ready, medium (marginal); same
  odds as q01; reviewer still prefers q01. handover-q03.md verified. Never submit with q01.
  q04 DRAFT rev 0 (ff615a1b...): Idaho Web-site share 25.0%; correct and fair but predicted Too easy
  or Easy (base wording defuses the printed-71 trap); retired for this attempt.
  Dropped: i14 (term collision), i09 (GAO sampling, 57 wording), i11 (two lookups).
- Revision rounds used: 0. Platform quick tests used: 0 of 10 (as of the capture).
- Hand-over advice: quick-test q01 (question + "2,361"); if it survives, enter handover-q01.md fields,
  run the difficulty check, submit only on "In band - Medium tier" or higher; paste platform output
  back for recording against this fingerprint. Origin claude: "I wrote this question myself" is the
  user's call.
- Runtime: Claude Code, claude-opus-5-5 (max); blind-solver/shortcut-auditor under the scope hook;
  closed-book (no tools); question-review (two independent reviewers).
