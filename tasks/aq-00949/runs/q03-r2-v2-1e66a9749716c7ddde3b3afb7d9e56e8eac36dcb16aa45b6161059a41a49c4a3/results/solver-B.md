role: blind-solver B (fresh Agent subagent, blind-solver role, packet solver-2)
received: 2026-10-05
input: workspace root, packet path solver-2, q03 rev 2 question text verbatim (nothing else)
tested_sha256: 1e66a9749716c7ddde3b3afb7d9e56e8eac36dcb16aa45b6161059a41a49c4a3
tool_uses: 23 | duration_ms: 232107

--- raw return (verbatim as received) ---

**Answer:** The expectation was not met in one quarter only, 2Q 2025. Operating cash flow was $2,032M against $2,051M of capex plus dividends, a $19M shortfall. It was met in 1Q, 3Q and 4Q 2025 and in 1Q and 2Q 2026.

answer: 2Q 2025 only. Net cash provided by operating activities was $2,032M; capex of $1,523M plus dividends paid of $528M came to $2,051M, leaving a $19M shortfall. The test was met in 1Q 2025, 3Q 2025, 4Q 2025, 1Q 2026 and 2Q 2026.

confidence: high

path:
1. **The expectation (D01, line 35):** "Net cash from operating activities is expected to fund both capital expenditures and dividend payments assuming mid-$30 oil prices for the remainder of 2020." The same line defines the capex scope as "Exploration and development expenditures ... including facilities and gathering, processing and other expenditures, and excluding acquisitions and non‐cash exchanges."
   - The test applied to each quarter is: GAAP net cash provided by operating activities ≥ capex (excluding acquisitions) + dividends paid.
2. **Matching capex measure (D07, endnote 5, line 1197):** "Capital Expenditures exclude Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges and Transactions and exploration costs incurred as operating expenses." This is EOG's "Total Capital Expenditures (Non-GAAP)". D04 endnote 4 says the same.
3. **Data from D07 ($M), quarters 1Q25 / 2Q25 / 3Q25 / 4Q25 / 1Q26 / 2Q26:**
   - Net cash provided by operating activities (lines 278 and 722): 2,289 / 2,032 / 3,111 / 2,612 / 2,966 / 4,669
   - Total capital expenditures, non-GAAP (lines 744 and 766): 1,484 / 1,523 / 1,648 / 1,639 / 1,636 / 1,587
   - Dividends paid (line 297): 538 / 528 / 545 / 550 / 544 / 540
   - Footings check out: operating cash flow 1Q–4Q 2025 sums to 10,044, and the first half of 2026 to 7,635; capex sums to 6,294 and 3,223; dividends paid sum to 2,161 and 1,084.
4. **Calculation (operating cash flow minus capex plus dividends):**

| Quarter | Capex + dividends | Operating cash flow | Surplus / (shortfall) | Result |
|---|---|---|---|---|
| 1Q25 | 2,022 | 2,289 | +267 | met |
| 2Q25 | 2,051 | 2,032 | **−19** | **not met** |
| 3Q25 | 2,193 | 3,111 | +918 | met |
| 4Q25 | 2,189 | 2,612 | +423 | met |
| 1Q26 | 2,180 | 2,966 | +786 | met |
| 2Q26 | 2,127 | 4,669 | +2,542 | met |

5. **Corroboration:** the same 2Q25 figures (2,032; 1,523; 528) appear in D04 (lines 265, 283, 776), D05 (lines 274, 293, 793) and D06 (lines 280, 299, 766). The 1Q25 figures match D02 (lines 265, 282, 767). No 2025–2026 document states the funding result directly, so the answer is computed.

minimal_documents: D01 + D07. D07 is the only source for 2Q 2026 and covers all six quarters. D02, D04, D05 and D06 corroborate the earlier quarters. D03 (the Encino deal announcement) is not needed.

readings:
- **Cash-flow-statement capex** (additions to oil and gas properties plus additions to other property, plant and equipment): same answer.
  - 2Q25: 1,699 + 94 + 528 = 2,321 against 2,032, a shortfall of 289.
  - The other quarters pass: +268, +903, +407, +778 and +2,347.
- **Dividends declared instead of paid** (D07 line 85; 2Q25 had two declarations, $0.975 and $1.02 per share): 2Q25 still fails and the other quarters still pass. This check is approximate.
- **Including acquisitions** (GAAP total expenditures of 8,544 in 3Q25, or the $4,464M Encino cash outflow): 3Q25 would also fail, giving 2Q25 and 3Q25. I reject this because D01 explicitly excludes acquisitions.
- **Non-GAAP "Adjusted Cash Flow from Operations"** (2,496 in 2Q25) instead of GAAP operating cash flow: no quarter fails. I reject this because D01 says "net cash from operating activities".
- **Oil-price premise:** the mid-$30 oil assumption was a condition of the 2020 forecast, not part of the funding test. 2025 WTI averaged $64.78 (D07 line 1119).

gaps:
- No PDFs or layout files are in this packet; the sources are text only. The decisive rows extracted cleanly and are consistent across documents.
- Read in full: D01–D04.
- Read in part:
  - D05: lines 1–320 and 735–804.
  - D06: lines 240–311 and 712–771.
  - D07: lines 1–48, 238–309 and 710–771.
- Not read: the remaining sections of D05–D07 (income-statement detail, balance sheets, adjusted net income, per-Boe tables, key financial information). Greps of D05–D07 found no funding statements or narrative text.

contaminated: no

Packet: D:\Dev\Docket\tasks\aq-00949\runs\q03-r2-v2-1e66a9749716c7ddde3b3afb7d9e56e8eac36dcb16aa45b6161059a41a49c4a3\solver-2\text\ (key files D01.txt and D07.txt)
