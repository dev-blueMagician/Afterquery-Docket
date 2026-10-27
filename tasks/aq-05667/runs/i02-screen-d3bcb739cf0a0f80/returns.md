# i02 strong-solver screen: raw returns (2026-10-15)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i02-screen-d3bcb739cf0a0f80/solver-1 and the exact sentence. Gold: -0.3%.
Returns are kept verbatim below (the harness indents subagent reports; indentation removed).

## Solve 1: -0.3% (right), confidence high

answer: −0.3%
confidence: high
path: D02 L35 FY CBG 3,166.4 / 3,108.0; D02 L42 Suvinil "contributed $164.5 million, or 5.3%"; all in
Q4 (D02 L40, D08 L36 "October 2025 acquisition"; D07 L56 nine-month acquisition impact "— %"; D07 L162
"deposit held for the Suvinil acquisition"); D07 L56 9M 2,341.7 / 2,445.8; quarterly sums reconcile
(762.2 + 809.4 + 770.1 = 2,341.7; 811.0 + 844.3 + 790.5 = 2,445.8). Q4 2025 824.7; Q4 2024 662.2;
ex-Suvinil 660.2; change −2.0/662.2 = −0.302% -> −0.3%; rounding band −0.26% to −0.34%.
minimal_documents: D02 + D07 (D04 can supply 9M 2024, D01 FY2024; D07 needed for Q3 2025).
readings: +24.5% with Suvinil (not asked); −3.4% full year (wrong period); ex-Suvinil and currency not
computable (not asked).
gaps: no direct Q4 table; Suvinil-all-in-Q4 inferred from the October date and the 0% nine-month impact.
contaminated: no

## Solve 2: -0.3% (right), confidence high

answer: -0.3% (CBG net sales excluding Suvinil $660.2M in Q4 2025 vs $662.2M in Q4 2024)
confidence: high
path: D02 L35 FY figures (D01 L38 confirms 3,108.0, no restatement); D02 L42 $164.5M = 5.3% (164.5/3,108.0
= 5.29%); all of it in Q4 (D02 L40/L42, D08 L36 "October 2025 acquisition"; D07 L162 deposit at Sept 30;
D07 "— %" acquisition column Q3 and 9M); D07 L56 9M; Q4 2025 824.7, Q4 2024 662.2, ex-Suvinil 660.2,
−0.302% -> −0.3%; percentage-point cross-check 24.54 − 24.84 = −0.30; using 5.3% × 3,108.0 = 164.7 gives
−0.33%, still −0.3%. Searches for "fourth quarter", "Q4", "three months ended December" found only
treasury retirement, dividends, inventory policy.
minimal_documents: D02 + D07.
readings: (a) +24.5% including Suvinil; (b) −3.4% full year; (c) also excluding currency not
determinable to one decimal (about −1.0% to −1.8%), not asked.
gaps: Q4 derived (FY − 9M); Suvinil wholly in Q4 assumed with support; D02 read L1-170, D07 L1-75 and
L155-179, D08 L24-39, rest by search.
contaminated: no (only auto-attached git status and e-mail in context)

## Solve 3: -0.3% (right), confidence high

answer: -0.3% (Consumer Brands Group net sales fell by about 0.3% in Q4 2025 versus Q4 2024 when Suvinil
is left out)
confidence: high
path: no Q4 segment figure printed (only "fourth quarter" hits: treasury stock, LIFO); D02 L35 FY; D02 L42
$164.5M (5.29% = 5.3% column, Suvinil the only acquisition effect); D07 L56 9M with "— %" acquisition
impact, Q3 "— %", D07 L162 deposit -> all $164.5M in Q4; cross-checks D01 L38, D04 L52, quarterly sums;
824.7 − 164.5 = 660.2; (660.2 − 662.2)/662.2 = −0.302% -> −0.3%; rounding band −0.34% to −0.26%.
minimal_documents: D02 + D07.
readings: Q4 ex-Suvinil −0.3% (main); exclusion applied to both periods same; full year −3.4%; with
Suvinil +24.5%; currency removal not asked and not determinable.
gaps: Q4 derived; D01, D03-D06 only table rows; D02 past L80 unread; D07 L1-80 and L158-177; D08/D09
net-sales sections.
contaminated: no
