# q01 rev 0 shortcut audit (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

tested_sha256: 562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87
Prompt: workspace root, packet path shortcut, question verbatim. Return copied verbatim from the task notification.

---

answer: $309.0 million. At June 30, 2026, the end of Q1 FY2027, Microchip's inventory was $1,047.3M. The December 2024 high point works out to $1,356.3M, so the balance was 1,356.3 − 1,047.3 = $309.0M below that peak.

verdict: clear

shortest_path:
1. D06 (Q4 FY2026 release, filed 2026-05-07), text line 46 (docs line 44), where the CFO says: "During the quarter, we reduced inventory by $22.3 million and lowered days of inventory from 201 days in December to 185 days in March... From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million."
2. D06 balance sheet (text line 229): "|Inventories|1,035.4|1,293.5|" for March 31, 2026 and March 31, 2025. So the peak was 1,035.4 + 320.9 = 1,356.3.
3. D04 (Q1 FY2027 release, filed 2026-08-06) balance sheet (text line 203): "|Inventories|1,047.3|1,035.4|" for June 30, 2026 and March 31, 2026.
4. 1,356.3 − 1,047.3 = 309.0. The same result comes from 320.9 − (1,047.3 − 1,035.4 = 11.9) = 309.0.
5. Consistency check: D05 shows $1,057.7M at December 31, 2025. 1,057.7 − 1,035.4 = 22.3, which matches D06's "$22.3 million" reduction for that quarter. So the $320.9M figure is measured from the March 31, 2026 balance.

Why this isn't a shortcut: D04 never mentions the peak. Its narrative only gives inventory days ("declining from 185 days on March 31 to 175 days on June 30"). D06 gives the reduction from the peak, but only up to March 2026, and has no June 2026 balance. No document in the packet prints the peak value of 1,356.3 or the answer of 309.0. You need both documents and one subtraction step.

Difficulty risk: This is a simple two-document route. The question's phrase "end-of-2024 peak" closely echoes D06's "high point at the end of December 2024," so a keyword search finds the anchor quickly. A second step is still required, because inventory rose by $11.9M in Q1 FY2027 even though inventory days fell. Days going down while dollars went up is a natural trap.

sufficient_documents: D04 + D06 (minimal, verified). There are no alternatives. D06 is the only source for the December 2024 peak, and D05 can't stand in for it because its balance sheet compares against March 31, 2025 and it never mentions the peak. D04 is the only source for the June 30, 2026 balance. The March 31, 2026 anchor of 1,035.4 appears in both D04 and D06.

searches:
- Terms searched: "inventor", "peak", "high point", "December 2024", "end of 2024", "320.9", "1,356", "309", "Microchip|MCHP", "reduced inventory", "days of inventory", "inventory by $", and the balance values 1,047.3, 1,035.4, 1,057.7 and 1,293.5.
- I read D04, D05 and D06 in full (text/). I re-checked the key D06 quote and all three Inventories rows in the original docs/ files, and they match.
- Microchip appears only in D04–D06 (plus the manifest). For the other companies I only ran keyword searches: ADI (D01–D03), onsemi (D07–D09) and TI (D10–D12). The "309" hits in those files are unrelated values.

readings/gaps:
- Stale reading: $320.9M. That figure is as of March 31, 2026 and misses the $11.9M build in Q1 FY2027. Rejected because it's the wrong period.
- Fiscal-year misreading: treating the FY2025 year-end balance (March 31, 2025, $1,293.5M) as "end-of-2024" gives 1,293.5 − 1,047.3 = $246.2M. Rejected: that date isn't the end of calendar 2024, it isn't the stated high point, and it's below the implied December 2024 balance.
- The fiscal 2024 year-end (March 2024) balance isn't in the packet, and D06 explicitly puts the high point at December 2024, so that reading isn't supported.
- Gaps: none for the Microchip documents. The 1,356.3 peak is derived, not printed.

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\shortcut\text\D06.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\shortcut\text\D04.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\shortcut\text\D05.txt (consistency check only)
