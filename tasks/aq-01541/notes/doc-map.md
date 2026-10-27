# aq-01541 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

## Bundle

- What it is: seven rulings by one judge in one federal case, *William Norman Brooks, III v. Trans Union LLC*, E.D. Pa. Civil Action No. 2:22-cv-00048-KSM (FCRA § 1681e(b); consumer reports showing a bankruptcy remark on a tradeline without a public-record bankruptcy). There are two sealing memoranda, one sealing order with Appendix A, a ruling on a motion to strike an expert (FRE 702), class certification, decertification plus a motion to strike experts, and preliminary approval of a settlement. Dates run from July 30, 2024 to July 6, 2026. All rulings are by Judge Karen Spencer Marston.
- Documents: 7 (D01-D07 from `text/manifest.json`). The local ids are alphabetical by file name, so they DIFFER from the task page's numbering. Use platform numbers on the form.

  | Local | Platform | File suffix | ECF Doc | Date | What |
  |---|---|---|---|---|---|
  | D01 | Doc 1 | _0 | 105 | July 30, 2024 | Memorandum on Joint Motion to Seal (class-cert / motion-to-strike materials) |
  | D02 | Doc 2 | _1 | 106 | dated "July 2021" in body, filed 07/30/24 | Order on the same motion + Appendix A redaction chart |
  | D03 | Doc 7 | _10 | 176 | July 6, 2026 | Memorandum granting preliminary settlement approval |
  | D04 | Doc 3 | _2 | 114 | August 1, 2024 | Memorandum on motion to strike Wodzinski expert report/supplemental exhibit |
  | D05 | Doc 4 | _4 | 116 | August 1, 2024 | Memorandum granting class certification |
  | D06 | Doc 5 | _6 | 154 | October 29, 2025 | Memorandum on two motions to seal (decertification materials) |
  | D07 | Doc 6 | _8 | 157 | December 2, 2025 | Memorandum denying decertification and Plaintiff's motion to strike experts |

  Date order: D01/D02 → D04/D05 → D06 → D07 → D03.
- Gaps: there are no unread ranges. Every document was read line by line (ledgers are in each Coverage line). The source itself is missing or unreproduced in these places:
  - D01 lines 209-222: "EXHIBIT A" (ECF 105 pp. 18-24, the Mary Lee Trevino declaration, Case 3:20-cv-01348 Doc 51-1, pp. 1-6) has page-header stamps only and no text in the source. These are probably image pages. They are visually unresolved because no PDF is in the bundle.
  - D07 line 58: the Lasater Report's "Table 1" is referenced but not reproduced.
  - D02 footnote 4 (grey shading, lines 323-325) cannot be checked visually.
  - D02 line 336: the boundary in "dctiv5 2, 100, …" is ambiguous. The footnote 5 marker sits next to the first listed line number.
  - None of the orders that follow D03-D07 ("An appropriate Order follows") is in the bundle. Neither are the settlement agreement (Doc. 172-2) or the class-certification order (Doc. 117, cited in D06 line 30).
- Extraction spot-checks: the originals are plain text (`method: text`, `pages: null`). Each `text/Dnn.txt` equals its original plus a 2-line header, so original line = text line − 2. Checks run by grep on the `docs/` originals:
  - Page stamps are all present (164): D01 24/24, D02 20/20, D03 20/20, D04 18/18, D05 43/43, D06 10/10, D07 29/29.
  - Footnotes matched: D01 Pansy fn 2 (orig 74); D02 fn 4 (orig 322); D03 fn 5 (orig 101); D04 fn 3 (orig 89); D05 fn 30 (orig 320); D06 fn 2 (orig 97); D07 fn 8 (orig 205).
  - Table/list rows matched: D02 Appendix A PubRec row (orig 334); D03 schedule "Day 106" (orig 127); D06 list "145-9 Exhibit 8" (orig 34). D04 has no tables, so not applicable. D05 "270 of 97330" (orig 314) is a source artifact, not an extraction error.
  - Each Dnn section lists its own layout problems (merged rows, interleaved footnotes).
- Provenance: `notes/intake.json` (schema 1) records capture_sha256 6d26e763…cee5f, from `AQ-01541_2026-10-07_0358.txt`, "7 of 7 read in full (318,834 characters)". Manifest character counts sum to 318,834. All 7 documents have incomplete=false, gap_characters 0 and matches_capture true, and their source_sha256 equals captured_sha256 (the manifest hashes). There is no recovered-source history.

## D01 - Memorandum on amended Joint Motion to Seal (Doc. No. 104), July 30, 2024

- Source: `text/D01.txt` lines 1-225 ← `docs/uscourts_paed_2_22_cv_00048_0.txt` | task page **Doc 1** (_0) | ECF Document 105, 24 pages.
  - Memorandum: pp. 1-14 (lines 3-146).
  - Vergara declaration: pp. 15-17 (lines 148-207).
  - Exhibit A: pp. 18-24 (lines 209-222, stamps only).
- Written or submitted by: Judge Marston ("MARSTON, J. July 30, 2024", line 6). Attachments:
  - Declaration of Catalina Vergara, partner at O'Melveny & Myers LLP, "Attorney for Nonparty Bank of America, N.A." Dated July 16, 2024 (lines 148-205).
  - Exhibit A: Declaration of BANA employee Mary Lee Trevino from *Brooks v. Bank of America* (line 193; no text).
- Type, date, edition: single memorandum. The motion is called an "amended joint motion to file redacted copies" (line 7) and a "Joint Motion to Seal (Doc. No. 104)" (line 31). The companion order is D02 (line 144 "An appropriate Order Follows").
- Period covered: class period January 6, 2020 to January 31, 2023 (class definition, line 22). Procedural events:
  - complaint January 2022, amended the following month (line 20)
  - reassignment May 2024 (line 25)
  - "Friday, July 12" and "Yesterday, July 15" (lines 180, 182)
  - Vergara/Trevino declarations emailed July 16, 2024 (line 141)
  - telephone conference July 23, 2024 (fn 1, line 37)

  Exhibit dates: Jan 15, 2020; Jan 17, 2020; Mar 11, 2020; Mar 13, 2020 (lines 34-45).
- Entities and aliases:
  - Parties: Plaintiff William Norman Brooks, III; Trans Union LLC ("Trans Union"; Vergara writes "TransUnion", line 184).
  - Corinne Wodzinski: "a 20-year employee" (line 7), "putative expert witness" (line 108).
  - Other people: Danielle Nowlin (line 35); Jonathan Jaffe (deposition only, line 42); Lauren KW Brennan (line 43); Albert E. Hartmann (lines 46, 84, 133-134); "Bank of America executive Neil Patak" (line 141).
  - Bank of America: "BANA" (line 175), "BOA" (inside a quote, line 182).
  - Lundquist Consulting, Inc. ("LCI"), a BANA contractor (line 184).
  - Benchmark Funding (lines 41, 45); Credco (line 36).
  - Separate case: "Brooks v. Bank of America, Case No. 3:20-cv-01348-JO-BLM (S.D. Cal.)" (line 184). The exhibit stamp reads "Case 3:20-cv-01348-RSH-BLM" (line 212).
- Tables: the exhibit list (lines 32-48) is flattened, with several entries per line (lines 34, 36, 44, 45, 48). Columns are docket no. | exhibit no. | description. There are no numeric tables, units or scale.
- Lists:
  - **16 exhibits** for targeted redaction (lines 32-48; "these 16 exhibits", line 50; "16 previously sealed documents", line 84; line 128):
    - Doc. No. 47: 10 entries, 47-1 Ex. 1 through 47-22 Ex. 29.
    - Doc. Nos. 49 & 52: 5 entries (49-1 Ex. A, 49-2 Ex. B, 52-2 Ex. D, 52-3 Ex. E, 52-4–52-7 Ex. F).
    - Doc. No. 58: 1 entry.
    - Last item: "58-3 Ex. 33 Annotated Chart Documenting SSN Inconsistencies" (line 48).
    - The Patak Declaration (47-10) is not among the 16. It is treated separately in Part C (lines 139-142).
  - **8 categories** of sealed material (lines 89-91). The last is "(8) so-called “consumer report information,”".
  - **7 Pansy factors** (fn 2, lines 68-76). The 2nd and 3rd are "not … relevant" to sealing (line 78).
  - fn 1 lists 5 briefs still sealed or redacted (line 37): 58 (redacted), 65 (sealed), 69 (sealed), 72 (sealed), last 73 (redacted).
  - BANA's redaction request: ¶¶ 8-22, final two sentences of ¶ 23, ¶¶ 26-29 (line 142; Vergara lines 184, 193).
- Forecasts, guidance, deadlines, effective dates: BANA was told it "had 24 hours to advise the court" (quote, line 182). Filing deadlines are not in D01; they are in D02.
- Hedged claims:
  - Line 108: "it is not clear that the disclosure of approximate salary information will work a clear and definable injury against Wodzinski". The hedge attaches to the injury showing. The ruling itself is firm: "the Court denies leave to redact Wodzinski’s salary information".
  - Line 116: "It is unclear whether the First Amendment standard, in addition to the common law test, applies to a motion to seal class certification materials." The hedge attaches to which standard applies. The Court then says "Thus, the Court assumes that the First Amendment right of access applies." (line 127).
  - Line 134: "there is a very real possibility that the content of those redactions could be reverse engineered". This is the re-identification risk that supports sealing.
  - Line 7: "allegedly sold". This is Plaintiff's allegation.
  - fn 4 (line 122): "conflicting guidance … from other circuits".
