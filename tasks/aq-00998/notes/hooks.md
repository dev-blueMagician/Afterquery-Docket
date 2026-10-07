# aq-00998 - cross-document hooks

Caller (Claude Opus 5.5, 2026-10-05) from the complete capture; locations are text/Dnn.txt line
numbers; local Dnn = platform Doc N. Draft inventory written while the mappers ran; finalise after
the merged map. Repeated-table rule: a quarter's highlight-table figures appear in its own release,
the next release (prior-quarter column) and the release a year later (year-ago column); attachment
tables (income statement, earnings by area, capex by segment, cash flow, special items) carry only
the current quarter, the year-ago quarter and year-to-date columns. Values in one release only:
non-year-end balance-sheet lines and share counts (Attachment 1 note), 2Q 2026 (D12), the YTD
2026 columns (D12), D01's "Crude Oil Inputs" rows and most prose events. Cash-flow attachment is
in $ billions through D10 and $ millions in D11-D12. No same-label, same-period restatement was
found in the highlight tables (scripted comparison of 791 cells).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D12 l.54 "During the quarter, Chevron signed a 20-year power purchase agreement" with Microsoft (2Q 2026); D11 l.105 exclusivity agreement on a "proposed" offtake agreement (1Q 2026); net debt D11 l.356 40,101 (Mar 31, 2026), D12 l.364 28,545 (Jun 30, 2026) vs 34,461 (Dec 31, 2025) | Change in net debt over the PPA quarter: -11,556 ($M) | Mentions it vs does it (bridge); Scatter the pieces | D12 six-month change -5,916; exclusivity quarter (1Q26) +5,640; D12 prose total-debt cut "$8.4 billion" | Post-cutoff values (closed-book safe); bridge sentence plain | investigate |
| h1b | Same bridge; capital employed = equity + total debt + NCI (ROCE footnote, D11 l.386); D11 l.344-346, D12 balance lines | Change in capital employed over the PPA quarter: -2,166 ($M) | Mentions it vs does it; definition applied to instance | Printed "Total debt plus total stockholders' equity" (no NCI) -2,185; average capital employed -151; D12 six-month -301 | Near-miss decoy (19) tests NCI inclusion; D12 l.391 average capital employed 233,716 lets a solver back out the Mar 31 capital employed (234,799) from D12 alone | rejected (D11 not necessary) |
| h2 | D04 l.81 "third quarter 2023 acquisition of a majority stake in ACES Delta"; D01 l.79/l.97 undated mentions; D04 l.161 3Q23 U.S. crude unit inputs 980; D01 l.167 3Q23 "Refinery Crude Oil Inputs" 961; D12 l.163 2Q26 1,070 | 2Q26 U.S. crude unit inputs minus ACES Delta quarter: 90 MBD | Same series, right edition; Calculate across documents | D01 crude-oil row gives 109; 9M 2023 column 965 gives 105 | Old q03 rev 1 shape (checked on the clipped corpus; records lost) | investigate |
| h3 | D06 l.93/l.97/l.99 April 2025 events (Ballymore start-up, midstream sale, Far South discovery); D06 l.79 1Q25 growth TCO 20, Permian 12, Gulf 7 percent; D08 l.85 2Q25 TCO 34, Gulf 22, Permian 14 percent | Growth figure or ranking in the April-2025 event quarter (2Q 2025) | Scatter the pieces | D06's own-quarter figures in the bridge document | Old q02 shape; Ballymore date may be public; one-sentence bridge into a prose figure (aq-00949 too-easy signal) | investigate |
| h4 | D07 l.37 "approximately 301 million shares" for Hess, closing July 18, 2025; share notes D08 l.310 1,714M (Jun 30, 2025), D09 l.297 1,999M (Sep 30, 2025) vs 1,755M (Dec 31, 2024) | Share-count change in the closing quarter excluding Hess shares: about -16M | Scatter the pieces; Calculate across documents | D09 base 1,755 gives -57; no Hess removal +285 | Closed-book can estimate a quarterly buyback (~15-20M) and knows 301M and the closing date | likely reject (general knowledge/estimation) |
| h5 | D09 l.84 Hess 495 MBOED + legacy 227 (3Q25); D10 l.87 Hess 261 + legacy 124 (FY2025) | Unstated 4Q25 Hess contribution | Calculate across documents | n/a | Needs day-weighting vs simple average: two defensible answers | rejected (one clear answer) |
| h6 | D12 l.93 total debt "reduced by a record $8.4 billion"; D12 cash flow net change in debt (8,406); balance sheet 45,428 -> 37,075 (-8,353) | Debt reduction in 2Q26 | Exact table vs rounded prose | three different stated measures | Two exact measures disagree | rejected as an ask; warns against total-debt changes |
| h8 | D05 l.179 Pasadena upgrade "completed during fourth quarter 2024" (only dated mention; D05 l.115 undated; D09 l.164 LTO "completion" undated); D05 l.68/l.71 4Q24 FCF 4.4, FCF ex. working capital 1.0; D10 l.72 Adjusted FCF 4Q24 8.0 (measure defined from D08 l.229) | Adjusted FCF in the Pasadena-upgrade quarter: $8.0 billion | Same series, right edition (measure introduced after the quarter) | Bridge-document decoys FCF 4.4 and FCF ex WC 1.0 (D05); D10 current quarter 4.2; D05 rebuild without the loans row 1.0 + 7.1 = 8.1 | D10 needed for the exact 8.0 (D05 shows "Other investing activity" (0.1), not the loans row); closed-book could estimate FCF ex WC + Canada proceeds | investigate (old i05, now fully visible) |
| h7 | Shares-repurchased cash-flow rows include prior-year excise tax (D05 l.500 $145M; D08 l.506 $146M; D12 l.503 $114M/$146M) | Buyback cash excluding excise tax | footnote changes what a figure covers | n/a | Single-document answers in each release | hold |

