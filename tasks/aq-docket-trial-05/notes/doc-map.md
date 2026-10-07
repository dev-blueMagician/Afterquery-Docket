# aq-docket-trial-05 - document map

Written by three parallel `bundle-mapper` runs (parts a-c, 2026-10-06) from `text/`; merged by the
caller without editing their entries. Navigation only, like the form's bundle overview: where things
are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: ten unrelated federal district-court rulings, all dated September 2026 (Law and
  contracts bundle); no ruling cites another and no party recurs across rulings.
- Documents: 10; local ids alphabetical by file. D01=Doc 2 Wagner (E.D. La.), D02=Doc 8 Resper
  (D. Md.), D03=Doc 5 Hill (D. Md.), D04=Doc 10 Worsley (D. Md.), D05=Doc 7 Langworthy (D.N.M.),
  D06=Doc 9 Hernandez (E.D.N.Y.), D07=Doc 3 Mulvilhill (N.D.N.Y.), D08=Doc 6 Howard (E.D. Pa.),
  D09=Doc 1 Richards (W.D. Pa.), D10=Doc 4 Cora (D.P.R.).
- Gaps: none. Every line of every document was read (ledgers in each part below).
- Extraction spot-checks: text equals the originals after NFKC (U+2026 ellipsis in D05, D08, D10)
  plus a header line; page-footer counts, footnotes and line offsets checked per document.
- Provenance: notes/intake.json; capture AQ-DOCKET-TRIAL-05_2026-10-06_0111.md, "10 of 10 captured
  in full", capture_sha256 68a49875fbf54fb6515ac13e0aa95f0bf8bf39528f22e152c80c375710104e34.

<!-- merged from doc-map-part-a.md -->
Written by the part-(a) mapper (2026-10-06) from `text/D01.txt`, `text/D02.txt`, `text/D03.txt` and
`text/D09.txt`, with spot-checks against the `docs/` originals. This is for navigation only: it records
where things are, not what to ask. Line numbers (L) are `text/Dnn.txt` lines. The original `docs/` line
equals the text line minus 2, because of the added header line and a blank line. Quotations here use
straight quotes, so re-copy exact wording from `text/Dnn.txt` before any use. Platform ids differ from
local ids: **D01 = Doc 2, D02 = Doc 8, D03 = Doc 5, D09 = Doc 1**.

## Part (a) scope, coverage and spot-checks

- Documents: four federal court rulings. These are an E.D. La. order and reasons (D01), two D. Md.
  memorandum opinions (D02, D03) and a W.D. Pa. memorandum opinion by a magistrate judge, issued on the
  parties' consent (D09).
- Coverage: every line of all four was read in chunks (the ledger is in each Coverage field). No unread
  ranges. There are no tables, charts or images in any of the four, so Tables are not applicable.
- Extraction spot-checks against originals:
  - Page counts: the number of "Page N of M" footers equals M in each text. D01 6/6, D02 16/16, D03 36/36, D09 9/9.
  - Footnotes: D01 fn14 "R. Doc. 36 at 6." (orig 133 = text 135). D02 fn3 "ECF Nos. 11, 14, 17, 19"
    (orig 61 = text 63) and fn8 "should normally be without prejudice" (orig 265 = text 267). D03 fn10
    Kimbrough citation (orig 375 = text 377). D09 fn2 "Medical Defendant Baird" (orig 145 = text 147).
  - Printed anomalies confirmed in the originals, so they are not extraction errors:
    - D09 "June 31, 2023" (orig 75 = text 77).
    - D03 "on or about March 31, 2024" (orig 101 = text 103).
    - D03 "[“Reply”] at 8, ECF No. 1)" (orig 433 = text 435).
    - D03 signature "George L. Russell, III" (orig 529 = text 531).
  - Table spot-check: not applicable (no tables).
- Layout of the plain text (all four):
  - Page footers ("Case ... Document N Filed MM/DD/YY Page N of M") and page numerals often sit mid-sentence.
  - Footnote reference numerals often sit at the start of the next paragraph, for example:
    - D01 L45 "5 Wagner", L47 "7 Consequently", L127 "14 But,".
    - D03 L53 "2 CBMST", L59 "3 (See", L63 "4 who", L77 "5 Captain", L333 "8 and".
    - D09 L143 "2 The Court".
  - Footnote bodies are interleaved at the ends of pages.

## D01 - Wagner v. Delgado Community College (E.D. La.): order and reasons granting a motion to dismiss

- Source: docs/uscourts_laed_2_25_cv_01383_0.txt | text/D01.txt L1-156 | platform **Doc 2** | 6 pages
  (footers L41, L73, L97, L119, L137, L155)
- Written or submitted by: United States District Court, Eastern District of Louisiana (L5-7). Signed by
  "WILLIAM J. CRAIN, UNITED STATES DISTRICT JUDGE" (L151-153), "New Orleans, Louisiana, this 14th day of
  September, 2026" (L149).
- Type, date, edition: "ORDER AND REASONS" (L17); "CIVIL ACTION ... NO. 25-1383 ... SECTION: C (4)"
  (L9-13); footer "Case 2:25-cv-01383-WJC-KWR Document 37 Filed 09/14/26". Single edition.
- Period covered: one live-fire maritime and fire training exercise "on a single date" (L111), called
  "the May 8 incident" (L111; no year is stated in D01). Motion filed April 27, 2026 (L19); ruling
  September 14, 2026 (L149). Calendar dates only.
- Entities and aliases:
  - Plaintiff "FREDDIE L. WAGNER, JR." (L9), "Wagner". He proceeds pro se (L51, L125).
  - Caption defendant "DELGADO COMMUNITY COLLEGE- MARINE/FIRE TRAINING, ET AL" (L13-15); "Delgado" (L85,
    L111). The second amended complaint "names two defendants" (L25), and Delgado is not one of them.
  - "Board of Supervisors of Louisiana Community and Technical Colleges" (L19, L25, L133-141), also "the
    Board of Supervisors" and "Delgado's governing board" (L85).
  - "Regina Radosta, in her official capacity" (L19, L25), "Radosta". Her role is described only as "a
    government official alleged to be responsible for implementing board policies, and who has general
    oversight responsibility but no policy making authority" (L123).
  - Louisiana, the state (L83-85). The Fifth Circuit "uses two inquiries" (L93).
- Tables: not applicable.
- Lists:
  - Claims (L25): 42 U.S.C. § 1983 claims for deprivation of rights "including bodily injury and due
    process," allegedly caused by the Board's policies, customs or practices, and an injunction against
    Radosta. "He does not request past monetary damages" (L25).
  - Prayer, four items (L47, fn8):
    1. A declaration that his constitutional rights "were violated".
    2. Prospective injunctive relief.
    3. Costs and fees.
    4. Other relief the court deems just and proper.
  - Motion grounds (L47): Fed. R. Civ. P. 12(b)(1) and 12(b)(6), and 28 U.S.C. § 1915. Dismissal "with
    prejudice" was requested (fn9, R. Doc. 35-1 at 1, 16-17).
  - Ex parte Young, two inquiries (L93-99):
    1. "whether the complaint alleges an ongoing violation of federal law and seeks prospective relief".
    2. "whether the named official holds a sufficient 'connection [to] enforcement of the act.'"
  - Decretal paragraphs, three "IT IS ORDERED"-type paragraphs (L131-147):
    - The Motion (R. Doc. 35) is GRANTED. Claims against the Board and Radosta are "DISMISSED WITH PREJUDICE
      for lack of subject matter jurisdiction" (L133-141).
    - Leave to amend is DENIED (L143).
    - The previously filed Motion to Dismiss (R. Doc. 18) is "DENIED AS MOOT" (L145-147).
  - Dispositions by defendant:
    - The Board is dismissed because the Eleventh Amendment bars "every form of relief", and the defect
      "cannot be cured by an amendment" (L91).
    - Radosta is dismissed "for lack of subject matter jurisdiction" (L123).
    - Both dismissals are with prejudice (L141).
- Forecasts, guidance, deadlines, effective dates:
  - May 8 incident (no year; L111).
  - R. Doc. 18, earlier motion to dismiss (date not stated; L145-147).
  - R. Doc. 27, second amended complaint (date not stated; fn1, fn4, fn7, fn10, fn12).
  - R. Doc. 35, the motion, filed April 27, 2026 (L19); R. Doc. 35-1 (fn9).
  - R. Doc. 36, cited for Wagner's reframing (fn13, at 4) and his leave request (fn14, at 6). The type of
    document is not named.
  - Order dated September 14, 2026 (L149).
  - No deadline to object or amend is set, and no appeal is mentioned.
- Hedged claims:
  - "allegedly caused by official policies, customs, or practices" (L25): the hedge attaches to causation.
  - "The conditions are alleged to have arisen from institutional practices, training failures, and a lack
    of proper safeguards" (L27): attaches to the source of the conditions.
  - "Under limited circumstances, Ex parte Young permits suits against a state official, but not the state
    or its agencies" (L89): limits the exception, not the bar against the state.
  - "Even if the relief requested is prospective" (L103): an assumption made after L101 finds the relief
    retrospective.
  - "District courts ordinarily afford a plaintiff at least one opportunity to cure" (L125): "ordinarily"
    attaches to the general practice, which L127 then declines to follow.
- Rounded prose beside exact figures: none. Figures as printed:
  - "two defendants" (L25) and "two inquiries" (L93).
  - "a single training exercise on a single date" (L111).
  - "amended twice" (L125) and "at least one opportunity" (L125).
  - 6 pages; 14 footnotes.
- Notes:
  - Footnotes (14):
    - fn1 L29: R. Doc. 27 at 1-2, ¶¶ 5-6.
    - fn2 L31-33: ¶¶ 13-14.
    - fn3 L35-37: ¶¶ 15-16.
    - fn4 L39: R. Doc. 27 at 2, ¶ 7.
    - fn5 L57-59: ¶¶ 8, 10.
    - fn6 L61-63: ¶¶ 11-12.
    - fn7 L65: See R. Doc. 27.
    - fn8 L67-69: Id. at 3.
    - fn9 L71: R. Doc. 35-1 at 1, 16-17.
    - fn10 L95: R. Doc. 27 at 2, ¶ 6.
    - fn11 L113: Id. at 3.
    - fn12 L115: R. Doc. 27 at 2, ¶ 12.
    - fn13 L117: R. Doc. 36 at 4.
    - fn14 L135: R. Doc. 36 at 6.
  - Negative and exclusion statements:
    - "No damage for an isolated or accidental event is alleged" (L27/L43).
    - The second amended complaint "neither refers to nor incorporates any earlier pleadings" (L45).
    - "Louisiana has not consented to be sued in federal court" (L83).
    - The relief is "retrospective, not prospective" (L101).
    - "He does not allege he is still enrolled at Delgado, nor does he allege he is returning for further
      training" (L111).
    - A resolved grievance "is a completed injury, not a threatened future injury" (L121).
    - "There is no allegation she has any policy making authority" (L123).
    - Radosta's status "cannot change"; the defects "cannot be pled away" (L127).
  - Past tense as retrospective relief: a declaration that defendants "violated" his rights; "The use of
    the past tense looks backwards" (L101).
  - Citations:
    - New Orleans Ass'n of Cemetery Tour Guides (L47); In re FEMA Trailer (L51).
    - Savage v. Westcott, 152 F.4th 687 (5th Cir. 2025) and Erickson v. Pardus, 551 U.S. 89, 94 (2007) (L51-53).
    - Pennhurst, 465 U.S. 89 (L81, L101, L123).
    - La. Rev. Stat. § 13:5106(A) and Kling v. Hebert (L83-85).
    - Hall v. Bd. of Supervisors of Cmty. & Tech. Colls., No. 15-67 (E.D. La. May 18, 2015) (L85).
    - Ex parte Young, 209 U.S. 123 (1908) (L87; pin 157 at L99); Raj; City of Austin v. Paxton (L89-91).
    - Warnock v. Pecos County (L91); Verizon Md. (L93); White Hat v. Murrill, 141 F.4th 590, 600 (5th Cir. 2025) (L99).
    - Green v. Mansour (L101).
    - Smith v. Bd. of Comm'rs of La. Stadium & Exposition Dist., printed "371 F. Supp. 313, 321 (E.D. La.
      2019)" (L103-105).
    - Stringer v. Whitley (L107); City of Los Angeles v. Lyons (L107-109); Geiger v. Jowers (L121).
    - Okpalobi v. Foster (en banc) (L123); Fed. R. Civ. P. 15(a)(2) and Brewster v. Dretke (L125).
  - L87 ends with a stray " ." (as in the source).
- Operative definitions, rules and scope exceptions:
  - Rule 12(b)(1) "challenges the court's subject matter jurisdiction". "The party asserting jurisdiction
    bears the burden of establishing it" (L51).
  - Pro se filings are "construed liberally", but "liberal construction cannot be used to expand
    jurisdiction which the court does not possess" (L51-55).
  - "Absent waiver by the state or valid abrogation by Congress, the Eleventh Amendment bars suit in
    federal court against a state, its agencies, and its officials acting in their official capacity"
    (L79). "The bar extends to claims for injunctive and declaratory relief" (L81).
  - "Louisiana's governing boards of higher education are arms of the state and entitled to Eleventh
    Amendment immunity" (L85).
  - An official-capacity suit "is a suit against the state. Such claims can only proceed under the Ex parte
    Young exception" (L93).
  - Standing for prospective relief:
    - It "requires more than a past injury" (L103).
    - The threatened future injury must be "concrete and particularized, and actual or imminent, not
      conjectural or hypothetical" (L105).
    - The plaintiff must show "continuing, present adverse effects" (L107).
  - An injunction against an official with "general oversight responsibility but no policy making
    authority, is effectively an injunction against the state" (L123).
  - Leave to amend is denied "Because no amendment can establish jurisdiction over these defendants" (L127).
- Amendments or contradictions:
  - Pleading history: "Wagner's original complaint has now been amended twice" (L125). The second amended
    complaint (R. Doc. 27) is operative and confines the analysis (L45-47). The earlier motion (R. Doc. 18)
    is mooted (L145-147).
  - Labelling as printed: L93-99 states the two inquiries, with the second being "connection [to]
    enforcement". L103 calls the ongoing-injury and standing analysis "the second inquiry under Ex parte
    Young". The connection and policy-making point appears under "Last," (L123). The document states no
    precedence between these.
  - Requested versus ordered: the defendants moved to dismiss "with prejudice" (L47), and the order
    dismisses "WITH PREJUDICE for lack of subject matter jurisdiction" (L141).
- Coverage: **full**. Read L1-156 in one chunk. Unread: none. Missing source text: none known. Not stated
  in the source: the year of the May 8 incident, the dates of R. Doc. 18 and R. Doc. 27, and the type of
  R. Doc. 36.

## D02 - Resper v. Weber (D. Md.): memorandum opinion on the State Defendants' motion to dismiss or for summary judgment

- Source: docs/uscourts_mdd_1_24_cv_03278_0.txt | text/D02.txt L1-270 | platform **Doc 8** | 16 pages
  (footers L31, L41, L49, L71, L85, L105, L119, L133, L153, L169, L189, L201, L215, L235, L249, L269)
- Written or submitted by: United States District Court for the District of Maryland (L3-5). Signed
  "September 18, 2026 /S/ Julie R. Rubin, United States District Judge" (L259-263).
- Type, date, edition: "MEMORANDUM OPINION" (L17); "Civil No.: 1:24-cv-03278-JRR" (L11); footer "Document
  52 Filed 09/18/26". The disposition is "by accompanying order" (L19) and "by separate order" (L259).
- Period covered: wheelchair assignments from August 30, 2022 (L37) to an order dated through June 10,
  2025 (L41-43); state-court emergency complaint March 20, 2024 (L25/L33); ruling September 18, 2026.
  Calendar dates only.
- Entities and aliases:
  - Plaintiff "WAYNE RESPER" (L7), "Plaintiff". He is "an incarcerated individual" housed at "Western
    Correctional Institute ("WCI")" (L25). Formerly self-represented, he is "now represented by appointed
    counsel. (ECF Nos. 20, 27.)" (fn2 L27). His declaration is "Resper Decl., ECF No. 5-2" (L39, L45, L205).
  - "State Defendants" = "Defendants Weber and Lasher" (L49):
    - "WARDEN RONALD S. WEBER" (L13), also "former Warden Ronald S. Weber" (L19), "[then Warden Defendant
      Weber]" (L37) and "the Warden" (L45).
    - "Sergeant Lisa Lasher" (L19).
  - "Medical Defendants" = "Defendants Mace and Akintade" (L49):
    - "[Nurse Practitioner Burnice Mace]" (L37).
    - "Regional Medical Director Solaide Akintade" (L37).
    - They are not movants, and D02 states no disposition of the claims against them.
  - Non-party "Dr. Masoud Djahanmir" (L41), who issued the wheelchair referral and the order.
  - Targets of the state-court complaint: "Maryland Department of Public Safety and Correctional Services
    and the Division of Corrections (or personnel therein) and medical personnel at WCI" (L33). That
    complaint was filed in the "Circuit Court of Allegany County, Maryland" (L25/L33).
  - An unnamed "private medical contractor" provides medical services at WCI (L55; fn4; fn6 L213).
  - "the Motion" = "Motion to Dismiss, or in the Alternative, Motion for Summary Judgment at ECF No. 44" (L19).
  - Same-surname entities: "Francis v. Weber" (fn4 L67) is a case name. "Richards" appears in D02 only in
    "Merritts v. Richards" (fn8 L267).
- Tables: not applicable.
- Lists:
  - Wheelchair assignments for full-time use, three periods (L37; ECF Nos. 1-4, 1-5, 1-6):
    - "from August 30, 2022, through August 30, 2023".
    - "on August 31, 2023, for one year".
    - "on November 1, 2024, for one year".
  - A separate "long distance" order, "completed 'for' Defendant Mace, dating from June 10, 2024, through
    June 10, 2025" (L41-43; ECF No. 2 ¶ 13; ECF No. 5-1).
  - All Housing Unit access denied, six items (L39): "showers, medication, telephone, commissary, mail[,]
    and medical receptacles".
  - Claims as the court understands them (L49-51): two § 1983 claims, (1) Eighth Amendment deliberate
    indifference to serious medical needs and (2) retaliation for First Amendment activity. He seeks
    "compensatory and punitive damages" (L51).
  - Equal Protection is considered "out of an abundance of caution" (L243). Injunctive relief is "now moot"
    and "voluntarily withdrawn" (fn5 L187).
  - Eleventh Amendment exceptions, three (L165-167):
    1. Congressional abrogation.
    2. A suit "for prospective injunctive relief against state officials acting in violation of federal law".
    3. State waiver in federal court.
  - Rule 12(d) conversion, "two requirements" (L99-109): "some indication by the court", and "a reasonable
    opportunity for discovery".
  - Examples of limits on relying on medical judgment (L231): "failing to investigate cries for help,
    failing to have an individual examined by medical professionals, relying on medical judgment of
    individuals without direct knowledge of the individual, etc."
  - Dispositions (L259, fn8 L267):
    1. The Complaint is "dismissed without prejudice as against State Defendants in their official
       capacities".
    2. "summary judgment will be entered in favor of Defendant Weber in his individual capacity and
       against Plaintiff on Plaintiff's § 1983 claims".
    3. "Plaintiff's § 1983 claims against Defendant Lasher will be dismissed without prejudice."
    - Equal Protection: "similarly subject to dismissal for failure to state a plausible claim" (L255).
    - Not reached: "remaining arguments regarding the relief sought and qualified immunity" (fn7 L265).
- Forecasts, guidance, deadlines, effective dates:
  - August 30, 2022 to August 30, 2023: full-time wheelchair (L37).
  - August 31, 2023: one-year order (L37, L45).
  - March 20, 2024: emergency complaint filed by "Plaintiff and five other prisoners" (L25/L33).
  - March 30, 2024: "advised of [his] transfer from [WCI]"; the attempt "failed" (L33-35).
  - June 7, 2024: interview by Mace "pursuant to instructions from" Akintade (L37).
  - June 10, 2024 to June 10, 2025: the "long distance" order period (L41-45).
  - June 14, 2024: meeting with then-Warden Weber "with his 'entire administration' in attendance" (L37).
  - The wheelchair was confiscated "At some point after that meeting" (L39; no date).
  - November 1, 2024: Djahanmir's full-time referral, followed "three hours later" by the different order (L41).
  - Undated: the ECF No. 40 order on the operative pleading (fn3 L63) and the ECF No. 44 motion.
  - Opinion September 18, 2026 (L259). No deadlines are set.
- Hedged claims:
  - "Defendant Mace apparently told Plaintiff that 'the Warden had placed her in charge of [his] care,'
    which 'the Warden acknowledged.'" (L45): "apparently" attaches to Mace's statement.
  - "Seemingly in an effort to generate a dispute of fact as to Defendant Weber" (L201): attaches to the
    plaintiff's purpose.
  - Medical staff "seemingly informed at least Defendant Weber of some such decisions" (L231): attaches to
    whether Weber was informed.
  - "Although it is not clear to the court that Plaintiff has raised a claim under the Equal Protection
    Clause" (L243): attaches to whether the claim was raised. The court still rules on it (L255).
  - "at most, these support that Defendant Weber attended a patient care meeting and instructed Plaintiff
    to abide the protocol set by medical staff" (L205). The defendants' actions were "minimal, if any" (L253).
  - Statements of legal doctrine:
    - States "generally enjoy immunity" (L157).
    - The court "routinely 'favor[s]'" Rule 12(b)(1) (L81).
    - "[n]either the Supreme Court nor [the Fourth Circuit] has conclusively determined" (L81).
    - Immunity dismissal "should normally be without prejudice" (fn8 L267).
- Rounded prose beside exact figures:
  - "which he had possessed for nearly two years" (L39), beside the dated assignments (L37).
  - "three hours later" (L41).
  - "several times a week over the past five months" (L47; the reference date is not stated).
  - License "placed on hold at least three times" (L49; fn6 L213).
  - "five other prisoners" (L25).
- Notes:
  - Footnotes (8):
    - fn1 L27: construes the Motion as both dismissal and summary judgment; ECF Nos. 1, 5, 39; Byers v.
      Painter, 173 F.4th 155 (4th Cir. 2026).
    - fn2 L27-29: counsel appointed; no liberal construction; the proposed amended pleading has "never
      been operative".
    - fn3 L63-65: operative pleading per ECF No. 40; ECF Nos. 11, 14, 17, 19 reviewed and found "not
      material".
    - fn4 L67-69: Francis v. Weber, No. 1:23-CV-2175-LKG (D. Md. Aug. 2, 2024); Blankumsee v. Maryland
      Dep't of Pub. Safety & Corr. Servs.
    - fn5 L187: injunctive relief moot and withdrawn.
    - fn6 L213: the license-hold allegation is not evidence; Rule 56(c)(1) quoted.
    - fn7 L265: relief and qualified immunity not reached.
    - fn8 L267: declines the request for dismissal with prejudice; Adbul-Mumit; Albert v. Lierman, 152
      F.4th 554, 564; Merritts v. Richards, 62 F.4th 764, 772 (3d Cir. 2023).
  - ECF index:
    - 1: Complaint. 1-4, 1-5, 1-6: wheelchair assignments.
    - 2: cited for ¶¶ 8, 12, 13, 15-19 and not otherwise identified.
    - 5: supplement (5-1 order; 5-2 Resper Decl.).
    - 11, 14, 17, 19: additional filings.
    - 20, 27: counsel. 39: supplement filed after counsel appeared. 40: order on the operative pleading.
    - 44: the Motion (44-1 memorandum pp. 16-17; 44-2 Weber Decl. ¶¶ 3-5; 44-3 Lasher Decl. ¶¶ 3-5).
    - 45: Medical Records, p. 105. 50-1: opposition, pp. 5-7.
    - Document 52: this opinion.
  - Negative and exclusion statements:
    - "no hearing is necessary" (L19).
    - After counsel appeared, the plaintiff "did not seek to file an amended complaint" except ECF No. 39 (L29).
    - Medical staff are "employed solely by that private medical contractor" (L55).
    - Neither Weber nor Lasher hired staff, took part in care, or had authority over it (L55, L199).
    - "Plaintiff does not dispute" the official-capacity bar (L153).
    - "No exception is applicable here, and Plaintiff does not argue to the contrary" (L167).
    - "Congress has not abrogated sovereign immunity for § 1983 suits" (L167).
    - "Plaintiff does not seek prospective injunctive relief against a state official" (L173).
    - The State "has not waived its Eleventh Amendment immunity to suit in federal court; nor does
      Plaintiff argue any waiver" (L173).
    - No challenge to conversion and no Rule 56(d) affidavit (L113).
    - "Plaintiff has identified no evidence to support that Defendant Weber directed medical staff" (L205).
    - "no allegation (or evidence) of Defendant Lasher's involvement" (L207).
    - The providers "were not subordinates of State Defendants" (L233).
    - "includes no factual allegations" of different treatment (L249).
    - Failing to respond "concedes the point" (L177-181, L253).
- Operative definitions, rules and scope exceptions:
  - Rule 12(b)(1): facial versus factual challenge (L73-77). "The plaintiff bears the burden of
    establishing subject matter jurisdiction by a preponderance of the evidence" (L79).
  - Eleventh Amendment under Rule 12(b)(1): not "conclusively determined", but the court "favor[s]"
    Rule 12(b)(1) (L81-83). The exhibits do not bear on immunity, so the court proceeds as under Rule
    12(b)(6) (L89).
  - Rule 12(d) text (L95), and a motion captioned "in the alternative" puts the non-movant "on notice"
    (L105-109).
  - Rule 12(b)(6) plausibility (L117-125). Rule 56: "no genuine dispute as to any material fact" (L129); a
    "scintilla" is insufficient (L141).
  - Official-capacity suits "are the equivalent of suits against the state itself" (L159).
  - Ex parte Young "only permits actions against state officials, not the State itself or its
    instrumentalities" (L173, quoting MediGrow).
  - MD. CODE ANN., STATE GOV'T § 12-201(a) waives immunity only for "certain types of claims raised in
    state court" (L173).
  - § 1983 personal liability: "the official charged acted personally in the deprivation of the plaintiff's
    rights" (L193-195).
  - Non-medical officials are "entitled to rely on the professional judgment of the medical personnel"
    (L209), but the rule is "not without limit" (L229).
  - Supervisory liability element: "actual or constructive knowledge that his subordinate was engaged in
    conduct that posed a pervasive and unreasonable risk of constitutional injury" (L233).
  - Equal Protection:
    - The plaintiff must have been "treated differently from others with whom he is similarly situated",
      and "the unequal treatment was the result of intentional or purposeful discrimination" (L247).
    - In prisons, the treatment must be "not reasonably related to any legitimate penological interests"
      (L247).
