# aq-01188 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Line numbers are `text/Dnn.txt` lines (header line 1 = "# Dnn | docs/..."); the `docs/` original
line = text line minus 2 (verified by grep in every document's spot-check).

## Bundle

- What it is: nine U.S. GAO products (2003-2008): reports, a correspondence report and
  congressional testimonies on toy guns, the National Flood Insurance Program (two), alternative
  mortgage products, OCC consumer assistance, insurance-sector preparedness, bankruptcy credit
  counseling/debtor education, long-term care insurance, and fair lending data.
- Documents: 9 (D01-D09 from `text/manifest.json`; local ids alphabetical by file name and NOT
  equal to the task page's Doc N; mapping on each Source line).
- Gaps: UNREAD readable text: none (all nine documents read in full; per-document ledgers in each
  Coverage line). MISSING IN SOURCE (absent from docs/ originals, not extraction faults; the original
  PDFs are not in the workspace, so visual content is unresolved):
  - D01: Table 1 body (contacts table; title, source and notes only, L205-211).
  - D02: Appendix I Figure 1 and Figure 2 bar values (axis labels only, L317-369).
  - D03: Figure 1 and Figure 2 images (captions only, L147, L173).
  - D04: all footnote bodies (letter 1-34, Appendix I 1-3); block quotes after L313 and L319; Appendix
    II OCC comment letter (heading only, L411); Figures 1-3 values (prose repeats some).
  - D05: footnote bodies 1-17; Appendix II NAIC letter (heading only, L355); Figures 1-2 images.
  - D06: none (no tables/figures); "�" encoding artifacts at L167, L321.
  - D07: none material (Figure 1 data written out L233-607; "�" artifacts L119-131, fn6).
  - D08: none ("�" artifacts L111-125, fn1, fn4).
  - D09: Figure 1 and Figure 2 bodies (notes only, L235-239, L307-317); Appendix II DHS letter
    (heading only, L473); duplicated paragraphs L169-173 (repeated text).
- Extraction spot-checks: plain-text sources (method "text", pages null): page count not
  applicable. Each `text/Dnn.txt` line N equals `docs/` line N-2 for every grep below; in each
  document at least one table row (where tables exist: D01 Tables 2-3, D07 Tables 1-2 and Figure 1
  rows) and one footnote or note line were found identical in `docs/` (details in each Coverage
  line). Pipe tables exist only in D01 (two blocks, L337-342 and L378-383); their "1989 (8 months)"
  and "Total" rows and column headers sit outside the pipe blocks as plain lines. Lines over 1,900
  characters (D03 L189; D04 L141, L149, L297; D05 L197; D09 L185, L205, L445) were verified by grep
  to end as read (no display truncation).
- Provenance: notes/intake.json (capture_sha256 30cdaec4...); all 9 documents incomplete=false,
  gap_characters 0, matches_capture true; source_sha256 = captured_sha256 = manifest sha256 for
  every document. Capture file D:\Dev\Docket\AQ-01188_2026-10-06_1251.md ("9 of 9 captured in
  full"); no recovered-source history.

## D01 - Information Generally Not Available on Toy Gun Issues Related to Crime, Injuries or Deaths, and Long-Term Impact (GAO-03-1135R)

- Source: text/D01.txt = docs/gaoreports_gao_03_1135r.txt; task page Doc 1; 402 text lines; no pages.
- Written or submitted by: "United States General Accounting Office" (L43; note the 2003 name);
  letter signed by Laurie E. Ekstrand, Director, Homeland Security and Justice Issues (L171-173);
  Assistant Director Danny R. Burton (L167); other key contributors (6): Fredrick D. Berry, Ann H.
  Finley, SaraAnn W. Moessbauer, Julia A. Rachiele, Miguel A. Salas, Susan B. Wallace (L167).
  Requester: Representative Edolphus Towns (L7, L47). Product code (440210) at L399.
- Type, date, edition: correspondence report (letter + Enclosures I-II, "Enclosures-2" L175),
  dated September 30, 2003 (L5 "30-SEP-03", L15 "09/30/2003", L45). ACCNO A08625 (L13).
- Period covered: GAO work May to August 2003 (L55). Data periods: PERF survey Jan 1, 1985 - Sep 1,
  1989 (L73, L87, "4-2/3 years-1985 through 8 months of 1989" L321); CPSC NEISS January 2000 - July
  2003 (L93, L237); CPSC Death Certificate System and Incident Data Base "most recent 10 years (1993
  through 2002)" (L95, L97, L239, L241); CDC NEISS review "1 year reviewed (2001)" (L101); NVISS data
  2000 and 2001 (L121, L255). Literature searches: Dialog Jan 1, 1990 - July 10, 2003 (L191); Nexis
  Jan 1, 2000 - July 11, 2003 (L195); Statistical Universe files from 1973 (ASI), 1980 (SRI), 1983
  (IIS) to July 31, 2003 (L197-199). Calendar years throughout (Table 2/3 column "Calendar year").
- Entities and aliases: BJS = Department of Justice's Bureau of Justice Statistics (L55); CDC =
  HHS Centers for Disease Control and Prevention (L55); CPSC = Consumer Product Safety Commission
  (L55); PERF = Police Executive Research Forum (L69; "national membership organization of police
  executives" fn1 L81, fn9 L295, incorporated 1977); ATF = Bureau of Alcohol, Tobacco, Firearms and
  Explosives; NIJ = National Institute of Justice; FBI (L67, L225-229); UCR = Uniform Crime Reporting
  Program (L227, L358); NEISS spelled out only as "National Electronic Injury Surveillance System"
  (L93); NVDRS = CDC National Violent Death Reporting System (L121); NVISS = Harvard University's
  National Violent Injury Statistics System, pilot for NVDRS (L121); CDC National Center for Injury
  Prevention and Control (L245-249); Toy Industry Association (counsel/representative L55, L201);
  American Academy of Pediatrics' Committee on Accident and Poison Prevention (L131); Brandeis
  University (Watson and Peng study, L137, L149, L261); Surgeon General / U.S. Public Health Service
  (L141, L153). DOJ components with "no information": ATF, NIJ, FBI (L67).
- Tables:
  - Table 1 "Federal Agencies, Universities, and the Trade Association GAO Contacted" (L205): title,
    "Source: GAO." and footnotes a/b only (L207-211); NO table body in the source (absent in docs/
    original too). Missing source content, not an extraction fault.
  - Table 2 "Number of Robberies and Assaults Committed Involving Toy Guns (Jan. 1, 1985 to Sep. 1,
    1989)" (L331-354), counts by calendar year: robberies 1985 453, 1986 482, 1987 665, 1988 753,
    1989 (8 months) 443, Total 2,796; assaults 635, 615, 601, 686, 567, Total 3,104. Source PERF June
    1990 pp. 29 and 32 (L348-350). fn a: 148 police agencies (robberies); fn b: 121 agencies
    (assaults) (L352-354). Layout: pipe table L337-342 has an empty header row and holds only
    1985-1988; the "1989 (8 months)" row (L344) and "Total" row (L346) sit outside the pipe block
    as plain lines; the column header is a plain line L335 ("Calendar year Robberiesa Assaultsb").
    Column sums checked = printed totals.
  - Table 3 "Number of Incidents Where Police Officers Warned of Using or Actually Used Force Based
    on the Belief That a Toy Gun Was Real (Jan. 1, 1985 to Sep. 1, 1989)" (L374-395): warned/
    threatened 1985 55, 1986 61, 1987 72, 1988 106, 1989 (8 months) 91, Total 385; actual force
    (deadly or less than deadly) 6, 7, 45, 31, 16, Total 105. Source PERF pp. 34 and 35. fn a: 82
    agencies; fn b: 31 agencies (L393-395). Same layout as Table 2 (pipe block L378-383 holds
    1985-1988; 1989 row L385, Total L387; column header flattened into one line L376). Sums checked.
- Lists:
  - Requester's 3 objectives (L7, L53, L183-185).
  - Agencies contacted (L55): BJS, CDC, CPSC + researchers + Toy Industry Association counsel.
  - DOJ components contacted (Enclosure I, L217-229): BJS, NIJ, FBI, ATF (4; last ATF L229).
  - CPSC three major databases (L93-97, L237-241): NEISS (98 hospitals, almost 700,000 cases/yr;
    301 toy-gun injury incidents Jan 2000-Jul 2003), Death Certificate System (no toy-gun deaths
    1993-2002), Incident Data Base (four cases of individuals fatally shot by police who mistook toy
    guns, 1993-2002) - last member L97/L241.
  - CDC 2001 NEISS review: 66 incidents = 62 aged 0-19 + 4 over 19; of the 62, 57 unintentional and 5
    reported as assaults; the 5 listed L111-119 (13-year-old, 12-year-old female, 12-year-old male,
    7-year-old, unspecified individual - last L119).
  - NVISS 12 sites (fn2 L125-127; repeated fn6 L267-269): 6 states (Connecticut, Kentucky, Maine,
    Maryland, Wisconsin, Utah); 5 metro areas/counties (Atlanta, Detroit, Miami-Dade County,
    Allegany County, San Francisco); 1 University of Pennsylvania pilot covering Bethlehem,
    Youngstown, Iowa City. 7 sites reviewed for 2001 (L123, fn7 L271): Connecticut, Maine,
    Wisconsin, Utah, San Francisco, Miami-Dade County, Allegany County (not reviewed: Kentucky,
    Maryland, Atlanta, Detroit, the Penn pilot).
  - Literature sources searched (3): Dialog, Nexis, Nexis' Statistical Universe (3 data files: ASI,
    SRI, IIS) (L189-199).
  - PERF imitation-gun categories (fn11 L325): toy guns, pneumatic guns (BB, pellet), replica guns;
    Tables 2 and 3 cover toy guns only.
  - PERF study population (L293): municipal and consolidated police departments serving 50,000+,
    sheriff's departments with 100+ sworn employees, all primary state police agencies; 27 site
    visits (fn10 L297).
  - Draft sent for comment to DOJ, HHS, CPSC (L145); copies planned to Attorney General, Secretary
    of HHS, Executive Director of CPSC (L161-163).
- Forecasts, guidance, deadlines, effective dates: Public Law 100-615 (Nov. 5, 1988) required a
  "blaze orange plug inserted in the barrel" and a BJS study (L279); BJS cooperative agreement with
  PERF effective June 1, 1989 (L279); PERF report June 1990 (L67, L279); BJS told GAO in June 2003
  it has no current plans for a follow-up study (L69, L287); NVDRS "not yet operational" (L121,
  L249); agency comments received September 17-25, 2003 (L145); distribution held until 30 days
  after issue date (L159). AAP policy statement 1987 (Mar. 1987, L131, fn3 L147); Brandeis study
  Oct. 1992, pp. 370-389 (L149-151, L261); Surgeon General report Jan. 2001 (L153, L273).
- Hedged claims: L61 "probably do not represent an accurate or comprehensive reporting" (hedge
  attaches to the database counts' accuracy); L61 "long-term effects that childhood play with toy
  guns may have" ("may" is inside the noun phrase, the finding "scant data exist" is unhedged); L73
  and L313 "may have resulted in either an under- or over-reporting" (officer recall); L99/L243
  CPSC officials: statistics "likely represent an undercounting"; L95 Death Certificate System "may
  record deaths involving toy guns not caused by a firearm" (database capability); L109 the 5
  incidents "apparently were reported to the police as being assaults"; L131 AAP quote "may
  inadvertently be drawn"; L137 Brandeis method "may have overstated the significance"; L139 study
  did not examine whether longer-term associations "are likely"; L311 PERF "may not be as robust as
  we initially hoped"; L362 PERF "it is conceivable ... the more likely crime is the 'simple
  assault'"; L397 PERF "it is probable that the data are more accurate" (attaches to the 105
  actual-force incidents).
- Rounded prose beside exact figures: response rate "66 percent" (L71) vs "65.5 percent (458
  responses)" (L293), 458/699; non-response "34 percent" (L71, L293); 148 agencies "32 percent", 121
  agencies "26 percent", 31 agencies "7 percent" of 458 (L75, L77, L87); "about 100" incidents
  reviewed (L93); "almost 700,000 cases each year" (L93); "over 800 databases" (L191).
- Notes: exclusion/negative facts: projectile toy guns excluded (BB, paintball, pellet) (L55,
  L189); Death Certificate System excludes firearm-related deaths (L95); 10,065 toy guns seized
  excludes stolen property (L79); PERF did not specify injuries/deaths among the 105 (L89); NEISS 301
  covers the broad toy-gun category, not only replicas (L93); CPSC review of about 100 incidents
  (victims 10+) found no police-mistook cases (L93); NVISS no search variable for toy guns (L121);
  no toy-gun deaths in 2001 NVISS data, none recalled for 2000 (L123, L129); no authoritative
  long-term study (L135); Surgeon General report did not consider toy guns (L141). No GAO
  recommendations in this document; agencies said the draft was accurate (L155).
- Operative definitions, rules and scope exceptions: scope "imitation or look-alike toy guns"
  excluding toy guns that fire projectiles (L55, L189); P.L. 100-615 plug requirement (L279); toy
  guns (intended for playing) vs pneumatic vs replica (fn11 L325).
- Amendments or contradictions: response rate 66 percent (L71) vs 65.5 percent (L293) - rounding of
  the same 458/699; body (L87) cites "table 3 in enc. II" for the 105 actual-force incidents.
- Coverage: FULL. Read L1-402 in one pass (ledger: 1-402 read; none remaining). Spot-check vs docs/
  original: Table 2 row "| 1987 | 665 | 601 |" (docs L339 = text L341), Table 3 "1989 (8 months) 91
  16" (docs L383), footnote "bBased on 121police agencies" (docs L352) all identical. Table 1 body
  absent in the original (source gap, not readable text left unread). Pages not applicable.

