# i03 strong-solver screen, solve 3 of 3 (blind-solver, fresh context; launch label "i03 blind solve 3")

Judged by the author against gold 1.0: RIGHT.

answer: 1.0 (US$ per wet metric tonne). On a like-for-like basis, H1 2026 was $84.1/wmt and H2 2025 was $83.1/wmt.
confidence: high

path:
1. H2 2025 price (D04, Q4 2025 operations review p.4, table "Average realised prices achieved for our major commodities", text/D04.txt line 9; the same text is in docs/ line 7): "Units H1 2025 H2 2025 2025 2024 Pilbara iron ore FOB, $/wmt 82.5 83.1 82.8 89.6". So H2 2025 = $83.1/wmt. The table's only Pilbara footnote is "Assuming 8% moisture". D04 does not mention joint-venture arrangements. The FY figure is repeated at D04 p.6 (line 13): "Achieved average pricing in 2025 was $82.8 per wet metric tonne".
2. H1 2026 price as reported (D02, Q2 2026 operations review p.4, line 9): "Units H1 2026 H1 2025 Pilbara iron ore FOB, $/wmt 85.2 83.2". It is repeated at D02 p.6 (line 13): "Achieved average pricing1 in H1 2026 was $85.2 per wet metric tonne ($83.2 in H1 2025) on an FOB basis".
3. The basis change (D02 footnote 1 on p.4 and p.6): "Pilbara average realised price excludes the impact of certain joint venture arrangements. Including these, realised prices for H1 2026 would have been $1.1/wmt lower (H1 2025, $0.7/wmt)."
4. The two reports cover H1 2025 on different bases. D02 gives H1 2025 as 83.2 on the new basis, which excludes the joint-venture arrangements. D04 gives 82.5. Since 83.2 − 0.7 = 82.5 exactly, D04's figures (H1 82.5, H2 83.1, FY 82.8) are on the old basis, which includes the joint-venture arrangements. A second check is that D04's halves match its FY figure when weighted by volume. Using D04 shipments (FY 279.1 Mt, Q4 78.7 Mt, Q4 +10% vs Q3, so Q3 ≈ 71.5, H2 ≈ 150.2 and H1 ≈ 128.9): (82.5×128.9 + 83.1×150.2)/279.1 ≈ 82.8.
5. Calculation on the old basis, the only one where both halves are disclosed: H1 2026 = 85.2 − 1.1 = 84.1. H2 2025 = 83.1. 84.1 − 83.1 = 1.0 $/wmt.
   - Dry-tonne check: 84.1/0.92 = 91.4 and 83.1/0.92 = 90.3. This is consistent but not requested.

minimal_documents: D02 + D04. Both are necessary and no substitute exists:
- Only D04 gives the H2 2025 price.
- Only D02 gives the H1 2026 price and the joint-venture footnote.
- D01 (Q1 2026) and D03 (Q3 2025) contain no Pilbara realised-price figures. I searched both for "achieved average", "average pricing", "realised price", "wmt", "dmt", "per wet" and "per dry" and found only cost guidance and index prices.

readings:
- **As printed, ignoring the basis change:** 85.2 − 83.1 = 2.1. This is not like-for-like because it compares a figure excluding the joint-venture arrangements with one including them.
- **On the new basis (excluding the arrangements):** the H2 2025 adjustment is not disclosed, so this cannot be computed from the documents.
  - If you assume H1 2025's $0.7 also applies to H2 2025, the answer is 85.2 − 83.8 = 1.4. That is an assumption, not a disclosed fact.
  - If you assume $1.1 instead, the answer is again 1.0.
- **Mixed-basis derivation:** working out H2 2025 from FY 82.8 (old basis) and the restated H1 83.2 (new basis) gives about 82.46 and an answer of about 2.7. This is a mixed-basis error, and D04 prints H2 2025 directly anyway.

gaps:
- The H2 2025 joint-venture adjustment is not disclosed, so the comparison can only be made on the old basis.
- Coverage:
  - I read D02 lines 9 and 13 and D04 lines 9, 11 and 13 in full.
  - I did not read the rest of D01–D04 line by line. I covered it with targeted searches across all four text files: realised, FOB, wet/dry tonne, "joint venture arrangement", restat, like-for-like and "Average realised prices achieved". That table appears only in D02 and D04.
- The manifest lists text sources (method "text"), with no PDFs or layout files. I checked the decisive table rows against the docs/ source text and they match.

contaminated: no. I did not read the packet's question.txt; the question came from the caller's input only.
