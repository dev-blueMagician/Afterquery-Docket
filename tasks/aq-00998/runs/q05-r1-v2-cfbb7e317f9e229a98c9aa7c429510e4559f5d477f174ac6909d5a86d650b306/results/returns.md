# q05 rev 1 raw returns (tested_sha256 cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306)

Fresh role agents dispatched 2026-10-06 by the caller session with only the workspace root, their own
packet path and the exact question (closed-book: question only). Returns are pasted unabridged.

## Solver A (blind-solver, packet solver-1), completed 2026-10-06

answer: **10.87%**

confidence: high

path:
1. **How the full-year method works.** The FY2025 ROCE table in D10 (lines 394–412) shows that for a full year, "Annualized ROCE earnings" is simply the ROCE earnings, 13,581 (no scaling). ROCE earnings = Total reported earnings 12,299 + Noncontrolling interest 186 + Interest expense (A/T) 1,096. Average capital employed is 205,316 and ROCE is 6.6% (13,581 / 205,316 = 6.61%). Footnote (1) says: "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period." D12 (line 396) repeats this wording exactly.
2. **The full-year average uses only the start and end of the year.** Capital employed at Dec 31, 2024 (D10 lines 370–372) is 24,541 + 152,318 + 839 = 177,698. At Dec 31, 2025 it is 40,758 + 186,450 + 5,726 = 232,934. Their average is exactly 205,316, the printed figure. Averaging all five quarter-ends instead gives about 200,853, which does not match. FY2024 also checks: Dec 31, 2023 capital employed (D05 lines 358–360) is 20,836 + 160,957 + 972 = 182,765, and (182,765 + 177,698) / 2 = 180,231.5, matching the printed 180,232.
3. **ROCE earnings for the twelve months ended June 30, 2026** (take the full year 2025, remove the first half of 2025, add the first half of 2026):
   - FY2025 (D10 line 405): 13,581
   - First half 2025 (D12 line 389 and D08 line 387): 6,469
   - First half 2026 (D12 line 389): 15,135
   - 13,581 − 6,469 + 15,135 = **22,247**
   - Check by adding the four quarters: Q3'25 3,942 (D09 l.372) + Q4'25 3,170 (D10 l.405) + Q1'26 2,603 (D11 l.379) + Q2'26 12,532 (D12 l.389) = 22,247. The components also agree: earnings 20,591 + noncontrolling interest 374 + after-tax interest 1,282 = 22,247.
4. **Capital employed at the start and end of the period:**
   - June 30, 2025 (D08 lines 358–360): "Total debt $ 29,467", "Total Chevron Corporation stockholders' equity $ 146,417", "Noncontrolling interests $ 841". Sum = 176,725.
   - June 30, 2026 (D12 lines 352–354): "Total debt $ 37,075", stockholders' equity "$ 189,883", "Noncontrolling interests $ 5,675". Sum = 232,633.
   - Both sums are consistent with the printed averages. D12's six-month 2026 average is (232,934 + 232,633) / 2 = 232,783.5, printed as 232,784. D08's six-month 2025 average is (177,698 + 176,725) / 2 = 177,211.5, printed as 177,212.
   - Average capital employed = (176,725 + 232,633) / 2 = **204,679**.
5. **Result:** ROCE = 22,247 / 204,679 = 0.108692, which is **10.87%**. The value is 10.869%, far from any rounding boundary.
6. No document prints a trailing-twelve-month ROCE. The only "trailing 12 months" figure is cash flow from operations (D11 l.368, D12 l.376). The 21.4% (Q2) and 13.0% (first half) in D12 are annualized quarter and half-year figures, not the twelve-month figure.

