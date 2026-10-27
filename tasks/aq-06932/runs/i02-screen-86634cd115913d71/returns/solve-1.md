# i02 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i02 blind solve 1")

Judged by the author against gold 3.21%: RIGHT.

answer: 3.21%

confidence: high

path:
1. **How the Q2 2026 review measures it.** D02 is the Q2 2026 review. Its exec-summary footnote 4 and the footnote to the operational-data row "Iron Ore Sales" (p.33–34) both say: "Includes all shipments from Pilbara and IOC, including those to our Portside trading business; excludes shipments from our Portside trading business. It also includes Simandou sales". That row is on a 100% basis, wmt.
2. **Five quarters from D02, page 33.** The row reads "Iron Ore Sales ('000 tonnes) (g) 84,414 88,369 95,027 75,681 88,847 158,562 164,528". The columns are Q2 2025, Q3 2025, Q4 2025, Q1 2026, Q2 2026, H1 2025 and H1 2026.
   - Check on Q2 2026: Pilbara 85,264 + IOC 3,161 + Simandou 422 = 88,847.
   - Check on the H1 2026 total: 75,681 + 88,847 = 164,528.
   - The exec summary agrees: 88.8 Mt, "+5%" YoY, which matches 88,847/84,414.
3. **The 2025 reviews use a different label.** In D03 (Q3 2025, p.32) and D04 (Q4 2025, p.33) there are two rows:
   - "Iron Ore Shipments", footnote (c): "Shipments includes material shipped to our portside trading facility in China".
   - "Iron Ore Sales (d)", footnote (d): "Include Pilbara and IOC sales adjusted for portside trading movements and third party volumes sold".
   - The "Shipments" row is the D02 measure. Its overlapping quarters equal D02's figures exactly (Q2 2025 84,414; Q3 2025 88,369; Q4 2025 95,027), and D01's Q1 2026 review restates 2025 the same way (74,148 / 84,414 / 88,369 / 95,027). The old "Sales (d)" values (86,474 / 90,808 / 93,201) do not match. D01's "+2%" for Q1 2026 also only works on this basis: 75,681/74,148.
4. **Q3 and Q4 2024 from D03, p.32.** The row reads "Iron Ore Shipments ('000 tonnes) 88,611 89,931 74,148 84,414 88,369 255,600 246,931", with columns Q3 2024, Q4 2024, Q1 2025, Q2 2025, Q3 2025, 9M 2024 and 9M 2025.
   - Q3 2024 = Pilbara 84,550 + IOC 4,061 = 88,611.
   - D04 repeats Q4 2024 as 89,931.
   - Simandou sales were 0 throughout 2024 and 2025 (D04: "Simandou iron ore sales ... 0 0 0 0 0 0 0", which includes the 2024 full-year column).
   - I checked these rows in the docs/ source files and they match the extracted text.
5. **Calculation.**
   - Twelve months to 30 June 2026: 88,369 + 95,027 + 164,528 = 347,924 kt.
   - Twelve months to 30 June 2025: 88,611 + 89,931 + 158,562 = 337,104 kt.
   - Cross-check using D04 annual totals: 2025 total 341,958 − 158,562 + 164,528 = 347,924. 2024 total 345,531 − (255,600 − 88,611) + 158,562 = 337,104.
   - Result: 10,820 / 337,104 = 3.2097%, which rounds to **3.21%**.
   - Rounding check: rebuilding each quarter from its Pilbara, IOC and Simandou parts gives 347,925 / 337,102, or 3.2106%. That also rounds to 3.21%.

minimal_documents: D02 + D03.
- D03 is the only source for Q3 2024.
- D04 can stand in for D03's Q4 2024 figure only, not for Q3 2024.
- D01 is not needed, but it confirms that the definition changed and how 2025 was restated.

readings:
- Using the old D03/D04 "Iron Ore Sales (d)" values for Q3 and Q4 2024 (87,349 + 92,063), combined with D02's H1 2025: base 337,974, giving **2.94%**. This mixes two different measures.
- Using the whole old-basis "Sales (d)" series for the base year (Q3 2024 to Q2 2025 = 341,225): **1.96%**. This compares two different measures.
- Leaving out Simandou (Pilbara + IOC only): 347,502 / 337,104, giving **3.08%**. This contradicts D02's definition, which includes Simandou.

gaps:
- No document states a twelve-month figure directly, so the answer is computed.
- Nothing in the packet explicitly announces the change in the "sales" definition. I inferred it from the footnotes and the restated figures matching.
- What I read:
  - D02: all of it.
  - D01: exec summary (line 3) and iron ore operational data (line 65).
  - D03: exec summary and lines 62–67.
  - D04: exec summary and line 67.
  - Searches across all four files for "global iron ore", definition/restatement wording and twelve-month wording.
- Not read: the remaining sections of D01, D03 and D04 (other commodities, projects, iron ore narrative pages). Searches found no restatement of the iron ore figures in them.
- The docs are text files (no PDFs or layout files). The rows I relied on parse cleanly, with 7 values for 7 columns.

contaminated: no
