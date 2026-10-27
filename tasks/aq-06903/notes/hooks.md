# aq-06903 - cross-document hooks

Target: hard (user, 2026-10-18: no Easy or Medium slot on this bundle). Local ids: D01 = Doc 3
(BHP 9M to Mar-26), D02 = Doc 4 (BHP FY26), D03 = Doc 1 (FCX 1Q26), D04 = Doc 2 (FCX 2Q26).
Lines are this capture's text/Dnn.txt lines. Same documents as aq-01189 (2026-10-06, Medium
target, two locally checked questions, no platform result): its edition-bridge hooks (h1 Cerro
Verde stake -> April outlook; h6 Carajas completion -> previous guidance) are not reused.

Mined first (notes/mine.md) and checked mechanically (scratchpad): no restated figure in either
pair. BHP's overlapping quarters (900 cells) and FY25 comparatives match; every FCX Q1 line equals
D04's six months less Q2. So no "restated figures" lever exists; designs rest on periods no
document reports, a changed working-capital sign, sensitivities by edition, and look-alike lines.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D03 322: OCF ~$8.7B "including $0.2 billion of working capital and other sources", deck $4,500 Au / $25 Mo, sensitivities $50M/$90M; D04 312: ~$8.3B "net of $0.3 billion ... uses", deck $4,000 / $30, H2 sensitivities $40M/$45M | 2026 OCF estimate change April -> July, before working capital and at April's deck: +0.19 ($B) | Like for like (WC sign), same series right edition (sensitivities), calculate across documents | headline -0.40; -0.31 no WC step; +0.13 April sensitivities; +0.10 no repricing; -0.41 sign slip | sensitivities past char 20,000 (form false alarm); approximate inputs | sketch i01 |
| h2 | D04 1181/1393/1614 six-month silver notes 0.8 + 1.6 + 1.1; D02 310 Total silver sales Mar-26 4,858 + Jun-26 3,822 | silver sold Jan-Jun 2026, BHP minus Freeport's mines: 5.2 Moz | Scatter the pieces (no FCX total), period no document reports (BHP calendar half), look-alike row (payable only) | 14.1 FY26; 6.0 no U.S.; 4.6 payable only; 6.9 Q2 notes | all inputs past char 20,000; Antamina reading settled by "report selling" | sketch i02 |
| h3 | D04 62-63 Q2 OCF 2,048, capex 1,104; D04 700-702 six-month dividends 434, NCI 359, treasury 203; D03 644-646 Q1 218, 225, 93 | Q2 2026 payout to common stockholders as % of OCF after capex and NCI distributions: 40% | Period no document reports (twice; bank's 3M move), look-alike NCI line, who belongs where (Cerro Verde stake) | 58 six months; 61 NCI income; 53 Cerro Verde; 35 NCI ignored | cash-flow lines past char 20,000 | sketch i03 |
| h4 | D02 203 H2 FY26 copper 6.21 (year ends 30 June, D02 47); D03 737 LME Q1 5.83; D04 835 LME Q2 6.05 | BHP realised copper premium over LME, Jan-Jun 2026: 27 cents | Period no document reports (LME half), same series right edition (BHP H2 not FY/Q4), look-alike (FCX realized beside LME) | 16 Q2 LME only; -20 FY26; 17 FCX realized; 48 Q4 vs Q2 | LME sentences past char 20,000; benchmark from the other company's release, named in the question | sketch i04 |
| h5 | D03 29/31 Mo: Q1 24, April FY 90 incl. Q2 est 22; D04 29 FY 93; D04 97 H1 49 | change in implied Jul-Dec 2026 molybdenum sales, April -> July: 0 | Same series right edition, period no document reports (implied half) | +3 headline; -22 April remainder vs half | nil gold; "own figures" pins April's Q2 estimate | sketch i05 |
| h6 | D01 202 exploration YTD Mar FY26 275 / 235 expensed; D02 263 FY26 408 / 347 | Q4 FY26 exploration expensed share 84.2% | one rebuild (FY less 9M) | 85.0 FY; 85.5 9M | one deciding step (playbook section 2) | hold |
| h7 | D01 229 Mar-25 quarter 513.4; D02 290 Jun-26 491.9; D04 86 FCX H1 1,448 vs 1,831 | calendar-half copper production decline gap: 15.0 pp (aq-01189 i03) | period no document reports, map the period | 17.7 fiscal years; 13.7 quarters | lookups only | hold |
| h8 | D04 128 idle costs $284M / $690M; D04 288 "$284 million ($1.86 per pound of copper)" PTFI basis; D03 128 $406M | consolidated unit net cash cost incl. idle costs (Q2 2.37; Q1 2.53) | look-alike per-pound figure | 3.83 PTFI per pound | D04 alone rebuilds Q1 (H1 less Q2), so D03 is not necessary | rejected |
| h9 | D01 150 Q3 FY26 prices; D02 203-206 Q4 prices, copper and energy coal both "11%" | largest Q3 -> Q4 FY26 price rise: energy coal 11.49 vs copper 11.43 | printed tie | copper | copper's cent rounding spans the gap (11.25-11.61%) | rejected |
| h10 | D03 741-751 Q1 2026 provisional adjustments prior 34 (open at Dec 31) / current -55; D04 839-849 Q2 prior 98 (open at Mar 31) / current 40; D04 851-861 six months prior 58 (open at Dec 31) / current 59 | Q2 2026 revenue from repricing copper sold in Q1 2026: 98 - (58 - 34) = 74 = 59 + 55 - 40 | Look-alike (Q2 prior column), like for like across the tables' column definitions, calculate across documents (Q1 split only in D03) | 98 (Q2 prior), 19 (59 - 40), 40 (no D03), 24 (older sales only), 73 (division schedules) | tables past char 20,000 (form false alarm); 2025 satisfies the same identity (-28 both routes) | sketch i06 (round 2) |
| h11 | D04 465-474 six-month copper sales Consolidated 1,367, Net 1,022; D02 Appendix 2 Mar-26 + Jun-26 sales by asset, Escondida note "Presented on a 100% basis. BHP interest ... 57.5%", basis rule (proportionate for equity-accounted Antamina) | own share of reported copper sales, Jan-Jun 2026, Freeport minus BHP: 74.76 - 72.88 = 1.9 pp | Footnote changes how the table is read (Escondida 100%), look-alike (Antamina interest label vs proportionate basis), period no document reports (BHP calendar half) | -25.2 (BHP totals as own), 7.4 (Antamina scaled twice), 2.2 (FY26), 0.4 (production) | by-asset rows past char 20,000; constructed cross-company comparison | sketch i07 (round 2) |

The map is navigation; quotes come from extracted sources. No pound/tonne factor is printed, so
kt-against-lb comparisons stay excluded (aq-01189); silver and gold are both in ounces.

Outcome (2026-10-19): h1-h5 (i01-i05) and h10-h11 (i06-i07) all failed quick tests against the High model; bundle closed
at the user's choice. Even the definitional decomposition (h10) and the cross-company consolidation bases (h11) were solved
by every local solver.
