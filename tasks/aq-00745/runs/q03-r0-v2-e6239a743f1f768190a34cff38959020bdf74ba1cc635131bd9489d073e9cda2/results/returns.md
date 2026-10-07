# q03 rev 0 - raw independent returns

tested_sha256: e6239a743f1f768190a34cff38959020bdf74ba1cc635131bd9489d073e9cda2
Date: 2026-10-05. Runtime: Claude Code (VS Code), fresh Agent-tool subagents (Opus 5.5), each given
only the workspace root, its own packet path and the frozen question (closed-book: question only).
Returns below are the agents' final reports as delivered, unedited.

## Solver B (blind-solver, packet solver-2)

I checked this against every relevant figure in the packet, and the result is a decrease of $318 million. No document prints a second-half-2025 figure under the 2026 structure, so I built it from the three businesses that were combined.

answer: **−$318 million.** Sales fell from $1,885 million in 2H25 (recombined) to $1,567 million in 1H26, a drop of about 16.9%.

confidence: high

path:
1. **What the business is.** D10, Diagnostics footnote (line 183, also in D08 line 127): "*Beginning in 2026, Abbott aggregated its previously reported Rapid Diagnostics, Molecular Diagnostics, and Point of Care businesses into the Rapid and Molecular Diagnostics business." Exact Sciences is reported separately as Cancer Diagnostics, so it is not included here.
2. **1H26 sales.** D10, "Sales 1H26 ($ in millions)", column "Rapid/Molecular Diagnostics": "Total reported 5,272 2,690 1,015 1,567". Two checks:
   - U.S. 858 + International 709 = 1,567.
   - 1Q26 of 812 (D08: "Total reported 2,180 1,272 96 812") plus 2Q26 of 755 (D10: "Total reported 3,092 1,418 919 755") = 1,567.
3. **3Q25 sales (old columns: Core Lab, Molecular, Point of Care, Rapid Diagnostics).** D04: "Total reported 2,253 1,364 131 158 600". So 131 + 158 + 600 = **889**. The row adds up to its total (1,364 + 889 = 2,253).
4. **4Q25 sales.** D07: "Total reported 2,457 1,461 141 158 697". So 141 + 158 + 697 = **996**. The row adds up to its total (1,461 + 996 = 2,457).
5. **2H25 total.** 889 + 996 = **1,885**. A second route gives the same number:
   - Full-year 2025 (D07, "Total reported 8,937 5,360 517 606 2,454"): 517 + 606 + 2,454 = 3,577.
   - 1H25 (D03, "Total reported 4,227 2,535 245 290 1,157"): 245 + 290 + 1,157 = 1,692.
   - 3,577 − 1,692 = 1,885. The nine-month figures also agree (D04: 376 + 448 + 1,757 = 2,581, which is 1H25 + 3Q25).
6. **Checking that the regrouping is a simple sum.** D10 reports 1H26 Rapid/Molecular as "(7.4)" percent versus 1H25. Using my 1H25 sum: 1,567 / 1,692 − 1 = −7.39%, which matches. For 1Q26: 812 / (122 + 142 + 613 = 877) − 1 = −7.4%, matching D08's "(7.4)". D10's 1H25 total for all Diagnostics of 4,227 also equals 2,535 + 1,692. So nothing else was moved into or out of this business.
7. **Change.** 1,567 − 1,885 = **−318**.
   - By region: U.S. was 858 − (520 + 591 = 1,111) = −253; International was 709 − (369 + 405 = 774) = −65. Together that is −318.

minimal_documents: D10 + D04 + D07. Alternatively, D10 + D07 + D03, using the full year minus the first half. D08 can replace the 1H26 total by adding 1Q26 to D10's 2Q26, but D10 alone is enough for that number. D10 + D07 by themselves only allow an estimate, because D10 gives 1H25 for this business only as a percentage.

readings:
- **Main reading (reported sales, total company, July–December 2025 vs. January–June 2026):** −318.
- **Leaving out Point of Care**, which contradicts the 2026 definition: 2H25 would be 1,569, and comparing it with 1H26's 1,567 would mix two different groupings. Not defensible.
- **Comparable or currency-adjusted sales:** the packet gives no second-half-2025 base for these, and the question asks for reported sales anyway.
- **Year over year (1H26 vs. 1H25):** 1,567 − 1,692 = −125. This is not the period the question asks about, but it is a likely place to go wrong.

gaps:
- No document gives a 2H25 figure for this business directly in the 2026 structure, so it is derived from the published quarterly figures for its three former parts.
- All documents are text-based (pages: null) with no layout files or PDFs, so there were no PDF pages to inspect.
- Coverage:
  - Read in full: D09 (litigation settlement notice), D10 and D11 (litigation release).
  - Read the diagnostics sections only: D03, D04, D07 and D08.
  - Read the opening sections only: D05 (Exact Sciences deal announcement) and D06 (By-laws).
  - Seen only through searches for Rapid, Molecular, Point of Care, aggregat, recast, second half and 2H25 across all text files: D01 and D02 (2024 and 1Q25 data, not needed).
  - I confirmed the key rows against the files in docs/.

