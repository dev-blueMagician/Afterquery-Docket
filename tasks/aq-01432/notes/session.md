# Current bundle checkpoint

Replace this file at each phase boundary; keep it under 4,000 characters.
It is working memory for resuming the bundle and is never submitted.

- Goal and user constraints: user 2026-10-06 "work on AQ-01432 ... difficulty_target to at least
  medium"; 2026-10-07 "make strongest one like the otheres"; 2026-10-08 "plz check arrived verdicts by
  using your feedback skill and fix", then "based on the verdict, you learned how they solve. plz prepare
  strongest another one". Page: slots Hard 0/2 · Medium 0/3 · Easy 0/1; 9 submissions; difficulty runs
  6 of 8 left (3 of 40 in 24 h, all tasks); quick tests unused.
- Verification target / measured platform tier: medium / none passed. Both runs Too easy, Low 5/5:
  q01 rev 1 (Run 1, e5d715) and q03 rev 0 (Run 2, 6c76af).
- Bundle: aq-01432, 11 plain-text docs, complete. Local id = platform Doc: D01=1, D02=4, D03=2, D04=5,
  D05=3, D06=6, D07=7, D08=10, D09=9, D10=11, D11=8. Map: notes/doc-map.md + part1-4.
- Phase (2026-10-08): HANDED OVER q02 rev 1 (notes/handover-q02.md) as the strongest remaining candidate,
  an Easy-slot candidate only. DECISION PENDING (user): use the Easy slot or stop.
- q01 DROPPED (platform Too easy). q03 DROPPED (platform Too easy; full saved page verdicts/...1307.txt).
- q04 DROPPED 2026-10-08, local only (no platform run). From round-3 i09: UK fake-review services under
  the FTC staff reading; account set-up decoy. Rev 0 review: revise (form quality). Rev 1 checks: two
  matches, clear audit, closed-book miss. The probe without Doc 2 forced the gold by rule-text inference,
  so it fails Q2 (staff's broker answer restates the rule's "sell"); no fair fix.
- q02 rev 1 draft (8372598f...): A/B match (rev 0, rev 1), closed-book misses, audits clear, review ready
  (easy). Rev 1 probes 2026-10-08 (bound packets q04-r0-alt-k8, verified): without Doc 5 not answerable;
  without Doc 2 the decoy 1, 3, 4, 5 unforced (p 0.65). Failure mode added (Linking across documents /
  Misapplies a rule or premise, decoy example 4) and checked (Q15 ready). Odds: Too easy ~60-65%, usable
  Easy ~20-23%, Medium ~3%; Doc 2 doc-check risk ~15-25%; "too vague" ~3-5%. Never pair with i02.
- Sketches: j02, i02 quick-test only; j03/i08 retired; i09 -> q04 (dropped). Three author rounds done:
  no fair Medium design (bundle has no numbers, editions, grouped figures or late members).
- Lessons saved: calibration (q01, q03, Coach check, round 3); removal-probe note (inference-based
  forced reach = FAIL; staff document must decide against the literal rule text); MEMORY index.
- Next action: user decides on the Easy slot. If yes: paste handover-q02.md, run the form's free check,
  then the quick test, then at most one difficulty run; record the result with docket-feedback. A
  retarget of q02 to easy needs a new revision and checks.
- Runtime: Claude Code (VS Code), Opus 5.5; fresh subagents per role; probe runs t5, h8, m2, w4, k8.
