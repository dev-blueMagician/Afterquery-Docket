# aq-03066 - document map, D01 only (per-document file for later merge)

Navigation only: where things are in `text/D01.txt`, not what to ask. Questions quote the
document, never this map. Line numbers are `text/D01.txt` lines (the `docs/` original is the
same text shifted by 2: text line N = docs line N-2). Quotes are verbatim and sit on one line
of the text file. Curly apostrophes/quotes are kept as in the source.

## Binding and coverage

- Source: `docs/nzcc_fibre_im_r1_framework_chorus_submission_on_new_regulatory_framework_fo.txt`
- Extraction: `text/D01.txt`, method `text`, pages `null`, chars 167702 (manifest.json)
- sha256 (manifest and intake.json agree): `fd87936d02df6fb825ee5869c8a6698818a29f6b01e8886cb8b145fb5456dcf1`
- Task-page number: intake.json lists this source as document number 4 ("Doc 4"); local id D01.
- intake.json: `incomplete: false`, `gap_characters: 0`, `matches_capture: true`.
- Reuse: no earlier D01 entry existed (notes/doc-map.md was the blank template); nothing reused.
- Coverage ledger (sequential read, Read tool): L1-200, L200-399, L400-599, L600-799, L800-999,
  L1000-1199, L1200-1392. Unread: none. File ends L1391 `-----`, L1392 blank.
- Extraction spot-checks against the `docs/` original (also plain text, so no page images):
  - Page count: not applicable in manifest; the running header `Submission on Commerce Commission’s invitation to comment (21 Dec 2018)` occurs 68 times (grep count) with printed page numbers 1-68.
  - Table: the "Network that connects" table, text L614-620 = docs L612-618. Same words; the only
    difference is the docs file has the single ellipsis character where text/ has three dots (`...`).
  - Footnote: fn 37, text L1356 = docs L1354, identical.
- Missing source text (distinct from unread): Appendix B has a heading only (L1107-1108,
  `PROPOSED PROCESS DIAGRAM`); the diagram/"proposed alternative timetable" content is absent in
  both text/ and docs/. Unresolved, cannot be inspected.

## D01 - Chorus submission on the Commission's 9 November 2018 fibre framework paper

### 1. Identity

- Title (L3-5, split over three lines): `Commission’s invitation to comment on its proposed approach to the new regulatory framework for fibre dated 9 November` then `2018` on L5.
- Date: L6 `21 December 2018`; running header gives `(21 Dec 2018)`.
- Written/submitted by: Chorus. The text never prints "Chorus Limited" or a signatory (grep: no
  hit for "Chorus Limited"/"Chorus New Zealand"). Authorship shows in first person, e.g. L203
  `Chorus supports the Commission clarifying the process and timing`, L24
  `higher levels of risk associated with Chorus’ fibre investment`, L118
  `the primary reason for Chorus’ existence as a structurally separated, wholesale only service provider`.
- Responds to: L33 `New regulatory framework for fibre – Invitation to comment on our proposed approach published on 9 November 2018 (Issues Paper)` (the Commerce Commission's consultation paper).
- Type/edition: single submission; no other edition of it in this file.
- Fiscal/calendar convention: no fiscal year end stated. Uses calendar quarters (`Q1 2020`) and
  "regulatory year" (L1354). L1345 `we anticipate our financial and regulatory years may be misaligned based on the proposed implementation date of 1 January 2022`.
- Attached expert reports: none. "CEPA report"/"CEPA’s report" (L934 onward) is cited as an
  external report the Commission asked about (Q25, L1305 `CEPA's advice`), not attached and not
  written for Chorus. CEPA's full name is not given.
- Appendices: A `ISSUES FOR EARLY DISCUSSION` (L571-1105); B `PROPOSED PROCESS DIAGRAM`
  (L1107-1108, heading only); C `Responses to questions` (L1111-1389).
- Numbering: body paragraphs 1-245; footnotes 1-37; Issues 1-10; Questions Q1-Q29 (sub-parts
  Q18a-b, Q27a-c, Q29a-d).

### 2. Structure with line ranges

| Lines | Heading (as printed) | Paras | Printed pages |
|---|---|---|---|
| 3-8 | cover/title | - | 1 |
| 10-29 | (no heading) eleven key-message paragraphs | - | 2 |
| 32-185 | OVERVIEW | 1-48 | 3-10 |
| 35-59 | Policy Context | 2-8 | 3-4 |
| 59-75 | `Shift to utility style regulation for FFLAS` (heading fused to end of para 8, L59) | 9-14 | 4-5 |
| 77-85 | Implementation of the Building Blocks Model | 15-18 | 5 |
| 86-115 | Process to establish the BBM | 19-23 | 5-7 |
| 116 | Key elements of the BBM framework (group heading) | - | 7 |
| 117-129 | Purpose statement | 24-29 | 7-8 |
| 131-139 | Financial losses | 30-34 | 8 |
| 141-148 | Cost of capital | 35-37 | 8-9 |
| 150-156 | Cost allocation | 38-40 | 9 |
| 158-162 | Scope of the regulated services | 41-43 | 9 |
| 164-173 | Implementing a price-quality path | 44-47 | 9-10 |
| 175-185 | Structure of our submission | 48 | 10 |
| 188-316 | PROCESS FOR DEVELOPING THE FIBRE INPUT METHODOLOGIES (summary box L190-197) | 49-76 | 11-16 |
| 199-209 | Introduction | 49-54 | 11-12 |
| 211-227 | Streamlining development of the IMs | 55-60 | 12 |
| 230-284 | Initial RAB and cost of capital (table L237-264) | 61-66 | 13-15 |
| 286-314 | Requirements for the price-quality proposal | 67-75 | 15-16 |
| 315-316 | Information disclosure | 76 | 16 |
| 319-444 | THE RELEVANT STATUTORY CONTEXT AND PURPOSES OF PART 6 (summary L321-328) | 77-102 | 17-22 |
| 329-350 | Relevance of Part 4 of the Commerce Act to Part 6 | 77-80 | 17-18 |
| 351-359 | Purpose statements | 81-83 | 18-19 |
| 361-367 | Section 162 | 84-85 | 19 |
| 368-412 | Section 166 | 86-95 | 19-21 |
| 414-427 | Section 173 | 96-97 | 21-22 |
| 429-444 | Building Block Model approach | 98-102 | 22 |
| 447-565 | ECONOMIC CONCEPTS AND PRINCIPLES (summary L448-458) | 103-128 | 23-28 |
| 472-534 | Real financial capital maintenance | 106-120 | 24-26 |
| 536-544 | Allocation of risk | 121-123 | 26-27 |
| 546-556 | Asymmetric consequences of over and under-investment | 124-127 | 27-28 |
| 558-565 | Pricing efficiency | 128 | 28 |
| 571-573 | APPENDIX A / ISSUES FOR EARLY DISCUSSION | 129 | 29 |
| 575 | REGIME WIDE ISSUES (group heading for Issues 1-3) | - | 29 |
| 576-643 | Issue 1: Scope of regulated services (summary L577-580; table L614-620) | 130-143 | 29-32 |
| 646-666 | Issue 2: Practical application of s 166(2)(b) (summary L648-650) | 144-147 | 33 |
| 669-696 | Issue 3: Matters for which input methodologies are determined (summary L669-679) | 148-153 | 34-35 |
| 699 | VALUATION OF ASSETS INPUT METHODOLOGY (group heading, Issues 4-5) | - | 36 |
| 700-745 | Issue 4: Scope of the regulated asset base and its valuation (summary L700-704; subheads L706 Determining the initial RAB, L724 Roll-forward) | 154-166 | 36-38 |
| 747-777 | Issue 5: Calculation of financial losses and Crown financing (summary L747-749; (a) L755; (b) L768) | 167-177 | 38-39 |
| 780 | COST ALLOCATION INPUT METHODOLOGY (group heading, Issues 6-7) | - | 40 |
| 781-835 | Issue 6: Allocating common costs between regulated FFLAS and other services (summary L782-786; subheads L798, L808, L816) | 178-189 | 40-42 |
| 836-854 | Issue 7: Allocating common costs between different types of FFLAS (summary L836-839) | 190-196 | 42-43 |
| 857 | COST OF CAPITAL INPUT METHODOLOGY (group heading, Issue 8) | - | 44 |
| 858-918 | Issue 8: Using Part 4/FPP approach for fibre regulation (summary L858-867; subheads L873, L888, L908, L912) | 197-206 | 44-46 |
| 921 | QUALITY DIMENSIONS INPUT METHODOLOGY (group heading, Issue 9) | - | 47 |
| 922-1010 | Issue 9: Scope of the quality dimensions input methodology (summary L922-931; subheads L933, L954, L989, L996) | 207-227 | 47-51 |
| 1013-1014 | CAPEX AND REGULATORY PROCESSES AND RULES INPUT METHODOLOGIES (group heading, Issue 10) | - | 52 |
| 1015-1104 | Issue 10: Input methodologies that support the setting of pricequality paths (summary L1015-1023; subheads L1025, L1042, L1054, L1067, L1080, L1091, L1097) | 228-245 | 52-55 |
| 1107-1108 | APPENDIX B / PROPOSED PROCESS DIAGRAM (no content) | - | 56 |
| 1111-1389 | APPENDIX C / Responses to questions | Q1-Q29 | 57-68 |

Notes: there is no Issue or group heading for taxation; "tax" occurs only as a list item at
L673 `Treatment of taxation` and L1030 `Cost of capital, asset valuation, cost allocation and taxation` (L854 "taxing" is the adjective).
Printed page starts (running-header lines): p2 L10, p3 L31, p4 L54, p5 L75, p6 L94, p7 L114, p8 L129,
p9 L148, p10 L169, p11 L187, p12 L207, p13 L229, p14 L258, p15 L280, p16 L300, p17 L318, p18 L343,
p19 L355, p20 L380, p21 L404, p22 L427, p23 L446, p24 L468, p25 L495, p26 L517, p27 L541, p28 L554,
p29 L570, p30 L595, p31 L613, p32 L630, p33 L645, p34 L668, p35 L693, p36 L698, p37 L720, p38 L741,
p39 L764, p40 L779, p41 L804, p42 L830, p43 L848, p44 L856, p45 L878, p46 L903, p47 L920, p48 L939,
p49 L962, p50 L984, p51 L1001, p52 L1012, p53 L1039, p54 L1063, p55 L1085, p56 L1106, p57 L1110,
p58 L1137, p59 L1164, p60 L1189, p61 L1212, p62 L1235, p63 L1259, p64 L1282, p65 L1307, p66 L1333,
p67 L1358, p68 L1386.

### 3. Number ledger (every figure found on the full read)

Source class: A = Chorus's own statement; C = attributed to the Commerce Commission (its report,
paper or timetable); T = attributed to another third party; S = statute/case/citation locator.

