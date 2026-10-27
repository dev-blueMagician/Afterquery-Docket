# Author A returns (focus: definition, classification and presentation changes) - origin: claude

## Lead 1 - silent fold of amortization into Other expenses (D08 onward)
Draft: By what percentage did State Street's Other expenses in the first half of 2026 differ from the first half of 2024, with amortization of other intangible assets included in both periods? Two decimals.
Gold: -10.38% (1H26 349+402=751; 1H24 (418+60)+(300+60)=838). Inputs: D05 L303-L307 1Q24 Amortization 60, Other 418; D02 L317 / D06 L319 2Q24 amortization 60, Other 300; D10 L281 Other 402 349. Fold proof by reconciliation only (no note anywhere): D07 L270-L271 3Q25 56+317=373 = D08 L270 3Q25; D05 276+54=330 = D09 1Q25; D06 305+56=361 = D10 L281 2Q25.
Necessary: D05 (1Q24 only there) and D10 (2Q26 only there); D02/D06 duplicate 2Q24; D09 duplicates 1Q26.
Decoys: unpinned label route 751/718 = +4.60% (sign flip); ex-notables variant 6.07% vs 27.72% using D05 L108 printed 1Q24 adjusted Other 288.
Fairness: without the amortization pin, +4.60% is a defensible literal reading (both rows are labelled Other); with the pin, the 2026 releases show no amortization row and never state the fold, so a careful solver must infer it from equalities; many will call it missing. The half-year 2024 vs 2026 window is chosen only for necessity (contrived).
Tier: Easy at best; too-vague risk high. Verdict: DROP.

## Lead 2 - passive-alternatives AUM revision vs D01 pre-revision 4Q23 inflows
Draft: What were State Street Global Advisors' total net asset flows, in billions of dollars, over the first half of 2023?
Gold: $12B = 117 - 95 - 10. Inputs: D04 L27 endnote 10 "Net new assets for 2023 and 2024 were $117B and $144B"; D02 L229-L237 5-quarter table, 4Q23(1) 95 and 3Q23(1) 10, note L243 "AUM for passive alternative investments has been revised from prior presentations". D04 is on the revised basis: its 2024 $144B equals the revised quarters -14-6+100+64 (D02/D03/D05).
Necessary: D04 (2023 NNA only there) and D02 (3Q23 only there). 4Q23 95 also in D03 L241.
Decoy: D01 L21 "record total quarterly net inflows in 4Q23 of $103B" gives 117-103-10 = 4. Variant first three quarters 22 vs 14, but then only D04 is unique (4Q23 in D02 and D03).
Weakness: the solver must open D02's table for 3Q23, where revised 4Q23 = 95 sits in the adjacent column under the revision marker, so the D01 decoy is off the natural path. Three lookups and two subtractions: the measured Too easy partial-period shape. Closed-book: SSGA 1Q23/2Q23 flows were public pre-cutoff (original basis), moderate recall risk.
Tier: Too easy 45%, Easy 45%, Medium 10%. Verdict: DROP (keep only as an Easy fallback; no Easy slot).

## Lead 3 - Software services caption over a window containing the never-restated 3Q25
Draft: What was State Street's Software services revenue for the twelve months ended June 30, 2026, in millions of dollars?
Gold: 665 = 3Q25 167 + 4Q25 163 + 1Q26 169 + 2Q26 166. Inputs: D07 L206 / D08 L215 front office software and data 167 (3Q25 never restated); D09 L233 Software services 169 163; D10 L223 166 169 169.
Decoys: 3Q25 taken from the renamed caption (D07 L208 / D08 L217 Software and processing fees 227) gives 725; both 2H25 quarters from D08 L217 (227, 221) give 783. These follow the note clause "the Software and processing fees caption has been changed to Software services" (D09 L245) read without its preceding lending-fee clause.
Necessity FAILS: only D10 is irreplaceable. 3Q25 is in D07 and D08; 4Q25 in D08 and D09; 1Q26 in D09 and D10. D09's note is also replaceable: D10 L94 says 2Q25 Software services of 169 carried the 24M client rescoping, and D06 L105 / D07 L257 put that same 24M in Front office software and data at 169, so the mapping follows without D09. The same reconciliation applies to the caller's i02: its D09 tick is at risk in the platform's Document check; tick D05 + D10 there and probe without D09.
Tier if necessity were fixed: Easy-Medium (the decoy is a misreading of a plainly worded note).
Verdict: DROP.

