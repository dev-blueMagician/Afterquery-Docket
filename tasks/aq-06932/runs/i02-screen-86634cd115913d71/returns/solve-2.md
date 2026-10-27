# i02 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i02 blind solve 2")

Judged by the author against gold 3.21%: RIGHT.

answer: 3.21%. Sales of 347,924 kt in the twelve months to 30 June 2026, against 337,104 kt in the twelve months to 30 June 2025 (up 10,820 kt, or 3.2097%).
confidence: high

path:
1. How the Q2 2026 review measures it (D02, page 1, footnote 4 to "Global iron ore sales4 (100% basis)"): "Includes all shipments from Pilbara and IOC, including those to our Portside trading business; excludes shipments from our Portside trading business. It also includes Simandou sales". D01, page 1, footnote 4 uses the same wording.
2. This is the older "shipments" measure under a new name. The Q3 and Q4 2025 reviews (D03, D04) showed two separate global rows: "Iron Ore Shipments" and "Iron Ore Sales (d)". Note (d) says "Include Pilbara and IOC sales adjusted for portside trading movements and third party volumes sold". In the quarters the reports share, D02's "Iron Ore Sales" row exactly equals the old "Iron Ore Shipments" row: Q2 2025 84,414; Q3 2025 88,369; Q4 2025 95,027. It does not match the old (d) row (86,474 / 90,808 / 93,201). The Rio Tinto-share rows follow the same pattern: "Pilbara iron ore shipments" 68,120 / 71,441 / 78,702 in D03/D04 reappear as "Pilbara iron ore sales" in D01/D02.
3. D02, page 33, "Global Iron Ore Totals … Iron Ore Sales ('000 tonnes) (g) 84,414 88,369 95,027 75,681 88,847 158,562 164,528". The columns are Q2 2025, Q3 2025, Q4 2025, Q1 2026, Q2 2026, H1 2025 and H1 2026. Twelve months to 30 June 2026 = 88,369 + 95,027 + 75,681 + 88,847 = 347,924 kt. Checks:
   - Q1 + Q2 2026 = 164,528, which matches the reported H1 2026.
   - Q2 2026 = Pilbara 85,264 + IOC 3,161 + Simandou 422 = 88,847.
4. D03, page 32 (columns Q3 2024, Q4 2024, Q1 2025, Q2 2025, Q3 2025, 9M 2024, 9M 2025): "Iron Ore Shipments ('000 tonnes) 88,611 89,931 74,148 84,414 88,369 255,600 246,931". Twelve months to 30 June 2025 = 88,611 + 89,931 + 74,148 + 84,414 = 337,104 kt. Checks:
   - Q1 + Q2 2025 = 158,562, which matches D02's H1 2025.
   - Q3 2024 = Pilbara 84,550 + IOC 4,061 = 88,611.
   - There were no Simandou sales before Q2 2026 (D04 Simandou sales row is all 0).
5. Cross-checks using D04, page 33 ("Iron Ore Shipments … 89,931 74,148 84,414 88,369 95,027 345,531 341,958"):
   - H2 2024 = FY2024 345,531 − (9M 2024 255,600 − Q3 2024 88,611) = 178,542. This equals Q3 2024 + Q4 2024.
   - FY2025 341,958 − H1 2025 158,562 + H1 2026 164,528 = 347,924.
6. Result: 347,924 / 337,104 − 1 = 10,820 / 337,104 = 0.0320969, which is 3.21%.
7. The key rows were checked against the original docs/*.txt sources (D03 line 63, D04 line 65, D02 line 65, D01 line 63). They are the same.

minimal_documents: D02 + D03.
- D02 is the only source for Q2 2026 and also defines the measure.
- D03 is the only document with a Q3 2024 column.
- D04 cannot replace D03: it has Q4 2024 and FY2024 but no Q3 2024 or H1 2024.
- D01 cannot replace D02: it has no Q2 2026.
- D01 and D04 only corroborate the figures and the rename.

readings:
- (a) Taking D03's old "Iron Ore Sales (d)" row for the earlier period: 87,349 + 92,063 + 75,339 + 86,474 = 341,225. Against 347,924 that gives +1.96%. This mixes two definitions and goes against the question's "as Rio Tinto's second-quarter 2026 operations review does", so I reject it.
- (b) Using the old (d) measure for both periods can't be computed, because no old-basis figures are published for Q1 or Q2 2026.
- No other defensible reading found.

gaps:
- The docs are text-only (manifest method "text", pages null). There are no PDFs or layout files, so the italic restatement markers mentioned in D02 can't be seen. However, all overlapping quarterly figures match across D01 to D04, so no restatement shows up.
- Unread material: D02 was read in full. For D01, D03 and D04 I read only the iron-ore operational-data pages and the summary-table lines (line 3), plus targeted searches; the rest of those documents is unread.
- I did not open question.txt.

contaminated: no
