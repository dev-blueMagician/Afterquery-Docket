# Independent author B, round 1 (question-author subagent, Claude Code Opus 5.5), 2026-10-07

Brief: other Guide levers (match then exclude, mentions vs does, hedge, who belongs where, status filters,
ordered answers, practitioner scenario, what changed), target medium/hard; told not to read notes/hooks.md,
ideas.md, sketches/ or questions/. Raw final report preserved below (lightly reformatted, content unchanged).

## Bottom line (author)

One design with a real untied decoy across two documents, iB1; promote only that one. iB2 worth a cheap
screen at most. iB3-iB5 cover the requested lever shapes but are expected Easy.

| id | lever | gold | Medium-or-better estimate |
|---|---|---|---|
| iB1 | status filter + computed figure | 12.8 | ~35% |
| iB2 | look-alike measure | 12.8 pp | ~10% |
| iB3 | mentions vs does | 398 MW | ~6% |
| iB4 | temporal alignment | 1.73 | ~5% |
| iB5 | what changed / planned vs available | 19.5% | ~4% |

What the bundle supports: 20 unrelated country chapters, one edition each, no cross-citations; no
forecast/actual pairs or edition traps across documents. Strong decoys sit inside single documents; the one
both untied and answer-shaped is Korea's printed 26 GW installed total against its reactor table.

## iB1 (promoted): operating nuclear capacity, Korea vs South Africa

- question (28 words): "As of September 2025, South Korea's nuclear reactors in operation had a combined capacity equal to how many times South Africa's nuclear generating capacity? Give one decimal place."
- answer: 12.8 (times). documents: D15 = Doc 4; D14 = Doc 12.
- facts: D15 L165 "Korea has 26 nuclear reactors, 23 of which are currently in operation, with total installed nuclear generating capacity of approximately 26 gigawatts electric (GW(e))." D15 Table 2 (L167-318, "Data as of September 25, 2025"): exactly 23 rows "in operation": Shin-Kori-1/2 1,000 each; Saeul-1/2 1,400 each; Wolsong-2/3/4 700 each (PHWR); Shin-Wolsong-1/2 1,000 each; Hanbit-1/2 950 each, Hanbit-3 to -6 1,000 each; Hanul-1/2 950 each, Hanul-3 to -6 1,000 each; Shin-Hanul-1/2 1,400 each; total 23,500 MWe. D14 L20: "Eskom operates the country’s only nuclear plant, at Koeberg, near Cape Town, where two reactors completed in the 1980s have a combined generating capacity of 1,830 MW."
- universe (32 rows): included the 23 "in operation" (23,500); excluded idle Kori-2 (650; "Taken offline on 3/8/23, 9/28/24, and 8/6/25 and waits for a decision on its operation license renewal"), Kori-3/Kori-4 (950 each; no status; the other two of the three installed-but-not-operating units implied by "26 … 23 in operation"); not yet operating Saeul-3/4 (1,400 each; "Expected to be in operation in the first half of 2026" / "in 2027"), Shin-Hanul-3/4 (1,400 each; "by Oct. 2033"); closed Kori-1 (587, 6/18/17), Wolsong-1 (679, 12/24/19). South Africa: one plant, two reactors, 1,830 MW ("10 GW of new nuclear" a plan; SAFARI-1 a research reactor).
- dependency: the Korea operating figure exists only as the table sum ("23,500"/"23.5" nowhere); Koeberg/1,830 only in D14; Korea elsewhere only as POSCO E&C (D11). Removal risk D15 ~10-15% (a model most likely uses ~26 GW -> 14.2); D14 ~5% (recalled 1,860 or 1,940 MW -> 12.6 or 12.1). Closed-book likely miss (~85-90%).
- levers: status filter; figure that must be computed (exact table sum vs rounded installed prose figure).
- wrong routes: prose 26 GW 26,000/1,830 = 14.2 (all 26 installed rows 26,050 also 14.2); every row containing "in operation" (27 rows incl. the four "Expected to be in operation…") 29,100 -> 15.9; blank Kori-3/4 as operating 25,400 -> 13.9; adding Saeul-3 24,900 -> 13.6; pro-rata 23/26 x 26 GW = 23,000 -> 12.6; all 32 rows 32,916 -> 18.0.
- arithmetic: 23,500/1,830 = 12.8415 -> 12.8 (integer inputs; one decimal stable). Difference form 21,670 MW.
- shortcut search: operation/GW(e)/Koeberg/1,830/23,500/23.5 across all 20 docs; best route prose (23 of 26) -> filter Table 2 -> sum -> divide.
- tags: Cross-document join, Conditional filter, Aggregation (Temporal alignment optional).
- risks: Kori-3/-4 blank status (prose count settles it; a reviewer may probe); flattened table "hard to parse" critique; a medium model that sums cleanly -> Between levels; a systematic table misread by the high model -> Answer not supported.
- harder variant (practitioner, two plain conditions): "A U.S. supplier of pressurized-water-reactor fuel is comparing markets. As of September 2025, South Korea's pressurized water reactors in operation had a combined capacity equal to how many times South Africa's nuclear generating capacity? Give one decimal place." PWR-only 23,500 - 2,100 = 21,400 -> 11.7; skipping the type filter gives 12.8. Overshoot risk.
- author reasoning steps: (1) Doc 4: 26 reactors, 23 in operation, ~26 GW(e) installed; (2) Table 2 marks exactly 23 rows "in operation", sum 23,500 MWe; (3) excluded Kori-2/3/4 (2,550 MWe), Saeul-3/4 and Shin-Hanul-3/4 (n/a; expected 2026, 2027, 2033), Kori-1 and Wolsong-1 (shut); (4) Doc 12: Koeberg 1,830 MW, only plant; (5) 23,500/1,830 = 12.84 -> 12.8.
- evidence quotes proposed (verify against text): Doc 4 L165 sentence above; "Taken offline on 3/8/23, 9/28/24, and 8/6/25 and waits for a decision on its operation license renewal"; "Former Shin-Kori-5 Expected to be in operation in the first half of 2026."; "Permanently shut down on 12/24/19 (Data as of September 25, 2025)"; row example "04/30/10 | 04/05/24 | in operation" (capacity cells sit on their own lines; multi-line quotes need a verbatim test); Doc 12 L20 sentence above. Roles: both Answer component.
- failure modes proposed: (1) Part vs total / Takes the wrong line item: the printed ~26 GW(e) installed total -> 14.2. (2) Out-of-range period / Wrong members in a list: keyword "in operation" keeps the four "Expected to be in operation…" units -> 15.9 (adding only Saeul-3 -> 13.6). (3) optional, weakest: Figure that must be computed / Misapplies a rule or premise: pro-rata 23/26 x 26 GW -> 12.6.

