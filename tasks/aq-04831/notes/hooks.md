# aq-04831 - cross-document hooks

Target: medium (lowest open tier the user named; slots at capture Hard 0/5 · Medium 0/1 · Easy 0/0). Medium has
one slot and every captured run on 2026-10-14 started at the High level, so every hook is audited against the
strongest solver (two solvers x 3 tries; pass needs each wrong at least once, not all wrong) as well as the medium one.
No earlier captures exist for these bytes (new bundle), so the family record in
`.claude/memory/docket-local-solver-calibration.md` is the prior.

Structural finding (caller, all eight texts read 2026-10-14): the only document lineage is D01 -> D04 -> D07
(the RMBS article reuses the 2021 bank article's method; the 2021 article cites the April 2021 draft of CPG 229).
D08/D05 overlap on coal (Debbie, seaborne shares). D06 and D02 stand alone. No document answers, amends or
completes another's figures, and there is no forecast/actual or proposal/final pair across documents.

| Hook | Source inputs and locations | World fact / possible ask | Lever | Decoy / counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D04 l.26 five hazards; D01 fn 5 l.642 seven hazards | hazards in the later VaR not in the earlier (cyclone wind, surface (flash) flooding) | entity resolution; mentions vs does (D04 l.22 names "cyclones" among acute risks but its VaR covers "wind storms (other than cyclones)") | extreme wind / soil subsidence / forest fire are renamed, not new | none | sketched as i01; quick test "too easy" (user, 2026-10-14); closed |
| h2 | D07 l.89 climate risks = physical, transition, liability; D04 analyses physical + transition; D01 physical only (l.470) | kind of climate risk neither RBA article quantifies (liability) | conditional filter | transition (D01 only) | one-word answer | weak: guessable, pointed |
| h3 | D04 l.33 $2,500 at 0.5%; D01 l.95 0.22% = $1,075; 1% HRP threshold in both | premium arithmetic for a $500,000 home | calculate across documents | 0.22% vs 0.215% rounding | D01 restates every D04 parameter, so D04 is replaceable | dropped: necessity fails |
| h4 | D04 l.36/fn 4 (0.4 ppt ~ 10%, 4% yield), l.43 (1 ppt ~ up to 20%); D01 l.308 linear use (0.05 ppt -> 1.25%) | price fall implied by a VaR rise | exact vs rounded | linear vs user-cost form give different falls | two defensible methods | dropped: one-answer risk |
| h5 | D04 l.106 0.5% = 74,000 properties; D01 l.95 4% HRP 2020 | HRP dwelling count (~592,000) | derived base | 3 1/2% (D04) gives ~518,000 | "around 0.5 per cent" moves the base 13.5-16.4m | dropped: no supported precision |
| h6 | D08 l.13 380 Mt (2017/18); D05 l.108 Bowen Basin ~1/3 of coal exports | Bowen Basin export tonnage (~127 Mt) | calculate across documents | 510 Mt production base | period of D05's share unstated; two lookups + one operation | weak |
| h7 | D08 l.16 coal 14% of exports; D05 l.15 commodities two-thirds | coal share of commodity exports (~21%) | calculate across documents | coal 1/4 of resource exports | "around"/period mismatch | weak |
| h8 | D06 exec summary rounded vs ch. 8 exact (l.188, 1498-1513) | post-2033-34 remainders by option | exact table vs rounded prose; period remainder | rounded route gives 4 vs exact 4.6 ($bn) | single document | dropped: needs a second document |
| h9 | D07 "APRA-regulated institution" (l.91); D01 fn 10 issuer types; D01 Table 2 deal counts | deals from APRA-regulated sponsors | conditional filter | non-banks | D01 itself calls ADIs APRA-subject; Table 2 counts 264 vs text 283 deals, column order inferred | dropped: D07 not needed; table unreliable |
| h10 | D04 fn 10 FY2020 oil & gas $25bn; D06 LNG facts | any | - | - | figures never connected | dropped: contrived |
| h11 | D02 rent/6% asset rule, previous 4% rate | 2015 water asset at the old rate | - | - | single document | dropped |
| h12 | D01 l.95 ~4% of dwellings HRP in 2020; D04 l.106 "around 0.5 per cent of properties (or 74,000 properties)" | dwellings high-risk in 2020, 0.04 x 74,000 / 0.005 = 592,000 -> 600,000 (nearest 100,000) | derived base (unit normalization) | D04's "currently" 3 1/2% gives 518,000 -> 500,000; recalled ABS stock (~10.8m) gives ~430,000 | product of two "around" figures the documents never connect; two candidate shares; "how many" sends every solver to the bundle's only share-and-count pair | dropped after round 1, not offered |

Families the calibration note shows the strong solver clearing (not to be offered as High designs): two lookups plus
one operation, explicit list diffs, plainly stated rules pointed at by the question, name/string joins, period
remainders inside one document.

## Independent author B (resources cluster D08, D05, D06, D02), 2026-10-14

Verdict returned: nothing in Docs 5-8 meets the strong-solver bar; no parallel-rule asymmetry (D05 and D08 agree on
every shared fact), no component outside a headline figure, no outside definition that makes the natural figure wrong.
Its two best sketches, both not offered:

- B-i01 coal's share of commodity exports since 2015, 14% / (2/3) = 21% (D08 l.16 x D05 l.15; decoy D08 l.14
  one-quarter of resource exports = 25%). 0 unpointed steps ("commodity" points at D05's sentence); D05's two-thirds is
  undated; delete-and-guess fails on D08 (a recalled ~14-15% coal share gives 21-22%, within a few percent), closed-book
  ~22% likewise. Dropped.
- B-i02 Bowen Basin share of 2017/18 coal exports, 380 / 3 = 127 -> 130 Mt (D05 l.108 x D08 l.13). 0 unpointed steps;
  D08's 380 Mt is widely reported, so delete-and-guess reaches the gold without D08. Dropped (same as h6).
Its other hooks, all dropped: oil low US$28 vs Callaghan US$65 (contrived, recallable); LNG $70bn (2021-22) vs coal
$67bn (2018) (different years); LNG 21% of trade vs coal ~30% of export volumes; NZ rent/6% against PRRT settings
(cross-country); NZ renewables 79% vs coal shares of generation; D06 executive-summary rounding and Table 8.1's split
low-price row (single document); Callaghan WTI vs Brent (no second-document input); Debbie -50% coking vs
metallurgical (same figure); scope 3 definitions (method, not world); cap start dates (single document; financial vs
calendar "year of first production"); GWh-to-PJ conversion (public knowledge); implied rural share of exports
(unsupported precision, gold's treatment unknown); bank coal and oil-and-gas exposures vs export values (contrived).
