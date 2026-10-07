# q05 rev 2 raw returns (tested_sha256 fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e)

Fresh role agents dispatched 2026-10-06 by the caller session with only the workspace root, their own
packet path and the exact question (closed-book: question only). Returns are pasted unabridged.

## Closed-book solver (question only), completed 2026-10-06

answer: unknown
confidence: low
basis: I know the method. ROCE = (net income attributable to Chevron + after-tax interest expense + noncontrolling-interest net income) ÷ average capital employed. Capital employed is total debt + Chevron stockholders' equity + noncontrolling interests, averaged from the start and end of the period. For the twelve months ended June 30, 2026, I would need earnings, interest and noncontrolling-interest figures from Q3 2025 through Q2 2026. I would also need the balance sheets for June 30, 2025 and June 30, 2026. Chevron's Q2 2026 results would have come out around late July 2026, after my knowledge cutoff, so I can't get a figure to two decimal places. As a rough guess, the larger capital base after the Hess acquisition points to about 6–8%, but that is speculation.
contaminated: no

## Shortcut auditor (shortcut-auditor, packet shortcut), completed 2026-10-06

**Answer: 10.87%.** No document states a trailing-twelve-month ROCE, so it has to be built from three releases (or two, using a back-calculation). I found no shortcut, and the computation is not contaminated: I received only the workspace root, packet path and question, and I did not open `question.txt`.

answer: 10.87%

verdict: clear

shortest_path:
1. **The full-year method (D10, `text/D10.txt` lines 394–412).**
   - ROCE earnings = reported earnings + noncontrolling interest + after-tax interest expense.
   - For a full year nothing is annualized: "Annualized ROCE earnings" equals ROCE earnings, both 13,581.
   - The footnote says: "Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period."
   - Check on the reported figure: the FY2025 average of 205,316 equals (Dec-24 177,698 + Dec-25 232,934) / 2, a two-point average. A five-quarter-end average would be 200,852, which does not match.
   - D05 confirms the same method for FY2024: (182,765 + 177,698) / 2 = 180,232, as reported.
2. **ROCE earnings for the twelve months ($MM).**
   - FY2025 13,581 (D10 line 405) − six months 2025 6,469 + six months 2026 15,135 (both D12 line 389) = 22,247.
   - Quarterly cross-check: Q3-25 3,942 (D09 line 372) + Q4-25 3,170 (D10) + Q1-26 2,603 (D11 line 379) + Q2-26 12,532 (D12) = 22,247.
   - Component check: earnings 20,591 + noncontrolling interest 374 + after-tax interest 1,282 = 22,247.
3. **Capital employed (debt + Chevron equity + noncontrolling interests).**
   - June 30, 2025 (D08 lines 358–360): 29,467 + 146,417 + 841 = 176,725.
   - June 30, 2026 (D12 lines 352–354): 37,075 + 189,883 + 5,675 = 232,633.
   - Average: 409,358 / 2 = 204,679.
4. **ROCE** = 22,247 / 204,679 = 10.869%, which rounds to **10.87%**.

All the balance-sheet averages I derived match the reported quarterly averages within 1 of rounding: Q2-25 178,243, six months 2025 177,212, Q3-25 206,935, Q4-25 235,039, Q1-26 233,867, Q2-26 233,716.

sufficient_documents:
- **Direct route:** D08 + D10 + D12.
- **Two-document route (D10 + D12):** back out June 30, 2025 capital employed as 2 × 177,212 (D12, six months 2025 average) − 177,698 (D10, Dec-24) = 176,726. That gives 10.8692%, the same answer.
- **Other route for June 2025:** D09 gives 2 × 206,935 − 237,144 = 176,726.
- **No single document is enough.** D12 lacks the second half of 2025 and the June 2025 balance sheet, and D10 has no 2026 data. The D10 + D12 route is simple, which makes the question easier, but it still needs two documents.

searches:
- **Literal terms:** "return on capital employed", "ROCE", "capital employed", "trailing", "twelve months", "12 months", "prior four quarters", "LTM", "TTM", "rolling", "Average capital employed", "ROCE earnings", plus the balance-sheet line items.
- **Results:** the only "trailing 12 months" basis in the packet is for cash flow from operations (D11 and D12). Narrative ROCE mentions are period-specific only: D12 says "return on capital employed of 21 percent" for Q2, D09 says ROCE fell because of Hess, and D07 cites a "double-digit ROCE" target.
- **Coverage:** I read D12 in full. I read the ROCE tables and balance sheets in D05 and D08–D11, and D07's headlines.
- **Fidelity:** I checked key figures against the originals in `docs/` (2025-08-01, 2026-01-30, 2026-07-31) and they matched exactly.

