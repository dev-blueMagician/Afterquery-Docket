# i02 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i02 blind solve 3")

Judged by the author against gold 3.21%: RIGHT.

answer: 3.21% (global iron ore sales were about 347.9 Mt in the twelve months to 30 June 2026, against about 337.1 Mt in the twelve months to 30 June 2025)
confidence: high

path:
1. How D02 (the Q2 2026 review) defines the measure. Page 1 table: "Global iron ore sales4 (100% basis) Mt9 88.8 +5 % +17 % 164.5 +4 %". Footnote 4 says: "Includes all shipments from Pilbara and IOC, including those to our Portside trading business; excludes shipments from our Portside trading business. It also includes Simandou sales…". Footnote (g) on the operational data page (p.33–34) uses the same wording.
2. D02 quarterly figures. Operational data p.33 (text line 67), columns "Q2 2025 Q3 2025 Q4 2025 Q1 2026 Q2 2026 H1 2025 H1 2026": "Iron Ore Sales ('000 tonnes) (g) 84,414 88,369 95,027 75,681 88,847 158,562 164,528".
3. D03 (Q3 2025 review) supplies the 2024 quarters. Operational data p.32 (text line 65), columns "Q3 2024 Q4 2024 Q1 2025 Q2 2025 Q3 2025 9 MTHS 2024 9 MTHS 2025": "Iron Ore Shipments ('000 tonnes) 88,611 89,931 74,148 84,414 88,369 255,600 246,931 Iron Ore Sales ('000 tonnes) (d) 87,349 92,063 75,339 86,474 90,808…". Footnote (c): "Shipments includes material shipped to our portside trading facility in China…". Footnote (d): "Include Pilbara and IOC sales adjusted for portside trading movements and third party volumes sold."
4. Matching the two bases. D02's "sales" figures for Q2, Q3 and Q4 2025 (84,414; 88,369; 95,027) equal the "Iron Ore Shipments" row in D03 and D04. They do not match the old "(d) Sales" row (86,474; 90,808; 93,201). D01 shows the same for Q1 2025: 74,148 equals shipments. The 2024 quarters on D02's basis are therefore the shipments row: Q3 2024 = 88,611 and Q4 2024 = 89,931. D04 (p.33, line 67) repeats Q4 2024 = 89,931 and shows Simandou sales of 0 in every 2024–2025 column, so Simandou adds nothing to these quarters.
5. Cross-checks. The quarterly totals equal Pilbara + IOC (+ Simandou) shipments; for example Q2 2026 = 85,264 + 3,161 + 422 = 88,847, and Q3 2024 = 84,550 + 4,061 = 88,611. Some quarters differ by 1 kt because of rounding.
6. Calculation in kt:
   - Twelve months to June 2026 = 88,369 + 95,027 + 75,681 + 88,847 = 347,924. The last two quarters sum to 164,528, matching D02's H1 2026.
   - Twelve months to June 2025 = 88,611 + 89,931 + 74,148 + 84,414 = 337,104. The last two quarters sum to 158,562, matching D02's H1 2025.
   - Check using annual figures: D04's FY2025 shipments of 341,958 − 158,562 + 164,528 = 347,924. D04's FY2024 of 345,531 − H1 2024 (255,600 − 88,611 = 166,989) + 158,562 = 337,104.
   - Increase: (347,924 − 337,104) / 337,104 = 10,820 / 337,104 = 3.2097%, which rounds to **3.21%**.

minimal_documents: D02 + D03.
- D02 is the only source for Q2 2026 and for the definition.
- D03 is the only source for Q3 2024. D04 has Q4 2024 and FY2024 but neither H1 2024 nor Q3 2024.
- D04 can replace D03 for Q4 2024 only. D01 is redundant because D02 repeats its figures.

readings:
- Summing the components (Pilbara + IOC + Simandou) instead of using the printed totals gives 347,925 vs 337,102, which is 3.2106%. That is still 3.21%.
- Using the old "(d) Iron Ore Sales" figures for Q3 and Q4 2024, mixed with the new basis for H1 2025, gives a base of 337,974 and an increase of 2.94%. This does not measure the way the Q2 2026 review does.
- Using the old "(d)" figures for all four quarters to June 2025 gives a base of 341,225 and an increase of 1.96%. This is also inconsistent with the Q2 2026 basis.
- Using rounded Mt figures gives 3.20–3.23%, depending on where the rounding is applied. The '000 t data support 3.21%.

gaps:
- The packet has only text extractions (the manifest's method is "text" and pages are null). There are no PDFs or Dnn.layout.txt files, so I could not check any page images. The table rows came through extraction in order and the cross-sums agree.
- I read only these parts: the iron ore operational tables in D01–D04, the executive summaries of D01–D04, D01 pp.1–6 and D02 pp.1–4. Commodity sections not related to iron ore were not read.
- I did not open the packet's question.txt, following my instructions.

contaminated: no
