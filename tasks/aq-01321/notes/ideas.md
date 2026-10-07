# aq-01321 - lean candidate sketches

Current target: medium (user, 2026-10-06: "difficulty_target to at least medium"); measured platform
success pending. Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources
to verify premises, exact names, terms, periods and units. A sketch needs question, provisional short
gold, essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1 stale same-label cumulative figure (Microchip inventory) | "How far below its end-of-2024 peak, in millions of dollars, was Microchip's inventory balance at the close of its first quarter of fiscal 2027?" -> $309.0 million | D06 L46 (320.9 "now" = Mar 31, 2026), D06 L229 (1,035.4), D04 L203 (1,047.3) | Scatter; stale figure. Wrong routes 320.9, 246.2 | Dec-2024 balance derived from CFO prose; public Dec-2024 balance may be recalled | PROMOTED to q01 (rev 1 checked; review ready, difficulty easy) |
| i02 | h2 calendar-window aggregation | "What was the combined revenue of Analog Devices, Microchip, Texas Instruments and onsemi for each company's fiscal quarter that ended in the second calendar quarter of 2026? Give billions of dollars to one decimal place." -> $12.1 billion | D02 L13/L126, D04 L167, D11 L59, D07 L119-120 | Temporal alignment (onsemi Q1 ended Apr 3); unit normalization. Wrong routes 12.2, 12.5, 12.6 | Only D04 and D11 individually necessary; could read as a date gotcha | superseded by i05 (same window, date wording) |
| i03 | h3 claim vs numbers (onsemi Q2 2026) | "Of the ranges onsemi forecast for its second quarter of 2026, which ones did its actual results for that quarter fall below the midpoint of? List them in any order." -> GAAP gross margin, GAAP diluted earnings per share | D07 L66-72, D08 L13-17, L23 | Mentions it vs does it; decoy CEO claim (non-GAAP only) | Per-item printed values (keyword-filter risk); likely Easy | screen pass; blind match (reading: "below" as "worse" adds opex); closed-book miss; quick-test candidate |
| i04 | h1 percentage form of q01 | same facts -> 22.8% | as q01 | stale figure; state the rounding | sibling of q01 (never submit both) | screen pass; quick-test comparison only |
| i05 | h2 rewording of i02 (date window) | "...for the quarter each company ended between April 1 and June 30, 2026? Give billions of dollars to one decimal place." -> $12.1 billion | as i02 | temporal alignment | strong models know onsemi's Friday-nearest calendar | screen pass; blind match; closed-book miss (11.6) |
| i06 | h2 Jan-Mar window (onsemi excluded) | -> $9.3 billion | D01, D06, D10, D07 | temporal alignment; match then exclude | closed-book REACHED 9.3 (Q1 2026 actuals and onsemi calendar recalled) | DROPPED |
| i07 | TI twelve-month (R&D + SG&A) / revenue, independent author | "For the twelve months ended June 30, 2026, what was Texas Instruments' combined R&D and SG&A expense divided by its revenue, expressed as a percentage to two decimal places?" -> 20.26% | D12 L62-63 (2025), D10 L62-63, D11 L62-63, L220 (19,453); decoy D11 L17 "$3.9 billion" | Exact table vs rounded prose (same-window prose, exact only by a three-release rebuild); state the rounding | removal depends on recall of TI line items; pipe-row evidence | PROMOTED to q02 (rev 1 checked; review ready, difficulty easy, Medium ~12%) |
| i08 | onsemi buybacks / free cash flow, four quarters to July 3, 2026, independent author | -> 97.7% | D09 L253, D08 L232, L373 | Calculate across documents; printed ratios for other windows | Oct-2025 quarter buyback public (removal risk) | screen pass; blind match; closed-book miss (about 100%); D09 removal risk (Q3 2025 FCF recalled) |

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
