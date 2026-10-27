# aq-03066 - document map

Navigation only, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents (text/Dnn.txt), never this map. Line numbers are text/Dnn.txt lines.

## Bundle

- What it is: New Zealand Commerce Commission fibre input-methodologies project. Six items filed on
  21 December 2018 in response to the Commission's 9 November 2018 "proposed approach" paper (Chorus,
  Vodafone, Spark, Spark's expert Axiom Economics, CCHL, InternetNZ), plus the Commission's own later
  papers: emerging views summary paper (21 May 2019) and workshop slide pack (25 June 2019).
- Documents: 8. Local ids are alphabetical by file name and differ from the task page's Doc N:

| Local | Task page | Document | Chars |
| --- | --- | --- | --- |
| D01 | Doc 4 | Chorus submission, 21 Dec 2018 | 167,702 |
| D02 | Doc 6 | CCHL (Christchurch City Holdings) submission, 21 Dec 2018 | 15,100 |
| D03 | Doc 2 | Commission workshop slide pack, 25 June 2019 | 28,298 |
| D04 | Doc 1 | Commission emerging views summary paper, 21 May 2019 | 63,811 |
| D05 | Doc 8 | InternetNZ submission, 21 Dec 2018 | 11,580 |
| D06 | Doc 7 | Axiom Economics report for Spark, December 2018 | 105,880 |
| D07 | Doc 5 | Spark submission, 21 Dec 2018 | 83,131 |
| D08 | Doc 3 | Vodafone submission, 21 Dec 2018 | 63,479 |

- Gaps: none known. Capture header: "Documents: 8 of 8 read in full (538,941 characters)"; intake.json marks
  every document complete (gap_characters 0, matches_capture true). Figures/diagrams are absent as text
  (D04 Figure 1 and the timeline infographic, D08 Figures 1-11, D01 Appendix B process diagram, D03's
  "Similarity to Part 4" scale icons and the technical-paper pages it shows as images).
- Extraction spot-checks: plain-text captures, so page counts are not applicable. D03's appendix table
  (lines 277-279) was rebuilt by script from its stated inputs (WACC 10%, depreciation 5% of opening RAB) and
  every printed row and total reproduces (285, 291, 2,250, 2,826, 1,755, 1,071, 1,542). D04 footnotes 1-11 are
  inline after their paragraphs. D03 capex snapshot (lines 442-451): the "H1 FY 2018" column's rows sum to
  291 against a printed subtotal 301, and the two column headers both say FY 2018; treat that table as garbled.
- Provenance: notes/intake.json (capture AQ-03066_2026-10-11_1730.txt, sha256 d5819434...). Capture note:
  the page asked for a reload; all eight documents were nevertheless captured complete.
- Reuse binding: text/manifest.json hashes (D01 fd87936d, D02 79f54be3, D03 2b8a6d72, D04 6c48e548,
  D05 c9bd0dbc, D06 99cd53b9, D07 71f962b5, D08 646ce8f1).
- Coverage: D02, D03, D04, D05, D08 read in full by the caller. D01, D06, D07 mapped in full by
  bundle-mapper runs (notes/doc-map-D01.md, doc-map-D06.md, doc-map-D07.md); caller read D01 lines 1-270,
  735-925 and 1100-1130 directly.

## D04 (Doc 1) - Fibre regulation emerging views: Summary Paper

- Written by: Commerce Commission; foreword signed Stephen Gale, Telecommunications Commissioner. 21 May 2019.
- Process dates (lines 52-63, 139, 622-631): proposed approach paper 9 Nov 2018; Part 6 inserted 13 Nov 2018;
  notice of intention 19 Nov 2018; workshop 10 Dec 2018; submissions 21 Dec 2018; cross submissions 1 Feb 2019;
  this paper's submissions 5pm 16 July 2019, cross submissions 5pm 30 July 2019 ("extended the submission
  period by a fortnight, allowing eight weeks", line 23); workshop 25 June 2019; draft decision November 2019;
  final IM determination June 2020; PQ and ID determinations by end of 2021.
- Implementation date: "two-year extension ... until 1 January 2022" (line 139); "by 1 January 2022 (the
  amended implementation date)" (line 41).
- Foreword figures (line 16): "more than $3 billion invested since 2011"; build "about three quarters
  complete"; full deployment end of 2022; 87% of the population.
- Users able to connect (lines 72-80): Chorus 932,000; Northpower Fibre 25,000; Ultrafast Fibre 210,000;
  Enable Networks 200,000.
- Definition gate, footnote 2 (line 46): "Chorus and the other LFCs or regulated suppliers" = all four;
  "LFCs" = Enable, Northpower and Ultrafast as a group. Assumption (line 40): Chorus PQ + ID, other LFCs ID only.
