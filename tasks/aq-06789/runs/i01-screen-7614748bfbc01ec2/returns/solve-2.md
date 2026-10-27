# i01 blind solve 2 (fresh blind-solver, 2026-10-18) - judged RIGHT

Raw return, verbatim:

answer: 3.7 (billion dollars; "over $15.7 billion" for Katrina minus "about $12 billion" paid since inception as of April 2005)

confidence: high

path:
1. April 2005 cumulative figure: D02 (GAO-05-532T, testimony "Thursday, April 14, 2005", cover "April 2005"), text/D02.txt line 96: "Since its inception, the program has paid about $12 billion in insurance claims, primarily from policyholder premiums..." Raw source docs/gaoreports_gao_05_532t.txt line 94 says the same.
2. Katrina figure: D09 (GAO-08-28, dated 12/28/2007), text/D09.txt line 185: "FEMA estimated that NFIP had paid over $15.7 billion in flood insurance claims from Hurricane Katrina as of August 31, 2007, encompassing approximately 99 percent of all flood claims received." Footnote 21, line 311, same number: "FEMA estimates that Hurricane Katrina alone accounts for over $15.7 billion in flood insurance claims." Raw source docs/gaoreports_gao_08_28.txt lines 183 and 309 match.
3. Calculation: 15.7 − 12.0 = 3.7 billion dollars. "By how many billion dollars" asks for a difference, not a ratio.
4. Excluded:
   - D09 line 304: "For both Hurricanes Katrina and Rita, FEMA estimates that NFIP has paid approximately $16.2 billion": two storms, outside the scope.
   - D09 line 185: "$22.4 billion in claims tied to Hurricane Katrina (excluding flood)": private property-casualty payments, not NFIP.
   - D02 line 99: Isabel claims "$454.2 million".
   - D02 line 101: 2004 hurricanes "more than $1.3 billion in payments as of March 2005": part of the cumulative total, not a separate figure to add.

minimal_documents: D02 + D09. Both needed, neither replaceable: the only NFIP documents in the packet (67 and 79 NFIP/flood-insurance hits; every other document zero). Katrina is mentioned only in D09 (with dollar figures) and D05 (three non-numeric mentions about insurer preparedness and NAIC actions). D04's single "Rita" hit is a phone outage at an OCC office.

readings:
- Katrina+Rita: 16.2 − 12 = 4.2. Rejected: the question says Katrina, and D09 separates "Katrina alone" as $15.7B.
- "Add the 2004 hurricanes": treating the $1.3B (2004 storms, as of March 2005) as missing from the $12B gives 12 + 1.3 = 13.3 and 15.7 − 13.3 = 2.4. Weak: an April 2005 statement that the program has paid about $12B "since its inception" already covers payments to that date.
- Precision caveat: Katrina is a lower bound ("over $15.7 billion"), the cumulative figure approximate ("about $12 billion"); the printed figures give exactly 3.7; the true gap is "at least about 3.7".

gaps:
- D02 Appendix I, Figure 1 ("Total NFIP Payments to Claimants, 1972-2004", "Data compiled and available as of February 28, 2005") extracted with axis labels only, no bar values; same in docs/. Manifest method "text", pages null: no PDF page to check. The cumulative total rests on the prose "$12 billion" alone, which is the direct statement anyway.
- Katrina figure is as of August 31, 2007, covering about 99% of claims, so not a final total.
- Unread: D02 and D09 read in full. D01, D03–D08 not read in full; titles checked (toy guns, alternative mortgages, OCC consumer assistance, insurance-sector terrorism preparedness, bankruptcy credit counseling, long-term care insurance, fair lending) and searched for Katrina/Katr/Rita/Wilma/2005 hurricane, NFIP/flood insurance, "since inception"/"history"/"cumulative", dollar-billion amounts. None had relevant NFIP figures.
- No Dnn.layout.txt files in text/; none needed.

contaminated: no. A Glob of the packet root listed question.txt; not opened; nothing outside text/ and docs/ read.

Files used:
- D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i01-screen-7614748bfbc01ec2\solver-1\text\D02.txt
- D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i01-screen-7614748bfbc01ec2\solver-1\text\D09.txt
- D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i01-screen-7614748bfbc01ec2\solver-1\text\manifest.json
