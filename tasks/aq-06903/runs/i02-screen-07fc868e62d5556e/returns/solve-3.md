# i02 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i02 blind solve 3")

Judged by the author against gold 5.2: RIGHT.

answer: 5.2 million ounces. BHP sold 8.68 Moz and Freeport's mines sold 3.5 Moz.
confidence: high

path:
1. Time window. BHP's financial year ends 30 June, so January–June 2026 is BHP's March 2026 quarter plus its June 2026 quarter. For Freeport it is the six months ended June 30, 2026.
2. BHP (D02, the year to 30 June 2026 review, Appendix 2 "Group production and sales summary – By commodity", silver block, line 310): "|Total|troy koz|4,127|4,341|4,393|5,147|3,990|17,871|14,773|21%|3,739|4,391|4,502|4,858|3,822|17,573|13,945|26%|". The Sales columns are Jun 2025, Sep 2025, Dec 2025, Mar 2026, Jun 2026, YTD Jun 2026, YTD Jun 2025, so Mar 2026 quarter sales = 4,858 koz and Jun 2026 quarter sales = 3,822 koz.
   - Components (lines 303 and 308): payable metal in concentrate 4,518 + refined silver 340 = 4,858, and 3,573 + 249 = 3,822.
   - Payable metal in concentrate by asset: Escondida 2,780 + Spence 375 + Copper South Australia 162 + Antamina 1,201 = 4,518. For June: 2,193 + 241 + 192 + 947 = 3,573.
   - The year-to-date figure checks out: 4,391 + 4,502 + 4,858 + 3,822 = 17,573.
   - D01 (the nine months to 31 March 2026 review, line 249) prints the same Mar 2026 quarter sales of 4,858, so the figure was not restated.
   - BHP total = 4,858 + 3,822 = 8,680 koz = 8.68 Moz.
3. Freeport (D04, the 2Q 2026 release, "Product Revenues and Production Costs" tables for the six months ended June 30, 2026):
   - U.S. copper mines (footnote b, line 1181): "silver sales of 0.8 million ounces ($69.40 per ounce average realized price)"
   - South America operations (footnote a, line 1393): "Includes silver sales of 1.6 million ounces ($69.33 per ounce average realized price)"
   - Indonesia operations (footnote a, line 1614): "Includes silver sales of 1.1 million ounces ($76.66 per ounce average realized price)..."
   - The Molybdenum mines tables mention no silver. Line 887 of D04 lists the four mining divisions: "U.S. copper mines, South America operations, Indonesia operations and Molybdenum mines."
   - Freeport total = 0.8 + 1.6 + 1.1 = 3.5 Moz.
   - Cross-check by quarter: in D04, 2Q26 is U.S. 0.4 (line 1075), South America 0.8 (line 1287) and Indonesia 0.6 (line 1497). In D03, 1Q26 is South America 0.8 (line 1009) and Indonesia 0.5 (line 1116). D03 gives no U.S. silver quantity (line 903: "Includes gold and silver product revenues and production costs"). The quarters agree with the six-month figures: 0.8+0.8 = 1.6 and 0.5+0.6 = 1.1, which implies U.S. 1Q = 0.4.
4. Difference: 8.680 − 3.5 = 5.18, which rounds to 5.2.

minimal_documents: D02 and D04.
- D01 can stand in for D02 only for the March quarter; it does not cover the June quarter.
- D03 cannot stand in for D04, because it has no 1Q U.S. silver quantity.

readings:
- Counting only BHP's "Payable metal in concentrate" and leaving out refined silver: 8,091 koz − 3.5 = 4.59, so 4.6. I think this is weaker, because the question asks about all silver BHP sold, and the total row includes refined silver.
- Cutting Escondida down to BHP's 57.5% interest. BHP reports Escondida on a 100% basis (D02 line 353: "Presented on a 100% basis. BHP interest in saleable production is 57.5%"). The adjusted BHP figure is about 6,566 koz, giving 6.567 − 3.5 = 3.07, so 3.1. This is not what BHP reported, so I rejected it.
- Using Freeport quarterly figures from D03 + D04 and missing the 1Q U.S. silver: 1.3 + 1.8 = 3.1, giving 5.58, so 5.6. This is wrong because it leaves out U.S. 1Q silver.
- Leaving out the U.S. mines (counting only Cerro Verde and PTFI): 8.68 − 2.7 = 5.98, so 6.0. Not defensible, because the U.S. copper mines explicitly report silver sales.

gaps:
- Freeport prints silver to only 0.1 Moz, so the true difference could be anywhere from about 5.03 to 5.33. Using the printed figures, the answer at the requested precision is 5.2. Revenue lines can't make this more precise, because "Other" and "Silver & Other" also include molybdenum, other metals and acid.
- Coverage: I searched all four documents for "silver", "ounces" and table headers. I read D01 lines 190–399, D02 lines 265–449, and the D04 U.S., South America and Indonesia six-month tables and the 2Q U.S. table. I located the D03 table headers and footnotes but did not read the full narratives.
- The sources are text files (method "text"). There are no PDFs or layout files, so the italics that mark restated BHP figures are not visible. The D01 and D02 March-quarter values match, though.

contaminated: no. There is a question.txt in the packet folder, which I did not open.
