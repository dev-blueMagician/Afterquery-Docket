# i01 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i01 blind solve 1")

Judged by the author against gold 9%: RIGHT.

answer: 9%

confidence: high

path:
1. **What the 2025 basis is.** In 2025 Rio Tinto counted Queensland Alumina (QAL) at its 80% share. From 2026 it counts QAL at 100%.
   - D03 (Q3 2025 report, p.7, line 15) says the extra output from Rio Tinto taking 100% of QAL capacity "is excluded from the production tables in this report as QAL remains 80% owned by Rio Tinto and 20% owned by Rusal."
   - D04 (p.8, line 17) says the extra output "is excluded from the production tables in this report for 2025; however, we will be including the additional output from 2026 and reporting QAL on a 100% basis."
   - D02 (p.8, footnote 2) says "we have included QAL on a 100% basis from 2026." D01 (p.7) says the same thing.
2. **2024 halves, from D03 p.20 (line 41).** The columns run Q3 2024, Q4 2024, …, 2024 9 MTHS. The row reads "Alumina ('000 t) 1,770 1,992 1,921 1,815 1,888 5,310 5,623".
   - H1 2024 = 5,310 − 1,770 = **3,540**
   - H2 2024 = 1,770 + 1,992 = **3,762**
3. **2025 halves and reported H1 2026, from D02 p.21 (line 43).** The columns run Q2 2025, Q3 2025, Q4 2025, Q1 2026, Q2 2026, 2025 H1, 2026 H1. The row reads "Alumina ('000 t) 1,815 1,888 1,969 2,038 2,002 3,735 4,040".
   - H1 2025 = **3,735**
   - H2 2025 = 1,888 + 1,969 = **3,857**
4. **Putting H1 2026 on the 2025 basis.**
   - D02 p.22 (line 45), Rio Tinto share: "Queensland Alumina 80 % 699 697 710 839 859 1,384 1,698".
   - D02 p.28 (line 57), 100% operating data: "Queensland Alumina Refinery … 80 % 874 871 887 839 859 1,730 1,698".
   - So the 2025 share figures are 80% of the 100% figures (e.g. 699 ≈ 0.8 × 874), and the 2026 figures are the full 100%.
   - H1 2026 on the 2025 basis = 4,040 − 0.2 × 1,698 = **3,700.4**. By quarter: Q1 = 2,038 − 167.8 = 1,870.2 and Q2 = 2,002 − 171.8 = 1,830.2.
5. **Ranking ('000 t).** H1 2024 3,540 < H1 2026 3,700 < H1 2025 3,735 < H2 2024 3,762 < H2 2025 3,857.
   - Highest is H2 2025 and lowest is H1 2024.
   - 3,857 / 3,540 − 1 = 317 / 3,540 = **8.95%, which rounds to 9%**.
6. **Rounding check.** D04 p.21 (line 43) gives "7,303 7,593" for full-year 2024 and 2025. That makes H2 2025 = 7,593 − 3,735 = 3,858 and H1 2024 = 7,303 − 1,992 − 1,770 = 3,541. Summing the individual refinery rows gives H1 2024 ≈ 3,539 and H2 2025 ≈ 3,856. Every combination falls between 8.90% and 9.02%, so the answer is 9% in all cases.

minimal_documents: D02 + D03.
- D03 is the only source for Q3 2024 and the nine-month 2024 total, which are needed for H1 2024 and H2 2024.
- D02 is the only source for Q2 2026 and H1 2026. It also gives Q3 and Q4 2025, H1 2025, and the QAL rows at both 80% and 100%.
- D01 and D04 are redundant. The Q4 2025 figure and the basis statement also appear in D01 and D04, and D04 provides the full-year cross-check.

readings:
- If you take the 2026 figures as reported (QAL at 100%), H1 2026 = 4,040 becomes the highest. The answer would then be 4,040 / 3,540 − 1 = 14.1%, or 14%. The question's wording ("the basis Rio Tinto used to report alumina production in 2025") rules this out.
- Adjusting with the 80%/20% split gives the same result whether done per quarter or on the half-year total.
- No other defensible reading changes which half is highest or lowest, or the 9% result.

gaps:
- Q1 2024 and Q2 2024 are not given separately. H1 2024 is worked out as the nine-month 2024 total minus Q3 2024.
- The packet has only .txt sources (the manifest says "method": "text"), with no PDFs and no layout files, so I could not check any page images.
- Unread material:
  - D02: lines 21–42, 46–56, and 58 onward.
  - D03: lines 4–14, 16–40, 44–54, and 56 onward, which includes line 7, the markets commentary on alumina prices.
  - D04: lines 18–42 except line 39, 46–56, and 58 onward.
  - These cover copper, iron ore, projects and similar sections. Every alumina table row and every QAL statement was read.
- D01 was read in full.

contaminated: no. Only the manifest and text/Dnn.txt were read; question.txt in the packet was not opened.