- Rounded prose beside exact figures: "approximate salary information" (line 108); no amount is stated. Otherwise not applicable.
- Notes:
  - Ruling: "The Court grants all but one of the parties’ proposed redactions." (line 50).
    - Denied: Wodzinski salary redaction. This is "page 85 of Deposition" (¶ 15b Row 2), and the Court cites "Doc. No. 47-3 at 84:4–86:24" (line 108). The salary is "relevant to her credibility" (line 108).
    - Sealed whole: Exhibit 2 to the Hartmann Declaration, and the bankruptcy docket printouts, "Pages 16–173" of the supplemental exhibit (¶ 15p Row 5) (lines 84, 133-134).
    - Patak Declaration: public filing approved for the paragraphs BANA does not object to (line 142).
    - Conclusion: "grants in part and denies in part leave to file redacted and sealed documents" (line 144).
  - Docket history:
    - Doc. No. 79 denied two motions to seal (Doc. Nos. 71, 74) without prejudice (lines 25-28).
    - The parties then filed their briefs publicly (Doc. No. 82, line 29).
    - The Court raised unsealing sua sponte (Doc. No. 83, line 31).
    - Doc. No. 101 had earlier unsealed Docs. 47 and 52 (fn 1).
    - Protective order: Doc. No. 40 ¶ 2 (lines 105-106).
    - The Court had directed a chart (Doc. No. 79 ¶ 4; Doc. No. 85 ¶ 3a; line 87).
  - Figures:
    - 20-year employee (line 7); "two years of class discovery" (line 20); 16 exhibits.
    - Deposition page 85 and 84:4–86:24 (line 108); Pages 16–173 (line 84).
    - Hartmann ¶ 21 (line 84) and ¶¶ 5–6, 10–12, 14–21 (line 134); 24 hours (line 182).
    - "ten (10) years" (line 22).
  - Footnotes (4): fn 1 at line 37; fn 2 at lines 65-78 (Pansy); fn 3 at line 120; fn 4 at lines 122-123. Markers: "redactions:1" (line 31), "insufficient.2" (line 64), "materials.3" (line 116), "Circuit,⏎4" (lines 116-117).
- Operative definitions, rules and scope exceptions:
  - Judicial record (line 53): "A ‘judicial record’ is a document that has been filed with the court or otherwise somehow incorporated or integrated into a district court’s adjudicatory proceedings."
  - Common-law test: "interest in secrecy outweighs the presumption" (line 57); "material is the kind of information that courts will protect and that disclosure will work a clearly defined and serious injury to the party seeking closure" (line 58).
  - First Amendment test: strict scrutiny, "an overriding interest … narrowly tailored" (lines 60-62); experience/logic two-prong test (line 117).
  - Review is document by document; reciting Pansy is insufficient (line 64).
  - E.D. Pa. L.R. 5.1.3 lists required redactions: SSNs, dates of birth, financial account numbers, names of minor children (lines 65, 81). FCRA 15 U.S.C. § 1681b(a)(1) also applies (lines 102-103).
  - fn 3 (line 120): the materials count as class-certification materials, "not disputes pursuant to Rule 702".
  - Scope exception: "the parties, with one exception, seek to seal only personally identifying and consumer credit information" (line 88).
  - Class definition, verbatim (line 22), cited as "Doc. No. 47 at 10".
- Amendments or contradictions:
  - Vergara ¶ 4a reads "Paragraphs 8-23 of the Patak Declaration" (line 187). ¶ 4, ¶ 5 and the Court say ¶¶ 8-22 plus the final two sentences of ¶ 23 (lines 142, 184, 193).
  - Exhibit numbers within the Doc. 47 group are non-sequential as printed ("47-9 Ex. 19 Deposition of Danielle Nowlin", line 35; "47-11 Ex. 16", line 36). See D02 for 47-9.
  - Case-number suffixes differ: "JO-BLM" (line 184) vs "RSH-BLM" (line 212).
- Coverage: **full**. Lines 1-225 were read in one pass and all 24 page stamps are present. Missing source text, not unread coverage: lines 209-222 (Exhibit A, pp. 18-24).

## D02 - Order on Joint Motion to Seal with Appendix A (ECF 106)

- Source: `text/D02.txt` lines 1-446 ← `docs/uscourts_paed_2_22_cv_00048_1.txt` | task page **Doc 2** (_1) | ECF Document 106, filed 07/30/24, 20 pages. The Order is pp. 1-5 (lines 3-93); Appendix A is pp. 6-20 (lines 95-443).
- Written or submitted by: Judge Marston ("/s/ Karen Spencer Marston", line 90). The Appendix A description text is the parties' proposed-redaction chart ("Plaintiff proposes…", line 100; "The Parties do not propose…", line 325). The "Ruling" column (Granted/Denied) is the Court's.
- Type, date, edition: the Order accompanying D01. Its body reads "this 30th day of July 2021" (line 6). The stamp says "Filed 07/30/24" (line 23), and the deadlines are "no later than July 31, 2024" (lines 11, 70).
- Period covered:
  - Vacated orders: February 27, 2024 (Doc. No. 46) and April 3, 2024 (Doc. No. 68), "insofar as they conflict" (lines 8-9).
  - Chart columns dated "(6/30/2022)" (lines 301-302, 313, 317, 332, 389, 398-399).
- Entities and aliases:
  - "Ms. Wodzinski" (lines 306, 336-337).
  - Lauren KW Brennan (fn 2, line 283); Neil Patak (fn 1, line 40); Catalina Vergara and Mary Lee Trevino (line 38).
  - "witness’s spouse" rows; Plaintiff's "non-litigant spouse" (line 257).
  - Bates prefixes BROOKS-TU, BROOKSTU and BROOKS. Jaffe is not named; his deposition is "Exhibit 26" (lines 53, 270-278).
