# i10 strong-solver screen, solver C (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-19

Raw return, verbatim. Judged: right (gold 3.8). Readings raised: 3.2 (Huntington's printed own-definition ratio),
8.6 / 8.0 (Q2-Q4 only), 3.0 ("highest efficiency" read as the lowest ratio, called less defensible), input-rounding
band 3.69-3.84.

answer: 3.8 percentage points. Fifth Third's highest 2025 quarter was 1Q25 at about 61.0%. Huntington's was 4Q25 at about 64.8%.
confidence: medium-high. The ratio basis and arithmetic are clear. Fifth Third's 1Q25 figure is not printed as a quarter; I worked it out as six-month 2025 minus 2Q25. That keeps the result inside a rounding band of about 3.69 to 3.84.

path:
1. Fifth Third's ratio matches the question's definition. D02 slide 42: "Efficiency ratio (FTE) (g) / [(c) + (e)] 64.3% 84.5% 55.8% 54.9% 56.2%". Here g is GAAP noninterest expense, c is FTE net interest income and e is noninterest income. D01 p.29 L1665 gives the same formula: "Efficiency ratio (FTE) (w) / [(a) + (u)]".
2. Fifth Third quarterly figures, D01 p.15 L644-691 (columns Jun26, Mar26, Dec25, Sep25, Jun25):
   - Total revenue (FTE): 3,279 / 2,834 / 2,344 / 2,306 / 2,250
   - Noninterest expense: 2,109 / 2,395 / 1,309 / 1,267 / 1,264
   - Efficiency (FTE): 64.3 / 84.5 / 55.8 / 54.9 / 56.2
3. Fifth Third year-to-date June 2025, D01 p.14 L541-544 and L582: "Total revenue (FTE) ... 6,113|4,386", "Noninterest expense ... 4,504|2,568" and efficiency "73.7% | 58.6%". The income statement at L785 and L797 agrees: noninterest income 1,444, total noninterest expense 2,568.
   - 1Q25 revenue = 4,386 − 2,250 = 2,136
   - 1Q25 expense = 2,568 − 1,264 = 1,304
   - 1Q25 ratio = 1,304 / 2,136 = 61.05%
   - Check: the six-month ratio (58.6%) is above 2Q25 (56.2%), so 1Q25 must be higher than 2Q25.
   - Fifth Third 2025 quarters: 61.05, 56.18, 54.94, 55.84. Highest is 1Q25 at 61.05%.
4. Huntington's reported ratio uses a different basis. D04 note (4) L294: "Noninterest expense less amortization of intangibles divided by the sum of FTE net interest income and noninterest income excluding securities gains (losses)." So I recomputed it as total noninterest expense over total FTE revenue.
5. Huntington quarterly figures (Jun26, Mar26, Dec25, Sep25, Jun25). D04 p.10 L704 and L738; D03 Table 8 L295 and Table 3 L153 show the same:
   - "Total noninterest expense|1,809 1,774 1,420 1,246 1,197"
   - "Total revenue FTE (1)|$|2,857 $|2,592 $|2,191 $|2,151 $|1,954"
   - Amortization of intangibles: 54 41 13 11 11 (L700)
   - Reported ratios in D03 L80: "61.5 67.2 64.2 57.4 59.0"
6. Huntington year-to-date June 2025, D04 p.22 L1405 and L1426: total noninterest expense 2,349; "Total revenue (1)|$|5,449 $|3,889".
   - 1Q25 = (2,349 − 1,197) / (3,889 − 1,954) = 1,152 / 1,935 = 59.53%
   - Other 2025 quarters: 2Q25 = 1,197/1,954 = 61.26%; 3Q25 = 1,246/2,151 = 57.93%; 4Q25 = 1,420/2,191 = 64.81%
   - Highest is 4Q25 at 64.81%. The reported figure is 64.2% because 13 of intangible amortization is excluded; there were no securities gains in 4Q25.
7. Difference: 64.8106 − 61.0487 = 3.76, which rounds to 3.8. The rounded ratios give the same result (64.8 − 61.0 = 3.8).
   - Rounding check: each derived 1Q25 input could be off by up to ±1, so Fifth Third's 1Q25 ratio falls between 60.97% and 61.12%. The gap then falls between about 3.69 and 3.84. The central value is 3.8.

minimal_documents: D01 + D04.
- D01 is the only Fifth Third document with the six-month data needed for 1Q25. D02 repeats 2Q25-4Q25 only, so it cannot replace D01.
- D04 contains everything D03 has for Huntington's quarters and also the six-month data that rules out 1Q25. D03 alone leaves 1Q25 unverified.
- D05 (KeyCorp) is irrelevant.

readings:
- Using Huntington's reported 4Q25 ratio (64.2%) instead of the stated definition: 64.22 − 61.05 = 3.2. This conflicts with "each measured as noninterest expense over fully taxable-equivalent revenue".
- Using only the quarters printed in the trend tables (2Q25-4Q25), so Fifth Third's highest is 2Q25 at 56.18%: 64.81 − 56.18 = 8.6. With Huntington's reported figure: 64.2 − 56.2 = 8.0. This leaves out 1Q25, which is part of 2025.
- Reading "highest efficiency" as the best (lowest) ratio, both in 3Q25: 57.93 − 54.94 = 3.0. Less defensible given the wording "highest ... ratios".

gaps:
- Neither bank prints a 1Q25 quarterly figure; both are derived as six-month 2025 minus 2Q25 from rounded millions.
- Unread material:
  - D01: lines 120-515, 819-1480 and 1699 to the end. Grep for "efficiency" found nothing else there.
  - D04: lines 300-660, 749-1080, 1139-1370 and 1439 to the end.
  - D05: searched by grep only.
- D02 and D03 were read in full. There are no layout files or PDFs; all sources are text.

contaminated: no
