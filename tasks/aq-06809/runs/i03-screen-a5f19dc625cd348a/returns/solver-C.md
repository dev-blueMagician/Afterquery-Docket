# i03 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-18

Raw return, verbatim. Judged: right (gold 13).

answer: +13 basis points (Fifth Third ≈58.13% − Huntington ≈58.00%; unrounded difference 12.96 bp)
confidence: high
path:
1. Fifth Third 2Q26 noninterest expense: D01 p.5 "Total noninterest expense|$2,109"; D01 p.29 non-GAAP reconciliation "Noninterest expense (w)|2,109".
2. Fifth Third itemized merger charges: D01 p.2 footnote "Pre-tax merger-related charges increased noninterest expense by $203 million"; D01 p.5 and p.29 "Merger-related charges|(203)" (expense). Income-side: D01 p.4/p.29 "Merger-related charges|— 22 —" → zero in 2Q26 (22 is 1Q26), so no revenue adjustment.
3. Fifth Third FTE revenue: D01 p.29 "Total revenue (FTE) (a) + (u)|$3,279" (= NII FTE 2,220 + noninterest income 1,059). Check: 2,109/3,279 = 64.3% matches printed "Efficiency ratio (FTE) (w) / [(a) + (u)]|64.3".
4. Huntington noninterest expense: D03 Table 8 "Total noninterest expense|$|1,809" (also D04 p.1, p.10).
5. Huntington itemized acquisition charges: D03 Table 9 "Acquisition-related expenses included in Notable Items|$|152" (2Q26), equal to total Notable Items in expense (152); D03 Table 2 lists "Acquisition-related expenses|$|(152)" as the only 2Q26 Notable Item; Table 7 shows no 2Q26 notable item in noninterest income.
6. Huntington FTE revenue: D03 Table 3 "Total revenue - FTE (1) $ 2,857" (= 2,072 + 785); D04 p.10 "Total revenue FTE (1)|$|2,857".
7. Huntington's printed ratio is not on the question's definition: D04 note (4) "Noninterest expense less amortization of intangibles divided by the sum of FTE net interest income and noninterest income excluding securities gains (losses)" (1,755/2,855 = 61.5%). Question defines plain noninterest expense over FTE revenue, so used 1,809 and 2,857.
8. Calculations: Fifth Third (2,109 − 203)/3,279 = 1,906/3,279 = 58.1275%; Huntington (1,809 − 152)/2,857 = 1,657/2,857 = 57.9979%; difference 0.1296 pp = 12.96 bp → 13 bp. (Rounding each ratio to nearest bp first: 58.13% − 58.00% = 13 bp, same.)
Excluded only merger/acquisition items; did not remove Fifth Third's other "certain items" (technology-related asset impairments 7, severance 7, interchange litigation 1 expense/1 income, securities repositioning 10, deferred comp 30) — not merger charges; hence did not use Fifth Third's 57.1% adjusted efficiency ratio.

minimal_documents: D01 + D03. Alternatives: D02 can replace D01 (slide 42: "Noninterest expense (U.S. GAAP) (g) $2,109", "Merger-related charges (203)", income-side merger charges "—", "Revenue (FTE) (c) + (e) 3,279"; slide 40 "$203 million pre-tax ... merger-related charges"). D04 cannot replace D03 — it has 1,809 expense and 2,857 revenue but does not itemize the $152 million (only "Notable Items, after tax|116"), so D03 is required. D05 (KeyCorp) not needed (no Fifth Third/Huntington/Comerica/Cadence mentions).

readings:
- Using Huntington's own definition adjusted for acquisition charges: (1,755 − 152)/2,855 = 56.15% → vs Fifth Third 58.13% ≈ +198 bp (rejected; the question's parenthetical sets the definition).
- GAAP rather than FTE revenue: 1,906/3,274 = 58.22% vs 1,657/2,837 = 58.41% → ≈ −19 bp (rejected; question says FTE).
- No exclusions: 64.32% − 63.32% ≈ 100 bp; printed ratios 64.3 − 61.5 = 280 bp — neither matches question.
- Rounding ratios to 0.1% before subtracting → 58.1 − 58.0 = 10 bp (conflicts with requested nearest-bp precision).

gaps: None affecting the answer (all inputs whole millions; result 0.46 bp from the 12.5 rounding boundary; printed figures agree across documents). Coverage: D01 lines 1–349 and 1480–1739 (lines 350–1479 only searched); D02 lines 1–30 and 84–100 (lines 31–83 not read; searches for merger/efficiency/integration terms hit only read lines); D03 read in full; D04 lines 150–299, 660–749, 1080–1139 plus searches; D05 searched only. Did not open original PDFs (extracted figures internally consistent across documents).

contaminated: no
