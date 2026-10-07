# q05 rev 0 raw returns (tested_sha256 5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72)

Fresh role agents dispatched 2026-10-06 by the caller session with only the workspace root, their own
packet path and the exact question (closed-book: question only). Returns are pasted unabridged.

## Closed-book solver (question only), completed 2026-10-06

answer: unknown
confidence: low
basis: Chevron calculates full-year ROCE as net income attributable to Chevron, plus after-tax interest and debt expense, plus noncontrolling-interest income, divided by average capital employed. Capital employed is total debt plus Chevron stockholders' equity plus noncontrolling interests, averaged from the start and end of the period. For the twelve months ended June 30, 2026, that needs earnings from Q3 2025 through Q2 2026 and the balance sheets at June 30, 2025 and June 30, 2026. Q2 2026 results came out around late July 2026, after my knowledge cutoff. I also don't reliably remember Chevron's first-half 2026 earnings. A rough estimate puts it somewhere around 7–10%, which is too uncertain to give to one decimal place.
contaminated: no

## Solver A (blind-solver, packet solver-1), completed 2026-10-06

answer: 10.9%

confidence: high

path:
1. **How Chevron calculates full-year ROCE (D10, FY2025 table, lines 394–412).** ROCE earnings are "Total reported earnings" plus "Noncontrolling interest" plus "Interest expense (A/T)". For a full year, "Annualized ROCE earnings" equal actual earnings: 13,581 | 13,581. Footnote (1): "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period." FY2025: ROCE earnings 13,581, average capital employed 205,316, ROCE 6.6%.
2. **The full-year average uses only two balance sheet dates.**
   - D10 lines 370–373 give capital employed at Dec 31, 2024 as 24,541 + 152,318 + 839 = 177,698, and at Dec 31, 2025 as 40,758 + 186,450 + 5,726 = 232,934.
   - (177,698 + 232,934) / 2 = 205,316, which matches the printed figure exactly.
   - FY2024 checks out the same way. D05 lines 358–360 give Dec 31, 2023 as 20,836 + 160,957 + 972 = 182,765. (182,765 + 177,698) / 2 = 180,231.5, printed as 180,232.
   - An average of five quarter-end values for 2025 would be about 200,852, which does not match.
3. **ROCE earnings for the twelve months.** This is FY2025 minus H1 2025 plus H1 2026.
   - FY2025 (D10 line 405): 13,581.
   - H1 2025 (D08 line 387, repeated in D12 line 389): 6,469.
   - H1 2026 (D12 line 389): 15,135.
   - 13,581 − 6,469 + 15,135 = **22,247**.
   - Cross-check by quarter: Q3'25 is 3,942 (D09 line 372), Q4'25 is 3,170 (D10), Q1'26 is 2,603 (D11 line 379) and Q2'26 is 12,532 (D12). They also sum to 22,247.
   - Cross-check by component: net income 20,591 + noncontrolling interest 374 + after-tax interest 1,282 = 22,247.
4. **Capital employed at the start and end of the period.**
   - June 30, 2025 (D08 lines 358–360): "Total debt $ 29,467", equity "$ 146,417", "Noncontrolling interests $ 841". Total 176,725.
   - June 30, 2026 (D12 lines 352–354): "Total debt $ 37,075", equity "$ 189,883", "Noncontrolling interests $ 5,675". Total 232,633.
   - These balances reproduce every printed period average, so the inputs are consistent. Sep 30, 2025 = 237,144 (D09) and Mar 31, 2026 = 234,799 (D11).
     - Q2'26: (234,799 + 232,633) / 2 = 233,716, printed 233,716.
     - H1'26: (232,934 + 232,633) / 2 = 232,783.5, printed 232,784.
     - H1'25: (177,698 + 176,725) / 2 = 177,211.5, printed 177,212.
5. **Result.** Average capital employed = (176,725 + 232,633) / 2 = **204,679**. ROCE = 22,247 / 204,679 = 10.869%, which rounds to **10.9%**. The answer would only round differently if the true value were below 10.85%, which needs about 38 less in earnings or about 360 more in capital. That margin is well beyond any rounding in the inputs.

minimal_documents: D08, D10, D12, which give every input directly.
- Alternative: D10 + D12 alone. Back out June 30, 2025 capital employed from D12's H1 2025 average (177,212) and D10's Dec 31, 2024 balance: 2 × 177,212 − 177,698 = 176,726. That gives 22,247 / 204,679.5 = 10.9%.
- D09 can stand in for D08 the same way: 2 × 206,935 − 237,144 = 176,726.
- D10 cannot be replaced. It is the only source for Q4 2025 / FY2025 ROCE earnings.