Money, percentages, speeds, coverage, counts

| Line | Verbatim | Value and unit | What it measures / period | Class |
|---|---|---|---|---|
| 38 | `to 87% of New Zealand` | 87 % | coverage Chorus and LFC networks are "on track to build" to; no date given | A |
| 41-42 | `There are now over` / `90 RSPs bringing choice to consumers` (number split across two lines) | over 90 RSPs | count of retail service providers, "now" (Dec 2018) | A |
| 44 | `can still be obtained for $90 a month which is 5% below the OECD average and 24% below the equivalent Australian offering` | NZ price $90 per month; 5 %; 24 % | 'premium' 100Mbps fibre broadband, unlimited data plus voice line; Commission's 2017 Annual Market Monitoring Report (fn 1, p.7) | C |
| 44 | `A ‘premium’ 100Mbps fibre broadband service` | 100 Mbps | speed of the priced service | C |
| 45 | `moving from 5 percent to 9 percent below the OECD average for the 100 Mbps high user broadband and voice category` | 5 % to 9 % | gap below OECD average; 2018 Annual Market Monitoring Report (fn 2, p. 12) | C |
| 48 | `to deliver gigabit capability and beyond` | gigabit (no figure) | fibre capability | A |
| 70 | `We require an investment grade credit rating to service nearly $2 billion of debt` | nearly $2 billion | Chorus debt (present tense, no date) | A |
| 252 | `The Commission has outlined two approaches` | 2 | Commission's approaches to Crown financing value | C |
| 820 | `We operate one network that includes two technologies, copper and fibre` | 1 network, 2 technologies | Chorus network | A |
| 941 | `fibre quality dimensions can be grouped into six broad categories` | 6 | CEPA's quality categories (named in fn 32, L960) | T (CEPA) |
| 993 | `two broad approaches for stakeholder input` | 2 | CEPA: regulator-led and industry-led | T (CEPA) |
| 1008 | `none of Transpower’s four (service performance) quality targets were linked to revenue` | 4 targets, 0 linked to revenue | Transpower's first regulatory period | A (about Transpower) |
| 1168 | `the three key economic principles used under Part 4` | 3 | Commission's Q7 wording | C |

Same quantity twice: the 2017 gap is `5%` at L44 and `5 percent` at L45 (format only). No WACC
value, percentile number, leverage percentage, beta value, debt-premium figure, TAMRP value,
connection count, RAB value or loss amount appears anywhere in D01 (full read; grep for
"percentile|beta|leverage|debt premium|WACC|connection" inspected: all hits are qualitative).

Durations, terms, periods

| Line | Verbatim | Value | What it measures | Class |
|---|---|---|---|---|
| 18 | `after five years of policy review` | 5 years | length of policy review (compare L33 `from 2013 to 2017`) | A |
| 33 | `MBIE’s review of the Telecommunications Act 2001 from 2013 to 2017` | 2013-2017 | MBIE review period | A |
| 33 | `pre 2011 policy review and legislation` | pre-2011 | start of the process | A |
| 80 | `losses incurred in providing UFB services between 2011 and 2022` | 2011-2022 | UFB loss period | A |
| 134 | `We think this means the unrecovered loss period – 2011 to implementation – should be treated as a single regulatory period` | 2011 to implementation | loss period | A |
| 167 | `the preparation of a five year forecast of operating expenditure (opex) and capital expenditure (capex)` | 5 years | forecast length, "new for us" | A |
| 220 | `development of the Part 4 IMs in 2009 and 2010` | 2009, 2010 | when Part 4 IMs were developed | A |
| 240 | `methodology for valuing pre- and post-2011 assets` | 2011 cut | section 176(1) valuation split | S |
| 760 | `10 year term rates should be used rather than a five year term` | 10-year vs 5-year | risk-free rate term for the RROI (loss period) | A |
| 906 | `The risk free rate should use 10-year New Zealand government bonds when estimating the RROI` | 10-year | same; scope stated as the financial loss calculation, `(2011 to implementation)` | A |
| 1252 | `10 year term rates should be used rather than a 5 year term` | 10-year vs 5-year | same, Appendix C (digit "5" where L760 has "five") | A |
| 1078 | `Historically our forecasts have focused on a three year period.` | 3 years | Chorus's historical forecast horizon | A |
| 1078 | `we believe five years of forecast expenditure should be provided as part of RP1 proposal` | 5 years | forecast in RP1 proposal | A |
| 1078 | `This could then be extended to 7 to 10 years in subsequent periods.` | 7 to 10 years | later forecast horizon ("could") | A |
| 1103, 1375 | `in the short (three year) RP1 period` | 3 years | length of RP1 | A |
| 1354 | `four years of historical information from regulatory year 201637 through to regulatory year 2019 inclusive` | 4 years; regulatory years 2016-2019 ("201637" = 2016 + footnote marker 37) | historical information preference; "Subject to confirmation of the timing of the regulatory year" | A |
| 1356 | `Due to final exit from Spark’s SAP system in 2014, reassigning pre-2015 expenditure` | 2014; pre-2015 | fn 37 reason for starting at 2016 | A |

