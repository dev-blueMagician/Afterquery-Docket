# q01 rev 1 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-07

Transcript audit (caller, parsed tool calls): every path inside shortcut/; clean.

answer: 22.8 percentage points. Poland's 2024 coal share was 56.2%. Bulgaria's was about 33.37%, derived from figures in its guide. 56.2 − 33.37 = 22.83, which rounds to 22.8.

verdict: clear

shortest_path:
1. D11 (Poland guide), Energy Sector, line 13: "In 2024, the share of coal in electricity generation was 56.2% (down from 70.7% in 2022 and 4.3 p.p. less than in 2023)." This is a direct lookup.
2. D02 (Bulgaria guide), Energy section. No sentence states coal's share for calendar 2024, so it has to be derived from three statements in the same document:
   - Line 10: "electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024"
   - Line 11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". The comma is a decimal comma, so this is 28.46 TWh, which fits the 37.963 TWh total.
   - Line 13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the ... (IAEA)"
   - Calculation: nuclear = 0.416 × 37.963 = 15.793 TWh. Coal = 28.46 − 15.793 = 12.667 TWh. Coal share = 12.667 / 37.963 = 33.37%. Equivalently, 74.97% − 41.6% = 33.37%.
3. Difference: 56.2 − 33.37 = 22.83, so 22.8. Rounding Bulgaria to 33.4 first also gives 22.8.

sufficient_documents: D02 and D11 are both needed. I found no alternative. Neither document mentions the other country. D13 (Romania) names Bulgaria only as an electricity-trading neighbour and the BRUA pipeline, with no coal share. No other document mentions Bulgaria or Poland.

searches:
- Literal and concept terms: coal, lignite, baseload, nuclear, share, TWh/GWh, 41.6, 27.6, 35 percent, 56.2, 70.7, "4.3 p.p", and Bulgaria/Bulgarian/Poland/Polish across all 20 text files and the raw docs.
- Read in full: D02, D11, D13.
- Coal hits in the other 15 documents were checked: none mention Bulgaria or Poland. The country-name count search covers every line, including long lines omitted from the coal output.
- I spot-checked the raw docs/ files for Bulgaria and Poland; the key lines match the text extraction (method "text"). In the Bulgaria raw file, "56.2" occurs only in "$56.2 million" (EBRD), which is unrelated.
- No whole-answer summary, ranking, cross-country comparison or single passage gives Bulgaria's 2024 coal share or the difference.
- I did not open question.txt.

readings/gaps:
- Decoy 1, wrong period: D02 line 18 says "From September 2024 to August 2025 ... coal being dominant at 27.6%". That window is not 2024 and the figure is framed as consumption/supply. Using it gives 56.2 − 27.6 = 28.6. This is the main misreading risk.
- Decoy 2, wrong year: D02 lines 70/135 say coal "dropped from 35 percent in 2020 to 27 percent in 2025". Using 27 gives 29.2.
- Decoy 3: using the September 2024–August 2025 nuclear share of 40.38% in the derivation gives 74.97 − 40.38 = 34.59, so 21.6.
- Poland decoys: 60.5% is the 2023 value (56.2 + 4.3) and 70.7% is 2022. "Fossil fuels made up 70% of Poland's energy sources in 2024" covers all fossil fuels in energy sources, not coal in electricity. The "at least 56 percent" figure is a 2030 target. None fits the question.
- Rounding sensitivity: "approximately 41.6%" is a rounded input. If the true nuclear share were 41.633% or more, the result would round to 22.9. With the figures as stated, it is 22.83, which gives 22.8.
- Source-mixing caveat: the nuclear share comes from IAEA, while the baseload and total figures come from a separate national source. The document presents them as consistent, so I treat them that way.
- Unread/extraction gaps: D02 line 44 refers to a monthly production chart whose data is not in the text. It covers total output, not coal, so it should not matter. Web resources such as lowcarbonpower.org are not in the packet.
- Difficulty risk, not a shortcut: the Poland side is a single direct lookup, and the Bulgaria side is a short three-number derivation inside one document. The answer still needs both documents.

Contamination note: the session's auto-attached git status showed file names only (memory-file names and run files from an unrelated task, aq-00949), with no contents. Nothing about aq-01543's key, notes or prior outputs appeared, and no CLAUDE.md or project instructions were loaded. I do not consider this contaminated.