- Amendments or contradictions:
  - Operative pleading, as printed:
    - fn1 (L27) refers to "the Complaint and its Supplements. (ECF Nos. 1, 5, 39.)".
    - fn3 (L63) says "Per the order at ECF No. 40 ... the Complaint at ECF No. 1, as supplemented by the
      filings at ECF Nos. 5, 11".
    - ECF No. 11 also appears among the "additional documents at ECF Nos. 11, 14, 17, 19" (L63).
  - The Mace/Weber statement is described twice:
    - L45: "apparently told ... 'the Warden had placed her in charge' ... which 'the Warden acknowledged'".
    - L201-203: "Defendant Mace informed Plaintiff (which Weber confirmed) he put her in charge".
  - The plaintiff contends the June 10, 2024 order is "fraudulent" because "the August 31, 2023, order
    remained in effect at that time" (L45).
  - The defendants requested dismissal with prejudice; the court declined (fn8 L267).
  - The Motion is "construed as a motion to dismiss in part and a motion for summary judgment in part"
    (L19, L113).
- Coverage: **full**. Read L1-120, L120-229, L229-270. Unread: none. Missing source text: none known.
  Not stated in the source: the dates of ECF No. 1 and ECF No. 44, the confiscation date, the contractor's
  name, and the content of ECF No. 45 p. 105.

## D03 - Hill v. Maryland Department of State Police (D. Md.): memorandum opinion granting in part and denying in part a motion to dismiss

- Source: docs/uscourts_mdd_1_25_cv_02281_0.txt | text/D03.txt L1-536 | platform **Doc 5** | 36 pages
  (36 footers, first L47 and last L535)
- Written or submitted by: United States District Court for the District of Maryland (L3-5). "Entered
  this 17th day of September, 2026" (L527); signed "/s/ George L. Russell, III, Chief United States
  District Judge" (L529-533).
- Type, date, edition: "MEMORANDUM OPINION" (L33); "Civil Action No. JRR-25-2281" (L29); footer "Case
  1:25-cv-02281-JRR Document 20 Filed 09/17/26". "A separate Order follows" (L525). The document does not
  explain the "JRR" suffix.
- Period covered: the 2020 captain promotional exam (L57) to the ruling on September 17, 2026. The core
  events run from 2021 to 2023. Complaint page cites use CM/ECF pagination (fn2 L65). Calendar dates only.
- Entities and aliases:
  - Plaintiff "DUANE HILL" (L7), "Plaintiff Duane Hill ("Lt. Hill")". He is "an African American
    lieutenant" with MDSP "for over twenty years" (L41) and a "longstanding member" of CBMST (L43).
  - Defendant "MARYLAND DEPARTMENT OF STATE POLICE" (L13-15), "("MDSP")" (L35, L41).
  - "Coalition of Black Maryland State Troopers ("CBMST")" (L43). "CBMST President Anthony Alexander" (L99).
  - Internal Affairs Division ("IAD") (L75). Positions:
    - "Assistant Commander of IAD ("Assistant Commander")" (L75).
    - "Acting IAD Commander" (L85). The opposition calls it a captain-level position (L85; Opp'n at 4).
    - "permanent IAD commander position (the 'permanent IAD Commander position' or 'IAD Commander
      position')" (L123). Hill conceded it is a "Captain-level position" (L251; Opp'n at 4).
    - "IAD's civilian administrator" (L105, L499).
  - Other people:
    - "Captain Daniel Everett ("Cap. Everett")" (L77-79).
    - "[then Captain] Chappell" (fn5 L91).
    - "Mr. Hock (Chief of Staff)" (L85).
    - "Maryland Governor Wes Moore ("Gov. Moore")" (L87), "Governor Moore" (L415).
    - "Colonel Roland Butler ("Col. Butler"), an African American male" (L87).
    - "Captain James DeCourcey ("Cap. DeCourcey"), a White male" (L123), "Captain DeCourcey" (L301).
  - People named from the 2020 captain promotional list:
    - Robert Iman: White, "ranked first", promoted June 16, 2021 (L241).
    - Justin Moss: White, "ranked second" (L241).
    - Kenny Brown: African American, "ranked third" (L63, L241); "Major Brown" (fn4 L69).
    - Douglas Reiner: White, "ranked fifth" (fn3 L67, L243).
    - Diane Hansen: White female, "ranked sixth" (fn3 L67, L243).
    - Jeffrey Jones and Thomas Quade: White, "ranked first and second respectively" (L111); also "two
      other lieutenants who ranked higher than Lt. Hill" (L237).
    - Hill: "nine (9) out of twenty-five (25)" (L57, L233), "number three (3)" at the March 24, 2023
      meeting (L111), and "ranked third" (fn6 L133).
    - Of the top nine, "six were White; Lt. Hill and Kenny Brown ... were the only African American
      lieutenants" (L61-63). The fourth-ranked lieutenant is not named in D03.
  - EEOC: "Equal Employment Opportunity Commission ("EEOC")" (L131). "EEOC Charge" = "Attach. Def.'s Mot.
    Dismiss ... ECF No. 13-3" (L81-83).
  - Statutes:
    - Title VII of the Civil Rights Act of 1964, 42 U.S.C. §§ 2000e et seq. ("Title VII") (L139).
    - Maryland Fair Employment Practices Act ("MFEPA"), Md. Code Ann., State Gov't §§ 20-601 et seq.
      (L139); "FEPA" in the Pense parenthetical (L505).
  - Same name, different entity, within D03:
    - Moore: Gov. Moore versus Moore v. Abbott Lab'ys (L449).
    - Brown: Kenny Brown versus Brown v. Dir. SCDC (L299).
    - Perkins: Perkins v. Int'l Paper Co. (short cite L367, full cite L405), Perkins v. Univ. of Md.
      (L505), and Evans v. B.F. Perkins Co. (L157).
    - Williams: Big Picture Loans (L163), Giant Food (L221), Fam. Health Int'l (L265-267).
    - White: the racial descriptor; "White" as a short cite for Burlington N. v. White (L361, L437, L451);
      and White v. BFI (L257).
    - Lewis: Lewis v. Balt. City Bd. (L475) and Hooven-Lewis (L477).
    - "Napolitano" is the short form of Allen v. Napolitano (L449-459).
- Tables: not applicable. Statistics appear in prose only:
  - "approximately 31.7%" Black share of the state population and "approximately 12-13%" Black share of
    MDSP troopers (L49, repeated at L315).
  - Counts of commissioned officers by rank "on January 31, 2023 and December 31, 2023" are said to be in
    the Complaint (Id. at 7) but are not reproduced (L317).
- Lists:
  - Counts (L139-141; Compl. at 13-21):
    - Count I: race discrimination under Title VII.
    - Count II: hostile work environment under Title VII. It holds two claims, race-based and "retaliatory
      harassment" (L329-331).
    - Count III: retaliation under Title VII (printed "(Counts III)").
    - Count IV: MFEPA "similar claims" for disparate treatment, hostile work environment and retaliation (L503).
  - Dispositions (summary at L193):
    - Count I: granted (L325).
    - Count II: granted (L383-385).
    - Count III: denied (L471, L499).
    - Count IV: dismissed "for lack of subject-matter jurisdiction" (L505).
    - Counts I, II and IV are dismissed "without prejudice" (L519-521). Leave to amend is denied (L515-519).
    - Overall: "grants in part and denies in part" (L525).
  - Relief sought (L141): declaratory, injunctive and monetary relief, reinstatement, and attorneys' fees
    and costs.
  - MDSP's grounds (L193):
    - Counts I-III fail to state a claim.
    - Count IV is barred by sovereign immunity.
    - On Count III, three arguments (L391-393): no protected activity, no materially adverse action, and
      no causation.
  - Failure-to-promote elements (L213-217): (1) protected class; (2) applied; (3) qualified; (4) failure
    to promote "under circumstances that give rise to an inference of unlawful discrimination".
  - Similarly-situated factors, five (L285-289): same job and responsibilities; same standards; same
    supervisor; comparable education and experience; differentiating or mitigating circumstances.
  - Hostile work environment elements (L331-335): unwelcome; based on race or protected activity; severe
    or pervasive; imputable to the employer.
  - Retaliation elements (L391): protected activity; materially adverse action; causal relationship.
  - Causation routes (L463-465): close temporal proximity; facts suggesting causation; a combination of both.
  - Circumstances for the severe-or-pervasive test (L367): frequency; severity; physically threatening or
    humiliating versus an offensive utterance; interference with work.
  - Alleged adverse actions (L261, L389, L433): denial of promotion to captain; failure to appoint to the
    permanent IAD Commander post; exclusion from key communications and decision-making.
- Forecasts, guidance, deadlines, effective dates (in date order as printed):
  - "Sometime in 2020": the exam (L57).
  - Six of the eight lieutenants ranked above Hill were promoted "between June 2021 and April 2022" (L57).
  - June 16, 2021: Iman promoted (L241).
  - "Sometime in 2021": transfer request. September 2021: Hill becomes Assistant Commander (L75).
  - January 12, 2022: Everett appointed IAD Commander, per the Complaint (L75; fn5 L89). The EEOC Charge
    says "[i]n or around February 2022" (fn5 L91).
  - January 12, 2022: Kenny Brown promoted to captain after Moss (fn4 L69; L241).
  - April 8, 2022: Reiner promoted after Hansen (fn3 L67; L243).
  - October 1, 2022: Everett "began leave", and Hill becomes Acting IAD Commander (L81, L85, L111).
  - November 1, 2022: Everett "retired" (L81).
  - January 31, 2023: date of the officer data (L317).
  - February 23, 2023: Gov. Moore nominates Col. Butler (L87).
  - March 24, 2023: CBMST meeting in Annapolis (L99, L111).
  - September 2023: Hill takes the 2023 test and does "not pass" (L119-121).
  - September 6, 2023: Brown promoted to major (fn4 L69).
  - October 18, 2023: DeCourcey appointed permanent IAD Commander (L123, L245).
  - October 31, 2023: the 2020 list "was set to expire" (L111; fn6 L133-135).
  - December 31, 2023: date of the officer data (L317).
  - January 24, 2024: EEOC Charge (L131).
  - "on or about March 31, 2024": Col. Butler "ultimately was appointed Superintendent" (L103).
  - April 16, 2025: Notice of Right to Sue, ECF No. 1-2 (L139).
  - July 14, 2025: action filed, ECF No. 1 (L139).
  - October 20, 2025: Motion, ECF No. 13 (L143).
  - February 2, 2026: Opposition, ECF No. 16 (L143).
  - March 4, 2026: Reply, ECF No. 19 (L143).
  - September 17, 2026: opinion entered (L527).
  - Deadlines: the list expires October 31, 2023, and Hill would have had to retake the exam in September
    2023 "to remain eligible" (L111). The court sets no deadline. Leave is denied because Hill did not file
    the proposed amendment and redline under Local Rules 103.6(a) and (c) (L515-519).