Dates, deadlines, milestones

| Line | Verbatim | Date | What | Class |
|---|---|---|---|---|
| 4-5, 33 | `published on 9 November 2018 (Issues Paper)` | 9 Nov 2018 | Commission's invitation to comment | C |
| 6 | `21 December 2018` | 21 Dec 2018 | submission date | A |
| 29 | `set a price-quality path before 2022` | before 2022 | PQ path timing | A |
| 51 | `2017-Annual-Telecommunications-MonitoringReport-20-December-2017.PDF p.7.` | 20 Dec 2017 | fn 1 URL date | C |
| 52 | `2018-Annual-Telecommunications-MonitoringReport-18-December-2018.pdf p. 12.` | 18 Dec 2018 | fn 2 URL date | C |
| 64 | `Crown contracts governing UFB1 end on 31 December 2019` | 31 Dec 2019 | end of UFB1 Crown contracts | A |
| 73 | `13 October 2011, available at https://gazette.govt.nz/notice/id/2011-go7120` | 13 Oct 2011 | Government Policy Statement (fn 4) | T (Government) |
| 87 | `extension to the implementation date from 1 January 2020 to 1 January 2022` | 1 Jan 2020 to 1 Jan 2022 | implementation date change | A |
| 100 | `keep the IMs to the minimum required to implement the regime by 2022` | 2022 | regime implementation | A |
| 192 | `We would appreciate the final decision on initial RAB by Q1 2020` | Q1 2020 | Chorus's requested initial RAB final decision | A (request) |
| 200 | `The Minister has agreed to defer the implementation date to 1 January 2022` | 1 Jan 2022 | implementation date; action by the Minister | A |
| 221 | `allow the Commission to reach a final decision by Q2 2020` | Q2 2020 | IMs final decision under Chorus's streamlining options ("should allow") | A (proposal) |
| 278, 500 | `In the course of the 2016 IMs Review the Commission fasttracked certain IMs` | 2016 | Commission's IMs Review | C |
| 288 | `we will have to submit a price-quality path proposal mid-2020` | mid-2020 | Commission's proposed timetable, as read by Chorus ("suggests") | C |
| 288 | `will only be published at the end of 2019` | end of 2019 | draft capex IM and rules/processes IM under Commission's timetable | C |
| 296 | `proposed approach to expenditure by June 2019` | June 2019 | Chorus's "Ideally" date for draft capex IM and rules and processes IM | A (proposal) |
| 316 | `If the ID regime was finally determined by Q2 2021` | Q2 2021 | conditional date for final ID regime | A (conditional) |
| 423 | `as introduced on 8 August 2017` | 8 Aug 2017 | Telecommunications (New Regulatory Framework) Amendment Bill introduced (fn 15) | S |
| 567, 568, 898, 916, 918 | `15 December 2015, page 67` | 15 Dec 2015 | Commission's UCLL/UBA cost of capital Final Decision (pages 67, 70, 11-13) | C |
| 638 | `Open letter – Our intention to gather information relating to emerging technologies (May 2018)` | May 2018 (URL: 9-May-2018) | Commission open letter, para 30 | C |
| 639 | `Telecommunications Act Review: Options Paper (July 2016) at pages 21 and 56` | July 2016 | MBIE Options Paper | T (MBIE) |
| 876 | `Approach-to-Estimating-the-Cost-of-Capital-19-June-2009.pdf` | 19 June 2009 | Commission Revised Draft Guidelines (URL) | C |
| 893 | `Ofcom’s statement earlier this year` | 2018 | Ofcom statement (fn 28: 28 March 2018) | T (Ofcom) |
| 901 | `Statement – Annexes 17-27, 28 March 2018 at [A20.223]-[A20.237].` | 28 Mar 2018 | Ofcom WLA Market Review | T (Ofcom) |
| 1117, 1345 | `While the implementation date has been deferred to 1 January 2022` | 1 Jan 2022 | repeated in Appendix C | A |

Paragraph/page locators cited: Issues Paper section 6 (L459), paragraphs 7.16 (L587), 7.19
(L589), 7.53 to 7.55 (L700), 7.104 (L937), 7.121.3.1 (L1059); CEPA report section 6.2 (L980,
L982); Fletcher Inquiry Report page 42 (L400); Bill explanatory note at 4 (L402); Topic Paper 3
[2016] at [72-73] (L515); MBIE Options Paper at 33 (L641, L643); Cabinet Paper at [42] (L643).
Network layers: "layer 2" L159, L593, L666, L1194; "layer 1" L663-664, L995.

### 4. Lists (heading, count, items, summary-versus-body differences)

Timetable/process lists

- L190-197 summary box, "matters should be progressed early" for purposes (a) certainty and (b)
  preparation time: 4 items: Initial RAB (final decision by Q1 2020); Cost of capital; the process
  for setting forecast opex and capex; ID.
  - Appendix C Q2 (L1130-1135) answers "which IMs earlier" with 2 bullets: `Initial RAB and cost of capital` and `Price-quality path requirements`; ID is not in the Q2 list (it is the 4th bullet of Q1, L1124).
- L102-115 para 23 "precedents and adjustments to its programme of work": 6 bullets: lighter touch
  first regulatory periods (Part 4 precedent); initial RAB prioritised as a discrete exercise
  (early PQD "if necessary"); prioritise cost of capital IM; ID regime brought forward, run in
  parallel with the PQD; reporting requirements in RP1 rather than strict quality compliance
  thresholds; other options (bring forward/combine papers, stagger IM topics, early indication of
  relevant Part 4 elements).
- L221-227 para 60 "options available to streamline": 3 items (60.1 bring forward emerging views
  paper and/or combine with second process paper; 60.2 staggered tranches; 60.3 early indication
  of Part 4 IMs that can be adapted).
  - Appendix C Q1 (L1117-1124) lists 4 bullets: the same three plus `Commencing work on the new ID regime earlier (between the draft and final IMs)`.
- L268-282 para 65 "points support accelerating the initial RAB and cost of capital parameters":
  7 items (65.1 basis set down in the Act; 65.2 initial RAB IM; 65.3 discrete parameters; 65.4
  section 170(4) early determinations; 65.5 RAB can be updated to the PQD date; 65.6 2016 IMs
  Review precedent; 65.7 cost of capital IM can start now). 65.3 and 65.4 are fused on L274.
- L292-295 para 70: 2 items (70.1 begin discussion now, `use of an independent verifier` as the e.g.; 70.2 flexibility in IMs).
- L301-303 para 72: 2 items (unforeseen challenges; short timeframe).
- L308-314 para 75 "A transitional approach to setting expenditure for RP1 might include, e.g.":
  5 items (75.1 less granular information; 75.2 up-front versus later information requests; 75.3
  proportionate scrutiny; 75.4 optional mechanisms, e.g. `resetting forecasting annually`; 75.5 `Deferring the implementation of any consultation requirements to RP2`).
- L177-185 para 48 structure of submission: 6 bullets (the last three fused on L185).
- Prose milestones (no list; Appendix B diagram missing): Q1 2020 initial RAB decision (L192);
  Q2 2020 IMs final decision (L221); June 2019 draft capex and rules/processes IMs (L296); Q2 2021
  ID regime (L316); Commission's timetable per Chorus: end of 2019 drafts, mid-2020 proposal (L288).

Statutory/economic lists

- L321-326 Part 6 section summary "we support": 4 items (interpretation of end-users; general
  approach to ss 162 and 166(2)(b); section 173 view; BBM view). L328 then states a difference.
