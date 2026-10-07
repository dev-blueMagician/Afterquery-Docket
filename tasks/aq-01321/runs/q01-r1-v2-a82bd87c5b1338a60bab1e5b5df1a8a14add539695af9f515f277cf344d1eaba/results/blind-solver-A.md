# q01 rev 1 blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

tested_sha256: a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba
Prompt: workspace root, packet path solver-1, question verbatim. Return copied verbatim from the task notification.

---

answer: $309.0 million

confidence: high

path:
1. The period is the close of Microchip's first quarter of fiscal 2027, which is June 30, 2026. D04 (FQ1 2027 release), page 1: "today reported results for the three months ended June 30, 2026" under the heading "FIRST QUARTER OF FISCAL YEAR 2027".
2. The peak at the end of calendar 2024 is stated as a cumulative reduction, not a dollar level. D06 (FQ4 2026 release, filed 2026-05-07), page 2, CFO quote: "From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million." This is measured as of March 31, 2026. The same quote says: "During the quarter, we reduced inventory by $22.3 million". I confirmed this wording in the original docs/ file, line 44.
3. Inventory on March 31, 2026 was $1,035.4M. The D06 balance sheet, page 9, shows "|Inventories|1,035.4|1,293.5|" (March 31, 2026 and March 31, 2025). D04, page 8, shows the same 1,035.4 figure.
4. Inventory on June 30, 2026 was $1,047.3M. The D04 balance sheet, page 8, shows "|Inventories|1,047.3|1,035.4|" (June 30, 2026 and March 31, 2026, in millions).
5. The CFO's figures use the same balance-sheet basis. The D05 balance sheet, page 8, shows "|Inventories|1,057.7|1,293.5|" (December 31, 2025 and March 31, 2025). 1,057.7 − 1,035.4 = 22.3, which matches the $22.3M quarterly reduction in D06.
6. Calculation:
   - Implied peak at the end of December 2024: 1,035.4 + 320.9 = $1,356.3M.
   - Reduction by June 30, 2026: 1,356.3 − 1,047.3 = **$309.0M**.
   - Check: inventory rose during the June 2026 quarter by 1,047.3 − 1,035.4 = 11.9, and 320.9 − 11.9 = 309.0.
7. Inventory days fell during the June quarter (D04: "inventory days declining from 185 days on March 31 to 175 days on June 30"). Inventory in dollars still rose by $11.9M, so the cumulative reduction from the peak shrank from $320.9M to $309.0M.

minimal_documents: D04 and D06. D04 provides the June 30, 2026 and March 31, 2026 inventories. D06 provides the "$320.9 million" reduction from the December 2024 high point, anchored at March 31, 2026. D05 only corroborates the $22.3M figure and cannot replace either one, since it has neither the December 2024 figure nor the June 2026 figure. I found no alternative set; no other document mentions Microchip.

readings:
- Using the stated cumulative figure without updating it for the first quarter of fiscal 2027 gives $320.9M. That is the position at March 31, 2026, the end of fiscal 2026, so it is the wrong time window.
- Treating March 31, 2025 inventory ($1,293.5M) as the "peak" gives 1,293.5 − 1,047.3 = $246.2M. This doesn't fit the question, because March 2025 is not the end of calendar 2024, and D06 places the high point at the end of December 2024.
- Assuming inventory kept falling in the June 2026 quarter, because inventory days dropped, would overstate the answer. The balance sheet shows a $11.9M increase.

gaps:
- The December 31, 2024 inventory level ($1,356.3M) is never printed in the packet. I derived it from D06's $320.9M and the March 31, 2026 balance. If the release's $320.9M was calculated from unrounded amounts, the result could be off by about ±$0.1M. The printed figures give exactly 309.0.
- Coverage: I read D04, D05 and D06 in full. I did not read the ADI, onsemi and TI documents (D01–D03, D07–D12) in full. A search found no "Microchip" or "MCHP" mention in them, and their "peak/high point" hits are in onsemi documents (D07–D09).
- The extraction method is "text", so there are no PDF pages or layout files. I checked the decisive rows against the original docs/*.txt files and they match.

contaminated: no

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\solver-1\text\D04.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\solver-1\text\D06.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\solver-1\text\D05.txt (corroboration only)
