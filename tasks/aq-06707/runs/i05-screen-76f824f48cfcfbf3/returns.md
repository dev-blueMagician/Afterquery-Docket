# i05 strong-solver screen: raw returns (2026-10-18)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i05-screen-76f824f48cfcfbf3/solver-1 and the exact sentence. Gold: -$239.2 million.
Returns kept in substance (harness indentation removed), numbered by launch label (arrival order: 2, 1, 3).

## Solve 1: -239.2 (right), confidence high

answer: -239.2 (a decrease of $239.2 million)

path: (1) D09 balance sheet (text L331-360, p.14) has only two long-term liability lines, "|Long-term operating lease liabilities|1,846.5|1,544.4|" and "|Other long-term liabilities|1,269.5|1,014.6|"; no "Long-term finance lease liabilities" line, which appears only in D03, D06, D08, D01 and is absent from D04, D07, D09, D02, D05. (2) D08 balance sheet (L352-382): "|Long-term finance lease liabilities|112.8|376.1|", "|Other long-term liabilities|901.8|877.7|" (Dec 31, 2024 | Dec 31, 2023). (3) Mapping: 901.8 + 112.8 = 1,014.6, exactly D09's restated Dec 31, 2024 figure; every other Dec 31, 2024 liability line identical in D08 and D09 (other current 363.0, total current 3,564.6, LT operating lease 1,544.4, equity 16,409.6, total 22,533.2); totals foot in both (D08 2023: 3,547.4 + 348.6 + 376.1 + 877.7 + 17,580.4 = 22,730.2; D09 2024: 3,564.6 + 1,544.4 + 1,014.6 + 16,409.6 = 22,533.2) → the 2025 presentation folds LT finance lease liabilities into other LT liabilities. (4) Dec 31, 2023 on the 2025 basis: 877.7 + 376.1 = 1,253.8 (D03 L368-370 and D06 L362-364 print the same 376.1 and 877.7). (5) Change: 1,014.6 - 1,253.8 = -239.2; cross-check (901.8 - 877.7) + (112.8 - 376.1) = 24.1 - 263.3 = -239.2. (6) docs/ originals match.

minimal_documents: D08 + D09 (D01 + D03/D06 can replace D08; D04 or D07 give 1,014.6 but are mid-2025 sheets; D02/D05 confirm the Dec 31, 2025 structure without Dec 31, 2024).

readings: As originally reported, 901.8 - 877.7 = +24.1 (contradicts "presentation used at December 31, 2025"); mixed bases 1,014.6 - 877.7 = +136.9 (not a consistent basis); wrong period (change during 2025) 1,269.5 - 1,014.6 = +254.9. Only -239.2 defensible.

gaps: No release footnotes the reclassification (searched "reclassif", "conform", "recast", "prior period", "combined with", "presentation"); merger inferred from the exact match. No document prints Dec 31, 2023 on the 2025 basis (rebuilt). Balance sheets of D01, D03, D04, D06, D08, D09 read in full; D02, D05, D07 by targeted searches.

contaminated: no

## Solve 2: -239.2 (right), confidence high

answer: -239.2 (other long-term liabilities fell by $239.2 million during 2024, on the December 31, 2025 presentation)

path: (1) D09 (L337-359, header "|December 31, 2025|December 31, 2024|"): only "Long-term operating lease liabilities|1,846.5|1,544.4|" and "Other long-term liabilities|1,269.5|1,014.6|"; no finance lease line → Dec 31, 2024 = 1,014.6 on this presentation. (2) D08 (L358-381): "|Long-term operating lease liabilities|1,544.4|348.6|", "|Long-term finance lease liabilities|112.8|376.1|", "|Other long-term liabilities|901.8|877.7|". (3) 901.8 + 112.8 = 1,014.6 exactly; all other Dec 31, 2024 lines identical (AP 3,201.6, other current 363.0, total current 3,564.6, LT op lease 1,544.4, equity 16,409.6, total 22,533.2); D09 ties 3,564.6 + 1,544.4 + 1,014.6 + 16,409.6 = 22,533.2 → newer presentation folds LT finance leases into other LT liabilities; no footnote states it (searched reclass, conform, prior period, presentation, combined, finance lease); mapping rests on the arithmetic tie. (4) Dec 31, 2023 restated: 877.7 + 376.1 = 1,253.8; residual check 22,730.2 - 3,547.4 - 348.6 - 17,580.4 = 1,253.8; D03 (L368-370), D06 (L362-364) repeat 376.1 / 348.6 / 877.7. (5) 1,014.6 - 1,253.8 = -239.2; components +24.1 - 263.3. (6) Combined presentation first in D04 (L347-348 "Other long-term liabilities|1,195.5|1,014.6"), continues in D07; D01 still split (finance 111.4/112.8, other 951.9/901.8); D02/D05 combined. (7) docs/ match.

minimal_documents: D08 + D09 (alternatives: D01 + D03/D06 for D08; D04/D07 for 1,014.6 with D02/D05 to confirm the Dec 31, 2025 presentation; D09 + D03/D06 alone via the residual method).

readings: As originally presented, +24.1 (ignores the explicit presentation); mixing presentations, +136.9 (not defensible); requested reading -239.2.

gaps: No document describes the reclassification; inferred from the exact tie and matching totals. Balance sheets of D04, D08, D09 read in full; others by targeted searches; narratives not read in full.

contaminated: no

## Solve 3: -239.2 (right), confidence high

answer: -239.2 (a decrease of $239.2 million)

path: (1) D09 (L333-359): below current liabilities only "|Long-term operating lease liabilities|1,846.5|1,544.4|" and "|Other long-term liabilities|1,269.5|1,014.6|"; no finance lease line → Dec 31, 2024 = 1,014.6. (2) D08 (L358-381): LT operating lease 1,544.4 / 348.6; LT finance lease 112.8 / 376.1; other LT 901.8 / 877.7. (3) All other Dec 31, 2024 lines identical; only difference 901.8 + 112.8 = 1,014.6 → the Dec 31, 2025 presentation includes LT finance lease liabilities in other LT liabilities; both columns foot (D09 2024 22,533.2; D08 2023 22,730.2). (4) Timing: D01 (Q1 2025) still separate at Dec 31, 2024 (L353-355); D04 (L348) and D07 (L332) already show 1,014.6 → merge from Q2 2025, in place at Dec 31, 2025; D02/D05 show Dec 31, 2025 = 1,269.5 with no finance line. (5) Dec 31, 2023 the same in D03 (L368-370) and D06 (L362-364). (6) 877.7 + 376.1 = 1,253.8; 1,014.6 - 1,253.8 = -239.2; components +24.1 - 263.3. (7) No footnote explains the reclassification (searched reclass, conform, recast, prior period).

minimal_documents: D09 + D08 (alternatives: D09 + D01 + D03/D06; D09 + D03/D06 alone with one inference; D04 or D07 for 1,014.6).

readings: Old presentation +24.1 (against "presentation used at December 31, 2025"); mixed bases +136.9 (not consistent); change during 2025 +254.9 (wrong year). No other defensible reading.

gaps: Mapping inferred from the exact line identity and balancing totals. Balance sheets of D01, D03, D04, D06, D08, D09 read in full; D02, D05, D07 by grep hits; narratives not read beyond keyword searches.

contaminated: no