- L331-334 para 77: 2 items. L339-350 para 80 "context": 5 items (80.1 single network; 80.2
  differentiated regulated services; 80.3 constructed ahead of demand, early maturity; 80.4
  transitional challenge; 80.5 more complex regulatory environment).
  - Inside 80.5 (L350), constraints: 5 named (`nondiscrimination, mandatory products, equivalence of inputs (EOI), geographically consistent pricing, and unbundling`).
- L364-367 para 85: 2 items. L369-381 para 86: 2 objectives of section 166. L390-393 para 90:
  2 conditions. L408-411 para 94: 2 reasons for section 162 primacy.
- L435-442 para 101 "For example": 4 items (quality dimension methodologies; prices for mandatory
  services; unbundling; coverage for anchor services review).
- L459-464 para 103 Commission's key economic principles: 3 (FCM; efficient allocation of risk;
  asymmetric consequences of over and under-investment). Same three at L448 and Q7 (L1172-1176).
  A fourth, pricing efficiency, is discussed and not supported (L559, L1190).
- L479-482 para 108: 2 items. L484-485 para 109: 2. L487-490 para 110: 2. L495-498 para 111: 2
  cases where the Commission "may need to remove assets from the RAB".
- L518-523 para 116 "e.g.": 3 items (signal deregulation ahead; allocate costs to keep a
  proportion in the RAB; keep deregulated assets in RAB with allocated unregulated revenues).
- L527-529 para 118 flexibility "should include": 3 items (depreciation methodologies; carry
  forward under-recoveries under the revenue cap; pricing flexibility), all fused on L529.
- L549-550 para 125: 2 circumstances. L559-565 para 128: 3 reasons against a pricing efficiency
  principle.

Scope lists

- L585-596 para 131 "We also agree with the Commission that": 5 items (131.1-131.5).
- L601-606 para 134 Schedule 1 distinction: 2 classes. Access services: UBA, UCLL, UCLFS.
  Backhaul services: UBA backhaul, UCLL backhaul – Cabinet to Exchange, UCLL Backhaul – Exchange
  to Interconnection point.
- L627-634 "two implications" (paras 141, 142); para 142: 2 items on ICABS.
- L657-664 para 146: 3 aspects of the Commission's example.

IM lists

- L669-677 Issue 3 summary `Mandatory IMs are:` 7 lines: Cost of capital; Valuation of assets;
  Allocation of common costs; Treatment of taxation; Quality dimensions; Regulatory rules and
  processes (including pass through and recoverable costs, wash up and reopeners); Capex projects.
  L678 adds `We also consider that IMs for setting the initial RAB are mandatory.`
  - Body para 148 (L680) does not enumerate; it points to `the mandatory IMs listed in section 175(1)`. Para 149 (L682) makes the initial-RAB point conditional (`To the extent the Commission considers the initial RAB should be set utilising IMs`).
- L1029-1035 para 229 "IMs relevant to the setting of the price-quality path": 4 items (229.1
  cost of capital, asset valuation, cost allocation and taxation; 229.2 quality IM; 229.3 rules
  and processes; 229.4 capex IM); para 230 adds reopeners.
- L688-694 para 152 "likely candidates for a more principles based approach": 3 (Cost allocation;
  Quality; Expenditure).
  - Q14 (L1222) lists `cost allocation, quality, and the requirements for price-quality path proposals` (third item worded differently). Q14 repeats only the asset-valuation example of para 153; the body's second example (Expenditure, L696) is not in Q14.
- L700-704 Issue 4 summary: 5 points (initial value under section 176; commissioning date; cost
  under GAAP; rules for particular asset types; `The IMs should permit certain one-off adjustments.`).
  - Body para 162 (L725-728) lists 3 (162.1-162.3); the one-off adjustments point is not in para 162.
- L709-711 para 155: 2 steps (section 176(1) initial value; section 176(2) financial losses asset).
- L732-739 para 164 mechanism for assets entering/exiting the RAB: 4 items.
- L758-765 para 170 "In practice, this would mean": 3 items (170.1 RROI and 10-year risk-free
  rate; 170.2 shared asset costs `(including pre-demerger assets)`; 170.3 scope of UFB revenue deducted from the notional MAR).
  - Q18 answer (L1246-1252) restates 170.1 and the causal-allocator points; 170.2 and 170.3 are not restated there.
- L788-794 para 178 cost allocation contexts: 3 (initial RAB; UFB financial losses asset;
  forwards-looking IM).
  - Q21 (L1267-1270) lists 2 (Initial RAB; BBM forwards-looking).
- L817-828 para 187 features of the business: 4. L831-834 para 188 sharing: 3 (regulated and
  non-regulated; access and backhaul; third party, `e.g. Spark and EDBs`).
- L841 types of FFLAS named: 4 (`the broadband anchor, voice anchor, DFAS and unbundled fibre services`).
- L880-886 para 200 risks Part 4 suppliers do not face in the same way: 6 (200.1-200.6).
- L891-906 para 203 parameter adjustments: 3 (203.1 asset beta; 203.2 leverage and debt premium;
  203.3 risk free rate); the percentile is a separate heading/para 204 (L908-909).
  - The "e.g." lists at L144, L865 and L1301 name 4: `asset beta, leverage, debt premium and percentile estimate` (risk-free rate not in those lists).
- FFLAS characteristics that differ from Part 4/copper:
  - Overview para 17 (L83) and para 35 (L142): 4, including `the higher level of financial leverage associated with the UFB initiative`.
  - Issue 8 summary (L861) and Q24 (L1297): 3 (systematic risk; stranding; price-cap plus revenue-cap); financial leverage is not listed there.
- L924-929 Issue 9 summary "broad principles will need to": 3 items; body para 219 (L969-978): 3
  items with (a)-(c) under 219.2; Q25 (L1312-1315): same 3 as the summary.
- L960 fn 32, CEPA's six categories: `ordering, provisioning, switching, faults, availability and performance`.
- L946-950 para 211 factors giving other LFCs quality incentives: 3; within 211.1 four
  requirements (unbundling, EOI, non-discrimination, reference offers).
- L999-1004 para 226 "This is appropriate because": 3 reasons (226.1 smooth transition/stable
  quality; 226.2 remote areas and unbundling mean past performance is not a reliable baseline;
  226.3 streamlined initial IMs). 226.1 and 226.2 are fused on L1002.
  - Q26 (L1325-1329) gives 3 bullets with different content (legislation locks in quality and price; Commission recognises lower risk; no historic data).
- L1006-1010 para 227 Transpower approach: 2 items (targets not linked to revenue; targets rather
  than strict standards).
- L1015-1023 Issue 10 summary: 4 points. L1026-1028 para 228: 3. L1045-1049 para 233: 3 matters to
  agree before submission. L1055-1066 para 236 evaluation criteria: 4 (236.4 `From RP2, whether there is consumer support for the price-quality trade-off`). L1068-1073 para 237 proposal information: 4.
- L1098-1104 para 245 reasons to defer incentive mechanisms: 4; Q28 (L1371-1376) same 4.
- L1360 Q27 "we favour": (a) defer customer consultation to RP2, (b) terms of reference for a
  voluntary verifier process, (c) flexibility in form and contents.
- Crown financing obligations: Overview para 34 (L139) names transaction costs, phasing and
  specification obligations, penalties, management step in remedies; uncompensated e.g.: 3
  (`step in rights, restrictions on Chorus’ decisions to invest in and compete with copper services, and an ex ante risk of penalties`).
  - Body para 176 (L776) names transaction costs, phasing/specification, management step in rights, `restrictions on our ability to compete with copper services in other LFC areas`, penalties; uncompensated e.g.: 1 (`but others are not (e.g. ex ante risk of penalties)`).
- NIPA "competitive market outcomes, including for example" (L90-99): 3 bullets.