- Key features (lines 146-194): IM list of seven (cost of capital; valuation of assets; cost allocation; tax;
  quality dimensions; regulatory processes and rules; capital expenditure projects); current prices plus CPI
  rolled over; initial value of assets = actual cost plus "financial losses between 1/12/2011 and the
  implementation date" (line 160); "initial regulatory period will be three years, followed by regulatory
  periods of 3-5 years" (line 163); revenue cap with wash-up plus price caps for anchor services and DFAS;
  anchor services "expected to be 100/20Mbps broadband, and voice"; unbundled fibre service "no price cap
  initially"; review of PQ features "from three years after the implementation date (and then at intervals
  of no less than five years)".
- Scope (lines 212-256): this paper covers six IMs (asset valuation, cost allocation, cost of capital, quality
  dimensions, capital expenditure, tax); regulatory processes and rules not set out here; nine other
  requirements to be consulted on separately (lines 237-256).
- Legal framework (lines 261-323): s 166(2)(a)/(b) no hierarchy (lines 299-302); 2011 Government Policy
  Statement not relevant (line 319).
- Economic principles (lines 334-356): three adopted (real FCM, allocation of risk, asymmetric consequences);
  none on competition or pricing "at this stage".
- Topic 1 asset valuation (lines 384-413), 13 numbered views: Crown financing "Method 1" (item 6); straight-line
  depreciation; loss asset amortised over "weighted average life of the main (non-loss assets) RAB" (item 11);
  CPI indexation of total RAB including the loss asset (item 12).
- Topic 2 cost allocation (lines 417-458), 14 numbered views: ABAA; "must not use" ACAM (5) and OVABAA "when
  allocating common costs" (6); no prescriptive rules between FFLAS types (9); past losses use ABAA (12-14).
- Topic 3 WACC (lines 463-530): SBL-CAPM; service-wide asset beta; risk-free rate matched to the regulatory
  period "(3 years initially)", 3-month window; credit rating BBB+; 5-year debt premium with TCSD; losses WACC
  views 1-4 (same asset beta, rolling-average risk-free rate, Crown financing cost "likely to be nil", notional
  leverage); uplift 5-7 (no uplift for asymmetric consequences; Type II stranding Options 1-4); ID WACC Options 1-2.
- Topic 4 quality (lines 534-556): seven dimensions "ordering, provisioning, switching, faults, availability,
  performance, and customer service" (line 548).
- Topic 5 capex (lines 560-593): customer consultation; independent verification; Transpower capex IM as
  starting point; no totex "at this stage".
- Topic 6 tax (lines 597-617): tax payable approach; post-tax WACC; benchmark leverage; items numbered 1-3, 5-7
  (no item 4).

## D03 (Doc 2) - Slide pack for Fibre Emerging Views workshop, 25 June 2019

- Written by: Commerce Commission staff; cover note says positions are not Commission endorsed except where
  they reflect the emerging views paper (line 7).
- Agenda (lines 17-28); Commissioners and fibre team names (lines 33-38).
- Input to date (lines 59-67): Nov 2018 paper "16 subs and expert reports", "9 cross-subs"; Dec 2018 workshop
  60 attendees; June 2019 workshop 41 RSVPs; consumer focus group 3 RSVPs. MBIE submissions due 3 July 2019 (line 45).
- Process (lines 80-97): November 2019 draft decisions; March 2020 technical consultation; June 2020 final decisions.
- s 177(2)-(3) quoted (lines 157-162): losses "for the period starting on 1 December 2011 and ending on the
  close of the day immediately before the implementation date".
- Losses method (lines 168-239): simplifying assumptions (lines 174-181); formula (lines 184-195); government
  funding deducted from RAB, actual financing cost assumed nil (line 229); losses "adjusted to present value at
  the end of 2021" at "the same as the WACC value" (line 231); amortisation alternatives: weighted average life,
  or fixed "15, 20 or 30 years", or "2, 3 or 4 periods", or no amortisation (line 237).
- Cost allocation example (lines 256-270): $100 investment in 2015, $10 p.a. depreciation, $40 unallocated value
  in 2022; allocated to past losses $60 (full), $30 (customer mix), $40 (traffic mix).
- Appendix table (lines 277-279), 2012-2021, "All figures are purely illustrative", no currency unit printed:
  inputs WACC 10%, depreciation rate 5%; rows capex, government funding, UFB revenues, UFB opex, opening/closing
  RAB, opening/closing government funding, qualifying RAB, return on capital (total 285), depreciation (291),
  opex (2,250), allowable revenue (2,826), revenues (1,755), losses (1,071), PV losses forward to 2021 (1,542).
- Quality (lines 285-404): CEPA levels 1-4 (lines 348-351); emerging view "up to CEPA's level 3" (line 358).
- Capex (lines 409-520): Chorus fibre capex snapshot (lines 442-451, garbled, see above); Transpower total capex
  FY 2018 $248.6m; "Capex allowance in price-quality path (3-5 years)" (line 461).

