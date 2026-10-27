# i01 strong-solver screen, solve 2 (blind-solver, claude-opus-5-5, effort max, fresh context)

Raw return as received 2026-10-19:

answer: about US$85.7 per tonne (calculated value 85.696) for the quarter ended 30 June 2025 (Q4 FY25)

confidence: high

path:
1. Full-year FY25 price. D02 (year to 30 June 2026), energy coal panel at line 176: "Average realised price US$104.28/t ê3% FY25 US$107.80/t".
2. Nine-month price to March 2025. D01 (nine months to 31 March 2026), line 129: "Average realised price US$99.04/t ê15% YTD Mar FY25 US$115.99/t".
3. Which sales count. The price footnote in D02 (line 218) says "Export sales only. Includes energy coal sales from steelmaking coal mines". D01's footnote (line 157) says the same but uses "thermal coal". So the weight is NSWEC export sales plus BMA energy coal sales.
4. Sales volumes in kt (D02 lines 484 and 489; D01 lines 419 and 424):
   - NSWEC export, quarter to June 2025: 3,554. Nine months to March 2025: 10,015. FY25: 13,569.
   - BMA energy coal (BHP 50% share; hard coking coal plus energy coal adds to the share total, e.g. 4,831 + 199 = 5,030): quarter to June 2025: 199. Nine months to March 2025: 114. FY25: 313.
   - Combined: quarter 3,753; nine months 10,129; FY25 13,882. The parts add up (10,129 + 3,753 = 13,882).
5. Calculation, with kt × US$/t giving US$ thousands:
   - FY25: 107.80 × 13,882 = 1,496,479.60
   - Nine months to March 2025: 115.99 × 10,129 = 1,174,862.71
   - Quarter to June 2025: 1,496,479.60 − 1,174,862.71 = 321,616.89
   - Price: 321,616.89 ÷ 3,753 = 85.6960 US$/t, which rounds to **85.7**.
   - Rounding check: the inputs are rounded to the cent, so the result could be off by about ±0.03 (range 85.66–85.73). It still rounds to 85.7.
6. Checks that BHP uses this weighting (my calculations; the reported figures are in D02 lines 203–206):
   - Second half FY26: (105.61 × (3,935+10) + 117.74 × (4,224+383)) ÷ 8,552 = 112.146. BHP reports 112.15. Using NSWEC exports alone gives 111.89, and counting BMA at 100% gives 112.38.
   - Full year FY26: (99.04 × 11,839 + 117.74 × 4,607) ÷ 16,446 = 104.278. BHP reports 104.28. NSWEC exports alone give 104.01.
   - Year-on-year change: 117.74 ÷ 85.696 = +37.4%, which matches D02's "v Q4 FY25 37%". The NSWEC-only answer of 84.72 would imply +39%.

minimal_documents: D01 + D02. D01 is the only source of the 115.99 nine-month price. D02 is the only source of the 107.80 FY25 price, and it also has every volume needed (nine-month volumes = FY25 minus the June quarter: 13,569 − 3,554 = 10,015 and 313 − 199 = 114). D01 repeats the June-quarter and nine-month volumes, so D02's volumes can be swapped for D01's. Neither document can be dropped. D03 and D04 (Freeport-McMoRan) do not mention BHP or coal.

readings:
- NSWEC export sales only, leaving out BMA energy coal despite the footnote: 301,098.35 ÷ 3,554 = 84.7. This contradicts BHP's reported +37% and its second-half and full-year FY26 weighting.
- Including domestic sales (which goes against "Export sales only"): NSWEC total plus BMA gives 351,497.37 ÷ 4,125 = 85.2; NSWEC total only gives 84.3.
- Working back from the rounded percentage instead of volumes: 117.74 ÷ 1.37 = 85.9 (anything from about 85.6 to 86.3 fits the rounded 37%). This does not follow the instruction to use prices and volumes.

gaps:
- BMA's energy coal sales are not labelled export or domestic. Including them rests on the footnote, and the second-half and full-year FY26 figures confirm it.
- BHP describes its prices as "provisional, unaudited estimates".
- The packet has text extracts only (manifest method "text", pages null), so I checked no original PDF pages. Italic markers for restated figures are lost in the text, but the June 2025 quarter volumes are identical in D01 and D02.
- I did not read the D02 Ministers North JORC appendix (about lines 509–870) closely, and I only searched D03 and D04 (no BHP, coal or thermal hits).
- I did not open the packet's question.txt.

contaminated: no
