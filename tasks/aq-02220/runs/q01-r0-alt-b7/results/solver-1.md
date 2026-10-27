# Removal probe return: q01 rev 0 without Doc 4 (D01)

- Date: 2026-10-08
- tested_sha256 (rev 0, question without ", to the nearest percent"): 274c116f875f1ddf6893227dbb0c5af77373e29c7cfbdd6d9dfe9ab45fd15601
- Rev 1 (2784008a...) differs only by the added precision phrase; answer, evidence and documents unchanged.
- Packet: tasks/aq-02220/runs/q01-r0-alt-b7/solver-1 (Doc 1 -> D01, Doc 2 -> D02, Doc 3 -> D03; neutral headers)
- Role: blind-solver (fresh context, question only, plus the forced-guess instruction)

Raw return (verbatim):

answer: About 32.7% of the electricity-plus-gas input is gas. Per unit of zone heat, gas is about 0.118 and electricity about 0.242, which is a gas:electricity ratio of roughly 33:67. The benchmark is read as the impact assessment's central technology mix for heat networks in zones.

confidence: medium. The arithmetic is firm. The weak point is that no document uses the phrase "zone emissions benchmark", so I had to map it to a table.

path:
1. **What the benchmark is (D02, the impact assessment).**
   - The packet's only numbers for how zone heat is supplied are in D02 Table 4, "Central assumption for generation technologies supplying heat networks in zones". The figures are EfW 9%, High Temp Waste Heat 4%, Low Temp Waste Heat 6%, ASHP 14%, GSHP 24%, WSHP 34%, Back-up Boilers 10% (lines 988-1007).
   - Table 16 "Central" repeats exactly the same figures (lines 1780-1797).
   - Paragraph 53 (line 973) ties this mix to the zone carbon rule: "there will be a requirement for new heat networks in zones to be low carbon from the outset. This has informed the assumptions we have made regarding the generation technology mix". It also says the mix drives "Carbon and air quality savings".
   - D01 (lines 1061, 1071) proposes the zone limit as "grams of CO2 emissions per kWh of heat delivered" but says "we are not proposing the level". D03 (lines 1850-1854) says the threshold "will be set out in secondary legislation". So neither gives a numeric benchmark.
2. **Which inputs count as electricity or gas (D02 paragraph 54, lines 979-985).**
   - Waste heat includes "waste heat sources that require a water source heat pump", so Low Temp Waste Heat is an electric heat pump.
   - "There is also a role for gas as back-up boilers", so the back-up boilers are gas.
   - EfW and High Temp Waste Heat are left out because their input is neither electricity nor gas.
3. **Efficiencies (D02 Table 24, "Thermal Efficiency (factual and counterfactual)", lines 2230-2257).**
   - The technologies are listed in the same order as Table 21: ASHP 321, GSHP 284, WSHP 330, WSHP-Low grade waste heat 541, WSHP-Medium grade 690, Energy from Waste 500, Heat Exchanger N/A, Gas CHP 40, Back-up Gas Boiler 85. These are the "Heat network" rows.
   - The "Individual" rows are Commercial Gas Boiler 84, Domestic Gas Boiler 86 and Electric Heater 100.
   - The values appear nowhere else in D02, so there are no conflicting printed figures.
4. **Calculation (input = heat share ÷ efficiency).**
   - Electricity: 0.14/3.21 = 0.043614; 0.24/2.84 = 0.084507; 0.34/3.30 = 0.103030; 0.06/5.41 = 0.011091. Total 0.242242.
   - Gas: 0.10/0.85 = 0.117647.
   - Gas share: 0.117647 / 0.359889 = 0.32690, so **32.7%**.
   - Table 4 sums to 101% because of rounding. That does not change a ratio.

minimal_documents: D02 alone is enough. D01 (lines 1061-1080) only adds the "zone low carbon requirement" idea behind the term "benchmark". D03 cannot replace D02, because it has no mix and no efficiencies.

readings:
- If "Low Temp Waste Heat" is matched to the WSHP-Medium grade efficiency (690%) instead of Low grade, the answer is 32.9%.
- If EfW's 500% is treated as an electricity input (0.09/5.00 = 0.018), the answer is 31.1%. The documents never say EfW uses electricity.
- If the sensitivity-test Alternative mix is used (Table 16: EfW 18, HT 6, LT 12, ASHP 11, GSHP 18, WSHP 25, boilers 10), the answer is 37.6%.
- If the gas counterfactual (Table 5) is treated as the "benchmark", the answer is about 90.1%. This needs the individual-building efficiencies (86, 84, 100) as well as the heat-network ones, which conflicts with the question saying "heat-network efficiencies".
- If the ASHP and GSHP values were misaligned in extraction (swapped), the answer would be 33.1%.

gaps:
- No layout file exists. I read only text\, as instructed, and did not check the original PDF. So I could not visually confirm which row each Table 24 value belongs to; I inferred it from the column order matching Table 21. The waste-heat shares 9+4+6 = 19% match paragraph 54's "19%", which supports the Table 4 alignment.
- Coverage was targeted searches across all three files (benchmark, gCO2, kWh, carbon intensity/threshold, gas, electricity, efficiency, EfW, percentages, synonyms such as baseline/reference/comparator), plus section reads of:
  - D01 lines 1-80, 150-180, 500-640, 755-785, 866-895, 915-940, 1020-1130, 1320-1345
  - D02 lines 1-80, 636-1085, 1640-1963, 2040-2349
  - D03 lines 1-150, 1275-1295, 1420-1490, 1720-1868, 3110-3139
- The rest of each document was not read line by line.

contaminated: no. The caller's message contained only the workspace root, packet path and question.

forced_guess: 32.7%
forced_probability: 0.6, source: documents
