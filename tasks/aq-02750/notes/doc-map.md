# aq-02750 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Locator convention used below: `Lnnn` = line number in `text/Dnn.txt` (one line = one source
paragraph or wrapped fragment; the same line in `docs/` is `L - 2` because of the two header lines),
plus the Federal Register page marker `[[Page N]]` and the nearest heading. Character offsets were
not computed (no script tool in the mapping pass). Snippets are verbatim; the sources write quotation
marks as two backticks and two apostrophes, and footnote calls as `\N\`.

## Bundle

- What it is: seven Federal Register plain-text documents in two groups. D01-D03 are immigration
  rulemakings on mandatory bars in fear screenings and the 2020 "Security Bars and Processing" rule
  (May 2024 DHS proposal, December 2024 DOJ/EOIR interim final rule, December 2025 DHS/DOJ partial
  withdrawal and correction). D04-D07 are HHS/CDC texts from May-August 2026 (one 42 CFR part 71
  interim final rule and three orders under PHS Act sections 362 and 365).
- Documents: 7; ids D01-D07 from `text/manifest.json`. `notes/intake.json` numbers them 1-7 in the
  same order (Doc 1 = D01 ... Doc 7 = D07).
- Gaps: none. D01-D03 were read in full by the mapper (see each Coverage line); D04-D07 were read in
  full by the caller (2026-10-10), entries below.
- Extraction spot-checks (D01-D03, against `docs/`): page markers D01 `[[Page 41347]]`-`[[Page 41361]]`
  all 15 present (header "Pages 41347-41361"); D02 `[[Page 105393]]`-`[[Page 105403]]` 11 markers,
  first page 105392 unmarked (header "Pages 105392-105403"); D03 `[[Page 61035]]`-`[[Page 61049]]`
  all 15 present. Footnote check: D01 fn 5 "87 FR 79989 (Dec. 28, 2022)" at docs L139 = text L141;
  D03 fn 19 "withdrawal of the parts of amendatory instructions 3 and 11" at docs L359 = text L361.
  Table check: D02 row "the Service............................... DHS." at docs L346/L391 =
  text L348/L393. No charts or images (plain text).
- Provenance: `notes/intake.json` schema 1, every document `incomplete: false`, `gap_characters: 0`,
  `matches_capture: true`.
- Reuse binding (source sha256 = manifest sha256):
  - D01 `c949459df2005524e4839539486ffada45e416c2160cdbf90f77f2898b422237` (117,768 chars)
  - D02 `d8c045ecd93f7c09f518531e2a47bb45dd2e4941f72883d75854f59ccd49866a` (84,321 chars)
  - D03 `3606d26a7bd836a4804471210594a8868ca144fe535e29630cc34ee6333e2772` (116,775 chars)
  - D04 `0bef6474cb0e598690c2c8bd035ddf38ff71d77cca7be2bf130ad30bccd019b4` (44,162 chars)
  - D05 `a3fadc9b81a16aa0a502b51e29265c9185686fac8731116d1df46bcb98cec9e9` (41,644 chars)
  - D06 `68718f35704a268da3150b470ea4c62a680bd7b0a9cc9b3b71c7abf3520a3acd` (45,155 chars)
  - D07 `3eb23cf1e7d08e0b8263d08f7d9ea99e058bdeaf6d272dd06df865340584e90d` (41,005 chars)

## D01 - Application of Certain Mandatory Bars in Fear Screenings (DHS NPRM)

- Source: `docs/fr_2024_10390.txt` -> `text/D01.txt`, 538 lines; FR pages 41347-41361 (15 pages).
- Written or submitted by: Department of Homeland Security, U.S. Citizenship and Immigration Services
  (USCIS). Signed "Alejandro N. Mayorkas, Secretary, U.S. Department of Homeland Security" (L534-535).
  DHS alone; DOJ is mentioned, not a co-issuer.
- Type, date, edition: Notice of proposed rulemaking (NPRM). Federal Register Vol. 89, No. 93,
  Monday, May 13, 2024 (L3-7). FR Doc 2024-10390, "Filed 5-9-24; 4:15 pm" (L536). 8 CFR Part 208;
  DHS Docket No. USCIS-2024-0005; RIN 1615-AC91 (L23-26). No "Dated:" line.
- Period covered: statistics by federal fiscal year, FY 2020-FY 2023 and "FY 2024 through April 23,
  2024" (L181-197); data-as-of dates in fn 11-18. The document does not define the fiscal year.
- Entities and aliases (as defined in the text): USCIS; DHS / "the Department"; AOs (asylum
  officers); SAOs (used L420, not expanded); DOJ; "DHS and DOJ" / "the Departments"; EOIR (used from
  L106, never formally defined; fn 25 L238 "Exec. Off. For Immigration Rev."); ICE OPLA; ICE ERO; OHSS;
  FERM (Family Expedited Removal Management, L229); CLP rule =
  "Circumvention of Lawful Pathways rule"; AMI (asylum merits interview); INA; HSA; CAT; FARRA;
  "Global Asylum Rule"; "Global Asylum NPRM"; "Asylum Processing IFR"; "Asylum Processing NPRM";
  "Lawful Pathways NPRM"; "Third-Country-Transit Bar IFR"; "Security Bars" or "Asylum Eligibility and
  Public Health" rule (two names for one rule, L137); "security bar" (L137); "mandatory bars" (L81);
  "firm resettlement bar" (L315); "section 240 removal proceedings" (L106).
- People: Samantha Deshommes, Chief, Regulatory Coordination Division, tel. (240) 721-3000 (L41);
  Daniel Delgado, Director for Immigration Policy, tel. (202) 447-3459 (L43-44); Alejandro N. Mayorkas
  (signer; also memo author, fn 19 L209); "then- Acting Secretary Chad Wolf" (fn 3, L134).

### D01 dates (what each is)

- Publication: Monday, May 13, 2024 (L3, L5, L17).
- Comment deadline: "on or before June 12, 2024" ... "prior to midnight eastern time at the end of
  that day" (L38). Stated length: "a 30-day comment period" (L398, L408).
- No effective date (proposal).
- Treaties/statutes: Refugee Protocol "January 31, 1967"; Refugee Convention "July 28, 1951" (L63-68);
  CAT "Dec. 10, 1984 ... (entered into force for United States Nov. 20, 1994)" (L71); Refugee Act of
  1980 (L69); IIRIRA 1996 (L93); FARRA 1998 (L71).
- Earlier rules cited, section II.D "Past Regulatory Actions on This Topic" (L125-158):
  - "Asylum Procedures, 65 FR 76121, 76129 (Dec. 6, 2000)" - former INS rule "in 2000" (L128).
  - Global Asylum Rule: "85 FR 80274, 80391, 80393, 80399 (Dec. 11, 2020)"; Global Asylum NPRM
    "85 FR. 36264, 36272 (June 15, 2020)" (L131).
  - Injunction: "On January 8, 2021, before the rule became effective, the U.S. District Court for the
    Northern District of California preliminarily enjoined" - Pangea Legal Servs. v. DHS, 512 F. Supp.
    3d 966, 977 (N.D. Cal. 2021) (L132; fn 3 L134 gives the ground: DHS official "was not properly
    designated as Acting Secretary").
  - Security Bars rule: "On December 23, 2020, DHS and DOJ jointly published a final rule" ... "The rule
    was scheduled to take effect on January 22, 2021, but its effective date has been delayed multiple
    times, now until December 31, 2024." (L137). fn 4 "85 FR 84160 (Dec. 23, 2020)" (L139); fn 6
    "85 FR 84160, 84190" (L147-148).
  - Delay rules, fn 5 (L140-141), four listed in this order: "87 FR 79989 (Dec. 28, 2022)"; "86 FR 73615
    (Dec. 28, 2021)"; "86 FR 15069 (Mar. 22, 2021)"; "86 FR 6847 (Jan. 25, 2021)". No delayed-to date
    is given for any individual delay rule; only the current "December 31, 2024".
  - Asylum Processing IFR: "87 FR 18078, 18219, 18221-22 (Mar. 29, 2022)" - "In 2022" (L151); pin cites
    87 FR 18093, 18134, 18092-94, 18134-36 (L151, fn 7 L154). Asylum Processing NPRM "86 FR at 46914-15"
    (L264, no date).
  - CLP rule: "In May 2023" ... "88 FR 31314 (May 16, 2023)"; Lawful Pathways NPRM "88 FR 11704
    (Feb. 23, 2023)" (L157-158). "in constant effect since May 11, 2023" (L284).
  - Third-Country-Transit Bar IFR: "84 FR 33829 (July 16, 2019)" (L283). Applied "consistently only
    between approximately September 9, 2019, and March 26, 2020--just over six months--after an initial
    two months of abrupt starts and stops" (L284).
  - fn 35 litigation chronology (L287-290): "preliminarily enjoined nationwide on July 24, 2019, six
    days after it went into effect"; stay denied "Aug. 1, 2019"; "halted nationwide for twenty-three
    days, on August 16, the Ninth Circuit then granted a stay"; "Twenty-six days later, on September 9,
    the district court restored the nationwide scope"; "Two days later the Supreme Court stayed the
    preliminary injunction"; "until it was vacated on June 30, 2020"; "the first Title 42 public health
    Order issued on March 26, 2020".
  - CAT regulations: "64 FR 8478 (Feb. 19, 1999), as corrected by 64 FR 13881 (Mar. 23, 1999)" (L72);
    fn 40 (L362-363): reasonable fear process "promulgated in 1999", "64 FR 8478 (1999) (interim rule)",
    "8 CFR 241.8 (1998)".
- Other dated sources: Mayorkas memo "(Sept. 30, 2021)", "last visited Feb. 9, 2024" (fn 19 L209);
  RAIO training "(Feb. 20, 2023)" (fn 21 L218); EOIR pending-cases sheet "(Oct. 12, 2023)", "last
  visited Apr. 28, 2024" (fn 25 L238); OHSS monthly tables "last updated Apr. 5, 2024" (fn 44 L405);
  DHS Directive 023-01 "(Oct. 31, 2014)", Instruction Manual "(Nov. 6, 2014)" (fn 47-48 L464-465).

### D01 numbers (units; repeats)

- Positive credible fear of persecution determinations with a potential bar flagged "(without counting
  firm resettlement)", L181, [[Page 41351]], section III. Prose only, no table. Counts exact;
  percentages printed at mixed precision:

  | Period | Flagged | Total positive | Printed % | Data as of |
  | --- | --- | --- | --- | --- |
  | FY 2024 through April 23, 2024 | 733 | 29,751 | 2.5% | Apr. 25, 2024 (fn 11) |
  | FY 2023 | 1,497 | 50,117 | 3% | Feb. 10, 2024 (fn 12) |
  | FY 2022 | 626 | 24,282 | 2.6% | Id. (fn 13) |
  | FY 2021 | 479 | 24,512 | 2% | Id. (fn 14) |
  | FY 2020 | 346 | 8,887 | 4% | Id. (fn 14) |

- Positive reasonable fear of persecution determinations with a potential bar to withholding flagged,
  L190-197, [[Page 41351]]-[[Page 41352]] (no "without counting firm resettlement" qualifier here):

  | Period | Flagged | Total positive | Printed % | Data as of |
  | --- | --- | --- | --- | --- |
  | FY 2024 through April 23, 2024 | 143 | 1,430 | 10% | Apr. 25, 2024 (fn 15) |
  | FY 2023 | 309 | 1,534 | 20% | Feb. 10, 2024 (fn 16) |
  | FY 2022 | 236 | 1,127 | 21% | Id. (fn 17) |
  | FY 2021 | 80 | 541 | 15% | Id. (fn 18) |
  | FY 2020 | 56 | 394 | 14% | Id. (fn 18) |

  Source system both tables: "Asylum Global Case Management System". Wording shifts within L181: FY
  2020-2021 say "positive credible fear determinations", FY 2022-2024 say "positive credible fear of
  persecution determinations".
- Repeat inside D01: "in FY 2023, only 1,497 (or about 3%) of all positive credible fear decisions were
  flagged by the AO for a potential bar" (L419, section V.B). No other document in the bundle prints
  any of these counts (grep of D01-D07).
- Immigration court backlog: "exceeded 2,400,000 cases pending cases at the end of FY 2023" (L231).
- Detained-case timing: "from February 2023 through February 2024, the median monthly EOIR processing
  time for a detained case ranged from 44 to 69 days" (L241); fn 26: "OHSS analysis of EOIR data as of
  April 1st, 2024. EOIR data up-to-date as of February 29, 2024" (L244).
- Removals: "From May 12, 2023 to March 31, 2024, DHS has removed or returned over 660,000 individuals"
  (L400); fn 42 "UIP data as of April 2, 2024". "exceed removals and returns in every full fiscal year
  since 2011" (L400); "over the last three years accounts for a majority of southwest border
  encounters" (L400).
- Examples with thresholds: "convicted of murder and sentenced to ten or more years in prison" (L295);
  aggravated felony "sentenced to a term of imprisonment of more than five years. See INA
  241(b)(3)(B)(iv)" (L358).
- "OPLA personnel dedicate dozens of hours in cases pending before the immigration courts" (fn 24 L226).
- UMRA threshold "$100 million or more in any one year, adjusted for inflation" (L428); also in D02
  L261 and D03 L421, L427.
- Not present in D01: wage figures, quantified cost or burden estimates, population estimates in
  dollars or hours. Benefits are "a modest, unquantified reduction in strains" (L419). Paperwork
  Reduction Act: "does not propose new, or revisions to existing" collections (L478).

### D01 lists and exact membership

- Statutory bars list, section II.B.1 (L81-89, [[Page 41348]]): five bars to asylum at INA
  208(b)(2)(A)(i)-(v) that are also bars to withholding at 241(b)(3)(B): (1) persecution of others;
  (2) "particularly serious crime"; (3) "serious nonpolitical crime outside the United States";
  (4) "danger to the security of the United States"; (5) "certain terrorism-related provisions".
  "A sixth statutory bar to eligibility for asylum, which does not bar eligibility for statutory
  withholding" = firm resettlement, INA 208(b)(2)(A)(vi) (L87-88). "additionally" bars to withholding
  for admitted noncitizens deportable under INA 237(a)(4)(D): "genocide, torture, extrajudicial
  killing, or Nazi persecution" (L88-89). "There are no bars to deferral of removal" under CAT (L81).
- Bars the proposal covers: asylum bars "section 208(b)(2)(A)(i) through (v)" and withholding bars
  "section 241(b)(3)(B)" (L303-304, L315, L502).
- Not covered / left as is (section IV.A, L315-338):
  - firm resettlement, 208(b)(2)(A)(vi) (L315; reason: burden-shifting framework, Matter of A-G-G-);
  - "the bars to applying for asylum found at section 208(a)(2)" (L315); fn 30 (L267): safe-third-
    country bar 208(a)(2)(A) "has long applied" via 8 CFR 208.30(e)(6); "not proposing to apply other
    INA 208(a)(2)(A) bars, see, e.g., INA 208(a)(2)(C) (successive asylum application)";
  - CAT: "does not propose to change how DHS considers bars to protection under the CAT" (L321);
  - reasonable fear of torture: "does not propose to allow for the application of the mandatory bars
    to withholding of removal to reasonable fear of torture determinations under 8 CFR 208.31(c)" (L338);
  - stowaway special rules unchanged (L321);
  - 8 CFR 208.30(e)(4) "novel or unique issues" not disturbed (L254);
  - immigration judge review of adverse determinations unaffected (fn 10 L178, fn 27 L251).
- CFR sections proposed to be amended: "8 CFR 208.30, 208.31, and 208.33" (L303; repeated L327-328).
  Only chapter I (DHS) sections; no 8 CFR part 1003 / 1208 (EOIR) text.
- Amendatory instructions, 4 numbered (L486-532, [[Page 41360]]-[[Page 41361]]):
  1. Authority citation for part 208 "continues to read" (L487-489).
  2. Sec. 208.30: revise "the first sentence of paragraph (e)(2) and paragraph (e)(5)" (L492-508).
     New (e)(5)(i) keeps Notice to Appear/retained jurisdiction for bars in "section 208(a)(2) and
     (b)(2)(A)(vi)"; (e)(5)(ii) "the asylum officer may consider the applicability of such bar(s)";
     (ii)(A) negative finding standard; (ii)(B) positive path; (iii) stowaways.
  3. Sec. 208.31: revise "paragraphs (c) and (g)" (L510-519). fn 36 (L306): the (g) change is "an
     unrelated non-substantive change" replacing the last sentence and (g)(1)-(2) with a pointer to
     8 CFR 1208.31(g).
  4. Sec. 208.33: revise "paragraphs (b)(2)(i) through (iii)" (L522-532).
- "This rule has three anticipated impacts" (L207): First (L207), Second (L214), Third (L223); a
  further "Finally" paragraph on detention follows (L241).
- Four reasons the Department "refined its prior position" (L279): First (L280), Second (L283),
  Third (L293), Fourth (L294).
- NEPA: categorical exclusion "A3(d)" (L474); three conditions (L468).

### D01 definitions, standards, conditions

- Credible fear of persecution: statutory "significant possibility" definition (L108-109); fn 2 (L112):
  the statute sets the standard only for asylum; the withholding/CAT screening standard is regulatory.
- Reasonable fear: "reasonable possibility" (L120). Withholding/deferral: "more likely than not" (L80).
- Proposed standards by track: Sec. 208.30 credible fear - "a significant possibility that the
  noncitizen would be able to prove by a preponderance of the evidence that the given bar would not
  apply" (L330); Sec. 208.33 CLP track - "a reasonable possibility the bar does not apply" (L336);
  Sec. 208.31 reasonable fear - "a reasonable possibility that no mandatory bar applies" (L337).
- Permissive, not mandatory: "would allow, but not require" (L326); "with supervisory review of any
  decision" (L254); contrast with Global Asylum Rule in fn 28 (L257-260).
- Condition in proposed 208.30(e)(5)(ii): applies to an alien "who is unable to establish a credible
  fear of torture" (L502).
- Conditions that govern the L181-197 statistics:
  - "flagged" is not "applied": fn 11 (L184) "USCIS does not currently apply bars in credible or
    reasonable fear screenings but notes the possible applicability of the bar, and thereby notifies
    OPLA, if the case is referred to EOIR for adjudication."
  - Credible fear counts exclude firm resettlement flags ("without counting firm resettlement", each
    year in L181); the reasonable fear sentences (L190-197) carry no such qualifier.
  - Scope of effect: "limited to cases that would have otherwise been found to have a positive credible
    or reasonable fear of persecution" (L181); positive fear-of-torture cases "would not be impacted"
    (L206).
  - "The Department expects that AOs would choose to apply a mandatory bar to an even smaller subset of
    these flagged cases" (L419).
- Severability (section IV.E, L388-392).

### D01 hedged claims (hedge -> what it attaches to)

- "The population to which this rule will apply is likely to be relatively small" (L181, L419) - size
  of affected population.
- "this rule may provide efficiencies for ICE ... and may reduce referrals to EOIR" (L223).
- "the rule may reduce or eliminate the need for detention" (L241); "would potentially conserve ICE
  ERO resources" (L241).
- "DHS believes the rule would likely result in AOs using discretion" (L247).
- "DHS may address such bars through other rulemaking" (L315) - firm resettlement / 208(a)(2) bars.
- fn 37 (L307): "if DHS finalizes this NPRM, DOJ may wish to clarify the procedures immigration judges
  will follow in reviewing DHS screenings."
- "Should the provisions of the Asylum Eligibility and Public Health rule go into effect as currently
  scheduled on December 31, 2024, it would have implications" (L382) - conditional on that rule
  taking effect.
- "The public safety of the United States may be enhanced"; "may create disincentives" (L419).
- Firm statements near hedges: "This rule has three anticipated impacts" (L207); OMB "has designated
  this rule as a significant regulatory action" though "not been designated significant under section
  3(f)(1)" (L412).

### D01 public health / Title 42 / 2020 references

- L137 (II.D, [[Page 41350]]): Security Bars rule "to clarify that the Departments may consider
  emergency public health concerns based on communicable disease (not limited to COVID-19)".
- L144: "physically present in a country in which a communicable disease was prevalent or epidemic,
  and the Secretary of Homeland Security and the Attorney General determined that the physical
  presence in the United States of noncitizens coming from that country would cause a danger to the
  public health"; credible fear effect: negative determination, then screened "only for deferral of
  removal" at "clear probability (more likely than not standard)"; that portion "was rooted in the
  provision of the Global Asylum Rule that never went into effect".
- L278 ([[Page 41354]]): "following the end of the Title 42 public health Order".
- L290 (fn 35): "the first Title 42 public health Order issued on March 26, 2020, which limited the
  processing of certain noncitizens under Title 8."
- L381-382 (section IV.D "Security Bar to Asylum and Withholding of Removal", [[Page 41358]]).
- L412: Executive Order boilerplate "public health, and safety effects".
- No occurrence of "Ebola", "CDC", "HHS", "Health and Human Services", "pandemic" or "42 U.S.C. 265".

### D01 as-printed inconsistencies (both locations)

- Firm resettlement paragraph: fn 8 (L167) and fn 20 (L210) say "the ``firm resettlement'' bar at INA
  208(b)(2)(A)(iv)"; body text L87-88 and L315 place it at 208(b)(2)(A)(vi), and (iv) is the security
  bar at L85 and L381.
- Cross-reference: L264 "As discussed above in section II.C of this preamble, the Global Asylum Rule";
  the discussion is under heading II.D (L125-131); L381 and L399 say "Section II.D".
- L283 "See, e.g., 84 FR at 18092, 18135-36" for the Asylum Processing IFR, cited elsewhere as 87 FR.
- fn 38 (L318) "See supra, n.31"; fn 30 (L267) is the note on 208(a)(2) bars.
- U.S.C. parallels for INA 241(b)(3)(B) printed as "1231(b)(2)(B)(i)" etc. at L83-86 and L299;
  "1231(b)(3)(B)" at L82, L89.
- L63 "19 552U.S.T. 6223"; L131 "85 FR. 36264"; L231 "cases pending cases".

- Coverage: FULL. Ledger: L1-60, L55-144, L145-254, L255-354, L354-463, L463-538 read in sequence;
  last line L537 "BILLING CODE 9111-97-P" reached. Remaining unread: none. Manifest 117,768 chars.

## D02 - Clarification Regarding Bars to Eligibility During Credible Fear and Reasonable Fear Review (DOJ/EOIR IFR)

- Source: `docs/fr_2024_30500.txt` -> `text/D02.txt`, 450 lines; FR pages 105392-105403 (12 pages).
- Written or submitted by: Department of Justice, Executive Office for Immigration Review (EOIR).
  Signed "Merrick B. Garland, Attorney General" (L446-447). DOJ alone ("the Department" = DOJ here).
- Type, date, edition: "Interim final rule; request for comment" (L23). Federal Register Vol. 89,
  No. 248, Friday, December 27, 2024 (L3-5). FR Doc 2024-30500, "Filed 12-26-24; 8:45 am" (L448).
  8 CFR Parts 1003 and 1208; "EOIR Docket No. 025-0910; A.G. Order No. 6107-2024"; RIN 1125-AB33 (L15-17).
- Period covered: none (no statistics).
- Entities and aliases: "the Department" = DOJ; DHS; EOIR; USCIS; IFR; INA; HSA; CAT; FARRA; IIRIRA;
  APA; RFA; UMRA; OIRA; NEPA; CEQ; "Global Asylum Rule"; "Asylum Processing IFR"; "DHS Mandatory Bars"
  (= 89 FR 103370); "Lawful Pathways rule"; "Securing the Border rule"; "noncitizen" used for "alien"
  (fn 1 L60-61). Forms: "Form I-863, Notice of Referral to Immigration Judge"; "Form I-869, Record of
  Negative Credible Fear Finding and Request for Review".
- People: Sarah Flinn, Acting Assistant Director for Policy, Office of Policy, EOIR, "5107 Leesburg
  Pike, Suite 1800, Falls Church, VA 22041" (L36), tel. (703) 305-0289 (L38); Merrick B. Garland.

### D02 dates

- Signed: "Dated: December 17, 2024." (L445).
- Publication: Friday, December 27, 2024. Effective: "This interim final rule is effective December
  27, 2024." (L30).
- Comment deadline: "on or before January 27, 2025" ... "until 11:59 p.m. Eastern Time on that date" (L31).
- Rules cited with dates:
  - DHS final rule on the D01 subject: "Most recently, in December 2024, DHS issued a rule" ... "See 89
    FR 103370 (Dec. 18, 2024) (``DHS Mandatory Bars'')" (L147, [[Page 105396]]); again L159, L298;
    categorical exclusion "89 FR 103412- 413" (L298-299).
  - Global Asylum Rule "85 FR 80274, 80278 (Dec. 11, 2020)"; "On January 8, 2021, the Global Asylum
    Rule was enjoined before its effective date" (L144-145); "85 FR at 80278" (L237).
  - Asylum Processing IFR "87 FR 18078, 18219, 18221-22 (Mar. 29, 2022)" - "in 2022" (L146).
  - "Circumvention of Lawful Pathways, 88 FR 31314, 31450 (May 16, 2023)"; "Securing the Border, 89 FR
    81156 (Oct 7, 2024)" (L119; again L160-161).
  - "64 FR 8478 (Feb. 19, 1999), amended by 64 FR 13881 (Mar. 23, 1999)" (L80); 64 FR at 8478, 8479,
    8485 (L128-133).
  - "68 FR 9824, 9834 (Feb. 28, 2003)"; "70 FR 4743, 4749 & n.7 (Jan. 31, 2005)"; "73 FR 10130, 10132
    (Feb. 26, 2008)" (L192); "Efficient Case and Docket Management in Immigration Proceedings, 89 FR at
    46787" (L189, no date).
  - Executive orders: "58 FR 51735 (Sept. 30, 1993)"; "88 FR 21879 (Apr. 6, 2023)"; "76 FR 3821 (Jan.
    18, 2011)" (L253); "61 FR 4729 (Feb. 5, 1996)" (L270).
  - "Immigration Court Practice Manual, Chapter 7.4(e)(4)(E) (October 25, 2023)" (L175).
  - fn 14 (L294): "November 12, 2024 decision in Marin Audubon Society v. Federal Aviation
    Administration, No. 23- 1067 (D.C. Cir. Nov. 12, 2024)".
  - Treaties: "January 31, 1967"; "July 28, 1951"; "Dec. 10, 1984" / "Nov. 20, 1994" (L68-69, L79);
    Refugee Act of 1980 = "Public Law 96-212, 94 Stat. 102" (fn 3 L72).
- Not mentioned anywhere in D02: the Security Bars rule, its delays, 85 FR 84160, Title 42, COVID-19.

### D02 numbers and time limits

- Credible fear review (statute): "as expeditiously as possible, to the maximum extent practicable
  within 24 hours, but in no case later than 7 days" after the asylum officer's determination (L120).
  Regulatory text Sec. 1003.42(e): "within 24 hours, but in no case later than 7 days after the date the
  supervisory asylum officer has concurred with the asylum officer's negative credible fear
  determination issued on the Form I-869" (L365). L200 explains "concurred with" replaces "approved".
- Reasonable fear review: "within 10 days of filing the referral with the immigration court" (L136);
  regulatory text Sec. 1208.31(g): "In the absence of exceptional circumstances, such review shall be
  conducted by the immigration judge within 10 days of the filing of the Form I-863 ... and the
  complete record of determination" (L402).
- Bar counts: "the statute contains six mandatory bars to asylum eligibility" (L99-100); "four similar
  mandatory bars to withholding of removal eligibility" (L101); fn 6 (L104) "another bar to withholding"
  (Nazi persecution, genocide, torture, extrajudicial killing) that "does not apply to noncitizens in
  expedited removal" but "could be relevant for purposes of reasonable fear screening".
- APA "30-day delay in the effective date" (L239-240) - stated not to apply.
- UMRA "$100 million or more expenditure (adjusted annually for inflation)" (L261).
- No statistics, wages, costs, burden hours or populations. "will not have a significant impact on
  adjudicators, the parties, and the broader public" (L256). No new collections (L306).

### D02 tables

Three word-replacement tables in the amendatory text; two columns (unlabelled; instruction text calls
them "left column" = words removed, "right column" = words added). No units.

- Instruction 2.a, Sec. 1003.42 (L339-349, [[Page 105401]]), 8 rows: an alien -> a noncitizen; The
  alien -> The noncitizen; the alien -> the noncitizen; the alien's -> the noncitizen's; an alien's ->
  a noncitizen's; Aliens -> Noncitizens; same alien -> same noncitizen; the Service -> DHS.
- Instruction 4.d, Sec. 1208.31 (L386-394, [[Page 105402]]), 6 rows: an alien -> a noncitizen; the
  alien -> the noncitizen; any alien -> any noncitizen; alien's -> noncitizen's; aliens ->
  noncitizens; the Service -> DHS.
- Instruction 5.a, Sec. 1208.33 (L410-417), 5 rows: An alien -> A noncitizen; an alien -> a
  noncitizen; The alien -> The noncitizen; the alien -> the noncitizen; alien's -> noncitizen's (no
  "the Service" row).

### D02 lists: sections and amendatory instructions (6 numbered, L324-443)

1. Authority citation, part 1003, "continues to read" (L327-332).
2. Sec. 1003.42: (a) word table; (b) "Revising paragraphs (a), (d) and (e)"; (c) "In paragraph (b),
   (c), and (f) through (i)" decapitalise "Immigration Court"/"Immigration Judge" (L335-365).
3. Authority citation, part 1208, "continues to read" (L371-373).
4. Sec. 1208.31: (a) revise section heading; (b) "Removing and reserving paragraphs (b), (c), and (d)";
   (c) revise paragraph (g) introductory text; (d) word table (L378-402).
5. Sec. 1208.33: (a) word table; (b) "unaccompanied alien child as defined in 6 U.S.C. 279(g)(2)" ->
   "unaccompanied child as defined in 8 CFR 1001.1(hh)" in (a)(2)(i); (c) "8 CFR 214.201(a)" ->
   "8 CFR 214.201" in (a)(3)(i)(C); (d) revise (b)(1), (b)(2)(i), (b)(2)(ii) (L406-436).
6. Sec. 1208.35: "Sec. 214.11 of this title" -> "Sec. 214.201 of this title" in (a)(2)(i)(C) (L442-443).

- Sections amended: 8 CFR 1003.42, 1208.31, 1208.33, 1208.35. Parts in the header: 1003 and 1208.
- Sections named as not changed: 8 CFR 1208.30 (procedures "currently follow" unchanged, L178);
  Sec. 1208.35 for the bars-review clarification - fn 8 (L171): "unnecessary to also amend the Securing
  the Border regulatory section at 8 CFR 1208.35". Compare instruction 6 (L442), which does amend
  Sec. 1208.35(a)(2)(i)(C) as one of "two non-substantive corrections to inadvertent errors in
  cross-references" (L183-187). Both locations recorded; the document treats them as different kinds
  of change.
- Terminology change scope stated in the preamble: "replaces the term ``alien'' with ``noncitizen'' in
  8 CFR 1003.42, 1208.31, and 1208.33" (L188).
- NEPA: adopts DHS's categorical exclusion determination; "categorical exclusion A3" (L298-302).

### D02 definitions, rules, conditions

- New Sec. 1003.42(d) sentence: "This determination shall, where relevant, include review of the asylum
  officer's application of any bars to asylum and withholding of removal pursuant to 8 CFR
  208.30(e)(5)." (preamble L167; regulatory text L364 - identical).
- New Sec. 1208.31(g) sentence, regulatory text: "The immigration judge's review shall, where relevant,
  include review of the asylum officer's application of any bars to withholding of removal pursuant to
  8 CFR 208.31(c)." (L401-402). Preamble quotation of it omits "to withholding of removal": "application
  of any bars pursuant to 8 CFR 208.31(c)" (L168). "de novo" added to 1208.31(g) (L158, L401).
- New Sec. 1208.33(b)(1) sentence: "include review of the asylum officer's application of any bars to
  withholding of removal pursuant to 8 CFR 208.33(b)(2)" (L429).
- Scope limits: "does not itself modify or alter the substantive standards" (L178); "do not affect the
  ability of a noncitizen to pursue or receive deferral of removal under the CAT" (L179); country
  designation "is not reviewable during a credible fear review" (L211-217).
- Condition on review: "where relevant"; a bar review "may be unnecessary" when the judge finds no fear
  "for a separate reason unrelated to any bars" (L176).
- APA basis: procedural-rule exemption, 5 U.S.C. 553(b)(A) (L234); "the Department invites public
  comment on this IFR, and will, before issuing a final rule, consider any such comments" (L238).
- Congressional Review Act: "is not a ``rule''" (L310).

### D02 hedged claims

- "there may be instances where review of an asylum officer's application of a bar may be unnecessary"
  (L176) - attaches to the need for bar review in a given case.
- fn 6 "this bar could be relevant for purposes of reasonable fear screening" (L104).
- "should DHS make future regulatory changes" (L237) - future DHS action; the EOIR text is stated firmly
  ("will not require further EOIR rulemaking action").
- fn 14 "To the extent that a court may conclude that the CEQ regulations ... are not judicially
  enforceable" (L294).
- "the Department believes that the changes adopted in this IFR will not have a significant impact"
  (L256).

### D02 as-printed inconsistencies

- "8 U.S.C. 1241(b)(3)(B)" at L139 and L147; "8 U.S.C. 1231(b)(3)(B)" at L69, L101, L107.
- Reinstatement cited "INA 241(b)(5), 8 U.S.C. 1231(b)(5)" at L134; "section 241(a)(5) of the INA,
  8 U.S.C. 1231(a)(5)" at L128.
- fn 8 (L171) "screened for a reasonable probability of establishing eligibility"; "reasonable
  possibility" elsewhere (L134, L436).
- Sec. 1003.42(d) text says withholding "under section 241(b)(3)(B) of the Act" (L364); Sec.
  1208.33(b)(2)(i) says "under section 241(b)(3) of the Act" (L431).
- Address: "Suite 1800" in ADDRESSES (L36), no suite in FOR FURTHER INFORMATION CONTACT (L38).

- Public health references: only L253 (Executive Order boilerplate "public health, and safety
  effects"). No Title 42, communicable disease, CDC, HHS, Ebola, COVID, pandemic.
- Coverage: FULL. Ledger: L1-109, L110-218, L219-337, L338-450 read in sequence; last line L449
  "BILLING CODE 4410-30-P" reached. Remaining unread: none. Manifest 84,321 chars.

## D03 - Security Bars and Processing; Confirmation of Effective Date; Partial Withdrawal (DHS/DOJ final rule)

- Source: `docs/fr_2025_23970.txt` -> `text/D03.txt`, 530 lines; FR pages 61035-61049 (15 pages).
- Written or submitted by: jointly DHS (USCIS) and DOJ (EOIR) = "the Departments". Signed "Kristi
  Noem, Secretary of Homeland Security" and "Daren K. Margolin, Director, Executive Office for
  Immigration Review, Department of Justice" (L525-528). fn 2 (L78-79): "Attorney General Order Number
  6260-2025 (May 8, 2025)" delegated EOIR rulemaking authority to EOIR's Director.
- Type, date, edition: "Final rule; partial withdrawal and correction" (L43). Federal Register Vol. 90,
  No. 246, Tuesday, December 30, 2025 (L3-5). FR Doc 2025-23970, "Filed 12-29-25; 8:45 am" (L529). DHS:
  8 CFR Parts 208 and 235, RIN 1615-AC57, "CIS No. 2844-26; Docket No: USCIS 2020-0013". DOJ: 8 CFR
  Parts 1003, 1208, and 1235, RIN 1125-AB08, "Dir. Order No. 03-2025" (L25-37). No "Dated:" line.
  It corrects "FR Doc. 2020-28436 appearing on page 84160 in the Federal Register of Wednesday,
  December 23, 2020" (L476-477).
- Period covered: rulemaking history July 2020 - December 2025. No fiscal-year statistics.
- Entities and aliases: "the Departments"; "Security Bars Final Rule" (also printed "Security Bar Final
  Rule" L229, L235, and "Security Bars final rule" inside quotations L175-177); "Security Bars NPRM";
  "Global Asylum Final Rule"; "January 2021 Delay Final Rule"; "March 2021 Delay IFR"; "December 2021
  Delay IFR"; "December 2022 Delay IFR"; "December 2024 Delay IFR"; "Asylum Processing IFR"; "Lawful
  Pathways Final Rule"; "TCT Bar Final Rule"; "DHS Mandatory Bars Rule"; "EOIR Bars IFR"; "Pangea II";
  AOs; "AWO" (asylum-and-withholding-only) proceedings; OFR; BIA / "Board"; "CAT protection";
  "statutory withholding of removal"; "IFR" = interim final rule (fn 1 L66). Uses "alien" throughout.
- Contacts: USCIS Humanitarian Affairs Division, "5900 Capital Gateway Drive, Camp Springs, MD 20746;
  telephone (240) 721-3000" (L55); EOIR Immigration Law Division, "5107 Leesburg Pike, Suite 2500,
  Falls Church, VA 22041; telephone (703) 305-0289" (L56).

### D03 dates

- Publication: Tuesday, December 30, 2025.
- "Partial Withdrawal: As of December 29, 2025, amendatory instructions 4, 5, 6, 7, 8, 12, 13, and 14
  published on December 23, 2020, at 85 FR 84160 ... are withdrawn." (L50-51).
- "Effective Date: The corrections in this document are effective December 31, 2025." (L52).
- No comment period is opened by D03.

### D03 chronology of the Security Bars rule (all dates and FR cites as printed)

| Step | Document (D03 name) | FR cite / date | Effective date it set or delayed to | Location |
| --- | --- | --- | --- | --- |
| Proposal | Security Bars NPRM | "On July 9, 2020" - 85 FR 41201 | - | L136 |
| Related rule | Global Asylum Final Rule | 85 FR 80274 (Dec. 11, 2020) | enjoined (Pangea II) | L136, L168 |
| Final | Security Bars Final Rule | 85 FR 84160 (Dec. 23, 2020); FR Doc. 2020-28436 | "slated to become effective on January 22, 2021" | L62, L136, L168, L477 |
| Injunction | Pangea II, 512 F. Supp. 3d 966, 977 (N.D. Cal. 2021) | "prior to the January 22, 2021, effective date" (no day given in D03) | - | L168 |
| Delay 1 | January 2021 Delay Final Rule | 86 FR 6847 (Jan. 25, 2021) | not stated in D03 | L62-63, L169 |
| Delay 2 | March 2021 Delay IFR | 86 FR 15069 (Mar. 22, 2021); pin 15070-71, 15071 | not stated in D03 | L63, L169, fn 11 L216 |
| Delay 3 | December 2021 Delay IFR | 86 FR 73615 (Dec. 28, 2021); pin 73616-17, 73617 | not stated in D03 | L63, L169, L216 |
| Delay 4 | December 2022 Delay IFR | 87 FR 79789 (Dec. 28, 2022); pin 79790-93 | "until December 31, 2024" ("a two-year delay", L319) | L63, L175, L319 |
| Delay 5 | December 2024 Delay IFR | 89 FR 105386 (Dec. 27, 2024); pin 105387-89 | "until December 31, 2025" ("a one-year further delay", L319) | L63, L176-177, L319 |
| This rule | D03 | Vol. 90, page 61035, Dec. 30, 2025 (header; no "90 FR" self-cite printed) | unwithdrawn provisions take effect "as scheduled" Dec. 31, 2025 | L47, L213 |

- Ordinals used by D03: "the second, third, and fourth delays" = March 2021, December 2021, December
  2022 delay IFRs (L276-277, L335); "the fifth delay" = December 2024 Delay IFR (L335).
- The delayed-to dates of delays 1-3 are printed nowhere in D01-D03 (grep for "March 22, 2021",
  "December 31, 2021", "December 31, 2022" as effective dates: no hits).
- Comments: requested and received on delays 2-4 (L276-277); "The Departments did not receive any
  comments on the December 2024 delay IFR" (L277; fn 17 L281 gives the docket query window
  "postedDateFrom=2024-12-27&postedDateTo=2025-11-10"). The March 2021 Delay IFR also asked about
  "a potential future rulemaking rescinding or amending" the rule (fn 11 L216; L335).
- Stated reasons for delays: Pangea II injunction against the Global Asylum Final Rule (L168-169);
  conflict with the Asylum Processing IFR (L175); "limited resources and intervening regulatory
  priorities" (L176); "no existing public health situation that would trigger the bars" as of the
  December 31, 2024 date (L177, quoting 89 FR 105389).
- Proposal vs action: the Departments "previously suggested that they may initiate a new rulemaking"
  ... "after further consideration decline to pursue a new rulemaking" (L213).

### D03 other dates

- Subsequent rules: "On March 29, 2022, the Departments issued the Asylum Processing IFR" - 87 FR 18078
  (L175, L189); "On May 16, 2023, the Departments published the Lawful Pathways Final Rule, 88 FR
  31314" (L191); "On December 18, 2024, DHS issued the DHS Mandatory Bars Rule" - 89 FR 103370 (L193);
  EOIR Bars IFR "89 FR 105392 (Dec. 27, 2024)" (L69, L202); "Securing the Border, 89 FR 81156 (Oct. 7,
  2024)" (L176; fn 22 L381 "89 FR 81186").
- Rescinded bars (fn 8 L165): "83 FR 55934 (Nov. 9, 2018)"; "Asylum Eligibility and Procedural
  Modifications, 85 FR 82260 (Dec. 17, 2020)" = "TCT Bar Final Rule" (L191).
- 2025 items (section V.A.4 and footnotes, L367-405): "Designating Aliens for Expedited Removal, 90 FR
  8139, 8139 (Jan. 24, 2025)" (L370); "Executive Order 14150 of January 20, 2025" - "90 FR 8337 (Jan.
  20, 2025)" (L375); "Executive Order 14165 ... 90 FR 8467 (Jan. 20, 2025)" (fn 21 L380); Colombia
  "on January 26, 2025" (fn 24 L389); "90 FR 12200, 12200 (Mar. 14, 2025)" (L405); OMB "M-25-20 ...
  (Mar. 26, 2025)" (L412); "Presidential Proclamation 10935, 90 FR 20357 (May 9, 2025)" (L392);
  "on May 19, 2025, DHS conducted a voluntary charter flight" (fn 25 L395); "90 FR 27439, 27454-55 &
  nn.48-55 (June 27, 2025)" (L375); "Document Drafting Handbook 6-4 (June 2025)" (L207); DHS release
  "(Aug. 1, 2025)" (fn 13 L245); CBP release "(Oct. 24, 2025)" (fn 20 L379); DHS NEPA page "(July 29,
  2025)" (fn 26 L450).
- fn 23 agreements (L387-388): Honduras "90 FR 30076 (July 8, 2025)"; Guatemala "90 FR 31670 (July 15,
  2025)"; Uganda "90 FR 42597 (Sept. 3, 2025)"; Ecuador "90 FR 51376 (Nov. 17, 2025)"; Paraguay press
  statement "(Aug. 14, 2025)"; Belize "(Oct. 20, 2025)"; Ecuavisa "(Sept. 1, 2025)".
- Older: "69 FR 60938, 60938 (Oct. 13, 2004)" (fn 5 L93-94); "88 FR 18227 (Mar. 28, 2023)" (fn 15
  L271); "April 1, 1997" in the regulatory text (L489, L514).

### D03 numbers

- No statistics, wages, cost or burden estimates, or population counts.
- "four rules amending their credible fear provisions" (L185); "five different paragraphs" (L227);
  eight withdrawn instruction numbers (L50, L225); "30-day delay" (L332), "not less than 30 days"
  (L341); "$100 million or more" (L421, L427); Executive Order 14192 "at least 10 prior regulations"
  (L409-410); titles of cited releases contain "5 Straight Months of 0 Releases" (fn 20) and "hasta
  300 refugiados al a[ntilde]o" (fn 23, as printed with bracketed diacritics).
- Regulatory text has no numeric day count: "the number of days equivalent to the longest known
  incubation and contagion period for the disease" (L492, L517).

### D03 lists and exact membership

- Withdrawn in full (8): amendatory instructions "4, 5, 6, 7, 8, 12, 13, and 14" (L50, L225).
  - "amendatory instructions 4, 6, 8, 12, and 14 are withdrawn" (L242) - the credible-fear instructions
    (also named at L137).
  - "also withdrawing amendatory instructions 5, 7, and 13, which include authority citations rendered
    unnecessary by the withdrawal of the former list of instructions" (L242).
  - Sections these eight would have amended: "8 CFR 208.30, 235.6, 1003.42, 1208.30, and 1235.6" (L225).
  - Instruction-to-provision links D03 states: instruction 4 -> 8 CFR 208.30(e)(5) (would "add paragraph
    (iv)", L200; would add back 208.30(e)(5)(iii), L191); instruction 8 -> "8 CFR 1003.42(d)(1), a
    paragraph that no longer exists" (L202); instruction 12 -> 1208.30(g)(1) (L191); "amendatory
    instructions 4, 8, and 12 instruct OFR to revise five paragraphs that no longer exist: 8 CFR
    208.30(e)(5)(i)(A) and (B) and (f)(1), 1003.42(d)(1), and 1208.30(g)(1)(ii)" (L227). Instructions 6
    and 14 are not individually tied to a section; 235.6 and 1235.6 amendments are cited only by FR
    page (L162).
- Withdrawn in part (2): "the parts of amendatory instructions 3 and 11 that relate to revisions to
  paragraph (f) in 8 CFR 208.16 and 1208.16" (fn 19 L361; section III.B L248-258). Implemented as two
  numbered corrections:
  1. "On page 84193, starting in the third column, in part 208, amendment 3" now reads "Amend Sec.
     208.16 by revising paragraph (d)(2)" (L480-502).
  2. "On page 84197, starting in the first column, in part 1208, amendment 11" now reads "Amend Sec.
     1208.16 by revising paragraph (d)(2)" (L505-523).
- Provisions the Security Bars Final Rule "will no longer amend" (7): "8 CFR 208.16(f), 208.30, 235.6,
  1003.42, 1208.16(f), 1208.30, and 1235.6" (L221).
- Retained, effective as scheduled: "8 CFR 208.13(c)(10), 1208.13(c)(10) (clarification with respect to
  asylum), and at 8 CFR 208.16(d)(2), 1208.16(d)(2) (clarification with respect to statutory and CAT
  withholding of removal)" (L219; detail L262-268). The instruction numbers for the 208.13 / 1208.13
  amendments are not printed; instructions 1, 2, 9 and 10 are never mentioned by number; the total
  number of instructions in the 2020 rule is not stated.
- Subsequent rules "relevant here" (4): "(1) the Asylum Processing IFR; (2) the Lawful Pathways Final
  Rule; (3) the DHS Mandatory Bars Rule; and (4) the EOIR Bars IFR" (L185-186). A different list at
  L176 (rules noted in the December 2024 Delay IFR): Asylum Processing IFR; Lawful Pathways Final Rule;
  DHS Mandatory Bars Rule; Securing the Border - no EOIR Bars IFR.
- Which later rule drives which withdrawal: Asylum Processing IFR removed 208.30(e)(5)(i)(A), (B) and
  (f)(1) (L189, L227-228); Lawful Pathways Final Rule removed 208.30(e)(5)(iii) and 1208.30(g)(1),
  redesignated 1003.42(d)(1) as (d) -> instructions 4 and 12 (L191, L228); DHS Mandatory Bars Rule ->
  instruction 4 (L200); EOIR Bars IFR -> instruction 8 (L202-209).
- Five ways the 2020 rules changed the expedited removal process: First ... Fifth (L138-161).
- Statutory bars list (L113-125): same five-plus-sixth structure as D01 L81-89, U.S.C. parallels
  printed "1231(b)(3)(B)(i)" etc.
- Third-country agreement list, fn 23 (L387-388): Honduras, Guatemala, Uganda, Ecuador (Federal
  Register notices); Paraguay, Belize (press statements); plus an Ecuavisa news item.
- APA grounds invoked (section V.A): 1 Notice and Comment satisfied (L333); 2 Procedural Rule (L339);
  3 Good Cause (L355); 4 Foreign Affairs (L367).
- "List of Subjects 8 CFR Parts 208 and 1208" (L472) - header parts are 208, 235, 1003, 1208, 1235.

### D03 regulatory text and definitions (corrections 1 and 2)

- Paragraph (d)(2) structure, same in both sections: (i) "In general" (preponderance burden; "April 1,
  1997"); (ii) "Public health emergencies" - "If a communicable disease has triggered an ongoing
  declaration of a public health emergency under Federal law, such as under section 319 of the Public
  Health Service Act, 42 U.S.C. 247d, or section 564 of the Food, Drug, and Cosmetic Act, 21 U.S.C.
  360bbb-3" and the alien (A) "Exhibits symptoms" or (B) "Has come into contact with the disease
  within the number of days equivalent to the longest known incubation and contagion period"; (iii)
  "Danger to the public health caused by an epidemic outside of the United States" - "a communicable
  disease of public health significance as defined at 42 CFR 34.2(b), the Secretary and the Attorney
  General, in consultation with the Secretary of Health and Human Services, have jointly" (A)
  Determined, (B) Designated, then (C) ineligibility; (iv) exception for an alien returning "from
  Canada" under the U.S.-Canada agreement. Sec. 208.16 text L489-501; Sec. 1208.16 text L514-522.
- Difference between the two corrected texts: in Sec. 208.16(d)(2)(iii)(B) and (C) the internal
  cross-references read "paragraph (d)(2)(ii)(A) of this section" and "paragraph (d)(2)(ii)(B)" (L499,
  L500); in Sec. 1208.16(d)(2)(iii)(B) and (C) they read "paragraph (d)(2)(iii)(A)" and "paragraph
  (d)(2)(iii)(B)" (L520, L521). Punctuation also differs ("if the alien:" L490 vs "if the alien--"
  L515; "have jointly:" L493 vs "have jointly--" L518); Sec. 1208.16(d)(2)(iv) ends "Third Countries)."
  with an unmatched parenthesis (L522).
- Preamble description of the retained provisions (L262-268): criteria "such as exhibiting symptoms of
  a disease or having been exposed to the disease during its incubation and contagion period"; "allow
  DHS, DOJ, and the Department of Health and Human Services to jointly designate regions or countries
  experiencing epidemics"; Canada exemption "under section 208(a)(2)(A) of the INA".
- Standards: fn 7 (L148-150) - the "significant possibility of eligibility for asylum" standard "is
  lower than the ``reasonable possibility of persecution or torture'' standard". AWO proceedings: "may
  apply only for asylum, statutory withholding of removal, and CAT protection" (L159).
- Discretionary vs mandatory: "Under the DHS Mandatory Bars Rule, AOs determine at their discretion"
  ... "in contrast, the Security Bars Final Rule would make such consideration mandatory" (L194).
  Current 8 CFR 208.30(e)(5)(ii) quoted: "``appears to be subject to one or more of the mandatory
  bars'' other than the firm resettlement bar, the AO ``may consider the applicability of such
  bar(s).''" (L200). Torture screening standard under current (ii) "significant possibility"; under
  withdrawn paragraph (iv) "more likely than not" (L200).
- Third-country removal: withdrawn 208.16(f)/1208.16(f) revisions would have tested only likelihood of
  torture, not persecution (L250-252); current paragraph (f) "reiterates that DHS may remove an alien
  granted withholding ... to a third country" (L250). Preamble-vs-text condition: the 2020 preamble
  limited third-country removal to aliens found ineligible under the security bars (quoted L252, 85 FR
  84181), "However, the regulatory text does not include the requirement" (L252); fn 14 (L255) adds the
  2020 rule also contemplated third-country removals under the TCT Bar.
- fn 19 (L361): the 208.16(f)/1208.16(f) withdrawals "are not the result of amendments by intervening
  rules" (unlike the eight fully withdrawn instructions).
- fn 18 (L282): comments "unrelated to the changes made by the Security Bars Final Rule" are not
  addressed.
- Effect statements: "these withdrawals will have no immediate impact on current credible fear
  screening processes or the adjudication of asylum applications" (L242); "The rule makes no changes to
  the substantive public health-related provisions" (L69).

### D03 hedged claims

- "the Departments may still consider the Security Bars Final Rule's clarifications ... in such
  screenings" (L69) - permission, tied to the DHS Mandatory Bars Rule and EOIR Bars IFR.
- "cover aliens who may pose certain public health risks" (L219); "aliens may be ineligible for asylum
  and withholding of removal ... based on certain public health concerns" (L231).
- "the OFR would be unable to revise a non-existent paragraph and thus would add an editorial note"
  (L206; also L228 "would instead add editorial notes") beside the Handbook's "OFR may ``add an
  editorial note of the agency error''" (L207, L228).
- "it may interfere with the Departments' ability to apply its amendments" (L235).
- "could lead a reader to believe, incorrectly" (L252) - attaches to the 208.16(f) text.
- "there would be no direct, immediate impact ... because there [was] no existing public health
  situation" (L177) - quoted from the December 2024 Delay IFR, scoped to December 31, 2024.
- "those disincentives may disappear" (L370); "countries may be less inclined to engage" (L399).
- "some courts have required such a showing" (L369).

### D03 public health / HHS / pandemic references

- Summary L47 ("an alien who poses a public health risk"); L62 ("certain emergency public health
  concerns"); L136 ("emergency public health concerns generated by a communicable disease"); L177; L219;
  L231; L251; L262-268 (HHS joint designation; "epidemics"); comments section IV.A-B L287-311 ("pandemic-
  related spread" L294; "COVID-19 testing and isolation" L298; INA 212(a)(1)(A)(i) "communicable disease
  of public health significance" L289); L321-325, L337-338, L348; regulatory text L490-501, L515-522.
- "infectious diseases" (L336).
- No occurrence of "Title 42", "42 U.S.C. 265", "Ebola", "CDC" or "Centers for Disease".

### D03 as-printed inconsistencies

- "See 85 FR 84810" (L250) vs "85 FR 84181" for the same preamble passage two sentences later (L252,
  fn 14 L255).
- "section 533(d) of the APA" (L365) vs "5 U.S.C. 553(d)" (L332, L356).
- fn 12 (L238) labels a citation to the 2024 NPRM page as "DHS Mandatory Bars Rule, 89 FR 41358".
- "85 FR 84194--98" (L162); "84197-8" (L157); "85 FR 84194-5" (L191).
- Billing code "4410-10-P; 9111-979111-97-P" (L529).

- Coverage: FULL. Ledger: L1-89, L90-178, L179-258, L259-332, L333-422, L423-530 read in sequence;
  last line L529 (signature/billing code) reached. Remaining unread: none. Manifest 116,775 chars.

## D04 - CDC interim final rule, Foreign Quarantine (Doc 4)

- Source: docs/fr_2026_10543.txt | 91 FR 31362-31368, Wednesday May 27, 2026; FR Doc 2026-10543, filed 5-22-26 4:15 pm
- Written by: HHS / CDC; signed Robert F. Kennedy, Jr. Docket CDC-2026-0991, RIN 0920-AA88
- Type, date, edition: interim final rule amending 42 CFR 71.40(f). Read in full (lines 1-231).
- Dates (L29-31): effective May 22, 2026; comments by June 26, 2026; expires "on the earlier of (1) six months from the publication of this interim final rule, or (2) when the HHS Secretary determines there is no longer a need".
- Rule text (L223): "(f) This section shall not apply to U.S. citizens and U.S. nationals." (LPR exception removed; preamble L62 says current rule excepted LPRs.)
- Outbreak facts (L77-79): centered in Ituri; "hundreds of suspected cases and dozens of deaths"; Uganda "confirmed imported cases ... including one case detected in Kampala"; South Sudan no confirmed cases. No case counts.
- May 18, 2026 (L89): WHO PHEIC declaration; CDC "initial order suspending the entry of covered aliens".
- Incubation (L64, L85): "typically between 2 and 21 days, with most people developing symptoms within 4 to 10 days"; "can extend up to 21 days".
- Travel figures (L73): 2025 international visitations "over 68 million"; 2020 "when this regulation was amended to introduce the suspension of introduction of persons" "only 19.8 million".
- Other figures (L105): 2009 H1N1 100,000-600,000 deaths; Spanish Flu over 50 million; COVID-19 2020-2023 "approximately 7.11 million deaths"; pandemics "three months or less", "12 to 18 months". UMRA threshold "approximately $193 million" (L164).
- Lists: transit hubs (L84) five: ADD, NBO, DOH, DXB, IST (no Brussels); U.S. gateways five: JFK, IAD, ATL, ORD, LAX. Prior outbreaks list (L72). Influenza pandemics (L103).
- Determinations: "economically significant" (L155); "major rule" (L190).

## D05 - CDC Order of June 21, 2026 (Doc 5)

- Source: docs/fr_2026_12790.txt | 91 FR 38441-38446, Thursday June 25, 2026; filed 6-24-26. Docket CDC-2026-0892. Read in full (lines 1-258).
- Signed: Admiral Brian Christine, ASH, "at Santa Fe, NM this 21st day of June, 2026" (L238). Contact Matthew J. Buzzelli, Chief of Staff.
- Dates (L25-27): issued June 21, 2026; took effect June 21 at 5:00 p.m. EDT; "in effect through 4:59 p.m. ... Tuesday, July 21, 2026"; comments by July 10, 2026; "simultaneous 15-day comment period" (L234).
- History (L38-39): May 18 Order by "the Senior Official Carrying out the Delegable Duties of the Director"; May 22 Amended Order by the ASH (LPR exemption gone); comments on both "through June 22, 2026"; "three comments".
- Comments (L43-56): one on discrimination; a second on CDC/DHS roles; Airlines for America with six numbered requests. CDC declines province-only scope, foreign flight crew and transit exceptions; arrival airports are DHS's (91 FR 29896).
- DRC (L125): "On May 22, 2026, when the Amended Order was issued, DRC reported 91 confirmed cases across 11 health zones. As of June 15, 2026, DRC reports 837 confirmed cases across 31 health zones, representing an increase of more than 800 percent". Provinces: Ituri, North Kivu, South Kivu. No DRC death count.
- Uganda (L126): "As of June 14, 2026, Uganda reports 19 confirmed cases of Ebola disease and two deaths, as well as one probable case and one probable death. When the Amended Order was issued, only two cases were reported."
- THN (L147): "Level 3 ... for DRC on May 15, 2026, and a Level 2 THN ... for Uganda on May 26, 2026. On June 15, 2026, CDC narrowed the geographic scope of the DRC Level 3 THN to ... Ituri, North Kivu, and South Kivu, while maintaining a Level 2 THN for the remainder". Footnote 7: notice updated May 22.
- Hubs (L139): six (adds Brussels BRU).
- Scope (L87-107): present in DRC, Uganda or South Sudan in last 21 days, incl. LPRs; four excepted groups.

## D06 - CDC Order of July 13, 2026 (Doc 6)

- Source: docs/fr_2026_14365.txt | 91 FR 43636-43642, Thursday July 16, 2026; filed 7-15-26. Read in full (lines 1-286).
- Signed: "at Washington, DC this 14th day of July, 2026" (L264), "Dated: 07/14/2026"; the notice says issued July 13.
- Dates (L25-27): issued July 13; effect 5:00 p.m. EDT July 13; through 4:59 p.m. EDT Wednesday, August 12, 2026; comments by July 31, 2026. L261: "Monday, July 13, 2026" then "Tuesday, July 13, 2026" (flights sentence).
- History (L38-43): as D05, plus "On June 21, 2026, the ASH signed a new 30-day Order ... 15-day comment period. During this time CDC received five comments".
- Comments (L47-56): one (CDC lacks authority to exempt citizens); another (opposed; citizens' right to return); "Three of the commenters" on LPRs; "Two of these commenters also requested that Uganda be evaluated independently and removed".
- DRC (L125): "On June 15, 2026, when the last Order was issued, DRC reported 837 confirmed cases across 31 health zones. As of July 12, 2026, DRC reports 1,873 confirmed cases and 672 deaths across 41 health zones, with cases more than doubling since issuance of the June 22 Order." Provinces add Haut-Uele, Tshopo.
- L126-130: "an estimated 80 percent of newly confirmed cases are not linked to known contacts" (epicenter; Reuters July 10); "true magnitude ... two to four times greater".
- Uganda (L136): "As of July 12, 2026, Uganda reports 20 confirmed cases of Ebola disease and two confirmed deaths, as well as one probable case and one probable death."
- Events: physician diagnosed in France (WHO briefing June 24, 2026); July 10, 2026 U.S. citizen humanitarian worker positive; monoclonal antibody trial (WHO item 02-07-2026); CDC response Level 1 (Internal Decision Memo, June 26, 2026).
- THN (L170): "Level 2 ... for Ituri and North Kivu provinces of DRC and a Level 1 THN ... for Uganda on May 15, 2026. On May 18, 2026, CDC escalated ... to a Level 3 ... South Kivu was added to the Level 3 on May 22, 2026. On May 27, 2026, the THN for Uganda was elevated to a Level 2. On June 15, 2026 CDC issued a Level 2 THN for the remainder of DRC and Uganda." Conflicts with D05 L147 (Level 3 on May 15; Uganda Level 2 on May 26).

## D07 - CDC Order of August 12, 2026 (Doc 7)

- Source: docs/fr_2026_16706.txt | 91 FR 53252-53256, Monday August 17, 2026; filed 8-14-26. Read in full (lines 1-266).
- Signed: "at Washington, DC this 12th day of August, 2026". Contact Jordan Faircloth, Deputy Chief of Staff.
- Dates (L25-28): issued August 12; effect 5:00 p.m. EDT; through 4:59 p.m. EDT Friday, September 11, 2026; comments by September 1, 2026.
- History (L39-43): May 18 Order signed by "the Acting Director" (D05/D06: Senior Official); comments: original+Amended "3 comments"; June 21 order "five comments"; July 13 order "no comments were received".
- DRC (L112): "On July 13, 2026, when the last Order was issued, DRC reported 1,873 confirmed cases and 672 deaths across 41 health zones. As of August 9, 2026, DRC reports 4,318 confirmed cases and 2,011 deaths across 53 health zones, with cases and deaths more than doubling since issuance of the July Order." (D06 dates the 1,873 "As of July 12".)
- L113-118: contact tracing "approximately 78% nationwide", "operational threshold of 95%"; "two to four times greater".
- Uganda (L125): "As of August 11, 2026, Uganda reports 20 confirmed cases ... two confirmed deaths, as well as one probable case and one probable death. The last confirmed case was reported on June 21, 2026. Of the confirmed cases, 15 were imported cases and 5 were secondary cases"; "On July 28, 2026, the Republic of Uganda Ministry of Health declared the outbreak over"; most recent imported case "discharged ... on July 16, 2026".
- THN (L151 + fn 13-15): Aug 4, 2026 Level 4 for Ituri and North Kivu; Level 3 for South Kivu, Haut-Uele, Tshopo (the last two added Aug 4); rest of DRC and Uganda Level 2. Footnotes repeat D06's May 15 / May 18 / May 22 / May 27 / June 15 history.
- Determination (L238): "confirmed currently present in DRC and recently present in Uganda".

<!-- Read actual candidate-relevant passages with context and search the entire bundle for
duplicates/substitutes. A search is not a full read. Expand coverage when the candidate needs it;
lists/counts require the complete relevant universe, and needed gaps stay blocking. -->

## Shared ground (navigation only)

### Documents that cite, amend or respond to another document in the bundle

- D01 -> D02 (anticipated): D01 fn 37 (L307) "if DHS finalizes this NPRM, DOJ may wish to clarify the
  procedures immigration judges will follow in reviewing DHS screenings." D02 is that DOJ rule.
- D02 -> D01's final rule (not D01 itself): D02 cites "89 FR 103370 (Dec. 18, 2024) (``DHS Mandatory
  Bars'')" at L147, L159, L298; it never cites the NPRM (89 FR 41347) or its docket. The final rule
  89 FR 103370 is NOT in the bundle.
- D03 -> D01 directly: fn 12 (L238-239) quotes D01 at "89 FR 41358" - the passage is D01 L382,
  [[Page 41358]], section IV.D. D03's quotation replaces "as currently scheduled on December 31, 2024"
  with an ellipsis ("go into effect . . . , it would have implications") and prints "Under the Instant
  rule" where D01 has "Under the instant rule". D03 calls D01 "the 2024 notice of proposed rulemaking
  that preceded the DHS Mandatory Bars Rule in 2024".
- D03 -> D01's final rule: "Application of Certain Mandatory Bars in Fear Screenings, 89 FR 103370
  (Dec. 18, 2024) (``DHS Mandatory Bars Rule'')" (L69; L176, L193-200). Same title as D01 (D01 L28).
- D03 -> D02 directly: "Clarification Regarding Bars to Eligibility During Credible Fear and
  Reasonable Fear Review, 89 FR 105392 (Dec. 27, 2024) (``EOIR Bars IFR'')" (L69; section II.E.4
  L201-209). 105392 is D02's first page (D02 L6). D03 L202 quotes D02's Sec. 1003.42(d) sentence and
  cites "89 FR 105402" = D02 L364 under [[Page 105402]] (L354). D03 withdraws instruction 8 so that
  "EOIR will maintain its later-enacted provision from the EOIR Bars IFR at 8 CFR 1003.42(d)" (L209).
- D03 does not say whether comments were received on D02 or whether D02 was finalised. D02's own
  comment deadline (January 27, 2025, D02 L31) is not referred to in D03.
- Same Federal Register issue: D02 (89 FR 105392) and the December 2024 Delay IFR (89 FR 105386, cited
  D03 L51, L63) are both dated Dec. 27, 2024; D02 does not mention the delay rule.
- D04-D07 do not cite D01-D03 or any rule those documents discuss (grep, zero hits for "Security Bars",
  "84160", "credible fear", "reasonable fear", "8 CFR", "expedited removal", "withholding of removal",
  "immigration", "Pangea", "Global Asylum"). D05 L83, D06 L83, D07 L73 cite "85 FR 56424 (Sept. 11,
  2020), as amended by 91 FR 31362 (May 27, 2026); 42 CFR 71.40" - 91 FR 31362 is D04.

### Same rule described in more than one document (locations of differing details)

- December 2022 delay rule citation: D01 fn 5 (L141) "87 FR 79989 (Dec. 28, 2022)"; D03 (L51, L63,
  L172) "87 FR 79789 (Dec. 28, 2022)", with pin cites 79790-93 (L169, L175, L319). Neither document
  comments on the other.
- Security Bars rule scheduled effective date: D01 "now until December 31, 2024" (L137) and "as
  currently scheduled on December 31, 2024" (L382); D03 "scheduled to take effect on December 31, 2025"
  (L47) via the December 2024 Delay IFR (L176-177). Original date "January 22, 2021" in both (D01 L137;
  D03 L62, L168).
- Number of delay rules: D01 fn 5 lists four (through Dec. 28, 2022); D03 lists five (adds 89 FR
  105386, Dec. 27, 2024) (L50-51, L63, fn 9 L172).
- Name of the 2020 rule: D01 "``Security Bars'' or ``Asylum Eligibility and Public Health'' rule"
  (L137, L381-382); D03 "Security Bars Final Rule" (L62). D02: not mentioned.
- Who makes the public-health determination: D01 "the Secretary of Homeland Security and the Attorney
  General determined" (L144); D03 preamble "DHS, DOJ, and the Department of Health and Human Services
  to jointly designate" (L266); D03 regulatory text "the Secretary and the Attorney General, in
  consultation with the Secretary of Health and Human Services, have jointly" (L493, L518).
- Security Bars rule in credible fear: D01 L144 (negative determination, then "screened only for
  deferral of removal" at more-likely-than-not); D03 L157 (screen for more likely than not to be
  tortured, then AWO proceedings or third-country removal); D01 L382 vs D03 L229-235 on applying the
  security bar through the discretionary 208.30(e)(5) framework.
- Pangea injunction: D01 "On January 8, 2021" (L132) with ground in fn 3 (L134); D02 "On January 8,
  2021" (L144); D03 "Pangea II", no day, "prior to the January 22, 2021, effective date" (L168) and
  quotes the order's scope. Citation 512 F. Supp. 3d 966, 977 identical in all three.
- Global Asylum Rule: D01 "85 FR 80274, 80391, 80393, 80399 (Dec. 11, 2020)" (L131), "Global Asylum
  Rule"; D02 "85 FR 80274, 80278 (Dec. 11, 2020)" (L144); D03 "Global Asylum Final Rule", 85 FR 80274
  with pins 80389-94, 80399-400 (L136-162). D01 also cites its NPRM (June 15, 2020).
- Asylum Processing IFR: D01 L151 and D02 L146 both "87 FR 18078, 18219, 18221-22 (Mar. 29, 2022)";
  D03 "On March 29, 2022" with pins 18091, 18218-23, 18218-19 (L189, L227-228). Sections named: D01
  "8 CFR 208.30(e)(5)" and "8 CFR 1003.42 and 1208.30"; D02 "8 CFR 208.30(e)(5), 8 CFR 1003.42, and
  8 CFR 1208.30"; D03 "8 CFR 208.30, 1003.42, and 1208.30" plus "208.30, 235.6, 1003.42, 1208.30, and
  1235.6".
- Circumvention of Lawful Pathways: D01 "88 FR 31314 (May 16, 2023)" = "CLP rule" (L157-158) and "in
  constant effect since May 11, 2023" (L284); D02 "88 FR 31314, 31450 (May 16, 2023)" (L119); D03
  "Lawful Pathways Final Rule", "On May 16, 2023 ... published", pins 31319, 31449, 31451 (L191, L228).
- Transit-bar rules are two different documents: D01 "Third-Country-Transit Bar IFR", 84 FR 33829
  (July 16, 2019) (L283); D03 "TCT Bar Final Rule", 85 FR 82260 (Dec. 17, 2020) (L191, fn 8 L165).
- Securing the Border, 89 FR 81156 (Oct. 7, 2024): D02 L119, L160-161, fn 8 L171; D03 L176, fn 22
  L381. Not in D01 (later than D01).
- What the DHS final rule allows, as described by others: D02 L147 "bars relating to national security
  and public safety as set forth in INA 208(b)(2)(A)(i) through (v) ... and INA 241(b)(3)(B) ... during
  credible fear and reasonable fear screenings in certain instances"; D03 L193 "during credible fear
  screenings except for the bar to asylum for aliens who were firmly resettled"; D03 L69 "discretion to
  consider ... during fear screening processes"; D03 L200, L229 quote/describe current 8 CFR
  208.30(e)(5)(i)-(ii). D01's proposed text for the same paragraph: L500-507.
- Proposed vs final (D01 vs 89 FR 103370): no document in the bundle states a difference between the
  proposal and the final rule. Facts available: proposal published May 13, 2024, comments to June 12,
  2024 (D01); final "issued"/published Dec. 18, 2024 (D02 L147, D03 L193); phrase "may consider the
  applicability of such bar(s)" in D01's proposed (e)(5)(ii) (L502) and in D03's quotation of the
  current rule (L200); NEPA exclusion "A3(d)" in D01 (L474) vs "A3" for the final rule in D02 (L298).
- Statutory bar counts: D01 L82-89 and D03 L114-125 (five shared bars, a sixth asylum-only bar, plus
  further withholding bars for admitted aliens); D02 L99-101 ("six mandatory bars to asylum
  eligibility"; "four similar mandatory bars to withholding"; fn 6 "another bar").
- CAT regulation cite: D01 "as corrected by 64 FR 13881" (L72); D02 "amended by 64 FR 13881" (L80).

### Entities that appear in more than one document

- DHS / USCIS: D01 (issuer), D03 (co-issuer), D02 (mentioned). DOJ / EOIR: D02 (issuer), D03
  (co-issuer), D01 (mentioned). DHS is also mentioned in D04 L38, L99; D05 L43, L102; D06 L102; D07 L91.
- HHS: D03 L266, L493, L518 (mentioned); issuer of D04-D07.
- Signers: Mayorkas (D01); Garland (D02); Noem and Margolin (D03).
- Phone (240) 721-3000: D01 L41 and D03 L55. Phone (703) 305-0289 and 5107 Leesburg Pike: D02 L36/L38
  (Suite 1800) and D03 L56 (Suite 2500).
- RINs: 1615-AC91 (D01); 1125-AB33 (D02); 1615-AC57 and 1125-AB08 (D03). Dockets: USCIS-2024-0005
  (D01); EOIR 025-0910 (D02); USCIS 2020-0013 (D03 L28), EOIR-2020-0010 (D03 fn 16 L280).
- 8 CFR sections touched in more than one document: 208.30 (D01 proposes; D03 withdraws 2020
  amendments; D02 cross-refers); 208.31 and 208.33 (D01 proposes; D02 cross-refers at L401-402, L429);
  1003.42 (D02 amends; D03 withdraws instruction 8); 1208.31, 1208.33, 1208.35 (D02); 1208.30 (D02
  unchanged; D03 withdraws); 208.16 / 1208.16 (D03 corrects; D01 and D02 cite); 235.6 / 1235.6 (D03).
- NEPA boilerplate and DHS Directive 023-01 / Instruction Manual dates: D01 L461-474, D02 L284-302,
  D03 L447-466. Family assessment seven criteria: D01 L440, D02 L275 (not in D03).
- UMRA "$100 million": D01 L428, D02 L261, D03 L421 (and CRA L427).

### Public health, Title 42 and communicable disease across the two groups

- "Title 42 public health Order": D01 L278, L290 only (first Order "March 26, 2020"). The phrase
  "Title 42" does not occur in D02-D07.
- "42 U.S.C. 265" / PHS Act section 362: D04 L58, L62, L89, L111; D05 L65, L71, L79, L172, L185, L197,
  L252; D06 L61, L67, L75, L199, L208, L224, L279; D07 L50, L56, L63, L69, L182, L192, L205, L260. Not
  in D01-D03.
- "asylum" in D04-D07: one sentence each, "temporary visas, refugee or asylum processing mechanisms"
  (D04 L87, D05 L146, D06 L168, D07 L150). No other asylum/immigration-adjudication term found there.
- 2020 / COVID-19 in D04-D07: D04 L72 ("COVID-19 in 2020"), L73 ("in 2020 when this regulation was
  amended ... 19.8 million"; "In 2025 ... over 68 million"), L105 ("COVID-19 pandemic from 2020-2023
  caused approximately 7.11 million deaths"); D05 L83, D06 L83, D07 L73 (85 FR 56424, Sept. 11, 2020).
  COVID-19 in D01-D03: D01 L137, L381; D03 L298 (commenter).
- Incubation period: D03 regulatory text "longest known incubation and contagion period" (L492, L517,
  no number); D04 L64, L85, L91; D05 L117, L144, L163; D06 L113, L149, L189; D07 L101, L142, L173
  ("typically between 2 and 21 days", "up to 21 days", "21-day incubation period").
- Public health emergency wording: D03 L490/L515 "declaration of a public health emergency under
  Federal law, such as under section 319 of the Public Health Service Act, 42 U.S.C. 247d"; D04 L89
  WHO "Public Health Emergency of International Concern" declared "May 18, 2026" (also L140, L155).
  "section 319", "247d", "360bbb" and "42 CFR 34.2" do not occur in D04-D07 (grep).
- Canada: D03 exemption L267-268, L501, L522; D04 L136 "potential implementing partners Mexico and
  Canada".
- "Ebola", "CDC": zero occurrences in D01-D03.

### Periods

- D01 statistics: FY 2020 - FY 2024 (to April 23, 2024). No other document covers these series.
- Rulemaking timeline shared by D01-D03: July 2019 (D01) through December 30, 2025 (D03); D04-D07
  cover May-August 2026.

## Gaps

- D01, D02, D03: none. Every line of readable text was inspected; no clipped or unreadable passages.
- D04-D07: none; read in full by the caller. Series relationships among D05-D07 (restated counts and
  their date labels, travel-notice history, comment tallies) are in the D05-D07 entries above.
- Not in the bundle (cited only): DHS final rule 89 FR 103370; Security Bars Final Rule 85 FR 84160
  and its NPRM 85 FR 41201; the five delay rules; Global Asylum, Asylum Processing, Lawful Pathways
  and Securing the Border rules. Their contents are known here only as D01-D03 describe them.
