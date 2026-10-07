# q01 rev 0 blind solver B (fresh blind-solver, packet solver-2, question text only)

Date: 2026-10-05. tested_sha256: e6924891d7d17b2e587af7e71ad6e4080c0b219ce9134b435956ba27b7ec5ab2

Raw return (verbatim):

answer: For FDIC, from most to least frequent: (1) FDIC gave the consumer additional information, with no finding of error; (2) FDIC found the bank was not in error; (3) the complaint was withdrawn or tabled because it was in litigation; (4) FDIC found the bank was in error.

confidence: high

path:
1. **Which regulator.** D03 (GAO-06-1112T, Alternative Mortgage Products, 20-SEP-06), line 189: "FDIC officials told us that they have developed a review program to identify high-risk lending areas and evaluate risk management and underwriting approaches." The other regulators in the same paragraph did different things. NCUA "informally contacted their largest credit unions." OTS reviewed "68 most active AMP lenders." OCC reviews "promotional and marketing materials." The Federal Reserve is reviewing Regulation Z. So the regulator is FDIC.
2. **Scope and category names.** D04 (GAO-06-293, OCC Consumer Assistance, Feb 2006) used complaint data from the four regulators for "calendar years 2000 to 2004" (line 141; again at line 397). Line 403 names the categories: "(1) regulators provide consumers additional information, (2) complaint is withdrawn or tabled due to litigation, (3) regulators determine that bank was not in error, and (4) regulators determine that bank was in error."
3. **First place (additional information).** D04 line 225: "Between 2000 and 2004, the most common resolution of complaints handled by all federal regulators was that consumers were provided more in-depth or specific information."
4. **Withdrawn or in litigation is third for FDIC.** D04 line 241: "For OCC, the second most frequent type of complaint resolution was 'withdrawn' or 'complaint in litigation,' while it was the least common for the Federal Reserve and OTS and the third most common for FDIC."
5. **Bank not in error is second for FDIC.** D04 line 249: "This category of complaint resolution was third for OCC in terms of frequency, while it was second for the other regulators." The "other regulators" are the Federal Reserve, FDIC and OTS.
6. **Bank made an error is last for FDIC.** D04 line 253: "'Bank Made an Error' was the least common outcome for complaints resolved by OCC and FDIC."
7. **Consistency check.** For FDIC the ranks are 1 information, 2 not in error, 3 withdrawn/litigation, 4 bank error. Each category gets exactly one rank. The other regulators also come out consistent:
   - OCC: information, withdrawn/litigation, not in error, bank error.
   - Federal Reserve and OTS: information, not in error, bank error, withdrawn/litigation.

minimal_documents: D03 + D04. I found no alternatives. D03 is the only document with the high-risk lending review program; FDIC appears only in D03, D04 and D08. D04 is the only document that ranks complaint outcomes.

readings:
- **Pooled four-regulator order.** D04 line 217 says the regulators "generally resolved them in one of four ways, as shown in order of decreasing frequency." That order is: information, withdrawn/litigation, not in error, bank error. If you apply it to FDIC, the 2nd and 3rd places swap. I reject this because lines 241 and 249 rank FDIC specifically, and that pooled order matches OCC's own ranking.
- **Misidentifying the regulator as OCC.** D04 line 325 mentions "lending practices that pose high risk," but that is consumer groups criticizing OCC's centralized complaint office, not a program. Reading it as OCC would give the same pooled order as above.
- **Other "high risk" mentions.** D08 line 207 (all four agencies say HMDA data shows lenders "at high risk" of discrimination) and D05 line 227 (insurers' physical security) are not programs to identify high-risk lending areas.

gaps:
- D04's Figure 2 (the bar chart of outcome percentages by regulator) and footnotes 15, 18 and 19 are missing from both the extracted text and the source .txt file. No PDF is in docs/. So I relied on the text's ordinal statements and could not check the ranking against the actual FDIC percentages.
- The text gives one ranking for the whole 2000–2004 period; FDIC's order in individual years can't be checked.
- Reading coverage:
  - Read in full: D04.
  - Read in part: D03 (lines 1–20 and 185–192) and D08 (lines 1–12 and 203–210).
  - Searched only (high-risk/pinpoint/program/FDIC/complaint/outcome terms), not read: D01, D02, D05, D06, D07 (long-term care insurance), D09 (flood insurance).
- I did not open question.txt.

contaminated: no
