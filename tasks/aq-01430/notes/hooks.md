# aq-01430 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Target: medium (user, 2026-10-06). Caller's first pass, written from a full read of all eight
documents (2026-10-06). Local id = platform Doc: D01 = Doc 8 (gas review, 9 Jun 2026), D02 = Doc 5
(mid-year H1-2023, 5 Oct 2023), D03 = Doc 6 (mid-year H1-2025, 7 Oct 2025), D04 = Doc 1 (2020
review, 29 Mar 2021), D05 = Doc 2 (2021 review, 30 Mar 2022), D06 = Doc 3 (2024 review, 8 Apr
2025), D07 = Doc 4 (2025 review, 21 Apr 2026), D08 = Doc 7 (Q1-Q3 2025 report, 13 Nov 2025).
All prose; no tables (charts render as "Loading data...").

## Bundle-wide source risks (apply to every hook)

- Restatements: D07 restates many 2024 figures from D06 (demand growth 4.0% / +1,172 TWh ->
  4.3% / +1,265; solar 2,131 -> 2,143 TWh and +474 -> +479; wind +182 -> +190; gas +103 -> +183;
  emissions +1.6% -> +1.7%; intensity 473 -> 471; India demand +98 -> +118; EU demand +1.1% ->
  +1.9%; China demand +623 -> +631). D08 L83 gives 2024 fossil growth as +322 TWh (+1.8%) vs D06
  +245 (+1.4%). Also 2021 demand +1,414 (D05) vs +1,536 (D07); 2021 wind +227 (D05) vs +268 (D02)
  vs +265 (D07); 2015 wind+solar share 4.6% (D04/D05) vs 4.5% (D07); 2020 wind+solar 9.4% (D04)
  vs 9.3% (D05); 2025 gas +38 (D01) vs +36 (D07); 2025 demand 31,774 (D01) vs 31,779 (D07).
  Any ask on a restated quantity has two defensible answers unless the precision absorbs it.
- Units: D07 uses MtCO2e and gCO2e/kWh; D02/D03/D06 use MtCO2 and gCO2/kWh. Capacity: D06 China
  in GWac, global in DC by default; D07 China/global in GW(DC), India/Brazil in GW(AC).
- Overview exposure: Q1-Q3 (498, 603), FY 2025 (636, 849, -38) and H1-2025 (306) headline figures
  sit in the capture's overview; Q4/H2 derivations from those are exposed. China/US/EU/India
  comparators and country counts are not in the overview.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D07 L587/L617: 50 countries >10% solar in 2025 (all countries); D06 L685: 42 countries at least a tenth from solar (2024) | Countries above 10% solar: 2025 minus 2024 = 8 | Who belongs where (population), temporal alignment | D07 L617 same paragraph: larger markets (>5 TWh) 19 in 2025 "up from 15 in 2024" (4; or 35 if 15 is misread as all countries); D03 L168 H1 counts 29 vs 22 (7); D05 L155 wind+solar 50 (2021); D06 L707 wind 35 (2024) | ">=" (D06) vs ">" (D07) wording; vintage mix | investigate (strongest scope-decoy set) |
