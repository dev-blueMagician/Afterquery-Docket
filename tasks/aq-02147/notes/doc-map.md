# aq-02147 - document map

Maintained by the caller or optional `bundle-mapper` from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Line references are `text/Dnn.txt` line numbers (Lnnn). "Doc N" is the task page's number. Map
arithmetic (column sums and similar checks) is marked as such and is not a document statement.

## Bundle

- What it is: five UK government documents on Statutory Sick Pay (SSP) and work-and-health policy in
  two consultation cycles. Cycle 1: DWP/DHSC consultation "Health is everyone's business" (July 2019,
  D04) and the government response (July 2021, D02). Cycle 2: DWP consultation "Making Work Pay:
  Strengthening Statutory Sick Pay" (October 2024, D05), DWP Equality Analysis of the SSP measures
  (November 2024, D01) and the government response (© 2025, print code 03/25, D03).
- Documents: 5. Local id = task page Doc N: D04 = Doc 1, D02 = Doc 2, D05 = Doc 3, D01 = Doc 4,
  D03 = Doc 5 (manifest ids are alphabetical by file name; form fields must use Doc N).
- Gaps: no unread text; every document read sequentially to EOF (ledgers below). Visual-only material
  not in text: D05 Figure 1 (L139) and Figure 2 (L157) are chart titles with no data; D03 Figure 1
  (L77) is a chart described only by its modes and base (L79, L81); D02 has two image placeholders
  `""` (L1036 after the example choice scenario, L1076 after Annex B Figure 1 caption). No PDF or
  rendered page is available, so visual checks of these charts are unresolved. D02's correction slip
  cites page numbers (P.30, P.32) that the text capture does not carry (mapped to L447 and L464 below).
- Extraction spot-checks (text vs docs/ originals; caller reports whitespace-only differences plus the
  "# Dnn" header line; page count not applicable, text capture with no pages):
  - D01: table row "|Below LEL|27% (263,000)|73% (717,000)|" (text L281 = docs L288); marital rows
    (L324, L328 = docs L335, L339); Case study 2 stray row "||80%||" (L432 = docs L447); footnote 1
    "DWP Internal Estimate using combination of Family Resource Survey 2022/23 and Labour Force Survey
    2022." (L448 = docs L464). Match.
  - D02: Table 1 header "|Respondent Type|Responses%||" and "|Other|102|21%|" (L194, L204 = docs L193,
    L203); displaced row "|£500|£800|£1,000|||" (L846 = docs L857); Table 3 total (L859 = docs L872);
    Table 4 header and QALY-value row (L887, L890 = docs L902, L905); "planproportion" (L967 = docs
    L987); `""` placeholders (L1036, L1076 = docs L1062, L1102); footnotes 47/55 Ballard (L1370, L1402 =
    docs L1410, L1442). Match; the layout faults are in the capture, not introduced by extraction.
  - D03: Figure 2 row "|0 to 20%|24%|" (L95 = docs L94); Figure 3 row "|80 to 100%|71%|" (L145 = docs
    L146); response counts (L55 = docs L53); "1257 duplicate responses" (L229 = docs L231). Footnotes:
    not applicable (none).
  - D04: tables not applicable (0 pipe tables); footnote 92 "Calculated as £94.25 x (25/35 hours) =
    £67.32" (L2106 = docs L2104); footnote 93 (L2110 = docs L2108); "earn an average of at least £118 per
    week" (L604 = docs L602); "around 2 million employees" (L732 = docs L730). Match.
  - D05: Table 1 60% row (L149 = docs L148); Table 2 "Total costs" row (L171 = docs L172); footnote 4
    "Brain Drain report - final.doc" (L278 = docs L280). Match.
  - Pipe-table counts ("|---" separators): D01 9, D02 21, D03 2, D05 2, D04 0.
- Provenance: notes/intake.json (capture_sha256 151ff944c526b5f3b07faad4b66bdad0c45a781249481e989b8a78b84a68b3ef);
  5/5 documents incomplete=false, gap_characters 0, matches_capture true; captured_sha256 =
  source_sha256 for all five. Capture page carried a stale-page reload warning (form-check issue, not
  document text). The capture's platform bundle overview was not used (navigation only, not evidence).
- Reuse binding (map dated 2026-10-08; extraction method "text", pages null; all coverage full):

  | Id | Doc N | Source file | sha256 (manifest = intake source) | chars | text lines |
  | --- | --- | --- | --- | --- | --- |
  | D01 | 4 | docs/Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt | 9013a369099a897cb39e77998923bde617c5f444022cedbbd5443bc40cfd872b | 41,035 | 453 |
  | D02 | 2 | docs/Government-response-Health-is-everyones-business.txt | aa81f35a008874836870d25ac16f40ae07e11c1e93d70ca09441bf9868006812 | 175,385 | 1,631 |
  | D03 | 5 | docs/Government-response-Making-Work-Pay-Strengthening-Statutory.txt | 99994b4b3c6786d2485e5ce423dde0c58957aaf69bf9b4b538a8d58d0b164273 | 41,164 | 268 |
  | D04 | 1 | docs/Health-is-everyones-business-proposals-to-reduce-ill.txt | f205d38d847e6ff83c3dd404c3224844ff5a95991edf76117afb624ca39ad538 | 189,101 | 2,251 |
  | D05 | 3 | docs/Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt | 2871925cdbcd5b544e45d55a88f009cf8c7f596d69e88dc011d6c521c407d5f8 | 25,675 | 279 |

  Any change to these hashes or a re-extraction invalidates the line references and every entry below.

## D01 (task page Doc 4) - Equality Analysis for Statutory Sick Pay Reform Measures in the Employment Rights Bill

- Source: text/D01.txt (L1-453) from docs/Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt; no pages.
- Written or submitted by: Department for Work and Pensions (masthead L4-5; L23 "the Department to
  enable DWP"). No minister named. Mentioned, not authors: ONS (fn2 L452), UN conventions (L93-111).
- Type, date, edition: Equality Analysis under the Public Sector Equality Duty, s.149 Equality Act 2010
  (L23). Title from URL slug (L15, under the making-work-pay-strengthening-statutory-sick-pay
  consultation path). Subtitle L17 "Consultation on the percentage rate for those earning below the
  current rate of Statutory Sick Pay." Dated November 2024 (L19); "© Crown copyright 2025" (L9);
  "published under the 2024 to 2026 Starmer Labour government" (L7). No CP number or ISBN.
- Period covered: current rates at writing (SSP £116.75, LEL £123, L45); below-LEL estimate "in
  Quarter 1 of the financial year 2022/23" (L47; fn1 L448 = FRS 2022/23 + Labour Force Survey 2022);
  demographic analysis on Family Resources Survey 2022/23 (L157); DWP Employee Survey 2023 (L159);
  disability employment gap "as of June 2024" (L385). Financial-year months are not defined.
- Entities and aliases: DWP / "the Department"; PSED; Equality Act 2010; UNCRPD Articles 12, 19 ("All 3
  parts"), 27 (L93-105); UNCRC Article 27 (L109-111); FRS = Family Resources Survey (L157; spelled
  "Family Resource Survey" L395, L448); OSP = Occupational Sick Pay (L159); Plan to Make Work Pay (L67,
  L83); Employment Rights Bill / "the Bill" (L67, L89). Capitalised "Qualifying Day" and "Waiting Days"
  (L45). Cohort labels vary: "Below LEL"; "those earning above, but close to, the LEL"; table headers
  "Employee currently earning above, but close to, the LEL" (L177), "Employees currently earning above,
  but close to, the LEL" (L199, L282, L296, L322), "Employee currently earning above, but close to, LEL"
  (L227), "Current employee earning just above, but close to, the LEL" (L252). "Asian/Asian British"
  (L223, L231) vs "Asian/British Asian" (summary L351). "single individuals" (L314-316) vs "individuals
  who are not married" (summary L367).
- Tables (9 pipe tables; percentages from internal DWP analysis of FRS; three cohorts defined L139-153:
  all employees, below LEL, above-but-close = £123 to £146 per week at the illustrative 80% rate):
  1. L171-177 "Employee proportions by age" (rows = cohorts; columns 16-24 / 25-34 / 35-44 / 45-54 /
     55-64 / 65 and over): All 10/25/23/21/17/3; Below LEL 20/17/18/15/19/11; Above-close 18/18/17/20/18/9.
  2. L193-199 "Whether has a disability (under the Equality Act 2010 core definition)" Yes/No: All 16/84;
     Below LEL 22/78; Above-close 22/78.
  3. L225-234 "Proportion of employees by ethnicity" (columns Above-close / Below LEL / All): White
     78/86/84; Mixed/multiple 2/2/2; Asian/Asian British 13/7/9; Black/African/Caribbean/Black British
     6/3/4; Other ethnic group 1/2/2; Not declared 0/0/0.
  4. L250-262 "Proportion of employees by religion in England and Wales" (only England and Wales,
     "covering approximately 90% of each cohort", L248; columns Above-close / Below LEL / All): Missing
     11/10/11; No religion 39/41/41; Christian 36/41/39; Buddhist 0/0/0; Hindu 3/1/2; Jewish 0/0/0;
     Muslim 7/5/4; Sikh 1/1/1; "Any other religion, please describe" 3/2/1.
  5. L276-282 "Proportion of employees by sex" (Male / Female, % with counts): All 50% (14,378,000) /
     50% (14,107,000); Below LEL 27% (263,000) / 73% (717,000); Above-close 26% (88,000) / 74% (245,000).
  6. L294-302 "Proportion of employees by sexual orientation" (Above-close / Below LEL / All): Missing
     29/28/36; Heterosexual/straight 67/67/60; Gay/lesbian 2/1/1; Bisexual 3/3/1; Other 0/1/1.
  7. L320-329 "Proportion of employees by de facto marital status" (Above-close / Below LEL / All):
     Married/civil partnership 47/55/51; Cohabiting 14/14/19; Single 31/32/23; Widowed 2/2/1;
     Divorced/civil partnership dissolved 1/5/4; Separated 4/3/2.
  8. L409-422 Appendix Case study 1 "Employee works 5 days per week, and earns £123 per week":
     cumulative new illustrative entitlement at 80% vs old entitlement, weeks 1-10: £98/£47, £197/£163,
     £295/£280, £394/£397, £492/£514, £590/£630, £689/£747, £787/£864, £886/£981, £984/£1,097.
  9. L428-442 Case study 2 "Employee works 5 days per week, and earns £175 per week": header lacks the
     rate; a separate row "||80%||" (L432) carries it (same in docs). Weeks 1-10: £117/£47, £234/£163,
     £350/£280, £467/£397, £584/£514, £701/£630, £817/£747, £934/£864, £1,051/£981, £1,168/£1,097.
  - Column orientation differs: tables 1, 2 and 5 have cohorts as rows; tables 3, 4, 6, 7 have cohorts
    as columns in the order Above-close, Below LEL, All employees.
  - Map arithmetic checks: marital Below LEL column sums to 111% (others 99, 100); age All row 99;
    religion columns 100/101/99; ethnicity All 101; sexual orientation 101/100/99. Sex counts: All
    14,378,000 + 14,107,000 = 28,485,000; Below LEL 263,000 + 717,000 = 980,000; Above-close
    88,000 + 245,000 = 333,000.
- Lists: PSED three limbs L29-37 (repeated L373-381); "8 of the 9 protected characteristics" with
  marriage/civil partnership covered only by the first limb (L39); three problems L57-65; three
  outcomes L73-81; two most-impacted sub-groups L119-133; three cohorts L143-151; summary of
  disproportionate impacts, 7 items L343-367 (ages 16-24 and 65+; disabled; Asian/British Asian; Muslim;
  females; heterosexual/straight; "not married" = last item L367). Characteristics analysed but absent
  from the summary: gender reassignment (L209-211, FRS responses missing for 98-99% of each cohort) and
  pregnancy/maternity (L215-217, no FRS variable).
- Forecasts, guidance, deadlines, effective dates: percentage rate "will not initially be included in
  the Bill, which will be amended at a later stage to reflect the results of the 6 week Consultation"
  (L89); full analysis done "for indicative purposes only" at 80%, impacts "broadly similar for rates
  between 60% and 80%" (L89, L153). Monitoring plans (L395): DWP Employee and Employer Research surveys,
  extra FRS questions, secondary data matching "Given the absence of admin data on SSP"; no
  implementation date stated.
- Hedged claims (claim / hedge / attachment):
  - L117: "zero employees who will receive less SSP" stated firmly; then "this modelling is based on a
    small sample size ... in practice there could be employees who receive less SSP" (hedge attaches to
    the modelling result).
  - L129-131: "DWP modelling suggests that zero employees will receive less SSP"; "some individuals in
    this cohort who have a longer sickness absence may receive less overall"; "it is likely that these
    individuals would receive less in total by only a small amount per week (up to £4 per week after 5
    weeks of sickness absence)".
  - Net-impact wording by section: L155 (general, 3.7) "uncertain, although most likely positive"; L169
    age "overall positive"; L191 disability "positive"; L274 sex "positive"; L318 marriage "uncertain,
    although most likely positive". Assessments L201, L284, L304, L331: "there is uncertainty in the
    extent to which any negative impact will offset this".
  - L238 Asian/Asian British and L266 Muslim: "It is possible that ... will experience a
    disproportionate negative impact ... However, this impact is uncertain" (L266 adds "will likely be
    balanced by the removal of the waiting days").
  - L163 "there is a possibility that some of the employees ... will be eligible for Occupational Sick
    Pay"; L385 other impacts "expected to be small and not intentional"; L387 "there may be increased
    visible representation"; L424 "would likely to be notionally worse off once their sickness absence
    reaches 4 weeks under a rate at 80%"; L444 "always be notionally better off" (£175 case).