## D02 - National Flood Insurance Program: Oversight of Policy Issuance and Claims (GAO-05-532T)

- Source: text/D02.txt = docs/gaoreports_gao_05_532t.txt; task page Doc 2; 402 text lines; no pages.
- Written or submitted by: "United States Government Accountability Office" (L59); statement of
  William O. Jenkins, Jr., Director, Homeland Security and Justice Issues (L75; contact (202)
  512-8777, L309-311); Christopher Keisling, Assistant Director, Homeland Security and Justice
  ((404) 679-1917, L311); major contributors Christine Davis, Pawnee Davis, Deborah Knorr (L313).
- Type, date, edition: testimony before the Subcommittee on Housing and Community Opportunity,
  Committee on Financial Services, House of Representatives (L61-63); "For Release on Delivery
  Expected at 10:00 a.m. EDT ... Thursday, April 14, 2005" (L65-69); highlights page "April 2005"
  (L81); 14-APR-05 / 04/14/2005 (L5, L19); ACCNO A21682 (L15). Based on "preliminary results"
  of ongoing review mandated by the Flood Insurance Reform Act of 2004 (L105, L137).
- Period covered: Hurricane Isabel September 2003 (L7, L125); 2004 hurricane season beginning August
  2004 (L129); claims "as of March 2005" (L129); adjusters "as of April 2005" (L225); Appendix I
  payments 1972-2004 (data as of February 28, 2005, L339) and policies in force 1978-2004 (as of
  December 31, 2004, L369); "Calendar year" axes (L335, L365). No fiscal-year figures.
- Entities and aliases: NFIP = National Flood Insurance Program; FEMA = Federal Emergency Management
  Agency, "the administrator of the NFIP" (L7) / "administers the NFIP" (L121); DHS = Department of
  Homeland Security (fn1 L111: FEMA and its approximately 2,500 staff joined DHS in March 2003;
  FEMA's Federal Insurance and Mitigation Administration administers the NFIP, inside the Emergency
  Preparedness and Response Directorate); write-your-own (WYO) companies = 94 private insurers
  (L205); National Flood Insurance Fund (L205, L227); FEMA's "program contractor" (L135, L225,
  L235); "FEMA's director of claims"/"FEMA director of NFIP claims"/"NFIP claims director" (L181,
  L229, L237, L241, L243, L253); general adjusters / resident general adjusters (fn8 L237); state
  insurance commissions (L281-283); Senate Committee on Banking, Housing, and Urban Affairs (L131).
- Tables: none. Appendix I (L317-369) has two figures only: Figure 1 "Total NFIP Payments to
  Claimants, 1972-2004" (dollars in millions; y-axis labels 1,000-1,800; x-axis years printed
  1972-1976, 1977 ... 2003 though the title says 2004; Source NFIP; data as of February 28, 2005)
  and Figure 2 "Policies In Force, 1978-2004" (y-axis 0-5,000,000; x-axis to 2003; data as of
  December 31, 2004). Bar values are NOT in the text (chart images not reproduced) - unresolved.
- Lists:
  - Testimony objectives (3) (L9, L133).
  - Flood Insurance Reform Act mandates on FEMA (3): (1) insurance agent education and training
    requirements, (2) new processes for explaining coverage at purchase/renewal, (3) appeals process
    for dissatisfied claimants (L133, L149, L279); statutory cites P.L. 108-264 Sections 202-205, 207
    (fn5 L139), Sections 202-204 (fn12 L301), section 205 appeals (L299).
  - Coverage limitations examples (8 bullets, L161-179; last = detached garage L177-179): 80 percent
    of replacement cost / $250,000 / primary residence rule for actual cash value vs replacement cost
    (L161-165); optional personal property; deductible; basements (defined L171 "building areas below
    grade level on all sides"); $2,500 combined limit for jewelry, artwork, home business equipment,
    none in a basement (L173); actual cash value on furniture and personal property (L175).
  - Hypothetical adjustment (L181-199): home valued $60,000, insured $30,000, contractor estimate
    $40,000, personal property losses $10,000, payment $8,000; 5 reducing circumstances (no
    personal-property coverage; under 80 percent so actual cash value; $1,000 deductible; non-flood
    problems such as leaking pipes and preexisting mold; limited basement coverage - last bullet
    L195, finished at L199 after an interleaved heading at L197).
  - Ongoing work to be completed (4) (L137): MIS reliability; general-adjuster interviews (Maryland
    after Isabel, Florida 2004); monitoring observations; review of operational reviews.
  - Common reinspection errors (3) (L257-261; last = poor communication with homeowners).
  - Agent support offered (L213): training, hotline, rate quotes, Web sites.
  - Draft consumer materials (3) (L289-293): supplemental form; flood insurance handbook;
    acknowledgment form (last L293).
  - Informal appeal avenues (3) (L299): agent, adjuster's supervisor, hotline; "There is currently no
    official recourse."
- Forecasts, guidance, deadlines, effective dates: Flood Insurance Reform Act P.L. 108-264 enacted
  June 30, 2004 (fn2 L113, fn12 L301); FEMA's 6-month deadline "elapsed in December 2004" (L149) /
  "elapsed on December 30, 2004" (L279); FEMA "did not meet the 6-month timeframe" (L99); FEMA expects
  materials finalized "by October 2005" (L99, L295); FEMA official estimated full compliance "after
  October 2005" (L149); appeals process "would be after October 2005" (L305); GAO final report planned
  "later this year" (L137) and "in September 2005" (fn6 L151); projection "By 2005" approximately
  4.7 million policyholders, nearly 19,000 participating communities, $699 billion insurance in force
  (L123) / "expected to grow to about 4.7 million policies in 2005" (L203).
- Hedged claims: L89/L155 payments "may not cover/pay all of the costs" (hedge on payment adequacy);
  L149 FEMA official "estimated that it would be after October 2005"; L305 official "was uncertain
  when the process would be completed"; L277 FEMA: NFIP "is not necessarily more complex"; L211
  manager quote "some agents do not understand the program"; L225 adjuster community "stretched thin".
- Rounded prose beside exact figures: "about 40 FEMA employees", "about 170 contractor employees"
  (L91, L147, L203); "about $12 billion" claims since inception (L123); "about 23,770 claims for $454.2
  million" (Isabel, L127); "59,125 NFIP claims for more than $1.3 billion" (2004 hurricanes, as of
  March 2005, L129); "about 95 percent" WYO / "other 5 percent" (L205, fn7 L219); "about one-third"
  expense allowance (L205); "about 3.3 percent of the incurred loss" (L229); "about 10 general
  adjusters" (L233-235); "about 4 percent of the claims" reinspected (L253); 4,844 adjusters exact (L225).
- Notes: FEMA borrowed from Treasury three times in the last decade and repaid with interest (L121);
  NFIP self-supporting "for the average historical loss year" (L121); 90 percent of natural disasters
  involve flooding (L7, L107); max coverage $250,000 single-family / $100,000 contents (L109, L119);
  adjuster certification: 4 consecutive years full-time experience + workshop; yearly 1-day refresher
  and written exam (L223); unlike agents, adjusters have mandatory training (L93, L223); WYO
  operational review at least every 3 years, random sample of 100 files, follow-up in 6 months
  (L231-243); one company asked to withdraw once in program history, about 3 years ago (L243);
  3 of 4 WYO managers rated operational reviews effective, fourth no opinion (L245); 2 of 4 found
  problems on recently purchased policies (L245); adjuster fee $1,000 for a $25,000-$35,000 claim
  (L229); FEMA rejects that NFIP is "necessarily more complex" (L277). Interviewees: four WYO
  program managers + managers at one vendor (L135, L209). No GAO recommendations (work in progress).
- Operative definitions, rules and scope exceptions: "self-supporting for the average historical
  loss year" defined L121; actual cash value = "original cost of the structure less depreciation"
  (L161); replacement cost definition (L163); basement definition (L171); detached garage covered
  only if used solely for vehicles and storage (L177); 80 percent threshold (L161-163, L189).
- Amendments or contradictions: number of mandates needing rule making - L149 "the rule-making
  process required for two of the initiatives" with the third (coverage materials) "awaiting DHS
  approval", vs L279 and L295 stating that explaining coverage also requires rule making and
  Federal Register publication, and appeals requires formal rule making (all three described as
  rule making). "policyholders" (L123) vs "policies" (L203) for the 4.7 million 2005 projection.
  Closing addresses "Members of the Committee" (L307) though the hearing is a subcommittee (L61).
- Coverage: FULL. Read L1-402 in one pass (ledger: 1-402 read; none remaining). Spot-check vs docs/:
  fn7 (docs L217), L279 deadline sentence (docs L277), figure notes (docs L337, L367) identical.
  No tables (not applicable). Figure 1/2 bar values: visual-only, unresolved (no image in source).

## D03 - Alternative Mortgage Products: Impact on Defaults Remains Unclear, but Disclosure of Risks to Borrowers Could Be Improved (GAO-06-1112T)

- Source: text/D03.txt = docs/gaoreports_gao_06_1112t.txt; task page Doc 5; 292 text lines; no pages.
- Written or submitted by: "United States Government Accountability Office" (L83); statement of
  Orice M. Williams, Director Financial Markets and Community Investments (L95); key contributors
  (L211): Karen Tremba (Assistant Director), Tania Calhoun, Bethany Claus Widick, Stefanie Jonkman,
  Marc Molino, Robert Pollard, Barbara Roesmann, Steve Ruszczyk (8 names, last Ruszczyk).
- Type, date, edition: testimony before the Subcommittees on Housing and Transportation and Economic
  Policy, Committee on Banking, Housing, and Urban Affairs, U.S. Senate (L81, L269); delivered
  Wednesday, September 20, 2006, 10:00 a.m. EDT (L87-89; 20-SEP-06 L5; 09/20/2006 L21); ACCNO
  A61191 (L19); product code 250316 (L259). Summarizes "the report being released today" (L103),
  cited as GAO-06-1021 dated Sept. 19, 2006 (fn1 L251), requested by the Chairman of the Subcommittee
  on Housing and Transportation (L103). Highlights page placed at the END of the text (L263-289),
  dated September 20, 2006 (L271); a truncated table of contents at L59-75.
- Period covered: AMP growth "From 2003 through 2005" (L137, L283); "tripled over a 3-year period"
  (L111); 2005 securitization data (L137); disclosures provided 2004-2006 (L169); simulation of an
  April 2004 loan with actual rates 2004-2006 (L147, fn2 L253). Calendar years only.
- Entities and aliases: AMPs = alternative mortgage products (L7); ARMs = adjustable rate mortgages
  (interest-only ARMs, payment-option ARMs) (L101); federal banking regulators (5, L129): OCC
  (Office of the Comptroller of the Currency), Federal Reserve (Board of Governors of the Federal
  Reserve System; also "Federal Reserve Board" L123, L281), FDIC (Federal Deposit Insurance
  Corporation), NCUA (National Credit Union Administration), OTS (Office of Thrift Supervision);
  FTC (Federal Trade Commission) "is not a supervisory agency" (L131); SEC (Securities and Exchange
  Commission) Plain English Handbook (1998) (L175-177); Truth in Lending Act and Regulation Z (L131);
  CHARM booklet = Federal Reserve consumer handbook on ARM loans (L189); state banking and financial
  regulators; attorneys general (L133); "regulatory associations" (L199, unnamed).
- Tables: none. Figure 1 "Increase in Minimum Monthly Payments and Outstanding Loan Balance with an
  April 2004 $400,000 Payment-Option ARM, Assuming Rising Interest Rates" (L147) and Figure 2
  "Example of 2005 Interest-only ARM Disclosure Explaining How Monthly Payments Can Change" (L173):
  captions only, images not reproduced (visual content unresolved).
- Lists:
  - Testimony topics (5) (L105-107; last = selected state regulatory responses) vs the report's 4
    objectives in the abstract/highlights (L11-13, L277; federal and state responses combined).
  - Summary findings bullets (5) (L111-121).
  - Regions of AMP concentration: summary names California, Washington, Virginia, Maryland (L111);
    body names California (L137), East Coast Virginia, Maryland, New Jersey, Florida, Washington,
    D.C. (L139), and "Other examples" Washington, Nevada, Arizona (L139; last member).
  - Reasons borrowers may not understand AMPs (3) (L117).
  - Draft interagency guidance contents (L183): underwriting on fully indexed rates; written
    policies on portfolio limits, sales/securitization, risk management; consumer communications.
  - Agency-specific actions (L189): FDIC review program; NCUA informal contacts with largest credit
    unions; OTS review of its "68 most active AMP lenders"; OCC reviews of promotional materials;
    Federal Reserve Regulation Z review, summer 2006 hearings, CHARM booklet revision; FTC May 2006
    workshop and brochure (FTC last).
  - State sample: "the eight states in our sample" (L193) - the eight are NOT enumerated in this
    testimony; named states: Ohio, Nevada (L195), New Jersey and Nevada gathered data, New York plans
    to use association guidance (L199; New York last).
  - fn3 (L257) "Federally regulated financial institutions" = all banks and subsidiaries, bank
    holding companies and nonbank subsidiaries, savings associations and subsidiaries, savings and
    loan holding companies and subsidiaries, and credit unions (credit unions last).
