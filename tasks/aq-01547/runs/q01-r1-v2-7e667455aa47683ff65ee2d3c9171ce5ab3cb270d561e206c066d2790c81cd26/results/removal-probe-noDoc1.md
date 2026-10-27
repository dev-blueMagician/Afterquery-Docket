# Removal probe: Doc 1 (D06) left out (q01 rev 1)

- Date: 2026-10-08
- Role: fresh blind-solver (non-fork, omitClaudeMd), packet tasks/aq-01547/runs/q01-r0-alt-m4/solver-2, rebuilt in place from the rev 1 packet (six documents renumbered D01-D06; D06 withheld)
- Question: verbatim q01 rev 1
- Unforced answer: Wonneman. Forced guess: Wonneman, p 0.85.
- Result: misses (gold "Walden-Bing and Wonneman" not reached)
- Probe ids map D01-D05 = bundle D01-D05, D06 = bundle D07.

## Raw return (verbatim)

answer: Wonneman

forced best guess: Wonneman. Probability it is correct: 0.85.

confidence: high

path:
1. Time window. All six rulings fall in July to September 2026, so none is excluded by date. D01 (Feduccia) "Filed 09/30/26". D02 (Ling, 9th Cir.) "Filed September 24, 2026". D03 (Wonneman) "Date: September 25, 2026". D04 (Ghattas) "Filed 09/29/26". D05 (De Simone) "Dated: September 2, 2026". D06 (Adler) "Filed 09/10/26".
2. D03 qualifies (pp. 1–4, 11):
   - He worked for the company: "brings suit against his former employer, defendant Global Grab Technologies Inc., alleging retaliation in violation of the whistleblower provision"; "Plaintiff was employed by defendant from July 16, 2017, to May 13, 2025"; on May 13, 2025 he "was forced to resign".
   - He complained to a federal authority: "on or about April 15, 2025 individually, and on June 4, 2025, through [counsel], [he] submitted Whistleblower Retaliation Complaints with the Office of the Inspector General". The exhibits confirm "their submission to the OIG of the U.S. Department of Health and Human Services on the dates alleged".
   - He sued later: "Plaintiff filed this lawsuit on April 14, 2026."
   - Timing: April 15, 2025 is 28 days before May 13, 2025, so the first complaint came while he was still employed. The June 4 complaint came after he left and isn't needed.
   - A possible second instance: on March 21, 2025 he told the "acting supervisor for [d]efendant's [c]ontract with USCP", whom the court elsewhere calls "the USCP contract supervisor". It is unclear whether that person is a federal official, and the answer doesn't depend on it.
3. D05, De Simone, excluded. He did report to federal authorities, but only after leaving. "In November 2014, Professor De Simone resigned from VSL". His reports were all later: the FTC on "November 7, 2016" and "December 1, 2016", more FTC material in February and May 2017, and letters to HHS and DOJ in July 2020 and August 2021.
4. D06, Adler, excluded because federal reporting while employed isn't shown. He was a "former TSC employee" until "December 2019". His complaints while employed were internal, to Mr. Sporn: a June 2016 meeting, emails on June 28 and July 4, 2018, and in-person talks on July 8, 2018 and March 18, 2019. The only hint of federal reporting is undated: he "seeks to recover a portion of the CBP's $172,845.00 settlement payment under 19 U.S.C. § 1619", which rewards someone who "furnishes ... original information". The opinion gives no filing date for the original qui tam complaint.
5. D04, Ghattas, excluded. He was a former employee, but he complained only to colleagues and the Executive Committee: "Plaintiff's internal communications don't cross that line." No report to the government is alleged.
6. D01, Feduccia, excluded. The order says nothing about his employment or any report while employed. It says only that "Relator Christopher Feduccia filed his original Complaint" on December 17, 2024.
7. D02, Ling, excluded. The defendant is the "CITY OF LOS ANGELES, a municipal corporation", not a company, and no employment relationship is stated.

minimal_documents: D03 alone establishes the inclusion. Proving nobody else qualifies takes all six. The deciding near-misses are D05 (reports came after resigning) and D06 (internal-only complaints while employed; federal report undated). D04, D01 and D02 are excluded for lack of the needed facts. No other document can replace D03.

readings:
- If "whistleblowers" means only people whose disclosures were legally protected, the answer could be "none". D03 held Wonneman's disclosures unprotected: "more closely resemble a labor dispute from a disgruntled employee than a whistleblower claim". I think this reading is weak: ordinary usage covers whistleblower plaintiffs and relators, and Ghattas's claims also failed.
- If Adler's undated § 1619 "original information" to customs, or his qui tam filing, were assumed to predate December 2019, the answer would be Wonneman and Adler. The documents don't support that.
- If the USCP contract supervisor counts as a federal authority, the answer is still Wonneman.

gaps:
- D06 gives no date for Adler's first contact with DOJ or CBP, or for the original filing in the Southern District of New York.
- D05 doesn't describe De Simone's position at VSL, but this doesn't matter because all his reports came after November 2014.
- D01 and D02 don't describe the relators' employment.
- I read all of text/D01–D06 in full, plus manifest.json. All entries in the manifest are text extractions with no PDF pages, so there was no PDF to check. I didn't read docs/ separately, since the manifest maps each text file to its docs/ source. I didn't read question.txt.
- One grep produced too much output and was saved to the harness tool-results folder. I didn't open that file; I re-ran narrower greps inside the packet instead.

contaminated: no. I received only the workspace root, packet path and question. The session context included an unrelated git status listing other tasks (aq-00949) and MCP server text, with nothing about this question or its answer.