contaminated: no. I did not open question.txt, notes or any outside sources.

Files used: solver-2\text\D10.txt, D04.txt, D07.txt, D03.txt, D08.txt (under the run folder).

## Solver A (blind-solver, packet solver-1)

**answer:** -$318 million. Sales fell from $1,885 million in 2H25 to $1,567 million in 1H26, a drop of about 16.9%.

**confidence:** high

**path:**
1. **What the 2026 business includes** (D10, Diagnostics footnote at line 183; the same wording is in D08 line 127): "Beginning in 2026, Abbott aggregated its previously reported Rapid Diagnostics, Molecular Diagnostics, and Point of Care businesses into the Rapid and Molecular Diagnostics business." Cancer Diagnostics (Exact Sciences) is a separate business, so it is left out.
2. **1H26** (D10 line 171, "Sales 1H26 ($ in millions) … Rapid/Molecular Diagnostics"): "Total reported 5,272 2,690 1,015 1,567". So Rapid/Molecular = **1,567**.
   - U.S. 858 + International 709 = 1,567.
   - Total 5,272 − Core Lab 2,690 − Cancer Dx 1,015 = 1,567.
   - Quarters agree: 1Q26 812 (D08 line 109, "Total reported 2,180 1,272 96 812") + 2Q26 755 (D10 line 143) = 1,567.
3. **3Q25, old structure** (D04 line 157, columns Total / Core Lab / Molecular / Point of Care / Rapid Diagnostics): "Total reported 2,253 1,364 131 158 600". Molecular 131 + Point of Care 158 + Rapid 600 = **889**.
4. **4Q25** (D07 line 153, same columns): "Total reported 2,457 1,461 141 158 697". 141 + 158 + 697 = **996**.
5. **2H25** = 889 + 996 = **1,885**. Three other routes give the same total:
   - Full year minus first half: 12M25 (D07 line 179, "8,937 5,360 517 606 2,454") gives 517 + 606 + 2,454 = 3,577. 1H25 (D03 line 187, "4,227 2,535 245 290 1,157") gives 245 + 290 + 1,157 = 1,692. 3,577 − 1,692 = 1,885.
   - Total Diagnostics minus Core Lab: (2,253 + 2,457) − (1,364 + 1,461) = 4,710 − 2,825 = 1,885.
   - 12M25 minus 9M25 (D04 line 183, "6,480 3,899 376 448 1,757") gives 4Q25 components 141 / 158 / 697, matching step 4.
6. **The new structure is just the sum of the three old businesses.** D10 shows 1H26 Rapid/Molecular down "(7.4)" percent versus 1H25: 1,567 / 1,692 − 1 = −7.39%. D08 shows 1Q26 down "(7.4)": 812 / (1,692 − 815 = 877) − 1 = −7.41%. D10's reconciliation (line 615) still shows 1H25 Total Diagnostics at "4,227", the same as in D03, so 2025 Diagnostics was not otherwise restated.
7. **Change:** 1,567 − 1,885 = **−318**.

I spot-checked the decisive Total rows in the original docs/ files: 2,253 (abt_ex991_2025-10-15.txt:155), 2,457 and 8,937 (abt_ex991_2026-01-22.txt:151 and :177), and 5,272 / 2,690 (abt_ex991_2026-07-16.txt:169). All match the text extracts.

**minimal_documents:** D10 + D07 + D04 (3Q25 + 4Q25). An equally sufficient alternative is D10 + D07 + D03 (12M25 − 1H25). D08 can stand in for part of D10's 1H26 figure (1Q26 812), but D10 alone already gives the 1H26 total, so D08 adds nothing. Two documents are not enough for an exact answer: D10's −7.4% only pins 1H25 to roughly 1,691–1,693.

**readings:**
- If "Rapid Diagnostics" alone were used for 2H25 (600 + 697 = 1,297), the answer would be +270. That ignores the 2026 aggregation the question tells us to use, so I reject it.
- Comparable or FX-adjusted figures do not apply, because the question asks for reported sales.
- Calendar halves are the right windows, since Abbott's quarters follow the calendar year.
- I found no other defensible reading.

**gaps:**
- The packet has no 2025 Rapid and Molecular figures restated under the new structure, so 2H25 is built from the old component columns. The footnote and the matching growth rates support doing this.
- The text extracts contain "[... N characters not shown on the page ...]" markers. They hide only some percent-change rows, not any sales row I used.
- Coverage:
  - Read in full or in the relevant sections: D03, D04, D07, D08, D10, D11.
  - Seen only through search hits or headers: D05 (Exact Sciences deal release), D06 (bylaws), D09 (derivative-suit settlement notice, first 40 lines).
  - Not read: D01 and D02 (4Q24 and 1Q25 releases, outside the time window). They appeared only in search hits.

**contaminated:** no

