# q01 rev 0 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

tested_sha256: 562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87
Prompt: workspace root, packet path solver-2, question verbatim. Return copied verbatim from the task notification.

---

answer: About $309.0 million. Microchip's inventory was $1,047.3 million on June 30, 2026. The implied end-of-December-2024 peak is $1,356.3 million.

confidence: high

path:
1. **Which quarter.** D04 (Microchip's results for the first quarter of fiscal 2027, filed 2026-08-06), line 20: it "reported results for the three months ended June 30, 2026." The close of the quarter is therefore June 30, 2026.
2. **Inventory at that date.** D04 balance sheet, "(in millions, unaudited)", line 203: "|Inventories|1,047.3|1,035.4|", under the columns June 30, 2026 and March 31, 2026.
3. **The peak.** D06 (results for the fourth quarter of fiscal 2026, filed 2026-05-07), line 46, CFO Eric Bjornholt: "During the quarter, we reduced inventory by $22.3 million … From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million." "Now" means March 31, 2026. The D06 balance sheet (line 229) shows March 31, 2026 inventories of 1,035.4, the same figure as the comparative column in D04.
4. **Implied peak.** 1,035.4 + 320.9 = $1,356.3 million at the end of December 2024. The packet has no December 31, 2024 balance sheet, so this figure has to be derived.
5. **Gap at June 30, 2026.** 1,356.3 − 1,047.3 = 309.0. Cross-check: inventory rose 1,047.3 − 1,035.4 = 11.9 in the June quarter, and 320.9 − 11.9 = 309.0.
6. **Consistency check that the $320.9M uses the balance-sheet inventory line.** D05 (third quarter of fiscal 2026) balance sheet, line 205, shows December 31, 2025 inventories of 1,057.7. 1,057.7 − 1,035.4 = 22.3, which matches D06's "reduced inventory by $22.3 million". So the CFO's dollar figures track the balance-sheet line.
7. **Days versus dollars.** D04 line 36 ("inventory days declining from 185 days on March 31 to 175 days on June 30") is measured in days. The dollar balance actually rose slightly over the quarter.

minimal_documents: D04 and D06. D04 gives the June 30, 2026 and March 31, 2026 balances. D06 gives the $320.9M reduction from the December 2024 high point. No other document in the packet states the December 2024 peak or the size of the reduction from it, so D06 cannot be replaced. D05 only corroborates the figures.

readings:
- **Reading "end-of-2024" as fiscal year-end 2025 (March 31, 2025, inventories 1,293.5 in D05 and D06):** 1,293.5 − 1,047.3 = $246.2M. This is weak. The question says "end-of-2024 peak", and D06 explicitly puts the high point "at the end of December 2024."
- **Using D06's $320.9M directly:** that figure measures the gap as of March 31, 2026, not at the end of the June quarter. It ignores the $11.9M increase during the June quarter, so it does not answer the question as asked.
- **Main reading:** $309.0M.

gaps:
- The peak balance is derived from the CFO's statement plus the March 31, 2026 balance. No December 31, 2024 balance sheet is in the packet.
- The packet has no layout files or PDFs: the manifest lists "method": "text" with "pages": null, and docs/ holds only .txt files. No page images could be checked, and none were needed.
- Fully read: D04, D05, D06.
- Not fully read: D01–D03 (Analog Devices), D07–D09 (onsemi), D10–D12 (Texas Instruments). I searched them instead:
  - "Microchip|MCHP" matched only D04–D06.
  - "high point|peak|320.9|1,356|1356" matched long lines in D07–D09. I did not open those lines. They are in onsemi releases that don't mention Microchip.

contaminated: no

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\solver-2\text\D04.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\solver-2\text\D06.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r0-v2-562912f20c2f52b1e77bdfc122bd851e98faf943a17fd1335ebe4cf76d989b87\solver-2\text\D05.txt (corroboration only)
