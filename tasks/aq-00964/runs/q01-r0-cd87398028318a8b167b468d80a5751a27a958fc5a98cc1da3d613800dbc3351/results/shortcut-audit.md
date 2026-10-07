# q01 rev 0 - shortcut auditor (packet shortcut)

- Date: 2026-10-05
- tested_sha256: cd87398028318a8b167b468d80a5751a27a958fc5a98cc1da3d613800dbc3351
- Role: shortcut-auditor, fresh non-fork context; input = root, shortcut packet path, question text.
- Usage: 47,012 subagent tokens, 24 tool uses, 201 s.

## Raw return (verbatim)

**answer:** About **$1,605 million**. That is the midpoint of the $1,595 million to $1,615 million range for full-year 2026 Africa & APAC property revenue, in the outlook issued April 28, 2026. That outlook was still in effect when the sale of ATC Philippines closed on June 15, 2026.

**verdict:** clear

**shortest_path:**
1. **When the sale closed and which segment it was in.** D07 (Q2 2026 release, July 28, 2026), `...\shortcut\text\D07.txt`:
   - Line 117: "On June 15, 2026, the Company completed the sale of its subsidiary in the Philippines ("ATC Philippines") for a total consideration of $75.6 million…"
   - Lines 531 and 567: the segment header reads "Africa & APAC(1)", and footnote (1) says "Includes results of Bangladesh and the Philippines through dates of sale." So the segment is Africa & APAC.
2. **Which outlook was current on June 15, 2026.** D06 (Q1 2026 release), `...\shortcut\text\D06.txt`:
   - Line 149: the outlook reflects "the Company's expectations as of April 28, 2026".
   - Line 173: "Africa & APAC property revenue of $1,595 million to $1,615 million", with a midpoint growth rate of 12.8%.
   - Line 151: its currency assumptions still include "(n) 58.20 Philippine Pesos", so this outlook still covered the Philippines.
   - The next outlook was issued July 28, after the sale. D07 line 41 calls that update a raise "for the second time this year", with April as the first. That points to no other change between April and July.
3. **Calculation:** (1,595 + 1,615) / 2 = **1,605**.
   - Cross-check: 1,605 / 1.128 ≈ 1,423 for the 2025 base. That matches D05 (1,545 / 1.086 ≈ 1,423) and D07 (1,630 / 1.146 ≈ 1,422).
   - The D06 range matches the original file (`docs\amt_ex991_2026-04-28.txt`, line 171).

**sufficient_documents:** D07 and D06 together. Neither works alone:
- D07 has the sale date and the segment, but only the July outlook, issued after the sale.
- D06 has the April outlook but never mentions the Philippines sale.

No other packet document can replace either one.

**searches:**
- Text searched: "Philippine", "ATC Philippines", "divest", "Bangladesh", "held for sale", "Kirtonkhola", "Africa & APAC property revenue", "Asia-Pacific", "prior outlook", and the numbers 1,595, 1,605 and 1,615.
- Read: the outlook sections of D05, D06 and D07; D07's divestitures paragraph and segment tables; D02's segment context.
- D01 is the November 2021 CoreSite acquisition announcement and is not relevant.
- Key figures were checked against the original files in `docs\`.
- Coverage: all 7 packet documents were searched; the relevant sections were read in full.

**readings/gaps:**
- **$1,630 million (rejected):** midpoint of D07's $1,620–1,640 million. This comes from the release that reported the sale, but that outlook was issued after June 15 and no longer lists the Philippine peso or Bangladeshi taka among its currencies. It was not the outlook in effect when the sale closed.
- **$1,545 million (rejected):** midpoint of D05's February 24, 2026 range of $1,535–1,555 million. The April 28 outlook replaced it.
- **Coincidental match:** "1,605.2" appears in D06 line 507 and D07 line 505 as cash at the beginning of the period. It is unrelated to the outlook.
- **Gaps:**
  - The packet has nothing dated between April 28 and July 28, 2026. An update in that window can't be fully ruled out, but D07's "second time this year" wording points against one.
  - Some segment-table text is cut off in extraction (for example D07 lines 535, 551 and 563). None of it affects the outlook figures.
- **No contamination:** question.txt and other off-limits files were not read.
