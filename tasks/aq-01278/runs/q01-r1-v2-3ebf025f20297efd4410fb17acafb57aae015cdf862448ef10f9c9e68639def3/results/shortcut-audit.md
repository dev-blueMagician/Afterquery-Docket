# q01 rev 1 shortcut audit (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

Raw return as received by the caller (agent result text; tool trace not exported):

answer: **−10.41%**. It fell from $2,074M in Q2 2025 to $1,858M in Q2 2026.

verdict: clear

shortest_path:
1. **Q2 2026, from D09** (the Q2 2026 press release, Personal Insurance net written premiums table, line 321): "Automobile $|1,858 $|1,968 (6)|%". International on line 324 is "International — 178 (100)", so Q2 2026 has no international personal business. The release says the prior-year quarter "included $178 million related to the Canadian operations divested by the Company in the first quarter of 2026", and Personal Insurance is now described as US-only. Worldwide auto for Q2 2026 is therefore 1,858.
   - Cross-check: six-month 2026 domestic auto of 3,614 (D09) minus Q1 2026 auto of 1,756 (D08/D10) gives 1,858.
2. **Q2 2025, from D10** (the Q1 2026 financial supplement, page 20, "Selected Statistics - Personal Insurance - Automobile", line 656): "Net written premiums $|1,955 $|2,074 $|2,165 $|1,956 $|1,756". The columns run 1Q2025 to 1Q2026, so Q2 2025 is 2,074.
   - **Why 2,074 is worldwide:** the Automobile page (2,074) plus the Homeowners and Other page (2,592, line 700) equals 4,666, which is total Personal Insurance including international. Domestic auto on page 19 is 1,968. That leaves international auto of 106 and international homeowners of 72, which sum to the 178 international total.
   - The same sum check works for every column (3,818, 4,718, 4,244, 3,486), which confirms the columns line up.
   - These "statutory" premium figures equal the GAAP figures for Personal Insurance in each quarter shown (for example 4,666 = 4,666, and 1,756 = 1,756 for 1Q2026).
3. **Calculation:** (1,858 − 2,074) / 2,074 = −216 / 2,074 = −10.4147%, which rounds to −10.41%.

The original files `docs\trv_ex991_2026-07-17.txt` (line 360) and `docs\trv_ex992_2026-04-16.txt` (line 741) match the extracted text.

sufficient_documents: D09 and D10 together. Neither works alone:
- D09 has both quarters of domestic auto, but its Q2 2025 international figure (178) is not split by product.
- D10 has worldwide auto for Q2 2025 but stops at 1Q2026.
- D08 (the Q1 2026 press release) only adds the 1,756 cross-check.

searches:
- **Terms searched:** automobile/auto; worldwide/world-wide/global/consolidated personal/total personal; international/Canad; 1,968; 2,074; 1,858; 10.4; (10)/(11); Travelers.
- **Read in full:** manifest, D09 and D10.
- **Read in part:** D08 lines 1–320 in full, the rest checked by targeted search.
- **Searched only:** D01–D07, which are Allstate, Chubb and Progressive and never mention Travelers.
- **Shortcut check:** 2,074 appears only in D10 and 1,858 only in D09. No Travelers document contains a ready-made figure near −10.4%.
- **Route risk:** this is a simple two-document lookup plus one division, which is a difficulty risk but not a shortcut. The word "worldwide" tells the reader to include international business; it doesn't give the answer away.
- **Excluded file:** I did not read the packet-root `question.txt`, because question files are off limits.

readings/gaps:
- **Domestic-only reading:** (1,858 − 1,968) / 1,968 = **−5.59%**, which is D09's "(6)%". This is wrong for "worldwide", but it is the likely trap if a solver uses one document.
- **Domestic auto plus all international personal:** (1,858 − 2,146) / 2,146 = **−13.42%**. This wrongly counts international homeowners as auto.
- **Gaps:**
  - The packet has no Q2 2026 financial supplement. Q2 2026 worldwide auto therefore relies on D09's domestic auto figure plus its "—" for international. That is consistent with the Q1 2026 pattern, where worldwide and domestic both equal 1,756.
  - D08 after line 320 and D01–D07 were only searched, not read.

Usage reported: 16 tool uses, 167 s.