- Hedged claims:
  - "The only exception to this order of promotion appears to occur with respect to ... Douglas Reiner"
    (fn3 L67): "appears" attaches to Reiner being the only exception. L241 states it without a hedge ("In
    fact, the only lieutenant ...").
  - Six of the top nine "appear to have been promoted ... based on the order in which they are ranked"
    (L239): attaches to promotion by rank order.
  - "Lt. Hill appears to allege his failure-to-promote ... claim under the McDonnell Douglas framework"
    (L213): attaches to the framework.
  - "Lt. Hill appears to allege Cap. DeCourcey as a relevant comparator" (L291).
  - The rank difference "not only suggests a difference in experience and qualifications, but also likely
    constitutes a 'differentiating circumstance'" (L295): "suggests" attaches to experience and
    qualifications; "likely" attaches to the differentiating circumstance.
  - "this data may indicate that there were more White commissioned officers than Black commissioned
    officers" (L317).
  - "Lt. Hill appears to rely on both" causation routes (L469). "the inquiry appears to be highly fact
    driven" (L491).
  - "Lt. Hill appears to concede— and the Court agrees—that MFEPA claims are barred" (L503): the hedge
    attaches to Hill's concession, not to the court's agreement.
  - fn6 (L133-135): "It is unclear ... whether failing the September 2023 promotional exam rendered him
    immediately ineligible", and "it is not clear to the Court whether ... Lt. Hill could have been
    promoted".
  - Rumours: "numerous rumors circulating that Col. Butler was not going to promote Lt. Hill" and
    "rumor[s] that Col. Butler was going to let the promotional list ... expire" (L113-117; EEOC Charge at 7).
  - Other qualified or conditional wording:
    - "Even assuming that MDSP did not have a formal application procedure" (L229).
    - "the Court is unpersuaded" (L265); "Even assuming, for argument's sake" (L273).
    - "The Fourth Circuit generally has interpreted" (L487).
    - "just enough facts to nudge his allegations across the threshold of plausibility" (L497).
- Rounded prose beside exact figures:
  - "Approximately four months later, on January 12, 2022" (L75), after "September 2021" (L75).
  - "after nearly a year of the IAD commander position being vacant" (L123, quoted again at L229) and "it
    took approximately a year" (L123). Exact dates: leave October 1, 2022 (L81); retirement November 1,
    2022 (L81); appointment October 18, 2023 (L123).
  - "serving as the acting IAD Commander for over a year" (L229, L235); "for over a year before the CBMST
    meeting" (L497).
  - "a seven-month gap between ... March 2023 and ... October 2023" (L475); exclusion "continued for seven
    months until Cap. DeCourcey became the permanent IAD Commander" (L499). Exact dates: March 24, 2023
    (L99), October 18, 2023 (L123), October 31, 2023 (L111).
  - Gaps in cited cases: "a two-month temporal gap" (L473); "A six month lag is sufficient to negate any
    inference of causation" (L477); "a 'handful of comments . . . spread over four years'" (L489).
  - "over twenty years" of service (L41).
- Notes:
  - Footnotes (10):
    - fn1 L45: facts are taken from the Complaint; Erickson v. Pardus.
    - fn2 L65: CM/ECF pagination.
    - fn3 L67: Reiner and Hansen; April 8, 2022; Hill's IAD investigation of Reiner.
    - fn4 L69: Brown made captain January 12, 2022 and major September 6, 2023; not a CBMST member.
    - fn5 L89-91: Everett's date in the Complaint versus the EEOC Charge.
    - fn6 L133-135: eligibility after failing the exam is unclear.
    - fn7 L225: the court assumes no formal application was needed for captain.
    - fn8 L337-339: the third element for retaliatory harassment (Hinton; Burlington N.).
    - fn9 L353: protected activity is found; cross-reference "subsection II.B.3".
    - fn10 L377: new allegations raised in the opposition; a party "may 'not amend his Complaint through
      an opposition'" (Kimbrough, D. Md. July 23, 2026).
  - ECF index:
    - 1: Complaint. 1-2: Notice of Right to Sue.
    - 13: Motion (13-2 "Mot."; 13-3 "EEOC Charge").
    - 16: Opposition (16-1 "Opp'n").
    - 19: Reply, which L435 cites as "ECF No. 1".
    - Document 20: this opinion.
  - Negative and exclusion statements:
    - Col. Butler "was not a member of the CBMST" (L87).
    - Brown "is not a member of the CBMST nor has he advocated for the changes favored by CBMST" (fn4 L69).
    - The first six lieutenants had not "outwardly complained" (L63).
    - Jones and Quade "had also not been promoted to captain as of the CBMST meeting" (L111).
    - Hill "did not study" and "did not pass" (L119-121).
    - Hill "never formally applied for or even expressed interest in the permanent IAD commander position
      to Col. Butler" (L223; undisputed).
    - The Complaint "contains no facts alleging that Lt. Hill communicated his interest" (L229).
    - It is "bereft of facts regarding Lt. Hill's ranking ... on October 18, 2023" (L245).
    - Non-promotion "does not constitute materially adverse action" (L435, L443).
    - MDSP raises no argument on the subjective component (L365).
    - "the Parties have not cited—and the Court has not found—Fourth Circuit case law limiting this
      route" (L491).
    - Hill did not submit a proposed amendment or redline (L515). The court "declines to rule on whether
      an amendment would be futile" (L519).
    - The statistics do not show applicant numbers or qualifications (L315, L321).
  - Mentions versus actions around the meeting:
    - CBMST "opposed" the nomination (L97).
    - Hill "was asked to attend the meeting to listen and provide points" (L101-103).
    - MDSP called his participation "nothing more than public disapproval of a political opponent" (L421).
    - The court found the meeting's purpose was "opposing discriminatory personnel practices within MDSP" (L429).
  - Citation-form anomalies as printed:
    - "Laurent-Workman, 54 F.4th at 331" (L361), where elsewhere the first page is 201 and the pins are
      210, 213 and 219 (L333-335, L441, L473).
    - "780 F.Supp.2d 600, 621–21" (L449).
    - Short cites with no earlier full citation: "Harris, 510 U.S. at 22" (L367). "Perkins, 936 F.3d at
      208" (L367) comes before the full cite at L405.
    - "185F.Supp.3d" (L337).
    - Subsection numbers: "3. Count III" (L387) and "3. Count IV" (L501).
  - The Complaint is quoted two ways: "limited to nearly non-existent" (L105) and "limited or nearly
    non-existent" (L499).
  - Salary phrases at L267 ("total salary was lowered ...") carry bracketed substitutions and are cited to
    Williams, 2025 WL 2506580, at *8.
- Operative definitions, rules and scope exceptions:
  - Rule 12(b)(1) is granted "only if the material jurisdictional facts are not in dispute and the moving
    party is entitled to prevail as a matter of law" (L151). The plaintiff bears the burden by a
    preponderance (L157), but for sovereign immunity the burden "falls to [the] entity seeking immunity as
    an arm of the state" (L163).
  - "the defense of sovereign immunity is a jurisdictional bar"; the court "must dismiss the action for
    lack of subject-matter jurisdiction" (L161-163).
  - Integral documents, and judicial notice of EEOC charges (L185-189).
  - Applying for a position:
    - A plaintiff must apply if "the employer has a formal system for posting vacancies"; "general
      requests for advancement are insufficient" (L221).
    - The requirement "may be relaxed" when vacancies are not made known (L221).
    - The court assumes no formal application was needed for captain (fn7 L225).
  - An "acting" position "by definition, is temporary" (L265). "There can be no adverse employment action
    where an employee's terms, conditions, and benefits of employment remain the same" (L267).
  - Comparators: the plaintiff must "identify the proposed comparator", and there is "no bright-line rule"
    (L283-285).
  - "statistical evidence alone is insufficient to raise an inference of discriminatory intent in a
    disparate treatment case" (L313).
  - Severe or pervasive:
    - The test has subjective and objective components (L363) and is a "high bar" (L371).
    - Exclusion from communications is "sufficient to state a claim for retaliation" but is not
      "physically threatening or humiliating" (L373).
  - Protected activity:
    - Two categories, "participation and opposition" (L407), with an "expansive view" of opposition (L409).
    - The employee must "communicate[] to [his] employer a belief that the employer has engaged in ... a
      form of employment discrimination" (L409-411).
  - Materially adverse action: one that "could well dissuade a reasonable worker from making or supporting
    a charge of discrimination" (L437). The standard is "more lenient than" the one for adverse employment
    action (L439-441).
  - Causation:
    - Temporal proximity counts only if "very close" (L473).
    - Otherwise, "continuing retaliatory animus and conduct" during the gap can establish it (L479-481).
  - MFEPA: "[MFEPA's] waiver of sovereign immunity does not extend to suits in federal court" (the
    opposition's words, L505). Pense: Maryland "has not waived its Eleventh Amendment immunity as to FEPA
    claims in federal court" (L505).
  - Leave to amend:
    - It is "futile where an amended complaint could not survive a motion to dismiss" (L509).
    - Dismissal with prejudice is proper only "if there [are] no set of facts" (L511-513).
    - Local Rules 103.6(a) and (c) require a proposed amendment and a redline (L515-517).
- Amendments or contradictions:
  - Everett's appointment: the Complaint says January 12, 2022 (L75; fn5 L89); the EEOC Charge says "[i]n
    or around February 2022" (fn5 L91). The court records both and does not resolve them.
  - Ranks on the 2020 list:
    - L111: Jones and Quade "ranked first and second respectively".
    - L241: Iman "ranked first", Moss "ranked second".
    - Hill: 9th of 25 (L57, L233) versus "number three (3)" (L111) and "ranked third" (fn6 L133).
    - The document does not say expressly whether the L111 ranks are positions remaining after promotions.
  - Reiner as the only out-of-order promotion is hedged at fn3 L67 and stated without a hedge at L241.
  - Reply ECF number: "ECF No. 19" (L143) versus "at 8, ECF No. 1" (L435; confirmed in the original).
  - Butler's appointment is printed "on or about March 31, 2024" (L103), after his nomination on February
    23, 2023 (L87). L223 speaks of "Col. Butler after he became Superintendent" in relation to the vacancy
    filled October 18, 2023 (L123). Recorded as printed.
  - Requests on amendment (L507):
    - Hill sought leave to amend the Title VII counts and "dismissal without prejudice" of the MFEPA
      claims (Opp'n at 16-17).
    - MDSP sought denial of leave as futile and dismissal with prejudice (Reply at 14).
    - The court denied leave on procedural grounds, did not reach futility, and dismissed without
      prejudice (L515-521).
  - The opposition's new allegation ("publicly demoted ...") is not treated as an amendment (fn10 L377).
- Coverage: **full**. Read L1-90, 90-179, 180-259, 260-329, 329-398, 398-457, 457-516, 516-536. Unread:
  none. Missing source text: none known. Not stated in the source: the officer counts (L317), the name of
  the fourth-ranked lieutenant, the date of Moss's promotion, and when Everett "announced his retirement"
  (L79).

## D09 - Richards v. Edwards (W.D. Pa., Erie Division): memorandum opinion on motion to dismiss ECF No. 108

- Source: docs/uscourts_pawd_1_24_cv_00004_2.txt | text/D09.txt L1-184 | platform **Doc 1** | 9 pages
  (footers L63, L81, L103, L121, L135, L149, L157, L161, L183)
- Written or submitted by: United States District Court for the Western District of Pennsylvania, Erie
  Division (L5-9). "Christopher B. Brown, United States Magistrate Judge" (L51; signed "BY THE COURT:
  s/Christopher B. Brown", L177-181). "DATED this 14th day of September, 2026" (L175). The magistrate
  judge has authority because all parties consented (fn1 L59-61; 28 U.S.C. § 636).
- Type, date, edition: "MEMORANDUM OPINION" "ON MOTION TO DISMISS ECF No. 108" (L47-49); case
  "1:24-CV-00004-CBB" (L45); footer "Document 122 Filed 09/14/26". "An appropriate Order follows" (L173).
- Period covered: medical events from June 2023 to December 8, 2023 (L75-85); ruling September 14, 2026.
  Calendar dates only.
- Entities and aliases:
  - Plaintiff "SAMUEL E. RICHARDS" (L11), "Richards". He is pro se (L131) and "currently in DOC custody and
    incarcerated at SCI Forest" (L73).
  - "Pennsylvania Department of Corrections ("DOC")" at "State Correctional Institution ("SCI") at Albion"
    (L55); "SCI-Albion" and "SCI- Albion" (L77-79, L155, L161). He was transferred from "SCI-Dallas" (L77).
  - Caption defendants (L15-19): "M.J. EDWARDS", "DR. BAIRD, MEDICAL DIRECTOR", "NURSE SUPERVISOR LOCK",
    "RNS MONEY".
  - "Corrections Defendants" = "Defendants M.J. Edwards, Nurse Supervisor Lock, and RNS Money" (L57-67).
    They are the movants.
  - "The remaining Defendants filed an Answer. ECF No. 104" (L69). fn2 calls Baird "Medical Defendant
    Baird", "represented by different counsel who filed an Answer, ECF No. 104" (L147).
  - Edwards is "the Corrections Health Care Administrator assigned to SCI-Albion and responsible for all
    administrative duties in SCI-Albion's medical department" (L155).
  - Unnamed: "reception nurses" (L79) and "an ophthalmologist" (L85).
  - Documents named: "the DOC's Health Care Procedure Manual" and "the Inmate Health Care Plan" (L161).
- Tables: not applicable.
- Lists:
  - Four claims (L87-95). The last item, Count 4 against Baird, is at L95.
    1. § 1983 Eighth Amendment deliberate indifference against Edwards, for "failing to promptly
       schedule[unintelligible] plaintiff's sick call requests" (¶ 11).
    2. § 1983 Fourteenth Amendment equal protection against Edwards, Lock and Money, for "failing to
       provide reasonable accommodations" (¶¶ 12, 14).
    3. ADA (42 U.S.C. §§ 12101 et seq.) failure to accommodate against Edwards, Lock and Money (Id.).
    4. § 1983 Eighth Amendment deliberate indifference against Baird, for "failing to promptly
       schedule/coordinate plaintiff's recommended specialized medical treatment[.]" (¶ 13).
  - Relief sought: "declaratory, injunctive and monetary relief" (L97; ¶¶ 15-18).
  - The Corrections Defendants' three arguments (L135-137; ECF No. 109 at 5-11):
    1. Official-capacity claims are barred by Eleventh Amendment immunity.
    2. There is no personal involvement.
    3. The ADA and Equal Protection claims fail to state a claim.
  - Concessions (L141; ECF No. 112 at 5, 10): the official-capacity claims are withdrawn; declaratory and
    injunctive relief is withdrawn; he cannot state an ADA claim or a Fourteenth Amendment equal protection
    claim.
  - Sick-call slips (L81, L161): June 25, 2023; August 23, 2023; September 7, 2023. Accommodation requests
    (L81): June 27, 2023; July 19, 2023.
  - Supervisory liability, two "general" ways (L155): the supervisor personally participated, or the
    supervisor set a policy, custom or practice that caused the harm. The first theory covers a supervisor
    who "participated in violating the plaintiff's rights, directed others to violate them, or, as the
    person in charge, had knowledge of and acquiesced in his subordinates' violations" (L157).
  - Dispositions (L141, L167, L171):
    - Granted, "dismissed with prejudice": official-capacity claims, declaratory and injunctive relief, the
      equal protection claim and the ADA claim.
    - Denied: the Eighth Amendment claim against Edwards, Count One (L167).
    - The conclusion's list of what remains has a single numbered item: "(1) an Eighth Amendment
      deliberate indifference to serious medical needs claim against Defendants Edwards and Baird" (L171).
    - Count Four against Baird is not addressed and "will remain" (fn2 L147).
    - No claim against Lock or Money is listed as remaining (L141, L171).
- Forecasts, guidance, deadlines, effective dates:
  - June 2023: approved and scheduled for a "keratoplasty procedure", which "did not occur" (L75).
  - June 25, 2023: sick-call slip (L81).
  - June 27, 2023: accommodation request (L81).
  - Transfer from SCI-Dallas to SCI-Albion, printed "On June 31, 2023" (L77) and "in June 2023" (L161).
  - July 19, 2023: accommodation request (L81).
  - August 23, 2023 and September 7, 2023: sick-call slips (L81).
  - A grievance, undated: he was seen "one week after" it (L85).
  - September 20, 2023: seen by medical staff (L85, L161).
  - December 8, 2023: an ophthalmologist recommends a corneal transplant and darker-tinted glasses (L85).
  - ECF Nos. 104, 108, 109 and 112 are undated (L67-69).
  - September 14, 2026: opinion (L175). No deadlines are set.
- Hedged claims:
  - "Richards generally alleges" (L55).
  - "This request was seemingly granted in part" (L81): "seemingly" attaches to the accommodation being
    granted in part (he viewed the records, received no hard copy and had "15 to 20 minutes").
  - "It appears that Richards names Defendant Edwards ... by virtue of his status as a supervisor" (L155):
    attaches to why Edwards is named.
  - "It appears that Richards bases his constitutional claims against Defendant Edwards for his failure to
    follow the DOC's Health Care Procedure Manual, the Inmate Health Care Plan and because he denied
    Richards's requests" (L161): attaches to the basis of the claims.
  - "While Richards' allegations are not fully developed, the amended complaint includes enough facts to
    raise a reasonable expectation discovery will reveal evidence" (L161).
  - "Richards concedes almost all of the arguments" (L141). The argument not conceded is personal
    involvement on Count One (L141-143).
- Rounded prose beside exact figures:
  - "one week after he filed a grievance" (L85); the grievance date is not printed.
  - "only given 15 to 20 minutes" (L83).
  - "in June 2023" (L161) versus "June 31, 2023" (L77).
- Notes:
  - Footnotes (2):
    - fn1 L59-61: consent to the magistrate judge (§ 636).
    - fn2 L147: Baird's Count Four remains; he has different counsel and filed an Answer (ECF No. 104).
  - ECF index:
    - 47: amended complaint (¶¶ 4, 8-18). 47-1: exhibits (at 4, at 6).
    - 104: Answer. 108: the motion.
    - 109: brief in support (at 5, 5-11, 7-9, 9).
    - 112: Richards's response (at 5, 7-9, 10).
    - Document 122: this opinion.
  - Negative and exclusion statements:
    - The keratoplasty "did not occur" (L75).
    - "no surgery documented in his medical chart" (L79).
    - "not scheduled or seen" (L81).
    - "not provided with a hard copy" (L83).
    - "no need to address this claim here" (fn2 L147).
    - "Liability under § 1983 cannot be predicated solely by a defendant's status as a supervisor" (L155).
    - The court's role is "not if they will ultimately prevail" (L117).
  - Citations:
    - Gould Elecs. (3d Cir. 2000), "holding modified by Simon v. United States" (L107).
    - Iqbal and Twombly (L111); Fowler (L111); Phillips (L111-113); Doug Grant (L115); Morse (L117).
    - Scheuer v. Rhodes, 416 U.S. 232, 236 (1974), "(overruled on other grounds)" (L117-119).
    - Schmidt v. Skolas (L125-127).
    - Haines v. Kerner; Boag v. MacDougall; Mala (citing Riddle, 10th Cir.) (L131).
    - Evancho v. Fisher; A.M. ex rel. J.M.K. v. Luzerne Cnty. Juv. Det. Ctr. (L155-159).
    - Zilich v. Doll (M.D. Pa.) (L161).
  - Grammar as printed: "The following claims remains" (L171); "should be dismiss" (L137); "with this
    respect to this claim" (L143).
- Operative definitions, rules and scope exceptions:
  - Jurisdiction under 28 U.S.C. § 1331 (L57).
  - Rule 12(b)(6):
    - "A defendant bears the burden of showing a plaintiff's complaint fails to state a claim" (L105).
    - The complaint needs "enough facts to raise a reasonable expectation that discovery will reveal
      evidence of" each element (L111).
  - The court may consider the complaint, exhibits, public records and documents "integral to or
    explicitly relied upon". Otherwise the motion is converted under Rule 12(d) (L125-129).
  - Pro se pleadings get "less stringent standards", but "pro se litigants still must allege sufficient
    facts" (L131).
  - Personal involvement: a defendant "must have personal involvement in the alleged wrongdoing" (L155).
    Supervisor theories at L155-159.
- Amendments or contradictions:
  - The operative pleading is the "amended complaint", ECF No. 47 (L81, L135, L161). The original
    complaint is not described.
  - The transfer is printed "June 31, 2023" (L77; confirmed at original line 75) and "in June 2023"
    (L161). The June 25, 2023 sick-call slip and the June 27, 2023 accommodation request (L81) are dated
    before the printed June 31. Recorded as printed.
  - Party labels:
    - Lock ("NURSE SUPERVISOR") and Money ("RNS") are among the "Corrections Defendants" (L67).
    - Baird is called "Medical Defendant Baird" (fn2 L147) and is captioned "MEDICAL DIRECTOR" (L15-17).
  - The motion sought dismissal of "the entire amended complaint" (L135). After the concessions only
    personal involvement on Count One was left (L141-143), and that part of the motion was denied (L167).
- Coverage: **full**. Read L1-80, 80-159, 159-184. Unread: none. Missing source text: none known. Not
  stated in the source: the grievance date and the dates of ECF Nos. 47, 104, 108, 109 and 112.

## Shared ground candidates (part a)

Locations only. Hits in other documents come from targeted greps of `text/D04-D08, D10.txt`; those
documents are mapped elsewhere.

- Eleventh Amendment:
  - Appears in all ten texts:
    - D01 L79-91, L101, L127.
    - D02 L81-89, L151-181.
    - D03 L503-505 (and sovereign immunity at L161-163).
    - D09 L135 (argument), L141 (withdrawn).
    - D04 L345, L389, L437-455.
    - D05 L211.
    - D06 L73, L311, L397-457, L799-815.
    - D07 L181-191.
    - D08 L81, L183-191, L259.
    - D10 L209.
  - The amendment's text is quoted at D02 L157 and D06 L401.
- Ex parte Young: D01 L87-103; D02 L173; D06 L411-445.
  - A past-tense declaration as retrospective relief: D01 L101; D06 L445 (T.W., "in the past tense").
- Whether sovereign immunity is jurisdictional (Fourth Circuit):
  - D02 L81: not "conclusively determined"; the court favours Rule 12(b)(1).
  - D03 L161-163: the Fourth Circuit "has stated" it is "a jurisdictional bar".
- With or without prejudice for immunity-based or jurisdictional dismissals:
  - D01 L141: with prejudice, for lack of subject matter jurisdiction.
  - D02 L259 and fn8 L267: without prejudice; Albert v. Lierman, "should normally be without prejudice".
  - D03 L505, L519-521: Count IV for lack of subject matter jurisdiction, without prejudice.
  - D09 L141, L171: official-capacity claims conceded and dismissed with prejudice.
  - Other "with prejudice" hits are in D04, D08 and D10; "without prejudice" hits are in D04, D05, D06 and D07.
- Shared case citations:
  - Erickson v. Pardus, 551 U.S. 89, 94: D01 L53; D02 L27; D03 L45.
  - Pennhurst: D01 L81, L101, L123; D06 L419, L455.
  - Will v. Mich. Dep't of State Police, 491 U.S. 58, 71: D02 L161-163; D06 L463.
  - Laughlin v. Metro. Washington Airports Auth., 149 F.3d 253: D02 L109 (at 260-61); D03 L405-409 (at
    255 and 259).
  - Scheuer v. Rhodes, 416 U.S. 232, 236: D03 L177-179; D09 L117-119.
  - Hutto v. S.C. Ret. Sys., 773 F.3d 536: D03 L163 (at 543); D04 L441-443 (at 549).
  - Evans v. B.F. Perkins Co., 166 F.3d 642: D03 L157-159; D04 L95.
  - City of Cleburne: D02 L247; D05 L149, L151.
  - Evancho v. Fisher: D09 L155; D08 L225.
  - A.M. ex rel. J.M.K.: D09 L155; D08 L237.
  - Schmidt v. Skolas: D09 L125-127; D08 L133.
  - Iqbal, 556 U.S. 662: D02, D03, D04, D06, D07, D08 and D09 (D02 L121, L193-195; D03 L169; D09 L111).
  - Twombly, 550 U.S. 544: D02, D03, D04, D06, D07, D08, D09 and D10.
- Maryland sources:
  - Local Rule 105.6 (D. Md. 2025): D02 L19; D03 L35; D04 L35 ("Loc. R. 105.6").
  - Md. Code Ann., State Gov't: § 12-201(a) at D02 L173; §§ 20-601 et seq. at D03 L139; § 12-101(a)(8) at
    D04 L395.
  - Maryland Dep't of Public Safety and Correctional Services: D02 L33 (state-court target) and L67
    (Blankumsee case name); D03 L505 (Pense case name).
- Pennsylvania Department of Corrections: D09 L55, L73, L161 (SCI Albion, SCI Forest, SCI-Dallas); D08
  L45, L191 (DOC; SCI Phoenix at L41, L87).
- Rules and statutes:
  - Fed. R. Civ. P. 12(d): D02 L91-113; D09 L129.
  - Rule 15(a)(2): D01 L125; D05 L261.
  - Rule 8(a)(2): D03 L169; D09 L105.
  - 28 U.S.C. § 1915: D01 L47; D07 L53, L55.
  - 28 U.S.C. § 636 (magistrate judge): D09 L61; D05 L89; D07 L279, L291.
  - 28 U.S.C. § 1331: D09 L57; D07 L201.
  - Qualified immunity: D02 L265 (not reached); D04 L361; D05 L97, L99; D10 L193.
- Claim types, by grep line counts:
  - Deliberate indifference: D02 (2), D09 (7), D08 (12), D04 (1). D02 L49-51, L209; D09 L89, L95, L141,
    L147, L153, L171.
  - Equal protection: D02 (5), D09 (4), D05 (18), D06 (1). D02 L241-255; D09 L91, L141, L171.
  - ADA: D09 (4), D06 (26), D05 (1).
  - Title VII: D03 (14), D07 L83, L219.
  - Retaliation: D02 (4), D03 (20), D04 (1), D06 (3).
  - EEOC, hostile work environment and MFEPA: D03 only.
  - Pro se: D01, D02, D05, D06, D07, D08, D09 (D01 L51, L125; D02 L27-29, L65; D09 L131).
- Labels for groups of defendants:
  - D02 L49: "State Defendants" (Weber, Lasher) and "Medical Defendants" (Mace, Akintade).
  - D09 L67: "Corrections Defendants" (Edwards, Lock, Money). D09 fn2 L147: "Medical Defendant Baird".
- Decision and filing dates:
  - 14 September 2026: D01 L149 (footer 09/14/26) and D09 L175 (footer 09/14/26).
  - 17 September 2026: D03 L527.
  - 18 September 2026: D02 L259.
  - D04 is signed "September 18, 2026" (L481) with footer "Filed 09/21/26" (L487).
  - Other footers: D05 09/18/26 (L39); D08 09/18/26 (L33); D07 09/15/26 (L43); D10 09/16/26 (L31); D06
    09/20/26 (L49).
- Judges:
  - D01: William J. Crain (L151).
  - D02: Julie R. Rubin (L261).
  - D03: George L. Russell, III, Chief (L531-533).
  - D04: Matthew J. Maddox (L483-485).
  - D06: Nusrat J. Choudhury (L37, L861-863).
  - D07: Daniel J. Stewart, Magistrate Judge (L29-31).
  - D09: Christopher B. Brown, Magistrate Judge (L51, L179-181).
  - D05, D08 and D10 signatures were not located by this pass.
- Case-number suffix "JRR":
  - D02 L11 (signed by Rubin) and D02 L211 ("No. CV JRR21-1893").
  - D03 L29 and footers (signed by Russell).
  - D04 L221 ("Semenchenko v. Brown, No. 1:25-CV-01044-JRR").
- Same surname, different entity:
  - Richards: D09 L11 (plaintiff); D02 L267 (Merritts v. Richards).
  - Brown: D03 L61-63, L69, L241 (Kenny Brown); D03 L299 (Brown v. Dir. SCDC); D09 L51, L179 (Judge
    Christopher B. Brown); D02 L195 (Wilcox v. Brown); D04 L221 (Semenchenko v. Brown).
  - Moore: D03 L87, L99-103, L125, L389, L415 (Gov. Wes Moore); D03 L449 (Moore v. Abbott Lab'ys); D08 L83
    (Moore v. Luffey); D07 L209 ("v. Moore").
  - Hill: D03 (plaintiff); D06 L669 (Hill v. Didio).
  - Weber: D02 (Ronald S. Weber); D02 L67 (Francis v. Weber).
  - Board of Supervisors: D01 (Louisiana Community and Technical Colleges); D02 L163 (Bd. of Supervisors of
    Fairfax Cnty.).
  - State Police: D03 (Maryland Department of State Police); D02 L161 and D06 L463 (Will v. Mich. Dep't of
    State Police); D05 L211 (Langworthy v. New Mexico State Police).
  - Williams: D03 L163, L221, L265; D02 L211 (Neal-Williams); D04 L239; D06 L421, L809; D07 L63; D08 L137.
  - Perkins: D03 L157, L367/L405, L505; D04 L95.
  - Johnson: D02 L105, L233; D04 L129, L293; D05 L225, L241, L261.
  - Lewis: D02 L221; D03 L475, L477.
  - Robinson: D02 L139-141; D03 L283.
- Amendment and pleading posture:
  - D01: amended twice; the second amended complaint is operative and leave is denied (L45, L125-127).
  - D02: no amended complaint after counsel appeared; a proposed amended pleading was never operative (fn2
    L29); supplements ECF Nos. 5, 11, 39 (fn1, fn3).
  - D03: leave denied for lack of a proposed amendment and redline (L515-521); new allegations in the
    opposition are not an amendment (fn10).
  - D09: the amended complaint, ECF No. 47, is operative (L81, L135).

<!-- merged from doc-map-part-b.md -->
Mapper part b, 2026-10-06. Navigation only: where facts sit, not what to ask. Questions quote the
documents, never this map. Line numbers are `text/Dnn.txt` lines; the matching `docs/` original
line is the text line minus 2 (one header line plus one blank line; verified on footnotes in all
three files). Local ids are alphabetical by file name; task-page "Doc N" numbers differ
(D04 = Doc 10, D05 = Doc 7, D10 = Doc 4; confirmed against `notes/intake.json`).
Caller merges this file into `notes/doc-map.md`; parts a/c cover the other seven documents.

## D04 (Doc 10) - Worsley v. Rinaldo et al., Memorandum Opinion (D. Md.)

- Source: `text/D04.txt` (488 lines) from `docs/uscourts_mdd_1_25_cv_03696_0.txt`; local D04 = task page Doc 10; sha256 0ff67666bc052057e2b48867e428b8e81f0488cba8b2e3c857926c95523a6ea2 (manifest); 67,413 chars; plain-text source, `pages: null` in manifest; printed pagination 32 pages (footer "Case 1:25-cv-03696-MJM Document 41 Filed 09/21/26 Page N of 32", 32 footers present, Page 1 at line 37, Page 32 at line 487).
- Written or submitted by: United States District Court for the District of Maryland (lines 5-7); signed "/S/ ... Matthew J. Maddox, United States District Judge" (481-485). Caption "Civ. No. MJM-25-3696" (17). All other organisations (BPD, the City, the SAO, FOP, Fourth Circuit, Maryland appellate courts, other D. Md. judges) are mentioned, not authors.
- Type, date, edition: Memorandum Opinion (33) deciding four dismissal motions plus a motion for leave to file a sur-reply; "A separate Order will issue" (479) - that Order is not in the bundle (no other document carries case number 3696). Signed "September 18, 2026" (481); filed 09/21/26 (every footer); Document 41. Single edition.
- Period covered: alleged events from March 5, 2023 (47) through continuing post-acquittal conduct "from March 2023 to present date" (199); BPD-status dispute window January 1, 2023 - January 1, 2025 (181-199). Calendar dates only; fiscal convention not applicable.
- Entities and aliases:
  - Plaintiff Larry Worsley ("Plaintiff", 35), "a BPD Sergeant" (47). One stray "her contention" (413) - elsewhere "he/his".
  - Baltimore Police Department ("BPD", 35); misspelt "BDP" once (231). "Officer Defendants" = BPD officers Louis Rinaldo, Robert Cucchiaro, Maggie Tran, Noah Carter (35); "Officer Rinaldo" (49, 75).
  - Mayor and City Council of Baltimore ("the City", 35); also "the City of Baltimore" (59); "the Mayor of Baltimore" (199, Compl. ¶ 13).
  - "State’s Attorney Defendants" = Ivan Bates, "the State’s Attorney for Baltimore City", and Assistant State’s Attorney Steven Trostle (35). Bates is "a state official—not a municipal official" (463, citing Md. Const. art. V, § 7).
  - State’s Attorney’s Office ("SAO", 61); "Office of the State’s Attorney for Baltimore City" (389, 403, 453); "Baltimore City SAO" (403). Its published "Do Not Call" list (61, 189, 389, 403-427, 453).
  - Fraternal Order of Police ("FOP") and BPD's Memorandum of Understanding ("MOU") (51, 309, 311).
  - Tequila Sunset, "a bar in Baltimore, Maryland" (47); bartender Shanika Lee ("Lee", 47-53; "the [victim] bartender", 365).
  - Maryland Tort Claims Act ("MTCA", 393); Local Government Tort Claims Act ("LGTCA", 229); Maryland Declaration of Rights (35, 73).
  - In cited precedent only: Marilyn Mosby, "then-State’s Attorney for Baltimore City" (397; misspelt "Mosly" at 401); Freddie Gray, Jr. (397); "BALT" = Balt. Action Legal Team v. Off. of State’s Att’y of Balt. City (403-405); "then-Maryland Court of Special Appeals (now, Appellate Court of Maryland)" (405).
  - Same-name items inside D04: "Carter" = Officer Noah Carter (35) vs Carter v. Morris (285); "Jordan" = Jordan v. Mayor & City Council of Baltimore (185), Virginia Dep’t of Corr. v. Jordan (195), Jordan v. Jackson (271); "Jones" = Est. of Jones v. Md. Dept. of Pub. Safety (99/113), Jones v. Queen Anne’s Cnty. (237), Jones v. Chapman (299); "Johnson" = Johnson v. City of Shelby (129), Johnson v. Baltimore City (293); "Trump" = short form of Mayor of Balt. v. Trump (93, 99, 113); "Lee" = bartender Shanika Lee only.
- Tables: none (no tables, charts or pipe rows). Layout hazards: page footers are fused into body lines (e.g. 37, 53, 69, 79, 127, 139, 155, 199, 241, 279, 291, 303, 343, 357, 397, 405, 417, 429, 445, 453); new-page numbers lead some lines ("3 not to volunteer", 55; "4 substantive", 71; "9 accusations", 157); footnotes interrupt sentences (fn 1 at 101-107 splits the Est. of Jones citation between 99 and 113; fn 3 at 187-189 splits the Jordan/Corrigan comparison between 185 and 193; fn 7 at 471 plus a page break splits the conclusion sentence "All claims asserted against the State’s" (469) / "Attorney Defendants are dismissed without prejudice." (477)). Verbatim quotes across those points pick up footer or footnote text.
- Lists:
  - Twelve counts (67-77): "Plaintiff alleges twelve counts total. The first four counts are federal constitutional claims" (67); "The remaining counts—the tenth through the twelfth—are mislabeled as Count XI, Count X, and a second Count XI." (73). Last member: battery, the second "Count XI", "brought only against Officer Rinaldo" (75-77). Per-count index under Notes.
  - Officer Defendants: four names (35). State's Attorney Defendants: two (35).
  - Motion/brief ECF index (79-85; see Notes).
  - Punitive-damages counts named with "including": Compl. at 16 (Count IV), 18 (Count V), 19 (Count VI), 20 (Count VII), 23 (Count IX), 24 (civil conspiracy count) (337).
  - fn 3 continuing-conduct mapping (189): "Do Not Call" conduct -> defamation (¶ 85), IIED (¶ 99), Declaration of Rights (¶ 114), negligence (¶ 127); failure to reinstate -> breach of contract (¶ 107), Declaration of Rights (¶ 114), negligence (¶ 127); Count VI "based entirely on conduct that occurred in 2023".
  - Enumerated legal tests: Monell two components (271); four ways a policy/custom arises (273); failure-to-train three facts (295); civil conspiracy three elements (147); Martin five inquiries (449).
  - Charges: "assault, theft, and use of a firearm in a felony" (53).
- Forecasts, guidance, deadlines, effective dates:
  - No day-count deadline anywhere in D04 (no days to amend/object). Count VIII: "dismiss Count VIII without prejudice to Plaintiff seeking leave to amend" (333), no deadline stated.
  - Effective dates for BPD control: Plaintiff says the transition "began on January 1, 2023" (167); Editor's Note to Article 17, Baltimore City Code: transfer "became effective January 1, 2023[,]" but "was not complete" and "did not become fully effective until January 1, 2025, following subsequent legislation" (193); parties agree state-agency status "ceased, at the latest, by January 1, 2025" (181, citing ECF 29 at 2-3); fn 3: continuing conduct "post-dates January 1, 2025—the date by which both sides agree that BPD came under city control" (189).
  - Dated events: Jan 1, 2023 (167, 169, 179, 193); March 5, 2023, "approximately 10:45 p.m." 911 call, arrest (47-49); March 6, 2023 suspension, unpaid status (51); detention "for over six months awaiting trial" (53); acquittal of all charges, date not stated (55-57); City's hypothetical "between March and September 2023" (229); Corrigan conduct "beginning in September 2023" (193); Jordan: BPD "remain[ed] a state agency as of [June 12, 2024]" (185); Jan 1, 2025 (181, 189, 193, 199); opinion signed September 18, 2026 (481), filed 09/21/26.
  - Not stated in D04: complaint filing date, motion/brief filing dates, trial or acquittal date, date of Bates's statement (only "immediately after Plaintiff’s acquittal", 389, 453).
- Hedged claims (claim / hedge word / what it attaches to):
  - "the Court must consider BPD’s state sovereign immunity defense at least with respect to Count VI" (189): "at least" limits the minimum scope; fn 3 opens "Most of the state-law claims ... are based, in part, on continuing conduct" ("Most", "in part").
  - BPD "has failed to establish, at this early stage of the case" (169): stage qualifier on the immunity ruling; repeated "At this point in the litigation" (199).
  - "there is some divergence among judges of this Court regarding the timing of BPD’s transition" (185): BPD's own brief (ECF 29 at 3 n.3), quoted.
  - "In many cases [a state sovereign immunity defense] will not be appropriate for resolution on a motion to dismiss" unless it "clearly applies" (197): quoted Yampierre standard.
  - "under the facts alleged in the Complaint, their liability for the conduct of BPD officers is plausible" (255): plausibility of City/BPD liability on Count IX only.
  - "Even assuming these allegations suffice to plead ... a ‘custom or usage with the force of law[,]’" (283): assumption; the firm holding is the next clause ("the Complaint contains no facts to suggest that this alleged policy or custom caused any constitutional deprivation").
  - "presumably to the news media" (389, 403): attaches only to the audience of Bates's public statements.
  - "Public, out-of-court statements typically fall outside the scope of absolute prosecutorial immunity" (389): "typically"; the Court then rests Bates's dismissal on statutory and Eleventh Amendment immunity instead.
  - Annappareddy: post-probable-cause acts "generally are classified as ‘advocative’"; pre-probable-cause acts "are more likely to be ‘investigative’" (361).
  - BALT quote: listed officers testifying "would potentially jeopardize a prosecution" (405): describes the list's purpose, not a finding about Plaintiff.
  - Gross negligence "likely more akin to reckless conduct" (423, quoting Barbre); "probably false" (425): part of the quoted Nero standard.
  - "the Eleventh Amendment generally does not bar suits for [monetary] damages against state officers ... in their individual capacities" (443); "The Martin inquiry suggests Plaintiff’s claims against Bates form an official-capacity suit in substance" (453).
  - "The Court infers that this allegation applies to all times relevant" (199); "Plaintiff implicitly concedes that point" (337, punitive damages vs the City).
  - Plaintiff's argument, not the Court's: BPD's arguments "at most, justify granting Plaintiff leave to add facts" (311).
- Rounded prose beside exact figures: none. Approximate phrases with no exact counterpart in D04: "over six months" (53), "approximately 10:45 p.m." (47), "a number of “high-profile examples”" (281).
- Notes:
  - Motion and brief index (79-85): motions to dismiss by BPD ECF 20, City ECF 21, State's Attorney Defendants ECF 32 ("respectively", 79); Officer Defendants' partial motion ECF 38 (civil conspiracy only, 79). Oppositions "ECF 23, 22, 33, 39" and replies "ECF 29, 30, 34, 40" (83) listed in the same order (the word "respectively" is printed only for the motions). Memoranda cited: 20-1, 21-1 (City adopts BPD's arguments: 261, 311, 313, 337), 22-1, 23-1, 32-1, 33-1, 38-1, 39-1. Sur-reply: motion for leave ECF 37 "granted", "proposed sur-reply, which is accepted, ECF 37-2" (85); fn 1 says the Court considered "Plaintiff’s sur-reply, ECF 37-1" (107). "The motions are fully briefed. A hearing is not necessary" (35, Loc. R. 105.6 (D. Md. 2025)).
  - Motion outcomes (469): Officer Defendants' motion for partial dismissal granted; State's Attorney Defendants' motion granted; City's and BPD's motions granted in part and denied in part. Sur-reply leave granted (85).
  - Per-count index (counts 67-77; complaint page ranges as printed; disposition lines):
    - Count I, § 1983 unlawful seizure, Fourth Amendment; Officer Defendants; Compl. 10-11 (67-69). No motion directed at it (79); summary at 41 says remaining claims proceed against the Officer Defendants.
    - Count II, § 1983 malicious prosecution and wrongful detention, Fourth Amendment; Officer Defendants; 11-13 (69). No motion directed at it.
    - Count III, § 1983 suppression and fabrication of evidence, Fourteenth Amendment due process; Officer Defendants and Trostle; 13-15 (69-71). Trostle: absolute prosecutorial immunity (349, 365-383; "All counts asserted against Trostle must be dismissed", 383); without prejudice (469/477). Officers: no motion.
    - Count IV, § 1983 municipal liability (custom, policy, failure to train/supervise); BPD, City, Bates; 15-16 (71). City/BPD: failure to state a claim, "Count IV must be dismissed as to the City and BPD" (305); without prejudice (477). Bates: only § 1983 claim against him, Monell cannot be pursued against an individual (459-463); dismissed with all State's Attorney counts (465), without prejudice (469/477).
    - Count V, defamation, libel and slander; Bates, City, BPD; 16-18 (73). City/BPD: governmental immunity (203, 227); without prejudice (477). Bates: MTCA (393-435), Eleventh Amendment official capacity (439-457).
    - Count VI, Maryland common-law malicious prosecution; Officer Defendants, Trostle, BPD, City; 18-19 (73). City/BPD: governmental immunity (227); also the only count "based entirely on conduct that occurred in 2023" (189). Trostle: prosecutorial immunity. Officers: no motion.
    - Count VII, IIED; Officer Defendants, State's Attorney Defendants, BPD, City; 19-20 (73). City/BPD: governmental immunity (227); State's Attorney Defendants dismissed.
    - Count VIII, breach of contract; BPD and City; 21-22 (73). Construed "to assert only a claim for breach of contract" (fn 5, 313); failure to plead exhaustion of MOU grievance/arbitration remedies (311, 317-333); "without prejudice to Plaintiff seeking leave to amend" (333, 477).
    - Count IX, Maryland Declaration of Rights; Officer Defendants, State's Attorney Defendants, BPD, City; 22-23 (73). City/BPD "are not immune from the state constitutional claims asserted in Count IX" (255); BPD's sovereign-immunity motion "is denied" (199-201); not in the conclusion's dismissed list (477). State's Attorney Defendants dismissed.
    - Tenth count (first "Count XI"), civil conspiracy; Officer Defendants, State's Attorney Defendants, BPD, City; 23-24 (75; fn 2 at 175; "against all named defendants", 139). "shall be dismissed" (153); "dismissed with prejudice as to all defendants" (477). Conspiracy remains usable "as a theory of liability against each Officer Defendant for the acts of co-conspirators" (157).
    - Eleventh count ("Count X"), negligence and gross negligence; Officer Defendants, State's Attorney Defendants, BPD, City; 24-25 (75; fn 4 at 215). City/BPD: governmental immunity (227); without prejudice (477). State's Attorney Defendants dismissed.
    - Twelfth count (second "Count XI"), battery; Officer Rinaldo only; 26 (75-77). No motion directed at it.
    - Punitive damages prayer v. City and BPD: "dismissed with prejudice" (339, 477); Plaintiff "is not seeking punitive damages against BPD" (337, ECF 23-1 at 11).
  - Numeric figures: twelve counts, first four federal (67); four Officer Defendants, two State's Attorney Defendants (35); 911 call "approximately 10:45 p.m." (47); detention "over six months" (53); Complaint paragraphs 51-57 used twice (fn 6, 369-373: first 57 "on page 11", second instance "on page 12"); Compl. ¶ 46 cites "§ 3-108.2" (313); 32-page opinion; BALT "No. 1251, Sept. term, 2020" (403-405); ECF numbers above.
  - Footnotes (7): fn 1 sur-reply leave, Local Rule 105.2(a) (101-107); fn 2 civil conspiracy is the tenth count (175; printed "the the tenth count"); fn 3 continuing conduct and Count VI (187-189); fn 4 negligence is the eleventh count mislabeled "Count X" (215); fn 5 Public Safety § 3-107, Wage Payment and Collection Law, § 3-108.2 (313); fn 6 duplicated paragraph numbers (369-373); fn 7 alternative failure-to-state arguments not reached (471).
  - Negative and exclusion statements: "A hearing is not necessary" (35); Rinaldo's probable-cause statements: "None of these statements were ever corroborated by any witnesses" (49); no back pay restored (59); conspiracy "will not support a separate cause of action" (149); LGTCA "does not waive any preexisting immunity" / does not "authorize any actions directly against local governments" / "does not create a cause of action" (239); local governments "are not immune" from constitutional torts (247); Monell: "the only policy or custom Plaintiff alleges with factual support" is the back-pay restoration custom (279), which Plaintiff alleges was departed from "contrary to policy and past practice" (289); "Plaintiff has not pleaded any such exception" (325); "Plaintiff does not argue that these facts are sufficient to demonstrate exhaustion" (333); "Section 3-108 has no apparent connection" (313); Trostle: no harm "apart from the prosecution" (377), acquittal "a favorable—not harmful— outcome" (379), no investigative conduct alleged (383); Bates: no facts of malice or gross negligence (409-427), no allegation the statement "was false at all" (427), "retaliatory" theory "is not reflected in the Complaint" (431), no allegation of personal interests or ultra vires conduct (453); "The Court need not reach" failure-to-state arguments of the State's Attorney Defendants (fn 7, 471).
- Operative definitions, rules and scope exceptions (as written, with locations):
  - Rule 12(b)(1): plaintiff's preponderance burden (91); facial vs factual challenge (99, 113-117).
  - Rule 12(b)(6)/Rule 8(a)(2): Twombly, Iqbal plausibility (123-131); legal conclusions not accepted (135).
  - Maryland civil conspiracy elements: "an unlawful agreement, the commission of an overt act in furtherance of the agreement, and that as a result, the plaintiff suffered actual injury" (147); "it is improper pleading to allege conspiracy in a separate count" (149).
  - Sovereign immunity is jurisdictional (171) but "akin to an affirmative defense", defendant's burden (197).
  - Local governmental immunity: immunity "only for acts that are governmental", none "for State constitutional torts" (207); "The operation of a police force is quintessentially a governmental function" (221); immunity extends to agencies (225); LGTCA limited waiver for duty to defend/indemnify (237-241); BPD is a "local government" for LGTCA purposes, Cts. & Jud. Proc. § 5-301(d) (241); respondeat superior for state constitutional violations (DiPino, 257).
  - Monell: two components (271); four ways (273); "only specific instances ... are [his] own" insufficient (Johnson v. Baltimore City, 293); failure to train needs "(1) the nature of the training, (2) ... ‘deliberate or conscious’ choice ..., and (3) that the officer’s conduct resulted from said training" (295) and a "‘specific deficiency’" (299-301).
  - Exhaustion of collective-bargaining remedies (Gazunis, 319-323); exception for unions whose remedies lack monetary damages (Lovelace, 325-327).
  - Punitive damages: municipalities immune under § 1983 (City of Newport) and Cts. & Jud. Proc. § 5-303 (337).
  - Prosecutorial immunity: functional approach; timing "a key factor"; withholding exculpatory information still prosecutorial (351-381).
  - MTCA: State personnel immune for acts "within the scope of the public duties" and "without malice or gross negligence" (395, Cts. & Jud. Proc. § 5-522(b), State Gov’t § 12-101(a)(8)); malice and gross negligence definitions (415, 423).
  - Eleventh Amendment: official-capacity damages barred (441); Martin five-factor real-party-in-interest test (449); "one key exception": Martin factors not applied to § 1983 claims (459, Gibbons v. Gibbs).
- Amendments or contradictions (recorded, not resolved):
  - Sur-reply exhibit number: ECF 37-2 "accepted" (85) vs "Plaintiff’s sur-reply, ECF 37-1" considered (107).
  - Trostle quotation: "with or without the witness help" (53, Compl. ¶¶ 21-22) vs "without or without the witness[’s] help" (429, Compl. ¶ 22).
  - Statute number: Complaint cites "§ 3-108.2"; Court writes "Section 3-108 has no apparent connection" (313).
  - Count labels: Complaint's tenth-twelfth counts mislabeled (73; fns 2, 4); Court uses "X" in quotation marks for the eleventh count (227, 477).
  - Summary at 37-41 ("his count for municipal liability ... is dismissed", "remaining constitutional and common-law claims shall proceed against the City, BPD, and the Officer Defendants") vs conclusion at 469-477 (Counts IV, V, VI, VII, VIII, "X" dismissed as to City/BPD; conspiracy with prejudice; State's Attorney claims without prejudice). The intro does not state prejudice; the conclusion does.
  - BPD sovereign immunity "denied" for state constitutional and common-law claims (199-201), while the same common-law tort counts are dismissed against BPD on local governmental immunity (227).
  - BPD state-status timing: Jordan (June 12, 2024 still a state agency, 185) vs Corrigan (status extinguished by the January 2023 change, 193) vs Editor's Note (effective January 1, 2023, complete January 1, 2025, 193); D04 itself decides only that BPD has not met its burden at this stage (199).
  - Typos as printed: "BDP" (231), "Mosly" (401), "the the" (175), "her contention" (413), "commonlaw" (201).
- Coverage: FULL. Read ledger: lines 1-120, 120-239, 240-339, 340-439, 440-488 (end of file confirmed at 487-488). All 32 printed pages present (footers Page 1-32 of 32 in both text and original). Unread ranges: none. Missing source text: none. Extraction spot-checks: page count 32 = 32 footers in `docs/` original; footnote 6 matches original lines 367-371 (text 369-373); table check not-applicable (no tables); page-image/visual check not-applicable (plain-text original); D04 original contains no U+2026, so no normalisation change.

## D05 (Doc 7) - Langworthy v. Alcon, Order to Show Cause (D.N.M.)

- Source: `text/D05.txt` (282 lines) from `docs/uscourts_nmd_1_24_cv_01291_6.txt`; local D05 = task page Doc 7; sha256 9f3f738e3493030f3b1fbad2db3592b008a45e9a8b4c2335e45b7c6ceefa9d14 (manifest); 39,861 chars; plain-text source; printed pagination 17 pages (footer "Case 1:24-cv-01291-MLG-KRS Document 64 Filed 09/18/26 Page N of 17", 17 footers).
- Written or submitted by: United States District Court for the District of New Mexico (3-5); signed "KEVIN R. SWEAZEA / UNITED STATES MAGISTRATE JUDGE" (277-279); refers to itself as "the undersigned" and to an unnamed "presiding judge" who decides (261, 267). Judges named but not authoring: Chief District Judge Kenneth J. Gonzales, Senior District Judge William P. Johnson, District Judge David Urias, Magistrate Judge Kirtan Khalsa (225, 239, 241). Caption "No. 1:24-cv-1291-MLG-KRS" (15).
- Type, date, edition: Order to Show Cause, issued "sua sponte upon review of the docket" (25-27); "IT IS SO ORDERED this 18th day of September, 2026" (273); filed 09/18/26; Document 64. Single edition.
- Period covered: alleged events "fall of 2021" (45), "fall of 2022" (53, 57), "winter of 2023" (75); Tatum "since 2015" (55); plaintiff's case history 8/17/2023 to 12/8/2025 (211-239); order dated September 18, 2026. Seasons only for the three incidents (no exact dates); "On the same date" (47) has no stated date.
- Entities and aliases:
  - Plaintiff Geneva Langworthy ("Plaintiff", "Ms. Langworthy", "Langworthy"); pro se (209). Property "12 1/2 Towhee Lane" (45, 95); "Ms. Langworthy’s house on Jaybird Lane" (47); Jaybird Lane "a private road" (55, 103), misprinted "Jaybird Land" once (103); Ute Park (55).
  - Defendant Edward Alcon ("Defendant Alcon", "Deputy Edward Alcon", "Deputy Alcon", "Alcon", "the deputy").
  - Todd Tatum (non-party): "local buffoon Todd Tatum" (55), "fraudster Tatum" (57), Court calls him "her neighbor Todd Tatum" (163).
  - Colfax County Sheriff (69; also defendant in case (ii), 213); Colfax County (cases (v), (vi)); New Mexico State Police (i); Seidel (iii); State of New Mexico (v); United States Postal Service (vii); Chavez (two separate cases, (viii) 1:25-cv-402 and (x) 1:25-cv-409); Cadwell (ix); New Mexico Administrative Office of the Courts (ix); 8th Judicial District Court of New Mexico (x); Gonzales (xi).
  - Same-name items inside D05: "Oliver" = Oliver v. United States, 466 U.S. 170 (111, 121, 139; printed "Oliver, 66 U.S. 170" at 115) vs Oliver v. Woods, 209 F.3d 1179 (133-135); "Jones" = Jones v. Helms, 452 U.S. 412 (153) vs short cite "Jones, 565 U.S. at 408 n.5" (135) with no full citation anywhere in the bundle; "Helms" in Jones v. Helms and Pratt v. Helms (181); "Gonzales" = Chief Judge Kenneth J. Gonzales (225, 239) and caption "Langworthy v. Gonzales" (239); "Johnson" = Senior District Judge William P. Johnson (225, 241, 261).
- Tables: none. Layout hazards: footnote 1 runs from line 35 to 39 and continues at 63, inside the block quotation of the second claim (53-61, 69) across a page break (65-67); footnote marker "5 For instance," (107) leaves the body sentence to resume at 121 after fns 3-5 and a page break; footer text fused into lines 39, 87, 137, 153, 181, 233.
- Lists:
  - Three claims against Alcon, "two based on the Fourth Amendment and one based on the Equal Protection Clause" (33): first, "the following two paragraphs" (43-49, Doc. 1-2 at 2-3); second, "the following three paragraphs" (51-71, Id. at 3); third, "the following two paragraphs" (73-81, Id. at 3-4). Text block counts differ from the stated counts (second claim: blocks at 53-55, 57-59, 61, 69; third claim: 75, 77, 79); paragraph boundaries are unresolved (no page image).
  - Plaintiff's lawsuits "in this District", items (i)-(xi) (211-239); the eleventh and last item (xi) is at 239 on page 15; the present case is item (iv) (221). Per item: case number; filed; terminated; stated basis:
    - (i) v. New Mexico State Police, 1:23-cv-684-DHU-JFR; filed 8/17/2023; terminated 9/20/2023; lack of subject-matter jurisdiction due to Eleventh Amendment immunity (211).
    - (ii) v. Colfax County Sheriff, et al., 1:23-cv-997-DHU-JFR; filed 11/13/2023; terminated 2/21/2024; failure to state a claim and noncompliance with order to file amended complaint (213).
    - (iii) v. Seidel, et al., 1:23-cv-1028-JCH-JFR; filed 11/20/2023; terminated 2/21/2024; failure to state a claim, no amended complaint after OSC (219).
    - (iv) v. Alcon, 1:24-cv-1291-MLG-KRS; "filed in state court 11/27/2024; removed 12/23/2024"; "(present case)" (221).
    - (v) v. New Mexico, et al., 1:24-cv-1229-KG-LF; filed 12/5/2024; terminated 3/27/2025; Inspection of Public Records Act theory; dismissed without prejudice; motion to re-open granted; motion to disqualify denied; appeal terminated on Plaintiff's stipulation of voluntary dismissal (223).
    - (vi) v. Colfax County, et al., 1:25-cv-18-WJ-JHR (KK); filed 1/8/2025; terminated 3/18/2025; dismissed by Chief District Judge Kenneth J. Gonzales (Doc. 28); reopen/change of judge denied by Senior District Judge William P. Johnson (Doc. 42); filing restrictions (Doc. 43, entered 7/28/2025) (225).
    - (vii) v. United States Postal Service, 1:25-cv-432-KWR-SCY; "filed in D.D.C. 2/5/2025; transferred to D.N.M. 5/7/2025; terminated 6/16/2025"; failure to state a claim, no amended complaint after OSC (227).
    - (viii) v. Chavez, et al., 1:25-cv-402-WJ-SCY; "filed in state court 3/20/2025; removed 4/28/2025; terminated 12/8/2025"; motions to dismiss denied as moot; dismissed without prejudice for failure to respond to OSC on keeping a current address (229).
    - (ix) v. Cadwell, 1:25-cv-398-WJ-JFR; filed 4/28/2025; terminated 5/27/2025; ADA claims v. Administrative Office of the Courts; dismissed without prejudice (231).
    - (x) v. Chavez, et al., 1:25-cv-409-SMD-LF; filed 4/30/2025; terminated 10/20/2025 (closing parenthesis missing as printed); dismissed without prejudice as sanction (233-237).
    - (xi) v. Gonzales, et al., 1:25-cv-433-REB-SBP; "filed 5/6/25; terminated 7/2/2025"; access-to-courts claims naming Gonzales, Urias, Khalsa; failure to state a claim, no amended complaint after OSC (239).
    - "without prejudice" is printed for (v), (viii), (ix), (x) only; (i)-(iii), (vi), (vii), (xi) state grounds without a prejudice label.
  - Filing-restriction steps 1-3 for permission to proceed pro se (quoted from 1:25-cv-18 Doc. 43 at 2-3) (243-259).
  - Rule 20(a)(2) conditions (A) and (B) (207); equal protection "two ways" (157-159).
- Forecasts, guidance, deadlines, effective dates:
  - Deadline: "Plaintiff shall, within 21 days of entry of this Order: (a) show cause why the Court should not dismiss her claims against Defendant Alcon; and (b) file an amended complaint in compliance with this Order." (271). Counted from "entry of this Order"; no calendar date printed. Consequence: "Failure to timely show cause and file an amended complaint may result in dismissal of this case." (271).
  - Sequencing rule: no new parties or claims in the responsive amended complaint (201, 261, 267); a later Rule 15(a)(2) motion for a second amended complaint only after a finding that the amended complaint states a claim (261, 267); the undersigned issues proposed findings and recommended disposition, the presiding judge decides (261, 267).
  - Filing restrictions imposed July 28, 2025 by Senior District Judge William P. Johnson (241; "7/28/2025" at 225).
  - Pending motion: Alcon's motion for summary judgment based on qualified immunity, Doc. 46 (fn 2, 97-99).
  - Other docket items: operative state-court complaint Doc. 1-2 (27); "Order Striking Pro Se Motions And Permission To File Electronically (Doc. 62)" (31-33); "Order Striking Pro Se Filings And Revoking Permission To File Electronically, entered contemporaneously herewith" (267). Neither order is in the bundle.
- Hedged claims (claim / hedge word / what it attaches to):
  - Allegations "may fit the description of “short and plain,”" (93): "may" attaches to brevity only; the firm statement follows ("they do not provide sufficient details").
  - "may not even be sufficient to show that a trespass occurred" (93): attaches to whether a trespass is shown.
  - 2022 incident: conditional "if Plaintiff did not possess a property right ... then both the trespass claim and any Fourth Amendment claim ... would be legally insufficient" (103).
  - "Assuming that, as to the 2021 incident at least, Plaintiff has alleged facts to support a trespass claim" (105): assumption; firm rule follows ("a trespass does not itself amount to a violation").
  - "The yard in question could be outside the curtilage", Alcon "could have been looking for Plaintiff ... to investigate a complaint", flashlight "might have been no more than a de minimus intrusion" (139): possibilities explaining insufficiency.
  - "she appears to be trying to allege a “class of one” claim" (163): attaches to the Court's characterisation of the claim type.
  - "one could conclude that a police officer’s investigative decisions simply “may not be attacked in a class-of-one equal protection claim.”" (191): "could" attaches to the conclusion drawn from Flowers.
  - "a police officer’s investigative decisionmay “remain subject to traditional class-based equal protection analysis,”" (197): availability of class-based review.
  - Firm, unhedged: "Accordingly, as alleged, Plaintiff’s equal protection claim must be dismissed." (197) - stated inside an order to show cause; no dismissal is entered.
  - "the new claims and partiesshe apparently wishes to add do not appear to have any relation" (207); "although the issue is not currently before the Court, it is questionable whether Plaintiff should be permitted to expand this lawsuit" (209).
  - Consequences: amended complaint "may be stricken" and claims "dismissed without further notice" (267); failure "may result in dismissal" (271).
- Rounded prose beside exact figures: "eleven cases in this District over the past three years" (209) beside the itemised list (211-239: eleven items, earliest filing 8/17/2023); "most of which were terminated shortly after they were filed" (209) beside exact filing/termination dates.
- Notes:
  - Claims and current status: three claims (33, 43-81); no claim dismissed by this order; Court's analysis finds the Fourth Amendment allegations insufficient without more facts (137-141) and the equal protection claim deficient for standing doubts, no similarly situated showing, no clear standard and no class-based motive (181-197).
  - Numeric figures: three claims (33); "eleven cases", "past three years" (209); "21 days" (271); "since 2015" (55); Dunn "198-acre ranch" (fn 5, 115); Rieck driveway "within a few feet of the entrance gate" (fn 6, 125); LaFave treatise "§ 2.3(b), at 475 (3d ed. 1996)" (133); 17-page order; docs 1-2, 28, 42, 43, 46, 62, 64.
  - Footnotes (6): fn 1 equal protection arises directly under the Fourteenth Amendment, Fourth Amendment via incorporation; § 1983 is the vehicle (35-39, continued at 63); fn 2 pending summary-judgment motion (97-99); fn 3 Ciraolo (109); fn 4 trespass "neither necessary nor sufficient" (111-113); fn 5 Oliver/Dunn examples (115); fn 6 curtilage examples (125-127).
  - Negative and exclusion statements: complaint "does not allege that Jaybird Lane is “Geneva Langworthy’s property.”" (95-103); "a trespass does not itself amount to a violation of the Fourth Amendment" (105); Plaintiff "has not alleged facts showing that an actual search occurred" (135); allegations "do not identify any class-based discrimination" (163); "gross incompetence is not the same thing as intentional discrimination" (187); "An officer’s duty to investigate reports of trespass is not subject to a clear standard" (189); "she does not allege she is a member of a suspect class, or that a fundamental right is implicated" (197); "This Order does not grant Plaintiff leave to amend the Complaint for any other purpose" (261).
  - Courts in cited authority: Tenth Circuit (most), Eighth Circuit (Doe v. Anoka Cnty., "Aug. 10, 2026", 181; Pratt v. Helms; Flowers), First Circuit (Daoust, 131), W.D. Wash. (Clark, 155), Ninth Circuit (Monteiro, 155), Second Circuit (St. German, 197).
- Operative definitions, rules and scope exceptions:
  - Trespass: "a physical invasion of property that directly infringes on another’s right of possession" (93, Dolan citing Padilla); Restatement (Second) of Torts § 158 (93).
  - Curtilage: "the area immediately surrounding the home" (121); open fields unprotected (121); "an open field need not be either open or a field" (121).
  - Search requires an attempt to obtain information (135, Jones 565 U.S. at 408 n.5); de minimis intrusions may not be unreasonable (131); officers may approach a home to interview without a warrant or suspicion (131-133).
  - Equal protection: similarly situated persons treated alike (149); class-based vs class-of-one theories (157-159); class-of-one needs differential treatment plus no rational basis (163-165) and "a specific and detailed account" (175); "the existence of a clear standard" (187-189).
  - Joinder: Rule 18(a) and Rule 20(a)(2) (A)-(B) (207). Magistrate authority to point out deficiencies on non-dispositive referral: 28 U.S.C. § 636(b)(1)(A), Fed. R. Civ. P. 72(a) (87-89).
- Amendments or contradictions (recorded, not resolved):
  - Location of first incident: "12 1/2 Towhee Lane" (45, 95) vs "Ms. Langworthy’s house on Jaybird Lane" in the same quoted claim (47).
  - Name of the related order: "Order Striking Pro Se Motions And Permission To File Electronically (Doc. 62)" (31-33) vs "Order Striking Pro Se Filings And Revoking Permission To File Electronically, entered contemporaneously herewith" (267).
  - Citation forms as printed: "Oliver, 66 U.S. 170" (115) vs "466 U.S." elsewhere; "Oliver, 466 U.S. at 300" (139); "de minimis" (131) vs "de minimus" (139); "Jaybird Land" (103).
  - Paragraph-count statements vs text blocks for the quoted claims (see Lists).
- Coverage: FULL. Read ledger: lines 1-110, 110-209, 210-282 (end of file confirmed at 281-282). All 17 printed pages present. Unread ranges: none. Missing source text: none. Extraction spot-checks: 17 footers in `docs/` original; footnote 2 matches original lines 95-97 (text 97-99); "12 1/2 Towhee" is ASCII in both original and text; four U+2026 ellipses in the original (orig lines 87, 91, 205, 241 = text 89, 93, 207, 243) became "..." as reported; table check not-applicable; visual check not-applicable (plain text) except the unresolved paragraph boundaries noted above.

## D10 (Doc 4) - Cora v. Commonwealth of Puerto Rico et al., Opinion and Order (D.P.R.)

- Source: `text/D10.txt` (414 lines) from `docs/uscourts_prd_3_26_cv_01105_0.txt`; local D10 = task page Doc 4; sha256 18e0e22fc76b260401d9fb4c16a793005e0a674a5a4d80c1084f1d1a36fb3b5b (manifest); 32,304 chars; plain-text source; printed pagination 17 pages (footer "Case 3:26-cv-01105-CVR Document 44 Filed 09/16/26 Page N of 17", 17 footers; running header "Captain Richard Cora v. Commonwealth of Puerto Rico et al. / Opinion and Order / Civil No. 26-1105 (CVR) / Page N" on pages 2-17).
- Written or submitted by: United States District Court for the District of Puerto Rico (3-5); "S/CAMILLE L. VELEZ-RIVE / UNITED STATES DISTRICT JUDGE" (407-411), "In San Juan, Puerto Rico" (405). The P.R. VPO, Puerto Rico Court of Appeals and Supreme Court of Puerto Rico are mentioned bodies, not authors.
- Type, date, edition: Opinion and Order (19) on two motions; "on this 16th day of September 2026" (405); filed 09/16/26; Document 44; "Judgment shall be entered accordingly" (401; judgment not in the bundle). Caption "CIVIL NO. 26-1105 (CVR)" (17).
- Period covered: administrative complaint December 2, 2019 through Supreme Court of Puerto Rico denials of April 25 and May 23, 2025; "final since June of 2025" (367); opinion September 16, 2026. Calendar dates; no fiscal convention.
- Entities and aliases:
  - Plaintiff Captain Richard Cora ("Plaintiff" or "Captain Cora", 23; "[Captain] Cora" in a quotation, 315); a "combat veteran" (27, 79).
  - Commonwealth of Puerto Rico ("Puerto Rico", 23). Puerto Rico’s Veteran Procurement Office ("P.R. VPO", 23).
  - Veteran’s Solicitor Agustín Montañez-Allman; defined alias printed "Solicitor MontañezAllman" (23), elsewhere "Solicitor Montañez-Allman"; he signed the Resolution (125).
  - Attorney Nelson H. Meléndez-López ("Attorney Meléndez-López"); Attorney Antonio Álvarez-Torres ("Attorney Álvarez-Torres"; printed "ÁlvarezTorres" at 55 and 149).
  - "Defendants" defined in fn 1 (55) as Puerto Rico, P.R. VPO, Solicitor Montañez-Allman and Attorney Meléndez-López; Álvarez-Torres is outside that definition and "did not file a Motion to Dismiss" (55, 383). Docket No. 21 is filed by Puerto Rico, P.R. VPO and Montañez-Allman only (43) yet is called "Defendants’" motion (45, 175, 377).
  - Amgen Manufacturing Limited ("AML", 79), the employer charged under Act No. 203.
  - VPO-appointed attorneys for Cora, in order: María M. Pérez-Hernández and María Teresa Quintana-Román (81-83; resigned September 2021, "health issues and incompatibility of criteria, respectively", 103); Raúl E. Bandas (appointed September 21, 2021, served until January 10, 2022, 105); Joseph Deliz-Hernández (appointed January 10, 2022, served until May 2, 2022 "when he retired", 105); Meléndez-López and Álvarez-Torres (appointed June 13, 2022, 107). Six named attorneys; two named María; two names end "-Hernández".
  - Evelyn Herrero, Deputy Veteran’s Solicitor (101); "the administrative judge" (97).
  - Courts: Puerto Rico Court of Appeals ("Court of Appeals", 129); Supreme Court of Puerto Rico (171) = "Puerto Rico Supreme Court" (213); Court of First Instance (209).
  - Quoted state-court judgment uses "the Veteran’s Advocate" / "the Advocate" and "Section 10 of Act No. 79" (315); no line in D10 equates these with the Solicitor or Act No. 203.
  - Same-name items inside D10: González v. Banco Cent. Corp. (289) vs González-Pina v. Rodríguez (179); Puerto Rico as party vs in case names (Santiago-Rodríguez v. Puerto Rico; Financial Oversight and Management Board for Puerto Rico, 209-213).
- Tables: none. Layout hazards: running headers and underscore rules between pages (e.g. 31-41, 57-67, 279-289); footnote 2 (153-155) and page break split "on the issue of personal" (151) / "damages" (169); footnote 15 (383) sits after the conclusion's first paragraphs; "DISMISSED" (397) and "WITH PREJUDICE." (399) are separate lines.
- Lists:
  - Dated chronology (79-171) - see deadlines field.
  - State appellate case numbers: "KLRA 2023-0463" (127) = "KLRA 2023-00463" (143) (AML appeal); KLRA 2024-00090 (AML, 147); KLRA 2024-00564 (AML, 151); KLRA 2024-00585 (Cora, 151); the last two consolidated (169). Administrative complaint "QI-7-19-12-12-784" (fn 4, 317).
  - Meléndez-López's dismissal arguments: color of state law (Polk County v. Dodson), no personal involvement, all due process received, no causation, appointment limited to administrative proceedings (231-233) - five.
  - Defendants' (Docket No. 21) grounds: Rooker-Feldman; res judicata and collateral estoppel; no § 1983/Fifth Amendment claim because no federal employee; sovereign immunity; qualified immunity for Montañez-Allman (177-193). Reply points (209-213).
  - Res judicata three elements (289); collateral estoppel four elements (291).
  - Docket index: No. 1 Complaint (29, 77; fns 4-7, 11, 12, 14 cite ¶¶ 30, 42, 44, 55, 60, 63, 75); No. 21 motion, No. 35 opposition, No. 41 reply (43); No. 24 Meléndez-López joinder/motion, No. 36 opposition (43); No. 27, Exhibit No. 1, pp. 22-23 (state appellate judgment, fns 8-10, 13). No reply listed for No. 24.
- Forecasts, guidance, deadlines, effective dates (dated procedural events, as printed):
  - Dec 2, 2019 Cora's complaint against AML in the P.R. VPO under Act No. 203 (79; repeated 311). Act No. 203 "of December 14, 2007" (79); Act No. 104 "of June 29, 1955" (195).
  - Jan 10, 2021 Quintana-Román letter asking Cora to quantify damages (97); Feb 1, 2021 she requested an administrative hearing (99); Feb 3, 2021 Herrero report finding probable cause, recommending a hearing (101); Feb 10, 2021 VPO notified AML it would hold a hearing (101).
  - September 2021 first two attorneys resigned (103); Sep 21, 2021 Bandas appointed (105); Jan 10, 2022 Bandas's service ends, Deliz-Hernández appointed (105); May 2, 2022 Deliz-Hernández retired (105); Jun 13, 2022 Meléndez-López and Álvarez-Torres appointed (107).
  - Sep 1, 2022 hearing limited to whether AML violated Act No. 203; Cora told a second damages hearing would follow (121-123); no damages evidence presented (123); the second hearing "never happened" (259). Reply calls it "a one-time violation on September 1, 2022" (213).
  - Jun 29, 2023 Resolution "notified" (125) / "issued" (145, 313): AML violated Act No. 203; fines "totaling $34,500.00"; no damages to Cora; signed by Montañez-Allman; notified to Meléndez-López and Álvarez-Torres.
  - Aug 31, 2023 AML appeal KLRA 2023-0463 (127); Sep 18, 2023 Meléndez-López and Álvarez-Torres special appearance saying they were hired to represent the P.R. VPO, not Cora (127); Oct 4, 2023 VPO (through Montañez-Allman) told the Court of Appeals it did not represent Cora (129); Oct 23, 2023 judgment: appeal premature for lack of proper notice (143); Nov 8, 2023 AML reconsideration motion (143).
  - Dec 18, 2023 VPO notified the Resolution, "allegedly altered" to erase the two attorneys from the notification list (145); Jan 16, 2024 reconsideration denied (145).
  - Feb 14, 2024 AML appeal KLRA 2024-00090 (147); May 14, 2024 premature again, notification "deficient and was therefore null and without effect" (147).
  - Aug 16, 2024 VPO notified the Resolution again, "allegedly altered" (149; "notified the Resolution to Captain Cora", 313); both AML and Cora sought reconsideration, denied Sep 13, 2024 (149).
  - Oct 13, 2024 AML appeal KLRA 2024-00564; Oct 15, 2024 Cora appeal KLRA 2024-00585 on personal damages; consolidated (151, 169).
  - Dec 20, 2024 Court of Appeals judgment affirming liability, "modifying the amount of fines" (new amount not stated), damages award "at the agency’s discretion" (169; quoted at 315).
  - Jan 9, 2025 Cora reconsideration motion "denied soon thereafter" (169; no date).
  - Feb 18, 2025 certiorari petition to the Supreme Court of Puerto Rico, "denied on April 25, 2025"; two reconsideration motions "denied on April 25, 2025 and on May 23, 2025" (171).
  - "This petition was finally denied on May 23, 2025 and is now final and unappealable" (341); "final since June of 2025" (367).
  - Sep 16, 2026 opinion. No day-count deadline appears in D10.
- Hedged claims (claim / hedge word / what it attaches to):
  - "allegedly altered" (145, 149): attaches to the alteration of the notification list in both later notifications; Spanish-language added paragraph not considered (fn 2, 153).
  - Quintana-Román "understood" AML's violations had caused "serious emotional damages" (99): her stated belief in the hearing request.
  - Cora "could produce his medical expenses if requested" (97); "Plaintiff did not think anything of it" (123).
  - Quoted state judgment: damages decision "ultimately remains a discretionary determination" (315); summary "such an award was at the agency’s discretion" (169).
  - Plaintiff "understands granting this request would be possible without voiding the P.R. VPO’s previous ruling" (271): Plaintiff's view, rejected at 343.
  - "Defendants understand there is no viable claim" (193): parties' position.
  - Court's own holding is unhedged: "the Court finds it is barred from resolving Plaintiff’s claims because it lacks jurisdiction" (297); "Thus, Plaintiff’s claims are barred by the Rooker-Feldman doctrine." (367).
- Rounded prose beside exact figures: "$34,500.00" printed identically twice (125, 313); "no less than $75,000.00" (25) is a floor, not a rounded figure; approximate phrases "hundreds of vacant positions" (79), "During September of 2021" (103), "denied soon thereafter" (169), "final since June of 2025" (367).
- Notes:
  - Claim: § 1983 action alleging violation of "Fifth Amendment due process right" (23); relief: compensatory damages "no less than $75,000.00" and an injunction ordering the P.R. VPO to schedule an administrative evidentiary hearing on damages (25-27, 271, 343). Conspiracy and Fourteenth Amendment theories raised first in oppositions: "these new allegations will not be considered as part of Plaintiff’s claims" (253-257).
  - Dispositions: Docket No. 21 "GRANTED" (45, 369, 377); Docket No. 24 joinder "GRANTED" (fn 1, 55) and the motion "GRANTED in part, as to the request for joinder, and DENIED in part as moot as to the additional arguments in support of dismissal" (379); "all claims raised by Plaintiff against all Defendants are DISMISSED WITH PREJUDICE." (397-399); ruling extends to Álvarez-Torres although he filed no motion (fn 1 at 55; fn 15 at 383). Ground: Rooker-Feldman (343-367); after listing all three doctrines the Court says "The Court agrees." (273-275) but the conclusion names only Rooker-Feldman (367); "no need for the Court to address the other arguments raised by Defendants" (369) - sovereign immunity, qualified immunity, failure to state a claim, Polk County color-of-law argument not decided.
  - Numeric figures: "$75,000.00" (25); "$34,500.00" (125, 313); two separate hearings promised (121-123); fines modified, amount not stated (169); "two reconsiderations" (213, 315); 17 pages; Docket Nos. 1, 21, 24, 27, 35, 36, 41, 44; fn markers 1-15.
  - Footnotes (15): fn 1 joinder granted, "Defendants" definition, Álvarez-Torres (55); fn 2 English-language rule, 42 U.S.C. § 864, Local Rule 5(c) (153-155); fn 3 "Id." (157); fns 4-10 record cites incl. complaint number QI-7-19-12-12-784 and Docket No. 27 Ex. 1 pp. 22-23 (317-329); fns 11-14 (347-353); fn 15 Álvarez-Torres (383).
  - Negative and exclusion statements: "no evidence was presented regarding damages" (123); "no monetary damages were awarded to Captain Cora" (125); attorneys said they were hired "not to represent Captain Cora" (127); VPO "did not represent Captain Cora in the appellate proceeding" (129); "the agency made no findings regarding the alleged damages" (315, quoted); "Anything not submitted in the English language will not be considered" (153); new allegations "will not be considered" (257); Plaintiff "is not requesting from this Court to vacate the ruling" (271, his position); "Attorney Álvarez-Torres did not file a Motion to Dismiss" (55, 383); Reply: Plaintiff "alleges no constitutionally protected property right" (213, Defendants' argument).
- Operative definitions, rules and scope exceptions:
  - Rule 12(b)(6) two steps (Schatz, 49-51); plausibility (Twombly, Sepúlveda-Villarini, 67-71).
  - Rooker-Feldman: no jurisdiction over "any action that is effectively or substantially an appeal from a state court’s judgment" (277); confined to "cases brought by state-court losers complaining of injuries caused by state-court judgments rendered before the district court proceedings commenced and inviting district court review and rejection of those judgments" (277, Exxon Mobil); Reed v. Goertz (343).
  - Res judicata: "(1) a final judgment on the merits in an earlier suit, (2) sufficient identicality between the causes of action ..., and (3) sufficient identicality between the parties" (289).
  - Collateral estoppel: "(1) ... same ..., (2) the issue was actually litigated; (3) ... determined by a valid and binding judgment; and (4) the determination ... was essential to the judgment" (291); claim vs issue preclusion distinguished (293-295).
  - A complaint cannot be amended through an opposition brief (253-257).
  - Judicial restraint: "if it is not necessary to decide more, it is necessary not to decide more" (369-373).
  - Language rule: pleadings in English, 42 U.S.C. § 864; Local Rule 5(c) certified translations (153).
- Amendments or contradictions (recorded, not resolved):
  - Certiorari denial date: "denied on April 25, 2025" (171) vs "This petition was finally denied on May 23, 2025" (341) vs "final since June of 2025" (367).
  - Court of Appeals reconsiderations: one motion on January 9, 2025 "denied soon thereafter" (169) and "an appeal and a reconsideration before the Puerto Rico Court of Appeals" (213, Reply) vs "Plaintiff requested two reconsiderations from the Puerto Rico Court of Appeals" (315). The Supreme Court level has "two reconsiderations" (171, 213).
  - KLRA number "2023-0463" (127) vs "2023-00463" (143).
  - Resolution June 29, 2023 "notified" (125) vs "issued" (145, 313); September 1, 2022 hearing "determined AML had violated Act No. 203" (311) vs violation conclusion in the June 29, 2023 Resolution (125).
  - Statute naming: Act No. 203 / Veteran’s Solicitor throughout vs "Section 10 of Act No. 79" / "Veteran’s Advocate" in the quoted state judgment (315).
  - Apparel Art quote "precludes the parties of their privies" (179) vs "precludes the parties or their privies" (279).
  - Constitutional basis: complaint pleads the Fifth Amendment (23, 193); opposition adds the Fifth and Fourteenth (195); Court excludes the Fourteenth Amendment addition (253-257).
  - Same day-month, different years: January 10 (2021 letter, 97; 2022 appointment, 105); June 29 (Act No. 104 of 1955, 195; Resolution of 2023, 125).
- Coverage: FULL. Read ledger: lines 1-90, 90-199, 199-308, 308-414 (end of file confirmed at 413-414). All 17 printed pages present. Unread ranges: none. Missing source text: none. Extraction spot-checks: 17 footers in `docs/` original; footnotes 4/8/13 match original lines 315/323/349 (text 317/325/351); one U+2026 in the original (orig 313 = text 315, "[...]") normalised to "..." as reported; table check not-applicable; visual check not-applicable (plain text).

## Shared ground candidates (part b) - locations only

- Issuing judges and filing dates (page-1 footers): D04 Maddox, D. Md., signed Sept 18, 2026 (481), filed 09/21/26 (37); D05 Sweazea (magistrate), D.N.M., Sept 18, 2026 (273), filed 09/18/26 (39); D10 Velez-Rive, D.P.R., Sept 16, 2026 (405), filed 09/16/26 (31). Other filings: D01 09/14/26 (41), D02 09/18/26 (31), D03 09/17/26 (47), D06 09/20/26 (49), D07 09/15/26 (43), D08 09/18/26 (33), D09 09/14/26 (63). Other magistrate-judge issuers: D07 Daniel J. Stewart (29-31), D09 Christopher B. Brown (51, 181).
- Same district: D. Md. in D02, D03, D04. "Local Rule 105.6 (D. Md. 2025)", no hearing: D04 35, D02 19, D03 35.
- Judge initials in case numbers (initials only; no document states whose they are): "JRR" in D04 citations (113, 221, 237), D02's own number 1:24-cv-03278-JRR (D02 71; signed Julie R. Rubin, D02 261-263) and D03's own number 1:25-cv-02281-JRR (D03 47, 71; signed George L. Russell, III, Chief Judge, D03 531-533). "GLR-17-3200" cited in D04 299.
- Same precedent, different citation forms:
  - Mayor of Balt. v. Trump, 416 F. Supp. 3d 452, 479 (D. Md. 2019): D04 91-93 (short "Trump" 99, 113-115); D02 73-75 as "Mayor & City Council of Baltimore v. Trump".
  - Kerns v. United States, 585 F.3d 187, 192 (4th Cir. 2009): D04 115; D02 75-77.
  - Evans v. B.F. Perkins Co., 166 F.3d 642: D04 95-97 (pin 647); D03 157.
  - Hutto v. S.C. Ret. Sys., 773 F.3d 536: D04 197 (pin 543, "South Carolina"), 441-443 (pin 549); D03 163 (pin 543).
  - King v. Rubenstein, 825 F.3d 206: D04 133-135 (pin 212); D03 167 (pin 214).
  - City of Cleburne v. Cleburne Living Ctr., 473 U.S. 432, 439 (1985): D05 149-151; D02 247 ("City of Cleburne, Tex.").
  - Polk County v. Dodson, 454 U.S. 312 (1981): D10 231-233 (pin 324-325); D06 581 ("Polk Cnty. V. Dodson", pin 318-19).
  - Twombly / Iqbal: D04 123-131 (both); D10 67-71 (Twombly only); D02 121, D03 169, D06 281, D07 61/69, D08 113, D09 111. D05 uses Rule 8(a)(2) without either (85-93).
- Doctrines across documents:
  - Eleventh Amendment, all ten documents: D04 345, 389, 437-455; D05 211 (case (i)); D10 209 (Reply argument); D01 79, 85, 101, 127; D02 81, 89, 151-181; D03 503-505; D06 73, 301-457, 799-815; D07 181-191; D08 81, 183-191, 259; D09 135.
  - State sovereign immunity: D04 165-207, 237, 441, 455; D10 193, 195; D02 163-173, 267; D03 161-193, 505; D06 311-457, 809-835; D07 187; D08 253-259.
  - Qualified immunity: D04 361; D05 97-99 (Doc. 46 motion pending); D10 193 (argument not decided, 369); D02 265.
  - 42 U.S.C. § 1983: every document except D03 (D04 12 lines; D05 39, 63, 181; D10 23, 177, 193, 231).
  - Monell municipal liability: D04 269-305, 461-463; D08 187.
  - Res judicata / collateral estoppel: D10 177-179, 195, 273, 279-295; D08 131, 153, 157, 159, 163.
  - Rooker-Feldman: D10 only (177, 195, 273, 277, 343-367).
  - Equal protection: D05 33-35, 73, 79, 143-197; D02 241-255; D06 617; D09 91, 137, 141, 171.
  - Conspiracy: D04 37, 75, 139-159, 175, 337, 477 (Maryland civil conspiracy count); D10 195, 235, 253 (raised first in oppositions); D06 143, 173, 561, 593, 611-641.
  - Fourth Amendment: D04 (67, 69) and D05 only. Fifth Amendment: D10 only (23, 193, 195, 209). Fourteenth Amendment: D04 69; D05 33-35, 73, 85, 143-149, 201, 267; D10 195, 209, 253; also D02, D08, D09. Malicious prosecution: D04 only (69, 73, 189).
  - Rule 8(a)(2): D04 123; D05 85-93, 99; D03 169; D07 75; D09 105. Rule 12(b)(1): D04 89-119; D01 47, 51; D02 59-81, 113; D03 149-151; D06 71 and later. Rule 15(a)(2): D05 261; D01 125. 28 U.S.C. § 636(b): D05 89; D07 279, 291.
  - Pro se litigants: D05 31, 209, 241-261; D01 51, 125; D02 29, 65; D06 39, 85, 99, 161, 221-235; D07 35, 57, 281; D08 25, 123-125; D09 131. Show cause: D05 throughout (25-27, 201, 261, 267, 271); D06 111, 585, 697.
  - Day-count deadlines: D05 271 (21 days); D06 87, 275 (90 days); D07 279-281. D04 and D10 state none.
  - With/without prejudice language appears in all ten documents (matching lines: D01 2, D02 2, D03 3, D04 3 (333, 339, 477), D05 4 (223, 229, 231, 237), D06 4, D07 2, D08 1, D09 2, D10 2 (209, 399)).
- No party, person, or case number of D04, D05 or D10 appears in any other bundle document (grep for party surnames and case numbers 3696/1291/1105 returned no hits outside the home document).

## Gaps (part b)

- None for readable text: D04, D05 and D10 read line by line to end of file; no clipped, missing or image-only material.
- Unresolved without page images: paragraph boundaries of the quoted claims in D05 (51-81).
- Not inspected by part b: the other seven documents beyond targeted greps listed above; platform capture overview text (outside assigned scope).

<!-- merged from doc-map-part-c.md -->
Navigation only, written by a parallel bundle-mapper for D06, D07 and D08. Facts and locations,
not questions, answers or difficulty claims. Line numbers ("L") are from `text/Dnn.txt`
(line 1 is the "# Dnn | docs/..." header). Quotes keep the source's curly quotes and dashes.
"Mapper count" marks a count made by the mapper that the document itself does not print.
Local ids differ from the task page's Doc N: D06 = Doc 9, D07 = Doc 3, D08 = Doc 6.

## D06 - Hernandez v. Supreme Court Suffolk County NY et al., E.D.N.Y. No. 2:25-cv-2057, Opinion and Order (Sept. 20, 2026)

- Source: local D06 = platform Doc 9 | `docs/uscourts_nyed_2_25_cv_02057_0.txt` -> `text/D06.txt`
  (868 lines, 92,199 chars per manifest; plain text with PDF page-footer lines
  "Case 2:25-cv-02057-NJC-ST Document 75 Filed 09/20/26 Page N of 46 PageID #:" from L49
  (Page 1) to L865 (Page 46); footers and page numbers are often run into body sentences,
  e.g. L111, L145, L205, L245, L317; each footer is followed by a literal "\<pageID>" line).
- Written or submitted by: the court - United States District Court, Eastern District of New
  York (L3-5); "NUSRAT J. CHOUDHURY, United States District Judge" (L37; signature
  "/s/ Nusrat J. Choudhury" L859-863). Case initials "(NJC) (ST)" (L33); "ST" is not expanded
  anywhere in the document. Parties' filings are only described, never reproduced.
- Type, date, edition: "OPINION AND ORDER" (L35) on motions to dismiss; "Dated: Central
  Islip, New York / September 20, 2026" (L855-857); every footer reads "Filed 09/20/26",
  "Document 75". Single edition; no amendment of this order in the bundle text read.
- Period covered: calendar dates only (no fiscal convention). Underlying events from June 2021
  to Sept. 26, 2025; federal docket from Apr. 11, 2025 to the Sept. 20, 2026 order; forward
  deadlines Oct. 2 and Oct. 9, 2026.
  - Dated events (chronological):
    - June 2021: Hernandez commenced the divorce/matrimonial action in Suffolk County Supreme
      Court (L103 "commenced in June 2021 currently before Justice Leo"; L107).
    - November 2021: Midland Credit Management commenced the debt collection action (L103).
    - December 2024: Hernandez filed a separate federal civil rights action against Suffolk
      County, the Suffolk County Police Department, Long Island Community Hospital "and other
      defendants" (L145-149); activity resumed in matrimonial/debt actions "shortly after" (L149).
    - Dec. 16, 2024: scheduling order in debt action; alleged notice not received "until March
      2025, after a court conference had already occurred and default judgment had been entered
      based upon her failure to appear" (L123).
    - Dec. 20, 2024: MLG Defendants filed an Order to Show Cause in the divorce action (L111-115).
    - Mar. 10, 2025: O’Brien allegedly "refused to upload" Hernandez's motion and uploaded it
      "the next morning" (L825); "delayed the electronic filing ... by one day" (L827);
      repeated at L835-839 ("causing a on day delay" [sic], L839).
    - Apr. 11, 2025: pro se Complaint filed, ECF No. 1, naming all Defendants "except the Bank
      Defendants and Justices Modelewski and Fields" (L161).
    - June 21, 2025: order to serve Defendants "by July 10, 2025, or to show good cause"
      (ECF No. 8) (L161).
    - July 9, 2025: Justice Liccione "entered a judgment against Hernandez" in the debt action
      (L103).
    - July 28, 2025: USPS receipts and letter stating service (ECF No. 9) (L161); "proof of
      service concerning all Defendants included in the original Complaint" (L343).
    - Aug. 1, 2025 ("Beginning on"): pre-motion letters, ECF Nos. 11, 13, 15 (L169).
    - Aug. 7, 2025: Court waived pre-motion conference requirement, scheduled briefing
      (Elec. Order) (L169).
    - Sept. 26, 2025: Justice Leo's decision/order in the divorce action that the Amended
      Complaint asks to vacate (L69 "decision"; L433 "order").
    - Nov. 14, 2025: Amended Complaint filed (ECF No. 30, L39) (L87, L171, L343).
    - Nov. 25-Nov. 30, 2025: all Defendants other than the Bank Defendants requested
      conferences (ECF Nos. 31, 34, 36, 37) (L205).
    - Dec. 1, 2025: Court again waived pre-motion conference; motions due Dec. 22, 2025,
      opposition Jan. 19, 2026, replies Feb. 2, 2026 (Elec. Order, Dec. 1, 2025) (L205-211).
    - Dec. 17, 2025: Judicial Defendants' motion, Rules 12(b)(1), 12(b)(2), 12(b)(5),
      12(b)(6) ("Mot. I", ECF No. 39-2) (L213).
    - Dec. 19, 2025: MLG Defendants' motion, Rules 12(b)(5), 12(b)(6) ("Mot. II", ECF No. 41)
      (L213).
    - Dec. 22, 2025: Pressler Defendants' motion, Rules 12(b)(5), 12(b)(6) ("Mot. III",
      ECF No. 42-1); same day O’Brien's motion, Rules 12(b)(1), 12(b)(6) ("Mot. IV",
      ECF No. 44-1) (L213). Motions collectively "ECF Nos. 39, 41, 42, 44" (L71).
    - Jan. 21, 2026: Hernandez sought leave to file a second amended complaint (ECF No. 46)
      (L215).
    - Jan. 26, 2026: leave denied "without prejudice, permitting Hernandez to renew her
      request only after resolution of the pending motions to dismiss" (Elec. Order, Jan. 26,
      2026) (L215-217). See contradiction (a) below: L345-347 cites "ECF No. 63; Elec. Order,
      Jan 21, 2026".
    - Undated, after Jan. 26, 2026: motion for reconsideration and renewed leave to amend
      (ECF Nos. 61, 63) (L217).
    - Feb. 21, 2026: reconsideration denied; Feb. 24, 2026: renewed leave to amend denied
      (L217).
    - Sept. 20, 2026: this Opinion and Order (L855-857).
- Entities and aliases:
  - Plaintiff: Veronica Hernandez, "proceeding pro se" (L7, L39); "Plaintiff" (L653).
  - "Suffolk County Supreme Court" = "the Supreme Court of the State of New York, Suffolk
    County" (L43) = caption "Supreme Court Suffolk County NY" (L11); described as "an arm of
    the state" (L427, L809).
  - "Judicial Defendants" = the four Justices "collectively, with the Suffolk County Supreme
    Court" (L55-57): Justice John J. Leo (caption L13 "Justice John J. Leo"; "John Leo" L361);
    Justice Maureen T. Liccione (caption L17 spells "Hon. Mareen T Liccione"; "Maureen
    Liccione" L361); Justice Christopher Modelewski (caption L23 "Christopher Modelewski",
    no honorific); Justice Aletha V. Fields (caption L23-25 "Hon. Aletha V. Fields").
  - "MLG Defendants" = Montefusco Law Group, Robert Montefusco, Abigail Miller (L59);
    represented Hernandez's "former husband" Anthony Hernandez in the matrimonial action
    (L109, L585).
  - "Pressler Defendants" = Pressler, Felt & Warshaw, LLP (caption L15 without comma before
    LLP), Craig Stiller, Ryan Tappan (L61); represented Midland Credit Management in the debt
    action (L585).
  - "the private attorney Defendants" / "private attorney defendants" = MLG + Pressler
    Defendants (L297, L595, L733, L771).
  - Theresa O’Brien: caption "Theresa" (L17); "identified in the Amended Complaint as
    “Theresa” and alleged to work as a “Court Filer”" (L63); also "a clerk at the Suffolk
    County Supreme Court" (L805), "court filer" (L813, L815).
  - "Bank Defendants" = Wells Fargo Bank, N.A., Woods Oviatt Gilman LLP, Lauren Russo, Richard
    Mullen, Encore Capital Group, Inc., Midland Credit Management, JP Morgan Chase Bank, Wells
    Fargo and Company (L65; 8 names, mapper count). The group label covers a law firm and two
    individuals as well as Midland Credit Management (which L103/L123 name as the debt-action
    plaintiff). "Wells Fargo" in the mortgage action (L127, L135: "Wells Fargo and its
    attorneys").
  - Non-party: Anthony Hernandez (other party to matrimonial action L103; "former husband"
    L585; mortgage action "involving Anthony Hernandez" L103; property "no longer owned by
    Anthony Hernandez" L135). Non-parties in the December 2024 federal action: Suffolk County,
    Suffolk County Police Department, Long Island Community Hospital (L145). New York
    Attorney General / Assistant Attorney General (service, L363, L373-385). "New York State
    Courts Electronic Filing system" (L671).
  - Motion aliases: "Mot. I" Judicial (ECF No. 39-2), "Mot. II" MLG (ECF No. 41), "Mot. III"
    Pressler (ECF No. 42-1), "Mot. IV" O’Brien (ECF No. 44-1) (L213).
  - Caption count: 20 defendant names in L11-27 (mapper count; 5 Judicial + 3 MLG +
    3 Pressler + O’Brien + 8 Bank).
- Tables: not applicable (no tables in D06).
- Lists:
  - Defendant groups, 5 bullets (L43, L55-57, L59, L61, L63, L65).
  - Relief sought, 5 numbered items "(Id. at 52.)" (L69): "1) an order clearing title to
    Hernandez’s home and vehicle; 2) an order vacating a September 26, 2025 decision rendered
    by Justice Leo in the divorce action; 3) a final judgment in her divorce litigation;
    4) compensatory damages; and 5) punitive damages." Variant list L157: compensatory
    damages, punitive damages, declaratory relief, injunctive relief.
  - Three underlying proceedings, numbered (L103): matrimonial (Leo), debt collection
    (Midland; Liccione), mortgage foreclosure (Fields).
  - Diagnoses (L139): Attention Deficit Hyperactivity Disorder, Autism Spectrum Disorder,
    Bipolar Disorder.
  - Fourteen enumerated claims in the Amended Complaint (L171-199; last item "14) Conversion."
    at L199): 1) Conspiracy, 18 U.S.C. § 241; 2) Retaliation, 18 U.S.C. § 1513;
    3) Interference, 18 U.S.C. § 1506; 4) 42 U.S.C. § 1983; 5) 42 U.S.C. § 1985; 6) ADA
    Title II, 42 U.S.C. § 12181; 7) Section 504 of the Rehabilitation Act, 29 U.S.C. § 794;
    8) Witness Tampering/Obstruction of Justice; 9) Intentional Infliction of Emotional
    Distress; 10) Negligent Infliction of Emotional Distress; 11) Slander Per Quod; 12) Libel
    Per Quod; 13) Abuse of Process; 14) Conversion. Prose summary of claims (L153-155) names
    New York common-law "abuse of process, defamation, intentional infliction of emotional
    distress, negligent infliction of emotional distress, and conversion". Criminal statutes
    named in discussion: "18 U.S.C. §§ 241, 1506, 1512, and 1513" (L671; § 1512 is not in the
    enumerated list).
  - Grounds raised by motions (L71-73): "lack of personal jurisdiction under Rule 12(b)(1)"
    [as written], insufficient service Rule 12(b)(5), failure to state a claim Rule 12(b)(6),
    Eleventh Amendment immunity, absolute immunity, Younger abstention.
  - Court's five reasons for granting the Judicial Defendants' motion (L325, "First" ...
    "And fifth").
  - Conclusion list of three dismissal groups (L847).
