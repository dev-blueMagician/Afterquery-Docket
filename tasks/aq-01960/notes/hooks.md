# aq-01960 - cross-document hooks

Bundle: 14 KLA quarterly earnings releases, Doc N = DNN (Q3 FY2023 ... Q4 FY2026; fiscal year
ends June 30). Target (user, 2026-10-08): no Easy slot; medium, with hard where a design allows.
Map: [doc-map.md](doc-map.md). Facts below were reopened in text/ before use.

Key structural facts found while hooking:

- Every release gives next-quarter guidance (revenue, GAAP and non-GAAP gross margin, GAAP and
  non-GAAP EPS). GM and EPS guidance is never restated later; revenue ranges are restated in the
  next release's highlights except D10 and D14 ("towards the upper end", "above the midpoint").
- No release prints an actual gross margin or any "gross profit"; both must be computed from the
  income statement (Total revenues, Costs of revenues) plus, for non-GAAP, the cost-of-revenues
  line of the "Pre-tax Impact of GAAP to Non-GAAP Adjustments" table.
- The reconciliation row "Acquisition-related charges" bundles cost-of-revenues amortization with
  SG&A amortization and, in Q4 FY2026, a -11,601 interest release in other expense (D14 L205,
  L224-227, footnote a L281). Only the cost-of-revenues part moves gross margin; D13's guidance
  reconciliation shows that treatment (acquisition-related charges 1.03% of revenue, L271).
- Each quarter's actuals reappear as comparatives (next release, year-later release) or can be
  rebuilt from year-to-date columns, except Q4 FY2026 (D14 only). Guidance values are unique to
  the issuing release.
- D14 effected a ten-for-one split (June 11, 2026) and restates per-share data; D01-D13 are
  pre-split. The split is stated in D14's highlights.
- Guidance-midpoint coincidences that matter for leave-one-out checks: non-GAAP GM 62.0% (D10,
  D11) and 61.75% (D12, D13); GAAP EPS $8.28 (D09, D10). GAAP GM midpoints are all distinct.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D13 L38-39 Q4 FY26 guidance ($3.575B +/- $200M, non-GAAP GM 61.75% +/- 1.00%); D14 L101/L104 revenue 3,657,556, CoR 1,413,108; D14 L224 CoR adj 36,200 | Q4 FY26 non-GAAP gross profit vs gross profit implied by guidance midpoints (%) | Calculate across documents; look-alike measure (bundled acquisition charges) | 33,069 total -> 3.2%; GAAP GP -> 1.7%; D14's own Q1 FY27 guidance -> -8.8% | revenue stated as $3,658M and $3.66B: one decimal keeps every stated figure on 3.3 | promoted i01 -> q01; quick test too easy, dropped |
| h1a | as h1, margin form | Q4 FY26 non-GAAP GM minus guided midpoint (pp) | as h1 | 33,069 -> 0.5 | gold 0.6 equals the GAAP-vs-GAAP route and the D12-proxy route (61.75%); two decimals split on stated revenue figures | rejected for h1 |
| h2 | D10 L37, D11 L38, D12 L39, D13 L39 GAAP GM and revenue guidance per FY26 quarter; D14 L101/L104 FY26 revenue 13,579,476, CoR 5,255,060 | FY26 GAAP gross profit minus sum of quarterly guidance-implied gross profits ($M) | Calculate across documents; aggregation; right edition per quarter | off-by-one editions (D11-D14 guidance) -> -$302M; non-GAAP GM midpoints -> $96M | revenue midpoints restated next quarter (GM not); percent form collides with proxies at one decimal, dollar form does not | promoted i02 -> q02; quick test too easy, dropped |
| h2a | as h2 with non-GAAP GM and quarterly CoR adjustments | FY26 non-GAAP version | bundled acquisition charges decoy (178,075) | 62.61% vs 62.40% | non-GAAP GM midpoint coincidences let a leave-one-out solver assume an unchanged midpoint; Q1/Q2 CoR adjustments sit in two releases each | rejected |
| h3 | D13 L39/L43 EPS guidance (pre-split); D14 L16 split, L25/L31 EPS $1.04/$1.05 | EPS beat per post-split share | Unit normalization | D14's own $1.14/$1.16 guidance | stated two-decimal post-split EPS vs exact: only whole cents agree (7 cents GAAP); non-GAAP splits 6 vs 7; split is flagged in D14 highlights | rejected (small integer, weak trap) |
| h4 | D03 L19, D09 L48, D13 L19 dividend levels; D14 L16 split | dividend level changes / post-split level | Same series, right edition | D13 $2.30 announced for May 2026 | lookups plus one operation; cash-flow payments allow approximate inference of $1.90 | rejected |
| h5 | D13 balance sheet Mar 31 2026; D14 balance sheet Jun 30 2026, cash flow Q4 | quarter change in cash plus securities, inventories | Part vs total (cash only) | D14 "Net increase (decrease) in cash" | simple subtraction once wording names the scope | rejected (too easy) |
| h6 | D05 L308 Display exit; D04/D05/D08 impairments | impairment per share etc. | Who belongs where | none strong | one-document answers or many substitutes; real-world recall | rejected |
| h7 | D14 L16 split dated June 11, 2026 (only document mentioning it), D14 L40 own post-split guidance $1.14 (issued July 28); D13 L39 GAAP EPS guidance $9.66 +/- $1.00 (April 29, quarter ending June) | GAAP EPS guidance midpoint in force when the split took effect, per post-split share ($0.966) | Same series, right edition (untied event); Unit normalization | D14 $1.14 (post-event, post-split, same label); $9.66 unconverted; D12 $0.885 | decoy's own quarter label (September quarter) can disarm it; without D14 a ten-for-one guess plus latest guidance reaches the gold | sketch i03; quick test too easy, dropped |
| h8 | D14 L205 fiscal-year "Acquisition-related charges a ... 178,075" (grouped: CoR + SG&A + -11,601 interest release); quarterly CoR splits D11 L212 / D12 L224, L230 / D13 L218 / D14 L224, L229; D14 L101/L104 FY revenue and CoR | FY26 non-GAAP gross margin from full-year totals (62.40%) | Part vs total (printed grouped figure, split elsewhere); Linking across documents | 178,075 -> 62.61%; D14's two quarters only -> 61.84% | first-half splits sit in two releases each: needs the form's "or" grouping (D12 with D11, D13); possible "too vague" block if both form solvers take 178,075 | sketch i04, quick test first (round 3) |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
