# aq-05023 - cross-document hooks

Target: hard (user, 2026-10-14: "there is no slot for Easy or Medium Tier for this bundle, we should target
high"; page 14:32: "Easy or Hard only", "Hard 0/5 · Medium closed · Easy 0/0"). The check will start at the
High level (two solvers, up to 3 attempts each; both must miss at least once, not every attempt wrong).
Audit rule (memory, 2026-10-14): count as unpointed only a step the question needs but no word, figure,
date or name in it reaches by lookup or by a sweep of one named property; only an inference can hold the
high model. Local ids D01-D08; page Doc numbers in doc-map.md.

Arithmetic checks (scratchpad scripts auth.py, deficit.py, 2026-10-14): every monthly drop in remaining
buyback authorization equals shares x average price within $5K (rounded prices); the accumulated deficit
moves by exactly the quarter's net income in all six quarters with an equity statement or printed income.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | 9M 2025 buybacks $63,944K (D08 l.455; D07 l.69 "$63.9 million"); remaining authorization $195,869K after Sept 2025 (D08 l.925) and $173,831K after Jan 2026 with no Jan purchases (D02 l.746); $250.0M program announced Feb 27, 2025 (D04 l.431, D02 l.413) | FY2025 buyback spending $85,982K: no document prints Q4 2025 or FY2025 buybacks | Calculate across documents; Part vs total | 9M only $63.9M; program-to-date 250,000 - 173,831 = $76,169K (misses about $9.8M bought before the Feb 27, 2025 program: Q1 2025 total $21,538K vs $11,726K of program use implied by D04's April row) | Necessity is by groups: 2025 side D04 or D08 (H1 $44,644K + Jun 30 remaining $215,168K also gives it); 2026 side D02 or D06 exact, D01/D05 approximate | lead family; unpointed: Q4 derivation (inference) and avoiding the program shortcut |
| h2 | Accumulated deficit (948,892) at Sept 30, 2025 (D07 l.181, D08 l.135) and (941,494) at Dec 31, 2025 (D01 l.205, D02 l.130, D05 l.203, D06 l.130); (961,546) at Dec 31, 2024 (D03-D04-D07-D08); 9M 2025 net income $12,654K (D07, D08) | Q4 2025 net income $7,398K; FY2025 $20,052K; no document prints either | Calculate across documents | 9M $12,654K taken for the year; "not reported" | Relies on the identity that only net income moves the deficit, shown in every equity statement in the bundle but not for Q4 2025 itself | lead family; unpointed: retained-earnings roll-forward (inference) |
| h3 | h1 + h2 | FY2025 buyback spending minus FY2025 net income = $65,930K (nearest million: 66 on every buyback basis: aggregate price 85,982, cash-flow 9M 64,339 + Q4 = 86,377, equity statement 64,453 + Q4 = 86,491) | Calculate across documents | 9M both 51; program shortcut 56; buybacks right, 9M NI 73; 9M buybacks, FY NI 44 | Two inferences in different passages (monthly tables in 10-Qs; balance sheets); delete-and-guess per group | sketch i01 |
| h4 | Remaining authorization Jun 30, 2025 $215,168K (D04 l.815) and Jun 30, 2026 $116,578K (D06 l.809; D05 l.81 "approximately $116.6 million"); deficit Jun 30, 2025 (956,550) (D03, D04) and Jun 30, 2026 (922,253) (D05, D06) | TTM to Jun 30, 2026: buybacks $98,590K; net income $34,297K | Calculate across documents | Q3 2025 + H1 2026 without Q4; 250 - 116.6 = 133.4 since program start | No pre-program trap (window inside the program); one subtraction across two editions each | reserve; weaker than h3 |
| h5 | Q1 2025 G&A original 25,884 (H1 47,566 - Q2 21,682, D03/D04) vs recast 20,885 (D01 l.151, D02 l.157); Q3 2025 G&A 24,325 (D07, D08) only on the 2025 basis | Q1->Q3 2025 G&A change is -1,559 on one basis, +3,440 if the recast Q1 is mixed in | Same series, right edition | Mixed-basis +3,440 | Fair only if the question names the basis, which points at the trap (scope phrase invites the check) | dropped for High |
| h6 | Q2 2026 guidance flat to +2% and 28.0-29.0% (D01 l.92-95); Q3 2026 guidance (D05 l.90-93) with Q3 2025 revenue 181,573 (D07, D08) | Dollar ranges implied by guidance | Calculate across documents | Margin applied to the wrong quarter's revenue | Every step named by the question; Q3 2026 top of range (54,635) is within $4K of Q3 2025 Adj. EBITDA (54,631): too fragile to use | dropped |
| h7 | Q4 2025 visits 138.8M and UVs 21.7M only in D01 l.47-48; 9M 2025 traffic 488,343K (D08 l.647) | FY2025 visits 627.1M | Calculate across documents | Sum of three quarters | A sweep of the named metric finds the Dec 31, 2025 column (cleared kind) | dropped |
| h8 | D06 MD&A l.734 "As of March 31, 2026 ... Total Net Leverage Ratio ... 1.95x" vs D02 1.84x and D06 Note 5 June 30, 2026 1.95x | Leverage change in Q2 2026 | Reconcile documents that disagree | 0 from the misdated sentence | Gold would rest on judging a document error | rejected |
| h9 | RIF expense recorded in Q1 2026 (D02 Note 12) vs "cost reduction program undertaken in April" (D01 l.95; D05 l.65) | Quarter of the workforce reduction | Temporal alignment | April -> Q2 | Not numeric; "recorded" points at Note 12 | dropped |
| h10 | FY2026 buyback target "$60-plus million" before April 9, 2026 (D01 l.81) | Target in force at a date | Same series, right edition | $90M | Imprecise prior target; single document | dropped |
| h11 | D2C earnout CAD$15.0M paid April 2025 (D04, D08) and April 2026 (D02, D06) | Earnout cash | Calculate across documents | n/a | Trivial sums of printed figures | dropped |
| h12 | Revolver $60.0M (D04) -> $50.0M (D06) | Principal repaid | Calculate across documents | H1 2026 payment only | Two printed endpoints | dropped |

