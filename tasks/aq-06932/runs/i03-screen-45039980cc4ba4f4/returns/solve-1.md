# i03 strong-solver screen, solve 1 of 3 (blind-solver, fresh context; launch label "i03 blind solve 1")

Judged by the author against gold 1.0: RIGHT.

answer: 1.0 (US$ per wet metric tonne; $84.1 for H1 2026 on the like-for-like basis minus $83.1 for H2 2025)

confidence: high

path:
1. H1 2026 figure (D02, Q2 2026 release, filed 2026-07-15).
   - Page 4, "Average realised prices achieved for our major commodities": "Units H1 2026 H1 2025 Pilbara iron ore FOB, $/wmt 85.2 83.2 Pilbara iron ore1 FOB, $/dmt 92.6 90.5".
   - Footnote 1 to that table: "Pilbara average realised price excludes the impact of certain joint venture arrangements. Including these, realised prices for H1 2026 would have been $1.1/wmt lower (H1 2025, $0.7/wmt)."
   - Page 6 repeats the figure: "Achieved average pricing1 in H1 2026 was $85.2 per wet metric tonne ($83.2 in H1 2025) on an FOB basis", with the same footnote.
2. H2 2025 figure (D04, Q4 2025 release, filed 2026-01-21).
   - Page 4 table: "Units H1 2025 H2 2025 2025 2024 Pilbara iron ore FOB, $/wmt 82.5 83.1 82.8 89.6 Pilbara iron ore1 FOB, $/dmt 89.7 90.3 90.0 97.4".
   - The only footnote is "Assuming 8% moisture." There is no wording about excluding joint venture arrangements.
3. Working out which basis D04 uses.
   - D04 gives H1 2025 as $82.5/wmt. D02 restates H1 2025 as $83.2 on the new basis, which excludes the JV arrangements.
   - 83.2 - 82.5 = 0.7, which is exactly the JV impact D02 gives for H1 2025.
   - So D04's figures, including H2 2025 at $83.1, include the JV arrangements. D02's $85.2 does not.
4. Putting H1 2026 on the same basis as D04: 85.2 - 1.1 = $84.1/wmt.
5. Difference: 84.1 - 83.1 = $1.0/wmt.
6. Checks.
   - The $/dmt figures match the 8% moisture assumption: 85.2/0.92 = 92.6; 83.1/0.92 = 90.3; 82.5/0.92 = 89.7.
   - Weighting D04's half-year figures by D04's consolidated Pilbara shipments (H1 2025: 62,537 + 69,985 kt; H2 2025: 73,431 + 80,586 kt) gives about 82.8, which matches the printed full-year 2025 figure.
   - All inputs are printed to 0.1, so the true unrounded difference could lie somewhere in roughly 0.85-1.15. On the printed figures it is 1.0.
7. Other documents. D01 (Q1 2026) and D03 (Q3 2025) give no Pilbara realised prices. They only contain index prices, sales mix and FOB-share data.

minimal_documents: D02 + D04, both needed. D02 is the only source for the H1 2026 price, the JV adjustment and the restated H1 2025 figure. D04 is the only source for H2 2025. Neither D01 nor D03 can stand in for either.

readings:
- Not like-for-like: 85.2 - 83.1 = 2.1. This mixes the two bases, so the question's "like-for-like" wording rules it out.
- Comparing on the new basis that excludes the JV arrangements: this needs H2 2025's JV impact, which the packet does not give, so it can't be computed. Guesses would give different answers:
  - assuming H2 2025's impact equals H1 2025's $0.7 gives 85.2 - 83.8 = 1.4;
  - assuming it equals H1 2026's $1.1 gives 1.0.
  Neither assumption is supported by the documents.
- Per dry tonne: 84.1/0.92 = about 91.4 against 90.3 gives about 1.1 $/dmt. The question asks for wet tonnes, so this does not apply.

gaps:
- No document restates H2 2025 on the basis that excludes the JV arrangements.
- D04 never says outright that its figures include the JV arrangements. That comes from the exact 0.7 reconciliation in step 3.
- The packet documents are plain text (manifest method "text", no PDF pages), so there was no chart or row loss to check. The decisive rows match the docs/ source files word for word.
- Unread material: I did not read every line of the remaining sections (capital projects, operational data tables, other commodities). These are D01 lines 21-59 and 69 onward, D02 lines 25 onward, D03 lines 13 onward and D04 lines 26-48. However, searches of all four text files for realis, FOB, wmt, wet metric, dmt, achieved average pricing, joint venture arrangements, restat, like-for-like and H2 2025 / second half turned up no other relevant passages. Every line that matched was read, including D01:65, D02:61, D04:51 and D04:67.

contaminated: no. I used only the packet's text/ and docs/. I did not open question.txt or any other packet's files.
