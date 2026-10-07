role: blind-solver A (fresh Agent subagent, blind-solver role, packet solver-1)
received: 2026-10-05
input: workspace root, packet path solver-1, q03 rev 1 question text verbatim (nothing else)
tested_sha256: 9a58bd1638c8bddb7fbef69b811750c83ee58e6e36eb16ec18a9e8343336bbf1
tool_uses: 19 | duration_ms: 224353

--- raw return (verbatim as received) ---

answer: Only 2Q 2025 (the three months ended June 30, 2025). In the other five quarters (1Q 2025, 3Q 2025, 4Q 2025, 1Q 2026 and 2Q 2026), net cash from operating activities was larger than capital expenditures plus dividends paid.

confidence: high (2Q 2025 fails under both capex definitions; under EOG's own capex measure the gap is only $19 million)

path:
1. **The expectation (D01, March 16, 2020).** The release says: "Net cash from operating activities is expected to fund both capital expenditures and dividend payments assuming mid-$30 oil prices for the remainder of 2020." The headline is "2020 Capital Expenditures and Dividend Funded with Net Cash from Operating Activities." The release defines capital spending as "including facilities and gathering, processing and other expenditures, and excluding acquisitions and non‐cash exchanges." So the test for each quarter is: Net Cash Provided by Operating Activities (GAAP) ≥ capital expenditures + dividends paid.
2. **The quarterly data (D07, cash flow statements, lines 278–297, and free cash flow reconciliation, lines 722–766).** D07 covers all six quarters: 2025 by quarter, plus 1Q and 2Q 2026. All figures are $ millions. "Cash capex" is Additions to Oil and Gas Properties plus Additions to Other Property, Plant and Equipment.

| Qtr | Operating cash | O&amp;G adds | Other PP&amp;E | Cash capex | Non-GAAP capex | Dividends paid |
|---|---|---|---|---|---|---|
| 1Q25 | 2,289 | 1,381 | 102 | 1,483 | 1,484 | 538 |
| 2Q25 | 2,032 | 1,699 | 94 | 1,793 | 1,523 | 528 |
| 3Q25 | 3,111 | 1,492 | 171 | 1,663 | 1,648 | 545 |
| 4Q25 | 2,612 | 1,543 | 112 | 1,655 | 1,639 | 550 |
| 1Q26 | 2,966 | 1,491 | 153 | 1,644 | 1,636 | 544 |
| 2Q26 | 4,669 | 1,638 | 144 | 1,782 | 1,587 | 540 |

3. **Surplus or shortfall** (operating cash minus capex plus dividends):
   - Using cash capex: 1Q25 +268, **2Q25 −289** (2,032 vs 2,321), 3Q25 +903, 4Q25 +407, 1Q26 +778, 2Q26 +2,347.
   - Using EOG's "Total Capital Expenditures (Non-GAAP)": 1Q25 +267, **2Q25 −19** (2,032 vs 2,051), 3Q25 +918, 4Q25 +423, 1Q26 +786, 2Q26 +2,542.
   - EOG's non-GAAP measure matches the 2020 plan's definition best. D07's endnote 5 (line 1197) says it "exclude[s] Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges."
4. **Cross-checks.**
   - The 2025 full-year column adds up: operating cash 2,289+2,032+3,111+2,612 = 10,044; O&amp;G additions total 6,115; other PP&amp;E 479; dividends 2,161; non-GAAP capex 6,294. The 2026 year-to-date column also adds up: 7,635 / 3,129 / 297 / 1,084 / 3,223.
   - The figures match the original quarterly releases with no restatements. 2Q25 is the same in D04 (lines 265, 271–272, 283, 755), D05, D06 and D07. 1Q25 matches D02, 3Q25 matches D05, and 1Q26 matches D06.
5. **Encino acquisition (3Q 2025).** The $4,464 cash outflow is excluded from capex, as the 2020 definition requires ("excluding acquisitions"). D03 also says the acquisition was to be funded "through $3.5 billion of debt and $2.1 billion of cash on hand."

minimal_documents: D01 + D07. D07 is the only source for 2Q 2026 and repeats every 2025 quarter. An alternative set, D01 + D02 + D04 + D05 + D06 + D07, gives the same figures.

readings:
- **Dividends declared instead of paid.** 2Q25 declared $1.995/share × ~546M shares ≈ $1,089M, which makes the 2Q25 miss larger. 3Q25 declared nothing. Result: still only 2Q 2025.
- **Acquisitions counted as capex.** Using Total Expenditures (GAAP) of 8,544, or adding the $4,464 Encino cash payment, 3Q 2025 also fails, giving 2Q 2025 and 3Q 2025. This contradicts the plan's "excluding acquisitions."
- **Adjusted Cash Flow from Operations (Non-GAAP) instead of the GAAP figure.** This measure was 2,813 / 2,496 / 3,031 / 2,617 / 3,129 / 4,386, so no quarter fails. But it is not "net cash from operating activities."
- **Share buybacks counted.** This would add 1Q25 and 4Q25, but buybacks are not part of the expectation.
- **The mid-$30 oil condition.** It was never in force: the composite oil price in 2Q25 was $64.82. Reading it as a precondition would make the test vacuous. Treated as an assumption, it does not change the answer.

gaps:
- The quarterly release files contain only the supplemental financial tables (no narrative pages), so I found no EOG statement on whether the funding test was met.
- Unread portions, all judged irrelevant (adjusted net income, per-share and per-Boe schedules):
  - D05 lines 311–729 and 810–1214
  - D06 lines 313–711 and 772 to end
  - D07 lines 311–709 and 770–1099
- No extraction problems were found in the decisive rows.

contaminated: no. Only the workspace root, packet path and question were supplied. I did not read question.txt.

Files used:
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r1-v2-9a58bd1638c8bddb7fbef69b811750c83ee58e6e36eb16ec18a9e8343336bbf1\solver-1\text\D01.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r1-v2-9a58bd1638c8bddb7fbef69b811750c83ee58e6e36eb16ec18a9e8343336bbf1\solver-1\text\D07.txt
- Cross-checks: text\D02.txt, D03.txt, D04.txt, D05.txt and D06.txt in the same folder.