## iB2: gas share of 2024 electricity, UK vs Germany (realistically Easy)

"In 2024, how many percentage points higher was gas-fired generation's share of total electricity generation in the United Kingdom than in Germany? Give one decimal place." -> 12.8 pp. D18 L12 (26% gas, 2024) and D06 L19 (56.9 TWh of 431.7 TWh = 13.18%). Decoys: UK 38% (2023 total energy supply) -> 24.8; Germany 25.9% (primary-energy mix) -> 0.1; both -> 12.1; Germany 8.9% (growth) -> 17.1; "about 430 TWh" -> 12.8. Removal: D18 moderate (25-35%, UK ~26% may be recalled); D06 low-moderate. Variant if both proceed: Korea 28.1 - Germany 13.18 = 14.9 (shares D15 with iB1; Korea 28.1% is recalled exactly per the caller's rev 0 tests).

## iB3: mentions vs does, green-hydrogen electrolyser capacity (Easy expected)

"Counting only green hydrogen projects that had reached financial close or begun construction, what was their combined electrolyser capacity, in MW, across Chile, Uruguay and the United Arab Emirates?" -> 398 MW (Chile D03 L19 396 MW in construction + Uruguay Khairos D19 L35 2 MW, financial close). Decoys: + Masdar-Engie 200 MW -> 598; + Helios 800 MW solar -> 1,198/1,398; Uruguay omitted -> 396; Chile omitted -> 2. D17 decoy-only (unticked).

## iB4: Korea vs mainland Portugal, January-November 2025 (Easy expected)

"Over January–November 2025, South Korea generated how many times as much renewable electricity as mainland Portugal? Give two decimal places." -> 1.73 (57.6 TWh / 33,271.6 GWh). Decoys 1.30, 18.70, 6.83, 1.90, 1.96. Stable 1.7286-1.7339. Post-cutoff data, low removal risk.

## iB5: planned vs available storage, Chiren vs Poland (Easy expected)

"In the 2025-26 autumn-winter season, the storage volume available at Bulgaria's Chiren gas facility was what percentage of Poland's domestic gas storage capacity at the end of 2024? Give one decimal place." -> 19.5% (650 mcm / 3.33 bcm). Decoys 30.0, 16.5, 19.8, 19.7.

## Hooks tried and rejected (author)

- WtE sums (Israel, Poland, UAE): Tamar vs southern Israel not explicitly linked; Poland "Eleven … seven completed" readable as 7 of 11 or 11 + 7; Dubai no tonnage; Sharjah "Phase 2" undefined.
- Vietnam PDP8 -> PDP8R: single-document; 2030 capacity pair and offshore wind inconsistent.
- EU REPowerEU 45% vs RED 42.5%: public knowledge (closed-book fail).
- Acronym collisions (IEC, CFE, EVN, National Energy Commission, SIN, PLN, MBR, EIA): trivia or invented ambiguity.
- Company links (OMV Petrom, NewMed, POSCO E&C, ZTE, Westinghouse, Fluor, Noble Corporation vs Noble Energy): keyword-findable, public, or matching numbers.
- NTCSA/NSMO/NESO independence in 2024: NTCSA open to two readings.
- Ordered rankings of shares: removal check fails (priors fill the missing country).
- PHWR fleets Korea + Romania: Romania 2 x 650 MWe recallable.
- Single-document traps (Germany US-LNG, Chile 2023 capacity, Bulgaria 41.6 vs 40.38): tied or precision splits.
