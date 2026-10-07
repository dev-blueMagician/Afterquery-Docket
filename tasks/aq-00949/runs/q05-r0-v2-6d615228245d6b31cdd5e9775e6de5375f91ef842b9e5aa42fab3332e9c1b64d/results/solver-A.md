role: blind-solver A (fresh Agent subagent, blind-solver role, packet solver-1)
received: 2026-10-05
input: workspace root, packet path solver-1, q05 rev 0 question text verbatim (nothing else)
tested_sha256: 6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d
tool_uses: 13 | duration_ms: 112572

--- raw return (verbatim as received) ---

**answer:** 22.7 percentage points. EOG's cash was 39.2% of its total debt on Dec 31, 2019 and 61.9% on June 30, 2026.

**confidence:** high

**path:**
1. **December 31, 2019 (D01, the March 16, 2020 press release).** The net-debt reconciliation table at lines 155–173 shows "Current and Long-Term Debt (GAAP) - (b) 5,175" and "Less: Cash (2,028)", in millions. The narrative at line 41 agrees in rounded form: "total debt outstanding was $5.2 billion … $2.0 billion of cash on the balance sheet." The table checks out: 5,175 − 2,028 = 3,147, which matches the printed Net Debt, and 21,641 + 5,175 = 26,816, which matches Total Capitalization. The original file, docs/eog_ex991_2020-03-16.txt, shows the same figures at lines 165 and 169.
2. **June 30, 2026 (D07, the Q2 2026 supplement dated Aug 4, 2026).** The reconciliation at lines 829–835 has "June 30, 2026" as its first column, with "Current and Long-Term Debt (GAAP) - (b) | 7,926" and "Less: Cash | (4,907)".
   - The balance sheet at lines 186, 212 and 216 matches. Cash and Cash Equivalents is 4,907 for June 2026, and Current Portion of Long-Term Debt (27) plus Long-Term Debt (7,899) equals 7,926.
   - The printed Net Debt of 3,019 equals 7,926 − 4,907.
   - The original file, docs/eog_ex991_2026-08-04.txt, shows the same figures at lines 832–833.
3. **Calculation:**
   - 2019: 2,028 / 5,175 = 39.1884%
   - 2026: 4,907 / 7,926 = 61.9102%
   - Change: 61.9102 − 39.1884 = 22.7218, which rounds to 22.7. Rounding each ratio first (61.9 − 39.2) also gives 22.7.

**minimal_documents:** D01 and D07. There are no substitutes. D01 is the only document with 2019 figures (a search for "2019" found matches only in D01). D07 is the only one with a June 30, 2026 balance; D06 stops at March 31, 2026, and D02, D04 and D05 cover earlier quarters.

**readings:**
- **Rounded narrative figures for 2019:** $2.0B / $5.2B = 38.46%. Against the exact 2026 ratio that gives 23.4 points; against D07 figures rounded to billions (4.9 / 7.9 = 62.03%) it gives 23.6. This reading is weaker because D01 prints the exact table values.
- **Long-term debt only, excluding the current portion:** the 2026 ratio would be 4,907 / 7,899 = 62.12%. D01 doesn't split 2019 debt into current and long-term, so this can't be applied to both dates.
- **Relative change instead of points:** the ratio rose about 58%. The question asks for percentage points, so this doesn't apply.

**gaps:**
- I read D01 in full. For D07 I read lines 1–60, 176–245 and 818–857, plus a search for debt and liquidity terms.
- I read D03 only at lines 1–60 (the Encino acquisition announcement; not relevant).
- For D02, D04, D05 and D06 I saw only search hits on the cash and debt rows.
- The documents are text-only, with no PDFs or layout files, so there was no chart or page to check. No extraction problems affected the figures used.

**contaminated:** no

Files used:
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d\solver-1\text\D01.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d\solver-1\text\D07.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d\solver-1\docs\eog_ex991_2020-03-16.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d\solver-1\docs\eog_ex991_2026-08-04.txt
