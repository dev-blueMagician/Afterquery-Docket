# q02 rev 0 blind solver B (2026-10-06)

Fresh blind-solver agent (scope hook), input: workspace root, solver-2 packet path, question
verbatim. Return copied verbatim.

**answer:** 9.8%

**confidence:** high

**path:**
1. **Which state.** D05 (GAO-06-387), Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators", in the Idaho row (text/D05.txt lines 817–821; docs/gaoreports_gao_06_387.txt line 819 says the same): "The Idaho Department of Finance is funded by assessments of regulated financial institutions… The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." The extraction mixes the table's columns together, but this text sits between the "Idaho" and "Iowa" headings. No other document mentions "branch office" or any per-branch charge, so the state is Idaho.
2. **Total without federal insurance at end of 2002.** D02 (GAO-03-971), Appendix I, p. 54 (line 1179): "As of December 2002, 214 state-chartered credit unions lacked federal deposit insurance, and all but two were privately insured." This total covers the whole country because federally chartered credit unions must be federally insured (line 231). Page 6 (line 233) agrees: "As of December 2002, 212 credit unions… chose to purchase private deposit insurance."
3. **Idaho's privately insured count.** D02 Table 3 (line 467): "Idaho 20 7 5 71", with "Total 212" (line 469). The eight state counts add up: 3+22+20+40+21+5+8+93 = 212. The Figure 1 map labels (December 2002) show the same numbers, including 20.
4. **The two uninsured credit unions.** D02 footnote 8 (line 239): "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire." These are the "all but two" from fact 2.
5. **Calculation.** Idaho had 20 + 1 = 21 credit unions without federal insurance, out of 214 nationwide. 21 / 214 = 0.098131, which is 9.8%.

**minimal_documents:** D02 + D05. No other document can replace either one: D05 is the only one with the $100 per-branch charge, and D02 is the only one with credit union counts.

**readings:**
- **Privately insured only (20 / 212):** 9.43%, so 9.4%. This follows the report's narrower working scope ("we limited our assessment of 'depository institutions lacking federal deposit insurance' to state-chartered credit unions that purchase private… insurance"). But the question says "all U.S. credit unions without federal deposit insurance," and the report itself counts 214 such credit unions in December 2002. So 9.8% is the better reading.
- **Mixed basis (20 / 214):** 9.3%. This is internally inconsistent because it uses the 214 total but leaves out Idaho's uninsured credit union.
- **Share of all U.S. credit unions (strained parse):** 21 / (9,688 federally insured + 214) = 21 / 9,902 = 0.21%, so 0.2%. This treats the question as asking what share of every U.S. credit union was both outside federal insurance and in Idaho, which is unlikely.

**gaps:**
- Table 3 has no date of its own. It matches the December 2002 total of 212 and the Figure 1 numbers, which are dated December 2002.
- Footnote 8 has no separate date, but Appendix I places both uninsured credit unions in the December 2002 count of 214.
- The D05 assessment details come from CSBS data for 2004–2005 and interviews from 2004–2006. That only matters for identifying the state, not for the 2002 counts.
- The text extraction loses which number belongs to which state on the D02 Figure 1 map. Table 3 provides that mapping. The docs/ folder has only .txt files, so there was no PDF to check.
- **What I did not read:** I read D02 lines 1–310, 440–540 and 1168–1219, and D05 lines 790–849. Elsewhere I only searched for terms (credit union, private/uninsured, branch, $100). I did not read D01 (household goods moving), D03 (predatory lending), D04 (assisted living) or D06 (bankruptcy and child support). Their titles and search results show nothing relevant: the only credit-union hits were three "Credit Union" mentions in D03, which is about predatory lending.

**contaminated:** no

Files used:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\solver-2\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\solver-2\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\solver-2\docs\gaoreports_gao_06_387.txt
