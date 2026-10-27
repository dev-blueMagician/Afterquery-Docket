# Removal probe: Doc 1 (D06) left out (q01 rev 2)

- Date: 2026-10-08
- Role: fresh blind-solver (non-fork, omitClaudeMd), packet tasks/aq-01547/runs/q01-r0-alt-m4/solver-2, rebuilt in place from the rev 2 packet (six documents renumbered D01-D06; D06 withheld)
- Question: verbatim q01 rev 2
- Unforced answer: Wonneman. Forced guess: Wonneman, p 0.88.
- Result: misses (gold "Walden-Bing and Wonneman" not reached)
- Probe ids map D01-D05 = bundle D01-D05, D06 = bundle D07.

## Raw return (verbatim)

answer: Wonneman

Forced best guess: Wonneman. Probability it is correct: 0.88.

confidence: high

path:
1. **Time window.** All six rulings are dated September 2026, so they all fall within July–September 2026:
   - D01: "Filed 09/30/26"
   - D02: "Filed September 24, 2026"
   - D03: "Date: September 25, 2026"
   - D04: "SO ORDERED this 29th day of September, 2026"
   - D05: "Dated: September 2, 2026"
   - D06: "Filed 09/10/26"
2. **Wonneman (D03) qualifies.**
   - D03 line 17, p.1: "Plaintiff Matthew David Wonneman brings suit against his former employer, defendant Global Grab Technologies Inc."
   - D03 line 27, p.2: "Plaintiff was employed by defendant from July 16, 2017, to May 13, 2025"
   - D03 line 37, p.4: on May 13, 2025 he "was forced to resign"
   - D03 line 101, p.11: "on or about April 15, 2025 individually, and on June 4, 2025, through [counsel], [he] submitted Whistleblower Retaliation Complaints with the Office of the Inspector General". The same line says the exhibits confirm "their submission to the OIG of the U.S. Department of Health and Human Services on the dates alleged".
   - D03 line 40, p.4: "Plaintiff filed this lawsuit on April 14, 2026."
   - Calculation: April 15, 2025 is about four weeks before his employment ended on May 13, 2025. So this federal complaint was made while he still worked there. The June 4, 2025 complaint came after he left and isn't needed.
3. **Exclusions.** Each of these was checked against its own text.
   - **De Simone (D05):** he did go to federal authorities, but only after leaving.
     - Line 85, p.4: "In November 2014, Professor De Simone resigned from VSL"
     - Lines 109–112, pp.6–7: "on November 7, 2016, he contacted … the Federal Trade Commission". He sent more material to the FTC in 2017 and wrote to HHS and DOJ in July 2020 and August 2021.
     - All of these reports come after November 2014, and nothing says he worked for Leadiant or Alfasigma.
   - **Adler (D06):** he sued his former employer, but the reports made while he worked there were internal.
     - Line 62, p.2: "former TSC employee … from February 2018 to December 2019, he worked as chief technology officer"
     - While employed, he raised the issue only internally: a June 2016 meeting, emails to Sporn on June 28 and July 4, 2018, a talk with Sporn on July 8, 2018, and "confronted Mr. Sporn" on March 18, 2019.
     - The only sign of contact with a federal agency is footnote 8 (line 305, p.18): he "seeks to recover a portion of the CBP's $172,845.00 settlement payment under 19 U.S.C. § 1619", which rewards someone who "furnishes … original information". No date is given. Separately, line 144 mentions the DOJ "referr[al of] Defendants to CBP".
   - **Ghattas (D04):** internal reports only.
     - Line 46: retaliation "for the things he said to the Executive Committee in the Summer of 2023"
     - Line 144: "Plaintiff's internal communications don't cross that line."
     - The references to "reports to the Government" (lines 134–135) describe other cases, not his conduct.
   - **Feduccia (D01):** the opinion never describes him as employed by I.C.E. and mentions no report to authorities. Line 45 says only: "On December 17, 2024, Relator Christopher Feduccia filed his original Complaint".
   - **Ling and the Fair Housing Council (D02):** the opinion never describes Ling as working for the City. Line 86: "In February 2011, Ling and FHC filed the underlying action".

minimal_documents:
- D03 alone establishes Wonneman.
- Showing that nobody else qualifies needs D01, D02, D04, D05 and D06, each excluded on its own text. No document can stand in for another, and only D03 mentions Wonneman.

readings:
- **Filing a qui tam counts as going to federal authorities:** the answer is still Wonneman only.
  - De Simone filed on March 14, 2023 (D05 line 116), long after his 2014 resignation.
  - Adler's suit was already pending when the CBP settlement was signed on October 11, 2023. That is after he left in December 2019.
  - For Feduccia and Ling, there is no stated employment by the defendants.
- **Assume Adler's CBP tip came while he was employed:** the answer becomes "Adler, Wonneman". The documents don't support this; no date is given, and the CBP matter appears to follow a DOJ referral.
- **Wonneman's March 21, 2025 disclosure to the "acting supervisor for [d]efendant's [c]ontract with USCP" counts as federal:** it's unclear whether this supervisor worked for the company or for the Capitol Police, which footnote 3 places in the legislative branch. Either way, the answer is unchanged.

gaps:
- When Adler gave information to CBP is not stated.
- Whether Feduccia or Ling ever worked for the defendants is not stated.
- The date of Wonneman's OIG complaint is only "on or about" April 15, 2025. The four-week gap to May 13, 2025 still leaves him employed at the time.
- The packet is text only: no PDFs or layout files exist. I read all six text/ files in full. For the docs/ originals, I only spot-checked the deciding lines of D03, D05 and D06 by search, and they matched text/.

contaminated: no
- I did not read question.txt.
- The system-attached git status listed unrelated task paths (aq-00949) but contained nothing about this question.
- One search returned too much output and the tool saved it to a file outside the packet. I didn't read that file and reran narrower searches instead.
