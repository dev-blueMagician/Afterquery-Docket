role: blind-solver B (fresh Agent subagent, blind-solver role, packet solver-2)
received: 2026-10-06
input: workspace root, packet path solver-2, q05 rev 1 question text verbatim (nothing else)
tested_sha256: ba6b4f23fa2ac13a1350d87cf2db06b6731994545d24d03c1acd2a56b73d1eac
tool_uses: 13 | duration_ms: 95961

--- raw return (verbatim as received) ---

**answer:** 22.7 percentage points. Cash as a share of total debt rose from about 39.2% at Dec 31, 2019 to about 61.9% at Jun 30, 2026.

**confidence:** high

**path:**
1. **D01** (EX-99.1, March 16, 2020), table "Reconciliation of Net Debt and Total Capitalization", column "At December 31, 2019":
   - "Current and Long-Term Debt (GAAP) - (b) 5,175"
   - "Less: Cash (2,028)"
   - "Net Debt (Non-GAAP) - (c) 3,147". This checks out: 5,175 − 2,028 = 3,147.
   - The narrative (line 41) agrees: "EOG's total debt outstanding was $5.2 billion… Considering $2.0 billion of cash on the balance sheet at the end of the fourth quarter". So "total debt" here means Current and Long-Term Debt.
2. **D07** (EX-99.1, August 4, 2026), "Net Debt-to-Total Capitalization Ratio" table, column "June 30, 2026" (lines 829–836):
   - "Current and Long-Term Debt (GAAP) - (b) | 7,926"
   - "Less: Cash | (4,907)"
   - "Net Debt (Non-GAAP) - (c) | 3,019". This checks out: 7,926 − 4,907 = 3,019.
   - The D07 balance sheet, JUN 2026 column, agrees: "Cash and Cash Equivalents … 4,907", "Current Portion of Long-Term Debt … 27" and "Long-Term Debt … 7,899". 27 + 7,899 = 7,926. The cash flow statement shows "Cash and Cash Equivalents at End of Period" of 4,907 for 2Q 2026.
3. Calculations ($ millions):
   - 2019: 2,028 / 5,175 = 39.188%
   - 2026: 4,907 / 7,926 = 61.910%
   - Change: 61.910 − 39.188 = 22.722, which rounds to **22.7 pp**.
   - Rounding each ratio first (39.2% and 61.9%) also gives 22.7.

**minimal_documents:** D01 and D07.
- The only document with December 31, 2019 figures is D01; a search for "2019" across text/ matched only D01.
- The only document with June 30, 2026 figures is D07.
- I found no replacement for either.

**readings:**
- If you use D01's rounded narrative figures ($2.0B cash / $5.2B debt = 38.46%) with D07's exact figures (61.91%), the change is 23.4 pp. This is weaker, because D01's table gives the exact figures.
- If you also round 2026 to billions (4.9 / 7.9 = 62.03%), the change is 23.6 pp. This is weaker still.
- Both documents label the cash line "Less: Cash", and it equals cash and cash equivalents. So reading "cash" as "cash and cash equivalents" gives the same answer.

**gaps:**
- I did not read D02–D06 in full. I only searched them, for "2019", "June 30, 2026" and "2Q 2026" patterns, and none of them have either date's figures.
- In D07 I read the table of contents, income statement header, balance sheet, cash flow ending rows, the non-GAAP intro and the net debt reconciliation. I did not read the rest.
- The sources are text extractions (method "text", no PDF pages). The table figures add up internally, so there are no extraction problems.

**contaminated:** no

Files used:
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r1-v2-ba6b4f23fa2ac13a1350d87cf2db06b6731994545d24d03c1acd2a56b73d1eac\solver-2\text\D01.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r1-v2-ba6b4f23fa2ac13a1350d87cf2db06b6731994545d24d03c1acd2a56b73d1eac\solver-2\text\D07.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r1-v2-ba6b4f23fa2ac13a1350d87cf2db06b6731994545d24d03c1acd2a56b73d1eac\solver-2\text\manifest.json
