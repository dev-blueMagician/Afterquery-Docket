# aq-03066 - cross-document hooks

No earlier captures exist for these bytes or this document family (grep of every saved capture, 2026-10-11),
so there are no measured misses to start from. Family lessons applied from memory: one lookup plus one
operation is solved; a trap must be untied and sit in the documents; date gaps and list diffs were too easy.

Shape of the bundle: six December 2018 submissions (mostly prose positions, few figures) and two later
Commission papers. Spark (D07), Axiom (D06) and Chorus (D01) print no WACC, RAB or connection figures
(mapper inventories). The only worked numerical object is the workshop pack's illustrative loss table
(D03 lines 277-279), rebuilt exactly by script. Unique figures elsewhere: CCHL's Crown Fibre Holdings WACC
(D02 line 110), Vodafone's leverage-adjusted WACC (D08 line 481), the summary paper's period lengths (D04 line 163).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D03 table and "discount rate ... same as the WACC value" (line 231); D02 line 110 "mid-point WACC of 9%, utilised by Crown Fibre Holdings" | Opening loss asset in the Commission's illustration rerun at the WACC mid-point CCHL urged as the starting point: 1,450 (nearest 10) | Calculate across documents; printed same-label decoy | Printed 1,542; return only at 9% 1,510; discount only at 9% 1,480-1,490; 0.9 x 1,542 = 1,390 | What-if on figures the Commission calls purely illustrative; ten-year arithmetic | sketch i01 |
| h2 | D03 line 237 "2, 3 or 4 periods" and 1,542; D04 line 163 "initial regulatory period will be three years, followed by regulatory periods of 3-5 years" | Yearly straight-line write-off of the illustrative loss asset over the longest four-period span, 18 years: 85.7 | Calculate across documents; look-alike figure | 4 x 5 = 20 years gives 77.1, and "20" is printed as a fixed-period alternative in the same sentence; 30 years gives 51.4 | D04's sentence can be rebuilt from D03 line 461 "(3-5 years)" plus D01 line 1103 "(three year) RP1", or recalled from the Act: Document-check risk on D04 | sketch i02, risk stated |
| h3 | D03 table; implementation deferred from 1 January 2020 (D01 line 87; D04 line 139 "two-year extension"; D06 line 668) | How much the deferral adds to the illustrative loss asset: 1,542 - 1,236/1.21 = 520 (naive 170 + 136 = 306) | Figure that must be computed | Sum of the two added years' PV cells 306; undiscounted 290 | The deciding input (original date) sits in three documents: fails necessity, not promoted | closed unless a single-source anchor is found |
| h4 | D08 line 481 "from 6.09% to 5.37%" x D03 table | Illustrative losses at Vodafone's leverage-adjusted WACC, undiscounted only (Vodafone wants PV at the cost of debt, lines 483-489): 940 | Calculate across documents | 6.09% and CCHL's 5.56% as wrong rates | One scaling step; Vodafone's own PV rule has no figure | closed (one lookup plus one operation) |
| h5 | D04 line 548 seven quality dimensions; D08 lines 543-549 CEPA's six; D01 lines 941-942 "only ... availability and performance" | Dimension outside every submitter's list: customer service; count outside Chorus's two: 5 | Match then exclude | CEPA's six minus two gives 4 | A list diff; small-integer answer | closed (list diff family) |
| h6 | D02 lines 22-23 (8 November 2011; 31 May 2018, 19 months early) x D03 line 159 (losses from 1 December 2011) x D04 line 41 | Date gaps: 23 days of build before the loss period; 43 months from completion to implementation | Calculate across documents | Scheduled versus actual completion | Date counts are the low model's strongest family | closed |
| h7 | Section numbers: D01 fn 6 (third-reading numbering, losses under 176) vs D03 line 157 (177) vs D06 (206/207) vs D08/D05 (208) | Same provision under two numbers | Entity resolution | Section 176 means the IM power in D04 | Trivia; answer would be a section number | closed |

Round 2 (2026-10-11), after h1 and h2 were quick-test too easy. Two independent question-author runs (rules and
definitions; figures and conflicts) each read the Commission papers and the short submissions in full and both
arrived at h8 separately.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h8 | D08 lines 543-549 (Vodafone agrees with CEPA's six); D01 lines 941-942, 960, 987 (Chorus: only availability and performance); D07 line 637 (Spark: "the full lifecycle dimensions set out in the CEPA report", none named) | Dimensions backed by exactly two of the three: ordering, provisioning, switching, faults. As a total of backings: 14 | Match then exclude; grouped statement resolved through another document | Spark's clause unresolved: availability, performance (total 8); Chorus credited with six: none (total 18) | Six-item universe; "exactly two of" three companies may be read against rule 10; Chorus's "management of congestion (performance)" | sketches i03 (list) and i05 (total) |
| h9 | D08 lines 317-325 (Frontier's four allocations); D04 lines 433-434, 449 (no prescriptive rules between FFLAS types "initially") | Allocations left without prescriptive rules: Layer 1 vs Layer 2, anchor vs other products | Rule applied to another party's table | Both fibre-vs-copper rows | No wrong default; the rule sentence is keyword-reachable | hold (i04), low priority |
| h10 | D01 line 967; D08 line 542; D03 lines 348-358 | CEPA level each party backed | Bridge | Level 3 | One of four; reachable without D08 | closed |
| h11 | D04 line 46 (fn 2), line 526, lines 74-80 | "LFCs" excludes Chorus: 435,000 users | Definition gate | 1,367,000 | Gate, rule and figures all in D04 | closed |
| h12 | D03 line 62 "16 subs and expert reports"; D08 line 20 (two attached reports); D07 line 77 (Axiom report) | Submissions and reports other than Vodafone's and Spark's: 11 | Calculate across documents | 14, 13, 12 | D03 never says attached reports were itemised in the 16; Spark leg printed in D06 and D07 | closed (i06, unstated counting convention) |

Figures author's other closures: Enable's schedule against the programme's (public end-2022 date, schedule rebuilt
from D01 line 64, a date gap); the two FPP WACC figures (basis of 5.56% and 9% never stated; Vodafone's sit past
character 55,000); InternetNZ's growth rule re-based (2022 in four documents; routes agree only to the nearest 100);
uptake ratios (three sources, three dates); Enable scale (200,000 duplicated; one third non-terminating); the
workshop pack's second worked example (closed family); capex snapshot (garbled: 291 against a printed 301);
participation counts; Chorus's milestones; Vodafone's tables and Axiom's figures (no partner figure elsewhere).
Rules author's other closures: Chorus-only rules and stale 2020 statements (statutory, repeated, recallable);
statute renumbering (answer a section number); Part 4 sectors against CCHL's holdings (public); OVABAA/ACAM
(two candidates); capex features (garbled D01 line 1021); ICABS scope; splitter layer; presenter and
policy-statement bridges.

The map is navigation; quotes come from text/Dnn.txt. Position-matrix asks (who backed an uplift, which CEPA
level) were set aside: answers are document authors (rule 10) or small guessable counts.
