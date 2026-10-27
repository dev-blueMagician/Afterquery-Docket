# i03 strong-solver screen: raw returns (2026-10-15)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i03-screen-c2521047f0b79326/solver-1 and the exact sentence. Gold: 2.52.
Returns kept in substance below (the harness indents subagent reports; indentation removed).

## Solve 1: 2.52 (right), confidence high

answer: 2.52 (net debt divided by trailing-twelve-month EBITDA, in times)
path: D02 L154 target on Net debt (D01 L158 same; D01 L23 "target debt-to-EBITDA leverage ratio of 2 to 2.5
times"); D02 L108 method in use 2.38 -> 2.4; EBITDA definition D02 L246 / D08 L175 (unadjusted); net debt
D08 L129-131, L103: 11,699.8 - 216.9 = 11,482.9; EBITDA FY2025 4,480.1 (D02 L256), Q1 2026 998.2 and Q1 2025
917.7 (D08 L187; D05 L189); TTM 4,560.6, cross-checked by quarters and by D08's own TTM net income,
depreciation and amortization; 11,482.9 / 4,560.6 = 2.51785 -> 2.52.
minimal_documents: D02 + D08.
readings: covenant gross 2.57 (D08 L168; covenant EBITDA undisclosed); Adjusted EBITDA 2.46 (rejected: target
uses EBITDA); FY2025 EBITDA 2.56 (wrong period).
gaps: none material; D08 read in full, others by section and search.
contaminated: no

## Solve 2: 2.52 (right), confidence high

answer: 2.52x (net debt / TTM EBITDA at March 31, 2026); noted the result sits just above the 2.0-2.5x range.
path: D02 L154 definition; D02's 2.4x check uses unadjusted EBITDA (Adjusted would give 2.31 -> 2.3);
FY2025 4,480.1 reconciled from components; Q1 EBITDA reconciled; TTM 4,560.6 (also by quarters); net debt
11,482.9; 2.5178 -> 2.52; bounds check.
minimal_documents: D02 + D08 (D05/D09 can stand in for Q1 EBITDA, not for the March 31, 2026 balances).
readings: covenant 2.57 (question says "leverage target"); Adjusted 2.46 (contradicts definition and the 2.4x
example); FY2025 2.56 (ignores the twelve-month window).
gaps: covenant EBITDA undisclosed (affects only the covenant reading).
contaminated: no

## Solve 3: 2.52 (right), confidence high

answer: 2.52 (times; 11,482.9 / 4,560.6 = 2.5178)
path: D02 L154 and D01 L158 definitions; EBITDA definition; FY2025 4,480.1; Q1 2026 998.2, Q1 2025 917.7;
TTM 4,560.6 (quarter cross-check; D09 confirms Q1 2026 unrevised); net debt 11,482.9; 2.52.
minimal_documents: D02 + D08.
readings: gross 2.57 "Based on the loose D01 line 23 wording ('target debt-to-EBITDA leverage ratio of 2 to 2.5
times') or the covenant's total-indebtedness definition (D08 line 168)", weaker; Adjusted 2.46; FY 2.56.
gaps: none material.
contaminated: no
