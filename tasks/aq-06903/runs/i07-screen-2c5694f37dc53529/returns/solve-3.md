# i07 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i07 blind solve 3")

Judged by the author against gold 1.9: RIGHT.

answer: 1.9 percentage points. Freeport is about 74.8% and BHP about 72.9%.
confidence: high

path:
1. Time window. Freeport's year is the calendar year, so January-June 2026 is its "Six Months Ended June 30, 2026". BHP's year ends 30 June, so January-June 2026 is its March 2026 quarter plus its June 2026 quarter (the second half of FY26).
2. Freeport, D04 (text/D04.txt), "SELECTED OPERATING DATA (continued) / Six Months Ended June 30", copper sales column for 2026:
   - lines 471-473: "|Consolidated|1,448|1,831|1,367|c|", "|Less noncontrolling interests|385|583|345|", "|Net|1,063|1,248|1,022|"
   - Line 87 matches: "Sales, excluding purchases ... 1,367".
   - Cross-check: the mine rows add up (639 + 493 + 235 = 1,367). D03 for Q1 (lines 419-421: sales 657 / 155 / 502) plus D04 for Q2 (lines 419-421: 710 / 190 / 520) gives 1,367 / 345 / 1,022.
   - Morenci partners are already removed from the reported figure. Footnote a (line 493): "Amounts are net of Morenci's joint venture partners' undivided interests."
   - Freeport's own share = 1,022 / 1,367 = 74.762%.
3. BHP, D02 (text/D02.txt), Appendix 2, "Total copper" sales columns:
   - Group total (line 290): Mar 2026 quarter 468.7 kt, Jun 2026 quarter 483.3 kt, so 952.0 kt.
   - Escondida (line 350): 302.2 + 305.4 = 607.6 kt. Line 341: "BHP interest 57.5%". Line 353: "1 Presented on a 100% basis. BHP interest in saleable production is 57.5%."
   - The other copper assets:
     - Pampa Norte/Spence: "BHP interest 100%", 52.3 + 53.7 = 106.0 kt.
     - Copper South Australia: 100%, 69.2 + 88.3 = 157.5 kt.
     - Carajás: 100%, 1.7 + 0 = 1.7 kt (sold 2 April 2026).
     - Antamina: "BHP interest 33.75%", 43.3 + 35.9 = 79.2 kt. It has no "Presented on a 100% basis" footnote, so I treat it as already BHP's share.
   - The pieces add back to the total: 607.6 + 106.0 + 157.5 + 79.2 + 1.7 = 952.0.
   - D01 (lines 229 and 286) shows the same March 2026 quarter figures (468.7 total, 302.2 Escondida), so nothing was restated.
   - Minority shareholders' part of Escondida = 0.425 × 607.6 = 258.23 kt. BHP's own part = 952.0 − 258.23 = 693.77 kt.
   - BHP's own share = 693.77 / 952.0 = 72.875%.
   - Check from year totals: FY26 sales 1,905.4 − (448.9 + 504.5) = 952.0, and Escondida 1,231.7 − (296.4 + 327.7) = 607.6.
4. Difference: 74.762 − 72.875 = 1.887, which rounds to 1.9. Rounding each share to one decimal first gives 74.8 − 72.9 = 1.9, so the answer holds either way.

minimal_documents: D02 + D04.
- D02 alone has both BHP quarters and the 57.5% Escondida footnote.
- D04 alone has Freeport's six-month figures.
- D03 + D04 is a valid replacement for D04 on the Freeport side (add the two quarters).
- D01 can replace D02 only for BHP's March quarter. D02 is still needed for the June quarter.

readings:
- If Antamina were read as a 100% figure (partners holding 66.25%): BHP = (693.77 − 52.47) / 952.0 = 67.36%, difference 7.4. The documents don't support this, because only Escondida (and Jimblebar iron ore) carry the 100%-basis footnote.
- If Freeport's purchased copper (47 Mlb, footnote c) were counted as Freeport's own sales: 1,069 / 1,414 = 75.60%, difference 2.7. This is not the reported sales figure, which excludes purchases.
- If Morenci were grossed up to include its partners' 28%: 1,022 / (1,367 + 236 × 28/72) = 70.06%, difference −2.8. This contradicts "reported" sales, which are already net of those partners.
- If the two quarterly ratios were averaged instead of pooling the six months: Freeport (76.41 + 73.24)/2 = 74.82, BHP (72.60 + 73.14)/2 = 72.87, difference 1.95, which could become 2.0. This method is wrong for a six-month share; pooling gives 1.9.

gaps:
- No document states outright that Antamina is reported at BHP's share. I inferred it from the missing 100%-basis footnote. The documents also don't name Escondida's other shareholders; only the 57.5% interest is given.
- The packet's docs/ files are .txt, not PDFs, so there were no original pages to check. Italics (BHP's restatement marker) are lost in the text. Comparing D01 with D02 showed no change to the March 2026 copper figures.
- Unread except by keyword search:
  - D02 after line 509 (resources/reserves appendix).
  - Most of D01 outside lines 208-232 and the matching lines.
  - D03 apart from lines 394-443.
  - D04 apart from lines 1-125, 395-504 and 875-884 (the financial schedules were searched only).
- I did not open question.txt in the packet.

contaminated: no
