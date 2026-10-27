# i04 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i04 blind solve 3")

Judged by the author against gold 27: RIGHT.

answer: 27 US cents per pound. BHP's US$6.21/lb is 27 cents above the six-month LME average of US$5.94/lb, which is the mean of Freeport's quarterly LME averages of $5.83 and $6.05.
confidence: high

path:
1. **BHP's average realised copper price for January to June 2026 is US$6.21/lb.**
   - Source: D02, the BHP operational review for the year ended 30 June 2026, Appendix 1 "Average realised prices", line 203.
   - Header row: "|Average realised pricesi|Q4 FY26|v Q3 FY26|v Q4 FY25|H2 FY26|v H1 FY26|v H2 FY25|FY26|v FY25|"
   - Copper row: "|Copper (US$/lb)ii, iii|6.53|11%|47%|6.21|18%|38%|5.74|35%|"
   - The columns line up: the FY26 column (5.74) matches the copper section at line 145, "Average realised price US$5.74/lb é35% FY25 US$4.25/lb".
   - Period: line 97 says "the second half of FY26 (H2 FY26)", and FY26 is the "year ended 30 June 2026". So H2 FY26 is 1 January to 30 June 2026.
2. **Freeport's LME average for the first quarter of 2026 is $5.83/lb.**
   - Source: D03, the Freeport 1Q 2026 earnings release, Derivative Instruments section, line 737: "quoted LME monthly average settlement copper prices, which averaged $5.83 per pound in first-quarter 2026".
   - Line 735 confirms the period is "the three months ended March 31, 2026".
3. **Freeport's LME average for the second quarter of 2026 is $6.05/lb.**
   - Source: D04, the Freeport 2Q 2026 earnings release, Derivative Instruments section, line 835: "quoted LME monthly average settlement copper prices, which averaged $6.05 per pound in second-quarter 2026".
   - D04 prints no six-month LME average. Its only LME mentions are lines 833, 835 and 871, and line 871 is a spot price ("$6.30 per pound on July 22, 2026"). D04 also does not repeat the first-quarter LME figure.
4. **Six-month LME average is $5.94/lb.** Each quarterly figure is an average of three monthly averages, so the six-month average is the simple mean: (5.83 + 6.05) / 2 = 5.94.
5. **The excess is 27 cents.** 6.21 − 5.94 = 0.27 US$/lb, or 27 US cents per pound.
   - Rounding check: the printed figures allow a range of about 26 to 28 cents. The computed value is 27.

minimal_documents: D02, D03 and D04.
- D01 cannot stand in for D02. It only has Q3 FY26 at 5.86 and the nine months to March at 5.47, not the H2 figure.
- D03 and D04 are each the only source of their quarter's LME average, and neither BHP document mentions LME.

readings:
- **Built from BHP's quarterly prices:** (5.86 + 6.53) / 2 = 6.195, so 6.195 − 5.94 = 0.255, about 25.5 cents (26 or 25 depending on rounding). This is weaker than the main answer, because BHP prints H2 FY26 = 6.21 directly as a sales-weighted figure.
- **Weighting the quarters by trading days:** the documents give no trading-day counts. My own outside rough count gives about 5.938, which still leaves the answer at 27 cents. That count is outside knowledge and is not used.
- **Other Freeport figures:** single-quarter comparisons (38 cents against Q1, 16 cents against Q2) and spot settlement prices ($5.99 on April 22, $6.30 on July 22) don't fit "average … over those six months".

gaps:
- Freeport reports no six-month LME average, so step 4 is my own calculation from the two quarterly figures.
- I did not read the documents in full. I read these sections, plus all four documents searched for LME, London Metal, COMEX, "averaged $x.xx per pound", realised/realized and the half-year period labels:
  - D01 lines 140–189
  - D02 lines 190–249, plus search hits at lines 53, 97, 145 and 212
  - D03 lines 728–757
  - D04 lines 1–140 and 780–879
- The sources are .txt files, with no PDFs or layout files in the packet, so no original pages could be inspected. No extraction problems were seen in the rows that decide the answer.
- I did not read the packet's question.txt.

contaminated: no — I received only the workspace root, packet path and question, with no answer or hints.
