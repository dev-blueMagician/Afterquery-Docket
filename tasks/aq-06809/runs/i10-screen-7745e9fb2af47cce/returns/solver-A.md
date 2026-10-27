# i10 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-19

Raw return, verbatim. Judged: right (gold 3.8). Readings raised: 3.2 (Huntington's printed own-definition ratio),
8.6 / 8.0 (Q2-Q4 only), input-rounding band 3.67-3.86 (a source printing Q1 2025 as 61.1% would give 3.7).

answer: 3.8 percentage points. Fifth Third's highest 2025 quarter was 1Q25 at about 61.0%. Huntington's highest was 4Q25 at about 64.8%.
confidence: high

path:
1. Fifth Third's ratio already matches the question's measure. D01 p.29, line 1665: "Efficiency ratio (FTE) (w) / [(a) + (u)]", where (w) is noninterest expense, (a) is "Net interest income (FTE)" and (u) is noninterest income.
2. Fifth Third's five-quarter table (D01 p.15, lines 650/653/691) gives total revenue (FTE) "2,344 | 2,306 | 2,250" and noninterest expense "1,309 | 1,267 | 1,264" for 4Q25, 3Q25 and 2Q25. The printed ratio row is "Efficiency (FTE)(a) 64.3|84.5|55.8|54.9|56.2", so 4Q25 = 55.8, 3Q25 = 54.9 and 2Q25 = 56.2. D02 line 91 repeats these ratios.
3. Fifth Third's 1Q25 is not printed, so I derived it from the year-to-date columns (D01 p.14, lines 541 and 544). Year to date June 2025: total revenue (FTE) 4,386 and noninterest expense 2,568 (the printed YTD ratio is 58.6%).
   - 1Q25 revenue = 4,386 − 2,250 = 2,136
   - 1Q25 expense = 2,568 − 1,264 = 1,304
   - 1,304 / 2,136 = 61.05%, which makes 1Q25 Fifth Third's 2025 high.
   - Check: the 2026 YTD columns equal 2Q26 + 1Q26 (4,504 = 2,109 + 2,395; 6,113 = 3,279 + 2,834).
4. Huntington's own ratio uses a different formula. D04 p.3, note (4): "Noninterest expense less amortization of intangibles divided by the sum of FTE net interest income and noninterest income excluding securities gains (losses)". Its printed ratios (D03 Table 1, line 80: 64.2 / 57.4 / 59.0 for 4Q25 / 3Q25 / 2Q25) therefore do not fit the question's measure, and I recomputed them.
5. Huntington quarterly figures (D04 p.10; also D03 Tables 3 and 8):
   - Line 704: "Total noninterest expense 1,809 1,774 1,420 1,246 1,197"
   - Line 738: "Total revenue FTE $2,857 $2,592 $2,191 $2,151 $1,954"
   - Columns run Jun-26, Mar-26, Dec-25, Sep-25, Jun-25.
6. Huntington six months to June 2025 (D04 p.22, lines 1405/1426; also p.2): noninterest expense 2,349 and total revenue 3,889, both FTE basis. So 1Q25 = 1,152 / 1,935.
7. Huntington ratios on the question's measure:
   - 1Q25: 1,152 / 1,935 = 59.53%
   - 2Q25: 1,197 / 1,954 = 61.26%
   - 3Q25: 1,246 / 2,151 = 57.93%
   - 4Q25: 1,420 / 2,191 = 64.81% (highest)
   - Check against Huntington's own formula: 4Q25 (1,420 − 13) / 2,191 = 64.2%, matching the printed figure.
8. Difference: 64.811 − 61.049 = 3.76, which rounds to 3.8. Rounding each ratio first gives the same result: 64.8 − 61.0 = 3.8.

minimal_documents: D01 + D04.
- D02 can stand in for D01's five-quarter ratios but has no 1Q25 or YTD 2025 figures, so D01 is required.
- D03 has Huntington's 2Q25–4Q25 figures but no six-month data, so D04 is required to rule out 1Q25.
- D05 is KeyCorp's release (30 KeyCorp mentions, none of either bank) and is not needed.

readings:
- (a) Using Huntington's printed 4Q25 ratio of 64.2% (its own formula) instead of the question's measure: 64.2 − 61.05 = 3.15, or 64.2 − 61.0 = 3.2. Answer 3.2.
- (b) Counting only the 2025 quarters printed in the five-quarter tables (2Q25–4Q25) and skipping the derived 1Q25: Fifth Third's high is 2Q25 at 56.18%, so 64.81 − 56.18 = 8.6. With Huntington's printed 64.2, it is 8.0.
- (c) Rounding sensitivity: Fifth Third's 1Q25 comes out at 61.049%, right at the 61.0/61.1 boundary. Because the inputs are rounded to $1 million, the true difference could fall anywhere from about 3.67 to 3.86. The packet's figures give 3.76, so 3.8, but a source printing 1Q25 as 61.1% would give 3.7.

gaps:
- Fifth Third's 1Q25 ratio is derived from year-to-date minus 2Q25, not printed. Huntington's 1Q25 is derived the same way, though it does not affect the answer.
- The documents are text extractions (method "text"), with no PDFs to check against.
- Unread coverage:
  - D01: read lines 1–140, 530–729 and 1480–1679 only.
  - D02: searched only (efficiency, 1Q25, FY25).
  - D03: read lines 1–200 and 274–303, plus searches.
  - D04: read lines 1–320, 640–779, 1080–1139 and 1360–1439.
  - D05: checked only for which bank it covers.

contaminated: no
