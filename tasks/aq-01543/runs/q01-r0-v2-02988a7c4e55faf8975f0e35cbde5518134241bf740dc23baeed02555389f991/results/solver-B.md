# q01 rev 0 - blind solver B (fresh blind-solver subagent, packet solver-2), 2026-10-07

Transcript audit (caller, parsed tool calls): 12 calls (Glob, Grep, Read), every path inside solver-2/; clean.

answer: 5.3 percentage points (Bulgaria about 33.4% minus South Korea 28.1%)

confidence: high

path:
1. South Korea, 2024 (D15, text\D15.txt line 9, and the table on lines 71-92). The text says: "Korea's total electricity generation in 2024 reached 595.6 TWh … Coal and LNG each generated 167.2TWh, or 28.1%". The 2024 table row repeats 167.2 and 28.1%, and the raw docs\ file has the same figures. A check gives 167.2 / 595.6 = 28.07%, so the printed 28.1% holds.
2. Bulgaria does not print a coal share for calendar year 2024, so I worked it out from three facts in D02 that are all dated 2024:
   - Total production (D02 line 10): "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - Coal plus nuclear (D02 line 11): "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". The comma is a decimal separator, so this is 28.46 TWh. Reading it as 2,846 TWh would make it larger than total production, so that reading is impossible.
   - Nuclear (D02 line 13): "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the International Atomic Energy Agency (IAEA)."
   - Calculation: 28.46 / 37.963 = 74.97% for coal plus nuclear. Subtracting nuclear gives 74.97 − 41.6 = 33.37% coal.
   - Check in GWh: nuclear = 0.416 × 37,963 = 15,792.6 GWh. Coal = 28,460 − 15,792.6 = 12,667.4 GWh, and 12,667.4 / 37,963 = 33.37%.
3. The difference is 33.37 − 28.1 = 5.27, which rounds to 5.3 pp. Using the unrounded Korea figure gives 33.368 − 28.073 = 5.295, still 5.3. Rounding both shares first gives 33.4 − 28.1 = 5.3. The answer does not change with the rounding method.
4. I excluded these Bulgaria figures because they cover other periods:
   - D02 line 18, "From September 2024 to August 2025 … coal being dominant at 27.6%": this is a rolling 12-month window, not calendar 2024.
   - D02 lines 70 and 135, "dropped from 35 percent in 2020 to 27 percent in 2025": these are 2020 and 2025.
   - D02 line 18, nuclear "about 40.38%": same September 2024 to August 2025 window.
5. I also excluded these Korea figures because they cover other years: the January–November 2025 coal share of 29.0% and the 11th BPESD targets (17.2% in 2030, 10.1% in 2038).

minimal_documents: D02 + D15. I found no alternatives. Searching every text\ file for "Bulgaria|Korea" matched only D02, D11, D13 and D15. The D11 mention (line 188, the South Korean company POSCO E&C in Poland) and the D13 mentions (lines 23 and 40, Romania's interconnections and the BRUA pipeline) contain no figures on generation mix.

readings:
- If someone used the September 2024 to August 2025 coal share of 27.6% for Bulgaria: 27.6 − 28.1 = −0.5. That is the wrong time window.
- If someone used Bulgaria's "27 percent in 2025": 27 − 28.1 = −1.1. That is the wrong year.
- If someone subtracted the September 2024 to August 2025 nuclear share of 40.38% instead of 41.6%: 74.97 − 40.38 = 34.6, and 34.6 − 28.1 = 6.5. That mixes two time windows.
- If someone used Korea's January–November 2025 share of 29.0%: 33.4 − 29.0 = 4.4. That is the wrong year.
None of these alternatives matches "calendar year 2024" as well as 5.3 does.

gaps:
- Bulgaria's 2024 coal share has to be calculated rather than read off the page. The calculation combines two sources: production and baseload figures with no named source, and the IAEA nuclear share. Their bases could differ slightly (gross vs. net generation), but at one decimal place this does not change the answer.
- The D02 chart "Bulgaria's Electricity Production from Jan 2024 to Dec 2024" (line 44) is missing from the text. The manifest lists method "text" with no PDF pages, so there was no page image to check.
- The renewables figure "3,3264 GWh" (D02 line 11) is garbled, but it is not needed.
- Coverage: I read D02 and D15 in full and confirmed the key numbers in the raw docs\ files. I did not read D01, D03–D10, D12, D14 or D16–D20 in full; I only checked them with the "Bulgaria|Korea" search, which found nothing. Following my instructions, I did not read question.txt in the packet root.

contaminated: no
