# aq-01547 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Conventions: `Lnn` = line nn of `text/Dnn.txt`; `p.N` = the printed page. For every document the
`docs/` original line = text line - 2 (verified on seven footnotes and on the normalized lines).
Quotations below use straight quotes and may be shortened; copy evidence verbatim from `docs/`.

## Bundle

- What it is: seven U.S. federal court rulings issued July-September 2026: six district-court
  orders/opinions and one published Ninth Circuit opinion. All concern the False Claims Act (FCA).
  The topics are qui tam pleading (presentment, falsity, scienter, materiality), reverse-FCA
  "obligation", the "alternate remedy" provision 31 U.S.C. § 3730(c)(5), and FCA anti-retaliation
  § 3730(h). Two rulings also cover NDAA whistleblower retaliation, 41 U.S.C. § 4712. Of the
  seven, five are qui tam captions (D01, D02, D05, D06, D07) and two are employee-retaliation
  suits with no United States party (D03, D04).
- Documents: 7 (ids from `text/manifest.json`; local ids are alphabetical by file and differ from
  the task page's numbers):
  D01 = Doc 7 (uscourts_akd_3_24_cv_00276_1.txt), D02 = Doc 4 (uscourts_ca9_25_249_0.txt),
  D03 = Doc 5 (uscourts_dcd_1_26_cv_01267_0.txt), D04 = Doc 6 (uscourts_gand_1_25_cv_00388_0.txt),
  D05 = Doc 2 (uscourts_mdd_8_23_cv_00700_0.txt), D06 = Doc 1 (uscourts_txsd_4_23_cv_01792_2.txt),
  D07 = Doc 3 (uscourts_vtd_2_24_cv_00617_6.txt).
- Gaps: none in readable text. All seven texts were read line by line, start to finish (ledger
  in each Coverage line). No PDFs or page images, so no charts or scans. Not applicable: tables
  (none in any document). Unresolved visual items, because the originals are text captures with
  the same damage:
  (a) D04's signature line, garbled "MICH " K E L L . BROW N" (L196-197);
  (b) D07's signature and dating line, garbled "1'cDated ... this /b day of September, 2026."
      and "Chnstina Reiss,Judg~" (L394-395). The day of signing is illegible; the footer gives
      "Filed 09/10/26";
  (c) D07's OCR damage to symbols (pilcrows printed as ",r", ",i", "~" or "iJ"; "l" for "1" in
      "(a)(l)(G)" and "12(b)(l)"). It is listed under D07.
- Extraction spot-checks:
  - Page counts from the running headers and footers: D01 32 (32 footers plus 31 headers =
    63 "Page N of" hits), D02 22 (slip-opinion headers pp.2-22; p.1 is the caption page), D03 22,
    D04 27, D05 16, D06 19, D07 26.
  - Tables: not applicable. As a substitute, two enumerated lists were checked against the
    originals: D07 reserved claim "a." (docs L161 = text L163) and D05 "(Count Twenty-Three)"
    (docs L60 = text L62).
  - One footnote per document, each identical to the original at text line - 2:
    D01 fn 2 (L21), D02 fn 2 (L99), D03 fn 7 (L199), D04 fn 5 (L104), D05 fn 4 (L220),
    D06 fn 1 (L22), D07 fn 2 (L178).
  - NFKC/whitespace normalization (15 characters):
    - D01 L391 "safe‐harbor" is U+2010 in the text and U+2011 in the original (docs L389).
    - D04 L110 "sets forth...mere": the original (docs L108) has U+2026.
    - D06 has 13 U+2026 in the original, which the text renders as "..." (or "...." where the
      original has an ellipsis plus a period): text L73 (1), L94 (1), L103 (3), L108 (1),
      L125 (3), L131 (1), L143 (1), L149 (1), L169 (1). The docs lines are 71, 92, 101, 106,
      123, 129, 141, 147 and 167.
- Provenance:
  - `notes/intake.json`: capture_sha256 0ba3a536...cc42; all seven have "incomplete": false,
    gap_characters 0 and matches_capture true.
  - The manifest sha256 values equal the intake captured/source hashes (D01 7779abe6, D02 966a3eaa,
    D03 6addceaf, D04 7d5b4bbf, D05 0959e717, D06 4d73055b, D07 d76deee2). Manifest method is
    "text" and pages is null.
  - No recovered-source history. The task-page bundle overview in the capture was not used.

## D01 - Feduccia v. I.C.E. Services, Inc., et al. (D. Alaska): Order on Second Motion to Dismiss

- Source: docs/uscourts_akd_3_24_cv_00276_1.txt | 32 pp. | task page Doc 7 | text L1-L560.
  Header "Case No. 3:24-cv-00276-SLG ... Page N of 32"; footer "Document 71 Filed 09/30/26".
- Written or submitted by: U.S. District Court, District of Alaska, signed "/s/ Sharon L. Gleason,
  United States District Judge" (L554-555). "DATED this 30th day of September, 2026, at Anchorage,
  Alaska" (L552).
- Type, date, edition: an order on Defendants' Motion to Dismiss Relator's Amended Complaint under
  Rules 12(b)(6) and 9(b) (Docket 54; briefing at Dockets 54, 57, 60, fn 1 L19).
  - The Amended Complaint is Docket 50; its sealed version with exhibits is Docket 66 (fn 2 L21).
  - The prior order on the first motion to dismiss is Docket 49. It is summarized in this order
    but is not in the bundle (L16-17, L135, L339).
  - Single edition.
- Period covered: PPP events April 2020-July 2021; litigation December 2024-September 2026;
  calendar dates. Also mentioned: "first quarter of 2020" revenues (L148); Pt Arctic Fund's
  "2019 Annual Report, dated March 31, 2020" (L189) and a "2020 Annual Rep." exhibit (Docket 66-4,
  fn 38 L153-154).
- Parties and roles:
  - Relator Christopher A. Feduccia (captioned "Plaintiff"; L5-6, L45).
  - Defendants Thomas J. Bourdon and I.C.E. Services, Inc. ("I.C.E."), collectively "Defendants"
    (L14).
  - The United States notified the Court of its decision not to intervene on March 17, 2025
    (Docket 12; L46).
  - Non-parties:
    - Deborah Bourdon, his spouse (L43-44).
    - I.C.E. Acquisition, Inc.
    - "PT Arctic Fund I, LP", which holds its shares through I.C.E. Acquisition (L44). Elsewhere
      "Pt Arctic Fund" or "the Fund".
    - Pt Capital, "the Manager" (L289). Its CEO, Mr. Hugh Short, sat on I.C.E.'s Board
      (L148, L234-235).
    - SBA.
  - Counsel: not listed.
- Entities and aliases:
  - Economic necessity certification:
    - "Economic Necessity Certification" (L219, L337) = "economic uncertainty certification"
      (L135-136).
    - The PPP application text (L32): "[c]urrent economic uncertainty makes this loan request
      necessary ...".
  - SBA "FAQ 31/37/46" = "Question 31/37/46" (L360-382, L441). The Loan Necessity Questionnaire is
    "(SBA Form 3509 or 3510)" (fn 111 L441).
  - Case-name variants:
    - Corinthian, 655 F.3d 984, appears under three names: "United States v. Corinthian Colleges"
      (L105), "Corinthian Colls." (L181) and "United States ex rel. Lee v. Corinthian Colls."
      (L290).
    - Winter, 953 F.3d 1108, appears as "Winter ex rel. United States v. Gardens Reg'l" (L275)
      and as "United States ex rel. Winter v. ..." (L417).
    - "Kinetic Concepts" = United States ex rel. Hartpence v. Kinetic Concepts (L400-401).
    - "Stephens Institute" = United States ex rel. Rose v. Stephens Inst. (L401-402).
    - "Sigma" / "Sigma Corp." = Island Indus., Inc. v. Sigma Corp., 151 F.4th 1003 (L482, L497).
    - "America West" = No. 84 Employer-Teamster ... v. Am. W. Holding Corp. (L309-310).
  - Two different "Lee" cases: Lee v. City of Los Angeles, 250 F.3d 668 (fn 44 L181) and
    ex rel. Lee v. Corinthian Colls. (fn 75 L290).
- Dated events:
  - CARES Act (Pub. L. No. 116-136, 2020): § 1102 created the PPP (L32).
  - March 18, 2020: Mr. Short's investor update/letter (Exhibit B) (L148, L177, L189).
  - March 31, 2020: the 2019 Annual Report (L189).
  - PPP application submitted "sometime between April 4 and April 10, 2020"; approved
    April 11, 2020; $5,682,490 disbursed April 30, 2020 (L44).
  - SBA FAQ 31 published April 23, 2020 and FAQ 37 published April 28, 2020 (L360). Fn 97 (L367)
    says the Amended Complaint "erroneously states" April 29, 2020 for Question 37 (Docket 50
    ¶ 28).
  - FAQ 31 safe harbor: loans applied for before April 23, 2020 and repaid in full by May 7, 2020
    (L374). Fn 100 (L380): "subsequently extended to May 18, 2020" (SBA FAQs as of May 9, 2024).
    Count 3 uses May 18, 2020 (L458).
  - May 13, 2020: SBA states its intent to review each loan of $2 million or more (FAQ 46)
    (L427, fn 111 L441). FAQ 46 was "deleted on July 29, 2021" (fn 111).
  - June 15, 2021: Bourdon submitted the forgiveness application; SBA approved it July 22, 2021
    (L45).
  - December 17, 2024: original Complaint (Docket 1) (L45).
  - March 17, 2025: the United States declines to intervene (L46).
  - April 22, 2025: first motion to dismiss (Docket 17) (L66).
  - November 21, 2025: first motion granted with leave to amend Counts 1, 2 and 4 (L66). Original
    Count 3, conspiracy, was dismissed with Relator's concurrence (fn 17 L75).
  - December 16, 2025: Amended Complaint with three counts (L66).
  - June 10, 2026: oral argument (Docket 67; L14). Transcript Docket 70; supplemental filings
    Dockets 68 and 69 (L170-181).
  - September 30, 2026: this order. Answer due "within fourteen (14) days" (L552, fn 139 L556).
