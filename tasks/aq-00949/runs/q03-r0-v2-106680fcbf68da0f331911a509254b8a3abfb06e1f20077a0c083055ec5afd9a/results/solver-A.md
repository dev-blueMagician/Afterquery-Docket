role: blind-solver A (fresh Agent subagent, blind-solver role, packet solver-1)
received: 2026-10-05
input: workspace root, packet path solver-1, q03 rev 0 question text verbatim (nothing else)
tested_sha256: 106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a
tool_uses: 20 | duration_ms: 256759

--- raw return (verbatim as received) ---

**answer:** Only 2Q 2025. Net cash provided by operating activities was $2,032M. Capital expenditures of $1,523M plus dividends paid of $528M came to $2,051M, so the shortfall was $19M. In every other quarter from 1Q 2025 through 2Q 2026, operating cash flow covered both.

**confidence:** high

**path:**
1. **The measure and the definition (D01, March 16, 2020, line 35).**
   - Measure: "Net cash from operating activities is expected to fund both capital expenditures and dividend payments".
   - Capital spending: "Exploration and development expenditures … including facilities and gathering, processing and other expenditures, and excluding acquisitions and non‐cash exchanges."
2. **Matching it to a reported figure (D07 endnote 5, line 1197; same wording in D04 line 1185, D05 line 1208, D06 line 1195).** Capital Expenditures "include expenditures for Exploration and Development Drilling, Facilities, Leasehold Acquisitions, Capitalized Interest, Dry Hole Costs and Other Property, Plant and Equipment … exclude Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges and Transactions and exploration costs incurred as operating expenses." This matches the plan's definition, so I used "Total Capital Expenditures (Non-GAAP)".
3. **Quarterly figures (D07; $ millions).** Sources are the Net Cash Provided by Operating Activities row (line 278), Dividends Paid (line 297) and Total Capital Expenditures (Non-GAAP) (lines 744/766). D02, D04, D05 and D06 show the same values for the quarters they cover.

| Qtr | Op. cash flow | Capex | Dividends paid | Capex + div | Surplus / (shortfall) |
|---|---|---|---|---|---|
| 1Q25 | 2,289 | 1,484 | 538 | 2,022 | +267 |
| 2Q25 | 2,032 | 1,523 | 528 | 2,051 | **(19)** |
| 3Q25 | 3,111 | 1,648 | 545 | 2,193 | +918 |
| 4Q25 | 2,612 | 1,639 | 550 | 2,189 | +423 |
| 1Q26 | 2,966 | 1,636 | 544 | 2,180 | +786 |
| 2Q26 | 4,669 | 1,587 | 540 | 2,127 | +2,542 |

4. **Checks.**
   - The capex reconciliations add up. For example, 2Q25: 1,883 − 14 − 2 − 270 − 74 = 1,523. 3Q25: 8,544 − 86 − 3 − 6,736 − 71 = 1,648.
   - The totals tie out. 2025 operating cash flow sums to 10,044, dividends to 2,161 and capex to 6,294. 2026 year-to-date operating cash flow is 7,635.
   - The Encino acquisition is excluded under the plan's definition. It was $4,464M in cash in 3Q25 (D07 line 284) and $6,736M of "Acquisition Costs of Properties" in the capex reconciliation (line 764).

**minimal_documents:** D01 + D07, since D07's tables show all six quarters.
- Alternatives: D01 + D06 (1Q25 to 1Q26) + D07 (2Q26). Or D01 + D02 + D04 + D05 + D06 + D07, one quarter from each.
- D03 (the Encino announcement) is not needed.

**readings:**
- **Gross capex less only acquisitions and non-cash items.** This keeps asset retirement and expensed exploration costs in capex. Capex + dividends: 1Q25 2,076 vs 2,289; 2Q25 2,139 vs 2,032 (short 107); 3Q25 2,350 vs 3,111; 4Q25 2,272 vs 2,612; 1Q26 2,237 vs 2,966; 2Q26 2,211 vs 4,669. Still 2Q25 only.
- **Cash-flow-statement additions (oil and gas properties plus other PP&amp;E, excluding the Encino line).** 2Q25: 1,793 + 528 = 2,321 vs 2,032 (short 289). Every other quarter is covered, so still 2Q25 only.
- **Dividends declared instead of paid.** 2Q25 declared $1.995 per share (D07 line 85), which makes its shortfall larger. 3Q25 declared nothing, and the other quarters' declared amounts are close to cash paid. Still 2Q25 only.
- **Rejected readings:**
  - Including the Encino acquisition would add 3Q25 as a shortfall. The plan's definition excludes acquisitions.
  - Using Adjusted Cash Flow from Operations (Non-GAAP) instead of the GAAP measure the plan named gives no shortfall in any quarter (2Q25: 2,496 vs 2,051).

**gaps:**
- The 2Q25 margin is thin ($19M). The packet does not break out cash leasehold acquisitions by quarter. If "acquisitions" were read to exclude leasehold purchases too, contrary to EOG's own definition, that reading can't be computed and could change 2Q25.
- The 4Q 2025 earnings release is not in the packet. I took 4Q25 from the comparative columns in D06 and D07.
- Coverage:
  - Read in full: D01–D04.
  - D05–D07: read only the headers, cash flow statements and capex reconciliations, plus targeted searches. Their income-statement, per-share, per-Boe and key-information sections were not read in full.
  - The sources are .txt files with no PDFs or layout files, so there were no pages to inspect.

**contaminated:** no

Files:
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\solver-1\text\D01.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\solver-1\text\D07.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\solver-1\text\D06.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\solver-1\text\D04.txt
