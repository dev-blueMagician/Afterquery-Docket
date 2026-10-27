role: blind-solver B (fresh Agent subagent, blind-solver role, packet solver-2)
received: 2026-10-05
input: workspace root, packet path solver-2, q03 rev 0 question text verbatim (nothing else)
tested_sha256: 106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a
tool_uses: 22 | duration_ms: 274285

--- raw return (verbatim as received) ---

**answer:** 2Q 2025 is the only quarter. Net cash from operating activities was $2,032M, while capital expenditures plus dividends paid came to $1,523M + $528M = $2,051M, so it fell short by $19M. In the other five quarters the cash covered both.

**confidence:** high

**path:**
1. **The measure and the capex definition (D01, line 35).** The March 2020 release says: "Net cash from operating activities is expected to fund both capital expenditures and dividend payments assuming mid-$30 oil prices…". It defines capital spending as: "Exploration and development expenditures… including facilities and gathering, processing and other expenditures, and excluding acquisitions and non‐cash exchanges." The headline on line 27 repeats this: "2020 Capital Expenditures and Dividend Funded with Net Cash from Operating Activities". So the measure is the GAAP line "Net Cash Provided by Operating Activities".
2. **How later releases define capex (D07 endnote 5, line 1197; same wording in D04, D05 and D06).** "Capital Expenditures include… Facilities, Leasehold Acquisitions, Capitalized Interest, Dry Hole Costs and Other Property, Plant and Equipment… exclude Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges and Transactions and exploration costs incurred as operating expenses." This is the reported "Total Capital Expenditures (Non-GAAP)". Like the 2020 definition, it includes facilities and other plant and equipment, and it excludes acquisitions and non-cash exchanges.
3. **Quarterly figures from D07, which has all six quarters ($M):**
   - Cash flow statement, line 278: Net Cash Provided by Operating Activities is 2,289 / 2,032 / 3,111 / 2,612 (2025) and 2,966 / 4,669 (2026).
   - Cash flow statement, line 297: Dividends Paid is 538 / 528 / 545 / 550 and 544 / 540.
   - Capex reconciliation, line 766: Total Capital Expenditures (Non-GAAP) is 1,484 / 1,523 / 1,648 / 1,639 and 1,636 / 1,587.
   - The 2Q 2025 figures are the same in D04 (lines 265, 283, 776), D05 and D06.
4. **Cash minus (capex + dividends):**

| Quarter | Calculation | Result |
|---|---|---|
| 1Q25 | 2,289 − 2,022 | +267 |
| **2Q25** | **2,032 − 2,051** | **−19** |
| 3Q25 | 3,111 − 2,193 | +918 |
| 4Q25 | 2,612 − 2,189 | +423 |
| 1Q26 | 2,966 − 2,180 | +786 |
| 2Q26 | 4,669 − 2,127 | +2,542 |

5. **Stricter reading of the 2020 wording.** This version keeps exploration costs and asset retirement costs in capex. It takes Total Expenditures (GAAP) from D07 line 756 and removes only acquisitions and non-cash items (lines 760–764):
   - 1Q25: 1,546 − 9 + 1 = 1,538
   - 2Q25: 1,883 − 2 − 270 = 1,611
   - 3Q25: 8,544 − 3 − 6,736 = 1,805
   - 4Q25: 1,730 − 10 + 2 = 1,722
   - 1Q26: 1,768 − 52 − 23 = 1,693
   - 2Q26: 1,919 − 53 − 2 − 193 = 1,671

   Adding dividends gives these margins: +213, **−107**, +761, +340, +729, +2,458. Only 2Q25 falls short. Also leaving out asset retirement costs only changes 2Q25 to −93.
6. **Cash-flow-statement additions.** Using additions to oil and gas properties plus other plant and equipment (D07 lines 285–286), 2Q25 is 1,699 + 94 + 528 = 2,321 against 2,032, a shortfall of 289. All other quarters still have a surplus.
7. **The Encino acquisition (3Q25).** The acquisition costs of 6,736 (line 764), or the 4,464 cash outflow on line 284, are excluded under the plan's "excluding acquisitions" rule. That is why 3Q25 does not fall short.

**minimal_documents:** D01 + D07. Alternatives: D01 + D06 covers 1Q25–1Q26 but still needs D07 for 2Q26; or D01 + D02, D04, D05, D06 and D07 quarter by quarter. D03 (the Encino deal announcement) is not needed.

**readings:**
- **Adjusted cash flow instead of the named measure.** Using EOG's non-GAAP "Adjusted Cash Flow from Operations" (2Q25: 2,496, D07 line 742), there is no shortfall in any quarter, so the answer would be none. This goes against "using that measure", because the plan named the GAAP net cash figure.
- **Including acquisitions.** Using Total Expenditures (GAAP) with acquisitions left in would give 2Q25 and 3Q25 (8,544 + 545 &gt; 3,111). This contradicts the plan's "excluding acquisitions" wording.
- **Dividends declared instead of paid.** 2Q25 declared $1.995 per share, 3Q25 declared nothing (D07 line 85). Only 2Q25 still falls short.

**gaps:**
- D02 and D04–D07 contain only the supplemental tables (contents pages start at page 12). The narrative pages of those earnings releases are not in the packet.
- The 2020 wording does not say whether expensed exploration costs or asset retirement costs count as capex. Steps 5–6 show this does not change the answer.
- I did not read in full the adjusted-EPS, per-barrel and balance-sheet sections of D04–D07. Keyword searches of those files found no conflicting figures.
- All documents are text-only (no PDFs), so there are no page images to check against.

**contaminated:** no. The packet folder contains a question.txt, which I did not read.

Files used:
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\solver-2\text\D01.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\solver-2\text\D07.txt
- Cross-checks in D04.txt, D05.txt and D06.txt in the same text\ folder
