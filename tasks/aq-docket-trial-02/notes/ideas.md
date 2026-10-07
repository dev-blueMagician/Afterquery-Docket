# aq-docket-trial-02 - lean candidate sketches

Current target: medium (user, 2026-10-06: "at least Medium", one attempt; a High-tier pass also meets
it). Measured platform success pending. Drafted from hooks.md shorthand, then reopened against
text/Dnn.txt for exact names, periods and units.

Design basis (memory, measured): Medium = Low 0/5 then Medium 1-3/5 (aq-00964 q01); High = Medium 0/5
then High 1-3/5 (aq-00745 q09, untied single trap); a definition/method applied to an unreported period
reached Low 2-3/5 (aq-00998 q05, Easy); labelled lookups plus one standard calculation are too easy;
two chained traps with an ambiguous anchor were Too hard (aq-00745 q08). Colgate's guidance updates all
print "(versus ... previously)" in the later release, so the edition-trap family is weak here (h6, h7).
This bundle's distinctive dependency is the 2026 segment realignment: the derived quantities are
printed nowhere and need the D11 composition note plus original (D09) and recast (D10) figures.

Round 1 (2026-10-06, origin claude; all four passed docket_agent.py screen with no failure/warning):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1: EMEA's former-A/E part = A/E minus the Russia/Belarus carve-out | EMEA 2025 net sales from operations previously reported in Africa/Eurasia. Gold $948 million | D11 l.85; D09 l.463-464; D10 l.28 (cross-route D09 l.460, 462; D10 l.25, 27) | Match then exclude; scatter. Decoys 1,172 (printed A/E), 1,314 (EMEA - Europe) | pipe-row quotes; composition only in D11 | screen pass; lead; promote to q01 |
| i02 | h2: impairment year -> skin health sales via NA original minus recast | 2025 net sales of the impaired business. Gold $366 million | D09 l.71, 460; D11 l.85; D10 l.25 | Scatter; event bridge. Decoys 142, impairment 794/919 | direct NA route (easier) | screen pass; alternate |
| i03 | h3: Russia/Belarus = recast AP minus original AP, two years | R&B net sales change 2024->2025. Gold +3.7% | D11 l.85; D09 l.463; D10 l.28, 59 | Calculate across documents. Printed decoys A/E +7.0%, AP -1.5% | names R&B (note one search away) | screen pass; alternate |
| i04 | h4: skin health Q4 2025 segment result = original Q4 NA OP - (recast FY - 9M) | Skin health segment result in the impairment quarter. Gold -$4 million | D09 l.71, 477, 491; D10 l.25, 333; D11 l.85 | Mentions vs does (impairment in Corporate); unreported quarter. Decoys 919/794 | three inference steps (too-hard risk); wording | screen pass; stretch |
| i05 | h5: SGPP latest estimate midpoint vs pretax charges recorded | Share recorded by June 30 2026. Gold 70.7% | D11 l.39; D09 Table 9; D12 l.800 | Exact line item | 300 (OP) vs 305 (pretax) two stated "charges" | not screened: answered-inconsistently risk |