- Figures and counts (scope):
  - Ownership of I.C.E.: Bourdon 25%, Deborah Bourdon 26%, I.C.E. Acquisition 49% (L44).
  - Relator alleges Pt Arctic Fund "effectively owned" 49% and held an option on the remaining 51%
    (L234).
  - $5,682,490 PPP disbursement (L44).
  - At December 31, 2019: about $4.5 million in cash plus an undrawn $2 million credit line, "an
    estimated $6.5 million in available liquidity" (L189). Repeated in fn 57 (L226) and fn 58
    (L236).
  - "$5.3 Million Recallable Distribution" (fn 37 L151, fn 57 L226).
  - April 2020: Pt Arctic Fund reserve capital $5.6 million and capital available to invest
    $8.4 million (L204).
  - Questionnaire required "for borrowers who obtained $2+ million" (L375); review of loans
    "greater than or equal to $2 million" (L427).
  - Bourdon's tenure: "running I.C.E. for 35 years" (Relator's brief, L289) and "(then) nearly 35
    years" (¶ 58, L336).
  - America West parenthetical: officers attended "71% and 65% respectively" of eleven board
    meetings; "four directors" on the Compensation Committee (fn 86 L327).
  - Falsity paragraphs of the Amended Complaint: ¶¶ 51-71, 83, 86-103, 118-122 (L148).
  - Footnotes: 139.
- Tables: not applicable.
- Lists:
  - FCA elements, four (L119).
  - AmerisourceBergen leave-to-amend factors, four (L531).
  - Defendants' three scienter arguments (L254).
  - Conclusion items 1-3; the last is the 14-day answer (L550-552).
- Claims and dispositions:
  - Count 1, § 3729(a)(1)(A), both Defendants: motion DENIED (L454, L550).
  - Count 2, § 3729(a)(1)(B): motion DENIED (L454, L550).
  - Count 3, § 3729(a)(1)(G) reverse FCA, against I.C.E. only (L68): GRANTED. Dismissed "with
    prejudice and without leave to amend" (L545, L551).
  - Element findings:
    - Falsity is pleaded with particularity (L220-232).
    - Scienter is adequately alleged under the "core operations" doctrine (L323-337).
    - Materiality is adequately pleaded (L437).
    - Element four (government paid out money): "no dispute" (L439).
- Forecasts, guidance, deadlines, effective dates: the safe-harbor deadlines and FAQ dates above;
  the 14-day answer deadline (L552).
- Hedged claims:
  - The omitted language "is suggestive of economic uncertainty" (L161).
  - "While Defendants are correct that these statements suggest ... economic uncertainty", the
    Amended Complaint has "many contrary allegations" (L189).
  - The annual report "may be relied upon" for purposes of the motion (L205).
  - "As alleged in the Amended Complaint, the SBA's [FAQ] suggest that the ... Certification is
    indeed 'central'" (L360).
  - "it is reasonable to infer that the SBA would not have issued the loan" (L427).
  - Mr. Short's summaries "support at least a reasonable inference" of scienter (L336).
- Alleged versus found:
  - What Relator alleges: liquidity, ownership and imputation (L189, L234-253, L286-289).
  - What Defendants argue: L133, L148, L177, L205-207, L254, L308, L473.
  - What the Court finds: L205, L220-232, L323-337, L427-437, L513-528, L545.
- Rounded prose beside exact figures: "$5.3 Million" and "$6.5 million" are stated as estimates or
  approximations in the allegations; "35 years" versus "nearly 35 years" (L289, L336).
- Notes: Defendants asked for dismissal "with prejudice" (L14) and "without leave to amend"
  (L113).
- Operative definitions, rules and scope exceptions:
  - The PPP certifications, 15 U.S.C. § 636(a)(36)(G)(i)(I)-(II) (L32).
  - "Knowingly", § 3729(b)(1)(A)-(B) (L255).
  - "Material", § 3729(b)(4) (L360).
  - "Obligation", § 3729(b)(3) (L472, fn 123 L484).
  - The reverse-FCA text, § 3729(a)(1)(G) (L459-472).
  - Rules 8(a), 9(b), 12(b)(6) and 15(a)(2).
  - Authorities:
    - Pleading: Iqbal and Twombly (L91, L99); Cafasso (L102); Wool (L124).
    - Elements: Erskine (9th Cir. 2026) quoting Campie (L127).
    - Scienter: SuperValu (2023) (L271); Silingo (L272); Winter (L275); the PSLRA contrast
      (fn 82); Reese, Berson and America West, "core operations" (L323-327); Nugget Construction
      held "inapplicable" (fn 85 L325); Nayab (fn 89).
    - Materiality: Escobar (L361-365); Barnes ("limited persuasive effect", L397); Kinetic
      Concepts ("persuasive", L412); Stephens Inst. (L412-427).
    - Particularity: United Healthcare (L222-223, L446-448); Moore v. Kayport (L448).
    - Reverse FCA: Sigma and Lesnik (L491-520); Bourseau (L516); Simoneaux (5th Cir.), cited by
      Relator but not applied (L491, fn 124).
    - Leave to amend: AmerisourceBergen, S.F. Herring, Williams, Zucco (L531-538).
- Amendments or contradictions:
  - The amended complaint supersedes the original (Lacey, L161). Inconsistent pleadings are not a
    basis to strike (PAE, L163).
  - FAQ 37 dated April 28 (Court, L360) versus April 29 (Amended Complaint, fn 97 L367).
  - Safe harbor May 7, 2020 (L374) extended to May 18, 2020 (fn 100 L380).
- Negative or exclusion facts:
  - Count 3 names only I.C.E. (L68).
  - Defendants' brief disclaims scienter of "Pt Arctic Fund or Pt Capital" (fn 33 L137).
  - No agency allegation; the Court says none is required (L321-323).
  - No established duty to repay "at the time" (L513, L528).
- Coverage: full. Read L1-249, L250-499 and L500-560 (pp.1-32). Remaining: none.

## D02 - Ling v. City of Los Angeles (9th Cir. No. 25-249): Opinion (for publication)

- Source: docs/uscourts_ca9_25_249_0.txt | 22 slip-opinion pages | task page Doc 4 | text L1-L264.
  P.1 (L3-L30) has no header. The running header alternates "N LING V. CITY OF LOS ANGELES" and
  "LING V. CITY OF LOS ANGELES N" (pp.2-22).
- Written or submitted by: U.S. Court of Appeals for the Ninth Circuit; opinion by Judge Nguyen
  (L37, L67).
  - Panel: Stephen A. Higginson (Fifth Circuit, sitting by designation, fn * L42), Jacqueline H.
    Nguyen and Daniel A. Bress (L34).
  - Appeal from the Central District of California, District Judge Philip S. Gutierrez presiding
    (L32).
  - Argued and submitted April 23, 2026 in Pasadena; filed September 24, 2026 (L32-33).
  - D.C. No. "2:11-cv-00974- JFW-JC" (L27-29).
- Type, date, edition: a published opinion. The court-staff SUMMARY (L38-52) "constitutes no part
  of the opinion" (fn ** L43). A simultaneously filed memorandum disposition decides other issues
  and is not in the bundle (L52, fn 1 L87).
- Period covered: grants February 2005-December 2018; litigation February 2011-September 2026.
- Parties and roles:
  - Plaintiff-Appellant: United States ex rel. Ms. Mei Ling, a relator (L6-9).
  - Plaintiffs-Appellees:
    - The United States, which intervened in July 2017 (L92).
    - Fair Housing Council of the San Fernando Valley ("FHC"), also a relator (L12-14, L40,
      L72).
  - Defendant-Appellee: City of Los Angeles ("the City") (L17-18).
  - Defendants: California and Community Redevelopment Agency of the City of Los Angeles,
    CRA-LA (L19-24). Fn 2 (L99): Ling and FHC reached a separate settlement resolving all claims
    against CRA.
  - HUD: a non-party, investigator and VCA counterparty.
