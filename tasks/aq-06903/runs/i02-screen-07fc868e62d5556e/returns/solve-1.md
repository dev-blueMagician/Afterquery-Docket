# i02 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i02 blind solve 1")

Judged by the author against gold 5.2: RIGHT.

answer: 5.2 million ounces (BHP 8.680 Moz minus Freeport 3.5 Moz = 5.18, which rounds to 5.2)
confidence: high

path:
1. The window is January to June 2026. For BHP (financial year ends 30 June) this is the Mar 2026 quarter plus the Jun 2026 quarter, i.e. H2 FY26. For Freeport it is the "Six Months Ended June 30, 2026".
2. BHP, D02 (FY26 operational review), Appendix 2 group production and sales summary. Column headers run Production, then Sales, each covering quarters Jun 2025, Sep 2025, Dec 2025, Mar 2026, Jun 2026, then YTD Jun 2026, YTD Jun 2025 and Var.
   - Line 310, silver Total row (troy koz), Sales half: "3,739|4,391|4,502|4,858|3,822|17,573|13,945|26%". So Mar 2026 quarter = 4,858 and Jun 2026 quarter = 3,822.
   - The components add up. Line 303, payable metal in concentrate sales: Mar 2026 = 4,518, Jun 2026 = 3,573. Line 308, refined silver sales: 340 and 249. 4,518 + 340 = 4,858 and 3,573 + 249 = 3,822. By asset for Jun 2026: Escondida 2,193 + Spence 241 + Copper South Australia 192 + Antamina 947 = 3,573.
   - The YTD total is consistent: 4,391 + 4,502 + 4,858 + 3,822 = 17,573.
   - D01 (nine months to March 2026), line 249, Sales Total for Mar 2026 = 4,858 (4,518 + 340). This matches D02, so the March quarter was not restated.
   - BHP total for Jan–Jun 2026: 4,858 + 3,822 = 8,680 troy koz = 8.680 Moz.
   - D02 line 875: sales volumes from subsidiaries are "reported on a 100% basis", and equity-accounted operations (Antamina) on a proportionate basis. I used the figures as BHP reports them.
3. Freeport, D04 (2Q 2026 release), six-month product revenue tables:
   - U.S. Copper Mines, "Six Months Ended June 30, 2026", footnote b (line 1181): "silver sales of 0.8 million ounces ($69.40 per ounce average realized price)".
   - South America Operations, six months 2026, footnote a (line 1393): "Includes silver sales of 1.6 million ounces ($69.33 per ounce…)".
   - Indonesia Operations, six months 2026, footnote a (line 1614): "Includes silver sales of 1.1 million ounces ($76.66 per ounce…)".
   - The Molybdenum mines report no silver.
   - Freeport total: 0.8 + 1.6 + 1.1 = 3.5 Moz.
   - Cross-check by quarter:
     - Q2 2026 in D04: US 0.4 (line 1075), South America 0.8 (line 1287), Indonesia 0.6 (line 1497).
     - Q1 2026 in D03: South America 0.8 (line 1009), Indonesia 0.5 (line 1116). The D03 US footnote (line 903) gives no quantity: "Includes gold and silver product revenues and production costs." The implied US Q1 is 0.8 − 0.4 = 0.4.
     - Quarter sum: 1.7 + 1.8 = 3.5, which agrees with the six-month figures.
4. Result: 8.680 − 3.5 = 5.18, which is 5.2 to one decimal place.

minimal_documents: D02 + D04.
- D02 alone has both BHP quarters; D01 only has the March quarter and cannot replace D02.
- D04 is needed because D03 has no Q1 US silver quantity, so D03 cannot replace D04's six-month US figure.
- D01 and D03 are redundant and only confirm the figures.

readings:
- Counting only BHP's "payable metal in concentrate" sales and leaving out refined silver from Olympic Dam: (4,518 + 3,573) = 8.091 Moz, minus 3.5 = 4.59, so 4.6. This is less natural, because the question asks what silver BHP sold and BHP reports a Total row.
- Reading "Freeport's mines" as the U.S. copper mines only: 8.68 − 0.8 = 7.9. This is weak, because Freeport's mines also include the South America and Indonesia operations.
- These are misreadings, not alternatives: production instead of sales (5,147 + 3,990 = 9.137 Moz, giving 5.6), or BHP's full FY26 year to date (17.573 Moz, giving 14.1).
- Not adopted: adjusting BHP's figures to its ownership shares (e.g. Escondida at 57.5%), since the question asks what BHP reported.
- The Antamina silver streaming deal (US$4.3 bn upfront, D01 line 70; D02 line 120) is a financing cash flow. It adds no silver sales volume.

gaps:
- Freeport's silver figures are printed rounded to 0.1 Moz, so the true total could be anywhere from 3.35 to 3.65. Using the printed figures gives 5.18, which rounds to 5.2.
- D02 says italics mark restated figures; plain text loses italics. This does not matter here because D01 and D02 agree for the March quarter.
- There are no PDF or layout files in the packet (all sources are .txt; the manifest lists method "text").
- I searched all four documents for silver, ounces, koz, Moz and stream, and read the relevant BHP Appendix 2 tables and the Freeport product revenue tables. I did not read the rest of the narrative in full.
- I did not open question.txt.

contaminated: no
