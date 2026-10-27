# i07 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i07 blind solve 1")

Judged by the author against gold 1.9: RIGHT.

answer: 1.9 percentage points. Freeport's own share is about 74.76% and BHP's is 72.875%, so the gap is 1.887 pp.
confidence: high

path:
1. Freeport, Jan–Jun 2026 (D04, "SELECTED OPERATING DATA (continued), Six Months Ended June 30", copper Sales column, 2026):
   - "Consolidated|...|1,367|c" means 1,367 Mlb consolidated sales.
   - "Less noncontrolling interests|385|583|345" means 345 Mlb belong to minority holders.
   - "Net|1,063|1,248|1,022" means 1,022 Mlb belong to FCX.
   - Footnote c says these sales "exclude purchased copper of 47 million pounds".
   - Footnote a says Morenci (72%) "Amounts are net of Morenci's joint venture partners' undivided interests", so no partner share sits inside the reported figure.
   - The Summary Operating Data shows "Sales, excluding purchases|...|1,367" for the six months.
   - Cross-check with D03 (1Q 2026): 657 / 155 / 502. Adding D04 2Q (710 / 190 / 520) gives 1,367 / 345 / 1,022, which matches.
   - Share: 1,022 / 1,367 = 74.762%.
2. BHP, Jan–Jun 2026 (D02 Appendix 2). This is the quarters ended Mar 2026 and Jun 2026, i.e. H2 FY26. Sales columns:
   - Group "Total|kt" copper sales: 468.7 + 483.3 = 952.0 kt. Check: 448.9 + 504.5 + 468.7 + 483.3 = 1,905.4, the full-year FY26 total.
   - Escondida "BHP interest 57.5%", footnote "Presented on a 100% basis. BHP interest in saleable production is 57.5%." Total copper sales: 302.2 + 305.4 = 607.6 kt.
   - Spence "BHP interest 100%": 52.3 + 53.7 = 106.0 kt.
   - Copper SA "BHP interest 100%": 69.2 + 88.3 = 157.5 kt.
   - Carajás "BHP interest 100%": 1.7 + 0 (sold 2 April 2026) = 1.7 kt.
   - Antamina "BHP interest 33.75%": 43.3 + 35.9 = 79.2 kt. This has no "100% basis" footnote. The basis note (D02 p.25, same text in D01 p.11) says "sales volumes from subsidiaries are reported on a 100% basis; production and sales volumes from equity accounted investments and other operations are reported on a proportionate consolidation basis". Antamina is listed as a non-operated asset, so its reported figure is already BHP's share. Samarco works the same way: 5.9 Mt reported against "11.8 Mt (100% basis)".
   - The asset figures add up: 607.6 + 106.0 + 157.5 + 79.2 + 1.7 = 952.0. Each quarter also checks: 468.7 and 483.3.
   - Partners' share of Escondida: 0.425 × 607.6 = 258.23 kt.
   - BHP's own share: (952.0 − 258.23) / 952.0 = 693.77 / 952.0 = 72.875%, which comes out exactly.
   - D01's Mar 2026 quarter figures (302.2, 52.3, 69.2, 43.3, 1.7, total 468.7) are the same as D02's, with no restatement.
3. Difference: 74.762 − 72.875 = 1.887, which rounds to 1.9 pp. Rounding each share first (74.8 − 72.9) also gives 1.9.

minimal_documents: D02 + D04. Both are needed: only D02 has BHP's Jun 2026 quarter, and only D04 has Freeport's 2Q and six-month figures. D01 (BHP Mar quarter) and D03 (FCX 1Q) are redundant because their figures are repeated in D02 and D04. There is no single-document alternative.

readings:
- Count purchased copper in Freeport's sales: (1,022 + 47) / (1,367 + 47) = 75.60%, giving 2.7 pp. I rejected this because the reported sales figure and the minority-interest split are both given excluding purchases.
- Average the two quarterly shares instead of pooling the six months. Freeport: (76.41% + 73.24%) / 2 = 74.82%. BHP: (72.60% + 73.14%) / 2 = 72.87%. This gives 2.0 pp. The question asks about the January–June period as a whole, so pooling fits it better.
- Treat Antamina's 79.2 kt as a 100% figure and keep only 33.75% for BHP: BHP share 67.36%, giving 7.4 pp. The documents' proportionate-basis note contradicts this.

gaps:
- No PDF or layout files exist; docs/ holds only .txt files (manifest method "text", pages null). The tables read cleanly and their totals check.
- Read in full: D01, and D02 (its JORC Appendix 3 only skimmed, iron ore and not relevant).
- Partly read: D03 lines 395–444 plus a search for minority-interest and sales terms; D04 lines 1–135 and 395–495 plus the same search. The rest of D03 and D04 was not read.
- The bundle never names Antamina as equity-accounted outright. The proportionate treatment rests on the basis note, the missing 100% footnote and the non-operated listing.

contaminated: no