Relevant files: solver-1\text\D10.txt, D07.txt, D04.txt, D03.txt, D08.txt (under the run folder).

## Closed-book (closed-book-solver, question text only)

answer: unknown
confidence: low
basis: I don't remember Abbott's 2026 sales figures for Rapid and Molecular Diagnostics under the new structure. The answer needs Q3 and Q4 2025 sales restated under that structure, plus Q1 and Q2 2026 sales, all from Abbott's 2026 earnings releases or filings. Abbott published Q2 2026 results in July 2026, which is past what I reliably know, and I don't recall the exact quarterly numbers before that either. Any number I gave would be invented, not remembered. No tools were called.
contaminated: no

## Shortcut audit (shortcut-auditor, packet shortcut)

answer: −$318 million. Rapid and Molecular Diagnostics reported sales fell from $1,885M in 2H25 to $1,567M in 1H26.

verdict: clear

shortest_path:
1. 1H26 figure. D10 (docs/abt_ex991_2026-07-16.txt, 2Q26 release), Diagnostics "Sales 1H26" table, Rapid/Molecular Diagnostics column: "U.S. … 858", "International … 709", "Total reported 5,272 2,690 1,015 1,567". So 1H26 = **1,567**. It ties to D08 1Q26 (812) plus D10 2Q26 (755).
2. Business definition. The footnote in D08 and D10 says: "Beginning in 2026, Abbott aggregated its previously reported Rapid Diagnostics, Molecular Diagnostics, and Point of Care businesses into the Rapid and Molecular Diagnostics business."
3. 3Q25 figure. D04 (abt_ex991_2025-10-15), "Total reported 2,253 1,364 131 158 600": Molecular 131 + Point of Care 158 + Rapid 600 = **889**.
4. 4Q25 figure. D07 (abt_ex991_2026-01-22), "Total reported 2,457 1,461 141 158 697": 141 + 158 + 697 = **996**.
5. 2H25 = 889 + 996 = **1,885**.
   - Cross-check: D07 full-year 2025 (517 + 606 + 2,454 = 3,577) minus D03 1H25 (245 + 290 + 1,157 = 1,692) = 1,885.
   - The 1H25 base of 1,692 matches D10's reported 1H26 change of "(7.4)": 1,567 / 1,692 − 1 = −7.39%.
   - Core Laboratory also ties (2,690 / 2,535 = +6.1%), so only the three businesses were combined.
6. Change = 1,567 − 1,885 = **−318**.
7. All rows used were checked against their row and column totals:
   - D04: 36 + 111 + 373 = 520 U.S. and 95 + 47 + 227 = 369 international.
   - D07: 39 + 107 + 445 = 591 U.S. and 102 + 51 + 252 = 405 international.
   - D10: 858 + 709 = 1,567.

sufficient_documents:
- Minimal exact set: {D10, D07, D04}, or {D10, D07, D03}.
- D08 + D10 can replace D10 alone for 1H26 (812 + 755).
- D07 is required, because it is the only source of 4Q25 / full-year 2025 data. D10 is required, because it is the only source of 2Q26 / 1H26 data.
- No single document holds both 2H25 and 1H26 figures under the 2026 structure, and no recast 2025 table exists in the packet.

searches:
- Terms searched: "Rapid and Molecular", "Rapid/Molecular", "Molecular Diagnostics", "Rapid Diagnostics", "Point of Care", "second half", "2H25", "sequential", "recast", "reclassif", "aggregat", "restat".
- Each period's sales-table header (1Q25, 2Q25, 1H25) was also searched directly.
- Read in full: the manifest, D08, D09, D10, D11.
- Read in part: the Diagnostics sections of D02, D03, D04 and D07, plus the opening of D05.
- What the remaining documents are:
  - D09 is a derivative-settlement notice and D11 is an NEC litigation release. Neither has sales data.
  - D05 announces the Exact Sciences deal and D06 is the amended bylaws. Keyword searches found no segment sales in either.
  - D01 covers 4Q24, which is outside the period asked about.
- I did not open question.txt, notes, or anything outside this packet.

readings/gaps:
- **Two-document route (a difficulty risk, not a shortcut).** D10's −7.4% implies 1H25 ≈ 1,567 / 0.926 ≈ 1,692. With D07's 3,577, that gives 2H25 ≈ 1,885 and a change of about −318. The rounding in the percentage leaves roughly −317 to −319, so this route is approximate. It still needs two documents.
- **Rounding.** Adding rounded components can be off by about 1 from the unrounded totals. For example, 755 / 815 = −7.36%, while D10 prints "(7.3)" for 2Q26. Using the published figures, the answer is −318.
- **Wrong readings to rule out:**
  - Using 1H25 instead of 2H25: −125.
  - Using only the old Rapid Diagnostics line for 2H25 (1,297): +270.
  - Leaving out Point of Care (2H25 of 1,569): −2.
  - None of these fits the question's wording.
- **Extraction gaps.** Some "[… characters not shown …]" placeholders fall inside percent-change rows. None of the sales-value rows I used is affected.
