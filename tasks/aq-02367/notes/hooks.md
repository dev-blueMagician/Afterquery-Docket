# aq-02367 - cross-document hooks

Target: medium, hard where a design supports it (user 2026-10-09: "there is no slot for Easy Tier for this
bundle, we should target medium and high. do your best."). Doc N = task-page numbers. Same bytes as aq-02220,
so its hooks h1-h12 are closed families here (tasks/aq-02220/notes/hooks.md): every one of its seven tested
designs was "too easy" for the low model (two lookups plus one or two operations, each input found by keyword).
Facts carried by two documents cannot be a necessary input (the platform leaves one marked document out).

## Carried over closed (aq-02220)

h1 benchmark gas share of input (40.0%); h2 CG-led stage costs in model C (removal probe reached it without
Doc 1); h3 2035 deployment as share of the 2035 target (46.3%); h4 "a fifth" x 439 TWh (87.8); h5 waste-heat
use vs economic potential (42%); h6 homes to exceed 50 MWh (11); h7 district-network growth (175%); h8 FTE x
zones (4,080); h9 responses per week; h10 grace period months (108); h11 7% coincidence; h12 wet-heating share.

## New hooks considered 2026-10-09 (caller)

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| n1 | Doc 4 L18 27 TWh; Doc 2 Table 12 High 25.0 (2045) / 31.2 (2050) and L953-955 linear profile | first year the preferred option's added heat reaches the 2035 target volume = 2047 | Figure that must be computed (interpolation) | 2050 (first tabulated year above 27); 2046 (crossing time truncated) | Doc 1's "around 31 TWh in 2050" plus an assumed ramp from 2025 also gives 2047 (Doc 2 necessity at risk); "first year" convention must be stated | held, weak |
| n2 | Doc 4 L116 85% ASHP; Doc 2 Table 4 / para 54 (LT waste heat needs a WSHP) | benchmark heat-pump share minus the IA central mix's, all heat pumps = 85 - 78 = 7 pp | Part vs total (membership) | 13 (labelled ASHP+GSHP+WSHP rows only), 71 (ASHP only) | para 108 L1947 groups LT waste with waste heat against heat pumps, so 13 is defensible: two answers | rejected (ambiguous) |
| n3 | Doc 3 L1760 182 gCO2/kWh gas; Doc 4 L116 15%; Doc 2 Table 24 back-up boiler 85% | gas-boiler part of the benchmark per kWh heat = 32.1 g | Calculate across documents | 27.3 (no efficiency); 32.5/31.7 (other boilers) | 182 is a respondent's figure; no grid factor, so only a partial benchmark; three keyword lookups | rejected (lookup path) |
| n4 | Doc 3 Q28 (19 explicit of 38 agreeing) + Doc 4 L150 12-month window | respondents explicitly backing the deadline length later replaced | Mentions vs does | 38 (all agreeing), 25, 17 | Doc 3 alone names the 10-year proposal; Doc 4 only identifies (weak necessity); tied in one sentence | rejected |
| n5 | Doc 2 Table 12 Medium/High 2050 (20.7/31.2) + Doc 4 L144 zero cap for communally heated domestic | 2050 deployment the IA ties to the communally heated group = 10.5 TWh | Linking across documents | Doc 1 rounded 31 - 21 = 10; Table 2 share 41% x 31.2 = 12.8 | bridge is a name mapping; IA states Medium omits that group; likely lookup path | held, weak |
| n6 | Doc 3 Q10 10 GWh proposal; Doc 2 Table 12 31.2 TWh and para 79 510 zones | average 2050 heat per zone vs the trade body's trigger = 6.1x | Unit normalization | 170 towns (18.4x); 3,500 networks (0.89x) | numbers the documents never connect; keyword lookups | rejected |
| n7 | Doc 1 L927 14/76 TWh; Doc 2 para 54 19% | gap between the IA's waste share and the study's TWh = 0.6 pp | Exact vs rounded | 0 (reading "about 19%" as the waste share) | lookup plus two operations | rejected |

## Independent authors, 2026-10-09 (two question-author agents, all four texts read in full; origin claude)

Both returned "no fair Medium design"; every sketch below was dropped by its author and the caller agrees.

| Hook | Inputs | Ask / gold | Defect |
| --- | --- | --- | --- |
| a1 | Doc 1 L795 or Doc 3 L1205 Option 3 with refurbishment; Doc 2 L632; Doc 4 L132-136 | group in the 2021 preferred option absent from both the IA and the final rules (refurbishment group) | Doc 1/Doc 3 duplicate the proposal; Doc 2's exclusion changes nothing; Doc 1 L144 summary omits the group (second reading); short list diff |
| a2 | Doc 4 L18 7% (27TWh); Doc 2 Table 12 2035 High 12.5 | share of England's 2035 heat demand the preferred option adds = 3.2% (decoy 2.8% via the 2050 439 TWh, which para 89 frames as Table 12's base) | 7% is rounded, so one decimal is unsupported (band 3.0-3.5%), and whole percent merges gold and decoy; Doc 1's 31 TWh with an assumed ramp also gives 3.2% |
| a3 | Doc 4 L144 zero cap; Doc 2 Table 12 (31.2, 20.7) | share of 2050 deployment lost without the zero-cap group = 34% (decoys 41%, 32%) | keyword bridge then two lookups and a ratio; 41% competes as a reading; kept as TWh form i01 (see ideas.md) |
| a4 | Doc 4 L154 may choose whether to buy heat; Doc 1 L837 Denmark, L321 Netherlands | country that already let connected buildings decline heat = Denmark | with "once connected" Doc 1 alone answers; without it vague; four-country guess |
| a5 | Doc 4 L142-144 caps; Doc 3 Q24 (10 / 33 / 17) | respondents preferring the option closest to the final caps | Doc 4's interim commercial negotiation reads as Option 1, its caps as Option 2: two readings |
| a6 | Doc 4 L188 operators to consult; Doc 1 L1891-1935 list | consultee missing from the 2021 list | "for example" leaves the list open; "other relevant utilities" covers it; two candidates |
| a7 | Doc 3 L2227 one day minimum; Doc 2 Tables 11/17 | familiarisation gap 3.5 hours | two lookups |
| a8 | Doc 1 L155 "31 TWh of deployment in the period to 2050"; Doc 2 linear profile | cumulative deployment 407 vs 391 TWh | one document; sum vs integral conventions |
| a9 | Doc 2 Table 1 MCA | option b 3.35 vs c 3.325 | within rounding; one document |
| a10 | Doc 1 L755 "use the heat provided"; Doc 4 L154 | dropped duty to take heat | one plain sentence |
| a11 | Carbon timing Doc 1 L1076 / Doc 2 L973 / Doc 4 L116 | deployment or gap at the limit's start | two lookups; Doc 4 read first |

Notes: no dated event in a later document postdates a changed value whose earlier edition alone holds the gold
(Doc 3 restates each 2021 value beside its decision; Doc 4 states the 2023 consultation's old body names itself),
so the measured untied edition trap has no fair analogue here. No grid carbon factor exists, so benchmark
emissions cannot be computed. IA Table 13 and Table 14 do not reconcile internally; keep them out of golds.
