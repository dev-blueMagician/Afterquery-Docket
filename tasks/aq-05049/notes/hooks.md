# aq-05049 - cross-document hooks

Target: hard (user, 2026-10-14: "there is no slot for Easy or Medium Tier for this bundle, we should
target high"; page 16:21: "Corporate filings · Easy or Hard only"). The check starts at the High
model: "two solvers try up to 3 times each. Ready when both get it wrong at least once and not every
attempt is wrong." Design rule: .claude/memory/reference/hard-playbook.md (a judgment with a lure;
numbers rebuilt from printed figures, look-alike labels and definitional gates are cleared by High).
Local ids D01-D07; page Doc numbers in doc-map.md. Arithmetic: scratchpad calc_aq05049.py (2026-10-14).

Verified first (caller, 2026-10-14): no silent restatement on either side. Docusign FY2025 (D04) =
9M (D02/D03) + Q4 (D04) on every line; Paylocity Q1 + Q2 = 6M and 9M - 6M = Q3 on every line. The
one change of basis is Paylocity's renamed cash-flow measure (h3).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Decoy/counterfactual | High-model audit (playbook) | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D03 Note 10 l.824 and MD&A l.1210 (program "commenced in March 2022"; $200.0M + $300.0M + $1.0B); D03 Part II l.2437-2439 ($769,641K remaining Oct 31, 2024, excl. excise); D04 l.303 (Q4 FY25 cash 161,725; FY25 683,528; FY24 145,515) | Cash paid for buybacks under the program through Jan 31, 2025 = 1,500,000 - 769,641 + 161,725 = 892,084K (FY2023 purchases 63,041K printed nowhere) | Calculate across documents; complete-looking account vs incidental fact | 829.0 (FY24 + FY25, D04's two-year account); 730.4 (through Oct 31); 683.5 (FY25 only); ~1,100 (D01 June 5 figure) | Kind: complete-looking account over an incidental fact (an absence). Deciding step: the program predates the releases' two years, so purchases before Feb 2023 must be recovered from the authorization arithmetic; no word asks for them. Risk: "repurchase program" leads to Note 10, whose first sentence dates the start | i01 screened 3/3 right 2026-10-14: retired |
| h2 | D03 Note 13 l.893 ("$837.7 million ... discrete tax benefit during the three months ended July 31, 2024"), MD&A l.1028 ($831.4M); D02/D03 9M (804,340) and Q3 9,151; D01 Q1 FY25 2,833 | Net tax benefit in Q2 FY25 = 816,324K | Printed number vs derived | 837.7, 831.4 (discrete item), 813.5 (Q1 omitted), 804.3 (9M) | Kind: printed number over a derived one. Pinned ("net"/"total"), what remains is a rebuild (cleared); unpinned, 837.7 is arguably a reading (form block risk) | i10 screened 3/3 right 2026-10-14: retired |
| h3 | D05 l.321-327 (FCF ex-interest Q1 44,066 = 73,917 - 29,851); D06 l.316-327 (6M FCF 110,746; cash paid for other items 5,073; adjusted FCF ex-interest 56,702); D06 Q2 interest 29,266 | Q2 FY25 FCF less interest income on funds held = 7,563K | Same series, right edition (basis change) | 12,636 (56,702 - 44,066, mixed bases); 36,829 (no interest); 51,629 (6M) | Kind: look-alike label ("Adjusted") beside the route; playbook lists look-alikes as cleared | i21 screened 3/3 right 2026-10-14: retired |
| h4 | Docusign quarterly non-GAAP operating income/revenue: D01 Q1 FY25, D02 Q3 + 9M, D04 Q4 + FY | Highest FY25 quarterly non-GAAP operating margin = Q2 (derived) 32.2% | Calculate across documents | 29.6% (Q3, highest printed quarter) | Completeness visible from format (four quarters): cleared kind | rejected |
| h5 | Billings Q2 FY25: printed route 724,508 vs definition on balances 729,526 (acquisition lines D02 l.408-409; D03 Note 5) | Q2 FY25 billings | Definition applied to instance | 729.5 | Printed route avoids the judgment entirely | rejected |
| h6 | Paylocity ex-interest margins over recurring revenue (D06 l.347, D07 l.348) applied to D05 Q2 guidance (D05 l.57-65) | Guided Q2 ex-interest EBITDA margin 26.9% (midpoints) | Definition applied to instance | 25.0% (over total revenue) | Definitional gate (cleared); delete-and-guess risk: the denominator is inferable from the measure's name | rejected |
| h7 | Docusign Q2 FY25 total SBC: CF/statement route 164,656 vs reconciliation route 164,448 (restructuring SBC 208) | Q2 FY25 total SBC | Look-alike measure | 164.4 | 0.2M difference; fiddly, "hard to parse" not reason | rejected |
| h8 | Docusign Q2 FY25 acquisition-related expense = 4,340 - (-376) - 1,358 = 3,358 (D02/D03 sign, D01 Q1) | Expense in the Lexion quarter | Calculate across documents | 2,606 (sign slip) | Sign handling and quarter placement both cleared; Lexion's May 2024 date recallable | rejected |
| h9 | Guidance edits: Docusign FY26 (D04 -> D01), Paylocity FY25 (D05 -> D06 -> D07), implied interest income 108/113/120 | Raise decompositions, implied quarters | Forecast vs actual | headline raise | Every step named by the question (rebuild): cleared | rejected |
| h10 | Docusign remaining authorization at Jan 31, 2025 (607,916) or Apr 30, 2025 (424,485) | Remaining authorization | Calculate across documents | 400 (D01 June 5 less increase) | Lookup plus subtraction (cleared); Apr 30 also open on when the June increase was authorized | rejected (h1 keeps the judgment) |

