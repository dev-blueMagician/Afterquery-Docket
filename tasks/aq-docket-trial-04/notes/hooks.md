# aq-docket-trial-04 - cross-document hooks

Target: medium (user, 2026-10-06). Caller-authored from a full read of D01-D06 and D08 and
targeted reads of D04/D07. Local ids: D03 = Doc 5, D05 = Doc 3; the rest coincide.

Edition facts that drive necessity: D06 and D08 print identical FY2021 actual, FY2022 actual
(country totals) and FY2023 estimate / "est. actual" figures, so neither is individually
necessary for those years. Edition-unique inputs: FY2023 requests and FY2022 estimates (D05
only), FY2024 requests and FY2022 actuals by account (D06 only), FY2025 requests and the FY2025
bills (D08 only), FY2023 global appropriations by FAA chapter (D04 only).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D05 Table 2 "FY2023 (req.)" (L541-1080), D06 Table 2 "FY2024 (request)" (L357-452), D08 Table A-1 "FY2025 (request)" (L703-810), thousands | Countries whose request fell in both successive requests: Colombia, Mexico, Peru, Venezuela | Scatter the pieces; Bury one list item late (Peru is table-only) | Decoys: printed "% Change" columns use the FY2023 estimate as base (gives Costa Rica, Honduras, Jamaica, Nicaragua, Panama, T&T...); El Salvador flat then falls; State Central America Regional falls twice but is a program | 4-item list (list-contract advisory); D05 table is one value per line | sketch i01 |
| h2 | D05 Table 2 FY2023 req; D08 A-1 FY2025 req and its "% Change: FY2023-FY2025" column (base = FY2023 est. actual) | Country with the largest % decline FY2023 request -> FY2025 request: Honduras, 35% (35.33% thousands, 35.36% millions) | Same series, right edition; Calculate across documents | D08 column route: Costa Rica -95%; Honduras via D08 column -39%; FY2024-request base (D06) Honduras -37%; prose-only countries: Mexico -23%; absolute: Colombia; non-country USAID Central America Regional -59% | Precision: one decimal splits 35.3/35.4, whole percent agrees | sketch i02 (lead) |
| h3 | D05 FY2023 req (summaries) vs D08 FY2025 req for the four countries D08 says the request prioritized | Rank/superlative among Colombia, Haiti, Mexico, Venezuela | Ordered answers | D08 prose bases on FY2023 estimate (Mexico +4.9% vs -22.5%) | Both summaries print all eight inputs: short lookup path | rejected (too easy) |
| h4 | D04 Table 3 FAA chapters (INCLE Part I ch 8 L1069; ESF Part II ch 4 L1285) + D08 A-3 Haiti FY2025 by account + D03 part I gloss | Haiti FY2025 request in accounts carrying out FAA part I: $349.4M | Who belongs where; Mentions it vs does it | D08/D03 grouping (development = DA+ESF+GHP) gives $187.4M; DA+GHP gives $180.4M | High model may know FAA structure without D04 (removal flag) | backup i03 |
| h5 | D05 FY2021 (excl. P.L. 117-2) vs D06/D08 FY2021 actual (incl. ARP) | Country ARP amounts (e.g. Haiti 14.8; differences sum to 97.15 = D06 note) | footnote that changes coverage | n/a | D06/D08 duplicate FY2021 actuals: only one document individually necessary | rejected (necessity) |
| h6 | D05 A-2 FY2022 est vs D06 A-1 FY2022 actual ESF ("a" marks) | Per-country share of the $64.0M Ukraine supplemental (sums exactly to 64.0) | Calculate across documents | n/a | Per-country amounts never stated; relies on unchanged base (Mexico/USAID LAC ESF shifted) | rejected (unsupported inference) |
| h7 | D05 P.L. 117-328 Colombia $487.4M; D06 FY2024 $377.5M and "$75.6 million less than Congress appropriated ... in FY2023" | FY2024 vs FY2023 designation (109.9) | Reconcile documents that disagree | D06 printed 75.6 | 377.5 also in D08; D06 wording makes 75.6 defensible | rejected (necessity, two readings) |
| h8 | D02 653(a) 30 days / Section 7019 10% rule + enactment dates/designations in D05/D06 | Due dates; deviation % | Calculate across documents | n/a | Public dates; FY2023 allocations duplicated in D06/D08 | rejected |
| h9 | D05 Venezuela crisis $656.3M FY2022; D06 $591.0M FY2023 | Two-year sum $1,247.3M | Scatter the pieces | D08 MRA obligations $543.9M | Two keyword lookups | rejected (too easy) |
| h10 | D05 Central America bilateral share 44.4%; D08 components (87.7+115.8+86.3+17.1 of 632.6) | Share change +4.1 pp | Calculate across documents | Northern Triangle only | Definition applied to unreported period (Easy-level mechanism) | not pursued |
| h11 (2026-10-06, after q03 passed) | D05 Table 2 "FY2021a" column (note a: excludes P.L. 117-2) vs D06 Table 2 FY2021 (note a: "sums include some" ARP; Table 1 note a: $97.2 million) and D08 A-1 FY2021 ("a" marks on exactly the rows that differ); D06 Table 2 FY2024 request | Per-country ARP money is printed nowhere; the edition difference gives it (row differences sum to 97,150 = D06's $97.2 million). South American maximum: Peru 13,350 (Colombia 13,100). Peru's FY2024 request over FY2021 aid without ARP: +26% | Same series, right edition; Match, then exclude; Scatter the pieces | Same-row FY2021 figure that includes ARP (D06 Peru 98,885, unmarked): +9%; D06's printed % column (FY2023 est. base) +7.2%; Colombia as the guess: -5%/-7% | Per-country ARP is an inference from two editions (supported by notes, "a" marks and the exact total); D05 one value per line, D06 pipe rows (Save passage) | sketch i05 |

Rejected within-document conflicts (avoid as inputs): D05 summary CBSI "$82.5 million" vs body
and Table 4 "82.0"; D06 summary "$427.3 million" vs body "$427.4 million"; D06 "$77.0 million in
IMET aid" for Colombia while stating IMET is not designated; D06 Table A-3 DA total "90.7"
(Table 1: 970.7); D06 "P.L. 118-147" typos; Bahamas 200/250/300 (thousands) vs 0.2/0.3/0.3
(millions) breaks any "rose in both" list.