- Forecasts, guidance, deadlines, effective dates:
  - Bank Defendants: "Hernandez shall serve the Bank Defendants by October 2, 2026, and shall
    file a document demonstrating that service was accomplished by October 9, 2026" (fn. 2,
    L91); repeated in Conclusion (L849-853: "by October 2, 2026. She shall file proof of
    service by October 9, 2026. Failure to demonstrate timely service on the Bank Defendants
    will result in dismissal of all claims against them under Rule 4(m)"). Fixed calendar
    dates, not day counts.
  - Rule 4(m) 90-day service period quoted (L87, L275); "more than ten months have passed
    since the filing of the Amended Complaint" (L89; filing date Nov. 14, 2025 at L87).
  - Past deadlines: serve by July 10, 2025 (L161); briefing Dec. 22, 2025 / Jan. 19, 2026 /
    Feb. 2, 2026 (L205-211).
  - No objection period, no leave-to-amend deadline, no appeal or IFP certification, no
    Clerk-of-Court directions (negative evidence; grep for "prejudice", "appeal", "Clerk",
    "1915", "in forma pauperis" found none beyond L87, L215, L275, L345).
- Hedged claims (claim / hedge / what it attaches to):
  - L385: "Although Hernandez’s efforts may have provided actual notice of this action, actual
    notice does not satisfy the requirements of Rule 4(j)(2) or N.Y. C. P.L. R. § 307." "may"
    attaches only to whether her mailing gave actual notice; the conclusion "this Court lacks
    personal jurisdiction over Justices Leo and Liccione" (L385) is unhedged.
  - L355: "even assuming Justices Modelewski and Fields became aware of this action through
    other means" (assumption arguendo) versus L347, which states it as a fact: "the fact that
    Justices Modelewski and Fields have actual notice of this action does not cure".
  - L537: "Assuming that Hernandez has adequately alleged that she is a qualified individual
    with a disability" - the disability element is assumed, not decided.
  - L155: "the Court assumes that all claims are brought against all Defendants."
  - Alternative holdings: L325 "even if Younger abstention did not apply"; L447 "Even assuming
    that Hernandez satisfied the requirements of Ex parte Young"; L457 "even if Hernandez had
    properly served the Judicial Defendants"; L533 "In any event"; L835 "Even if the claims
    against O’Brien are not barred".
  - Scope qualifiers "To the extent": L653 (ADA/Rehab vs MLG/Pressler), L805 and L813
    (O’Brien official capacity).
  - Not reached: fn. 4 (L331) the Court "does not reach" arguments that non-ADA claims are
    implausible under 12(b)(6); fn. 7 (L565) the 12(b)(5) service argument of MLG/Pressler is
    not decided ("Accordingly, this Court addresses the plausibility ... under Rule 12(b)(6)").
  - Rule statement with "generally": "judges generally have absolute immunity" (L473);
    "private citizens generally lack standing" (L667).
- Rounded prose beside exact figures: "more than ten months" (L89) beside exact filing date
  Nov. 14, 2025 (L87) and order date Sept. 20, 2026; "one day" (L827) beside Mar. 10, 2025 and
  "the next morning" (L825); "several hours" of testimony (L545, no figure); "an extended period
  of time" dormant (L123); "shortly after" (L149). No percentages or money amounts in D06.
- Notes:
  - Footnotes: fn. 1 (L45-47) ECF page numbers used because the Amended Complaint "lacks page
    numbers and continuous paragraph enumeration"; fn. 2 (L87-91) Bank Defendants first named
    in Amended Complaint, Rule 4(m), service deadlines; fn. 3 (L225-227) quotations omit
    internal quotation marks etc.; fn. 4 (L329-331) non-ADA 12(b)(6) arguments not reached;
    fn. 5 (L461-465) Section 1983 "person" requirement (Will v. Mich. Dep’t of State Police,
    491 U.S. 58, 71; Mallet, 126 F.4th 125, 138) bars 1983 claims against the court and
    official-capacity Justices; fn. 6 (L487-489) Rehabilitation Act: Judicial Defendants "do
    not respond", the Act is only listed "as a reason for jurisdiction", claims dismissed "on
    the same grounds as the ADA Title II claims under Rule 12(b)(6)"; fn. 7 (L565) MLG/Pressler
    "do not claim they were not served but rather raise procedural defects with the method of
    service ... Neither party has identified any case in which an action was dismissed based on
    similar purported procedural defects."
  - Background sources considered: original Complaint's exhibits considered because none were
    attached to the Amended Complaint (L101; pro se exception L85-99).
  - Dispositions (who / claim / ground / location):
    - Justices Modelewski and Fields: "all claims" dismissed under Rule 12(b)(2) (lack of
      personal jurisdiction) and 12(b)(5) - never served with summonses (L343, L357).
    - Justices Leo and Liccione: "All claims" dismissed under 12(b)(2) and 12(b)(5) -
      certified mailing without personal service on the Attorney General; C.P.L.R. § 307(1)
      not met (L363, L385-389).
    - Suffolk County Supreme Court and Justices in official capacities: damages claims barred
      by the Eleventh Amendment (L427-431); Ex parte Young inapplicable (retrospective relief,
      L433-455); state-law claims barred under Pennhurst (L455); exception carved out: "except
      Hernandez’s ADA Title II claim" (L457; also L325 "with the exception of claims under ADA
      Title II"; motion's own exception L397).
    - Justices in individual capacities: barred by absolute judicial immunity (L483).
    - ADA Title II vs Judicial Defendants: Younger bars claims "related to the matrimonial and
      foreclosure proceedings" (L521-531, L555); "all ADA Title II claims" (all three
      proceedings) dismissed as implausible under 12(b)(6) (L533, L555). Exclusion fact:
      Younger is applied to the matrimonial and foreclosure proceedings only, described as
      pending when the action commenced (L325, L521); the debt-collection proceeding (judgment
      July 9, 2025, L103) is not in the Younger holding.
    - Rehabilitation Act vs Judicial Defendants: dismissed under 12(b)(6) (fn. 6, L489).
    - Summary: "all claims against the Judicial Defendants ... are dismissed" (L559).
    - MLG and Pressler Defendants, all under Rule 12(b)(6): Section 1983 (L609), Section 1985
      (L647), ADA Title II and Section 504 (L655), 18 U.S.C. §§ 241, 1506, 1512, 1513 "for lack
      of a private right of action" (L675), abuse of process (L709), defamation (litigation
      privilege, L727-729), IIED (L749-751), NIED (L767), conversion (L791); summary L795.
    - O’Brien: official-capacity claims barred by the Eleventh Amendment, dismissed under
      12(b)(1) (L815); individual-capacity claims barred by quasi-judicial immunity, dismissed
      under 12(b)(1) (L831); alternatively no plausible claim (L835-841); motion "granted under
      Rules 12(b)(1) and Rule 12(b)(6)" (L843).
    - Conclusion (L847): Judicial Defendants under Rules 12(b)(1), 12(b)(2), 12(b)(5) and
      12(b)(6); Pressler and MLG Defendants under 12(b)(6); O’Brien under 12(b)(1) and 12(b)(6).
    - Bank Defendants: no motion; not served; conditional Rule 4(m) dismissal (fn. 2, L849-853).
    - Negative evidence: none of the dismissals is labelled "with prejudice" or "without
      prejudice"; the only "without prejudice" wording is the Rule 4(m) quotation (L87, L275)
      and the Jan. 26, 2026 denial of leave to amend (L215, L345). No leave to amend is granted
      in the Conclusion (L845-853). No Rooker-Feldman, supplemental-jurisdiction (§ 1367) or
      in forma pauperis discussion.
  - Numeric figures (exact wording): "Page 1 of 46" ... "Page 46 of 46"; "Document 75"; "90
    days" (L87, L275); "more than ten months" (L89); "four separate motions" (L299); "three
    overarching arguments" (L317); "two principal arguments" (L799); "only two circumstances"
    (L473); "three types of state-level proceedings" (L497); "three additional,
    non-dispositive factors" (L499); "several hours" (L545); "by one day" (L827); "on day
    delay" (L839); five relief items (L69); fourteen enumerated claims (L171-199).
  - Statutes and rules cited: 42 U.S.C. §§ 1983, 1985 (incl. 1985(3)); ADA Title II
    (42 U.S.C. § 12181 in claims list L183; § 12132 quoted L533); Rehabilitation Act § 504,
    29 U.S.C. § 794 (L185); 18 U.S.C. §§ 241, 242 (Wilson parenthetical L673), 1506, 1512,
    1513; Fed. R. Civ. P. 4(a)-(c) (L339-341), 4(j)(2) (L365-373), 4(m) (L87, L273-277),
    12(b)(1), 12(b)(2), 12(b)(5), 12(b)(6), 12(h)(3) (L243); N.Y. C.P.L.R. § 307(1), (2)
    (L373-385); U.S. Const. amend. XI (L401-403).
  - Selected cited cases (location): Ashcroft v. Iqbal (L281, L283, L289, L553, L765, L839);
    Bell Atl. Corp. v. Twombly (L839-841); Younger v. Harris, 401 U.S. 37 (L499, L503); Sprint
    Commc’ns v. Jacobs (L497-499, L513); Middlesex Cnty. Ethics Comm. (L501); Falco v. Justs.
    of Matrim. Parts of Sup. Ct. of Suffolk Cnty. (L499-501); Ex parte Young, 209 U.S. 123
    (L411); Pennhurst, 465 U.S. 89, 106 (L419, L455); Will v. Mich. Dep’t of State Police
    (L463); Mireles v. Waco (L473, L481, L829); Polk Cnty. v. Dodson (L581); Henrietta D. v.
    Bloomberg (L535, L545-547, L653); Gollomp v. Spitzer (L429, L809); Kellogg v. Nichols,
    170 F.4th 20 (2d Cir. 2026) (L473, L479); Abadi v. Greyhound Lines (2d Cir. Apr. 20, 2026)
    (L621-623); Gibson v. Trs. of Columbia Univ. (S.D.N.Y. Jan. 15, 2026) (L85).
