# i02 strong-solver screen: raw returns (2026-10-15)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i02-screen-a8db1fecfad6f0eb/solver-1 and the exact sentence. Gold: 1.5
percentage points. Returns kept verbatim in substance (harness indentation removed).

## Solve 1: 1.5 (right), confidence high

answer: 1.5 percentage points. The July 2026 outlook implies 6% to 7% growth, so the midpoint is 6.5%.
The July 2025 outlook expected about 8%.
confidence: high
path: (1) D03 "Full Year 2026 Guidance" table L197-203, Current column: "Comparable currency neutral EPS
excluding acquisitions and divestitures (non-GAAP)|7% to 8% growth|6% to 7% growth|" and "Comparable EPS
(non-GAAP)|9% to 10% growth, which includes: •Approx. 3% currency tailwind •Approx. 1% headwind from
acquisitions and divestitures|"; checked the original docs file, columns not swapped. (2) D03 L472
definitions treat them as separate measures; the July 2026 outlook does not state plain comparable currency
neutral EPS, so it must be worked out. (3) 9-10% minus ~3% = 6-7%; check 7-8% minus ~1% = 6-7%; midpoint
6.5%. (4) D02 L209 "comparable currency neutral EPS (non-GAAP) growth of approximately 8%. — Updated";
basis matches (L211 ~3% comparable EPS, L213 ~5% currency headwind "in addition to" ~1% A&D headwind;
3 + 5 = 8, so the 8% includes A&D); D02 L475 definition adjusts only for items and currency.
(5) 8.0 - 6.5 = 1.5. (6) Feb (D05 L223-225) and Apr (D01 L167-169) outlooks follow the same pattern.
minimal_documents: D02 and D03; D03 irreplaceable; D04 (Oct 2025, "approximately 8%. — No Update") could
stand in for D02.
readings: ex-A&D at face value (midpoint 7.5) -> 0.5, "ignores the word 'implied', D03's separate
definitions, and the fact that the 2025 figure of 8% includes acquisitions and divestitures"; currency removed
multiplicatively (1.095/1.03 - 1 = 6.3%) -> about 1.7, not the company's additive convention; D03 Prior
column (April, implied 5-6%) -> 2.5, wrong period; FY2025 actual 9% (D05 L119) -> 2.5, wrong measure.
gaps: none; the 8% is "approximately"; read outlook sections and definitions of D01-D05, not every table.
contaminated: no

## Solve 2: 1.5 (right), confidence high

answer: 1.5 percentage points
confidence: high
path: (1) D02 L209 "comparable currency neutral EPS (non-GAAP) growth of approximately 8%. — Updated";
check L211/L213: ~3% comparable EPS includes ~5% currency headwind "in addition to" ~1% A&D headwind,
3 + 5 = 8, so the 2025 measure removes currency only and the ~1% stays inside the 8%; D02 L475 definition.
(2) D03 table L197-203 Current column: ex-A&D 7% to 8%; comparable EPS 9% to 10% "which includes" ~3%
currency tailwind and ~1% A&D headwind; no direct figure for plain comparable currency neutral EPS.
(3) D03 L472 defines the measures separately. (4) 9-10% minus ~3% = 6-7%; cross-check 7-8% minus ~1% =
6-7%; midpoint 6.5%; components add arithmetically in Feb (D05 L223-225) and Apr (D01 L167-169) too.
(5) 8.0 - 6.5 = 1.5. (6) docs/ originals agree.
minimal_documents: D02 + D03; D04 a weaker alternative for D02 ("No Update" inference); D01, D05 cannot
replace D03.
readings: printed ex-A&D row as the measure -> 0.5, rejected ("names 'comparable currency neutral EPS'
and says 'implied by'"; separate definition; the 2025 ~8% does not exclude A&D); 2025 actual 9% -> 2.5,
does not fit "expected in July 2025"; Prior (April) column -> 2.5.
gaps: "approx." components inherit rounding; read Outlook sections of all five, D02/D03 definitions,
D05 L112-125, targeted searches; not every reconciliation table.
contaminated: no

## Solve 3: 1.5 (right), confidence high

answer: 1.5 percentage points (July 2026 outlook implies 6% to 7% for 2026, midpoint 6.5%; July 2025
outlook expected about 8% for 2025)
confidence: high
path: (1) D03 L197 Current/Prior table, footnote 1 L212; L202 ex-A&D 7% to 8%; L203 comparable EPS 9% to
10% with ~3% currency tailwind and ~1% A&D headwind. (2) D03 L472 definitions: the plain measure removes
currency only. (3) 9-10% minus 3% = 6-7%; 7-8% minus 1% = 6-7%; midpoint 6.5%. (4) D02 L209 ~8%
"Updated"; D02 L475; L211/L213 check (3% = 8% minus 5%; the ~1% A&D "in addition" sits inside the 8%).
(5) 8.0 - 6.5 = 1.5.
minimal_documents: D02 and D03; D03 irreplaceable; D04 could stand in for D02 (less direct).
readings: stated ex-A&D 7-8% taken as the measure -> 0.5 (ignores D03 L472); like for like on an
excluding-A&D basis also gives 1.5 (2025: 8% + 1% = 9% vs 7.5%); April (Prior) outlook -> 2.5 (its ex-A&D
6-7% happens to give 1.5); 2025 actual 9% -> 2.5, not the expectation.
gaps: none; "approx." inputs combined additively as presented; partial line ranges read plus searches.
contaminated: no
