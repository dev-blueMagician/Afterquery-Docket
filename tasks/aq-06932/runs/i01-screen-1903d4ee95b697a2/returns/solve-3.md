# i01 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i01 blind solve 3")

Judged by the author against gold 9%: RIGHT.

answer: 9%. On the 2025 basis (Queensland Alumina Limited (QAL) at Rio Tinto's 80% share), the highest half-year is H2 2025 at 3,857 kt and the lowest is H1 2024 at 3,540 kt. 3,857 / 3,540 − 1 = 8.95%, which rounds to 9%.

confidence: high

path:
1. What the 2025 basis is:
   - D03 p.7, alumina footnote: Rio Tinto took 100% of QAL capacity under a tolling agreement, but "This additional output is excluded from the production tables in this report as QAL remains 80% owned by Rio Tinto and 20% owned by Rusal."
   - D04 p.8 says the same for 2025 and adds "we will be including the additional output from 2026 and reporting QAL on a 100% basis."
   - D01 p.7: "QAL now included at 100% (from 80% in 2025)". D02 p.1 note 6: "QAL production now included on a 100% basis."
   - So the 2025 basis is QAL at 80%. 2024 used the same basis: the Q3 2024 QAL share of 693 against 866 at 100% is 80%.

2. H1 and H2 2024 (D03 p.21, "Rio Tinto total alumina production", '000 t):
   - Printed: Q3 2024 = 1,770; Q4 2024 = 1,992; 9 months of 2024 = 5,310.
   - H1 2024 = 5,310 − 1,770 = 3,540.
   - H2 2024 = 1,770 + 1,992 = 3,762.
   - Cross-check with D04 p.22, where full-year 2024 is 7,303: H1 2024 = 7,303 − 1,770 − 1,992 = 3,541. Adding up the individual refineries gives 3,539.

3. H1 and H2 2025 (D02 p.22):
   - Q1 2025 = 1,921; Q2 2025 = 1,815; Q3 2025 = 1,888; Q4 2025 = 1,969; printed H1 2025 = 3,735.
   - H1 2025 = 3,735, or 3,736 from adding the quarters.
   - H2 2025 = 1,888 + 1,969 = 3,857. Cross-check with D04's full-year 2025 of 7,593: 7,593 − 3,735 = 3,858.

4. H1 2026 restated to the 2025 basis:
   - D02 p.22 prints total alumina of 2,038 (Q1 2026), 2,002 (Q2 2026) and 4,040 (H1 2026). It prints the QAL row as 839, 859 and 1,698.
   - These QAL figures equal the 100% operational row on D02 p.28 ("Queensland Alumina Refinery … 839 859 … 1,698"), which confirms 2026 is reported at 100%.
   - Restated: 4,040 − 0.2 × 1,698 = 3,700.4. Quarter by quarter: (2,038 − 167.8) + (2,002 − 171.8) = 3,700.4. Adding up the refineries gives 3,699.4.

5. Ranking ('000 t): H2 2025 3,857 > H2 2024 3,762 > H1 2025 3,735 > H1 2026 (restated) 3,700 > H1 2024 3,540.
   - Highest is H2 2025; lowest is H1 2024.
   - 3,857 / 3,540 = 1.0895, so 8.95%.
   - Every rounding combination gives 8.92% to 9.01% (for example 3,858/3,541 and 3,858/3,539), so 9% in all cases.

6. I checked the decisive rows (total alumina, the QAL share row and the QAL 100% row) in both text/ and docs/ for all four documents, and they are identical.

minimal_documents: D02 + D03.
- D03 is the only source for Q3 2024, which H1 and H2 2024 need. It also states the 2025 basis.
- D02 is the only source for Q2 and H1 2026, including the QAL 100% figures. It also gives Q3 and Q4 2025.
- D04 duplicates full-year 2024, Q4 2024, Q3 and Q4 2025, and the basis statement. D01 duplicates the basis statement and Q1 2026. Neither can replace D02 or D03.

readings:
- If you don't restate 2026 and take the reported H1 2026 of 4,040 kt (QAL at 100%) as the highest: 4,040 / 3,540 − 1 = 14.1%, so 14%. The question's wording ("on the basis Rio Tinto used to report alumina production in 2025") rules this out.
- Using the rounded "Mt" headline figures (for example 2.0 Mt or 7.6 Mt) instead of the kt tables is too coarse for this question. I did not use it.
- I found no other defensible reading. The lowest half-year is H1 2024 whether or not 2026 is restated.

gaps:
- Q1 and Q2 2024 are not reported separately in the packet, so H1 2024 has to be derived (9-month 2024 minus Q3 2024). Rounding moves it by about 1 kt, which does not change the answer.
- The packet contains no PDFs, only text, so there were no PDF pages to check. The extraction is complete and the text/ and docs/ rows match.
- I read all four documents in full.

contaminated: no. The packet contains a question.txt, which I did not open. I worked only from the question text I was given.