- Operative definitions, rules and scope exceptions (verbatim tests):
  - Pro se construction (L221-235): construe "liberally and Interpret[s] them to raise the
    strongest arguments that they suggest" (Hunter v. McMahon); pro se status "does not exempt
    a party from compliance with relevant rules" (Lomax).
  - Amended pleading (L85): "an amended complaint ordinarily supersedes the original" with the
    pro se exception (Gibson; Jarvois; Galea L99).
  - Rule 12(b)(1) (L239-261): dismissal proper "when the district court lacks the statutory or
    constitutional power to adjudicate it"; plaintiff's burden "by a preponderance of the
    evidence" (Makarova); decided first (Daly; Pressley); facial vs factual challenges (Carter,
    Lugo, Tandon, Harty, Katz).
  - Rule 12(b)(5) (L263-277): plaintiff "bears the burden of establishing that service was
    sufficient"; Rule 4(m) text: "If a defendant is not served within 90 days after the
    complaint is filed ... must dismiss the action without prejudice against that defendant or
    order that service be made within a specified time. But if the plaintiff shows good cause
    for the failure, the court must extend the time for service for an appropriate period."
  - Rule 12(b)(6) (L281-289): "state a claim to relief that is plausible on its face"; "more
    than a sheer possibility".
  - Service on state officers (L365-383): Rule 4(j)(2)(A) chief executive officer or (B) state
    law; C.P.L.R. § 307(1) delivery to the Attorney General or an Assistant Attorney General at
    an office within the State; under § 307(2) "a plaintiff must both serve the state officer and
    personally serve the Attorney General" (Polletta). "actual notice does not cure improper
    service" (L349, Jean-Baptiste).
  - Eleventh Amendment (L401-409): bars damages actions against a state and officials in
    official capacities "unless the state waives sovereign immunity or Congress abrogates it".
  - Ex parte Young (L411-417): applies when "the complaint (1) alleges an ongoing violation of
    federal law; and (2) seeks relief properly characterized as prospective"; does not extend to
    state agencies (Deadwiley). Pennhurst bars state-law claims "regardless of the form of
    relief sought" (L419). Section 1983 judicial-officer clause (L447): "injunctive relief shall
    not be granted unless a declaratory decree was violated or declaratory relief was
    unavailable."
  - Judicial immunity (L473): overcome "in only two circumstances: (1) when a judge takes action
    outside the judge’s judicial capacity, and (2) when a judge takes action, though judicial in
    nature, in the complete absence of all jurisdiction."
  - Younger (L497-503): three categories - "(1) “ongoing state criminal prosecutions”; (2) state
    “civil enforcement proceedings” that are “akin to criminal prosecutions”; and (3)
    proceedings that are “uniquely in furtherance of the state courts’ ability to perform their
    judicial functions,”"; then three non-dispositive Middlesex factors (pending proceeding,
    important state interest, adequate opportunity for review); exception for "bad faith,
    harassment or any other unusual circumstance". Applied to divorce actions (Tomczyk L505-513)
    and ADA Title II accommodation claims (Roldan L515-517).
  - ADA Title II / Section 504 elements (L533-535, L653): "(1) [the plaintiff] is a qualified
    individual with a disability; (2) the defendant is subject to the ADA; and (3) ... was
    denied the opportunity to participate in or benefit from ..." (Henrietta D.); "meaningful
    access" (L535).
  - Section 1983 color of law (L579-581): private attorneys "do not act under color of state
    law when performing the traditional functions of counsel" (Polk Cnty.); joint action (L593):
    "(1) an agreement between a state actor and a private party; (2) to act in concert to inflict
    an unconstitutional injury; and (3) an overt act done in furtherance of that goal causing
    damages." (Ciambriello).
  - Section 1985(3) (L615-617): "(1) a conspiracy; (2) for the purpose of depriving a person or
    class of persons of the equal protection of the laws . . . ; (3) an act in furtherance of the
    conspiracy; and (4) an injury to person or property, or a deprivation of a right or
    privilege of a citizen of the United States."
  - Criminal statutes (L667): "Statutes creating criminal liability, however, do not create
    private rights of action" (Checo).
  - New York abuse of process (L691-695): "(1) employs regularly issued legal process to compel
    performance or forbearance of some act, (2) with intent to do harm without excuse o[r]
    justification, and (3) in order to obtain a collateral objective that is outside the
    legitimate ends of the process." Improper motive alone insufficient.
  - Litigation privilege (L715-719): absolute privilege for statements "pertinent to the
    litigation"; covers judges, parties, attorneys, witnesses; "not defeated by allegations of
    malice".
  - IIED (L735-745): "(i) extreme and outrageous conduct; (ii) intent to cause, or disregard of a
    substantial probability of causing, severe emotional distress; (iii) a causal connection
    between the conduct and injury; and (iv) severe emotional distress." Standard "rigorous, and
    difficult to satisfy".
  - NIED (L759-763): a duty owed directly and a breach that "either unreasonably endangered the
    plaintiff’s physical safety or caused the plaintiff to fear for her own safety" (Taggart).
  - Conversion (L773-781): "(1) the property subject to conversion is a specific identifiable
    thing; (2) plaintiff had ownership, possession or control over the property before its
    conversion; and (3) defendant exercised an unauthorized dominion over the thing in
    question . . . to the exclusion of the plaintiff’s rights."
  - Quasi-judicial immunity (L829): the document's parenthetical to Mitchell v. Fishbein, 377
    F.3d 157, 172-73 reads "absolute immunity extends to nonjudicial officials whose acts are
    functionally comparable to those of a judge or integrally related to an ongoing judicial
    proceeding"; Dieujuste v. Sin applies it to court personnel; immunity applies "even where a
    plaintiff alleges that the challenged conduct was erroneous, malicious, or undertaken in bad
    faith" (Mireles).
