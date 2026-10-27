role: blind-solver B (fresh Agent subagent, blind-solver role, packet solver-2)
received: 2026-10-05
input: workspace root, packet path solver-2, q05 rev 0 question text verbatim (nothing else)
tested_sha256: 6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d
tool_uses: 12 | duration_ms: 104108

--- raw return (verbatim as received) ---

**answer:** 22.7 percentage points. Cash covered about 39.2% of total debt at December 31, 2019 and about 61.9% at June 30, 2026.

**confidence:** high

**path:**
1. **December 31, 2019 (D01, 16 March 2020 press release, reconciliation table, lines 155–171):**
   - Debt: "At December 31, 2019 … Current and Long-Term Debt (GAAP) - (b) 5,175".
   - Cash: "Less: Cash (2,028".
   - The text at line 41 agrees with these: "EOG's total debt outstanding was $5.2 billion … Considering $2.0 billion of cash on the balance sheet." The table checks out: 5,175 − 2,028 = 3,147, which is the printed "Net Debt (Non-GAAP)."
   - The same numbers appear in the original file docs/eog_ex991_2020-03-16.txt at lines 165 and 169.
2. **June 30, 2026 (D07, 4 August 2026 release, Net Debt-to-Total Capitalization table, lines 829–836):**
   - Debt: under the "June 30, 2026" column, "Current and Long-Term Debt (GAAP) - (b) | 7,926".
   - Cash: "Less: Cash | (4,907)".
   - Checks: 7,926 − 4,907 = 3,019, which is the printed Net Debt. The balance sheet (lines 186, 212, 216) shows Cash and Cash Equivalents of 4,907, and current portion 27 plus long-term debt 7,899 equals 7,926.
   - The same numbers appear in the original file docs/eog_ex991_2026-08-04.txt at lines 832–833.
3. **Calculation:**
   - 2019: 2,028 / 5,175 = 39.188%
   - 2026: 4,907 / 7,926 = 61.910%
   - Change: 61.910 − 39.188 = 22.722, which rounds to **22.7 percentage points**.
   - I checked both divisions by long division (0.391884… and 0.619101…).

**minimal_documents:** D01 and D07. Neither can be swapped out. D01 is the only document that mentions 2019 (a search for "2019" across text/ found matches only in D01). D07 is the only document with June 30, 2026 balances. D06 runs only through March 31, 2026, and D02–D05 cover 2025.

**readings:**
- **Rounded 2019 figures:** Using the narrative's $2.0B / $5.2B gives 38.46% for 2019, so 61.91 − 38.46 = 23.4 percentage points. This is less precise than the table, which states both numbers exactly.
- **Long-term debt only:** Leaving out the current portion of long-term debt gives 4,907 / 7,899 = 62.12% for 2026. D01 doesn't split the 2019 debt between current and long-term, though, and "total debt" in D01 refers to the combined figure. So this reading can't be applied consistently, and I rejected it.
- **Relative change:** The question asks for percentage points, so a percent change in the ratio doesn't apply.

**gaps:**
- I read D01 and D07 in full and only the first 70 lines of D03 (an acquisition announcement with no relevant balances).
- I did not read D02, D04, D05 and D06 in full. I only searched them for "2019", "June 30, 2026"/"JUN", "total debt", "debt outstanding" and cash-balance phrases, and none of them had data for either date.
- The documents are text sources with no PDF pages, so there were no page images to check. The table rows came through cleanly and match the originals.

**contaminated:** no
