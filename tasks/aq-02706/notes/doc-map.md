# aq-02706 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Conventions: `Lnnn` = Read-tool line number of `text/Dnn.txt` (one paragraph per line). The matching
line in `docs/<file>.txt` is `L - 2` (text/ adds a 2-line header). "fn" = Federal Register footnote
`\n\`. "(word)" = the number is spelled out in the source, not printed in digits. "as printed" marks a
source oddity copied literally. Local id = task page Doc number (D01 = Doc 1 ... D07 = Doc 7; `notes/intake.json`).

## Bundle

- What it is: "Bank Merger Act Rulemaking" - seven Federal Register texts, Feb 2024 - Mar 2026: an OCC
  proposed rule and its final rule on business combinations (D01, D02), the FDIC final merger statement of
  policy (D03), an FDIC branch proposed rule (D04), an FDIC industrial-bank request for information (D05), a
  Federal Reserve Board reputation-risk proposed rule (D06) and an OCC community-bank licensing final rule (D07).
- Documents: 7; ids D01-D07 from `text/manifest.json`.
- Gaps: no scans, charts or tables in any document. No unread ranges (see Coverage statement at the end).
  Material referenced but NOT in the bundle: FDIC Proposed Statement (89 FR 29222) and Superseded Statement;
  OCC proposal for D07 (90 FR 51577); any final rule for D04 or D06; any rule that put 12 CFR 5.33(d)(3), (i),
  (j) back into part 5 between D02 and D07 (see "D02 vs D07").
- Extraction spot-checks: originals are plain-text captures, so PDF page count is not-applicable; Federal
  Register page markers `[[Page N]]` are present in every file (D03, D05, D06 and D07 lack a marker for
  their first page). Capture artifacts common to the files: every email address reads "[email protected]"
  (e.g. D01 L44, D03 L29, D04 L41); amendatory bullets print as a lone "0" line (e.g. D01 L299, D07 L276);
  superscripts print as `\2\` (D03 fn 12 L201); footnote separators are dashed lines, sometimes fused to the
  end of a paragraph (e.g. D01 L191, D03 L169, D04 L86). No truncated text was found. Checked text/ against docs/ at a figure and a footnote per document, all identical at offset 2:
  D01 fn 32 (docs L255 / text L257) and fn 17-18 (L138 / L140); D02 RFA count (L367 / L369) and fn 28
  (L198 / L200); D03 fn 12 HHI (L198-199 / L200-201); D04 statistics (L108-109 / L110-111) and RFA counts
  (L365 / L367); D05 industry counts (L126 / L128) and fn 21 (L130 / L132); D06 MRA percentages (L143 / L145)
  and fn 19 (L177 / L179); D07 RFA count (L199 / L201). Tables: not-applicable (none exist).
- Provenance: `notes/intake.json` schema 1, capture_sha256 736155cd...3557; all seven `incomplete: false`,
  `gap_characters: 0`, `matches_capture: true`.
- Reuse binding (source sha256 = extraction manifest sha256, method `text`, pages null):
  D01 f145f16d748966c8625c293680f96f50c59be2a262dbfa3422ec0040bc4f2bd1 (73,483 chars);
  D02 50d600045b7ad53c37274ed085dfcf5de30ad106db281c69494adbbc3a38e0e2 (114,773);
  D03 8f0c0b2ee0060bbfc268a9579f96517d8d8e1f0149477eb38a82d3332e3b0348 (123,763);
  D04 79235366090e4da19cf03c944e9255ab2deb627b2c2446930318ab4ae91b2b08 (96,535);
  D05 a9bdebf05225602e0f6f48cb19915a98460e09a03b73fe6853233ae45b84ac23 (40,924);
  D06 692e8ab26782941dd3af62b57bdd4c60570ce0f60692eb70b589372a358ad702 (41,245);
  D07 2904b33c09ef062df6558f4a90b03499454801852a253f2b254b7912b30f617f (60,800).
  No earlier map existed (template only); every entry below is new on 2026-10-10.

## D01 - OCC proposed rule, Business Combinations Under the Bank Merger Act

- Source: `docs/fr_2024_02663.txt` | 462 text lines | FR pages 10010-10018 (markers L19, L71, L106, L145,
  L187, L222, L276, L355, L405).
- Written or submitted by: Office of the Comptroller of the Currency (OCC), Department of the Treasury
  (L21-32). Signed Michael J. Hsu, Acting Comptroller of the Currency (L457-458).
- Type, date, edition: Notice of proposed rulemaking (L34). 89 FR No. 30, Tuesday, February 13, 2024
  (L3-5); FR Doc 2024-02663, filed 2-12-24 8:45 am (L7, L460). 12 CFR Part 5; Docket ID OCC-2023-0017;
  RIN 1557-AF24 (L25-28). Comments must be received by April 15, 2024 (L40). Proposal edition of D02.
- Period covered: merger-application counts for calendar 2019-2023 (L252, fn 32 L257); small-entity size
  measured at December 31, 2022 (fn 31 L255). No fiscal-year convention.
- Outline: SUMMARY L38; DATES L40; ADDRESSES L42-51; contacts L53; I. Background L57-76 (fn 1-5 L62-66);
  II. Description of the Proposed Policy Statement and Regulatory Amendments L78: Regulatory Amendments
  L80-102 (fn 6 L86, fn 7-8 L92-93, fn 9 L100, fn 10 L101-102); Policy Statement L108-216 = preamble
  summary of appendix A: Sec. I L110 (fn 11 L113), Sec. II L116-124 (fn 12-13 L119-120, fn 14-15 L127-128),
  Sec. III L131-154 (fn 16 L134, fn 17-18 L140, fn 19 L151, fn 20 L157), Sec. IV L160-199 (fn 21 L163,
  fn 22 L170, fn 23-24 L178-179, fn 25 L193), Sec. V L200-206 (fn 26 L203), Sec. VI L207-216 (fn 27-29
  L210-213); III. Request for Comments L218-220; IV. Regulatory Analysis L224: A. Paperwork Reduction Act
  L226-247 (fn 30 L231), B. Regulatory Flexibility Act L249-266 (fn 31-32 L255-257, fn 33-34 L264-265),
  C. Unfunded Mandates L268-278, D. RCDRIA L280-289 (fn 35-36 L285-286); List of Subjects L291-293;
  amendatory instructions L295-309; proposed Appendix A text L311-455: I. Introduction L313-315;
  II. General Principles of OCC Review L317-341; III. Financial Stability L343-367 (A. Factors Considered
  L345-357; B. Balancing Test L359-367); IV. Financial and Managerial Resources and Future Prospects
  L369-416 (A. Overarching Considerations L373-383; B. Individual Factors L385-416); V. Convenience and
  Needs L418-428; VI. Public Comments and Meetings L430-455 (A. Public Comments L432-442; B. Public
  Meetings L444-455).
- Entities and aliases: BMA = Bank Merger Act = section 18(c) of the Federal Deposit Insurance Act =
  12 U.S.C. 1828(c) (L59). "institutions" = insured depository institutions (L59, L315). UFIRS = Uniform
  Financial Institution Ratings System, "also known as the CAMELS system" (L116, fn 12 L119). ROCA = risk
  management, operational controls, compliance, asset quality; rating system for U.S. branches and agencies
  of foreign banking organizations (L116, fn 13 L120). CC Rating System (L116, L325). CRA (L116). LMI =
  low- or moderate-income (L200, L421). MRA = matters requiring attention (L182, L396). RAS = Risk
  Assessment System (L183, L397). "the Board" = Federal Reserve Board, only in fn 20 L157 (Bank Holding
  Company Act filing). SBA (L251). Contacts L53: Valerie Song, Assistant Director; Christopher Crawford,
  Special Counsel; Elizabeth Small, Counsel (Chief Counsel's Office, 202-649-5490); Yoo Jin Na, Director
  for Licensing Activities (202-649-6260). Mentioned, not issuing: FDIC (L97, L178, L390), DOJ Antitrust
  Division (fn 11 L113), FFIEC (L113), Basel Committee on Bank Supervision (fn 14 L127), "FRB" orders (L140).
- Tables: none. All figures are in prose or footnotes.
- Lists (count, last item):
  - BMA factors the OCC must consider: five, last = AML effectiveness "including in overseas branches" (L59).
  - Streamlined-application situations in Sec. 5.33(j): "four situations" (word, L96); (i)-(iv) in fn 9 L100.
  - Indicators "consistent with approval": 13 numbered, L321-333; last = 13. no adverse comment raising a
    significant CRA or consumer compliance concern.
  - Indicators that raise supervisory or regulatory concerns: 6 numbered, L336-341 (item 6 joins two
    conditions with "; or"). Preamble version L124 has seven clauses labelled (i)-(vi) with "(v)" twice.
  - Financial stability factors: 7, L348-357 (item 7 after the page break at L355).
  - Balancing test sub-paragraphs: 4 (L361-367); item 3's sub-items are lettered "b." and "c." only (L364-366).
  - Acquirer characteristics, IV.A.2 a-e: 5, L377-381, last = "functionally the target".
  - Risk categories in the OCC Risk Assessment System: "eight" (word) L174, L391; listed fn 24 L179 and L391:
    credit, interest rate, liquidity, price, operational, compliance, strategic, reputation.
  - Convenience and needs items V.A.1-6: 6, L421-426. Preamble summarises as (i)-(iii) L200.
  - Comment-period extension instances: 3 (L435-437); extenuating examples: 3 (L440-442).
  - Methods for oral input: "three" (word) L446: public hearing, public meeting, private meeting (also fn 27 L210-211).
  - Public-meeting criteria VI.B.3 a-f: 6, L449-455. Preamble (i)-(vi) L216 in a different order.
  - PRA comment topics (a)-(e): 5, L243-247.
- Quantities (unit, scope, line):
  - 30 days: BMA public notice "published for 30 days" (L59, fn 3 cites 12 U.S.C. 1828(c)(4) at L64);
    "statutory 30-day public notice period" and "30-day public comment period, which the OCC may extend"
    (L59, fn 4 = 12 CFR 5.8(b), 5.10(b)(1) at L65); "usual 30-day comment period" (L207); appendix VI.A.1
    "30-day comment period" (L434).
  - "15th day after the close of the comment period": current Sec. 5.33(i) deemed approval (L82, L234).
  - Sec. 5.33(j) streamlined thresholds, fn 9 L100: target total assets "no more than 50 percent" of
    acquirer's (i); total assets acquired "do not exceed 10 percent" of acquirer's (iii) and (iv).
  - "$50 billion": indicator 2 "total assets less than $50 billion" (L322); public-meeting criterion d
    "(e.g., resulting institution will have $50 billion or more in total assets)" (L453).
  - "50%": indicator 9 "target's combined total assets are less than or equal to 50% of acquirer's total assets" (L329).
  - Ratings: CRA Outstanding or Satisfactory (L323) vs Needs to Improve or Substantial Noncompliance
    (L336); UFIRS/ROCA composite and management 1 or 2 (L324) vs 3 or worse (L338); consumer compliance
    1 or 2 (L325) vs 3 or worse (L337).
  - "three-year period": multiple enforcement actions executed or outstanding (L124, L341).
  - PRA: OMB control number 1557-0014 (L228, L236); Estimated Number of Respondents 3,694 (L240);
    Estimated Total Annual Burden 12,481.15, no unit printed (L241); changes "de minis" as printed (L239).
  - RFA: small entity = total assets of $850 million or less (banks, savings institutions) and $47 million
    or less (trust companies) (L251, fn 31 L255). OCC "currently supervises 1,057 institutions"; "approximately
    661 are small entities"; "on average, 38 OCC-supervised institutions could be impacted by the rule in a
    given year"; "five-year average ... 2019 through 2023" (L252). fn 32 L257: 51 merger applications in 2019,
    36 in 2020, 46 in 2021, 36 in 2022, 18 in 2023. fn 34 L265: significant if > 5 percent of total annual
    salaries and benefits or > 2.5 percent of total non-interest expense. Certification L261.
  - UMRA: $100 million "(adjusted annually for inflation, currently $182 million)" (L271); "$182 million or more" (L278).
- Forecasts, guidance, deadlines, effective dates: comment deadline April 15, 2024 (L40); no effective date
  (proposal); RCDRIA "first day of a calendar quarter" rule described L282.
- Hedged claims: "additional transparency ... may be helpful" (L74); removal of streamlined form "should not
  significantly increase the burden" (L96); "OCC does not expect that the changes would ... result in a
  different decision outcome ... or ... a burden" (L260-261); impact "would likely be de minimis" (L261);
  "OCC is unlikely to find ... consistent with approval unless and until" (L123, L334); "is also
  considering, and welcomes comment on, whether to specify communities in addition to LMI communities" (L200).
- Rounded prose beside exact figures: "on average, 38" (L252) beside the five yearly counts (fn 32 L257);
  "approximately 661" (L252).
- Operative definitions, rules and scope exceptions:
  - Business combination "includes assumption of deposits in addition to mergers or consolidations" (fn 1 L62).
  - Proposed amendment: "Section 5.33 is amended by removing and reserving paragraphs (d)(3), (i), and (j)" (L307);
    "business reorganization" (d)(3) is only used to define a class eligible for expedited review (L89).
  - 12 CFR 5.13(a)(2) adverse-comment provisions "would no longer apply to business combination
    applications" (fn 6 L86). 12 CFR 5.2(b): OCC may adopt materially different procedures; may reduce
    information in failing-bank transactions (fn 10 L101-102).
  - Scope exclusion: proposed appendix A "would not address" the competition and AML factors (fn 11 L113),
    while indicators 8 (L328) and 11 (L331) refer to money laundering effectiveness and competition.
  - Undercapitalized applicant: OCC may not approve unless capital restoration plan approved or FDIC Board
    determination (L390; fn 23 L178, 12 U.S.C. 1831o(e)(4)).
  - Conditions enforceable under 12 U.S.C. 1818 (L147-148, L191, L362, L407); denial 12 CFR 5.13(b) (fn 25 L193).
- Amendments or contradictions (prose summary vs regulatory text, both locations):
  - Indicator summary: preamble groups into (i)-(iv) (L116) and does not itemise indicator 6 "no open formal
    or informal enforcement actions" (L326) or indicator 12 "significant legal or policy issue" (L332).
  - Concern indicators: preamble L124 order is CRA, UFIRS/ROCA, consumer compliance; text order is CRA,
    consumer compliance, UFIRS/ROCA (L336-338). Preamble has "rating of 3 worse" and duplicate "(v)"; text item 3
    adds "or the most recent report of examination otherwise indicates that the acquirer is not financially
    sound or well managed" (L338). Preamble says "if any of these indicators are present" (L123); text says
    "If certain indicators ... are present" (L334).
  - Stability factors (iv), (v): preamble "the extent to which..." / "the extent of cross-border activities"
    (L131); text "Whether the proposed transaction would materially increase the extent..." (L351-352).
  - Appendix D / E: preamble L154 pairs "recovery planning standards" with 12 CFR 30 appendix D (Heightened
    Standards title) and "heightened standards requirements" with appendix E (Recovery Planning title); text
    L364-366 pairs appendix D with heightened standards and appendix E with recovery planning.
  - Capital: preamble "less than adequate capital, less than satisfactory management, or poor earnings
    prospects" (L167); text "less than adequate capital or liquidity, ..." (L382).
  - Framing: preamble "less likely to approve an application when the acquirer" (L166); text "more likely to
    approve ... than when:" (L376).
  - MRAs: preamble "or lack thereof, may impact" (L182); text "suggests there may be insufficient managerial
    resources" (L396). RAS: preamble "for the applicant as well as ... an OCC-supervised target" (L183); text
    "for the combining institutions" (L397).
  - Public-meeting criteria: preamble (v) "potential value of any information that could be gathered and
    documented" (L216); text c. "useful information that the OCC would not otherwise be able to obtain in
    writing" (L451). Text adds "Public meetings are the most-employed public option" (L446).
  - "Comptroller's Licensing Handbook" (L200) vs "Comptroller's Licensing Manual" elsewhere (L73, L110, L166).
  - Typographic: "de minis" (L239); "would de minimis" (L274); fn 17 and fn 18 run together on L140 and
    fn 17 has no date; "(Version 1.1, September 2019)" L179.
- Notes: cited decisions - OCC Conditional Approval #1298 (November 2022) L134, L151; OCC Corporate Decision
  #2012-05 (April 2012) L134; FRB Order No. 2012-2 at 30 and FRB Order No. 2021-04 (May 14, 2021) at 24 (L140);
  Comptroller's Licensing Manual "Business Combinations" at 23 (January 2021) (fn 22 L170); Bank Merger
  Competitive Review--Introduction and Overview (1995) (fn 11 L113). Authority citation L302.
- Coverage: full. L1-462 read sequentially in one pass.

## D02 - OCC final rule, Business Combinations Under the Bank Merger Act

- Source: `docs/fr_2024_21560.txt` | 605 text lines | FR pages 78207-78221 (markers L9, L73, L105, L133,
  L159, L189, L222, L260, L278, L309, L356, L397, L482, L540, L596).
- Written or submitted by: OCC, Department of the Treasury (L13-24). Signed Michael J. Hsu, Acting
  Comptroller of the Currency (L601-602).
- Type, date, edition: Final rule (L26). 89 FR No. 186, Wednesday, September 25, 2024 (L3-5); FR Doc
  2024-21560, filed 9-24-24 (L7, L603). Same docket and RIN as D01: OCC-2023-0017, RIN 1557-AF24 (L19-20).
  "The final rule is effective on January 1, 2025" (L32, L403). Cites D01 as 89 FR 10010 (February 13, 2024)
  (fn 6 L56). Final edition of D01.
- Period covered: "past five years" of merger applications, years not named (L369); small-entity size at
  December 31, 2023 (fn 50 L373); supervised-institution count from FINDRS accessed August 18, 2024 (fn 49 L372).
- Outline: SUMMARY L30; DATES L32; contacts L34-35; I. Background L39-59 (fn 1-5 L44-48, fn 6 L56);
  II. Description of the Final Policy Statement and Regulatory Amendments L61: Regulatory Amendments L63-110
  (fn 7 L67, fn 8-11 L81-84, fn 12 L90-91, fn 13 L100); Policy Statement L112-323: general and Sec. I
  L114-124 (fn 14 L117-118, fn 15-16 L127-128); Sec. II L131-186 (fn 17-18 L138-139, fn 19-20 L145-146,
  fn 21 L165, fn 22-25 L172-175, fn 26 L183); Sec. III L187-219 (fn 27 L194, fn 28-29 L200-201, fn 30 L207,
  fn 31 L214); Sec. IV L220-266 (fn 32 L227, fn 33 L234, fn 34-35 L241-242, fn 36 L253); Sec. V L267-295
  (fn 37 L270, fn 38 L283-284, fn 39 L292); Sec. VI L296-323 (fn 40-42 L299-302, fn 43-44 L315-316,
  fn 45-46 L326-327). There is no "III." heading; numbering runs II then IV. IV. Regulatory Analysis L330:
  A. PRA L332-358 (fn 47 L337); B. RFA L360-383 (fn 48 L365, fn 49-50 L372-374); C. UMRA L385-399
  (fn 51-52 L391-392); D. RCDRIA L401-403 (fn 53-54 L406-407); E. Congressional Review Act L410-426
  (fn 55-57 L415-423). List of Subjects L428-430; amendatory instructions L432-447; final Appendix A text
  L449-599: I. Introduction L453-455; II. General Principles of OCC Review L457-480; III. Financial
  Stability L484-505 (A L486-495; B L497-505); IV. Financial and Managerial Resources and Future Prospects
  L507-556 (A L511-522; B L524-556); V. Convenience and Needs L558-568; VI. Public Comment Period and
  Public Meetings L570-599 (A L572-582; B L584-599).
- Entities and aliases: as D01, plus G-SIB = global systemically important banking organization (L142);
  CAMELS components spelled out (fn 17 L138); SBA's Office of Advocacy (L103-108, L368-369); Riegle-Neal =
  Riegle-Neal Interstate Banking and Branching Efficiency Act of 1994 (L169, fn 22 L172); Consumer Financial
  Protection Bureau (L161, commenter suggestion); Department of Justice (L124); FINDRS (fn 49 L372). Contacts
  identical to D01 (L34). Mentioned, not issuing: FDIC (L97, L121, L241, L283, L529), FRB (L200-201), "the Board" (fn 31 L214).
- Tables: none.
- Lists (count, last item): 13 indicators L460-472; 6 concern indicators L475-480; 7 stability factors
  L489-495; balancing test 4 sub-paragraphs L499-505 (item 3 sub-items lettered "b." and "c." only, L502-504);
  IV.A overarching considerations 5 (L513-522; new item 2 at L514; acquirer characteristics a-e L516-520);
  V.A items 1-6 L561-566; VI.A extension instances 3 (L575-577) and examples 3 (L580-582); VI.B.3 criteria
  a-f L589-599 (item e crosses the page break at L596; f at L599); "eight categories of risk" (word) L238, L530;
  "four situations" (word) L87, fn 12 L90-91; PRA topics a-e L349-353; Congressional Review Act "major rule"
  tests (1)-(3) L419-420.
- Quantities (unit, scope, line):
  - Comments: "The OCC received 34 substantive written comments on this proposal from banks, trade groups,
    academics, and members of the public" (L59). Counted commenter mentions: "Two commenters" on the 50
    percent indicator (L155), on G-SIB and Congressional intent (L168), on extending the comment period (L306).
  - 30 days / 30-day: L41 (three times), fn 10 L83 "typically 30 days", L296, L312 ("standard 30-day notice
    period prescribed by the BMA", fn 44 = 12 U.S.C. 1828(c)(3) at L316), appendix VI.A.1 L574; PRA comments
    "within 30 days of publication" (L354).
  - "15th day after the close of the comment period": L65, L76, L340, L379. "within 15 days after the close
    of the comment period" = OCC practice on expedited applications (L78).
  - Target time frame for licensing decisions on merger applications: "45 days for expedited review and
    60 days for standard review" (L76; source fn 11 L84 = OCC 2023 Annual Report at 36). OCC may extend the
    standard time frame (L78).
  - Sec. 5.33(j) thresholds, fn 12 L90-91: "no more than 50 percent"; "do not exceed 10 percent" (twice).
  - "$50 billion": preamble L153 (six times) and L154; appendix indicator 2 "less than $50 billion" (L461);
    public-meeting criterion d "$50 billion or more" (L593). "at least $50 billion in total assets" =
    scope of the OCC heightened-standards guidelines (L153).
  - "$100 billion or more in total assets": commenter request to raise the indicator (L153). Not adopted (L154).
  - "below $10 billion in assets": commenter suggestion to categorise as low financial-stability risk (L217).
  - "50 percent" (preamble L155-156) / "50%" (appendix indicator 9, L468).
  - "three-year period": L142, L480. "three years" twice: commenter proposals on branch-closure lists and a
    closure prohibition (L274). "initial 60-day comment period for larger transactions": commenter (L306).
  - PRA: OMB 1557-0014 (L334, L342, L354); respondents 3,694 (L346); burden 12,481.15 (L347); "de minis" (L345).
  - RFA: $850 million / $47 million (L362, fn 50 L373). OCC "currently supervises 1,040 institutions"; "approximately
    636 are small entities"; annual impact "could be 78 OCC-supervised small institutions in a given year,
    assuming that all merger applications are submitted by small banks" (L369). Significance 5 percent / 2.5
    percent; "5 percent or more of OCC-supervised small entities to be a substantial number"; "At present, 32
    OCC-supervised small entities constitute a substantial number" (L382). Certification L383.
  - UMRA: $100 million "(adjusted annually for inflation, currently $183 million)" (L388); "$183 million or more" (L399).
  - Congressional Review Act: major rule may not take effect "until at least 60 days following its
    publication" (L412); "$100,000,000 or more" (L419).
- Forecasts, guidance, deadlines, effective dates: effective January 1, 2025 (L32, L403); RCDRIA first day
  of a calendar quarter (L403); OCC "does not expect" a significant change in processing time (L78).
- Hedged claims (scope of hedge):
  - "The OCC believes that most transactions will be in this middle category and that many of these
    transactions are likely consistent with approval" (L151) - belief about a category that the appendix text
    does not name.
  - "$50 billion indicator merely reflects the likelihood of an expeditious approval"; OCC "may require
    additional time"; "many transactions where the resulting institution will have total assets of more than
    $50 billion are consistent with approval" (L153).
  - "The OCC is not aware of any application for a business combination having been deemed approved solely
    due to the passage of time" (L78; repeated L380).
  - Eliminating the streamlined application "may decrease the likelihood the OCC requests additional
    information" (L96, L380).
  - RFA: rule "will potentially affect a substantial number of OCC-supervised small entities" yet "will not
    have a significant economic impact on any small entities" (L382-383).
  - "G-SIB status is unlikely to be remediated" (L178) - preamble only.
- Rounded prose beside exact figures: "approximately 636" (L369); no yearly application counts are printed
  in D02 (compare D01 fn 32).
- Operative definitions, rules and scope exceptions:
  - Final amendment: "Section 5.33 is amended by removing and reserving paragraphs (d)(3), (i), and (j)" (L444).
  - Appendix A does not address competition or AML factors (fn 14 L117-118); OCC declines to use appendix A
    for competition (L124); convenience and needs can outweigh anticompetitive effects under 12 U.S.C.
    1828(c)(5)(B) (fn 15 L127).
  - Appendix A does not address disclosure of confidential supervisory information, reasons for withdrawal of
    applications, internal decision-making, or prefiling meetings (L124).
  - Conditions: 12 CFR 5.13(a)(1) governs; imposed case by case (fn 16 L128).
  - Preamble-only glosses: indicators "are not required for a transaction to be approved" (L152); indicators
    of concern "do not preclude OCC approval" (L169); 50 percent indicator "is not intended to discourage
    mergers of equals" (L156); a comment filed "is insufficient alone to warrant a meeting" (L321); "Applicants
    need not make a showing with respect to any or all of these items" (L288); "A net positive impact ... is
    ... generally consistent with approval" (L287).
  - Credit-union acquirers: FDIC, not the OCC, is the responsible agency where assets and deposit liabilities
    go to an institution not covered by the Deposit Insurance Fund (fn 38 L283-284, 12 U.S.C. 1828(c)(1)(C)).
  - Statutory limits named without figures: BMA national deposit cap, Riegle-Neal national and State deposit
    caps, Dodd-Frank liability cap (L169; fn 23 L173, fn 25 L175).
- Proposals versus actions (commenter suggestions the final rule did not adopt): keep expedited review for
  banks under a certain size (L71) and for small entities (L103-108, L368); raise the indicator to $100
  billion (L153); low-risk category below $10 billion (L217); scored stability factors (L217-218); integration
  plan, diversity, climate items (L265); three-year branch-closure list and prohibition (L274, response L288);
  CRA rating as primary convenience-and-needs test (L289); 60-day comment period (L306, response L307-312);
  meeting whenever requested or protested (L319-321).
- Amendments or contradictions: see "D01 vs D02" below for every change and each preamble description.
- Notes: cited decisions - OCC Conditional Approval #1298 (November 2022) L194, L207; OCC Corporate Decision
  #2012-05 (April 2012) L194; FRB Order No. 2012-2 (February 14, 2012) at 30 (L200); FRB Order No. 2021-04
  (May 14, 2021) at 24 (L201); Comptroller's Licensing Manual "Business Combinations" at 23 (January 2021)
  (fn 33 L234) and "(Jan. 2021) at 7" (fn 39 L292); 12 U.S.C. 2903(a)(2) (fn 26 L183); 89 FR 8084
  (February 6, 2024) (fn 43 L315). Authority citation L439.
- Coverage: full. L1-260, L261-440, L441-605 read sequentially in three chunks.

## D03 - FDIC Final Statement of Policy on Bank Merger Transactions

- Source: `docs/fr_2024_22189.txt` | 674 text lines | FR pages 79125-79140 (markers L67, L96, L135, L175,
  L208, L226, L253, L276, L296, L357, L404, L453, L512, L568, L615; no marker for 79125).
- Written or submitted by: Federal Deposit Insurance Corporation (FDIC) (L11-19). "By order of the Board of
  Directors. Dated at Washington, DC, on September 17, 2024. James P. Sheesley, Assistant Executive
  Secretary" (L667-671).
- Type, date, edition: Final statement of policy (L21). 89 FR No. 188, Friday, September 27, 2024 (L3-5);
  FR Doc 2024-22189, filed 9-26-24 (L7, L672). 12 CFR 303; RIN 3064-ZA31 (L13-15). "The Final Statement
  supersedes the prior FDIC Statement of Policy on Bank Merger Transactions on October 28, 2024" (L27).
  Earlier editions named but not in the bundle: Superseded Statement "last amended in 2008" (L36); 2022
  request for information 87 FR 18740 (March 31, 2022) (fn 1 L39); Proposed Statement 89 FR 29222
  (April 19, 2024) (L36, fn 2 L40); 1998 and 1989 statements (fn 14 L240-241).
- Period covered: not a data document. Dates only (see quantities).
- Outline: SUMMARY L25; DATES L27; contacts L29-30; I. Background L34-46 (fn 1-3 L39-46); II. Overview of
  the Final Statement L49-149: Introduction L54-56; Jurisdiction and Scope L58-61; Process and Adjudication
  L63-75 (fn 4 L72); Statutory Factors L77-88 (fn 5 L85); Monopolistic or Anticompetitive Effects L90-104
  (fn 6 L101); Financial Resources L106-109; Managerial Resources L111-113; Future Prospects L115-117;
  Convenience and Needs L119-128 (fn 7 L124); Risk to Stability L130-137 (fn 8 L140); AML L143-145; Other
  Matters L147-149. III. Summary and Discussion of Comments L151-294: general L153-157; Jurisdiction and Scope
  L159-169 (fn 9 L164-165, fn 10 L171); Process and Adjudication L177-188 (fn 11 L185); Monopolistic L192-215
  (fn 12 L200-201); Financial and Managerial Resources and Future Prospects L217-230; Convenience and Needs
  L232-268 (fn 13 L237-239, fn 14 L240-241, fn 15 L259-260); Risk to Stability L270-282; AML L284-286; Other
  Matters L288-294. IV. Administrative Law Matters L298-306 (fn 16 L303). V. Final Statement of Policy
  L308-663 (the SOP text): I. Introduction L314-325 (fn 17-22 L320-329); II. Jurisdiction and Scope L332-349
  (fn 23-26 L336-339, fn 27 L346); III. Application Process and Adjudication L351-398 (Overview L353-375,
  fn 28-29 L362-363, fn 30-33 L369-372, fn 34 L378; Merger Application Adjudication L381-398, fn 35-36
  L387-388); IV. Statutory Factors L400-625: intro L402-406 (fn 37 L409); Monopolistic or Anticompetitive
  Effects L412-438 (fn 38 L417, fn 39 L423, fn 40-41 L429-431); Nationwide Deposit Cap L440-442 (fn 42-43
  L445-446); Financial Resources L449-470 (fn 44-46 L458-460, fn 47 L467); Managerial Resources L472-506
  (fn 48 L477, fn 49 L486, fn 50 L493-494, fn 51 L501); Future Prospects L508-514 (fn 52 L517); Convenience
  and Needs L520-557 (fn 53-54 L525-526, fn 55-57 L533-535, fn 58 L541, fn 59-61 L546-548, fn 62 L554,
  fn 63 L560); Risk to Stability L563-609 (fn 64-65 L574-575, fn 66 L584, fn 67-68 L591-592, fn 69 L598,
  fn 70 L606; Other Stability Considerations L601-609); AML L611-625 (fn 71-73 L620-622, fn 74 L628);
  V. Other Matters and Considerations L631-651 (Interstate L633-637; Non-Banks L640-645; Operating
  Non-Insured Entities L648-651); VI. Resources L653-663.
- Entities and aliases: SOP = statement of policy (L316); Final Statement / Proposed Statement / Superseded
  Statement (L25, L36); BMA = section 18(c) of the FDI Act (L316); IDI = insured depository institution
  (L317); FDIC Board = FDIC Board of Directors (L69, L384); Federal Reserve Board (L137) = FRB (fn 24 L337);
  DOJ (L94, L375); HHI = Herfindahl-Hirschman Index (L197, fn 12 L200, fn 41 L431); CRA (L245, L366);
  CBAs = community benefit agreements (L264); FinCEN (L286, fn 51 L501); AML/CFT, BSA (L498, fn 51 L501);
  "management" = directors, officers and, as appropriate, principal shareholders (L474); "non-bank" = an IDI
  that is a bank for FDI Act purposes but not for BHCA purposes (fn 76 L645); "non-insured entity" = any
  entity that is not FDIC-insured (fn 23 L336); Board Briefings Resolution (L82); APM = Applications
  Procedures Manual (L72, L660). Contacts L29-30: George Small, Annmarie Boyd, Benjamin Klein, Jessica
  Thurman, Mark Haley, Ryan Singer. Mentioned, not issuing: OCC (fn 9 L164-165, fn 24 L337), Federal Reserve
  Board, DOJ / Attorney General, Consumer Financial Protection Bureau (L155), Senator A. Willis Robertson
  (fn 13 L237), United States v. Philadelphia National Bank, 374 U.S. 321 (1963) (fn 40 L429-430).
- Tables: none. HHI worked example is in fn 12 (L200-201).
- Lists (count, last item):
  - Circumstances likely to produce unfavorable findings: six, L392-396 (two share L395); last = incomplete,
    unsustainable, unrealistic or unsupported projections (L396).
  - Financial stability items: five, L578-579; last = cross-border activities. Preamble repeats the five at L132.
  - Resolvability tests inside the complexity discussion: (1)-(3), L589.
  - Additional managerial considerations: seven, L490-505 (three share L498); last = recent rapid growth (L505).
  - Ways an applicant may show public benefit: L522 (also L244).
  - Types of operating non-insured entities: L650. Resources: L655-663.
  - Other items commenters suggested (outside scope): L155.
- Quantities (unit, scope, line):
  - Comments: "The FDIC received 23 letters from the public in response to the Proposed Statement" (L43);
    "Only one comment letter" addressed AML effectiveness (L286).
  - "270 days": Board Briefings Resolution requires full FDIC Board briefings on merger, and certain other,
    applications "outstanding for more than 270 days since the application's filing"; "on June 18, 2024, the
    FDIC Board adopted" it (L82); fn 5 L85 cites "FDIC Board Resolution Seal No. 088980 (June 20, 2024)" and
    says it also applies to outstanding deposit insurance applications.
  - "$50 billion" (six locations): preamble L88 "$50 billion or more in total assets should be the subject of
    public meetings"; L128 "public hearings for mergers resulting in IDIs that have $50 billion or more in
    total consolidated assets"; fn 10 L171 "Even in cases where the IDI is over $50 billion in assets, it may
    not be necessary ... to hold public hearings"; L247 commenters (twice); L249 "over $50 billion in total
    assets will be the subject of hearings"; SOP L551 "generally expects to hold a hearing for any application
    resulting in an IDI with greater than $50 billion in assets or for which significant CRA protests are received".
  - "$100 billion": preamble L88 "$100 billion or more in total assets ... heightened financial stability
    analysis"; L137 "$100 billion or more in total consolidated assets" and "total assets over $100 billion
    ... aligns with the Federal Reserve Board's delegations of authority" (fn 8 L140 = 12 CFR
    265.20(c)(12)(vii)); comments L272-273; L278 "$100 billion in total assets or more ... not a threshold for
    a presumptive denial"; L279 "over $100 billion in assets"; L280 Form FR Y-15 firms "greater than $100
    billion"; SOP L580 "(e.g., in excess of $100 billion) ... will be subject to added scrutiny".
  - "$10 billion": commenters' de minimis requests - "less than $10 billion in total assets" (L179) and
    "(i.e., $10 billion or less)" (L282). Not adopted (L180, L282).
  - "0.4 percent of industry assets": commenter on a $100 billion IDI (L272).
  - "10 percent": nationwide deposit limit (L392, L406, L442; fn 42-43 L445-446); commenter "over 10 percent
    of U.S. deposits" (L155); commenter-suggested "10 percent tier 1 leverage ratio" (L222-223), not adopted.
  - HHI example: four firms with shares of 30, 30, 20 and 20 percent give 2,600 (fn 12 L201).
  - "three years": projected branch actions (L265-266, SOP L544, fn 59 L546); audited financial statements of
    operating non-insured entities "covering at least three years" (L651). "last three exams" (word): commenter
    on CRA (L251). "last five years" (word): commenter on regulator switching (L290).
  - Comment period: commenter request "from 30 days to 60 days"; periods are codified in Sec. 303.65 and
    "have not been changed" (L256).
  - "one or two CRA protest letters may not be considered significant enough to lead to a public hearing" (L250).
  - "three Federal banking agencies" (word): L317, L334.
- Forecasts, guidance, deadlines, effective dates: supersession date October 28, 2024 (L27); APM section 4
  "currently being revised" (L205) and "will be revised and issued subsequent to the publication" (L293-294).
- Hedged claims (scope of hedge): "generally expects to hold a hearing" (L551); "will generally result in
  unfavorable findings" for a less than Satisfactory CRA rating (L530), reductions in service (L544) and AML
  concerns (L625); "may present significant concerns" for consumer compliance rating (L538); "may not be able
  to find favorably" on resolvability (L589); statements on withdrawn applications "not expected for most
  transactions" (L188); "more likely to present potential financial stability concerns" (L580); the
  expedited-processing period lapsing "does not constitute an automatic or default approval" (L181).
- Rounded prose beside exact figures: none.
- Operative definitions, rules and scope exceptions:
  - Jurisdiction: FDIC acts on mergers involving an IDI and any non-insured entity, and IDI-only mergers where
    the acquiring, assuming or resulting institution is FDIC-supervised (L334); OCC and FRB jurisdiction (fn 24 L337).
  - Merger in substance: target "no longer a viable competitor" (L342); "no de minimis exception to the BMA" (L169).
  - Expedited processing: Sec. 303.64 "has not been changed"; removal under Sec. 303.11(c)(2) (L180-181).
  - Conditions "will not necessarily lead to the favorable resolution of any statutory factor" (L69, L182,
    L383); standard conditions Sec. 303.2(bb) (L383).
  - FDIC Board reserves authority: deny any merger; act where a factor is not favorably resolved; act where
    the Attorney General has not notified no significantly adverse effect (L69, L94-98, L384, L436; fn 36 L388).
  - Withdrawal: applicants "may be offered the opportunity to withdraw"; FDIC Board "may release a statement"
    (L398; preamble L75, L188).
  - CRA protest and adverse comment definitions: 12 CFR 303.2(l), 303.2(c) (fn 31 L370); frivolous comments
    excluded (L246, L250).
  - Financial resources: favorable finding "appropriate only in cases where the merger results in a combined
    IDI that presents less financial risk than the financial risk posed by the institutions on a standalone
    basis" (L455; preamble L108, L220). Higher capital as a non-standard condition (L464).
  - Convenience and needs: merger expected to enable the resulting IDI "to better meet the convenience and the
    needs of the community ... than would occur absent the merger" (L522); mergers between two IDIs only
    (fn 7 L124); credit unions not subject to CRA (fn 56 L534, L291).
  - Nationwide deposit cap exception: IDIs in default or in danger of default (L442, fn 43 L446).
  - Affiliate-only transactions "generally will not raise concerns" on stability (L609).
  - Exceptions to requesting the Attorney General's report: probable failure; affiliates (L375, fn 34 L378).
- Amendments or contradictions (preamble description vs SOP text, both locations):
  - Removed sentence, quoted at L219-220: "[t]he FDIC will not find favorably on the financial resources
    factor if the merger would result in a weaker IDI from an overall financial perspective"; L108 paraphrases
    it as "a weaker IDI from a financial perspective". Replacement at SOP L455.
  - Hearing threshold wording: "public meetings" (L88), "public hearings ... $50 billion or more in total
    consolidated assets" (L128), "over $50 billion in total assets" (L249), SOP "greater than $50 billion in
    assets" and separately "may also hold public or private meetings" (L551).
  - Stability threshold wording: "$100 billion or more" (L88, L137, L272, L278) vs SOP "in excess of $100
    billion" (L580) and "over $100 billion" (L137, L279).
  - Stability section: preamble L132 "retains without change the Proposed Statement's discussion"; preamble
    L282 "has been revised to clarify that the evaluation considers the implications for the industry if the
    transaction is not approved or does not consummate". Whole-file search for "not approved" and "does not
    consummate" hits only L244 and L282 (both preamble); the SOP stability text L563-609, read in full, has
    no such sentence.
  - Job losses: preamble L268 "will request that applicants quantify or provide information regarding job
    losses to the extent those are known or knowable"; SOP L544 lists "any job losses or lost job opportunities
    from branching changes" among items "closely evaluated"; "known or knowable" appears only at L268.
  - Reduced services: preamble L244 "Applications that project reduced or diminished banking services will
    generally result in unfavorable findings"; SOP L544 "Applications that project material reductions in
    service, especially to low- and moderate-income communities or consumers".
  - Property waivers: preamble L104 "also expects the IDI to waive any terms or conditions (e.g., exclusive
    use clauses)"; SOP L438 "may request an IDI ... to waive any terms or conditions".
  - Non-compete: preamble L214 "will generally not view favorably"; SOP L437 "generally expects that the
    selling IDI will neither enter into ... nor enforce".
  - Board Briefings Resolution date: text "June 18, 2024" (L82) vs fn 5 "(June 20, 2024)" (L85).
  - Footnote cross-references as printed: "See generally note 41" in fn 46, 54, 57, 61, 66, 67, 69, 70, 72,
    74 (L460, L526, L535, L548, L584, L591, L598, L606, L621, L628) although fn 41 (L431) is the HHI note;
    fn 50 "See footnote 28" (L493-494) although UFIRS is fn 45 (L459) and fn 28 (L362) is the APM note; fn 21
    "Ibid." (L328).
  - "While not explicitly stated, the evaluation also considers the implications if the transaction was not
    approved" (L244) - preamble statement about convenience and needs.
- Notes: Applications Procedures Manual section 1.1 and 1.11 (fn 4 L72, fn 11 L185), section 4 Mergers (L205,
  L293-294, L662); Delegations of Authority Seal No. 086825 (October 20, 2020) (fn 35 L387); E.O. 14036
  (July 9, 2021) (L94, fn 6 L101); UFIRS 61 FR 67021 (December 19, 1996) (fn 45 L459); Consumer Compliance
  Rating System 81 FR 79473 (Nov. 14, 2016) (fn 49 L486, fn 58 L541); Branch Closing policy 64 FR 34845
  (June 29, 1999) (fn 60 L547, L659); 63 FR 44761, 44764 (Aug. 20, 1998) and 54 FR 39042, 39047
  (Sep. 22, 1989) (fn 14 L241); 112 Cong. Rec. 2542 (1966) (fn 13 L237-238); no PRA collection (L306).
- Coverage: full. L1-149, L150-298, L299-548, L549-674 read sequentially in four chunks.

## D04 - FDIC proposed rule, Establishment and Relocation of Branches and Offices

- Source: `docs/fr_2025_13568.txt` | 670 text lines | FR pages 33898-33910 (markers L19, L75, L129, L159,
  L202, L247, L283, L329, L369, L417, L467, L557, L625).
- Written or submitted by: Federal Deposit Insurance Corporation (L21-29). "By order of the Board of
  Directors. Dated at Washington, DC, on July 15, 2025. Debra A. Decker, Executive Secretary" (L664-667).
- Type, date, edition: Proposed rule (L31). 90 FR No. 136, Friday, July 18, 2025 (L3-5); FR Doc 2025-13568,
  filed 7-17-25 (L7, L668). 12 CFR Parts 303 and 345; RIN 3064-AG10 (L23-25). "Send comments on or before
  September 16, 2025" (L37). No final rule in the bundle.
- Period covered: branch applications "From 2015 to 2024" (L110-112, L281, L367); supervisory baseline "as of
  the quarter ending March 31, 2025" (L280-281, L367, L386, L392); final status of applications "as of June
  24, 2025" (fn 40 L322, fn 52 L403); "Over the past five years" for comment counts (L131). Calendar years.
- Outline: SUMMARY L35; DATES L37; ADDRESSES L39-46; contacts L48-49; I. Policy Objectives L53-61 (fn 1 L58);
  II. Background Information L63-112: A. Statutory Requirements L65-77 (fn 2 L70, fn 3 L80); B. FDIC Rules and
  Regulations L83-106 (fn 4-5 L88-89, fn 6-7 L95-96, fn 8-9 L102-103); C. Branch Application Statistics
  L108-112. III. Description of the Proposed Rule L114-275: A. Rules of General Applicability L116-147
  (1. Public Notice 12 CFR 303.7 L118-140, fn 10-13 L121-124, fn 14 L137, fn 15 L143; 2. Hearings 12 CFR
  303.10(a) L146-147); B. Definitions 12 CFR 303.41 L149-179 (Branch L151-152; Branch Relocation L153-156;
  De Novo Interstate Branch L157-161; Remote Service Unit L162-175; fn 16 L166, fn 17 L171, fn 18 L178-179);
  C. Filing Procedures 12 CFR 303.42 L182-208 (fn 19 L195); D. Processing 12 CFR 303.43 L210-267 (1. L212-242,
  fn 20 L217, fn 21 L225, fn 22 L231-233, fn 23 L239; 2. L243-256, fn 24 L252; 3. FDIC Internal Processes
  L257-267, fn 25-27 L261-263); E. Public Notice 12 CFR 303.44 L269-271; F. 12 CFR 303.184 L273-275.
  IV. Expected Effects L277-338 (fn 28-30 L287-289, fn 31 L295, fn 32-35 L300-303, fn 36-38 L310-312,
  fn 39-40 L320-322, fn 41-42 L334-335). V. Alternatives Considered L340-343. VI. Request for Comments
  L345-354. VII. Regulatory Analysis L356-488: A. RFA L358-411 (fn 43-44 L363-364, fn 45-47 L374-377,
  fn 48 L383, fn 49 L389, fn 50 L395, fn 51-52 L401-403); B. PRA L413-450 (fn 53-55 L422-424, fn 56 L436);
  C. Plain Language L452-461; D. RCDRIA L463-472 (fn 57-58 L471-472); second "D." Providing Accountability
  Through Transparency Act L475-484 (fn 59 L480); E. Executive Orders 12866 and 14192 L486-488. List of
  Subjects L490-498; proposed regulatory text L500-660: Sec. 303.7 L512-521; Sec. 303.10 L523-526; Sec.
  303.40 L528-535; Sec. 303.41 L537-559; Sec. 303.42 L561-572; Sec. 303.43 L574-582; new Sec. 303.44 Special
  provisions L584-594; Sec. 303.45 L596-601; Sec. 303.184 L603-640; Part 345 appendix G Sec. 345.29(c) L642-660.
- Entities and aliases: FDI Act; "statutory factors" = section 6 FDI Act factors (L73); subpart C / subpart A /
  subpart J of 12 CFR part 303 (L58, L85, L106, L132); RSU = remote service unit (L152); ITM = interactive
  teller machine (L174); APM = Application Procedures Manual (L258); RO = regional office (L258); IDIs here =
  FDIC-supervised insured State nonmember banks and insured branches of foreign banks (L280); UFIRS = Uniform
  Financial Institutions Rating System (L92); OIRA (L488). Contacts L48-49: Sandra Macias, Scott Leifer, Tara
  Oxley, Benjamin Klein, Karlyn Hunter, Julia Dempewolf. Comments to Jennifer Jones, Deputy Executive
  Secretary (L42). Mentioned, not issuing: OCC (L163, fn 16 L166, fn 17 L171), "the Comptroller" (L619), SBA (L360).
- Tables: none. Statistics are in prose (L110-112, L281, L298, L367).
- Lists (count, last item):
  - Section 6 statutory factors: (1)-(7), L73-77; last = corporate powers consistent with the FDI Act.
  - "Eligible depository institution" criteria: (1)-(5), L92; repeated as five clauses L222-223; last = not
    subject to a cease and desist order, consent order, prompt corrective action directive, written agreement,
    memorandum of understanding, or other administrative agreement.
  - Current content of filing: six items, L189-193 (fifth and sixth share L193). Proposed: four items,
    L205-208 and regulatory text (1)-(4) L567-570. "from six to four items" (word) L292, L307, L380.
  - Current deemed-approved triggers: (1)-(3), L99 and L214. Proposed: (1)-(2), L229 and L579-580.
  - Reasons to remove a filing from expedited processing (current): four clauses, L237.
  - De minimis change-in-address examples: (1)-(3) L154; (A)-(C) L548-550.
  - RSU inclusions: L163, L559; last = drop boxes.
  - Request for comment: seven questions numbered 1, 2, 2, 3, 4, 5, 6 (L348-354).
  - Sec. 303.184(c)(1) approval criteria (i)-(vi): L630-636.
- Quantities (unit, scope, line):
  - Branch applications received, 2015 to 2024: 6,641 total = 5,059 to establish a branch, 461 to relocate a
    main office, 1,120 to relocate a branch, 1 to relocate an insured branch of a foreign bank; "an average of
    664 applications received per year" (L110-111; repeated L281). Mapper check: the four parts sum to 6,641.
  - Approved: "an average of 630 branch applications annually (482 branch establishment applications, 105
    branch relocation applications, and 43 main office relocation applications)"; "On average, 537 applications
    per year were approved under expedited processing (85 percent) and 93 ... under standard processing (15
    percent)" (L111-112).
  - Average time from receipt to approved, denied, returned or withdrawn: "25 days for applications subject to
    expedited processing and 69 days for applications subject to standard processing" (L112); 25 days repeated
    L317, L399.
  - Comments: "an average of seven comments per year" (word) on branch applications over the past five years (L131).
  - Current expedited timing: deemed approved on the latest of "21 days after" receipt of a substantially
    complete application (L99) / "the 21st day" (L214); "the 5th day after" the comment period expires; "the 5th
    day after" host State confirmation (L99, L214). Current filing timing: on the date of newspaper notice or
    "within five days after" the last publication (L185).
  - Proposed expedited timing: "the third business day after receipt" (L229, L256; text L579, L581, L622);
    de novo interstate branch "the fifth day" (L229) / "the 5th day" (text L580). RO single letter "within
    three business days" (L267).
  - Proposed relocation eligibility: "FDIC-assigned composite rating of 3 or better under the UFIRS" (L244,
    L255, L316, L399; text L581).
  - Expected effects: FDIC supervises 2,835 State nonmember banks or insured branches of foreign banks
    operating 25,424 branches and main offices, as of March 31, 2025 (L281); "approximately 700 branch
    applications per year" affected (L281-285; fn 30 L289); de minimis relocation: "five-hour burden", "$200
    per hour", "$1,000 per de minimis relocation", distance "less than 0.1 miles", "299" of 6,641,
    "approximately 30 branch applications per year", "$30,000 annually" (L298; fn 35 L303: 30 = 299
    applications / 10 years); fully loaded cost "approximately $147 per hour" State nonmember banks and "$135
    per hour" foreign banks (fn 33 L301, fn 37 L311, fn 49 L389); "remaining 670 branch applications",
    "approximately two hours", "approximately $268,000 per year" (L306-307; fn 38 L312 prints the product 670 applications, 2 hours, $200);
    "approximately $300,000 in savings per year" for "all 700" (L315).
  - Processing-time reduction: "a deadline of three days ... a reduction of between 18 days and 28 days,
    respectively" (L316, L399); fn 39 L320-321 and fn 51 L401-402: comment period path "at most could be 23
    days (consisting of 8 days to meet the newspaper publication requirement plus a 15 day comment period),
    and 5 + 23 = 28"; "three days (down from 21)" = 18.
  - RFA: small = total assets "less than or equal to $850 million" (L360, fn 44 L364); 5 percent / 2.5
    percent thresholds (L360); 2,835 IDIs of which 2,109 small; small IDIs "collectively operated 8,412
    branches and main offices"; small-IDI applications 2015 to 2024: 2,020 establish, 352 relocate a branch,
    295 relocate a main office, "total of 2,667 applications across all 10 years, or an average of 267
    applications per year" (L367); "approximately 300" per year (L371; fn 47 L377); "upwards of 30" de minimis
    relocations, "upwards of 10" involving small IDIs (L386); "remaining 290"; "$400 per application" (L392);
    "would not significantly affect more than two small IDIs" (L398); "300 small IDIs" (L408). No insured
    branches of foreign banks are small (fn 46 L376).
  - PRA: OMB 3064-0070: average time per response "from 5 hours to 3 hours"; respondents "from 436 to 700";
    total "2,100 hours, a decrease of 80 hours" (L432-433). OMB 3064-0114: "placeholder of a single
    respondent" (L444). Extension "for three years" (L419). Comments within 60 days (L450).
  - Special provisions (text): notify within 3 days of emergency relocation (L589); filing within 10 days
    (L590); approval expires within 18 months (L593-594).
  - PATA summary "not more than 100 words" (L477).
- Forecasts, guidance, deadlines, effective dates: comment deadline September 16, 2025 (L37); FDIC "intends
  to review its delegations of authority" (L258) and "to update its internal processes" (L266); no effective date.
- Hedged claims: "the likelihood that opening a new branch would present material supervisory concerns is
  extremely remote" (L242); FDIC "does not believe the proposed rule would likely result in a material
  increase in the number of branch applications" (fn 30 L289, fn 47 L377); 700 and 300 are "conservative"
  estimates (L289, L377); "may result in some confusion" (L331); not expected to be an E.O. 14192 action (L488).
- Rounded prose beside exact figures: 664 (average) beside 6,641 over 2015 to 2024 (L110-111); "approximately
  700" beside 664 (L281-285); 267 beside 2,667 (L367); "approximately 300" beside 267 (L371); "approximately
  30" beside 299 over 10 years (L298, fn 35 L303); "approximately $300,000" beside $30,000 and $268,000
  (L298, L307, L315); "$200 per hour" conservative beside $147 and $135 (L298, fn 33 L301); 85 percent / 15
  percent beside 537 / 93 of 630 (L112).
- Operative definitions, rules and scope exceptions:
  - Eligible depository institution: 12 CFR 303.2(r), five criteria (L92, L221-223); retained (L220).
  - Branch relocation = move within the same immediate neighborhood (fn 24 L252, L245; text L544); de minimis
    change in address is neither a branch establishment nor a branch relocation (text L546-551), but advance
    written notice to customers and advance notice to the FDIC remain (L156, L551).
  - De novo interstate branch (L157-161; text L553). Remote service unit (L163; text L555-559). ITM criteria
    from FIL-53-2024 (Aug. 9, 2024) (L174-175, fn 18 L178-179).
  - Expedited processing for intrastate relocations applies "regardless of whether the institution satisfies
    the other criteria in 12 CFR 303.2(r)" (L244).
  - Removal discretion eliminated (L220, L242, L256, L316, L399).
  - Public notice: section 18(d) of the FDI Act imposes no notice or comment requirement, unlike the Bank
    Merger Act and Change in Bank Control Act (L118, fn 11-12 L122-123); FDIC proposes to eliminate notice and
    comment for subpart C (L132) and newspaper publication (L271); State-law requirements not preempted (L271).
  - Foreign bank insured branch: expedited only "if the filer is proposing to move within the same State" (text L622).
- Amendments or contradictions (prose vs proposed regulatory text, both locations):
  - Branch exclusion: prose "a remote service unit (RSU) or a financial education program" (L152); text "a
    remote service unit or a facility described in Sec. 303.45" (L542).
  - "a deadline of three days" (L316, L399) vs "third business day" (L229, L256, L579, L581).
  - "the fifth day" (L229) vs "the 5th day" (L580).
  - "eliminate or greatly reduce public notice requirements" (L292, L380) vs "eliminate the public notice and
    related public comment period" (L132) and "Remove Sec. 303.44" (L584).
  - Definitions clarified: "de novo interstate branch" only (L326) vs "interstate branch, intrastate branch,
    and de novo interstate branch" (L407); the text defines only de novo interstate branch (L553).
  - Standard conditions cited as "Sec. 303.2(dd)" (L636); D03 cites "Sec. 303.2(bb)" (D03 L383).
  - "Under 12 CFR 303.183" (L443) beside "Section 303.184, Moving a Branch" (L443).
  - fn 14 cites "12 CFR 345.29(a) (Mar. 29, 2024)" (L137) for a sentence about 12 CFR 345.29(c) (L134).
  - As printed: two "Question 2." entries (L349-350); two "D." headings (L463, L475); marker \46\ appears
    before \45\ and is used twice in L367; fn 33 gives one URL then "respectively" (L301; two URLs in fn 37
    L311 and fn 49 L389); "Gramm-Leah-Bliley" (L454); "Office of Budget and Management (OMB)" (L419); PATA
    cited as "12 U.S.C. 553(b)(4)" (fn 59 L480); Change in Bank Control Act called "section 17(j) of the FDI
    Act" with cite 12 U.S.C. 1817(j)(2)(D) (L118, fn 12 L123).
- Notes: Delegations of Authority Resolution 086825 (Oct. 20, 2020) (fn 26 L262); OCC regulation 12 CFR 7.1027
  (fn 16 L166); 85 FR 83686, 83703 (Dec. 22, 2020) (fn 17 L171); FDIC CRA regulation "as in effect on March
  29, 2024" (L134); SBA size standard as amended by 87 FR 69118, effective December 19, 2022 (fn 44 L364).
- Coverage: full. L1-200, L200-379, L379-598, L598-670 read sequentially in four chunks.

## D05 - FDIC Request for Information on Industrial Banks and Industrial Loan Companies and Their Parent Companies

- Source: `docs/fr_2025_13589.txt` | 286 text lines | FR pages 34271-34276 (markers L57, L114, L164, L224,
  L266; no marker for 34271).
- Written or submitted by: Federal Deposit Insurance Corporation (L11-17). "By order of the Board of
  Directors. Dated at Washington, DC, on July 15, 2025. Debra A. Decker, Executive Secretary" (L279-283).
- Type, date, edition: Request for information and comment (L19); a notice, not a proposed rule. 90 FR No.
  137, Monday, July 21, 2025, [Notices] (L3-5); FR Doc 2025-13589, filed 7-18-25 (L7, L284). RIN 3064-ZA48
  (L13). "Comments must be received on or before September 19, 2025" (L25).
- Period covered: industry profile "As of March 31, 2025" (L128, fn 21 L131); history 1910-2025. Calendar dates.
- Outline: SUMMARY L23; DATES L25; ADDRESSES L27-34; contacts L36; I. Policy Objectives L40-49 (fn 1 L45-47,
  fn 2 L48-49); II. Background Information L52-178: intro L54-59 (fn 3-6 L61-64); A. The Industrial Bank
  Charter L67-77 (fn 7-9 L72-74, fn 10 L80); B. 2020-2021 Rulemaking--Part 354 L83-87 (fn 11 L90); C. Industry
  Profile L93-128 (fn 12-13 L98-99, fn 14-15 L105-106, fn 16-20 L119-124, fn 21 L131-132); D. Supervision
  Framework L135-166 (fn 22-25 L140-143, fn 26-28 L148-150, fn 29-30 L156-157, fn 31-32 L169-170); E. Other
  Considerations L173-178. III. Request for Comment L180-275: A. Information Relevant to Evaluation of
  Applicable Statutory Factors L184-232 (section 6 factors L186-194; fn 33-34 L199-200; 1. General Q1-4
  L203-207; 2. Adequacy of Capital Structure Q5 L208-209; 3. Risk to the DIF Q6-9 L210-215, fn 35 L218;
  4. Convenience and Needs Q10-12 L221-228; 5. Corporate Powers Q13 L229-230; 6. Other Statutory Factors Q14
  L231-232); B. Characteristics of Industrial Bank Parent Companies L234-260 (1. Foreign-Owned Q15-16
  L237-239; 2. Size and Market Share Q17-23 L240-249; 3. Non-Financial Companies Q24-30 L250-257; 4. Other
  Considerations Q31-32 L258-260); C. Existing Regulatory and Supervisory Framework Q33-34 L262-271;
  D. General Request Q35 L273-275.
- Entities and aliases: "industrial banks" = industrial banks and industrial loan companies together (L42;
  definition fn 2 L48-49); ILC (quoted GAO text L102); RFI (L42); BHCA = Bank Holding Company Act (fn 2 L48);
  FRB = Federal Reserve Board (L54); CEBA = Competitive Equality Banking Act of 1987 (L77); part 354 = 12 CFR
  part 354 (L85); DIF = Deposit Insurance Fund (L153); CALMAs = capital and liquidity maintenance agreements
  (L160-161); "Covered Company" (fn 35 L218); "nonbank bank" (fn 12 L98); "commercial firm" (fn 20 L124).
  Named institutions: Fidelity Savings and Trust Company of Norfolk, Virginia, established by Arthur Morris in
  1910 (L95); BMW, Target, Pitney Bowes, Harley Davidson (L102); Wal-Mart Bank (L111, L175); The Home Depot
  (L111); Nelnet Bank, Draper, Utah; Square Financial Services, Inc., Salt Lake City, Utah; Thrivent Bank,
  Salt Lake City, Utah (L127); UBS Bank USA (L128). Contacts L36: Catherine Topping, Gregory Feder, Rachel
  Harrison, Scott Leifer, Melanie Sheow. Comments to Jennifer Jones (L30). Mentioned, not issuing: GAO (L102,
  fn 15 L106, fn 32 L170), FRB, Department of the Treasury (fn 31 L169).
- Tables: none.
- Lists (count, last item): section 6 statutory factors, seven bullets L188-194 (same seven in fn 29 L156);
  Change in Bank Control Act disapproval grounds and BMA factors in fn 30 L157; 35 numbered questions, Q1 L204
  to Q35 L275; Q3 parent types (1)-(4) L206; Q8 parent types (1)-(5) L213; Q17 (a)-(c) L241; State charters
  in fn 21 L131-132 (five States, last = Minnesota).
- Quantities (unit, scope, line):
  - Part 354: final rule published February 23, 2021 (86 FR 10703, fn 11 L90), "took effect on April 1, 2021"
    (L85); applies to events "on or after April 1, 2021" (L87).
  - Industry assets: "between 1987 and 2006 ... total assets held by industrial banks grew from $4.2 billion to
    $213 billion" (L102).
  - Moratoria: "on July 28, 2006, the FDIC imposed a six-month moratorium" (word); "effective through January
    31, 2007", then extended "one additional year" for commercially owned applicants (L112); Dodd-Frank
    "three-year moratorium" (word) in 2010, "expired in July 2013" (L116). Notices: 71 FR 43482 (Aug. 1, 2006)
    fn 17 L120; 71 FR 49456 (Aug. 23, 2006) L112, fn 18 L121; 72 FR 5290 (Feb. 5, 2007) fn 19 L122.
  - "commercial firm" = derives "less than 15 percent of its annual gross revenues" from financial activities
    or from ownership or control of depository institutions (fn 20 L124).
  - New charters: "Since 2008, there have been three newly established industrial banks" (word): Nelnet Bank
    and Square Financial Services approved "in March 2020", FDIC-insured "in November 2020 and March 2021,
    respectively"; Thrivent Bank approved "on June 20, 2024", "commenced operations on June 1, 2025" (L127).
  - Profile "As of March 31, 2025": "23 industrial banks with $247.4 billion in aggregate total assets"; UBS
    Bank USA "$116.3 billion in total assets", controlled by a bank holding company subject to FRB supervision;
    "Six ... $10 billion or more; eight ... $1 billion or more but less than $10 billion; and the remaining
    nine ... less than $1 billion" (words) (L128). fn 21 L131-132: "15 were chartered in Utah, three in Nevada,
    three in California, one in Hawaii, and one in Minnesota"; "one additional industrial bank opened on June
    1, 2025". Mapper check: both breakdowns sum to 23.
  - Written agreements: "Of the 24 industrial banks, six are subject to written agreements (two are subject to
    capital maintenance agreements, one is subject to only a CALMA, and three are subject to both CALMAs and
    parent company agreements)"; "all but three became FDIC-insured between 1984 and 2006" (L162). "Previously
    10 other industrial banks ... were also subject to CALMAs and/or parent company agreements"; additional
    prudential requirements began "in March 2004"; GAO 2005 audit pages 41-44 (fn 32 L170).
  - Wal-Mart Bank application "In 2005"; The Home Depot change in control notice "In 2006"; both "ultimately
    withdrawn" (L111-112).
- Forecasts, guidance, deadlines, effective dates: comment deadline September 19, 2025 (L25); no proposal text.
- Hedged claims: review "will inform potential changes" (L42); companies that "have applied, or may in the
  future apply" (L42); FDIC "proposes to comprehensively review" (L177); industrial banks "fared similarly to
  other types of financial institutions" "For the most part" (L162).
- Rounded prose beside exact figures: none.
- Operative definitions, rules and scope exceptions:
  - "industrial bank" = insured State-chartered bank that is an industrial bank, industrial loan company or
    similar institution excluded from the BHCA definition of "bank" under 12 U.S.C. 1841(c)(2)(H); "does not
    include limited purpose trust companies and credit card banks" (fn 2 L48-49).
  - Part 354 applies to changes in bank control (12 U.S.C. 1817(j)), merger transactions (12 U.S.C. 1828(c))
    and deposit insurance applications (12 U.S.C. 1816) where the industrial bank is or would be controlled by
    a company not subject to Federal consolidated supervision (fn 1 L45-47).
  - 2006-2007 moratorium "was not applicable to industrial banks to be owned by financial companies" (L112-116).
  - Source of strength: section 38A(b) FDI Act (L146, fn 26-28 L148-150).
  - BMA factors as described here: "the money laundering record of insured depository institutions involved
    in the merger transaction" (fn 30 L157).
- Amendments or contradictions: "23 industrial banks" as of March 31, 2025 (L128, fn 21 L131) vs "Of the 24
  industrial banks" (L162); fn 21 states one more opened June 1, 2025. Scott Leifer's unit is "Division of
  Risk Management" here (L36) and "Division of Risk Management Supervision" in D04 (D04 L48).
- Notes: GAO-12-160 (Jan. 2012) quotation (L102, fn 15 L106); Pub. L. 100-86 (Aug. 10, 1987) (fn 10 L80);
  Pub. L. 111-203 section 603(a) (fn 20 L123-124); 12 CFR 354.4(b) (fn 35 L218).
- Coverage: full. L1-286 read sequentially in one pass.

## D06 - Federal Reserve Board proposed rule on reputation risk

- Source: `docs/fr_2026_03818.txt` | 280 text lines | FR pages 9499-9504 (markers L71, L114, L153, L193,
  L259; no marker for 9499).
- Written or submitted by: Board of Governors of the Federal Reserve System ("Board") (L11-20). "By order of
  the Board of Governors of the Federal Reserve System. Benjamin W. McDonough, Deputy Secretary of the Board"
  (L275-277).
- Type, date, edition: Notice of proposed rulemaking (L22); title "Prohibition on Use of Reputation Risk or
  Other Supervisory Tools To Encourage or Compel Banking Organizations To Engage in Politicized or Unlawful
  Discrimination" (L18). 91 FR No. 38, Thursday, February 26, 2026 (L3-5); FR Doc 2026-03818, filed 2-25-26
  (L7, L278). 12 CFR Part 262; Docket No. R-1884; RIN 7100-AH17 (L13-16). "Comments must be received on or
  before April 27, 2026" (L28). No final rule in the bundle.
- Period covered: MRA/MRIA analysis "over the past ten years" / "a ten-year period through March 2025"
  (L145); small-entity counts "As of the second quarter of 2025" (fn 19 L179); policy baseline June 2025 (L144).
- Outline: SUMMARY L26; DATES L28; ADDRESSES L30-35; contacts L37-38; Table of Contents L42-55;
  I. Introduction and Objectives of the Proposal L57-101 (fn 1-4 L63-66, fn 5-10 L76-82, fn 11-12 L88-89,
  fn 13-14 L97-98); II. Overview of the Proposal L103-118; III. Request for Comment L120-131 (Questions 1-9);
  IV. Economic Analysis L133-160 (A. Baseline L135-146, fn 15 L140-141; B. Economic Benefits and Costs
  L148-160); V. Administrative Law Matters L162-239 (A. PRA L164-166, fn 16-17 L169-170; B. RFA L173-198,
  fn 18-20 L178-180, fn 21-22 L187-188; C. Plain Language L200-217, fn 23 L206-207; D. RCDRIA L219-228,
  fn 24-25 L224-225; E. Providing Accountability Through Transparency Act L230-239, fn 26-27 L234-235); List
  of Subjects L241-243; proposed Sec. 262.9 L257-273: (a) Definitions (1)-(8) L263-270; (b) Statement of
  policy L271; (c) Prohibition on use of reputation risk L272; (d) Rule of construction L273.
- Entities and aliases: Board = Board of Governors of the Federal Reserve System (L26); "Federal Reserve" /
  "Federal Reserve System" (L137, L145); FBOs = foreign banking organizations (L137); MRAs / MRIAs = Matters
  Requiring Attention / Matters Requiring Immediate Attention (L145); SR 95-51 (fn 5 L76); IDIs (L221). Named
  other agencies: FDIC, OCC, NCUA (L60, fn 3 L65); OFAC (L117, L273); SBA (fn 19 L179). Contacts L37-38: Anna
  Lee Hewko, Mehdi Beyhaghi, Devyn Jeffereis, Asad Kudiya, Alyssa O'Connor, Harley Moyer.
- Tables: none in the document. fn 15 points to "Table 2" of an external Board report (L140-141).
- Lists (count, last item): 9 numbered questions L122-131; statutes in the rule of construction, 12 named,
  first = Bank Secrecy Act, last = Fair Housing Act (prose L117; text L273); definitions (1)-(8) L263-270;
  initial regulatory flexibility analysis contents (1)-(6) L175; "banking organization" components (prose
  L106-109; text L264); other risk channels named: "credit risk, market risk, liquidity risk, operational
  risk, and legal risk" (L93) and "credit, market, liquidity, and operational risk" (L151); SR 95-51
  "listed six risk channels, one of which was reputation risk" (word, L73).
- Quantities (unit, scope, line):
  - Announcement: Board "announced in June 2025" (L60, L144, L191); press release June 23, 2025 (fn 1 L63, fn 5 L77).
  - Other agencies: FDIC Press Release (October 7, 2025); OCC News Release 2025-21 (March 20, 2025) and OCC
    Bulletin 2025-4 (March 20, 2025); NCUA Press Release (September 25, 2025) (fn 3 L65). Their proposals: 90
    FR 48825 (October 30, 2025); 90 FR 48409 (October 21, 2025) (fn 4 L66).
  - History: reputation risk "increased in prevalence as a supervisory concept in the 1990s" (L69); "In 1995,
    the Board published guidance" (L73); SR Letter 95-51 (November 14, 1995) (fn 5 L76); SR Letter 96-14
    (May 24, 1996); SR Letter 03-22/CA Letter 03-15 (December 23, 2003) (fn 9 L81); E.O. 14331, 90 FR 38925
    (August 12, 2025) (fn 10 L82).
  - MRA/MRIA word search: "reputation" in "approximately 4.6 percent of MRAs/MRIAs for bank holding companies
    and savings and loan holding companies, 1.5 percent for state member banks, and 2.5 percent for FBOs
    operating in the United States over the past ten years"; method = percentage of examinations with at least
    one such finding per year, yearly percentages summed per institution type (L145); includes findings where
    reputation risk was one of several concepts (L146).
  - Small entities: total assets of $850 million or less; "approximately 2,796 small bank holding companies
    and approximately 157 small savings and loan holding companies, and approximately 443 small state member
    banks" as of the second quarter of 2025 (fn 19 L179).
  - PATA summary "not more than 100 words" (L232). Plain language rule applies to rules "published after
    January 1, 2000" (L203).
- Forecasts, guidance, deadlines, effective dates: comment deadline April 27, 2026 (L28); intends to include
  "permitted payment stablecoin issuers" as a banking organization after rulemakings under 12 U.S.C. 5901 et
  seq. (L125); training "If finalized" (L118).
- Hedged claims: benefits and costs since June 2025 "are expected to be de minimis" (L144, L195); benefits
  "are likely to outweigh the costs" (L160); organizations "would likely experience reduced regulatory burden"
  (L150); "could expand market access opportunities" (L156); "believes" no significant economic impact (L183,
  L197) while still publishing an initial regulatory flexibility analysis (L175, L183).
- Rounded prose beside exact figures: none.
- Operative definitions, rules and scope exceptions:
  - "reputation risk" = "the potential that negative publicity regarding an institution's business practices,
    whether true or not, will cause a decline in the customer base, costly litigation, or revenue reductions"
    (quoted from SR 95-51, L69); proposed text substitutes "a banking organization's" / "the banking
    organization's" (L110, L267).
  - "banking organization" (text L264): bank holding company; savings and loan holding company; state member
    bank; any subsidiary of those three; and the combined U.S. operations of a foreign banking organization.
    Cross-references: 12 CFR 225.2(c), 238.2(m), 208.2(g), 252.2, 211.21(o) (L106, L263-269).
  - Prohibition (c) L272; statement of policy (b) L271.
  - Carve-outs: proposal "would not prohibit criticism, supervisory feedback, or other actions to address
    other risk channels" (L116); rule of construction preserves authority under the listed statutes, including
    "the Bank Merger Act" and "the Change in Bank Control Act" (L117, L273).
  - "The proposal would only impose obligations on the Board itself" (L228); "would not impose mandatory
    requirements on any small entities" (L195).
- Amendments or contradictions (prose vs proposed text):
  - Banking organization: prose says subsidiaries of a bank holding company, savings and loan holding company
    and state member bank are included and that combined U.S. operations include "all U.S. subsidiaries of the
    foreign banking organization" (L106-109); text (2) lists "any subsidiary of a bank holding company,
    savings and loan holding company, and state member bank" (L264) while definition (8) "Subsidiary" also
    names a foreign banking organization as owner (L270).
  - Prose: "would implement, administer, and enforce applicable law consistent with the proposal" (L117); text:
    "consistent with subsections (b) and (c)" (L273).
  - "These agencies recently requested comment" names three agencies (L60) and cites two Federal Register
    notices (fn 4 L66).
  - As printed: "instructionsfor" (L31); "thesubject" (L34).
- Notes: authority citation for part 262 includes 12 U.S.C. 1828(c) (L254). PRA: no collections of
  information (L166). PATA cited as 5 U.S.C. 553(b)(4) (fn 26 L234).
- Coverage: full. L1-280 read sequentially in one pass.

## D07 - OCC final rule, Community Bank Licensing Amendments

- Source: `docs/fr_2026_04275.txt` | 478 text lines | FR pages 10491-10499 (markers L43, L80, L110, L139,
  L163, L222, L289, L421; no marker for 10491).
- Written or submitted by: OCC, Department of the Treasury (L11-22). Signed Jonathan V. Gould, Comptroller of
  the Currency (L474-475).
- Type, date, edition: Final rule (L24). 91 FR No. 42, Wednesday, March 4, 2026 (L3-5); FR Doc 2026-04275,
  filed 3-3-26 (L7, L476). 12 CFR Part 5; Docket ID OCC-2025-0273; RIN 1557-AF38 (L15-18). "The final rule is
  effective on April 3, 2026" (L31, L230). Its proposal: "On November 18, 2025" (L53), 90 FR 51577
  (Nov. 18, 2025) (fn 4 L56) - not in the bundle.
- Period covered: small-entity size at December 31, 2024 (fn 21 L205); supervised-institution count from the
  "Financial Institutions Data Retrieval System on February 18, 2026" (fn 20 L204).
- Outline: SUMMARY L28-29; DATES L31; contacts L33; I. Background L37-53 (fn 1-3 L48-50, fn 4-5 L56-57);
  II. Description of the Final Rule L60-165: intro L62; Definitions (Sec. 5.3) L64-97 (fn 6 L70, fn 7-8
  L85-86, fn 9 L94, fn 10 L100); Expedited or Reduced Filing Procedures L103-145 (fn 11 L116, fn 12 L122-123,
  fn 13-14 L132-133, fn 15-16 L148-149); Adverse Comments L152-165 (fn 17 L158). III. Regulatory Analysis
  L167-259: PRA L169-191 (fn 18 L174); RFA L193-209 (fn 19 L198, fn 20-21 L204-206); UMRA L211-224 (fn 22-23
  L216-217); RCDRIA L226-231; Executive Order 12866 L233-236; Executive Order 14192 L238-241; Congressional
  Review Act L243-259 (fn 24-25 L248-249, fn 26 L256). List of Subjects L261-263; amendatory instructions
  1-22 L269-472.
- Entities and aliases: "covered community bank or covered community savings association" (defined L282-292);
  "community national banks and community Federal savings associations" (L53, L62); "expedited or reduced
  filing procedures" (L40); PCA = prompt corrective action (L41); Call Report = Consolidated Report of
  Condition and Income (L67); UMRA (L213); OIRA, OMB (L235); "Community Bank group" (L78). Contacts L33:
  Christopher Crawford, "Acting Assisting Director" as printed, and Scott Burnett, Counsel, Chief Counsel's
  Office, 202-649-5490. Mentioned, not issuing: FDIC (L76, L97, fn 10 L100), SBA (L195), GAO (L259).
- Tables: none.
- Lists (count, last item): definition prongs (1)(i)-(iii) and (2), L283-292; amendatory instructions 1-22
  (21 sections of part 5 amended, Sec. 5.3 through Sec. 5.59, L277-472); E.O. 12866 "significant regulatory
  action" tests (1)-(4) L235; "major rule" tests (1)-(3) L252-253; Sec. 5.47(f)(1)(i)(B) conditions (1)-(3)
  L419-424 and (f)(2)(i)(B) conditions (1)-(4) L430-433; commenter-suggested additions to the definition
  (1)-(3) L77. Filing-type list: see "D02 vs D07" below.
- Quantities (unit, scope, line):
  - "$30 billion": SUMMARY "less than $30 billion in total assets" (L28); L53; definition "less than $30
    billion ... not an affiliate of a depository institution or foreign bank with $30 billion or more" (L67;
    text L284); commenters L74, L76; L78; aggregation L90; business combinations L119 (text L349).
  - Comments: "The OCC received eight responsive comments to the proposal" (word); "Three commenters broadly
    supported" (word) (L53); "one comment discussing various regulatory analyses" in addition (fn 5 L57);
    "Three commenters strongly supported" the definition (L74); "Two commenters" on review capacity (L105).
  - Outcome: "finalizing these proposed amendments with one change" (L53).
  - History: expedited or reduced filing procedures first introduced "in 1996" (L40; 61 FR 60342-43
    (Nov. 27, 1996), fn 1 L48); "since 1996" (L127-128, L155); "more than 160 years" of supervision (L78).
  - "thirteen types of filings" (word) with expedited review for eligible banks or eligible savings
    associations (L105, L108).
  - "a 45-day review period": commenter's description of expedited business-combination review (L126).
  - Sec. 5.33(j) thresholds quoted in fn 12 L122-123: "no more than 50 percent"; "do not exceed 10 percent" (twice).
  - "no later than 10 days after making" a non-controlling investment (L144, twice).
  - Sec. 5.46(i)(2) text: "deemed approved by the OCC 15 days after the date the OCC receives the application";
    plan for "up to four consecutive quarters"; "four-quarter period" (L396).
  - Sec. 5.47(f)(2)(i)(B)(4) text: prepayment "equal to or greater than one percent of the national bank's
    total capital" (word, L433).
  - "chartered prior to October 15, 1982" (fn 15 L148).
  - PRA: OMB 1557-0014 (L171, L179, L191); respondents 3,694 (L183); burden 12,481.15 (L184); "de minimis"
    (L182); comments within 30 days (L191).
  - RFA: $850 million / $47 million (L195, fn 21 L205). OCC "currently supervises 997 institutions";
    "approximately 609 are small entities"; "on average, up to 68 OCC-supervised institutions could be impacted
    by the rule"; 5 percent / 2.5 percent; "5 percent or more ... a substantial number"; "at present, 30
    OCC-supervised small entities would constitute a substantial number" (L201). Certification L209.
  - UMRA: "$100 million or more in any one year ($187 million as adjusted annually for inflation)" (L213).
  - E.O. 12866: "$100 million or more" (L235). E.O. 14192: "at least ten existing regulations" (word) and "at
    least ten prior regulations" (L240-241).
  - Congressional Review Act: "at least 60 days following its publication" (L246); "$100,000,000 or more"
    (L252); OMB determined "not a major rule" (L259).
- Forecasts, guidance, deadlines, effective dates: effective April 3, 2026 (L31, L230); RCDRIA first day of a
  calendar quarter described L229; indexing "may" be addressed "in a subsequent rulemaking" (L89).
- Hedged claims: community institutions "typically engage in lower risk and less complex activities" (L62,
  L78); OCC "will generally be able to review filings ... more quickly" (L62); "up to 68" institutions "could
  be impacted" (L201); "there would likely be a decrease in expenditures" (L220).
- Rounded prose beside exact figures: "approximately 609" (L201).
- Operative definitions, rules and scope exceptions:
  - Covered community bank or covered community savings association (text L282-292): national bank or
    Federal savings association that (i) "Has less than $30 billion in total assets, as reported in the ...
    Call Report, and is not an affiliate of a depository institution or foreign bank with $30 billion or more
    in total assets"; (ii) "Is well capitalized as defined in Sec. 5.3"; (iii) "Is not subject to a cease and
    desist order, a consent order, or a formal written agreement, that requires action to improve the
    financial condition ... unless otherwise informed in writing by the OCC". "affiliate" = any company that
    controls, is controlled by, or is under common control with, per Sec. 5.50(d)(4) (L287-292; preamble L67).
  - Not in the definition (commenter requests rejected): CRA rating of Outstanding or Satisfactory; absence
    of adverse public comment; absence of fair housing, fair lending or consumer protection orders (L77,
    response L91); inflation indexing (L74, L89); FDIC "community bank" definition (L76, L97); standalone
    (non-aggregated) asset test (L75, L90).
  - Enforcement-action prong "mirrors the current language in the 'troubled condition' definition in 12 CFR
    5.51(c)(7)(ii)" (L91). "The definition ... applies to the institution, not the filing itself" (L91).
  - Significant-concern standard added to Sec. 5.13(a)(2)(ii): "the OCC considers a concern to be
    significant if the facts are previously unknown to the OCC and, if proven accurate, would support denying,
    or imposing a condition on the approval of, the filing" (text L302; preamble L154-165).
  - OCC retains authority to extend or remove from expedited review, 12 CFR 5.13(a)(2)(i) (L91, L106, L128),
    and 12 CFR 5.2(b) discretion (L106-107).
  - Sec. 5.38 and Sec. 5.59 do not apply to Federal savings associations not subject to 12 U.S.C. 1828(m)
    (fn 15-16 L148-149).
- Amendments or contradictions (prose vs regulatory text, both locations):
  - The "one change" (L53) is the added reference to conditional approval: proposal "would support denial of
    the filing" (L154); final "would support denying, or imposing a condition on the approval of, the filing"
    (L302); described as "substantially as proposed with the additional reference to conditional approval"
    (L165). Definition adopted "as originally proposed" (L67) / "without alteration" (L78); Sec. 5.33(j)
    "without alteration" (L127).
  - Subordinated debt: preamble describes the existing eligible-bank test as "will not continue to be an
    eligible bank after the transaction" (L113); new covered-community-bank text uses "will not continue to be
    well capitalized after the transaction" (L419, L430) and adds a one percent prepayment condition (L433)
    that the preamble does not mention.
  - Business combinations: preamble says "add to paragraph (j) a new paragraph" (L119); text adds "(j)(1)(v)"
    (L341, L349); fn 12 quotes the existing options as (i)-(iv) (L122-123).
  - Capital distributions: preamble names Sec. 5.55(e)(1)(i) and (g)(1) (L136); text also amends (g)(2)(i) (L442).
  - Service corporations: preamble cites 12 CFR 5.59(f) and 5.59(h)(1)(i) (L145, fn 16 L149); text amends Sec.
    5.59(h)(2)(ii)(A) (L472). Operating subsidiaries of savings associations: preamble "Twelve CFR 5.38"
    (L145); text Sec. 5.38(f)(2)(ii)(A) (L377).
  - RCDRIA paragraph states the first-day-of-a-calendar-quarter rule (L229) and then "the overall effective
    date of April 3, 2026" (L230).
- Notes: OCC News Release 2025-89 (Sept. 18, 2025) (fn 7 L85); FDIC Community Banking Study (Dec. 2012)
  (fn 10 L100); 85 FR 80436 (Dec. 11, 2020) (fn 17 L158); 12 U.S.C. 1818(b) for conditions (L161);
  Comptroller's Handbook booklets "Bank Supervision Process," "Community Bank Supervision," "Large Bank
  Supervision" (fn 8 L86). Authority citation L274.
- Coverage: full. L1-478 read sequentially in one pass.

<!-- Read actual candidate-relevant passages with context and search the entire bundle for
duplicates/substitutes. A search is not a full read. Expand coverage when the candidate needs it;
lists/counts require the complete relevant universe, and needed gaps stay blocking. -->

## D01 vs D02 - proposed and final OCC text (edition relationship)

Both texts were read in full and compared paragraph by paragraph. "identical" means word-for-word apart from
line wrapping.

### A. Sec. 5.33 amendment and appendix placement

| Item | D01 proposed | D02 final | Change |
| --- | --- | --- | --- |
| Instruction 2 | L307 "removing and reserving paragraphs (d)(3), (i), and (j)" | L444 same words | identical |
| Instruction 3 | L309 "Add appendix A to part 5, subpart C" | L447 "Add appendix A to subpart C" | reworded |
| Appendix heading | L311 "Appendix A: Policy Statement Regarding Statutory Factors Under the Bank Merger Act" | L449-451 "Appendix A to Subpart C of Part 5--Policy Statement Regarding Statutory Factors Under the Bank Merger Act" | reworded |
| Authority citation | L302 | L439 | identical |
| Signature | L457-458 Michael J. Hsu, Acting Comptroller | L601-602 same | identical |

### B. Appendix A, paragraph by paragraph

| Paragraph | D01 | D02 | Change |
| --- | --- | --- | --- |
| I. Introduction | L315 "better understanding of the Office of the Comptroller of the Currency's (OCC's) consideration of certain statutory factors" | L455 "better understanding of how the Office of the Comptroller of the Currency (OCC) considers certain statutory factors" | reworded; rest identical |
| II opening sentences | L319 "range of potential actions on applications include" | L459 "includes" | grammar |
| II prefatory sentence | L320 "Applications that are consistent with approval generally feature all of the following indicators:" | L459 "Applications that tend to withstand scrutiny more easily and are more likely to be approved expeditiously generally feature all of the following indicators:" | reworded; now part of the opening paragraph |
| II.1 well capitalized | L321 "under Sec. 5.3 of this part and the resulting" | L460 "under Sec. 5.3, and the resulting" | "of this part" removed |
| II.2 size | L322 "total assets less than $50 billion" | L461 same | identical |
| II.3 CRA Outstanding or Satisfactory | L323 | L462 | identical |
| II.4 UFIRS/ROCA 1 or 2 | L324 | L463 | identical |
| II.5 consumer compliance 1 or 2 | L325 | L464 | identical |
| II.6 no open formal or informal enforcement actions | L326 | L465 | identical |
| II.7 no open or pending fair lending actions | L327 | L466 | identical |
| II.8 effective in combatting money laundering | L328 | L467 | identical |
| II.9 relative size | L329 "The target's combined total assets are less than or equal to 50% of acquirer's total assets" | L468 "The target's total assets are less than or equal to 50% of acquirer's total assets" | "combined" removed |
| II.10 eligible depository institution | L330 "as defined in Sec. 5.3 of this part" | L469 "as defined in Sec. 5.3" | "of this part" removed |
| II.11 competition | L331 | L470 | identical |
| II.12 legal or policy issue | L332 | L471 | identical |
| II.13 adverse comment | L333 | L472 | identical |
| II bridge ("If certain indicators ... unless and until") | L334-335 | L473-474 | identical |
| Concern 1 CRA Needs to Improve or Substantial Noncompliance | L336 | L475 | identical |
| Concern 2 consumer compliance 3 or worse | L337 | L476 | identical |
| Concern 3 UFIRS/ROCA 3 or worse | L338 | L477 | identical |
| Concern 4 G-SIB | L339 "organization, or subsidiary thereof" | L478 "organization or subsidiary thereof" | comma removed |
| Concern 5 | L340 "open or pending Bank Secrecy Act/Anti-money Laundering enforcement or fair lending actions, including referrals or notifications to other agencies" | L479 "open or pending Bank Secrecy Act/Anti-money Laundering, fair lending, or consumer compliance actions, including enforcement actions, referrals, or notifications to other agencies" | consumer compliance actions added; reworded |
| Concern 6 | L341 "Failure by the acquirer to adopt ... in a timely manner; or multiple enforcement actions against the acquirer executed or outstanding during a three-year period" | L480 "The acquirer has failed to adopt ... in a timely manner, or there have been multiple enforcement actions against the acquirer executed or outstanding during a three-year period" | reworded; same two conditions |
| III.A intro and factors 1-7 | L347-357 | L488-495 | identical |
| III.B.1 In general | L361 "section III(A) of this appendix" | L499 "section III.A. of this appendix" | citation form |
| III.B.2 Conditions | L362 "financial stability related conditions" | L500 "financial stability-related conditions" | hyphen |
| III.B.3 intro | L363 | L501 | identical; sub-items lettered b. and c. in both, no a. |
| III.B.3.b | L364-365 "12 CFR 30, appendix D" | L502-503 "12 CFR part 30, appendix D" | "part" added |
| III.B.3.c | L366 "Standards requirements applicable to the resulting institution's recovery planning pursuant to 12 CFR 30, appendix E" | L504 "Standards applicable to the resulting institution's recovery planning pursuant to 12 CFR part 30, appendix E" | "requirements" removed; "part" added |
| III.B.4 Concurrent filings | L367 | L505 | identical |
| IV intro | L371 | L509 | identical |
| IV.A.1 | L375 "resulting institutions, to their size" | L513 "resulting institutions to their size" | comma removed |
| IV.A.2 (new) | not present | L514 "The OCC considers these factors within the context of the prevailing economic and operating environment." | added |
| IV.A "more likely to approve ... than when" a-e | L376-381 as item 2 | L515-520 as item 3 | renumbered; identical |
| IV.A "normally does not approve" | L382 as item 3 | L521 as item 4 | renumbered; identical |
| IV.A comments and confidential supervisory information | L383 as item 4 | L522 as item 5 | renumbered; identical |
| IV.B.1.a, i, ii | L388-390 | L527-529 | identical |
| IV.B.1.b eight risk categories | L391 "earnings that can arise" | L530 "earnings, that can arise" | comma added |
| IV.B.1.c-d | L392-393 | L531-532 | identical |
| IV.B.2 intro, a, i-iii | L394-398 | L533-537 | identical |
| IV.B.2.a.iv | L399 "transaction, provided that" | L538-542 "transaction provided that" | comma removed |
| IV.B.2.b-e and holding-company sentence | L400-410 | L543-550 | identical |
| IV.B.3 Future Prospects | L411-416 | L551-556 | identical |
| V.A intro | L420 | L560 | identical |
| V.A.1 | L421 "any plans to close, expand, consolidate, or limit branches" | L561 "Any plans to close, consolidate, limit, or expand branches" | reordered; capital |
| V.A.2 | L422 | L562 | capital only |
| V.A.3 | L423 "credit availability throughout the community, including, for example, home mortgage, consumer, small business, and small farm loans" | L563 "Any plans to maintain, reduce, or improve credit availability throughout the community, including, for example, access to home mortgage, consumer, small business, and small farm loans" | reworded |
| V.A.4-6 | L424-426 | L564-566 | capitals only |
| V.B | L427 "public hearing or meeting for proposed business combinations" | L567 "public hearing or meeting related to the proposed business combination" | reworded |
| V.C | L428 | L568 | identical |
| VI heading | L430 "VI. Public Comments and Meetings" | L570 "VI. Public Comment Period and Public Meetings" | reworded |
| VI.A heading | L432 "A. Public Comments" | L572 "A. Public Comment Period" | reworded |
| VI.A.1-3 | L434-442 | L574-582 | capitals of sub-items only |
| VI.B heading, 1, 2 | L444-447 | L584-587 | identical |
| VI.B.3.a-c | L448-451 | L588-591 | capitals only |
| VI.B.3.d | L452-453 "$50 billion or more in total assets), and concentration" | L592-593 "$50 billion or more in total assets) and concentration" | comma removed |
| VI.B.3.e-f | L454-455 | L594-599 | capitals only |

Net: one item added (IV.A.2), three renumbered (IV.A.3-5), no item removed, no numeric threshold changed
($50 billion, 50%, three-year period, 30-day, ratings all unchanged).

### C. What the D02 preamble says changed, and what the text shows

| D02 preamble statement | Location | Regulatory text | Match |
| --- | --- | --- | --- |
| "adopting its proposed amendments to 12 CFR 5.33 in final form and making minor, clarifying modifications to proposed appendix A" | L59 | L444; section B above | consistent |
| "the final rule removes Sec. 5.33(i) and (j) as proposed ... also removes Sec. 5.33(d)(3)" | L109-110 | L444 | consistent |
| "finalizing Section I, Introduction, as proposed, with minor grammatical changes" | L124 | L455 reworded clause | consistent |
| "final appendix A includes prefatory text that notes that applications that feature all of the first set of indicators tend to be more likely to withstand scrutiny and to be approved expeditiously" | L152 | L459 "tend to withstand scrutiny more easily and are more likely to be approved expeditiously" | consistent in substance; wording differs |
| "these indicators are not required for a transaction to be approved" | L152 | no such sentence in L457-480 | preamble only |
| "a middle category of transactions" that "most transactions will be in" | L151 | no such category in L457-480 | preamble only |
| "finalizing the indicator as proposed at $50 billion or more in total assets" | L154 | indicator 2 reads "total assets less than $50 billion" (L461, same as D01 L322); "$50 billion or more" appears only in VI.B.3.d (L593) | indicator unchanged; preamble phrase differs from indicator wording |
| "deleting the word 'combined' referring to the target's total assets"; "finalizing this indicator as proposed" | L156 | L468 | consistent |
| enforcement, fair lending, competition and adverse-comment indicators "finalizing ... as proposed" | L161-162 | L465, L466, L470, L472 | consistent |
| G-SIB indicator "is appropriate"; will evaluate G-SIB applications "on their individual merits" | L178 | L478 (comma only) | indicator retained; individual-merits statement is preamble only |
| less than Satisfactory CRA rating "warranting inclusion on the list" | L180 | L475 | consistent |
| commenter "praised the inclusion of instances where an acquirer has experienced rapid growth as an indicator of supervisory or regulatory concern" | L180 | "rapid growth" is in IV.A.3.b (L517; D01 L378), not in the section II list L475-480 | location differs from the preamble's label |
| "making one change to the indicator regarding open enforcement actions ... including all types of consumer compliance enforcement actions" | L186 | L479 | consistent; concern 6 rewording (L480) is not separately described |
| "removing the word 'requirements'" in Section III; "otherwise generally finalizing Section III ... as proposed" | L219 | L504 | consistent |
| "adding a new overarching consideration in section IV" on "the prevailing economic and operating environment" | L266 | L514 | consistent; renumbering of items 3-5 not described |
| Section V: "changing the order" of close, consolidate, limit, expand; credit availability plans "to maintain, reduce, or improvement" (as printed) | L295 | L561, L563 ("improve") | consistent; V.B rewording (L567) not described |
| "revising the headings in section VI to specifically reference the public comment period" | L312, L323 | L570, L572 | consistent |
| principles of Sec. 5.33(i) "are reflected in section II of the final appendix A" | L78 | L459-472 | consistent |
| indicators of concern "do not preclude OCC approval" | L169 | bridge sentence unchanged: "unlikely to find ... unless and until" (L473) | preamble gloss; text unchanged from D01 L334 |

### D. Preamble and regulatory-analysis differences between the editions

- Restated summary of the proposal: D01 L124 "(ii) ... rating of 3 worse; (iii) a consumer compliance rating
  of 3 or worse ... or (vi)" becomes D02 L142 "(ii) ... 3 or worse; (iii) the acquirer has a consumer
  compliance rating of 3 or worse ... and (vi)"; "(G-SIB)" added; both keep "(v)" twice.
- Appendix D / E description: D01 L154 (recovery planning with appendix D; heightened standards with appendix
  E) vs D02 L210-211 (heightened standards with appendix D; recovery planning with appendix E).
- Capital sentence in both preambles omits "or liquidity" (D01 L167, D02 L231) which both texts contain
  (D01 L382, D02 L521).
- Footnotes: D01 fn 11 L113 (competition guided by the 1995 interagency document; FFIEC BSA/AML manual) is
  shortened in D02 fn 14 L117-118; the 1995 document moves to the comment summary (D02 L121). D01 fn 12 L119
  "CAMELS system" becomes D02 fn 17 L138 "CAMELS rating system" with six components. D01 fn 14 L127
  "identifies banking organizations" becomes D02 fn 19 L145 "identifies certain banking organizations". D01
  fn 17 L140 (no date) becomes D02 fn 28 L200 "(February 14, 2012)".
- D01 L74 sentence that the Licensing Manual "does not describe all of the OCC's considerations" has no
  counterpart in D02 L52. D01 L200 "is also considering, and welcomes comment on, whether to specify
  communities in addition to LMI communities" becomes D02 L267 "also sought comment on"; final V.A.1 still
  names only LMI areas (D02 L561).
- Only in D02: comment count 34 (L59); 45-day and 60-day target time frames (L76); "not aware of any
  application ... deemed approved solely due to the passage of time" (L78, L380); fn 6, 10, 11, 15, 16, 21-26,
  38, 39, 43-46, 49, 55-57; section E Congressional Review Act (L410-426); effective date (L32).
- Only in D01: III. Request for Comments (L218-220); ADDRESSES (L42-51); yearly merger-application counts
  (fn 32 L257); comment deadline (L40).
- RFA figures: institutions supervised 1,057 (D01 L252) vs 1,040 (D02 L369); small entities "approximately
  661" vs "approximately 636"; affected per year "38 OCC-supervised institutions" (D01 L252) vs "78
  OCC-supervised small institutions ... assuming that all merger applications are submitted by small banks"
  (D02 L369); size date December 31, 2022 (D01 fn 31 L255) vs December 31, 2023 (D02 fn 50 L373); "32 ...
  substantial number" only in D02 (L382). D01: removal of expedited review "would potentially affect OCC
  staff, but not affect banks" (L261); D02: "will likely not result in any change to the timing" (L377).
- UMRA inflation-adjusted figure: $182 million (D01 L271, L278) vs $183 million (D02 L388, L399).
- PRA figures unchanged: 3,694 and 12,481.15 (D01 L240-241; D02 L346-347).
- RCDRIA: D01 requests comment on the effective date (L289); D02 states January 1, 2025 (L403).

## D02 vs D03 - OCC policy statement and FDIC statement of policy (parallel topics)

Published two days apart (D02 Wednesday, September 25, 2024; D03 Friday, September 27, 2024). D02 takes effect
January 1, 2025 (D02 L32); D03 supersedes its predecessor October 28, 2024 (D03 L27). Each names the other
agency: D02 L121 (commenters urged coordination with the FDIC); D03 fn 9 L164-165 (OCC Licensing Manual
interpretation of "acquire the assets"), fn 24 L337 (OCC jurisdiction).

| Topic | D02 (OCC appendix A and preamble) | D03 (FDIC SOP and preamble) | In only one |
| --- | --- | --- | --- |
| Form of document | Final rule adding appendix A to 12 CFR part 5, subpart C, and removing Sec. 5.33(d)(3), (i), (j) (L26, L444-447) | Final statement of policy; "The regulation has not been changed" (L21, L180) | regulation amendment only in D02 |
| Public comments received | "34 substantive written comments" (L59) | "23 letters" (L43) | - |
| Factors covered | Financial stability; financial and managerial resources and future prospects; convenience and needs; comment period and meetings. Does not address competition or AML factors (fn 14 L117-118; L124) | All factors, each under its own heading, plus jurisdiction, process, deposit cap, interstate, non-banks, non-insured entities (L400-651) | competition, AML, jurisdiction, deposit-cap sections only in D03 |
| $50 billion | Indicator 2 for applications "more likely to be approved expeditiously": resulting institution "total assets less than $50 billion" (L459-461). Example of significance for a public meeting: "$50 billion or more in total assets" (L593). Heightened-standards guidelines apply "at least $50 billion" (L153) | "generally expects to hold a hearing for any application resulting in an IDI with greater than $50 billion in assets or for which significant CRA protests are received" (L551); preamble L88, L128, L249; exception fn 10 L171 | expedited-approval indicator only in D02; hearing expectation only in D03 |
| $100 billion | Commenter asked to raise the indicator "to $100 billion or more"; not adopted (L153-154). No $100 billion test in appendix A | Added scrutiny for transactions resulting in a large IDI "(e.g., in excess of $100 billion)" (L580); preamble L88, L137, L278-279; "not a threshold for a presumptive denial" (L278); aligns with Federal Reserve Board delegations (L137, fn 8 L140) | $100 billion scrutiny level only in D03 |
| $10 billion | Commenter: treat "institutions below $10 billion in assets" as low stability risk (L217); no such category in text | Commenters: de minimis exception "less than $10 billion" (L179), "$10 billion or less" (L282); "no de minimis thresholds were adopted" (L180) | neither adopts |
| Relative size of target | Indicator 9: target's total assets "less than or equal to 50%" of acquirer's (L468; L155-156) | none | only D02 |
| G-SIB | Concern indicator 4: acquirer is a G-SIB "or subsidiary thereof" (L478; L168-178) | Only a commenter's reference to "globally systemically important bank" (L272) | indicator only in D02 |
| Financial stability factors | Seven numbered factors (L489-495) including resolvability (6) and "any other factors" (7); balancing test weighing risk of approval against risk of denial, "particularly if ... a troubled target"; a single factor may suffice; stability benefits and enhanced prudential standards may offset (L499) | Five items: size, substitute providers, interconnectedness, complexity, cross-border (L578-579); resolvability considered within complexity, three tests (L589); regulatory framework "alone would not result in a favorable finding" (L603); cybersecurity and stress-testing records (L603); affiliate-only transactions generally no concern (L609) | balancing-test wording only in D02; interconnectedness heading, cybersecurity and stress tests only in D03 |
| Recovery planning / heightened standards | 12 CFR part 30 appendices D and E (L501-504) | Resolution scenarios, FDIC as receiver (fn 68 L592); commenter on resolution-planning requirements (L280) | part 30 references only in D02 |
| Concurrent / related filings | May consider concurrent filings for related transactions (L505; L218) | Related transactions and interim institutions evaluated in substance (L349); companion holding-company applications to the Federal Reserve Board (L137) | - |
| Financial resources | Pro forma capital; 12 CFR part 3 and 6.4; undercapitalized applicant bar (L527-529); eight risk categories (L530); "normally does not approve" less than adequate capital or liquidity (L521); "prevailing economic and operating environment" (L514) | Favorable finding "only in cases where the merger results in a combined IDI that presents less financial risk" than standalone (L455); higher capital as non-standard condition (L464); capital standards 12 CFR 324.10, 324.403 (fn 47 L467); commenter's 10 percent tier 1 leverage ratio not adopted (L222-223) | "less financial risk than standalone" test only in D03; eight-risk-category list only in D02 |
| Managerial resources | Ratings, MRAs, RAS conclusions, due diligence, integration plans, IT systems, governance (L533-550); less than satisfactory target ratings "do not preclude" approval (L538-542) | Management capability, organizational relationships, compliance management system, seven additional considerations (L474-506); existing or pending enforcement actions not "a bar" (preamble L221) | - |
| Rapid growth | Acquirer "has experienced rapid growth" among less-likely-approval characteristics (L517) | "Recent rapid growth and the record of management in overseeing and controlling risks" (L505) | - |
| Future prospects | L551-556 | L508-514 | - |
| Enforcement actions | Indicator 6 "no open formal or informal enforcement actions" (L465); concern indicators 5 and 6, "three-year period" (L479-480) | "both issued and pending enforcement actions" under non-compliance (L392); AML: "outstanding or proposed formal or informal enforcement action ... will generally result in unfavorable findings" (L625) | three-year count only in D02 |
| CRA rating | Indicator 3 Outstanding or Satisfactory (L462); concern indicator 1 Needs to Improve or Substantial Noncompliance (L475); 12 U.S.C. 2903(a)(2) (fn 26 L183); CRA record "separate and distinct" from prospective convenience and needs (L568) | "A less than Satisfactory historical rating or significant deterioration in CRA performance will generally result in unfavorable findings" (L530); review "not limited to the CRA record" (L530); 12 U.S.C. 2902(3)(E) and 2903(a)(2) (fn 53 L525) | - |
| Consumer compliance rating | Indicator 5 (1 or 2) L464; concern indicator 2 (3 or worse) L476 | "A less than Satisfactory consumer compliance rating may present significant concerns" (L538) | - |
| Convenience and needs standard | Prospective; six listed items (L560-566); preamble: "A net positive impact ... generally consistent with approval" and "Applicants need not make a showing with respect to any or all of these items" (L287-288) | Expects the merger to enable the resulting IDI "to better meet" convenience and needs "than would occur absent the merger"; applicants "expected to demonstrate" public benefit (L522) | "better meet ... than absent the merger" expectation only in D03 |
| Branch plans | "Any plans to close, consolidate, limit, or expand branches" (L561); commenter's three-year closure list not required (L274, L288) | "all projected or anticipated branch expansion, closings, or consolidations for the first three years" (L544); "at least three years of information" (fn 59 L546) | three-year information expectation only in D03 |
| Job losses | Item 4 "Job losses or reduced job opportunities" (L564); OCC agrees the BMA "does not require consideration of particular facts such as job losses" (L288) | "any job losses or lost job opportunities from branching changes" closely evaluated (L544); preamble L267-268 | - |
| Community benefit agreements | Commenters urged enforcement (L276-280); not added | "does not require CBAs or enforce their requirements"; claims and commitments made to the FDIC may be included in the Order (L264, L529) | - |
| Competition / HHI | Not addressed in appendix A (L124); indicator 11 "clearly would not have a significant adverse effect on competition" (L470); 1995 interagency document (L121); 12 U.S.C. 1828(c)(5)(B) (fn 15 L127) | Full section L412-438; HHI defined with example 2,600 (fn 12 L200-201; fn 41 L431); "does not include specific HHI metrics or benchmarks" (L204); deposits as "initial proxy" (L426); divestitures and non-compete (L437); rural markets (L414, L206-210) | HHI, market definition, divestitures only in D03 |
| Nationwide deposit cap | Named without a figure (L169; fn 23 L173) | "10 percent" (L392, L406, L442); exception for default (L442) | percentage only in D03 |
| AML | Indicator 8 "effective in combatting money laundering activities" (L467); factor not addressed in appendix A (fn 14 L117) | Section L611-625 | section only in D03 |
| Public comment period | 30-day; three extension instances; three examples (L574-582); commenter's "initial 60-day comment period for larger transactions" not adopted (L306-312) | Commenter asked "from 30 days to 60 days"; Sec. 303.65 "have not been changed" (L256) | extension criteria only in D02 |
| Public meetings / hearings | Three methods; balancing public interest against value or harm; six criteria (L586-599); a comment alone "is insufficient ... to warrant a meeting" (L321) | Hearing "generally" expected above $50 billion or with significant CRA protests; "may also hold public or private meetings" (L551); Sec. 303.10 (L249); one or two protest letters may not suffice (L250) | size-based hearing expectation only in D03 |
| Timing and processing | "aims to act promptly" (L459); target 45 days expedited and 60 days standard, from the Annual Report (L76); expedited review (15th day) removed (L65, L109-110) | Expedited processing under Sec. 303.64 retained; lapse is not "an automatic or default approval" (L180-181); Board briefings after "more than 270 days" (L82); expeditious approval under delegated authority when factors clearly favorable (L80) | 45/60-day targets only in D02; 270-day briefing only in D03 |
| Streamlined application | Removed (L87-97, L109-110) | Commenter request for a streamlined application and expedited review for small IDIs (L155, L179); no benchmarks adopted (L180) | - |
| Withdrawal of applications | OCC may request that an applicant withdraw "because any shortcomings are unlikely to be resolved in a timely manner" (L459); appendix A does not address reasons for withdrawal (L124) | Applicants "may be offered the opportunity to withdraw"; FDIC Board "may release a statement regarding the concerns" (L398; L75, L188) | public statement on withdrawals only in D03 |
| Conditions | May impose conditions enforceable under 12 U.S.C. 1818 for stability (L500) and systems integration (L547); 12 CFR 5.13(a)(1) (fn 16 L128) | Conditions "will not necessarily lead to the favorable resolution of any statutory factor" (L383; L69, L182); standard conditions Sec. 303.2(bb); non-standard conditions (L464, L551, fn 59 L546) | "not a substitute" principle only in D03 |
| Prefiling | Commenter concerns about prefiling meetings; not addressed in appendix A (L123-124) | "encourages prospective applicants to engage in a pre-filing process" (L355) | encouragement only in D03 |
| Decision authority | none stated | FDIC Board reserves authority; delegations of authority (L384, fn 35-36 L387-388) | only D03 |
| Credit unions | FDIC, not OCC, is the responsible agency for transfers to non-DIF institutions (fn 38 L283-284) | Same statute cite fn 27 L346; credit unions as competitors (fn 39 L423); extra information because not subject to CRA (fn 56 L534, L291) | - |
| Charter or regulator switching | Commenter on "charter shopping" (L123) | Commenters on recent charter switches and "last five years" (L290) | - |
| Climate and diversity suggestions | L217, L265, L274; declined (L265) | L224-230; not added | - |
| UFIRS definition | fn 17 L138 (CAMELS components) | fn 45 L459 (61 FR 67021) | - |

## D02 vs D07 - same 12 CFR part 5, 2024 final rule and 2026 final rule

### What D07 says about business combinations, expedited review and streamlined applications

- D07 L119: "Under 12 CFR 5.33(i), an application for a business combination is eligible for expedited review
  if the filing qualifies as a business reorganization as defined in 12 CFR 5.33(d)(3) or the filing qualifies
  as a streamlined business combination application as described in 12 CFR 5.33(j)" (present tense). fn 12
  L122-123 quotes Sec. 5.33(j) options (i)-(iv) with the 50 percent and 10 percent tests - the same four
  options quoted in D01 fn 9 L100 and D02 fn 12 L90-91.
- D07 L119: proposal "to add to paragraph (j) a new paragraph permitting the use of the streamlined
  application form when the acquiring national bank or Federal savings association is a covered community bank
  or covered community savings association and the transaction would result in a national bank or Federal
  savings association with less than $30 billion in total assets." Text: instruction 10, new Sec.
  5.33(j)(1)(v) (L336-349).
- D07 L126: a commenter said expedited review of business combinations was inconsistent with Bank Merger Act
  review, that "a 45-day review period" was insufficient, and that expedited review was "only conditioned on
  the acquirer being well capitalized".
- D07 L127-128: OCC "is adopting the revisions to 12 CFR 5.33(j) without alteration. The current streamlined
  application and expedited review process in Sec. 5.33 has been in place since 1996, and the OCC has a
  demonstrated history of completing reviews required under the Bank Merger Act under these procedures"; OCC
  can remove merger applications from expedited review; eligibility based on the acquirer's capital category
  "is consistent with the existing criteria"; OCC "will review the financial resources of both the existing
  and resulting institutions in accordance with the Bank Merger Act" (fn 14 L133 = 12 U.S.C. 1828(c)(5)).
- D07 L91: OCC "would consider any fair lending-related enforcement action as part of its review of the
  convenience and needs of the community to be served in a proposed merger under the Bank Merger Act" (fn 9 L94).
- D07 L105-108: "thirteen types of filings" (word) carry expedited review for eligible banks or eligible
  savings associations; the document does not number them. Sections named in L108-136 (mapper tally of 13
  sections): 5.20(j), 5.23(d)(4), 5.24(h), 5.26(e)(3), 5.30(f)(6), 5.31(f), 5.40(c)(4), 5.45(g)(3), 5.46(i)(2),
  5.47(f), 5.56(b)(1)(ii), 5.33(i)/(j), 5.55(g)(1).

### References in D07 to the 2024 rule or to intervening 2025 rules

- D02 removed and reserved Sec. 5.33(d)(3), (i) and (j) (D02 L109-110, L444), effective January 1, 2025 (D02 L32).
- D07 (published March 4, 2026) describes Sec. 5.33(d)(3), (i) and (j) as existing provisions (L119, fn 12
  L122-123, L127-128) and amends Sec. 5.33(j)(1)(iii)-(v) (L336-349).
- D07 contains no reference to D02, to appendix A, to 89 FR 78207, or to any rule restoring those
  paragraphs. Whole-file searches of D07 for "89 FR", "appendix A", "policy statement", "restor", "rescind",
  "reinstat", "interim final", "reserved" return nothing; "2024" occurs once, in "December 31, 2024" (size
  date, fn 21 L205); every "remov" hit concerns removal from expedited review or amendatory phrasing (L91,
  L106, L128, L154, L308-396). D07 was also read in full.
- The only 2025 items D07 cites: its own proposal, "On November 18, 2025" / 90 FR 51577 (Nov. 18, 2025) (L53,
  fn 4 L56); OCC News Release 2025-89, "OCC Announces Updates to Organizational Structure" (Sept. 18, 2025)
  (fn 7 L85). Other dated items: 61 FR 60342-43 (Nov. 27, 1996) (fn 1 L48); 85 FR 80436 (Dec. 11, 2020)
  (fn 17 L158); FDIC Community Banking Study (Dec. 2012) (fn 10 L100).
- Neutral statement of the relationship: the bundle holds the removal (D02) and a later amendment that
  presupposes the paragraphs exist (D07), and holds no document recording how they came back. Neither
  document states precedence over the other. This is missing source material, not unread text.

### Other D02 / D07 contact points

- Size lines: D02 indicator "less than $50 billion" (D02 L461) and meeting example "$50 billion or more"
  (D02 L593); D07 "less than $30 billion" for both the institution and the resulting institution (D07 L284, L349).
- Timing: D02 "45 days for expedited review and 60 days for standard review" as OCC target time frames (D02
  L76); D07 commenter's "45-day review period" (D07 L126). D02 "15th day after the close of the comment
  period" (D02 L65); D07 Sec. 5.46 "15 days after the date the OCC receives the application" (D07 L396).
- Streamlined form: D02 "the more complete record created with the Interagency Bank Merger Act Application
  provides the appropriate basis" (D02 L96); D07 extends the streamlined form to covered community acquirers
  (D07 L119, L349).
- Deemed approval: D02 "not aware of any application for a business combination having been deemed approved
  solely due to the passage of time" (D02 L78); D07 "demonstrated history of completing reviews ... under
  these procedures" (D07 L128).
- Adverse comments, 12 CFR 5.13(a)(2): D01 fn 6 L86; D02 fn 7 L67, fn 21 L165; D07 L91, L106, L154, L296-302, L396.
- 12 CFR 5.2(b) materially different procedures: D01 fn 10 L101; D02 fn 13 L100; D07 L107.
- Conditions: D02 fn 16 L128 (12 CFR 5.13(a)(1)), L500, L547 (12 U.S.C. 1818); D07 L161 (12 U.S.C. 1818(b)).
- Criteria a commenter wanted added to the D07 definition and that appear as D02 indicators: CRA rating of
  Outstanding or Satisfactory (D07 L77; D02 L462); no adverse public comment (D07 L77; D02 L472); fair
  lending and consumer protection orders (D07 L77; D02 L466, L479). D07 did not add them (D07 L91).
- "eligible depository institution" / "eligible bank" / "eligible savings association" as defined in 12 CFR
  5.3: D01 L116, L330, fn 9 L100; D02 L135, L152, L469, fn 12 L90-91; D07 L41, L108-113, L128, fn 13 L132.
- "well capitalized" under Sec. 5.3: D01 L321; D02 L460; D07 L67, L285.
- Identical in all three OCC documents: part 5 authority citation (D01 L302; D02 L439; D07 L274); OMB control
  number 1557-0014 with 3,694 respondents and 12,481.15 burden (D01 L240-241; D02 L346-347; D07 L183-184);
  List of Subjects (D01 L293; D02 L430; D07 L263).
- Changing across the three: institutions supervised 1,057 / 1,040 / 997 and small entities 661 / 636 / 609
  (D01 L252; D02 L369; D07 L201); institutions affected 38 / 78 / "up to 68"; substantial number not stated /
  32 / 30 (D02 L382; D07 L201); UMRA figure $182 million / $183 million / $187 million (D01 L271; D02 L388;
  D07 L213); size date December 31, 2022 / 2023 / 2024 (D01 L255; D02 L373; D07 L205); signatory Michael J.
  Hsu, Acting Comptroller (D01 L457, D02 L601) / Jonathan V. Gould, Comptroller (D07 L474); Christopher
  Crawford "Special Counsel" (D01 L53, D02 L34) / "Acting Assisting Director" (D07 L33); "de minis" (D01
  L239, D02 L345) / "de minimis" (D07 L182).
- Effective dates and the calendar-quarter rule: D02 January 1, 2025 with the RCDRIA sentence (D02 L403);
  D07 April 3, 2026 with the same RCDRIA sentence (D07 L229-230).

### Every filing type D07 touches (instruction number, section, conditions, time periods)

| # | Section | Filing type | Existing eligibility named in preamble | D07 change | Conditions, thresholds, periods | Preamble | Text |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 5.3 | Definition | none | adds "Covered community bank or covered community savings association" | less than $30 billion total assets per Call Report; not an affiliate of a depository institution or foreign bank with $30 billion or more; well capitalized; not subject to a cease and desist order, consent order or formal written agreement requiring action to improve financial condition, "unless otherwise informed in writing by the OCC"; affiliate via control in Sec. 5.50(d)(4) | L64-97 | L277-292 |
| 3 | 5.13(a)(2)(ii) | Decisions: when an adverse comment extends or removes expedited review | "significant" not defined | adds a sentence | concern is significant "if the facts are previously unknown to the OCC and, if proven accurate, would support denying, or imposing a condition on the approval of, the filing" | L152-165 | L296-302 |
| 4 | 5.20(j) | Charter: full-service national bank or Federal savings association sponsored by a holding company | lead depository institution is an eligible bank or eligible savings association | adds covered community bank, covered community savings association | expedited review | L108 | L308 |
| 5 | 5.23(d)(4) | Conversion "from an eligible bank to a Federal savings association" | eligible bank | adds "or covered community bank" | expedited review | L108 | L313 |
| 6 | 5.24(h) | Conversion from an eligible savings association to a national bank | eligible savings association | adds "or covered community savings association" | expedited review | L108 | L318 |
| 7 | 5.26(e)(3) | Fiduciary powers | eligible bank or eligible savings association | adds both covered terms | expedited review | L108 | L323 |
| 8 | 5.30(f)(6) | Establishment or relocation of a branch (national bank) | eligible bank | adds "or covered community bank" | expedited review | L108 | L328 |
| 9 | 5.31(f)(1)(iii), (f)(2)(iii) | Branch establishment or relocation (Federal savings association) | eligible savings association | adds "or covered community savings association" | (f)(2)(iii): no application if public notice published and no opposing comment, or the comment is not relevant or needs no OCC action; (f)(1)(iii): expedited review when an application is required because a comment was filed or the branch is in the District of Columbia (fn 11 L116) | L112 | L333 |
| 10 | 5.33(j)(1)(iii)-(v) | Business combination: streamlined application, hence expedited review under 5.33(i) | options (i)-(iv) in fn 12 | adds (j)(1)(v) | acquirer is a covered community bank or covered community savings association and the transaction "would result in a national bank or Federal savings association with less than $30 billion in total assets" | L119-129 | L336-349 |
| 11 | 5.34(f)(2)(i), (f)(6) | National bank operating subsidiary: establish, acquire or new activity | well capitalized and well managed | adds "a covered community bank or is both" | (f)(2): after-the-fact notice instead of an application if structural and activity requirements are met | L141-142 | L355-359 |
| 12 | 5.35(f)(2)(ii)(A) | Bank service company investment or new activity (notice) | well capitalized and well managed | adds covered community bank or savings association | expedited review of the notice | L143 | L364 |
| 13 | 5.36(e)(3), (h)(1) | National bank non-controlling investment | certification of well capitalized and well managed | adds "a covered community bank or is both" | notice "no later than 10 days after making" the investment (both (e) and (h)(1)); otherwise application under 5.36(f) | L144 | L369-372 |
| 14 | 5.38(f)(2)(ii)(A) | Federal savings association operating subsidiary | well capitalized and well managed | adds "a covered community savings association or is both" | expedited review; section does not apply to associations not subject to 12 U.S.C. 1828(m) (fn 15 L148) | L145 | L377 |
| 15 | 5.40(c)(4) | Relocation of main office or home office | eligible bank or eligible savings association | adds both covered terms | expedited review | L113 | L382 |
| 16 | 5.45(g)(3) | Capital increase by a Federal savings association | eligible savings association | adds covered community savings association | expedited review | L113 | L387 |
| 17 | 5.46(i)(2) | Change in permanent capital of a national bank | eligible bank | paragraph revised and republished to add covered community bank | "deemed approved by the OCC 15 days after the date the OCC receives the application" unless removed or extended under Sec. 5.13(a)(2); capital decrease plan "for up to four consecutive quarters"; must keep status "before and after each decrease" | L113 | L390-396 |
| 18 | 5.47(f)(1)(i)(B)-(C), (f)(2)(i)(B)-(C) | Subordinated debt issued or prepaid by a national bank | eligible bank needs approval only if it "will not continue to be an eligible bank after the transaction", prior notice, or law | new (B) for covered community bank; old (B) becomes (C) | issue: approval if (1) not well capitalized after the transaction, (2) OCC previously notified, (3) required by law; prepay debt not in tier 2 capital: "only if" (1)-(3) or (4) prepayment "equal to or greater than one percent of the national bank's total capital, as defined in 12 CFR 3.2" | L113 | L400-434 |
| 19 | 5.55(e)(1)(i), (g)(1), (g)(2)(i) | Capital distributions by Federal savings associations | eligible savings association | adds covered community savings association; (e)(1)(i) restructured | application required if the association is (A) not eligible or covered, or (B) eligible or covered "but would not continue to be well capitalized following the distribution"; expedited review of applications under (g) | L136 | L438-452 |
| 20 | 5.56(b)(1)(ii) | Inclusion of subordinated debt securities or mandatorily redeemable preferred stock in tier 2 capital (Federal savings association) | eligible savings association | adds "or covered community savings association" | expedited review | L113 | L458 |
| 21 | 5.58(e)(3), (h)(1) | Federal savings association pass-through investments | well capitalized and well managed | adds "a covered community savings association or is both" | "substantively identical" to Sec. 5.36 (L144) | L144 | L463-467 |
| 22 | 5.59(h)(2)(ii)(A) | Federal savings association service corporation: establish, acquire or new activity | well capitalized and well managed | adds "a covered community savings association or is both" | expedited review if only preapproved activities in 12 CFR 5.59(f); not applicable to associations not subject to 12 U.S.C. 1828(m) (fn 16 L149) | L145 | L472 |

Instruction 1 (L271-274) only restates the authority citation. Review-period lengths are printed for only
one filing type in D07's text (Sec. 5.46, 15 days); the 10-day notice periods (Sec. 5.36) and the 45-day
figure (commenter, L126) are in the preamble only.

## Shared ground (navigation only)

### Entities that appear in more than one document, and where

- Issuers: OCC issues D01, D02, D07; FDIC issues D03, D04, D05; the Federal Reserve Board issues D06.
- OCC named in non-OCC documents: D03 fn 9 L164-165, fn 24 L337; D04 L163, fn 16 L166, fn 17 L171, L619
  ("the Comptroller"); D06 L60, fn 3 L65. Not named in D05.
- FDIC named in non-FDIC documents: D01 L97, L178, L390; D02 L97, L121, L241, L283, L529; D06 L60, fn 3 L65;
  D07 L76, L97, fn 10 L100.
- Federal Reserve named in non-Board documents: D01 L140 ("FRB Order"), fn 20 L157 ("the Board"); D02
  L200-201, fn 31 L214; D03 L137, L204, fn 24 L337, fn 65 L575, fn 76 L645, L663; D05 L54, L73, L77, L128,
  fn 31 L169. Not named in D04 or D07.
- Department of Justice / Attorney General: D01 fn 11 L113; D02 L124; D03 L69, L94, L273, L375, L384, L436.
- Consumer Financial Protection Bureau: D02 L161; D03 L155 (both commenter suggestions).
- Small Business Administration: D01 L251, L255; D02 L103-108, L362, L368-369, L373; D04 L360, fn 44 L364;
  D06 fn 19 L179; D07 L195, fn 21 L205. SBA Office of Advocacy only in D02.
- Government Accountability Office: D02 L426; D05 L102, fn 15 L106, fn 32 L170; D07 L259.
- NCUA and OFAC only in D06 (L60, L117). FinCEN only in D03 (L286, fn 51 L501). Basel Committee: D01 fn 14
  L127; D02 fn 19 L145. FFIEC only in D01 fn 11 L113.
- People: Christopher Crawford, Valerie Song, Elizabeth Small, Yoo Jin Na (D01 L53; D02 L34); Christopher
  Crawford again (D07 L33, different title); Michael J. Hsu (D01 L457; D02 L601); Jonathan V. Gould (D07
  L474); Benjamin Klein, Supervisory Counsel (D03 L29; D04 L48); Scott Leifer, Senior Review Examiner (D04
  L48; D05 L36); Jennifer Jones, Deputy Executive Secretary (D04 L42; D05 L30); Debra A. Decker, Executive
  Secretary (D04 L666; D05 L282); James P. Sheesley only D03 L670; Benjamin W. McDonough only D06 L32, L276.
  Similar names in different agencies: Elizabeth Small (OCC, D01 L53, D02 L34) and George Small (FDIC, D03 L29).
- Named commercial banks and firms occur only in D05 (L95, L102, L111, L127, L128, L175). Elsewhere the only
  bank names are a case citation, United States v. Philadelphia National Bank (D03 fn 40 L429), and Federal
  Reserve Banks (St. Louis, D03 L663; Chicago, D06 fn 6 L78).
- Credit unions: D02 fn 38 L283-284; D03 L93, L154, L197, L210, L291, fn 39 L423, fn 56 L534, L650.
- G-SIB: D01 L124, fn 14 L127, L339; D02 L142, fn 19 L145, L168-178, L217, L478; D03 L272 (commenter).
- Community bank concepts: D03 "traditional community banks" (L642); D07 "covered community bank" (L282) and
  the FDIC "community bank" definition from a 2012 study (L76, L97).
- "Non-bank" / "nonbank bank": D03 fn 76 L645; D05 fn 12 L98.
- Stablecoins: D05 Q29 L256; D06 Question 3 L125.

### Periods or series that more than one document covers, and where

- Publication sequence: D01 February 13, 2024; D02 September 25, 2024; D03 September 27, 2024; D04 July 18,
  2025; D05 July 21, 2025; D06 February 26, 2026; D07 March 4, 2026 (line 3-5 of each file).
- Comment deadlines: D01 April 15, 2024 (L40); D04 September 16, 2025 (L37); D05 September 19, 2025 (L25);
  D06 April 27, 2026 (L28). Effective dates: D02 January 1, 2025 (L32); D03 October 28, 2024 (L27); D07
  April 3, 2026 (L31). No document prints the length of its own comment or lead period in days.
- Other dates within the bundle's span: FDIC Proposed Statement April 19, 2024 (D03 L36); FDIC Board
  Briefings Resolution June 18, 2024 / June 20, 2024 (D03 L82, fn 5 L85); Thrivent Bank approval June 20, 2024
  (D05 L127); FIL-53-2024 August 9, 2024 (D04 fn 18 L178); FINDRS data August 18, 2024 (D02 fn 49 L372); D03
  dated September 17, 2024 (D03 L669); OCC reputation-risk release March 20, 2025 (D06 fn 3 L65); March 31,
  2025 baseline (D04 L280-281, L367; D05 L128); Thrivent opened June 1, 2025 (D05 L127); Board announcement
  June 23, 2025 (D06 fn 1 L63); D04 status date June 24, 2025 (D04 fn 40 L322); D04 and D05 both dated July
  15, 2025 (D04 L665; D05 L281); E.O. 14331 August 12, 2025 (D06 fn 10 L82); OCC News Release 2025-89
  September 18, 2025 (D07 fn 7 L85); NCUA September 25, 2025, FDIC October 7, 2025, 90 FR 48409 October 21,
  2025, 90 FR 48825 October 30, 2025 (D06 fn 3-4 L65-66); D07 proposal November 18, 2025 (D07 L53); FIDRS
  data February 18, 2026 (D07 fn 20 L204).
- OCC regulatory-analysis series (three editions): supervised institutions 1,057 / 1,040 / 997; small
  entities 661 / 636 / 609; UMRA figure $182 million / $183 million / $187 million; size dates December 31,
  2022 / 2023 / 2024 (D01 L252, L255, L271; D02 L369, L373, L388; D07 L201, L205, L213). OMB 1557-0014
  respondents 3,694 and burden 12,481.15 constant (D01 L240-241; D02 L346-347; D07 L183-184).
- Same as-of date, different populations: March 31, 2025 - 2,835 FDIC-supervised State nonmember banks or
  insured branches of foreign banks (D04 L281) and 23 industrial banks (D05 L128).
- Merger-application counts by year exist only in D01 fn 32 L257; D02 L369 refers to "the past five years"
  without figures.

### Documents that cite, amend or respond to another document in the bundle

- D02 finalises D01 and cites it: "89 FR 10010 (February 13, 2024)" (D02 fn 6 L56); same docket and RIN (D01
  L27-28; D02 L19-20).
- D07 amends the same part 5 and the same Sec. 5.33(j) that D02 reserved; D07 does not cite D01 or D02 (see
  "D02 vs D07").
- D03 cites OCC guidance (Comptroller's Licensing Manual: Business Combinations, D03 fn 9 L164-165), the same
  booklet D01 and D02 describe (D01 L69-73, fn 22 L170; D02 L51, fn 33 L234, fn 39 L292). D03 does not cite
  D01 or D02; D02 does not cite D03 or the FDIC Proposed Statement (it reports commenters urging coordination
  with the FDIC, D02 L121).
- D06 refers to OCC and FDIC reputation-risk actions and proposals (D06 L60, fn 3-4 L65-66), none of which is
  in the bundle. D01 and D02 list "reputation" among the eight OCC Risk Assessment System categories (D01
  fn 24 L179, L391; D02 fn 35 L242, L530). D06 says the Board's 1995 guidance listed "six risk channels"
  including reputation risk (D06 L73) and names five continuing channels (D06 L93).
- D04 proposes to align the FDIC "remote service unit" definition with OCC regulations (D04 L163, fn 16 L166).
- D05 fn 1 L45-47 says part 354 applies to merger transactions subject to 12 U.S.C. 1828(c), the statute D03
  interprets; D03 addresses non-bank and non-community-bank applicants (D03 L640-645; fn 4 L72).
- D03 fn 5 L85: the 270-day Board Briefings Resolution "also applies to outstanding deposit insurance
  applications" - the filing type D05 discusses (D05 L42, L153).
- D03 fn 26 L339: a merger that includes establishing or relocating branches is also subject to 12 U.S.C.
  1828(d), the provision D04 implements (D04 L67, fn 2 L70). D04's revised Sec. 303.7(a) keeps public notice
  for merger transactions (D04 L516).
- No bundle document is cited by D04, D05 or D06.

### Forecast/actual pairs, repeated/changed tables, same-period conflicts and scope relationships

Proposed versus final or later action:

- D01 proposal to D02 final: full diff in "D01 vs D02". Comment deadline (D01 L40) and comment count (D02 L59)
  sit in different documents. D01 estimate "38" (L252) vs D02 "78" (L369).
- D02 removal of expedited review and the streamlined application (D02 L109-110) vs D07's expansion of both
  (D07 L119, L349).
- D03 keeps merger public notice, comment and hearing processes (D03 L256, L263, L551) while D04 proposes to
  remove them for branch filings (D04 L132, L147, L526, L584).
- Proposals with no final edition in the bundle: D04, D06. Request for information only: D05. Final editions
  with no proposal in the bundle: D03, D07.

Repeated thresholds (every location):

- "$50 billion": D01 L322, L453; D02 L153 (six), L154, L461, L593; D03 L88, L128, fn 10 L171, L247 (two),
  L249, L551. Not in D04-D07.
- "$100 billion": D02 L153 (commenter); D03 L88, L137 (two), L272 (seven), L273, L278, L279, L280, L580.
  Distinct from "$100 million" / "$100,000,000" in regulatory analyses: D01 L271; D02 L388, L419; D07 L213,
  L235, L252.
- "$30 billion": D07 only (L28, L53, L67, L74, L76, L78, L90, L119, L284, L349).
- "$10 billion": D02 L217; D03 L179, L282; D05 L128 (industrial-bank size bands, with "$1 billion").
- "$850 million": D01 L251, L255; D02 L362, L373; D04 L360, L364; D06 L179; D07 L195, L205. "$47 million"
  (trust companies): D01, D02, D07 only, same lines.
- Significance tests "5 percent" of salaries and benefits / "2.5 percent" of non-interest expense: D01 L265;
  D02 L382; D04 L360, L386, L392; D07 L201, L209. "2.5 percent" also appears as an unrelated MRA share in
  D06 L145.
- "50 percent" and "10 percent" streamlined-application tests: D01 fn 9 L100; D02 fn 12 L90-91; D07 fn 12
  L122-123. "50%" indicator: D01 L329; D02 L468 (L155-156 "50 percent"). "10 percent" deposit cap: D03 L392,
  L406, L442. "15 percent": D04 L112 (standard-processing share) and D05 fn 20 L124 (commercial-firm test).
- Rating cut-offs: OCC indicators 1 or 2 vs 3 or worse (D01 L324-325, L337-338; D02 L463-464, L476-477);
  FDIC eligible depository institution composite 1 or 2 and compliance 1 or 2 (D04 L92, L222); FDIC proposed
  relocation test "composite rating of 3 or better" (D04 L244, L581). CRA "Outstanding or Satisfactory" (D01
  L323; D02 L462; D07 L77 as a commenter request); "satisfactory or better" (D04 L92, L140, L222); "less than
  Satisfactory" (D02 L179-180; D03 L251, L255, L530).

Repeated time periods (every location):

- 30 days / 30-day: D01 L59, L207, L434; D02 L41, L83, L296, L312, L354, L574; D03 L256; D07 L191.
- 60 days / 60-day: D02 L76 (standard review target), L306 (commenter), L412 (Congressional Review Act); D03
  L256 (commenter); D04 L450 (PRA); D07 L246 (Congressional Review Act).
- 45 days / 45-day: D02 L76; D07 L126.
- 15th day / 15 days / 15-day: D01 L82, L234; D02 L65, L76, L78, L340, L379; D04 fn 39 L320, fn 51 L401
  (branch comment period); D07 L396 (Sec. 5.46).
- 270 days: D03 L82 only.
- three-year period (enforcement actions): D01 L124, L341; D02 L142, L480. three years (branch plans): D02
  L274; D03 L265-266, L544, L546. Other "three-year": D05 L116 (moratorium); D04 L419 (PRA extension).
- Deemed-approved clocks: OCC business combinations 15th day after the comment period closes (D01 L82; D02
  L65); FDIC branches 21st day / 5th day, proposed third business day (D04 L99, L214, L229, L579-581); OCC
  permanent capital 15 days after receipt (D07 L396); FDIC mergers "does not constitute an automatic or
  default approval" (D03 L181).
- "first day of a calendar quarter" (RCDRIA, 12 U.S.C. 4802): D01 L282; D02 L403; D04 L465; D06 L221; D07 L229.
- "100 words" (Providing Accountability Through Transparency Act): D04 L477; D06 L232.

Same statutory factor or provision described differently:

- BMA factor on money laundering: "effectiveness of any insured depository institution involved in
  combatting money laundering activities, including in overseas branches" (D01 L59; D02 L41); "effectiveness
  of the IDIs involved in the merger transaction in combatting money laundering" (D03 L325) and "including in
  overseas branches" (D03 L613); "the money laundering record of insured depository institutions involved in
  the merger transaction" (D05 fn 30 L157).
- BMA stability factor: "risk to the stability of the United States banking or financial system" (D01 L59,
  L347; D02 L41, L488; D03 L325; D05 fn 30 L157); list lengths differ - seven OCC factors (D01 L348-357; D02
  L489-495) vs five FDIC items (D03 L578-579).
- Public-notice citation: BMA 30-day notice cited to 12 U.S.C. 1828(c)(4) (D01 fn 3 L64; D02 fn 3 L46) and to
  12 U.S.C. 1828(c)(3) (D02 fn 44 L316; D03 fn 18 L321, L366; D04 fn 11 L122); D03 uses 1828(c)(4) for the
  Attorney General report (D03 fn 19 L322, L375).
- "Convenience and needs of the community to be served" as a BMA factor (D01 L59; D02 L41; D03 L79, L325,
  L522; D05 fn 30 L157; D07 L91, L126) and as a section 6 FDI Act factor (D04 L77; D05 fn 29 L156, L193).
- Section 6 FDI Act seven factors: D04 L73-77 (and L630-631); D05 fn 29 L156, L188-194 (last factor "purposes
  of the FDI Act" in D04 L77 and D05 L156; "purposes of this chapter" in D05 L194).
- "Eligible depository institution": OCC term defined in 12 CFR 5.3, not spelled out in the bundle (D01 L330;
  D02 L469; D07 fn 13 L132 says it requires being well capitalized); FDIC term in 12 CFR 303.2(r), five
  criteria spelled out (D04 L92, L222-223).
- Expedited vocabulary: OCC "expedited review" (D01, D02, D07); FDIC "expedited processing" (D03 L179-181;
  D04 throughout). Removal authority: 12 CFR 5.13(a)(2) (OCC) and 12 CFR 303.11(c)(2) (FDIC; cited D03
  L180-181, four reasons spelled out D04 L237).
- UFIRS name: "Uniform Financial Institution Ratings System" (D01 L116, L324; D02 L135, L463); "Uniform
  Financial Institution Rating System" (D03 fn 45 L459); "Uniform Financial Institutions Rating System" (D04
  L92, L581).
- FDIC standard conditions: "Sec. 303.2(bb)" (D03 L383) vs "Sec. 303.2(dd)" (D04 L636).
- Providing Accountability Through Transparency Act cite: "12 U.S.C. 553(b)(4)" (D04 fn 59 L480) vs "5
  U.S.C. 553(b)(4)" (D06 fn 26 L234). Section 722 statute: "Gramm-Leah-Bliley" (D04 L454) vs
  "Gramm-Leach-Bliley" (D06 L202).
- Dodd-Frank Act: D02 L169, fn 24 L174 (liability cap); D03 L565-570 (section 604), fn 65 L575 (section 165);
  D05 L116, fn 20 L123-124 (section 603(a)), fn 26 L148 (section 38A).
- Change in Bank Control Act, 12 U.S.C. 1817(j): D04 L118, fn 12 L123; D05 fn 1 L46-47, L153, fn 30 L157,
  L196, L200, L232; D06 L117, L273; D07 L67, fn 6 L70; in the part 5 authority citation D01 L302, D02 L439,
  D07 L274.
- 12 U.S.C. 1831o prompt corrective action / section 38: D01 fn 23 L178, L390; D02 fn 34 L241, L529; D04
  L77, L86, L571; D07 L41 (12 CFR part 6). Section 38A (12 U.S.C. 1831o-1): D05 L146-150.
- 12 U.S.C. 1831u / section 44 interstate: D02 fn 23 L173; D03 L633-637, L657; D04 fn 22 L233.
- CRA 12 U.S.C. 2903: D02 fn 26 L183 (2903(a)(2)); D03 fn 53 L525, fn 55 L533 (2902(3)(E) and 2903(a)(2));
  D04 fn 3 L80 (2903(a)), fn 15 L143 (2902(3)(C) through (D)).
- 12 U.S.C. 1828(c)(1)(C) (transfers to non-insured institutions): D02 fn 38 L283; D03 fn 27 L346.
- 12 U.S.C. 1828(c)(13) deposit cap: D02 fn 23 L173; D03 fn 37 L409, fn 42-43 L445-446.
- Bank Merger Act named in every document: D01 L59; D02 L41; D03 L25, L316; D04 L118; D05 L153, L196, L232;
  D06 L117, L273 (and 12 U.S.C. 1828(c) in the part 262 authority, L254); D07 L91, L126-128.

Repeated cross-references:

- OCC Corporate Decision #2012-05 (April 2012): D01 fn 16 L134; D02 fn 27 L194. OCC Conditional Approval
  #1298 (November 2022): D01 L134, L151; D02 L194, L207. FRB Order No. 2012-2: D01 L140 (undated); D02 L200
  (February 14, 2012). FRB Order No. 2021-04 (May 14, 2021): D01 L140; D02 L201.
- Comptroller's Licensing Manual, "Business Combinations": D01 L69-73, L131, fn 22 L170; D02 L51, L123, L187,
  fn 33 L234, L289, fn 39 L292; D03 fn 9 L164-165. Comptroller's Handbook "Bank Supervision Process": D01
  fn 24 L179; D02 fn 35 L242; D07 fn 8 L86.
- Bank Merger Competitive Review--Introduction and Overview (1995): D01 fn 11 L113; D02 L121.
- Interagency Bank Merger Act Application / Form: D01 L96-97; D02 L87, L95-97, L288, L380; D03 L663.
- FDIC Applications Procedures Manual: D03 fn 4 L72, fn 11 L185, L205, L292-294, fn 28 L362, L660-662; D04
  L258, fn 25 L261. FDIC Delegations of Authority, No. 086825 (October 20, 2020): D03 fn 35 L387; D04 fn 26 L262.
- Uniform Interagency Consumer Compliance Rating System: D01 L116, L325; D02 L135, L464; D03 L483, fn 58 L541.
- Branch closing policy statement: D03 L544, fn 60 L547, L659; D04 L544.
- Matters requiring attention: D01 L182, L396; D02 L245, L535; D06 L145.
- 12 CFR 303.10 (hearings): D03 L249, fn 33 L372; D04 L146-147, L523-526. 12 CFR 303.2(l) CRA protest: D03
  fn 31 L370; D04 L635.
- Regulatory boilerplate: PRA 44 U.S.C. 3501 (D01 L231; D02 L337; D03 L303; D04 L422; D06 L169; D07 L174);
  RFA 5 U.S.C. 601 (D01 L251; D02 L365; D04 L363; D06 L178; D07 L198); UMRA (D01 L270; D02 L387; D07 L213);
  Congressional Review Act (D02 L410; D07 L243); E.O. 12866 and 14192 (D04 L488; D07 L233-241); plain
  language (D04 L452; D06 L200).

Counts of comments, by document: 34 (D02 L59); 23 (D03 L43); "seven comments per year" on branch applications
(D04 L131); "eight responsive comments" plus one other (D07 L53, fn 5 L57). D01, D05, D06 report none.

Narrative passages that repeat figures found elsewhere in the same document: D03 preamble thresholds (L88,
L128, L137, L249, L278) repeat SOP L551 and L580 with different wording; D04 L281 repeats L110-111; D04 L399
and fn 51 repeat L316 and fn 39; D02 L340 and L379 repeat L65 and L76; D06 L183-184, L195, L238 repeat L26;
D07 L67 repeats the definition at L282-292.

## Coverage statement

| File | Lines | Read in full (sequential) | Searched only |
| --- | --- | --- | --- |
| text/D01.txt | 1-462 | 1-462 (one pass) | none |
| text/D02.txt | 1-605 | 1-260, 261-440, 441-605 | none |
| text/D03.txt | 1-674 | 1-149, 150-298, 299-548, 549-674 | none |
| text/D04.txt | 1-670 | 1-200, 200-379, 379-598, 598-670 | none |
| text/D05.txt | 1-286 | 1-286 (one pass) | none |
| text/D06.txt | 1-280 | 1-280 (one pass) | none |
| text/D07.txt | 1-478 | 1-478 (one pass) | none |

- Every line of every text file was read. Whole-bundle pattern searches were run afterwards only to gather
  every location of repeated items (dollar thresholds; day, year and percent figures; statute and CFR
  citations; decision and control numbers; personal and institution names; rating-system names; "reputation",
  "stablecoin", "credit union"); each hit lies inside a range that was read.
- `docs/` originals were consulted by targeted search only (extraction spot-checks listed under Bundle), not
  read end to end; they are the same text at a 2-line offset.
- Method limit: the D01 / D02 comparison was made by reading both texts, not with a diff tool. Word-level
  changes are recorded as found; a row marked "identical" was checked by eye and could still hide a
  punctuation-level difference.
- Counts labelled "mapper tally" or "mapper check" are my own counts of printed items, not figures the
  documents state.

## Gaps

- Unread text: none.
- Missing source material (not in the bundle, so not checkable here): the action that returned Sec.
  5.33(d)(3), (i), (j) to 12 CFR part 5 between D02 and D07; D07's proposal (90 FR 51577); the FDIC Proposed
  Statement (89 FR 29222) and Superseded Statement, so D03's "retains without change" statements cannot be
  compared; the text of 12 CFR 5.3 "eligible bank" / "eligible depository institution"; the OCC Annual Reports
  behind D01 fn 32 and D02 fn 11; final rules for D04 and D06; the OCC and FDIC reputation-risk proposals
  cited in D06 fn 4.
- Unresolved inside the documents: D03 June 18 vs June 20, 2024 resolution date (L82, L85); D03 preamble L282
  revision not found in the SOP text; D03 "note 41" and "footnote 28" cross-references; D05 23 vs 24
  industrial banks (L128, L162); 12 U.S.C. 1828(c)(3) vs (c)(4) for the 30-day notice (D01 L64; D02 L46, L316);
  D02 L154 "$50 billion or more" beside indicator text "less than $50 billion" (L461).
- Visual material: none in any document.