- Amendments or contradictions (internal to D06; stated as found, not resolved):
  - Pleading amendment: Amended Complaint (Nov. 14, 2025) added the Bank Defendants and Justices
    Modelewski and Fields (L201, L87, L161); leave for a second amended complaint denied
    (L215-217, L345). Court considers original Complaint's exhibits (L101).
  - (a) Denial of leave to file a second amended complaint: L215-217 "On January 21, 2026,
    Hernandez sought leave ... (ECF No. 46.) On January 26, 2026, the Court denied that motion
    without prejudice ... (Elec. Order, Jan. 26, 2026.)" versus L345-347 "(See ECF No. 63; Elec.
    Order, Jan 21, 2026.)".
  - (b) Ground labels: L71 "lack of personal jurisdiction under Rule 12(b)(1)" versus
    L239 (12(b)(1) = subject matter jurisdiction) and L357/L389 (personal jurisdiction under
    Rule 12(b)(2)).
  - (c) ADA Title II citation: claims list "42 U.S.C. § 12181" (L183) versus quoted Title II
    "42 U.S.C. § 12132" (L533).
  - (d) O’Brien's quasi-judicial argument cited to "(Mot. III at 10.)" (L819) though O’Brien's
    motion is "Mot. IV" (L213, L311, L799) and Mot. III is the Pressler motion.
  - (e) Same reporter cite spelled "Williams v. Marinelli, 987 F.3d 188, 197" (L419-421) and
    "Williams v. Marinello, 987 F.3d 188, 197" (L809); "Mayo v. Mayo" (L581-583) then "May,
    2023 WL 5587596" (L585).
  - (f) Liccione spelled "Mareen T" in caption (L17) and "Maureen T." in body (L55, L123).
  - (g) Debt action judgment timing: L103 Justice Liccione "entered a judgment against
    Hernandez on July 9, 2025"; L123 says notice arrived "until March 2025, after ... default
    judgment had been entered". Both are stated; the document does not reconcile them.
  - (h) Section 1985 argument attributed to "The MLG Defendants" (L613, Mot. II at 12), but the
    holding covers MLG and Pressler (L647); L697 says "the Pressler Defendants improperly
    pursued debt collection and foreclosure claims" while L135 attributes the foreclosure to
    "Wells Fargo and its attorneys" and L585 says Pressler represented Midland in the debt
    action.
  - Typos as printed: "Rulle 12(b)(1)" (L799); "ADA Title claims" (L325); "labels the claims as
    issue" (L765); "on day delay" (L839); "Mot II"/"Mot III" without periods (L651).