- Rounded prose beside exact figures: L157 "of 28.5 million employees, around 1 million ... below the
  Lower Earnings Limit ... and around 300,000 are earning between £123 and £146 per week" vs counts in
  table 5 (L280-282); L123 "around 1 million employees"; L129 "up to 300,000"; L187, L223, L246, L272,
  L292, L314 restate single table cells (22/22/16; 13 vs 9; 7 vs 4; 73/74/50; 67/67/60; 32/31/23);
  L424 "Currently, this individual receives 95% replacement rate of income" (£123 earner).
- Notes (other figures): L47 "around 1 to 1.3 million employees in the UK who earned below the LEL",
  excludes self-employed "who are not eligible for SSP"; L85 "an estimated 1 to 1.3 million" benefit
  from LEL removal; L385 disability employment gap 28.6 percentage points as of June 2024 [fn2 ONS A08].
- Operative definitions, rules and scope exceptions: L43 SSP "provides a minimum level of earnings
  replacement"; L45 flat rate £116.75 per week, payable for each Qualifying Day ("days on which an
  employee is contracted or scheduled to usually work"); "Gig workers and those on zero-hour contracts
  may be entitled ... if they meet all eligibility criteria, including being classed as an employee";
  "not payable for the first 3 Qualifying Days of sickness absence (Waiting Days) and is only payable
  when an employee is sick for at least 4 days or more (including non-working days/non-Qualifying
  Days)"; entitlement limited to earnings at least LEL £123 per week. L87 new structure: "either a
  percentage of their earnings or the flat rate of SSP (currently £116.75) whichever is lower". L117
  entitlement to start "from the first, rather than the fourth, day". L137 all other employees keep
  the flat rate. L153 80% illustration: lower weekly rate for earnings between LEL (£123) and £146.
  L179 SSP available to employees below the LEL "aged 16 and above". L107 disability definition
  (Equality Act 2010: "substantial" and "long-term" negative effect).
- Amendments or contradictions (internal, neutral):
  - Religion: text L264 "no religions or beliefs are overrepresented in the Below LEL cohort" vs table
    L260 Muslim Below LEL 5% vs All 4% (also Christian 41 vs 39, Any other 2 vs 1).
  - Marital: text L314 "cohabiting or married/in civil partnerships are underrepresented in both
    cohorts" vs table L324 Married/civil partnership Below LEL 55% vs All 51%; Below LEL column sums
    to 111%.
  - Above-close cohort size: L129 "up to 300,000" and L157 "around 300,000" vs table 5 counts (L282).
  - L131 "up to £4 per week after 5 weeks" sits beside Case study 1 week-5 cumulative £492 vs £514
    (L417); the document does not reconcile the two.
- Coverage: full. Ledger: L1-453 read sequentially (single chunk). Remaining: none. Footnote 2 (L452)
  ends with an unclosed Markdown link (as captured).

## D02 (task page Doc 2) - Government response to "Health is everyone's business" (DWP/DHSC, July 2021)

- Source: text/D02.txt (L1-1631) from docs/Government-response-Health-is-everyones-business.txt; no pages.
- Written or submitted by: DWP and DHSC (mastheads L4-9); "Presented to Parliament by the Secretary of
  State for Work and Pensions on behalf of the Department for Work and Pensions and the Department of
  Health and Social Care by Command of Her Majesty" (L21). Ministerial foreword signed Justin Tomlinson
  MP, Minister for Disabled People, Health and Work, and Jo Churchill MP, Minister for Prevention,
  Public Health and Primary Care (L89-93). Annex B authors: Michael Oldridge, Lisa Schulze (DWP), Peter
  Burge, Hui Lu, Pamina Smith, Nadja Koch (RAND Europe) (L996); RAND commissioned by the DWP/DHSC joint
  Work and Health Unit (L1004). Enquiries `workandhealthunit.consultationteam@dwp.gov.uk` (L31).
- Type, date, edition: "Government response to the consultation on proposals to reduce ill-health
  related job loss" (L19, L47); CP 509 (L37, L51); ISBN 978-1-5286-2363-6 (L33; "978 -1-5286-2363-6" L53);
  CCS1120523008 (L35); July 2021 (L39); Session 2021/2022 (L49); © Crown copyright 2021 (L11, L23).
  Includes a correction slip (L41-69) dated 23 September 2021 (L69).
- Period covered: consultation launched 15 July 2019, closed 7 October 2019 (L190); COVID-19 period
  2020-21 (L113-121, L170-178); data series to March 2021 (L177), Q4 2020 (L468), 2018 LTSA (L367);
  Annex A costs use ASHE 2019 (fn98, fn104) and BEIS business population estimates 2020 (fn100-101),
  Oxford Economics 2014; Annex B research "carried out in 2018" (L1046); "2020/21 financial year" (fn11
  L1226).
- Entities and aliases: DHSC written "Department of Health & Social Care" (L8) and "Department of Health
  and Social Care" (L21); HSE (L129); ALBs = arm's length bodies (L129); EHRC (L347); "EA10" = Equality
  Act 2010 (L347); EASS (L349); AtW = Access to Work (L261, L351); SOM = Society of Occupational Medicine
  (L59, L61, L447, L464, L615); "The At Work Partnership" (L65, L67); OHEG = Occupational Health Expert
  Group (L488); SEQOHS (L490, L546); GIRFT (L554); FOM = Faculty of Occupational Medicine (L556); ESRC,
  MRC, Academic Forum for Health and Work (L615); NIHR PRP (L617); GRiD (L155, L720); GIP/IIP (L714);
  BEIS (L361); Mind (L255); RAND / RAND Europe (L996, L1004); IAPT (L107); IPS (L109); CJRS, SEISS (L117);
  LTSA (L166); RTW (L925); QALY, SF-36 (L889, fn88 L1534, fn90 L1542); PHE (L879); NICE (L890); Bank of
  England (L468); Ballard J. survey for "Occupational Health [at Work]" (fn47 L1370, fn55 L1402).
  "Annual Survey of Household Earnings" is the document's expansion of ASHE (L829, L844, L946).
