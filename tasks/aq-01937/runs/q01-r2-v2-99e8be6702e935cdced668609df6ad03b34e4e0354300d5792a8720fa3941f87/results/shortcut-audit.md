# q01 rev 2 shortcut audit (fresh shortcut-auditor, packet shortcut), 2026-10-08
tested_sha256: 99e8be6702e935cdced668609df6ad03b34e4e0354300d5792a8720fa3941f87
Transcript audit (audit_transcript2.py): 20 tool calls (Glob, Grep, Read, handback), all inside the packet (clean); it did not read the harness overflow file of an oversized grep and re-ran narrower searches.

answer: 22.40%. Assets State Street actually managed went from $5,001B at June 30, 2025 to $6,121B at June 30, 2026: 1,120 / 5,001 = 22.3955% -> 22.40%.

verdict: clear (the route is easy, so difficulty is a risk; it is not a shortcut)

shortest_path:
1. D10 line 58 "AUM ($ billions)(2) 6,278 5,620 5,117 12 23" (2Q26 = 6,278; 2Q25 comparative = 5,117).
2. D10 line 189 note: "... for which we are not the investment manager but act as the marketing agent." The question's wording echoes this exclusion.
3. D10 line 360: approximately $157 billion at June 30, 2026.
4. D06 line 394: approximately $116 billion at June 30, 2025; D06 lines 47, 128, 223, 241 confirm 5,117.
5. 6,121 and 5,001; 1,120 / 5,001 = 0.2239552 -> 22.40%. Footnotes checked against docs/ (stt_ex991_2025-07-15.txt line 415; stt_ex991_2026-07-16.txt lines 59 and 371).

sufficient_documents: D10 + D06, both needed, no alternatives ($116B only in D06; $157B and 6,278 only in D10; 5,117 identical in D06-D10; no document gives investment-manager-only AUM: no hits for 5,001 or 6,121).

searches: "assets under management|AUM", "marketing agent", "investment manager", "June 30, 2025", "5,117|5,001|6,121", "116 billion|157 billion|116|157|SPDR(R) products". Every release D02-D10 carries the footnote for its own date: $83B, $82B, $106B, $116B, $145B, $173B, $184B, $157B. Other "116"/"157" hits unrelated. D10 read in full; D06 lines 1-250, 386-397; D01 and D04 predate the periods; D02, D03, D05, D07-D09 by search.

readings/gaps:
- Headline-AUM reading 22.69% (ignores "not the investment manager"); the likely trap; if the gold used it, D10 alone would answer (with the rounded "increased 23%").
- Whole Alternative Investments 22.96%: weaker.
- Rounding sensitivity: 22.39552% is 0.0005 points above the 22.395 boundary; truncation 22.39; correct rounding 22.40. Both carve-outs "approximately".
- Difficulty risk: searching "investment manager" or "marketing agent" leads straight to both footnotes; then a date join across two documents, two subtractions and a percentage change.
- Contamination: none.
