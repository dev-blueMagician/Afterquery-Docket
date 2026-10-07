# q01 rev 0 blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

tested_sha256: 562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87
Prompt: workspace root, packet path solver-1, question verbatim. Return copied verbatim from the task notification.

---

answer: Microchip's inventory was **$309.0 million** below its end-of-2024 peak on June 30, 2026: an implied peak of $1,356.3M minus $1,047.3M.

confidence: high

path:
1. **Time window.** D04 covers the first quarter of fiscal 2027: "FIRST QUARTER OF FISCAL YEAR 2027" (D04 line 6), "results for the three months ended June 30, 2026" (line 20). So the quarter closed on June 30, 2026.
2. **June 30, 2026 balance.** D04's balance sheet ("in millions", line 195) shows `|Inventories|1,047.3|1,035.4|` for June 30, 2026 and March 31, 2026 (line 203). So the balance was $1,047.3M.
3. **The end-of-2024 peak.** In D06 line 46, the CFO states: "During the quarter, we reduced inventory by $22.3 million and lowered days of inventory from 201 days in December to 185 days in March... From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million." That statement is as of March 31, 2026. D06's balance sheet shows March 31, 2026 inventory of `1,035.4` (line 229).
4. **Consistency check (D05).** The December 31, 2025 balance is `1,057.7` (D05 line 205). 1,057.7 − 1,035.4 = 22.3, which matches D06's "$22.3 million". So the CFO's figure lines up with the balance sheets.
5. **Calculation.**
   - Implied December 2024 peak = 1,035.4 + 320.9 = $1,356.3M.
   - Gap at June 30, 2026 = 1,356.3 − 1,047.3 = **$309.0M**.
   - Cross-check: inventory rose 1,047.3 − 1,035.4 = 11.9 in the June quarter, and 320.9 − 11.9 = 309.0.
6. No document in the packet prints the December 2024 balance directly. A search for "1,356" found nothing, and "320.9" appears only in D06 line 46. The peak therefore has to be derived as in step 5.

minimal_documents: D04 and D06. D04 gives the June 30, 2026 and March 31, 2026 balances. D06 gives the $320.9M reduction from the December 2024 high point and the March 31, 2026 balance. D05 only confirms the numbers and can't replace D06, because its balance sheet compares December 31, 2025 with March 31, 2025, not December 2024. No other document can stand in for D06.

readings:
- **Using the March figure as is:** Taking D06's "$320.9 million" without updating it gives $320.9M. That measures the gap at March 31, 2026 (end of fiscal 2026), not at the close of Q1 fiscal 2027. It misses the $11.9M inventory increase during the June quarter.
- **Using the earliest balance in the packet as the peak:** March 31, 2025 inventory was $1,293.5M (D05 line 205, D06 line 229). Using it gives 1,293.5 − 1,047.3 = $246.2M. That date isn't end-of-2024, and D06 names December 2024 as the high point, so this reading doesn't fit the question.
- **As a percentage:** 309.0 / 1,356.3 ≈ 22.8% below the peak. The question asks for dollars, so this isn't the answer.

gaps:
- The December 31, 2024 balance isn't printed anywhere in the packet. It's inferred from the CFO's statement plus the March 31, 2026 balance sheet, and the result depends on that statement being exact to $0.1M.
- I read D04, D05 and D06 in full. I didn't read D01–D03 (Analog Devices), D07–D09 (onsemi) or D10–D12 (Texas Instruments) in full. I searched all of them for "Microchip", "high point", "peak", "December 2024", "1,356", "1356", "309.0" and "320.9". The only non-Microchip hits were "peak" inside the word "speaks" in onsemi boilerplate (checked D08 line 109).
- The sources are .txt files (manifest method "text", pages null), so there are no PDF pages or layout files to check. I didn't read question.txt, following the instructions.

contaminated: no

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\solver-1\text\D04.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\solver-1\text\D06.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\solver-1\text\D05.txt