Round 1 screens (raw: runs/sketch-round1/returns.md; q01 rev 0 records in questions/q01.md):
q01/i01 A and B matched $948 million (high), audit clear (difficulty risk "one footnote plus two
subtractions"), closed-book missed (~$1,100 million, the whole-A/E decoy). i02 blind matched 366
(high); closed-book missed but recalled a 2022 skin health impairment the bundle never mentions
(anchor "the year Colgate took a charge" would be ambiguous in the world). i03 closed-book missed
(+14.5%). i04 blind matched -4 (medium) but found defensible rounding routes giving -3 and -2:
dropped (one-clear-answer risk); closed-book missed.

Round 1b (same day): caller judgement that i01's carve-out is signposted inside the very note a
solver must read (tied, like aq-00745 q01's Easy result), so the low model may reach 948 by one
inferred subtraction. Variants needing the derivation for two years, with a salient decoy:

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i06 | h1 over 2024 and 2025 | Change in full-year net sales of the operations moved from Africa/Eurasia into EMEA, 2024 to 2025. Gold +$69 million (948 - 879) | D11 l.85; D09 l.463-464 (both FY columns); D10 l.28, l.59 | Match then exclude; scatter. Decoys +77 (whole A/E, adjacent D09 columns; D09 l.583 prints +7.0%), +230 (EMEA), +8 (R&B) | FY2024 old columns also in D05 (D09 still unique for 2025) | screen pass; blind/closed-book pending |
| i07 | same, percentage | Same, percent, two decimals. Gold +7.85% (7.8498%) | as i06 | Decoy printed A/E +7.0% (7.03%), EMEA +5.68% | two-decimal precision (one decimal sits on 7.85) | screen pass; blind/closed-book pending |

Removal approximations (python): without D09, 9M-based extrapolation gives +49 to +53 (+5.6% to
+6.0%); without D10, no FY2024 recast (not computable; naive +77); without D11, +77 (+7.03%).

Round 2 (2026-10-06, after both q01 reviews judged the realignment family Easy-leaning: tied
exclusion in the defining parenthesis; Medium or higher about 20%):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i08 | h5: latest programme estimate vs pretax charges recorded, three untied close-reading points | Unrecorded part of the latest estimate's midpoint at June 30, 2026. Gold $132 million (450 - 318) | D11 l.39; D09 l.865, l.903; D12 l.800 | Same series, right edition (original estimate -68); scatter; line item (operating-profit 300 -> 137; 2026 only -> 145) | 300 vs 305 split; too-hard risk | two blind matches (high; 137 and 145 classed weaker), closed-book miss (~$100M); promoted to q02 |

Round 3 (2026-10-06, after platform results reported by the user: q01 "passed in pipeline"; q03, the
same carve-out as a one-year margin, did not pass the quick test). Working diagnosis: the low model
derives the Russia and Belarus carve-out by itself; q01's surviving extra was a printed, answer-shaped
whole-segment decoy (D09 +7.0%) over two years. No other entity gives that slot with robust D11
necessity (skin health and Russia/Belarus questions supply D11's fact through their own wording;
quarterly and FY2023 routes split by $1M; FY2025 operating profit splits 195/196). So a new mechanism:

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i09 | Restated figures plus a twelve-month build: full-year 2025 recast only in D10, first half 2026 only in D12; D09 prints the same-label pre-2026 full-year row | North America segment operating margin, 2026 definition, twelve months ended June 30, 2026. Gold 20.33% (739 / 3,635) | D10 l.25; D12 l.428, l.444, l.457 | Same series, right edition; scatter; calculate across documents. Wrong routes 18.32% (D09 FY + recast H1), 19.14% (all original), 21.35%, 19.11%, 21.47%, 19.38%, 18.72%, 21.55% | the pin "as the company defined that segment from 2026" is needed for one answer but tips the recast; no printed answer-shaped twelve-month margin; pipe rows | screen pass (no warnings); promoted to q04 |

Round 4 (2026-10-06, after q04 failed two quick tests, "Too easy - solver got it": the low model went
straight to the recast tables and built the twelve months). No other untied edition change, silent
restatement or dated event exists (Q1 and mid-2025 income statement and cash flow comparatives equal the
originals; guidance basis dates are not events). The Emerging Markets definition changes in D11/D12
(Africa, the Middle East and Eastern and Central Europe) but supports no calculation.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i10 | h5 decimal twin of q02: prominent operating-profit charge (D12 $300) vs pretax 305; 2025 charges only in D09; D09's 2024 "Restructuring programs" (85) is another programme | Share of the latest estimate's midpoint recorded by June 30, 2026. Gold 70.67% (318 / 450) | D11 l.39; D09 l.865, l.903; D12 l.800 | Exact line item; scatter; latest edition (tied). Wrong routes 69.56%, 67.78%, 66.67%, 127.20%, 89.56% | 300 vs 305 answered-inconsistently risk (as q02) | screen pass; quick test first; test i10 or q02, not both |

Round 5 (2026-10-06, user: "make another one again which targeted difficulty to medium"). The only
untied outlook change (D06, FY2025 organic 3-5% -> 2-4%) has no dated event before it, and the 2025
annual-meeting anchor (D05, May 9) is guessable and the 2025 outlook/actuals are recallable (closed-book
risk). FY2026 outlook edits are all tied ("versus ... previously") and numeric items unchanged.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i11 | h5 with three independent traps: estimate in effect at the first charges (Q4 2025: the August 2025 $200-$300M, not D11's April 2026 $350-$550M); pretax 305 vs operating-profit $300; 2025 charges only in D09 beside a 2024 restructuring figure of another programme | Cumulative pretax SGPP charges at June 30, 2026 as a % of that estimate's midpoint. Gold 127.20% (318 / 250) | D09 l.703, l.903; D12 l.800; D07 l.41 or D11 l.39 (estimate, duplicated) | Same series right edition (tied); exact line item; scatter; mentions vs does. Wrong routes 70.67%, 125.20%, 122.00%, 120.00%, 161.20%, 75.60% | answer above 100%; 300 vs 305; mark D09, D12 only | screen pass; sketch blind solve and closed-book running; quick test first |

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
