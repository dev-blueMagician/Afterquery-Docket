# i09 strong-solver screen, solver A (fresh blind-solver, claude-opus-5-5, effort max), 2026-10-19

Raw return, verbatim. Judged: right (gold 1.5). Readings raised: 3.0 (printed quarters only), 2.5 / 2.1
(Huntington's own-definition ratio, against the stated formula), input rounding (1.35-1.67, still Q1).

answer: 1.5 percentage points. The narrowest gap was in Q1 2025: Fifth Third about 61.0% vs Huntington about 59.5%. Unlike the other quarters, Fifth Third's ratio was the higher one that quarter.

confidence: high

path:
1. The question's definition matches Fifth Third's own ratio. D01 p.29 non-GAAP reconciliation: "Efficiency ratio (FTE) (w) / [(a) + (u)]", where (w) is noninterest expense, (a) is NII (FTE) and (u) is noninterest income. D02 slide 42 says the same: "Efficiency ratio (FTE) (g) / [(c) + (e)]".
2. Huntington's reported ratio does not match it, so I recomputed it. D04 note (4): "Noninterest expense less amortization of intangibles divided by the sum of FTE net interest income and noninterest income excluding securities gains (losses)".
3. Fifth Third quarterly figures, D01 p.14 five-quarter table ($M; Total revenue (FTE) / Noninterest expense / reported Efficiency (FTE)):
   - 4Q25: 2,344 / 1,309 / 55.8%
   - 3Q25: 2,306 / 1,267 / 54.9%
   - 2Q25: 2,250 / 1,264 / 56.2%
   - D02 slides 7 and 42 repeat these.
4. Fifth Third first-half 2025, D01 p.13 Year to Date column (June 2025): "Total revenue (FTE)(a) ... 6,113|4,386" and "Noninterest expense ... 4,504|2,568", efficiency 58.6%. The 2026 columns tie to quarterly sums (3,279+2,834=6,113; 2,109+2,395=4,504), so the column alignment is confirmed. I checked these rows against docs/fitb_ex991 lines 630/633.
   - 1Q25 = first half minus 2Q25: expense 2,568−1,264 = 1,304; revenue 4,386−2,250 = 2,136. Cross-check: NII FTE 2,942−1,500 = 1,442 plus noninterest income 1,444−750 = 694 gives 2,136.
5. Huntington quarterly figures, D04 p.10 (and D03 Tables 3 and 8):
   - "Total revenue FTE (1)|$|2,857 $|2,592 $|2,191 $|2,151 $|1,954"
   - "Total noninterest expense|1,809 1,774 1,420 1,246 1,197"
   - Column order is 2Q26, 1Q26, 4Q25, 3Q25, 2Q25.
6. Huntington first-half 2025, D04 p.22: "Total revenue (1)|$|5,449 $|3,889" and "Total noninterest expense|3,583 2,349". D04 p.2 shows NII-FTE 2,924 and noninterest income 965.
   - 1Q25 = first half minus 2Q25: expense 2,349−1,197 = 1,152; revenue 3,889−1,954 = 1,935 (NII 1,441 + noninterest income 494).
   - I checked these rows against docs/hban_ex992.
7. Ratios (noninterest expense / FTE revenue) and gaps:
| Quarter | Fifth Third | Huntington | Gap (pp) |
|---|---|---|---|
| 1Q25 | 1,304/2,136 = 61.049% | 1,152/1,935 = 59.535% | 1.514 |
| 2Q25 | 1,264/2,250 = 56.178% | 1,197/1,954 = 61.259% | 5.081 |
| 3Q25 | 1,267/2,306 = 54.944% | 1,246/2,151 = 57.927% | 2.983 |
| 4Q25 | 1,309/2,344 = 55.845% | 1,420/2,191 = 64.811% | 8.966 |
   - The smallest is 1Q25 at 1.514, which rounds to 1.5. Using the rounded ratios (61.0 − 59.5) also gives 1.5.

minimal_documents: D01 + D04.
- D03 can stand in for D04 for 2Q25–4Q25 (Tables 3 and 8), but it has no six-month 2025 data, so it cannot give Huntington's 1Q25.
- D02 can stand in for D01 for 2Q25–4Q25, but it has no year-to-date 2025 column, so it cannot give Fifth Third's 1Q25.
- D05 (KeyCorp) is not relevant. It mentions neither bank.

readings:
- (a) Only the quarters printed as standalone columns (2Q25–4Q25): narrowest is 3Q25 at 3.0 pp. This leaves out 1Q25, even though the documents let you derive it.
- (b) Using Huntington's reported ratio (59.0 / 57.4 / 64.2) against Fifth Third's FTE ratio: gaps are 2.8 / 2.5 / 8.4. A 1Q25 figure on Huntington's own definition, (2,327−1,186)/(3,947−2,012) = 1,141/1,935 = 58.97%, gives a 2.1 gap. Narrowest would be 2.5 pp (3Q25). This contradicts the question's stated definition.
- (c) Rounding: the source figures are rounded to the nearest $1M. Propagating ±0.5M through the 1Q25 subtractions puts the true 1Q25 gap between about 1.35 and 1.67. At the printed figures it is 1.5, and 1Q25 stays the narrowest quarter either way (next is 3.0).

gaps:
- Neither bank prints a standalone 1Q25 column in the packet, so 1Q25 comes from first-half minus 2Q figures. That relies on 2025 not being restated; I found no restatement note.
- I did not fully read:
  - D01 segment and average-balance pages (after line 1680, lines 805–1479 apart from grep hits).
  - Most of D02's middle slides.
  - D04 pages 4–9 and 11–17, and pages 19–21 and 23–26.
  - D05 beyond searches.
- No extraction problems; the decisive rows match the docs/ source text.

contaminated: no