- Tables (21 pipe tables):
  - L192-205 Table 1 "Responses to 'Health is everyone's business' by respondent type". Header
    "|Respondent Type|Responses%||" merges the count and percent labels; counts sit in column 2,
    percentages in an unlabeled column 3. Employer 88 (18%); Employer Representative 46 (9%); Charity
    47 (10%); Trade Union 17 (4%); Occupational Health Provider 35 (7%); Health Service Provider 23 (5%);
    Self-Employed 16 (3%); Individual 111 (23%); Other 102 (21%); Total 485 (100%). Map check: counts sum
    to 485; percentages sum to 100.
  - L209-249 Figure 1 "Charts illustrating employer responses by size and type", rendered as 4 tables
    (percent of employer respondents): Size Micro (0-9 employees) 12%, Small (10-49) 23%, Medium
    (50-249) 23%, Large (250+) 43%; Sector Private 63, Public 23, Voluntary 14; Region NE 7, NW 11,
    Yorkshire and the Humber 7, East Midlands 8, West Midlands 9, East of England 8, London 11, South
    East 13, South West 8, Wales 7, Scotland 7, Northern Ireland 3; Industry Agriculture/forestry/fishing
    1, Energy and water 1, Manufacturing 7, Construction 9, Distribution/hotels/restaurants 4, Transport
    and communication 7, Banking and finance 4, Public admin/education/health 29, Other services 37.
    Map checks: size 101, region 99, industry 99. Prose L207 restates size and top three industries and
    lists who classed themselves as "other services".
  - Annex A Table 1 "Productivity (£)" L824-832 (Lower/Median/Upper): weeks of lost productivity
    3.8/6.4/8.0; average weekly gross pay (ASHE 2019 revised) £500/£500/£500; Productivity
    £1,800/£3,100/£3,800; "Note: figures have been rounded." Map check: products of the rounded inputs
    do not reproduce the printed productivity row.
  - Annex A Table 2 "Replacement costs (£)" L838-849: advertising/agency £200/£500/£900; temporary cover
    £2,000/£3,500/£5,000 (assumes 18 days per vacancy); HR process £200/£200/£200 (1.5-2 HR person-days);
    interviewing: label row L845 (text says "around £700–800" per vacancy) with its values displaced to
    the next row L846 "|£500|£800|£1,000|||"; Replacement costs £2,900/£5,000/£7,100 (map check:
    components sum to these).
  - Annex A Table 3 "Societal benefits of retaining an individual in work (£)" L853-861 (column label
    "Employer benefits"): Productivity £1,800/£3,100/£3,800; Replacement costs £2,900/£5,000/£7,100;
    Total £4,700/£8,000/£11,000; "Figures have been rounded."
  - Annex A Table 4 L885-891: header has six columns and each value row sits one column to the right of
    the Lower/Median/Upper labels. QALY change 0.0282/0.0675/0.1068; NICE value per QALY £60,000 (all
    three); individual health benefits £1,700/£4,100/£6,400.
  - Annex A Table 5 "One-off business familiarisation costs" L935-946: Small (1-49 employees) 0 hours,
    £31.29/hour, 1,368,770 businesses, "-"; Medium (50-249) 2 hours, £33.39, 36,140, £2,414,000; Large
    (250+) 2 hours, £33.39, 7,835, £523,000; Total £2,937,000. Note L946 (ASHE 2019 table 20.5a, uprated
    for non-wage costs; 2 hours assumed).
  - Annex A Table 6 "Business sickness absence management cost" L956-980. Volumes: Small 1,368,770
    businesses / 492,757 without a RTW plan / 18,232 LTSA in those; Medium 36,140 / 8,312 / 391; Large
    7,835 / 392 / 21; Total 1,412,700 / 501,500 / 18,600. p (develop RTW plans) 64% small, 77% medium,
    95% large (L967; the formula text reads "those without a RTW planproportion of business" with an
    operator missing, as captured). Cost (columns Time hours / Management cost per hour / No. of LTSA in
    businesses without a RTW plan / Total business cost): Small 5.5 / £31.29 / 18,232 / 3,137,600;
    Medium 5 / £33.39 / 391 / 65,200; Large 5 / £33.39 / 21 / 3,500; Total - / - / 18,600 / 3,206,300
    (cost cells printed without £; note L980 "Total business cost is businesses in scope of adopting new
    guidance * cost per return to work plan"; volume totals are rounded). Time
    assumptions L978 (2 hours at 4-6 weeks plus 0.5 hour for small employers; 2 hours at 2-3 months; 1
    hour after the absence).
  - Annex B attribute table L1014-1020 (5 attribute groups; reimbursement levels 0/25/50/75/100%; payment
    timing "All paid at the end" or "30% paid up front and 70% paid at the end"; admin requirements);
    example "Choice 1 of 6" L1024-1034 (spelling "reiumbursed" as printed).
  - Annex B Figure 1 (n=500) L1074-1116 rendered as 5 sub-tables by size group 10-19 (179), 20-49 (186),
    50+ (135); columns Current/last 12 months / Would provide / Would not provide. Independent expert
    advice 21/50/28, 28/48/24, 65/23/12; psychological therapy 8/47/45, 14/41/45, 40/32/28;
    rehabilitative services 11/43/46, 12/35/53, 30/33/37; programmes for specific problems 10/52/39,
    10/44/46, 25/42/33; other non-medical advice 13/42/44, 15/38/47, 28/42/30.
  - Annex B Table 1 "Forecasts of take-up under different rates of reimbursement" L1140-1146 (0/25/50/75/
    100%): all-employee schemes only 42/55/68/74/79; targeted schemes only 40/53/66/72/78; both
    53/66/77/82/86.
  - Annex B Table 2 "Forecasts of take-up of different levels of advice and guidance" L1160-1166 (No
    advice / Online resources / Personal adviser, at 50% reimbursement per L1158): all-only 60/68/69;
    targeted-only 58/66/67; both 70/77/78.
  - Numbering repeats inside D02: "Table 1" at L192, L824, L1140; "Table 2" at L838, L1160; "Figure 1"
    at L209, L1074.
- Lists: respondent types, 9 plus Total (L196-205); improved buying-support measures ranked "From most
  popular option to least popular", 6 items (L522-534: toolkit; provider database; online
  questionnaire; comparison website; information on the value of OH services; basic online information
  on procuring OH = last); barriers to innovating, 2 (L587-589); workforce aims, 3 (L625-629); fit note
  actions (L694-710); Annex A policy areas, 4 (L782-788); Annex B caveats, 4 (L1040-1046); conclusions
  summary (L766-770); IAPT/IPS actions (L107-109).
- Forecasts, guidance, deadlines, effective dates: March 2020 Budget non-taxable counselling, "The
  changes took effect from April 2020" (L157, L732); COVID-19 Mental Health and Wellbeing Recovery
  Action Plan published 27 March 2021 (L119); information and advice service design work "during 2021"
  (L303); Access to Work campaign January 2021 (L742); HEE e-learning module "(summer 2021)" (L704);
  hospital electronic fit notes "(from spring 2022)" (L708); National Disability Strategy "due to be
  published in 2021" (L764); Mintel forecast of OH opportunities "from 2021 onwards" (L462); Bank of
  England: investment not expected to recover "until at least 2022" (L468); Coronavirus SSP rebate
  "Take up of the scheme has been lower than initially forecast" (L425, no figures); Annex B take-up
  forecasts with the caution that estimates "should be interpreted with extreme caution" (L1038).
- Hedged claims: L131 and L345 not proceeding with the right to request "at this stage"; L397 HSE
  "will strengthen existing non-statutory guidance before exploring the introduction of statutory
  guidance"; L441 and L768 "now is not the right time to introduce changes to the sick pay system";
  L135 the pandemic "was not the right time to introduce changes to the rate of SSP or its eligibility
  criteria"; L500 subsidy test to "inform the case for potential fixed term roll-out in the future";
  L794-796 package "may bring costs ... these costs are minimal"; L808 "could save employers between
  £5,000 and £11,000 ... (subject to the caveats detailed)"; L178 "This suggests that the disability
  employment rate is not currently being disproportionately impacted"; L311 numbers entitled to
  adjustments "could be increasing".
- Rounded prose beside exact figures: L808 "between £5,000 and £11,000" vs Table 3 totals £4,700 /
  £11,000 (L859); L948 "£2.9m", "£67 per medium or large employer", 43,975 businesses vs Table 5
  £2,937,000; L982 "approximately 18,600 LTSAs", "£3.2m every year", "£172 per employee on LTSA" vs Table
  6 £3,206,300; L881 "between £1,700 and £6,400" = Table 4; L1136 restates the "both" row of Annex B
  Table 1 with increments (+13, +11, +5, +4 points); L1158 "7–8 percentage points" = Annex B Table 2;
  L845 interviewing "around £700–800" vs values £500/£800/£1,000 (L846).
- Notes (main-text figures): L81 "Before COVID-19, an estimated 300,000 disabled people fell out of
  work every year" [fn4]; L115 working-age disabled people in employment +1.4m, from 3.0m to 4.4m,
  October-December 2013 to October-December 2019 [fn12]; L117 £5bn Restart Grants; L166 "Prior to
  COVID-19" 12.7m working-age with a long-term health condition incl. 7.6m disabled, 1.4m with at least
  one absence of four weeks or longer, disabled people 10 times more likely to have LTSA and leave work;
  L171 £160 billion first-phase support; L177 12 months to March 2021 disability employment rate -1.2
  percentage points, gap -0.2 points; L178 over half of COVID redundancies disabled or long-term
  condition; L190 485 responses submitted electronically; L251 separate stakeholder submissions
  (uncounted); L253 12 roundtables and 6 insight groups (right to request, SSP, OH); L255 772 responses
  from Mind; L359 over 400 resources (Mental Health at Work gateway); L367 "In 2018 around 1.4 million
  people experienced LTSA ... resulting in over 100,000 people falling out of work. Of these, 25,000 fell
  out within the first six weeks"; L369 79% regular meetings, 69% RTW plans; L413 7% of fit notes
  reference phased return; L417 LEL £120 per week; L419 75% agreed SSP should be extended below the
  LEL; L431 72% agreed on better SSP enforcement; L450 large employers "five times more likely to offer
  OH", "Over a third of employers who do not access OH services cite cost as the main barrier"; L466 up
  to an additional 8% of businesses newly purchased OH in the pandemic; L621 44% of OH providers have
  unfillable roles; L728 up to £500 recommended medical treatment; L867 SMEs with 1-249 employees "make
  up 99% of all businesses in the UK", half of small vs a quarter of large employers use the internet;
  L988 "five times", "one in six employers cited cost"; L1008 500 SME employers (at least 10 employees)
  and 30 interviews; L1052 over 80% cite MSK or mental health; L1066 70% provide a proactive scheme
  (58% of 10-19 vs 82% of 50-249), 39%/39%; L1120 barriers 49% expertise, 49% time/resources, 52%
  capital; L1136 take-up 53% → 66% → 77% → 82% → 86%.
- Notes (footnote figures): fn3 L1194 44% small vs 72% large proactive; fn11 L1226 Employment Advice in
  about 40% of IAPT services, 29,000 people in 2020/21 financial year; fn13 L1234 disability employment
  rate gap -5.3 points Q1 2014 to Q1 2021; fn14 L1238 CJRS 2.4 million furloughed May 2021, peak 5.1
  million January 2021, 11.6 million jobs supported; fn16 L1246 "18% of small employers, compared to 92%
  of large employers, invest in OH"; fn20 L1262 1-year LTSA 8 times more likely to leave than 4-week;
  fn59 L1418 99% / 96%; fn60 L1422 3% of all and 23% of large employers cite lack of knowledge; fn68
  L1454 54% aware of Isolation Note, 92% would accept; fn75 L1482 workers earning above £25,000; fn82
  and fn106 (L1510, L1606) one in 5 employers offered OH: large 92%, medium 49%, small 18%; fn84 and
  fn97 (L1518, L1570) 5% small vs 20% large used an HR team; fn85 L1522 disabled employees in small
  workplaces over 1.5 times more likely to fall out of work; fn95 L1562 sickness absence policy 25%
  small, 72% medium, 69% large; fn96 L1566 small employers 64% time/staff, 51% capital.
- Operative definitions, rules and scope exceptions: L417 below-LEL employees (LEL £120) do not qualify,
  "This includes those who have multiple jobs which are each paid below the LEL"; L411 "Payment of SSP
  stops when an employee returns to work, even if they return on reduced hours"; L405 COVID actions:
  SSP extended to employees self-isolating, Coronavirus Statutory Sick Pay Rebate Scheme for SMEs,
  waiting days temporarily suspended so SSP was payable "from the first day of a coronavirus-related
  sickness absence" [fn42 "Other SSP eligibility criteria applies."]; L367 LTSA "defined as a leave of
  absence for four or more weeks"; L445 scope of "OH services"; L564 innovation definition; size bands:
  Figure 1 micro 0-9 / small 10-49 (L213-214), Annex A small 1-49 (L941, L962) and "fewer than 50"
  (L931), medium/large "more than 50 employees" (L929) vs table "50–249" (L942), Annex B SMEs with at
  least 10 employees and micro <10 excluded (L1008, L1046); L347 EHRC enforcement scope.