- Forecasts, guidance, deadlines, effective dates: draft interagency guidance issued December 2005
  (L183, L289), not yet final ("When finalized" L183; regulators "are using these comments as they
  finalize" L185); Federal Reserve hearings summer of 2006 (L189); FTC workshop May 2006 (L189);
  report GAO-06-1021 Sept. 19, 2006 (fn1). Simulation (L145, fn2 L253-255): $400,000 payment-option
  ARM, 1 percent initial rate, 7.5 percent annual payment cap, 10 percent negative amortization cap;
  minimum payment $1,287 rising to $2,931 ("128 percent") at end of the 5-year option period / "in year
  six"; qualifying fully indexed rate 4.41 percent with first-year fully amortizing payment $2,039;
  shock "44 percent more" than the qualifying payment.
- Recommendations and responses: one recommendation to the Federal Reserve Board (Board of Governors)
  to consider requiring AMP-specific disclosure language as it reviews Regulation Z (L123, L201,
  L281). Response (L201, L281): Federal Reserve "will conduct consumer testing" and use design
  consultants to develop model disclosure forms; the text does not label it agree/disagree.
- Hedged claims: L113/L149 "Lenders may have increased risks to themselves and their customers" (hedge
  on the increased-risk claim itself); L115 "too early to determine"; L117 "may not fully understand
  their risks" and disclosures "may be hard to understand"; L145 "could see payments rise"; L149
  borrowers "may pose credit risks"; L153 "while underwriting trends may have loosened over time"
  (side clause; main claim "lenders have generally attempted to mitigate" unhedged); L153/L201 "too
  soon to tell"; L155 past experience "may not be a good indicator"; L163 advertising "may not clearly
  provide information"; L171 statement "may be sufficient for a traditional ARM ... may be more
  relevant for certain AMPs"; L185 guidance "might put ... at a competitive disadvantage", "might be
  difficult to enforce"; fn2 L253 lender "likely would have qualified the borrower" at 4.41 percent;
  L285 most banks "appeared to be managing their credit risk well"; L121 states collecting data "as a
  prelude to other possible actions".
- Rounded prose beside exact figures: "less than 10 percent ... to about 30 percent" (L137, L283) and
  "tripled"/"threefold" (L111, L137); "about 47 percent" interest-only vs "58 percent" payment-option
  ARMs originated in California (L137); "over 25 percent" market share of six lenders (L169); 128
  percent and 44 percent rounded from $1,287/$2,931/$2,039 (L145, fn2).
- Notes: contact phone for Orice M. Williams differs inside the document: (202) 512-5837 (L207) vs
  (202) 512-8678 (highlights L267). California contained "7 of the 20 highest-priced metropolitan real
  estate markets" (L137-139). Eight disclosures reviewed from six lenders (L169). Commenters said
  guidance would not apply to independent mortgage lenders or brokers (L185). Negative/exclusion:
  current Regulation Z/federal disclosure requirements do not require AMP-specific risk information
  (L117, L123, L159, L169, L287); FTC not a supervisory agency (L131); most AMPs from 2003-2005 had
  not reset (L153, L285).
- Operative definitions, rules and scope exceptions: credit risk defined (L129); risk-layering
  described (L113, L149); FTC enforcement scope over non-depository brokers and lenders (L131);
  Regulation Z applies to all mortgage lenders and brokers that close loans in their own names (L131);
  guidance scope = federally regulated financial institutions (L183, fn3 L257).
- Amendments or contradictions: two phone numbers for the same witness (L207 vs L267); 5 testimony
  topics vs 4 report objectives (L105-107 vs L11-13/L277).
- Coverage: FULL. Read L1-292 in one pass (ledger: 1-292 read; none remaining). Spot-check vs docs/:
  fn1 (docs L249), fn2 (docs L251), contact lines (docs L205, L265) identical. No tables (not
  applicable); Figures 1-2 captions only (unresolved images).

## D04 - OCC Consumer Assistance: Process Is Similar to That of Other Regulators but Could Be Improved by Enhanced Outreach (GAO-06-293)

- Source: text/D04.txt = docs/gaoreports_gao_06_293.txt; task page Doc 4; 456 text lines; no pages.
  Title line misspells "Comsumer" (L3, L5, L17); report headings say "OCC CONSUMER ASSISTANCE".
- Written or submitted by: GAO; letter signed David G. Wood, Director, Financial Markets and
  Community Investment (L391; phone (202) 512-8678 at L387 and L415, but (202) 512-6878 in the
  highlights L427). Key contributors (L417, 12 names): Katie Harris (Assistant Director), Nancy
  Eibeck, Jamila Jones, Landis Lindsey, James McDermott, Kristeen McLain, Suen-Yi Meng, Marc Molino,
  David Pittman, Barbara Roesmann, Paul Thompson, Mijo Vodopic. Product code (250226) (L419).
- Type, date, edition: report to the Subcommittee on Oversight and Investigations, Committee on
  Financial Services, House of Representatives (L57, L115); February 2006; letter dated February 23,
  2006 (L127; 23-FEB-06 L5) to Chairwoman Sue W. Kelly and Ranking Minority Member Luis V. Gutierrez
  (L129); ACCNO A47577 (L15). Highlights at the END (L421-453). Earlier companion report on the
  rulemaking process provided October 17, 2005 (L137); a separate later report on dual banking
  impact promised (L139, L173) - neither cited by GAO number here (footnotes absent).
- Period covered: complaint data calendar years 2000-2004 (L141, L397); audit work October 2004 -
  December 2005 (L141, L409); site visits March - August 2005 (L141). Fiscal vs calendar explicitly
  distinguished for timeliness (L267-269: OCC annual reports use fiscal-year data; GAO used calendar
  year data). OCC's fiscal-year end is NOT stated.
- Entities and aliases: OCC = (Treasury Department's) Office of the Comptroller of the Currency,
  supervisor of "national" banks (L131); Comptroller of the Currency; "former Comptroller" (L311,
  L365); CAG = Customer Assistance Group, Houston, Texas, part of OCC's Office of the Ombudsman,
  managed by the Deputy Ombudsman (L135, L175-177); CAGNet (L201); CAG Wizard (L279); REMEDY (OCC
  database, L397); Federal Reserve (Board of Governors + 12 Federal Reserve Banks, L133; database
  CAESAR); FDIC (database STARS); OTS (database CCS) (L397). The comparison set is FOUR federal bank
  regulators (OCC, Federal Reserve, FDIC, OTS; L133, L141, L185); NCUA is never mentioned (grep: no
  match). Preemption rules = "bank activities rule" (also "banking activities rule" L169) and
  "visitorial powers rule" (L131); National Bank Act (L135, L165); Federal Trade Commission Act (L135);
  GPRA = Government Performance and Results Act of 1993 (L213). NAAG = National Association of
  Attorneys General; CSBS = Conference of State Bank Supervisors (L315, L407); NAAG Consumer
  Protection Committee (L317); Better Business Bureaus (L299, L303); OCC Community and Consumer Law
  Division (L309, L347); Enforcement and Compliance division (L347); Community Affairs office (L305).
- Tables: none in text. Figure 1 "Consumer Complaint Processes of Selected Banking Regulators"
  (L199), Figure 2 "Complaint Resolutions of Selected Federal Regulators" (L227; note "Columns may
  not add to 100 due to rounding. Bars without numbers are less than 4 percent." L229), Figure 3
  "Number of Complaints Per Billion Dollars in Assets under Supervision of Selected Federal
  Regulators" (L261): captions only; values unresolved except those repeated in prose (below).
  "Contents"/"Figures" lists empty (L123-125).
- Lists:
  - Six complaint-processing steps (L187-197; last "notifies consumer of complaint's outcome").
  - Four resolution categories "in order of decreasing frequency" (L217-221; also L403): additional
    information; withdrawn/litigation; bank not in error; bank in error. Per-regulator order differs:
    withdrawn/litigation second for OCC, least common for Federal Reserve and OTS, third for FDIC
    (L241); not-in-error third for OCC, second for the others (L249); bank-error least common for OCC
    and FDIC, next-to-least for the other two (L253).
  - Referral shares 2000-2004 to another federal agency (L237): FDIC about 40 percent, Federal Reserve
    about 53 percent, OTS about 3 percent, OCC approximately 38 percent "of its callers"; text names
    only Federal Reserve, FDIC and OCC as referring "a considerable number".
  - Complaints per billion dollars of assets 2000-2004 (L257-259): OCC 10, FDIC 6, Federal Reserve 3,
    OTS 5.
  - Feedback mechanisms: Federal Reserve (mailed survey since mid-1980s) and FDIC (Web survey) have
    them; OCC and OTS do not (L209-211).
  - Recommendations to the Comptroller of the Currency (3) (L369-375; highlights L441): feedback
    mechanism; separate timeliness reporting for complaints vs inquiries; comprehensive outreach plan
    (last). Response: "concurred with our recommendations" (L151); "generally concurred with the
    report and agreed with our three recommendations" (L379); "OCC agreed with our conclusions and
    recommendations" (L443). Appendix II (OCC comment letter) is a heading only (L411) - text absent.
  - CAG constituent groups (3) (L177); OCC program areas (3): chartering, regulation, supervision
    (L157-159).
  - Site-visit states (4): California, Georgia, New York, North Carolina; telephone states Iowa and
    Idaho (L141, L407); work locations add Texas and Washington, D.C. (L141, L409). "three of the six
    state regulators with whom we spoke" have a 60-day goal (L327).
  - National consumer groups interviewed (5, L407): Center for Responsible Lending, Consumer
    Federation of America, National Community Reinvestment Coalition, National Consumer Law Center,
    Association of Community Organizations for Reform Now (last). FY2005 outreach meetings (3, L305):
    Consumer Federation of America, American Association of Retired Persons, National Association of
    Consumer Agency Administrators.
  - Source categories (4, L401): consumer, federal, state, other.
  - Hurricane Rita closure (L333): telephones unstaffed 4 days (September 2005); 14 faxes, 184 E-mails
    (34 bankers + 150 consumers); 16 of the consumer complaints from Members of Congress.
- Forecasts, guidance, deadlines, effective dates: preemption rules issued January 2004 (L7, L131) /
  January 13, 2004 (L167); MOU suggested July 2003 (L311), revised in 2004 (L317); one state official
  signed the 2003 MOU, none signed the 2004 version (L149, L321); November 2004 meeting with one state
  AG office (L303); no further meetings planned as of November 2005 (L303); brochures distributed as of
  November 2005 (L299); December 2005 OCC began seeking private-sector (third-party vendor) support to
  expand telephone hours (L335, L353), "from 7 to 12 hours a day" (L149, L453); expansion to begin
  after vendor selection and training (L355); phone line until 2004 "4 days a week, 8 hours a day",
  now 5 days (L349-351); 3-minute answer goal (80 percent of calls) met June 2004 - November 2005
  (L351-353); 2005 complaint data through June "indicate a potential increase" (L341).
- Hedged claims: L145/L359/L445 higher OCC volume "likely reflecting its position as the supervisor
  of banks that account for the majority of the nation's bank assets" (hedge on the explanation, the
  volume fact is unhedged); L257 "Likely reflecting the greater volume of bank assets"; L263 "it would
  appear that the volume ... is not out of proportion"; L173 "too soon to assess the practical effect
  of the rules"; L341 "potential increase", CAG officials "believe" the charter conversions account
  for it; L345 "data suggest that an increase ... could be absorbed", "might not have a dramatic
  effect" (also L149); L331 "might be disruptions"; L333 "may have resulted in some backlog"; L363
  "OCC appears to make appropriate use"; L365 "possibly contributing to the lack of trust", concerns
  "may inhibit", "could adversely affect", outreach "might help allay"; L293 advocates "may hesitate";
  L339 rules "could potentially increase the number of complaints".
- Rounded prose beside exact figures: timeliness (L269): 2003 annual report 87 percent vs GAO calendar
  2003 "about 66 percent"; 2004 annual report 74 percent vs GAO calendar 2004 "approximately 55
  percent"; target 80 percent within 60 calendar days in fiscal years 2003 and 2004 (L267-269); annual
  reports' closed totals 69,044 (2003) and 68,104 (2004) include inquiries (L271). Top-10 banks' share
  of 2004 complaints "about 81 percent" (L147) vs "81 percent" (L289). OCC-supervised assets
  "approximately 67 percent-about $5.8 trillion" as of March 2005; "more than 1,800 banks"; 14 of the
  top-20 (L155). CAG budget "more than doubled from $2.6 million to $5.4 million" 1999-2005; staff
  "about 40" since 1999 and 49 in 2005 (L177). Withdrawn/litigation share about 17 percent (2000) vs
  nearly 37 percent (2004) (L241) - distinct from the 37 percent decrease in complaints received
  2000-2004 (L341). Credit-card bank assets averaged $221 billion (OCC) vs $87 billion (other three)
  (L263). "close to 3,000 letters" on the banking activities rule (L297). "more than twice as many
  complaints as the other regulators combined" (L181) vs "more complaints ... than FDIC, OTS, and the
  Federal Reserve combined" (L257).
- Notes: CAG referrals data November 2001 - September 2005 from all 50 state banking departments and
  49 state attorneys' general offices (L297). OCC initial-response request 10 days; range 10-20 days
  across the four (L203). All four have 60-day resolution goals (L267). Withdrawn coding after 30 days
  (mid-2000 database change) and reopening policy after 60 days (L241). OCC guidance in 2000 on
  third-party vendors (L285-287). 18 closed cases reviewed (L395); examiners at six national banks
  (L405); data obtained September 2005 (L397). Complaint volume high around 2000 due to a settlement
  with a large national bank (L341). OTS's most common complaint product: home mortgage loans; credit
  cards for OCC, FDIC, Federal Reserve (L263). OCC: will address complaints regardless of transaction
  date (L301). Negative/exclusion: OCC won't require banks to display brochures, no public
  distribution plan (L299); state offices handle other complaint types (auto dealers, mortgage
  brokers, check cashers) (L339).
- Operative definitions, rules and scope exceptions: inquiries defined as "questions or comments
  subject to an immediate, simple answer" (L271, L361); formal acceptance requires signed form or
  letter (L201); no regulator addresses complaints already in litigation (L241); appeals treated as
  reopened complaints with original start date (L273); consumer compliance exams on a continuous
  3-year cycle (large banks) / at least every 36 months (small banks) (L163); safety-and-soundness
  exams of smaller banks once per 12- or 18-month period (L161); visitorial powers rule content (L169).
- Amendments or contradictions: OCC-reported vs GAO-computed timeliness (L269-271, explained by
  inclusion of inquiries; GAO says fiscal/calendar difference cannot entirely explain it); Wood's two
  phone numbers (L387/L415 vs L427); phone hours 8 per day until 2004 (L349-351) vs expansion "from 7"
  hours (L149, L453).
- Coverage: FULL for readable text. Read L1-200, L200-359, L360-456 (ledger complete; none remaining;
  the three lines over 1,900 characters - L141, L149, L297 - verified to end as read). MISSING IN
  SOURCE (not unread): all footnote bodies (letter markers 1-34, Appendix I markers 1-3); block quotes
  introduced at L313 ("saying,") and L319 ("Specifically, it states,"); Appendix II comment letter
  text; Figures 1-3 values. Spot-check vs docs/: figure note (docs L227), 69,044 (docs L269), "it
  states," (docs L317), 512-6878 (docs L425) identical. Pages not applicable.

## D05 - Insurance Sector Preparedness: Insurers Appear Prepared to Recover Critical Operations Following Potential Terrorist Attacks, but Some Issues Warrant Further Review (GAO-06-85)

- Source: text/D05.txt = docs/gaoreports_gao_06_85.txt; task page Doc 3; 398 text lines; no pages.
  Title variant inside the report: "Insurers Appear Prepared to Recover from Potential Terrorist
  Attacks, but Some Issues Warrant Further Review" (L57, L117) vs indexing/highlights title with
  "Recover Critical Operations Following" (L3, L17, L379).
- Written or submitted by: GAO; signed Orice M. Williams, Director, Financial Markets and Community
  Investment (L335; (202) 512-8678 at L331, L359, L371). Key contributors (L361, 7): Lawrence Cluff
  (Assistant Director), Emily Chalmers, Kirk Daubenspeck, Patrick Dugan, Marc Molino, Stephen
  Ruszczyk, Patrick Ward. Product code (250227) (L363).
- Type, date, edition: report to the Chairman (Michael G. Oxley), Committee on Financial Services,
  House of Representatives (L51, L125); November 2005; letter dated November 18, 2005 (L123; 18-NOV-05
  L5); ACCNO A41777 (L15). Highlights at the END (L365-395).
- Period covered: GAO work December 2004 through October 2005 (L139, L353); insurers selected on 2003
  total revenue (L139, L343); events referenced: 9/11 (2001), August 2004 DHS terror-target
  announcement (L129), Hurricane Katrina "in September 2005" (L233) / "in 2005" (L265); one insurer's
  2004 annual report (L193). Calendar years; no fiscal-year data.
- Entities and aliases: NAIC = National Association of Insurance Commissioners, "a body composed of
  state insurance regulators" that "does not regulate insurers" (L167); NAIC's Executive Vice
  President and Chief Executive Officer (comments, L159, L327); President of NAIC (copy, L329); NAIC
  Securities Valuation Office (L273-275); ISQ = NAIC's Information Systems Questionnaire (L289); DHS;
  Treasury (delegated coordinating role for banking and finance sector incl. insurance, L181); FBIIC
  = Financial and Banking Information Infrastructure Committee (NAIC a participating member, L183);
  FSSCC = Financial Services Sector Coordinating Council (American Insurance Association a member,
  L183); FEMA (continuity guidance used as criteria for state regulators, L261); FISCAM; National
  Institute of Standards and Technology; Department of Justice facility standards (L269); FFIEC =
  Federal Financial Institutions Examination Council (separate business-continuity handbook, L285);
  GLBA = Gramm-Leach-Bliley Act; Sarbanes-Oxley Act of 2002; HIPAA = Health Insurance Portability
  and Accountability Act of 1996 (L279, L283, L349); SAS 70 reports (L257). Insurers and states are
  deliberately unnamed (L139, L353).
- Tables: none. Figure 1 "Insurer's Mobile Operations Vehicle" (L235, photo) and Figure 2 "Insurer
  Recovery Time Objectives for Several Insurer Functions" (L243): captions only; Figure 2 values
  unresolved except those in prose (L237-241). Footnote markers 1-17 appear but NO footnote bodies
  exist in the source; Appendix II (NAIC comments) is a heading only (L355).
- Lists:
  - Objectives (3) (L7-9, L133-137, L339-341).
  - Sample: 18 large insurers = 5 health, 6 life, 7 property/casualty, in five states; 5 state
    insurance regulators; NAIC (L139, L343). Revenue coverage: life+health ~44 percent, P/C ~37
    percent of 2003 revenue of all such insurers (L343).
  - Three insurance-sector characteristics limiting spread (L143-145; L197 adds a fourth point on
    reinsurers, "Finally"): limited interdependencies; no single transaction point; geographic
    dispersion; reinsurer relationship financial not operational (last, L197).
  - Prior events (L199): 7 insurers reported no disruption from 9/11, power outages, hurricanes;
    post-9/11 changes: 13 plan for wider-scale disruptions, 5 increased physical security, 3 sped up
    improvements.
  - Backup arrangements (L233): 14 owned backup facility, 3 vendor-contracted, 1 combination; at least
    16 of 18 multi-site critical operations; at least 13 multiple call centers; at least 11 remote
    login; 4 mobile operations vehicles; 2 used them after Hurricane Katrina.
  - Recovery priorities and times (L237-241): all health insurers prioritize customer service, 4 of 5
    restore within 24 hours; all P/C and life prioritize investment management (all 6 life and 6 of 7
    P/C within 24 hours); claims processing top priority for 3 of 5 health, 3 of 7 P/C, 0 of 6 life;
    life claims within 24 hours: 2 (other 4 need 2 to 4 days); P/C claims within 24 hours: 3 (other 4
    within 2 or 3 days).
  - Intrusion attempts (L225): 1 "frequent", 6 "average", 4 "occasional" or "infrequent".
  - Testing (L253): 2 surprise recovery tests; 6 continuous/multiple daily data copying; 4 routing
    calls among call centers. Telecom: 3 insurers use redundant fiber-optic rings (L247).
  - Outsourcing (L257): all but one insurer outsource; about half outsource software development
    (most overseas); 4 outsource data-center backup; 3 outsource some claims processing; "slightly less
    than half" visit vendors on site.
  - State regulators (5): all back up critical data; one had no backup computer systems, one had no
    business continuity plans, one had neither (L151, L391) = three lacking other critical elements
    (L211, L305); body version: two lacked backup computer capabilities and two (including one of
    those) lacked plans for inaccessible primary offices (L263); "Three state insurance regulators had
    business continuity plans" (L261); only two of five aware of state guidance (L261); two set 2-day
    recovery objectives (L263); three use outside contractors for IS exam portions; three said they
    could retain expert staff (L297); only one had conducted audit work at a vendor facility (L155,
    L301, L395).
  - NAIC disruption: 16 of the 17 insurers that commented said no effect on normal operations (L207).
  - Need for quick recovery: 10 of 18 insurers said less than other financial market organizations
    (L221).
  - NAIC tests (3, L275): annual full plan test; quarterly backup power; annual backup-procedure audit.
  - Recommendations (3) (L157, L315-323, L385-387): (1) state regulators working through NAIC "as well
    as other appropriate state officials" ensure consistent continuity capabilities at state insurance
    regulators; (2) NAIC more frequent independent testing of information security; (3) state
    regulators working through NAIC consider changes on business continuity review placement/minimum
    recovery time objectives and on review of outsourcing (two sub-bullets, outsourcing last L323).
    Response: NAIC's Executive Vice President and CEO "generally agreed with our findings and
    recommendations" (L159, L327), citing actions including after Hurricane Katrina (L327).
  - Report copies (L329): Chair and Ranking Minority Member, Senate Committee on Banking, Housing, and
    Urban Affairs; Ranking Minority Member, House Committee on Financial Services; President of NAIC.
- Forecasts, guidance, deadlines, effective dates: NAIC has not had independent testing since 2002 and
  budgeted funds for independent testing in 2006 (L271, L305); one state established a business
  continuity policy "subsequent to our visit" (L261); state regulators' informal expectation of claims
  recovery "within 2 days" (L153, L393) / "within two days" (L285); NAIC recovery within 24 hours
  (L151, L211, L273); state exams every 3 to 5 years (L165, L203, L291); 2003 securities and banking
  regulators' guidance (same-business-day recovery) used as NAIC criteria (L269).
- Hedged claims: L3/L57 title "Insurers Appear Prepared"; L143 characteristics "would likely restrict"
  effects; L147/L187/L203 services "did not/do not appear to be highly time sensitive"; L187 effects
  "would likely be limited to that insurer's policyholders"; L197 "would likely mitigate"; L203 delay
  "would likely not have a significant negative effect"; L153 guidelines "may not reflect this
  concern", goals "would seem to not meet this expectation", "it is not clear whether" (outsourcing);
  L157/L305 "less likely"/"unlikely to lead to wider disruptions"; L285 review "may not result in
  business continuity getting the warranted attention"; L289 examiners "appeared to follow" NAIC
  guidelines; L291 "some information may become dated"; L295 workpapers "suggested" improvements;
  L301 "It is unclear whether" outsourcing examination is adequate; L305 NAIC "appeared well-prepared";
  L307 "may not fully reflect", "may limit"; L309 "may be sufficient in many cases", "it is unclear";
  L311 concerns "may not necessarily have resulted in lengthier disruptions". Unhedged: L271 "NAIC's
  information security efforts were reasonable".
- Rounded prose beside exact figures: "half of the insurers" (L153, L393) = "9 of the 18 insurers"
  with goals of 3 or more days (L285); "Most insurers ... within 1 day ... most other operations within
  3 days" (L151, L211, L237); "approximately 65 million policies" and "approximately 30,000 claims a
  day" (one insurer, 2004, L193); "about half" outsource software development (L257).
- Notes: no insurer had recovery objectives beyond 5 days for any critical system (L151); none aware of
  industrywide recovery objectives (L215); NAIC backup center workspace for six staff (L273); NAIC ran
  the Securities Valuation Office from its primary facility for 6 weeks after 9/11 (L275); reinsurers:
  a 1-week delay would not significantly affect an insurer (L197); critical securities organizations
  must recover within several hours, banks have plan criteria but no specific recovery times (L287);
  one regulator collects continuity information annually (L291); highlights say health insurers'
  priority "was customer service and claims processing" (L391) while the body gives claims processing
  as top priority for 3 of 5 health insurers (L237). Exclusion/negative: no state law in any of the
  five states requiring business continuity plans for agencies (L261); laws do not set recovery
  times (L153, L279, L283); GAO did not test controls by attempting entry (L351).
- Operative definitions, rules and scope exceptions: GLBA "financial institutions" defined to include
  most insurance providers (L283); Sarbanes-Oxley applies to public companies including insurers
  (L283); HIPAA directs HHS standards (L283); physical vs information security measures defined
  (L171); critical securities organizations defined (L287).
- Amendments or contradictions: none between documents inside D05; internal variants are the title
  wording and the per-regulator gap breakdown (L151/L263) noted above.
- Coverage: FULL for readable text. Read L1-170, L170-299, L299-398 (ledger complete; none
  remaining; L197, the only line over 2,000 characters, verified to end as read). MISSING IN SOURCE:
  footnote bodies 1-17, Appendix II NAIC letter, Figure 1-2 images. Spot-check vs docs/: L155 sentence
  (docs L153), Figure 2 caption (docs L241), "approximately 44 percent" (docs L341) identical.

## D06 - Bankruptcy Reform: Value of Credit Counseling Requirements Is Not Clear (GAO-07-778T)

- Source: text/D06.txt = docs/gaoreports_gao_07_778t.txt; task page Doc 6; 414 text lines; no pages.
  Title has "Requirements" (L3, L5, L15) but the cover, highlights and the underlying report use
  singular "Requirement" (L105, L123, L373). Encoding artifact "�" for an apostrophe at L167 and L321
  (present in the docs/ original too).
- Written or submitted by: GAO; statement of Yvonne D. Jones, Director, Financial Markets and
  Community Investment (L107-111; (202) 512-8678, L317, L365). Key contributors (L317-319, 5): Jason
  Bromberg, Anne A. Cangi, Emily R. Chalmers, Carl M. Ramirez, Omyra Ramsingh. Product code (250342).
- Type, date, edition: testimony before the Subcommittee on Commercial and Administrative Law,
  Committee on the Judiciary, House of Representatives (L91); Tuesday, May 1, 2007, 10:30 a.m. EDT
  (L99-101; 01-MAY-07 L5); ACCNO A68965 (L13). Based on report GAO-07-203, "Bankruptcy Reform: Value
  of Credit Counseling Requirement Is Not Clear" (Apr. 6, 2007) (fn2 L123), requested by members of
  the Senate and House Judiciary Committees (L117). Highlights at the end (L363-397); link list
  L399-413.
- Period covered: GAO review February 2006 - March 2007 in Washington, D.C., and Boston (L131);
  provider counts as of October 2005 and October 2006 (L135, L297-299); complaints October 2005 -
  October 2006 (L193); IRS status as of March 2007 (L197-199); session-mode data for certificates
  issued July 11 - October 17, 2006 (L221, L255); NFCC survey October 2005 - August 2006 (fn16 L227).
  Calendar dates only.
- Entities and aliases: Bankruptcy Act = Bankruptcy Abuse Prevention and Consumer Protection Act of
  2005, Pub. L. No. 109-8, 119 Stat. 23 (fn1 L121), "BAPCPA" in the NFCC report title (fn26 L283);
  Trustee Program = Department of Justice's U.S. Trustee Program = U.S. Trustees + Executive Office for
  U.S. Trustees (L119, fn4 L129); Credit Counseling and Debtor Education Unit (est. June 2005, L171);
  IRS = Internal Revenue Service (Credit Counseling Compliance Project, began October 2003, L197); FTC
  (enforcement actions against several agencies, L159); NFCC = National Foundation for Credit
  Counseling (fn16, fn26, L271); Financial Literacy and Education Commission (fn20, L235);
  Administrative Office of the U.S. Courts (L249-251); bankruptcy administrators (Alabama, North
  Carolina, fn5 L161); panel trustees (Chapter 7) and standing trustees (Chapter 13) (fn17 L229);
  House Judiciary Committee report H.R. Rep. No. 109-31 (fn18-19). "provider" = Trustee-approved
  provider (fn4 L129); "credit counseling requirement" and "debtor education requirement" defined (fn3
  L127).
- Tables: none (no figures either).
- Lists:
  - Testimony topics (4) (L7, L131, L375).
  - Recommendations to the Trustee Program (2): (1) track and analyze outcomes of prefiling credit
    counseling (L143, L249-251); (2) issue formal guidance on what constitutes "ability to pay" (L145,
    L293). Responses: "concurred" (L143, L145, L251), "agreed with our recommendation and said it will
    promulgate formal fee waiver guidance in a rulemaking later this year" (L293); highlights "The
    Trustee Program agreed with GAO's recommendations" (L383).
  - Credit counseling statutory elements (L155): briefing on credit counseling opportunities +
    budget analysis assistance, within 180 days before filing; exigent-circumstance waiver.
  - Credit counseling approval criteria examples (L169): nonprofit, independent board, full
    disclosures, trained counselors.
  - Debtor education topics (4) (L255): budget development, money management, wise use of credit,
    consumer information (last).
  - Session delivery modes (certificates July 11 - October 17, 2006): counseling 45 percent telephone,
    43 percent Internet, 13 percent in person (sum 101; fn15 "does not add up to 100 due to rounding",
    L221-225); education 50 percent Internet, 29 percent telephone, 21 percent in person (L255).
  - Three largest providers' fee waiver criteria (L289): at/below 150 percent of poverty line; at/below
    120 percent; free legal aid or disability income. Waiver rates: counseling 4, 15, 26 percent;
    education 6, 21, 34 percent.
  - Unfair-practice complaint examples (L195): legal advice, discouraging filing, not informing about
    fee waiver.
  - Prior GAO products cited (fn22 L257-259; fn25 L275-281; link list L403-413): GAO-07-203 (Apr. 6,
    2007), GAO-06-67 (Oct. 28, 2005), GAO-04-38 (Mar. 10, 2004), GAO/T-GGD-97-43 (Feb. 12, 1997),
    GAO-07-100 (Dec. 4, 2006), GAO-05-93SP (Nov. 15, 2004, last). None is another bundle document.
- Forecasts, guidance, deadlines, effective dates: Act signed April 20, 2005; most provisions effective
  October 17, 2005 (L153); counseling requirement "became effective in October 2005" (L119); Trustee
  Program unit established June 2005 (L171); interim final rule July 2006 (L135, L169; "July 2006 rule"
  in highlights L385), 71 Fed. Reg. 38076-38085 (2006), to be codified at 28 C.F.R. 58.15 and 58.25
  (fn9 L175-179); fee-waiver policy disclosure required as of July 2006 (L273); OMB forms 1105-0084 and
  1105-0085 "Exp. 12/31/2005" (fn10 L181-183); IRS project began October 2003 (L197); fee waiver
  rulemaking promised "later this year" (L293); Trustee Program "considering issuing a rule" on ability
  to pay, no final decision (L291); web site eventually to allow full language search (L307).
- Hedged claims: L139/L209 very few clients "appeared"/"appear" to be entering debt management plans;
  L141/L391 "anecdotal evidence suggests" dire situations and the requirement "may often serve more as
  an administrative obstacle"; L145/L393 "Evidence suggests fees are being waived as appropriate";
  L147/L395 supply "appears (to be) sufficient"; L197 IRS: revoked organizations "appeared to be
  motivated mostly by profit"; L221 in-person counseling "may have advantages"; L235 "it is unclear
  whether the credit counseling requirement is achieving its intended purpose", timing "could mitigate
  its value", requirement "may not be serving its purpose"; fn21 L247 early filers "may therefore not
  be representative"; L265 observers believed course "was likely to help improve" literacy; L301
  "existing data suggests" in-person access for most, clients "appear to prefer" phone/Internet; L305
  requirement "may create hardship"; L309 unrepresented filers "have reportedly attempted to file".
- Rounded prose beside exact figures: providers approved: 71 counseling / 76 education when the Act
  took effect October 2005 vs 153 / 268 by October 2006 (L135, L189, L297-299, L385); about 94 percent
  of the 153 had 501(c)(3) status; at least one-third of the 268 (L189); "Three large nationwide
  organizations represent about half of the market" (L147) / "three large nationwide companies have
  provided about half of the sessions" (L189); "about a dozen" nationwide providers (L299); fees "about
  $50 or less per session" (L145) / "around $50" (L269) / "about $50 per session" (highlights L393);
  NFCC survey of 107 providers (L271); 124 complaints out of "more than 930,000 certificates" (Oct
  2005 - Oct 2006, L193), 20 alleging unfair practices (L195); five formal complaints alleging harmful
  recommendations out of "more than 650,000 credit counseling certificates" (as of October 2006, L223);
  debt-management-plan entry "fewer than 2 percent" (L223) vs NFCC survey "about 3 percent" of
  October 2005 - August 2006 sign-ups (fn16 L227, described as corroborating); 15 counseling providers
  representing "more than two-thirds of certificates" (L219); 17 education providers reviewed (L255);
  43-provider case file sample and 10 providers interviewed (L131); IRS completed 47 examinations, all
  ending in revocation, proposed revocation or other termination (as of March 2007, L197); four
  approved providers under IRS examination (L137, L201, L385); 8 of the 22 comments on the interim
  final rule asked for ability-to-pay guidance (L291); at least 29 languages (L307).
- Notes: 94 judicial districts (L153); Alabama and North Carolina outside the Trustee Program (fn5);
  Chapter 13 plans usually 3 to 5 years (fn7); nonprofit status is a state-law concept and 501(c)(3)
  not required (fn8 L173); fn14 cites "11 U.D.C. S 109(h)(1)" (typo in source; fn6 has 11 U.S.C. S
  109(h)); no complaint led to removal of a provider (L195); no state/federal enforcement action
  against approved providers (L191); applicants sometimes rejected for inadequate fee waiver policies
  (L273); no party tracks how many counseled consumers later file (L249). Exclusion facts: neither the
  statute nor guidance defines "ability to pay" (L145, L291); Trustee Program does not cover Alabama
  and North Carolina (fn5).
- Operative definitions, rules and scope exceptions: "debtor" eligibility rule with 180-day window and
  exigent-circumstance exception (L155); Chapter 7 / Chapter 13 definitions (fn7); debt management
  plans defined (fn11 L185); 501(c)(3) qualification (fn12 L203); statutory description of counseling
  (L213) and education (L255, 11 U.S.C. S 111(d)(1)(C)); fees must be reasonable and services provided
  regardless of ability to pay (L269).
- Amendments or contradictions: "fewer than 2 percent" vs NFCC "about 3 percent" (L223 vs fn16);
  fee wording variants; title singular/plural variants. Interim final rule (July 2006) formalized the
  application process set by the Act (L135, L169).
- Coverage: FULL. Read L1-180, L180-359, L359-414 (ledger complete; none remaining). Spot-check vs
  docs/: fn15 (docs L223), fn16 (docs L225), "11 U.D.C." (docs L215), the "�" heading (docs L165)
  identical. No tables/figures (not applicable).

## D07 - Long-Term Care Insurance: State Oversight of Rate Setting and Claims Settlement Practices (GAO-08-1016T)

- Source: text/D07.txt = docs/gaoreports_gao_08_1016t.txt; task page Doc 9; 852 text lines; no pages.
  GAO "accessible" text format: footnotes numbered consecutively at the end (L731-783), table and
  figure data written out as text (L83). Encoding artifacts "�" for apostrophes (L119-131) and "��"
  for the section sign in fn6 (L743).
- Written or submitted by: GAO; statement of John E. Dicken, Director, Health Care (L105-107;
  (202) 512-7114, L133, L727). Key contributors (L727): Kristi Peterson (Assistant Director), Krister
  Friday, Rachel Moskowitz. Congressional Relations Ralph Dawn; Public Affairs Chuck Young (L829-843).
- Type, date, edition: testimony before the Subcommittee on Oversight and Investigations, Committee on
  Energy and Commerce, House of Representatives (L89, L113); Thursday, July 24, 2008, 10:00 a.m. EDT
  (L97-99; 24-JUL-08 L5); ACCNO A83045 (L15). Based on the June 2008 report GAO-08-712 "Long-Term Care
  Insurance: Oversight of Rate Setting and Claims Settlement Practices" (L9, L119, L141), dated June
  30, 2008 (fn2 L735; "draft of GAO's report issued on June 30, 2008" L131, L151). Highlights placed
  at the START (L111-135). No recommendations: "The draft reported differences in states' oversight
  without making any conclusions or recommendations" (L131, L151).
- Period covered: GAO work September 2007 - June 2008 (L143); Table 2 state-law review September 2007 -
  May 2008 (L705); rate-increase data 1990 through 2006 from the California Department of Insurance
  (L143); Figure 1 covers 2003 through 2006 (L229); market shares "in 2006" (L143, L219, fn4); status
  "as of 2006" / "as of December 2006" (L123, L147, L209); enforcement "As of March 2008" (L717);
  complaints 2007 (L715, fn22). Calendar years.
- Entities and aliases: LTCI = long-term care insurance (L7); NAIC = National Association of Insurance
  Commissioners (model LTCI act 1986 and model regulation, fn1 L733; "member states" comments L131;
  member-state group formed March 2008 L719); ADL = activities of daily living (L155); HIPAA = Health
  Insurance Portability and Accountability Act of 1996, Pub. L. No. 104-191 (L167, fn6); IRS
  (Department of the Treasury; 1998 regulations, L167); CMS = Centers for Medicare & Medicaid
  Services; OPM = Office of Personnel Management (L143); California Department of Insurance (L143,
  L605, L611); Massachusetts Division of Insurance (L611); Henry J. Kaiser Family Foundation (fn5);
  Lewin Group 2002 report (fn19 L773); Medicaid (L139, L141).
- Tables:
  - Table 1 "Selected Rate Setting Standards Added to NAIC's LTCI Model Regulation in 2000" (L185-207),
    five standards (Standard / Description / Purpose): actuarial certification ("moderately adverse
    conditions"; four states' regulators; one company: initial premiums up 11 percent); higher loss
    ratio for increases (58 percent of original-premium revenue, 85 percent of the increase; two
    states' regulators); enhanced reporting for at least 3 years after an increase; disclosure at
    application of all increases in any state for the preceding 10 years; protections if lapse within
    120 days (last). Note [A] (L205): old standard 60 percent claims / up to 40 percent expenses and
    profit; new standard 15 percent of the increase for expenses and profit. Source line L203.
  - Table 2 "Claims Settlement Standards in Place in the 10 States in GAO's Review" (L623-711), nine
    rows with Number of states / Included in NAIC LTCI models ([Check] or [Empty]) / variation:
    timely communication 10[A], Empty, 10 or 15 days, 5 states undefined; affirm or deny within
    reasonable time 10[A], Empty, 15-40 days, 6 undefined; timely investigation 9[A], Empty, 15 or 30
    days, 5 undefined; timely payment 9[A], Empty, 5-45 days, 2 undefined; claims forms 9[A], Empty, 10
    or 15 days, 1 unspecified; written explanation of denial 8[A], Check, 40-60 days, 2 undefined;
    written explanation of delay 8 (no [A]), Empty, 15-45 days; licensed/certified professional
    assessment 10, Check, no significant variation; appeals process description in policy 9, Check,
    no significant variation (last row L697-703). Note [A] (L709): explicit in some states, part of
    the unfair claims settlement definition in others; note L707: not comprehensive.
  - Figure 1 "Outcome of One Company's Request for a Premium Rate Increase in 46 States from 2003
    through 2006" (L229-609), written out per state (year 1 / year 2 / total, percent): CT 0/0/0; DC
    0/0/0; NJ 15/0/15; NY 15/0/15; GA 14/6/20; OK 15/15/30; OR 30/0/30; DE 15/20/35; ME 35/0/35; MD
    20/15/35; TX 35/0/35; KS 20/20/40; IA 40/0/40; CA 25/20/45; AR 25/25/50; MN 30/20/50; ND 30/20/50;
    then 50/0/50 for AL, AK, AZ, CO, HI, ID, IL, KY, LA, MA, MI, MO, NE, NV, NH, NM, NC, OH, PA, RI, SC,
    SD, TN, UT, VT, VA, WA, WV, WI (last, L597-603). 46 entries counted; 2 not approved, 12 partial
    (15-45), 32 full; among full approvals only AR, MN, ND show a year-2 amount. Formatting slips: MI
    total "50." (L459), MO year 1 "50;" (L463). Note L607: Connecticut and DC did not approve. Source:
    California Department of Insurance data (L605).
- Lists:
  - 10 case-study states (fn4 L739): California, Florida, Illinois, Iowa, New York, North Dakota,
    Pennsylvania, Texas, Washington, Wisconsin (last); chosen to cover at least 40 percent of active
    LTCI policies in 2006; findings not generalizable.
  - Federal agencies interviewed (3, L143): IRS, CMS, OPM.
  - Benefit triggers (2, L155); ADL examples bathing, dressing, eating.
  - Two NAIC-identified weaknesses of the loss ratio standard (L181).
  - Company rate-increase histories (L221-223): 30-year seller, increases since 1995 mostly 30-50
    percent; mid-1980s entrant, increases since 1991, one policy totaling 70 percent; seller since
    1975, first increase as of February 2008 of 8 to 12 percent (nearly a half million consumers,
    fn16); another company with only one increase.
- Forecasts, guidance, deadlines, effective dates: NAIC model regulation changes in 2000 (L173, L183);
  NAIC estimate of adoption "Since 2000 ... more than half" (L123, L173, L179) / "by 2006 more than
  half" (L147, L209; fn12: based on NAIC review completed in 2006); HIPAA standards tied to NAIC model
  act and regulation "in effect as of January 1993" (L167); IRS regulations 1998 (L167); NAIC group
  formed March 2008 (L719); regulators expect complaints to increase (L715); "might be as much as a
  decade" before effectiveness can be assessed (L211).
- Hedged claims: summary states "some consumers remain more likely to experience rate increases"
  unhedged (L123, L145, L147, L173) while the body says "may remain more likely" (L175, heading L215,
  L217); "consumers may face more risk of a rate increase depending on..." (L125, L147, L175); L7/L117
  demand "is likely to grow and could strain", LTCI "may be a way of reducing"; L9/L117/L141 denials
  "may leave consumers without LTCI coverage"; L131/L151 member states said the report "seemed to
  critique"; L139 "will likely strain"; L149/L621 variation "may leave consumers in some states less
  protected"; L161 companies "lacked and may continue to lack sufficient data"; L183 standards "may
  result in higher, but more stable, premium rates" (several state regulators); L195 "could act as a
  disincentive"; L199 disclosure standard "may discourage companies"; L209 policies "were likely to have
  been issued before"; L211 assumptions "may eventually require revision"; L219 likelihood "also may
  depend on the company"; L225/L227 consumers in some states "may be more likely", "may raise equity
  concerns"; L613 variation "may have significant implications", "may continue"; L129/L149/L719 an
  independent review "may be useful"; L719 "some evidence to suggest" companies frequently overturn
  denials; fn15 phase-in "may not provide a net financial benefit"; fn18 one reason "may be" capacity;
  fn23 states "may not have taken enforcement actions" because of several factors.
- Rounded prose beside exact figures: "About $193 billion" long-term care spending in 2004; "less than
  10 percent" private insurance; elderly "about two-thirds" of services (L139); "about 9 million"
  policies sold as of end of 2002 (L155); 90 percent tax qualified in 2002 (L169); "at least 30 percent
  of policies in force" issued in non-adopting states as of December 2006 (L209); six companies = 40
  percent of the 2006 market (L143) vs four companies = 36 percent of the 2006 market (L219); "over 30
  increases" since 1995, variation in 18 of 20 requests over 15 percent (L227); 46-state example: "over
  one quarter (14 states)" = 2 not approved + 12 less than 50 (range 15-45), 32 full, "at least 4" of the
  32 phased in over 2 years (L227) - Figure 1 shows year-2 amounts for only AR, MN, ND among the full
  approvals and shows MA 50/0, while L611 says Massachusetts required phase-in "not exceeding 20
  percent in any one year"; $2,000 premium illustration: +$1,000 Colorado, +$300 New York, level in
  Connecticut (L613); one state 54 LTCI complaints in 2007, 20 on claims settlement (L715); five states'
  data: 44 percent of complaints on claims settlement in 2007 (fn22); denials overturned on appeal
  average 20 percent in 2006, range 7-34 percent (four companies, L719-721).
- Notes: state counts in the 10-state review: complaint data from 6 states (L143) vs fn22 "five states
  that provided LTCI complaint data from 2001 through 2007"; 4 states regularly review complaint
  trends (3 within broader market analyses), 3 cite small complaint numbers (L715); as of March 2008, 4
  of 10 reported enforcement actions and 7 ongoing examinations (L717); 6 of 10 considering additional
  claims protections (L129, L149, L719); 3 states lack authority over factual disputes (L719); rate
  setting: 3 states data-reliability standards, 2 states limits on increases, all 10 reduce or phase
  in, 6 say increases can be necessary for solvency (L213); 7 states say increases mainly hit older
  policies, 5 blame pricing assumptions (L217); 1 state lacks a timely-payment standard (L621); federal
  tax-qualified rules do not address timely claims handling (L621); Louisiana had notice-only filing
  for part of the period and four other states required no filing per Lewin Group 2002 (fn19); for
  increases of 15 percent and below almost all states approved in full (fn20).
- Operative definitions, rules and scope exceptions: elimination period (L157); tax-qualified policy
  under HIPAA = substantial assistance with at least two of six ADLs for at least 90 days, or severe
  cognitive impairment (L167); fn8 tax-qualified if state law same or more stringent; loss ratio
  standard (pre-2000 at least 60 percent, fn9 L751); rate stability defined (fn10 L753); rate setting
  and claims settlement practices defined (fn3 L737); class-wide increases allowed, individual
  increases not (L161); going-forward adoption leaves pre-implementation policies under the loss
  ratio (fn13 L759); premiums "designed--though not guaranteed--to remain level" (L161).
- Amendments or contradictions: NAIC model revised in 2000 replacing the single loss-ratio standard
  with more comprehensive standards (L173-183); Massachusetts phase-in statement vs Figure 1 row
  (L611 vs L445-451); hedge variation noted above.
- Coverage: FULL. Read L1-170, L170-339, L340-599, L600-849, L849-852 (ledger complete; none
  remaining). Spot-check vs docs/: Table 2 "Number of states: 8;" (docs L677), Figure 1 MI/MO rows
  (docs L457, L461), fn20 (docs L773) identical. Figure 1 image itself not in text, but its data are
  fully written out.

## D08 - Fair Lending: Race and Gender Data Are Limited for Nonmortgage Lending (GAO-08-1023T)

- Source: text/D08.txt = docs/gaoreports_gao_08_1023t.txt; task page Doc 8; 380 text lines; no pages.
  Accessible format (footnotes at end, L273-311). Encoding artifacts "�" for apostrophes (L111-125)
  and section signs (fn1 L275-277, fn4 L283).
- Written or submitted by: GAO; statement of Orice M. Williams, Director Financial Markets and
  Community Investment (L101; (202) 512-8678, L129, L267-269). Key contributors (L269, 10): Wesley M.
  Phillips (Assistant Director), Benjamin Bolitzer, Emily Chalmers, Kimberly Cutright, John
  Forrester, Simin Ho, Omyra Ramsingh, Robert Pollard, Carl Ramirez, Ethan Wozniak. Congressional
  Relations Ralph Dawn; Public Affairs Chuck Young (L357-369).
- Type, date, edition: testimony before the Subcommittee on Oversight and Investigations, Committee on
  Financial Services, House of Representatives (L85, L107); Thursday, July 17, 2008, 10:00 a.m. EDT
  (L93-95; 17-JUL-08 L5); ACCNO A82913 (L15). Based on report GAO-08-698 (June 27, 2008) (L9, L113,
  fn2 L279), "our June 2008 report" (L141). Highlights at the START (L105-131). No GAO recommendation
  stated; "FRB did not take a position on this report's analysis" (L9, L115, L159).
- Period covered: audit work September 2007 - June 2008, Washington, D.C. (L149); regulatory history
  1974 (ECOA), 1975 (prohibition), 1999 (proposal), 2003 (decision), 2002 (HMDA pricing data), SSBF
  1987-2003, discontinued 2007, SCF elements from 2010 (L137-173). Calendar years.
- Entities and aliases: FRB = Federal Reserve Board (L7); "Federal Reserve Bank" (one comment letter in
  1999, L211) distinct from FRB; Regulation B implements ECOA = Equal Credit Opportunity Act of 1974
  (L7, fn1: Pub. L. No. 90-321 title VII as added by Pub. L. No. 93-495, Oct. 28, 1974); HMDA = Home
  Mortgage Disclosure Act of 1975, amended 1989 (L139, L167; fn4 Pub. L. No. 94-200, Dec. 31, 1975);
  SSBF = FRB's Survey of Small Business Finances (L173); SCF = Survey of Consumer Finances (about 4,500
  consumers, L199); five federal regulators enforcing ECOA for depository institutions: FRB, OCC,
  FDIC, OTS, NCUA (L171); four agencies GAO contacted: FRB, OCC, FDIC, OTS (L207; NCUA not among
  them); fn5 L285 other ECOA enforcers for nondepository institutions: Securities and Exchange
  Commission, Small Business Administration, Farm Credit Administration, with the Federal Trade
  Commission as residual enforcer; Interagency Fair Lending Examination Procedures (L209).
- Tables: none; no figures.
- Lists:
  - Testimony topics (3) (L9, L113, L141).
  - FRB's two reasons for not adopting the 1999 amendment (L123-125, L139): (1) opportunity for
    discriminatory use; (2) data not useful/reliable (inconsistent collection).
  - SSBF limitations (3 bullets, L187-191): borrower-collected; self-reported/unverified; about every 5
    years (most studies use 1993 and 1998 surveys, data about 10 years old) - last L191.
  - Studies: all eight minority-business-lending studies (seven of the eight specifically on
    African-American-owned businesses) (L183); one auto-lending study (SCF, L199); two credit-card
    studies with mixed results (L201-203); some studies found no significant disadvantage for
    women-owned businesses (L183).
  - Examiner surrogates (3, L209): Hispanic by last name, female by first name, African-American by
    census tract.
  - Reporting-requirement cost items (L127, L157, L245): information system integration, software
    development, data storage and verification, employee training.
  - Options considered (L157, L253-259): limit to certain loan types (small business and/or
    automobile); collect-and-provide-to-regulators without public reporting (last).
  - Cited studies in footnotes 7-11 (L289-305): Holloway and Wyly 2001; Avery, Brevoort and Canner
    2007; Munnell et al. 1996; Bocian, Ernst and Li 2008; Brevoort and Canner 2007; Getter 2006; Ayres
    and Siegelman 1995; Ayres 1991; Hazembuller, Lombardi and Hogarth 2007 (last).
- Forecasts, guidance, deadlines, effective dates: 1975 FRB general prohibition (L137); 1999 FRB
  proposal (L139); 2003 decision to keep the prohibition after "more than 600 public comment letters"
  (L139) and 2003 expansion of the self-test exception (L163); HMDA amended 1989 (L167); 2002 pricing-
  data requirement (L169); SSBF about every 5 years 1987-2003, discontinued 2007, elements to be added
  to the SCF "starting in 2010" (L173, L261); FRB cost to process the 2008 HMDA data approximately $3.5
  million (fn13 L309); GAO "plan to further explore" fair lending enforcement in future work (L211).
- Hedged claims: L119/L151 "most research/studies suggest that discrimination may play a role" (hedge
  on discrimination's role); L177 studies "suggested that certain minority-owned businesses may be
  denied loans more often"; but L183 "all eight studies ... generally found that lenders denied loans
  ... significantly more often" (stated as a finding); L119/L209 examiners "may rely on
  time-consuming and possibly unreliable techniques"; L125 voluntary data "would not likely materially
  benefit"; L155 lenders "would likely adopt different approaches", "relatively few, if any, lenders
  would likely choose to collect"; L153/L179/L205 data limitations "may also impede" exam efficiency;
  L195 underwriting variables "may account for many apparent discrepancies" (some argue); L199 "racial
  discrimination could play a role" (auto study); L203 minorities "were likely to pay higher interest
  rates" (one credit-card study's finding); L211 oversight "may be less efficient"; L213/L215 benefits
  "would likely be limited"; L235 data "would likely be skewed"; L261 "It is also not yet clear how
  FRB's decision ... will impact", "now may be the time to consider".
- Rounded prose beside exact figures: "more than 600" comment letters, random sample of 90 analyzed
  (L139, L145-147); "about 4,500" SCF consumers (L199); SSBF "about every 5 years" (L173, L191); data
  "about 10 years old" (L191); "approximately $3.5 million" (fn13).
- Notes: self-test results are privileged (L163); very few if any lenders conduct self-tests (L233);
  no evidence lenders used HMDA data for discrimination (L225); FRB's 1999 proposal did not require
  public reporting (fn12 L307); HMDA criticized for lacking credit scores and loan-to-value ratios
  (L195, fn3); credit card applications typically by mail or Internet (L255). Exclusion facts:
  Regulation B prohibits collection for nonmortgage loans except limited circumstances such as
  self-tests (L163-165); NCUA not among agencies contacted (L207).
- Operative definitions, rules and scope exceptions: self-test defined (L163); ECOA protected
  characteristics: race, gender, color, religion, national origin, marital status, age (L135); HMDA
  requires collection and public reporting for mortgage applicants (L167).
- Amendments or contradictions: FRB proposed (1999) an amendment it did not adopt (2003) (L139);
  footnote citation of the same 2007 Journal of Real Estate Research article lists Avery, Brevoort and
  Canner in fn7 (L293) but only Brevoort and Canner in fn8 (L297-299); L235 "other researchers and
  researchers" (source wording).
- Coverage: FULL. Read L1-200, L200-380 (ledger complete; none remaining). Spot-check vs docs/: "random
  sample of 90" (docs L143), fn5 (docs L283), fn13 (docs L307) identical. No tables/figures (not
  applicable).

## D09 - National Flood Insurance Program: Greater Transparency and Oversight of Wind and Flood Damage Determinations Are Needed (GAO-08-28)

- Source: text/D09.txt = docs/gaoreports_gao_08_28.txt; task page Doc 7; 590 text lines; no pages
  (printed page numbers only in the contents list L119-141: Letter 1, Results in Brief 2, Background 6,
  Conclusions 25, Matters/Recommendation/Agency Comments 27, Appendix I 30, II 32, III 35; Figure 1
  p. 8, Figure 2 p. 15). Layout duplication: the opening letter paragraph is printed twice (L169 and
  again inside L171, which also repeats its last sentence) and L173 repeats a sentence fragment
  ("Evidence at the damage scenes was often limited or The unprecedented scope...") - repeated text,
  not differing facts. Footnote 1 marker appears as "^11" (L169).
- Written or submitted by: "United States Government Accountability Office" (L105, L155); signed
  Orice M. Williams, Director, Financial Markets and Community Investment (L457-461; (202) 512-8678,
  L451, L479, L525). Staff (L483, 8): Lawrence D. Cluff (Assistant Director), Tania Calhoun, Emily
  Chalmers, Rudy Chatlos, Chir-Jen Huang, Barry Kirby, Kristopher Natoli (intern), Melvin Thomas.
  Product code (250287) (L523). Congressional Relations Gloria Jarmon; Public Affairs Chuck Young
  (L517-521).
- Type, date, edition: report to the Ranking Member (The Honorable Spencer Bachus), Committee on
  Financial Services, House of Representatives (L103, L159-165); December 2007; letter dated December
  28, 2007 (L157; 28-DEC-07 L5); ACCNO A79248 (L13). Highlights at the END (L525-551).
- Period covered: GAO work May 2006 - November 2007 (L181, L471); 2005 hurricane season (Katrina,
  Rita); P/C Katrina payouts as of December 31, 2006 (L243); NFIP Katrina payments as of August 31,
  2007 (L243); FEMA staffing as of September 2007 (L245); Figure 2 "as of 2007" (L307). Calendar dates.
- Entities and aliases: NFIP (est. 1968 under the National Flood Insurance Act of 1968, 42 U.S.C. 4001
  et seq., "as a subsidized program", fn1 L175); FEMA, U.S. Department of Homeland Security (L169);
  WYO = write-your-own insurers (L149, L209); NFIP program contractors (L181, L195); National Flood
  Insurance Fund (L245); TRRP = Transaction Record Reporting and Processing Plan (L149, L365, fn19 44
  C.F.R. Part 62); NAIC (L147, L181); IDRS = Insurance Disaster Reporting System (fn24 L407; data call
  by Alabama, Florida, Louisiana, Mississippi, Texas regulators, L401); DHS Office of Inspector General
  interim report OIG-07-62 (July 2007) (fn23 L393); McCarran-Ferguson Act of 1945 (L227, fn6);
  Property Casualty Insurers Association of America (fn16 L343); Louisiana Department of Insurance
  (L325, fn15); state-sponsored wind insurance pools (L263); adjuster types (4, L219-225): staff
  (company), independent (and adjuster firms), emergency, public (last).
- Tables: none. Figure 1 "Key Flood Insurance Claims Processing Steps on Flood-Damaged Properties"
  (L235; notes a-b L237-239) and Figure 2 "Licensing and Training Requirements for Adjusters in
  Selected Coastal States as of 2007" (L307; notes a-d L309-317): figure bodies NOT in text
  (unresolved); Figure 2 notes: (a) Louisiana 2006 Acts No. 783 (Claims Adjuster Act) and No. 806
  (Public Adjuster Act), licensure from June 30, 2007, public adjusters barred from contingent/
  percentage fees; (b) Mississippi 2007 House Bill No. 1524 (public adjusters); (c) requirements
  established after the 2005 season; (d) Alabama bars independent public adjusting.
- Lists:
  - Objectives (3) (L7, L179, L537).
  - Fieldwork states (8, L181, L467): Florida, Illinois, Louisiana, Mississippi, North Carolina,
    Pennsylvania, South Carolina, Texas. Coastal states contacted (8, L305): varying requirements in
    Florida, Georgia, Mississippi, North Carolina, South Carolina, Texas; no exam or continuing-
    education requirements in Louisiana and Alabama (last) during 2005. The two eight-state lists
    differ (Illinois/Pennsylvania vs Georgia/Alabama).
  - Parties consulted (L181, L465): FEMA, NFIP program contractors, state insurance regulators,
    NAIC, property-casualty insurers, state-sponsored wind insurers, insurance agents, claims
    adjusters, industry associations, mediators (last).
  - Emergency-adjuster approaches (L347): review/certification by sponsor in Florida, Mississippi,
    North Carolina, Texas; North Carolina minimum guidelines; South Carolina application; Louisiana
    registration only (last).
  - Matters for congressional consideration (2, L203, L429-433): clear statutory access for FEMA to (1)
    wind and flood damage claims information from WYO insurers and (2) WYO policies, procedures and
    instructions for wind vs flood.
  - Recommendation (1, L203, L437): state insurance commissioners/regulators acting through
    (in conjunction with) NAIC enhance standards and oversight for all types of claims adjusters.
  - Responses (L205, L441-443, L541): DHS written comments (Appendix II, text ABSENT, L473) - "It
    concurred with our recommendation ... but disagreed with the matters for congressional
    consideration" (L205, attributed to DHS) / "FEMA concurred ... but disagreed" (L441) / highlights
    "FEMA agreed ... but did not agree that Congress should grant it enhanced authority" (L541); FEMA
    cites "unneeded burden and cost(s)" (L205, L443); GAO disagrees (L205, L443-445); NAIC gave no
    written comments, orally expressed general agreement (L205, L441). Highlights phrase the matters
    as "GAO recommends granting FEMA authority" (L541).
  - Report copies (L447): Administrator of FEMA; CEO of NAIC; Chairman, House Financial Services;
    Chairman and Ranking Member of Senate Banking, Housing, and Urban Affairs; of House Homeland
    Security; of Senate Homeland Security and Governmental Affairs (last).
  - Reinspection file results (740 files, L395-399): "Around two-thirds" undetermined; "Approximately
    26 percent" flooding only; "8 percent" wind and flood combination.
  - IDRS phases (3, L409): I totals; II by damage type; III closed claims.
  - Prior GAO products cited (fn6, fn9, fn17, fn18, fn20, fn22, fn25; links L557-569): GAO-05-81R (July
    28, 2005), GAO-07-1078 (Sept. 5, 2007), GAO-01-885R (July 6, 2001), GAO-03-433 (Sept. 30, 2003),
    GAO-06-119 (Oct. 18, 2005; cited twice, fn20 and fn25), GAO-07-169 (Dec. 15, 2006). None is a
    bundle document.
- Forecasts, guidance, deadlines, effective dates: Louisiana Claims Adjuster Act (2006) licensing of
  staff and independent adjusters "beginning on June 30, 2007" (L325; fn a L309-311 adds public
  adjusters); Mississippi 2007 public-adjuster law (L327, fn b); industry observers' estimate that
  Katrina insured losses other than flood "could total more than $40 billion" (L243); FEMA agreed to
  implement GAO's earlier recommendation on statistically valid reinspection samples (L405); NAIC
  developing an updated disaster reporting system (L401); DHS OIG work "ongoing" (L385).
- Hedged claims: L185 homeowners "may find themselves without the funds"; L187-189 requirements "may be
  temporarily relaxed", adjusters "may not have met", qualifications "may vary significantly"; L193
  NFIP data "may not always allow FEMA to effectively oversee"; total-damage data "could be useful in
  some cases"; fn7 L249 FEMA official: same-company wind and flood coverage "likely occurs in the
  majority of cases"; L281 evidence "may have been further compromised"; L345 oversight "may be
  weakened"; L421 standards "may be relaxed or eliminated"; L431 statutory access sought "in cases in
  which it is likely that both wind and flooding contributed"; L443 "the likely eventuality that FEMA
  would need to draw on the U.S. Treasury to pay flood losses that exceed the funds available from
  premiums". Unhedged: "an inherent conflict of interest exists" (L185, L259, L283).
- Rounded prose beside exact figures: "about 96 percent" of NFIP policies sold/serviced by WYO insurers
  (L209); "about 68 employees" and "about 170 contractor employees" as of September 2007 (L245); P/C
  Katrina claims "approximately $22.4 billion" (excluding flood, as of December 31, 2006, fn8 lines of
  business L251); NFIP Katrina "over $15.7 billion" as of August 31, 2007, "approximately 99 percent of
  all flood claims received" (L243; fn21 L379); Katrina + Rita NFIP "approximately $16.2 billion",
  average payments "exceeding $95,000 and $47,000, respectively" (L371); WYO allowance "3.3 percent of
  each claim settlement amount" (L283); coverage limits $250,000 structure / $100,000 contents (L185,
  L267); illustration: $450,000 house vs $250,000 flood limit (L275); 740 reinspection files (L181,
  L395, L471); Florida and Texas staff/independent adjusters 24 hours of continuing education every 2
  years (2005, L323).
- Notes: NFIP does not cover building damage over $250,000 or additional living expenses (L185, L267;
  fn11 FEMA limited evacuation reimbursement); NFIP does not participate in state mediation (fn14
  L297); Louisiana and Mississippi mediation programs resolved the majority of cases (L295);
  Louisiana market conduct exams addressed timeliness, not wind vs flood; Mississippi exams ongoing
  (L353); industry declined to share adjuster guidance (L331, L467); TRRP "Total Building Damages",
  "Total Damage to Contents" flood-only, "Cause of Loss" has no wind option (L367); expedited Katrina/
  Rita methods (aerial/satellite photography, flood depth data, foundation-only adjustments) "As we
  reported in December 2006" (L371); "as we reported in 2005, following Hurricane Isabel" claims were
  denied because damage was wind-driven rain (L367, fn20 GAO-06-119); reinspections generally several
  months after the event (L403); FEMA previously did not use statistically valid samples (L405);
  senior FEMA officials question usefulness of wind data (L373). Exclusion/negative: D09 never
  mentions the Flood Insurance Reform Act of 2004 or its mandates (grep "Reform Act": no match);
  state wind data lacked zip-code/property-level detail (L195, L401).
- Operative definitions, rules and scope exceptions: anti-concurrent causation clause (L293);
  replacement cost value (fn10 L269); FEMA audit access under 42 U.S.C. 4084 limited to audit and
  examination (fn4 L199); market conduct examinations (fn2 L191); reciprocity for nonresident
  adjusters (L339); emergency adjuster waivers (L345); NFIP flood adjusters trained and certified
  annually and must hold a state license if independent (L333).
- Amendments or contradictions: response attribution DHS (L205) vs FEMA (L441, L541); Louisiana Act
  coverage (staff and independent at L325 vs staff/company, independent and public "respectively"
  across two Acts in fn a L309-311).
- Coverage: FULL. Read L1-150, L150-239, L239-328, L328-407, L407-486, L486-590 (ledger complete; none
  remaining; long lines L185, L205, L445 end as read). MISSING IN SOURCE: Figure 1 and Figure 2
  bodies; Appendix II DHS letter (heading only L473). Spot-check vs docs/: "about 68 employees" (docs
  L243), Figure 2 note a (docs L307), fn21 (docs L377), "Approximately 26 percent" (docs L397)
  identical.

## Shared ground (navigation only)

Facts and locations only; hooks belong in notes/hooks.md.

- Issue order (dates from each title line): D01 Sept 30, 2003; D02 Apr 14, 2005; D05 Nov 18, 2005;
  D04 Feb 23, 2006; D03 Sept 20, 2006; D06 May 1, 2007; D09 Dec 28, 2007; D08 July 17, 2008; D07 July
  24, 2008. Issuer of every document is GAO: "United States General Accounting Office" in D01 (L43),
  "Government Accountability Office" from D02 on (D02 L59). Testimonies: D02, D03, D06, D07, D08;
  reports: D04, D05, D09; correspondence report: D01.
- Cross-citation: no document cites another bundle document by GAO number (grep of all "GAO-" ids).
  Underlying non-bundle reports: D03 -> GAO-06-1021 (Sept. 19, 2006, fn1 L251); D06 -> GAO-07-203
  (Apr. 6, 2007, fn2 L123); D07 -> GAO-08-712 (June 30, 2008, fn2 L735); D08 -> GAO-08-698 (June 27,
  2008, fn2 L279); D02 -> final report planned "in September 2005" (fn6 L151), unnumbered; D04 ->
  companion rulemaking report of October 17, 2005 (L137), unnumbered. D09 cites GAO-06-119 (Oct. 18,
  2005) for a 2005 Hurricane Isabel finding (L367, fn20 L375-377); no document states whether that is
  the report D02 planned.
- GAO officials and contacts: Orice M. Williams signs/testifies in D03 (title "Director Financial
  Markets and Community Investments", L95), D05 (L335), D08 (L101), D09 (L457-461); David G. Wood
  (D04 L391) and Yvonne D. Jones (D06 L107-111) hold the same "Financial Markets and Community
  Investment" directorship; Laurie E. Ekstrand (D01 L171-173) and William O. Jenkins, Jr. (D02 L75)
  are each "Director, Homeland Security and Justice Issues" with the same phone (202) 512-8777 (D01
  L165, D02 L311); John E. Dicken, Director, Health Care (D07). Phone (202) 512-8678 is printed for
  Williams (D03 L267, D05, D08, D09), Wood (D04 L387, L415) and Jones (D06 L317, L365); variants
  (202) 512-5837 (D03 L207, Williams) and (202) 512-6878 (D04 L427, Wood). Staff names repeated
  across documents: Marc Molino (D03 L211, D04 L417, D05 L361); Barbara Roesmann (D03, D04); Robert
  Pollard (D03, D08 L269); Tania Calhoun (D03, D09 L483); "Steve Ruszczyk" (D03) / "Stephen
  Ruszczyk" (D05); Emily Chalmers (D05, D08, D09) / "Emily R. Chalmers" (D06 L317-319); Omyra Ramsingh
  (D06, D08); "Carl M. Ramirez" (D06) / "Carl Ramirez" (D08); "Lawrence Cluff" (D05) / "Lawrence D.
  Cluff" (D09), Assistant Director in both. Congressional Relations/Public Affairs contacts: Gloria
  Jarmon and Paul Anderson (D02, D03, D06); Ralph Dawn and Chuck Young (D07, D08); Gloria Jarmon and
  Chuck Young (D09). Product codes: D01 440210, D04 250226, D05 250227, D09 250287, D03 250316, D06
  250342; none in D02, D07, D08.
- Congressional recipients: House Committee on Financial Services - Subcommittee on Housing and
  Community Opportunity (D02 L61-63); Subcommittee on Oversight and Investigations (D04 L57, L129, to
  Chairwoman Sue W. Kelly and Ranking Minority Member Luis V. Gutierrez; D08 L85); full-committee
  Chairman Michael G. Oxley (D05 L125); Ranking Member Spencer Bachus (D09 L159-165). Same subcommittee
  NAME but a different committee: D07 is before the Subcommittee on Oversight and Investigations,
  Committee on Energy and Commerce (L89). Senate Committee on Banking, Housing, and Urban Affairs:
  D03 testimony to its Subcommittees on Housing and Transportation and Economic Policy (L81); mandate
  discussed with it (D02 L131); report copies (D05 L329, D09 L447). D06: House Judiciary Subcommittee
  on Commercial and Administrative Law (L91). D01: Representative Edolphus Towns (L7, L47).
- NFIP pair (D02 2005 testimony vs D09 2007 report), same quantities located in both:
  - FEMA staff: "about 40 FEMA employees" (D02 L91, L147, L203) vs "about 68 employees" as of September
    2007 (D09 L245); "about 170 contractor employees" in both (D02 L91, L147, L203; D09 L245).
  - WYO share of policies: "about 95 percent", 94 companies, other 5 percent direct (D02 L205, fn7
    L219) vs "About 96 percent" (D09 L209).
  - WYO claim compensation: "about 3.3 percent of the incurred loss" (D02 L229) vs "an allowance of 3.3
    percent of each claim settlement amount" (D09 L283); D02 also gives the expense allowance of
    "about one-third of the premium" (L205); D09 points to GAO-07-1078 on payment formulas (L247).
  - Coverage limits $250,000 building / $100,000 contents (D02 L109, L119, L161-163; D09 L185, L267);
    replacement cost defined in both (D02 L163; D09 fn10 L269).
  - NFIP created in 1968 under the National Flood Insurance Act (D02 L7, L109, fn3-4; D09 L169, fn1
    L175 "as a subsidized program"); FEMA inside DHS (D02 fn1 L111, since March 2003; D09 L169).
  - Finances: D02 "self-supporting for the average historical loss year", three Treasury borrowings in
    the last decade all repaid with interest, about $12 billion paid since inception (L121-123) vs D09
    Katrina flood claims over $15.7 billion as of August 31, 2007 (L243, fn21), Katrina + Rita about
    $16.2 billion (L371), and "the likely eventuality that FEMA would need to draw on the U.S.
    Treasury" (L443).
  - Adjusters: D02 FEMA certification (4 years' experience, workshop, yearly refresher and exam;
    4,844 flood-certified adjusters as of April 2005; L223-225) vs D09 annual NFIP training and
    certification on top of varying state licensing (L333).
  - Reinspections/reviews: D02 about 10 general adjusters reinspect a random sample of about 4 percent
    of claims per flood event; operational reviews at least every 3 years with 100-file samples
    (L231-253) vs D09 reinspection program via program contractor, earlier samples not statistically
    valid (L405, citing GAO-06-119), 740 files reviewed (L395-399), "periodic operational reviews"
    (L373).
  - Hurricane Isabel: D02 September 2003, about 23,770 claims for $454.2 million (L125-127), GAO review
    of Isabel claims under way (L137, fn6) vs D09 2005 finding that some Isabel claims were not paid
    because damage was wind-driven rain (L367).
  - Flood Insurance Reform Act of 2004 (P.L. 108-264, June 30, 2004): D02 gives the three FEMA mandates
    (agent education/training, coverage explanation materials, appeals process), the 6-month deadline
    (elapsed December 30, 2004), status and FEMA's October 2005 expectations (L99, L133, L149,
    L279-305). D09 never mentions the Act (grep "Reform Act": no match); D09 lists FEMA's
    responsibilities as including "offering training to insurance agents and adjusters" (L245).
  - Hurricane seasons: D02 covers Isabel (2003) and the 2004 hurricanes Charley, Frances, Ivan, Jeanne
    (59,125 claims, more than $1.3 billion as of March 2005, L129); D09 covers the 2005 season
    (Katrina, Rita).
- Hurricanes elsewhere: Hurricane Rita in September 2005 closed OCC's Houston CAG phones for 4 days
  (D04 L333); Hurricane Katrina "in September 2005" (D05 L233) / "in 2005" (D05 L265), NAIC actions
  after Katrina (D05 L265, L327); Katrina/Rita throughout D09. 9/11 appears in D05 (L131, L199, L275)
  and D02 (2001 attacks' costs surpassed by the 2004 hurricanes, L129).
- NAIC and state insurance regulators (D05, D07, D09; D02 mentions state insurance commissions only,
  L213, L281-283): NAIC described as "a body composed of state insurance regulators" that "does not
  regulate insurers" (D05 L167) and as author of LTCI model act (1986) and model regulation revised in
  2000 (D07 fn1 L733, L173-183). Recommendations routed through NAIC: D05 (state regulators working
  through NAIC, plus NAIC itself; L157, L315-323) and D09 (state insurance commissioners acting
  through NAIC; L203, L437); D07 makes none (L131, L151). NAIC's responses: D05 written comments by
  NAIC's Executive Vice President and CEO, "generally agreed" (L159, L327); D07 NAIC compiled member
  states' comments, report "accurate but seemed to critique" (L131, L151); D09 no written comments,
  oral "general agreement" (L205, L441). NAIC officers named as copy recipients: "President of NAIC"
  (D05 L329), "Chief Executive Officer of NAIC" (D09 L447). Market conduct examinations: D05 (conduct
  exams in response to complaints, L165), D07 (L149, L165, L717), D09 (fn2 L191, L351-353). State exam
  cycle "every 3 to 5 years" (D05 L165, L203, L291). Disaster data: NAIC developing an updated disaster
  reporting system (D09 L401); NAIC coordinated a complaint system after Katrina (D05 L265).
- State lists that share members: D07 case-study states (fn4 L739: CA, FL, IL, IA, NY, ND, PA, TX, WA,
  WI); D09 fieldwork states (L181: FL, IL, LA, MS, NC, PA, SC, TX) and coastal states (L305: FL, GA,
  MS, NC, SC, TX, LA, AL); D04 site-visit states (L141: CA, GA, NY, NC; phone IA, ID; work also TX,
  D.C.); D03 named states (L111, L139, L195-199); D01 NVISS sites (fn2 L125-127); D05 states unnamed
  by design (L139, L353).
- Federal banking regulators (D03, D04, D08): five listed in D03 (OCC, Federal Reserve, FDIC, NCUA,
  OTS; L129) and in D08 as ECOA enforcers for depository institutions (L171); D04 compares four (OCC,
  Federal Reserve, FDIC, OTS; L133) and never mentions NCUA; D08 contacted four (FRB, OCC, FDIC, OTS;
  L207). Federal Reserve naming varies: "Board of Governors of the Federal Reserve System (Federal
  Reserve)" / "Federal Reserve Board" (D03 L129, L123); "Federal Reserve System (Federal Reserve)
  -including the Board of Governors and the 12 Federal Reserve Banks" (D04 L133); "Federal Reserve
  Board's (FRB)" and separately "a Federal Reserve Bank" (D08 L7, L211). Federal Reserve rules:
  Regulation Z / Truth in Lending Act (D03 L131, L189) vs Regulation B / ECOA (D08 L7, L137-139).
  Federal Reserve actions: Regulation Z review, summer 2006 hearings (D03 L189); 1999 proposal and 2003
  decision on Regulation B (D08 L139); consumer feedback survey since mid-1980s (D04 L209). OTS: review
  of 68 most active AMP lenders (D03 L189); about 3 percent referrals, 5 complaints per billion dollars,
  most complaints about home mortgage loans (D04 L237, L259, L263). OCC: D03 (AMP promotional
  reviews, L189), D04 (subject), D08 (staff discussions, L211). Credit cards: most common complaint
  product for OCC, FDIC, Federal Reserve (D04 L263) and the subject of two SCF studies (D08 L201-203).
- FTC across documents: not a supervisory agency, enforces consumer laws for non-depository lenders and
  brokers (D03 L131); FTC workshop May 2006 and brochure (D03 L189); Federal Trade Commission Act
  charges OCC (D04 L135); FTC settled enforcement actions against several credit counseling agencies
  (D06 L159); residual ECOA enforcer (D08 fn5 L285). Absent from D01, D02, D05, D07, D09.
- IRS / Treasury / DOJ / DHS / HHS: IRS Credit Counseling Compliance Project since October 2003, 47
  completed exams, four Trustee-approved providers under exam (D06 L137, L159, L197-201); IRS
  (Department of the Treasury) issued HIPAA LTCI regulations in 1998 and relies on states (D07 L143,
  L167). Treasury also appears as OCC's parent (D04 L131), sector coordinator delegated by DHS (D05
  L179-183), FEMA's lender (D02 L121; D09 L443). DOJ: BJS, NIJ, FBI, ATF and draft comments (D01
  L67, L145, L215-229); U.S. Trustee Program (D06 L119, L153); DOJ federal-facility security standards
  (D05 L269). DHS: FEMA's parent (D02 fn1; D09 L169), August 2004 terror-target announcement and
  delegation to Treasury (D05 L129, L181), written comments and Office of Inspector General report
  OIG-07-62 (D09 L205, L385, fn23). HHS: CDC (D01) and HIPAA standards (D05 L283).