## Lead 4 - notable-item category regrouping across editions (FY2023, 4Q24, 4Q25)
Draft: From 2023 through 2025, what net repositioning charges did State Street record as notable items, in millions of dollars?
Candidate gold: 527 = FY2023 203 (D01 L23 "net repositioning charges of $(203)M") - 2 (D08 L114/L133 4Q24 "Repositioning charges (net)" +2 = 15 comp release - 13 occupancy) + 100 (2Q25, D06/D07/D10) + 226 (4Q25, D08/D09). D01 and D08 would be the irreplaceable sources.
Decoys: D03 L99 4Q24 combined row "Repositioning charges and other notable items (net)" (10) gives 539; D03 4Q23 combined (233) gives 557; both 569.
Fairness FAILS: the category has no stable definition. D08 itself files 4Q24's 12M operating-model charge under Other notable items (net) (L134) but files 4Q25's 24M + 22M operating-model charges under Repositioning charges (net) (L126); D09/D10 do the same for 1Q26's 9M. Treating 4Q24's 12M like 4Q25's gives 539, the same as the D03 decoy, so 527 and 539 are both defensible. Also 3Q24's investment-portfolio repositioning loss (81) sits in D03's combined row (L112) and in D07's Other notable items, a third reading. Line-item versions (adjusted comp, occupancy, Other) agree across editions, so the regrouping never changes a line-defined answer.
Verdict: DROP (two defensible answers; any fix becomes a rulebook).

## Lead 5 - silent revision of the preliminary year-end 2025 standardized CET1 ratio
Draft: Using State Street's most recent estimate for each date, by how many percentage points did its standardized CET1 ratio change from December 31, 2025 to June 30, 2026?
Gold: -0.8 pp = 10.8 (D10 L316) - 11.6 (D09 L323 4Q25 column; D09 L125/L345 "decreased 1.0% point compared to 4Q25" from 10.6). Necessary: D09 (revised 11.6 only there) and D10 (2Q26 only there).
Decoy: D08 prints 11.7% three times (L140, L305, L324) and "increased 0.8% points compared to 4Q24"; 10.8-11.7 = -0.9. No note anywhere explains the revision; D10 L376 says all capital ratios are estimated.
Fairness: without the "most recent estimate" pin both -0.8 and -0.9 are defensible readings of "the year-end ratio"; the pin spells out the edition check (the measured too-easy signal, trial-03 q01 rev 3), so a low model checks D09's comparative column. A 0.1-point revision with a one-step subtraction leaves little to reason about.
Tier: Too easy 45%, Easy 40%, Medium 12%. Verdict: DROP (record only: the bundle's one silent numeric revision outside the fee reclass; 1Q25 Advanced CET1 12.5 in D05 vs 12.6 in D06 is the same pattern and has no second unique document).

## Lead 6 - fairness fix for the caller's like-for-like FX hook (h2/i05): pin the 2026 definition with a restated number, not by naming the reclassification
Draft (33 words): Using the definition under which State Street's foreign exchange trading services revenue was $393 million in 2Q25, by what percentage did that revenue grow from 4Q25 to 2Q26? Round to the nearest whole percent.
Gold: 41% (494/350 = 1.41143). Inputs: D10 L216/L221 2Q26 494, 2Q25 393 (pin; also L93 "$393 million in 2Q25"); D09 L226/L231 4Q25 restated 350, note L245. Every exact or chained route gives 41: table pcts 1.243 x 1.136 = 41.2%, prose 24% and 14% = 41.4%.
Necessary: D09 (restated 4Q25 only there) and D10 (2Q26 only there). The pin is not an arithmetic input, so it does not replace D10.
Decoy: D08 L213 4Q25 405 (the quarter's own release, old basis): 494/405 = 22%. Answer-shaped, in the natural path; the deciding fact is that D10's 393 differs from D06 L255 / D07 L204 2Q25 431, which only D09's note explains. D08 untick, unquoted. Probe without D09: 405-38 gives 35%, 405x393/431 gives 34%, raw 22%; none is 41.
Fairness: the concrete pin removes the aq-01278 undefined-tie problem; 22% mixes definitions and is excluded by the pin. Risk: the word definition cues a check (aq-01333 q02 was Low 4/5 on a structure pin), and D09 holds note plus restated column together. Unlike there, the pinned document (D10) carries no note.
Sibling (same path, pick one): management fees 772/717 = 8% vs D08 662 decoy 17%, pin "$600 million in 2Q25".
Tier: Too easy 30%, Easy 35%, Medium 28%, High 7%. Verdict: KEEP as improvement of i05 (not a new family).

Addendum to Lead 6 (shortcut search): chaining the printed QoQ columns, D09 L231 24.3% (4Q25 to 1Q26, restated basis) and D10 L221 13.6% (1Q26 to 2Q26), gives 41.2%, i.e. 41%, without ever touching D08. That route needs both ticked documents (good for necessity), but it lets a solver skip the decoy. The trap therefore catches only solvers who fetch the 4Q25 level from the quarter's own release. Revised tier: Too easy 35%, Easy 35%, Medium 25%, High 5%. The same chain works for the management-fee sibling (1.0% then 6.6% = 7.7%).

## Summary (author A)
No fresh Medium family exists in this focus beyond caller hooks h1-h3. ARR recast: recast points only in D10. AUM reorganisation: strategy recast covers 2025 only, and the D09 EMEA/Asia label is a document error. Amortization fold: silent; unpinned it has two readings, pinned it is weak. Notable regroupings: categories flip inside D08. CET1 revision: needs a spelled-out edition pin. Passive-alternatives revision: the D01 decoy is off the path. Kept: Lead 6 (a fix to i05). Lead 2 is an Easy fallback only.
