# q04 rev 0 blind solver A (2026-10-06)

Fresh blind-solver agent (scope hook), input: workspace root, solver-1 packet path, question
verbatim. Return copied verbatim.

answer: 25.0%

confidence: high

path:
1. Finding the state (D05, GAO-06-387, Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators", text/D05.txt lines 817–821). It says: "The Idaho Department of Finance is funded by assessments of regulated financial institutions… The assessment structure includes a graduated base fee and excess fee based on total assets and $100 per branch office." I searched all documents for "$100", "per branch", "each branch" and "branch office". This is the only per-branch charge. California, Georgia, Iowa, New York and North Carolina in the same table have no such charge. So the state is Idaho.
2. The 2003 review is D02, GAO-03-971, dated "DATE: 08/20/2003" (line 17), on section 43 of the FDI Act.
3. The required notice (D02 line 455) reads: "we also reviewed 78 Web sites of privately insured credit unions… 39 of the 78 sites had not included language to notify consumers that the credit union was not federally insured… (see table 3)."
4. Table 3, "Number and Percent of Web Sites Reviewed without Required Disclosures" (D02 line 467; the docs/ source has the same text at line 465). The Idaho row is "Idaho 20 7 5 71". That means 20 privately insured credit unions, 7 Web sites identified and analyzed, 5 without the required disclosures, and 71 percent.
   - The column order checks out by arithmetic. The columns add up to the printed totals ("Total 212 78 39 50"): 3+22+20+40+21+5+8+93 = 212; 2+18+7+15+7+2+4+23 = 78; 0+3+5+8+4+2+3+14 = 39. Each row's percent also matches number ÷ sites (for example, 3/18 ≈ 17 and 5/7 ≈ 71). Exactly six states are over 50%, which matches the text's "six of the eight states".
5. Coverage of the Web site search (D02 lines 1213–1215): "We attempted to locate Web sites for all 212 privately insured credit unions; however, we were able to only identify 78 Web sites. We analyzed all Web sites identified." So the 20 Idaho credit unions were all candidates, and 7 had sites GAO could find.
6. Calculation: the question's denominator is all privately insured credit unions in Idaho. 5 ÷ 20 = 0.25, which is **25.0%**.
7. Two things I excluded. D02 footnote 8 (line 239) mentions "two uninsured credit unions, one was located in Idaho". That credit union has no insurance at all, so it is not one of the privately insured ones and isn't in the 20. Figure 1 (lines 245–273) is garbled in extraction, but its numbers {3, 5, 8, 20, 21, 22, 40, 93} match Table 3.

minimal_documents: D05 + D02. I found no alternatives. D05 is the only document with the $100-per-branch charge, and D02 is the only one with credit union Web site data. D03 mentions credit unions only as the regulator NCUA, in a predatory-lending context.

readings:
- Share of Idaho's analyzed Web sites, rather than of all its credit unions: 5 ÷ 7 = 71.43%, so **71.4%** (Table 3 prints it rounded as 71). The question's wording, "Of the privately insured credit unions in the state … what percentage had a Web site…", points to 20 as the denominator, so 25.0% is the main answer.
- If the 7 analyzed sites were the denominator but the printed whole-number figure were used, the answer would be 71.0%. That is weaker, because one decimal calls for computing from the counts.

gaps:
- The documents are text extractions only (method "text", no PDF or layout files), so I could not check Table 3 or Figure 1 against a printed page. The arithmetic checks above confirm the row reading.
- Unread coverage:
  - D02 and D05: I read the relevant sections, not the full text.
  - D01, D04 and D06: covered only by targeted searches ("$100", "branch", "credit union", "Web site", "Idaho"), not read.
  - D03: covered only by the "credit union" search.

contaminated: no

Relevant files:
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q04-r0-v2-ff615a1bd4cc8758d76076b05fa4f28089510d0572fff500a1c0107c8b8270a6\solver-1\text\D05.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q04-r0-v2-ff615a1bd4cc8758d76076b05fa4f28089510d0572fff500a1c0107c8b8270a6\solver-1\text\D02.txt
- D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q04-r0-v2-ff615a1bd4cc8758d76076b05fa4f28089510d0572fff500a1c0107c8b8270a6\solver-1\docs\gaoreports_gao_03_971.txt
