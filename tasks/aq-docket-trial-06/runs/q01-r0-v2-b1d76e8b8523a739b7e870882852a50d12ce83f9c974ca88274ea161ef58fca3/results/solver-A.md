# q01 rev 0 blind solver A, 2026-10-08, fresh blind-solver, packet solver-1 (prepared), question verbatim
tested_sha256: b1d76e8b8523a739b7e870882852a50d12ce83f9c974ca88274ea161ef58fca3

answer: 40.5%
confidence: high
path:
1. Which states (D05, GAO-06-387, "OCC Preemption Rules", dated 04/28/2006). This report covers OCC's final rules of January 13, 2004 (line 173). The scope section (line 183, repeated in Appendix I at line 533) says GAO "conducted site visits or phone interviews with officials and representatives of state attorneys general offices, state banking departments, ... in six states (California, Georgia, New York, North Carolina, Idaho, and Iowa)." Appendix VI (line 797) confirms the bank regulators specifically: "Table 4 provides more detailed information on the funding arrangements for six state bank regulators that we interviewed." Table 4 lists California, Georgia, Idaho, Iowa, New York and North Carolina. The work ran "from August 2004 through March 2006", which is after the 2003 visits.
2. Privately insured credit unions at the end of 2002 (D02, GAO-03-971, August 2003). Line 233 says "As of December 2002, 212 credit unions ... chose to purchase private deposit insurance." Line 243 says these "are located in eight states". Table 3 (line 467) gives "Alabama 3 California 22 Idaho 20 Illinois 40 Indiana 21 Maryland 5 Nevada 8 Ohio 93 / Total 212". Figure 1 (line 245) shows the same counts and is titled "Number of Privately Insured Credit Unions (December 2002)". D02 never mentions Georgia, Iowa, New York or North Carolina, so each of those states had 0.
   - Total for the six states: CA 22 + ID 20 = 42.
3. Visits (D02). The visits happened in 2003 ("between February and August 2003", line 167) and only in "Alabama, California, Illinois, Indiana, and Ohio" (lines 157 and 407). That means Idaho had 0 visits. They covered "57 locations ... (49 main and 8 branch locations)" (line 407). Table 1 (line 423) row: "California 22 21 b 6 29", meaning 22 credit unions, 21 sites visited, footnote b. Prose at line 411 confirms "six of the 21 sites visited in California".
   - Footnote b (lines 429-431): "For one credit union, in addition to conducting a site visit at the main location, we conducted site visits at three branch locations. For another credit union, in addition to conducting a site visit at the main location, we conducted a site visit at a branch location."
   - Distinct California credit unions visited: 21 - 3 - 1 = 17.
   - Cross-check: Alabama has 5 sites (footnote a: 2 extra branch sites, so 3 main) and Illinois has 10 sites (footnote c: 2 branch-only sites, so 8 main). Branches total 2 + 4 + 2 = 8. Main locations total 3 + 17 + 8 + Indiana 5 + Ohio 16 = 49. Both match the "49 main and 8 branch" statement.
4. Calculation: 17 / 42 = 0.40476, which is 40.5%.

minimal_documents: D02 + D05. No alternatives in the packet. D03 (GAO-04-412T, predatory lending) mentions OCC preemption but does not list which states' regulators were interviewed about the 2004 rules. D01, D04 and D06 don't cover this topic: searches for "credit union", "preempt" and "Comptroller" found only one unrelated hit in D01 (Carmack Amendment) and none in D04 or D06.

readings:
- Counting sites visited instead of distinct credit unions (taking Appendix I's wording "site visits to 57 privately insured credit unions" literally): 21/42 = 50.0%. Footnote b rules this out because 4 of California's 21 sites were extra branches of 2 credit unions whose main offices were also visited.
- Limiting the base to states that were both interviewed and visited (California only): 17/22 = 77.3%, or 21/22 = 95.5% using sites. The question says "across the states" GAO interviewed, so Idaho's 20 belong in the base.

gaps:
- No PDFs or layout files; docs/ holds only .txt files; manifest method "text", pages null. Table 1 and footnotes read from extracted text; the prose and the 49/8 arithmetic confirm the footnote assignments.
- Table 1 doesn't state its date. Its California count (22) matches Table 3 and the December 2002 figure, and the totals reconcile to 212.
- Assumes every California credit union GAO visited in 2003 was already privately insured at the end of 2002. The report doesn't address this; it mentions a "recent conversion" of a large credit union without saying where or when.
- Fully read D02 lines 1-537 and 1180-1243, the relevant D05 sections (scope, Appendix I, Appendix VI including Table 4), and relevant parts of D03; the rest of D02, D05, and D01, D04, D06 by keyword search only.

contaminated: no
