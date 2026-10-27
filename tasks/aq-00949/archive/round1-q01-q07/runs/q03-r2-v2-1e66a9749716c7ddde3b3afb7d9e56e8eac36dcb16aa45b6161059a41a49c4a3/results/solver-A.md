role: blind-solver A (fresh Agent subagent, blind-solver role, packet solver-1)
received: 2026-10-05
input: workspace root, packet path solver-1, q03 rev 2 question text verbatim (nothing else)
tested_sha256: 1e66a9749716c7ddde3b3afb7d9e56e8eac36dcb16aa45b6161059a41a49c4a3
tool_uses: 20 | duration_ms: 210470

--- raw return (verbatim as received) ---

**answer:** Only in **2Q 2025**. In that quarter, net cash from operating activities was $2,032 million. Capital expenditures plus dividends paid came to $2,051 million, so the shortfall was $19 million. In the other five quarters (1Q, 3Q and 4Q 2025, and 1Q and 2Q 2026), operating cash flow covered both.

**confidence:** high

**path:**
1. **The expectation (D01, line 35):** "Net cash from operating activities is expected to fund both capital expenditures and dividend payments assuming mid-$30 oil prices for the remainder of 2020." The same line defines capex as "including facilities and gathering, processing and other expenditures, and excluding acquisitions and non-cash exchanges." So each quarter's test is: net cash provided by operating activities (GAAP) ≥ capex excluding acquisitions + dividends paid.
2. **Matching capex measure:** D07's endnote 5 (line 1197) says the non-GAAP Capital Expenditures "exclude Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges and Transactions." The same wording appears in D04 and D06. This is the "Total Capital Expenditures (Non-GAAP)" row.
3. **D07 data, $ millions** (cash flow statement lines 276/283/284/295 of the original source file; free cash flow table line 744 of the text file):

| Quarter | Operating cash flow | Non-GAAP capex | Dividends paid | Capex + dividends | Surplus / (gap) |
|---|---|---|---|---|---|
| 1Q25 | 2,289 | 1,484 | 538 | 2,022 | 267 |
| **2Q25** | **2,032** | **1,523** | **528** | **2,051** | **(19)** |
| 3Q25 | 3,111 | 1,648 | 545 | 2,193 | 918 |
| 4Q25 | 2,612 | 1,639 | 550 | 2,189 | 423 |
| 1Q26 | 2,966 | 1,636 | 544 | 2,180 | 786 |
| 2Q26 | 4,669 | 1,587 | 540 | 2,127 | 2,542 |

4. **Cross-check using cash-flow-statement capex** (Additions to Oil and Gas Properties + Additions to Other Property, Plant and Equipment, leaving out the separate Encino acquisition line):

| Quarter | Additions | Plus dividends | Surplus / (gap) |
|---|---|---|---|
| 1Q25 | 1,381+102 = 1,483 | 2,021 | 268 |
| **2Q25** | 1,699+94 = 1,793 | 2,321 | **(289)** |
| 3Q25 | 1,663 | 2,208 | 903 |
| 4Q25 | 1,655 | 2,205 | 407 |
| 1Q26 | 1,644 | 2,188 | 778 |
| 2Q26 | 1,782 | 2,322 | 2,347 |

   Only 2Q 2025 fails here too.
5. **Arithmetic checks:**
   - 2025 column sums reconcile: operating cash flow 10,044, dividends 2,161, non-GAAP capex 6,294.
   - 2026 year-to-date sums reconcile: 7,635, 1,084 and 3,223.
   - The 2Q25 capex reconciles from the GAAP total: 1,883 − 14 − 2 − 270 − 74 = 1,523.
   - Earlier releases report the same figures: D02 (1Q25), D04 (2Q25), D05 (3Q25), D06 (4Q25 and 1Q26).
6. **Oil price premise:** prices were far above mid-$30s (2Q25 composite crude price $64.82/bbl in D04), so the price assumption doesn't excuse the 2Q25 shortfall.

**minimal_documents:** D01 + D07. Alternative set: D01 + D02 + D04 + D05 + D06 + D07, but D07 is still required for 2Q26. D03 is not needed.

**readings:**
- **Non-GAAP "Adjusted Cash Flow from Operations"** in place of GAAP operating cash flow: 2Q25 would be 2,496 vs 2,051, so **no quarters fail**. This is weaker because D01 names "Net cash from operating activities."
- **Including acquisitions** (Total Expenditures (GAAP), or the $4,464M Encino cash outflow): **2Q25 and 3Q25** fail (3Q25: 8,544 + 545 = 9,089 vs 3,111). This contradicts D01's "excluding acquisitions."
- **Dividends declared instead of paid:** still **2Q25 only**. That quarter declared $1.995 per share, which makes its gap larger, and 3Q25 declared nothing.

**gaps:** None material. The sources are text filings with no PDFs or layout files, and column alignment was confirmed by the arithmetic above.
- Read in full: D01–D04.
- Read in part: D05 lines 1–800, D06 lines 1–330, 714–773 and 1100–1206, D07 lines 1–90, 240–314 and 712–771, plus targeted searches.
- Unread sections hold adjusted net income, per-share, per-Boe and net-debt tables, which don't affect this test.

**contaminated:** no

Files used (under `D:\Dev\Docket\tasks\aq-00949\runs\q03-r2-v2-1e66a9749716c7ddde3b3afb7d9e56e8eac36dcb16aa45b6161059a41a49c4a3\solver-1\`):
- `text\D01.txt`
- `text\D07.txt`
- `docs\eog_ex991_2026-08-04.txt`
