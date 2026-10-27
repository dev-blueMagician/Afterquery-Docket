# aq-05015 - cross-document hooks

Target: hard (page 2026-10-14 15:26: "Still open on this set: Hard", "Hard 0/5 · Medium closed ·
Easy 0/0"; user: no Easy slot, "target medium and high"). Runs on 2026-10-14 started at the High
level (two solvers, three tries each; both must miss once, not every attempt wrong). Audit every
hook against the high model: count only steps no phrase of the question asks about.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Decoy/counterfactual | High-model audit | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D06:103-105, D07:103-105, D08:96-98 restated cost of materials + new taxes line; D04:98, D05:97 as first printed | Cost of materials on the current presentation for a period never restated: H2 2025 50,370; Q3 2025 26,132; twelve months to Jun 30, 2026 111,685 | Same series, right edition; calculate across documents | 47,216 (D04 first half), 52,196 (D05 Q3), 113,511 / 108,531 (TTM) | One unpointed step (silent change, never announced); a full sweep of the line can resolve it | i01, i02: quick test "too easy" 2026-10-14; CLOSED (playbook 4.2/4.3: unpinned it rests on an inclusion no document states; pinned it is a rebuilt number). The Q3-to-Q4 change variant (detection without a restated figure) was not sketched for the same reason |
| h9 | West Coast operating expenses excl. D&A: D05:433 (Q3 239, note (a) $50M Benicia retention costs; D05:857-860 adjusted 189), D05:624 (259 kbpd), D05:628 printed adjusted per barrel 7.94; D06:463 (Q4 213), D06:657 (265), D06:661 printed 8.72 | Per-barrel change Q3 -> Q4 2025 on the asked measure: -$1.3 (10.03 -> 8.74); the printed adjusted rows say +$0.8 | Printed number over a derived one (playbook section 2); calculate across documents | Lure +0.8 (printed adjusted rows); -1.5 (with D&A) | Settlement quotable (question word, D05 note and definition). Measure noun "operating expenses" sits in the deciding note: pointed risk | i03, strong-solver screen 2026-10-14 |
| h10 | Benicia plan costs kept in adjusted earnings: incremental depreciation ~100 per quarter (D04-D08 notes), retention 50 and LIFO 37 excluded (D05/D06) | Twelve months to Mar 31, 2026: ~400 left in | Mentions it vs does it | 0, 87, 300 | Fails delete-and-guess: without D06 a solver can fill Q4 2025 at the steady ~100 and reach 400 | rejected |
| h11 | Q3 2025 West Coast refining operating income per barrel (GAAP -2.10) vs Q4 (-8.16); printed adjusted rows (0.01) and (6.62) | Change -$6.1 vs lure -$6.6 | Two judgments (D05 retention, D06 LIFO) | -6.6, -4.5, -8.2 | Effectively one judgment (GAAP vs adjusted) applied twice; sibling of h9 | not sketched |
| h2 | Benicia chain D03-D08 (incremental depreciation 100/100/100/100/33; retention 50; LIFO +37/-44) | Total incremental depreciation ~433 | Cumulative vs quarterly footnotes | 533, 300 | All pointed ("incremental depreciation", "LIFO") | not sketched |
| h3 | D01 table (3.650% 2025 $600M; 2.850% 2025 $1,050M) + D03:15/50 repaid 189/251 | Retired before maturity since Nov 2021: 1,210 (73.3%) | Calculate across documents | tender caps $400M | All pointed (note names) | not sketched |
| h4 | D02:793-796 (2025 outlook 2,060/1,950, DGD (110)); D06:818-836 (actual 1,888/1,797; DGD 71+99; 2026 outlook 1,725/1,700) | Outlook vs actual; DGD implied 220 vs 170 | Forecast vs actual | attributable vs total | Pointed; x2 inference trivial | not sketched |
| h5 | D04 six months 2024 per-day (182 days) vs D08 six months 2026 (181) | Extra barrels H1 2026 vs H1 2024 ~5.6 million | Unit normalization | 8.5 million (same days) | One unpointed step (leap day) high model likely clears | not sketched |
| h6 | West Coast margins/throughput D03-D08 | Per-barrel margin over the closure window ~$15.4 | Aggregation | simple mean 16.5 | Weighting likely cleared | not sketched |
| h7 | Sustaining capital, prose only: D03 582, D04 371, D05 364, D06 368; FY 1,888 | 2025 non-sustaining 203 | Scatter the pieces | Q4 only 44; attributable base 112 | Pointed ("sustaining") | not sketched |
| h8 | Propylene series renamed/restated D05+ | Polymer grade margins | Same series | old series values | Renamed caption = pointed (aq-01937 too easy) | rejected |

Only h1 has a step the question need not name. Every comparative printed twice was checked line
by line: identical except cost of materials (taxes split out) and the propylene series.