## D08 (Doc 3) - Vodafone submission, 21 December 2018

- Attached but not in the bundle: Frontier Economics report (cost allocation); James Every-Palmer QC opinion (2016).
- Losses (lines 38-49, 393-489): losses "up to when the new regime comes into effect in 2022"; Chorus ROE 2011-2018
  24.4% average, over $300m; analysts' "as much as $2b for Chorus alone" (line 393); 2018 cost per premises
  connected $1,037 vs forecast $1,050-$1,200 (line 416); uptake target 20% by 2020 vs 44.1% (line 419); OVABAA for
  the loss period (lines 434-455); leverage 76% vs 38% FPP estimate (line 479); pre-tax mid-point WACC 6.09% to
  5.37% (line 481); PV of losses at the cost of debt (lines 483-489).
- Competition (lines 63-389): fourth economic principle (line 104); unbundling IM (lines 177-270); Netherlands
  "less than 6%" unbundled by end 2017 (line 212); Table 2 six countries (lines 220-229); EC five non-price issues
  (lines 261-265); Frontier Table 3 (lines 317-325); wash-up (lines 326-345); ONT "less than $100", Layer 2 life
  "around five years" (line 372); no WACC uplift (lines 374-389).
- Products (lines 496-551): anchor review under s 208; pricing methodology with "six-month lead time" (line 524);
  CEPA "Level 2" supported (line 542); "CEPA's six high level categories" ordering, provisioning, switching,
  faults, availability, performance (lines 543-549).

## D02 (Doc 6) - CCHL submission, 21 December 2018

- CCHL assets $3 billion; owns 100% of Enable Services (which owns Enable Networks), 89.3% of Orion, 75% of CIAL
  (lines 17-20, 73); ratepayers invested "~ $500 million" (line 20).
- Build (lines 22-24): commenced 8 November 2011; completed 31 May 2018, "19 months ahead of schedule"; "more than
  200,000" premises; 100Mbps speed doubled from 1 July 2018.
- Dividends estimate $1.7 billion to $3 billion (line 34); December 2010: 1.88 million fixed lines, 58% (1.09 million)
  on fixed broadband (line 45); Chorus VDSL vectoring over 40% / over 30% (line 54); Vodafone HFC covers "one third
  of Enable's UFB footprint" (line 106).
- WACC (line 110): Crown Fibre Holdings 8%-10% range, mid-point 9%; Commission's UCLL/UBA FPP mid-point 5.56%.
- Q20 answer (line 139): "the converse of Method 2" for CCHL's concessional funding.
- Government Policy Statement dated 13 October 2011 (line 112); Minister's announcement 24 May 2011 (line 39).

## D05 (Doc 8) - InternetNZ submission, 21 December 2018

- Five recommendations a)-e) (lines 26-33); 668,000 fibre connections "reported at 30 September", a 45% increase in
  one year (line 53); anchors: 100/20 "proposed as an anchor for 2020-2023", Nielsen's law 50% a year, 750/150 Mb/s
  baseline by 2020, Northpower 10 Gigabit test February 2017 (lines 81-83); data usage up almost 50% (line 85);
  s 208(7) cited for anchor purposes (line 73).

## D01 (Doc 4), D06 (Doc 7), D07 (Doc 5)

See notes/doc-map-D01.md, notes/doc-map-D06.md, notes/doc-map-D07.md (bundle-mapper runs, full sequential reads).

## Shared ground (navigation only)

- Every December 2018 item answers the 9 November 2018 paper (Chorus calls it the "Issues Paper", CCHL the
  "Discussion Document"); the two Commission papers come after them and respond to them.
- Implementation date: original 1 January 2020 and amended 1 January 2022 together in D01 line 87; "two-year
  extension" in D04 line 139; D08 line 116 "pushed out to 2022"; D05 line 81 "anchor for 2020-2023".
- Section numbering differs by source: D01 footnote 6 (line 127) says it uses the Issues Paper's references "which
  reflects the third reading of the Act" and cites losses under section 176 and Crown financing under 170A, while
  D03 line 157 quotes losses as section 177 and D04 line 262 gives s 176 as the IM power. Anchor review: s 208 in
  D08/D05, section 206 in D06.
- Crown financing "Method 1": D04 line 398, D03 lines 168 and 229, D01 lines 136-137, 771-777; "Method 2": D02 line 139 only.
- Quality dimensions: seven in D04 line 548; six CEPA categories in D08 lines 543-549; CEPA levels in D03 lines
  348-351 and D08 line 542.
- FPP WACC: 5.56% mid-point (D02 line 110); 6.09% pre-tax mid-point (D08 line 481).
- Enable premises: 200,000 (D04 line 80); "more than 200,000" (D02 line 24).
- First regulatory period three years: D04 line 163; D01 line 1103 "short (three year) RP1 period".