readings:
- **Main reading (two-point average, same as Chevron's full-year method): 10.9%.**
- Average of the five quarter-end capital employed values (1,114,235 / 5 = 222,847): 22,247 / 222,847 = 10.0%. This is not Chevron's stated method.
- Mean of the four quarterly average capital employed figures (227,389): 9.8%. Also not the stated method.
- Leaving noncontrolling interest out of capital employed (debt plus equity only, average 201,421): 11.0%. This contradicts Chevron's definition.
- Printed YTD 2026 annualized ROCE (13.0%) and Q2 2026 annualized ROCE (21.4%) cover different periods, so neither answers the twelve-month question.

gaps:
- The documents contain no twelve-month ROCE figure, so the answer is computed rather than quoted.
- Coverage of what I read:
  - D12: read in full.
  - D08, D09, D10, D11: read only their Attachment 2 sections, plus the D08 and D10 income statements.
  - D01–D07: only the lines that matched my searches.
  - docs/ originals: not opened. Extraction looks reliable because all printed averages and ROCE values reconcile.
- No later restatement of the June 30, 2025 balance sheet appears in the packet.

contaminated: no

Key files:
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\solver-1\text\D08.txt
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\solver-1\text\D10.txt
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\solver-1\text\D12.txt

## Solver B (blind-solver, packet solver-2), completed 2026-10-06

answer: **10.9%**

confidence: high

path:
1. **How Chevron calculates full-year ROCE.** The footnote, which is the same in every release (for example D10 line 412 and D12 line 396), says: "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period." ROCE earnings are "Total reported earnings" plus "Noncontrolling interest" plus "Interest expense (A/T)". For a full year the earnings are not annualized. D10 (lines 402–410) shows FY2025 ROCE earnings of 13,581, "Annualized ROCE earnings" of 13,581, average capital employed of 205,316 and ROCE of 6.6%.
   - Check that the full-year average uses only two points (D10 lines 370–372): Dec 31, 2025 is 40,758 + 186,450 + 5,726 = 232,934. Dec 31, 2024 is 24,541 + 152,318 + 839 = 177,698. (232,934 + 177,698) / 2 = 205,316, which matches the printed figure exactly.
   - The same two-point average reproduces every quarterly, 6M and 9M average in D08–D12 to within ±1 from rounding.

2. **ROCE earnings for the twelve months July 2025 to June 2026 ($ millions).**
   - From the period tables: FY2025 13,581 (D10 line 405), plus 6M 2026 15,135 (D12 line 389), minus 6M 2025 6,469 (D12 line 389; D08 line 387) = **22,247**.
   - Check by quarters: Q3'25 3,942 (D09 line 372) + Q4'25 3,170 (D10) + Q1'26 2,603 (D11 line 379) + Q2'26 12,532 (D12) = 22,247.
   - Check by component: earnings 12,299 + 14,282 − 5,990 = 20,591; noncontrolling interest 186 + 225 − 37 = 374; after-tax interest 1,096 + 628 − 442 = 1,282. Total 22,247.

3. **Capital employed at the start and end of the period.**
   - June 30, 2025 (D08 lines 358–360): "Total debt $29,467", "Total Chevron Corporation stockholders' equity $146,417", "Noncontrolling interests $841". Total 176,725.
   - June 30, 2026 (D12 lines 352–354): "Total debt $37,075", equity "$189,883", "Noncontrolling interests $5,675". Total 232,633.
   - Average: (176,725 + 232,633) / 2 = **204,679**.

4. **ROCE:** 22,247 / 204,679 = 10.869%, which rounds to **10.9%**.

minimal_documents: D08, D10 and D12. D10 and D12 alone also work. The June 30, 2025 figure can be backed out of D12's 6M 2025 average (177,212 × 2 − 177,698 = 176,726, one off from rounding). That gives an average of 204,679.5 and still 10.87%, so 10.9%. Another route is D09's Q3 average (206,935 × 2 − 237,144 = 176,726).

readings:
- **Main reading (Chevron's stated method): 10.9%.**
- Five quarter-end average of capital employed (176,725; 237,144; 232,934; 234,799; 232,633), giving 222,847: 22,247 / 222,847 = **10.0%**. This contradicts Chevron's footnote, so it is less defensible. The gap is large because the Hess acquisition was not yet in the June 2025 starting figure.
- Mean of the four quarterly average capital employed figures (206,935; 235,039; 233,867; 233,716), giving 227,389: **9.8%**. Not Chevron's method.
- Simple mean of the four quarterly ROCEs (7.6, 5.4, 4.5, 21.4): **9.7%**. Not Chevron's method.

gaps:
- No document prints a trailing-twelve-month ROCE, so the figure is calculated from the reported numbers.
- Sources are EX-99.1 text files with no PDF pages to inspect. The extracted rows reconcile internally.
- D01–D07 were covered only by search hits for ROCE and capital employed, not read in full. D07 (dated 2025-07-18) contains only a forward-looking ROCE target. D11 was read only for its balance sheet and ROCE table. Also read: D08 lines 330–399, D09 lines 330–381, D10 lines 355–434 and D12 lines 1–110 and 300–419.

contaminated: no

Packet files used, all under `D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\solver-2\text\`: `D08.txt`, `D09.txt`, `D10.txt`, `D11.txt`, `D12.txt`, `manifest.json`.

## Shortcut auditor (shortcut-auditor, packet shortcut), completed 2026-10-06

answer: **10.9%**

verdict: clear

shortest_path:
1. **The full-year method (D10, Attachment 2 ROCE table, Q4 2025 release).** For a full year Chevron does not annualize: "Annualized ROCE earnings" equals ROCE earnings (13,581 for 2025). It divides that by the simple average of capital employed at the start and end of the year. The footnote says: "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period." I checked this against D10's balance sheet:
   - Dec 31, 2024: 24,541 + 152,318 + 839 = 177,698
   - Dec 31, 2025: 40,758 + 186,450 + 5,726 = 232,934
   - Average: (177,698 + 232,934) / 2 = 205,316, which matches the reported 205,316. 13,581 / 205,316 = 6.6%, which matches the reported 6.6%.
2. **ROCE earnings for the twelve months ended June 30, 2026.**
   - FY2025 13,581 (D10) − H1 2025 6,469 (D08, and the same comparative in D12) + H1 2026 15,135 (D12) = **22,247**.
   - Cross-check by adding the four quarters: Q3'25 3,942 (D09) + Q4'25 3,170 (D10) + Q1'26 2,603 (D11) + Q2'26 12,532 (D12) = 22,247.
   - Cross-check by component: reported earnings 20,591 + noncontrolling interest 374 + after-tax interest 1,282 = 22,247.
3. **Capital employed at the two end points.**
   - June 30, 2025 (D08, Attachment 2): 29,467 + 146,417 + 841 = 176,725
   - June 30, 2026 (D12, Attachment 2): 37,075 + 189,883 + 5,675 = 232,633
   - Average: 409,358 / 2 = **204,679**
4. **Result.** 22,247 / 204,679 = 10.87%, which rounds to **10.9%**. That is well away from a rounding boundary.

sufficient_documents:
- Direct route: D08 + D10 + D12.
- Two-document route: D10 + D12. Back-solve June 30, 2025 capital employed from D12's H1 2025 average (177,212) and D10's Dec 31, 2024 figure: 2 × 177,212 − 177,698 = 176,726. That gives 10.87%, the same answer.
- Other alternatives: D09 can stand in for D08 (2 × 206,935 − 237,144 = 176,726). D09 + D10 + D11 + D12 work via the quarterly sum.
- D10 is the only document with Q4/FY2025 ROCE earnings, so every route needs it. No single document is enough: D12 has nothing for H2 2025.

searches:
- Search terms: "return on capital", "ROCE", "capital employed", "trailing", "twelve months", "12 months", "last/prior four quarters", "TTM", "LTM", "rolling". All 12 text files (D01–D12) were covered.
- The only "trailing 12 months" basis in the packet is for CFFO (D11 and D12 footnotes). No document states a trailing-twelve-month or June-2026 twelve-month ROCE.
- Read in full: D12. Read in part: the ROCE and balance-sheet sections of D08, D09, D10 and D11, plus the D08 and D10 headers and highlights. I also checked D05's Dec 31, 2023 data against the FY2024 average (consistent).
- I checked the key inputs in the original docs/ files (cvx_ex991_2025-08-01, 2026-01-30, 2026-07-31). They match text/.
- I did not open question.txt.

readings/gaps:
- Other readings, none of which match Chevron's full-year method:
  - Average of the five quarter-end balances (Sep 30, 2025: 237,144; Mar 31, 2026: 234,799) gives 222,847 and **10.0%**.
  - Average of the four quarterly average balances (227,389) gives **9.8%**.
  - Using Dec 31, 2025 as the starting balance (232,784) gives 9.6%.
  - Simple mean of the four quarterly ROCE percentages gives 9.7%.
- Likely traps:
  - D12's headline "return on capital employed of 21 percent" is Q2 2026 annualized (21.4%).
  - D12's YTD figure of 13.0% is H1 2026 annualized.
  - Neither is a twelve-month figure.
- Difficulty risk: the D10 + D12 route needs only simple subtraction plus one back-solved balance. That is an ordinary cross-document calculation, not a shortcut.
- Gaps: I did not read D01–D07 in full, but keyword searches covered them and they predate the period. No extraction problems found. No contamination: I received only the packet path and the question.

Key file paths:
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\shortcut\text\D12.txt
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\shortcut\text\D10.txt
- D:\Dev\Docket\tasks\aq-00998\runs\q05-r0-v2-5153104dde36d6a95f5bb77f699632e08b34af03c78f45396dff260e698dcf72\shortcut\text\D08.txt