minimal_documents: D08, D10, D12.
- D10 is required: Q4 2025 and FY2025 ROCE earnings appear only there.
- D12 is required: Q2 2026 results and the June 30, 2026 balances appear only there.
- D08 can be dropped. June 30, 2025 capital employed can be backed out as 2 × 177,212 (D12's six-month 2025 average) − 177,698 (D10), giving 176,726 because of rounding. The average becomes 204,679.5 and ROCE is still 10.87%. D09 works too: 2 × 206,935 − 237,144 gives 176,726.

readings:
- Averaging all five quarter-end capital employed figures (176,725; 237,144; 232,934; 234,799; 232,633 → 222,847) gives **9.98%**. This contradicts the printed FY2025 average, so it is not the full-year method.
- Averaging the four printed quarterly averages (227,389.25) gives **9.78%**. Averaging the four quarterly ROCE rates gives 9.73%. Neither is Chevron's method.
- Using reported earnings only, without the noncontrolling-interest and interest add-backs: 20,591 / 204,679 = 10.06%. This is not the method either.

gaps:
- I read the ROCE, balance-sheet and headline sections of D08–D12 and searched D05. D01–D04, D06 and D07 were covered only by keyword searches for ROCE, capital employed and trailing/12-month wording.
- The packet has no PDFs or `.layout.txt` files (the manifest says method "text"), so nothing could be checked against original pages. The table rows I needed were extracted cleanly.

contaminated: no

Files used: `D:\Dev\Docket\tasks\aq-00998\runs\q05-r1-v2-cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306\solver-1\text\D08.txt`, `...\text\D09.txt`, `...\text\D10.txt`, `...\text\D11.txt`, `...\text\D12.txt`, `...\text\D05.txt`

## Closed-book solver (question only), completed 2026-10-06

answer: About 9%. This is a rough estimate, and I don't know the exact two-decimal figure.
confidence: low
basis: I'm reasoning from memory and couldn't look anything up. Chevron's full-year method is: (net income attributable to Chevron + after-tax interest expense + noncontrolling-interest income) ÷ average capital employed. Capital employed is total debt + Chevron stockholders' equity + noncontrolling interests, averaged here over June 30, 2025 and June 30, 2026. I roughly recall earnings of about $3.5B for Q3 2025 and about $2.8B for Q4 2025. I don't have Q1–Q2 2026 earnings or the June 30, 2026 balance sheet, because those filings come after what I reliably know. Filling the gaps with assumptions (2026 oil prices and earnings, the Hess-enlarged capital base) gives roughly 6.5–10%. My best guess is around 9%.
contaminated: no

## Solver B (blind-solver, packet solver-2), completed 2026-10-06

answer: 10.87%

confidence: high

path:
1. **The full-year method.** Every ROCE table carries this footnote (D10 line 412, D12 line 396): "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period." For full years the earnings are not annualized. D10 line 406 shows "Annualized ROCE earnings" equal to ROCE earnings (13,581). So FY2025 ROCE = 13,581 / 205,316 = 6.6% (D10 line 410).
2. **Checking the two-point average.** D10 lines 370–372 give the balance sheets. Capital employed (CE) at Dec 31, 2024 = 24,541 + 152,318 + 839 = 177,698. CE at Dec 31, 2025 = 40,758 + 186,450 + 5,726 = 232,934. Their average is (177,698 + 232,934) / 2 = 205,316, which matches the printed FY2025 figure. A five-point quarter-end average does not fit the printed figures.
3. **TTM ROCE earnings** (total reported earnings + noncontrolling interest + after-tax interest expense):
   - Q3 2025: 3,942 (D09 line 372)
   - Q4 2025: 3,170 (D10 line 405)
   - Q1 2026: 2,603 (D11 line 379)
   - Q2 2026: 12,532 (D12 line 389)
   - Sum: 22,247
   - Cross-check: FY2025 13,581 − H1 2025 6,469 + H1 2026 15,135 (D12 line 389) = 22,247.
   - By component: earnings 20,591 + noncontrolling interest 374 + interest 1,282 = 22,247.
4. **CE at June 30, 2025** (D08 lines 358–360): total debt 29,467 + Chevron equity 146,417 + noncontrolling interests 841 = 176,725.
5. **CE at June 30, 2026** (D12 lines 352–354): total debt 37,075 + Chevron equity 189,883 + noncontrolling interests 5,675 = 232,633.
6. **Consistency checks.** These balances reproduce the printed averages:
   - Q3 2025: (176,725 + 237,144) / 2 ≈ 206,935
   - H1 2025: ≈ 177,212
   - Q2 2026: (234,799 + 232,633) / 2 = 233,716
   - H1 2026: ≈ 232,784
   - The Sep 30, 2025 CE (237,144) comes from D09 lines 343–345. The Mar 31, 2026 CE (234,799) comes from D11 lines 344–346.
   - The prior-year figures in D12 (2,765 / 6,469 / 178,243 / 177,212) match D08, so nothing was restated.
7. **Result.** Average CE = (176,725 + 232,633) / 2 = 204,679. ROCE = 22,247 / 204,679 = 10.869%, which rounds to **10.87%**. The value is not close to a rounding boundary.
8. **Context.** Q2 2026 dominates the result. D12 line 19 says "Reported earnings of $12.1 billion; return on capital employed of 21 percent." No document gives a trailing-12-month ROCE directly. The only "trailing 12 months" mentions are about cash flow from operations (D11 line 368, D12 line 376).

minimal_documents: D10 + D12 are enough. June 30, 2025 CE can be derived as 2 × 177,212 (D12, H1 2025 average CE) − 177,698 (D10, Dec 31, 2024 balance sheet) = 176,726. That gives an average of 204,679.5 and the same 10.87%. Reading the June 30, 2025 balance sheet directly adds D08. D09 can replace D08 for that figure (2 × 206,935 − 237,144 = 176,726). D10 is required because it is the only source for Q4 2025 or FY2025 ROCE earnings, and D12 is required for Q2 2026.

readings:
- Five-point average of quarter-end CE (Jun 30, 2025 through Jun 30, 2026): 1,114,235 / 5 = 222,847, giving 9.98%. This is not Chevron's full-year method, since the FY2025 figure matches only the two-point average.
- Mean of the four printed quarterly average CEs (227,389.25), giving 9.78%. Not the stated method.
- Simple mean of the four printed quarterly ROCEs (7.6, 5.4, 4.5, 21.4), giving 9.73%. This uses rounded inputs and is not the method.
- Leaving out noncontrolling interest (debt plus equity only, average 201,421), giving 11.05%. This contradicts the footnote's definition.

gaps: none that matter. Coverage:
- A ROCE-term search covered all of D01–D12.
- I read the ROCE tables and balance sheets of D08–D12 and lines 1–419 of D12.
- I did not read D01–D07 in full. They cover periods before the window; D07 only states a "double-digit ROCE" target.
- The sources are text extractions (method "text", no pages, no layout files), so there was no PDF page to inspect.
- I saw a question.txt in the packet listing but did not read it.

contaminated: no

Files used are in `D:\Dev\Docket\tasks\aq-00998\runs\q05-r1-v2-cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306\solver-2\text\`: D08.txt, D09.txt, D10.txt, D11.txt, D12.txt (located through manifest.json).

## Shortcut auditor (shortcut-auditor, packet shortcut), completed 2026-10-06

answer: 10.87%

verdict: clear

shortest_path:
1. **Method.** I got this from the Q4 releases and checked it against FY2025 in D10 (lines 402–412). ROCE earnings = "Total reported earnings" + "Noncontrolling interest" + "Interest expense (A/T)". For a full year these earnings are not annualized. Footnote: "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period."
   - FY2025: 12,299 + 186 + 1,096 = 13,581, divided by 205,316 = 6.6%.
   - 205,316 = (177,698 + 232,934) / 2, so the year uses only two points, start and end. A five-point quarter-end average would be about 200,853, which does not match.
2. **ROCE earnings for the 12 months ended June 30, 2026 ($MM).** I took FY2025 from D10 (13,581), added H1 2026 from D12 line 389 (15,135), and subtracted H1 2025 from D12/D08 (6,469). That gives **22,247**.
   - Quarterly cross-check: Q3 2025 3,942 (D09 line 372) + Q4 2025 3,170 (D10) + Q1 2026 2,603 (D11 line 379) + Q2 2026 12,532 (D12) = 22,247.
   - The components sum the same way: earnings 20,591 + noncontrolling interest 374 + interest 1,282 = 22,247.
3. **Capital employed.**
   - June 30, 2025 (D08 lines 358–360): 29,467 + 146,417 + 841 = **176,725**.
   - June 30, 2026 (D12 lines 352–354): 37,075 + 189,883 + 5,675 = **232,633**.
   - Both match the reported averages: D08's H1 2025 average (177,698 + 176,725) / 2 = 177,212, and D12's Q2 2026 average (234,799 + 232,633) / 2 = 233,716.
4. **Average and result.** (176,725 + 232,633) / 2 = 204,679. ROCE = 22,247 / 204,679 = 10.8692%, which rounds to **10.87%**.
   - Rounding variants of the average (204,679.5 or 204,680) still give 10.87%.

sufficient_documents:
- **Direct route:** D08 + D10 + D12.
- **Two-document route:** D10 + D12. June 30, 2025 capital employed can be backed out as 2 × 177,212 (D12's H1 2025 average) − 177,698 (Dec 31, 2024, from D10) = 176,726, which gives 10.87%.
- **Alternative:** D09 + D10 + D12. Here June 30, 2025 is backed out as 2 × 206,935 − 237,144 = 176,726.
- **Required in every route:** D10, because it is the only source for Q4 2025 / FY2025. D12, because it is the only source for June 30, 2026 balances and H1 2026 earnings.
- **No single document works.** D12 has no FY2025 or Q3–Q4 2025 data and no Dec 31, 2024 balances.

searches:
- **Terms:** ROCE, return on capital employed, capital employed, interest expense (A/T), noncontrolling interest, total debt, stockholders' equity, trailing, twelve months, 12 months, LTM, TTM, rolling, 10.87, 10.86, 10.9%, restat, recast, pro forma.
- **Documents inspected:** the ROCE tables and balance sheets in D05 and D08–D12, the D10 and D12 highlights and summaries, the D12 non-GAAP definitions, and D07, the Hess closing release. D07 has no balance data, only a "double-digit ROCE" target.
- **Shortcut check:** no document gives a trailing-12-month ROCE. The only trailing-12-month item is cash flow from operations (D11/D12 footnotes). The capital-employed inputs show no restatements.
- **Out of scope:** I did not read question.txt.

readings/gaps:
- **Rejected alternatives:**
  - Five-point quarter-end average (222,847): 9.98%. Contradicted by FY2025's two-point 205,316.
  - Mean of the four quarterly average capital-employed figures (227,389): 9.78%.
  - Capital employed without noncontrolling interest (201,421): 11.05%. Contradicted by the footnote.
  - Reported earnings only (20,591): 10.06%.
  - Mean of the quarterly ROCEs (7.6, 5.4, 4.5, 21.4): 9.73%.
  - D12's 13.0% H1 2026 annualized figure is a distractor; it covers six months, not twelve.
- **Difficulty risk:** this is a routine twelve-month build plus a two-point average, and the method is printed in every footnote. A strong reader needs only D10 + D12. That makes it easy, but it is not a shortcut.
- **Gaps:** none in what I read. I skipped D01–D04 and D06 beyond the grep hits; they fall before the relevant period.

Packet path: D:\Dev\Docket\tasks\aq-00998\runs\q05-r1-v2-cfbb7e317f9e229a98c9aa7c429510e4559f5d477f174ac6909d5a86d650b306\shortcut\text\ (D08.txt, D09.txt, D10.txt, D11.txt, D12.txt)
