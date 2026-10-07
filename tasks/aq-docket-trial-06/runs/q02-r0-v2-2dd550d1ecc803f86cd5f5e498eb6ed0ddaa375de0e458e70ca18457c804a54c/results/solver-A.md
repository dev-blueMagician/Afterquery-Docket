# q02 rev 0 blind solver A (2026-10-06)

Fresh blind-solver agent (scope hook), input: workspace root, solver-1 packet path, question
verbatim. Return copied verbatim.

**answer:** 9.8%

**confidence:** high

**path:**
1. **Which state.** D05 (GAO-06-387, dated 04/28/2006), Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators", line 819–821, Idaho row: "The Idaho Department of Finance is funded by assessments of regulated financial institutions … The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." The text extraction interleaves the table's columns, but the Idaho wording is clear. I searched for "per branch", "branch office", "branch" and "$100" across all six documents. This is the only per-branch charge. The other "$100" hits in D05 (lines 669 and 767) are about asset totals and supervision cost. So the state is **Idaho**.
2. **Privately insured credit unions, end of 2002.** D02 (GAO-03-971, August 2003), line 233: "As of December 2002, 212 credit unions—about 2 percent of all credit unions—chose to purchase private deposit insurance."
3. **Idaho's privately insured count.** D02 Table 3, lines 467–469: "Idaho 20 7 5 71 … Total 212 78 39 50". The first column is "Total number of privately insured credit unions". The state values (3+22+20+40+21+5+8+93) add up to 212. They are also the same set of numbers shown in Figure 1, which is dated December 2002 (lines 63–73 and 245–273).
4. **Credit unions with no insurance at all.** D02 footnote 8, line 239: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire." The footnote sits between two "As of December 2002" statements on lines 231–233.
5. **Calculation.** All credit unions without federal deposit insurance = 212 privately insured + 2 uninsured = 214. Idaho = 20 + 1 = 21. 21 / 214 = 0.098131, which is **9.8%**.

**minimal_documents:** D02 + D05. No alternatives: D05 is the only document with the $100 per-branch charge, and D02 is the only one with credit-union insurance counts.

**readings:**
- **Privately insured only (the report's main measure):** 20 / 212 = 9.434%, so **9.4%**. I rank this below the main answer because the question says "all U.S. credit unions without federal deposit insurance", and in plain terms that includes the two with no insurance at all.
- **Mixed versions (less consistent):** 20/214 = 9.3%, or 21/212 = 9.9%.

**gaps:**
- Footnote 8 has no explicit date for the two uninsured credit unions. They were found "through our discussions with state regulators", and that fieldwork ran from February to August 2003. I assumed they existed at the end of 2002 because of where the footnote sits.
- The packet has no PDFs and no Dnn.layout.txt files (docs/ only holds .txt files). So I couldn't check Figure 1's map visually. Its text extraction scrambles which number goes with which state, but Table 3 settles Idaho's value.
- What I read: D02 lines 1–320, 440–540, 757 and 1185–1224; D05 lines 1–20 and 790–849. For the rest I relied on targeted searches across all six files (credit union, privately/uninsured, deposit/share insurance, Idaho, New Hampshire, branch, $100). I did not read D01, D03, D04 or D06 in full. Of those, only D03 mentions credit unions (3 hits, all about NCUA preemption, nothing relevant), and D01, D04 and D06 have no "credit union" hits.

**contaminated:** no. Following the instructions, I did not open question.txt.

Relevant files:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\solver-1\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\solver-1\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\solver-1\text\manifest.json
