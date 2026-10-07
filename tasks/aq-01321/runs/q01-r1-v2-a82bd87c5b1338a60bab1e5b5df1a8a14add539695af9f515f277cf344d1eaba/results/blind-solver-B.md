# q01 rev 1 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

tested_sha256: a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba
Prompt: workspace root, packet path solver-2, question verbatim. Return copied verbatim from the task notification.

---

I found the answer by combining two Microchip earnings releases. No document states it directly.

answer: $309.0 million

confidence: high

path:
1. **Reduction from the peak to March 31, 2026.** D06 (the fiscal Q4 2026 release, filed 2026-05-07), text/D06.txt line 46 (source doc line 44). The CFO says: "During the quarter, we reduced inventory by $22.3 million … From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million." "High point at the end of December 2024" is the same thing as the question's "peak at the end of calendar 2024."
2. **Inventory on March 31, 2026.** D06 balance sheet, line 229: "|Inventories|1,035.4|1,293.5|" (columns are March 31, 2026 and March 31, 2025; in millions). D04 line 203 repeats the 1,035.4 figure in its prior-period column.
   - So the December 2024 peak works out to 1,035.4 + 320.9 = $1,356.3M.
3. **Close of Q1 fiscal 2027 is June 30, 2026.** D04 line 20: "reported results for the three months ended June 30, 2026." The D04 balance sheet, line 203, reads "|Inventories|1,047.3|1,035.4|" (June 30, 2026 and March 31, 2026; "in millions").
4. **Calculation.** 1,356.3 − 1,047.3 = 309.0. Checked another way: inventory rose 1,047.3 − 1,035.4 = 11.9 during the June quarter, and 320.9 − 11.9 = 309.0.
5. **Consistency check against D05.** The December 31, 2025 inventory in D05 (line 205) is 1,057.7. That minus 1,035.4 = 22.3, which matches the $22.3M quarterly reduction D06 reports. This confirms that D06's narrative and the balance sheets use the same basis.
6. **A possible trap.** D04 line 36 says "inventory days declining from 185 days on March 31 to 175 days on June 30." Inventory *days* fell that quarter, but the *dollar* balance rose by $11.9M. The cumulative reduction from the peak therefore shrank from $320.9M to $309.0M.

minimal_documents: D04 + D06. Both are needed: only D06 links the December 2024 peak to a dated balance, and only D04 has the June 30, 2026 balance. D05 only corroborates and cannot replace either one. Its balance sheet compares December 31, 2025 with March 31, 2025, so it has no December 2024 figure and no June 2026 figure. None of the other documents mention Microchip.

readings:
- **Stopping at D06's figure: $320.9M.** This is the stated reduction "now" as of March 31, 2026, the end of fiscal 2026. It doesn't fit the question, which asks about the close of Q1 fiscal 2027 (June 30, 2026).
- **Reading "reduction" as inventory days instead of dollars.** That would give a figure in days, not "millions of dollars," and the packet doesn't state peak days for December 2024. The question's units rule this out.
- **Treating the December 2024 peak as unknown.** It isn't. It can be derived exactly as $1,356.3M from D06, so the answer is fully determined: $309.0M.

gaps:
- No document prints the December 31, 2024 inventory balance directly. It is derived from D06's stated $320.9M reduction plus the March 31, 2026 balance, using basic arithmetic.
- All packet documents are text (no PDFs), so there was no page-image step. I checked the decisive figures against the original files in docs/: "320.9 … high point" (D06 source line 44) and the Inventories rows (D06 source line 234, D04 source line 208, D05 source line 210).
- D04, D05 and D06 were read in full. The other nine documents (D01–D03 Analog Devices, D07–D09 onsemi, D10–D12 Texas Instruments) were only searched for "microchip", "high point", "peak", "320.9" and "1,356". None mention Microchip; the only hits were "peak" inside "speak" in D07–D09.
- I did not read the Dnn.layout.txt files; the plain-text tables were clean.

contaminated: no. A file-listing glob showed that a question.txt file exists in the packet, but I never opened it. No answer, reasoning or source hint leaked.

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\solver-2\text\D06.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\solver-2\text\D04.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\solver-2\text\D05.txt (corroboration only)
