# q02 rev 0 - blind solver B (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-2 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747

## Return

**answer:** $132 million (latest estimate midpoint of $450 million minus $318 million of pretax charges recorded through June 30, 2026)

**confidence:** high

**path:**
1. **Latest estimate (D11, May 1, 2026 release, text/D11.txt line 39):** "on April 30, 2026, the Company's Board of Directors approved an expansion of the SGPP … cumulative pretax charges related to the SGPP, once all projects are approved and implemented, are now estimated to be $350 million to $550 million, increased from $200 million to $300 million." The midpoint is (350 + 550) / 2 = **450**.
2. **No later revision:** D12 (July 31, 2026, Q2 results) only names the program in its forward-looking-statement and non-GAAP text. Searching text/ and docs/ for "cumulative", "pretax", "$350", "$550" and "now estimated" finds estimate wording only in D07 and D11.
3. **Same program under another name:** D07 (Aug 1, 2025, line 41) announced "a new three-year productivity program" with "cumulative pre-tax charges … totaling between $200 and $300 million." D08 (line 37) calls it "our previously announced Strategic Growth and Productivity Program". D11's "increased from $200 million to $300 million" ties the two together.
4. **2025 charges (D09, Q4/FY2025 release):** In the twelve-month reconciliation (line 865), the Income Before Income Taxes column shows "Restructuring programs(1) 13 2 11 — 11". Note (1) at line 903 says "The restructuring program charges relate to the Strategic Growth and Productivity Program in 2025". Line 495 gives SGPP charges of "$13" for the twelve months, and line 491 gives $13 for Q4 alone, so nothing was recorded in Q1–Q3 2025. Total: **13**.
5. **Q1 2026 (D11, line 548):** "Strategic Growth and Productivity Program 176 37 139 1 138". This is 171 of operating-profit charges (line 494) plus 5 of non-service related postretirement costs (line 508).
6. **First half 2026 (D12, Table 9 continued, line 800):** "Strategic Growth and Productivity Program 305 61 244 2 242" in the Income Before Income Taxes column. That is 300 of operating-profit charges (line 742: gross profit 2 + SG&amp;A 13 + other 285) plus 5 of non-service related postretirement costs (line 760). Cross-check: Q2 alone is 129 (line 656), and 176 + 129 = 305.
7. **Recorded through June 30, 2026:** 13 + 305 = **318**.
8. **Not yet recorded:** 450 − 318 = **132** (in millions of dollars).

**minimal_documents:** D09, D11, D12.
- D11 is the only source for the $350–$550 million estimate.
- D09 is the only source for the 2025 charges. D10's recast segment tables don't break out the program.
- D12's six-month figure already includes Q1, so a separate Q1 figure isn't needed. If D12 were missing, D11 (176) plus a Q2 figure would be needed, and only D12 has Q2.
- D07 and D08 only confirm that the program and its original name refer to the same thing. They aren't needed for the number.

**readings:**
- **Operating-profit charges only** (13 + 300 = 313, leaving out the 5 in non-service postretirement costs): 450 − 313 = **137**. This is weaker, because the estimate is stated as "pretax charges" and the pretax reconciliation column includes the 5.
- **2026 charges only** (ignoring the 2025 $13): 450 − 305 = **145**. This is unsupported, because the estimate is cumulative over the whole program.
- **Original $200–$300 million estimate:** the midpoint of 250 would already be exceeded by 68. The question asks for the latest estimate, so this doesn't apply.

**gaps:**
- I didn't fully read D01–D06 (the 2019 and 2024–April 2025 releases). They predate the program's August 2025 announcement, and searches of text/ and docs/ found no references to the program in them.
- I skimmed the income statements, balance sheets and cash-flow sections of D07–D12 only through searches.
- I checked docs/ against the text extraction for the decisive estimate wording, and both agree. No PDFs were involved: the manifest lists method "text".

**contaminated:** no
