# q01 rev 6 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-08

Input: workspace root, packet path and the verbatim question only.
Transcript audit (caller, parsed tool calls): 15 calls (Glob, Grep, Read, SubagentHandback), every path inside shortcut/; clean.

answer: 22.8 percentage points. Poland's coal share was 56.2%. Bulgaria's works out to about 33.37%, so 56.2 − 33.37 = 22.83, which rounds to 22.8.

verdict: clear

shortest_path:
1. Poland, D11 (text/D11.txt line 13, Energy Sector, "Power Generation"): "In 2024, the share of coal in electricity generation was 56.2% (down from 70.7% in 2022 and 4.3 p.p. less than in 2023)." This is a direct lookup.
2. Bulgaria, D02 (text/D02.txt). No 2024 coal share is stated, so it has to be worked out from three inputs:
   - line 10: "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - line 11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". The comma is a decimal point, so this is 28,460 GWh.
   - line 13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the International Atomic Energy Agency (IAEA)."
   - Coal plus nuclear share: 28,460 / 37,963 = 74.968%. Coal share: 74.968 − 41.6 = 33.368%.
   - Same result in GWh: nuclear is 0.416 × 37,963 = 15,792.6 GWh, so coal is 28,460 − 15,792.6 = 12,667.4 GWh, and 12,667.4 / 37,963 = 33.37%.
3. Difference: 56.2 − 33.368 = 22.832, giving 22.8 pp. The rounding is stable: varying 28.46 TWh by ±0.005 gives 22.82–22.85. If 41.6% is taken as exact, the result is always 22.8.

sufficient_documents: D11 and D02 are both required, and there is no alternative pair. Of all 20 texts, only D11 mentions Poland or Polish. Only D02 has Bulgarian data; D13 (Romania) mentions Bulgaria twice, as a trading neighbour and as part of the BRUA pipeline name. No single document gives both values, and nothing gives the whole answer.

searches:
- Read D02 and D11 in full, plus manifest.json.
- Ran these searches across all 20 files in text/:
  - "Bulgaria" (73 hits: D02 and D13 only) and "Poland|Polish" (D11 only)
  - coal or lignite within reach of a % or percent figure, in every document
  - answer-shaped values and phrases: 22.8, 33.4, 33.3, 74.9, 75.0, "percentage point", "p.p.", "pp". Only D11's own "p.p." matched; the "pp" hits were URLs such as kznpp.org and unrelated text.
  - comparative wording: "coal-dependent", "most coal", "reliance on coal". Only D11 says "one of the most coal-dependent countries in the EU", and it gives no ranking or Bulgaria figure.
- Checked the original docs/ccg_energy_cleantech_sectors_bulgaria.txt (lines 1–50) and grepped docs/ for the key figures. The original matches the D02 text, with no extra table or chart data.
- Coverage: every document was searched by keyword, and the two relevant documents were read in full.

readings/gaps:
- Wrong-period trap 1: D02 line 18 says that from September 2024 to August 2025 "coal being dominant at 27.6%". That gives 56.2 − 27.6 = 28.6. I rejected it because eight of those twelve months are in 2025 and the passage describes the consumption/supply mix, not 2024 generation.
- Wrong-period trap 2: D02 lines 70 and 135 say coal "dropped from 35 percent in 2020 to 27 percent in 2025". That gives 29.2, but it is the wrong year.
- Mixed-period variant: using the Sep 2024–Aug 2025 nuclear share of 40.38% instead of 41.6% gives a coal share of 34.59% and a difference of 21.6. I rejected the period mismatch.
- Poland alternatives:
  - A derived figure from TWh is possible: coal is about 94.6 TWh (from "fell by 5.4 TWh (-5.4% y/y)") against a total of about 169 TWh (from RES 49.8 TWh at 29.4%), which gives about 55.8–56.0%. The explicit 56.2% outranks this.
  - "at least 56 percent reliance on coal" is a 2030 target.
  - "Fossil fuels made up 70% of Poland's energy sources in 2024" covers all fossil fuels and all energy, not coal in electricity.
- Interpretive risks, which I judge minor:
  - Bulgaria's figure depends on the document's own definition of baseload as "(coal, nuclear)". In reality this category may include some gas-fired thermal plants.
  - It also combines the IAEA nuclear share with a total from another source.
  - Both points are stated as given in D02, and I found no conflicting 2024 coal figure.
- Difficulty risk, not a shortcut: the Poland input is a direct keyword match, and the step across documents is a plain subtraction. The non-trivial work is the derivation inside D02 and avoiding the 27.6% and 27% traps.
- Extraction gaps:
  - D02's "View Bulgaria's Electricity Production from Jan 2024 to Dec 2024 in the chart:" has no chart data in either docs/ or text/. It shows monthly total production, so it is unlikely to hold a coal share, but it is unread.
  - "3,3264 GWh" for renewables is garbled; it is not needed.
- Contamination check: none found. The automatically attached git status listed only file names from other tasks and memory files, with no content about this question. I did not read question.txt, notes, or other packets.