| h11 | D07 l.13 (May 1, 2025 dateline), l.15 (CEO: "$150 million or approximately 800,000 shares repurchased through April of this fiscal year"), l.208 (9M cash 91,080); D06 l.207 (6M cash 8,395) | Buybacks Jan 1, 2025 to the Q3 announcement = 150,000 - 8,395 = 141,605K ($142M) | Scatter the pieces; prose figure beside own complete-looking table | 83 (tables only, Jan-Mar), 150 (fiscal-year figure), 91 (nine months), 59 (April only) | Kind: prose member beside the same author's complete-looking table (measured Hard kind) plus fiscal-vs-calendar judgment in a second document. Risks: CEO quote opens D07 (visible); round $150M | i20 screened 3/3 right 2026-10-14: retired |

Independent authors (2026-10-14, origin claude, no files written):

- Docusign author: i10 = h2 (tax part vs total, gold $816.3M; screening) and i11 = h1 asked as "FY2025 spending
  minus all earlier years of the program" ($475M; lures 538, 477), judged likely cleared by the authorization
  arithmetic. Rejected (beyond h4-h10 above): Q2 billings minus revenue; excise accrued vs "1%" (D03 alone);
  restructuring after Q1 FY25 (597K); total authorization $2.5B vs "up to $1.4 billion"; fiscal 2023 buybacks
  alone (D04 fails delete-and-guess); Q1 FY26 billings miss; FY25 margin and Q4 shares vs guidance (exact vs
  rounded, cleared); FX-adjusted guidance ("approximately" footnotes); cash, restricted cash and investments
  change (+58.8M, named rebuild); IAM launch timing (event vs announcement); noncancelable commitments and
  Lexion closing cash (D03 alone); Lexion amortization; customers > $300K, international share, workforce
  cuts, derivative cases (D03 alone); date gaps.
- Paylocity author: i20 = h11 (screening) and i21 = h3 asked "in the fiscal quarter in which it completed its
  Airbase acquisition" ($7.6M; lures 12.6, 44.1), judged likely cleared. Rejected: Q2 SBC vs combined SBC and
  payroll tax (vague-block risk); Headcount Planning edition trap (D06 only dates a launch); outlook in force
  at a quarter end; guidance-implied interest income (rebuild); rest-of-year raises (endpoint rulebook);
  six/nine-month FCF ex-interest (one document); Q3 FCF ex-interest (1.2% gap); ex-interest margins
  (definition named; Q1 rebuildable from D06); adjusted FCF margin (drafting slip); April-only buybacks (D07
  alone); Q2 borrowings (zero gold); client fund obligations gap (two defensible "changes"); goodwill in the
  Airbase quarter (lure 0.03% away); Q1 revenue vs recurring growth (D06 alone); Q1 other-items split;
  payroll taxes as SBC difference; any Docusign-Paylocity comparison (no aligned quarters, different bases);
  FY2024 other financing activities (unexplained reclassification).

The map is navigation; quotes come from the extracted sources.
