# i02 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i02 blind solve 2")

Judged by the author against gold 5.2: RIGHT.

answer: 5.2 million ounces (BHP 8.68 Moz minus Freeport 3.5 Moz = 5.18, which rounds to 5.2)
confidence: high

path:
1. The window is calendar January to June 2026. For BHP that is the March 2026 quarter (Jan–Mar) plus the June 2026 quarter (Apr–Jun) of its FY26. For Freeport (FCX) it is the "Six Months Ended June 30, 2026". The question asks for silver sales, not production, in million ounces to one decimal.
2. BHP, D02 (FY26 operational review), group production and sales summary, Silver "Total" row, line 310. The sales block reads: "|Total|troy koz|...|3,739|4,391|4,502|4,858|3,822|17,573|13,945|26%|". The sales columns are Jun25, Sep25, Dec25, Mar26, Jun26, FY26 YTD, FY25 YTD and Var.
   - Mar 2026 quarter = 4,858 koz. This is payable metal in concentrate of 4,518 (line 303) plus refined silver of 340 (line 308).
   - Jun 2026 quarter = 3,822 koz, which is 3,573 + 249.
   - Check: 4,391 + 4,502 + 4,858 + 3,822 = 17,573, matching the FY26 YTD figure. The concentrate split for Jun Q also adds up: Escondida 2,193 + Spence 241 + Copper South Australia 192 + Antamina 947 = 3,573.
   - Cross-check with D01 (nine-month review), line 249: the Mar 2026 quarter total is the same 4,858 ("...|4,391|4,502|4,858|13,751|..."), so that quarter was not restated.
   - BHP Jan–Jun 2026 = 4,858 + 3,822 = 8,680 koz = 8.68 Moz.
3. Freeport, D04 (2Q26 release). Freeport gives no consolidated silver figure, only per-operation footnotes. All three six-month 2026 footnotes:
   - U.S. Copper Mines, "Six Months Ended June 30, 2026", footnote b (line 1181): "silver sales of 0.8 million ounces ($69.40 per ounce average realized price)".
   - South America Operations, six months 2026, footnote a (line 1393): "Includes silver sales of 1.6 million ounces ($69.33 per ounce...)".
   - Indonesia Operations, six months 2026, footnote a (line 1614): "Includes silver sales of 1.1 million ounces ($76.66 per ounce...)".
   - The Molybdenum Mines table has no silver.
   - Total = 0.8 + 1.6 + 1.1 = 3.5 Moz.
4. Quarterly cross-check against D03 (1Q26) plus D04 (2Q26):
   - South America: 0.8 (D03 line 1009) + 0.8 (D04 line 1287) = 1.6.
   - Indonesia: 0.5 (D03 line 1116) + 0.6 (D04 line 1497) = 1.1.
   - U.S.: the 1Q26 footnote in D03 (line 903) only says "Includes gold and silver product revenues and production costs", with no volume. 2Q26 is 0.4 (D04 line 1075), which implies about 0.4 for 1Q. This agrees with the six-month figures.
5. Difference: 8.680 − 3.5 = 5.18, which rounds to 5.2.

minimal_documents: D02 + D04.
- D02 alone gives both BHP quarters. D01 can replace D02 only for the March quarter; it does not cover June.
- D04 alone gives Freeport's six-month figures. D03 + D04 cannot replace them by summing quarters, because D03 has no U.S. silver volume for 1Q26.

readings:
- Counting only BHP's payable silver in concentrate (leaving out refined silver): 4,518 + 3,573 = 8,091 koz, giving 4.6. This is less defensible because the question asks for silver as a whole and BHP prints a group Total row.
- Summing Freeport's quarterly footnotes and leaving out the undisclosed U.S. 1Q26 figure: Freeport = 3.1, giving 5.6. This is flawed because D04 gives the full six-month figures.
- Using BHP's FY26 year to date (July 2025–June 2026), 17,573 koz, gives 14.1. That does not match "January and June 2026".
- Rounding: Freeport prints each figure to 0.1 Moz, so the true total could lie between about 3.35 and 3.65 Moz. That puts the exact difference between about 5.03 and 5.33. On the printed figures the answer is 5.2.

gaps:
- No PDFs are in the packet; the manifest lists the sources as text with no page markers, so I could not check the original pages. The extraction also drops italics, which BHP uses to flag restated figures. I compared the March-quarter numbers across D01 and D02 instead, and they match.
- I did not read the documents end to end. I ran a case-insensitive search for "silver" across all four text files and reviewed every hit. I also searched D04 for ounce-related terms and D02 for stream, troy, koz and Moz.
- Freeport's figures appear to be consolidated (100%) volumes, and BHP's group summary counts Escondida at 100%. I made no ownership-share adjustments, because the question asks for reported sales.
- As instructed, I did not read question.txt.

contaminated: no