- Coverage: FULL. Read L1-868 in seven chunks (L1-120, L120-239, L239-358, L358-467,
  L467-566, L566-665, L665-868) plus targeted greps. Remaining unread: none. Missing source
  text: none known (intake: complete capture, gap_characters 0; text equals original after
  NFKC). Spot-checks: page footers run Page 1 to Page 46 of 46 consecutively (L49 ... L865);
  tables not applicable; footnotes 1-7 located (numbers are run into body lines, e.g. "ECF No.
  30.)1" L39, "2" at end of L85, "(2d 3" L225, "5" L455/L461, "6" L487). Original `docs/` file
  spot-checked by search: 46 "Page N of 46" footers; fn. 7 sentence "Neither party has
  identified any case ..." at docs line 563 = text L565 (constant offset of 2 lines for the
  id header and blank line); no U+2026 in the original.

## D07 - Mulvilhill v. Kuchler et al., N.D.N.Y. No. 6:26-CV-1517, Report-Recommendation and Order (Sept. 15, 2026)

- Source: local D07 = platform Doc 3 | `docs/uscourts_nynd_6_26_cv_01517_0.txt` -> `text/D07.txt`
  (298 lines, 28,380 chars per manifest; plain text with page headers "- 1 -" ... "- 18 -" and
  footers "Case 6:26-cv-01517-ECC-DJS Document 8 Filed 09/15/26 Page N of 18" from L43 (Page 1)
  to L297 (Page 18); several footers are run into body sentences, e.g. L83, L93, L103, L119).
- Written or submitted by: the court - United States District Court, Northern District of New
  York (L5-7); the author block names "DANIEL J. STEWART / United States Magistrate Judge"
  (L29-31) under "APPEARANCES". No /s/ signature line; the document ends "Dated: September 15,
  2026 / Albany, New York" (L293-295). Case initials "(ECC/DJS)" (L15); "ECC" is not expanded
  in the document. The recommendation is addressed to "the District Court" (L225).
- Type, date, edition: "REPORT-RECOMMENDATION and ORDER" (L33) on initial review of a pro se
  complaint after referral "pursuant to L.R. 72.3" (L39-47); Document 8, filed 09/15/26; dated
  Sept. 15, 2026, Albany, New York (L293-295). Recommendations (dismissal) plus orders (counsel
  motion denied; Clerk to serve). Single edition.
- Period covered: calendar dates only. The document gives no dates for the underlying events
  (mother's death, Herkimer/Oneida County proceedings, probate) and no filing date for the
  Complaint, the IFP motion or the counsel motion; the only document date is Sept. 15, 2026.
  - Dated or sequenced events: Clerk forwarded the Complaint (Dkt. No. 1) for review (L35);
    IFP motion (Dkt. No. 2) "has been granted" (L37; by whom/when not stated); Motion for
    Appointment of Counsel (Dkt. No. 4) (L37); referral under L.R. 72.3 (L39-47); report dated
    Sept. 15, 2026 (L293). Summons request at Dkt. No. 2-1 at p. 1 (L87, L101, L181).
- Entities and aliases:
  - Plaintiff: Ashley Mulvilhill (caption "ASHLEY MULVILHILL" L9; "Plaintiff, Pro Se /
    Forestport, New York 13338" L23-27; "pro se Plaintiff Ashley Mulvilhill (“Plaintiff”)" L35).
    Spelling note: the mother's attached documents are for "Marybeth Mulvihill" (L93, L99) -
    "Mulvihill" without the second "l" before "h".
  - Defendants: "RICKI KUCHLER, et al." (L17). Ricki Kuchler (“Ricki”), "who appears to be
    Plaintiff’s sister" (L91; "appears to indicate" L143); Peter Kuchler (“Peter”) referenced
    with Ricki as “trustee/executor” (L101, L143); Ricki listed as "fiduciary and executrix"
    and "trustee" in attachments (L101). Summonses sought (Dkt. No. 2-1 at p. 1) for "Judge
    Crandall of the Herkimer County Surrogate Court; Camille Kahler (“Camille”); Deborah
    VanSlyke; Gregory VanSlyke; and Custom Wealth Management" (L101). Mapper count: 7 named
    defendants (Ricki, Peter, Judge Crandall, Camille Kahler, Deborah VanSlyke, Gregory
    VanSlyke, Custom Wealth Management).
  - Judge Crandall: no first name given; "Judge Crandall of the Herkimer County Surrogate
    Court" (L101); pronoun "his official duties" (L177); misspelled "Judge Randall" once (L155).
  - Court alias: "Herkimer County Surrogate Court" (L101) vs "Herkimer County Probate Court"
    (L181, L191) - the latter treated "To the extent that Plaintiff is attempting to assert any
    claims against" it (L181), citing Dkt. No. 2-1 at p. 1.
  - Camille Kahler: "listed as the attorney on an “Affidavit of Fiduciary”" (L101) "but is not
    otherwise named in the allegations".
  - Custom Wealth Management: an "investment company" is referenced (Dkt. No. 1-1 at pp. 5-6),
    "but it is uncertain if that is intended to refer to Custom Wealth Management" (L101).
  - Marybeth Mulvihill: Plaintiff's mother (death certificate Dkt. No. 1-1 at p. 82; Last Will
    and Testament Dkt. No. 1-1 at pp. 11-18) (L93-99).
  - Places: Herkimer and Oneida Counties (court proceedings, L91); Forestport, New York 13338
    (L27); Albany, New York (L295).
- Tables: not applicable (no tables in D07).
- Lists:
  - 28 U.S.C. § 1915(e)(2)(B) grounds (L53-55): "(i) is frivolous or malicious; (ii) fails to
    state a claim on which relief may be granted; or (iii) seeks monetary relief against a
    defendant who is immune from such relief."
  - Allegations against Ricki, seven quoted phrases (L91): "kicked me out of our mother[’]s
    home," "began taking items even my personal items," "refused to allow me to find my own
    apartment or vehicle," "refused to allow me to have any part in the death arrangements for
    our mother," "sold my mother[’]s home to the neighbor," "opened accounts in my name," and
    "a verbal altercation [with me] at our mother’s home where [she] attacked me."; plus court
    proceedings in "both Herkimer and Oneida Counties" (L91).
  - Five summons targets beyond Ricki and Peter (L101; last item "Custom Wealth Management").
  - "Plaintiff lists three causes of action, id. at p. 7" (L103-107): first - probate
    ("[a]ll documents are changed and forged as to probate"; requests documentation as to "a
    trust or accounting or my mothers finances or legal sale of her home"); second - "not
    incompetent and [is] able to control [her] own affairs and monies" and "identity has been
    stolen"; third - "unable to obtain any help or legal representation". Relief: "requests her
    removed and him removed as trustees of my money and that all money be repaid to me." (Id.
    at p. 8, L107-109).
  - Rule 8(a) three elements (L111-117).
  - Hodge factors (L253): "the indigent’s ability to investigate the crucial facts, whether
    conflicting evidence implicating the need for cross-examination will be the major proof
    presented to the fact finder, the indigent’s ability to present the case, the complexity of
    the legal issues and any special reason in th[e] case why appointment of counsel would be
    more likely to lead to a just determination."
  - Conclusion: one RECOMMENDED item and two ORDERED items (L273-277).
- Forecasts, guidance, deadlines, effective dates:
  - Objections (L279): "Pursuant to 28 U.S.C. § 636(b)(1), the parties have fourteen (14)4 days
    within which to file written objections"; "FAILURE TO OBJECT TO THIS REPORT WITHIN FOURTEEN
    (14) DAYS WILL PRECLUDE APPELLATE REVIEW." (Roldan v. Racette, 984 F.2d 85, 89; Small v.
    Sec’y of Health and Human Servs.; 28 U.S.C. § 636(b)(1); Fed. R. Civ. P. 72 & 6(a), L279-291).
  - Fn. 4 counting rule (L281-283): "If you are proceeding pro se and are served with this Order
    by mail, three additional days will be added to the fourteen-day period, meaning that you
    have seventeen days from the date the order was mailed to you to serve and file objections.
    FED. R. CIV. P. 6(d). If the last day of that prescribed period falls on a Saturday, Sunday,
    or legal holiday, then the deadline is extended until the end of the next day that is not a
    Saturday, Sunday, or legal holiday. FED. R. CIV. P. 6(a)(1)(C)." No calendar end date is
    printed; the mailing date is not stated.
  - No amendment deadline is set; leave to amend is mentioned only conditionally in fn. 3 (L239).
- Hedged claims (claim / hedge / what it attaches to):
  - Identity/relationship hedges: Ricki "who appears to be Plaintiff’s sister" (L91); "The
    Complaint appears to indicate that Ricki is Plaintiff’s sister" (L143); death certificate
    "presumably for her mother" (L93); "Presumably, Judge Crandall was somehow involved in the
    court proceedings ... that took place in Herkimer County ... though Plaintiff does not state
    so or explain how" (L173-177); "uncertain if that is intended to refer to Custom Wealth
    Management" (L101); "It is not entirely clear what relation these remaining Defendants have
    to this action" (L101); "the individuals named in the Complaint all appear to be private
    parties" (L143).
  - Claim-basis hedges: "it does not appear ... that Plaintiff was an employee" (L87, L219);
    "it does not appear ... that Plaintiff is suing a government official ... except Judge
    Crandall" (L87, L219); "it remains unclear what the legal basis is for any of her claims"
    (L103); first cause of action "seems to relate to the probate proceedings" and "appears to
    request" (L103); "it is not clear that any of Plaintiff’s claims arise under the
    Constitution" (L109); "it does not appear that any of the claims ... arise under the
    Constitution" (L223); "The Complaint appears to relate to events following the death of
    Plaintiff’s mother" (L89).
  - "may" in a side clause: "The mere fact that Ricki may have allegedly availed herself of the
    judicial system ... does not make her or any of the other Defendants a state actor" (L145);
    "that any Defendant may have spoken or provided a statement to a police officer or a court,
    even if that information was false, ... is insufficient" (L147-151) - the holdings (not a
    state actor; insufficient) are unhedged.
  - Conditional scope: "To the extent that Plaintiff attempts to assert claims pursuant to
    Section 1983" (L129); "To the extent that Plaintiff’s allegations against Judge Crandall
    relate to the performance of his official duties ... no exception to the immunity doctrine
    would apply" (L177); "To the extent that Plaintiff is attempting to assert any claims against
    the Herkimer County Probate Court" (L181); "Even assuming that the Complaint asserts a
    federal claim" (L225); fn. 3 "Should Plaintiff be granted leave to amend ... can be
    reconsidered" (L239); counsel denial "At this moment in time" (L267).
  - Rule statements with "generally": "Private parties are generally not amenable to suit under
    § 1983" (L143, Bhatia); "Generally, “acts arising out of, or related to, individual cases
    before [a] judge are considered judicial in nature.”" (L167).
- Rounded prose beside exact figures: not applicable (no estimates beside exact figures). Exact
  figures: "$75,000" (L201, L205); "fourteen (14)" days (L279); "three additional days" and
  "seventeen days" (L281); "three causes of action" (L103); "Page 1 of 18" ... "Page 18 of 18".
- Notes:
  - Footnotes: fn. 1 (L41) "Citations to Plaintiff’s Complaint are to page numbers provided by
    the Court’s CM/ECF system."; fn. 2 (L63) frivolousness test - "lacks an arguable basis
    either in law or in fact." (Neitzke v. Williams, 490 U.S. 319, 325); fn. 3 (L239)
    supplemental jurisdiction may be reconsidered if leave to amend is granted and a viable
    federal claim is asserted; fn. 4 (L281-283) mail service: 14 + 3 = 17 days, weekend/holiday
    extension.
  - Recommended/ordered dispositions (who / claim / ground / location):
    - Whole Complaint: recommended dismissed "for failure to provide proper notice of the basis
      of Plaintiff’s claims" under Rule 8 (L111-125).
    - Section 1983, state action (L155): "dismissed against all Defendants except Judge Randall
      [sic]" for failure to allege state action.
    - Section 1983, personal involvement (L153-155): "additionally, the Section 1983 claims
      against all Defendants except Ricki be dismissed based on failure to allege personal
      involvement."
    - Judge Crandall: Section 1983 claims dismissed "based on judicial immunity" (L191).
    - Herkimer County Probate Court: "any Section 1983 claim ... dismissed pursuant to the
      Eleventh Amendment" (L191); "No other basis for waiver or abrogation is set forth in the
      Complaint" (L187).
    - Title VII: not a separate holding; noted that "it does not appear ... that Plaintiff was
      an employee of any of the Defendants" (L87, L219).
    - Subject-matter jurisdiction: no complete diversity ("Plaintiff and several of the
      Defendants reside in New York, Compl. at pp. 1-4, which destroys complete diversity",
      L207-209); federal question basis claimed (Compl. at p. 3, L109, L219) but no claim
      appears to arise under federal law (L223).
    - State-law claims: recommends declining supplemental jurisdiction (L225, L237).
    - Motion for Appointment of Counsel (Dkt. No. 4): "denied without prejudice to being
      renewed" (L267); Conclusion "ORDERED, that Plaintiff’s Motion for Appointment of Counsel
      (Dkt. No. 4) is DENIED" (L275, without the "without prejudice" words).
    - Conclusion: "RECOMMENDED, that the Complaint (Dkt. No. 1) be DISMISSED as set forth above"
      (L273); "ORDERED, that the Clerk of the Court serve a copy" (L277).
    - Negative evidence: the dismissal recommendation does not say "with prejudice" or "without
      prejudice" for the Complaint, and does not recommend leave to amend (only fn. 3's
      conditional; "prejudice" appears only in the Carnegie-Mellon quotation L237 and the counsel
      denial L267). The IFP motion was granted (L37), not denied. The Complaint "does not allege
      any conduct on behalf of anyone other than Ricki" (L101); "Plaintiff makes no specific
      claims against Judge Crandall" (L173); "The Complaint does not assert that any of the
      Defendants are state actors" (L143). No Rooker-Feldman or Younger discussion.
  - Statutes and rules cited: 28 U.S.C. § 1915(e)(2)(B) (L53-55); Title VII, 42 U.S.C. §2000e-2
    (L83-87); 42 U.S.C. § 1983 (L83, L87); Fed. R. Civ. P. 8(a), 8(a)(2) (L75, L111-119); Rule
    12(h)(3) (L201); 28 U.S.C. §§ 1331, 1332 (L201); 28 U.S.C. § 1367(a), (c) (L225-237); 28
    U.S.C. § 636(b)(1) (L279, L291); Fed. R. Civ. P. 6(a), 6(a)(1)(C), 6(d), 72 (L281-291);
    N.D.N.Y. L.R. 72.3 (L39-47); Eleventh Amendment (L181-189).
  - Selected cited cases (location): Bell Atl. Corp. v. Twombly (L61, L69, L73, L77); Ashcroft v.
    Iqbal (L69-79); Neitzke v. Williams (fn. 2, L63); Nance v. Kelly; Anderson v. Coughlin (L57);
    Bliven v. Hunt (L167, L169); Pierson v. Ray; Stump v. Sparkman; Bradley v. Fisher (L165-167);
    McCluskey v. Roberts (L169-171); Gollomp v. Spitzer, 568 F.3d 355, 368 (via Dodd v.
    O’Sullivan, L187); Carnegie-Mellon Univ. v. Cohill (L237); Osborn v. Haley (L237); Wisconsin
    Dep’t of Corr. v. Schacht (L207); Roldan v. Racette (L279-289); Howe v. First Am. Title
    Agency, 2026 WL 672956 (E.D. Mich. Mar. 9, 2026) (L147); Leftridge; Hendricks v. Coughlin;
    Terminate Control Corp. v. Horowitz; Hodge v. Police Officers; Velasquez v. O'Keefe
    (L247-261).
- Operative definitions, rules and scope exceptions (verbatim tests):
  - Pro se review (L57-59): duty "to show liberality"; "extreme caution . . . in ordering sua
    sponte dismissal of a pro se complaint before the adverse party has been served" (Anderson).
  - Plausibility (L59-79): "enough facts to state a claim to relief that is plausible on its
    face"; "Threadbare recitals of the elements of a cause of action, supported by mere
    conclusory statements, do not suffice."
  - Rule 8(a) (L111-117): "(1) a short and plain statement of the grounds for the court’s
    jurisdiction . . . ; (2) a short and plain statement of the claim showing that the pleader is
    entitled to relief; and (3) a demand for the relief sought, which may include relief in the
    alternative or different types of relief."
  - State action (L131-135): "State action requires both the exercise of some right or privilege
    created by the State and the involvement of a person who may fairly be said to be a state
    actor." Litigants (L145-147, Sam & Mary Hous. Corp.) and court-appointed executors/trustees
    (L147-151, Howe; Heinemann) are not state actors by that fact alone.
  - Judicial immunity (L161-171): absolute except acts "performed in the clear absence of all
    jurisdiction"; "Judicial immunity is overcome in only two circumstances: (1) a judge is not
    immune from liability for nonjudicial actions, i.e., actions not taken in the judge’s
    judicial capacity; and (2) a judge is not immune for actions, though judicial in nature,
    taken in the complete absence of all jurisdiction." (McCluskey v. Roberts).
  - Eleventh Amendment (L181-189): immunity for the State and "arms of the state"; New York
    "has not consented to § 1983 suits in federal court"; probate courts are part of the New
    York State Unified Court System, "unquestionably an arm of the State" (Dodd quoting Gollomp).
  - Jurisdiction (L195-217): court must notice jurisdiction on its own motion; "When subject
    matter jurisdiction is lacking, dismissal is mandatory"; federal question (§ 1331) or
    diversity with amount in controversy over $75,000 (§ 1332); complete diversity "only if
    there is no plaintiff and no defendant who are citizens of the same State."
  - Supplemental jurisdiction (L225-237): § 1367(a) text; § 1367(c) discretion; "[W]hen the
    federal-law claims have dropped out of the lawsuit in its early stages and only state-law
    claims remain, the federal court should decline the exercise of jurisdiction by dismissing
    the case without prejudice." (Carnegie-Mellon).
  - Appointment of counsel (L247-261): "no constitutionally guaranteed right to the assistance
    of counsel in a civil case"; no "brightline test"; threshold "whether the indigent’s claims
    seem likely to be of substance"; may be denied if "chances of success are highly dubious";
    then the Hodge factors; "each case must be decided on its own facts."
- Amendments or contradictions (internal to D07; stated as found, not resolved):
  - Name forms: "Judge Randall" (L155) vs "Judge Crandall" elsewhere (L87, L101, L143, L159,
    L173, L177, L191, L219); "Herkimer County Surrogate Court" (L101) vs "Herkimer County
    Probate Court" (L181, L191); plaintiff "Mulvilhill" (L9, L35) vs mother "Mulvihill" (L93,
    L99).
  - Cross-reference: L225 says the Court "has recommended dismissal of those claims, see section
    II.B", but Section II (L245-267) is "APPOINTMENT OF COUNSEL" with no subsections; the
    federal-claim recommendations are in sections I.B-I.C (L81-191).
  - Counsel motion: body says "denied without prejudice to being renewed" (L267); Conclusion
    says "DENIED" (L275) without that qualifier.
- Coverage: FULL. Read L1-298 in three chunks (L1-120, L120-239, L239-298) plus a check of
  L290-298 for trailing text and targeted greps. Remaining unread: none. Missing source text:
  none known (intake: complete capture; extraction equals original after NFKC; no ellipsis
  change in D07). Spot-checks: page headers "- 1 -" to "- 18 -" and footers Page 1 to Page 18
  of 18 consecutive; tables not applicable; footnotes 1-4 located (fn. 1 L41, fn. 2 L63, fn. 3
  L239, fn. 4 L281-283; reference marks run into text: "Compl.1" L35, "(B).2" L55, "claims.3"
  L237, "(14)4" L279). Original `docs/` file spot-checked by search: 18 "Page N of 18"
  footers; fn. 4 "seventeen days" sentence at docs line 279 = text L281; the two "..." in the
  § 1367(c) quotation (L237) are literal periods in the original (docs line 235), not a
  converted U+2026.

## D08 - Howard v. Wellpath, LLC et al., E.D. Pa. Civil Action No. 24-CV-4839, Memorandum (dated Sept. 17, 2026; filed 09/18/26)

- Source: local D08 = platform Doc 6 | `docs/uscourts_paed_2_24_cv_04839_0.txt` -> `text/D08.txt`
  (284 lines, 40,712 chars per manifest; plain text with page numbers and footers "Case
  2:24-cv-04839-JLS Document 42 Filed 09/18/26 Page N of 19" from L33 (Page 1) to L283
  (Page 19); several footers are run into body sentences, e.g. L71, L91, L153, L161, L171).
  Extraction report: one U+2026 ellipsis in the docs/ original became "..." (located at L253,
  "standard...”" in the Pa. R. Civ. P. 1042.3(a) quotation; the other "..." spans such as
  ". . ." are spaced periods in the original text).
- Written or submitted by: the court - "IN THE UNITED STATES DISTRICT COURT / FOR THE EASTERN
  DISTRICT OF PENNSYLVANIA" (L3-5; L3 begins with a stray "7": "7IN THE UNITED STATES DISTRICT
  COURT"). Judge line: "SCHMEHL, J. - /s/ JLS SEPTEMBER 17, 2026" (L23); case initials "JLS"
  in footers. No first name for Schmehl appears.
- Type, date, edition: "MEMORANDUM" (L21) on motions to dismiss; dated "SEPTEMBER 17, 2026"
  (L23) while every footer reads "Filed 09/18/26", "Document 42". Ends "An appropriate Order
  follows." (L281); the Order itself is not in the text (negative evidence). Dispositions are
  phrased in the future tense ("will be granted", "will be denied"). Single edition.
- Period covered: calendar dates only. Medical/grievance history from 2010 to Feb. 2, 2026;
  prior case decided Feb. 24, 2023; this case stayed Dec. 19, 2024 to May 21, 2025; Memorandum
  Sept. 17, 2026. The Complaint's filing date is not printed (Complaint is ECF No. 2, fn. 2 L49).
  - Dated events (chronological, as printed):
    - "since 2010": SCI Phoenix medical staff familiar with symptoms "dating back to treatment
      received since 2010"; "intestinal pain for thirteen years" (prior case, L171).
    - February 2021: "two severe heart attacks" (L45).
    - 2022: Temple University gastroenterologist diagnosed "a small intestinal infection and
      prescribed antibiotics in 2022" (L171); April 2022: Dr. Letizio said "they would contact
      the gastroenterologist" (L171).
    - Feb. 24, 2023: prior case Howard v. Wellpath, No. 22-3241, 2023 WL2226797, at *1
      (E.D. Pa. Feb. 24, 2023) dismissed deliberate-indifference claims against Wellpath, Dr.
      Letizio, Huner and Dr. Bora "for failure to state a claim" (L149-151, L169-171).
    - August 2023: a family member contacted the DOC Central Office (L45 prints "August 2023"
      with fn. 4 marker run in as "August 20234"); fn. 4 (L53): "It appears based on the
      chronological events as described that the contact with the Central Office was in 2023,
      not August 2024 as stated, and this was a typographical error."
    - Nov. 29, 2023: appointment with Dr. Steven R. Stanek, Einstein Gastroenterology (L59,
      L259; "in November 2023" L177).
    - Narrative order at L61 (printed dates are not in calendar order): Dec. 6, 2024 (as
      printed) Howard "wrote Quigley a letter"; Apr. 11, 2024 (as printed) response "from
      Erica Benning, the Director of the Bureau of Health Care Services". See contradiction (a).
    - Sept. 6, 2024: blood test, hemoglobin dropped (fn. 8, L105).
    - Sept. 20, 2024: grievance filed over Dr. Letizio's denial of the specialist (fn. 8, L107).
    - Dec. 19, 2024: Court "entered an Order staying this case" (ECF No. 7) after Wellpath's
      Chapter 11 petition in the U.S. Bankruptcy Court for the Southern District of Texas
      (fn. 1, L27).
    - May 1, 2025: confirmation of Wellpath's plan of reorganization (fn. 1, L27).
    - May 21, 2025: stay lifted (ECF No. 8) (fn. 1, L27-29).
    - June 20, 2025: CAT scan; "did not receive an appointment with the disease specialist";
      scan "revealed two large lumps on his colon" (fn. 8, L109).
    - Feb. 2, 2026: "MRI, colonoscopy, and evaluation by a gastroenterologist" (fn. 8, L109).
    - Sept. 17, 2026: Memorandum dated (L23); filed 09/18/26 (footers).
  - Undated filings: Bankruptcy Motion (ECF No. 16); Wellpath and Dr. Letizio motion (ECF No.
    21); Huner motion (ECF No. 27); Howard's opposition (ECF No. 41) (L25).
