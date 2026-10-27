# i03 strong-solver screen, solve 2 of 3 (blind-solver, fresh context; launch label "i03 blind solve 2")

Judged by the author against gold 1.0: RIGHT.

answer: US$1.0 per wet metric tonne (84.1 − 83.1, with both halves on the basis that includes the joint-venture effect)
confidence: high

path:
1. H1 2026 figure on the new basis. D02 (Q2 2026 results, filed 2026-07-15), text/D02.txt line 9, page 4 table: "Units H1 2026 H1 2025 Pilbara iron ore FOB, $/wmt 85.2 83.2". The same figures appear at line 13 (page 6): "Achieved average pricing1 in H1 2026 was $85.2 per wet metric tonne ($83.2 in H1 2025) on an FOB basis".
2. The basis changed in D02. The footnote appears both at line 9 and at line 13: "Pilbara average realised price excludes the impact of certain joint venture arrangements. Including these, realised prices for H1 2026 would have been $1.1/wmt lower (H1 2025, $0.7/wmt)."
3. H2 2025 figure on the old basis. D04 (Q4 2025 results, filed 2026-01-21), text/D04.txt line 9, page 4 table: "Units H1 2025 H2 2025 2025 2024 Pilbara iron ore FOB, $/wmt 82.5 83.1 82.8 89.6". D04's only footnote on this row is "Assuming 8% moisture". It has no joint-venture exclusion. The column order matches the original docs/ file.
4. D04 is on the basis that includes the joint-venture effect. D02 gives H1 2025 as 83.2 excluding that effect, and 83.2 − 0.7 = 82.5, which is exactly D04's H1 2025 figure. So D04's whole table, including H2 2025 = 83.1, includes the effect.
   - Check on D04's internal consistency: H1 2025 Pilbara shipments are 279.1 − (71.4 + 78.7) = 129.0 Mt (D04 full year; D03 Q3; D04 Q4). Weighting gives (82.5×129.0 + 83.1×150.1)/279.1 = 82.82, which matches the printed full-year 82.8.
5. Calculation:
   - H1 2026 including the effect = 85.2 − 1.1 = 84.1 $/wmt.
   - Like-for-like difference = 84.1 − 83.1 = 1.0 $/wmt.
   - Rounding: each printed input could be off by up to 0.05, so the true difference lies between about 0.85 and 1.15. Using the printed figures, the answer is 1.0.
6. The other like-for-like route cannot be computed. Putting H2 2025 on the new basis that excludes the effect would need H2 2025's joint-venture effect, which no document gives. D02 gives only the H1 2026 (1.1) and H1 2025 (0.7) amounts.

minimal_documents: D02 + D04. There is no alternative set. D01 (Q1 2026) and D03 (Q3 2025) contain no Pilbara realised prices. A grep for "achieved average pricing|average realised price|realised prices" matched only D02 and D04, and "certain joint venture" appears only in D02. D03 supplied only the Q3 2025 shipment figure used in the optional consistency check.

readings:
- Mixing bases (not like-for-like): 85.2 − 83.1 = 2.1. The question's "like-for-like" rules this out.
- Moving H2 2025 to the new basis by assuming its joint-venture effect equals H1 2025's 0.7: 85.2 − (83.1 + 0.7) = 1.4. The documents don't support this, because H2 2025's effect is not disclosed.
- Dry tonnes instead of wet (not requested): like-for-like 84.1/0.92 ≈ 91.4 − 90.3 = 1.1; mixed bases 92.6 − 90.3 = 2.3.
- The benchmark index moved from 62% Fe to 61% Fe from 1 January 2026 (D01 line 9, D02 line 9). That changes the index comparison, not the realised-price basis, so it does not affect the answer.

gaps:
- No figure for H2 2025 on the new basis (excluding the joint-venture effect) exists in the packet.
- The manifest lists every document as method "text" with pages null. There are no PDFs or layout files to inspect. The text in docs/ matches text/ for the decisive rows.
- Coverage:
  - Read in full: D01 and D02 lines 1–14 (pages 1–6), D03 lines 1–14 (pages 1–6) and D04 lines 1–20 (pages 1–9).
  - Covered only by keyword greps: the remaining lines of each document. The search terms were FOB, wet metric, wmt, like-for-like, realis, achieved average, joint venture, per wet and H2.
- I did not open question.txt in the packet folder; I used the question as supplied.

contaminated: no
