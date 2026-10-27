# i01 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i01 blind solve 2")

Judged by the author against gold 9%: RIGHT.

answer: 9%

confidence: high

path:
1. **What 2025 basis means.** In 2025 Rio Tinto counted Queensland Alumina (QAL) at its 80% equity share. From 2026 it counts QAL at 100%.
   - D03 p.7, footnote 1: "This additional output is excluded from the production tables in this report as QAL remains 80% owned by Rio Tinto and 20% owned by Rusal."
   - D04 p.8, footnote 1: "This additional output is excluded from the production tables in this report for 2025; however, we will be including the additional output from 2026 and reporting QAL on a 100% basis."
   - D01 p.7: "QAL now included at 100% (from 80% in 2025)".
   - D02 p.8, footnote 2: "we have included QAL on a 100% basis from 2026."
   - 2024 also used QAL at 80% (D03 p.21 row "Queensland Alumina 80 %"), so 2024 and 2025 are on the same basis. Only 2026 needs adjusting.

2. **2024 quarters (D03 p.20 production summary, '000 t).** Row "Alumina ('000 t) 1,770 1,992 1,921 1,815 1,888 5,310 5,623", with columns Q3 24, Q4 24, Q1 25, Q2 25, Q3 25, 9M 2024, 9M 2025. The refinery table on D03 p.21 matches.
   - H1 2024 = 5,310 − 1,770 = **3,540**
   - Cross-check: D04 p.21 gives FY2024 of 7,303, so 7,303 − 1,770 − 1,992 = 3,541. Summing the refinery rows gives 3,539.
   - H2 2024 = 1,770 + 1,992 = **3,762**

3. **2025.** D04 p.21 row "Alumina ('000 t) 1,992 1,921 1,815 1,888 1,969 7,303 7,593". D02 p.21 shows the same quarters and prints "2025 H1" as 3,735.
   - H1 2025 = 1,921 + 1,815 = **3,736** (3,735 as printed)
   - H2 2025 = 1,888 + 1,969 = **3,857** (or 7,593 − 3,735 = 3,858)

4. **H1 2026 (D02 p.22).** Row "Queensland Alumina 80 % 699 697 710 839 859 1,384 1,698" and "Rio Tinto total alumina production 1,815 1,888 1,969 2,038 2,002 3,735 4,040".
   - The operational data on D02 p.28 shows the QAL 100% figure for H1 2026 is also 1,698, so 2026 now counts QAL in full.
   - On the 2025 basis: 4,040 − 0.2 × 1,698 = **3,700.4**. Adding up the refinery rows gives 3,699.4. Going quarter by quarter, Q1 is 2,038 − 0.2 × 839 = 1,870.2 and Q2 is 2,002 − 0.2 × 859 = 1,830.2, which also totals 3,700.4.

5. **Ranking.** H2 2025 (3,857) > H2 2024 (3,762) > H1 2025 (3,736) > H1 2026 adjusted (~3,700) > H1 2024 (3,540).
   - (3,857 − 3,540) / 3,540 = 317 / 3,540 = **8.955%, which rounds to 9%**.
   - Rounding variants: 3,858/3,540 gives 8.98%, 3,857/3,541 gives 8.95%, and 3,858/3,539 gives 9.01%. All round to 9%.
   - H1 2026 adjusted is far from both extremes. It would only become the highest if the adjustment were under 183 kt; the actual adjustment is about 340 kt.

6. I checked the decisive rows against the docs/*.txt sources ("Rio Tinto total alumina production…" and the QAL operational rows). They match the text/ extracts.

minimal_documents: D02 + D03.
- D03 is the only document with Q3 2024 or 9M 2024, so it is needed to split 2024 into halves. It also states the 2025 QAL-80% basis.
- D02 is the only document with Q2 2026 and H1 2026, plus the QAL 1,698 figure. It also gives Q3 and Q4 2025.
- D04 is redundant here. Its FY2024 figure gives an alternative H1 2024 of 3,541, and it restates the basis.
- D01 is redundant here. Its Q1 2026 data is already inside D02's H1 2026 columns.

readings:
- **Not adjusting 2026 (ignores the stated basis).** H1 2026 at 4,040 becomes the highest: 500 / 3,540 = 14.1%, so 14%. The question explicitly asks for the 2025 basis, so I reject this reading.
- **Restating every half at QAL 100% (not what the question asks).**
  - H1 2024 = 3,540 + 0.2 × (2,463 − 866) = 3,859.4
  - H2 2025 = 3,857 + 0.2 × (871 + 887) = 4,208.6
  - The ratio is 1.0905, so the answer is still 9%.
- **Any half-year totals produced by rounding.** All give 9%.

gaps:
- No document gives Q1 or Q2 2024 separately, or H1 2024 directly, so I derived it by subtraction. The resulting 3,539–3,541 range does not change the answer.
- No document gives a like-for-like figure for 2026 at QAL 80%, so the adjustment is my own calculation: 20% of QAL's 100% output.
- Not read: the non-alumina sections of D01, D02 and D03 (iron ore, copper, projects and so on). Every "alumina" match across all four documents was reviewed. D04 was read in full.
- I did not read question.txt in the packet, because question files are off-limits.

contaminated: no
