# aq-04830 - cross-document hooks

Target: medium (user 2026-10-14: no Easy slot, "target medium and high"; lower open tier). Slots at
capture: Hard 0/5 · Medium 0/1 · Easy 0/0. Medium has one slot and every captured run on 2026-10-14
started at the High level, so each hook is audited against the medium and the high solver.
Step audit: a step is pointed when a lookup of any word in the question reaches it.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 3 (D03 lines 87-110): receipts heads grew X% vs Y% forecast and were $Z higher than forecast; Doc 1 (D01 Table 3.1 2024-25 Actual block, lines 144-160): outcome levels 717.0 / 657.8 / 59.1 | Percentage by which 2024-25 non-tax (or tax) receipts exceeded the 2024-25 Budget forecast amount: non-tax 3.2/55.9 = 5.7%, tax 15.3/642.5 = 2.4% | Look-alike measure (growth-rate gap vs level gap); Calculate across documents | Growth route: non-tax 2.6% (ratio) or 2.7 pts; tax 3.3%. Outturn base: non-tax 5.4%, tax 2.3%. The growth route flips the ranking (tax first) | 2024-25 column unlabeled in the flattened table; inputs rounded to $0.1b (non-tax 5.63-5.82 range) | sketched i01 (non-tax), i02 (which head) |
| h2 | Doc 7 (D07 Table A.3 + notes, lines 784-816): Australia average maturity mismatch 139 days, definition note (b); Doc 2 (D02 Tables 7.4-7.5): 29 TB and 6 TIB maturities at 1 May 2026 | Mismatch on the article's measure at 1 May 2026: (0+92+0+61+273+485)/6 = 151.8 days, +12.8 on 139 | Applying a stated rule; Calculate across documents; State the rounding | Face-weighted 125.7 (-13.3); earlier-only 279.7 (+140.7); 20-Sep-30 read as the 21st: +12.7 | 139 deep in Doc 7 (form number-check false alarm); mostly computational | sketched i03 |
| h3 | Same pair: note (a) excludes green bonds, counts bills; Doc 2: 29 TB lines incl. one green, 9 Treasury Notes | Nominal lines on the article's basis: 37 (38 in the article) | Match then exclude | 38 (green kept) equals the article's 38 | "Treasury Notes are bills" is not stated in Doc 2 (Doc 5 defines bills): second reading 28 lines | not offered (one-answer risk) |
| h4 | Doc 6 (D04 line 117, Chart 7 note line 139): 2025-26 Budget interest 9.5%, NDIS ~8, aged care 5.2, child care 5.1, Medicare 5.6, hospitals ~6; Doc 1 lines 1461-1481: MYEFO and 2026-27 Budget rates | Edition revisions (e.g. PDI 9.5 -> 8.8 = 0.7 pts; largest MYEFO revision up = interest +1.2) | Same series, right edition | Doc 1's MYEFO comparison (1.9) | Defence has no 2025-26 Budget figure (ranking open); every step pointed by the edition names | not offered (0 unpointed steps) |
| h5 | Doc 6 line 82 (peak 37.0% in 2029-30); Doc 1 (35.8% in 2028-29, "two years earlier than at MYEFO") | Years earlier than the Roundtable projection: 1 | Right edition | "2 years" (MYEFO) | edition of Doc 6's chart not labelled; pointed | not offered |
| h6 | Doc 3 confidence intervals (% of GDP); Doc 1/Doc 2 $ and % pairs give 2026-27 GDP ~3,091b | 70% CI width for 2026-27 receipts in dollars: ~$93b | Unit normalization | 3.0 pts of GDP | pointed by "in dollars"; GDP backed out of rounded ratios | not offered (0 unpointed) |
| h7 | Doc 10 footnote 2 (yield-target bond = AGS closest to 3 years); Doc 2 Table 7.4 | 3-year AGS at 1 May 2026 = April 2029 (3.25%, $43,500m) | Applying a stated rule | Nov-28 / Nov-29 | trivial date comparison | not offered |
| h8 | Doc 3 UCB $18.3b better; Doc 1 actual -10.0 | Deficit smaller than forecast by 64.7% in dollars vs 60% in % of GDP | Look-alike measure | 60% | headline figures ($28.3b, $10.0b) widely reported: closed-book risk | not offered |
| h9 | Doc 9 quarterly GFS (all levels) vs Doc 1 Commonwealth figures | none fair | - | - | different scope (all levels vs Commonwealth); no annual sum printed | rejected |
| h10 | Doc 8 (Belgium) | single-document only | - | - | no link to any other document | rejected |

Round 2 (2026-10-14, after q01 Run 1 "Too easy", High 3/3; target hard). RBA/markets scope searched by a
question-author agent (origin claude), arithmetic in scratchpad checks.py, threeyr.py, watm.py; none offered:

| Hook | Source inputs and locations | World fact/possible ask | Why not offered |
| --- | --- | --- | --- |
| h11 | D10 footnote 2 (3-year AGS = residual maturity closest to three years, line 155); D02 Table 7.4 | target bond at 1 May 2026 = Apr-29; passes to Nov-29 on 7 Aug 2026 (8 Aug with 1,095-day years) | delete-and-guess: "closest to three years" is the natural reading of "3-year AGS" (D10 guessable, as aq-02501); leap-year convention; no unpointed step |
| h12 | D10 market-function range "residual maturity between 1 and 10½ years" (line 148); D02 | 20 TB lines (21-Nov-27 to 21-Oct-36) | mechanical, every step pointed |
| h13 | D10 "adjacent bonds ... within one year" (line 579); D02 | adjacency counts | contrived; exact one-year tie 21-Jun-34 / 21-Jun-35 |
| h14 | D05 bills definition (line 25); D02 | short-term share 4.9% (notes only) or 13.1% (with TBs under a year) | two readings; D05 replaceable by general knowledge |
| h15 | D05 Graph 4 tenor measure; D02 "around 6.6 / 8.6 years" | 6.4 vs 6.45 years | rounding conflict; D02's 8.6 vs 8.86 from Table 7.5 |
| h16 | D07 "less than 5 per cent of total debt" (line 95); D02 Table 7.3 | TIB share 4.2% face, 5.7% market | D07 states no basis; Table A.1 shares unassignable |
| h17 | D07 10-year benchmark mismatch 61 days | - | measure undefined; analogy does not reproduce 61 |
| h18 | D07 data cut-off (end August 2024 vs Graph 3 "Q2 2024") | day counts to 1 May 2026 | date count only; two cut-offs |
| h19 | D10 purchase totals; D02 line 565 | AGS 293.0b or 361.0b with semis | D02 only identifies the operations; totals widely reported |

Also examined and dropped: author and citation joins across D05/D07/D09/D10 (string joins); D02's Treasurer's
Direction with D10 dates (date counts; headroom needs D02 alone); footnote 40's taps; D10's internal
inconsistencies (per month vs per week; Table 3's 2020 vs Figure 9's 2021); D09 ranges and graphs.

Round 2, fiscal scope (D01, D02, D03, D04, D06 read in full by a second question-author agent, origin claude);
nothing offered. Every link is a repeated figure (one document suffices), a named-edition comparison, outcome
minus variance (h1, closed at High) or a scope mismatch with no bridge (D06 all levels vs D01 Commonwealth):
- h20 medium-term payment growth across editions (D04 lines 117-139 vs D01 1461-1481): pointed by edition names;
  "around" figures; defence has no D04 rate. (= h4 widened.)
- h21 D01's faster-than-GDP list vs D04's seven pressures: string join (NDIS); D04 not needed for the count.
- h22 gross debt across editions (D04 line 82; D01; D02): 0.3 pp, 1 year, 1.4 pp, all pointed (= h5).
- h23 "since the 2022 PEFO" claims D04 vs D01 ($100b/177.9b, $207b/263.8b, 70%/76%, 1.7%/1.5%): windows differ,
  "around"/"almost", no single derived answer.
- h24 AGS interest growth 2025-26 to 2026-27 (D02 Table 7.9, 27,690/25,220 = 9.79%) vs D01's PDI 8.8% (line 1467;
  "PDI refers to interest payments on AGS", line 1487): gold 1.0 point; 0 unpointed steps; 8.8 at about character
  59,090 (number-check false alarm). Below the bar, not offered.
- h25 face value rise from end-2024-25 (D01 928.6) to the 2025-26 within-year peak (D02 Table 7.1 999.9): $71.3b;
  "highest point" points at the peak row; 0 unpointed steps. Not offered.
- h26 within-year peak 36.3% vs "35.8%" peak; $1,200b limit exceeded in 2029-30; 2022 PEFO's 1,224 for 2026-27:
  D02 alone. h27 D02 Table 7.2 vs D01 Table 3.3 reconcile exactly (single-document). h28 maturity buckets joined
  to other documents' dates (contrived or guessable). Also: TIB uplift (D02 footnote 38 vs D01 line 1504; any
  answer D02-only), NBN equity and net debt (needs an unstated accounting inference), revenue-head and hydrogen
  string joins, yield sensitivities and confidence intervals (pointed), prior-year levels from growth (pointed;
  recall risk), D06 four-quarter sums (tax 892,496; NOB -37,783; net borrowing -96,460 $m) with no bridge to D01.
- Same-period wording conflict noted (not a fair question): D02 line 744 says AGS interest is lower than MYEFO
  "across the forward estimates"; D01 line 1058 has debt-management payments up $17.5 million in 2026-27.

The map is navigation; quotes come from the documents. A short valid calculation is eligible;
prior failures set priority, not a veto.