- Tables: Appendix A (lines 95-442) has 16 numbered entries. Each is a flattened table with the columns Page/Line (or Page(s)) of Proposed Redaction | [Columns for Proposed Redactions] | Description and Analysis | Ruling. There are no units.
  - Row boundaries are mostly recoverable. Merged cells: "Granted 243:18-19, 22, 24" (line 136), "Granted 133:10-11, 13, 21-24" (line 274), and lines 280, 303, 317, 336.
  - Item 2 (Doc. 47-3, Plaintiff's Ex. 4, the Wodzinski deposition) has 42 page/line rows (lines 104-223, mapper count). The first is 54:24 (line 104) and the last 302:3 (line 221).
    - Exactly one row is "Denied": "85:11-12, 15-17 Salary information of nonlitigant witness" (lines 107-108). This is the only "Denied" in Appendix A (grep-verified).
    - Six rows are "First name of witness’s spouse": 171:6, 175:24, 183:11, 255:6-8, 258:9, 281:16.
  - Item 13 (Doc. 52-2, Ex. D, Wodzinski report's Exhibit A, pages 1-18):
    - Columns: party_id, acct_id, File A/B/C (6/30/2022), and "PubRec Input from sub_inp_in dctiv" (lines 296-341).
    - The PubRec column lists 21 line numbers, "2, 100, 200, … 4600, 4800" (line 336).
  - Item 14 (Doc. 52-3, Ex. E, Hartmann):
    - Exhibit 1, pages 1-3.
    - Exhibit 2: numbered BROOKS-TU pages and non-numbered PACER/docket pages, both redacted "in their entirety" (lines 346-381).
  - Item 15 (Doc. Nos. 52-4–52-7, Ex. F):
    - Pages 1-15 columns: party_id, File A, Bankruptcy Court Docket No., Bankruptcy Court Debtor Information.
    - "Pages 16-173" are docket-sheet printouts (lines 382-426).
  - Item 10 (Doc. 47-22, Ex. 29, Brennan): Exhibit A pp. 6-31, Exhibit B pp. 32-36, Exhibit C pp. 38-42 (lines 279-282).
  - Item 16 (Doc. 58-3, Ex. 33): pages 1-3, 8 column names (lines 427-442).
- Lists:
  - Order ¶ 3a: attachments to Plaintiff's class-certification memorandum (Doc. 47), i–xxxi = Exhibits 1-31 (lines 12-61). Last: "xxxi. Exhibit 31 … (Doc. No. 43-33), unredacted" (line 61).
  - ¶ 3b: Reply (Doc. 58) Exhibits 32-33 (lines 62-64). ¶ 3c: Doc. 69 (line 65). ¶ 3d: Doc. 73 (lines 67-68).
  - ¶ 4a: Defendant's Opposition (Doc. 52) Exhibits A-F (lines 71-84). ¶ 4b: Doc. 65 (line 85). ¶ 4c: Doc. 72 (line 87, last item of the Order).
  - Treatment of the 39 exhibits (mapper tally of lines 13-87):
    - "redacted as outlined in Appendix A": 16 (Ex. 1, 4, 16, 18, 19, 20, 21, 22, 26, 29, 33, A, B, D, E, F).
    - "unredacted": 15 (Ex. 2, 3, 5, 6, 7, 9, 10, 11, 23, 24, 25, 30, 31, 32, C).
    - "unredacted (except to the extent plainly required by E.D. Pa. L.R. 5.1.3)": 4 (Ex. 12, 13, 17, 28).
    - Placeholders for still-sealed exhibits: 2 (Ex. 8 = Doc. 47-7, line 31; Ex. 27 = Doc. 47-21, line 54).
    - Ex. 14: "redacted as reflected by Doc. No. 102" (line 37).
    - Ex. 15 (Patak): redacted per the Vergara/Trevino declarations (line 38; fn 1, line 40).
  - Appendix A items 1-16 (lines 98-442). The last is "16. Doc. No. 58-3 – Plaintiff’s Exhibit 33" (line 427).
- Forecasts, guidance, deadlines, effective dates: both parties must file "no later than July 31, 2024 … in the order they appear here" (lines 11, 70). ¶ 1 contains the vacatur (lines 8-9).
- Hedged claims: these hedges attach to whether a bankruptcy belongs to a person, not to any ruling.
  - "possible bankruptcy docket number" (lines 205, 219, 273).
  - "possibly filed by a nonlitigant/possible class member" (lines 408, 424).
  - "(when present)" (lines 408, 414).
  - fn 4: "The majority of the shaded cells either contain no data, or state “could not find file w/ pubrec.”" (line 324).
- Rounded prose beside exact figures: not applicable.
- Notes:
  - Ruling: "GRANTED IN PART and DENIED IN PART as outlined in the accompanying Memorandum and Appendix A" (line 10).
  - Footnotes (5):
    - fn 1 (line 40): "redacts only paragraphs 8-22, 26-29, and the last two sentences of paragraph 23".
    - fn 2 (line 283): Brennan exhibits are charts.
    - fn 3 (line 306): Exhibit A to Wodzinski's report is a chart.
    - fn 4 (lines 323-325): grey shaded cells in File B/File C are not redacted.
    - fn 5 (lines 340-341): only line numbers containing PII are redacted.
    - Markers: "Trevino;1" (line 38), "Redactions2" (line 279), "Redactions3" (lines 296, 309, 328), standalone "4" (line 319), "dctiv5" (line 336).
  - Rule citations differ: Appendix A cites "Local Civil Rule 5.2.1(11)(b)" (lines 100, 232-233, 241, 247, 254, 257, 290, 293). The Order cites "E.D. Pa. L.R. 5.1.3" (lines 35-36, 44, 55).
- Operative definitions, rules and scope exceptions:
  - Vacatur "insofar as they conflict with this Order" (line 9).
  - The L.R. 5.1.3 exception for four exhibits.
  - fn 4: shaded cells are excluded from redaction. fn 5: only PII line numbers are redacted.
  - Bankruptcy columns are redacted "(when present)".
- Amendments or contradictions:
  - The year in the date line ("July 2021", line 6) conflicts with the filed stamp and the deadlines.
  - ¶ 3 has no verb: "Plaintiff SHALL, no later than July 31, 2024, the following documents" (line 11). ¶ 4 has "file the following" (line 70).
  - Doc. No. 47-9 is listed as both Exhibit 14 (line 37) and Exhibit 19 (line 46).
    - Appendix A item 5 is "Doc. No. 47-9 – Plaintiff’s Exhibit 19": Bates page BROOKS-TU00000275, with Plaintiff's SSN, DOB and account numbers (lines 243-248).
    - D01 line 35 labels 47-9 "Ex. 19 Deposition of Danielle Nowlin".
  - Column labels: "MATCHING ADDRESS OF STATE ON DOCKET" (item 14, line 357) vs "MATCHING ADDRESS OR STATE ON DOCKET" (item 16, lines 435-437).
- Coverage: **full**. Lines 1-446 were read in one pass and all 20 page stamps are present. Shading (fn 4) cannot be checked visually (unresolved, no PDF).

## D03 - Memorandum granting preliminary approval of class settlement, July 6, 2026

- Source: `text/D03.txt` lines 1-251 ← `docs/uscourts_paed_2_22_cv_00048_10.txt` | task page **Doc 7** (_10) | ECF Document 176, filed 07/06/26, 20 pages.
- Written or submitted by: Judge Marston ("Marston, J. July 6, 2026", line 8). Settlement terms come from Plaintiff's motion (Doc. 172-1) and the settlement agreement (Doc. 172-2). The schedule is one "Plaintiff proposes, and the parties’ settlement agreement contemplates" (line 122).
- Type, date, edition: memorandum granting Plaintiff's motion for preliminary approval (lines 9-10, 243). Caption "NO. 22-0048-KSM" (line 6).
- Period covered: class period (line 26). Dates:
  - complaint January 2022, amended the following month (line 24)
  - reassigned May 2024 "from the late Honorable Gene E.K. Pratter" (line 24, Doc. 80)
  - decertification moved July 31, 2025 (Doc. 139) and "denied on December 2, 2025. (Doc. No. 145.)" (line 37)
  - settlement in principle March 5, 2026 (Doc. 169, line 39)
  - motion filed April 23, 2026 (line 41)
  - hearing June 25, 2026 (Doc. 175; lines 41, 214)
  - "oral argument on June 24, 2026" (line 158)
  - certification "August 1, 2024" (line 158)
  - "certification decision in May 2025" (line 86)
  - Jaffe's "April 22, 2025 Supplemental Report" (fns 2-3, lines 67-68)
  - final settlement hearing "December 2, 2026" (line 243)
- Entities and aliases:
  - Magistrate Judge Carol Sandra Moore Wells (lines 39, 168); "a private mediator" (line 168).
  - Jonathan Jaffe (lines 30, 67-68).
  - Class counsel Francis Mailman Soumilas, P.C. (lines 164-165).
  - Settlement Administrator Continental DataLogix, LLC (lines 86-90, 236-240).
  - Website www.BrooksBankruptcyClassAction.com (line 92).
  - Two unnamed cy pres recipients, one chosen by class counsel and one by Trans Union (lines 76-77).
  - Groups "No Bankruptcy Group" and "Aged Bankruptcy Group(s)" (lines 55-68, 88).
  - Spellings: "Tran Union" (line 158); "Bennet" (line 204) vs "Bennett" (line 218).
- Tables: Proposed Schedule (lines 123-147), flattened, "Event Date", 8 rows. It is split by fn 7 and a page break (lines 132-141).

  | Event | Date |
  |---|---|
  | Preliminary approval order entered | Day 0 |
  | Settlement Fund established with an initial $210,000.00 payment | Day 7 |
  | Notice issued | Day 60 |
  | Fee motion | Day 106 (or 14 days before objection deadline) |
  | Claims / Exclusion / Objection Deadline | Day 120 |
  | Intent to Appear | 14 Days before Final Approval Hearing |
  | Plaintiff's approval motion | 14 Days before Final Approval Hearing |
  | Final Approval Hearing | Day 145, or thereafter as ordered by the Court (last row, lines 146-147) |
- Lists:
  - Settlement terms II.A-H (lines 49-147): Injunctive Relief; Payments; Fees/Costs/Service Award; Notice & Administration; Right to Object; No Reverter; Release; Proposed Schedule.
  - Rule 23(e)(2) factors (1)-(4) (lines 153-155), addressed in III.A-D.
  - Rule 23(e)(2)(C) sub-factors (a)-(d) (lines 175-176), addressed in III.C.1-4 (lines 177-202).
  - Claim-form certifications (i)-(ii) (fn 4, line 70).
  - fn 8 service-award comparators, each $15,000: Vista Healthplan; Lincoln Adventures, where each of two plaintiffs got $15,000; Alvarez (lines 160-161, 172).
  - fn 10: Continental DataLogix prior cases Berryman v. Avantus (D. Conn. 2024) and Ramirez v. Trans Union LLC (N.D. Cal. 2022). The last item, Wilson v. Trans Union LLC (S.D. Ind. 2025), is at line 247, after the Conclusion.
- Forecasts, guidance, deadlines, effective dates:
  - Payments and funds:
    - $8,310,000.00 Settlement Fund (line 53).
    - $100.00 automatic payment for the No Bankruptcy Group only. "Approximately $2,100,000.00" is reserved for these payments (lines 63-64).
    - "Approximately $2,882,000.00" is reserved for valid-claim payments to both groups (line 66).
    - Pro rata points: 3 for No Bankruptcy Group claimants, 1 for Aged Bankruptcy Group claimants (line 73; repeated lines 210-212).
    - Expected payments: No Bankruptcy Group claimants "approximately $1,000, in addition to their automatic payment of $100"; Aged Bankruptcy Group claimants "approximately $350" (lines 75, 210-212).
    - A second distribution happens if funds allow "$10 or more" to everyone who cashed (line 76).
  - Fees and awards:
    - Fees: "one-third of the Settlement Fund, or $2,770,000" (line 82). Also "$2,770,000, which equals 30 percent of the total fund" (line 191). The comparator range is "roughly 20 to 45 percent" (line 193).
    - Expenses "up to $308,000.00" (line 82).
    - Service award "up to a maximum of $50,000" (line 82); "$50,000" (line 158).
    - Notice/admin costs "$210,000", paid within seven calendar days (line 101).
  - Time windows:
    - Injunctive relief lasts "five years" (line 50).
    - 10 calendar days for the class list, 30 for the toll-free number, 60 for email notice (lines 88, 226-228).
    - 120 calendar days for objections, exclusions and claims (lines 98, 109, 131).
    - Intent to appear "at least fourteen days before the hearing"; the hearing is "145 days after the entry" (line 109).
    - Checks void after "sixty calendar days of mailing" (line 112).
  - fn 5: exclusion requests from "five percent or more" of the class give Trans Union a termination right (line 103).
  - The order's entry date is not in the bundle (line 245).
- Hedged claims:
  - Rule 23(e)(1)(B)(i): the settlement must be "likely" to be approved (line 150).
  - "Approximately" (lines 64, 66).
  - "expects … approximately $1,000"; "are expected to receive approximately $350"; "the actual recoveries may differ from these estimates based on historical data" (line 75).
  - "would likely require further specialized expertise and millions of dollars in attorneys’ fees" (line 179).
  - "including potentially an Article III standing challenge" (line 214).
  - "On its face, the Court finds this award appears fair, reasonable, and adequate." (line 192).
  - The service award is deferred to the final hearing (line 158).
- Rounded prose beside exact figures:
  - "one-third" (line 82) vs "30 percent" (line 191) for the same $2,770,000. Mapper arithmetic: $8,310,000 ÷ 3 = $2,770,000; 30% × $8,310,000 = $2,493,000.
  - "four years" (lines 9, 158, 168, 178); "more than fifteen thousand pages" of discovery (line 178); "over 70 class actions" (line 165, citing Doc. No. 116 at 29); "two years of class discovery" (line 24).
- Notes:
  - Ruling: grants preliminary approval (lines 10, 243). Appoints Continental DataLogix (line 240). Final hearing December 2, 2026 (line 243).
  - Footnotes (10): fn 1 at line 56; fn 2 at line 67; fn 3 at line 68; fn 4 at line 70; fn 5 at line 103; fn 6 at line 114; fn 7 at lines 132-137 (Cal. Civ. Code § 1542); fn 8 at lines 159-161, continued at 172 (interleaved with body); fn 9 at line 195; fn 10 at lines 237-238, continued at 247.
  - Docket cites are mostly 172-1/172-2, but "Doc. No. 171-2 at 11" (line 75), "Doc. No. 171-1 at 12" (line 82) and "Doc. No. 171-1 at 24" (line 109) also appear.
- Operative definitions, rules and scope exceptions:
  - No Bankruptcy Group (fn 2, line 67): "there is no locatable public record of a bankruptcy with the same nine-digit SSN as on the Trans Union consumer report giving rise to class membership".
  - Aged Bankruptcy Group (fn 3, line 68): "the only locatable public record of a bankruptcy with the same nine-digit SSN as on the Trans Union consumer report giving rise to class membership was filed more than ten years prior to the date of that report".
  - Both group definitions use the phrase "according to the analysis conducted by Plaintiff’s expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report".
  - fn 1: terms take their meaning from the Class Action Agreement and Release (Doc. 172-2 at 3-7).
  - Injunctive standard (line 50). Release (line 119; fn 7). Rule 23(e) (lines 150-155). Equitable treatment (lines 204-218). Notice (lines 221-224).
  - Scope exceptions:
    - Aged Bankruptcy Group members get no automatic payment (lines 64, 211).
    - The second distribution goes only to valid claimants (line 76).
    - No reverter (line 112).
    - fn 5 opt-out termination.
    - The service award also covers individual claims "not covered by this class action" (line 158).
- Amendments or contradictions (internal):
  - Fee share: one-third (line 82) vs 30 percent (line 191).
  - Hearing date: June 25 (lines 41, 214) vs June 24, 2026 (line 158).
  - Settlement in principle: March 5, 2026 (line 39) vs "in January 2025" (line 164); both cite Doc. No. 169.
  - Certification: "certification decision in May 2025" (line 86) vs "certified the class on August 1, 2024" (line 158).
  - Doc. No. 145 is cited for the December 2, 2025 denial (line 37). D06 and D07 identify Doc. 145 as Plaintiff's opposition, and D07 is ECF 157.
  - "(Doc. No. 139.)" is cited for "the Court’s denial" (lines 179-180).
  - "Section XIV [sic]" (line 132).
- Coverage: **full**. Lines 1-251 were read in one pass and all 20 page stamps are present.

## D04 - Memorandum on motion to strike Wodzinski expert report and supplemental exhibit, August 1, 2024

- Source: `text/D04.txt` lines 1-206 ← `docs/uscourts_paed_2_22_cv_00048_2.txt` | task page **Doc 3** (_2) | ECF Document 114, filed 08/01/24, 18 pages.
- Written or submitted by: Judge Marston ("MARSTON, J. August 1, 2024", line 6).
- Type, date, edition: memorandum on Plaintiff's motion (Doc. No. 109) to preclude the Wodzinski report and testimony (FRE 702/Daubert) and to strike TU's supplemental exhibit ("Doc. Nos. 111-5 at 8–80, 111-6, 52-4–52-7", line 7). Decided "granted in part and denied in part" (lines 7, 200). The opening paragraph (line 7) nearly duplicates D01 line 7, with different docket numbers.
- Period covered:
  - Wodzinski report dated December 13, 2023 (line 36); supplemental exhibit produced January 12, 2024 (line 177); Rule 702 hearing July 9, 2024 (line 51).
  - Data: June 2022 (line 90).
  - Career: 2002, 2004, 2005, 2007 (lines 116-119).
- Entities and aliases:
  - Corinne Wodzinski: "a 20-year employee" (lines 7, 30); "Advisor on Trans Union’s Subject Selection team" (line 30); her "associate" (line 90).
  - Jonathan Jaffe, "Plaintiff’s uncontested expert" (line 131).
  - "A paralegal in the office of Trans Union’s counsel" (line 189).
  - Northern Illinois University; Information Resources, Inc.; Elgin Community College (lines 116-117).
- Tables: none (not applicable).
- Lists:
  - Wodzinski's four opinions (lines 39-47, repeated verbatim at lines 98-104). The last is (4): "Trans Union likely has multiple files for a significant number of possible class members, only one of which would contain a bankruptcy public record."
  - FRE 702 (a)-(d) (lines 55-66).
  - Three requirements: qualification, reliability, fit (lines 71-77).
  - Jaffe's three criticisms (line 131): (1) skewed sample, assigned to fit; (2) too small a sample and (3) no confidence interval, both assigned to reliability.
  - Two class features not considered (line 151): (1) a government-held public record within ten years; (2) sale to a third party.
- Forecasts, guidance, deadlines, effective dates: not applicable.
- Hedged claims:
  - Opinion (4): "likely has multiple files" (lines 47, 104).
  - Opinions (2)-(3): "does not definitively establish" (lines 43, 45).
  - "Wodzinski appears to have incorrectly believed" (line 36).
  - Wodzinski report ¶ 43c: "it is possible that additional research … would reveal that some of these consumers had filed for bankruptcy". The Court calls this "purely speculative" (line 187).
  - Jaffe's concern that she "may have engaged in “peeking”" (line 140). The Court's finding is firm: "Whether or not Wodzinski was “peeking,” her small sample size undermines the reliability of her methodology."
  - "none of the files she reviewed may have ever been sold as a credit report" (line 161).
  - fn 6: "the selected file will most likely be the one containing the highest number of associated consumer credit accounts" (line 164).
  - fn 4: "may be a sufficient preliminary analysis … it is not clear to what uses" (line 136).
  - fn 7: "likely a capable percipient fact witness" (line 181).
  - fn 3: "Thus, the Court infers that Wodzinski’s associate searched for matches to four-digit social security numbers." (line 92). This is an inference; the report does not specify.
  - "would allegedly establish" (line 88); "30 did not ultimately appear to be enough" (line 134); "there appears to be no dispute" (line 150).
- Rounded prose beside exact figures: "30 of roughly 22,000 files from June 2022" (line 133) vs "22,141 primary files from June 2022" (line 90).
- Notes:
  - Ruling:
    - Qualified (line 121).
    - Fails reliability (lines 124, 142) and fit (line 161).
    - Expert report and testimony stricken (lines 172-173, 200).
    - May testify as a fact witness (lines 169, 173, 200).
    - Supplemental exhibit is "not a proper supplement" but is "permitted for any admissible, factual evidence" (lines 196-197, 200).
  - Figures:
    - 22,141 primary files (line 90).
    - 30 sampled (line 90); "17 of the 30 primary files" matched (line 96).
    - "she added 20 more records" (line 134); fn 4 "30 or 50 test cases" (line 136).
    - "For 24 of the 50 primary files" no secondary file was found (line 187). The paralegal matched "19 of the 24" (line 189).
    - "hundreds of pages of documents" (quote, line 190).
    - "eight discrete classes" (line 22).
    - "20 years’ experience" (line 116); 2002 B.S. Mathematics and M.S. Applied Probability and Statistics; since 2005 most senior employee; 2007 created the basic match logic; "She has not authored any publications." (lines 116-119).
  - Footnotes (8): fn 1 at line 56; fn 2 at line 81 (2023 Rule 702 amendment); fn 3 at lines 91-92; fn 4 at lines 135-136; fn 5 at line 153; fn 6 at line 164; fn 7 at lines 181-182; fn 8 at line 192.
- Operative definitions, rules and scope exceptions:
  - FRE 702 text (lines 54-66); "gatekeeper" (line 68); qualification/reliability/fit (lines 71-77).
  - § 1681e(b) "reasonable procedures to assure maximum possible accuracy" (lines 163-168).
  - How Trans Union files work: Trans Union errs "on the side of not adding new consumer information" and creates "secondary" files (lines 31-34). Primary/secondary/tertiary and real-time aggregation (line 161, fn 6).
  - Class definition (line 23), cited as "Doc. No. 107 at 10". Two-step process (lines 25-27).
  - Scope exceptions: fact-witness testimony is allowed; the exhibit is considered for class-certification facts.
- Amendments or contradictions:
  - fn 5 (line 153): "Plaintiff revised his class definition to include reference to records that are publicly held". The report rested on the earlier understanding (lines 36-37).
  - fn 1 (line 56): Trans Union conceded some opinions moot but "did not state which".
  - Docket numbers differ from D01 for the same items (see Shared ground).
- Coverage: **full**. Lines 1-206 were read in one pass and all 18 page stamps are present.

## D05 - Memorandum granting class certification, August 1, 2024

- Source: `text/D05.txt` lines 1-496 ← `docs/uscourts_paed_2_22_cv_00048_4.txt` | task page **Doc 4** (_4) | ECF Document 116, filed 08/01/24, 43 pages.
- Written or submitted by: Judge Marston ("MARSTON, J. August 1, 2024", line 6).
- Type, date, edition: memorandum granting certification (lines 7, 469, 491). It appoints the class representative (line 472) and class counsel FMS (line 479), and includes a trial-plan section (lines 481-488).
- Period covered: class period January 6, 2020 to January 31, 2023, "37 months long" (line 317). Sample months January 2020, March 2021 and June 2022 (lines 91-98).
  - Clark:
    - settlement December 2003, effective after May 31, 2004 (line 30)
    - Clark Rule applied to joint accounts only 2004-2020 (line 36)
    - expansion "proposed" in 2020 (line 37)
    - "began expanding … in April 2021" (line 151)
    - completed "By February 2023" (line 38) / "by early 2023" (line 372)
  - Plaintiff's story:
    - non-party William Eugene Brooks filed bankruptcy January 3, 2020 in Mobile, Alabama (line 43)
    - Plaintiff's letter to Bank of America January 20, 2020 (line 47)
    - Trans Union file shows the remark as of January 15, 2020 (line 60)
    - Plaintiff's letter to Trans Union January 17, 2020 (line 60)
    - Bank of America furnished again March 4, 2020 (fn 2)
    - report sold March 2020 (line 61)
  - Procedure:
    - initial class-certification deadline September 2, 2022 (Doc. 25, line 65), extended (Doc. Nos. 30, 35, 38, 41)
    - motion filed February 2, 2024 (line 70)
    - opposition March 1, 2024 (Doc. 48, line 70)
    - oral argument July 9, 2024 (line 70)
    - reassigned May 15, 2024 (fn 3, line 79)
  - Other dates: Jaffe declaration "March 2023" / "March 28, 2023" (lines 100, 227); CFPB opinion Nov. 10, 2021 (line 260); Stockdale declaration December 2003 (fn 27).
- Entities and aliases:
  - Plaintiff, a California resident, and non-party William Eugene Brooks, who "shared the same last four digits" of the SSN (line 47).
  - Bank of America; Lundquist Consulting, Inc. ("LCI") (fn 1, line 52); Neil Patak (Doc. 107-15).
  - Trans Union deponents (line 88):
    - James Garst, Vice President of Data Governance.
    - Mary Wang-Chang, Senior Consultant, Online Support Team ("Senior Consultant of Online Support", line 216).
    - Danielle Nowlin, Senior Analyst, Litigation Support Department.
    - Corinne Wodzinski, "Advisor on Trans Union’s Linking and Matching Team"; also called "longtime employee" (line 159).
  - Jonathan Jaffe, "an independent technology consultant and data scientist" (line 88).
  - Lauren KW Brennan, Esq. (line 148); Albert E. Hartmann, Esq. (line 162).
  - William Stockdale, Trans Union Senior Director of Customer Information Services (fn 27, line 298).
  - Francis Mailman Soumilas ("FMS") (line 341).
  - Clark: "Clark v. Trans Union Corp. and Trans Union, LLC, C.A. No. 8:00-cv-01219-CMC (D.S.C.)" (line 28).
  - CFPB (line 260).
  - Systems and terms: Splunk; LTFS ("long term file storage", line 111); PACER; input/output logs = FFI + FFR (fn 6, line 104); "data furnishers" (line 22); outside public-record vendor (line 25).
- Tables: no formal tables; figures are inline.
  - Source artifact (also in the original): "270 of 97330 such files" (line 316). The footnote 30 marker is fused to "973". fn 30 (line 322) gives 973, and the stated 27.7% and 32.0% equal 270/973 and 311/973 (mapper check).
  - Footnote continuations interleave with body text (lines 66, 138, 168, 236, 267).
- Lists:
  - Two sources Trans Union consults (lines 21-26).
  - Four Trans Union deponents plus Jaffe (line 88).
  - **Four objective criteria** (line 196). Criterion (4) reads "within ten years of the month in which Trans Union sold the credit report".
  - Rule 23(a) four requirements (lines 173, 305); "Trans Union only challenges commonality" (line 305).
  - City Select's three reasons (line 190); adequacy's two factors (lines 337-339).
  - § 1681e(b) four elements (lines 384-386).
  - Trans Union's three categories (lines 400-409; restated line 421):
    - (1) name + full address: 17 of 50
    - (2) name + state: 13 of 50
    - (3) name + address + last four SSN digits: 19 of 24
  - Superiority factors (A)-(D) (lines 440-445).
  - fn 11: files with "0, 1, 2, and 3 additional names" (lines 127-128).
- Forecasts, guidance, deadlines, effective dates:
  - "If these proportions hold steady" (line 317): January 2020 "would yield an additional 4,736 files returning no bankruptcy … and 5,471 files returning only a stale bankruptcy". March 2021: "4,741 … and 4,623".
    - Mapper arithmetic: 27.7% × 17,098 ≈ 4,736 and 32.0% × 17,098 ≈ 5,471, which reproduce.
    - 27.7% × 14,816 ≈ 4,104 and 32.0% × 14,816 ≈ 4,741. The March 2021 pair therefore does not reproduce from the stated percentages: 4,741 matches the 32.0% product, and 4,623 matches neither.
  - "the class is likely to number in the tens of thousands" (line 152).
- Hedged claims:
  - Line 152: "likely" attaches to class size.
  - Line 317: conditional projection.
  - fn 2: "putative error by a bank employee"; "some record-evidence appears to probe" (line 55); then the firm statement "this complication is irrelevant to Plaintiff’s class claim".
  - "there appears to be little difficulty" (line 110); "Trans Union’s own Senior Consultant appears to agree" (line 121).
  - fn 9 "appears to be moot" (line 116); fn 16 "appears to be based on irrelevant information" (line 159).
  - fn 23: "This level of matching might appear to be strong evidence … but it is not"; the CFPB says "name-only matching is likely to lead to inaccuracies" (line 260).
  - fn 25 "could be partially automated" (line 276); fn 27 "appear to militate in favor" (line 298); fn 32 "presumably would have caught" (line 373).
  - "three somewhat arbitrary categories that could suggest they belong together"; "the class may not be able to prove" (line 430).
  - "appears poised to argue" (lines 431, 436); "reportedly arises" (line 204); "reportedly found thirteen" (line 165).
- Rounded prose beside exact figures:
  - 27.7% and 32.0% beside 270 and 311 of 973 (line 316).
  - "about 242 million consumers based on over 85,000 data sources" (line 88).
  - "about three (3) billion Trans Union credit reports" (line 236).
  - "about two years" (line 110); "about a month" (line 234); "tens of thousands" (lines 152, 436, 462, 466).
- Notes:
  - Ruling:
    - Ascertainable (line 290).
    - Numerosity, typicality and adequacy met (line 350); commonality and predominance met (line 436); superiority met (line 466).
    - Granted (line 491). Brooks appointed representative (line 472); FMS appointed counsel (line 479).
    - Trial-plan issue: the sufficiency of Plaintiff's method for showing inaccuracy (lines 486-488).
  - Figures, June 2022:
    - 22,141 files meeting the criteria on June 30 and May 31, 2022 (lines 91-92).
    - 1,100 sold, i.e. with a hard inquiry (lines 92-96).
    - 1,527 I/O logs extracted (line 207); 170 logs not found (fn 18, line 210).
    - "at least 270" of 1,100 lacked a PACER record (line 148); 311 had a bankruptcy over 10 years old (line 148).
    - 581 class members (line 312).
    - fn 30: "only 973 of the 1,100 input/output logs from June 2022 contained a nine-digit social security number" (line 322).
  - Figures, January 2020 and March 2021:
    - January 2020: 185,232 files, 17,098 with a hard inquiry (line 98).
    - March 2021: 138,077 files, 14,816 with a hard inquiry (line 98). Both repeated at line 312.
  - Figures, log processing:
    - The single day of March 31, 2021 took "more than one day" (lines 121, 231). fn 21: defense counsel "stated that it took one day" (line 239).
    - Jaffe: "seven full years of older data … in “a matter of hours to days to weeks,”" (line 121).
  - Figures, Trans Union's double-check:
    - "50 of the 270" (lines 162, 400, 405); 17 exact name/address matches (lines 165, 403); 13 name+state matches (lines 165, 405).
    - fn 23 says "at least 17 of the 270" (line 259).
  - Other figures:
    - Numerosity threshold "exceeds 40" (line 311).
    - Wal-Mart "approximately 1.5 million" (line 377).
    - FMS "over 70 class actions" (line 341).
    - "eight discrete classes" (fn 4).
    - "twenty years ago in Clark" (line 289); "for almost twenty years" (line 368).
    - fn 32 "eleven-year-old bankruptcy" (line 373).
  - Footnotes (37):
    - fn 1-9: fn 1 at 52-53; fn 2 at 55-57 (+66); fn 3 at 79-80; fn 4 at 82; fn 5 at 93; fn 6 at 104; fn 7 at 112-113; fn 8 at 115; fn 9 at 116.
    - fn 10-19: fn 10 at 124-125; fn 11 at 127-128; fn 12 at 129 (+138); fn 13 at 140-141; fn 14 at 154-155; fn 15 at 156-157; fn 16 at 159 (+168); fn 17 at 169; fn 18 at 210-211; fn 19 at 227.
    - fn 20-29: fn 20 at 229 (+236); fn 21 at 239; fn 22 at 251; fn 23 at 259-260 (+267); fn 24 at 269; fn 25 at 276; fn 26 at 284; fn 27 at 297-298; fn 28 at 300; fn 29 at 313.
    - fn 30-37: fn 30 at 322-323; fn 31 at 325; fn 32 at 373; fn 33 at 410; fn 34 at 422; fn 35 at 432; fn 36 at 448; fn 37 at 463.
- Operative definitions, rules and scope exceptions:
  - Class definition (lines 72, 188), cited as "Doc. No. 107 at 10".
  - Clark settlement text (line 32); Clark Rule (line 34); I/O log definition (line 100).
  - Rule 23(a), (b)(3), (c)(1)(B), (g) (lines 173-184, 355, 439-447, 475, 482-484).
  - Ascertainability: Byrd quoting Carrera (line 190); Niaspan (line 195); Kelly (lines 266-275).
  - Numerosity: Stewart (line 311).
  - § 1681e(b) elements (lines 384-386).
  - Plaintiff's "unitary standard" (line 395).
  - fn 15: "It is against Trans Union policy to report bankruptcies that are more than 10 years old." (line 156).
  - Scope:
    - Stale (>10-year) filers are inside the class (lines 332, 397; fn 32).
    - fn 2: "This litigation challenges only Trans Union’s policy of failing to apply the Clark Rule’s cross-check procedure to non-joint accounts" (line 57).
    - fn 9: only LTFS is relevant (line 116).
    - fn 24: Kelly's predominance analysis is not relevant (line 269).
- Amendments or contradictions:
  - Class definition changed:
    - fn 13: the amended complaint first defined the class "exclusively with reference to Trans Union’s internal files" (Doc. 13 ¶ 49(a)); it is now defined by government-held files (lines 140-141).
    - fn 4: eight classes became one (line 82).
  - Clark timing: 2020 proposal (line 37) vs "began expanding … in April 2021" (line 151); "By February 2023" (line 38) vs "by early 2023" (line 372).
  - Denominator for the 270: 1,100 (line 148) vs 973 (lines 316, 322).
  - Processing time: one day vs more than one day (lines 121, 231 vs 239).
  - Splunk retention: "about two years" (line 110) vs fn 7 "up to three to six months" (line 112).
  - fn 16: Wodzinski's report says one file is typically sold; at the hearing she described real-time aggregation ("Confusingly", line 168).
  - As printed: "The nonapplication of the Clark Rule to joint accounts was indisputably Trans Union’s policy" (line 372).
  - "As discussed above in Part II.B.3, Rule 23(g) provides a non-exclusive list of factors" (line 475). Part II.B.3 (lines 336-348) lists no Rule 23(g) factors.
  - March 2021 projections: see the arithmetic above.
- Coverage: **full**. Read in five chunks (lines 1-120, 120-229, 229-328, 328-427, 427-496); all 43 page stamps are present.

## D06 - Memorandum on two motions to seal decertification materials, October 29, 2025

- Source: `text/D06.txt` lines 1-123 ← `docs/uscourts_paed_2_22_cv_00048_6.txt` | task page **Doc 5** (_6) | ECF Document 154, filed 10/29/25, 10 pages.
- Written or submitted by: Judge Marston ("MARSTON, J. October 29, 2025", line 9).
- Type, date, edition: memorandum on the motions to seal of Trans Union (Doc. 140) and Plaintiff (Doc. 146). "The Court grants all the parties’ proposed redactions and sealing" (lines 10, 117). Caption "NO. 22-0048-KSM" (line 7).
- Period covered: class period (line 28). Exhibit dates March 12, 2025; April 22, 2025; June 20, 2025 (line 33).
- Entities and aliases: Jonathan Jaffe; David Alfaro; "Lauren Brennan, Esquire" (line 114); "Honorable Gene E. K. Pratter" (no "late", line 25).
- Tables: a "Doc. No. | Title" list (lines 32-36), flattened, with four entries on line 33.
- Lists:
  - **7 documents**, "these seven documents" (line 36):
    - 139-1: Trans Union's decertification memorandum
    - 139-3: Exhibit A, March 12, 2025 Expert Report of Jonathan Jaffe
    - 139-4: Exhibit B, April 22, 2025 Supplemental Expert Report of Jonathan Jaffe
    - 139-6: Exhibit D, June 20, 2025 Expert Report of David Alfaro
    - 145: Plaintiff's Memorandum in Opposition
    - 145-7: Exhibit 6 – Chart
    - last, 145-9: "Exhibit 8 – Exhibit B to Expert Report of David Alfaro" (line 36)
  - 8 categories (line 81). These match D01 lines 89-91 except the spellings "PartyIDs" and "account IDs".
  - Pansy factors 1-7 (fn 1, lines 57-65).
- Forecasts, guidance, deadlines, effective dates: not applicable.
- Hedged claims:
  - fn 2: "It is unclear whether the First Amendment standard, in addition to the common law test, applies to a motion to seal class decertification materials." (line 99). Then "the Court assumes that the First Amendment right of access applies" (line 105).
  - "not entirely irrelevant" (line 107).
- Rounded prose beside exact figures: not applicable (no numeric data).
- Notes:
  - Ruling: all redactions are granted. "Exhibit 6 to Plaintiff’s Memorandum in Opposition" is sealed in its entirety (lines 74, 114).
  - Footnotes (2): fn 1 at lines 54-67, continued at 77 inside body Part A; fn 2 at lines 98-101.
  - D06 cross-references D01 (ECF 105):
    - "The Court previously granted in part the parties’ joint motion to seal" (line 30).
    - "which the Court granted. (See Doc. No. 105.)" (line 74).
    - "Doc. No. 105 at 8–9" (line 88).
    - Doc. No. 79 ¶ 4 (line 81); Doc. No. 40 ¶ 2 (line 91).
- Operative definitions, rules and scope exceptions:
  - Same sealing framework as D01, near-verbatim: Avandia, Leucadia, Wartluft, Pansy, "E.D. Pa. L. Civ. R. 5.1.3", § 1681b(a)(1), experience/logic test, Mosaid, Carson, Del Nero (lines 40-112).
  - Scope: Exhibit 6 is sealed wholesale because targeted redactions "would not be feasible". Per the Brennan declaration (Doc. 145-1 ¶ 9), Exhibit 6 "was developed using Alfaro’s report and comparing the Trans Union consumer report data with the potential bankruptcy information" (line 114).
- Amendments or contradictions:
  - Exhibit 6 is listed as "145-7 Exhibit 6 – Chart" (line 35) but cited as "(See generally Doc. No. 145-6, Ex. 6.)" (line 114).
  - Doc. 105 is described as "granted in part" (line 30) vs "granted" (line 74). D01's salary denial is not mentioned.
  - The class definition is cited as "Doc. No. 117 at 1" (line 30).
- Coverage: **full**. Lines 1-123 were read in one pass and all 10 page stamps are present.

## D07 - Memorandum denying decertification and Plaintiff's motion to strike experts, December 2, 2025

- Source: `text/D07.txt` lines 1-294 ← `docs/uscourts_paed_2_22_cv_00048_8.txt` | task page **Doc 6** (_8) | ECF Document 157, filed 12/02/25, 29 pages.
- Written or submitted by: Judge Marston ("MARSTON, J. December 2, 2025", line 8).
- Type, date, edition: memorandum denying both motions: Trans Union's decertification motion (Doc. 139) and Plaintiff's motion to strike (Doc. 147). It grants both sides leave to file sur-rebuttal reports (lines 11, 157, 289).
- Period covered:
  - "After the Court granted Plaintiff’s motion for class certification on August 1, 2024" (line 9); "Nearly a year after certification" (line 10).
  - Jaffe reports March 12, 2025 and April 22, 2025 (line 41); Trans Union reports June 20, 2025 (lines 41, 84); interrogatory responses May 9, 2025 and June 6, 2025 (fn 4).
  - Experts deposed "in July 2025" (line 135).
  - Motions and argument: decertification moved July 31, 2025; opposition and motion to strike September 11, 2025; reply September 22, 2025; oral argument November 5, 2025 (line 67).
  - Deadlines: affirmative reports April 22, 2025 (fn 5); rebuttal June 20, 2025 (Doc. 124 at 2, line 84).
- Entities and aliases:
  - Jonathan Jaffe ("Jaffe").
  - Trans Union's experts (line 41): David Alfaro ("Alfaro"); Dr. David Lasater ("Dr. Lasater"; spelled "Lasaster" at line 67); Nicholas DeGiacomo ("DeGiacomo").
  - Wodzinski spelled "Corrine" (lines 199, 206) and "Corinne" (line 262).
  - Lauren Brennan (Doc. 145-1; lines 215, 264).
  - Thomson Reuters archived bankruptcy search (lines 47, 97, 218, 228, 238-245).
  - "the late Honorable Gene E.K. Pratter" (line 26).
  - Clark: fn 12 "Clark v. Experian Info. Sols., Inc., No. 00-cv-1217-24, 2002 WL 2005709 (D.S.C. June 26, 2002)" (lines 253-254).
  - CFPB (line 211).
- Tables: none in the text. "Table 1" of the Lasater Report is referenced only (line 58).
- Lists:
  - Trans Union's three experts and reports (line 41).
  - Pennypack factors (1)-(4) plus "importance of the evidence" (line 80; fn 6, lines 128-131).
  - Four objective criteria (lines 184-185), identical to D05 line 196.
  - § 1681e(b) elements (lines 232-237).
  - McMahon's six cross-reference sources (line 226). The last is "affidavits".
  - DeGiacomo's "five buckets" (line 60).
  - Docket entries:
    - scheduling Doc. Nos. 124, 127, 129, 130 (line 41)
    - fn 3 extensions 127, 128, 129, 130, 134, 135, 143 (line 75)
    - briefing 149-152 (line 67)
    - expert depositions 145-3 (Alfaro), 145-4 (Lasater), 145-5 (DeGiacomo) (line 110)
- Forecasts, guidance, deadlines, effective dates:
  - Plaintiff's sur-rebuttal: "within sixty days of the accompanying Order". Trans Union: "within thirty days of receipt of Plaintiff’s report" (line 157).
  - Plaintiff had asked for sixty days (lines 70, 147). Rule 26(a)(2)(D)(ii) gives 30 days (line 84).
  - Scheduling order suspended (Doc. 144, lines 136-137).
- Hedged claims:
  - Alfaro: "meaning that a customer may have had bankruptcy filings"; a one-digit SSN difference "could have been the result of a typo, which would likely explain why Mr. Jaffe’s methodology failed" (line 58).
  - "potential strong multi-attribute matching" (line 60); three "potential public bankruptcy records" (line 61).
  - Expert depositions (line 199): Alfaro "very likely the same person"; DeGiacomo "these are all probabilistic"; Lasater "no insight".
  - fn 7: "then there may have been a change in factual circumstances that would warrant decertification. Here, it remains a hypothetical question" (line 204).
  - fn 8 "suggesting" (line 207).
  - "may appear to be strong evidence … but it is not" (line 211); "likely because the experts did not opine" (line 212).
  - "appear to be most likely caused by error … did likely file" (line 264); "That results in a 4.75% error rate, which is still speculative." (line 265).
  - "the uninjured parties likely represent a de minimis portion of the class" (line 265).
  - "Plaintiff may suffer prejudice" (line 135); "So it appears it is still the case" (line 238).
- Rounded prose beside exact figures:
  - "between 17% and 28%" (Trans Union, line 194) and "between an 17% and 28% error rate" (Court, line 260) sit beside "sixty-nine of the 400 files (17.3% of the sample)" (line 58) and "110 of the 400 files (27.5% of the sample)" (line 60).
  - "4.75%" (line 265). Mapper arithmetic: 19/400 = 4.75% and 19/69 ≈ 27.5%. The text does not state the denominator.
- Notes:
  - Figures, March 2025 report (PACER, SSN + first two letters of last name; line 45): "22,212 SSNs that had no bankruptcy records returned, and 35,941 SSNs" with filings more than ten years old (line 47).
  - Figures, April 2025 report (Thomson Reuters, nine-digit SSN only): "elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals" (line 47).
  - Figures, populations and samples:
    - 20,891 class members with no record in PACER or Thomson Reuters (lines 49, 58); 400-person sample (line 49).
    - 36,317 class members with a record more than ten years old (lines 61, 63); sixty-record sample; 3 potential records (line 61).
  - Other figures:
    - fn 8: "55% of the possible bankruptcies Alfaro identified involve SSN differences of five digits or more and 20 of Alfaro’s possible bankruptcies share no SSN digits at all" (line 207).
    - "nineteen of the sixtynine records" (line 264).
    - fn 9: two "test subject" records (line 215).
    - Lidoderm "three uninjured individuals out of a class of fifty-five"; Vista Healthplan "5% uninjured" (line 265).
  - Class-list arithmetic (mapper check):
    - 22,212 + 35,941 = 58,153, and 58,153 − 920 = 57,233.
    - 20,891 + 36,317 = 57,208, which is 25 below 57,233.
  - Ruling:
    - Motion to strike denied: the reports are timely rebuttal reports (line 112), alternatively substantially justified (line 119), and the Pennypack factors favor admission (line 138).
    - Sur-rebuttal allowed (line 157).
    - Decertification denied: ascertainability (line 228), predominance (lines 252-269), due process (line 277).
    - Conclusion (line 289).
  - D07 re-quotes D05 lines 431-436 as "Doc. No. 116 at 38–39" (lines 239-242), inserting "[and Thomson Reuters]".
  - Footnotes (13):
    - fn 1-7: fn 1 at 49-50; fn 2 at 52; fn 3 marker at 67, text at 74-75; fn 4 at 115; fn 5 at 127; fn 6 at 128-131; fn 7 marker at 198, text at 203-204.
    - fn 8-13: fn 8 marker at 201, text at 206-208; fn 9 at 215; fn 10 at 233; fn 11 at 245; fn 12 at 253-254; fn 13 at 281-283.
- Operative definitions, rules and scope exceptions:
  - Rule 26(a)(2)(D) and (D)(ii) (lines 72, 84); Rule 37(c)(1) (lines 72-79); Pennypack (line 80).
  - "same subject matter" (lines 89-91).
  - Substantially justified = "genuine dispute concerning compliance" (line 114).
  - Sur-rebuttal standard (line 149).
  - Rule 23(c)(1)(C) (line 161); the burden question is unsettled (lines 164-167); decertification is an "extreme step" (line 168).
  - "The essential question is whether circumstances have changed since certification." (line 168).
  - Byrd quoting Hayes v. Wal-Mart (lines 177-178); Kelly's yes-or-no review (line 224).
  - Uninjured members do not "categorically bar" predominance (line 259); Carrera due process (line 277).
  - Scope: "other than the shift to use Thomson Reuters for further exclusion using only the nine-digit SSN" (line 218). fn 2: Trans Union "now raises no objection to the execution or efficacy of Step One" (line 52).
- Amendments or contradictions:
  - Step Two changed: PACER now requires the first two characters of the last name (line 45). Thomson Reuters allowed "only the nine-digit SSN as represented at the time the Court certified the class" (line 47).
  - fn 4: Plaintiff "now states that he does not intend to rely on Jaffe’s opinions …". The footnote sets this against Doc. 108 at 7, Doc. 116 at 35 and Doc. 145 at 23 (line 115).
  - Trans Union says 17-28% "actually did match" (line 194); the experts say "potential" (lines 194-199). fn 11: Trans Union "overstates Alfaro’s analysis" (line 245).
  - fn 12 cites "Doc. No. 116 at 116 (discussing origin of Clark Rule)" (line 253); D05 has 43 pages. The Clark caption differs from D05 line 28.
  - Hearing transcript cite: "27:6-18" (line 262) vs D05 fn 22 "27:1–18".
- Coverage: **full**. Read in three chunks (lines 1-110, 110-209, 209-294); all 29 page stamps are present.

## Shared ground (navigation only)

- Entities that appear in more than one document, and where:
  - Brooks, Trans Union and Judge Marston appear in all seven (opening lines).
  - Prior judge Gene E.K. Pratter:
    - "the late": D03 24, D05 65, D07 26
    - no "late": D06 25
    - unnamed in D01 25
    - reassignment date May 15, 2024: D05 fn 3 79
  - Wodzinski: D01 (7, 24, 34, 45, 48, 84, 108, 134), D02 (306, 336-337; Ex. 4 rows 104-223), D04 (throughout), D05 (88, 93, fn 16, 251, 257-258, 267, 409-410, 432), D07 (199, 206, 262). Absent from D03 and D06.
    - Titles: "Subject Selection team" (D04 30) vs "Linking and Matching Team" (D05 88).
    - Spelling: "Corrine" (D07 199, 206).
  - Jaffe: D01 42; D03 30, 67-68; D04 131-150; D05 88-121, 147-148, 216-227, fn 25; D06 33; D07 throughout. D02 only has "Exhibit 26".
  - Brennan: D01 43; D02 279-283; D05 148 (Doc. 107-29); D06 114 (Doc. 145-1 ¶ 9); D07 215, 264 (Doc. 145-1).
  - Hartmann: D01 46, 84, 133-134 (Doc. 52-3); D02 item 14 (346-381, as "Exhibit E"); D05 162 (Doc. 111-5).
  - Nowlin: D01 35 (47-9); D05 55, 60, 88 (Doc. 107-14).
  - Patak / Bank of America / LCI: D01 139-193; D02 38-40; D05 44-60, fns 1-2.
  - Vergara and Trevino: D01 141-205; D02 38.
  - Alfaro: D06 33, 36, 114; D07 throughout. Lasater and DeGiacomo: D07 only.
  - FMS: D03 164-165 and D05 341-343, 479. "over 70 class actions" appears in both (D03 165 cites Doc. 116 at 29; D05 341).
  - Single-document entities: Continental DataLogix, Judge Wells and the settlement groups in D03 only; Splunk/LTFS/Garst/Wang-Chang/Stockdale in D05 only; Thomson Reuters in D07 only.
  - Clark: D05 28-38, 289, fn 27, 368-379, fn 32; D07 fn 12 (different caption and number). D03 line 50's injunctive wording parallels D05 line 32's Clark settlement wording.
  - CFPB name-only advisory (Nov. 10, 2021): D05 260; D07 211.
  - Kelly v. RealPage: D05 211, 243, 248, 266-275; D07 220-224.
  - Same case name, different citations:
    - Ramirez v. Trans Union: D03 247 (2022 WL 2817588, July 19, 2022) vs D05 343 (2022 WL 17722395, Dec. 15, 2022).
    - Vista Healthplan v. Cephalon: D03 fn 8 (2020 WL 1922902, $15,000 service award) vs D07 265 (2015 WL 3623005, 5% uninjured).
  - McIntyre v. RealPage: D03 165; D05 342-343.
- Periods or series that more than one document covers, and where:
  - Class definition, verbatim: D01 22, D03 26, D04 23, D05 72/188, D06 28, D07 28. Each cites a different source: Doc. 47 at 10 (D01); Doc. 107 at 10 (D04/D05); Doc. 116 (D03); Doc. 117 at 1 (D06); Doc. 116 at 1 (D07). Absent from D02.
  - Four objective criteria: D05 196 = D07 184-185.
  - Two-step process: D03 30-33; D04 25-27; D05 77-86; D07 32.
  - Background paragraph (complaint January 2022, reassignment May 2024, "two years of class discovery"): D01 20/25; D03 24; D04 22 (+fn 5); D05 7, 65, 234; D06 25-26; D07 26.
  - June 2022 data:
    - D04 90 (22,141, 30, 17)
    - D05 91-103, 148, 207-210, 312-322
    - D02 "(6/30/2022)" columns (lines 300-336, 389)
  - January 2020 and March 2021 data: D05 98, 312, 317.
  - Two different "March" Jaffe documents: D05 (March 28, 2023 declaration, Doc. 107-25) and D06/D07 (March 12, 2025 report, Doc. 139-3).
  - The "April 22, 2025" Jaffe supplemental report: D03 fns 2-3; D06 33; D07 41, fn 5.
- Documents that cite, amend or respond to another document in the bundle:
  - D02 is the Order for D01 (D01 144; D02 6, 10). D02 fn 1 implements D01 Part C. D02 Appendix A line 107-108 ("Denied") implements D01 108.
  - D01 and D02 seal exhibits that D04 and D05 rule on substantively: the Wodzinski report, supplemental exhibit, Hartmann and Brennan declarations, and the Jaffe and Wodzinski depositions.
    - D04 ruling on the supplemental exhibit: lines 7, 176-197.
    - D05: 162-165 and 400-410.
  - Cross-references to "contemporaneously filed" memoranda:
    - D01 19 and D04 19 refer to "the contemporaneously filed Memorandum ruling on Plaintiff’s Motion for Class Certification", which is D05, dated Aug 1, 2024. D01 itself is dated July 30, 2024.
    - D05 fn 5 (93) and fn 33 (410) refer to the contemporaneous motion-to-strike memorandum ("Doc. Nos. 56, 109"), which is D04's subject.
  - Re-filed docket numbers (ordered by D01 fn 1 line 37 and D02 ¶¶ 3-4) differ for the same named items. Before → after:

    | Item | Before (D01/D02) | After (D04/D05) |
    |---|---|---|
    | Class-certification memorandum | 47 (D01 24) | 107 |
    | Wodzinski report | 52-2 | 111-4 |
    | Wodzinski deposition | 47-3 | 107-4 |
    | Motion to strike | 69 | 109 |
    | Trans Union opposition | 49 & 52 | 111 |
    | Opposition to motion to strike | 72 | 113 |
    | Jaffe deposition | 47-20 | 107-26 |
    | Brennan declaration | 47-22 | 107-29 |
    | Patak declaration | 47-10 | 107-15 |
    | Plaintiff's Jan 17, 2020 letter | 47-11 | 107-16 |
    | Hartmann declaration | 52-3 | 111-5 |
    | Nowlin deposition | 47-9 (D01 35, "Ex. 19") | 107-14 |

    D02 lists 47-9 as both Ex. 14 (37) and Ex. 19 (46). D03 35, D05 70 and D07 36 cite Trans Union's opposition as Doc. 48.
  - D06 cites D01 (Doc. 105) at lines 30, 74 and 88. D06 seals Exhibit 6 (145-7/145-6), and D07 264 relies on "Ex. 6 to Brennan’s Declaration" for its 19-of-69 review.
  - D07 cites D05 (Doc. 116) at lines 14, 30, 32, 36-38, 52, 115, 173-174, 187-191, 212, 218, 221, 228, 242, 252-253, 257.
  - D03 cites D05 (Doc. 116) at lines 12, 28, 30, 33, 35, 158, 165. D03 cites D07's denial (Dec 2, 2025) at line 37 as "Doc. No. 145", and lines 179-180 cite "Doc. No. 139".
  - D03 fns 2-3 define the settlement groups by the April 22, 2025 report. That report is listed in D06 33 and its counts appear in D07 47-49 and 61-63. D03 gives no group counts.
- Forecast/actual pairs, repeated/changed tables, same-period conflicts and scope relationships (locations only):
  - Class-size estimates and later counts:
    - D05: "likely … tens of thousands" (152); 581 in June 2022 (312); projections for Jan 2020/Mar 2021 (317)
    - D07: class list 57,233 (47); 20,891 (49); 36,317 (61); March 2025 stage 22,212 and 35,941 (47)
  - Same number, different populations:
    - 17: D04 96 (17 of 30) vs D05 165/259/403 (17 of 50 / "at least 17 of the 270")
    - 19: D04 189 = D05 409 (19 of 24) vs D07 264 (19 of 69)
    - 50: D04 134/187 (Wodzinski's 30+20) vs D05 162 (50 of the 270)
  - Agreeing repeats: 22,141 (D04 90 = D05 91); "roughly 22,000" (D04 133).
  - Percentages:
    - D05 316: 27.7% and 32.0% (PACER result shares)
    - D07: 17.3% (58), 27.5% (60), "17% and 28%" (194, 260), 4.75% (265), 55% (207)
  - Ten-year look-back: in every class definition; Trans Union policy at D05 fn 15 156 = D07 fn 1 50 (same cite, 107-14 at 67:19–68:14); Clark at D05 298.
  - Certification date: Aug 1, 2024 (D05 6; D03 158; D07 9) vs "May 2025" (D03 86).
  - Decertification:
    - motion July 31, 2025: D03 37 = D07 67
    - denial Dec 2, 2025 = D07's date (D03 37 cites Doc. 145)
    - D03 243 sets the final settlement hearing for Dec 2, 2026 (same month and day, next year)
  - Settlement estimates: D03 75 and 210-212 give approximate payments. There are no actuals in the bundle. Fees and the service award are deferred to final approval (D03 83, 158).
  - Wodzinski's "great" testimony about nine-digit SSNs: D05 fn 22 251 (Tr. 27:1–18) vs D07 262 (Tr. 27:6-18).
  - Repeated passages:
    - Pansy factors and the 8 sealing categories: D01 66-76, 89-91 = D06 57-65, 81.
    - D06 40-112 repeats D01 52-134.
    - D07 211-212 repeats D05 fn 23; D07 239-242 re-quotes D05 431-436; D07 252-257 repeats D05 416-419; D07 220-224 repeats D05 266-275.
    - D03 24-37 and D06 25-30 summarize D05 (and, in D03, D07).
    - D05 fn 5 and fn 33 summarize D04.
  - Ruling scope compared: D01 granted all but one requested redaction (salary), sealing Hartmann Ex. 2 and the docket printouts whole. D06 granted all, sealing Exhibit 6 whole.
  - Deadlines across documents:
    - D02's July 31, 2024 re-filing deadline produced the numbers cited in D04/D05.
    - D07's rebuttal deadline June 20, 2025 and affirmative deadline April 22, 2025 (84, fn 5) match the exhibit dates in D06 33.
    - D07's sur-rebuttal windows (157) are not mentioned in D03. D03 39 says Judge Wells vacated all existing deadlines in the Scheduling Order (Doc. 159).
    - D03's schedule (123-147) runs from an order-entry date that is not in the bundle.
