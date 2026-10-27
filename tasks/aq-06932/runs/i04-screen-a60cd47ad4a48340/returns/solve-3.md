# i04 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i04 blind solve 3")

Judged by the author against gold +0.41%: RIGHT.

answer: +0.41%

confidence: high

path:
1. **2025 on the Q2 2026 review's basis (D02).** The text extraction is the same as the docs/ original, which I checked by grep.
   - Page 33, "Global Iron Ore Totals", with columns Q2 2025, Q3 2025, Q4 2025, Q1 2026, Q2 2026, H1 2025 and H1 2026: "Iron Ore Production ('000 tonnes) (f) 87,980 88,102 95,670 82,828 87,070 161,697 169,898". The footer says: "The data represents production and sales on a 100% basis unless otherwise stated."
   - Definition (page 1, footnote 3 to "Global iron ore production3 (100% basis)"): "Iron Ore production for Pilbara operations and Iron Ore Company of Canada (IOC) refers to saleable production … For Simandou, it represents ore ready for train loading at the SimFer mine gate".
   - Simandou table, page 7, footnote 2: "2.3 Mt (100% SimFer) of crushed iron ore … was produced in 2025 and was recorded for the first time in Q4 2025".
   - Q4 2025 of 95,670 is Pilbara 89,674 + IOC 3,725 + Simandou 2,271 (page 33 rows).
   - Calendar 2025 = H1 2025 + Q3 2025 + Q4 2025 = 161,697 + 88,102 + 95,670 = **345,469 kt**.
2. **2024 (D04, the Q4 2025 review).** D02 contains no figure for calendar 2024.
   - Page 33, with columns Q4 2024, Q1–Q4 2025, 2024 and 2025: "Global Iron Ore Totals Iron Ore Production ('000 tonnes) 90,798 73,716 87,980 88,102 93,399 344,058 343,197". So 2024 = **344,058 kt**, which is Pilbara 327,972 + IOC 16,086 + Simandou 0.
   - Cross-check from D03 (Q3 2025 review, page 32): 9 months of 2024 (253,260) + Q4 2024 (90,798) = 344,058.
3. **Calculation.** (345,469 − 344,058) / 344,058 = 1,411 / 344,058 = +0.4101%, which rounds to **+0.41%**.
   - Summing the quarters instead gives 345,468 kt (D01 page 32: 73,716 + 87,980 + 88,102 + 95,670; or D04's 343,197 + 2,271). That is 1,410 / 344,058 = +0.4098%, still +0.41%.
   - The two 2025 totals differ by 1 kt because H1 2025 is 161,697 while Q1 + Q2 sum to 161,696; the report notes that "Production figures are sometimes more precise than the rounded numbers shown".

minimal_documents: D02 + D04. D02 + D03 also works, with 2024 = 9 months of 2024 + Q4 2024. D01 carries the same restated 2025 quarters (Q4 2025 = 95,670) and could stand in for D02's numbers, but the question names D02.

readings:
- **Annual totals as first published in D04: −0.25%.** D04 gives 2025 as 343,197 and says this "excludes Simandou production in 2025 which represents crushed ore at the mine gate". That gives −861 / 344,058 = −0.2502%, or −0.25%. It contradicts the question's instruction to use the Q2 2026 review; the sign flips because D02 includes Simandou in Q4 2025.
- **Rio Tinto share (not the requested 100% basis): +1.03%.** D02 gives 135,956 + 74,168 + 80,515 = 290,639. Against D04's 2024 figure of 287,676, that is +1.03%. On D04's 2025 share figure of 289,616, it would be +0.67%.

gaps:
- D02 has no 2024 baseline, so a second document is needed for it (D04, or D03).
- Italic restatement flags are lost in the plain-text sources, which only matter as confirmation and do not change the answer. The packet has no PDFs.
- I read D02 and D04 in full. For D01 and D03 I read only the iron ore operational data and summary/definition lines found by search: D01 lines 3, 13, 41 and 63–65; D03 lines 41 and 63–65.
- I did not open question.txt.

contaminated: no