- HIPAA (Health Insurance Portability and Accountability Act of 1996) appears in two documents for
  different provisions: information-security requirements on insurers (D05 L279, L283, L349) and
  tax-qualified LTCI standards (D07 L167, fn6-8). GLBA and Sarbanes-Oxley appear only in D05.
- Repeated overview passages (summaries that restate body results): D01 Results in Brief L59-63 and
  body L75-77/L87 restate Table 2-3 totals; D02 highlights L87-99 and summary L143-149; D03 summary
  L109-123 and highlights L277-289; D04 Results in Brief L143-151 and highlights L437-453; D05 Results
  in Brief L141-159 and highlights L381-395; D06 summary L133-149 and highlights L375-397; D07
  highlights L115-133 and summary L145-151; D08 highlights L109-129 and summary L151-159; D09 Results
  in Brief L183-205 and highlights L535-551. Wording differences between summary and body are noted in
  each document entry (e.g., D07 "remain" vs "may remain"; D05 health-insurer priorities; D06 fee
  wording; D09 "recommends" vs "matters for congressional consideration").
- Forecasts/plans vs later actuals (located; no later document reports the outcome unless stated):
  D02 FEMA expected Reform Act materials by October 2005 and compliance after October 2005 (L99,
  L149, L295, L305) - D09 silent; D02 GAO final report planned September 2005 (fn6 L151); D03 draft
  interagency AMP guidance (December 2005) not yet final (L183-185); D04 phone-hour expansion
  planned (L149, L335, L353-355); D05 NAIC independent testing budgeted for 2006 (L271, L305); D06
  provider counts 71/76 (October 2005) to 153/268 (October 2006) (L297-299) and fee-waiver rulemaking
  promised for 2007 (L293); D07 NAIC group formed March 2008 (L719); D08 SSBF elements to the SCF from
  2010 (L173); D09 FEMA agreed to a prior recommendation on statistically valid samples (L405).