Question-author round 1 (fresh Opus 5.5 role, 2026-10-05) added:

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h9 | International production declines blamed on the Canada sale (D05 l.166, D06 l.140, D08 l.154) vs Canada only an offset (D03 l.144, D09 l.147, D10 l.172) | Quarters attributing a decline to Canada: 4Q24, 1Q25, 2Q25 | Mentions it vs does it | 4-5 quarters without the cause test | Direction words printed per quarter (aq-00745 keyword-filter signal) | rejected |
| h10 | Simplified structure "Announced" (D06 l.101) vs "Effective July 1, began implementing" (D08 l.111) | Date used as a chronology step | Mentions it vs does it | announcement placed first | standalone versions end in one cell | folded into i05 |
| h12 | Event dates: Far South April 2025 (D06 l.99); structure July 1 (D08 l.111); Hess July 18, 2025 (D07 l.23; D08 l.97 only "in July"); Malaysia-Thailand JDA "After closing of the Hess transaction" (D09 l.46-52, l.100) | Order of four 2025 events | Ordered answers; Mentions it vs does it | announced structure first; Hess before July 1 via D08's list order | Hess date public; overview date lists | i05 |
| h13 | Hess average purchase price 2,225 / 15.38M (D11 l.452, D07 l.37) | $144.67 per share | Calculate across documents | rounded $2.2B gives $143.04 | two stated figures; public share price | rejected |
| h14 | Exploration acreage lists 2024 (D05 l.117) vs 2025 (D10 l.119) | list differences | which items | n/a | plain list lookup | rejected |
| h15 | 3Q25 total debt change: balance sheet +12,077 vs cash flow 2.1B (Hess debt assumed) | debt change | Exact table vs rounded prose | measures differ | pre-cutoff recall; two measures | held |
| h16 | 2Q25 net debt: D06 "Adjusted debt" 25,038 -> D08 "Net debt" 25,401 | +363 over the Far South quarter | Entity resolution (label change); scatter | D06 own quarter +7,282; D08 six months +7,645 | pre-cutoff balances may be recalled | held |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
