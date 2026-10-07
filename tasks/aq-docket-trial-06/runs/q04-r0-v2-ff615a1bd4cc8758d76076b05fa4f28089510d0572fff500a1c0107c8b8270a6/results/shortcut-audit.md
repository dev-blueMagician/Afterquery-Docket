# q04 rev 0 shortcut audit (2026-10-06)

Fresh shortcut-auditor agent (scope hook), input: workspace root, shortcut packet path, question
verbatim. Return copied verbatim.

answer: **25.0%.** Idaho had 20 privately insured credit unions, and GAO found 5 of them had Web sites without the required notice: 5 / 20 = 25.0%.

verdict: **clear.** I found no single-document lookup and no stated answer. Two documents are needed: one names the state, the other gives its counts. The route is easy, though, so there is a difficulty risk (see readings/gaps). No project instructions, memory, key, author reasoning or prior outputs reached my context. I did not open `question.txt` in the packet root.

shortest_path:
1. **Find the state.** D05 (GAO-06-387, April 2006), Table 4 "Information on Funding for Selected State Bank Regulators", text/D05.txt lines 817–821: "The Idaho Department of Finance is funded by assessments … The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." The other five states in the table (California, Georgia, Iowa, New York, North Carolina) have no per-branch charge. The state is Idaho.
2. **Find Idaho's figures.** D02 (GAO-03-971, dated 08/20/2003), Table 3 "Number and Percent of Web Sites Reviewed without Required Disclosures", text/D02.txt line 467: "Idaho 20 7 5 71". The columns are: total privately insured credit unions (20), Web sites identified and analyzed (7), Web sites without required disclosures (5), and that number as a percent of sites analyzed (71).
3. **Confirm the disclosure is the right one.** Line 455 says "39 of the 78 sites had not included language to notify consumers that the credit union was not federally insured." That matches the table's total of 39.
4. **Check the table was read correctly.** The columns add up to 212 / 78 / 39 as printed. Each row's percent matches (3/18 is about 17, 5/7 about 71, 14/23 about 61). Figure 1 (lines 243–269) also shows 20 for Idaho as of December 2002. The same row appears in the original source file, docs/gaoreports_gao_03_971.txt line 465.
5. **Calculate.** The question's base is all of the state's privately insured credit unions, so 5 / 20 = 25.0%.

sufficient_documents: D05 and D02 are both needed, and no alternative set works.
- D02 lists eight states and never mentions any per-branch fee.
- D05 never covers private deposit insurance or Web-site disclosures.
- D01 (household goods moving), D03 (predatory lending), D04 (assisted living) and D06 (bankruptcy and child support) are unrelated.

searches:
- **Terms:** `$100`, "per branch", "branch office", "branch" (every hit in D02 and D05 checked, including the long lines D05:359, D05:669, D02:551), `Idaho`, "Web site", "credit union", "deposit insurance", "federally insured", "section 43", "assessment", "Department of Finance".
- **Answer-shaped terms:** "25 percent", "25.0", "one-fourth", "one quarter", "5 of 20", "five of twenty". The only hits were GAO's bulk-order discount boilerplate, D04's assisted-living figure and D02's note about ASI monitoring 25 percent of its assets. None is the answer.
- **Sources read:** the manifest and all six document headers. In D02, the Background section, Figure 1, Tables 1–3, the monitoring text and the scope and methodology section. In D05, Table 4 in full.

readings/gaps:
- **Alternative reading, 71.4%.** This is 5 of the 7 Idaho Web sites analyzed; Table 3 prints it as 71. It is the likely trap. The question says "Of the privately insured credit unions in the state", which makes the base 20, so I reject it.
- **Uninsured credit union.** Footnote 8 mentions one credit union in Idaho with no insurance at all. It is not privately insured, so it is excluded.
- **Difficulty risk.** The phrase "$100 … per branch office" matches D05 almost word for word. One search finds Idaho, a second finds Idaho's row in D02, and the arithmetic is trivial. That is an allowed lookup-and-divide route, not a shortcut.
- **Gaps.** I did not read every document end to end; coverage comes from the targeted searches above. Figure 1's layout is garbled in the text, but its numbers match Table 3. All files were plain text, so there were no extraction gaps.
