# i04 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i04 blind solve 2")

Judged by the author against gold +0.41%: RIGHT.

answer: +0.41%. On the Q2 2026 review's basis, global iron ore production (100%) went from 344,058 kt in 2024 to 345,469 kt in 2025.

confidence: high (medium on whether the question means exactly this basis; see readings)

path:
1. The Q2 2026 review (D02) has no calendar-2024 or full-year 2025 columns. Its iron ore table headers are "Q2 2025 Q3 2025 Q4 2025 Q1 2026 Q2 2026 H1 2025 H1 2026". Every "2024" in D02 is a project date. So 2025 has to be built from D02's periods, and 2024 has to come from D03 or D04.
2. D02 line 67 (source docs/...q2-2026...txt line 65), "Global Iron Ore Totals": "Iron Ore Production (‘000 tonnes) (f) 87,980 88,102 95,670 82,828 87,070 161,697 169,898". That gives H1 2025 = 161,697, Q3 2025 = 88,102 and Q4 2025 = 95,670.
3. D02's basis includes Simandou. Line 67 reads "Simandou iron ore production ('000 tonnes) (d) 0 0 2,271 570 660 0 1,230". Footnote (f) says "For Simandou, it represents ore ready for train loading at the SimFer mine gate". On page 7 D02 says: "2.3 Mt (100% SimFer) of crushed iron ore ... was produced in 2025 and was recorded for the first time in Q4 2025".
4. 2025 on the D02 basis: 161,697 + 88,102 + 95,670 = 345,469 kt.
   - Check by component: Pilbara 153,514 + 84,104 + 89,674 = 327,292; IOC 8,182 + 3,998 + 3,725 = 15,905; Simandou 2,271. Total 345,468. The 1 kt gap is rounding in the H1 figure, which D02 itself flags as possible.
5. 2024 comes from D04 line 67: "Global Iron Ore Totals Iron Ore Production ('000 tonnes) 90,798 73,716 87,980 88,102 93,399 344,058 343,197". The columns are Q4 24, Q1–Q4 25, 2024 and 2025, so 2024 = 344,058. That equals Pilbara 327,972 + IOC 16,086. Simandou 2024 = "0" in D04, so 2024 is the same on either basis.
   - D03 line 65 agrees: 9M 2024 253,260 + Q4 2024 90,798 = 344,058.
6. Change: (345,469 − 344,058) / 344,058 = 1,411 / 344,058 = +0.4101%. Using 345,468 gives +0.4098%. Both round to +0.41%.
7. Why D04's own 2025 total differs: 343,197 = Pilbara 327,292 + IOC 15,905, which leaves out Simandou. D04 footnote (a) says "This, therefore, excludes Simandou production in 2025". D02's restated Q4 2025 figure is 95,670 = 93,399 + 2,271. D01 line 65 shows the same restated Q4 2025 figure of 95,670.

minimal_documents:
- D02 + D04: D04 gives full-year 2024 directly.
- Alternative: D02 + D03, with 2024 = 9M 2024 + Q4 2024.
- D01 + D04 or D03 would give the same arithmetic, since D01 lists all four 2025 quarters on the new basis. But the question names D02 as the basis.
- D04 alone gives +0.41% only if you manually add Simandou's 2,271, which D04 itself excludes.
- No single document is enough.

readings:
- If you use D04's printed full-year totals, which exclude Simandou: (343,197 − 344,058) / 344,058 = −861 / 344,058 = −0.25%. That conflicts with "on the basis of the Q2 2026 review", whose global total includes Simandou.
- On a strict "D02 only" reading, the question can't be answered: D02 has no calendar-2024 data.
- Rio Tinto-share basis (not what was asked): 2024 287,676 (D04) vs 2025 135,956 + 74,168 + 80,515 = 290,639 (D02), which is +1.03%.

gaps:
- No document prints a full-year 2025 global total on the Q2 2026 basis. It has to be summed from H1 2025 + Q3 + Q4.
- Italics that mark restated figures are lost in the text extraction. This doesn't matter here: there is no PDF, and the decisive rows match the docs/ source files.
- What I read:
  - D02: all of it.
  - D04: lines 1–16 and 41–72; lines 17–40 (copper, aluminium, lithium and projects sections) unread.
  - D03: line 65 only.
  - D01: line 65 plus grep hits on lines 3, 13, 15, 17 and 41.
- I didn't open question.txt.

contaminated: no