Questions answered (Appendix C): Q1 L1113; Q2 L1128; Q3 L1140; Q4 L1146; Q5 L1154; Q6 L1162;
Q7 L1168; Q8 L1178; Q9 L1187; Q10 L1194; Q11 L1201; Q12 L1204; Q13 L1210; Q14 L1219; Q15 L1226;
Q16 L1233; Q17 L1240; Q18/18a/18b L1242-1244; Q19 L1255; Q20 L1262 (answer `Not relevant to Chorus.`);
Q21 L1266; Q22 L1276; Q23 L1286; Q24 L1294; Q25 L1305; Q26 L1320; Q27/27a-c L1334-1340; Q28 L1367;
Q29/29a-d L1380-1388 (answer `We have no further matters to raise at this time.`).
"For more information, refer to section" pointers: Q1, Q2 to Process; Q4 Purpose statements; Q6
Building Block Model approach; Q7, Q8 Economic concepts and principles; Q9 `Pricing Efficiencies`
(body heading is "Pricing efficiency", L558); Q10 Issue 1; Q12 Issue 2; Q13 Issue 3; Q15 Issue 4;
Q18, Q19 Issue 5; Q21 Issue 6; Q22 Issue 7; Q23, Q24 Issue 8; Q25, Q26 Issue 9; Q27, Q28 Issue 10.
No pointer: Q3, Q5, Q11, Q14, Q16, Q17, Q20, Q29.

### 5. Positions by topic (hedge words kept)

Building blocks model
- L17 `We support the Commission’s proposal to apply a building blocks model (BBM).`
- Strength of the Parliament claim varies: L78 `a BBM is both appropriate and implicitly mandated by Parliament`; L430 "Parliament intended a BBM approach would be adopted"; L1165 `demonstrates that Parliament contemplated that a BBM would be adopted`.
- L20 `We note that a lighter touch first regulatory period may be required` (hedge "may"); L104 `Precedent from Part 4 established lighter touch first regulatory periods`.

Initial RAB / asset valuation
- Priority and timing: L192 (Q1 2020 request); L202 `followed closely by cost of capital`; L1133 `Priority, if necessary, should be on completing the initial RAB and then the cost of capital.`
- Form: L266 `we do not think an extensive IM is necessarily required`; same line "could be addressed directly in an IM for this discrete exercise (and a section 170 determination if necessary)".
- Conditional: L682 `To the extent the Commission considers the initial RAB should be set utilising IMs, we consider those IMs are mandatory`.
- Methodology is statutory: L242 `Straight-line depreciation is required by section 176(1)`; L270 `Unlike Part 4, the basis for setting the initial RAB is set down in the Act`.
- Records: L721 `We do not have a preexisting valuation of the fibre network`; L718-720 accounting records exist but reflect past reporting needs.
- Roll-forward: Part 4 approach (L725); L696 `the roll forward can be principled but initial valuation should be prescriptive`.
- Deregulated assets: L739 `we don’t think this is an issue the Commission needs to resolve for the purposes of RP1`; L518 `Commission can’t remove assets from the RAB if doing so would undermine FCM`; L455 `assets do not drop out of the RAB when they are physically stranded`.
- Section 222 regulations not a bar: L284 `We are aware section 222 regulations need to be set`; L1228.
- IFRS: L745 `we were an early adopter of IFRS16 changes`; asks for treatment and principles in the IMs.
- Granularity: L730 `some degree of disaggregation to reflect different asset lives`.

Financial losses
- Period and treatment: L758 `can and should be treated as a single regulatory period` (2011 to implementation).
- Method: L756 agrees "accumulated unrecovered returns" requires a BBM approach.
- Discount rate: RROI = cost of capital consistent with cost of capital IMs, risk-free on a 10-year basis (L760, L906, L1252).
- What counts: L762 `An allocation of shared asset costs should be included in the financial losses calculation (including pre-demerger assets)`; L765 revenue scope consistent with cost scope.
- Backward versus forward: L81 `will likely differ from forward-looking approaches`; L256 `we expect an orthodox cost of capital methodology will be appropriate to both`; L258 `backward-looking RROI across a longer than usual regulatory period`; L867 `This RROI should be broadly consistent with the cost of capital applied after the implementation date.`; L914 "will be broadly similar ... `as implied by section 171`".
- Section 176(2A): L543 ex ante expectation `but not an ex post guarantee`.

Crown financing
- Preference: L136 `modified version of Method 1 set out in the Issues Paper`; L1257 `The Commission should adopt a modified Method 1`. Method 2 is never described in D01.
- Should NOT be assumed nil: L749 `The Commission cannot assume that the Crown financing has a nil value. Our view is that the financing has a material cost.`
- Promise, not shown here: L139 `We will demonstrate that Crown financing was not costless` (also L773, L776; future tense).
- Commission's formula: L137 `assumes implicitly that this avoided financing cost was equal to the RROI`.
- Post-implementation adjustment: L777 `should end at the date of repayment or dividend commencement`; methodology "should be specified in the IMs".
- Related parties: L769 `In our case there are no related parties to the funding arrangement. We don’t have an opinion on how the Commission should treat other LFC parent companies.`; Q20 L1264.

Cost allocation
- Backward-looking: L782 `is a one-off exercise, which is prescriptive`; causal allocators; L804 `proxies should only be used where a credible causal allocator is not available`; L153 `the Commission should adopt sensible proxies`.
- Chorus to prepare first: L156 `propose to prepare an allocation of the initial RAB for the Commission’s review`; L806 `we propose that we prepare a cost allocation model`.
- Forward-looking: Part 4-consistent; L786 `We support cost allocation IMs that are principled, rather than an overly prescriptive approach.`; L1271 `It is not necessary for the same methodology to apply in both cases.`
- Copper/fibre: L809 `those that are not (such as copper)`; L820-828 sharing expected to "substantively increase".
- Between types of FFLAS, should NOT apply: L836 `We don’t support an approach that allocates common costs between different types of FFLAS`; L1278; conditional fallback L854 `If the Commission nevertheless considers common costs should be allocated between different types of FFLAS, RP1 is not the appropriate time`.
- Geographic: L853 `We also query the value of a geographic allocation`; `(i.e. urban areas will subsidise rural)`.
- ABAA/OVABAA: not mentioned anywhere (grep "ABAA": no hit).
- Current ID regime: L110 `is not fit for purpose, in particular given its approach to cost allocation`; L208 `not fit for purpose in certain respects, generally related to the cost allocation approach`.

Cost of capital
- Starting point: L858 `use the Part 4 approach as a starting point when determining the cost of capital IMs for FFLAS`; L264 `draw on its FPP and Part 4 experience` ("broadly support ... with the caveat"); Q23 L1288 `use the Part 4 and UCLL/UBA FPP approach as the starting point`.
- Asset beta: conditional, L896-903 "Where appropriate comparators cannot be identified, and ... `an uplift should be applied to the asset beta`".
- Leverage and debt premium: L904 `The leverage and debt premium may need to take into account the regulatory and contractual framework` ("may need").
- Risk-free rate: 10-year NZ government bonds, stated only for the RROI/loss calculation (L906).
- Percentile: L909 `We suggest the Commission applies the Part 4 approach of using a percentile estimate above the midpoint` (no number).
- Uplift: L148 `we believe the BBM approach justifies an uplift`; L534 `remaining risk should be reflected in an uplift to cost of capital` ("To the extent that other aspects of the framework don’t provide an expectation of compensation"); L554 `the Commission’s test is more likely to be met for fibre under a BBM framework`.
- Commission's earlier view (mention of another's finding): L549 `the Commission concluded there was insufficient evidence to support a cost of capital uplift`; L550 `consumers do not value broadband outages as highly as electricity outages` (Chorus says this "should be reconsidered").
- Per-provider: L871 `It may also be appropriate for the Commission to take into account intrasector factors`.
- Crown financing link: L863 `is a unique feature that has not been tested and applied under the Part 4 approach`.
- Timing: L194 `certain cost of capital parameters will only be set in a PQD closer to the start of RP1`; fn 7 L298.
- TAMRP: only in the Commission's question text (L1294 `Should we re-estimate parameters that apply across sectors, such as the TAMRP?`); the answer (L1296-1301) does not mention it.