- Entities and aliases:
  - Plaintiff: Leon J. Howard (caption "LEON J. HOWARD" L7), pro se (L25), "an inmate at SCI
    Phoenix" (L41), "a convicted prisoner" (fn. 5, L71).
  - Defendants (caption "WELLPATH, LLC, et al." L17): Wellpath, LLC (“Wellpath”) (L25), "a
    private entity" (L195); "SCI Phoenix Wellpath Medical Director Dr. Anthony Letizio" (L25),
    "a Wellpath employee" (L195), later "no longer employed with SCI Phoenix" (fn. 6 L87; fn. 8
    L109); "SCI Phoenix Chief Healthcare Administrator Britney Huner" (L25; "Chief Health Care
    Administrator" L241), a "non-medical provider" (fn. 9 L251), "not licensed medical provider"
    (fn. 10 L253). Individual defendants sued "in their respective individual and official
    capacities" (L25). Mapper count: 3 defendants.
  - Non-parties: Health Service Specialist Shannon Quigley (L47; "Quigley" L61); Erica Benning,
    "the Director of the Bureau of Health Care Services" (L61; "Ms. Benning" L63, L241; "a third
    party" L243); Dr. Steven R. Stanek, gastroenterologist at Einstein Gastroenterology (L59,
    L177, L259); "Dr. Delgado Daza Alejandro, a “good” disease specialist, at the Einstein
    Infectious Disease Center" (L59) = "Dr. Alejandro ... at the Einstein Infection Disease
    Center" (L259; "disease specialist Dr. Alejandro" L105); Dr. Bora, "another medical
    provider", defendant only in the prior case (L169, L177); Temple University
    gastroenterologist (L171, L177); "a physician’s assistant" (L47); "a family member" (L45);
    "the new medical director" (L109); Department of Corrections (“DOC”) Central Office (L45,
    L239); "the Commonwealth" (L187-191); United States Bankruptcy Court for the Southern
    District of Texas (L27).
  - Filing aliases: "the “Bankruptcy Motion”" = ECF No. 16 (L25); Complaint (“Compl.”) = ECF
    No. 2 (fn. 2, L49); prior case "Howard v. Wellpath, No. 22-3241 (E.D. Pa.)" (L77-79,
    L149) cited short as "Howard, 2023 WL2226797" (L171).
- Tables: not applicable (no tables in D08).
- Lists:
  - Symptoms (L41): "fatigue, pain, muscle and joint aches, weakness, bowel movement
    complications, tongue infections, and significant weight loss".
  - Pennsylvania issue-preclusion conditions, numbered (1)-(5) (L157; last item "(5) whether
    the determination in the prior proceeding was essential to the judgment").
  - Claim-preclusion elements, three (L165).
  - Rouse deliberate-indifference ways, three (L203).
  - Supervisory-liability ways, two (L231-237).
  - Conclusion items (L267-279).
- Forecasts, guidance, deadlines, effective dates: no deadline with a day count or calendar date.
  "The Court will direct Dr. Letizio to file a responsive pleading as to remaining claim" (L271-
  279) - no time period stated. Stay/lift dates in fn. 1 (L27-29). No objection period, appeal
  notice or amendment deadline (negative evidence).
- Hedged claims (claim / hedge / what it attaches to):
  - Dr. Stanek's reported statement: "he may have an undiagnosed intestinal disease that had been
    overlooked" (L59; repeated L259) - "may" belongs to the doctor's reported opinion.
  - Fn. 4 (L53): "It appears ... that the contact with the Central Office was in 2023, not August
    2024 as stated, and this was a typographical error."
  - Fn. 6 (L87-89): injunctive request "is likely a request to order Dr. Letizio to schedule his
    appointment with the disease specialist"; "it appears Howard has received the additional
    treatment requested" - the result ("this request will be denied as moot") is unhedged.
  - L241: "it is not clear if Huner received the letter from Benning or even knew about Dr.
    Letizio’s denial"; L245 "He also appears to attempt to impose liability upon Huner based on
    general allegations"; L243 "As pled, this does not sufficiently allege Huner was personally
    involved".
  - L259: "Although it is unclear why Dr. Letizio denied Dr. Stanek’s order ..., the deliberate
    indifference claim based on the allegations as pled may proceed past this stage" - "unclear"
    attaches to Letizio's reason; "may proceed" is permission; L263 states firmly "the
    deliberate indifference claim against him is sufficient to proceed to discovery".
  - L177: "the issues raised here cannot be determined from the face of the Complaint as
    “identical”"; L151 "In an abundance of caution, the Court will address both issue preclusion
    and claim preclusion."
  - Fn. 9 (L251): counterfactual "even had Howard alleged that Huner received the letter ... she
    still could not be held liable"; quoted rule "a nonmedical prison official will generally be
    justified in believing that the prisoner is in capable hands".
  - Fn. 10 (L253): "In any event, a state law negligence claim against her would be barred by
    sovereign immunity" (conditional; Howard pleads negligence only against Wellpath).
  - Fn. 8 (L105): post-complaint timeline "included for background purposes only" because
    "allegations filed outside the Complaint cannot be considered for the underlying
    plausibility of the claims".
  - Fn. 11 (L273): "It is also worth noting that ... Dr. Letizio was well aware of Howard’s
    complications" (stated without a hedge).
- Rounded prose beside exact figures: "nearly two years after he saw the Temple University
  gastroenterologist" (L177) beside "in 2022" (L171) and "November 2023" (L177); "for thirteen
  years" and "since 2010" (L171), both reported from the prior case. No money amounts or
  percentages in D08.
- Notes:
  - Footnotes: fn. 1 (L27-31) bankruptcy stay and lift; fn. 2 (L49) Complaint ECF No. 2, CM/ECF
    pagination; fn. 3 (L51) "duplicative paragraph numbers in the initial pages of the Complaint,
    these allegations begin on page 3"; fn. 4 (L53) 2023 vs "August 2024 as stated"; fn. 5
    (L71, L83-85) Fourteenth Amendment cited but "as a convicted prisoner, the Eighth Amendment
    governs his claims" (Kingsley; Jacobs; Moore v. Luffey; Natale); fn. 6 (L87-89) injunctive
    relief moot; fn. 7 (L91, L101) certificate of merit: "In light of recent United States
    Supreme Court precedent, the motion will be denied to the extent he seeks dismissal on this
    basis. See Berk v. Choy, 607 U.S. 187, 189 (2026) (holding state law requiring submission of
    an affidavit from a medical professional attesting to the suit’s merit has no application in
    federal court)"; Talley v. Pillai; fn. 8 (L103-109) updated timeline; fn. 9 (L251) non-medical
    provider; fn. 10 (L253, L259) negligence/sovereign immunity/Rule 1042.3(a) (Poteat v. Lydon;
    Kidd v. Pennsylvania; Rightmyer v. Philly Pregnancy Ctr.); fn. 11 (L273) Letizio "well
    aware". Fn. 10's text continues at L259 after the Letizio paragraph (page-break interleaving).
  - Claims pleaded: Eighth Amendment deliberate indifference to serious medical needs against
    all Defendants (Compl. ¶¶ 16-27, L65-69); "a state law negligence claim against Defendant
    Wellpath based on the theory of respondent superior" (¶¶ 28-29, L69-75); Fourteenth
    Amendment deliberate indifference cited (Compl. ¶ 1, fn. 5); relief: "unspecified injunctive
    relief" and "compensatory and punitive damages" (¶¶ 30-33, L75).
  - Defendants' arguments: issue preclusion from the prior case (L77-79); implausible Eighth
    Amendment claim (L79); Huner: Eleventh Amendment for official-capacity claims (ECF No. 27 at
    7-8, L81; "at 7-9" L183) and not "persons" (L183-185); Wellpath: no respondeat superior, no
    policy or custom (ECF No. 21 at 10-13, 17-19, L81); certificate of merit under Pa. R. Civ.
    P. 1042.3 (L81, fn. 7).
  - Plaintiff's positions: claims are new and post-date the prior case (ECF No. 41 at 2-4,
    L95); concedes Wellpath: "Claims against the Defendants should not be dismissed or result in
    any of the Defendants being dismissed from the comp[laint] (with the exception of
    Wellpath)." (L95); "Howard does not respond" to Huner's official-capacity argument (L185);
    does not "state her name once throughout his response" (L215).
  - Dispositions (who / claim / ground / location):
    - Bankruptcy Motion (ECF No. 16): "denied as moot" (L25).
    - Preclusion (issue and claim) as to all moving Defendants: "preclusion is inapplicable and
      Defendants’ motions will be denied as to this ground" (L177).
    - Huner, official capacity: granted - claims are against the Commonwealth, barred by the
      Eleventh Amendment and not a "person" (L187-191).
    - Dr. Letizio, official capacity: "not cognizable because Wellpath is a private entity";
      duplicative of conceded Wellpath claims; "also dismissed" (L195-197).
    - Huner, Eighth Amendment: no personal involvement or supervisory liability; "her motion to
      dismiss this claim will be granted" (L247-249).
    - Dr. Letizio, Eighth Amendment: survives - "Dr. Letizio has not met his burden for
      obtaining dismissal on the merits, and the deliberate indifference claim against him is
      sufficient to proceed to discovery" (L263).
    - Wellpath: motion "granted as to the claims against Wellpath" (L269), following Howard's
      concession (L95, L197).
    - Certificate-of-merit ground: motion denied "to the extent he seeks dismissal on this
      basis" (fn. 7, L91).
    - Injunctive relief: "denied as moot" (fn. 6, L89).
    - Conclusion (L267-279): "Huner’s Motion to Dismiss will be granted and the claims against
      her will be dismissed with prejudice"; Wellpath/Letizio motion "granted in part and denied
      in part"; "Huner and Wellpath will be terminated as a defendant in this case. All official
      capacity claims and Fourteenth Amendment claims will also be dismissed."; Dr. Letizio to
      file a responsive pleading on the remaining "Eighth Amendment medical indifference claim".
    - Negative/exclusion evidence: "with prejudice" is stated only for Huner (L267); no
      prejudice label is given for the Wellpath dismissal, Dr. Letizio's official-capacity
      dismissal or the Fourteenth Amendment dismissal; no leave to amend is mentioned. "The
      Complaint in this case does not reallege any factual allegations occurring in 2022" (L171);
      "Importantly, it was not determined that Howard did not actually have an intestinal
      disorder as Defendants insinuate." (L171); "Howard only alleges the negligence claim against
      Wellpath" (fn. 10, L253). No Younger, Rooker-Feldman or supplemental-jurisdiction
      discussion.
  - Numeric figures (exact wording): "two severe heart attacks" (L45); "two large lumps on his
    colon" (L87, L109); "thirteen years" (L171); "nearly two years" (L177); "Chapter 11" (L27);
    "Page 1 of 19" ... "Page 19 of 19"; "Document 42"; ECF Nos. 2, 7, 8, 16, 21, 27, 41.
  - Statutes and rules cited: 42 U.S.C. § 1983 (L143 ff.); Fed. R. Civ. P. 12(b)(6) (L25, L99);
    Pa. R. Civ. P. 1042.3 and 1042.3(a) (L81, L253); § 1303.512 (in Rightmyer parenthetical,
    L259); Chapter 11 of the Bankruptcy Code (L27); Eighth, Fourteenth and Eleventh Amendments.
  - Selected cited cases (location): Ashcroft v. Iqbal (L113, L219, L247); Bell Atl. Corp. v.
    Twombly (L113); Farmer v. Brennan (L201); Monell (L187-189); Kentucky v. Graham (L187,
    L197); West v. Atkins (L143); Rode v. Dellarciprete (L145, L219-221, L225); Spruill v.
    Gillis (L207, L251); Berk v. Choy, 607 U.S. 187 (2026) (fn. 7); DiFraia v. Ransom, 171
    F.4th 622, 630 (3d Cir. 2026) (L207); Kokinda v. Pa. Dept. of Corrections (L175,
    distinguished); Beasley v. Howard (L159-163) - a case name containing "Howard" that is not
    the plaintiff's prior case.
- Operative definitions, rules and scope exceptions (verbatim tests):
  - Rule 12(b)(6) (L99-125): "A 12(b)(6) motion tests the sufficiency of the allegations
    contained in the complaint."; plausibility "more than a sheer possibility"; "defendant bears
    the burden of showing that no claim has been presented" (Hedges); materials considered
    (Mayer v. Belichick); pro se construed liberally (Vogt).
  - Affirmative defenses (L131-137): dismissal "only appropriate at the pleading stage when the
    “defense is apparent on the face of the complaint.”" (Wisniewski); burden on defendant.
  - § 1983 (L143-145): "must allege the violation of a right secured by the Constitution and
    laws of the United States, and must show that the alleged deprivation was committed by a
    person acting under color of state law." Personal involvement required (Rode).
  - Issue preclusion, Pennsylvania (L157): "(1) the issue decided in the prior adjudication was
    identical with the one presented in the later action; (2) there was a final judgment on the
    merits; (3) the party against whom issue preclusion is asserted was a party or in privity
    with a party to the prior adjudication; and (4) the party against whom it is asserted has had
    a full and fair opportunity to litigate the issue in question in a prior action; and (5)
    whether the determination in the prior proceeding was essential to the judgment."
  - Claim preclusion (L159-167): "(1) a final judgment on the merits in a prior suit involving
    (2) the same parties or their privies and (3) a subsequent suit based on the same cause of
    action." Covers claims that "could have asserted"; turns on "essential similarity of the
    underlying events".
  - Official capacity (L187-197): official-capacity suits are suits against the entity
    (Graham); Commonwealth shielded by Eleventh Amendment and not a "person"; official-capacity
    claims "inapplicable to suits against private parties where the entity is also susceptible
    to suit" (Kreis).
  - Eighth Amendment (L201-211): deliberate indifference requires the official "knows of and
    disregards an excessive risk to inmate health or safety" (Farmer); serious medical need =
    "diagnosed by a physician as requiring treatment or one that is so obvious that a lay person
    would easily recognize the necessity for a doctor’s attention" (Lanzaro); properly alleged
    "where the prison official (1) knows of a prisoner’s need for medical treatment but
    intentionally refuses to provide it; (2) delays necessary medical treatment based on a
    non-medical reason; or (3) prevents a prisoner from receiving needed or recommended medical
    treatment." (Rouse); malpractice and "mere disagreement" insufficient (Spruill; Durmer).
  - Personal involvement / supervisory liability (L219-237): "participation in or actual
    knowledge of and acquiescence"; knowledge "must be actual, not constructive"; "in charge of"
    allegations insufficient (Saisi); no respondeat superior; two ways - policy/practice/custom
    with deliberate indifference, or participated/directed/knew and acquiesced (Barkes).
  - Non-medical officials (fn. 9, L251): not deliberately indifferent where the prisoner is
    under medical staff care (Spruill; Stewart; Carter v. Smith).
  - Certificate of merit (fn. 7, fn. 10): Pa. R. Civ. P. 1042.3 inapplicable in federal court
    per Berk v. Choy (2026); Rule 1042.3(a) reaches "a licensed professional".
- Amendments or contradictions (internal to D08; stated as found, not resolved):
  - (a) Letter/response order: "Howard wrote Quigley a letter on December 6, 2024" and "received
    a response to his letter on April 11, 2024, from Erica Benning" (both L61); the printed
    response date is earlier than the printed letter date; the document does not comment.
  - (b) Central Office contact: body L45 prints "August 2023" (marker "20234"); fn. 4 (L53) says
    the Complaint stated "August 2024" and treats it as a typographical error for 2023.
  - (c) Injunctive relief: fn. 6 says "it appears Howard has received the additional treatment
    requested" and treats the request (likely a specialist appointment) as moot (L87-89); fn. 8
    says after the June 20, 2025 CAT scan he "did not receive an appointment with the disease
    specialist" (L109).
  - (d) Name/citation variants: "Einstein Infectious Disease Center" (L59) vs "Einstein
    Infection Disease Center" (L259); "Chief Healthcare Administrator" (L25) vs "Chief Health
    Care Administrator" (L241); "respondent superior" (L75) vs "respondeat superior" (L81,
    L225); "ECF No. 27 at 7-8" (L81) vs "at 7-9" (L183); "Kentucky v. Graham, 473 U.S. 159,
    165-66" (L187) vs "Graham, 473 U.S. at 105" (L197); "Rode v. Dellarciprete, 845 F.2d 1195,
    1207" (L145) vs "Rode, 845 F.3d at 1207" (L221).
  - (e) Prior case parties: the prior case named Wellpath, Dr. Letizio, Huner and Dr. Bora
    (L169); "the same parties are sued here, with the exception of Dr. Bora" (L177).
  - (f) Fn. 7 speaks of Wellpath's motion as "to the extent he seeks dismissal" (pronoun as
    printed, L91).
  - (g) Date pair: dated "SEPTEMBER 17, 2026" (L23) vs "Filed 09/18/26" (all footers).
- Coverage: FULL. Read L1-284 in three chunks (L1-110, L110-219, L219-284) plus a check of
  L278-284 for trailing text and targeted greps. Remaining unread: none. Missing source text:
  none known (intake: complete capture; extraction equals original after NFKC). Spot-checks:
  footers Page 1 to Page 19 of 19 consecutive; tables not applicable; footnotes 1-11 located
  (fn. 1 L27, fn. 2 L49, fn. 3 L51, fn. 4 L53, fn. 5 L71/L83-85, fn. 6 L87-89, fn. 7 L91/L101,
  fn. 8 L103-109, fn. 9 L251, fn. 10 L253/L259, fn. 11 L273). Footnote text is interleaved
  with body text at page breaks (fn. 5 at L71 then L83-85; fn. 7 at L91 then inside L101; fn. 10
  at L253 then inside L259), so body sentences at L101 and L259 contain footnote text mid-line.
  Original `docs/` file spot-checked by search: 19 "Page N of 19" footers; the U+2026 is at
  docs line 251 = text L253 (fn. 10); "7IN THE UNITED STATES DISTRICT COURT" (docs line 1),
  "August 2023" (docs line 43) and the "December 6, 2024"/"April 11, 2024" pair (docs line 59)
  are as printed in the original, not extraction artefacts.

## Part c read ledger

| Doc | Lines | Chunks read | Unread | Missing source text | Original spot-check |
|---|---|---|---|---|---|
| D06 (Doc 9) | 1-868 | 1-120, 120-239, 239-358, 358-467, 467-566, 566-665, 665-868 | none | none known | 46 footers; fn. 7; no U+2026 |
| D07 (Doc 3) | 1-298 | 1-120, 120-239, 239-298 | none | none known | 18 footers; fn. 4; literal "..." L237 |
| D08 (Doc 6) | 1-284 | 1-110, 110-219, 219-284 | none | none known | 19 footers; fn. 10 U+2026 L253 |

Tables: none in D06-D08 (not applicable). Charts/images: none. Gaps: none for D06-D08.

## Shared ground candidates (part c)

Locations only; the other mappers own the D01-D05, D09 and D10 entries. Lines for other
documents come from targeted greps of `text/Dnn.txt`, not full reads.

- Decision/filing dates, all September 2026 (footer "Filed" dates): D06 dated and filed Sept.
  20, 2026 (L855-857; footers); D07 dated and filed Sept. 15, 2026 (L293; footers); D08 dated
  "SEPTEMBER 17, 2026" (L23) but filed 09/18/26 (footers). Other footers: D01 09/14/26 (L41),
  D02 09/18/26 (L31), D03 09/17/26 (L47), D04 09/21/26 (L37), D05 09/18/26 (L39), D09 09/14/26
  (L63), D10 09/16/26 (L31).
- Pro se plaintiffs: D06 L39; D07 L25, L35; D08 L25. "pro se" also occurs in D01, D02, D05, D09.
- Eleventh Amendment / sovereign immunity: D06 L325, L397-457, L799-815; D07 L181-191; D08
  L81, L183-191. Elsewhere: D01 L79-127; D02 L81-181, L267; D03 L161-193, L503-505; D04
  L165-237, L345-455; D05 L211; D09 L135; D10 L193-209.
- Ex parte Young: D06 L301, L325, L399, L411-455, L813; D01 L87-103; D02 L173.
- Pennhurst: D06 L419, L455; D01 L81, L101, L123.
- Will v. Mich. Dep’t of State Police ("person" under § 1983): D06 fn. 5 L463; D02 L161. The
  same "not a person" point without that cite: D08 L183-191.
- Official-capacity claims: D06 L397-457, L805-815; D08 L179-197, L271; D01 L25, L79, L93; D02
  L153-181, L259; D04 L389-453; D09 L135-171.
- Gollomp v. Spitzer, 568 F.3d 355 (New York court system an arm of the State): D06 L429
  (pin 366-67), L809 (pin 368); D07 L187 (pin 368, quoted through Dodd v. O’Sullivan).
- Judicial immunity: D06 L459-483 (Mireles; Bliven; Kellogg) and quasi-judicial immunity
  L817-831; D07 L157-191 (Pierson; Stump; Bliven; McCluskey). Bliven v. Hunt, 579 F.3d 204:
  D06 L473, L479-481; D07 L167, L169. Two-circumstance exception worded differently: D06 L473
  vs D07 L169. No judicial-immunity, Mireles, Bliven or Gollomp hits in D01-D05, D09, D10.
- Iqbal/Twombly plausibility: D06 L281-289, L553, L765, L839-841; D07 L59-79; D08 L113,
  L219, L247; D02 L121-125, L195; D03 L169-211; D04 L123-131, L295, L313, L383; D09 L111-113;
  D10 L67-69.
- Private lawyers and color of state law: D06 L573-609 (Polk Cnty. v. Dodson L581); D10 L231
  (Polk County v. Dodson; appointed attorney). State action: D07 L129-155; D08 L143 (West v.
  Atkins); D05 L63, L169.
- Personal involvement: D07 L153-155; D08 L145, L213-249; D02 L199, L239; D09 L137-161; D10 L233.
- Prisoner medical care / Eighth Amendment deliberate indifference: D08 L65-69, L199-263; D09
  L89-171; D02 L49, L209; D05 L37 (Eighth Amendment mention).
- Pennsylvania DOC: D08 L45 ("Central Office for the Department of Corrections (“DOC”)"; SCI
  Phoenix L25, L41); D09 L55 ("Pennsylvania Department of Corrections (“DOC”)"), SCI Forest
  L73. Same "DOC" short form, different prisons.
- "the Commonwealth" means different entities: D08 L187-191 (Pennsylvania); D10 L23, L33
  ("Commonwealth of Puerto Rico").
- ADA: D06 Title II (L137-141, L183, L485-555, L649-655); D09 L93 ("Americans with Disabilities
  Act, 42 U.S.C. §§ 12101 et seq. (“ADA”) failure to accommodate"), L137-171; D05 L231 (in a
  citation parenthetical).
- 42 U.S.C. § 1985: D06 L153-155, L181, L611-647; D01 L101; D02 L105, L193, L247; D04 L295;
  D05 L151.
- Title VII: D07 L83-87, L219 (form complaint; no employment relationship apparent); D03
  L139-507.
- Preclusion: D08 L77-79, L131-177 (issue and claim preclusion; prior case No. 22-3241); D10
  L177-195, L273-293 (res judicata/collateral estoppel, with Rooker-Feldman L177, L195,
  L273-277, L345, L367). Rooker-Feldman does not appear in D06-D08.
- Monell: D08 L187-189 (inside the Kentucky v. Graham quotation); D04 L269-295, L461-463.
- Magistrate judges: D07 report-recommendation (L33, L39-47 L.R. 72.3; L279-291 § 636(b)(1),
  Fed. R. Civ. P. 72); D05 L89 (§ 636(b)(1)(A), Fed. R. Civ. P. 72(a)).
- 28 U.S.C. § 1915: D07 L53-55 (§ 1915(e)(2)(B)); D01 L47 (defendants move under § 1915).
- Amended pleadings and earlier pleadings: D06 L85-101 (amended complaint "ordinarily
  supersedes the original"; pro se exception; original exhibits considered); D01 L45-47 (second
  amended complaint "neither refers to nor incorporates any earlier pleadings"; analysis
  "confined to the second amended complaint").
- Fed. R. Civ. P. 12(h)(3): D06 L243; D07 L201. Not found in the other eight documents.
- Found only in D06 (greps of the other nine found none): Rule 4(m), Rule 12(b)(2), Rule
  12(b)(5), "actual notice", Younger abstention. Found only in D07 among D06-D08 and not in the
  other seven by grep: 28 U.S.C. § 1367 / supplemental jurisdiction, appointment of counsel.
- Same names, different cases or entities: "Roldan v. Fam. Ct." (D06 L515-517) vs "Roldan v.
  Racette" (D07 L279-289); "Stewart": D07 author Daniel J. Stewart (L29) vs "Stewart v. Pa.
  Dep’t of Corr." (D08 fn. 9 L251) vs "Woods v. Stewart Title Guar. Co." (D04 L145); "Woods":
  Woods Oviatt Gilman LLP (D06 L19, L65) vs "Woods v. Rondout Valley" (D07 L181) vs D04 L145;
  "Hill v. Didio" (D06 L669) vs D03 plaintiff "Duane Hill (“Lt. Hill”)" (D03 L41); "Howard":
  D08 plaintiff vs "Beasley v. Howard" (D08 L159); "Carter v. HealthPort Techs." (D06 L245) vs
  "Carter v. Smith" (D08 L251); "Mitchell v. Fishbein" (D06 L829) vs "Mitchell v. Connecticut
  Region 14 Dist. Prob. Ct." (D07 L187); "Williams v. Marinelli/Marinello" (D06 L419-421,
  L809), "Neitzke v. Williams" (D07 L63), "Williams v. Runyon" (D08 L137).
- Parties of D06-D08 (Hernandez, Mulvilhill, Kuchler, Crandall, Howard, Wellpath, Letizio,
  Huner, Suffolk, Herkimer, Montefusco, Pressler) and judges Choudhury and Schmehl do not
  appear in D01-D05, D09 or D10 (grep). No document in D06-D08 cites, amends or responds to
  another bundle document.
- 2026 authorities cited: D06 Kellogg v. Nichols, 170 F.4th 20 (2d Cir. 2026) (L473); Abadi v.
  Greyhound Lines (2d Cir. Apr. 20, 2026) (L621-623); Gibson v. Trs. of Columbia Univ.
  (S.D.N.Y. Jan. 15, 2026) (L85). D07 Howe v. First Am. Title Agency (E.D. Mich. Mar. 9, 2026)
  (L147). D08 Berk v. Choy, 607 U.S. 187 (2026) (fn. 7 L91); DiFraia v. Ransom, 171 F.4th 622
  (3d Cir. 2026) (L207).
- Deadlines and counting rules: D06 fixed calendar dates for the Bank Defendants (Oct. 2 and
  Oct. 9, 2026; fn. 2 L91, L849-853) and Rule 4(m) 90 days (L87, L275); D07 objections in
  fourteen days, seventeen if served by mail, weekend/holiday roll-forward (L279-283); D08 sets
  no dated deadline (responsive pleading, no period stated, L271-279).
- Prejudice wording: D06 never labels its dismissals "with" or "without prejudice" (only Rule
  4(m) quotation and the Jan. 26, 2026 denial of leave to amend); D07 does not label the
  recommended dismissal (counsel motion "denied without prejudice to being renewed" L267); D08
  "with prejudice" only for Huner (L267). Other documents: D09 L171 "dismissed with prejudice"
  (ADA claim); D05 L231 "dismissed without prejudice" (in a citation parenthetical).
