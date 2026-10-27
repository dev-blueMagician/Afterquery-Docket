# Removal probe: Doc 5 (D03) left out (q01 rev 1)

- Date: 2026-10-08
- Role: fresh blind-solver (non-fork, omitClaudeMd), packet tasks/aq-01547/runs/q01-r0-alt-m4/solver-1, rebuilt in place from the rev 1 packet (six documents renumbered D01-D06; D03 withheld)
- Question: verbatim q01 rev 1
- Unforced answer: Walden-Bing. Forced guess: Walden-Bing, p 0.80.
- Result: misses (gold "Walden-Bing and Wonneman" not reached)
- Finding: rev 1's "complained or reported to federal authorities" admits a parse in which "complained" stands alone (to anyone, including internally), giving Adler, Ghattas, Walden-Bing.
- Probe ids map D01 = D01, D02 = D02, D03 = D04, D04 = D05, D05 = D06, D06 = D07 of the bundle.

## Raw return (verbatim)

answer: Walden-Bing. She is the only one, under the natural reading where the complaint or report itself went to federal authorities.

Forced best guess: Walden-Bing. Probability correct: 0.80.

confidence: medium-high. The facts are clear. The remaining risk is how "complained or reported to federal authorities" is parsed, plus a timing inference from the word "Meanwhile".

path:
1. Every case in the packet was ruled on between July and September 2026, so all six are candidates:
   - D05: "ENTERED July 20, 2026"
   - D04: "Dated: September 2, 2026"
   - D06: "Filed 09/10/26"
   - D02: "Filed September 24, 2026"
   - D03: "Filed 09/29/26"
   - D01: "Filed 09/30/26"
2. D05, Walden-Bing v. Horne, LLP et al. (S.D. Tex.), p.2 — she qualifies.
   - Employment: "Walden-Bing was employed by Horne as a Quality Assurance/Quality Control Specialist".
   - Internal reports: she "reported her concerns to management and human resources".
   - Federal reports: "Meanwhile, Walden-Bing made reports to the Office of Inspector General, the Securities and Exchange Commission, and the U.S. Department of Labor."
   - Timing: "Walden-Bing was terminated around September 2, 2022 ... Two months later, she 'communicated' with the Office of Inspector General."
   - The "Meanwhile" reports come before her termination, so she was still employed. The SEC and the U.S. Department of Labor are federal even if the OIG's agency is unclear.
   - She sued Horne afterwards: original complaint "filed May 8, 2023", naming Horne.
3. D04, De Simone v. VSL (D. Md.), pp.4, 6-7 — excluded on timing.
   - "In November 2014, Professor De Simone resigned from VSL".
   - His federal reports all came later: FTC contacts "on November 7, 2016" and "December 1, 2016", more in "February and May 2017", and letters to "HHS and DOJ in July 2020" and "August 2021".
   - So he reported only after leaving.
4. D06, Adler v. Sporn Co. (D. Vt.), pp.2-7 — excluded on the evidence.
   - He was a "former TSC employee" from January 2016 to December 2019.
   - While there, his complaints were internal: the June 2016 meeting, emails to Mr. Sporn in June and July 2018, and on March 18, 2019 he "confronted Mr. Sporn".
   - Footnote 8 implies he gave CBP "original information" (his 19 U.S.C. § 1619 claim), but no date is given. The document says DOJ "referr[ed] Defendants to CBP", and his test purchases on June 24 and October 10, 2020 came after he left. Nothing places a federal report during his employment.
5. D03, Ghattas v. OrthoAtlanta (N.D. Ga.) — excluded. He "sues his former employer", but his complaints went only to "colleagues and members of the Executive Committee". The court discusses "reports to the Government" only as a general legal category, not something he did.
6. D01, Feduccia v. I.C.E. Services (D. Alaska) — excluded. Nothing says he was employed by I.C.E. or reported to any agency; he relies on fund annual reports and investor letters.
7. D02, Ling v. City of Los Angeles (9th Cir.) — excluded. No employment facts (a search for "employ" finds nothing), and the defendant is "a municipal corporation", not a company.

minimal_documents:
- D05 is enough to establish Walden-Bing.
- Showing that no one else qualifies needs D04 (De Simone reported only after resigning) and D06 (Adler's complaints were internal; any CBP report is undated). D03, D01 and D02 rule out the remaining candidates.
- No other document substitutes for D05.

readings:
- **Broader reading** — "complained [to anyone, including internally] or reported to federal authorities", while employed by a company later sued: Adler, Ghattas, Walden-Bing. De Simone is still excluded because no complaints during his time at VSL are described.
- **Counting a qui tam filing served on DOJ as a report**: no change. Feduccia has no employment shown, Adler's filing date isn't given and he left in 2019, and Walden-Bing is already included.
- **Reading "company" strictly as a corporation**: Horne is an LLP, which could give "none". I think that reading is unreasonable; an LLP is a company in the ordinary sense.

gaps:
- D05 doesn't say which agency's Office of Inspector General received her reports, and gives no exact dates for the "Meanwhile" reports beyond their order relative to her termination.
- D06 gives no date for when Adler gave information to CBP or filed his original S.D.N.Y. complaint.
- Ling's and Feduccia's relationships to the defendants are not described.
- All six text files were read in full. The manifest lists text sources only (method "text", no PDF pages), so there was no PDF to check. OCR artifacts in D06 (e.g., "201 7", "oflnterest") don't affect the answer.
- I did not read question.txt or any material outside text/ and docs/.

contaminated: no. The session started fresh with only the packet path and question. The workspace's git-status context listed unrelated file names for another task (aq-00949), with no content or answers.