Quality
- L934 `quality regulation should focus on output measures, rather than prescribing the use of particular inputs` (agreeing with CEPA).
- Dimensions: L941 `the IMs should only focus on the end of the product lifecycle` / L942 `specifically availability and performance.`; L944 `it may be preferable to specify “management of congestion” as the relevant dimension`; L987 `the specific quality dimensions which could be recognised are availability and management of congestion (performance)`.
- L924 `These dimensions should be permissive rather than mandatory.`; L987 also "restrictive".
- No duplication: L952 `a principle of no duplication in the quality dimensions IM`.
- RP1: L997 `reporting obligations in RP1 rather than strict targets`; L1002 `no consultation on quality standards is necessary or appropriate prior to RP1`; L991.
- Process: propose/approve (L931); L993 `an industry-group led approach as described in the CEPA report would not be as productive`.
- Agreement with CEPA hedged: L967 `We broadly agrees with CEPA’s suggested level of prescription required in the IM.`

Capex IM, proposal and approval process
- L287 `Section 175 obliges the Commission to develop a capex IM`; L101 `indicated preference for a propose/approve model` (Chorus agrees).
- L1043 `we support an approach more closely modelled on Transpower’s IPP`; L1343 "strong preference".
- L1075 `we will be the only supplier subject to a price-quality path under Part 6`.
- Consultation: L1083 `this consultation requirement should not begin until RP2`; L314; L1360.
- Verifier: L1087 `We support the use of independent verifiers in the price-quality path proposal process.`; L1088 `the terms of reference could be agreed voluntarily`.
- Totex, should NOT apply: L1092 `We do not support the introduction of a totex approach to setting expenditure allowances.`
- Incentive mechanisms: L1098 `We believe, on balance, incentive mechanisms should be implemented for RP2 rather than RP1`; L1023.
- Transitional: L304 `there is a reasonable prospect we will have to agree an approach`; L171 `transitional approaches will be necessary`; L1051 `our proposal will have to pre-date finalisation of the IMs`.

Tax: no position; list mentions only (L673, L1030).

Regulatory processes and rules
- L680: rules and processes IMs "should include IMs for pass through and recoverable costs, wash up and reopeners".
- Reopeners: L1039 `should be broadly similar to those for EDBs`.
- Principles-based IMs supported (L686, L1220); L1215 `revisit non-core issues in the course of RP1 in anticipation of RP2`.

Scope of FFLAS, anchor services, unbundling, geography
- Agrees with Commission's questions (para 7.16), copper exclusion (para 7.19) and layer-2 point: L587-593; L589 `Chorus’ FTTN network are excluded from the scope of Part 6`; L593 `Services provided above layer 2 may be regulated if they are specified in regulations made under section 222`.
- Disagrees: L160 `is overly-broad` (the "services that support the operation of a network or its users" formulation).
- Out of scope: L162 `are out of scope, as are backhaul services (including ICABS)`; L600 `and is therefore not a FFLAS` (in-home wiring example); L1198.
- ICABS facts: L633 `ICABS was not a service required by CIP agreements or subject to a UFB reference offer`; L634 `ICABS is not subject to Fibre Open Access Deeds in Part 4AA`.
- Hedge on backhaul competition: L625 `services like backhaul can be provided by entities other than Chorus or LFCs` "so may already be subject to workable competition".
- Anchor services: constraint on prices (L563, L886 `Limited ability to reset prices at the end of each regulatory period`); L444 `There may also be a review of anchor services before implementation`; L946 `unlikely to apply to other LFCs, most importantly anchor services`.
- Unbundling: L441 `The requirement to unbundle will affect competition, but the outcomes are uncertain`; L1002 `the requirement to unbundle the PON fibre network for the first time`.
- Geographic: geographically consistent pricing is a constraint (L350, L563, L853); deregulation where competition develops "in certain areas" is the Commission's point reported at L498.

Price-quality versus information disclosure
- L190 `allow Chorus, and other LFCs for ID, sufficient time`; ID development earlier, L197 `between the draft and final stage of IM development`; L316 (Q2 2021, conditional).
- L650 `the Commission’s approach to confidentiality requirements for ID regulation` (example of separate section 166(2)(b) consideration).

Revenue cap / wash-up
- L525 `it was an express policy choice to provide for symmetrical wash-up`; L529 `the application of a symmetric wash-up is mandatory under the Act`.
- L838 `a revenue cap implies pricing freedom to achieve the MAR within a regulatory period`.
- L1027 `The application of a smoothing mechanism to minimise financial hardship to Chorus or price shocks to consumers` (agreed matter).
- L532 `We should therefore not be required to carry any such demand risk`.

Purpose statements
- L120 `if there is a conflict section 162 has primacy`; L408 `the section 162 purpose statement should be given primacy`; L412 `section 166(2) is framed conjunctively, not disjunctively`; L390 `it will arguably be relevant to consider the section 166(2)(b) objective where` ("arguably").
- L648 `we’re not confident this is a situation where section 162 and section 166(2)(b) require balancing`.
- Pricing efficiency, should NOT be added: L559 `We don’t think there is a case for developing an additional ‘pricing efficiency’ economic principle`; L1190 `A pricing efficiency principle is not necessary or appropriate`; L458 `specific constraints on price structures and/or relativities is required` (preceded by "We don’t think").

Timing / implementation date
- L87 (1 January 2020 to 1 January 2022); L200 (Minister agreed to defer); L1004 `ready by the statutory deadline`.

### 6. Other organisations, people, statutes, cases, documents

- Commerce Commission (addressee): Issues Paper; 2017 and 2018 Annual Market Monitoring Reports
  (L44-45; URLs name them "Annual-Telecommunications-MonitoringReport"); 2016 IMs Review (L278,
  L500); Topic Paper 3 (L515); `Cost of capital for the UCLL and UBA pricing reviews – Final Decision` 15 December 2015 (L567, L568, L898, L916, L918); open letter on emerging technologies, `Regulatory treatment of EV chargers costs and revenue` (L638); Revised Draft Guidelines on cost of capital (L876); FPP process; CPP IMs; `Under Subpart 6 of the Electricity Distribution Services IM.` (L1061).
