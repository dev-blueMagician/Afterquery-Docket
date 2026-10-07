# aq-00949 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Round 1, 2026-10-05. Inventory from the map's shared ground, the caller's reading and the
question-author's round-1 return (origin: claude). Line numbers are text/Dnn.txt lines.
Structural facts: the five series editions agree on every overlapping visible figure, and D07
covers FY2021-FY2025 annual plus 2025-2026 quarterly, so most series-only asks are one-document
(D07). Individually necessary inputs come from D01, D03, or edition-unique series facts (each
edition's EPS walk, its year-to-date column, its footnotes; D02's 1Q24 per-Boe column).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D06 79/89/125 (1Q26 Other International crude 0.1, $89.12; note B "Production volumes from Bahrain operations"); D07 79/89/123/923 (2Q26 0.5, $103.40; note B "Crude oil and condensate volumes are from UAE and Bahrain operations"; endnote 1 "2025 volumes are from Bahrain operations"); D05 111/123 (Bahrain named, gas price only, 3Q25) | First quarter of Bahrain crude output (4Q25) and of UAE crude output (2Q26) | Same series, right edition; mentions it vs does it | D07 alone puts UAE in 1Q26 or 2Q26 (row-wide note); reading the note as covering 2026 gives 1Q26. D05 names Bahrain in 3Q25 but only for gas: 3Q25 decoy | Hidden ranges near the rows are numeric volume tables; "—" also prints for FY25 although 4Q25 is 0.1 | sketch i01 |
| h2 | D03 47 (dividend $1.02 declared May 30, 2025, payable October 31, 2025); D06 471-487 (4Q25 to 1Q26 walk, volume step (0.11)) | Volume effect on diluted EPS in the quarter after the raised dividend's payment quarter | Scatter the pieces (date bridge) | Declaration date route: 2Q25 -> 3Q25 walk +0.32/+0.33; D07 walk +0.14 | Overview prints "October 31, 2025" for Doc 3; D07 hidden BOE rows let a solver recompute | sketch i02 (fallback) |
| h3 | D01 41/197 (end-2019 debt-to-total capitalization 19%, table 5,175 / 26,816); series GAAP ratios (D05 675: 20.3% at Sep 30, 2025; <=13.9% before); D05 473-481 (2Q25 to 3Q25 walk, volume step 0.32) | Volume effect on GAAP diluted EPS in the first quarter whose quarter-end GAAP debt ratio exceeded the end-2019 level | Scatter the pieces (threshold bridge) | Net-debt ratio route points to Dec 31, 2025 (no walk into 4Q25); adjusted walk 0.33 | Overview prints "19% debt-to-total-capitalization ratio" for Doc 1 | sketch i03 (fallback, same family as i02) |
| h4 | D04 221-241, 577-585 (Encino costs: Adjusted NI 18 pre-tax incl. $6M financing; CFO add-back 10 after tax, G&A only) | Encino cost treatment differs by measure | Mentions it vs does it | Not applicable | One document holds both | rejected: one source |
| h5 | D02 185/553 (old "Cash Flow from Operations Before Changes in Working Capital") vs D04 561 onward (renamed, acquisition add-back) | Free cash flow under the pre-Encino definition | Same series, right edition | Not applicable | D04-D07 restate the change and the add-backs | rejected: D02 not necessary |
| h6 | D06/D07 457 (FY24 impairments "primarily" Rocky Mountain) + D02/D04/D05 per-Boe 4Q24 (254) | Quarter of the Rocky Mountain write-down | Who belongs where | Not applicable | Both sides duplicated; "primarily" blocks a clean tie | rejected |
| h7 | D01 35 (2020 crude target 446,000-466,000 bopd) + D07 79-81 (2Q26 crude 548.8 MBbld) | Growth of crude output over the 2020 target | Calculate across documents; unit normalization | Not applicable | Lookup plus one calculation (platform history: too easy) | parked |
| h8 | D01 41/199 (net debt ratio 13%, exact 12.70%) vs series ratios | Change in net-debt ratio since 2019 | Exact table vs rounded prose | 13% vs 12.70% flips one-decimal answers | Answered-inconsistently risk | rejected |
| h9 | Five walks (D02, D04, D05, D06, D07) | Ranking of realized-price EPS effects | Ordered answers | Not applicable | Exhaustive labelled lookups | parked |
| h10 | D01 49 vs D03 63 (proved-reserve countries: China dropped) | Country dropped | Match, then exclude | Not applicable | Two-lookup comparison; public knowledge | rejected |
| h11 | D03 47 ($3.5B debt + $2.1B cash funding; $1.02 dividend) vs series balance-sheet debt/cash and cash-flow dividends (hidden rows) | Planned vs actual funding; dividends paid | Forecast vs actual | Needs hidden rows | Requires a complete capture of Docs 2, 4-7 | superseded by round 2 (h13, h16) |

