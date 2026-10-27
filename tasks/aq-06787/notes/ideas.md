# aq-06787 - lean candidate sketches

Current target: hard (user, 2026-10-18: no Easy or Medium slot). Measured platform success pending.
Origin of every sketch: claude.

| ID | Sketch | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | H1: IIP margin range over the eight quarters to June 30, 2026, latest printing per quarter; gold 3.7 (20.4 - 16.7); lures 5.5, 5.3, 3.3 | one watched reading: D07's "20.3% ... in 2024" as full-year (gives 5.5); necessary D07, D08, D10 | screened 3/3 (row 61); quick test failed (user, 10-18) |
| i02 | [i02](sketches/i02.md) | H1: same range over calendar 2025; gold 3.2 (20.3 - 17.1); lures 4.9, 3.3 | necessary D08, D09, D10; no second reading found | screened 3/3 (row 62); quick test failed (user, 10-18) |
| i03 | [i03](sketches/i03.md) | new hook (round 2): Metro's net-rate rise Q4 2024 -> Q2 2025 (D05 Q&A 102.40 -> D06 Q&A 107.50) less the company's (104.73 via D05's +0.93 -> 105.33); gold 4.50; lures 5.90 (Metro from D06's first month ~101), 5.43 (company base Q1 2025) | necessary D05, D06 (D08 substitutes for the company Q4 2024 rate only); Q&A figures past the form's number window (expected false alarms) | screened 3/3 (row 63); quick test failed (user, 10-18) |
| i04 | [i04](sketches/i04.md) | round 3: change in net debt / trailing-four-quarter adjusted EBITDA, June 2025 -> June 2026; windows need Q4 2024 (D08 only) and Q1 2025 (printed only as differences); gold 0.64; lures 0.53 (fiscal years), 0.52 (gross), 0.91 (term loan only) | necessary D06, D07, D08, D10 (+ D09 or D05/D02, D04 or D07); rounding routes still give 0.64 | screened 3/3 (rows 64-65); quick test failed (user, 10-18) |
| i05 | [i05](sketches/i05.md) | round 3: Metro's net-rate rise from its acquisition quarter (Q4 2024, $102.40) to the earliest quarter it topped the company's rate (Q2 2025, $107.50); gold 5.10; lures 6.50 (first month ~101), 2.10/3.60 (March's monthly $106.00) | necessary D05, D06; selector is the analysis | screened 3/3 (rows 64-65); quick test failed (user, 10-18) |

Both sketches share hook H1, so a result on one is weak evidence about the other; H2 and H3 were
rejected as lone hooks (one finding step each, notes/hooks.md).
