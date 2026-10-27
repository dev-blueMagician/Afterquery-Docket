# i03 strong-solver screen, solver B (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 13).

answer: 13 basis points (Fifth Third ≈ 58.127% − Huntington ≈ 57.998% = 12.96 bps → +13 bps)
confidence: high
path:
 1. Fifth Third Q2 2026 noninterest expense $2,109M — D01 p.5 "Noninterest expense (U.S. GAAP) $2,109 $2,395 $1,264"; also D01 p.29 reconciliation row "Noninterest expense (w) 2,109".
 2. Fifth Third itemized merger charges in expense $203M — D01 p.5/p.29 "Merger-related charges (203) (635) —"; D01 p.2 footnote "Pre-tax merger-related charges increased noninterest expense by $203 million". Noninterest-income merger line is zero for Q2 (D01 p.4 "Merger-related charges — 22 —"); "Merger-related Day 1 ACL build" is a provision item and also zero in Q2 ("— 83 —").
 3. Fifth Third FTE revenue $3,279M — D01 p.29 "Total revenue (FTE) (a) + (u) | $3,279" (= NII FTE 2,220 + noninterest income 1,059). D01's own definition matches the question: "Efficiency ratio (FTE) (w) / [(a) + (u)] 64.3%".
 4. Huntington Q2 2026 noninterest expense $1,809M — D03 Table 8 "Total noninterest expense $1,809".
 5. Huntington itemized acquisition charges $152M — D03 Table 2 "Acquisition-related expenses $ (152) (116) (0.06)"; D03 Table 9 "Total noninterest expense $ 152" and "Acquisition-related expenses included in Notable Items $ 152" (line items 38+74+15+2+4+8+7+4 = 152); D03 p.1 "inclusive of $152 million of pre-tax Notable Items ... due to acquisition-related expenses". No acquisition item itemized in revenue for Q2 (only revenue notable item is a Q3 2025 trust-sale gain, "—" for Q2 2026).
 6. Huntington FTE revenue $2,857M — D03 Table 3 "Total revenue - FTE (1) $ 2,857" (= NII FTE 2,072 + noninterest income 785).
 7. Huntington's reported 61.5% is not the question's definition (D04 p.18 footnote (2): "Noninterest expense less amortization of intangibles divided by ... FTE ... excluding gains (losses) on sales of securities"), so computed from line items rather than using the published ratio.
 8. Fifth Third: (2,109 − 203) / 3,279 = 1,906 / 3,279 = 58.1275%.
 9. Huntington: (1,809 − 152) / 2,857 = 1,657 / 2,857 = 57.9979% (D03 Table 10 also prints "Total adjusted noninterest expense $1,657").
 10. Difference: 58.1275 − 57.9979 = 0.1296 percentage points = 12.96 bps → +13 bps (Fifth Third higher). Arithmetic verified by long division; result far from 12.5/13.5 rounding boundaries.
minimal_documents: D01 + D03. D02 (Fifth Third presentation) can replace D01 (slide 42: "Noninterest expense (U.S. GAAP) (g) $2,109", "Merger-related charges (203)", income-side "Merger-related charges — 22", "Revenue (FTE) (c) + (e) 3,279"; slide 40 "$203 million pre-tax ... merger-related charges"). D04 cannot replace D03 for the $152M (it shows only "Add: Notable Items, after tax 116" without labeling it acquisition-related), though D04 confirms 1,809 and "Total revenue FTE $2,857". D05 (KeyCorp) not needed — search found no mention of either bank/Comerica/Cadence.
readings:
 - Using Huntington's own ratio formula (excluding amortization and securities gains) then removing the $152M: (1,755 − 152) / 2,855 = 56.147% → gap ≈ 198 bps; conflicts with the question's stated definition and "only."
 - Unadjusted reported ratios: 64.3% − 61.5% = 280 bps; Fifth Third's adjusted 57.1% excludes more than merger charges (not "only").
 - Rounding each ratio to one decimal before subtracting: 58.1% − 58.0% = 10 bps (less defensible given "to the nearest basis point").
gaps: Inputs are rounded to $ millions ("Totals may not foot due to rounding"), so in the theoretical worst case the true difference could vary by up to about ±10 bps; computed from printed figures it is 13. Read: D01 lines 1–260 and 1590–1750 plus targeted definitions search; D02 in full; D03 lines 1–354 and 400–435; D04 lines 150–290, 660–750, 1040–1240 plus targeted searches; D05 only by keyword search. Sources are text/HTML extractions — no PDFs or layout files existed in the packet, so no PDF pages were inspected; no extraction problems found in the decisive rows.
contaminated: no (received only the question; did not open question.txt)