- MBIE: review 2013 to 2017 (L33); Options Paper July 2016 (L639); L636 `national backhaul were excluded from the review`; Cabinet Paper at [42] (L643).
- The Minister: deferred implementation (L200); review under section 157AA (L430 `including the Minister’s review under section 157AA`); prescribes service conditions/prices (L437, L439, L663).
- Parliament / Select Committee: L388 `The Economic Development, Science and Innovation Committee’s report`, quoted `give the Commission the necessary flexibility to respond to technological change`; L402 `Telecommunications (New Regulatory Framework) Amendment Bill (293-2) (explanatory note) at 4`.
- Government Policy Statement, 13 October 2011 (fn 4, L73), cited for L59 `equity investors and debt holders took on significant risk`.
- Crown Infrastructure Partners: L89 `Network Infrastructure Project Agreement (NIPA) with Crown Infrastructure Partners (CIP)`; L97 "ongoing CIP approval mechanisms"; CIP agreements L633, L934. "Crown Fibre Holdings" does not appear.
- LFCs: generic only; no LFC is named (no Enable, Northpower, Ultrafast Fibre; "Ultrafast" appears only in `Ultrafast Broadband (UFB)`, L36).
- RSPs: generic; L950 `The countervailing power of the major RSPs`; L118 `disadvantage RSPs who do not own mobile networks`.
- Spark: L834 `Where we share an asset with a third party (e.g. Spark and EDBs)`; fn 37 L1356 (Spark's SAP system). Vodafone: no mention.
- Electricity/gas: L169 `like the electricity lines companies at the outset of Part 4`; L348 `electricity distribution businesses (EDBs) were previously regulated under the thresholds regime`; L501 `provided lines companies with an option to shorten asset lives`; L547 `This uplift is currently applied by the Commission in respect of electricity and gas under Part 4.`; L836 `there is no precedent with EDBs or GPBs`; L1039; L1101.
- Transpower: L1006 `Transpower’s transition to its first regulatory period is a useful benchmark.`; L1008; L1010 `any failure to achieve a quality target was not significant from a compliance perspective`; IPP (L1043, L1343); L1068 `such as Transpower’s RP2 proposal, and Powerco’s CPP proposal`; L1323.
- Powerco: CPP proposal (L1068); case L378 `Powerco v Commerce Commission [2008] NZCA 289 at [23]`.
- Cases: `Chorus v Commerce Commission [2014] NZCA 440 at [153]` (L373; [155] L375; [151] L400); `Wellington International Airport Ltd v Commerce Commission [2013] NZHC 3289` (L377; [222] L378; [213] L422; [214] L425; `17 WIAL v CC at [256].` L493); `Vector v Commerce Commission [2012] NZSC 99, [2013] 2 NZLR 445 at [56] – [61]` (L422). L363 `considered in detail by the High Court in the IM merits appeal`.
- `Fletcher Inquiry Report, at page 42` (L400).
- Ofcom / BT: L893 `the systematic risk of NGA is likely to exceed that of copper access for the time being`, `which justified applying a higher beta to BT’s fibre access services`; fn 28 L900-901.
- EU policy makers / Europe: L49; fn 3 L72 `set out in paragraph [203.1] of this submission`. UK regulators: L1094 `The purpose of the totex regime in the UK`.
- OECD average and "equivalent Australian offering": L44-45 (via the Commission's reports). No Australian regulator is named.
- CEPA: L934, L941, L955, L963, L964, L967, L985, L993; fn 33/34 `CEPA report, section 6.2.`
- Not mentioned at all (grep, no hit): Vodafone, Enable, Northpower, Oxera, Frontier, Sapere, ACCC, Crown Fibre Holdings.
- Statute sections cited: Telecommunications Act 2001 (L33); `Commerce Act 1986` (L330), s 52A (L363), s 52A(1) (L476), s 1A (L383); the Act s 18 (L383), s 157AA, s 162, s 162(b) (L972), s 166, s 166(2)(a)/(b), s 170, s 170(4) (L274), s 170A / `170(A)`, s 171 (L914), s 173, s 175, s 175(1), s 175(2)(a) (L965), s 176, s 176(1), s 176(2), s 176(2A), "(2AA)" (Commission's Q18 text, L1242), s 191, s 192 (L971), s 222; Parts 2, 4AA, 6; Schedule 1; Part 4 of the Commerce Act.

### 7. Definitions and abbreviations (first full form)

| Short form | Full form as printed | Line |
|---|---|---|
| FTTH | fibre-to-the-home | 14 |
| BBM | building blocks model (also "Building Blocks Model" L77, "Building Block Model" L429) | 17 |
| initial RAB | initial regulated asset base | 18 |
| FCM | real financial capital maintenance | 22 |
| RSPs | Retail Service Providers | 27 |
| PQR | price-quality regulation | 29 |
| Issues Paper | the 9 November 2018 consultation paper | 33 |
| UFB | Ultrafast Broadband | 36 |
| LFCs | Local Fibre Companies | 38 |
| Commission | Commerce Commission | 44 |
| FFLAS | fibre fixed line access services | 60 |
| POI | Point of Interconnect | 61 |
| IMs | Input Methodologies | 85 |
| NIPA / CIP | Network Infrastructure Project Agreement / Crown Infrastructure Partners | 89 |
| RROI | Rate of Return on Investment (fn 5: backwards-looking; "cost of capital" kept for forwards-looking) | 92, 192 |
| WSA | wholesale services agreements | 97 |
| PQD | price-quality determination | 106 |
| ID | information disclosure | 110 |
| RP1 | first regulatory period (RP2 never expanded) | 112 |
| opex / capex | operating expenditure / capital expenditure | 167 |
| MAR | Maximum Allowable Revenue | 276 |
| EDBs | electricity distribution businesses | 348 |
| EOI | equivalence of inputs | 350 |
| FWA / DFAS | Fixed Wireless Access / Direct Fibre Access Services | 367 |
| PDN | public data network | 603 |
| SLAs | Service Level Agreements | 963 |
| totex | forecast total expenditure (Commission's question text) | 1340 |

Used without expansion: TSLRIC (L60), UFB1 (L64), UCLL/UBA (L142), FPP (L144), UCLFS (L603),
ICABS (L162), FTTN (L589), ONT (L599), NGA (L893), GPBs (L836), PON (L1002), CPPs/IPPs (L1043),
IRIS (L1098), TAMRP (L1294), GAAP (L704), IFRS16 (L745), MBIE (L33), CEPA (L934), WLA (L900),
NPV=0 (L476).
Stated definitions/rules: L78 "FCM is applied ex ante, meaning that investors can expect to recover
the opportunity cost of their capital and the nominal value of their investment over time"; L194
`certain cost of capital parameters will only be set in a PQD closer to the start of RP1` ("in this context we mean the cost of capital IM"); L278 "By streamlining we mean moving faster on some aspects of the IMs workstreams and potentially PQD for early visibility"; L366 end-user = ultimate recipient "rather than intermediate acquirers like RSPs"; L621 fibre handover point = "specified point of interconnection for the relevant end-user premises, building or other access point"; L61 `Other services, such as backhaul, are not subject to` Part 6 regulation; L60 `TSLRIC based pricing for those services will no longer apply`.

### 8. Tables

Table 1, L237-264 (para 63; pages 13-14, interrupted by the page header at L258). Two columns,
`Issue Comment` (L237). No numeric cells. Flattened: row label and comment share a line.

| Group | Row label | Comment (location) |
|---|---|---|
| Initial value of fibre assets: | Valuation | L240 `methodology for valuing pre- and post-2011 assets` |
| | Depreciation | L242 |
| | Backward-looking cost allocation | L244, L246 (separate from the forward-looking cost allocation IM) |
| UFB financial losses asset: | Unrecovered returns | L250 (supports building blocks approach) |
| | Crown financing | L252 `We prefer a modified version of the Commission’s proposed Method 1` |
| | RROI for financial losses | L254-258 `an appropriate RROI for the period 2011 to implementation` |
| Cost of capital for RP1 | Forward-looking cost of capital | L262 `These are discrete exercises.`; L264 |

Table 2, L614-620 (para 136; page 31). Header garbled: L614 `31 Network that connects` (page
number fused), L615 `Enduserto Handover point`. Columns: service | network that connects |
end-user end | handover point. Cells are separated by `...` in text/ (single ellipsis character
in docs/). No units, no numbers.

| Service | Network | End-user end | Handover point |
|---|---|---|---|
| FFLAS (L616) | Network structure used to deliver telecommunications services over fibre media | Enduser’s premises, building, or other access point | Fibre handover point |
| UBA (L617-618) | Fixed PDN | Enduser’s building | First data switch |
| UCLL (L619-620) | Chorus copper network | Enduser’s building | `Handover point in telecommunications exchange` |

UCLFS is named in para 134.1 (L603) but has no table row.

Appendix B (L1107-1108): diagram not present; no table or timetable cells recoverable.

### 9. Internal differences, footnote qualifications, wording variants (both locations)

- Consultation in RP1: Issue 10 summary L1021 `but consultation a requirement for RP1` (as printed, in docs/ too) beside L1083 `this consultation requirement should not begin until RP2`, L991 `this should not be required for RP1 where the key elements of quality are locked-in by legislation`, L314 and L1360.
- Sections 162/166(2)(b): summary L328 `Our view differs from the Commission’s on the relationship between sections 162 and 166(2)(b)` beside L653 "We agree with the Commission’s interpretation, but consider that section 162 ... should be given primacy" and L406 "We agree with the Commission that the objectives will be complementary rather than competing".
- Loss period wording: L80 "between 2011 and 2022"; L134/L254/L758/L906 "2011 to implementation"; L543 "between 2011 and the implementation date".
- RROI versus forward cost of capital: L81 `will likely differ from forward-looking approaches` beside L867 (broadly consistent) and L914 (broadly similar).
- Cost of capital starting point: body L858/L869 "Part 4 approach"; Q23 answer L1288 "Part 4 and UCLL/UBA FPP approach"; L264 "FPP and Part 4 experience".
- Risk-free term wording: L760 "five year term"; L1252 "5 year term"; L760 "consistent with the cost of capital IMs" versus L1252 "consistent with the Commission’s cost of capital IMs".
- Citation mismatch: quoted passage is labelled `[263] Thus as with NPV=0, FCM is seen as an outcome` (L478) while its footnote 17 reads `17 WIAL v CC at [256].` (L493).
- Section label: `ongoing adjustment required by section 170(A)` (L138) versus `the ongoing adjustment required by section 170A` (L772) and L777.
- `objectives of sections 1626 and 166(2)(b)` (L120) = "162" plus footnote marker 6; fn 6 L127 `which reflects the third reading of the Act` (section numbers follow the Issues Paper). Chorus cites "176(2A)" (L124, L543, L544) while the Commission's Q18 text has "ss 176(2) and (2AA)" (L1242).
- Part 6 purpose wording: L415 "to establish a stable and predictable regulatory framework" versus Q5 L1158 `a key purpose of Part 6 was to enhance certainty and regulatory stability`.
- Stranding wording: L83 "higher risk of economic stranding"; L142 "higher risk of network assets stranding"; L1297 "network asset stranding".
- Trade-off wording: L1095 "significant opex-capex trade-offs"; L1363 `we are unlikely to face significant capex-opex trade-offs`.
- Heading label: Q9 pointer `refer to section Pricing Efficiencies.` (L1192) versus heading "Pricing efficiency" (L558); Q22 pointer "between types of FFLAS" (L1283) versus heading "between different types of FFLAS" (L836).
- Appendix C adds content not in the body: four years of historical information 2016-2019 with fn 37 (L1354-1356); audit/misaligned years (L1345); L1215 (revisit non-core issues); Q20 `Not relevant to Chorus.`; Q11 L1203 `assets and services can change from in scope to out of scope (and vice versa)`.
- Footnotes qualifying body statements:
  - fn 5 (L92): RROI versus "cost of capital" naming convention for the whole submission.
  - fn 7 (L298) on para 65.7: `some of the cost of capital parameters may be set in a PQD closer to the implementation period`.
  - fn 19 (L539) on para 118.1: `the enhanced risk of stranding was managed by the option of front-loading depreciation` (electricity distribution).
  - fn 3 (L72) sends "EU policy makers" to para 203.1, whose text (L893) refers to "regulation of NGA services in Europe" and Ofcom.
  - fn 28 (L900): Ofcom's basis (higher systematic demand risks, higher capital leverage, longer term payoffs).
  - fn 31 (L937): `The Commission acknowledges this at paragraph 7.104 of its paper.`
  - fn 37 (L1356): why historical information would start at regulatory year 2016.
  - fn 20/21 and 29/30 are the same two citations (pages 67 and 70) given twice (L567-568, L916-918) for near-identical body text at L552-554 and L911.
- Repeated passages (same wording in two or more places): overview para 32-34 (L136-139) and
  paras 173-176 (L771-776); para 22 (L101) and para 67 (L287); para 42-43 (L160-162), Issue 1
  summary (L578-580), para 132 (L597) and Q10 (L1197); para 126 (L552-554) and para 205 (L911);
  Issue 9 summary (L924-931) and Q25 (L1310-1316); para 245 (L1098-1104) and Q28 (L1369-1376).

### 10. Extraction quality notes

- Hyphens lost at original line breaks: `post2020` (L33), `pricequality` (L101, L293, L1015), `longterm` (L212), `fasttracked` (L278), `nondiscrimination` (L350), `endusers` (L397), `overlybroad` (L597), `nonpremise` (L636), `preexisting` (L721), `nonregulated` (L820), `copperbased` (L1194), `MonitoringReport` (L51-52), `gatherinformation` (L638), `DraftGuidelines` (L876), `Enduserto` (L615).
- Footnote markers fused to words or digits: `offering.1` (L44), `capital5` (L81), `1626` (L120), `201637` (L1354); markers stranded on their own lines: L47 (2), L56 (3), L358 (9), L384 (12), L418 (16), L510 (18), L895 (28).
- Para 7 is broken across footnotes and a page header (L48-49, then L54, L56-57). Para 8 and the next heading are fused (L59).
- Typos as printed: `Where TSRLIC is focussed on services, BBM is much more focussed on assets.` (L349); `ICABs is a backhaul service so out of scope).` (L1198); "(including share assets)" (L792); "We broadly agrees" (L967); stray `]` in the page-1 header (L8).
- Several numbered sub-items share a line (e.g. L274, L303, L309, L485, L529, L711, L1002, L1027, L1049, L1066, L1073); bullets are a private-use glyph.
- Ellipsis normalisation: text/ `...` versus docs/ single-character ellipsis (table rows L616-620 only).
- Nothing is clipped mid-sentence at the end; the last content line is L1389.

## Gaps

- Unread ranges in D01: none.
- Missing source text: Appendix B diagram (L1107-1108). The "proposed alternative timetable"
  promised at L185 (`Our proposed alternative timetable in Appendix B`) and L209 is not available;
  only the prose milestones listed in section 4 exist.
- Not covered by this file: D02-D08 (other mappers). Only exact-string searches were run there.

## Shared ground seen from D01 (locations only; other documents searched by string, not read)

- Paper responded to, `9 November 2018`: D01 L4-5, L33; also D02:29, D04:52/61/66, D06:48/165.
- Coverage `87%`: D01 L38 ("of New Zealand"); D04:16 ("fibre networks will cover 87% of the population", with "full deployment scheduled for the end of 2022").
- RP1 length: D01 L1103, L1375 ("three year"); D04:163 ("The initial regulatory period will be three years, followed by regulatory periods of 3-5 years"), D04:182, D04:213.
- Implementation date `1 January 2022`: D01 L87, L200, L1117, L1345; D04:41, 139, 156, 322, 496. `1 January 2020`: D01 L87; D06:192, 257, 769.
- `June 2019`: D01 L296 (Chorus's requested draft date); D03 lines 6, 9, 65, 123, 285, 410; D04:629 (contexts not read here).
- D01-only by exact string (no hit in D02-D08): `$90`, `24% below`, `9 percent below`, `nearly $2`, `Q1 2020`, `Q2 2020`, `Q2 2021`, `mid-2020`, `IFRS16`, `31 December 2019`.
- Unrelated string hits inspected: "four years" D08:156 (Vodafone/Gartner); "ten-year" D06:292 ("five- or ten-years’ time").
- "Chorus" string counts: D02 6, D03 8, D04 19, D06 101, D07 27, D08 53, D05 none returned.
- Cross-references out of D01 to documents that may be in the bundle: the Issues Paper paragraph
  numbers (section 3 locators) and the CEPA report section 6.2; whether those texts are in the
  bundle was not checked here.
