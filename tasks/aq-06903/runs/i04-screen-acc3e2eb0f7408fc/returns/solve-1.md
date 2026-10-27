# i04 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i04 blind solve 1")

Judged by the author against gold 27: RIGHT.

answer: 27 US cents per pound. BHP's realised price was US$6.21/lb and the LME average was about US$5.94/lb, so the gap is US$0.27/lb.
confidence: high

path:
1. BHP's year runs to 30 June. D02 is titled "Operational review for the year ended 30 June 2026" and D01 is "Operational review for the nine months ended 31 March 2026". So FY26 runs from 1 July 2025 to 30 June 2026, and H2 FY26 covers January to June 2026. D02 line 97 confirms the label: "the second half of FY26 (H2 FY26)".
2. BHP's realised copper price for H2 FY26 is reported directly. D02, Appendix 1 "Average realised prices", line 203: "|Copper (US$/lb)ii, iii|6.53|11%|47%|6.21|18%|38%|5.74|35%|". The column headers on line 202 are Q4 FY26 | v Q3 FY26 | v Q4 FY25 | H2 FY26 | v H1 FY26 | v H2 FY25 | FY26 | v FY25, so H2 FY26 is US$6.21/lb. A cross-check holds: the FY26 figure of 5.74 matches line 145, "Average realised price US$5.74/lb".
3. Freeport's LME average for Q1 2026 is in D03, Derivative Instruments, line 737: "...based on quoted LME monthly average settlement copper prices, which averaged $5.83 per pound in first-quarter 2026".
4. Freeport's LME average for Q2 2026 is in D04, Derivative Instruments, line 835: "...based on quoted LME monthly average settlement copper prices, which averaged $6.05 per pound in second-quarter 2026".
5. Freeport does not report an LME average for the full six months. In D04, LME is mentioned only on lines 833, 835 and 871. Line 833 is a six-month sales-mix sentence with no price, and line 871 is a single-day price ("$6.30 per pound on July 22, 2026"). Searches for "averaged" and "London" found no six-month LME figure. The six-month figure therefore has to be calculated from the two quarters.
6. Six-month LME average = (5.83 + 6.05) / 2 = 5.94 US$/lb. Weighting the two quarters by trading days makes little difference: about 63 and 61 days gives about 5.938. That day count comes from the calendar, not the packet. Because each quarterly figure is rounded to the cent, the true average lies between about 5.935 and 5.945, which keeps the result at 27 cents to the nearest cent.
7. 6.21 − 5.94 = 0.27 US$/lb, which is 27 US cents per pound.

minimal_documents: D02, D03, D04. None of them can be swapped out. D04 has no Q1 LME figure and D03 has no Q2 figure, and only D02 gives a BHP price covering January to June. D01 is not needed; it only adds Q3 FY26 = 5.86 (line 150).

readings:
- Rebuilding BHP's half from its quarters as a plain average, (5.86 [D01] + 6.53 [D02]) / 2 = 6.195, gives about 25.5 cents. This is weaker than using the reported 6.21. BHP's prices are sales-weighted, and the period is reported directly.
- Using Freeport's own realised price for the first six months (D04 line 88, $6.04) instead of LME would give 17 cents. That does not answer the question, which asks for the LME settlement average.
- Using BHP's full-year FY26 price of 5.74 would cover the wrong period.
No other reasonable reading changes the answer of 27 cents.

gaps: Freeport reports no six-month LME average, so 5.94 is calculated from the two quarterly averages, and both are rounded to the cent. The BHP prices are marked provisional and unaudited (D02 note i). I did not read the documents in full. I read D02 lines 1–70, 138–149 and 190–249; D01 lines 140–164; D03 lines 728–757; and D04 lines 100–159 and 825–879. I also searched all four text files for realised/realized, LME/London Metal/COMEX, averaged, and the price-per-pound and H2/half-year wording, and searched docs/ for LME. Every document is plain text with no PDF pages (the manifest lists method "text" and pages null), so nothing was lost in extraction.

contaminated: no. Only the workspace path, packet path and question were supplied. I did not open question.txt or anything outside text/ and docs/.
