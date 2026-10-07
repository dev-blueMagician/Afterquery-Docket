# q03 rev 0 - shortcut auditor (packet shortcut)

- Date: 2026-10-05
- tested_sha256: 760ce0c02b4770adeb47a0140cbd01c64d34f1822e12f3e08cbb158d2f47c5f7
- Role: shortcut-auditor, fresh non-fork context; input = root, shortcut packet path, question text.
- Usage: 42,973 subagent tokens, 17 tool uses, 186 s.

## Raw return (verbatim)

answer: **$240 million.** FY2025 actual Adjusted EBITDA was $7,130M. The outlook in place before the Q1 report had a midpoint of $6,890M. 7,130 − 6,890 = $240M, about 3.5% above that midpoint.

verdict: clear

shortest_path:
1. **Pre-Q1 midpoint (D02, Q1 2025 release dated 2025-04-29).**
   - Updated outlook table (line 195): "Adjusted EBITDA(3) 6,885 to 6,955", so the midpoint is $6,920M.
   - Line 181: "the Company is raising the midpoints of its full year 2025 outlook for property revenue, Adjusted EBITDA, … by $50 million, $30 million, $20 million and $0.04, respectively." Line 177 says these changes are "relative to the Company's prior 2025 outlook".
   - So the outlook in place before the Q1 report had a midpoint of 6,920 − 30 = **$6,890M**.
2. **Actual FY2025 (D05, FY2025 release dated 2026-02-24).**
   - Line 43: "Adjusted EBITDA increased 4.7% to $7,130 million".
   - Line 799 reconciliation: "Adjusted EBITDA $1,818.5 $1,692.0 $7,130.0 $6,812.1" (Q4 2025, Q4 2024, FY2025, FY2024). The 4.7% growth checks out: 7,130.0 / 6,812.1 = 1.0467.
3. **Calculation:** 7,130.0 − 6,890 = **$240M**, and 240 / 6,890 = 3.48%.

Cross-checks:
- **The midpoint chain adds up.**
  - D03 (line 195, 2025-07-29): $7,005–$7,075M, midpoint $7,040M. This matches 6,920 + 120, the "$120 million" raise stated at line 181.
  - D04 (line 197, 2025-10-28): $7,058–$7,113M, midpoint $7,085.5M. That is about 7,040 + 45, the "$45 million" raise stated at line 183.
- **D02's own growth rate fits.** Its 1.6% midpoint growth (line 195) matches 6,920 / 6,812.1 = 1.0158.
- **FY2025 was not restated later.**
  - The 2026 outlook midpoint growth rates imply the same $7,130M base.
  - D06 (line 167): midpoint $7,230M at 1.4%; 7,230 / 7,130 = 1.0140.
  - D07 (line 171): midpoint $7,275M at 2.0%; 7,275 / 7,130 = 1.0203.
  - D05's own 2026 outlook (line 189): midpoint $7,125M at (0.1)%.

sufficient_documents:
- **Minimal set:** D02 + D05.
  - D02: `.../shortcut/text/D02.txt` (source docs/amt_ex991_2025-04-29.txt)
  - D05: `.../shortcut/text/D05.txt` (source docs/amt_ex991_2026-02-24.txt)
- **Alternative for the actual:** D06 or D07, but only approximately, by backing the FY2025 base out of a 2026 midpoint and its rounded growth rate. That route is less precise than D05.
- **No alternative for the pre-Q1 midpoint.** Only D02 gives it, through the $30M raise. The February 2025 outlook release is not in the packet, and no document states the prior range directly.
- **No single document works.** D02 has no actual result, and D05–D07 do not include the 2025 outlook.

searches:
- Terms searched in all text files: "outlook"; "adjusted ebitda"; "initial|original|prior outlook"; "midpoint"; "7,130"; "recast|restat"; "6,8xx|6,9xx|6,890"; "February 2x, 2025".
- What I inspected: D02 lines 141–349; D03 lines 170–209; D04 lines 172–211; D05 lines 1–120 plus grep hits at 189 and 799; D06 and D07 grep hits only; D01 header only (2021 CoreSite release, irrelevant).
- What the searches showed: no document gives a ready-made comparison between the actual and the initial outlook. D02's 6,862 and 6,977 hits are leverage figures (total debt and Q1 annualized Adjusted EBITDA), not prior-outlook numbers.

readings/gaps:
- **Wrong-anchor answers:** April 29 updated midpoint ($6,920M) gives $210M; July ($7,040M) gives $90M; October ($7,085.5M) gives $44.5M. None match "in place before".
- **Rounding:** D04's stated $45M raise is really 45.5 when computed from the ranges, so the stated raises may be rounded. D02's prior midpoint could therefore be off by about ±$0.5M. The supported answer is still $240M.
- **FX:** the $30M raise came entirely from currency movements. The question asks for a plain comparison, not a currency-neutral one.
- **Not fully read:** the rest of D05–D07 beyond the targeted sections; D05's long grep hits at lines 177, 353 and 383 (probably currency assumptions and definitions). Targeted greps found no conflicting figures.
- **Contamination:** none. Only the root, the packet path and the question were received; only the packet's text/ files and manifest were read.
