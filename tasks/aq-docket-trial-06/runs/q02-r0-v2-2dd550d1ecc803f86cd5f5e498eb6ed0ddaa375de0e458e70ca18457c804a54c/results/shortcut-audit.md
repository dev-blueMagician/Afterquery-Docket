# q02 rev 0 shortcut audit (2026-10-06)

Fresh shortcut-auditor agent (scope hook), input: workspace root, shortcut packet path, question
verbatim. Return copied verbatim.

answer: 9.8% (21 of 214). Idaho had 20 privately insured credit unions plus 1 with no insurance at all, out of 212 privately insured plus 2 uninsured nationwide. If you count only privately insured credit unions, the answer is 9.4% (20 of 212).

verdict: ambiguous

shortest_path:
1. Find the state. D05 (GAO-06-387), Appendix VI, Table 4 "Information on Funding for Selected State Bank Regulators". The Idaho row is lines 817–821 of `D:\Dev\Docket\tasks\aq-docket-trial-06\runs\q02-r0-v2-2dd550d1ecc803f86cd5f5e498eb6ed0ddaa375de0e458e70ca18457c804a54c\shortcut\text\D05.txt`. It says "The Idaho Department of Finance ... assessment structure includes a graduated base fee and excess fee based ... on total assets and $100 per branch office." The text columns are jumbled, but the row sits between the "Idaho" (817) and "Iowa" (823) headings, so the fee belongs to Idaho. No other document mentions a branch fee.
2. Get the counts. D02 (GAO-03-971), `...\shortcut\text\D02.txt`:
   - Line 233: "As of December 2002, 212 credit unions— about 2 percent of all credit unions— chose to purchase private deposit insurance."
   - Table 3, lines 461–469: "Total number of privately insured credit unions ... Idaho 20 ... Total 212."
   - Figure 1 (December 2002) and the Highlights page repeat the per-state numbers: 22, 93, 3, 5, 8, 20, 21, 40, which add up to 212.
   - Footnote 8, line 239: "we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire."
3. Calculate.
   - Literal reading (privately insured plus uninsured): (20+1)/(212+2) = 21/214 = 9.813%, which rounds to 9.8%.
   - Privately insured only: 20/212 = 9.434%, which rounds to 9.4%.

sufficient_documents: You need both D05 and D02. Neither can be replaced. Only D05 identifies the regulator with the $100 branch fee, and it contains no credit union content at all. Only D02 has the credit union counts, and it never mentions assessments or branch fees.

searches:
- Search terms: "$100"; "per branch", "each branch", "branch office"; branch near fee/assessment/charge; "Idaho Department of Finance"; "Idaho"; privately insured / private deposit insurance / without federal / uninsured; "212"; "9,688"; "New Hampshire"; "credit union".
- All six text files (D01–D06) were searched; I also read manifest.json.
- Close reading: D05 lines 780–870; D02 lines 1–320, 440–534, 591 and 1188–1219.
- "Idaho" appears only in D02 and D05. "Credit union" appears only in D02 and in D03, where it only names the National Credit Union Administration. D01, D04 and D06 contain nothing for either step.
- Shortcut attempts all failed:
  - No single document covers both the fee and the counts.
  - The question doesn't name the state.
  - No sentence states the answer directly. Idaho's "71" in Table 3 is a percentage of noncompliant websites, a distractor.
  - D02 alone lists 8 states and gives no way to pick one.
- The real route links two documents through the state name and then takes a simple ratio. That is an easiness risk, since Table 3 is a lookup with a total row, but it is not a shortcut.

readings/gaps:
- **Reading A, 9.4%.** This treats "without federal deposit insurance" as the report's privately insured group. Support:
  - Only the 212 figure is explicitly dated "As of December 2002," matching "end of 2002."
  - The report limits "depository institutions lacking federal deposit insurance" to credit unions that buy private insurance (line 157).
  - It also equates the two terms directly ("Depository institutions lacking federal deposit insurance— privately insured credit unions—", line 285).
- **Reading B, 9.8%.** This takes "all U.S. credit unions without federal deposit insurance" literally and adds footnote 8's two uninsured credit unions, one of which is in Idaho. Gap: footnote 8 gives no date. The uninsured credit unions were found in discussions with state regulators during 2003 fieldwork, so their status at end-2002 is inferred. I give B as the main answer because it is the literal reading and doesn't ignore evidence in the text. Still, the two readings round differently at one decimal place, which is why the verdict is ambiguous.
- Mixed calculations (20/214 = 9.3%, 21/212 = 9.9%) aren't defensible.
- Minor uncertainty: GAO left a second Maryland insurer, Credit Union Insurance Corporation, out of its analysis because it was dissolving. The text doesn't show any of its credit unions missing from the 212, and Idaho's count is unaffected.
- No text extraction problems affect the answer. D05's Table 4 has jumbled columns but is readable.
- Contamination: none. I read only manifest.json and the docs/text files. I did not open `question.txt` in the packet root, any notes, or other packets.