- Proposed vs final actions and effective dates: D08 FRB 1999 proposal not adopted in 2003 (L139); D06
  Act signed April 20, 2005, effective October 17, 2005, interim final rule July 2006 (L153, L169); D02
  Reform Act enacted June 30, 2004, 6-month deadline elapsed December 30, 2004 (fn2 L113, L279); D04
  preemption rules issued January 13, 2004 (L167); D07 NAIC model regulation revised 2000, HIPAA tied
  to the January 1993 model (L167, L173); D09 Louisiana licensing from June 30, 2007 (L325, fn a);
  D01 P.L. 100-615 of Nov. 5, 1988 and BJS agreement effective June 1, 1989 (L279).
- Recommendation recipients and responses (actions vs mentions): D03 Federal Reserve Board (response:
  will conduct consumer testing; L201, L281); D04 Comptroller of the Currency, three recommendations
  (concurred/agreed; L151, L379-381, L443); D05 state insurance regulators via NAIC and NAIC itself
  (generally agreed; L159, L327); D06 U.S. Trustee Program, two recommendations (concurred/agreed;
  L143, L145, L251, L293, L383); D09 one recommendation to state insurance commissioners via NAIC
  (DHS/FEMA concurred; NAIC oral agreement) and two matters for Congress (DHS/FEMA disagreed; L205,
  L437-443, L541). No recommendations: D01 (agencies said draft accurate, L155), D02 (work in
  progress), D07 (L131, L151), D08 (FRB "did not take a position", L9, L159).
- Same-document conflicts/variants (both locations in each document entry): D01 66 vs 65.5 percent
  (L71/L293); D02 rule making for "two of the initiatives" vs all three (L149/L279, L295); D03 and D04
  witness phone numbers; D04 OCC-reported vs GAO-computed timeliness (L269-271); D05 title wording;
  D06 "fewer than 2 percent" vs NFCC "about 3 percent" (L223/fn16); D07 Massachusetts phase-in vs
  Figure 1 row (L611/L445-451), complaint-data states 6 vs 5 (L143/fn22), NAIC adoption "since 2000"
  vs "by 2006"; D08 fn7 vs fn8 author lists; D09 DHS vs FEMA as respondent (L205/L441).
- Unit/scale notes: D01 counts (incidents, agencies); D02 dollars (millions/billions), percent; D04
  percent, counts, dollars in millions/billions/trillions, complaints per billion dollars of assets;
  D06 percent, dollars per session, counts of certificates; D07 percent rate increases, dollars, counts
  of states; D09 dollars in billions, percent. Fiscal-year usage only in D04 (OCC annual reports;
  fiscal-year end not stated); all other periods are calendar dates.
