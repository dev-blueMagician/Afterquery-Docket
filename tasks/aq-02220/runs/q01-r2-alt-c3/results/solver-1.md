# Removal probe return: q01 rev 2 without Doc 2 (D02)

- Date: 2026-10-08
- tested_sha256: 89e95f8b06ac883340b59c53c084c832df7634d2967e621823fb802dcfee2d14
- Packet: tasks/aq-02220/runs/q01-r2-alt-c3/solver-1 (Doc 1 -> D01, Doc 3 -> D02, Doc 4 -> D03; neutral headers)
- Role: blind-solver (fresh context, question only, plus the forced-guess instruction)

Raw return (verbatim):

answer: Not answerable from this packet. The packet gives the benchmark's heat split, but it does not include the impact assessment or any heat-network efficiency figures (heat pump COP/SCOP or gas-boiler efficiency). Without those two numbers the gas share of the electricity and gas input cannot be calculated.
confidence: high (that the packet is insufficient)

path:
1. The benchmark split is in D03 (2026 summary of the government response to the 2023 consultation), line 116, under "Emissions in Heat Network Zones": "This will be based on a benchmark scenario assuming 85% of heat is delivered by low-carbon air source heat pumps using electricity and 15% is supplied by gas boilers." This is a share of heat output, not of fuel input.
2. The impact assessment is referred to but never included. D01 (October 2021 consultation) mentions an "accompanying" IA at lines 155, 508, 801 and 822, plus the glossary at 1707 ("IA – Impact Assessment"). The quoted content covers only SNPV (£560m / £290m / –£110m), deployment (31 / 21 / 5 TWh) and the 100 MWh "large" building definition. No efficiencies appear.
3. I searched all three documents for efficiency figures and found none:
   - Terms searched: efficien*, efficiencies, COP/SCOP/SPF, seasonal, coefficient, boiler, heat pump, air source/ASHP, losses, kWh, assum*, gCO2, carbon intensity, emissions factor, every "N%" figure, every decimal number, and "gas".
   - All "efficien*" hits in D01 are about fabric/energy efficiency or process efficiency.
   - D02 (June 2022 government response) never mentions the IA. Its only relevant number is a respondent's suggestion: "182gCO2/kWh (reflecting the carbon intensity of gas)" (line 1760). That is a carbon intensity, not an efficiency.
   - D03 line 120 says "Exact emissions factors will be published before 2030."
4. The calculation the question needs: gas share = (0.15/η_boiler) ÷ (0.85/COP_ASHP + 0.15/η_boiler) × 100. Results for illustrative values only (none are sourced from the packet):
   - COP 3.0, boiler 90% → 0.16667/(0.28333+0.16667) = 37.0%
   - COP 3.0, boiler 85% → 0.17647/0.45980 = 38.4%
   - COP 2.8, boiler 85% → 0.17647/0.48004 = 36.8%
   - COP 2.8, boiler 90% → 35.4%
   - COP 2.5, boiler 85% → 34.2%

minimal_documents: D03 supplies the 85/15 benchmark. The missing impact assessment would supply the efficiencies. D01 only shows that the IA exists. Nothing else in the packet can replace either input.

readings:
- Ignoring efficiencies would give 15.0%, but the question explicitly asks to use them, so this reading doesn't hold up.
- Reading "input" as emissions rather than energy would also need factors the packet lacks (only the respondent's 182 gCO2/kWh for gas, and no electricity factor). Also not answerable.

gaps:
- The impact assessment (or any source of heat-network ASHP efficiency and gas-boiler efficiency) is not in the packet. text\manifest.json lists only D01–D03.
- There is no docs\ folder at D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-02220\runs\q01-r2-alt-c3\solver-1\docs and no .layout.txt files, so I couldn't check original PDF pages. The image-only "Theory of change diagram" in D01 (line 1939) was lost in extraction and could not be checked, though it is unlikely to hold efficiency figures.
- Coverage: I read D03 in full. In D01 and D02 I did full-text keyword searches and read these sections: D01 lines 1–30, 140–169, 300–339, 515–604, 740–889, 1020–1139, 1880–1948; D02 lines 1–60, 1240–1289, 1715–1884. I did not read the rest of D01/D02 line by line.

contaminated: no

forced_guess: 37.0% (assumes a heat-network ASHP COP of 3.0 and a gas-boiler efficiency of 90%; neither value is from the packet)
forced_probability: 0.1, source: both