- Amendments or contradictions:
  - Correction slip L41-69 (dated 23 September 2021) states that P.30 "Research conducted by the Society
    of Occupational Medicine (SOM) during the early stages of the crisis ..." and P.32 "A survey by the
    Society of Occupational Medicine (SOM) conducted in April 2020 ..." should read "The At Work
    Partnership". The body text still carries the uncorrected attributions at L447 [footnote 47] and
    L464 [footnote 55]; both footnotes cite Ballard J., "An exclusive survey for Occupational Health [at
    Work]" (L1370, L1402). The slip's corrected P.30 text drops the footnote marker. SOM also appears at
    L615 as a named partner for the Centre for Work and Health Research; the slip does not mention L615.
    Document-stated precedence: the slip says "Text should read".
  - L450 "Over a third of employers who do not access OH services cite cost as the main barrier" [fn50]
    vs L988 "one in six employers cited cost as a reason for not providing access to OH" [fn107].
  - L808 lower bound "£5,000" vs Table 3 lower total £4,700.
  - L131 executive-summary sentence is garbled as captured ("In particular In light of feedback ...
    we heard concerns that ...").
- Coverage: full. Ledger: L1-160, L160-309, L309-448, L448-577, L577-706, L706-825, L825-954, L954-1083,
  L1083-1232, L1232-1451, L1451-1631 (EOF). Remaining: none.

## D03 (task page Doc 5) - Government response: Making Work Pay: Strengthening Statutory Sick Pay (DWP, © 2025)

- Source: text/D03.txt (L1-268) from docs/Government-response-Making-Work-Pay-Strengthening-Statutory.txt; no pages.
- Written or submitted by: DWP (masthead L4-5); no minister named; enquiries `ssp.team@dwp.gov.uk` (L27).
  Respondents quoted anonymously: "One employer respondent" (L115), "One employee" (L154, L158), "One
  trade union or representative organisation" / "One trade union or other representative organisation"
  (L156, L161).
- Type, date, edition: government response (URL L13 ".../outcome/government-response-making-work-pay-
  strengthening-statutory-sick-pay"); CP 1275 (L15); ISBN 978-1-5286-5382-4 (L29); print code
  "E03273303 03/25" (L31); © Crown copyright 2025 (L7, L17). No explicit publication day or month in the
  text. L25 "See Making Work Pay: Strengthening Statutory Sick Pay".
- Period covered: ERB introduced 10 October 2024 (L35); consultation published on Gov.uk 21 October
  2024, "open for six weeks and closed on 4 December 2024" (L51); flat rate "currently £116.75 per week,
  increasing to £118.75 in April 2025 subject to parliamentary approval" (L53); LEL "frozen in 2021,
  2023 and 2024" (L176); costs per year (L194-195).
- Entities and aliases: Employment Rights Bill (L35 and passim); Plan to Make Work Pay (L35, L37, L184);
  Next Steps to Make Work Pay (L47, L204); New Deal for Working People (L73); "Department of
  Communities" and "Department for Communities in Northern Ireland" in the same paragraph (L45);
  Northern Ireland Assembly Legislative Consent Motion (L45); Equality Analysis (L51) also called
  "Equality Impact Assessment" (L171); Regulatory Impact Assessment / "published impact assessment"
  (L109, L118-120, L125, L167, L218; not in bundle); Support with Employee Health and Disability (L128);
  Keep Britain Working, independent review led by Sir Charlie Mayfield (L133, L263); Get Britain Working
  white paper (L204, L265); Percentage Threshold Scheme (L223, L225); National Living Wage (L200, L229);
  Statutory Maternity Pay (L229); Industrial Strategy (L263).
- Tables: 2 pipe tables. Figure 2 L91-99 (business/employer representatives; base 275 "employers and
  employer representative groups (hereafter referred to as 'employers')", L103): 0 to 20% 24%; 20 to 40%
  19%; 40 to 60% 21%; 60 to 80% 12%; 80 to 100% 24% (map check: 100). Figure 3 L137-145
  (employees/members of the public; base 157, L149): 0 to 20% 4%; 20 to 40% 6%; 40 to 60% 14%; 60 to 80%
  4%; 80 to 100% 71% (map check: 99). Band edges are shared (20, 40, 60, 80); the document does not say
  which band holds an edge value. Figure 1 (L77-81) is chart-only: modes "overall was 100%, for members
  of the public was 100%, and for businesses was 0%"; base 499.
- Lists: unique-response breakdown, 3 bullets (L61-65: 55% businesses and/or employers; 30% public
  and/or employees; "the remaining 15% of respondents included trade unions, charities or other
  respondents"); further-reform suggestions, 4 bullets (L241-247; last "extending the duration of SSP
  from 28 weeks to 52 weeks"); stakeholder groups met (L53); formats offered (L51).
- Forecasts, guidance, deadlines, effective dates: decision "We now plan to set this percentage rate as
  80% of normal weekly earnings, which will apply where 80% of an employee's normal weekly earnings is
  less than the flat rate. This will be set in law through a government amendment to the Employment
  Rights Bill." (L41; repeated L184); "An amendment to include the percentage rate in the Employment
  Rights Bill will be brought forward for consideration at Report Stage in the House of Commons" (L261);
  Northern Ireland: amendments to extend the changes incl. the 80% rate, "subject to the approval of a
  Legislative Consent Motion by the Northern Ireland Assembly" (L45); no plans to reduce the 7-day
  self-certification period (L219); annual uprating continues (L235). No commencement or implementation
  date for the SSP changes is stated (searched).
- Response counts: 1,797 responses; 530 unique; 499 suggested a percentage rate; "Unique responses are
  those that were not identical written responses" (L55). Percentages of the 530 unique (L59-65). Bases
  499 (L81, L85), 275 employers (L103), 157 employees (L149). "We received 1257 duplicate responses which
  welcomed the removal of the waiting period and the Lower Earnings Limit, but did not specify a
  particular percentage rate" (L229). Medians: employers 50%, "lower than the overall median rate for
  all respondents" (L105; overall median not given); employees 90% (L151). "44% of employees suggested
  the percentage rate should be set at 100%" (L158). "Over a third of employers suggested a percentage
  rate over 60%" and "23% of employers suggested a 0% percentage rate" (L112). "Around a quarter of
  employers and employer representatives were concerned about the disproportionate cost impact to small
  and medium-sized employers" (L125).
- Cost figures: L121 "The difference between the 60% and 80% examples ... amounts to approximately £30
  million across the whole labour market, which is around £1 per employee or less than 0.01% of total
  spending on wages annually"; L194 "A rate of 60% would cost employers £1.04 billion (£37 per employee)
  per year, whilst 80% would cost employers £1.07 billion (£38 per employee)"; L195 "the total amount
  saved by businesses at 60% (compared to an 80% rate) is around £10 million to £30 million per year
  ... around £1 difference per employee per year"; L196 these are "the total annual cost of Statutory
  Sick Pay to employers, including the costs of removal of waiting days and removing the Lower Earnings
  Limit"; L120 and L197 most of the cost increase comes from removing the waiting period.
- Worked examples and other figures: L169 10 hours a week for three companies "could receive 3 times
  more SSP" than 30 hours for one company; L175 SSP "approximately 95% of the Lower Earnings Limit";
  L176 "historically just under 80% of the Lower Earnings Limit until the latter was frozen in 2021,
  2023 and 2024"; L177 alternative system up to 100% replacement; L178 "one penny in average weekly
  earnings making nearly a £24 difference in entitlement"; L192-193 £110 per week: currently no SSP,
  £88 at 80%, £66 at 60%; L200 average £125, two days a week (about 5 hours a day at National Living
  Wage) "cumulatively be entitled to more SSP for the first 9 weeks"; L212 and L219 self-certification
  currently 7 days; L223 PTS "abolished in 2014"; L233 "Around 60% of all employees are eligible for
  occupational or contractual sick pay"; L73, L202, L231, L249 "up to 1.3 million employees" newly
  eligible.
- Hedged claims: L109 "these changes may result in increased absenteeism, however ... risks of
  inappropriate absenteeism can be mitigated"; L118 cost "likely to be offset in part by increased
  levels of productivity"; L119 "expected in turn to reduce"; L125 "likely to be small additional costs
  ... these will likely be offset"; L186 80% "should still encourage employees to return to work"; L200
  "Our internal modelling suggests that employees will not, over the course of their sickness absence,
  be worse off"; L202 "While this may occur in some specific circumstances"; conditional decisions L45
  (LCM) and L53 ("subject to parliamentary approval").
- Rounded prose beside exact figures: L101 and L147 restate Figures 2 and 3; L112 "Over a third ...
  over 60%" vs bands 60-80% 12% and 80-100% 24%; L112 "23% ... 0%" vs band 0-20% 24%; L158 44% at 100%
  vs band 80-100% 71%; L121 "approximately £30 million" vs L195 "around £10 million to £30 million".
- Operative definitions, rules and scope exceptions: L83 "A person will be entitled to the lower of the
  existing weekly rate of SSP ('the flat rate') or a defined percentage of their normal weekly earnings
  ('the percentage rate')"; L53 "a specified percentage of their weekly earnings or the existing flat
  rate of SSP, whichever is the lower"; L186 "the lower of 80% of average weekly earnings or the flat
  rate". "Normal weekly earnings" (L41, L83) and "average weekly earnings" (L178, L186) are both used;
  neither is defined in D03 or elsewhere in the bundle (searched). L71 LEL removed "as an entitlement
  condition"; L169 multiple-jobs rules unchanged; L45 changes apply to England, Wales and Scotland,
  extension to NI conditional; L53 flat rate not consulted on.
- Amendments or contradictions: L121 vs L195 (single figure vs range for the same 60%/80% comparison);
  "Equality Analysis" (L51) vs "Equality Impact Assessment" (L171); "Department of Communities" vs
  "Department for Communities" (L45); L178 "encouraging employees to keep part-time employees earning
  below a certain amount" (as printed).
- Coverage: full. Ledger: L1-268 read sequentially (single chunk). Remaining: none.

## D04 (task page Doc 1) - Health is everyone's business: proposals to reduce ill health-related job loss (DWP/DHSC, July 2019)

- Source: text/D04.txt (L1-2251) from docs/Health-is-everyones-business-proposals-to-reduce-ill.txt; no pages.
- Written or submitted by: DWP and DHSC (mastheads L4-9); "Presented to Parliament by the Secretary of
  State for Work and Pensions on behalf of the Department for Work and Pensions and the Department of
  Health and Social Care by Command of Her Majesty." (L21). Ministerial foreword unsigned (L60-74). DHSC
  also written "Department for Health and Social Care (DHSC)" (L50). Case-study organisations and cited
  bodies are mentions, not authors (Sainsbury's L357-365, Taylor Review, etc.).
- Type, date, edition: consultation (URL L19); July 2019 (L23); CP 134 (L25); ISBN 978-1-5286-1364-4
  (L27); "published under the 2016 to 2019 May Conservative government" (L11); "© Crown copyright 2021"
  (L13). Consultation principles of March 2018 (L33). No closing date in D04 (searched; dates appear in
  D02 L190). Workshops "during the consultation period" (L393, L1590).
- Period covered: 2019 rates (LEL £118, SSP £94.25); evidence mostly 2014-2019 studies; Access to Work
  "2017 to 2018" (L343); Q1 2019 disabled employment (fn9 L1774); OH workforce 2005/2009-2018 (L1104,
  L1112); SEQOHS "as of June 2019" (L1318).
- Entities and aliases: OH = occupational health (L66); SMEs; PIW = period of incapacity to work (L678);
  OSP (L914); HMRC (L788); Acas (L812); Taylor Review of Modern Working Practices / "Taylor" (L97, L149,
  L526, L630, L732, L738, L780, L818, L840); Good Work Plan (December 2018, L149, L818, L840); Thriving at
  work: the Stevenson/Farmer review (L151, L630, L1444); Improving Lives (L159, L175, L186); Prevention is
  Better than Cure (L153); Ageing Society Grand Challenge (L155); NHS Long Term Plan (L175); Industrial
  Strategy (L147); Federation of Small Businesses (L191); Access to Work (L195, L341-347); Disability
  Confident (L195, L347, L1424, L1536); Jobcentre Plus (L347, L846); German model (L502-512); Netherlands
  approach, "Gatekeeper" (L900-908); Sweden (L900, L938); Percentage Threshold Scheme (PTS) (L886);
  National Minimum Wage / National Living Wage (L790, L810-816); Maternity Allowance, Statutory Maternity
  or Paternity Pay (L730, L736); Universal Credit (L730, L844, L910); SSP1 form (L844); SEQOHS (L1314-1348);
  Faculty of Occupational Medicine (L1172, L1314); Royal College of Physicians (L1314); National School
  of Occupational Health (L1114, L1166, L1172); Health Education England (L1166, L1172); General Medical
  Council (L1104); Nursing and Midwifery Council (L1114); Skills for Health (L1138-1158); Council for
  Work and Health (L1040, L1132); All-Party Parliamentary Group on Occupational Safety (L1040; bibliography
  "Occupational Safety and Health" L1612); Dame Carol Black, "Working for a healthier tomorrow" (2008)
  (L1246, L1314); What Works Centres / Centre for Ageing Better (L1250, L1272-1278); Productivity
  Insights Network, UK Prevention Research Partnership (L1250); Cornwall and Isle of Scilly LEP "Beacon
  Project" (L1432-1434); Fit for Work (L1440, L1540-1544); HSE (L1423, L1440, L1484); "Time to Talk"
  (L1536); OH Expert Group (L1590).
- Tables: none (0 pipe tables). Figures sit in prose, boxes, worked examples, 128 footnotes
  (L1740-2250) and a bibliography (L1610-1738).
- Lists: four proposal areas (L161-169); chapters (L201-207); most common OH services, 5 (L251-259);
  legal-framework changes, 3 (L327-331); illustrative modifications, 4, "illustrative and not
  exhaustive" (L401-409); SSP reform proposals, 3 (L582-586); SSP qualifying conditions, 4 (L598-604);
  phased-return change features, 3 (L636-640); qualifying-day simplification, 3 (L686-690); rebate
  options, 4 (L870-876); rebate principles, 3 (L880-884); tax-free health benefits in kind, 7
  (L950-962); subsidy routes, 2 (L972-974); OH workforce actions, 4 (L1046-1052); SEQOHS core standards,
  6 (L1320-1330); revised standards, 5 (L1336-1344); standards approaches, 4 (L1356-1368); dissemination
  components, 6 (L1260-1270); ERA 1996 five potentially fair reasons (L482). Numbered consultation
  questions: 56 (Question 1 L295 to Question 56 L1598). SSP questions 16-26 (L612-922): Q16 L612; Q17
  phased returns L666; Q18 qualifying days L714; Q19 extend below LEL L742; Q20 80% of earnings L754;
  Q21 accrual L766; Q22 fines L794; Q23 NMW-style enforcement L822; Q24 SSP1 four weeks before end L850;
  Q25 rebate L890; Q26 rate and length L922. Q4 eligibility options, 5 (L435-443); Q46 "As a provider,
  what indicators of quality could help improve the standard of services in the OH market?" (L1392);
  Q53 buying-support options, 6 (L1520-1530, order: online questionnaire; toolkit; basic online
  information; provider database; comparison website; information on the value of OH services).
- Proposals and stated positions (2019; for outcomes see Shared ground):
  - Phased returns: "The government will amend SSP regulations to enable an employee returning from a
    period of sickness absence to have a flexible, phased return to work" (L632); part wage plus part
    SSP pro rata (L636); "after 2 or more weeks of absence" (L638); full sick days count toward the
    28-week maximum, part-days do not, only during a phased return; flexibility only on return, not at
    the start of absence (L642); GOV.UK calculator (L644); no legislation on how requests are made
    (L660); OSP employers to use pro rata as a minimum (L662).
  - Qualifying days: "The government could remove this rule" (L684-690).
  - Below-LEL extension: Taylor recommended it; "This would extend SSP protection to around 2 million
    employees, including over 1 million who work less than 16 hours per week. The government believes
    there is a case to accept this recommendation." (L732). "If eligibility were to be widened in this
    way, the government proposes that those earning below the LEL would be paid a proportion of their
    wage as SSP, set at 80%[footnote 93]. Those earning above the LEL would continue to receive a flat
    rate." (L734). LEL removal for SSP only; no change to other statutory payments (L736).
  - Accrual: "The government is not currently persuaded" (L738).
  - Enforcement: could increase fines (L788); case for NMW-style enforcement (L806); will consider SSP
    within a single labour market enforcement body (L818).
  - Day one written statement: government "intends to bring forward legislation" (L840).
  - SSP1 earlier notification considered (L844-850).
  - SME rebate: "not asking for a view on a particular proposal at this stage" (L878).
  - Rate and length: "government does not intend to change the rate or length of SSP at this time"
    (L918); "not proposing to make any further changes to the structure of SSP beyond the reforms
    outlined above" (L592).
  - Right to request work(place) modifications (L90, L367, L381-421; Q3-Q7 L425-468); strengthened
    statutory guidance (L92, L516-526; Q8-Q15); not pursuing prescriptive return-to-work plans (L514).
  - OH subsidy or voucher (L105, L940, L970-978; Q27-Q32), "not committing at this stage" (L940).
  - Tax: "no plans to make further reforms in this area at this time" (L966).
  - Sickness absence reporting through payroll explored (L123, L1554-1556; Q54-Q55).
  - Working Age Health Research and Development Network considered (L1252).
- Notes (main-text figures): L64 and L217 "around 300,000 people with a long-term mental health
  condition fall out of work every year" [fn40]; L66 NHS "additional £20.5 billion a year settlement";
  L97, L604, L728 LEL £118 per week; L105, L265, L936 small employers "5 times less likely" to invest in or
  provide OH; L135 around 5 in 10 disabled vs 8 in 10 non-disabled in work; L137 "300,000 disabled people
  leave work every year", "10 times more likely to leave work following long-term sickness absence",
  ill health costs the economy around £100 billion a year, sickness absence costs employers £9 billion a
  year; L155 1 in 5 aged 50-64 left their last job for health reasons; 5 extra healthy years by 2030;
  L159 1 million more disabled people in work by 2027; L191 SMEs "over 99.9% of all private sector
  businesses", 50% of employed disabled people in small businesses (<50 employees) vs 47% of
  non-disabled; L193 "Almost 10% of small employers do not take action ... and only 21% of small
  employers provide OH compared with 92% of large employers" [fn29]; L195 Disability Confident over
  11,000 employers; L213 12.7 million working-age with a long-term condition incl. 7.6 million disabled,
  around half say health limits work, one in three with physical conditions also have mental illness;
  L215 around 1.4 million with an absence of 4 weeks or longer, about 4%; L281 OH market around £800
  million a year, about half of employees have OH access; L343 nearly 34,000 Access to Work recipients
  2017-18; L345 9 months Mental Health Support Service; L373 26 weeks for flexible-working requests; L375
  3 months; one request a year; agency workers excluded; L383 1.4 million; L506 Germany more than 6
  weeks; L606 SSP from the fourth day at £94.25 per week for a maximum of 28 weeks, estimated employer
  cost £1.5 billion a year [fn88 Black & Frost 2011]; L648-658 phased-return example (£9 an hour, 35
  hours = £315; 2 hours x 5 days = £90; SSP for 25 hours £67.32 [fn92]; total £157.32); L688 average of
  last 8 weeks; L710 £94.25; L788 around 3,000 disputes a year, 90% resolved at first stage, 10% formal
  decision, 30-day appeal period, fines up to £3,000; L814 NMW penalties up to 200% of arrears, maximum
  £20,000 per worker; L838 written statement for employees of more than a month, within two months;
  L844 SSP1 no more than 7 days after entitlement ends; L850 4 weeks before end; L886 PTS until 2014,
  reclaim SSP above 13% of the monthly NIC bill; L900 most countries less than 10 weeks, Netherlands 70%
  of wages for 2 years; L906 1996 and 2002 Netherlands reforms; L914 "28% of employers provide
  occupational sick pay (OSP), or a combination of OSP and SSP"; L916 93% of returners after LTSA had
  absences of 6 months or less; L954 and L964 £500 medical treatment exemption (introduced 2015; 28
  days / 4 weeks; average treatment cost £150-£250); L1040 44% of providers unable to fill roles; L1104
  GMC-licensed OH specialists fell 16% to 569 (2009-2018), 53% of OH doctors over 55, specialist trainees
  178 (2005) to 69 (2018); L1112 OH nurse trainees 200 (2009) to roughly 80 (2018); L1172 NSOH formed
  2014; L1238 less than 15% of firms use external sources; L1314 SEQOHS developed 2010; L1318 187
  accredited OH services (as of June 2019); L1332 2015 clinical-effectiveness standards; L1346 review due
  2020; L1542 Fit for Work introduced 2014, assessment service withdrawn December 2017.
- Notes (footnote figures): fn9 L1774 disabled employment rate +7.5 points in 5 years to 51.7%, around
  3.9m disabled people in employment in Q1 2019, +around 950,000 in 5 years; fn19 L1814 91% / 90%; fn22
  L1826 wellbeing ratings 6.5/6.8/6.8 vs 7.5/7.8/7.4; fn26 L1842 small 0-49, medium 50-249, large 250+
  employees; fn28 L1850 80% vs 69%; fn29 L1854 "9% of small employers responded 'None of the above'";
  fn36 L1882 around 9 in 10 return, two-thirds within 2 months; fn37 L1886 around 10 times; fn38 L1890
  54% / 53%; fn43 L1910 8 times; fn44 L1914 4%; fn51 L1942 35% cost (22% + 13%) "for not providing access
  to OH services"; fn52 L1946 90% / 91%; fn53 L1950 two in 5; fn56 L1962 47% internet (47% small vs 25% large),
  formal paid-for services 49% large vs 7% small; fn59 L1974 6 of 10 providers; fn62 L1986 72% large vs
  44% small proactive; fn63 and fn66 (L1990, L2002) 46% small and 2% large do not collect absence data;
  fn64 L1994 15%, over a third; fn65 L1998 24%; fn71 L2022 24%, a third, 30%, 10%; fn72 L2026 Netherlands
  two years at 70%; fn73 L2030 a fifth; fn75 L2038 32%; fn76 L2042 just under three-fifths, 14%; fn77
  L2046 55/60/59%, 22% vs 10%; fn86 L2082 Gatekeeper reduced inflow by 15-33%; fn89 L2094 "54% of
  employers pay SSP only, 28% pay OSP or a combination of OSP and SSP. 18% ... did not pay either type
  ... or did not know"; fn92 L2106 "Calculated as £94.25 x (25/35 hours) = £67.32"; fn93 L2110 "This
  reflects the ratio of the SSP rate to the LEL, which is the maximum replacement rate in the current
  system."; fn102 L2146 61%; fn103 L2150 64% time/staff, 51% capital; fn104 L2154 35% (22% + 13%) "main
  barrier to supporting employees to return to work following a long-term sickness absence"; fn105
  L2158 "18% of small employers, compared to 92% of large employers, invest in OH"; fn106 L2162 64%, 50%
  capital; fn122 L2226 accessed 18 June 2019; fn123 L2230 43%; fn124 L2234 49%/25% large, 47%/27% small.
- Hedged claims: L732 "believes there is a case to accept"; L734 conditional "If eligibility were to be
  widened ... the government proposes"; L940 and L1216 "not committing at this stage"; L107 "There may be
  a role for government"; L1036 "market forces alone are unlikely to be sufficient"; L1370 "Subject to
  consideration of responses ... the government will explore"; L628 "This current system may deter ...
  Alternatively, it may prompt"; L906 Gatekeeper "appears to have reduced"; L916 "unlikely to support
  significantly more people"; firm statements: L632 "will amend SSP regulations", L918 "does not intend
  to change the rate or length of SSP at this time".
- Rounded prose beside exact figures: L193 "Almost 10%" vs fn29 9%; L193 21% vs fn105 18% (both against
  92% of large employers); "5 times less likely" (L105, L265, L936) beside fn105; L1104 "fell by 16% to
  569".
- Operative definitions, rules and scope exceptions: L141 long-term health condition (lasting or
  expected to last 12 months or more); L143 disabled (condition reduces ability to carry out day to day
  activities); L145 long-term sickness absence (four weeks or more); L596-604 SSP qualifying conditions:
  "employed earner" whose employer is liable for secondary Class 1 NICs; some work done under the
  contract; ill "for at least 4 or more days in a row (including non-working days)"; "earn an average of
  at least £118 per week"; L606 paid "from the fourth day of sickness absence at a flat rate of £94.25
  per week for a maximum of 28 weeks"; L678 PIW = sickness of 4 or more days in a row "(including bank
  holidays, weekends and non-working days)"; L680 "SSP is paid from the fourth qualifying day of
  sickness absence. The first 3 days are called waiting days."; L682 qualifying days normally contracted
  working days, may be agreed for varied patterns, exclude days when no employees work; "The weekly rate
  of SSP is the same, regardless of how many days a week an employee normally works"; L692-710 worked
  examples (current: Wednesday/Friday/Sunday qualifying days; proposed: paid from the second Monday at
  £94.25); L728 below-LEL employees, including those with several jobs each below the LEL, do not
  qualify; L730 no SSP equivalent of Maternity Allowance; L736 LEL also used for SMP/SPP; L482-498 ERA
  1996 dismissal tests; L373-377 flexible-working right; L351 "work(place)" scope; L367 and L397 a
  right-to-request could be refused on legitimate business grounds, unlike reasonable adjustments.
- Amendments or contradictions (internal, neutral): L193 [fn29] 21% vs fn105 L2158 18% for small
  employers' OH provision/investment (both against 92% large); fn103 L2150 capital barrier 51% vs fn106
  L2162 50% (same survey cited); fn51 L1942 and fn104 L2154 attach the same 35/22/13 split to differently
  worded questions; "300,000" describes people with a long-term mental health condition (L64, L217) and
  disabled people (L137); dated July 2019 with © 2021 (L13, L23).
- Coverage: full. Ledger: L1-200, L200-369, L369-538, L538-697, L697-856, L856-1015, L1015-1184,
  L1184-1353, L1353-1522, L1522-1701, L1701-1900, L1900-2099, L2099-2251 (EOF). Remaining: none.

## D05 (task page Doc 3) - Making Work Pay: Strengthening Statutory Sick Pay (DWP consultation, October 2024)

- Source: text/D05.txt (L1-279) from docs/Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt; no pages.
- Written or submitted by: DWP (masthead L4-5); "Presented to Parliament by the Secretary of State for
  Work and Pensions by Command of His Majesty" (L17); ministerial foreword by Alison McGovern, Minister
  for Employment (L55); enquiries `ssp.team@dwp.gov.uk` (L31); response address "The Statutory Sick Pay
  Team" (L218). Mentioned: Oxford Economics (L117), Department for Communities (L83).
- Type, date, edition: consultation; October 2024 (L19); CP 1168 (L21); ISBN 978-1-5286-5198-1 (L33);
  E03204748 10/24 (L35); "© Crown copyright 2025" (L9) and "Crown copyright 2024" (L23); "published
  under the 2024 to 2026 Starmer Labour government" (L7). "The consultation will be open until 4
  December 2024." (L227); opening date not stated in D05. Revised Cabinet Office Consultation Principles
  March 2018 (L233).
- Period covered: 2024 rates (LEL £123; SSP £116.75); cost model uses Family Resources Survey 2022/2023
  and DWP Employee Survey 2023 (L165); presenteeism cost compared with 2018 (L113). ERB "introduced
  earlier this month" (L61) and "laid in Parliament earlier this month" (L109); Next Steps to Make Work
  Pay "published earlier this month" (L93).
- Entities and aliases: SSP; LEL; Employment Rights Bill; Plan to Make Work Pay; Next Steps to Make Work
  Pay; Public Sector Equality Duty (PSED); Equality Analysis "will be published shortly" (L159);
  Regulatory Impact Assessment (L165; not in bundle); "2019 Health is Everyone's Business consultation"
  (L133); Department for Communities (L83).
- Tables: Table 1 "Comparison of Illustrations on Impact on Employees" L145-151. Columns: Maximum
  estimated number of employees who could receive a lower weekly rate / Weekly earnings range of
  employees affected / Estimated number of employees who would receive less SSP overall / Break-even
  point. 60% earnings: 1,300,000 / £123 to £195 / 0 / 2 weeks. 70%: 500,000 / £123 to £167 / 0 / 3 weeks.
  80%: 300,000 / £123 to £146 / 0 / 4 weeks. Description L143: break-even is for "an employee earning
  £123 per week working five days per week"; "(0)" is the internal estimate. Table 2 "Comparison of
  Illustrations on Impact on Business" L167-172 (Current system / 60% / 70% / 80%): Total costs £0.65
  billion / £1.04 billion / £1.06 billion / £1.07 billion; Per employee £23 / £37 / £37 / £38. Source
  L165 (internal DWP model, FRS 2022/2023, DWP Employee Survey 2023; details in the Regulatory Impact
  Assessment). Figure 1 (L139) and Figure 2 (L157): chart titles only.
- Lists: three groups invited (L69-77); two priorities (L105-107); three consultation questions (L192-210);
  Q1 respondent options, 5 (L194-202; last "Other (please specify)"); Q2 answer constraint "Number must be
  between 0 to 100" (L206); Q3 500-word suggested maximum (L210); footnotes 1-4 (L264-278).
- Forecasts, guidance, deadlines, effective dates: percentage rate to be specified in law "through
  government amendment to the Employment Rights Bill" (L131); views to inform "a decision on the
  earnings replacement rate" (para 38, L186); closing date 4 December 2024 (L227). No implementation
  date.
- Proposals: remove the LEL (L95, L119-123) and the waiting period (L95, L111-117); taper "whereby an
  employee is entitled to a certain percentage of their average weekly earnings or the current SSP flat
  rate, whichever is lower" (L127); illustrative examples "are not specific government proposals, or
  choices to select from ... They range from 60% of earnings, which is the lowest rate our internal
  modelling suggests would not leave employees worse off, to 80% of earnings, as proposed in the 2019
  Health is Everyone's Business consultation" (L133); flat rate not consulted on (L190); "The proposed
  changes in this consultation apply to England, Wales and Scotland only" with NI decisions resting with
  the devolved administration and NI views shared with the Department for Communities (L83).
- Notes (figures): L101 payable up to 28 weeks per period of sickness absence; L105 first 3 qualifying
  days; L107 LEL £123, "between 1 and 1.3 million individuals who earn below the LEL"; L113 up to 33% of
  influenza-like illnesses contracted in the workplace [fn1], 43.6 productive days lost to presenteeism
  per employee per year, "an increased cost of around £25 billion compared to 2018" [fn2]; L115 around
  15.9 million working-age people with a long-term health condition incl. 10.5 million disabled [fn3];
  L117 Oxford Economics: loss of an employee across 5 sectors (IT, Legal, Accounting, Media, Retail)
  "average financial impact of £30,614" [fn4]; L121 "up to 1.3 million employees are excluded from SSP",
  women and young people particularly benefit; L125 "many of those earning below the LEL also earn less
  than £116.75 per week"; L137 at 80% £100 earner gets £80, £150 earner gets the flat £116.75; £125.00
  earner gets £75 at 60% vs £116.75 currently; L153 two jobs at £125 each: £116.75 each, total £233.50,
  "93% earnings replacement rate", up to £200 at 80%; single £250 job: £116.75, "just under 47%"; L163
  removing the waiting period alone "around £1.02 billion (£36 per employee)"; L174 SSP costs "around
  0.06% of total spending on wages" rising to "around 0.09%"; L176 "small and micro businesses pay around
  60% of the annual SSP cost to employers and make up around 47% of businesses. Given 60% of the
  additional costs to businesses will be borne by 47% of the population, there will be a
  disproportionate burden".
- Hedged claims: L137 "may see a reduction in their weekly SSP entitlement"; L141 modelling "suggests"
  no one worse off at 60% or above; "could notionally receive a lower entitlement"; L143 "could
  nominally receive less per week"; L117 "are likely to remain in their roles for longer"; L123 "This
  potentially delivers benefits"; L155 "more likely to be effective"; L174 "the costs to business are an
  estimate", "difficult to predict", "may be different depending on the sector", "These changes may
  therefore only have a small impact on employers overall"; L163 "estimated to cost around".
- Rounded prose beside exact figures: L174 "range from £37 to £38 per employee" = Table 2 option
  columns; L141/L143 restate Table 1's zero column; L107 "between 1 and 1.3 million individuals" vs L121
  "up to 1.3 million employees"; L163 £1.02 billion (waiting period alone) sits beside Table 2's current
  £0.65 billion and option totals £1.04-£1.07 billion; the document does not reconcile them.
- Operative definitions, rules and scope exceptions: L101 SSP "is the minimum statutory payment an
  employee is entitled to for periods where they are unable to work due to illness. It is both
  administered and paid entirely by employers and is payable for up to 28 weeks per period of sickness
  absence."; L105 waiting days = "the first 3 qualifying days (days on which an employee is contracted
  or scheduled to work)"; L119-121 eligibility requires earnings of at least the LEL (£123); L123 ERB
  "repeals the exclusion on employees earning below the LEL"; L127 "whichever is lower"; L83 territorial
  scope.
- Amendments or contradictions: L176 moves from "annual SSP cost" and "47% of businesses" to
  "additional costs" and "47% of the population" (as printed); copyright years 2025 (L9) and 2024 (L23).
- Coverage: full. Ledger: L1-279 read sequentially (single chunk). Remaining: none.

<!-- Read actual candidate-relevant passages with context and search the entire bundle for
duplicates/substitutes. A search is not a full read. Expand coverage when the candidate needs it;
lists/counts require the complete relevant universe, and needed gaps stay blocking. -->

## Shared ground (navigation only)

- Entities that appear in more than one document, and where:
  - Issuers: DWP in all five (D04 L4, D02 L4, D05 L4, D01 L4, D03 L4); DHSC only in D04 (L8, L21, L50)
    and D02 (L8, L21). Secretary of State for Work and Pensions presents D04 (L21), D02 (L21), D05 (L17).
    Named ministers: D02 L89-93 (Tomlinson, Churchill); D05 L55 (McGovern); none in D04, D01, D03.
  - Employment Rights Bill: D05 (L51, L61, L93, L109, L123, L131), D01 (L67, L89), D03 (L35, L41, L73,
    L184, L208, L249, L261, L263). Plan to Make Work Pay: D05, D01, D03. Next Steps to Make Work Pay: D05
    L93, D03 L47/L204. None of these in D04 or D02.
  - Percentage Threshold Scheme: D04 L886 (in place "Until 2014"; reclaim above 13% of monthly NIC bill;
    "administratively complex and was underused"); D03 L223 ("abolished in 2014"), L225 (review: "complex
    and expensive to administer, was underused by small businesses").
  - Equality Analysis: D05 L159 (to be published shortly), D01 (the analysis itself, November 2024),
    D03 L51 (published) and L171 ("Equality Impact Assessment findings").
  - Regulatory Impact Assessment (not in bundle): D05 L165; D03 L109, L118, L120, L125, L167, L218.
  - Oxford Economics staff-turnover study: D05 L117 and fn4 L278 ("Brain Drain report"; 5 sectors IT,
    Legal, Accounting, Media, Retail; £30,614); D02 Annex A L812-818, L828, L836 and fn73/74/78
    (L1474-1494, "The cost of Brain Drain", February 2014; about 500 employers; five sectors Retail, IT and
    Technology, Legal, Accounting, Media and Advertising; employees earning at least / above £25,000,
    L816, L1482).
  - ONS A08 "Labour market status of disabled people": D04 fn9/fn10/fn32 (2019), D02 fn12/13/18/24
    (July 2021), D05 fn3 L274, D01 fn2 L452.
  - Northern Ireland: D05 L83, D03 L45, D02 L237 (respondent region 3%), D01 L248 (FRS religion data
    separate). Department for/of Communities: D05 L83; D03 L45 (both spellings).
  - Universal Credit: D04 L730, L844, L910; D02 L417; D01 L65; D03 L202. National Living Wage: D04 L812;
    D03 L200, L229. Statutory Maternity Pay: D04 L730, L736; D03 L229.
  - HSE: D04 L1423, L1440, L1484; D02 L129, L395-397, L615. SEQOHS: D04 L1314-1348; D02 L490, L546, L556,
    fn62 L1430. Access to Work: D04 L195, L341-347, L1462; D02 L159, L351, L355-357, L734-746.
    Disability Confident: D04 L195, L347, L1424, L1536; D02 L159, L281, L399, L740. Fit for Work: D04
    L1440, L1540-1544; D02 L506. Improving Lives / 1 million more disabled people in work by 2027: D04
    L159; D02 L78, L97, L182. Stevenson/Farmer: D04 L151, L630, L1444; D02 L359 (Thriving at Work
    Leadership Council). Single enforcement body: D04 L99, L818 ("single labour market enforcement
    body"); D02 L433 ("Single Enforcement Body"). Fit note: D04 L175, L281; D02 L147-153, L413, L678-710.
  - "Biggest upgrade to workers' rights": D04 L149 (Good Work Plan, "in over 20 years"); D03 L35 (ERB,
    "in a generation").
  - Organisations only in one document: SOM, The At Work Partnership, Mind, RAND, GRiD (D02); Sainsbury's,
    Taylor Review, Skills for Health (D04); Keep Britain Working / Sir Charlie Mayfield (D03); Oxford
    Economics also D02.
- Periods or series that more than one document covers, and where:
  - Lower Earnings Limit (per week): £118 (D04 L97, L604, L728; July 2019); £120 (D02 L417; July 2021);
    £123 (D05 L107, L121; D01 L45, L153, L157; October/November 2024). D03 gives no LEL value; D03 L176
    says the LEL was "frozen in 2021, 2023 and 2024".
  - SSP flat weekly rate: £94.25 (D04 L606, L710, fn92 L2106); £116.75 (D05 L125, L137, L153, L190, L204;
    D01 L45, L87, L153 and analysis paragraphs; D03 L53 "currently"); £118.75 "in April 2025 subject to
    parliamentary approval" (D03 L53). D02 states no SSP rate.
  - Replacement-rate statements: D04 fn93 L2110 (80% reflects SSP/LEL ratio, "the maximum replacement
    rate in the current system"); D03 L175-176 (now about 95% of LEL; historically just under 80% until
    the LEL freezes); D01 L424 (95% for a £123 earner); D05 L153 (93% two-job example; just under 47% at
    £250).
  - 28-week maximum: D04 L606, L642, L738, L910; D05 L101; D03 L158; D03 L247 (suggestion to extend to 52).
  - Waiting days / fourth day: D04 L606, L680 (2019 rule); D02 L405 (temporarily suspended for
    coronavirus-related absence); D05 L105; D01 L45, L117; D03 L212. Four-day period of incapacity: D04
    L602, L678; D01 L45.
  - Qualifying-day definitions: D04 L680-682 ("normally an employee's contracted working days", may be
    agreed); D05 L105 ("contracted or scheduled to work"); D01 L45 ("contracted or scheduled to usually
    work").
  - Percentage/flat-rate interaction: D04 L734 (2019: below-LEL earners at 80% of wage, above-LEL earners
    flat rate); D05 L127 (percentage of average weekly earnings or flat rate, "whichever is lower"); D01
    L87 (percentage of earnings or £116.75, "whichever is lower"); D03 L41, L53, L83, L186 (80%; "normal
    weekly earnings" vs "average weekly earnings"; undefined).
  - Consultation windows: 2019 launched 15 July 2019, closed 7 October 2019 (D02 L190; D04 itself says
    only July 2019, L23). 2024: D05 dated October 2024 (L19), "open until 4 December 2024" (L227); D03
    published on Gov.uk 21 October 2024, open six weeks, closed 4 December 2024 (L51); D01 "6 week
    Consultation" (L89). ERB introduced 10 October 2024 (D03 L35); D05 L61/L109 "earlier this month".
  - Response counts and respondent typologies: 2019: 485 online responses by 9 types (D02 L190, Table 1
    L194-205), separate stakeholder responses (L251), 12 roundtables and 6 insight groups (L253), 772 Mind
    responses (L255). 2024: 1,797 / 530 unique / 499 with a rate (D03 L55), 1257 duplicates (L229), 3
    groupings of unique responses (L59-65), bases 275 and 157 (L103, L149); D05 Q1 offers 5 respondent
    categories (L194-202).
  - "Other" categories (different bases): D02 Table 1 "Other" 102 respondents, 21% of 485 (L204); D02
    Figure 1 industry "Other services" 37% of employer respondents (L249; prose L207); D03 "the remaining
    15% ... trade unions, charities or other respondents" of 530 unique (L65); D05 Q1 option "Other
    (please specify)" (L202); D04 question options "other (please state)" / "other – please state"
    (e.g. L443, L466, L550); D01 "Other ethnic group" 1/2/2 (L233), sexual orientation "Other" 0/1/1
    (L302), "Any other religion, please describe" 3/2/1 (L262).
  - Employees below the LEL: D04 L732 "around 2 million employees, including over 1 million who work less
    than 16 hours per week" (extension estimate in the Taylor context, 2019); D05 L107 "between 1 and 1.3
    million individuals"; D05 L121 "up to 1.3 million employees"; D01 L47 "around 1 to 1.3 million
    employees" (Q1 FY 2022/23; excludes self-employed; fn1 FRS 2022/23 + LFS 2022), L85 "an estimated 1
    to 1.3 million", L123 "around 1 million employees", L157 "around 1 million" of 28.5 million (FRS
    2022/23), L281 263,000 + 717,000; D03 L73, L202, L231, L249 "up to 1.3 million employees". D02 gives no
    count.
  - Employees just above the LEL: D05 Table 1 (1,300,000 / 500,000 / 300,000 by option; ranges £123-£195 /
    £123-£167 / £123-£146, L149-151); D01 L129 "up to 300,000", L157 "around 300,000 ... between £123 and
    £146", L282 88,000 + 245,000. D05 Table 1's 60% row (1,300,000) has the same magnitude as the "up to
    1.3 million" below-LEL figure but describes a different population.
  - Break-even and loss examples: D05 Table 1 (2/3/4 weeks; £123 earner, five days, L143); D01 Case study
    1 (five days, £123; L424 notionally worse off from 4 weeks at 80%) and Case study 2 (£175; always
    better off, L444); D03 L200 (£125 average, two days a week, more SSP for the first 9 weeks); D01 L131
    ("up to £4 per week after 5 weeks").
  - Employer cost of SSP: D04 L606 "£1.5 billion a year" (fn88 Black & Frost 2011); D05 Table 2 current
    system £0.65 billion (£23 per employee) and options £1.04/£1.06/£1.07 billion (£37/£37/£38) (L171-172;
    model L165); D05 L163 waiting-period removal about £1.02 billion (£36 per employee); D05 L174 0.06% to
    0.09% of wage spending; D03 L194 60% £1.04 billion (£37), 80% £1.07 billion (£38) per year; D03 L121
    "approximately £30 million" difference; D03 L195 "around £10 million to £30 million per year". Other
    cost aggregates: D04 L137 £9 billion (sickness absence, employers), £100 billion (economy); D05 L113
    £25 billion (presenteeism vs 2018); D02 Annex £2.9m one-off (L948) and £3.2m a year (L982).
  - Weekly entitlement examples: D04 L648-658 (phased return, 2019 rate); D05 L137, L153; D03 L169,
    L192-193, L200; D01 case studies L409-444.
  - Survey sources and years: FRS 2022/23 (D01 L157, fn1 L448) = "Family Resources Survey 2022/2023"
    (D05 L165); DWP Employee Survey 2023 (D05 L165; D01 L159); LFS 2022 (D01 fn1 L448). The employer survey
    "Sickness absence and health in the workplace: understanding employer behaviour and practice" is cited
    as a 2019 interim summary report in D04 footnotes and as "Tu T and others ... report number 981 July
    2021" in D02 footnotes. D02 Annex B (RAND) survey of 500 SMEs carried out in 2018 (L1008, L1046).
  - Disability employment: D04 L135 (about 5 in 10 vs 8 in 10); D04 fn9 L1774 (51.7%; about 3.9m employed
    Q1 2019; +about 950,000 over 5 years); D02 L115 (+1.4m, 3.0m to 4.4m, Oct-Dec 2013 to Oct-Dec 2019);
    D02 L177 (12 months to March 2021: rate -1.2 points, gap -0.2 points); D02 fn13 L1234 (gap -5.3 points,
    Q1 2014 to Q1 2021); D01 L385 (gap 28.6 percentage points as of June 2024).
  - Long-term health conditions: D04 L213 and D02 L166 (12.7m incl. 7.6m disabled; D02 "Prior to
    COVID-19"); D05 L115 (15.9 million incl. 10.5 million disabled).
  - Long-term sickness absence 1.4 million: D04 L215 (about 4%), L383; D02 L166, L367 (2018; over 100,000
    fell out of work; 25,000 within six weeks). Definitions: D04 L145 (four weeks or more); D02 L367 (four
    or more weeks).
  - "300,000 a year": D04 L64 and L217 (long-term mental health condition); D04 L137 (disabled people);
    D02 L81 (disabled people, before COVID-19).
  - "10 times" / "8 times": D04 L137, fn37 L1886 and D02 L166; D04 fn43 L1910 and D02 fn20 L1262 (same
    wording).
  - Small vs large employers and OH: D04 L105, L265, L936 ("5 times less likely"); D04 L193 (21% vs 92%,
    fn29); D04 fn105 L2158 (18% vs 92%); D02 L139 ("five times less likely to invest", fn16 18% vs 92%);
    D02 L450 and L988 ("five times more likely to offer", fn48; fn82/fn106 large 92%, medium 49%, small
    18%). Unfilled OH provider roles 44%: D04 L1040 (fn111 → 2019 interim provider survey) and D02 L621
    (fn67, Tindle report 985, May 2020). Proactive employers: D04 fn62 L1986 and D02 fn3 L1194 (72% large
    vs 44% small). Small-employer barriers: D04 fn103 L2150 (64%, 51%), fn106 L2162 (64%, 50%); D02 fn96
    L1566 (64%, 51%); D02 Annex B L1120 (RAND: 49%, 49%, 52%). Cost as a barrier: D04 fn51 L1942 and fn104
    L2154 (35% = 22% + 13%); D02 L450 ("Over a third" of non-accessing employers) and L988 ("one in six").
  - Sick-pay provision: D04 L914 and fn89 L2094 (employers: 54% SSP only, 28% OSP or OSP+SSP, 18% neither
    or don't know); D03 L233 (employees: "Around 60% of all employees are eligible for occupational or
    contractual sick pay"); D01 L159, L163 (Employee Survey 2023 probability of SSP vs OSP).
  - Business-size definitions: D04 fn26 L1842 (small 0-49, medium 50-249, large 250+); D04 L191 (small =
    fewer than 50; SMEs over 99.9% of private sector businesses); D02 Figure 1 L213-216 (micro 0-9, small
    10-49, medium 50-249, large 250+); D02 Annex A L929, L931, L941-943, L962-964 (small 1-49; "more than
    50" for medium/large); D02 L867 (SMEs 1-249 = 99% of all UK businesses); D02 Annex B L1008, L1046
    (SMEs at least 10 employees; micro <10 excluded); D05 L176 (small and micro about 47% of businesses;
    no size bands given); D03 L125 ("small and medium-sized employers").
  - Tax-free medical treatment up to £500: D04 L954, L964 (introduced 2015); D02 L728. Non-taxable
    counselling from April 2020: D02 L157, L732 (D04 L950 lists welfare counselling as already exempt).
- Documents that cite, amend or respond to another document in the bundle:
  - D02 responds to D04: title L45-47; L99; L165; L186 ("This document forms the government's response
    to the 'Health is everyone's business' consultation"); Annex A L780; fn62 L1430 refers to "Q.46,
    'As a provider, what indicators of quality could help improve the standard of services in the OH
    market?'", which is D04 Question 46 (L1392).
  - D03 responds to D05: L25 ("See Making Work Pay: Strengthening Statutory Sick Pay"), L39, L51, L53, L83.
  - D01 is the Equality Analysis announced in D05 L159 and reported published in D03 L51 (and called
    "Equality Impact Assessment" in D03 L171); D01's URL (L15) sits under the D05 consultation path and
    its subtitle (L17) names that consultation.
  - D05 L133 cites the 2019 consultation (D04) as the source of the 80% example; D04's 80% is at L734
    (proposal) and L754 (Question 20). D02 does not mention an 80% rate (searched "80%"; only L1052,
    unrelated).
  - D02's correction slip (L41-69) amends D02's own body text (L447, L464); no document amends another.
  - Cited but absent from the bundle: Regulatory Impact Assessment (D05, D03); Taylor Review, Good Work
    Plan, Improving Lives (D04, D02); Get Britain Working, Keep Britain Working, Next Steps to Make Work
    Pay (D03, D05); Single Enforcement Body consultation response (D02 L433).
- Forecast/actual pairs, repeated/changed tables, same-period conflicts and scope relationships (locations only; author owns hooks):
  - Proposed (D04, 2019) vs response (D02, 2021):
    - Right to request work(place) modifications: D04 L90, L367, L381-421, Q3-Q7 (L425-468) → D02 L131,
      L345, L766: not proceeding "at this stage"; raise awareness of existing duties.
    - Strengthened statutory guidance: D04 L92, L516-526, Q8-Q15 → D02 L129, L373-401, L766: majority
      agreed; HSE to strengthen non-statutory guidance first, then explore statutory guidance.
    - SSP phased returns: D04 L96, L582, L632-662 ("will amend SSP regulations"), Q17 → D02 L407-413
      (broad support; current rules still stop SSP on return) and L439-441, L768 ("now is not the right
      time to introduce changes to the sick pay system"). D02 does not report the regulations as amended.
    - Remove qualifying-day identification: D04 L676-724, Q18 → no D02 response found (searched
      "qualifying").
    - Extend SSP below the LEL at 80%: D04 L97, L584, L728-736, Q19-Q20 → D02 L415-419 (75% agreed;
      not extended in the pandemic; no rate result reported), L135, L441, L768.
    - Accrual (Q21, D04 L738), SSP1 timing (Q24, D04 L842-850), day one written statement (D04 L100-101,
      L836-840), payroll sickness-absence reporting (Q54-Q55, D04 L1554-1570): no D02 response found
      (searched "accru", "SSP1", "day one", "payroll", "written statement"; the only "accru" hits, L818
      and L954, concern benefits/costs that "accrue", not SSP accrual).
    - Fines and enforcement (D04 L98-99, L586, L788-832, Q22-Q23) → D02 L429-435 (72% agreed; SSP
      enforcement to sit within the Single Enforcement Body).
    - SME SSP rebate (D04 L103, L588, L862-892, Q25) → D02 L421-427 (mixed views; temporary Coronavirus
      SSP Rebate Scheme, take-up lower than forecast).
    - SSP rate and length (D04 L918, Q26: no change) → D02 L135 (pandemic not the time to change rate or
      eligibility).
    - OH subsidy (D04 L105, L968-1018, Q27-Q32) → D02 L472-508 (test a subsidy; evaluation; possible
      fixed-term roll-out). Research network (D04 L1252 "Working Age Health Research and Development
      Network") → D02 L143, L613-617 ("Centre for Work and Health Research" with ESRC, MRC, HSE, SOM,
      Academic Forum). OH workforce (D04 L1038-1192, Q33-Q39) → D02 L619-672. Quality and buying support
      (D04 L1310-1530, Q45-Q53; Q53 option order L1520-1530) → D02 L510-556 (ranked measures L522-534).
      Information and advice (D04 L1436-1488, L1546) → D02 L283-303. Tax (D04 L946-966) → D02 L724-732.
      Fit note: not consulted on in D04 → D02 L147-153, L678-710 ("Although not specifically consulted
      on").
  - Proposed (D05, October 2024) vs response (D03, 2025):
    - Percentage rate: D05 paras 22-24 (L127-133; illustrative 60-80%; Tables 1-2 L145-172) → D03 L41,
      L184-198, L259-261 (80%; lower-of rule; amendment at Commons Report Stage).
    - LEL and waiting-period removal: D05 L95, L105-107, L111-123 → D03 L73, L212-219, L231, L249.
    - Territorial scope: D05 L83 (England, Wales and Scotland only) → D03 L45 (extension to Northern
      Ireland incl. 80%, subject to an LCM).
    - Flat rate: D05 L190 (£116.75; not consulted on) → D03 L53 (£116.75, to £118.75 in April 2025
      subject to approval).
    - Business costs: D05 Table 2 L169-172 and L163, L174 → D03 L121, L194-196.
    - Equality analysis: D05 L159 ("will be published shortly") → D01 (November 2024) → D03 L51.
  - Forecasts and actuals: D02 L425 (Coronavirus SSP rebate take-up "lower than initially forecast", no
    figures); D02 L462 (Mintel OH forecast from 2021); D02 L468 (Bank of England expectation); D04 L159 and
    D02 L78/L97/L182 (target of 1 million more disabled people in work by 2027) with progress figures at
    D04 fn9 L1774 and D02 L115; D04 L155 (2030 healthy-life target); D05 Table 1 "0" and D01 L117, L129
    (modelled zero losers) beside D01's hedges (L117, L130-131) and D03 L200; D02 Annex B take-up
    forecasts (L1140-1166).
  - Repeated or changed tables: no table is repeated across documents. D05 Table 2 cost figures reappear
    as D03 prose (L194); D05 Table 1's 80% row (300,000; £123-£146; 4 weeks) aligns with D01 L153, L157,
    L424 and Case study 1 (L409-422). D04 Q53 option list (L1520-1530) reappears in D02 ranked by popularity
    (L522-534) in a different order.
  - Same-period or internal conflicts (recorded, unresolved): D04 L193 vs fn105 (21% vs 18%); D04 fn103
    vs fn106 (51% vs 50%); D02 L450 vs L988 ("over a third" vs "one in six"); D02 L808 vs Table 3 (£5,000
    vs £4,700); D02 correction slip vs body (SOM vs The At Work Partnership); D03 L121 vs L195 (£30
    million vs £10-30 million); D05 L107 vs L121 ("individuals" vs "employees"); D01 religion and marital
    text vs tables (L264 vs L260; L314 vs L324) and Below LEL marital column 111%; D01 L129/L157 vs L282
    cohort counts.
  - Issuer vs mentioned organisations: D04 and D02 are joint DWP-DHSC; D05, D01 and D03 are DWP only.
    D02 Annex B is authored by named DWP and RAND Europe staff. Quoted respondents are unnamed (D03 L115,
    L154, L156, L158, L161; D02 L684, L686). Mind distributed questions to its members (D02 L255).
  - Actions vs mentions: actual COVID-period SSP actions (D02 L405: self-isolation eligibility, SSP
    rebate scheme, temporary suspension of waiting days) vs 2019 proposals (D04) and 2024 statutory
    proposals (D05, D03). D02 L433 reports the government "confirmed its intention" in a separate
    consultation response (not in bundle).
  - Hedge scope pointers: D01 L117 and L129-131 (zero-loser claim vs "may"/"could" qualifiers); D05 L174
    ("may therefore only have a small impact"); D03 L109, L118, L125, L200; D04 L734 (conditional "If
    eligibility were to be widened") vs L632 (firm "will amend").
  - Exclusion facts: self-employed not eligible and excluded from the below-LEL estimate (D01 L47);
    suggestions to cover the self-employed and all workers listed but not adopted (D03 L241-243); gig and
    zero-hour workers only if classed as employees (D01 L45); multiple jobs each below the LEL excluded
    (D04 L728; D02 L417) and multiple-job rules unchanged (D03 L169); agency workers cannot request
    flexible working (D04 L375); RAND sample excluded micro employers (D02 L1046); D01 religion figures
    cover England and Wales only (L248); D05 proposals exclude Northern Ireland (L83).
  - Late list members: D03 L247 (52 weeks, last of 4 suggestions); D01 L367 ("not married", last of 7);
    D02 L534 (basic online information, last of 6 ranked measures); D05 L202 ("Other", last of 5
    options); D04 Question 56 (L1598) and footnote 128 (L2250); D02 footnote 112 (L1630).
  - Narrative passages that repeat tables: D03 L101, L147 (Figures 2-3); D02 L207 (Figure 1), L808, L881,
    L948, L982 (Annex A), L1136, L1158 (Annex B); D01 L187, L223, L246, L272, L292, L314; D05 L141, L143,
    L174.