readings/gaps:
- **Five-quarter-end average capital employed (222,847):** 9.98%. Rejected because it contradicts the reported FY2025 average of 205,316.
- **Mean of the four quarterly averages (227,389):** 9.78%. Rejected for the same reason.
- **Dec-25 to Jun-26 average (232,784) as the denominator:** 9.56%. This is the wrong period.
- **The six-month 13.0% or the Q2 21.4%:** these are year-to-date and quarterly figures, not twelve-month figures.
- **Gaps:** I didn't fully read D01–D04, D06, or the narrative parts of D08–D11. They cover earlier periods or are irrelevant to the inputs, and I grep-checked them for ROCE and trailing-period wording. All extractions are plain text and I found no extraction gaps.

Relevant files are under `D:\Dev\Docket\tasks\aq-00998\runs\q05-r2-v2-fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e\shortcut\`:
- `text\D12.txt`
- `text\D10.txt`
- `text\D08.txt`
- `text\D09.txt`
- `text\D11.txt`
- `text\D05.txt`
- `text\manifest.json`

## Solver A (blind-solver, packet solver-1), completed 2026-10-06

I worked this out from the filings. No document prints a trailing-twelve-month ROCE, but Chevron's full-year method is shown in its FY2025 table and reproduces exactly from the balance sheets. Applying it to July 2025 through June 2026 gives 10.87%.

answer: 10.87%

confidence: high

path:
1. **The full-year method (D10, ROCE table, lines 394–412).**
   - FY2025 "ROCE earnings" is 13,581: total reported earnings 12,299 + noncontrolling interest 186 + after-tax interest expense 1,096.
   - "Annualized ROCE earnings" is also 13,581, so full-year earnings are not annualized. Six-month figures are multiplied by 2 (D12: 15,135 → 30,270).
   - "Average capital employed (1) … 205,316"; ROCE is 6.6%.
   - Footnote (1): "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period."
   - Check against the D10 balance sheet (lines 370–372):
     - Dec 31, 2025: 40,758 + 186,450 + 5,726 = 232,934
     - Dec 31, 2024: 24,541 + 152,318 + 839 = 177,698
     - (177,698 + 232,934) / 2 = 205,316, an exact match. So the full-year figure is a two-point average.
   - Averaging the four FY2025 quarterly averages does not reproduce it: (178,730 + 178,243 + 206,935 + 235,039) / 4 = 199,737.
2. **ROCE earnings for the twelve months ended June 30, 2026.**
   - D12, lines 386–389: six months 2026 "ROCE earnings" is 15,135 (14,282 + 225 + 628); six months 2025 is 6,469 (5,990 + 37 + 442).
   - Twelve months = 13,581 + 15,135 − 6,469 = 22,247.
   - Cross-check by quarters: Q3'25 3,942 (D09, line 372) + Q4'25 3,170 (D10, line 405) + Q1'26 2,603 (D11, line 379) + Q2'26 12,532 (D12, line 389) = 22,247.
3. **Capital employed at each end of the window.**
   - June 30, 2026 (D12, lines 352–354): total debt 37,075 + Chevron stockholders' equity 189,883 + noncontrolling interests 5,675 = 232,633.
   - June 30, 2025 (D08, lines 358–360): 29,467 + 146,417 + 841 = 176,725.
   - Consistency checks:
     - D12 six-month 2026 average: (232,934 + 232,633) / 2 = 232,783.5, printed as 232,784.
     - D08 six-month 2025 average: (177,698 + 176,725) / 2 = 177,211.5, printed as 177,212.
     - Every quarterly average from Q3'25 to Q2'26 also reproduces, using D09 Sep 30, 2025 capital employed of 237,144 and D11 Mar 31, 2026 capital employed of 234,799.
   - Average = (176,725 + 232,633) / 2 = 204,679.
4. **ROCE** = 22,247 / 204,679 = 10.869%, which rounds to 10.87%. This is not near a rounding boundary.

minimal_documents: D08, D10, D12.
- D09 can replace D08: June 30, 2025 capital employed can be backed out as 2 × 206,935 − 237,144 = 176,726. That gives an average of 204,679.5 and still 10.87%.
- D10 cannot be replaced. It is the only source for Q4'25 / FY2025 earnings and the full-year method.

readings:
- Averaging the four quarterly averages (206,935, 235,039, 233,867, 233,716 → 227,389) gives 9.78%. This is not the full-year method.
- A five-point average of quarter-end capital employed (176,725, 237,144, 232,934, 234,799, 232,633 → 222,847) gives 9.98%. This is also not the full-year method.
- Leaving noncontrolling interests out of capital employed ((175,884 + 226,958) / 2 = 201,421) gives 11.05%. This contradicts the footnote.
- The printed six-month 2026 annualized ROCE is 13.0%, but that is a different period and method.

gaps:
- No trailing-twelve-month ROCE is printed anywhere; a search for "trailing" or "twelve months" found only the cash-flow-from-operations footnotes in D11 and D12.
- The sources are text only (manifest method "text"), so there were no PDF pages to inspect.
- I read the manifest, the ROCE tables and balance-sheet blocks in D08–D12, and the search hits across D01–D12. I did not read every narrative section in full.
- Debt and noncontrolling-interest rows were checked against the docs/ originals. The equity rows were checked in text/ only.

contaminated: no

Files used, all under `D:\Dev\Docket\tasks\aq-00998\runs\q05-r2-v2-fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e\solver-1\text\`: `D08.txt`, `D09.txt`, `D10.txt`, `D11.txt`, `D12.txt`, `manifest.json`.

## Solver B (blind-solver, packet solver-2), completed 2026-10-06

answer: 10.87%

confidence: high

path:
1. **The full-year method (D10, Q4 2025 release, ROCE table lines 394–412).** Year ended Dec 31, 2025: "Total reported earnings | … | $ 12,299", "Noncontrolling interest | … | 186", "Interest expense (A/T) | … | 1,096", "ROCE earnings | … | 13,581". The full-year "Annualized ROCE earnings" is also 13,581, so the year's actual earnings are used without annualizing. "Average capital employed (1) … 205,316". "ROCE … 6.6 %". Footnote: "Capital employed is the sum of Chevron Corporation stockholders' equity, total debt and noncontrolling interest. Average capital employed is computed by averaging the sum of capital employed at the beginning and the end of the period."
   - Test that the average uses only the start and end of the year. D10 balance sheet: Dec 31, 2025 is 40,758 + 186,450 + 5,726 = 232,934, and Dec 31, 2024 is 24,541 + 152,318 + 839 = 177,698. (232,934 + 177,698)/2 = 205,316, which matches the printed figure exactly.
   - An average of the five quarter-ends would give 200,852 (a 6.76% ROCE), so that is not Chevron's method.
2. **ROCE earnings for the twelve months ended June 30, 2026.**
   - D12 (Q2 2026 release, lines 386–389): six months 2026 = 14,282 + 225 + 628 = 15,135; six months 2025 = 5,990 + 37 + 442 = 6,469 (D08 line 387 shows the same 6,469).
   - TTM = 13,581 + 15,135 − 6,469 = **22,247**.
   - Cross-check by summing quarters: Q3'25 3,942 (D09 line 372) + Q4'25 3,170 (D10 line 405) + Q1'26 2,603 (D11 line 379) + Q2'26 12,532 (D12 line 389) = 22,247.
   - By component: reported earnings 20,591 + NCI 374 + after-tax interest 1,282 = 22,247.
3. **Capital employed at the start and end of the window.**
   - June 30, 2026 (D12 lines 352–354): "Total debt $ 37,075", "Total Chevron Corporation stockholders' equity $ 189,883", "Noncontrolling interests $ 5,675". Sum: **232,633**.
   - June 30, 2025 (D08 lines 358–360): "Total debt $ 29,467", equity "$ 146,417", "Noncontrolling interests $ 841". Sum: **176,725**.
   - Check: these balances reproduce every printed average in the packet. For example, Q2'26 is (234,799 + 232,633)/2 = 233,716; H1'25 is (177,698 + 176,725)/2 = 177,211.5, printed as 177,212; Q3'25 is (176,725 + 237,144)/2 = 206,934.5, printed as 206,935.
   - Average capital employed: (176,725 + 232,633)/2 = **204,679**.
4. **ROCE.** 22,247 / 204,679 = 0.108692, which is **10.87%** at two decimal places.

minimal_documents: D08, D10, D12.
- Alternative set: D10 and D12 only. The June 30, 2025 capital employed can be derived from D12's printed H1 2025 average and D10's Dec 31, 2024 balances: 2 × 177,212 − 177,698 = 176,726 (±1 from rounding). The average is then 204,679 to 204,680, which still gives 10.87%.
- D10 cannot be replaced: full-year 2025 and Q4 2025 ROCE earnings appear only there.
- D09 and D11 were used only for the quarter-sum cross-check.

readings:
- **Average of the five quarter-end balances** instead of start and end only: (176,725 + 237,144 + 232,934 + 234,799 + 232,633)/5 = 222,847, giving 9.98%. The Hess-driven jump in capital employed after June 2025 is why this differs. It contradicts the stated method and the 2025 check, so I reject it.
- **Mean of the four printed quarterly averages**: 227,389, giving 9.78%. This is not Chevron's method.
- **The printed six-month 2026 annualized ROCE (13.0%) or Q2 2026 ROCE (21.4%)**: these cover different periods and use annualization, which the full-year method does not.

gaps:
- No document states a trailing-twelve-month ROCE directly. Searches for "trailing", "twelve months", "12 months", "TTM" and "LTM" across D01–D12 found only the TTM cash-flow footnote.
- All documents are text extractions (no page images, no layout files), so I inspected no PDF pages.
- I did not read every document in full; I searched all 12 for ROCE, capital-employed and balance-sheet terms, read the relevant tables in D08–D12, and checked D01, D05 and D06 balance-sheet rows through those searches.
- I did not read the docs/ originals separately; the manifest says the text files were extracted from them.

contaminated: no

Packet files: D:\Dev\Docket\tasks\aq-00998\runs\q05-r2-v2-fc72fa1299ebd4444a7ca123164fcc7ac5cd15ac529f43890faaf8f446a3295e\solver-2\text\D08.txt, D10.txt, D12.txt (and D09.txt, D11.txt for the cross-check)
