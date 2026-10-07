# q01 rev 0 shortcut audit (fresh shortcut-auditor, packet shortcut, question text only)

Date: 2026-10-05. tested_sha256: e6924891d7d17b2e587af7e71ad6e4080c0b219ce9134b435956ba27b7ec5ab2

Raw return (verbatim):

answer: FDIC (the Federal Deposit Insurance Corporation). From most to least frequent, its 2000–2004 complaint outcomes were:
(1) the consumer was given more in-depth or specific information, with no finding of error by either side;
(2) the bank was found not to be in error;
(3) the complaint was withdrawn, or set aside because it was already in litigation;
(4) the bank was found to have made an error.

verdict: clear

shortest_path:
1. D03 (GAO-06-1112T), line 189: "FDIC officials told us that they have developed a review program to identify high-risk lending areas and evaluate risk management and underwriting approaches." This matches the question's description, so the regulator is FDIC. The other agencies on that line did different things: OTS reviewed its 68 most active alternative-mortgage lenders, NCUA made informal contacts, and OCC reviewed marketing materials. None of these fits.
2. D04 (GAO-06-293). FDIC's order has to be put together from four statements about individual categories:
   - Line 225: "Between 2000 and 2004, the most common resolution of complaints handled by all federal regulators was that consumers were provided more in-depth or specific information." That makes it 1st.
   - Line 249, "Bank Was Not in Error": "third for OCC in terms of frequency, while it was second for the other regulators." That makes it 2nd for FDIC.
   - Line 241, "Withdrawn or Tabled Due to Litigation": "least common for the Federal Reserve and OTS and the third most common for FDIC." That makes it 3rd.
   - Line 253: "'Bank Made an Error' was the least common outcome for complaints resolved by OCC and FDIC." That makes it 4th.
   - The four ranks fit together with no conflict. The category names come from Appendix I, line 403.

sufficient_documents: D03 and D04 together are the minimal set. No alternative set exists. The docs/ copy of D04 (gaoreports_gao_06_293.txt) has the same text. Neither document is enough alone:
- D03 has no complaint-outcome data. Its complaint mentions are only general background at lines 131, 133 and 197.
- D04 never mentions a high-risk-lending program; line 325 is consumer groups talking about OCC. It also gives three different orders for different regulators:
  - OCC: information, withdrawn, not in error, bank error
  - FDIC: information, not in error, withdrawn, bank error
  - Federal Reserve and OTS: information, not in error, bank error, withdrawn

  So you can't get the answer from D04 without first knowing the regulator is FDIC.

searches:
- Exact words and related ideas: high-risk / high risk, pinpoint, identify areas, risky lending, review program, FDIC officials, nontraditional, alternative mortgage, complaint, resolution / resolved, FDIC / Federal Deposit Insurance, withdrawn / litigation, "decreasing frequency", "Figure 2", and the specific rank phrases.
- Files checked: all nine text files (D01–D09), plus the D04 phrases in docs/.
- Other "high risk" hits were off-topic: D08 is about fair-lending data and analysis of home-mortgage lending data, and D05 is about physical security at insurers.
- The remaining complaint and resolution hits are about other things: product-safety incidents (D01), FEMA appeals (D02), insurers (D05), bankruptcy credit counseling (D06), long-term care insurance claims (D07), and hurricane insurance lawsuits (D09). No document repeats FDIC's complaint outcomes.
- I did not open question.txt or any material outside this packet.

readings/gaps:
- Wrong reading to watch for: D04's summary at lines 217–221 lists the order "across the four federal regulators" as information, withdrawn/litigation, not in error, bank error. That is the combined order for all four regulators (and also OCC's order). It is not FDIC's, because FDIC swaps 2nd and 3rd. A reader who stops at the summary gets it wrong. This is a difficulty risk, not a shortcut.
- Extraction gaps:
  - The values in Figure 2 ("Complaint Resolutions of Selected Federal Regulators") were not extracted, so I could not check the order against percentages.
  - Footnotes 15–21 were not extracted. Footnote 19, attached to the FDIC "third most common" sentence, could add a qualification I couldn't read.
  - Both remain unresolved. Even so, the text states every FDIC rank directly, and the ranks agree with each other.
- Contamination: none found.
