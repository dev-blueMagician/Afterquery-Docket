# q01 rev 1 blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

Raw return as received by the caller (agent result text; tool trace not exported):

**Answer: −10.41%.** Travelers' worldwide personal auto net written premiums fell from $2,074 million in Q2 2025 to $1,858 million in Q2 2026.

answer: −10.41%

confidence: high

path:
1. **What is asked:** the percentage change in worldwide (domestic plus international) Personal Insurance automobile net written premiums, Q2 2025 to Q2 2026, in $ millions, with sign, to two decimal places.
2. **Q2 2026 figures, D09 (Travelers Q2 2026 press release, Personal Insurance net written premiums table, text line 321; docs/trv_ex991_2026-07-17.txt lines 360–363):**
   - "Automobile $|1,858 $|1,968 (6)|%" is listed under "Domestic".
   - "Total Domestic 4,308 4,488 (4)"
   - "International — 178 (100)"
   - "Total $|4,308 $|4,666 (8)|%"
   - So there was no international business in Q2 2026. D09 line 340 says the prior-year quarter "included $178 million related to the Canadian operations divested by the Company in the first quarter of 2026."
   - Worldwide auto for Q2 2026 is therefore 1,858 + 0 = **1,858**.
3. **Q2 2025 figures, D10 (Q1 2026 financial supplement):**
   - Page 19, "Net Written Premiums - Personal Insurance" (text lines 638–643): Domestic "Automobile $|1,859 $|1,968 $|2,062 $|1,856 $|1,756", "Homeowners and Other 1,813 2,520 2,489 2,229 1,730" and "International 146 178 167 159 —". The columns are 1Q2025 through 1Q2026.
   - Page 20, "Selected Statistics - Personal Insurance - Automobile" (text line 656; docs/trv_ex992_2026-04-16.txt line 741): "Net written premiums $|1,955 $|2,074 $|2,165 $|1,956 $|1,756".
   - Page 21, Homeowners and Other (text line 700): "Net written premiums $|1,863 $|2,592 $|2,553 $|2,288 $|1,730".
4. **Checking that page 20 is worldwide:** the labels don't say so in words, but the numbers show it.
   - For 2Q2025: 2,074 − 1,968 = 106 of international auto, and 2,592 − 2,520 = 72 of international homeowners. Together 106 + 72 = 178, which equals the International line. Also 2,074 + 2,592 = 4,666, which equals the segment total.
   - The same check works for every other quarter: 1Q25 96 + 50 = 146; 3Q25 103 + 64 = 167; 4Q25 100 + 59 = 159; 1Q26 0 + 0 = "—".
   - So worldwide auto for Q2 2025 = **2,074**.
5. **Calculation:** (1,858 − 2,074) / 2,074 = −216 / 2,074 = −0.104147, which is **−10.41%**. As a check, 2,074 × 0.1041 = 215.90 and 2,074 × 0.10415 = 216.01, so the ratio falls between them.

minimal_documents: D09 and D10, both needed.
- D10 is the only document that splits the Q2 2025 international $178 million by product line (the page 20 total of 2,074).
- D09 is the only document with Q2 2026 data.
- D08 (Q1 2026 press release) can't replace either one. It has only domestic auto and an unsplit international figure. No other document in the packet covers Travelers.

readings:
- **Domestic auto only**, using the "Domestic – Automobile" row: (1,858 − 1,968) / 1,968 = −110 / 1,968 = −5.5894%, which rounds to **−5.59%**. D09 prints this rounded as "(6)%". The word "worldwide" points to the international-inclusive figure instead.
- A per-sale-adjusted view gives the same −5.59%: once the divested Canadian auto is removed, what remains is domestic.

gaps:
- The packet has no Q2 2026 financial supplement. The Q2 2026 worldwide figure is therefore derived as domestic 1,858 plus nil international, not printed as a total. It is well supported: D09 shows International as "—", and in 1Q2026 the page 20 figure equals domestic auto (1,756 = 1,756).
- The fact that D10 page 20 includes international is shown by the arithmetic, not by a label or footnote.
- Not fully read:
  - D01–D07 (Allstate, Chubb and Progressive releases) were only covered by a packet-wide "automobile" search. That search found nothing about Travelers outside D08–D10.
  - D08 was checked by search only.
  - D10 was read at lines 1–80, 560–720 and 1265–1312.
  - D09 was read at lines 1–420, plus searches.
- The sources are .txt files (method "text", no pages), so there was no PDF page to check. I confirmed the decisive rows in the original docs/ files.

contaminated: no

Usage reported: 14 tool uses, 153 s.