- Counsel (L55-63):
  - For the appellant: Mick G. Harrison (argued) and Bruce Leichty.
  - For the appellees:
    - Department of Justice: Steven A. Myers (argued), Michael S. Raab, Wesley J. Heath and
      Charles W. Scarborough (Appellate Staff, Civil Division), and Brett A. Shumate (Assistant
      Attorney General).
    - U.S. Attorney's Office: Karen Paik (AUSA) and Bilal A. Essayli (U.S. Attorney).
    - Others: Donald R. Warren (argued) and Phillip E. Benson (Warren Benson Law Group), and
      David Iyalomhe.
  - For the City: Shaun D. Jacobs, Kathleen A. Kenealy, Denise C. Mills and Hydee F. Soto (City
    Attorney's Office).
- Entities and aliases:
  - "the Government" = the United States (L72).
  - "VCA" = voluntary compliance agreement (L46, L75, L102).
  - "alternate remedy provision" = § 3730(c)(5) (L150).
  - "Kennedy v. Novo A/S", 5 F.4th 47 (L190).
- Dated events:
  - February 2005-December 2018: the City received "millions of dollars" in HUD grants (L82).
  - February 2011: Ling and FHC filed suit (L86). The VCA quote says "filed Feb. 1, 2011"
    (L115, L180).
  - 2011: HUD investigation begins. January 2012: Letter of Findings. February 2012: Letter of
    Determination (L95).
  - September 2016: the City's letter to the HUD Secretary (L96-106).
  - 2016: the alleged $100 million offer (L230, L248).
  - July 2017: the Government intervenes. December 2018: it files an amended complaint (L92).
  - September 2017: HUD refers the matter to DOJ (L108).
  - April 2019: supplemental Letter of Findings. May 2019: Letter of Determination (L108).
  - July 2019: HUD says it intends to withhold about $80 million. The VCA follows "The next
    month" (L108), which is August 2019 (L197).
  - Fact discovery ran until November 2023 (L120, L197).
  - March 1, 2024: the City moves for summary judgment (L120; "March 2024", L248).
  - March 5, 2024: pre-trial mediation (L122).
  - May 2024: the not-yet-signed settlement is shared with Ling. June 2024: the settlement is
    executed (L122).
  - August 2024: fairness hearing and approval (L124).
  - October 2024: all claims against the City dismissed (L124).
- Figures and counts:
  - Settlement $38,266,989 (L46, L73, L122); restated as "a $38 million settlement" (L177).
  - The Government's calculation: damages of $26,800,000 "and included a multiplier sum of
    $11,466,989" (L236).
  - VCA value:
    - "at least $200 million over ten years" (Summary L46; opinion L75).
    - The VCA text: "a value that averages a minimum of $20 million per year" for ten years
      (L110).
  - Other amounts:
    - "$92 million of DOJ's calculated actual damages" (September 2016 letter, L106).
    - About $80 million in federal housing funds to be withheld (L108).
    - "more than $500 million": Ling's characterization of the United States' damages figure
      (L223).
    - $100 million offer (L226-250). Its existence is disputed (L232) and it is called
      "[alleged]" (L248, L250).
  - Relators' share: "at least 15 percent but not more than 25 percent" (L124).
  - "at least five percent of the multifamily housing" must be accessible for mobile impairment
    (L233).
  - Durations: "five years after" the VCA (L197); "more than six years later" (district court,
    L228); "nine years and two mediations" (L250).
  - Footnotes: 3 numbered plus * and **.
- Tables: not applicable.
- Lists:
  - Civil-rights laws, three: Section 504 of the Rehabilitation Act, the Fair Housing Act and
    Title II of the ADA (L82, L95).
  - Relief sought in the operative complaint, four (L209-212): FCA damages and penalties,
    negligent misrepresentation, unjust-enrichment restitution, payment by mistake.
- Claims and dispositions:
  - Ling appealed the approval of the FCA settlement.
  - Held: the VCA was not an "alternate remedy" (L163-214), and the district court did not abuse
    its discretion (L216-254). AFFIRMED (L259-261).
  - Other appeals (evidentiary hearing and limited discovery; motion to alter or amend; sanctions)
    are decided in the memorandum disposition (fn 1).
- Forecasts, guidance, deadlines, effective dates: none prospective. The VCA covers ten years
  (L46, L110).
- Hedged claims:
  - "there may be scenarios where the FCA suit proceeds by an alternate remedy ... even where the
    FCA suit remains ongoing" (L160).
  - "Under some circumstances, there could be issues of collusion or bad faith" (L160).
  - "Whether or not such an offer existed is irrelevant" (L233).
  - The district court found that "even if" the claims survived summary judgment, the Government
    "faces an onerous task" (L244-247).
  - Costs "would likely increase" (the Government's acknowledgment, L247).
- Alleged versus found:
  - Ling's contentions: L208, L223-230, L240-241.
  - The Government's representations at the fairness hearing: L233-238.
  - The City's statements: L238.
  - Findings by the panel and the district court: L197, L228, L250-254.
- Rounded prose beside exact figures: "$38 million" (L177) versus $38,266,989 (L46, L73, L122);
  "$200 million over ten years" (L46, L75) versus "averages a minimum of $20 million per year"
  (L110).
- Operative definitions, rules and scope exceptions:
  - Statutory text quoted: § 3730(c)(5) (L148); § 3730(c)(2)(B) (L218); § 3730(d) (L69-70,
    L145); § 3729(a)(1)(A) (L83); § 3730(b)(1)-(2) (L83-92).
  - Standards of review:
    - De novo for interpreting the FCA: Mateski and Barajas (L129).
    - Abuse of discretion for approving a settlement: Briseño and Robinson v. HealthNet
      (7th Cir. 2024) (L131-135). Fn 3: the parties agree.
  - Rule: an alternate remedy "takes the place of the FCA suit"; whether it does "can therefore
    involves a fact-intensive evaluation" [sic] (L143-160).
  - Nonmonetary value is possible but not sufficient (L199-205).
  - Authorities: Babalola (5th Cir.) and LaCorte (4th Cir.) (L152-157); Barajas (L158-206);
    Kennedy v. Novo A/S (D.C. Cir. 2021) (L190-195); Polansky (2023) (L219-221, L254); Everglades
    Coll., abrogated on other grounds (L238-239); Schoenberg (L251); Officers for Just. (L254).
- Amendments or contradictions:
  - The VCA carve-out is quoted twice with different wording:
    - L112-118: "Department of Housing and Urban Development", "No. CV-11-00974-PSG-JC",
      "Fa[lse]".
    - L180: "Department of Urban Development", "No. CV-11- 00974-PSG-JC", "Fal[se]".
  - The caption's D.C. No. suffix is "JFW-JC" (L29), while the carve-out's case number is
    "PSG-JC".
- Negative or exclusion facts:
  - The VCA "explicitly carved out" the FCA claims (L46, L75, L111-118, L178-182).
  - "no evidence of collusion or bad faith" (L197).
  - CRA settled separately (fn 2).
- Layout: run-together words "City'sremedial" (L212) and "AirForce" (L168, L173).
- Coverage: full. Read L1-199 and L200-264 (pp.1-22). Remaining: none.

## D03 - Wonneman v. Global Grab Technologies Inc. (D.D.C. No. 26-cv-1267 (BAH)): Memorandum Opinion

- Source: docs/uscourts_dcd_1_26_cv_01267_0.txt | 22 pp. | task page Doc 5 | text L1-L204.
  Footer "Case 1:26-cv-01267-BAH Document 16 Filed 09/25/26 Page N of 22". The page numeral sits
  at the top of each page; several footers fall inline mid-sentence.
- Written or submitted by: U.S. District Court for the District of Columbia, Judge Beryl A. Howell
  (L15, L197-198). Dated September 25, 2026 (L196). An order is entered contemporaneously; it is
  not in the bundle (L194).
- Type, date, edition: a ruling on a motion to dismiss under Rules 12(b)(1), (3) and (6).
  - Filings: Def.'s Mot. ECF No. 8; Def.'s Mem. ECF 9; Pl.'s Opp'n ECF No. 10. No reply was filed
    (L17, L40-42).
  - Single edition.
- Period covered: employment from July 16, 2017 to May 13, 2025, called an "eight-year period"
  (L27). Events run from 2017 to 2026.
- Parties and roles:
  - Plaintiff Matthew David Wonneman, a former employee.
  - Defendant Global Grab Technologies Inc., the employer; "GGT" in fn 5 (L130).
  - No United States party; not a qui tam case.
  - Non-parties:
    - Chris Cutlip, "USCP Project Supervisor & Service Specialist" (L28).
    - USCP, printed "United States Capital Police" (L27, L90).
    - Defendant's "Acting HR" representative and a payroll department member (L32).
    - The "acting supervisor for [d]efendant's [c]ontract with USCP" (L28, L37).
    - Brian Cooper, defendant's President/COO (declaration, ECF No. 9-2, fn 5).
    - Paul V. Bennet (declaration, ECF 10-2, L101).
    - The OIG of the U.S. Department of Health and Human Services (L101, fn 2 L104).
    - The USCP OIG, which did not receive the complaints (fn 3 L116).
- Entities and aliases: "NDAA" = National Defense Authorization Act of 2013, 41 U.S.C. § 4712
  (L17, L126). Defendant's "Tennessee location" (L83); Middle District of Tennessee (L41).
- Dated events:
  - July 16, 2017: employment starts (L27).
  - From 2017 through early 2020: clock-in and badge rules. In or around 2020 the timekeeping
    system was "modified ... during COVID, to be touchless" (L27).
  - In or around October 2022: Cutlip's absences begin (L28). "Within six months" the team was
    working 18-hour shifts (L28-30).
  - March 20, 2023: plaintiff's protest (L30).
  - September 11, 2023: email to Cutlip (L32).
  - April 24, 2024: email to HR. "The following week": meeting with payroll and Acting HR (L32).
  - May 9, 2024: Acting HR meets Cutlip (L33).
  - May 15, 2024: in-person meeting with Cutlip's "Capitol Hill" statement (L33, L85).
  - July 19, 2024: email to HR (L33).
  - August 13, 2024: HR meeting; plaintiff rejects the transfer proposal (L36).
  - March 21, 2025: final disclosure, to the acting contract supervisor (L37).
  - April 15, 2025 (individually) and June 4, 2025 (through counsel): OIG complaints (L101).
  - May 13, 2025: "forced to resign" (L37).
  - April 14, 2026: suit filed (L40).
  - No reply filed "timely on June 25, 2026, or otherwise" (L42). Local Civil Rule 7(d) allows
    seven days.
  - September 25, 2026: this opinion.
- Statutory periods (L95-101): § 4712(b)(4), (b)(1)-(2), (c)(2).
  - Complaint to the Inspector General within "three years" of the reprisal.
  - OIG report within 180 days.
  - Deemed exhaustion: a denial order, no order within 210 days, or 30 days after an extension
    expires.
  - De novo action within "two years" of exhaustion.
  - The court's application (L101): "more than 210 days before he filed ..., less than three
    years after ..., and within the two-year statute of limitations period."
- Figures and counts:
  - One of six technicians (L27); two other team members (L28); eighteen-hour shifts (L30).
  - "five categories" of protected information (L126); three NDAA elements (L126); two FCA
    retaliation elements (Kini, L165) and two protected-activity prongs (L167).
  - Footnotes: 7.
- Tables: not applicable.
- Lists:
  - § 4712(a)(1) categories (L128): gross mismanagement of a Federal contract or grant; gross
    waste of Federal funds; abuse of authority relating to a Federal contract or grant;
    substantial and specific danger to public health or safety; violation of law, rule or
    regulation related to a Federal contract (last).
  - Plaintiff's disclosure descriptions, Compl. ¶¶ 17-23 and 36-44 (L149-152).
- Claims and dispositions:
  - Count I, NDAA § 4712 retaliation: dismissed under 12(b)(6) (L158).
  - Count II, constructive discharge: conceded to be "subsumed within" Counts I and III (L70).
    Fn 1 (L74): the request for leave to amend to clarify this is denied.
  - Count III, FCA § 3730(h) retaliation: dismissed (L188, L191).
  - Venue under 12(b)(3): DENIED (L93).
  - Subject-matter jurisdiction / exhaustion: it "cannot dismiss" (L111).
  - Conclusion: the motion under 12(b)(6) "is granted" (L194). Dismissal with or without prejudice
    is not stated.
- Forecasts, guidance, deadlines, effective dates: the § 4712 periods above; Local Rule 7(d).
- Hedged claims:
  - Fn 4 (L118-119):
    - Defendant "appears to raise" exhaustion as jurisdictional.
    - Whether § 4712(c) exhaustion is jurisdictional "is not so clear"; the question "need not be
      resolved".
  - Fn 2 (L104-105): whether the HHS OIG is the OIG "of the executive agency involved" is "not
    further scrutinized".
  - Fn 6 (L154-159): "To be sure, plaintiff may not be privy ..."; "discovery may be necessary".
  - The misconduct "appears to be 'attenuated from the contract itself'" (L156); it "more closely
    resemble[s] a labor dispute" (L158).
  - "Even accepting those facts" (venue, L83).
- Alleged versus found:
  - Facts "as alleged" (L26); "[o]n information and belief" (L28).
  - Defendant's exhibits (fixed-fee contract; Cutlip salaried) are "not properly before the
    [Court]" (L115-123, fn 5 L130).
  - Findings: L85-93, L101-111, L153-158, L184-191.
- Rounded prose beside exact figures: "eight-year period" (L27) beside the exact dates.
- Operative definitions, rules and scope exceptions:
  - Venue rules:
    - 28 U.S.C. § 1391(b)(2) (L80).
    - FCA special venue, 31 U.S.C. § 3732(a), "transacts business"; not contested by defendant
      (L78, L87).
    - § 1406(a) (L49-51).
  - Elements of § 4712 (Arawole quoting Sargent, L126) and of § 3730(h) (Kini, L165).
  - Protected-activity prongs (Singletary and Hoyte, L167-173).
  - Authorities:
    - Venue: Atl. Marine, Lamont, McCain, Nabong, Exelon, Hale, Media Matters v. Paxton, and
      Glob. Reach v. Hawkwood (BAH, May 13, 2026).
    - Jurisdiction: Gunn, Arbaugh, Arpaio, Lujan, Kareem, West.
    - 12(b)(6): Iqbal, Twombly, Langeman, Hettinga, Simmons v. Rubio (D.C. Cir. 2026), Lott
      (2018).
    - Exhaustion: Wykosky ("affirmative defense", L103), Pullen, Johnsen; fn 4 Olson, Iovino and
      Thomas v. Hutson.
    - NDAA: Fuerst (11th Cir. 2022), Sargent, Arawole; Moses (contrast).
    - FCA retaliation: Kini (D.C. Cir. 2025), Singletary (D.C. Cir. 2019), Hoyte, Yesudian, Brown
      v. Aramark, United States v. Novo Nordisk Inc. (D.D.C. March 31, 2026), Lott (2017).
- Amendments or contradictions:
  - Defendant sought transfer under 28 U.S.C. § 1404(a) (L41-42); the court declines to address
    "transfer under 28 U.S.C. § 1406(a)" (L93).
  - Hettinga is cited as 677 F.3d 471 (L65) and as "677 F.4th at 476" (L67, L158).
  - The brief is cited as "Pl.'s Opp'n" throughout and once as "Pl.'s Mem. at 12" (L184).
  - Two different Lott cites (L122-123 and L177-178).
- Negative or exclusion facts:
  - No allegation that defendant "failed to provide security, overcharged the government, or
    procured the contract through underhanded means" (L153).
  - No allegation of duplicative wage claims (L184).
  - The complaints were not lodged with the USCP OIG. USCP is "not an executive agency but is
    rather part of the legislative branch" (fn 3).
  - No reply was filed (L42, fn 2).
- Coverage: full. Read L1-204 (pp.1-22). Remaining: none.

## D04 - Ghattas v. OrthoAtlanta, LLC (N.D. Ga. No. 1:25-cv-388-MLB): Opinion & Order

- Source: docs/uscourts_gand_1_25_cv_00388_0.txt | 27 pp. | task page Doc 6 | text L1-L200.
  Footer "Case 1:25-cv-00388-MLB Document 24 Filed 09/29/26 Page N of 27"; many footers fall
  inline.
- Written or submitted by: U.S. District Court, Northern District of Georgia, Atlanta Division.
  "SO ORDERED this 29th day of September, 2026" (L194). The signature is garbled in the text and in
  the original: "1 (1" / "MICH " K E L L . BROW N" (L196-197; docs L194-195).
- Type, date, edition: an opinion granting the motion to dismiss.
  - Filings: Dkt. 21 (brief Dkt. 21-1) against the amended complaint, Dkt. 20 (L16, L88).
    Response Dkt. 22; reply Dkt. 23.
  - Fn 5: the court cites the CM/ECF page numbers for Dkts. 21-1 and 23.
- Period covered: late 2022 or early 2023 through a termination "about thirteen months later"
  (L40); the termination date is not stated.
- Parties and roles:
  - Plaintiff Dr. Timothy Ghattas, MD: a physician, an owner "(for a time)" and a member of the
    Executive Committee (L6, L26).
  - Defendant OrthoAtlanta, LLC, an orthopedic practice (L19); "Ortho" in quoted allegations
    (L39, L77, L98).
  - No United States party; not a qui tam case.
  - Non-parties:
    - Dr. Orcutt, "the President and Chairman of Defendant's Executive Committee" (L26).
    - Dr. Snehal Dalal, "Defendant's Chairman". He sent the termination letter and is the only
      decision-maker identified (L170).
    - Director of Coding; Piedmont Hospital's coding education supervisor; Chief Medical Officer;
      a billing coder (L28, L34-35).
- Entities and aliases:
  - Two "Chairman" titles: Orcutt (Executive Committee) and Dalal (Defendant).
  - "Piedmont Hospital" (L35, L94) is a different entity from the cited case Cervalli v.
    Piedmont Healthcare (L134).
- Dated events:
  - Late 2022 or early 2023: Orcutt's statement (L26, L91).
  - March 2023-June 2023: training (L34). The defendant "began providing extensive training ...
    in March 2023" (L94).
  - March 10, 2023: email from the Director of Coding with three attachments (L34).
  - April 26, 2023: the Piedmont supervisor's webinar emails (L35).
  - May 2023: another email (L35).
  - June 13, 2023: the CMO's mandatory-webinar email (L35).
  - Plaintiff "began raising the issue in June 2023" (L94); "Summer of 2023" (L46, L75, L128).
  - Termination "about thirteen months later" (L40), date not stated.
  - September 29, 2026: this order.
- Figures and counts: three attachments (L34); three suggestions (L39); five allegations (L75-80);
  four categories of complaint (L134); three elements (Grant, L52); a six-year statute of
  limitations (O.C.G.A. § 9-3-24, L187). Footnotes: 5.
- Tables: not applicable.
- Lists:
  - Suggestions (L39; ¶¶ 24-26), rejected (¶ 27): (1) improved Modifier 25 training; (2) a billing
    coder to accompany physicians; (3) a tip sheet.
  - Allegations offered for reasonable belief (L75-80), five. The last is "(5) Defendant
    internally circulated training".
  - "Distinct possibility" categories (L133-135): internal reports calling the conduct illegal or
    fraudulent; complaints that lead to an internal audit; complaints to upper management and
    the ethics hotline; reports to the Government.
- Claims and dispositions:
  - FCA retaliation, § 3730(h): no protected activity under either standard (L150), and no
    awareness or causation (L178).
  - Breach of contract (Georgia law; employment contract and operating agreement, L40): the court
    declines supplemental jurisdiction under § 1367(c)(3) (L187).
  - Motion to dismiss GRANTED; the Clerk is directed to close the case (L192).
  - Prejudice and leave to amend: not stated.
- Forecasts, guidance, deadlines, effective dates: the CMO's warning that "the government had
  escalated oversite [sic] and punishment" (L35); the six-year limitations period (L187).
- Hedged claims:
  - The Eleventh Circuit "has not interpreted the amended language precisely" (L62).
  - Simon applied the standard "without deciding that this is the applicable standard" (L66).
  - "Regardless of which test the Court uses" (L72).
  - "Perhaps Dr. Orcutt provided that ... Or perhaps he did not" (L83).
  - "Perhaps that could work if paired with allegations ..." (L118).
  - "Plaintiff may have had a sincere belief" (L120).
  - "even if the Court reaches the merits" (L159).
  - Fn 3: Plaintiff "suggests" the standard "may not apply"; the court: "Nothing suggests that
    conclusion" (L67).
- Alleged versus found:
  - Complaint allegations: L19-40.
  - A response-brief allegation not in the amended complaint (L88).
  - Concessions by failure to respond (fn 4 L100; L156).
  - Court conclusions: L109-120, L144-150, L162-178, L187.
- Rounded prose beside exact figures: "about thirteen months later" (L40).
- Operative definitions, rules and scope exceptions:
  - Modifier 25: "a separate, significant, and identifiable evaluation-and-management service";
    a provider "gets paid more" (L24). CPT codes (L20).
  - The pre-2009 "in furtherance" / "distinct possibility" test (L54-60).
  - The 2009 amendment, "efforts to stop 1 or more [FCA] violations" (L62).
  - Authorities:
    - Pleading: Iqbal; Womack (unpublished; fn 1 citing Searcy).
    - Elements: Simon; Grant v. United Airlines (4th Cir. 2018) (L52).
    - Standards: Hickman; Sanchez; Chorches (2d Cir.). Fn 3: Briggs, Lisenby (3d Cir. 2026),
      Singletary (D.C. Cir. 2019).
    - Conclusory allegations: Wilchombe, Franklin, Gilmour, Lane, Maglana (11th Cir. 2025),
      Afr. People's Educ. (11th Cir. 2026).
    - Distinct possibility: Schinnerer, Cervalli, Childree, Prime, Mann, Carpenter.
    - Awareness: Mack, HPC Healthcare, Dunkel ("pigs, hunting for truffles"), Simpson, W. Sur.,
      Rehfeldt.
    - Supplemental jurisdiction: Cook, L.A. Draper, Gibbs.
- Amendments or contradictions: none internal. The plaintiff's response-brief characterization
  differs from the pleading (L88).
- Negative or exclusion facts:
  - No allegation that Modifier 25 cannot be used with steroid injections (L83).
  - No allegation that Orcutt continued after training (L94).
  - Never spoke to Dalal about Modifier 25 (L171-172).
  - Defendant "does not deny it took an adverse action" (L52).
  - The "parties are not of diverse citizenship" (Defendant's brief, L183).
- Normalization: L110 "...", which is U+2026 in the original.
- Layout: "Medicareregulations" (L139).
- Coverage: full. Read L1-200 (pp.1-27). Remaining: none.

## D05 - United States ex rel. De Simone v. VSL Pharmaceuticals, Inc. (D. Md. No. 23-cv-00700-LKG): Memorandum Opinion

- Source: docs/uscourts_mdd_8_23_cv_00700_0.txt | 16 pp. | task page Doc 2 | text L1-L244.
  Footer "Case 8:23-cv-00700-LKG Document 38 Filed 09/02/26 Page N of 16". The caption's
  parenthesis column occupies L14-L40.
- Written or submitted by: U.S. District Court, District of Maryland, "s/Lydia Kay Griggsby", United
  States District Judge (L238-240). "Dated: September 2, 2026" (L43). "A separate Order shall be
  issued"; it is not in the bundle (L234).
- Type, date, edition: a ruling on a motion to dismiss under Rules 9(b) and 12(b)(6).
  - Filings: ECF No. 26 and 26-1; opposition ECF No. 35; reply ECF No. 36.
  - No hearing (L.R. 105.6, L47).
  - Fn 1 (L57): facts come from the complaint, the motion and the briefs; "Unless otherwise
    stated, the facts recited herein are undisputed."
- Period covered: research in the 1980s-1990s; license in 2002; events 2014-2026; FOIA figures for
  2016-2022.
- Parties and roles:
  - Relator: Professor Claudio De Simone, a resident of Switzerland and inventor of the "De Simone
    Formulation" (L46, L66). He sues on his own behalf and for the United States and 22 "State
    Plaintiffs". Caption: "Plaintiffs and Relator" (L5-8).
  - Defendants:
    - VSL Pharmaceuticals, Inc. ("VSL"): Delaware; offices in Herndon, Virginia and
      Gaithersburg, Maryland (L68).
    - Leadiant Biosciences, Inc. ("Leadiant"): formerly Sigma-Tau Pharmaceuticals, Inc.; Nevada;
      principal place of business Gaithersburg, Maryland (L70).
    - Alfasigma USA, Inc. ("Alfasigma"): Delaware; principal place of business Covington,
      Louisiana (L71).
  - The United States and the State Plaintiffs declined to intervene on June 20, 2025 (ECF Nos. 12
    and 13; L117).
  - Non-parties:
    - ExeGi Pharma, LLC (exclusive licensee; sells Visbiome® from February 2016) (L86).
    - FTC, HHS, DOJ, the VA, and state agencies in Maryland, Louisiana, New York and
      Massachusetts (L105, L109-112).
- Entities and aliases:
  - "VSL#3®" / "VSL#3" / "VSL #3"; "VSL # 3" is split across L181-182.
  - "Italian VSL#3" (L90).
  - The De Simone Formulation is the eight-strain mix licensed to VSL in 2002 (L83). Visbiome® is
    ExeGi's brand of the same formulation (L86).
  - The Defendants' product is a seven-strain, Italy-made product sold as VSL#3 from mid-2016
    (L89).
- Lists:
  - State Plaintiffs (L46), 22: California, Colorado, Connecticut, Delaware, Florida, Georgia,
    Hawaii, Illinois, Indiana, Louisiana, the Commonwealth of Massachusetts, Nevada, New
    Hampshire, New Jersey, New Mexico, New York, North Carolina, Rhode Island, Tennessee, the
    Commonwealth of Virginia, Washington, and the District of Columbia (last). Maryland is not
    listed. Maryland appears only as an office or principal-place-of-business location (L68, L70)
    and as a FOIA respondent (L105).
  - Counts (L54-62; ¶¶ 166-345), 23: Count One is the FCA, § 3729(a)(1)(A)-(C). Counts Two to
    Twenty-Three are the state statutes in the same order, ending with "(23) ... District of
    Columbia Procurement Reform Amendment Act" (Count Twenty-Three, L62). "Count Fourt" [sic] is
    at L54.
  - Alleged false statements, four (L97): the May 17, 2016 marketing letter; the May 24, 2016 press
    release ("more than 170 studies"); the August 2016 press release ("original proprietary mix
    of eight strains"); and Alfasigma's sales script ("same 8 diverse strains ... for 15 years").
  - Programs (L99, L171): Medicare, Medicaid, TRICARE, CHAMPUS, VA health care programs, and the
    Federal Employees Health Benefits Program.
  - Defendants' grounds, four (L157-159): elements; state claims; time bar; Article II.
  - Relator's responses, four (L160).
- Dated events:
  - 1980s-1990s: research (L81).
  - 2002: license to VSL; the product is sold as VSL#3 (L83).
  - November 2014: De Simone resigns from VSL and terminates the agreement (L85).
  - February 2016: Visbiome® launched (L86).
  - Mid-2016: the new VSL#3 (L89).
  - May 17, 2016, May 24, 2016 and August 2016: the marketing items above (L97).
  - November 7, 2016: contact with the FTC (L109).
  - December 1, 2016: letter to the FTC (L109).
  - December 8, 2016: the FTC forwards the letter to "Consumer Sentinel" (L109).
  - February and May 2017: further FTC submissions (L109).
  - July 2020: letter to HHS and DOJ alleging Medicare and Medicaid fraud (L109-112).
  - August 2021: letter to HHS and DOJ alleging FCA violations (L112).
  - March 14, 2023: action commenced (ECF No. 1; L116).
  - June 20, 2025: declinations; unsealing and service order the same day (ECF No. 14; L117).
  - October 13, 2025: motion to dismiss (L119).
  - December 12, 2025: opposition (L120).
  - January 26, 2026: reply (L122).
  - September 2, 2026: this opinion.
- Figures and counts (FOIA-based, as alleged; first at L105, repeated at L178-179 and L183):
  - VA: $610,361.00 for 8,738 boxes, and 2,728 prescriptions for 561 unique patients reimbursed
    in the amount of $341,171.00. Period "between 2016 and 2021" (L105, L178); the ¶ 179 quote
    says "from 2016 through 2021" (L183).
  - Louisiana Medicaid: 280 bottles in six orders from four prescribers, February 2018-March 2019.
  - Massachusetts: $19,726.93, 2016-2022.
  - New York Medicaid: $39,765.19 for 575 prescriptions; no period stated.
  - Maryland: a response is mentioned, but no figure is given (L105).
  - "millions of dollars" (L114; ¶ 178 at L206).
  - Relief sought: treble damages plus a civil penalty (L63, L114).
  - Footnotes: 5.
- Tables: not applicable.
- Claims and dispositions:
  - Presentment is not shown, so the § 3729(a)(1)(A) claim is DISMISSED (L191).
  - Causation is not shown, so the FCA claims are DISMISSED (L211).
  - The state-law claims are DISMISSED (L215).
  - Fn 4 (L220-221): leave to amend is not warranted; "any amendment of the complaint would be
    futile".
  - Conclusion: the motion is GRANTED and the complaint is DISMISSED (L231-232).
  - "with prejudice" appears only in Defendants' request (L159).
  - Fn 5 (L223): the time bar and Article II are not addressed.
- Forecasts, guidance, deadlines, effective dates: the time-bar positions. Defendants say claims
  arising before March 14, 2017 are barred (L159). Relator says he sued "within three years of the
  Government's constructive knowledge" (L160). Neither is decided.
- Hedged claims:
  - Relator's "upon information and belief" allegation that "a discrete number of claims ... have
    been presented" (L101, L171, L181).
  - Fn 3: the argument is made "without persuasion" (L196).
- Alleged versus found:
  - Background and figures are allegations (L74-114).
  - Relator concedes he lacks claim information (L101-103, L173-176, fn 4).
  - Court findings: L162, L171-191, L203-218.
- Rounded prose beside exact figures: "millions of dollars" (L114) beside the exact FOIA figures
  (L105).
- Operative definitions, rules and scope exceptions:
  - Probiotics are defined in fn 2 (L91).
  - Rule 9(b): Dominion Fin. Servs. quoting McCormick (L129).
  - Rule 12(b)(6): Iqbal, Twombly, Nemet Chevrolet, Lambeth, GE Inv. (L136-140).
  - FCA: Sheldon v. Allergan Sales (4th Cir. 2026), four elements (L145-148); Rostholder; Taylor
    v. Boyko; Grant v. United Airlines (4th Cir. 2018) (L152-154, L168-169, L187); Nathan v. Takeda
    (L153, L168, L185).
  - Presentment can be pleaded two ways: specific claims (time, place, contents, identity, what
    obtained), or a "pattern of conduct that would necessarily have led to submission" (L153-154,
    L168).
  - State claims: Nowak v. Medtronic (L215).
- Amendments or contradictions: none.
- Negative or exclusion facts:
  - No facts on where or when purchases were made, why they were false, who submitted them, or
    when (L183-185).
  - No facts that doctors or patients were aware of the statements, that the statements caused
    prescribing, or that they influenced payment (L203).
- Typos as printed: "with particularly" (fn 3), "potions of these claims" (fn 5).
- Coverage: full. Read L1-199 and L200-244 (pp.1-16). Remaining: none.

## D06 - United States ex rel. Walden-Bing v. Horne, LLP et al. (S.D. Tex. No. 4:23-cv-01792): Memorandum and Order

- Source: docs/uscourts_txsd_4_23_cv_01792_2.txt | 19 pp. | task page Doc 1 | text L1-L211.
  Footer "Case 4:23-cv-01792 Document 68 Filed 07/20/26 in TXSD Page N of 19". The caption has a
  section-sign column (L16).
- Written or submitted by: U.S. District Court, Southern District of Texas, Houston Division.
  - Yvonne Y. Ho, United States Magistrate Judge. The signature block is printed twice with a
    stray "Texas." (L200-207).
  - "Signed on July 20, 2026, at Houston, Texas" (L198).
  - Stamp "ENTERED July 20, 2026, Nathan Ochsner, Clerk" (L24-28).
  - Fn 1 (L22) explains the magistrate judge's authority over non-dispositive motions for leave to
    amend.
- Type, date, edition: a memorandum and order on two motions.
  - Motion for leave to amend: Dkt. 58, with the proposed pleading at Dkt. 58-1.
  - Motion to strike: Dkt. 57.
  - Responses: Dkt. 60 (Horne) and Dkt. 61 (Deloitte). Reply: Dkt. 63.
- Period covered: 2022 employment events through a July 20, 2026 order with deadlines in
  July-August 2026.
- Parties and roles:
  - Relator/Plaintiff Amy C. Walden-Bing, pro se by December 2025. Her counsel withdrew
    (Dkts. 27, 31; L41-42).
  - Defendants:
    - Horne, LLP, the employer.
    - Deloitte, LLP, described in the proposed pleading as a subcontractor with "audit and/or
      oversight functions" (L73).
    - Cohn Reznick and Witt O'Briens: named in the original complaint, dropped from the amended
      complaint (L39-42).
  - United States:
    - Declined to intervene (Dkt. 22); the case was unsealed (Dkt. 23) (L41).
    - Later "intervened solely to seek dismissal of the FCA claims, which a pro se litigant cannot
      pursue on the Government's behalf" (Dkts. 45, 46; L43).
  - Agencies Walden-Bing reported to: the Office of Inspector General, the SEC and the U.S.
    Department of Labor (L36). She "communicated" with OIG two months after her termination
    (L37). Which agency's OIG is not stated.
- Entities and aliases:
  - The program is the "Texas Rent Relief program, which is federally funded" (L35). The original
    complaint calls it the "Emergency Rental Assistance program" (L131); also "ERA grant-funded
    operations" (L169).
  - Role: Quality Assurance/Quality Control Specialist (L35).
- Dated events:
  - June 2022: transfer to Texas Rent Relief (L116).
  - "During 2022": observations (L35).
  - July and August 2022: applications flagged (L131).
  - August 26, 2022: email to HR (L131).
  - Termination "around September 2, 2022" (L37); "on or about September 2, 2022" (L116);
    "September 2, 2022 termination" (L122).
  - Two months later: OIG communication (L37).
  - May 8, 2023: original qui tam complaint (Dkt. 1; L41, L122).
  - July 18, 2025: unsealed (Dkt. 23; L176).
  - December 8, 2025: pro se amended complaint (Dkt. 42; L42).
  - December 29, 2025: order granting Horne's extension (Dkt. 49; L49, L183).
  - January 6, 2026: order granting Deloitte's extension (Dkt. 53 at 12; L49). L183 prints
    "January 6, 2023".
  - January 7, 2026: Dkt. 57 "filed" (L50). L183 says "On January 9, 2026, Walden-Bing moved to
    strike".
  - January 13, 2026: Dkt. 58 (L52).
  - Earlier rulings: dismissal at Dkt. 66 adopting Dkt. 53 (L20, L43-44). Dkt. 53 at 11 denied the
    "barebones" leave request "without prejudice" (L46).
  - July 20, 2026: this order.
  - July 27, 2026: deadline to file the conformed second amended complaint (L194).
  - August 18, 2026, 9:00 a.m.: initial conference by Zoom. The joint Discovery Case Management
    Plan is due "at least 14 days before" it (L195).
- Figures and counts:
  - Four original defendants (L39).
  - Counts I-VI of the first amended complaint (L42).
  - Three proposed claims (L52-53).
  - Three FCA-retaliation elements (King, L94).
  - Three NDAA elements (Beltran, L143).
  - Four Lewis v. Knutson factors (L57-60).
  - Four Sabine Pilot elements (L166).
  - "four months is close enough" (L114).
  - Limitations: "3-year" (§ 3730(h)(3), L123).
  - Footnotes: 1.
- Tables: not applicable.
- Lists:
  - First amended complaint (Dkt. 42 at 23-26; L42):
    - Counts I-III: FCA § 3729(a)(1)(A), (a)(1)(B) and (a)(1)(G), against Horne and Deloitte.
    - IV payment by mistake; V unjust enrichment; VI negligence.
  - Proposed claims (L52-53): FCA retaliation (31 U.S.C. § 3730); NDAA § 4712; alternative Texas
    wrongful discharge.
- Claims and dispositions:
  - Earlier order: the FCA claims were dismissed (a pro se litigant cannot pursue them) and the
    common-law claims were dismissed for lack of standing (L43-44).
  - This order (L186-194):
    - Motion to strike DENIED as moot.
    - Leave GRANTED IN PART and DENIED IN PART.
    - GRANTED: FCA and NDAA retaliation claims against Horne, LLP.
    - DENIED: any claims against Deloitte, LLP. These are futile (L73-74); "Walden-Bing is barred
      from asserting any claim against Deloitte" (L74).
    - DENIED: the Texas common-law wrongful-discharge claim, which is futile (L169).
  - Holdings on the merits:
    - The FCA retaliation claim is stated and relates back to May 8, 2023, so it is timely
      (L120-132).
    - The NDAA claim is not futile (L137-159).
    - Venue is irrelevant to futility (L81-83).
    - Horne suffers no undue prejudice (L170-179).
- Forecasts, guidance, deadlines, effective dates: the July 27 and August 18, 2026 deadlines above;
  the 14-day plan deadline.
- Hedged claims:
  - "it is unclear whether Walden-Bing intends to assert claims against Deloitte" (L65); "mixed
    signals" (L73).
  - "it is unclear whether Walden-Bing's alleged communication to OIG ... qualifies as a complaint"
    (L153).
  - The Fifth Circuit "has 'even suggested that four months is close enough'" (L114).
  - "it is plausible to conclude that those who made the adverse employment decision were told"
    (Nichols, L116-118).
  - "allegedly transferred" (L116).
  - "The following facts are taken as true" (L35).
- Alleged versus found:
  - The proposed-complaint allegations: L35-37, L103-108.
  - Horne's arguments: L77-79, L86, L109-112, L122, L129, L139, L146-149, L155, L163, L172.
  - Court conclusions: L106, L108, L119, L132, L153, L159, L169, L179.
- Rounded prose beside exact figures: "around September 2, 2022" (L37) against "September 2, 2022"
  (L122).
- Operative definitions, rules and scope exceptions:
  - Leave and futility:
    - Rule 15(a)(1)-(2) (L56-57).
    - Jones v. Robinson (L57); Lewis v. Knutson (L60).
    - Futility means the claim "could not survive a motion to dismiss" (Rio Grande, L61-62).
    - Venue is not a futility ground (Shoes by Firebug; Stripling; L83).
  - FCA retaliation:
    - Elements: Robertson v. Bell Helicopter, Jamison, King v. Solvay quoting Bias (L93-95).
    - Distinct possibility: Gomez quoting Nichols (2019) (L97).
    - Protected activity: George, Patton and Guerrero (2012 and 2013) (L100-106).
    - Timing: Garcia, four months (L113-114); Nichols (2020) (L118).
    - Relation back: § 3730(h)(3), Rule 15(c)(1)(B), Mayle v. Felix (L122-125).
  - NDAA:
    - Tex. Educ. Agency (L141); Beltran v. Lockheed Martin (5th Cir. March 20, 2026) (L143-144).
    - Exhaustion: Robertson v. Intratek says it is required (L146-149); Thomas v. Hutson calls it
      an "affirmative defense" (L152); Coleman v. Sweetin (L152).
    - "§ 4712(2)(G)" [as printed] (L158).
  - Wrongful discharge: Sabine Pilot; White v. FCI USA (L163-167).
  - Prejudice: Susca, Smith v. EMC, Bias (L175-179).
- Amendments or contradictions (no precedence stated):
  - Dkt. 53 date: January 6, 2026 (L49) versus January 6, 2023 (L183).
  - Motion to strike: filed January 7, 2026 (L50) versus "On January 9, 2026" (L183).
  - L56 attributes the amend-once rule to "Rule 15(c)" but cites 15(a)(1).
  - Garbled sentences as printed:
    - L116: "those complaints must have less than four months after she lodged those complaints".
    - L149: "while Walden-Bing alleges that she 'reported' ... she state that she submitted a
      retaliation complaint to the OIG".
- Negative or exclusion facts:
  - The proposed caption lists only Horne as "Defendant" (L73).
  - She does not allege that she was required to commit an illegal act, or that she refused
    (L167-169).
  - She does not specify precise complaint dates (L113).
  - No scheduling order, and discovery has not begun (L172, L177).
- Normalization: 13 ellipses in the original at the lines listed under Bundle.
- Coverage: full. Read L1-199 and L200-211 (pp.1-19). Remaining: none.

## D07 - United States ex rel. Adler v. The Sporn Company, Inc. et al. (D. Vt. No. 2:24-cv-00617): Opinion and Order Denying Defendants' Motion to Dismiss the SAC

- Source: docs/uscourts_vtd_2_24_cv_00617_6.txt | 26 pp. | task page Doc 3 | text L1-L401.
  - Footer "2:24-cv-00617-cr Document 153 Filed 09/10/26 Page N of 26". The printed page numeral
    ends each page's last line (for example "exported, 2", L68).
  - Footers fall at L55, L69, L79, L88, L110, L125, L142, L158, L182, L194 (inline), L207, L217,
    L230, L248, L260, L273, L289, L307, L318, L328, L341, L355, L366, L377, L388 and L398.
  - The caption has a parenthesis column (L13-L33).
- Written or submitted by: U.S. District Court, District of Vermont (Burlington). The signature and
  dating are garbled in the text and the original (L394-395).
- Type, date, edition: an opinion and order on Defendants' motion to dismiss the Second Amended
  Complaint (Doc. 140), under Rules 12(b)(1) and 12(b)(6).
  - L61-L135 is a block quotation of the court's own prior opinion on the first motion to dismiss
    (Doc. 91 at 2-8; L59, L136).
  - L264-266 also quotes Doc. 91 at 12 and cites Doc. 91 at 20.
- Period covered: Adler's employment January 2016-December 2019; importation allegations
  2016-2020; the October 2023 settlement; the Settlement Period October 1, 2017-March 31, 2022;
  litigation through September 2026.
- Parties and roles:
  - Plaintiff-Relator Steven Adler: a Florida citizen and former TSC employee. He sues "on behalf
    of the United States ... and on his own behalf" (L44, L62).
  - Defendants:
    - The Sporn Company, Inc. ("TSC"): incorporated in New York; principal place of business in
      Vermont.
    - Bixler's, Inc. ("Bixler's"): TSC's wholly owned subsidiary; incorporated in Delaware;
      shares TSC's headquarters.
    - Perry Sporn: a natural person, a citizen of Vermont or New Hampshire; owner, president,
      CEO, director and secretary of TSC. He was added by the SAC (L44, L59-63).
  - The caption lists only TSC and Bixler's (L36-38).
  - The government:
    - Filed a "Statement of Interest" on June 8, 2026 (Doc. 143; L49).
    - Is "not a party to the CBP Settlement" (L173).
    - Whether it intervened is not stated.
  - Others:
    - CBP, U.S. Customs and Border Protection (the settlement counterparty).
    - DOJ (Defendants allege a DOJ "referr[al of] Defendants to CBP", L144, fn 1).
    - PwC (L84).
    - TSC staff: VP of marketing, consultant, engraver, director of product development,
      director of finance, logistics manager. Also "Maj and Brian" (L121).
- Counsel (L52-53):
  - For Adler: Andrew S. Macurdy, Arthur J. Ruben, Frank Tong Xu, Shaun Rosenthal, Ting Cheung.
  - For Defendants: Justin B. Barnard, Robert M. Wasnofski, Jr., Timothy J. Storino.
- Entities and aliases:
  - Bixler names: the "Bixler" line, Bixler's, Inc., "Bixler's Jewelers products", and the
    "America's Oldest Jeweler" trademark (L63, L74).
  - "Devotion Diamonds" line (L74) = "Devotion jewelry" (L82).
  - "CBP Settlement" = the October 11, 2023 agreement (L140). Within it, "CBP" or "Government"
    means U.S. Customs and Border Protection, and "Importer" means TSC and Sporn (L250).
  - "Settlement Period" = October 1, 2017-March 31, 2022 (L140-144).
  - "CIT" = Court of International Trade (L176).
  - "NovoAIS" / "Novo" [OCR] = 5 F.4th 47 (L324, L338, L344).
  - "All.flex" / "Al/flex" [OCR] = Felton v. Allflex USA (L224-235).
  - "Island Indus." = Island Indus., Inc. v. Sigma Corp. (L206-210).
- Dated events:
  - Adler's roles (L62): January-May 2016 independent consultant; May 2016-February 2018 VP of
    manufacturing; February 2018-December 2019 CTO and COO of a non-jewelry business unit.
  - 2016: TSC acquires Bixler's (L63).
  - June 2016: plant-policy meeting. String tags are agreed, with interim engraving in Burlington
    (L76).
  - Early 2017: new Montreal factory; PwC hired (L84).
  - September 2017: meeting with two PwC consultants (L84).
  - June 28, 2018: National Jeweler email exchange (L92-96).
  - July 4, 2018: "we are NOT in compliance" email with two recommendations (L98-121).
  - July 8, 2018: in-person conversation (L123).
  - September 2018: logistics manager's report (L124).
  - Invoices:
    - Undated FedEx invoice, $3,157.15 (Doc. 30-15; L81).
    - November 14, 2018: $96,342.20 (L86).
    - December 17, 2018: $79,221.96 (L124).
    - August 26, 2019: $44,000.99 (L130).
    - "November 22 and/or 25, 2019": $238,545.80 (L130).
  - February 2019: plant visit. March 18, 2019: confrontation with Sporn (L129).
  - September 26, 2019: two Bixler-line pieces shipped to Pennsylvania (L132).
  - June 24, 2020 and October 10, 2020: purchases delivered to Florida (L133).
  - October 11, 2023: CBP Settlement (L140).
  - June 5, 2024: transfer from S.D.N.Y. (Doc. 59; fn 2 L178).
  - March 27, 2026: leave granted (Doc. 134). April 16, 2026: SAC filed (Doc. 136) (L47-48).
  - June 8, 2026: Statement of Interest and Adler's response (Docs. 143, 144; L49-50).
  - June 29, 2026: reply (Doc. 152; L50).
  - Order filed September 10, 2026 (footer).
- CBP Settlement contents:
  - Recital: CBP alleges TSC and Perry Sporn are liable under 19 U.S.C. §§ 1304 and 1592 "for
    entries filed with CBP from October 1, 2017 through July 2018" (L148).
  - "CBP has not determined whether there is a loss of revenue to the United States for the period
    of July 1, 2018 to March 31, 2022" (L149; repeated fn 6 L270).
  - TSC agreed to pay $172,845.00 (L153; repeated fn 8 L305).
  - Release of TSC and Perry Sporn from marking duties and administrative monetary claims under
    §§ 1592 and 1304 (L153-160).
  - Reserved claims, a-e (L163-170). Item e. is "any liability based upon obligations created by
    this Stipulation".
  - "in and of itself is not outcome determinative" of this litigation (L171).
  - The parties are CBP, TSC and Perry Sporn (L250). Bixler's is not named.
  - Further clauses (L252-253): ¶ 5 (TSC releases the United States); ¶ 10 (nothing precludes the
    United States from other action); ¶ 12 (Federal income taxes).
- Figures and counts:
  - More than $16 million of jewelry made at Montreal factories, 2016-2020 (L65). Separately: "at
    least 289 separate importations totaling $14 million", April 2017-January 2020, which
    "avoided obligations to pay in excess of $1.4 million" (L135).
  - "a duty of 10 per centum ad valorem" (§ 1304(i), L71); "ten percent marking duties" (L82,
    L90).
  - $172,845.00 (L153, L305).
  - Five invoices (above); two PwC consultants; two email recommendations (L108-114); three
    Bledsoe distinctions (L363-369).
  - Footnotes: 11.
- Tables: not applicable.
- Lists:
  - Reserved claims a-e (L163-170).
  - July 4, 2018 bullets (L108-114). Sporn answered "ok" to the first and questioned the second
    (L120-121).
  - Bledsoe distinctions: First, Second, third (L363-369).
- Claims and dispositions: Adler's FCA claim under 31 U.S.C. § 3729(a)(1)(G) (L173, L264) is
  pending. The rulings:
  - (B) Exclusive CIT jurisdiction, 28 U.S.C. § 1582(3): the court has subject-matter
    jurisdiction; DENIED (L238-240).
  - (C) Release by the CBP Settlement: DENIED (L269). No double recovery is permitted. Defendants'
    claim that Adler already received part of the CBP Settlement is "not before the court"
    (L269-275).
  - (D)(1) Rule 12(g) waiver: not waived (L285-291).
  - (D)(2) "Alternate remedy": the court cannot find it as a matter of law; DENIED; further
    argument is not foreclosed (L346).
  - (D)(3) Preclusion, "Assuming arguendo": DENIED; further argument is not foreclosed (L349-390).
  - Conclusion: the motion to dismiss is DENIED (L393).
- Forecasts, guidance, deadlines, effective dates:
  - Adler's July 4, 2018 forecast that border agents "will at some point seize one of our
    commercial shipments" (L104).
  - Sporn's commitments: "Thank you, I'll look into it" (L123); "reassured [Mr. Adler] he would
    bring the Defendants' practices into compliance" (L129). Adler alleges these were not
    followed (L124, L130).
- Hedged claims:
  - Adler "believes" the invoiced jewelry was unmarked (L82, L90, L124); "upon information and
    belief" (L130).
  - Fn 7: the argument "may also be understood as an 'accord and satisfaction' claim" (L286).
  - The CBP Settlement "appears to share common facts and legal theories"; "There is thus a
    plausible argument" (L335).
  - "it is not clear whether [§ 1592] is an 'alternate remedy'" (L344).
  - "Assuming arguendo" (L349).
  - "Dicta from the Sixth Circuit lends support" (L357).
  - "This arguably supports an interpretation" (L385).
  - L-3: "not entirely clear" (L309) and "hardly clear" (L310).
  - The Second Circuit "has not addressed" (L206, L314, L385).
  - Barajas: "rarely will be" (L320).
- Alleged versus found:
  - L61-135 are allegations quoted from Doc. 91.
  - Defendants' contentions: L140-145, L176-184, L204, L212-213, L244-247, L279, L301, L349-350,
    fn 8.
  - The government's positions: L173, fn 1, fn 3.
  - Findings: L238-240, L256, L262, L269, L291, L346, L371, L390.
- Rounded prose beside exact figures: "$16 million" / "$14 million" / "$1.4 million" (L65, L135)
  beside the exact invoice amounts.
- Operative definitions, rules and scope exceptions:
  - Statutes:
    - 19 U.S.C. § 1304(a) (quoted L66-68) and § 1304(i) (L71).
    - § 1592 (L343-344, fn 10).
    - § 1619(a), informant award (fn 8 L305).
    - 28 U.S.C. §§ 1340 and 1582(3) (L201).
    - 31 U.S.C. § 3730(c)(5) (quoted L297-299); § 3730(b)(1) (L227, fn 5 L257);
      § 3730(c)(2)-(5) and (d)(1) (L228).
    - Fed. R. Civ. P. 3 (L206); Rules 12(g)(2) and 12(h)(2) (L283-284).
  - Authorities:
    - 12(b)(1): Nike, Sharkey, Lujan, Fountain.
    - 12(b)(6): Iqbal, Twombly, Hayden, Christiansen.
    - CIT jurisdiction: K Mart v. Cartier, Island Indus. v. Sigma (9th Cir. 2025), Eisenstein,
      Vt. Agency v. Stevens (fn 4), Murray v. UBS, Vallejo, Felton v. Allflex, Universal Fruits.
    - Release: Berkley and SM Kids (fn 1), NRDC v. NHTSA, Hughes Aircraft ("[o]nly the United
      States Attorney General has the authority to settle", L256), Wanxiang, Miller (2d Cir.
      2024), Unisys, James River, Rounds.
    - Waiver: Patel, Lyndonville; fn 7 Bibawy and Nat'l Mkt. Share.
    - Alternate remedy: L-3 (2d Cir. 2019), Bledsoe (6th Cir. 2003), Birchall, Barajas (9th Cir.
      2001), Novo (D.C. Cir. 2021), Globemaster, Broadening-Info (fn 10), S. Rep. 99-345 (L361),
      LaCorte (4th Cir. 1999), Dunleavy (3d Cir. 1997; abrogated on other grounds by Graham Cnty.),
      Neher, Mergent, Stevens and Polansky (L379-383).
    - Fn 11: Defendants rely on "non-controlling precedent from the Ninth Circuit" (Barajas).
- Amendments or contradictions:
  - The SAC "merely adds Mr. Sporn as a defendant" (L59).
  - The settlement periods differ: the recital's alleged entries run October 1, 2017-July 2018
    (L148); the Settlement Period runs October 1, 2017-March 31, 2022 (L140-144); the
    undetermined-loss period runs July 1, 2018-March 31, 2022 (L149).
  - Adler's email cites "Title 19 Section 103" (L96) and also "Title 19, U.S. Code, Section 1304"
    (L93).
- Negative or exclusion facts:
  - The CBP Settlement was "not attached to or quoted in the SAC" (L145).
  - CBP "has no authority to release FCA claims and did not do so" (L368).
  - "Defendants cite no authority for a non-DOJ release of FCA liability" (L262).
  - Jewelry repairs are "exempt from customs duties" (PwC advice, L84). The first email bullet
    reads "( not repairs )" (L112).
  - Adler's suit "has not been dismissed, much less with prejudice" (L369).
- OCR artifacts as printed:
  - Pilcrows as ",r", ",i", "~" or "iJ" (L63, L74, L81, L90, L269).
  - "l" for "1": "(a)(l)(G)" and "12(b)(l)" (L154-155, L173, L264, L285).
  - Run-together or misread words: "oflnterest" (L49, L173); "ofTSC" (L63, L76, L84, L266);
    "includingjewelry" (L74); "201 7" (L84); "i~formation" (L130); "Ifwe" (L121).
  - Misread names and words: "NovoAIS" (L324); "h[ e ]Id" (L322); "U oder" (L293); "[g]ovemment"
    (L228, L361); "Bell At!." (L192); "Nat'! Highway" (L255); "ajf'd" (L188).
- Coverage: full. Read L1-149, L150-279 and L280-401 (pp.1-26). Remaining: none.

## Shared ground (navigation only)

- Entities that appear in more than one document, and where:
  - The United States' role differs by document:
    - D01: declined (L46).
    - D02: intervened in July 2017 and settled; plaintiff-appellee (L41, L72-73, L92).
    - D05: declined with the State Plaintiffs on June 20, 2025 (L117).
    - D06: declined (Dkt. 22), then intervened only to seek dismissal of the pro se FCA claims
      (L41-43).
    - D07: filed a Statement of Interest; not a party to the CBP Settlement; intervention not
      stated (L49, L173).
    - D03 and D04: no United States party.
  - Agencies:
    - DOJ: D02 (counsel L58-60; VCA L104-106 and L115-116; referral L108), D05 (L109-112), D07
      (L144, fn 1, L256, L365-368).
    - HHS: D03 (its OIG received the § 4712 complaints, L101, fn 2) and D05 (letters of July 2020
      and August 2021, L109-112).
    - OIG: D03 (HHS OIG; the USCP OIG was not used, fn 3) and D06 (reports and a later
      "communicated", L36-37, L149-153; agency unstated).
    - Single-document agencies: SBA (D01), HUD (D02), FTC and VA (D05), SEC and the Department of
      Labor (D06), CBP and the CIT (D07), USCP (D03).
  - Programs: Medicare in D04 (Modifier 25) and D05 (VSL#3). Medicaid in D05, and in D06 only
    inside a Guerrero parenthetical (L106).
  - City of Los Angeles: the defendant in D02; also named in a case cited in D01 fn 44 (L181,
    Lee v. City of Los Angeles, 250 F.3d 668).
  - The Air Force / Northrop agreement (Barajas) is described in D02 (L166-206) and D07
    (L320-322, fn 11).
- Similar names to keep apart:
  - The Novo cases:
    - D02 L190 "United States ex rel. Kennedy v. Novo A/S, 5 F.4th 47" and D07 L324 "United
      States v. NovoAIS, 5 F.4th 47" share the same reporter cite.
    - D03 L177 "United States v. Novo Nordisk Inc., ... 2026 WL 880085" is a different case.
  - Stevens versus Stephens: Vt. Agency v. Stevens (D07 L214, L381) is a different case from
    Rose v. Stephens Inst. (D01 L401-427).
  - Sigma:
    - "Sigma Corp." (D01) = "Island Indus." (D07), 151 F.4th 1003.
    - D05's "Sigma-Tau Pharmaceuticals" (Leadiant's former name, L70) is unrelated.
  - Two Chairmen in D04: Orcutt and Dalal (L26, L170).
  - Duplicate-surname cites inside one document:
    - D01: Lee ×2, Corinthian ×3 forms, Winter ×2 forms.
    - D03: Lott ×2.
    - D06: Robertson ×2, Nichols ×2, Guerrero ×2, Bias ×2.
- Statutes and tests that recur:
  - § 3729(a)(1)(A)-(B): D01 Counts 1-2 (L68); D02 (L83); D05 Count One, (A)-(C) (L54, L143);
    D06 first amended Counts I-II (L42).
  - § 3729(a)(1)(G) reverse FCA:
    - D01 Count 3, dismissed with prejudice (L459-551).
    - D06 first amended Count III, dismissed earlier because she was pro se (L42-44).
    - D07, Adler's pending claim (L173, L264).
    - The "obligation" analysis appears in D01 (§ 3729(b)(3); Lesnik; Sigma) and D07 (Doc. 91
      quote: § 1304(i) obligation "does not consist merely of 'potential or contingent exposure to
      penalties'", L266).
  - § 3730(c)(5) "alternate remedy":
    - Covered in D02 (L50-214) and D07 (L144, L184, L277-390). Both quote the statute (D02 L148;
      D07 L297).
    - Shared authorities: Barajas, 258 F.3d 1004 (D02 L129, L158-206; D07 L320-322, fn 11);
      LaCorte, 185 F.3d 188 (D02 L152-157; D07 L364-370); Novo A/S, 5 F.4th 47 (D02 L190-195;
      D07 L323-344); Polansky, 599 U.S. 419 (D02 L219-221, L254; D07 L382-383).
    - Barajas's "rarely will be" is quoted in D02 L170 and D07 L320. Its "appropriate credit for
      funds paid or value received" is quoted in D02 L187 and D07 fn 11.
    - Status of Barajas: D02 treats it as circuit precedent ("We acknowledged", L170); D07 calls it
      "non-controlling precedent from the Ninth Circuit" (fn 11).
    - Authorities in one document only: D02 Babalola (5th Cir.); D07 Bledsoe (6th Cir.), L-3
      (2d Cir.), Dunleavy (3d Cir.), Birchall.
    - Outcomes: D02 holds the VCA is not an alternate remedy and affirms. D07 cannot decide the
      question as a matter of law and denies dismissal.
    - D07 was filed September 10, 2026; D02 was filed September 24, 2026. Neither cites the other.
  - Agreements with carve-outs: D02's VCA carve-out (L111-118, L178-182); D07's CBP reserved claims
    and "not outcome determinative" clause (L161-171); D02 fn 2's separate CRA settlement.
  - § 3730(h) FCA retaliation:
    - Outcomes: D03 Count III dismissed (L165-191); D04 dismissed (L46-178); D06 proposed claim
      not futile (L84-132).
    - Elements: two in D03 (Kini, L165); three in D04 (Grant, L52; fn 2 notes the parties'
      variants); three in D06 (King, L94).
    - "Distinct possibility": D03 L167, D04 L59-60 and L126-145, D06 L97.
    - "Objectively reasonable belief": D03 L170-173, D04 L62-120.
    - Singletary v. Howard Univ., 939 F.3d 287, is cited in D03 (L167-188) and D04 fn 3 (L68).
    - Limitations: § 3730(h)(3), 3 years (D06 L123).
  - § 4712 NDAA:
    - Outcomes: D03 Count I dismissed; D06 proposed claim not futile.
    - Exhaustion: D03 (periods at L95-101; Wykosky "affirmative defense", L103; fn 4 on whether
      it is jurisdictional) and D06 (Robertson v. Intratek "requires"; Thomas v. Hutson
      "affirmative defense", L146-153).
    - Thomas v. Hutson, 2025 WL 903131, is cited in D03 fn 4 (L119) and D06 (L152).
    - Elements, three each: D03 (L126) and D06 (L143).
  - The FCA's four elements: D01 (Erskine/Campie, L119) and D05 (Sheldon, L145-147).
  - Grant v. United Airlines, 912 F.3d 190: D04 L52 (retaliation elements) and D05 L152-154,
    L168-169, L187 (presentment).
  - Island Indus. v. Sigma, 151 F.4th 1003: D01 L482-520 (reverse-FCA obligation; antidumping
    duties on welded outlets) and D07 L206-210 (§ 1582 is no bar to a relator's customs-duty FCA
    suit).
  - Other recurring authorities:
    - Iqbal and Twombly: D01 L91-99, D03 L64-65, D04 L42-44, D05 L136, D07 L192-197.
    - Lujan: D03 L61, D07 L188.
    - Rule 9(b): D01, D05; D07 L368-369.
  - Leave-to-amend factors, four each: D01 AmerisourceBergen (L531) and D06 Lewis v. Knutson
    (L57-60). D05 fn 4 finds amendment futile.
  - Venue: D03 (§ 1391(b)(2) and § 3732(a); proper) and D06 (venue is not a futility ground).
- Periods or series that more than one document covers, and where:
  - Ruling dates in 2026: D06 July 20; D05 September 2; D07 filed September 10 (day of signing
    illegible); D02 filed September 24 (argued April 23); D03 September 25; D04 September 29; D01
    September 30.
  - Commencement:
    - D02: February 2011 ("Feb. 1, 2011", L115).
    - D05: March 14, 2023.
    - D06: May 8, 2023.
    - D01: December 17, 2024.
    - D03: April 14, 2026.
    - D07: not stated; transferred June 5, 2024.
    - D04: not stated.
  - Declination dates: D01 March 17, 2025; D05 June 20, 2025; D06 undated (unsealed July 18,
    2025).
  - 2016 events: D02 (September 2016 letter; alleged $100 million offer); D05 (February 2016
    Visbiome; May and August 2016 marketing; November-December 2016 FTC); D07 (Adler engaged in
    January 2016; Bixler's acquired; June 2016 meeting).
  - 2020 events: D01 (PPP, April-May 2020); D03 (timekeeping made touchless "during COVID");
    D05 (July 2020 letter to HHS and DOJ); D07 (June 24 and October 10, 2020 purchases; $16 million
    through 2020; $14 million through January 2020).
  - COVID: named in D01 and D03 (L27). D06's rent program is not tied to COVID in its text.
  - Employment endings: D03 May 13, 2025 (resignation); D04 "about thirteen months" after the
    rejection (undated); D06 about September 2, 2022; D07 Adler's roles end December 2019 (no
    dispute about that described).
- Documents that cite, amend or respond to another document in the bundle: none. Party names
  were checked across all seven texts. Each ruling refers to its own unbundled orders:
  D01 Docket 49; D02's memorandum disposition and district-court order; D03's contemporaneous
  order; D05's separate Order; D06 Dkts. 53 and 66; D07 Doc. 91 (quoted).
- Forecast/actual pairs, repeated/changed tables, same-period conflicts and scope relationships
  (locations only; the author owns hooks):
  - Figures stated twice with different precision or scope:
    - D02: $38,266,989 (L46, L73, L122) versus "$38 million" (L177); components $26,800,000 and
      $11,466,989 (L236); $200 million over ten years (L46, L75) versus an average of at least
      $20 million a year (L110).
    - D05: the VA figures three times (L105, L178, L183), "between" versus "from ... through"
      2016-2021.
    - D07: $16 million (2016-2020) versus $14 million (April 2017-January 2020); $172,845.00
      (L153, L305); the undetermined-loss period (L149, L270).
    - D01: $6.5 million (L189, L226, L236).
  - Proposed versus final:
    - D01: safe-harbor deadline May 7 extended to May 18, 2020 (L374, L380); FAQ 46 review intent
      (May 13, 2020) later deleted (July 29, 2021) (fn 111).
    - D02: the $92 million offset proposal (L106), the alleged $100 million offer (L226-250), the
      VCA (August 2019) and the settlement (June 2024).
    - D06: three proposed claims (L52-53) versus two allowed (L190-192); conformed pleading due
      July 27, 2026 (L194).
    - D04: three suggestions rejected (L39).
    - D03: the HR transfer proposal was rejected (L36).
    - D07: the July 4, 2018 recommendations and Sporn's replies (L108-123) versus the September
      2018 report (L124).
  - Same-document conflicts:
    - D01: FAQ 37 date (L360 versus L367).
    - D02: carve-out wording (L112-118 versus L180); D.C. No. suffix (L29 versus L115).
    - D03: transfer statute (L41 versus L93); Hettinga reporter (L65 versus L67).
    - D06: Dkt. 53 and Dkt. 57 dates (L49-50 versus L183).
    - D07: settlement periods (L140-149).
  - Narrative or overview passages that repeat results:
    - D02 SUMMARY (L38-52), "no part of the opinion".
    - Introductory or closing statements of results: D01 L548-552; D03 L17 and L194; D04 L16 and
      L192; D05 L47, L162 and L218; D06 L32-33 and L186-194; D07's title (L40-42) and L393.
  - Issuer versus mentioned organizations: each issuer is the court named in its section. HUD,
    CBP, SBA, FTC, HHS, PwC, Piedmont Hospital, National Jeweler, Pt Arctic Fund and Pt Capital
    are mentioned only.
  - Actions versus mentions:
    - D06: the Government intervened "solely to seek dismissal" (L43).
    - D07: a Statement of Interest was filed (L49); the DOJ referral is only alleged, and the
      government contests considering it (fn 1).
    - D02: HUD investigated, issued letters and entered the VCA (L95-110).
  - Dispositions:
    - D01: granted in part and denied in part (L548-552).
    - D02: affirmed (L261).
    - D03: granted (L194).
    - D04: granted; case closed (L192).
    - D05: granted; complaint dismissed (L231-232).
    - D06: leave granted in part; motion to strike denied as moot (L186-194).
    - D07: denied (L393).
    - "With prejudice" appears as a disposition only in D01 Count 3 (L545, L551). D06 L46 has
      "without prejudice"; D05 L159 is a request; D07 L368-369 describes Bledsoe.
  - Last items of lists:
    - D05: District of Columbia (L46); Count Twenty-Three (L62).
    - D07: reserved claim e. (L170); the third Bledsoe distinction (L368-369).
    - D04: allegation (5) (L80).
    - D01: conclusion item 3 (L552).
    - D03: the fifth § 4712(a)(1) category (L128).
