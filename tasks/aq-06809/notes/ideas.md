# aq-06809 - lean candidate sketches

Current target: hard (user, 2026-10-18: "there is no slot for Easy or Medium Tier for this bundle, we should target
high"); measured platform success pending. Origin of every sketch: claude. Hooks in notes/hooks.md; design by
the playbook (section 4); each sketch's lever stack, checks and arithmetic live in notes/sketches/iNN.md.
Local ids vs task-page Doc numbers: D01 = Doc 1, D02 = Doc 2, D03 = Doc 4, D04 = Doc 5, D05 = Doc 3.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h1: Q2 2026 YoY operating leverage excluding only itemized M&A charges, Huntington (7.78) minus KeyCorp (1.28) = 6.5 | lures 6.2 (Table 10's Q2 2025 1,194), -6.2 (reported), 2.2 ($58M loss removed), 10.1 (amortization also removed; ruled out by "charges each bank itemizes"), 6.6/6.7 (GAAP revenue); needs D03 (152 and the Q2 2025 item types) and D05 | screened 3/3 (run e0b52ba8; ledger row 66); quick test too easy (user, 10-18: "all too easy"); closed |
| i02 | [i02](sketches/i02.md) | h2: rank by Q2 2026 consumer-loan NCO rate: KeyCorp 0.28 (rebuilt), Huntington 0.30, Fifth Third 0.53 | lures H, F, K (KeyCorp Consumer Bank segment 0.54%, or totals) and H, K, F (gross charge-offs, 0.36%); each bank's documents place one position; KeyCorp margin holds under input rounding | screened 3/3 (run 7bd70f84; ledger row 67); quick test too easy (user, 10-18: "all too easy"); closed |
| i03 | [i03](sketches/i03.md) | h3: Q2 2026 efficiency ratio excluding only itemized M&A charges, Fifth Third (58.13) minus Huntington (58.00) = 13 bps | lures -90 (Fifth Third's 57.1% adjusted), -33 (all certain items), -19 (GAAP revenue), 198/280 (Huntington's own definition), 10 (rounded first); sibling of i01 (same clause and Huntington input): write up at most one | screened 3/3 (run a5f19dc6; ledger row 68); quick test too easy (user, 10-18: "all too easy"); closed |
| i04 | [i04](sketches/i04.md) | h4: rank by Q2 2026 total cost of deposits: Fifth Third 1.54 (D02 slide / D01 computed), KeyCorp 1.63, Huntington 1.88 (D04) | decoy K, F, H (interest-bearing costs, or releases only); K, H, F (Fifth Third interest-bearing only); each bank's documents place one position; two solvers raised "total cost" as dollar interest (K, F, H), weak since every source prints a rate | screened 3/3 (run 4bc5700d; ledger row 69); quick test too easy (user, 10-18: "all too easy"); closed |
| i05 | [i05](sketches/i05.md) | h9: Q2 2026 noninterest-bearing share of average total deposits, Fifth Third (63,976 / 231,506 = 27.63%) minus KeyCorp (27,566 / 147,577 = 18.68%) = 9.0 | decoy 9.3 (Fifth Third's printed 28.0% is over core deposits; its pie rounds the total share to 28%); -13.7 (KeyCorp's interest-bearing "demand deposits" taken as noninterest-bearing); 7.1 (period-end); D01 or D02 plus D05 | round 3; screened 3/3 (run b17fcfaa; ledger row 80); wording defect (8.9 if the shares are rounded first; the gold sits 0.006 above 8.95): superseded by i07, not offered |
| i06 | [i06](sketches/i06.md) | h10: difference between the Q2 2026 CET1-ratio declines, KeyCorp (-23.76 bps) and Huntington (-18.12 bps), from capital over risk-weighted assets = 6 bps | decoy 0 (printed ratios fall 20 bps each); 4 (AOCI-inclusive Marked/Adjusted CET1); D04 and D05 | round 3; screened 3/3 (run 2cfcfa49; ledger row 81); quick test survived (user, 10-18: "i06 survived"); promoted to q01 rev 0 |
| i07 | [i07](sketches/i07.md) | h9 repaired: i05 plus "without rounding the two shares first"; gold 9.0 | as i05; 8.9 now fails the wording | round 3; screened 3/3 (run e1cf2669; ledger row 82); quick test too easy (user, 10-18: "i07 too easy"); closed |
| i08 | [i08](sketches/i08.md) | h10 repaired after q01 rev 0's form block ("One defensible answer" Failed: both form solvers answered 0 from the printed ratios): i06's sentence plus "with each ratio calculated from the bank's reported CET1 capital and risk-weighted assets"; gold 6 | the printed-ratio trap is now ruled out by the wording; remaining lures 4 (Marked / Adjusted CET1 capital), 5 (D03's RWA in $ billions); expected to cost most of the difficulty | screened 3/3 (run f7055124); quick test too easy (user, 10-18: "too easy"); hook h10 retired, q01 dropped |
| i09 | [i09](sketches/i09.md) | h11, round 4 (user, 10-19: "go on A"): narrowest quarterly gap in 2025 between Fifth Third's and Huntington's efficiency ratios (NIE over FTE revenue); the narrowest is Q1, which neither bank prints (six months less Q2: 61.05 vs 59.53); gold 1.5 | lures 3.0 (Q2-Q4 only), 2.1 (Huntington's own definition), 2.5 (printed ratios); D01 and D04 hold the six-month columns | screened 3/3 (run 198dab87); quick test survived (user, 10-19: "i09 survived, i10 failed"); promoted word for word to q02 rev 0; Run 1 Too easy at High (High 3/3, Version a02029); q02 dropped |
| i10 | [i10](sketches/i10.md) | h11, round 4, sibling of i09: each bank's highest 2025 quarterly ratio, Fifth Third's (Q1, unprinted, 61.05) below Huntington's (Q4, 64.81 on the stated basis, printed 64.2 on its own); gold 3.8 | lures 8.6 (Fifth Third's printed Q2 56.2), 3.2 (Huntington's own definition), 8.0 (both printed); D01 and D04 | screened 3/3 (run 7745e9fb); quick test failed (user, 10-19: "i10 failed"); closed |

Rejected or held hooks: h5 (Huntington organic loan growth: one rebuild), h6 (Q1 2025 growth: one lever),
h7 (the $111M / $21M conflict), h8 (single-document guidance), and a calendar-2025 FTE NII gap (Huntington 6,056
minus Fifth Third 6,000 = 56: skipping the derived Q1 2025 gives 57, one unit from the gold). Reasons in notes/hooks.md.
Round 2 (2026-10-18) added i03 and i04 after i01 and i02 screened 3/3 (playbook section 6: "design a new stack next");
the task page tests up to five ideas at once. Round 3 (2026-10-18), after the user's "all too easy" on i01-i04: the trap
moves from spelled-out computations to which printed figure to trust (a look-alike share; one-decimal ratios), i05 and i06.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
Allow one focused repair per distinct observed failure; a repeated failure means change the hook.
