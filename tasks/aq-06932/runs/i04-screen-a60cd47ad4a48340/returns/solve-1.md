# i04 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i04 blind solve 1")

Judged by the author against gold +0.41%: RIGHT.

answer: +0.41%

confidence: high

path:
1. The question asks for global iron ore production (100% basis), calendar 2024 to calendar 2025, using the Q2 2026 review's figures. The answer is a signed percentage to 2 dp. Units are '000 wet tonnes.
2. D02 (Q2 2026 review, text/D02.txt line 67, "Global Iron Ore Totals Iron Ore Production ('000 tonnes) (f) 87,980 88,102 95,670 82,828 87,070 161,697 169,898"). The columns are Q2 2025, Q3 2025, Q4 2025, Q1 2026, Q2 2026, H1 2025, H1 2026.
   - 2025 = H1 2025 + Q3 2025 + Q4 2025 = 161,697 + 88,102 + 95,670 = **345,469**.
   - Footnote (f) counts Simandou as global production: "For Simandou, it represents ore ready for train loading at the SimFer mine gate".
   - Q4 2025 reconciles from its parts: Pilbara 89,674 + IOC 3,725 + Simandou 2,271 = 95,670.
   - Adding the 2025 parts instead gives Pilbara 327,292 + IOC 15,905 + Simandou 2,271 = 345,468. The 1 kt gap is rounding; the printed H1 2025 is 161,697, while the parts sum to 161,696.
3. D02 has no 2024 iron ore data. Its tables only go back to Q2 2025/H1 2025, and every "2024" mention in it is a non-production date.
4. 2024 comes from D04 (Q4 2025 review, line 67, columns Q4 2024 | Q1–Q4 2025 | 2024 | 2025): "Global Iron Ore Totals Iron Ore Production ('000 tonnes) 90,798 73,716 87,980 88,102 93,399 344,058 343,197". That gives 2024 = **344,058**.
   - The 2024 Simandou column is 0, so 2024 is on the same basis as D02.
   - D03 (Q3 2025, line 65, columns Q3 2024, Q4 2024, Q1–Q3 2025, 9M 2024, 9M 2025) gives the same total: 9M 2024 253,260 + Q4 2024 90,798 = 344,058.
5. Why D04's 2025 total (343,197) differs from D02's:
   - D04's Q4 2025 global figure of 93,399 equals Pilbara 89,674 + IOC 3,725, so it leaves out Simandou.
   - D04 footnote (a), lines 43 and 51: "This, therefore, excludes Simandou production in 2025 which represents crushed ore at the mine gate."
   - D01 (line 13) and D02 (p.7, footnote 2) say: "2.3 Mt (100% SimFer) of crushed iron ore … was produced in 2025 and was recorded for the first time in Q4 2025".
   - D01 (line 65) already shows the restated Q4 2025 figure of 95,670.
6. Calculation:
   - (345,469 − 344,058) / 344,058 = 1,411 / 344,058 = 0.4101% → **+0.41%**
   - Using 345,468 instead: 1,410 / 344,058 = 0.4098% → +0.41%
   - Using Mt figures: (161.7 + 88.1 + 95.7 − 344.1) / 344.1 = +0.41%

minimal_documents: D02 + D04. The alternative is D02 + D03, which gives the same 2024 figure.
- D02 alone is not enough because it has no 2024 data.
- D01 has the same restated 2025 quarters (sum 345,468) but no 2024 data. It could replace D02 numerically, but the question names the Q2 2026 review.
- D04 alone gives −0.25% on its own reported basis. It reaches +0.41% only if you add its separately listed Simandou row (2,271) yourself, which goes against its own footnote.

readings:
- Using D04's as-reported 2025 total, which excludes Simandou: (343,197 − 344,058) / 344,058 = −861 / 344,058 = **−0.25%**. The "on the basis of the Q2 2026 review" wording points away from this, because D02's global total includes Simandou.
- Excluding Simandou from D02's 2025 to make it "like-for-like" with 2024: 343,198 − 344,058 = −860, giving −0.25%. This contradicts D02's own definition of global production.
- No other defensible reading changes the 2-dp result: the quarter-sum and half-year-sum versions both give +0.41%.

gaps:
- The docs are plain text (manifest method "text"; no PDFs in docs/), so I couldn't check the italics D02 uses to mark restated figures. The restatement is still fully reconciled by the Simandou row.
- Unread material: I read D02 in full. For D01, D03 and D04 I read only the iron ore operational table lines (D01 line 65, D04 line 67, D03 line 65 via search), D01 line 13, and search hits for global iron ore, Simandou, restatement and 2024 terms. Other sections of D01, D03 and D04 were not read in full.
- No 2024 restatement appears in any document. D01 and D02 have no 2024 iron ore columns.

contaminated: no. I did not open question.txt, notes or metadata, and nothing leaked. I worked only from text/manifest.json and text/D01–D04 under D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06932\runs\i04-screen-a60cd47ad4a48340\solver-1\text\