| h2 | D06 L767: China hydro "fell in 2023 due to droughts (-72 TWh)" (parenthetical in a 2024 sentence); D02 L279/L283: China hydro H1-2023 -22% (-129 TWh) | China hydro H2-2023 vs H2-2022 = -72 - (-129) = +57 TWh | Temporal alignment (H2 = FY - H1), buried comparator | Same D06 sentence: 2024 rebound +130 TWh (+11%); D06 L158 "72%" of 2024 global rebound; FY -72; H1 -129; D02 L285 hedged "could ... recover" | Standard transformation (trial-02 q01 Too easy); 2 lookups | investigate |
| h3 | D06 L1008: US demand 2023 -1.3% (-55 TWh) "a milder summer in 2023"; D02 L303: US H1-2023 demand -3.4% (-72 TWh) | US demand H2-2023 = +17 TWh (sign flip) | Temporal alignment; prose vs derived | Prose "milder summer ... demand decreased" suggests H2 fell; FY -55; H1 -72 | Same doc pair/mechanism as h2: pick one | investigate |
| h4 | D07 L179/L599: China solar +336 TWh 2025; D08 L59: China Q1-Q3 +280; global FY +636 (D07), Q1-Q3 +498 (D08) | China share of Q4-2025 global solar growth = 56/138 = 40.6% | Temporal alignment, aggregation | Printed "more than half" FY (52.8%) and Q1-Q3 (56.2%) | Headline inputs, overview-exposed globals | investigate |
| h5 | D07 L179/L191: FY 2025 solar +636, demand +849; D03 L89/L136: H1 solar +306, demand +369 | Solar share of H2-2025 demand growth = 330/480 = 68.75% (69%) | Temporal alignment, method applied to unreported period | Printed 75% (FY), 83% (H1); D08 forecast route 334/462 = 72% | Headline inputs; overview exposure | sketch-level only |
| h6 | D07 L207: 2025 additions 647 GW(DC), 2024 582 GW; D03 L180: H1-2025 380 GW, H1-2024 232 GW; D06 L172: 2024 585 GW | H2 solar capacity additions 2025 vs 2024 = 267/350 - 1 = -23.7% (-24%; 585 gives -24.4%) | Temporal alignment, sign flip | FY +11%, H1 +64% | DC/AC; 582 vs 585 agree at whole % | investigate |
| h7 | D01 L100: G7 gas 2,627 -> 2,577 (-50); D07 L703/L958: US gas -63 TWh (-3.4%), 1,807 TWh | Non-US G7 gas change 2025 = +13 TWh | Carve-out under a printed whole-group figure | G7 -50 printed; global coal also -63 | Route split: D06 1,865 vs D07 1,807 (-58 -> +8); D01 US 2015-25 +474 vs D06 2015-24 +531 (-57 -> +7) | risky (one clear answer) |
| h8 | D07 L139/L225: India fossil 2025 -52 TWh; D08 L29/L67: India Q1-Q3 -34 TWh; D08 L107 "decline is likely temporary" | India fossil Q4-2025 = -18 TWh | Temporal alignment | FY -52, Q1-Q3 -34; hedged rebound expectation | Standard transformation | low |
| h9 | D08 L46: fossil Q1-Q3 -17 TWh; D03 L152: fossil H1 -27 TWh | Global fossil Q3-2025 = +10 TWh (rose) | Temporal alignment, sign flip | Every printed 2025 period shows a fall | 9M - 6M = trial-02's measured Too easy shape | low |
| h10 | D07 L1036: Finland ended coal April 2025 (EU section, beside FY coal -14 TWh at L1020); D03 L353: EU coal H1-2025 +1.4 TWh | EU coal in the half-year of Finland's exit = +1.4 TWh | Event bridge into earlier edition (aq-00964 shape) | D07 FY -14 TWh in same section | "half-year" wording names the period type (aq-00998 q03 Too easy pattern) | low |
| h11 | D08 L79/L53: 2025 forecasts demand +831, solar ~640; D07 actuals 849, 636 | Forecast errors | Forecast vs actual | n/a | All four figures in the overview | reject (exposed lookups) |
| h12 | D06 L204: 2024 clean growth record 927 TWh; D07 L127: 2025 low-carbon +887 | 2025 shortfall vs 2024 record = 40 TWh | Calculate across documents | n/a | Two lookups | low |
| h13 | D07 L145 FY renewables 10,730 vs coal 10,476; D03 L198 H1 renewables 5,072 vs coal 4,896 | H2-2025 renewables minus coal = 78 TWh | Temporal alignment | FY 254, H1 176 | Standard transformation | low |
| h14 | D07 L1014 EU wind 2025 -12 TWh; D03 L347 EU wind H1 -21 TWh | EU wind H2-2025 = +9 TWh (sign flip) | Temporal alignment | FY and H1 both falls | Standard transformation | low |
| h15 | D07 L179/L1012/L1088/L956: FY solar China +336, US +85, EU +60, India +53; D03 L170: H1 China 168, US 44, EU 37, India 17 | H2-2025 ranking China, US, India, EU (FY/H1 both give EU above India); India minus EU = +13 | Ordered answers, temporal alignment | FY and H1 orders | Standard transformation | investigate as variant |
| h16 | D01 L33 G7 37% of global gas, US 26% (L98); D07 L713 US 1,807; D01 L100 G7 2,577 | US share of G7 gas 2025 = 70.1% (one decimal; 26/37 = 70.3% approximation) | Calculate across documents; exact vs rounded | 26/37 route differs at one decimal | Two lookups | low |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.

Not found (checked during the read): no Ember forecast series with more than one edition for the
same target (only D08's 2025 forecasts; D06 gives a conditional 3.3% scenario), so the measured
aq-00964/aq-00745 q09 "outlook in force at an event" trap has no clean analogue; no cross-document
lists of hedged findings; authors are Ember staff only (rule 10 bars author answers).
