# Current bundle checkpoint

- Goal and user constraints: user 2026-10-08: "let's work on AQ-01540_2026-10-07_1253. there is no slot for Easy Tier for this bundle, we should target medium and high. do you best." Capture 2026-10-07 12:53: "Still open on this set: Medium."; "Easy and Hard questions are full on this set"; slots "Hard 1/2 · Medium 1/3 · Easy 2/1", "In review: Hard 1", 4 submissions left, quick tests 0 of 10.
- Verification target / measured platform tier: medium (a Hard result is not submittable while Hard is full) / pending.
- Runs: q01 rev 0 6f8f40e3...; q02 rev 0 84a33fdc... (superseded); q02 rev 1 0a6b22bd...; probe runs q01-r0-alt-n5 (rev 0 probes, done) and q02-r0-alt-c9 (rebuilt for q02 rev 1: solver-1 without D08, solver-2 without D04); maps runs/probe-plan.json, runs/probe-plan-q02r1.json.
- Bundle: aq-01540, eight unrelated federal opinions (Sept 11-15, 2026). Ids vs page: D01 = Doc 6, D02 = Doc 8, D03 = Doc 7, D04 = Doc 5, D05 = Doc 2, D06 = Doc 4, D07 = Doc 1, D08 = Doc 3. Complete capture, no gaps; doc-map full read plus caller's own full read.
- Phase: checking (2026-10-08).
- q01 rev 0 (Vidino and Lewis Machining; D02 + D05): closed-book miss; A and B match (medium); audit clear; both probes miss; all flag a weaker "contested dismissal only" reading (Vidino alone). Independent review running.
- q02 rev 1 (Royal Caribbean and Steven Johnson with his law firm; D04 + D08): rev 0 had A/B matches, clear audit, closed-book miss and both probes missing, but every solver noted a narrow reading (only the September rulings' own relief: Royal Caribbean alone) and probes read "Give them in any order" as a plurality hint; rev 1 says "ever got" and "If more than one qualifies, list them in any order." Rev 1 checks running (A, B, audit, closed-book, two probes).
- Independent question-author round: running.
- Decisions: no fair cross-document numeric hook; doctrinal filters with keyword-printed holdings rejected; designs rest on non-salient list members. Local Opus found every buried item easily, so difficulty is unmeasured; the form's "too vague" check may block if both form solvers omit the same item.
- Revision rounds used: q02 one. Open platform feedback: none.
- Next action: record q02 rev 1 returns; reviews; hand over whole forms (check_questions --handover) for the free form check and quick tests.
- Runtime/model/effort and independent-context method: Claude Code, Opus 5.5 max; blind roles via agents with omitClaudeMd and the read guard; probes on renumbered packets with neutral names.
