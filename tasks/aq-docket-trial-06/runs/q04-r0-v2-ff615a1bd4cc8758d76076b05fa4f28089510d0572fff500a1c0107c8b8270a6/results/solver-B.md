# q04 rev 0 blind solver B (2026-10-06)

Fresh blind-solver agent (scope hook), input: workspace root, solver-2 packet path, question
verbatim. Return copied verbatim.

**answer:** 25.0%

**confidence:** high

**path:**
1. **Which state.** D05 (GAO-06-387), Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators", Idaho row (text/D05.txt lines 817–821). It says: "The Idaho Department of Finance is funded by assessments of regulated financial institutions… The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." The table lists six states: California, Georgia, Idaho, Iowa, New York and North Carolina. Only Idaho has a per-branch charge, and a search of all six documents for "per branch" or "branch office" found only this line. So the state is **Idaho**.
2. **The 2003 Web site review.** D02 (GAO-03-971, fieldwork "between February and August 2003"), text/D02.txt line 455. It says: "we also reviewed 78 Web sites of privately insured credit unions… 39 of the 78 sites had not included language to notify consumers that the credit union was not federally insured… (see table 3)." Table 3's total of 39 sites matches that count, so its "Web sites without required disclosures" column is the missing "not federally insured" notice.
3. **Idaho's numbers.** D02 Table 3, "Number and Percent of Web Sites Reviewed without Required Disclosures" (text/D02.txt line 467; the same row is in the raw file docs/gaoreports_gao_03_971.txt line 465). The row reads "Idaho 20 7 5 71". The columns are:
   - total privately insured credit unions: 20
   - Web sites identified and analyzed: 7
   - Web sites without required disclosures: 5
   - percent: 71
4. **Cross-checks.**
   - The Table 3 totals ("Total 212 78 39 50") match the column sums. Credit unions: 3+22+20+40+21+5+8+93 = 212. Sites analyzed: 2+18+7+15+7+2+4+23 = 78. Sites lacking the notice: 0+3+5+8+4+2+3+14 = 39.
   - The 212 matches the text: "As of December 2002, 212 credit unions… chose to purchase private deposit insurance."
   - Figure 1's data labels (3, 5, 8, 20, 21, 40, 22, 93) include Idaho's 20.
   - The methodology (lines 1213–1215) explains the gap between 20 and 7: "We attempted to locate Web sites for all 212 privately insured credit unions; however, we were able to only identify 78 Web sites."
5. **Calculation.** The question's base is "the privately insured credit unions in the state", which is all 20 Idaho credit unions. Five of them had a Web site GAO found lacking the notice: 5 / 20 = 0.25, or **25.0%**.

**minimal_documents:** D05 and D02. Neither can be replaced:
- Only D05 contains the $100-per-branch-office fact or any state bank regulator funding detail.
- Only D02 contains the privately insured credit union and Web site data. Searches for "privately insured", "private deposit insurance" and "not federally insured" matched only D02. "Credit union" also appears in D03, but only as passing mentions of NCUA in a predatory-lending context.
- D01, D04 and D06 contain no relevant matches.

**readings:**
- **Share of reviewed Web sites (the alternative):** if the base is the Idaho Web sites GAO found and analyzed rather than all Idaho credit unions, the answer is 5 / 7 = 71.428…%, or **71.4%**. The table prints this as a rounded 71. The question's wording ("Of the privately insured credit unions in the state…") points to the 25.0% reading.
- 25.0% only counts what GAO found. The 13 Idaho credit unions whose Web sites GAO did not identify were not assessed, so the true share with a non-compliant site could be higher.

**gaps:**
- No original PDF is in the packet (the manifest lists method "text" and pages null), so I could not check a page image. The Table 3 row was confirmed in both the extracted text and the raw docs source, and its totals reconcile.
- D05's state data is CSBS 2004–2005 information, published in 2006, while D02's counts are as of December 2002. The question links the two only through the state's identity, so the date difference does not affect the answer.
- Coverage: I read the relevant sections of D02 (summary, background and Figure 1, Tables 1–3, Appendix I methodology) and D05 (Appendix VI, Table 4). I covered D01, D03, D04 and D06, and the rest of D02 and D05, only by targeted regex searches ("$100", "branch", "Idaho", "privately insured", "credit union", "section 43", "Web site", "state bank regulator"). I did not read them in full.

**contaminated:** no
