# aq-docket-trial-02 - cross-document hooks

Target: medium (user, 2026-10-06: "at least Medium", one attempt). Caller-written from a full read of
D09-D12 and the guidance/segment/event passages of D02-D08 plus D01, before the merged map. Local ids
D01-D12 equal the platform's Doc 1-12. Line numbers are text/Dnn.txt lines.

Bundle shape: one company (Colgate-Palmolive), ten quarterly/annual releases Q1 2024 - Q2 2026, one
2026 segment recast exhibit (D10), one 2019 award-agreement form (D01, Exhibit A blank: no performance
period or criteria, so no join to the releases).

Segment structures (deciding facts for h1-h4):
- S1 (to Q2 2024; D02, D03): part of skin health in Europe, the rest in North America.
- S2 (effective July 1, 2024; D04-D09): "The results of the skin health business previously reported
  within the Europe reportable operating segment are reported with the other skin health businesses in
  the North America reportable operating segment" (D04 l.88, D05 l.113, D06 l.85).
- S3 (effective Q1 2026; D10-D12): "The results of the Europe and Africa/Eurasia (excluding Russia and
  Belarus) reportable operating segments and the skin health business (previously within the North
  America reportable operating segment) have been combined in a new Europe, Middle East & Africa
  reportable operating segment. In conjunction with this realignment, Russia and Belarus, which were
  previously reported within the Africa/Eurasia reportable operating segment, are now reported within
  the Asia Pacific reportable operating segment." Only D11 l.85 states this; D10 has no notes on it and
  D12 l.83 says only "recast ... to conform to the reporting structure effective for the quarter ended
  March 31, 2026".
- Script check (scratchpad recast.py): FY2025 net sales give the same derived values by every route:
  skin health 366 (NA 4,045 - 3,679; or EMEA route), Russia/Belarus 224 (AP 3,038 - 2,814), former
  Africa/Eurasia operations inside EMEA 948 (1,172 - 224; or 4,276 - 2,962 - 366). FY2024 sales/OP also
  agree but S2 FY2024 is duplicated in D05 and D09. FY2025 OP, Q2-Q4 2025 sales, 9M sales disagree by
  $1M between routes (rounding): unusable at $1M precision.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D11 l.85 (S3 composition); D09 l.463-464 (FY2025 AP 2,814, A/E 1,172), l.462 Europe 2,962, l.460 NA 4,045; D10 l.25-28 (FY2025 S3 NA 3,679, EMEA 4,276, AP 3,038) | EMEA's 2025 net sales from former Africa/Eurasia operations = 948 (never printed) | Match, then exclude (A/E minus the Russia/Belarus carve-out); scatter the pieces | Printed A/E 2025 1,172 (D09) and EMEA - Europe 1,314; omit the exclusion -> 1,172 | D11 is the only composition source; R&B never printed; OP version has route conflicts (195/196) | sketch i01 (lead) |
| h2 | D09 l.71 impairment "related to the skin health business"; D11 l.85; D09 l.460; D10 l.25 | 2025 net sales of the impaired business (skin health) = 366 | Scatter the pieces; event bridge | EMEA - Europe - A/E = 142 (forgets R&B); impairment $794M/$919M | NA route is direct once D11 is read | sketch i02 |
| h3 | D11 l.85; D09 l.463 (AP 2025/2024 2,814/2,858); D10 l.28, l.59 (3,038/3,074) | Russia/Belarus net sales change 2024->2025 = 224/216 -> +3.7% | Calculate across documents; unit/scope normalization | Printed A/E +7.0% (D09 l.583), AP -1.5% (D09 l.581) | FY2024 S2 also in D05 (D09 still unique for 2025) | sketch i03 |
| h4 | D09 l.71, l.491 (impairment in Corporate), l.477 Q4 NA OP 203; D10 l.25/l.333 (FY 790, 9M 583); D11 l.85 | Skin health segment operating result in Q4 2025 = 203 - (790 - 583) = -4 (EMEA route also -4) | Mentions vs does (impairment is Corporate, not segment); unreported period | Impairment 919/794; FY2025 -6/-5 | Three inference steps: too-hard risk; wording of "segment measure" | sketch i04 (stretch) |
| h5 | D07 l.41 ($200-$300M, Aug 1 2025); D11 l.39 ($350-$550M from April 30 2026, "increased from"); D09 Table 9 restructuring 13 (2025); D12 Table 9 SGPP pretax 305 (1H 2026), segment note $300 (OP) | Share of the latest cumulative pretax charge estimate recorded by June 30 2026 = 318/450 | Exact line item; calculate across documents | OP 300 -> 69.6%; old estimate 250 -> 127%; 1H only 67.8% | Two stated "charges" (300 OP vs 305 pretax) -> answered-inconsistently risk | sketch i05 (risky) |
| h6 | FY2025 organic guidance D05 l.75 (3-5%), D06 l.47 (2-4%, no "previously"), D07 l.49, D08 l.45; actual D09 l.33 | Gap of actual vs a chosen edition's midpoint | Same series, right edition | Later editions | No dated untied event between Jan 31 and Apr 25 2025 in D06; every other change prints "(versus ... previously)" in the later release | not pursued |
| h7 | FY2026 gross margin guidance D09 l.81 (expansion), D11 l.49 (down, "versus up previously"), D12 l.49 (roughly flat, "versus down previously") | Direction in force at an event | Same series | Same-release "previously" text | One-word, three-option answer; one-passage answers | not pursued |
| h8 | S1->S2 (July 2024) Europe-held skin health: D03 l.416 (Q2 2024 Europe 720; 6M 1,432) vs D07 l.436 (685; 1,358) | 1H 2024 Europe-held skin health sales 74 | Who belongs where | none salient | Mapping in D04-D06 (none individually necessary) | backup |
| h9 | Market share YTD series (each release headline) | ranking/count | Ordered answers | n/a | Pure lookups (trial-07 q05 profile) | not pursued |
| h10 | ERISA Q4 2025 reclass: D09 Table 8 SG&A (84) vs non-service +84 | net pretax effect 0 | Mentions vs does | n/a | One document | not pursued |

The map is navigation; quotes come from text/Dnn.txt. A short valid calculation or ID join is eligible.
Prior failures suggest tests/priority, not a universal veto.
