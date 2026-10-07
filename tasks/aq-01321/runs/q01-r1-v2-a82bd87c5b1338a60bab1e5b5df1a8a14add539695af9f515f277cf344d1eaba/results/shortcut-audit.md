# q01 rev 1 shortcut audit (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

tested_sha256: a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba
Prompt: workspace root, packet path shortcut, question verbatim. Return copied verbatim from the task notification.

---

answer: **$309.0 million.** By June 30, 2026, the close of Microchip's first quarter of fiscal 2027, inventory was $309.0 million below its December 2024 peak.

verdict: **clear.** No single document, wording cue or stated figure gives the whole answer. It takes one fact from each of two documents and a simple subtraction. The difficulty risk is that the route is easy to follow and the arithmetic is light.

shortest_path:
1. **D06** (FQ4 2026 release, filed 2026-05-07), text line 46; the same wording is at line 44 of the original docs/ file. The CFO says: "During the quarter, we reduced inventory by $22.3 million ... From the high point at the end of December 2024, we have now reduced the inventory by $320.9 million." That is the cumulative reduction as of March 31, 2026.
2. **D06** balance sheet, line 229: inventories were $1,035.4M at March 31, 2026. So the December 2024 peak was 1,035.4 + 320.9 = **$1,356.3M**.
3. **D04** (FQ1 2027 release, filed 2026-08-06). Line 20 says the quarter is the "three months ended June 30, 2026". Line 203 gives inventories of **$1,047.3M** at June 30, 2026, with $1,035.4M at March 31, 2026 as the comparative.
4. 1,356.3 − 1,047.3 = **309.0**. Equivalently, inventory rose 11.9 during the quarter (1,047.3 − 1,035.4), so 320.9 − 11.9 = 309.0.
5. Optional check from **D05** line 205: inventories were $1,057.7M at December 31, 2025. 1,057.7 − 1,035.4 = 22.3, which matches D06's "$22.3 million". The figures agree with each other.

sufficient_documents: **D04 + D06** is the minimal set.
- D06 alone stops at March 2026 and gives the outdated $320.9M.
- D04 alone has no peak or December 2024 reference. Its only inventory narrative is "continued inventory normalization" and inventory days falling from 185 to 175.
- D04's March 31 comparative can stand in for D06's balance sheet, but D06's "high point" sentence cannot be replaced.
- D05 only corroborates. No balance sheet in the packet shows the December 31, 2024 figure directly: D05 compares December 31, 2025 with March 31, 2025.

searches:
- **Terms searched:** "inventor", "peak", "high point", "December 2024", "calendar 2024", "from (the|its) peak", "320.9", "309"/"309.0", "1,356", "Microchip|MCHP". The same key values (320.9, high point, 1,047.3, 1,035.4, 1,057.7, "22.3 million") were also checked against the original docs/.
- **Read in full:** D04, D05, D06 and the manifest.
- **Searched but not read in full:** D01–D03 (ADI), D07–D09 (onsemi), D10–D12 (TI). None of them mentions Microchip. Their inventory lines are about their own companies, and no "309" hit relates to Microchip.
- **Synonym step:** searching "peak" does not find the passage, because D06 says "high point". Searching "inventory" finds it at once.
- **Not opened:** question.txt, notes and snapshots.

readings/gaps:
- **Most likely wrong answer:** $320.9M, taking D06's figure at face value. It is out of date because inventory rose $11.9M in the June 2026 quarter.
- **Sign error:** 320.9 + 11.9 = 332.8, assuming inventory kept falling.
- **Wrong baseline:** treating March 31, 2025 ($1,293.5M) as the peak gives 246.2, but that date is not the end of calendar 2024.
- **Weak alternative reading:** reading the question as "the most reduction achieved by then" would give 320.9. The phrase "by the close of" points to the June 30, 2026 position, so 309.0 is the only defensible answer.
- **Unverifiable premise:** the $1,356.3M peak is derived, not stated. The packet has no other 2024 quarter-end balances to confirm it was the maximum, so the "peak" rests on D06's wording and the question's premise.
- **Extraction:** no gaps found; the text matches the source at the checked lines.
- **Contamination:** none. No project instructions, memory, author reasoning or prior outputs were in my context. I could not check the invocation flags myself.

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\shortcut\text\D06.txt (lines 46, 229)
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\shortcut\text\D04.txt (lines 20, 203)
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\shortcut\text\D05.txt (line 205)
- D:\Dev\Docket\tasks\aq-01321\runs\q01-r1-v2-a82bd87c5b1338a60bab1e5b5df1a8a14add539695af9f515f277cf344d1eaba\shortcut\docs\microchip-technology-incorporated-fiscal-4q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-05-07.txt (line 44)
