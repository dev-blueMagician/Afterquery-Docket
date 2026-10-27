role: shortcut-auditor (fresh Agent subagent, shortcut-auditor role, packet shortcut)
received: 2026-10-05
input: workspace root, packet path shortcut, q03 rev 1 question text verbatim (nothing else)
tested_sha256: 9a58bd1638c8bddb7fbef69b811750c83ee58e6e36eb16ec18a9e8343336bbf1
tool_uses: 23 | duration_ms: 348415

--- raw return (verbatim as received) ---

answer: Only 2Q 2025. In the March 16, 2020 update, EOG expected net cash from operating activities to cover both capital expenditures (excluding acquisitions and non-cash exchanges) and dividend payments. In 2Q 2025 operating cash flow was $2,032M against $1,523M capex plus $528M dividends paid ($2,051M), a $19M shortfall. The test was met in 1Q, 3Q and 4Q 2025 and in 1Q and 2Q 2026.

verdict: clear (difficulty risk: D07's prior-period columns hold all six quarters, so D01 + D07 is enough)

shortest_path:
1. D01 (`docs\eog_ex991_2020-03-16.txt`, line 33): "Net cash from operating activities is expected to fund both capital expenditures and dividend payments assuming mid-$30 oil prices for the remainder of 2020." Capex there is "including facilities and gathering, processing and other expenditures, and excluding acquisitions and non‐cash exchanges."
2. D07 (`docs\eog_ex991_2026-08-04.txt`) has every quarter. Operating cash flow and dividends paid are on lines 276 and 295 (also line 720). Total Capital Expenditures (Non-GAAP) is on lines 742/764. Endnote 5 (line 1195) says that capex excludes property acquisitions and non-cash exchanges, which matches the 2020 definition.
3. Operating cash flow minus (capex + dividends paid), $M:
   - 1Q25: 2,289 − (1,484 + 538) = +267
   - **2Q25: 2,032 − (1,523 + 528) = −19**
   - 3Q25: 3,111 − (1,648 + 545) = +918
   - 4Q25: 2,612 − (1,639 + 550) = +423
   - 1Q26: 2,966 − (1,636 + 544) = +786
   - 2Q26: 4,669 − (1,587 + 540) = +2,542
4. The original releases (D02, D04, D05, D06) report the same figures as D07, so nothing was restated.

sufficient_documents: D01 + D07 is the minimal verified set.
- Alternatives: D01 + D06 + D07, or D01 + D02 + D04 + D05 + D06 + D07 using each quarter's own release.
- D01 is needed because no other document states the expectation.
- D03 (Encino deal announcement) is not needed. It only supports leaving the 3Q 2025 $4,464M acquisition out.

searches:
- Searched for: fund, mid-$30, 2020 Capital Plan, cover, exceed, shortfall, dividend, Total Capital Expenditures, Total Expenditures (GAAP), Adjusted Cash Flow from Operations, Free Cash Flow, Acquisition Costs, and the capex endnote.
- D01 and D03 were read in full. D02 and D04 were read fully. In D05, D06 and D07 I read the income, balance sheet and cash flow sections, the free cash flow and capex reconciliations, and the endnotes. Everything else in those three was covered by search only.
- Only the "Recoverable"/"refund" hits from those searches turned up beyond D01, and they are false positives. There is no narrative text in D02 or D04–D07 and no answer-shaped summary anywhere. The text/ files mirror docs/, with a 2-line header added.
- I did not open question.txt.

readings/gaps:
- **Adjusted operating cash flow instead of GAAP:** using EOG's non-GAAP "Adjusted Cash Flow from Operations" gives no failing quarter (2Q25: 2,496 vs 2,051). Comparing free cash flow with dividends gives the same result. Both contradict D01's explicit "net cash from operating activities."
- **Including acquisitions:** using Total Expenditures (GAAP) or adding the Encino cash outflow gives 2Q25 and 3Q25 (3Q25: 8,544 + 545 &gt; 3,111). This contradicts D01's "excluding acquisitions."
- **Other readings give the same answer, 2Q25 only:**
  - cash-flow-statement additions instead of non-GAAP capex: shortfall −289, which includes about $270M of property acquisitions;
  - adding exploration costs to capex: −93;
  - dividends declared instead of paid (2Q25 declared $1.995/share): about −574.
  - Adding back the 2Q25 acquisition costs ($10M after tax) still leaves −9.
- **Price premise:** the mid-$30 oil assumption doesn't match 2025–26 prices (WTI about $59–98). I applied the test literally, as the question asks.
- **Precision risk:** the 2Q25 shortfall is small ($19M, under 1%).
- **Coverage:** the per-share and per-barrel tables in D05–D07 were only searched, not fully read; they are not needed for the answer.