Round 2, 2026-10-05 (complete capture AQ-00949_2026-10-06_0251.md, re-split and re-extracted; no
gaps). Caller read every line of D01-D07 after the re-ingest. D06/D07 line numbers are after the
splitter fix (2 lower than the first re-extraction). Structural finding: the formerly hidden
statements agree across editions except the 2026 "Other" recast (PRM folded in) and relabels
(mapper and caller's cell-by-cell script). So every 2025 quarter is repeated in D06 and D07, and
D07 alone can rebuild most walk steps. Individually necessary inputs: D01 and D03 facts, D07-only
2Q 2026 / June 30, 2026 / 1H 2026 values, D05-only items (Bapco name, Sep 30, 2025 PRM split),
and edition walks (rebuildable from later editions, disclosed risk).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h12 | D01 27/35 (2020 plan: "Net cash from operating activities is expected to fund both capital expenditures and dividend payments"; capital plan = exploration and development expenditures "excluding acquisitions and non-cash exchanges"); D07 278/285-286/297/744 (quarterly GAAP CFO, additions, dividends paid, non-GAAP capex 1Q25-2Q26) | Quarter in which GAAP CFO fell short of capex plus dividends paid: 2Q 2025 only, under every acquisition-excluding capex measure | Definition applied to an instance; match then exclude (acquisitions) | FCF/adjusted-CFO route -> none; capex-only (overview wording) -> none; Encino-inclusive investing or GAAP total expenditures -> 2Q25 and 3Q25; adding buybacks -> 1Q25, 2Q25, 4Q25 | 2Q25 margin is 19 on non-GAAP capex (289 on cash additions); 2Q25 is also the lowest-CFO quarter, so a lazy heuristic lands on it; D01 overview mentions only CFO funding of the plan | sketch i04 |
| h13 | D03 47 ($1.02 declared May 30, 2025; payable Oct 31; indicated annual rate $4.08); D07 85 (dividends declared 2Q25 1.9950, 3Q25 -, 4Q25-2Q26 1.0200) | Declared over 3Q25-2Q26 = 3.06 vs indicated 4.08 | Temporal alignment | Lazy 4 x 1.02 | Every lazy route coincides with a correct total in some window (4.08 through 2Q26; 3.06 = three quarters from 3Q25), and the table prints the dash | rejected: no discriminating window |
| h14 | D01 51-59 (Investor Contacts: Streit, Panchal; "Media and Investor Contact": Ehmer); D03 65-75 (Investor Contacts: Hammond, Panchal, O'Connor; "Media Contact": Ehmer) | Investor contact at both events: Neel Panchal | Who belongs where; match then exclude | Ehmer is listed in both releases but only as media contact in 2025 | Boilerplate subject (trivia risk); closed-book recall of EOG's long-time IR contact | sketch i05 |
| h15 | D01 159-199 (end-2019 ratios 19%/13%, exact 19.30%/12.70%); D07 840-842 (quarter-end ratios Jun 2025-Jun 2026) | Quarter-ends with gross ratio above and net ratio below end-2019: Sep 2025, Mar 2026, Jun 2026 | Match then exclude | Dec 31, 2025 (13.2% net) is the excluded item; rounded and exact thresholds agree | Explicit numeric filter over one five-column table: exhaustive lookup (platform history: solved) | held |
| h16 | D03 19 ($5.6B incl. net debt); D07 284 (Encino outflow (4,464) 3Q25, 13 4Q25, (4,451) FY25; none in 2026) | Price minus net cash outlay through Jun 30, 2026 = 1,149 | Calculate across documents | Closing-quarter figure (4,464) -> 1,136 | Mixes a price including assumed net debt with cash net of cash acquired (meaning not stated); FY column printed | rejected |
| h17 | D03 47 (record date Oct 17, 2025) -> Sep 30, 2025; D05 186/210 (PRM assets 19, liabilities 17, split shown only in D05) | Net derivative position at the last quarter-end before the record date | Same series, right edition | D06/D07 fold PRM into Other | One-sentence date bridge into labelled cells (q02 failure pattern) | rejected |
| h18 | D03 (May 30, 2025) -> latest completed quarter 1Q25 -> D02 walk (realized prices +0.43); decoy D04 walk (-0.90) | Temporal precedence into an earlier edition | Same series, right edition | 2Q25 walk | D04's 2Q25 Encino costs let a reader place the deal without D03; walk rebuildable from D04/D05; same family as q02 | rejected |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