Independent author hooks (2026-10-14, origin claude, reports checked and recomputed by the caller):

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h13 | Nine-month 2025 G&A 71,890 and Q3 24,325 (D07 l.127, D08 l.162); H1 2025 47,566 and Q2 21,682 (D03 l.134, D04 l.162); re-presented Q1 2025 20,885 (D01 l.151, D02 l.157; D01 reconciliation "As Reported (1)", footnote l.313) | Q1 2025's share of the reported nine-month G&A = 25,884 / 71,890 = 36.0% (h5 reframed as part of a printed total, so the basis is fixed by the denominator) | Same series, right edition | 29.1% (re-presented Q1); 37.6% (re-presented Q2 mixed in) | "One defensible answer" risk if both form solvers take 29.1% | both authors' rank 1; sketch i02 |
| h14 | h1 inputs plus H1 2026 aggregate purchase price 57,253 (D06 l.427) and $116.6M remaining (D05 l.81, D06 l.422) | Buybacks Jan 1, 2025 - Jun 30, 2026 = 143,235 | Calculate across documents; Part vs total | 133 (250.0 - 116.6), 121 (Q4 omitted), 144 (cash-flow/equity basis) | Window start may point at the program start | reserve r1 |
| h15 | h2 inputs | Q4 2025 net income 7,398 | Calculate across documents | equity change, comprehensive income, FY figure | No printed decoy; recall if 2026 filings are real | reserve r2 |

Also found by the authors and rejected: D05's H1 2026 adjusted opex table repeats Q2's stock-based
compensation column (prints 299,032; Q1 145,921 + Q2 144,296 = 290,217), a document error unfit for a gold;
the D06 l.734 leverage misdating (h8).

The map is navigation; quotes come from the extracted sources.
