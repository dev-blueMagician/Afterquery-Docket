# q01 rev 1 shortcut audit (fresh shortcut-auditor, packet shortcut), 2026-10-08
tested_sha256: 4dd1e15ab64ee0fcee654f2e9d820bf4aa602c4b6a46e04b7cad962181656fb4
Transcript audit: 17 tool calls (Glob, Grep, Read, handback), all inside the packet (clean).

answer: 22.40%. Assets for which State Street was the investment manager = total AUM minus the SPDR assets where it acts only as marketing agent: $6,121B at June 30, 2026 versus $5,001B at June 30, 2025.

verdict: clear. No disqualifying shortcut. The route is easy: two documents, one search on "marketing agent" and a ratio. Treat that as a difficulty risk.

shortest_path:
1. D10 line 58 "AUM ($ billions)(2) 6,278 5,620 5,117 12 23" (5,117 also in D06 lines 47, 128, 223 and as a comparative in D07-D09).
2. D10 footnote (2) line 189 "...for which we are not the investment manager but act as the marketing agent." The question's wording echoes this footnote.
3. D10 line 360 approximately $157 billion (June 30, 2026).
4. D06 line 394 approximately $116 billion (June 30, 2025).
5. 6,278 - 157 = 6,121; 5,117 - 116 = 5,001; 6,121 / 5,001 = 1.2239552 -> 22.3955% -> 22.40%.

sufficient_documents: D10 + D06, both required, no substitute. "116" in the SPDR context only in D06; "157" and "6,278" only in D10. Other footnotes: D02 $83B (9/30/24), D03 $82B (12/31/24), D05 $106B (3/31/25), D07 $145B (9/30/25), D08 $173B (12/31/25), D09 $184B (3/31/26). No document gives AUM excluding marketing-agent assets, a growth rate on that basis, or a prior-period comparative of the SPDR amount.

searches: "assets under management", "AUM", "investment manager", "marketing agent", "acts solely as", "SPDR", "gold", "116", "157", "5,117", "6,278", "5.1 trillion", "6.3 trillion", "AUM ($ billions)", "Total Assets Under Management", "Ending balance as of June 30" across D01-D10; D06 and D10 read in full; D04 no SPDR or marketing-agent matches; docs/ originals match on every input (5,117; 6,278; 263; $116B; $157B).

readings/gaps:
- Total-AUM reading 22.69% (D10 alone; highlight "AUM ... increased 23%"): rejected because the qualifier matches the documents' explicit "not the investment manager". "If the reviewer's gold uses total AUM, the question is a single-document shortcut (D10)."
- Whole Alternative Investments category: 22.96%; over-excludes ($263B / $225B larger than the quantified amounts). Weak.
- Adjusting only 2026: 19.62%; invalid (different bases).
- SPDR assets' own growth 35.34%; not asked.
- Rounding sensitivity: 22.3955% sits just above the 22.395 boundary; the deductions are "approximately" $116B and $157B, so the second decimal depends on those amounts as stated.
- D02, D03, D05, D07, D08, D09 searched, not read in full.
contamination: none.
