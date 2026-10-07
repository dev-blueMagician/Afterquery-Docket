# aq-docket-trial-02 - document map

Written by three bundle mappers in parallel (D01-D04, D05-D08, D09-D12) and merged by the caller on
2026-10-06. Navigation only, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers are text/Dnn.txt lines; the docs/
original line = text line - 2. Arithmetic marked [m] is mapper hand arithmetic; recompute by script.

## Bundle

- What it is: Colgate-Palmolive Company documents: a 2019 performance stock unit award agreement form
  (D01), ten quarterly/annual earnings releases Q1 2024 - Q2 2026 (D02-D09, D11, D12) and a
  segment-information recast exhibit (D10, file dated 2026-03-17).
- Documents: 12; ids from text/manifest.json. Local D01-D12 = platform Doc 1-12 (alphabetical file
  names follow the release dates; checked against the capture's "### Doc N" headings).
- Gaps: none in readable text; every line of every document read (ledgers in each section). The
  source HTML exhibits are not in the bundle, so visual checks of flattened headers/rows are
  unresolved (read by order and arithmetic). Missing from the sources themselves (not extraction
  losses): D01 Exhibit A is blank; the 2013 Plan, Notice of Grant and International Appendix are
  referenced but absent; the recast historical data "on the Company's website" is absent except
  what D10 prints.
- Extraction spot-checks: plain-text captures, method text, no pages; one table row and one footnote
  per document compared with docs/ (identical apart from the 2-line header offset).
- Provenance: notes/intake.json, capture AQ-DOCKET-TRIAL-02_2026-10-06_0110.md (sha256 ded187b3...),
  "12 of 12 captured in full", no gap markers; all documents matches_capture true.

## Shared ground across all parts (caller merge; locations only)

- Three segment structures. S1 (D02, D03: no recast note). S2 effective July 1, 2024 (long-form
  note with the skin-health sentence: D04 l.88, D05 l.113, D06 l.85; short form elsewhere in
  D04-D07; absent from D08-D09). S3 effective for the quarter ended March 31, 2026 (composition
  stated only in D11 l.85; D10 has no notes; D12 l.83/117/457/515/567 short form).
- Original-versus-recast pairs for the same period: Q1 2024 S1 (D02 l.349-374) vs S2 (D06 2024
  column l.359-384); Q2/6M 2024 S1 (D03 l.414-439) vs S2 (D07 2024 columns l.434-459); 2025
  quarters/YTD/FY S2 (D06, D07, D08, D09 Table 5) vs S3 (D10; Q1 2025 also D11 l.369-392; Q2/6M
  2025 also D12 l.428-451); FY2024/FY2023 S2 (D05 Table 5; FY2024 also D09) vs S3 (D10 l.56-59,
  l.93-96). Latin America, Pet Nutrition, Corporate and totals are identical across structures.
- Guidance chains: FY2024 (D02 l.47-53, D03 l.47-53, D04 l.47-53; actual D05), FY2025 (D05
  l.73-79, D06 l.45-51, D07 l.47-53, D08 l.43-49; actual D09), FY2026 (D09 l.77-83, D11 l.45-51,
  D12 l.45-51). Each later edition restates changed items as "(versus ... previously)" except D06's
  FY2025 items ("now expects" without the prior value).
- Productivity programme: announced D07 l.41 ($200-$300 million, by December 31, 2028); named SGPP
  D08 l.37; charges Q4/FY2025 $13 (D09 l.491/495, Table 8/9 "Restructuring programs" with note);
  expansion approved April 30, 2026, $350-$550 million "increased from $200 million to $300
  million" (D11 l.39); Q1 2026 171 OP / 176 pre-tax (D11 l.402, 548); Q2 2026 129 / 129 and 6M
  2026 300 / 305 (D12 l.461, 656, 800).
- Skin health: Europe -> North America (July 2024 notes above); goodwill and intangible assets
  impairment in Q4 2025, pre-tax 919, after-tax 794, "primarily Filorga" (D09 l.69-71, 491, 701);
  North America -> Europe, Middle East & Africa (D11 l.85).
- Russia and Belarus: Africa/Eurasia -> Asia Pacific (D11 l.85 only); "Russia" appears nowhere else
  except as part of that note.
- Prime100: volume-effect footnotes D07-D12; "Payment for acquisition, net of cash acquired" (293)
  D07 l.380, D08 l.365, D09 l.406, D12 l.374; no acquisition date stated anywhere.
- Private label pet exit: D05 l.17/39/75, D06 l.15, D07 l.15/49, D08 l.15/45, D09 l.17/41/79, D11
  l.15/47, D12 l.15/47.
- ERISA litigation matter: 2023 comparatives (267) in D02-D05; Q1 2025 65 pre-tax (D06-D08, D11,
  D12 comparatives); Q4 2025 SG&A (84) offset by non-service +84 (D09 Table 8).
- Market share YTD (headline bullets): toothpaste 41.3/41.5/41.6/41.4/40.9/41.1/41.2/41.3/41.1/41.3;
  manual toothbrush 31.7/32.2/32.3/32.2/31.9/32.4/32.4/32.4/32.6/32.7 (D02-D09, D11, D12).
- Annual meetings: May 9, 2025 (D05 l.156); May 8, 2026 (D09 l.154).
- D01 cites no other document; no release cites D01. D01's performance criteria are absent.


<!-- merged from map-part1.md: aq-docket-trial-02 - document map, part 1 (D01-D04) -->
Written by a bundle mapper for D01-D04 only; the caller merges the parts into `doc-map.md`.
Navigation only: where things are, not what to ask. Line numbers are `text/Dnn.txt` lines;
the `docs/` original line = text line - 2 (text adds the `# Dnn | docs/...` header and a blank line).
Arithmetic marked [m] is mapper hand arithmetic (no script tool in this session) - recompute before use.

## Chunk provenance and extraction spot-checks

- Sources (manifest sha256 = intake.json captured/source sha256; `incomplete: false`, `gap_characters: 0`, `matches_capture: true` for all four):
  D01 `docs/cl_ex991_2019-03-20.txt` 45e30794...1802 (130 text lines); D02 `docs/cl_ex991_2024-04-26.txt` b76cfabe...dfde (538);
  D03 `docs/cl_ex991_2024-07-26.txt` 59fcb3d9...49fbbaf (792); D04 `docs/cl_ex991_2024-10-25.txt` d5507b36...30ea2c (786).
- Method `text`, `pages: null` for all four: the originals are plain-text captures. The HTML exhibits they came from
  (`c93240_ex99.htm`, `q12024pressreleasetables.htm`, `q22024pressreleasetables.htm`, `q32024pressreleasetables.htm`) are not in the bundle, so
  a visual page check is unresolved. Page count: D01 prints page numbers 2-6 (lines 59, 81, 97, 111, 125), then Exhibit A; D02-D04 not applicable (no page markers).
- Spot-checks against `docs/` (all identical apart from the 2-line offset):
  D01 table: not applicable; detail: "March 15, 2022" (orig 49 = text 51) and Exhibit A "[Intentionally Left Blank]" (orig 127 = text 129), so the blank is in the source.
  D02 table: Table 1 Net sales row (orig 165 = text 167) and division Total Company row (orig 77 = text 79); footnotes: marketable securities (orig 249 = text 251), Emerging Markets (orig 426 = text 428).
  D03 table: Table 2 Net sales $10,124 (orig 227 = text 229) and Hill's division row (orig 76 = text 78); footnotes: EPS note (orig 272 = text 274), Foreign tax matter rows (orig 655/777 = text 657/779).
  D04 table: Table 2 Net sales $15,156 (orig 236 = text 238) and Table 5 North America(1) row (orig 421 = text 423); footnote: recast (orig 86, 114, 450, 504, 552 = text 88, 116, 452, 506, 554).
- Layout: Markdown pipe tables plus ```text fences. Several multi-column headers are split across lines and some rows sit outside their fence
  (listed per document). Every split header was resolved by matching the values against a companion table in the same release.

## D01 - Colgate-Palmolive Company 2019 Performance Stock Unit Award Agreement (form)

- Source: `docs/cl_ex991_2019-03-20.txt` | text lines 1-130. Header lines 3-7: "EX-99", "2 c93240_ex99.htm", "Exhibit 99".
  The file-name date 2019-03-20 is not printed anywhere in the document text.
- Written or submitted by: Colgate-Palmolive Company (signature block "COLGATE-PALMOLIVE COMPANY / Authorized Signature", lines 117-119; no signatory named).
  The counterparty is "the individual named on the Notice of Grant ('you')" (line 13), who is not named.
- Type, date, edition: award agreement form titled "2019 PERFORMANCE STOCK UNIT AWARD AGREEMENT" (line 11). It is "effective as of the date indicated on the
  Notice of Grant delivered herewith" (line 13), and the Notice of Grant is not included. There is no version or edition marker beyond "2019".
- Period covered: "Performance Period (as defined in Exhibit A)" (line 37). Exhibit A (lines 127-129) is "[Intentionally Left Blank]" in the source, so
  neither the Performance Period dates/length nor the Performance Criteria appear in the document. The only printed years/dates are "2019" (title, line 11),
  "2013" (the Plan's name, line 17) and "March 15, 2022" (line 51). Page 1 is unnumbered (lines 7-57), pages 2-6 are marked at lines 59/81/97/111/125, and Exhibit A follows at line 127.
- Entities and aliases:
  - "Colgate Palmolive Company, a Delaware corporation (the 'Company')" (line 13). It is spelled without the hyphen at lines 13 and 17 and as "COLGATE-PALMOLIVE COMPANY" at lines 9 and 117.
    The Data Privacy section redefines "Company" as "the Company, its subsidiaries and Affiliates (collectively referred to in this Data Privacy section as the 'Company')" (line 107).
  - "Plan" = "the Colgate Palmolive Company 2013 Incentive Compensation Plan" (lines 17-19); not in the bundle.
  - "PBRSUs" = "performance-based Restricted Stock Units" (line 19). The title says "Performance Stock Unit"; §8(d) says "the related Restricted Stock Unit Award" (line 89).
    Other names used: "Award" (line 31), "Award Agreement" (line 89), "Agreement" (line 13), "Target PBRSUs" (line 31).
  - Defined in the Agreement: "Notice of Grant" (13), "Target PBRSUs" (31), "Performance Criteria" (37), "Certification Date" (37), "Data" and "Providers" (107), "Merrill" (85).
  - Capitalized but not defined here (line 27: "Capitalized terms used and not otherwise defined in this Agreement shall have the meanings set forth in the Plan"):
    Committee, Affiliate, Share(s), Common Stock, Fair Market Value, Retirement, Disability, Cause, Change in Control.
  - "Merrill, Lynch, Pierce, Fenner & Smith Incorporated ('Merrill')" is "the Company's plan administrator" (line 85). Acceptance is through the "Merrill BenefitsOnline system" (line 121).
  - Also named: the Secretary at the Company's principal executive offices (85), the Delaware Court of Chancery (89), Section 409A of the Code (103),
    and the "International Appendix hereto" (57), which is referenced but absent from the text.
- Tables: not applicable (no tables).
- Lists:
  - Sections: 1 Grant of Award (29-31); 2 Vesting of Award (33): (a) Vesting Upon Performance and Continued Service (35-37), (b) Termination of Employment due to
    Death, Disability or Retirement (39-41), (c) Vesting Upon a Change in Control (43), (d) Forfeiture of Unvested PBRSUs (45), (e) Repayment (47);
    3 Distribution of Shares (49): (a) Distribution Upon Vesting (51), (b) Forfeiture of Shares; Termination for Cause (53-55), (c) Compliance With Law (57-61);
    4 No Stockholder Rights (63); 5 Tax Withholding (65-71); 6 PBRSUs Not Transferable (73); 7 Plan Incorporated (75);
    8 Miscellaneous (77) with eleven items (a)-(k): (a) No Guaranteed Employment 79-83, (b) Notices 85, (c) Binding Agreement 87, (d) Governing Law; Jurisdiction 89,
    (e) Severability 91, (f) Interpretation 93, (g) Entire Agreement 95, (h) No Waiver 99, (i) Section 409A of the Code 101-103, (j) Data Privacy 105-113,
    and the last, (k) Counterparts 115. Then the acceptance paragraph (121-123) and Exhibit A (127-129).
  - §2(b) has three triggers (39-41): "(A) you begin to receive benefits under the Company's long-term disability plan, (B) you terminate your employment ... due to
    Retirement or (C) your employment ... terminates due to your death".
  - §3(b) has two Cause triggers (55): (i) termination for Cause; (ii) termination for any reason where "before the Certification Date it is discovered that you engaged in
    conduct that would have justified termination for Cause".
- Forecasts, guidance, deadlines, effective dates:
  - Vesting date: "as of the Certification Date" (37; also 41).
  - Distribution (51): "as soon as administratively practicable, but no later than the earlier of (i) 60 days after the Certification Date, and (ii) March 15, 2022."
  - §2(b) eligibility (39-41): "employed ... for at least six months of the Performance Period", with the trigger occurring "in each case on or before the Certification Date". Then
    "the remaining portion of the Performance Period shall continue through its last day".
  - Tax (67): payment due "No later than the date as of which an amount first becomes includible in your gross income".
  - Acceptance (121-123): "If you do not do so prior to the Certification Date, then the Company may declare the Award null and void at any time."
- Hedged claims (what the qualifier attaches to):
  - "Unless otherwise determined by the Committee" qualifies the whole §2(b) pro-rata rule (39).
  - "or as otherwise determined by the Committee" qualifies the §2(d) forfeiture (45).
  - In §2(e), "may" attaches to the policies the Committee "may adopt from time to time". The Agreement's being "subject to" those policies is stated firmly (47).
  - §3(c): "The Company, in its discretion, may postpone the vesting ..." (61). §5: "Unless otherwise determined by the Company, withholding obligations may be settled with Common Stock" (67).
  - The acceptance paragraph's "may declare the Award null and void" (123) is permissive.
  - §8(i): "This Agreement is intended to comply with the requirements of Section 409A" (103) is a statement of intent.
  - Data Privacy uses "may" in several places: "may hold" (107), "may be necessary" (109), "may affect your ability to participate" (109, 113).
- Rounded prose beside exact figures: not applicable.
- Notes: the keyword "dividend" appears only in §4 (63: "you have no right to vote or receive dividends"). There is no dividend-equivalent provision.
- Operative definitions, rules and scope exceptions:
  - §1 (31): "Each PBRSU is equivalent to one Share." The Plan "is incorporated herein by reference".
  - §2(a) (37) gives the general vesting rule, subject to the opening "Except as otherwise provided in Section 2(b) and Section 2(c) below".
    The rule: "if (i) the Committee certifies in writing the extent to which the applicable Performance Criteria in the Performance Period are attained and (ii) you remain continuously employed ...
    through the date on which the Committee certifies such performance (the 'Certification Date'), you will become vested in the number of PBRSUs earned pursuant to Exhibit A as of the Certification Date".
  - §2(b) pro-rata formula (41): the product of "(x) the total number of PBRSUs earned with respect to the Performance Period based on actual performance" and "(y) a fraction". The numerator
    "is the total number of days in the Performance Period during which you are employed ... (or, in the case of (A) above, the number of days during the Performance Period
    before you began receiving benefits under the Company's long-term disability plan)". The denominator "is the total number of days during the Performance Period".
  - §2(c) (43): "The treatment of your PBRSUs in the event of a Change in Control shall be governed by Section 11 of the Plan." Section 11 is not in the bundle.
  - §2(d) (45) covers termination "for any reason during the Performance Period or the period after the Performance Period and before the Certification Date". The PBRSUs are
    "forfeited and canceled as of the date of such termination". The exceptions are §2(b), §2(c) and a Committee determination.
  - §3(b) (55) opens "Notwithstanding any provision of this Agreement or the Plan to the contrary". Unvested PBRSUs are "immediately forfeited and canceled as of such termination date".
  - §4 (63): there are no stockholder rights "unless and until your Shares shall have been issued".
  - §5 (67): stock withholding uses Fair Market Value "on the date of withholding". §6 (73): PBRSUs are not transferable except under the Plan.
  - Precedence: §7 (75) says "In the event of a conflict between this Agreement and the Plan, the Plan shall prevail". The same section makes Committee decisions "final and conclusive".
    §8(a) (83) says "To the extent there is a conflict between this Agreement and such an employment contract as it relates to the PBRSUs ... the terms of this Agreement shall govern and take priority".
    §8(f) (93) says captions are "for convenience only". §8(g) (95) supersedes all prior agreements.
  - §8(d) (89): Delaware law; disputes go to "the Delaware Court of Chancery or if not maintainable therein, then before an appropriate federal or state court located in Delaware"; jurisdiction is "non-exclusive".
  - §8(i) (103): "In no event may you, directly or indirectly, designate the calendar year of any payment".
  - Data Privacy: consent can be withdrawn "without cost, by contacting your local human resources representative in writing" (109). "the only adverse consequence of refusing or withdrawing
    your consent is that the Company would not be able to grant PBRSUs or other equity awards or administer or maintain such awards" (113).
- Amendments or contradictions: none within the document. Its internal precedence rules are listed above. The title's "Performance Stock Unit" and the body's
  "performance-based Restricted Stock Units" are a naming difference only.
- Coverage: full. Lines 1-130 were read in one pass. Original header region and two details were spot-checked. Missing source material (not an extraction gap):
  Exhibit A content, the Notice of Grant, the 2013 Plan and the International Appendix.

## D02 - Colgate Announces 1st Quarter 2024 Results

- Source: `docs/cl_ex991_2024-04-26.txt` | text lines 1-538. Header lines 3-11: "EX-99", "2 q12024pressreleasetables.htm", "Exhibit 99".
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL), New York. Quoted: "Noel Wallace, Chairman, President and Chief Executive Officer", commenting on the Base Business results (35).
  Contacts (149-151): investor_relations@colpal.com and colgate_palmolive_media_inquiry@colpal.com. Mentioned third parties: Nielsen as the market share vendor (117) and the SEC.
- Type, date, edition: earnings press release "Colgate Announces 1st Quarter 2024 Results" (13), dated "New York, New York, April 26, 2024" (35). It is the Q1 2024 edition of the quarterly series.
- Period covered: three months ended March 31, 2024 vs 2023 (159). Balance sheet as of March 31, 2024, December 31, 2023 and March 31, 2023 (217). Cash flows for three months (259).
  Market share is "year to date" (15). Guidance is for "Full Year 2024" (43). The fiscal year ends December 31: the release cites the "Annual Report on Form 10-K for the year ended December 31, 2023" (125).
  Quarter labels used: "1Q 2024", "first quarter 2024".
- Entities and aliases:
  - Divisions: North America, Latin America, Europe, Asia Pacific, Africa/Eurasia and Hill's (71-79). The segment table groups the first five under "Oral, Personal and Home Care" and shows "Pet Nutrition" (345-356).
    Hill's and Pet Nutrition carry identical figures (operating profit $199 at line 97 = Pet Nutrition 199 at line 372).
  - "Total CP Products" (Table 5, 418) is not defined in the text. Its 6.8% equals Total Oral, Personal and Home Care 3,963 vs 3,709 (354) [m].
  - "Emerging Markets" is defined (428). "Developed Markets" (424) is not defined.
  - Items and programs: "2022 Global Productivity Initiative", "ERISA litigation matter", "product recall costs".
  - "About" section (115): "Colgate Bright Smiles, Bright Futures program, which has reached approximately 1.7 billion children and their families since 1991".
- Tables ($ millions except per share; "Unaudited"):
  - Headline GAAP table (19-23): Net Sales $5,065 vs $4,770, +6.2 %; EPS (diluted) $0.83 vs $0.45, +84 %.
  - Headline Base Business table (25-31): Organic Sales Growth +9.8 %, with no 2023 value printed; Base Business EPS (diluted) $0.86 vs $0.73, +18 %.
  - First Quarter Sales Growth By Division (59-81): % change 1Q 2024 vs 1Q 2023.
    - The header is split over lines 63-70 and the Total Company row (79) sits outside the fence.
    - Columns: % of Total Company Sales | Net Sales | Organic Sales* | As Reported Volume | Organic Volume | Pricing | FX. The order is confirmed against Table 5 (e.g. Latin America 72 = 410).
  - First Quarter Operating Profit By Division (85-103): $ millions; columns are % Change vs 1Q 2023, % to Net Sales, and bp change.
    Total Company As Reported $1,047 (15%, 20.7%, +160); Base Business $1,083 (15%, 21.4%, +170).
  - Table 1 Income Statement, Q1 (153-209): gross profit margin 60.0%/56.9% (171), operating profit margin 20.7%/19.1% (179), ETR 24.6%/26.2% (188), EPS (199-200),
    average shares basic 822.8/831.4 and diluted 825.9/833.0 (207-208; share unit not stated), Advertising $672/$579 (209).
  - Table 2 Balance Sheets (211-251): three columns. Supplemental net debt $7,379/$7,404/$7,764 and working capital % of sales (2.2)%/(1.4)%/(0.4)% (245-246). Note (1) marketable securities $231/$179/$276 (251).
  - Table 3 Cash Flows, three months (253-328):
    - Operations 681/735 (287); capex (126)/(163) (293).
    - "Principal payments on debt" (500)/(500) (304); Dividends paid (394)/(390) (306); Purchases of treasury shares (509)/(180) (307).
    - Free cash flow before dividends 555/572 (324); income taxes paid 150/171 and interest paid 123/94 (327-328).
  - Table 4 Segment Information (331-382): Net sales (349-356) and Operating profit (366-374), including Corporate(1) (196)/(168). Footnotes are at 378-382.
  - Table 5 Geographic Sales Analysis, Q1 (384-428): header fragments at 394-404.
    - Columns: Sales Change As Reported | Organic Sales Change | As Reported Volume | Organic Volume | Pricing Coupons Consumer & Trade Incentives | Foreign Exchange.
    - Rows include Total CP Products (418), Emerging Markets(1) (422) and Developed Markets (424).
  - Table 6 Non-GAAP Reconciliations, Q1 (430-537):
    - SG&A (442-445); Other (income) expense (446-450).
    - Operating profit (452-458) and the OP margin row (462) are both flattened onto single lines.
    - Non-service postretirement costs (464-470).
    - Continued pages: IBT, tax, NI incl. NCI, NCI, NI attributable, ETR and diluted EPS for 2024 (484-509) and 2023 (511-529). The "Product recall costs" 2023 row (524) is outside the fence. Notes are at 531-537.
    - D02 has no gross profit reconciliation and no SG&A-%-of-net-sales reconciliation.
- Lists:
  - Headline bullets (line 15): seven. The last is "The Company updated its financial guidance for full year 2024".
  - Guidance bullets: four (47-53).
  - Base Business excluded items (131): three. Measures disclosed on both bases (139): nine, beginning with "Selling, general and administrative expenses"; Gross Profit is not listed.
  - Brands (115): 22 named (Colgate ... Suavitel) plus "Hill's Science Diet and Hill's Prescription Diet". Categories: Oral Care, Personal Care, Home Care and Pet Nutrition.
  - Forward-looking topics (123) include "the impact of the war in Ukraine, the impact of the Israel-Hamas war, cost-reduction plans (including the 2022 Global Productivity Initiative)".
- Forecasts, guidance, deadlines, effective dates (Full Year 2024; "Based on current spot rates:" at 45 heads all four bullets):
  - Net sales (47), raised: "The Company is raising its net sales growth guidance to 2% to 5% (versus 1% to 4% previously) including a mid-single-digit negative impact from foreign exchange (versus low-single-digit negative impact previously)."
  - Organic (49), raised: "The Company is raising its organic sales growth guidance to 5% to 7% (versus 3% to 5% previously)."
  - GAAP (51), maintained: "On a GAAP basis, the Company still expects gross profit margin expansion, increased advertising investment and double-digit earnings-per-share growth."
  - Base Business (53), maintained: "On a non-GAAP (Base Business) basis, the Company still expects gross profit margin expansion, increased advertising investment and mid to high-single-digit earnings-per- share growth."
  - There is no numeric gross margin, advertising or tax-rate guidance, and no EPS dollar guidance.
  - Other wording: "The Company updated its financial guidance" (15); "our updated 2024 financial targets" (41); "we expect strong levels of brand investment over the balance of 2024" (39).
  - The "previously" values (1% to 4%, 3% to 5%, low-single-digit FX) are stated only here within D01-D04.
  - Release timing (109-111): prepared materials "At approximately 7:00 a.m. ET today"; conference call "At 8:30 a.m. ET today".
  - No acquisitions, divestitures, dividend declarations, impairments, program approvals or board actions appear. "dividend" occurs only in the FCF definition/discussion (135, 143) and the cash flow table (306, 318, 324).
- Hedged claims:
  - "Based on current spot rates" (45) covers all four guidance bullets.
  - "we expect strong levels of brand investment" (39).
  - Forward-looking boilerplate (123-125).
  - Market share data "typically reflects a lag time of one or two months" (119). The Company "has not verified the accuracy or completeness" of the vendor data (119).
  - Non-GAAP measures "may not be the same as or comparable to similar measures presented by other companies" (129).
  - "Table may not sum due to rounding" (81, 376, 426). "may not necessarily equal" (531).
- Rounded prose beside exact figures:
  - "a 16% increase in advertising" (39) vs Table 1 $672 vs $579 (209): ratio 1.1606 [m].
  - "GAAP EPS increased 84% to $0.83" (15) vs $0.83/$0.45 (200): 84.4% [m].
  - "Base Business EPS* increased 18% to $0.86" (15) vs $0.86/$0.73 (508, 528): 17.8% [m].
  - "GAAP Gross profit margin and Base Business Gross profit margin* increased 310 basis points to 60.0%" (15) vs 60.0%/56.9% (171).
  - "$681 million for the first three months" (15) vs 681 (287).
  - Hill's "% to Net Sales" is printed 18.0% (97), while 199/1,102 (355, 372) = 18.06% [m].
- Notes (period adjustments, Table 6):
  - Q1 2024, 2022 GPI: SG&A (1) (444), Other (35) (448), OP 36 (456). Row 507: IBT 36, tax 6, NI 30, ETR (0.3)%, EPS 0.03.
  - Q1 2023, ERISA litigation matter: non-service postretirement (267) (468). Row 521: IBT 267, tax 55, NI 212, ETR (1.8)%, EPS 0.25.
  - Q1 2023, product recall costs: Other (25) (449). Row 524: IBT 25, tax 6, NI 19, EPS 0.02.
  - Q1 2023, GPI: OP 5 plus non-service 1 (469). Row 527: IBT 6, tax 1, NI 5, ETR (0.1)%, EPS 0.01.
  - Corporate OP notes: Q1 2024 GPI $36 (380); Q1 2023 product recall $25 and GPI $5 (382).
- Operative definitions, rules and scope exceptions:
  - Base Business (131): "Base Business operating results exclude, as applicable, charges related to an ERISA litigation matter, the 2022 Global Productivity Initiative and product recall costs."
  - Organic sales growth (133): "Net sales growth excluding the impact of foreign exchange, acquisitions and divestments."
  - Free cash flow before dividends (135): "Net cash provided by operations less Capital expenditures."
  - General non-GAAP exclusions (139): "such as restructuring charges, charges for certain litigation and tax matters, acquisition-related costs, gains and losses from certain divestitures and certain other unusual, non-recurring items".
    The measures are also used "as factors in determining compensation" (141).
  - Market share (117) is "the percentage of the dollar value of sales ... (excluding Venezuela from all periods)", based "primarily [on] Nielsen" and internal estimates.
    Year-to-date runs "from January 1 of the relevant year through the most recent period for which market share data is available" (119).
  - Corporate operations (378) "include costs related to stock options and restricted stock units, research and development costs, Corporate overhead costs, restructuring and related implementation charges and gains and losses on sales of non-core product lines and assets."
  - Emerging Markets (428) "include Latin America, Asia (excluding Japan), Africa/Eurasia and Central Europe."
  - Table 6 notes (535-537) explain the tax effect basis and the ETR impact definition.
- Amendments or contradictions: the guidance changes against its own "previously" values (47-49). No internal conflicts beyond rounding.
- Coverage: full. Lines 1-150, 150-349 and 350-538 were read.

## D03 - Colgate Announces 2nd Quarter 2024 Results

- Source: `docs/cl_ex991_2024-07-26.txt` | text lines 1-792. Header lines 3-11: "EX-99", "2 q22024pressreleasetables.htm", "Exhibit 99".
- Written or submitted by: Colgate-Palmolive Company. Noel Wallace (same title) is quoted on the Base Business results (35).
- Type, date, edition: "Colgate Announces 2nd Quarter 2024 Results" (13), dated "New York, New York, July 26, 2024" (35). It is the Q2 2024 edition.
- Period covered: three and six months ended June 30, 2024 vs 2023. Balance sheet as of June 30, 2024, December 31, 2023 and June 30, 2023 (282). Cash flows for six months only (324).
  Guidance is for Full Year 2024 (43). The 10-K reference "year ended December 31, 2023" is at 127.
- Entities and aliases: as D02, plus "a foreign tax matter" (133; Table 8 row 657; Table 9 row 779). "Total CP Products" appears at 485 and 531.
- Tables ($ millions except per share; unaudited):
  - Headline GAAP (19-23): Net Sales $5,058 vs $4,822, +4.9 %; EPS $0.89 vs $0.60, +48 %.
  - Headline Base (25-31): Organic +9.0 %; Base EPS $0.91 vs $0.77, +18 %.
  - Second Quarter Sales Growth By Division (59-82): columns as in D02. The Hill's row (78) and Total Company row (80) are outside the fence. The column order is confirmed against Table 6 (473-487).
  - Second Quarter OP By Division (86-105): the Hill's row (100) is outside the fence. Total As Reported $1,092 (12%, 21.6%, +140); Base $1,118 (13%, 22.1%, +150).
  - Table 1 Income, Q2 (157-213): ETR 24.1%/39.8% (192); Advertising $706/$601 (213).
  - Table 2 Income, six months (215-274): EPS basic(1) $1.72/$1.05 (260) and diluted(1) $1.71/$1.05 (262); Advertising $1,378/$1,180 (270); note (1) at 274.
  - Table 3 Balance Sheets (276-316).
  - Table 4 Cash Flows, six months (318-394):
    - Operations 1,671/1,457 (352); capex (243)/(347) (358).
    - "Principal payments on debt" (500)/(903) (369); Dividends paid (867)/(847) (371); treasury shares (989)/(551) (372).
    - FCF before dividends 1,428/1,110 (389).
  - Table 5 Segment Information, three and six months (396-449): net sales (414-421), OP (431-439), footnotes (443-449).
  - Table 6 Geographic, Q2 (451-495). Table 7 Geographic, six months (497-541).
  - Table 8 Non-GAAP, Q2 (543-666):
    - Gross profit (555-558) and GP margin (562-564).
    - SG&A (568-571) and SG&A % of net sales (575-579).
    - Other (583-586); OP (588-594); OP margin (598, flattened); non-service (602-605).
    - Continued: 2024 (641-645) and 2023 (655-660). Notes are at 662-666.
  - Table 9 Non-GAAP, six months (668-791):
    - GP (680-683) and GP margin (685-687).
    - SG&A (691-694) and SG&A % (698-702).
    - Other (706-710); OP (712-718); OP margin (722); non-service (726-730).
    - Continued: 2024 (762-766) and 2023 (776-785). The 2023 "Product recall costs" (783) and "Non-GAAP" (785) rows are outside the fence. Notes are at 787-791.
- Lists:
  - Headline bullets (15): seven. The last is "The Company updated its financial guidance for full year 2024".
  - Base Business excluded items (133): four. Measures on both bases (141): eleven, beginning "Gross Profit, Gross Profit margin".
  - Brands (117): same list as D02 115. Forward-looking topics (125): same war wording as D02.
- Forecasts, guidance, deadlines, effective dates (Full Year 2024; "Based on current spot rates:" at 45):
  - Net sales (47), maintained: "The Company still expects net sales growth of 2% to 5% including a mid-single-digit negative impact from foreign exchange."
  - Organic (49), raised: "The Company is raising its organic sales growth guidance to 6% to 8% (versus 5% to 7% previously)."
  - GAAP (51), maintained: "On a GAAP basis, the Company still expects gross profit margin expansion, increased advertising investment and double-digit earnings per share growth."
  - Base Business (53), EPS raised/quantified: "On a non-GAAP (Base Business) basis, the Company still expects gross profit margin expansion and increased advertising investment and increased its earnings per share growth guidance to 8% to 11% (versus mid to high-single-digit previously)."
  - Other wording: "deliver on our increased 2024 organic sales and Base Business earnings growth expectations" (41); "The strong levels of investment should continue in the balance of the year" (39).
  - No tax-rate or numeric margin/advertising guidance. Release date July 26, 2024 (35); webcast timing (111-113). No acquisitions, divestitures, dividend declarations, impairments or board actions (keyword sweep).
- Hedged claims: "should continue" (39); "Based on current spot rates" (45); boilerplate (125-127); the EPS note's "may not equal" (274); rounding notes (82, 441, 493, 539, 607, 662, 787).
- Rounded prose beside exact figures:
  - "an 18% increase in advertising in the quarter" (39) vs Table 1 $706 vs $601 (213). The printed figures give 1.1747: 17.5% at one decimal, 17% at whole-percent rounding [m]. The release does not state the basis of its 18%.
  - Division OP table (Q2) printed % change vs the printed Table 5 dollars:
    - Asia Pacific "16%" (96) vs 195/169 = 15.4% (434) [m].
    - Africa/Eurasia "4%" (97) vs 64/62 = 3.2% (435) [m].
    - Asia Pacific "% to Net Sales" 28.7% (96) vs 195/682 = 28.6% (417) [m].
  - Bullets (15): EPS 48% (0.89/0.60) and 18% (0.91/0.77). Gross margin +280 bp to 60.6% and Base +300 bp to 60.8% (562-564). "$1,671 million for the first six months" vs 1,671 (352).
- Notes:
  - Prose-only comparatives and claims (35-39):
    - "(on top of 8.2% organic sales growth in the year ago quarter)" (37); no 2023 organic figure is in any table.
    - "every operating division delivered positive volume growth in the quarter" (37); Table 6 volumes are all positive (475-487).
    - "This is our fourth consecutive quarter delivering gross margin expansion and double-digit growth in operating profit, net income and earnings per share" (39).
  - Period adjustments, Q2 2024 GPI: GP 9 (557), SG&A (2) (570), Other (16) (585), OP 27 (592). Row 643: IBT 27, tax 4, NI 23, ETR (0.3)%, EPS 0.02.
  - Q2 2023:
    - Foreign tax matter, row 657: tax (126), NI 126, ETR (14.2)%, EPS 0.15.
    - GPI: SG&A (2), Other (16), OP 18, non-service (3) (604). Row 658: IBT 21, tax 4, NI incl. NCI 17, NCI 1, NI 16, ETR (0.2)%, EPS 0.02.
  - H1 2024 GPI: GP 9 (682), SG&A (3) (693), Other (51) (708), OP 63 (716). Row 764: IBT 63, tax 10, NI 53, ETR (0.3)%, EPS 0.07.
  - H1 2023:
    - ERISA (row 778): 267/55/212, ETR (2.2)%, EPS 0.25.
    - Foreign tax (row 779): ETR (7.3)%, EPS 0.15.
    - GPI (row 780): IBT 27, tax 5, NCI 1, NI 21, ETR (0.1)%, EPS 0.03.
    - Product recall (row 783): 25/6/19, EPS 0.02.
  - Corporate OP notes: Q2 2024/Q2 2023 GPI $27/$18 (445); H1 2024 GPI $63 (447); H1 2023 product recall $25 and GPI $23 (449).
- Operative definitions, rules and scope exceptions:
  - Base Business (133): "Base Business operating results exclude, as applicable, charges related to an ERISA litigation matter, a foreign tax matter, the 2022 Global Productivity Initiative and product recall costs."
  - Organic (135) and FCF (137) are worded as in D02.
  - EPS note (274): "Basic and diluted earnings per share are computed independently for each quarter and any year-to-date period presented ... the sum of the quarters' earnings per share may not equal the earnings per share for any year-to-date period."
  - Corporate footnote (443) is as D02. Emerging Markets (495, 541) is as D02. Market share (119-121) is as D02.
- Amendments or contradictions:
  - Guidance changes against D02 (see Shared ground).
  - The Base Business definition adds "a foreign tax matter" (133 vs D02 131).
  - Within-table rounding: Q2 non-GAAP OP is printed $1,118 (594), while GAAP 1,092 + GPI 27 = 1,119 [m]; note 607 says "Tables may not sum due to rounding".
- Coverage: full. Lines 1-130, 130-349, 350-599 and 599-792 were read.

## D04 - Colgate Announces 3rd Quarter 2024 Results

- Source: `docs/cl_ex991_2024-10-25.txt` | text lines 1-786. Header lines 3-11: "EX-99.1", "2 q32024pressreleasetables.htm", "Exhibit 99.1"; D01-D03 say "Exhibit 99".
- Written or submitted by: Colgate-Palmolive Company. Noel Wallace (same title) is quoted on the Base Business results (35).
- Type, date, edition: "Colgate Announces 3rd Quarter 2024 Results" (13), dated "New York, New York, October 25, 2024" (35). It is the Q3 2024 edition.
- Period covered: three and nine months ended September 30, 2024 vs 2023. Balance sheet as of September 30, 2024, December 31, 2023 and September 30, 2023 (291). Cash flows for nine months only (333).
  Guidance is for Full Year 2024 (43). The 10-K reference "year ended December 31, 2023" is at 138.
- Entities and aliases: as D02/D03, plus "the skin health business", the "Europe reportable operating segment" and the "North America reportable operating segment" (88).
  Rows marked North America(1) and Europe(1) carry the recast footnote. The Corporate footnote is renumbered (2) (447, 454) and Emerging Markets is (2) (500, 548).
- Tables ($ millions except per share; unaudited):
  - Headline GAAP (19-23): Net Sales $5,033 vs $4,915, +2.4 %; EPS $0.90 vs $0.86, +5 %.
  - Headline Base (25-31): Organic +6.8 %; Base EPS $0.91 vs $0.86, +6 %.
  - Third Quarter Sales Growth By Division (59-88): rows are split across fences (71-84).
    % of Total Company Sales: North America 20%, Latin America 23%, Europe 15%, Asia Pacific 14%, Africa/Eurasia 6%, Hill's 22% (72-82).
  - Third Quarter OP By Division (92-116): North America $206 -9%; Latin America $365 -2%; Europe $181 10%; Asia Pacific $199 3%; Africa/Eurasia $65 -1%; Hill's $258 28%.
    Total As Reported $1,065 (4%, 21.2%, +30); Base $1,080 (5%, 21.5%, +50). Short recast footnote at 116.
  - Table 1 Income, Q3 (166-222): ETR 21.3%/21.9% (201); Advertising $694/$598 (222).
  - Table 2 Income, nine months (224-283): EPS basic(1) 2.62/1.91 (269) and diluted(1) 2.61/1.90 (271); Advertising $2,072/$1,778 (279); note (1) at 283.
  - Table 3 Balance Sheets (285-325).
  - Table 4 Cash Flows, nine months (327-403):
    - Operations 2,838/2,609 (361); capex (377)/(508) (367).
    - "Principal payments of debt" (502)/(903) (378); Dividends paid (1,275)/(1,243) (380); treasury shares (1,284)/(883) (381).
    - FCF before dividends 2,461/2,101 (398).
  - Table 5 Segment, three and nine months (405-460): net sales (423-430), OP (440-448), notes (450-460).
  - Table 6 Geographic, Q3 (462-508). Table 7 Geographic, nine months (510-556).
  - Table 8 Non-GAAP, Q3 (558-671):
    - GP (570-573) and GP margin (577-579); SG&A and Other in one pipe table (583-590).
    - OP (592-598); OP margin (602).
    - Continued: 2024 (636-640) and 2023 (660-665); the 2023 As Reported row (660) is outside the fence. Notes are at 667-671.
    - There are no SG&A-% rows and no non-service rows for Q3.
  - Table 9 Non-GAAP, nine months (673-785):
    - GP (685-688) and GP margin (690-692); SG&A and Other (696-704).
    - OP (706-712); OP margin (716); non-service (720-724).
    - Continued: 2024 (756-760) and 2023 (770-779); the "Product recall costs" (777) and "Non-GAAP" (779) rows are outside the fence. Notes are at 781-785.
- Lists:
  - Headline bullets (15): seven. The last is "The Company updated its financial guidance for full year 2024".
  - Base Business excluded items (144): four, worded "an ERISA litigation matter, a foreign tax matter and the 2022 Global Productivity Initiative and product recall costs".
  - Measures on both bases (152): eleven, as in D03. Brands (128): same list as D02/D03.
  - Forward-looking topics (138) read "the impact of the wars in Ukraine and the Middle East"; D02 123 and D03 125 read "the war in Ukraine, the impact of the Israel-Hamas war".
- Forecasts, guidance, deadlines, effective dates (Full Year 2024; "Based on current spot rates:" at 45):
  - Net sales (47): "The Company now expects net sales growth of 3% to 5% (versus 2% to 5% previously) including a mid-single-digit negative impact from foreign exchange."
  - Organic (49): "The Company now expects organic sales growth of 7% to 8% (versus 6% to 8% previously)."
  - GAAP (51), maintained: "On a GAAP basis, the Company still expects gross profit margin expansion, increased advertising investment and double-digit earnings per share growth."
  - Base Business (53): "On a non-GAAP (Base Business) basis, the Company still expects gross profit margin expansion and increased advertising investment and now expects earnings per share growth of 10% to 11% (versus 8% to 11% previously)."
  - The verb for each changed item is "now expects", not "raising". The headline says "updated" (15). The CEO says "our updated 2024 organic sales and Base Business earnings growth expectations" (41)
    and "We expect continued strong advertising investment through the remainder of the year" (39).
  - Effective date: reporting structure "effective as of July 1, 2024" (88, 116, 452, 506, 554). Release date October 25, 2024 (35).
  - No acquisitions, divestitures, dividend declarations, impairments or board actions (keyword sweep).
- Hedged claims: "Based on current spot rates" (45); "We expect continued strong advertising investment" (39); boilerplate (138); the EPS note (283); rounding notes (86, 450, 504, 552, 667, 781).
  "with earnings exceeding our expectations" (35) appears; no Q3 earnings expectation figure is printed in D02-D04.
- Rounded prose beside exact figures:
  - "Advertising increased 16% in the quarter" (39) vs $694/$598 (222): 16.05% [m].
  - "GAAP EPS increased 5% to $0.90" (15) vs 0.90/0.86: 4.65% [m]. "Base Business EPS* increased 6% to $0.91": 0.91/0.86 = 5.8% [m].
  - Total Company As Reported OP is printed "4%" (112, 594) vs 1,065/1,029 = 1.034985, i.e. 3.4985% [m]. Base is printed 5% vs 1,080/1,031 = 4.75% [m].
  - Africa/Eurasia OP is printed "-1%" (106) vs 65/66 = -1.5% (444) [m].
  - Gross margin bullets (15): +260 bp to 61.1% and Base +270 bp to 61.3% (577-579). "$2,838 million for the first nine months" vs 2,838 (361).
- Notes:
  - Prose-only figures and claims:
    - "(on top of 8.8% organic sales growth in the year ago quarter)" (35-37).
    - "Every operating division delivered positive volume growth for the second consecutive quarter" (37); the Q3 volumes are all positive (484-498).
    - "This is our sixth consecutive quarter delivering gross margin expansion along with growth in operating profit, net income and earnings per share" (39); the "double-digit" qualifier is absent.
  - Q3 2024 GPI: GP 9 (572), SG&A (3) (585), Other (3) (589), OP 15 (596). Row 638: IBT 15, tax 2, NI 13, ETR (0.1)%, EPS 0.01.
  - Q3 2023 GPI: GP 1, Other (1), OP 2. Row 663: IBT 2, tax —, NI 2, ETR (0.1)%, EPS —.
  - 9M 2024 GPI: GP 19 (687), SG&A (4) (698), Other (54) (702), OP 77 (710). Row 758: IBT 77, tax 10, NI 67, ETR (0.3)%, EPS 0.08.
  - 9M 2023:
    - ERISA (722; row 772): 267/55/212, ETR (0.9)%, EPS 0.26.
    - Foreign tax (row 773): ETR (4.7)%, EPS 0.15.
    - GPI: GP 1, SG&A (2), Other (22), OP 25, non-service (4) (723). Row 774: IBT 29, tax 5, NCI 1, NI 23, ETR (0.1)%, EPS 0.03.
    - Product recall (703; row 777): 25/6/19, EPS 0.02.
  - Corporate OP notes: Q3 2024/Q3 2023 GPI $15/$2 (456); 9M 2024 GPI $77 (458); 9M 2023 product recall $25 and GPI $25 (460).
- Operative definitions, rules and scope exceptions:
  - Recast (88), verbatim: "(1) The Company has recast its historical geographic segment information to conform to the reporting structure effective as of July 1, 2024. The results of the
    skin health business previously reported within the Europe reportable operating segment are reported with the other skin health businesses in the North America reportable operating
    segment. Recast historical geographic segment information can be found on the Company's website." The short form (first sentence only) is at 116, 452, 506 and 554.
    The recast prior-quarter detail is not printed; the release refers to the website. The release does not say which brands make up "skin health".
  - Base Business (144), organic (146) and FCF (148) definitions. EPS note (283) as D03. Corporate (2) footnote (454) as D02. Emerging Markets (2) (508, 556). Market share (132-134) as D02.
- Amendments or contradictions: the recast changes the North America and Europe comparatives relative to D02/D03 (see Shared ground). Guidance changes against D03.
- Coverage: full. Lines 1-135, 135-364, 365-594 and 595-786 were read.

## Shared ground within D01-D04 (navigation only)

- Entities that appear in more than one document, and where:
  - Colgate-Palmolive Company: D01 9/13/17/117 (unhyphenated at 13 and 17); D02-D04 line 35 "(NYSE:CL)". Noel Wallace: D02/D03/D04 line 35 only. Merrill: D01 only (85, 121).
    Nielsen: D02 117, D03 119, D04 132.
  - Restricted stock units: D01 "PBRSUs" (19). D02 378, D03 443 and D04 454 Corporate footnote ("costs related to stock options and restricted stock units").
    "Stock-based compensation expense": D02 276, D03 341, D04 350.
  - D02 141, D03 145 and D04 154 say non-GAAP measures are used "as factors in determining compensation". D01's Performance Criteria sit in the blank Exhibit A, so no document states a link between D01 and any D02-D04 measure.
  - Hill's (division tables) = Pet Nutrition (segment tables) in D02-D04. "Total CP Products" is undefined in D02 418, D03 485/531 and D04 496/544.
- Periods or series that more than one document covers, and where:
  - D02 covers Q1 2024; D03 Q2 2024 and H1; D04 Q3 2024 and 9M. Each has 2023 comparatives. Cash flow statements are year-to-date only (3/6/9 months); D03 and D04 have no standalone Q2 or Q3 cash flow table.
    No full-year 2024 actuals are in D01-D04. D01's dates (2019, 2013 Plan, March 15, 2022) do not overlap D02-D04.
  - The December 31, 2023 balance sheet column is identical in D02 (225-246, 251), D03 (290-311, 316) and D04 (299-320, 325), checked row by row.
    Beginning cash is 966 (2024) and 775 (2023) in all three.
  - Market share YTD (line 15 in each): toothpaste 41.3% / 41.5% / 41.6%; manual toothbrushes 31.7% / 32.2% / 32.3%.
  - YTD operating cash in the bullets (line 15) matches the tables: $681M (D02 287), $1,671M (D03 352), $2,838M (D04 361).
- Forecast/guidance chain, Full Year 2024 (the "previously" values in each edition match the preceding edition; D02's baseline comes from a release outside D01-D04):

  | Item | D02 Apr 26, 2024 (line) | D03 Jul 26, 2024 (line) | D04 Oct 25, 2024 (line) |
  | --- | --- | --- | --- |
  | Net sales growth | raising to 2% to 5% (vs 1% to 4%) (47) | still expects 2% to 5% (47) | now expects 3% to 5% (vs 2% to 5%) (47) |
  | FX impact on net sales | mid-single-digit negative (vs low-single-digit) (47) | mid-single-digit negative (47) | mid-single-digit negative (47) |
  | Organic sales growth | raising to 5% to 7% (vs 3% to 5%) (49) | raising to 6% to 8% (vs 5% to 7%) (49) | now expects 7% to 8% (vs 6% to 8%) (49) |
  | GAAP | still expects GPM expansion, increased advertising, double-digit EPS growth (51) | same (51) | same (51) |
  | Base Business EPS growth | still expects mid to high-single-digit (53) | increased to 8% to 11% (vs mid to high-single-digit) (53) | now expects 10% to 11% (vs 8% to 11%) (53) |
  | Base Business GPM / advertising | still expects expansion / increased (53) | same (53) | same (53) |

  None of D02-D04 gives tax-rate guidance or numeric gross margin or advertising guidance.
- Definition and boilerplate edition changes:
  - Base Business exclusions: D02 131 has three items. D03 133 adds "a foreign tax matter". D04 144 has the same four with different conjunctions.
  - Measures on both bases: D02 139 has nine items without Gross Profit. D03 141 and D04 152 have eleven, adding Gross Profit and Gross Profit margin. The D02 headline (15) nonetheless states a Base Business gross profit margin.
  - War wording: D02 123 and D03 125 vs D04 138.
  - Cash flow label: "Principal payments on debt" (D02 304, D03 369) vs "of debt" (D04 378).
  - Exhibit number: "Exhibit 99" in D02 and D03 vs "Exhibit 99.1" in D04.
- Changed tables across editions (recast). D02 Table 4 (349-374) and D03 Table 5 (414-439) carry no recast footnote. D04 Table 5 (423-448) recasts North America and Europe.
  The table below compares D03 six-month + D04 Q3 with D04 nine-month [m]:

  | Line | D03 6M + D04 Q3 | D04 9M (line) |
  | --- | --- | --- |
  | 2024 North America net sales | 1,999 + 1,004 = 3,003 | 3,076 (423) |
  | 2024 Europe net sales | 1,432 + 744 = 2,176 | 2,102 (425) |
  | 2024 North America OP | 445 + 206 = 651 | 633 (440) |
  | 2024 Europe OP | 303 + 181 = 484 | 502 (442) |
  | 2023 North America net sales | 1,936 + 1,025 = 2,961 | 3,044 |
  | 2023 Europe net sales | 1,328 + 690 = 2,018 | 1,935 |
  | 2023 North America OP | 420 + 227 = 647 | 640 |
  | 2023 Europe OP | 250 + 165 = 415 | 422 |

  Latin America, Asia Pacific, Africa/Eurasia, Pet Nutrition, Corporate and the Oral, Personal and Home Care totals agree within ±1 [m].
  "% of Total Company Sales" (D02 73 / D03 73 vs D04 77-79): Europe 14% vs 15%, Latin America 25% vs 23%, Africa/Eurasia 5% vs 6%.
- Year-to-date figures vs sums of quarters [m]:
  - D02 Q1 + D03 Q2 vs D03 H1: every 2023 income and segment row sums exactly. 2024 rows that differ by ±1: net sales 10,123 vs 10,124; cost of sales 4,018 vs 4,019; tax 481 vs 482; NI incl. NCI 1,496 vs 1,495; NCI 82 vs 81.
  - D03 H1 + D04 Q3 vs D04 9M: 2023 rows sum exactly. 2024 rows that differ by ±1: net sales, cost of sales, SG&A, OP (3,204 vs 3,205), interest, tax, NI incl. NCI, NI attributable (2,151 vs 2,150).
  - GPI adjustments, 2024: H1 + Q3 vs 9M.
    - Corporate notes 63 + 15 = 78 vs 77 (D04 458).
    - Gross profit 9 + 9 = 18 vs 19 (687).
    - SG&A (3) + (3) = (6) vs (4) (D03 693 + D04 585 vs D04 698).
    - Tax effect 10 + 2 = 12 vs 10 (758); NI 53 + 13 = 66 vs 67.
    - Per-share: Q1 0.03 + Q2 0.02 = 0.05 vs H1 0.07 (D03 764); 0.07 + 0.01 = 0.08 = 9M.
    - The 2023 GPI rows sum exactly.
  - EPS: diluted Q1-Q3 2024 sum to 0.83 + 0.89 + 0.90 = 2.62, vs 9M 2.61 (D04 271). Base Business EPS sum to 0.86 + 0.91 + 0.91 = 2.68, vs 9M 2.69 (759); H1 Base 1.77 vs 1.78 (D03 765). The EPS notes at D03 274 and D04 283 apply.
  - The same $212 ERISA NI effect is printed at 0.25 per share (Q1 2023, D02 521; H1 2023, D03 778) and 0.26 (9M 2023, D04 772). Foreign tax matter is 0.15 in Q2, H1 and 9M 2023 (D03 657, 779; D04 773).
- Prose-only figures and repeated claims:
  - Q2 2023 organic growth 8.2% (D03 37) and Q3 2023 organic growth 8.8% (D04 35). The Q1 2023 organic rate is not stated in D02. The 2023 cells of the headline organic rows are blank (line 29 in each).
  - Consecutive-quarter claims: D02 37 "third consecutive quarter" of double-digit OP/NI/EPS growth; D03 39 "fourth consecutive quarter" of gross margin expansion and double-digit growth; D04 39 "sixth consecutive quarter" of gross margin expansion along with growth (no "double-digit").
  - Volume claims: D03 37 and D04 37. D02 37 says "organic sales growth in every division and across all categories". In D02 Table 5 the organic column is positive in every division row (408-420),
    while volume is negative for Asia Pacific (414) and Hill's (420).
- Other repeated items:
  - Organic Volume equals As Reported Volume in every row of the D02-D04 division and geographic tables.
  - The "About" brand list is identical in D02 115, D03 117 and D04 128.
  - "Emerging Markets" definition: D02 428, D03 495/541, D04 508/556.
- Documents that cite, amend or respond to another document in the bundle: D03 and D04 restate the previous edition's guidance as "previously" (lines 47-53). D04's recast note (88) changes how D02/D03 segment periods are presented. D01 cites no other bundle document.

## Gaps

- Readable text: none unread. All lines of D01 (1-130), D02 (1-538), D03 (1-792) and D04 (1-786) were inspected in the chunks listed under Coverage.
- Missing source material (absent from the source, not an extraction loss):
  - D01: Exhibit A is blank, so the Performance Period and Performance Criteria are absent. The Notice of Grant, the 2013 Incentive Compensation Plan (including Section 11 and the Retirement, Disability, Cause and Change in Control definitions) and the International Appendix are referenced but not included.
  - D04: the recast historical segment figures are on "the Company's website" and not in the bundle.
  - D02: the release that first set D02's "previously" guidance values is not in D01-D04; whether D05-D12 contain it belongs to the other mapper parts.
- Visual: unresolved for all four, because the source HTML is not in the bundle. Split headers and out-of-fence rows were resolved against companion tables; no charts are present.
- Arithmetic: all [m] values are hand-computed. Recompute with a script before any use.
- Next mapping chunk: none for D01-D04. D05-D12 are with the parallel mappers. When merging, compare D06-D08's 2024 comparatives against the D02-D04 values located above.


<!-- merged from map-part2.md: aq-docket-trial-02 - document map, part 2 (D05-D08) -->
Written by a bundle-mapper subagent from `text/D05.txt`-`text/D08.txt` for the caller to merge
into `notes/doc-map.md`. Navigation facts only (locations, wording, tables); no questions,
answers, traps or difficulty claims. Line numbers are `text/Dnn.txt` lines unless marked
"orig". Each text file adds a two-line header ("# Dnn | docs/<file>" plus a blank line), so
original line = text line - 2 (verified by grep for D05-D08, see each Coverage entry).
Money figures in tables are "$ in millions" unless the table says otherwise; per-share amounts
in dollars; percentages as printed. Parentheses in tables = negative / decrease.

## D05 - Colgate Announces 4th Quarter and Full Year 2024 Results

- Source: `docs/cl_ex991_2025-01-31.txt` (manifest sha256 812590d7...0d09c, 36,501 chars,
  method text, pages n/a) | `text/D05.txt` lines 1-862. Exhibit header lines 3-11 ("EX-99",
  "2 a4q2024pressreleasetables.htm", "Exhibit 99").
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL), New York (line 61). Quoted
  speaker: Noel Wallace, "Chairman, President and Chief Executive Officer" (line 61). Mentioned
  third parties only: Nielsen (market-share vendor, line 160), SEC (lines 166-168).
- Type, date, edition: earnings press release (Exhibit 99), title line 13; dateline "New York,
  New York, January 31, 2025" (line 61). Q4/full-year edition for 2024.
- Period covered: three months ended December 31, 2024 vs 2023 ("Fourth Quarter", "4Q 2024");
  twelve months ended December 31, 2024 vs 2023 ("Full Year"); balance sheet as of December 31,
  2024 and December 31, 2023. Year ends December 31 (calendar). Forward guidance labelled
  "Full Year 2025 Guidance" (line 69).
- Entities and aliases: "Colgate-Palmolive Company", "Colgate", "the Company", NYSE:CL (line 61);
  pet business shown as "Hill's" in division tables (lines 106, 134, 534, 582) and as "Pet
  Nutrition" in Table 5 (lines 463, 480); "Oral, Personal and Home Care" (Table 5) vs "Total CP
  Products" (Tables 6-7, lines 532, 580). Brand list in About section (line 154: Colgate,
  Palmolive, elmex, hello, meridol, Sorriso, Tom's of Maine, EltaMD, Filorga, Irish Spring, Lady
  Speed Stick, PCA SKIN, Protex, Sanex, Softsoap, Speed Stick, Ajax, Axion, Fabuloso, Murphy,
  Soupline, Suavitel, Hill's Science Diet, Hill's Prescription Diet). Program name in this
  edition: "2022 Global Productivity Initiative" (lines 174, 490-496, Tables 8-9); misspelled
  once as "2022 Global Productive Initiative" (line 752, also in original orig line 750).
  "Base Business" = non-GAAP basis.
- Headline bullets:
  - Full year (line 17): "Delivered over $20 billion in Net sales for the first time"; "Net sales
    increased 3.3%; Organic sales* increased 7.4%, including a 0.5% negative impact from lower
    private label pet volume"; "GAAP EPS increased 27% to $3.51; Base Business EPS* increased 11%
    to $3.60"; "Net cash provided by operations was $4,107 for the full year, up 10% versus 2023"
    (no unit stated in the bullet); "Returned $3.4 billion in cash to shareholders through
    dividends and share repurchases".
  - Fourth quarter (lines 39-41): "Net sales decreased 0.1%; Organic sales* increased 4.3%,
    including a 0.5% negative impact from lower private label pet volume"; "GAAP EPS increased
    3% to $0.90; Base Business EPS* increased 5% to $0.91"; "GAAP Gross profit margin and Base
    Business Gross profit margin* both increased 70 basis points to 60.3%"; toothpaste global
    market share "41.4% year to date"; manual toothbrushes "32.2% year to date".
- Tables (all $ millions except per share, unaudited):
  - Summary boxes: FY GAAP lines 21-25 (Net Sales $20,101 / $19,457, +3.3 %; EPS diluted
    $3.51 / $2.77, +27 %); FY Base Business lines 27-33 (Organic +7.4 %; Base Business EPS
    $3.60 / $3.23, +11 %); Q4 GAAP lines 45-49 ($4,944 / $4,950, -0.1 %; $0.90 / $0.87, +3 %);
    Q4 Base Business lines 51-57 (Organic +4.3 %; $0.91 / $0.87, +5 %).
  - Q4 Sales Growth by Division, lines 85-111 (% of Total Company Sales, Net Sales, Organic
    Sales, Volume, Pricing, FX): North America 21.0% / -1.0% / -0.7% / +1.9% / -2.7% / -0.3%;
    Latin America 22.4% / -7.2% / +9.2% / +0.9% / +8.3% / -16.4%; Europe 13.5% / +4.9% /
    +4.5% / +1.7% / +2.7% / +0.4%; Asia Pacific 14.6% / +3.7% / +3.8% / +5.8% / -2.0% / —%;
    Africa/Eurasia 5.4% / +2.8% / +9.4% / +11.5% / -2.1% / -6.6%; Hill's 23.1% / +2.3% / +2.9% /
    +0.8% / +2.0% / -0.5%; Total Company 100.0% / -0.1% / +4.3% / +2.5% / +1.8% / -4.4%.
    Layout: rows split across fenced blocks and a tab row (lines 97-109); the Volume and Pricing
    values are separated by a space, not a tab ("+1.9% -2.7%"). Footnote (1) recast, line 113.
  - Q4 Operating Profit by Division, lines 117-140 ($, % change vs 4Q 2023, % to Net Sales, bp
    change): NA $206 / -11% / 19.9% / -220; LA $339 / -8% / 30.6% / -10; Europe $155 / 3% /
    23.3% / -40; Asia Pacific $211 / 4% / 29.1% / +10; Africa/Eurasia $58 / -1% / 21.5% / -80;
    Hill's $275 / 19% / 24.1% / +340; Total As Reported $1,064 / -1% / 21.5% / -20; Total Base
    Business* $1,071 / —% / 21.7% / —.
  - Table 1, Q4 income statement, lines 198-255: Net sales 4,944 / 4,950; Cost of sales 1,962 /
    2,000; Gross profit 2,982 / 2,950; GPM 60.3 % / 59.6 % (line 216); SG&A 1,895 / 1,803; Other
    (income) expense, net 23 / 75; Operating profit 1,064 / 1,072; OPM 21.5 % / 21.7 %; Non-service
    related postretirement costs 20 / 22; Interest expense 66 / 74; Interest income 16 / 12;
    Income before income taxes 994 / 988; Provision 215 / 228; Effective tax rate 21.6 % /
    23.1 % (line 234); NI incl. NCI 779 / 760; NCI 40 / 42; NI attributable 739 / 718; EPS basic
    0.91 / 0.87, diluted 0.90 / 0.87 (lines 245-246); average shares basic 816.0 / 823.4, diluted
    819.7 / 825.1 (millions implied, no unit printed); Advertising $648 / $593 (line 255).
  - Table 2, twelve-month income statement, lines 257-317: Net sales 20,101 / 19,457; Cost of
    sales 7,940 / 8,131; Gross profit 12,161 / 11,326; GPM 60.5 % / 58.2 % (line 275); SG&A 7,729 /
    7,151; Other 164 / 191; Operating profit 4,268 / 3,984; OPM 21.2 % / 20.5 %; Non-service
    postretirement 87 / 360; Interest expense 292 / 287; Interest income 67 / 55; IBT 3,956 /
    3,392; Provision 907 / 937; ETR 22.9 % / 27.6 % (line 293); NI incl. NCI 3,049 / 2,455; NCI
    160 / 155; NI attributable 2,889 / 2,300; EPS basic 3.53 / 2.78, diluted 3.51 / 2.77 (lines
    303-305); shares basic 819.1 / 827.4, diluted 823.2 / 829.2; Advertising $2,720 / $2,371
    (line 313). Note (1) line 317: EPS "computed independently for each quarter and any
    year-to-date period"; quarters "may not equal" the year-to-date figure.
  - Table 3, balance sheet as of Dec 31, 2024 / Dec 31, 2023, lines 319-359: Cash 1,096 / 966;
    Receivables 1,521 / 1,586; Inventories 1,987 / 1,934; Other current assets 713 / 793; PP&E
    4,422 / 4,582; Goodwill 3,272 / 3,410; Other intangibles 1,756 / 1,887; Other assets 1,279 /
    1,235; Total assets 16,046 / 16,393; Total debt 7,949 / 8,549; Other current liabilities
    5,099 / 4,411; Other non-current liabilities 2,454 / 2,476; Total liabilities 15,502 /
    15,436; Colgate shareholders' equity 212 / 609; NCI 332 / 348; Total L&E 16,046 / 16,393.
    Supplemental (lines 353-354): Debt less cash, cash equivalents and marketable securities
    $6,693 / $7,404; Working capital % of sales (5.2)% / (1.4)%. Note (1) line 359: marketable
    securities $160 and $179 included in Other current assets.
  - Table 4, cash flows, twelve months, lines 361-437: Net cash provided by operations 4,107 /
    3,745 (line 395); ERISA litigation matter — / 267 (line 382); Restructuring and termination
    benefits, net of cash 51 / (23); Capital expenditures (561) / (705) (line 401); Dividends paid
    (1,789) / (1,749) (line 414); Purchases of treasury shares (1,739) / (1,128) (line 415);
    Proceeds from exercise of stock options 638 / 380; Proceeds from issuance of debt 2 / 1,495;
    Principal payments on debt (503) / (903); Short-term borrowing (repayment) <90 days 93 /
    (906); Free cash flow before dividends $3,546 / $3,040 (line 432); Income taxes paid $933 /
    $937; Interest paid $302 / $280 (lines 435-436); cash end of period 1,096 / 966.
  - Table 5, segment information, three and twelve months, lines 439-496 (columns Q4 2024, Q4
    2023, FY 2024, FY 2023). Net sales: NA 1,036 / 1,047 / 4,113 / 4,091; LA 1,106 / 1,192 /
    4,782 / 4,640; Europe 668 / 637 / 2,770 / 2,571; Asia Pacific 724 / 698 / 2,858 / 2,782;
    Africa/Eurasia 269 / 262 / 1,095 / 1,083; Total OP&HC 3,804 / 3,836 / 15,618 / 15,167; Pet
    Nutrition 1,140 / 1,114 / 4,483 / 4,290; Total 4,944 / 4,950 / 20,101 / 19,457. Operating
    profit: NA 206 / 231 / 839 / 871; LA 339 / 366 / 1,526 / 1,417; Europe 155 / 151 / 658 / 573;
    AP 211 / 203 / 812 / 767; A/E 58 / 59 / 253 / 254; Total OP&HC 969 / 1,010 / 4,088 / 3,882;
    Pet Nutrition 275 / 231 / 965 / 806; Corporate (179) / (169) / (784) / (704); Total 1,064 /
    1,072 / 4,268 / 3,984. Corporate charge sentences lines 490-496 (see definitions).
  - Table 6, Q4 Geographic Sales Analysis Percentage Changes, lines 498-544 (columns: Sales Change
    As Reported; Organic Sales Change; Volume; Pricing Coupons Consumer & Trade Incentives;
    Foreign Exchange; header split over lines 508-518): Total Company (0.1)% 4.3% 2.5% 1.8%
    (4.4)%; NA (1.0) (0.7) 1.9 (2.7) (0.3); LA (7.2) 9.2 0.9 8.3 (16.4); Europe 4.9 4.5 1.7 2.7
    0.4; AP 3.7 3.8 5.8 (2.0) —; A/E 2.8 9.4 11.5 (2.1) (6.6); Total CP Products (0.8) 4.7 2.9 1.8
    (5.5); Hill's 2.3 2.9 0.8 2.0 (0.5); Emerging Markets (2.2) 7.5 3.7 3.8 (9.7); Developed
    Markets 1.6 1.7 1.5 0.3 (0.2).
  - Table 7, twelve-month Geographic Sales Analysis, lines 546-592: Total Company 3.3% 7.4% 3.1%
    4.4% (4.1)%; NA 0.5 0.7 2.6 (1.9) (0.1); LA 3.1 16.8 3.9 12.9 (13.7); Europe 7.7 6.7 4.1 2.5
    1.1; AP 2.7 4.0 3.1 1.0 (1.3); A/E 1.2 13.3 7.6 5.7 (12.1); Total CP 3.0 8.1 3.7 4.4 (5.2);
    Hill's 4.5 4.9 0.8 4.1 (0.4); EM 3.0 12.2 4.0 8.2 (9.2); DM 3.5 3.6 2.3 1.3 —.
  - Table 8, Q4 Non-GAAP Reconciliations, lines 594-718: Gross profit GAAP 2,982 / 2,950, GPI 1 /
    —, non-GAAP 2,983 / 2,950 (lines 607-609); SG&A non-GAAP 1,894 / 1,803; Other (income)
    expense non-GAAP 18 / 73 (GPI (5) / (2)); Operating profit GAAP 1,064 / 1,072 (1)%, GPI 7 / 2,
    non-GAAP 1,071 / 1,074 —% (lines 621-625); OPM GAAP 21.5 % / 21.7 % (20) bp, non-GAAP 21.7 % /
    21.7 % (lines 629-631); non-service postretirement non-GAAP 20 / 21. Continued (lines
    640-710): 2024 As Reported IBT 994, tax 215, NI incl. NCI 779, NI 739, ETR 21.6 %, EPS 0.90;
    GPI 7 / 1 / 6 / 6 / —% / 0.01; Non-GAAP 1,001 / 216 / 785 / 745 / 21.6 % / 0.91. 2023 As
    Reported 988 / 228 / 760 / 718 / 23.1 % / 0.87; GPI 3 / 1 / 2 / 2 / —% / —; Non-GAAP 991 /
    229 / 762 / 720 / 23.1 % / 0.87. No Q4 gross-profit-margin reconciliation row (margin claim
    only in bullet line 39 and Table 1 line 216).
  - Table 9, twelve-month Non-GAAP Reconciliations, lines 720-861: Gross profit GAAP 12,161 /
    11,326, GPI 20 / 1, non-GAAP 12,181 / 11,327; GPM GAAP 60.5 % / 58.2 % (230 bp), GPI 0.1 %,
    non-GAAP 60.6 % / 58.2 % (240 bp) (line 739, all on one flattened line); SG&A % of sales GAAP
    38.5 % / 36.8 % (170), non-GAAP 38.4 % / 36.7 % (170) (lines 750-754); Other (income) expense
    GAAP 164 / 191, GPI (59) / (24), Product recall costs — / (25), non-GAAP 105 / 142; Operating
    profit GAAP 4,268 / 3,984 (7 %), GPI 85 / 27, recall — / 25, non-GAAP 4,353 / 4,036 (8 %)
    (lines 766-770); OPM GAAP 21.2 % / 20.5 % (70), non-GAAP 21.7 % / 20.7 % (100) (lines
    774-776); Non-service postretirement GAAP 87 / 360, ERISA — / (267), GPI — / (5), non-GAAP
    87 / 88. Continued (lines 786-853): 2024 As Reported IBT 3,956, tax 907, NI incl. NCI 3,049,
    NCI 160, NI 2,889, ETR 22.9 %, EPS 3.51; GPI 85 / 12 / 73 / — / 73 / (0.2)% / 0.09; Non-GAAP
    4,041 / 919 / 3,122 / 160 / 2,962 / 22.7 % / 3.60 (line 822). 2023 As Reported 3,392 / 937 /
    2,455 / 155 / 2,300 / 27.6 % / 2.77; ERISA litigation matter 267 / 55 / 212 / — / 212 /
    (0.5)% / 0.26; Foreign tax matter — / (126) / 126 / — / 126 / (3.4)% / 0.15; GPI 32 / 6 / 26
    / 1 / 25 / (0.1)% / 0.03; Product recall costs 25 / 6 / 19 / — / 19 / —% / 0.02 (line 851,
    outside the fenced block); Non-GAAP 3,716 / 878 / 2,838 / 156 / 2,682 / 23.6 % / 3.23.
- Lists: divisions (six reporting rows: North America, Latin America, Europe, Asia Pacific,
  Africa/Eurasia, Hill's); Base Business exclusion list of four items (line 174, last item
  "product recall costs"); Emerging Markets definition list (line 544/592: Latin America, Asia
  excluding Japan, Africa/Eurasia, Central Europe); Corporate-operations cost list (line 488);
  brand list (line 154, last items Hill's Science Diet and Hill's Prescription Diet);
  forward-looking risk topics (lines 166-168: tariffs, war in Ukraine, conflict in the Middle
  East, tensions between China and Taiwan, among others).
- Forecasts, guidance, deadlines, effective dates:
  - "Full Year 2025 Guidance" (line 69), "Based on current spot rates:" (line 71). First 2025
    outlook in D05; the release does not describe it as raised, lowered or maintained.
    - Net sales (line 73): "The Company expects net sales to be roughly flat, including a
      mid-single-digit negative impact from foreign exchange."
    - Organic sales (line 75): "within its long-term targeted range of 3% to 5%, including the
      impact of the planned exit from private label pet nutrition over the course of 2025."
    - GAAP (line 77): "gross profit margin expansion with advertising investment flat to up
      slightly on both a dollar basis and as a percent to sales and mid-single-digit
      earnings-per-share growth."
    - Base Business (line 79): "gross profit margin expansion with advertising investment flat to
      up slightly on both a dollar basis and as a percent to sales and low to mid-single-digit
      earnings-per-share growth."
    - No tax-rate, restructuring-charge or cash-flow guidance item in D05.
  - CEO: "well positioned to deliver against our guidance in 2025" (line 61); "sixth consecutive
    year with organic sales growth at or above our 3% to 5% targeted range" (line 63).
  - Dated events/effective dates: reporting structure "effective as of July 1, 2024" (lines 113,
    142, 486, 542, 590); annual meeting "currently scheduled for Friday, May 9, 2025" (line 156);
    prepared materials "At approximately 7:00 a.m. ET today", call "At 8:30 a.m. ET today" (lines
    148-150); planned private-label pet nutrition exit "over the course of 2025" (line 75). No
    dividend declaration, acquisition, divestiture closing, impairment or program approval is
    reported in D05.
- Hedged claims: forward-looking statements "may contain" (line 166); market-share vendors'
  data believed "reliable" but not verified (line 162); "Table may not sum due to rounding"
  (lines 111, 484, 540, 588); EPS quarters "may not equal" year-to-date (line 317); non-GAAP
  adjustments "may not necessarily equal the difference" (lines 712, 855). Guidance phrased as
  "expects" with ranges ("roughly flat", "flat to up slightly", "mid-single-digit", "low to
  mid-single-digit") at lines 73-79.
- Rounded prose beside exact figures:
  - "Delivered over $20 billion" / "Reaching $20 billion" (lines 17, 67) vs Net sales $20,101
    (lines 23, 271).
  - "15% increase in advertising spending in 2024, following a 19% increase in 2023" (line 65) vs
    Advertising $2,720 / $2,371 (line 313); the 2022 advertising base is not in D05.
  - "Net cash provided by operations was $4,107 ... up 10% versus 2023" (line 17) vs 4,107 /
    3,745 (line 395).
  - "Returned $3.4 billion in cash to shareholders through dividends and share repurchases"
    (line 17) beside Table 4 rows Dividends paid (1,789) and Purchases of treasury shares (1,739)
    (lines 414-415); the release does not state which rows or netting make up the $3.4 billion.
  - "net income and earnings per share both increasing double digits" (line 63) vs Tables 2 and
    9.
  - Percent changes in summary boxes are whole-number rounded for EPS (+27 %, +11 %, +3 %, +5 %)
    and one decimal for sales.
- Notes: Market Share Information section (lines 158-162): shares are dollar-value shares,
  "excluding Venezuela from all periods", year-to-date from January 1 with "a lag time of one or
  two months". About section: "more than 200 countries and territories"; Bright Smiles, Bright
  Futures "reached approximately 1.8 billion children and their families since 1991" (line
  154). Cautionary statement cites the Form 10-K "for the year ended December 31, 2023" (line
  168).
- Operative definitions, rules and scope exceptions:
  - Base Business (line 174): "Base Business operating results exclude, as applicable, charges
    related to an ERISA litigation matter, a foreign tax matter, the 2022 Global Productivity
    Initiative and product recall costs."
  - Organic sales growth (line 176): "Net sales growth excluding the impact of foreign exchange,
    acquisitions and divestments."
  - Free cash flow before dividends (line 178): "Net cash provided by operations less Capital
    expenditures."
  - Non-GAAP line items disclosed on both bases and general exclusion categories (lines
    182-184: "restructuring charges, charges for certain litigation and tax matters,
    acquisition-related costs, gains and losses from certain divestitures and certain other
    unusual, non-recurring items").
  - Corporate segment scope, footnote (2) line 488; Corporate charges: Q4 2024 GPI $7 (line 490),
    Q4 2023 GPI $2 (line 492), FY 2024 GPI $85 (line 494), FY 2023 GPI $27 and product recall
    costs $25 (line 496).
  - Emerging Markets definition, lines 544 and 592.
  - Tax-effect notes (1)-(2), lines 716-718 and 859-861.
- Amendments or contradictions:
  - Recast: "The Company has recast its historical geographic segment information to conform to
    the reporting structure effective as of July 1, 2024. The results of the skin health business
    previously reported within the Europe reportable operating segment are reported with the
    other skin health businesses in the North America reportable operating segment" (line 113;
    short form lines 142, 486, 542, 590). 2023 comparatives for North America and Europe in
    Tables 5-7 are therefore on the recast basis; recast detail is said to be on the Company's
    website (not in the bundle text of D05).
  - Footnote cross-references: FY non-GAAP note points to "Table 7" and "Table 9" (line 35); Q4
    notes point to "Table 6" and "Table 8" (lines 59, 115, 144); divisional note to "Table 6" and
    "Table 5" (line 83). Table numbering matches the tables as printed.
- Coverage: FULL. Read lines 1-120, 120-249, 249-398, 398-547, 547-706, 706-862 (end of file).
  Spot-checks vs original `docs/cl_ex991_2025-01-31.txt`: Table 1 row "| Net sales | $ 4,944 |
  $ 4,950 |" at orig 210 (text 212); Table 3 footnote "Marketable securities of $160 and $179"
  at orig 357 (text 359); bullet line orig 15 (text 17); last line orig 859 (text 861); page
  count not applicable (text source). No gap markers; no unread range.

## D06 - Colgate Announces 1st Quarter 2025 Results

- Source: `docs/cl_ex991_2025-04-25.txt` (manifest sha256 f3285648...ab34c, 27,290 chars,
  method text, pages n/a) | `text/D06.txt` lines 1-571. Exhibit header lines 3-11 ("2
  q12025pressreleasetables.htm", line 5).
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL), New York (line 35). Quoted
  speaker: Noel Wallace, "Chairman, President and Chief Executive Officer" (line 35). Mentioned
  only: Nielsen (line 126), SEC (line 132).
- Type, date, edition: earnings press release (Exhibit 99), title line 13; dateline "New York,
  New York, April 25, 2025" (line 35). Q1 2025 edition; first update of the 2025 outlook given
  in D05.
- Period covered: three months ended March 31, 2025 vs 2024 ("First Quarter", "1Q 2025"); no
  separate year-to-date table (Q1 only). Balance sheet "As of March 31, 2025, December 31, 2024
  and March 31, 2024" (line 227). Calendar year. Guidance "Full Year 2025" (line 41).
- Entities and aliases: as D05 (Colgate / the Company / NYSE:CL; Hill's = Pet Nutrition row in
  Table 4 lines 365, 382; Total CP Products line 432). Program names present: "2022 Global
  Productivity Initiative" (prior-year column only) and "the ERISA litigation matter" (current
  year). Brand list identical to D05 (line 124).
- Headline bullets (line 15, one flattened line): "Net sales decreased 3.1%; Organic sales*
  increased 1.4%, including a 0.4% negative impact from lower private label pet volume; foreign
  exchange was a 4.4% headwind to net sales"; "GAAP EPS increased 2% to $0.85; Base Business
  EPS* increased 6% to $0.91"; "GAAP Gross profit margin and Base Business Gross profit margin*
  increased 80 basis points to 60.8%"; "Net cash provided by operations was $600 million for the
  first three months of 2025"; toothpaste share "40.9% year to date"; manual toothbrushes "31.9%
  year to date"; "The Company updated its financial guidance for full year 2025".
- Tables (all $ millions except per share, unaudited):
  - Summary boxes lines 17-31: Q1 Net Sales $4,911 / $5,065, -3.1 %; EPS (diluted) $0.85 /
    $0.83, +2 %; Organic +1.4 %; Base Business EPS $0.91 / $0.86, +6 %.
  - Q1 Sales Growth by Division, lines 57-83 ("% change 1Q 2025 vs. 1Q 2024 except % of Total
    Company Sales"; % of sales printed as whole numbers here, one decimal in D05): NA 20% / -3.6% /
    -3.0% / -2.3% / -0.7% / -0.6%; LA 23% / -8.7% / +4.0% / +2.7% / +1.2% / -12.7%; Europe 14% /
    +2.5% / +5.4% / +3.0% / +2.4% / -2.9%; Asia Pacific 14% / -5.0% / -3.1% / -3.4% / +0.4% /
    -1.9%; Africa/Eurasia 6% / -1.5% / +1.8% / -2.3% / +4.1% / -3.4%; Hill's 23% / +1.5% / +2.9% /
    -0.3% / +3.2% / -1.4%; Total 100% / -3.1% / +1.4% / -0.1% / +1.5% / -4.4%. Recast footnote
    line 85.
  - Q1 Operating Profit by Division, lines 89-110: NA $196 / -8% / 19.6% / -100; LA $348 / -14% /
    30.4% / -190; Europe $172 / 12% / 24.9% / +220; Asia Pacific $198 / -4% / 28.7% / +20;
    Africa/Eurasia $57 / -14% / 21.0% / -290; Hill's $258 / 30% / 23.1% / +510; Total As Reported
    $1,076 / 3% / 21.9% / +120; Total Base Business* $1,091 / 1% / 22.2% / +80.
  - Table 1, Q1 income statement, lines 162-219: Net sales 4,911 / 5,065; Cost of sales 1,924 /
    2,026; Gross profit 2,987 / 3,039; GPM 60.8 % / 60.0 % (line 180); SG&A 1,898 / 1,916; Other
    (income) expense 13 / 76; Operating profit 1,076 / 1,047; OPM 21.9 % / 20.7 %; Non-service
    related postretirement costs 72 / 22 (line 192); Interest expense 66 / 73; Interest income
    15 / 15; IBT 953 / 967; Provision 227 / 238; ETR 23.7 % / 24.6 % (line 198); NI incl. NCI 726
    / 729; NCI 36 / 46; NI attributable 690 / 683; EPS basic 0.85 / 0.83, diluted 0.85 / 0.83;
    shares basic 812.0 / 822.8, diluted 815.0 / 825.9; Advertising $668 / $672 (line 219).
  - Table 2, balance sheets (Mar 31, 2025 / Dec 31, 2024 / Mar 31, 2024), lines 221-261: Cash
    1,112 / 1,096 / 1,079; Receivables 1,725 / 1,521 / 1,813; Inventories 2,125 / 1,987 / 1,914;
    Other current assets 852 / 713 / 834; PP&E 4,416 / 4,422 / 4,497; Goodwill 3,334 / 3,272 /
    3,341; Other intangibles 1,782 / 1,756 / 1,837; Other assets 1,301 / 1,279 / 1,256; Total
    assets 16,647 / 16,046 / 16,571; Total debt 8,269 / 7,949 / 8,689; Other current liabilities
    5,163 / 5,099 / 4,776; Other non-current liabilities 2,482 / 2,454 / 2,489; Total liabilities
    15,914 / 15,502 / 15,954; Colgate equity 363 / 212 / 230; NCI 370 / 332 / 387. Debt less cash,
    cash equivalents and marketable securities $6,958 / $6,693 / $7,379; Working capital % of
    sales (3.3)% / (5.2)% / (2.2)% (lines 255-256). Note line 261: marketable securities $199,
    $160, $231 in Other current assets. Dec 31, 2024 column repeats D05 Table 3.
  - Table 3, cash flows, three months, lines 263-339: ERISA litigation matter 65 / — (line 284);
    Restructuring and termination benefits, net of cash (7) / 30; Net cash provided by (used in)
    operations 600 / 681 (line 297); Capital expenditures (124) / (126); Dividends paid (406) /
    (394) (line 316); Purchases of treasury shares (284) / (509) (line 317); Proceeds from
    exercise of stock options 40 / 336; Short-term borrowing 164 / 728; Principal payments on debt
    (4) / (500); Free cash flow before dividends $476 / $555 (line 334); Income taxes paid $139 /
    $150; Interest paid $109 / $123; cash end 1,112 / 1,079.
  - Table 4, segment information, three months only, lines 341-396. Net sales: NA 998 / 1,035;
    LA 1,143 / 1,253; Europe 690 / 673; Asia Pacific 690 / 727; Africa/Eurasia 271 / 276; Total
    OP&HC 3,792 / 3,963; Pet Nutrition 1,118 / 1,102; Total 4,911 / 5,065. Operating profit: NA
    196 / 214; LA 348 / 405; Europe 172 / 153; AP 198 / 207; A/E 57 / 66; Total OP&HC 971 /
    1,044; Pet Nutrition 258 / 199; Corporate (153) / (196); Total 1,076 / 1,047.
  - Table 5, Q1 Geographic Sales Analysis, lines 398-446 (same five columns as D05 Table 6):
    Total (3.1)% 1.4% (0.1)% 1.5% (4.4)%; NA (3.6) (3.0) (2.3) (0.7) (0.6); LA (8.7) 4.0 2.7 1.2
    (12.7); Europe 2.5 5.4 3.0 2.4 (2.9); AP (5.0) (3.1) (3.4) 0.4 (1.9); A/E (1.5) 1.8 (2.3) 4.1
    (3.4); Total CP Products (4.3) 1.0 — 1.0 (5.3); Hill's 1.5 2.9 (0.3) 3.2 (1.4); Emerging
    Markets (6.2) 1.7 0.2 1.4 (7.9); Developed Markets (0.4) 1.1 (0.4) 1.5 (1.5).
  - Table 6, Q1 Non-GAAP Reconciliations, lines 448-570. No gross-profit reconciliation rows
    (first block is SG&A). SG&A GAAP 1,898 / 1,916, ERISA litigation matter (15) / —, GPI — / (1),
    non-GAAP 1,883 / 1,915 (lines 461-464); SG&A % of sales GAAP 38.6 % / 37.8 % (80 bp), ERISA
    (0.3)%, non-GAAP 38.3 % / 37.8 % (50 bp) (lines 468-470); Other (income) expense GAAP 13 / 76,
    GPI — / (35), non-GAAP 13 / 41; Operating profit GAAP 1,076 / 1,047 (3 %), ERISA 15 / —, GPI
    — / 36, non-GAAP 1,091 / 1,083 (1 %) (lines 481-485); OPM GAAP 21.9 % / 20.7 % (120), ERISA
    0.3 %, GPI 0.7 % (2024), non-GAAP 22.2 % / 21.4 % (80) (lines 489-491); Non-service related
    postretirement costs GAAP 72 / 22, ERISA (50) / —, non-GAAP 22 / 22 (lines 496-498).
    Continued: 2025 As Reported IBT 953, tax 227, NI incl. NCI 726, NCI 36, NI 690, ETR 23.7 %,
    EPS 0.85; ERISA litigation matter 65 / 12 / 53 / — / 53 / (0.3)% / 0.06 (line 532); Non-GAAP
    1,018 / 239 / 779 / 36 / 743 / 23.4 % / 0.91 (line 535). 2024 As Reported 967 / 238 / 729 /
    46 / 683 / 24.6 % / 0.83; GPI 36 / 6 / 30 / — / 30 / (0.3)% / 0.03; Non-GAAP 1,003 / 244 /
    759 / 46 / 713 / 24.3 % / 0.86 (lines 557-561).
- Lists: same six division rows; Base Business exclusion list now two items (line 138); risk
  topics list (line 132) adds "the impact of tariffs" and "global trade relations"; Emerging
  Markets definition (line 446); Corporate cost list (line 392).
- Forecasts, guidance, deadlines, effective dates:
  - "Full Year 2025 Guidance" (line 41): "Based on current spot rates and including the estimated
    impact of tariffs announced and in effect as of April 24, 2025:" (line 43). Described as
    "The Company updated its financial guidance for full year 2025" (line 15) and, by the CEO,
    "achieve our revised 2025 financial targets" (line 39). The words "raised"/"lowered" are not
    used. Each item uses "now expects":
    - Net sales (line 45): "The Company now expects net sales to be up low single digits,
      including a low-single-digit negative impact from foreign exchange."
    - Organic (line 47): "The Company now expects organic sales growth to be 2% to 4%."
    - GAAP (line 49): "the Company now expects both gross profit margin and advertising
      investment to be roughly flat as a percentage of net sales, and earnings per share to be up
      low single digits."
    - Base Business (line 51): "the Company now expects both gross profit margin and
      advertising to be roughly flat as a percentage of net sales, and earnings per share to be up
      low single digits."
    - No tax-rate or restructuring guidance item.
  - Dated items: tariff cut-off "as of April 24, 2025" (line 43); reporting structure "effective
    as of July 1, 2024" (lines 85, 112, 390, 444); prepared materials ~7:00 a.m. ET and call 8:30
    a.m. ET "today" (lines 118-120). No annual-meeting sentence, dividend declaration,
    acquisition, divestiture, impairment or program approval in D06.
- Hedged claims: CEO "uncertainty and volatility in global markets, including the impact of
  tariffs, remain challenging" (line 39); guidance includes only the "estimated impact of tariffs
  announced and in effect as of April 24, 2025" (line 43); rounding caveats lines 83, 386, 440,
  564; forward-looking caveats line 132.
- Rounded prose beside exact figures:
  - "Net cash provided by operations was $600 million" (line 15) = 600 (line 297).
  - CEO "a 30 basis point increase in advertising to 13.6% to sales" (line 37); no advertising
    ratio row is printed; Table 1 gives Advertising $668 / $672 and Net sales 4,911 / 5,065 (lines
    176, 219) (advertising dollars lower year over year while the ratio is stated as higher).
  - "foreign exchange was a 4.4% headwind" (line 15) = Table 5 Total Company FX (4.4)% (line
    420).
  - Summary EPS changes rounded to whole percent (+2 %, +6 %), lines 22, 31.
- Notes: the Non-GAAP list of measures disclosed on both bases (lines 146-148) begins with
  "Selling, general and administrative expenses" and omits the "Gross profit, Gross profit margin"
  items that open the D05 list (D05 line 182), while the bullet (line 15) still cites a Base
  Business gross profit margin. Cautionary statement cites the Form 10-K "for the year ended
  December 31, 2024" (line 132). About section and "CL-E Market Share Information" are joined on
  line 124 (layout only).
- Operative definitions, rules and scope exceptions:
  - Base Business (line 138): "Base Business operating results exclude, as applicable, charges
    related to the ERISA litigation matter and the 2022 Global Productivity Initiative."
  - Organic sales growth (line 140) and Free cash flow before dividends (line 142): wording as D05.
  - Corporate charges (lines 394-396): "Corporate Operating profit (loss) for the three months
    ended March 31, 2025 included charges related to the ERISA litigation matter of $15";
    "... for the three months ended March 31, 2024 included charges resulting from the 2022
    Global Productivity Initiative of $36."
  - ERISA litigation matter, Q1 2025: $65 pre-tax in total (cash-flow add-back line 284;
    reconciliation line 532), split $15 in SG&A / operating profit (lines 462, 483) and $50 in
    non-service related postretirement costs (line 497); tax effect 12; net income effect 53;
    EPS $0.06.
- Amendments or contradictions:
  - Guidance revision vs D05 (D05 lines 73-79 vs D06 lines 45-51): net sales "roughly flat" with
    "mid-single-digit negative" FX -> "up low single digits" with "low-single-digit negative" FX;
    organic "3% to 5%" -> "2% to 4%"; GAAP "gross profit margin expansion", advertising "flat to up
    slightly on both a dollar basis and as a percent to sales", "mid-single-digit" EPS growth ->
    gross margin and advertising "roughly flat as a percentage of net sales", EPS "up low single
    digits"; Base Business "low to mid-single-digit" EPS growth -> "up low single digits". D06
    labels this "updated" / "revised"; precedence by date only (D06 later).
  - Base Business exclusion list changed: D05 line 174 (four items incl. "a foreign tax matter"
    and "product recall costs", "an ERISA litigation matter") -> D06 line 138 (two items, "the
    ERISA litigation matter" and the 2022 GPI).
  - Prior-period comparatives to check against D02 (Q1 2024 release, other part): Q1 2024 Net
    sales 5,065, GAAP EPS 0.83, Base Business EPS 0.86, OP 1,047, GPI 36, ETR 24.6 % / non-GAAP
    24.3 %; NA (1,035 / OP 214) and Europe (673 / OP 153) are on the July 1, 2024 recast basis
    (footnote lines 85, 390, 444), so they may differ from the as-first-reported D02 figures.
- Coverage: FULL. Read lines 1-130, 130-279, 279-438, 438-571 (end of file). Spot-checks vs
  original `docs/cl_ex991_2025-04-25.txt`: Table 1 row "| Net sales | $ 4,911 | $ 5,065 |" orig
  174 (text 176); Table 2 note "Marketable securities of $199, $160 and $231" orig 259 (text
  261); guidance basis sentence orig 41 (text 43); last line orig 568 (text 570). Page count not
  applicable. No gap markers; no unread range.

## D07 - Colgate-Palmolive Company Announces 2nd Quarter 2025 Results

- Source: `docs/cl_ex991_2025-08-01.txt` (manifest sha256 af084d95...946d8, 36,457 chars,
  method text, pages n/a) | `text/D07.txt` lines 1-852. Exhibit header lines 3-11 ("2
  q22025pressreleasetables.htm", line 5).
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL), New York (line 35). Quoted
  speaker: Noel Wallace, "Chairman, President and Chief Executive Officer" (line 35). Mentioned
  only: Nielsen (line 140), SEC (line 146); acquired business "Prime100 pet food business" (lines
  92, 521, 573).
- Type, date, edition: earnings press release (Exhibit 99); title line 13 uses "Colgate-Palmolive
  Company Announces" (D05/D06 titles say "Colgate Announces"); dateline "New York, New York,
  August 1, 2025" (line 35). Q2 2025 edition.
- Period covered: three months ended June 30, 2025 vs 2024 ("Second Quarter", "2Q 2025") and
  six months ended June 30, 2025 vs 2024 (Tables 2, 4, 5, 7, 9). Balance sheet "As of June 30,
  2025, December 31, 2024 and June 30, 2024" (line 301). Cash-flow statement is six months only
  (no three-month cash-flow table). Calendar year. Guidance "Full Year 2025" (line 43).
- Entities and aliases: "the Company" replaces "Colgate" in the share bullets ("The Company's
  leadership in toothpaste", line 15) and prepared-materials lines 130-132 ("Colgate-Palmolive's
  website"); "Hill's Pet Nutrition" (lines 92, 521, 573) = "Hill's" rows = "Pet Nutrition" (Table
  5 lines 440, 457). Programs/items present: "2022 Global Productivity Initiative" (2024
  columns), "ERISA litigation matter" (2025 six-month columns), "Acquisition-related costs" (2025
  columns), and an unnamed "new three-year productivity program" (line 41; "the productivity
  program announced on August 1, 2025", line 146).
- Headline bullets (line 15): "Net sales increased 1.0%; Organic sales* increased 1.8%, including
  a 0.6% negative impact from lower private label pet sales"; "GAAP EPS increased 2% to $0.91;
  Base Business EPS* increased 1% to $0.92"; "GAAP Gross profit margin decreased 50 basis points
  to 60.1%; Base Business Gross profit margin* decreased 70 basis points to 60.1%"; "Net cash
  provided by operations was $1,484 million for the first six months of 2025"; toothpaste share
  "41.1% year to date"; manual toothbrushes "32.4% year to date"; "The Company updated its organic
  sales growth guidance for full year 2025".
- Tables (all $ millions except per share, unaudited):
  - Summary boxes lines 17-31: Q2 Net Sales $5,110 / $5,058, +1.0 %; EPS (diluted) $0.91 /
    $0.89, +2 %; Organic +1.8 %; Base Business EPS $0.92 / $0.91, +1 %.
  - Q2 Sales Growth by Division, lines 59-92; columns now "% of Total Company Sales", Net Sales,
    Organic Sales*, "As Reported Volume**", "Organic Volume", Pricing, FX (lines 63-69): NA 20% /
    -1.0% / -0.9% / -0.4% / -0.4% / -0.5% / -0.1%; LA 24% / -4.8% / +3.4% / +0.4% / +0.4% /
    +3.0% / -8.2%; Europe 14% / +7.8% / +2.0% / -0.2% / -0.2% / +2.2% / +5.7%; Asia Pacific 13% /
    +0.8% / —% / -1.6% / -1.6% / +1.6% / +0.9%; Africa/Eurasia 6% / +8.0% / +7.7% / +4.3% / +4.3%
    / +3.4% / +0.2%; Hill's 23% / +3.8% / +2.0% / +0.1% / -0.9% / +2.9% / +0.8% (line 82, outside
    fenced block); Total 100% / +1.0% / +1.8% / —% / -0.2% / +2.0% / -1.0% (line 84). Footnote **
    (line 92): "The impact of the acquisition of the Prime100 pet food business on as reported
    volume was 1.0% and 0.2% for Hill's Pet Nutrition and Total Company, respectively."
  - Q2 Operating Profit by Division, lines 94-122: NA $194 / -9% / 18.9% / -170; LA $367 / -12% /
    30.4% / -250; Europe $184 / 9% / 25.0% / +40; Asia Pacific $187 / -4% / 27.2% / -150;
    Africa/Eurasia $65 / 1% / 22.0% / -140; Hill's $264 / 13% / 22.9% / +180 (line 117); Total As
    Reported $1,080 / -1% / 21.1% / -50; Total Base Business* $1,089 / -3% / 21.3% / -80.
  - Table 1, Q2 income statement, lines 174-231: Net sales 5,110 / 5,058; Cost of sales 2,041 /
    1,992; Gross profit 3,069 / 3,066; GPM 60.1 % / 60.6 % (line 192); SG&A 1,963 / 1,939; Other
    (income) expense 26 / 35; Operating profit 1,080 / 1,092; OPM 21.1 % / 21.6 %; Non-service
    postretirement 23 / 22; Interest expense 71 / 78; Interest income 21 / 18; IBT 1,007 / 1,010;
    Provision 234 / 243; ETR 23.2 % / 24.1 % (line 210); NI incl. NCI 773 / 767; NCI 30 / 36; NI
    attributable 743 / 731; EPS basic 0.92 / 0.89, diluted 0.91 / 0.89; shares basic 810.2 /
    819.7, diluted 813.3 / 823.7; Advertising $678 / $706 (line 231).
  - Table 2, six-month income statement, lines 233-293: Net sales 10,021 / 10,124 (line 247);
    Cost of sales 3,965 / 4,019; Gross profit 6,056 / 6,105; GPM 60.4 % / 60.3 % (line 251); SG&A
    3,861 / 3,855; Other 39 / 111; Operating profit 2,156 / 2,139; OPM 21.5 % / 21.1 %;
    Non-service postretirement 95 / 44; Interest expense 137 / 151; Interest income 35 / 33; IBT
    1,959 / 1,977; Provision 460 / 482; ETR 23.5 % / 24.4 % (line 269); NI incl. NCI 1,499 /
    1,495; NCI 66 / 81; NI attributable 1,433 / 1,414; EPS basic 1.77 / 1.72, diluted 1.76 / 1.71
    (lines 279-281); shares basic 811.2 / 821.3, diluted 814.2 / 824.9; Advertising $1,346 /
    $1,378 (line 289). Note (1) line 293 (quarterly EPS computed independently).
  - Table 3, balance sheets (Jun 30, 2025 / Dec 31, 2024 / Jun 30, 2024), lines 295-335: Cash
    1,215 / 1,096 / 1,110; Receivables 1,773 / 1,521 / 1,825; Inventories 2,120 / 1,987 / 1,922;
    Other current assets 888 / 713 / 789; PP&E 4,529 / 4,422 / 4,392; Goodwill 3,696 / 3,272 /
    3,320 (line 314); Other intangibles 1,904 / 1,756 / 1,814 (line 315); Other assets 1,345 /
    1,279 / 1,308; Total assets 17,470 / 16,046 / 16,480; Total debt 8,758 / 7,949 / 8,676;
    Other current liabilities 5,161 / 5,099 / 4,820; Other non-current liabilities 2,499 / 2,454
    / 2,502; Total liabilities 16,418 / 15,502 / 15,998; Colgate equity 702 / 212 / 123; NCI 350
    / 332 / 359. Debt less cash, cash equivalents and marketable securities $7,346 / $6,693 /
    $7,341; Working capital % of sales (2.9)% / (5.2)% / (2.5)% (lines 329-330). Note line 335:
    marketable securities $197 / $160 / $225.
  - Table 4, cash flows, six months, lines 337-414: ERISA litigation matter 65 / — (line 358);
    Restructuring and termination benefits, net of cash (13) / 48; Net cash provided by (used in)
    operations 1,484 / 1,671 (line 371); Capital expenditures (232) / (243); "Payment for
    acquisition, net of cash acquired" (293) / — (line 380); Purchases of marketable securities
    (384) / (243); Proceeds 350 / 178; Short-term borrowing (30) / 736; Principal payments on
    debt (139) / (500); Proceeds from issuance of debt 497 / 2; Dividends paid (880) / (867) (line
    391); Purchases of treasury shares (516) / (989) (line 392); Proceeds from exercise of stock
    options 65 / 455; Other financing 136 / (43); Free cash flow before dividends $1,252 / $1,428
    (line 409); Income taxes paid $530 / $505; Interest paid $137 / $161; cash end 1,215 / 1,110.
  - Table 5, segment information, three and six months, lines 416-473 (columns Q2 2025, Q2 2024,
    6M 2025, 6M 2024). Net sales: NA 1,027 / 1,037 / 2,025 / 2,073; LA 1,207 / 1,267 / 2,350 /
    2,520; Europe 738 / 685 / 1,427 / 1,358; Asia Pacific 687 / 682 / 1,378 / 1,408;
    Africa/Eurasia 295 / 273 / 566 / 549; Total OP&HC 3,954 / 3,944 / 7,746 / 7,908; Pet Nutrition
    1,157 / 1,114 / 2,275 / 2,216; Total 5,110 / 5,058 / 10,021 / 10,124. Operating profit: NA 194
    / 213 / 390 / 427; LA 367 / 417 / 715 / 822; Europe 184 / 169 / 356 / 321; AP 187 / 195 / 385
    / 402; A/E 65 / 64 / 122 / 130; Total OP&HC 997 / 1,058 / 1,968 / 2,102; Pet Nutrition 264 /
    235 / 523 / 433; Corporate (181) / (201) / (334) / (397); Total 1,080 / 1,092 / 2,156 / 2,139.
  - Table 6, Q2 Geographic Sales Analysis, lines 475-525; columns Sales Change As Reported,
    Organic Sales Change, "As Reported Volume(1)", "Organic Volume", Pricing Coupons Consumer &
    Trade Incentives, Foreign Exchange (header lines 485-497): Total 1.0% 1.8% — (0.2) 2.0
    (1.0); NA (1.0) (0.9) (0.4) (0.4) (0.5) (0.1); LA (4.8) 3.4 0.4 0.4 3.0 (8.2); Europe 7.8 2.0
    (0.2) (0.2) 2.2 5.7; AP 0.8 — (1.6) (1.6) 1.6 0.9; A/E 8.0 7.7 4.3 4.3 3.4 0.2; Total CP
    Products 0.2 1.7 — — 1.7 (1.5); Hill's 3.8 2.0 0.1 (0.9) 2.9 0.8; Emerging Markets (1.1) 2.8
    0.2 0.2 2.6 (3.9); Developed Markets 2.8 0.9 (0.1) (0.5) 1.4 1.4. Footnote (1) line 521:
    Prime100 impact on as reported volume "0.2%, 1.0% and 0.4% for Total Company, Hill's Pet
    Nutrition and Developed Markets, respectively".
  - Table 7, six-month Geographic Sales Analysis, lines 527-577: Total (1.0)% 1.6% — (0.1) 1.7
    (2.7); NA (2.3) (2.0) (1.4) (1.4) (0.6) (0.3); LA (6.8) 3.7 1.6 1.6 2.1 (10.4); Europe 5.2
    3.7 1.4 1.4 2.3 1.5; AP (2.2) (1.6) (2.6) (2.6) 1.0 (0.6); A/E 3.2 4.8 1.0 1.0 3.7 (1.6);
    Total CP (2.0) 1.3 — — 1.3 (3.4); Hill's 2.6 2.5 (0.1) (0.6) 3.0 (0.3); EM (3.7) 2.2 0.2 0.2
    2.0 (5.9); DM 1.2 1.0 (0.2) (0.4) 1.5 —. Footnote (1) line 573: Prime100 six-month impact
    "0.1%, 0.5% and 0.2% for Total Company, Hill's Pet Nutrition and Developed Markets".
  - Table 8, Q2 Non-GAAP Reconciliations, lines 579-699: Gross profit GAAP 3,069 / 3,066, GPI — /
    9, non-GAAP 3,069 / 3,075 (lines 592-594); GPM GAAP 60.1 % / 60.6 % (50), GPI 0.2 % (2024),
    non-GAAP 60.1 % / 60.8 % (70) (lines 598-602); SG&A non-GAAP 1,963 / 1,937 (GPI (2) in 2024);
    Other (income) expense GAAP 26 / 35, Acquisition-related costs (9) / —, GPI — / (16),
    non-GAAP 17 / 20 (lines 611-614); Operating profit GAAP 1,080 / 1,092 ((1) %), Acquisition-
    related costs 9 / —, GPI — / 27, non-GAAP 1,089 / 1,118 ((3) %) (lines 618-622); OPM GAAP 21.1
    % / 21.6 % (50), acquisition 0.2 %, GPI 0.5 % (2024), non-GAAP 21.3 % / 22.1 % (80) (line
    626, flattened). No non-service postretirement block in Table 8. Continued: 2025 As Reported
    IBT 1,007, tax 234, NI incl. NCI 773, NCI 30, NI 743, ETR 23.2 %, EPS 0.91; Acquisition-related
    costs 9 / 2 / 7 / — / 7 / —% / 0.01 (line 664); Non-GAAP 1,016 / 236 / 780 / 30 / 750 / 23.2 %
    / 0.92 (line 666). 2024 As Reported 1,010 / 243 / 767 / 36 / 731 / 24.1 % / 0.89; GPI 27 / 4
    / 23 / — / 23 / (0.3)% / 0.02; Non-GAAP 1,036 / 247 / 789 / 36 / 753 / 23.8 % / 0.91 (lines
    688-692).
  - Table 9, six-month Non-GAAP Reconciliations, lines 701-851: Gross profit GAAP 6,056 / 6,105,
    GPI — / 9, non-GAAP 6,056 / 6,114; GPM GAAP 60.4 % / 60.3 % (10), GPI 0.1 % (2024), non-GAAP
    60.4 % / 60.4 % (—) (lines 718-722); SG&A GAAP 3,861 / 3,855, ERISA (15) / —, GPI — / (3),
    non-GAAP 3,845 / 3,852; SG&A % GAAP 38.5 % / 38.1 % (40), ERISA (0.1)%, GPI (0.1)% (2024),
    non-GAAP 38.4 % / 38.0 % (40) (lines 734-740); Other (income) expense GAAP 39 / 111,
    acquisition (9) / —, GPI — / (51), non-GAAP 30 / 60; Operating profit GAAP 2,156 / 2,139 (1
    %), ERISA 15 / —, acquisition 9 / —, GPI — / 63, non-GAAP 2,181 / 2,202 ((1) %) (lines
    752-760); OPM GAAP 21.5 % / 21.1 % (40), ERISA 0.2 %, acquisition 0.1 %, GPI 0.7 % (2024),
    non-GAAP 21.8 % / 21.8 % (—) (lines 764-768); Non-service postretirement GAAP 95 / 44, ERISA
    (50) / —, non-GAAP 45 / 44 (lines 773-775). Continued: 2025 As Reported 1,959 / 460 / 1,499 /
    66 / 1,433 / 23.5 % / 1.76; ERISA 65 / 12 / 53 / — / 53 / (0.1)% / 0.06 (line 813);
    Acquisition-related costs 9 / 2 / 7 / — / 7 / —% / 0.01 (line 816); Non-GAAP 2,034 / 475 /
    1,559 / 66 / 1,493 / 23.4 % / 1.83 (line 818). 2024 As Reported 1,977 / 482 / 1,495 / 81 /
    1,414 / 24.4 % / 1.71; GPI 63 / 10 / 53 / — / 53 / (0.3)% / 0.07; Non-GAAP 2,040 / 492 / 1,548
    / 81 / 1,467 / 24.1 % / 1.78 (lines 841-845).
- Lists: six division rows; Base Business exclusion list three items (line 152, last item
  "acquisition-related costs"); productivity-program initiative list of three (line 41: align
  organizational structure; optimize global supply chain; simplify and streamline organizational
  structure to reduce overhead costs); Prime100 footnotes list two entities (line 92) or three
  (lines 521, 573, last item "Developed Markets"); Corporate charge sentences four (lines
  467-473); risk topics (line 146) add "cost reduction plans (including the productivity program
  announced on August 1, 2025)".
- Forecasts, guidance, deadlines, effective dates:
  - "Full Year 2025 Guidance" (line 43): "Based on current spot rates and including the estimated
    impact of tariffs announced and finalized as of July 31, 2025:" (line 45). Bullet (line 15):
    "The Company updated its organic sales growth guidance for full year 2025".
    - Net sales (line 47): "The Company still expects net sales to be up low single digits, now
      including a flat to low-single-digit negative impact from foreign exchange."
    - Organic (line 49): "The Company now expects organic sales growth to be at the low end of 2%
      to 4%, including the impact over the course of 2025 of the planned exit from private label
      pet sales."
    - GAAP (line 51): "the Company still expects both gross profit margin and advertising
      investment to be roughly flat as a percentage of net sales, and earnings per share to be up
      low single digits."
    - Base Business (line 53): "the Company still expects both gross profit margin and
      advertising to be roughly flat as a percentage of net sales, and earnings per share to be up
      low single digits."
    - No tax-rate guidance; program charges are given separately (below), not as a guidance item.
  - New productivity program (line 41): "Separately, the Company today announced a new three-year
    productivity program to drive future growth and support the Company's 2030 strategy ... The
    productivity program is projected to result in cumulative pre-tax charges, once all
    initiatives are approved and implemented, totaling between $200 and $300 million over the
    course of the three-year program. It is expected that substantially all charges resulting
    from the productivity program will be incurred by December 31, 2028." Cross-reference "the
    productivity program announced on August 1, 2025" (line 146). D07 gives the program no proper
    name and does not add it to the Base Business definition (line 152).
  - CEO: "achieve our 2025 financial targets" (line 39); "organic sales growth improving
    sequentially versus the first quarter despite an even greater negative impact from lower
    private label pet sales" (line 37).
  - Dated items: tariffs "as of July 31, 2025" (line 45); program announcement "today" / "August 1,
    2025" (lines 41, 146); charges "by December 31, 2028" (line 41); reporting structure
    "effective as of July 1, 2024" (lines 88, 124, 463, 523, 575); call/materials "today" (lines
    130-132). The Prime100 acquisition date and price are not stated in D07 (only the volume
    footnotes, $9 acquisition-related costs and the (293) cash payment line). No annual-meeting,
    dividend-declaration, divestiture or impairment item.
- Hedged claims: program charges "projected" and conditional "once all initiatives are approved
  and implemented"; "It is expected that substantially all charges" (line 41); CEO "We feel we
  are well positioned" (line 39); guidance includes only the "estimated impact of tariffs
  announced and finalized as of July 31, 2025" (line 45); rounding caveats lines 86, 461, 519,
  571, 628, 695, 777, 847.
- Rounded prose beside exact figures:
  - "$1,484 million for the first six months" (line 15) = 1,484 (line 371).
  - GAAP GPM "decreased 50 basis points to 60.1%" (line 15) vs 60.1 % / 60.6 % (line 192); Base
    Business GPM "decreased 70 basis points to 60.1%" vs 60.1 % / 60.8 % (line 602).
  - Private-label pet drag "0.6%" (line 15) vs D06 "0.4%" (D06 line 15), described by the CEO as
    "an even greater negative impact" (line 37).
- Notes: quarter-sum relationships (arithmetic on printed figures, for navigation): six-month
  2025 net sales 10,021 = D06 Q1 4,911 + Q2 5,110; six-month 2024 net sales 10,124 (line 247)
  vs D06 Q1 2024 5,065 + D07 Q2 2024 5,058 = 10,123; six-month 2024 diluted EPS 1.71 (line 281)
  vs 0.83 + 0.89 = 1.72; six-month 2024 Base Business EPS 1.78 (line 845) vs 0.86 + 0.91 = 1.77;
  six-month 2025 diluted EPS 1.76 = 0.85 + 0.91; six-month Advertising 1,346 = 668 + 678, 2024
  1,378 = 672 + 706. The releases' own caveats: EPS computed independently (line 293), "Tables
  may not sum due to rounding". Six-month 2024 GPI 63 (line 473) = Q1 36 (D06 line 396) + Q2 27
  (line 471). Cautionary statement cites the Form 10-K "for the year ended December 31, 2024"
  (line 146).
- Operative definitions, rules and scope exceptions:
  - Base Business (line 152): "Base Business operating results exclude, as applicable, charges
    resulting from the ERISA litigation matter and the 2022 Global Productivity Initiative and
    acquisition-related costs."
  - Organic sales growth (line 154): "Net sales growth excluding the impact of foreign exchange,
    acquisitions and divestments." Prime100 volume impact shown separately as "As Reported
    Volume" vs "Organic Volume" (lines 63-69, 493-497, 545-549).
  - Free cash flow before dividends (line 156); both-bases measure list again opens with "Gross
    profit, Gross profit margin" (line 160).
  - Corporate charges (lines 467-473): "three months ended June 30, 2025 included
    acquisition-related costs of $9"; "six months ended June 30, 2025 included charges resulting
    from the ERISA litigation matter of $15 and acquisition-related costs of $9"; "three months
    ended June 30, 2024 included charges resulting from the 2022 Global Productivity Initiative of
    $27"; "six months ended June 30, 2024 ... of $63."
- Amendments or contradictions:
  - Guidance vs D06 (D06 lines 45-51 vs D07 lines 47-53): net sales "up low single digits"
    unchanged ("still expects") but FX wording "low-single-digit negative" -> "flat to
    low-single-digit negative"; organic "2% to 4%" -> "at the low end of 2% to 4%" ("now
    expects"); GAAP and Base Business items unchanged ("still expects"). Tariff basis "announced
    and in effect as of April 24, 2025" -> "announced and finalized as of July 31, 2025". Exit
    wording "private label pet nutrition" (D05 line 75) -> "private label pet sales" (line 49).
  - Base Business definition expanded vs D06 line 138: adds "acquisition-related costs" (line
    152); wording "charges resulting from" replaces "charges related to".
  - Prior-period comparatives to check against D03 (Q2 2024 release, other part): Q2 2024 Net
    sales 5,058; GAAP EPS 0.89; Base Business EPS 0.91; Operating profit 1,092; Base Business
    OP 1,118; GPM 60.6 % / non-GAAP 60.8 %; GPI 27; six-month 2024 Net sales 10,124, EPS 1.71,
    Base Business EPS 1.78, OP 2,139 / non-GAAP 2,202, GPI 63. NA and Europe 2024 columns are on
    the July 1, 2024 recast basis (footnotes lines 88, 463, 523, 575).
- Coverage: FULL. Read lines 1-110, 110-239, 239-398, 398-567, 567-736, 736-852 (end of file);
  keyword sweep for acquisition/divestiture/dividend/impairment/approval/board/effective wording
  (all hits located above). Spot-checks vs original `docs/cl_ex991_2025-08-01.txt`: Table 1 row
  "| Net sales | $ 5,110 | $ 5,058 |" orig 186 (text 188); Table 3 note "Marketable securities of
  $197, $160 and $225" orig 333 (text 335); Prime100 footnotes orig 90/519/571 (text 92/521/573);
  last line orig 849 (text 851). Page count not applicable. No gap markers; no unread range.

## D08 - Colgate-Palmolive Company Announces 3rd Quarter 2025 Results

- Source: `docs/cl_ex991_2025-10-31.txt` (manifest sha256 3dbeddbe...6637c, 34,918 chars,
  method text, pages n/a) | `text/D08.txt` lines 1-786. Exhibit header lines 3-11 ("2
  q32025pressreleasetables.htm", line 5).
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL), New York (line 35). Quoted
  speaker: Noel Wallace, "Chairman, President and Chief Executive Officer" (line 35). Mentioned
  only: Nielsen (line 123), SEC (line 129); Prime100 (lines 82, 119, 498, 548).
- Type, date, edition: earnings press release (Exhibit 99), title line 13; dateline "New York,
  New York, October 31, 2025" (line 35). Q3 2025 edition. Forward-looking statements made "on the
  basis of the Company's views and assumptions as of October 31, 2025" (line 129).
- Period covered: three months ended September 30, 2025 vs 2024 ("Third Quarter", "3Q 2025") and
  nine months ended September 30, 2025 vs 2024 (Tables 2, 4, 5, 7, 9). Balance sheet "As of
  September 30, 2025, December 31, 2024 and September 30, 2024" (line 286). Cash flows nine
  months only. Calendar year. Guidance "Full Year 2025" (line 39).
- Entities and aliases: pet division row label is now "Hill's Pet Nutrition" in the division and
  geographic tables (lines 74, 102, 492, 540) (D05-D07 used "Hill's"); "Pet Nutrition" in Table 5
  (lines 425, 442). Brand list ends "Hill's Science Diet, Hill's Prescription Diet and Prime100"
  (line 119). Program named "Strategic Growth and Productivity Program", called "our previously
  announced Strategic Growth and Productivity Program" (line 37) and listed under "cost reduction
  plans (including the Strategic Growth and Productivity Program)" (line 129); "our new 2030
  strategy" (line 37). North America and Europe rows carry no recast "(1)" marker.
- Headline bullets (line 15): "Net sales increased 2.0%; Organic sales* increased 0.4%, including
  a 0.8% negative impact from lower private label pet sales having exited that non-strategic
  business"; "GAAP EPS increased 1% to $0.91; Base Business EPS* was flat at $0.91"; "GAAP Gross
  profit margin decreased 170 basis points to 59.4%; Base Business Gross profit margin* decreased
  190 basis points to 59.4%"; "Net cash provided by operations was $2,745 million for the first
  nine months of 2025"; toothpaste share "41.2% year to date"; manual toothbrushes "32.4% year to
  date"; "The Company updated its organic sales growth guidance for full year 2025 and maintained
  its earnings per share guidance".
- Tables (all $ millions except per share, unaudited):
  - Summary boxes lines 17-31: Q3 Net Sales $5,131 / $5,033, +2.0 %; EPS (diluted) $0.91 /
    $0.90, +1 %; Organic +0.4 %; Base Business EPS $0.91 / $0.91, — %.
  - Q3 Sales Growth by Division, lines 55-82 (columns as D07: % of sales, Net Sales, Organic,
    As Reported Volume**, Organic Volume, Pricing, FX): NA 19% / -0.4% / -0.5% / -0.5% / -0.5% /
    +0.1% / +0.1%; LA 23% / +2.0% / +1.7% / -1.9% / -1.9% / +3.6% / +0.3%; Europe 16% / +7.6% /
    +1.2% / +0.8% / +0.8% / +0.4% / +6.4%; Asia Pacific 14% / -1.5% / -1.0% / -3.5% / -3.5% /
    +2.5% / -0.5%; Africa/Eurasia 6% / +6.8% / +6.2% / -1.1% / -1.1% / +7.3% / +0.6%; Hill's Pet
    Nutrition 22% / +1.4% / -1.3% / -2.6% / -4.2% / +2.9% / +1.1% (line 74, outside fenced block);
    Total 100% / +2.0% / +0.4% / -1.5% / -1.9% / +2.3% / +1.2% (line 76). Footnote ** (line 82):
    Prime100 impact on as reported volume "1.6% and 0.4% for Hill's Pet Nutrition and Total
    Company, respectively."
  - Q3 Operating Profit by Division, lines 84-107: NA $190 / -8% / 19.0% / -150; LA $337 / -8% /
    28.6% / -300; Europe $209 / 16% / 26.1% / +180; Asia Pacific $188 / -6% / 26.2% / -120;
    Africa/Eurasia $68 / 5% / 23.0% / -40; Hill's Pet Nutrition $255 / -1% / 22.4% / -50 (line
    102); Total As Reported $1,059 / -1% / 20.6% / -60; Total Base Business* $1,059 / -2% / 20.6%
    / -90 (lines 105-106).
  - Table 1, Q3 income statement, lines 159-216: Net sales 5,131 / 5,033; Cost of sales 2,082 /
    1,959; Gross profit 3,049 / 3,074; GPM 59.4 % / 61.1 % (line 177); SG&A 1,971 / 1,979; Other
    (income) expense 19 / 30; Operating profit 1,059 / 1,065; OPM 20.6 % / 21.2 %; Non-service
    postretirement 21 / 23; Interest expense 67 / 74; Interest income 21 / 18; IBT 992 / 986;
    Provision 226 / 210; ETR 22.8 % / 21.3 % (line 195); NI incl. NCI 766 / 776; NCI 31 / 39; NI
    attributable 735 / 737; EPS basic 0.91 / 0.90, diluted 0.91 / 0.90; shares basic 807.8 /
    817.7, diluted 810.2 / 822.5; Advertising $674 / $694 (line 216).
  - Table 2, nine-month income statement, lines 218-278: Net sales 15,152 / 15,156 (line 232);
    Cost of sales 6,047 / 5,977; Gross profit 9,105 / 9,179; GPM 60.1 % / 60.6 % (line 236); SG&A
    5,833 / 5,833; Other 58 / 141; Operating profit 3,214 / 3,205; OPM 21.2 % / 21.1 %;
    Non-service postretirement 116 / 67; Interest expense 203 / 226; Interest income 56 / 51; IBT
    2,951 / 2,963; Provision 685 / 693; ETR 23.2 % / 23.4 % (line 254); NI incl. NCI 2,266 /
    2,270; NCI 97 / 120; NI attributable 2,169 / 2,150; EPS basic 2.68 / 2.62, diluted 2.67 /
    2.61 (lines 264-266); shares basic 810.0 / 820.1, diluted 812.8 / 824.2; Advertising $2,020 /
    $2,072 (line 274). Note (1) line 278.
  - Table 3, balance sheets (Sep 30, 2025 / Dec 31, 2024 / Sep 30, 2024), lines 280-320: Cash
    1,279 / 1,096 / 1,234; Receivables 1,807 / 1,521 / 1,712; Inventories 2,109 / 1,987 / 2,041;
    Other current assets 844 / 713 / 819; PP&E 4,560 / 4,422 / 4,421; Goodwill 3,702 / 3,272 /
    3,389; Other intangibles 1,889 / 1,756 / 1,834; Other assets 1,323 / 1,279 / 1,324; Total
    assets 17,513 / 16,046 / 16,774; Total debt 8,419 / 7,949 / 8,436; Other current liabilities
    5,383 / 5,099 / 5,038; Other non-current liabilities 2,473 / 2,454 / 2,464; Total liabilities
    16,275 / 15,502 / 15,938; Colgate equity 856 / 212 / 435; NCI 382 / 332 / 401. Debt less cash,
    cash equivalents and marketable securities $6,947 / $6,693 / $6,942; Working capital % of
    sales (4.0)% / (5.2)% / (3.6)% (lines 314-315). Note line 320: marketable securities $193 /
    $160 / $260.
  - Table 4, cash flows, nine months, lines 322-399: ERISA litigation matter 65 / — (line 343);
    Restructuring and termination benefits, net of cash (15) / 54; Net cash provided by (used in)
    operations 2,745 / 2,838 (line 356); Capital expenditures (387) / (377); Payment for
    acquisition, net of cash acquired (293) / — (line 365); Purchases of marketable securities
    (537) / (358); Proceeds 508 / 260; Short-term borrowing 139 / 337; Principal payments on debt
    (655) / (502); Proceeds from issuance of debt 497 / 2; Dividends paid (1,300) / (1,275) (line
    376); Purchases of treasury shares (804) / (1,284) (line 377); Proceeds from exercise of stock
    options 83 / 611; Other financing 145 / 1; Free cash flow before dividends $2,358 / $2,461
    (line 394); Income taxes paid $712 / $762; Interest paid $235 / $267; cash end 1,279 / 1,234.
  - Table 5, segment information, three and nine months, lines 401-452 (columns Q3 2025, Q3
    2024, 9M 2025, 9M 2024). Net sales: NA 999 / 1,004 / 3,024 / 3,076; LA 1,178 / 1,156 / 3,528
    / 3,676; Europe 801 / 744 / 2,228 / 2,102; Asia Pacific 714 / 725 / 2,092 / 2,133;
    Africa/Eurasia 297 / 278 / 863 / 827; Total OP&HC 3,989 / 3,907 / 11,735 / 11,814; Pet
    Nutrition 1,142 / 1,126 / 3,417 / 3,342; Total 5,131 / 5,033 / 15,152 / 15,156. Operating
    profit: NA 190 / 206 / 580 / 633; LA 337 / 365 / 1,052 / 1,187; Europe 209 / 181 / 566 / 502;
    AP 188 / 199 / 573 / 602; A/E 68 / 65 / 190 / 195; Total OP&HC 992 / 1,016 / 2,961 / 3,119;
    Pet Nutrition 255 / 258 / 778 / 691; Corporate (189) / (208) / (523) / (605); Total 1,059 /
    1,065 / 3,214 / 3,205. Corporate footnote is now (1) (line 448); no recast footnote.
  - Table 6, Q3 Geographic Sales Analysis, lines 454-500 (header lines 464-476 as D07). LAYOUT:
    rows at lines 478-482 and 488-494 are 3-cell pipe rows whose first cell holds the region label
    plus the first four values (As Reported, Organic, As Reported Volume, Organic Volume), then
    Pricing and FX cells; Europe and Asia Pacific (lines 484, 486) are plain lines. The original
    has the same structure (orig 476-492). Read in header order: Total 2.0% 0.4% (1.5)% (1.9)% 2.3%
    1.2%; NA (0.4) (0.5) (0.5) (0.5) 0.1 0.1; LA 2.0 1.7 (1.9) (1.9) 3.6 0.3; Europe 7.6 1.2 0.8
    0.8 0.4 6.4; AP (1.5) (1.0) (3.5) (3.5) 2.5 (0.5); A/E 6.8 6.2 (1.1) (1.1) 7.3 0.6; Total CP
    Products 2.1 0.9 (1.3) (1.3) 2.1 1.3; Hill's Pet Nutrition 1.4 (1.3) (2.6) (4.2) 2.9 1.1;
    Emerging Markets 1.6 1.0 (2.6) (2.6) 3.6 0.6; Developed Markets 2.3 (0.1) (0.7) (1.4) 1.3 1.7.
    These agree with the front division table (lines 67-76) for the six divisions and total.
    Footnote (1) line 498: Prime100 impact "0.4%, 1.6% and 0.7% for Total Company, Hill's Pet
    Nutrition and Developed Markets, respectively."
  - Table 7, nine-month Geographic Sales Analysis, lines 502-550: Total —% 1.2% (0.5)% (0.7)% 1.9%
    (1.4)% (line 526); NA (1.7) (1.5) (1.1) (1.1) (0.4) (0.2); LA (4.0) 3.0 0.5 0.5 2.6 (7.1);
    Europe 6.0 2.8 1.2 1.2 1.6 3.2; AP (1.9) (1.4) (2.9) (2.9) 1.5 (0.6); A/E 4.4 5.2 0.3 0.3 4.9
    (0.8); Total CP (0.7) 1.2 (0.4) (0.4) 1.6 (1.8); Hill's Pet Nutrition 2.2 1.2 (0.9) (1.8) 3.0
    0.2; EM (2.0) 1.8 (0.7) (0.7) 2.5 (3.8); DM 1.6 0.6 (0.4) (0.8) 1.4 0.6. Footnote (1) line
    548: Prime100 nine-month impact "0.2%, 0.9% and 0.4% for Total Company, Hill's Pet Nutrition
    and Developed Markets".
  - Table 8, Q3 Non-GAAP Reconciliations, lines 552-641: Gross profit GAAP 3,049 / 3,074, GPI — /
    9, non-GAAP 3,049 / 3,083; GPM GAAP 59.4 % / 61.1 % (170), GPI 0.2 % (2024), non-GAAP 59.4 % /
    61.3 % (190) (lines 571-573); SG&A non-GAAP 1,971 / 1,976 (GPI (3) in 2024); Other (income)
    expense non-GAAP 19 / 27 (GPI (3) in 2024); Operating profit GAAP 1,059 / 1,065 ((1) %), GPI —
    / 15, non-GAAP 1,059 / 1,080 ((2) %) (lines 588-592); OPM GAAP 20.6 % / 21.2 % (60), GPI 0.3 %
    (2024), non-GAAP 20.6 % / 21.5 % (90) (line 596). "Table 8 Continued" is headed "For the Three
    Months Ended September 30, 2024" only (line 606): As Reported 986 / 210 / 776 / 39 / 737 /
    21.3 % / 0.90; GPI 15 / 2 / 13 / — / 13 / (0.1)% / 0.01; Non-GAAP 1,001 / 212 / 789 / 39 / 750
    / 21.2 % / 0.91 (lines 630-634). No 2025 adjustment rows in Table 8 (2025 cells are "—").
  - Table 9, nine-month Non-GAAP Reconciliations, lines 643-785: Gross profit GAAP 9,105 / 9,179,
    GPI — / 19, non-GAAP 9,105 / 9,198; GPM GAAP 60.1 % / 60.6 % (50), GPI 0.1 % (2024), non-GAAP
    60.1 % / 60.7 % (60) (lines 660-662); SG&A GAAP 5,833 / 5,833, ERISA (15) / —, GPI — / (4),
    non-GAAP 5,817 / 5,829; SG&A % GAAP 38.5 % / 38.5 % (—), ERISA (0.1)%, non-GAAP 38.4 % / 38.5
    % (10) (lines 674-676); Other (income) expense GAAP 58 / 141, acquisition (9) / —, GPI — / (54),
    non-GAAP 48 / 87; Operating profit GAAP 3,214 / 3,205 (— %), ERISA 15 / —, acquisition 9 / —,
    GPI — / 77, non-GAAP 3,240 / 3,282 ((1) %) (lines 688-696); OPM GAAP 21.2 % / 21.1 % (10),
    ERISA 0.1 %, acquisition 0.1 %, GPI 0.6 % (2024), non-GAAP 21.4 % / 21.7 % (30) (lines
    700-702); Non-service postretirement GAAP 116 / 67, ERISA (50) / —, non-GAAP 66 / 67 (lines
    707-709). Continued: 2025 As Reported 2,951 / 685 / 2,266 / 97 / 2,169 / 23.2 % / 2.67 (line
    747); ERISA 65 / 12 / 53 / — / 53 / —% / 0.06 and Acquisition-related costs 9 / 2 / 7 / — / 7
    / —% / 0.01 (both on line 749); Non-GAAP 3,027 / 702 / 2,325 / 97 / 2,228 / 23.2 % / 2.74
    (line 751). 2024 As Reported 2,963 / 693 / 2,270 / 120 / 2,150 / 23.4 % / 2.61; GPI 77 / 10 /
    67 / — / 67 / (0.3)% / 0.08; Non-GAAP 3,040 / 703 / 2,337 / 120 / 2,217 / 23.1 % / 2.69 (lines
    775-779).
- Lists: six division rows; Base Business exclusion list three items (line 135, same as D07);
  Corporate charge sentences two (lines 450-452: nine months 2025 "ERISA litigation matter of $15
  and acquisition-related costs of $9"; "three and nine months ended September 30, 2024 ...
  2022 Global Productivity Initiative of $15 and $77, respectively"); Prime100 footnotes (lines
  82, 498, 548); risk topics (line 129) add "category growth rates" and name the Strategic Growth
  and Productivity Program.
- Forecasts, guidance, deadlines, effective dates:
  - "Full Year 2025 Guidance" (line 39): "Based on current spot rates and including the estimated
    impact of tariffs announced and finalized as of October 29, 2025:" (line 41). Bullet (line
    15): "updated its organic sales growth guidance for full year 2025 and maintained its earnings
    per share guidance".
    - Net sales (line 43): "The Company still expects net sales to be up low single digits,
      including a flat to low-single-digit negative impact from foreign exchange."
    - Organic (line 45): "The Company now expects organic sales growth to be 1% to 2%, roughly in
      line with year-to-date organic sales growth of 1.2%, versus at the low end of 2% to 4%
      previously. This includes an approximately 70 basis point impact from our exit from private
      label pet sales."
    - GAAP (line 47): "the Company now expects gross profit margin to be roughly in line with
      year-to-date gross profit margin of 60.1% versus roughly flat previously, and still expects
      advertising to be roughly flat as a percentage of net sales and earnings per share to be up
      low single digits."
    - Base Business (line 49): same structure: "now expects gross profit margin to be roughly in
      line with year-to-date gross profit margin of 60.1% versus roughly flat previously, and still
      expects advertising to be roughly flat as a percentage of net sales and earnings per share
      to be up low single digits."
    - The headline bullet names organic (updated) and EPS (maintained); the gross-margin "now
      expects" change (lines 47, 49) is not named in the bullet. No tax-rate or program-charge
      guidance item.
  - Dated items: tariffs "as of October 29, 2025" (line 41); assumptions "as of October 31, 2025"
    (line 129); private-label exit described as completed ("having exited", line 15; "as we have
    exited", line 35) with no exit date stated; no recast/effective-date footnote; call/materials
    "today" (lines 113-115). Prime100 acquisition date/price not stated (only (293) cash line 365,
    $9 costs). No annual-meeting, dividend-declaration, divestiture-closing, impairment or
    program-approval item.
- Hedged claims: CEO "we are well positioned to reaccelerate growth despite uncertainty in global
  markets and lower worldwide category growth" (line 37); the program "will help ensure" (line
  37); guidance "roughly in line", "approximately 70 basis point impact" (line 45); assumptions
  dated "except as otherwise noted with respect to tariffs" (line 129); rounding caveats lines
  78, 446, 496, 546, 637, 711, 781.
- Rounded prose beside exact figures:
  - "year-to-date organic sales growth of 1.2%" (line 45) = Table 7 Total Company organic 1.2%
    (line 526).
  - "year-to-date gross profit margin of 60.1%" (lines 47, 49) = Table 2 GPM 60.1 % (line 236) and
    Table 9 GAAP/non-GAAP 60.1 % (lines 660-662).
  - "$2,745 million for the first nine months" (line 15) = 2,745 (line 356).
  - GPM "decreased 170 basis points to 59.4%" / Base Business "decreased 190 basis points"
    (line 15) = lines 177, 571-573.
  - Private-label drag Q3 "0.8%" (line 15); full-year organic guidance "approximately 70 basis
    point impact" (line 45).
  - "approximately two billion children" (line 119) vs "approximately 1.8 billion" in D05-D07.
- Notes: Q3 2025 has no non-GAAP adjustments: Base Business OP equals As Reported ($1,059, lines
  105-106), Base Business EPS equals GAAP EPS ($0.91), no Q3 2025 Corporate charge sentence (lines
  450-452). Arithmetic on printed figures (navigation): nine-month 2025 net sales 15,152 = D07
  six-month 10,021 + Q3 5,131; nine-month 2024 15,156 vs 10,124 + 5,033 = 15,157; nine-month
  2024 GPI 77 (line 452) vs D07 six-month 63 + Q3 15 = 78; nine-month 2025 non-GAAP operating
  profit 3,240 (line 696) vs 3,214 + 15 + 9 = 3,238 (SG&A non-GAAP 5,817 vs 5,833 - 15; Other
  non-GAAP 48 vs 58 - 9); rounding note line 711. Nine-month EPS 2.67 = 1.76 + 0.91; 2024 2.61 =
  1.71 + 0.90; nine-month Base Business EPS 2.74 = 1.83 + 0.91; 2024 2.69 = 1.78 + 0.91.
  Advertising nine months 2,020 = 1,346 + 674; 2024 2,072 = 1,378 + 694.
- Operative definitions, rules and scope exceptions:
  - Base Business (line 135): "Base Business operating results exclude, as applicable, charges
    resulting from the ERISA litigation matter and the 2022 Global Productivity Initiative and
    acquisition-related costs." The Strategic Growth and Productivity Program is not in this list,
    and no table in D08 shows a charge row for it.
  - Organic sales growth (line 137); Free cash flow before dividends (line 139); both-bases list
    (line 145).
  - ERISA litigation matter appears only in 2025 year-to-date columns (cash flow line 343; SG&A
    line 668; OP line 692; non-service line 708; line 749): same $65 pre-tax / $15 SG&A / $50
    non-service / $0.06 EPS as D06-D07; ETR impact "—%" here vs (0.3)% in D06 Q1 (D06 line 532)
    and (0.1)% in D07 six months (D07 line 813).
- Amendments or contradictions:
  - Guidance vs D07 (D07 lines 47-53 vs D08 lines 43-49): organic "at the low end of 2% to 4%" ->
    "1% to 2%" (stated as "versus at the low end of 2% to 4% previously"); gross profit margin
    "roughly flat as a percentage of net sales" -> "roughly in line with year-to-date gross profit
    margin of 60.1% versus roughly flat previously" (GAAP and Base Business); net sales,
    advertising and EPS "still expects" (unchanged). Tariff basis date July 31 -> October 29, 2025.
  - Program naming: D07 "a new three-year productivity program" (D07 line 41) -> D08 "our
    previously announced Strategic Growth and Productivity Program" (line 37). D08 does not restate
    the D07 charge estimate ($200-$300 million) or the December 31, 2028 date.
  - Prior-period comparatives to check against D04 (Q3 2024 release, other part): Q3 2024 Net
    sales 5,033; GAAP EPS 0.90; Base Business EPS 0.91; Operating profit 1,065 / non-GAAP 1,080;
    GPM 61.1 % / non-GAAP 61.3 %; ETR 21.3 % / 21.2 %; GPI 15; nine-month 2024 Net sales 15,156,
    EPS 2.61, Base Business EPS 2.69, OP 3,205 / 3,282, GPI 77; Sep 30, 2024 balance-sheet column
    (Table 3).
- Coverage: FULL. Read lines 1-110, 110-239, 239-408, 408-577, 577-746, 746-786 (end of file);
  keyword sweeps for program/2030/acquisition/divestiture/dividend/impairment/approval/board/
  recast/tariff/private label (all hits located above). Spot-checks vs original
  `docs/cl_ex991_2025-10-31.txt`: Table 1 row "Net sales | $ 5,131 | $ 5,033" orig 171 (text
  173); Table 3 note "Marketable securities of $193" orig 318 (text 320); irregular Table 6 rows
  orig 478/482 (text 480/484); merged line orig 747 (text 749); guidance date orig 39 (text 41).
  Page count not applicable. No gap markers; no unread range.

## Shared ground within D05-D08 (navigation only; locations, no hooks)

- Issuer and speaker: every document is issued by Colgate-Palmolive Company (NYSE:CL), New
  York, with Noel Wallace quoted as Chairman, President and CEO (D05 61; D06 35; D07 35; D08 35).
  Nielsen and the SEC are mentioned only (market-share and cautionary boilerplate).
- Editions and periods: D05 Q4/FY2024 (dated January 31, 2025); D06 Q1 2025 (April 25, 2025);
  D07 Q2 and six months 2025 (August 1, 2025); D08 Q3 and nine months 2025 (October 31, 2025).
  Prior-year comparatives: Q4/FY2023 (D05), Q1 2024 (D06), Q2/six-month 2024 (D07), Q3/nine-month
  2024 (D08). FY2025 actual results are not in D05-D08.
- Repeated balance-sheet column: December 31, 2024 appears in D05 Table 3 (lines 333-354), D06
  Table 2 (lines 235-256), D07 Table 3 (lines 309-330), D08 Table 3 (lines 294-315) with identical
  values (cash 1,096; total assets 16,046; total debt 7,949; Colgate equity 212; debt less cash
  6,693; working capital (5.2)%; marketable securities $160).
- Year-to-date chain for 2025: Q1 (D06 Tables 1/3/5/6) -> six months (D07 Tables 2/4/5/7/9) ->
  nine months (D08 Tables 2/4/5/7/9). Three-month-only figures for Q2 and Q3 cash flow are not
  printed (cash-flow tables are year-to-date only). The same Q1 ERISA charge ($65) and the Q2
  acquisition-related costs ($9) recur in each later year-to-date table.
- FY2025 guidance chain (exact wording in each section above): D05 lines 69-79 (initial, "Based
  on current spot rates") -> D06 lines 41-51 ("updated", "revised", tariffs as of April 24, 2025)
  -> D07 lines 43-53 ("updated its organic sales growth guidance", tariffs as of July 31, 2025) ->
  D08 lines 39-49 ("updated its organic sales growth guidance ... and maintained its earnings per
  share guidance", tariffs as of October 29, 2025). Item tracks: net sales (D05 73, D06 45, D07 47,
  D08 43); organic (D05 75, D06 47, D07 49, D08 45); GAAP gross margin/advertising/EPS (D05 77, D06
  49, D07 51, D08 47); Base Business (D05 79, D06 51, D07 53, D08 49). None of D05-D08 gives a
  tax-rate, capital-expenditure, cash-flow or restructuring-charge guidance item; none uses the
  words "raised" or "lowered".
- Base Business definition chain: D05 line 174 (ERISA litigation matter, foreign tax matter, 2022
  Global Productivity Initiative, product recall costs) -> D06 line 138 (ERISA, 2022 GPI) -> D07
  line 152 (ERISA, 2022 GPI, acquisition-related costs) -> D08 line 135 (same as D07). Organic
  sales and free-cash-flow definitions are unchanged across all four (D05 176/178, D06 140/142,
  D07 154/156, D08 137/139).
- Adjustment items by edition: foreign tax matter and product recall costs appear only in D05's
  2023 columns (lines 496, 761, 768, 774, 847, 851); ERISA litigation matter in D05 2023 columns
  (lines 382, 782, 846) and D06-D08 2025 columns; 2022 GPI in all four (prior-year columns only in
  D06-D08); acquisition-related costs only in D07-D08 2025 columns.
- Productivity program: announced D07 line 41 (unnamed, three-year, $200-$300 million
  cumulative pre-tax charges, substantially all by December 31, 2028; "announced on August 1,
  2025", D07 line 146) -> named "Strategic Growth and Productivity Program", "previously
  announced", in D08 lines 37 and 129. "2030 strategy": D07 line 41, D08 line 37. Not in the
  Base Business definitions of D07-D08; no charge rows in D07-D08 tables.
- Prime100: footnotes D07 92/521/573 and D08 82/498/548; brand list D08 119; related cash line
  "Payment for acquisition, net of cash acquired" (293) in D07 380 and D08 365; acquisition-related
  costs $9 (D07 467/469/612/620/626/664/746/757/764/816; D08 450/682/693/700/749); the phrase
  "acquisition-related costs" also appears in the generic non-GAAP boilerplate of all four (D05
  184, D06 148, D07 160, D08 145) and in the Base Business definitions of D07 152 and D08 135. Goodwill: 3,272 (Dec 31,
  2024) -> 3,334 (Mar 31, 2025, D06 240) -> 3,696 (Jun 30, 2025, D07 314) -> 3,702 (Sep 30, 2025,
  D08 299). No document in this part states the acquisition date.
- Private-label pet: drag on organic growth FY2024 0.5% and Q4 2024 0.5% (D05 17, 39); Q1 2025
  0.4% (D06 15); Q2 2025 0.6% (D07 15); Q3 2025 0.8% (D08 15); FY2025 guidance "approximately 70
  basis point impact" (D08 45). Wording: "planned exit from private label pet nutrition over the
  course of 2025" (D05 75) -> "planned exit from private label pet sales" (D07 49) -> "having
  exited that non-strategic business" (D08 15, 35). D06 guidance does not mention it.
- Recast footnote ("reporting structure effective as of July 1, 2024"; skin health moved from
  Europe to North America): D05 (113, 142, 486, 542, 590), D06 (85, 112, 390, 444), D07 (88, 124,
  463, 523, 575); absent from D08. Long form with the skin-health sentence: D05 113, D06 85 only.
- Market share year to date: toothpaste 41.4% (D05 39) / 40.9% (D06 15) / 41.1% (D07 15) / 41.2%
  (D08 15); manual toothbrushes 32.2% (D05 41) / 31.9% (D06 15) / 32.4% (D07 15) / 32.4% (D08
  15). Measurement basis and Venezuela exclusion: D05 160-162, D06 126-128, D07 140-142, D08
  123-125.
- Labels that change across editions: "Hill's" (D05-D07) vs "Hill's Pet Nutrition" (D08) vs
  "Pet Nutrition" (Table 5 in all); volume column split into "As Reported Volume" and "Organic
  Volume" from D07 onward; % of Total Company Sales one decimal in D05, whole numbers in D06-D08;
  title "Colgate Announces" (D05, D06) vs "Colgate-Palmolive Company Announces" (D07, D08);
  Bright Smiles reach "approximately 1.8 billion" (D05 154, D06 124, D07 136) vs "approximately two
  billion" (D08 119); annual-meeting sentence only in D05 (line 156, Friday, May 9, 2025).
- Narrative repeating tables: headline bullets (D05 17/39-41; D06 15; D07 15; D08 15) and summary
  boxes repeat Table 1/2 and reconciliation figures; D08 guidance quotes year-to-date 1.2% and
  60.1% from Tables 7/2/9; ratios stated only in prose: D05 advertising "+15%"/"+19%" (line 65),
  D06 advertising "13.6% to sales" (line 37).
- External references not in these documents (mentions, not extraction gaps): recast historical
  segment information "on the Company's website" (D05 113, D06 85); Form 10-K for 2023 (D05 168)
  and 2024 (D06 132, D07 146, D08 129); prepared materials and webcast (all four).

## Gaps (D05-D08)

- None for readable text: every line of D05 (1-862), D06 (1-571), D07 (1-852) and D08 (1-786)
  was read; no gap markers; original = text + 2-line header verified per document.
- Layout cautions (not missing text): flattened multi-row lines (D05 739, D06 468/489, D07 626/764,
  D08 571/596/660/674/700/749); column headers broken across lines in Tables 6-9 of each
  document; D08 Table 6 irregular pipe cells (lines 478-494; same in original). Rows outside
  fenced blocks: D05 851, D07 82/117, D08 74/102.
- Comparisons with D01-D04 and D09-D12 (prior-period figures as first reported, later FY2025
  actuals, later guidance) belong to the other mapping parts and are not verified here.


<!-- merged from map-part3.md: aq-docket-trial-02 - document map, part 3 (D09-D12) -->
Navigation only, written by a mapper for D09, D10, D11 and D12. The caller merges this part
into `doc-map.md`. Line numbers are `text/Dnn.txt` lines. For each of these four files the
text file is the original `docs/` file plus a two-line header ("# Dnn | docs/<file>" and a
blank line), so original line = text line - 2 (verified by spot-checks below). Sources are
plain-text captures (`pages: null`), so page counts are not applicable. Questions quote the
documents, never this map.

## D09 - Colgate-Palmolive 4th Quarter and Full Year 2025 results release (January 30, 2026)

- Source: docs/cl_ex991_2026-01-30.txt | text/D09.txt lines 1-908 (pages not applicable).
  File header "a4q2025pressreleasetables.htm" (L5), "Exhibit 99" (L11).
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL) (L63). Quoted executive: Noel
  Wallace, Chairman, President and Chief Executive Officer (L63-67). Mentioned only: Nielsen
  (market share vendor, L158), the SEC (L164-166).
- Type, date, edition: earnings press release, title "Colgate-Palmolive Company Announces 4th
  Quarter and Full Year 2025 Results" (L13); dateline "New York, New York, January 30, 2026"
  (L63); forward-looking statements "as of January 30, 2026" (L166); refers to the Form 10-K
  "for the year ended December 31, 2024" (L166).
- Period covered: fourth quarter 2025 ("Three Months Ended December 31, 2025", L200) and full
  year 2025 ("Twelve Months Ended December 31, 2025", L263), each with 2024 comparatives;
  fiscal year = calendar year. Balance sheet "As of December 31, 2025 and December 31, 2024"
  (L326). Labels used: "4Q 2025", "fourth quarter 2025", "Full Year". Guidance is for full
  year 2026 (L73).
- Entities and aliases:
  - Divisions North America, Latin America, Europe, Asia Pacific, Africa/Eurasia, Hill's Pet
    Nutrition (L102-107). In Table 5 the first five sit under "Oral, Personal and Home Care"
    (L456, L473) and Hill's appears as "Pet Nutrition" (L466, L483). "Total CP Products"
    (Tables 6/7, L535, L585) = the non-Hill's divisions. "Emerging Markets" defined L547/L597
    ("Latin America, Asia (excluding Japan), Africa/Eurasia and Central Europe"); "Developed
    Markets" L541/L591 (no definition printed).
  - Skin health business, "primarily Filorga" (L71). Prime100 pet food business (acquisition
    footnotes L116, L545, L595; brand list L152). Private label pet: "lower private label pet
    volume" (L17, L41), "excluding private label" (L63), "our exit from the private label pet
    food business" (L79).
  - Restructuring programs: "Strategic Growth and Productivity Program in 2025 and 2022 Global
    Productivity Initiative in 2024" (L172; also L739, L903, L491-497). ERISA litigation matter
    (L172, L383, L491, L495, L617, L643, L660, L774, L801, L821, L862).
  - "Colgate Bright Smiles, Bright Futures program" (L152).
- Tables (all "$ in millions" / "Dollars in Millions Except Per Share Amounts" unless noted):
  - L21-27 FY GAAP summary: Net Sales $20,382 vs $20,101, +1.4%; EPS (diluted) $2.63 vs $3.51,
    -25%. L29-35 FY Base Business: Organic Sales Growth +1.4%; Base Business EPS $3.69 vs $3.60,
    +3%.
  - L45-51 Q4 GAAP summary: Net Sales $5,230 vs $4,944, +5.8%; EPS $(0.05) vs $0.90, -106%.
    L53-59 Q4 Base Business: Organic +2.2%; Base Business EPS $0.95 vs $0.91, +4%.
  - L89-116 "Fourth Quarter Sales Growth By Division (% change 4Q 2025 vs. 4Q 2024)", columns %
    of Total Company Sales / Net Sales As Reported / Organic Sales / Volume** / Pricing / FX:
    North America 19% -1.5% -1.8% -2.3% +0.5% +0.3%; Latin America 24% +12.8% +6.5% +2.3%
    +4.2% +6.3%; Europe 14% +9.8% +1.8% +0.8% +1.0% +8.1%; Asia Pacific 14% -0.3% +0.1% -2.2%
    +2.3% -0.4%; Africa/Eurasia 6% +15.0% +10.3% +1.1% +9.1% +4.7%; Hill's 23% +4.9% +1.5% +0.3%
    +3.0% +1.6%; Total Company (L110, outside the fenced block) 100% +5.8% +2.2% —% +2.7% +3.1%.
    L112 "Table may not sum due to rounding." L116 Prime100 effect on as reported volume 1.8%
    (Hill's) and 0.5% (Total Company).
  - L118-140 "Fourth Quarter Operating Profit By Division" ($ millions; % change; % to net
    sales; bps change): NA $203 -1% 19.9% —; LA $360 6% 28.8% -180; Europe $183 17% 24.9% +160;
    AP $188 -11% 26.0% -310; Africa/Eurasia $65 13% 21.1% -40; Hill's $286 4% 23.9% -20; Total
    Company As Reported $92 -91% 1.8% NM; Total Company Base Business $1,108 3% 21.2% -50.
    Precision: % changes are whole percents and do not always equal a recomputation from the
    rounded $ (e.g. Europe $183 vs prior $155 in Table 5 L479).
  - L194-255 Table 1, Q4 income statement (2025 vs 2024): Net sales 5,230/4,944; Cost of sales
    2,084/1,962; Gross profit 3,146/2,982; GP margin 60.2%/60.3% (L212); SG&A 2,069/1,895;
    Other (income) expense, net 66/23; Goodwill and intangible assets impairment charges 919/—
    (L218); Operating profit 92/1,064; OP margin 1.8%/21.5%; Non-service related
    postretirement costs (61)/20; Interest expense 64/66; Interest income 18/16; Income before
    income taxes 107/994; Provision 112/215; Effective tax rate 104.7%/21.6% (L231); Net income
    (loss) incl. NCI (5)/779; NCI 32/40; Net income (loss) attributable $(37)/$739; Basic EPS
    $(0.05)/$0.91; Diluted $(0.05)/$0.90; shares basic 804.7/816.0, diluted 804.7/819.7;
    Advertising $682/$648 (L251). Footnote (1) L255: Q4 2025 diluted computation "excludes 1.3
    million of incremental common shares ... as they are anti-dilutive."
  - L257-318 Table 2, FY income statement: Net sales 20,382/20,101; Cost of sales 8,131/7,940;
    Gross profit 12,251/12,161; GP margin 60.1%/60.5%; SG&A 7,903/7,729; Other (income)
    expense, net 123/164; impairment 919/—; Operating profit 3,306/4,268; OP margin
    16.2%/21.2%; Non-service postretirement 55/87; Interest expense 267/292; Interest income
    75/67; Income before taxes 3,059/3,956; Provision 798/907; ETR 26.1%/22.9% (L294); NI incl.
    NCI 2,261/3,049; NCI 129/160; NI attributable $2,132/$2,889; Basic EPS $2.64/$3.53; Diluted
    $2.63/$3.51; shares basic 808.7/819.1, diluted 811.1/823.2; Advertising $2,703/$2,720
    (L314). Note (1) L318: EPS "computed independently for each quarter and any year-to-date
    period"; quarters may not sum.
  - L320-360 Table 3, balance sheet Dec 31, 2025/2024: Cash 1,288/1,096; Receivables
    1,675/1,521; Inventories 2,032/1,987; Other current assets 714/713; PP&E 4,660/4,422;
    Goodwill 3,122/3,272; Other intangible assets 1,536/1,756; Other assets 1,303/1,279; Total
    assets 16,330/16,046; Total debt 7,988/7,949; Other current liabilities 5,736/5,099; Other
    non-current liabilities 2,241/2,454; Total liabilities 15,965/15,502; CP shareholders'
    equity 54/212; NCI 311/332. L354 Debt less cash, cash equivalents and marketable securities
    $6,593/$6,693; L355 Working capital % of sales (7.0)%/(5.2)%. L360 marketable securities
    $107/$160 included in Other current assets.
  - L362-440 Table 4, cash flows, twelve months only (no Q4 cash flow table): Net cash provided
    by operations 4,198/4,107 (L397); ERISA litigation matter 65/— (L383); Restructuring and
    termination benefits, net of cash (7)/51; impairment 919/—; Capital expenditures
    (564)/(561) (L403); Payment for acquisition, net of cash acquired (293)/— (L406); Proceeds
    from issuance of debt 1,188/2; Dividends paid (1,823)/(1,789) (L417); Purchases of treasury
    shares (1,210)/(1,739) (L418); Proceeds from exercise of stock options 101/638; Free cash
    flow before dividends $3,634/$3,546 (L435); Income taxes paid $913/$933; Interest paid
    $270/$302 (L438-439).
  - L442-497 Table 5, Segment Information, three and twelve months (columns Q4 2025, Q4 2024,
    FY2025, FY2024). Net sales: NA 1,021/1,036/4,045/4,113; LA 1,248/1,106/4,776/4,782; Europe
    734/668/2,962/2,770; AP 722/724/2,814/2,858; Africa/Eurasia 309/269/1,172/1,095; Total Oral,
    Personal and Home Care 4,034/3,804/15,769/15,618; Pet Nutrition 1,196/1,140/4,613/4,483;
    Total 5,230/4,944/20,382/20,101. Operating profit: NA 203/206/784/839; LA
    360/339/1,411/1,526; Europe 183/155/748/658; AP 188/211/760/812; Africa/Eurasia
    65/58/255/253; Total OP&HC 999/969/3,959/4,088; Pet Nutrition 286/275/1,064/965; Corporate
    (1,194)/(179)/(1,717)/(784); Total 92/1,064/3,306/4,268. Footnote (1) L489 (Corporate
    contents) and charge notes L491-497 (see definitions).
  - L499-547 Table 6, Q4 geographic sales analysis (columns: As Reported sales change; Organic
    sales change; As Reported Volume; Organic Volume; Pricing, coupons, consumer and trade
    incentives; Foreign exchange): Total Company 5.8% 2.2% —% (0.5)% 2.7% 3.1% (L523); NA
    (1.5)% (1.8)% (2.3)% (2.3)% 0.5% 0.3%; LA 12.8% 6.5% 2.3% 2.3% 4.2% 6.3%; Europe 9.8% 1.8%
    0.8% 0.8% 1.0% 8.1%; AP (0.3)% 0.1% (2.2)% (2.2)% 2.3% (0.4)%; Africa/Eurasia 15.0% 10.3%
    1.1% 1.1% 9.1% 4.7%; Total CP Products 6.0% 2.5% (0.1)% (0.1)% 2.6% 3.6%; Hill's 4.9% 1.5%
    0.3% (1.5)% 3.0% 1.6%; Emerging Markets 8.7% 4.5% 0.3% 0.3% 4.2% 4.3%; Developed Markets
    3.5% 0.5% (0.3)% (1.0)% 1.5% 2.2%. Footnote (1) L545: Prime100 effect on as reported volume
    0.5% / 1.8% / 0.7% (Total Company / Hill's / Developed Markets).
  - L549-597 Table 7, FY geographic sales analysis: Total Company 1.4% 1.4% (0.4)% (0.7)% 2.1%
    (0.3)% (L573); NA (1.6)% (1.6)% (1.4)% (1.4)% (0.2)% (0.1)%; LA (0.1)% 3.9% 0.9% 0.9% 2.9%
    (4.0)%; Europe 6.9% 2.6% 1.1% 1.1% 1.5% 4.4%; AP (1.5)% (1.0)% (2.7)% (2.7)% 1.7% (0.5)%;
    Africa/Eurasia 7.0% 6.5% 0.5% 0.5% 6.0% 0.5%; Total CP Products 1.0% 1.5% (0.3)% (0.3)% 1.8%
    (0.5)%; Hill's 2.9% 1.2% (0.6)% (1.7)% 3.0% 0.5%; EM 0.6% 2.5% (0.5)% (0.5)% 2.9% (1.9)%; DM
    2.0% 0.6% (0.4)% (0.8)% 1.4% 1.0%. Footnote (1) L595: Prime100 effect 0.3% / 1.1% / 0.4%.
  - L599-743 Table 8, Q4 non-GAAP reconciliations: Gross profit GAAP 3,146/2,982, restructuring
    —/1, non-GAAP 3,146/2,983 (no Q4 gross margin rows); SG&A GAAP 2,069/1,895, ERISA (84),
    restructuring (6)/(1), non-GAAP 1,980/1,894; SG&A % of sales GAAP 39.6%/38.3% (+130 bps),
    non-GAAP 37.9%/38.3% (-40) (L623-627); Other (income) expense GAAP 66/23, restructuring
    (7)/(5), non-GAAP 58/18; Operating profit GAAP 92/1,064 (91)%, + impairment 919, ERISA 84,
    restructuring 13/7, non-GAAP 1,108/1,071 +3% (L636-646); OP margin GAAP 1.8%/21.5% NM,
    non-GAAP 21.2%/21.7% (-50) (L650-654); Non-service related postretirement costs GAAP
    $(61)/$20, ERISA 84, non-GAAP $24/$20 (L658-661). Continued (L667-733), columns Income
    before taxes / Provision / NI incl. NCI / NCI / NI attributable / ETR / Diluted EPS:
    2025 As Reported $107 $112 $(5) $32 $(37) 104.7% $(0.05); impairment 919 125 794 — 794
    (81.7)% 0.99 (L701); restructuring 13 2 11 — 11 (0.1)% 0.01; Non-GAAP $1,038 $238 $800 $32
    $768 22.9% $0.95 (L705). No ERISA row at the pre-tax level for Q4 2025. 2024 As Reported
    $994 $215 $779 $40 $739 21.6% $0.90; restructuring 7 1 6 — 6 —% 0.01; Non-GAAP $1,001 $216
    $785 $40 $745 21.6% $0.91 (L729-733).
  - L745-907 Table 9, FY non-GAAP reconciliations: Gross profit GAAP 12,251/12,161,
    restructuring —/20, non-GAAP 12,251/12,181; GP margin GAAP 60.1%/60.5% (-40 bps), non-GAAP
    60.1%/60.6% (-50) (L764-768); SG&A GAAP 7,903/7,729, ERISA (99), restructuring (6)/(6),
    non-GAAP 7,797/7,723; SG&A % GAAP 38.8%/38.5% (+30), non-GAAP 38.3%/38.4% (-10); Other
    (income) expense GAAP 123/164, acquisition-related costs (9)/—, restructuring (7)/(59),
    non-GAAP 107/105; Operating profit GAAP 3,306/4,268 (23)%, + impairment 919, ERISA 99,
    restructuring 13/85, acquisition-related 9/—, non-GAAP 4,347/4,353 —% (L794-805); OP margin
    GAAP 16.2%/21.2% (-500), non-GAAP 21.3%/21.7% (-40) (L809-815); Non-service postretirement
    GAAP 55/87, ERISA 34, non-GAAP 90/87 (L819-822). Continued: FY2025 As Reported $3,059 $798
    $2,261 $129 $2,132 26.1% $2.63; impairment 919 125 794 — 794 (2.9)% 0.98 (L861); ERISA 65
    12 53 — 53 (0.1)% 0.06 (L862); restructuring 13 2 11 — 11 —% 0.01; acquisition-related 9 2
    7 — 7 —% 0.01; Non-GAAP $4,065 $940 $3,125 $129 $2,996 23.1% $3.69 (L869). FY2024 As
    Reported $3,956 $907 $3,049 $160 $2,889 22.9% $3.51; restructuring 85 12 73 — 73 (0.2)%
    0.09; Non-GAAP $4,041 $919 $3,122 $160 $2,962 22.7% $3.60 (L893-897).
- Lists:
  - Brand list L152, 25 items in this order: Colgate, Palmolive, Ajax, Axion, Darlie, elmex,
    EltaMD, Fabuloso, Filorga, hello, Hill's Prescription Diet, Hill's Science Diet, Irish
    Spring, Lady Speed Stick, meridol, PCA SKIN, Prime100, Protex, Sanex, Softsoap, Sorriso,
    Soupline, Speed Stick, Suavitel, Tom's of Maine (last). Focus areas: "Oral Care, Personal
    Care, Home Care and Pet Nutrition"; "more than 200 countries and territories".
  - Base Business exclusions L172 (four: impairment charges; ERISA litigation matter;
    restructuring programs; acquisition-related costs).
  - Forward-looking topic list L164-166, naming conflicts "such as in Ukraine, the Middle East
    and Venezuela" and "cost reduction plans (including the Strategic Growth and Productivity
    Program)".
  - Measures disclosed on both GAAP and Base Business bases L180 (Gross profit ... Diluted
    earnings per common share).
- Forecasts, guidance, deadlines, effective dates:
  - "Full Year 2026 Guidance" (L73), initial guidance (no raised/lowered/maintained wording),
    preface L75: "Based on current spot rates and including the estimated impact of tariffs
    announced and finalized as of January 28, 2026:"
    - Net sales L77: "The Company expects net sales to be up 2% to 6%, including a
      low-single-digit positive impact from foreign exchange."
    - Organic sales L79: "The Company expects organic sales growth to be 1% to 4%. This
      includes an approximately 20 basis point impact from our exit from the private label pet
      food business."
    - GAAP L81: "gross profit margin expansion with advertising up on both a dollar basis and as
      a percentage of net sales and double-digit earnings per share growth."
    - Base Business L83: "gross profit margin expansion with advertising up on both a dollar
      basis and as a percentage of net sales and low to mid-single-digit earnings per share
      growth."
    - Exclusion fact: no tax-rate item and no restructuring-charge item in the 2026 guidance
      list (L73-83).
  - CEO outlook L67: "As we begin 2026, while we expect the difficult operating environment and
    slower category growth to continue in the short term ..."
  - Dated events: impairment "During the fourth quarter" (L71: "non-cash, after-tax charge of
    $794 million to adjust the carrying values of goodwill and intangible assets related to the
    skin health business"; pre-tax 919 in Tables 1, 2, 4, 5, 8, 9); prepared materials
    "approximately 7:00 a.m. ET today" (L146), call "8:30 a.m. ET today" (L148); annual meeting
    "currently scheduled for Friday, May 8, 2026" (L154); Bright Smiles programme "since 1991"
    (L152). No acquisition, divestiture, dividend-declaration, buyback-authorisation or
    restructuring-approval date is stated in D09; the Prime100 acquisition appears only through
    footnotes, the acquisition payment (293) (L406) and acquisition-related costs 9.
- Hedged claims: L71 "continues to believe in the growth prospects of the business" (belief
  about the skin health business); L67 "we expect ... to continue in the short term" and "are
  confident that the changes ... will enable us"; guidance conditioned on spot rates and
  tariffs as of January 28, 2026 (L75); boilerplate "may contain forward-looking statements"
  (L164), market share data "may be different" (L160), measures "may not be the same as or
  comparable to" (L170); rounding notes L112, L487, L543, L593, L665, L735, L824, L899.
- Rounded prose beside exact figures:
  - L19 "Returned $2.9 billion in cash to shareholders through dividends and share
    repurchases"; Table 4 shows Dividends paid (1,823) (L417) and Purchases of treasury shares
    (1,210) (L418); the release does not say which lines make up the $2.9 billion.
  - L19 "Net cash provided by operations was a record $4,198" (no unit word in the bullet;
    Table 4 L397 in $ millions).
  - L71 after-tax $794 million vs pre-tax 919 (L218) and tax effect 125 (L701/L861).
  - L17/L41 EPS "declined 25%" / "declined 106%"; L43 "decreased 10 basis points to 60.2%"
    (Table 1 L212 60.2% vs 60.3%); L43 toothpaste share "41.3% year to date", manual toothbrush
    "32.4% year to date"; L79 "approximately 20 basis point impact"; L17 FY "0.7% negative
    impact" and L41 Q4 "0.9% negative impact" from lower private label pet volume.
- Operative definitions, rules and scope exceptions:
  - Base Business L172: "Base Business operating results exclude, as applicable, goodwill and
    intangible assets impairment charges, charges resulting from the ERISA litigation matter and
    the restructuring programs (Strategic Growth and Productivity Program in 2025 and 2022 Global
    Productivity Initiative in 2024) and acquisition-related costs."
  - Organic sales growth L174: "Net sales growth excluding the impact of foreign exchange,
    acquisitions and divestments." Free cash flow before dividends L176: "Net cash provided by
    operations less Capital expenditures."
  - Non-GAAP exclusions in general L180: "such as restructuring charges, charges for certain
    litigation and tax matters, acquisition-related costs, gains and losses from certain
    divestitures and certain other unusual, non-recurring items."
  - Market share L158: dollar value of sales "(excluding Venezuela from all periods)"; L160
    year-to-date shares run "from January 1 of the relevant year" with "a lag time of one or two
    months".
  - Corporate L489: "Corporate operations include costs related to stock options and restricted
    stock units, research and development costs, Corporate overhead costs, restructuring and
    related implementation charges and gains and losses on sales of non-core product lines and
    assets." L491: Q4 2025 Corporate included impairment $919, ERISA $84 and SGPP $13. L493: Q4
    2024 included 2022 GPI $7. L495: FY2025 included impairment $919, ERISA $99, SGPP $13,
    acquisition-related costs $9. L497: FY2024 included 2022 GPI $85.
  - Restructuring note L739/L903: charges "relate to the Strategic Growth and Productivity
    Program in 2025 and the 2022 Global Productivity Initiative in 2024." Tax notes L741/L743
    (repeated L905/L907).
- Amendments or contradictions (within D09, recorded neutrally):
  - ERISA amounts differ by measure: Q4 SG&A (84) (L617) offset by non-service postretirement
    +84 (L660), and no ERISA pre-tax row in Q4 (L699-705); FY operating profit 99 (L801),
    non-service postretirement 34 (L821), pre-tax 65 (L862), cash flow add-back 65 (L383).
  - Impairment per-share effect 0.99 for Q4 (L701) vs 0.98 for FY (L861); same $794 after tax.
  - No stated restatement or recast in D09.
- Coverage: full. Ledger: L1-120, L120-239, L239-398, L398-557, L557-716, L716-875, L875-908
  read (end of file at L908). No unread ranges. Extraction spot-checks against the original:
  Q4 OP row "Total Company, Base Business* $1,108 3% 21.2% -50" (orig L135 = text L137);
  footnote "excludes 1.3 million of incremental common shares" (orig L253 = text L255); Prime100
  footnotes (orig L114/L543/L593 = text L116/L545/L595); Table 1 pipe rows exist in the
  original (orig L205-206). Pipe tables and fenced blocks are in the original file, not added by
  extraction. Page count: not applicable. Visual check of the HTML original: unresolved (only the
  text capture exists); flattened multi-line column headers in Tables 6-9 (e.g. L509-521,
  L679-697) were read by row order and arithmetic consistency.

## D10 - Colgate-Palmolive "Segment Information (Recast)" exhibit (file dated 2026-03-17)

- Source: docs/cl_ex991_2026-03-17.txt | text/D10.txt lines 1-383 (pages not applicable).
  Header "segmentrecast.htm EX-99" (L5), "Exhibit 99" (L9).
- Written or submitted by: Colgate-Palmolive Company (L11, repeated at each block). No people
  or other organisations named.
- Type, date, edition: tables-only exhibit, title "Segment Information (Recast)" (L13; repeated
  L77, L148, L208, L258, L298, L346), "(Dollars in Millions) (Unaudited)". The text holds no
  date, narrative, reason for the recast or effective date (searched "2026", "effective",
  "realign", "Africa/Eurasia", "Middle East": only table rows and the L1 file name). The date
  2026-03-17 comes only from the file name. The recast is explained in D11 (L85; short form
  L120, L398, L453) and D12 (see below).
- Period covered: years ended December 31, 2025 (L17), 2024 (L44-46) and 2023 (L81-83); three
  months ended March 31, 2025 (L152); three months ended June 30, 2025 (L212); six months ended
  June 30, 2025 (L233-235); three months ended September 30, 2025 (L302); nine months ended
  September 30, 2025 (L323). Exclusion facts: no three-month table for the quarter ended
  December 31, 2025, no 2024 or 2023 quarter, and no 2026 period.
- Entities and aliases: reportable segments "Oral, Personal and Home Care" = North America,
  Latin America, "Europe, Middle East & Africa", Asia Pacific; "Pet Nutrition" (the name
  "Hill's" does not appear in D10); "Reconciliation with Total Company Operating Profit
  Corporate". No standalone "Europe" or "Africa/Eurasia" rows (the old D09 names).
- Tables ($ millions; P&L columns Net sales / Cost of Sales / Selling, general and
  administrative expenses / Other (income) expense, net / Operating Profit; Total OP&HC and
  Total rows print only net sales and operating profit; Corporate prints only operating
  profit):
  - FY2025 (L17-42): NA $3,679 $1,510 $1,375 $4 $790; LA 4,776 2,107 1,268 (11) 1,411; EMEA
    4,276 1,572 1,686 80 938; AP 3,038 1,137 1,101 (20) 820; Total OP&HC 15,769 / 3,959 (L30);
    Pet Nutrition 4,613 1,818 1,717 14 1,064 (L32); Corporate (1,717) (L34); Total $20,382 /
    $3,306 (L36). Footnotes: US net sales OP&HC $3,596 (L40), Pet Nutrition $3,062 (L42).
    Reading caution: Pet Nutrition SG&A 1,717 (L32) equals the Corporate figure (1,717) (L34).
  - FY2024 (L44-73): NA $3,716 $1,476 $1,393 $(9) $856; LA 4,782 1,933 1,328 (5) 1,526; EMEA
    4,046 1,511 1,637 85 814; AP 3,074 1,144 1,061 (23) 892; Total OP&HC 15,618 / 4,088 (L61);
    Pet 4,483 1,869 1,641 8 965 (L63); Corporate (784); Total $20,101 / $4,268 (L67). US net
    sales OP&HC $3,640 (L71), Pet $3,059 (L73).
  - FY2023 (L75-110): NA $3,665 $1,489 $1,338 $4 $834; LA 4,640 1,977 1,241 5 1,417; EMEA 3,822
    1,537 1,460 71 754; AP 3,041 1,182 997 (16) 878; Total OP&HC 15,167 / 3,882 (L98); Pet 4,290
    1,964 1,493 26 806 (L100); Corporate (704); Total $19,457 / $3,984 (L104). US net sales
    OP&HC $3,625 (L108), Pet $2,918 (L110, no closing full stop).
  - Capex, years 2025/2024/2023 (L112-129): NA 63/47/45; LA 141/126/146; EMEA 75/80/55; AP
    82/64/65; Total OP&HC 361/317/311; Pet 88/143/301; Corporate 115/101/93; Total
    $564/$561/$705.
  - D&A, years 2025/2024/2023 (L131-144): NA 77/78/79; LA 106/100/98; EMEA 122/119/111; AP
    80/81/84; Total OP&HC 385/378/372; Pet 144/132/101; Corporate 101/95/94; Total
    $630/$605/$567.
  - Q1 2025 (L152-172): NA $904 $358 $350 $— $197 (L160, a tab row outside the pipe table); LA
    1,143 487 316 (7) 348; EMEA 1,007 367 399 18 222; AP 738 275 264 (5) 204; flattened L168:
    Total OP&HC 3,792 / 971, Pet Nutrition 1,118 437 422 1 258, Corporate (153); Total $4,911 /
    $1,076 (L170). Capex (L174-189): NA 16, LA 28, EMEA 11, AP 13, OP&HC 68, Pet 21, Corporate
    35, Total $124. D&A (L191-204): NA 19, LA 24, EMEA 29, AP 20, OP&HC 92, Pet 31, Corporate
    25, Total $148.
  - Q2 2025 (L212-231): NA $919 $380 $349 $3 $187; LA 1,207 527 318 (6) 367; EMEA 1,083 395 428
    19 241; AP 746 284 265 (6) 202; flattened L227: Total OP&HC 3,954 / 997, Pet 1,157 462 430 —
    264, Corporate (181); Total $5,110 / $1,080 (L229).
  - Six months to June 30, 2025 (L233-254): NA $1,823 $737 $700 $3 $384; LA 2,350 1,014 633
    (13) 715; EMEA 2,089 762 827 38 463; AP 1,484 559 529 (11) 407; flattened L250: Total OP&HC
    7,746 / 1,968, Pet 2,275 899 852 1 523, Corporate (334); Total $10,021 / $2,156 (L252).
  - Q2 / 6M capex (L262-277): NA 13/29; LA 21/50; EMEA 15/25; AP 19/32; OP&HC 68/136; Pet
    22/43; Corporate 18/53; Total $108/$232. D&A (L279-294): NA 19/38; LA 27/51; EMEA 30/58; AP
    19/40; OP&HC 95/187; Pet 31/63; Corporate 25/49; Total $151/$299.
  - Q3 2025 (L302-321): NA $922 $381 $342 $(1) $199; LA 1,178 541 303 (2) 337; EMEA 1,115 417
    435 20 243; AP 775 288 280 (6) 213; flattened L317: Total OP&HC 3,989 / 992, Pet 1,142 457
    427 2 255, Corporate (189); Total $5,131 / $1,059 (L319).
  - Nine months to September 30, 2025 (L323-342): NA $2,745 $1,119 $1,042 $2 $583; LA 3,528
    1,555 936 (15) 1,052; EMEA 3,204 1,179 1,261 58 706; AP 2,259 847 809 (17) 620; flattened
    L338: Total OP&HC 11,735 / 2,961, Pet 3,417 1,356 1,280 4 778, Corporate (523); Total
    $15,152 / $3,214 (L340).
  - Q3 / 9M capex (L350-365): NA 17/46; LA 46/96; EMEA 22/46; AP 18/51; OP&HC 103/239; Pet
    21/64; Corporate 31/84; Total $155/$387. D&A (L367-382): NA 20/58; LA 27/78; EMEA 30/89; AP
    20/59; OP&HC 97/284; Pet 35/98; Corporate 26/75; Total $158/$457.
  - Every P&L block carries "Note: Table may not sum due to rounding." (L38, L69, L106, L172,
    L231, L254, L321, L342). Whole $ millions; printed components can differ from printed totals
    by 1 (e.g. Q2 2025 regions sum to 3,955 vs printed 3,954 at L227; Q3 2025 3,990 vs 3,989).
- Lists: each block lists four OP&HC segments, Pet Nutrition and Corporate; no other lists.
- Forecasts, guidance, deadlines, effective dates: none in D10.
- Hedged claims: none (only the rounding notes). Rounded prose: none (no prose).
- Operative definitions, rules and scope exceptions: none printed in D10. What the recast
  changed is stated in D11 L85: "The results of the Europe and Africa/Eurasia (excluding Russia
  and Belarus) reportable operating segments and the skin health business (previously within the
  North America reportable operating segment) have been combined in a new Europe, Middle East &
  Africa reportable operating segment. In conjunction with this realignment, Russia and Belarus,
  which were previously reported within the Africa/Eurasia reportable operating segment, are now
  reported within the Asia Pacific reportable operating segment." Effective "for the quarter
  ended March 31, 2026" (D11 L85). D11 L85 also says recast information "can be found on the
  Company's website" (D10 itself does not say where it was published).
- Amendments or contradictions (recast vs the old structure in D09 Table 5, same periods):
  - FY2025 net sales: NA 4,045 (D09 L460) vs 3,679 (D10 L25); Europe 2,962 + Africa/Eurasia
    1,172 (D09 L462, L464) vs EMEA 4,276 (D10 L27); AP 2,814 (D09 L463) vs 3,038 (D10 L28).
    Unchanged: LA 4,776, Total OP&HC 15,769, Pet Nutrition 4,613, Total 20,382.
  - FY2025 operating profit: NA 784 (D09 L477) vs 790; Europe 748 + Africa/Eurasia 255 (D09
    L479, L481) vs EMEA 938; AP 760 (D09 L480) vs 820. Unchanged: LA 1,411, OP&HC 3,959, Pet
    1,064, Corporate (1,717), Total 3,306.
  - FY2024 net sales: NA 4,113 vs 3,716; Europe 2,770 + Africa/Eurasia 1,095 vs EMEA 4,046; AP
    2,858 vs 3,074. Unchanged: LA 4,782, OP&HC 15,618, Pet 4,483, Total 20,101.
  - FY2024 operating profit: NA 839 vs 856; Europe 658 + Africa/Eurasia 253 vs EMEA 814; AP 812
    vs 892. Unchanged: LA 1,526, OP&HC 4,088, Pet 965, Corporate (784), Total 4,268.
  - D10 adds per-segment Cost of Sales, SG&A and Other (income) expense, US net sales
    footnotes, and segment capex/D&A, none of which D09 Table 5 prints. Capex totals 564/561 and
    D&A totals 630/605 equal D09 Table 4 (L403, L382).
  - FY2023 and Q1-Q3 2025 old-structure figures sit in earlier releases outside this part
    (D05-D08, mapped elsewhere); comparison left to the merge.
  - Later editions in this part that reuse D10's recast comparatives: D11 Table 4 Q1 2025
    column (L369-392) equals D10 Q1 2025 (L160-170) row for row; D12 (see D12 entry).
- Coverage: full. Ledger: L1-150, L150-299, L299-383 read (end of file L383). Spot-checks
  against the original: "Total $ 20,382 $ 3,306" (orig L34 = text L36); footnote "Pet
  Nutrition were $2,918 in 2023" (orig L108 = text L110); the NA $904 tab row outside the pipe
  table is the same in the original (orig L158 = text L160). Page count not applicable; HTML
  original unavailable, so a visual check is unresolved. Flattened rows L168, L227, L250, L317,
  L338 were read by order and checked by arithmetic (segments + Pet - Corporate = Total).

## D11 - Colgate 1st Quarter 2026 results release (May 1, 2026)

- Source: docs/cl_ex991_2026-05-01.txt | text/D11.txt lines 1-586 (pages not applicable).
  Header "q12026pressreleasetables.htm" (L5), "Exhibit 99" (L11).
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL) (L35). Quoted: Noel Wallace,
  Chairman, President and Chief Executive Officer (L35-37). Actor named for the programme
  action: "the Company's Board of Directors" (L39). Mentioned only: Nielsen (L136), the SEC
  (L142).
- Type, date, edition: earnings press release, title "Colgate Announces 1st Quarter 2026
  Results" (L13); dateline "New York, New York, May 1, 2026" (L35); forward-looking statements
  "as of May 1, 2026"; refers to the Form 10-K "for the year ended December 31, 2025" (L142).
- Period covered: first quarter 2026 = "Three Months Ended March 31, 2026 and 2025" (L176,
  L277, L357, L412, L463); balance sheet "As of March 31, 2026, December 31, 2025 and March 31,
  2025" (L235). Labels "1Q 2026", "first quarter 2026", "first three months of 2026" (L15).
  Guidance for full year 2026 (L41). Segment data on the recast structure.
- Entities and aliases: "Strategic Growth and Productivity Program (the "SGPP")" (L39). Divisions
  North America(1), Latin America, Europe, Middle East & Africa(1), Asia Pacific(1), Hill's Pet
  Nutrition (L70-78); "Pet Nutrition" in Table 4 (L374, L390); "Total CP Products" (L439);
  Emerging Markets defined L455; Developed Markets L445. Prime100 (L89, L451, brand list L132).
  Private label pet: "lower private label pet food sales" (L15), "our exit from the private
  label pet food business" (L47). Skin health business and Russia and Belarus (L85 only).
  ERISA litigation matter (L148, L292, L404, L472, L479, L494, L500, L509, L575).
- Tables ($ millions unless noted):
  - L17-23 Q1 GAAP summary: Net Sales $5,324 vs $4,911, +8.4%; EPS (diluted) $0.80 vs $0.85,
    -6%. L25-31 Base Business: Organic +2.9%; Base Business EPS $0.97 vs $0.91, +7%.
  - L57-89 "First Quarter Sales Growth By Division (% change 1Q 2026 vs. 1Q 2025 except % of
    Total Company Sales)" (columns % of sales / Net / Organic / As Reported Volume / Pricing /
    FX): NA 17% -1.8% -2.2% -3.2% +1.0% +0.4% (L70); LA 25% +14.8% +5.4% +2.0% +3.4% +9.5%; EMEA
    21% +11.9% +3.5% +2.2% +1.2% +8.5% (L74, outside fenced blocks); AP 15% +8.9% +5.6% +4.6%
    +1.0% +3.3%; Hill's 22% +6.7% +2.1% +0.2% +3.8% +2.7%; Total Company 100% +8.4% +2.9% +1.1%
    +2.2% +5.1% (L81). L85 recast footnote; L89 Prime100 effect on as reported volume 1.9%
    (Hill's) and 0.4% (Total Company).
  - L91-120 "First Quarter Operating Profit By Division": NA $141 -28% 15.8% -590; LA $401 15%
    30.6% +20; EMEA $266 20% 23.6% +160 (L108); AP $222 9% 27.6% -10; Hill's $280 8% 23.4% +30;
    Total Company As Reported $964 -10% 18.1% -380; Total Company Base Business $1,134 4% 21.3%
    -90 (L116-117).
  - L170-227 Table 1, Q1 income statement 2026/2025: Net sales 5,324/4,911; Cost of sales
    2,098/1,924; Gross profit 3,226/2,987; GP margin 60.6%/60.8% (L188); SG&A 2,076/1,898;
    Other (income) expense, net 186/13; Operating profit 964/1,076; OP margin 18.1%/21.9%;
    Non-service postretirement 26/72; Interest expense 62/66; Interest income 16/15; Income
    before taxes 892/953; Provision 211/227; ETR 23.6%/23.7% (L206); NI incl. NCI 681/726; NCI
    35/36; NI attributable $646/$690; Basic $0.81/$0.85; Diluted $0.80/$0.85; shares basic
    802.3/812.0, diluted 805.1/815.0; Advertising $734/$668 (L227). No impairment line.
  - L229-269 Table 2, balance sheet Mar 31 2026 / Dec 31 2025 / Mar 31 2025: Cash
    1,335/1,288/1,112; Receivables 1,889/1,675/1,725; Inventories 2,086/2,032/2,125; Other
    current assets 772/714/852; PP&E 4,622/4,660/4,416; Goodwill 3,107/3,122/3,334; Other
    intangibles 1,521/1,536/1,782; Other assets 1,278/1,303/1,301; Total assets
    16,610/16,330/16,647; Total debt 7,973/7,988/8,269; Other current liabilities
    5,898/5,736/5,163; Other non-current liabilities 2,253/2,241/2,482; Total liabilities
    16,124/15,965/15,914; CP shareholders' equity 145/54/363; NCI 341/311/370. L263 Debt less
    cash... $6,554/$6,593/$6,958; L264 Working capital % of sales (5.7)%/(7.0)%/(3.3)%. L269
    marketable securities $84/$107/$199 in Other current assets. The Dec 31, 2025 column equals
    D09 Table 3 (D09 L334-349).
  - L271-349 Table 3, Q1 cash flows 2026/2025: Net cash provided by (used in) operations
    747/600 (L306); ERISA litigation matter —/65 (L292); Restructuring and termination benefits,
    net of cash 165/(7) (L293); D&A 156/148; Capex (138)/(124) (L312); financing line flattened
    at L320 (Short-term borrowing 1,138/164; Principal payments on debt (1,082)/(4)); Proceeds
    from issuance of debt —/— (L322); Dividends paid (417)/(406) (L326); Purchases of treasury
    shares (306)/(284) (L327); Proceeds from stock options 127/40; Free cash flow before
    dividends $609/$476 (L344); Income taxes paid $176/$139; Interest paid $96/$109.
  - L351-404 Table 4, Segment Information Q1 2026/2025 (recast): net sales NA(1) 888/904, LA
    1,313/1,143, EMEA(1) 1,126/1,007, AP(1) 804/738, Total OP&HC 4,131/3,792, Pet Nutrition
    1,194/1,118, Total 5,324/4,911 (L369-375); operating profit NA 141/197, LA 401/348, EMEA
    266/222, AP 222/204, Total OP&HC 1,030/971, Pet 280/258, Corporate(2) (346)/(153), Total
    964/1,076 (L385-392). Notes L398-404.
  - L406-455 Table 5, Q1 geographic sales analysis (As Reported / Organic / As Reported Volume /
    Organic Volume / Pricing / FX): Total Company 8.4% 2.9% 1.1% 0.6% 2.2% 5.1% (L430); NA(2)
    (1.8)% (2.2)% (3.2)% (3.2)% 1.0% 0.4% (L432); LA 14.8% 5.4% 2.0% 2.0% 3.4% 9.5%; EMEA(2) 11.9%
    3.5% 2.2% 2.2% 1.2% 8.5%; AP(2) 8.9% 5.6% 4.6% 4.6% 1.0% 3.3%; Total CP Products 8.9% 3.1%
    1.3% 1.3% 1.8% 5.9% (L436-439, pipe rows); Hill's 6.7% 2.1% 0.2% (1.7)% 3.8% 2.7% (L441);
    Emerging Markets 12.9% 6.2% 3.5% 3.5% 2.7% 6.7%; Developed Markets 4.9% 0.2% (0.9)% (1.7)%
    1.9% 3.9%. Note (1) L451 Prime100 0.4% / 1.9% / 0.8% (Total / Hill's / Developed Markets).
  - L457-585 Table 6, Q1 non-GAAP reconciliations: SG&A GAAP 2,076/1,898, SGPP (6)/—, ERISA
    —/(15), non-GAAP 2,071/1,883; SG&A % GAAP 39.0%/38.6% (+40), non-GAAP 38.9%/38.3% (+60)
    (L477-481); Other (income) expense GAAP 186/13, SGPP (165)/—, non-GAAP 21/13; Operating
    profit GAAP 964/1,076 (10)%, SGPP 171/—, ERISA —/15, non-GAAP 1,134/1,091 +4% (L490-496);
    OP margin GAAP 18.1%/21.9% (-380), SGPP 3.2%, ERISA 0.3% (2025), non-GAAP 21.3%/22.2% (-90)
    (L500-502); Non-service postretirement GAAP 26/72, SGPP (5)/—, ERISA —/(50), non-GAAP 20/22
    (L506-510). Continued: 2026 As Reported $892 $211 $681 $35 $646 23.6% $0.80; SGPP 176 37 139
    1 138 (0.4)% 0.17 (L548); Non-GAAP $1,068 $248 $820 $36 $784 23.2% $0.97 (L550). 2025 As
    Reported $953 $227 $726 $36 $690 23.7% $0.85; ERISA 65 12 53 — 53 (0.3)% 0.06; Non-GAAP
    $1,018 $239 $779 $36 $743 23.4% $0.91 (L572-576). No gross-profit reconciliation block in
    D11 Table 6.
- Lists:
  - Brand list L132: identical to D09 L152 (25 brands, same order, last "Tom's of Maine").
  - Base Business exclusions L148: two items (SGPP charges; ERISA litigation matter).
  - Forward-looking conflicts L142: "such as in Ukraine and the Middle East" (Venezuela, listed
    in D09 L166, is absent).
  - Dual-basis measures L156 begin with "Selling, general and administrative expenses"; Gross
    profit and Gross profit margin are not in this list (they are in D09 L180).
- Forecasts, guidance, deadlines, effective dates:
  - Summary bullet L15: "The Company maintained its sales and earnings per share guidance and
    updated its gross profit margin guidance for full year 2026".
  - "Full Year 2026 Guidance" (L41); preface L43: "Based on current spot rates and including the
    estimated impact of tariffs announced and finalized as of April 29, 2026:"
    - Net sales L45: "The Company still expects net sales to be up 2% to 6%, including a
      low-single-digit positive impact from foreign exchange."
    - Organic L47: "The Company still expects organic sales growth to be 1% to 4%. This includes
      the impact from our exit from the private label pet food business." (no basis-point
      figure; D09 L79 said "approximately 20 basis point impact").
    - GAAP L49: "the Company now expects gross profit margin to be down (versus up previously)
      and still expects advertising to be up on both a dollar basis and as a percentage of net
      sales and double-digit earnings per share growth."
    - Base Business L51: "the Company now expects gross profit margin to be down (versus up
      previously) and still expects advertising to be up on both a dollar basis and as a
      percentage of net sales; it also still expects low to mid-single-digit earnings per share
      growth."
    - Exclusion fact: no tax-rate or restructuring-charge item in the guidance bullets.
  - SGPP expansion L39: "on April 30, 2026, the Company's Board of Directors approved an
    expansion of the SGPP"; "The Company still expects substantially all of the charges to be
    incurred by December 31, 2028."; "cumulative pretax charges related to the SGPP, once all
    projects are approved and implemented, are now estimated to be $350 million to $550 million,
    increased from $200 million to $300 million."; "Cumulative pretax savings are projected to be
    $200 million to $300 million, annually, once all projects are approved and implemented." D11
    gives no prior savings figure and no "increased" wording for savings.
  - Recast "effective for the quarter ended March 31, 2026" (L85, L120, L398, L453).
  - Prepared materials "approximately 7:00 a.m. ET today" (L126); call "At 8:00 a.m. ET today"
    (L128; D09 L148 said 8:30 a.m.).
  - Exclusion facts (searched): no annual-meeting sentence (D09 L154 has one), no impairment, no
    acquisition-related costs reconciliation row (the phrase appears only in the general
    exclusions text L156), no dividend declaration, no "Global Productivity" text in D11.
- Hedged claims: L37 "While we expect the volatile macroeconomic conditions and slower category
  growth to continue in 2026"; L39 charges "estimated", savings "projected", "once all projects
  are approved and implemented", "substantially all". Scope of the CEO quote: L35 opens
  "commented on the Base Business first quarter results" before saying "operating profit, net
  income, earnings per share and free cash flow all increased year over year"; GAAP operating
  profit (964 vs 1,076, L194) and GAAP diluted EPS ($0.80 vs $0.85, L218) decreased, while Base
  Business operating profit (1,134 vs 1,091, L496) and EPS ($0.97 vs $0.91, L550/L576)
  increased. L35 "Net sales and organic sales grew in every category and in four of five
  divisions".
- Rounded prose beside exact figures: L15 "Net cash provided by operations was $747 million"
  (L306 747); "GAAP EPS decreased 6% to $0.80" and "Base Business EPS* increased 7% to $0.97"
  (L22, L31); "decreased 20 basis points to 60.6%" (L188 60.6% vs 60.8%); "0.6% negative
  impact from lower private label pet food sales" (L15); toothpaste share "41.1% year to date",
  manual toothbrush "32.6% year to date" (L15); L35 "Gross profit margin increased sequentially
  versus fourth quarter 2025" (Q4 2025 GP margin 60.2% in D09 L43/L212).
- Operative definitions, rules and scope exceptions:
  - Base Business L148: "Base Business operating results exclude, as applicable, charges related
    to the Strategic Growth and Productivity Program and the ERISA litigation matter." (D09 L172
    also listed impairment charges, the 2022 Global Productivity Initiative and
    acquisition-related costs.)
  - Organic L150 and FCF L152: same wording as D09 L174/L176. General exclusions L156 same
    wording as D09 L180 ("such as restructuring charges, ... acquisition-related costs, gains and
    losses from certain divestitures ...").
  - Emerging Markets L455: "Latin America, Asia (excluding Japan), Africa, the Middle East and
    Eastern and Central Europe." (D09 L547/L597: "Latin America, Asia (excluding Japan),
    Africa/Eurasia and Central Europe.")
  - Corporate L400 (same wording as D09 L489). L402: Q1 2026 Corporate included SGPP charges of
    $171. L404: Q1 2025 Corporate included ERISA litigation matter charges of $15.
  - Market share L136-138 (same wording as D09 L158-160).
- Amendments or contradictions (stated changes, neutral):
  - Guidance: gross profit margin from "expansion" (D09 L81, L83) to "down (versus up
    previously)" (D11 L49, L51); net sales, organic, advertising and EPS items "still expects"
    (L45-51). Tariff cut-off date moved from January 28, 2026 (D09 L75) to April 29, 2026 (L43).
  - SGPP charge estimate "increased from $200 million to $300 million" to "$350 million to $550
    million" (L39); completion "still" December 31, 2028.
  - Base Business definition and Emerging Markets definition changed versus D09 (above).
  - SGPP Q1 2026 amounts by line: SG&A 6 (L471), Other (income) expense 165 (L487), non-service
    postretirement 5 (L508); operating-profit level 171 (L494, L402); pre-tax 176 (L548); cash
    flow restructuring line 165 (L293).
  - ERISA Q1 2025 amounts: SG&A 15 (L472), non-service postretirement 50 (L509), pre-tax 65
    (L575), cash flow 65 (L292). D09 shows Q4 2025 ERISA SG&A 84 (D09 L617) and non-service +84
    (D09 L660), and FY2025 ERISA SG&A 99, non-service 34, pre-tax 65 (D09 L774, L821, L862).
  - Q1 2025 comparatives in D11 (Table 1 L184-227; Table 4 L369-392) equal D10's recast Q1 2025
    totals and segment rows (D10 L160-170); D10 prints no Q1 2026 figures.
- Coverage: full. Ledger: L1-130, L130-239, L239-368, L368-497, L497-586 read (end of file
  L586). Spot-checks against the original: recast footnote (orig L83 = text L85); Table 4 row
  "Corporate(2) | (346) | (153)" (orig L389 = text L391); Table 6 SGPP row "176 37 139 1 138
  (0.4)% 0.17" (orig L546 = text L548). Page count not applicable; HTML visual check
  unresolved. Mixed layout: some division rows sit outside fenced/pipe blocks (L74, L108, L432,
  L441-445) and were read in order.

## D12 - Colgate 2nd Quarter 2026 results release (July 31, 2026)

- Source: docs/cl_ex991_2026-07-31.txt | text/D12.txt lines 1-840 (pages not applicable).
  Header "q22026pressreleasetables.htm" (L5), "Exhibit 99" (L11).
- Written or submitted by: Colgate-Palmolive Company (NYSE:CL) (L35). Quoted: Noel Wallace,
  Chairman, President and Chief Executive Officer (L35-39). Mentioned only: Nielsen (L133), the
  SEC (L139). No Board action appears (searched "Board of Directors", "SGPP": no hits).
- Type, date, edition: earnings press release, title "Colgate Announces 2nd Quarter 2026
  Results" (L13); dateline "New York, New York, July 31, 2026" (L35); forward-looking statements
  "as of July 31, 2026"; refers to the Form 10-K "for the year ended December 31, 2025" (L139).
- Period covered: second quarter 2026 = "Three Months Ended June 30, 2026 and 2025" (L173) and
  "Six Months Ended June 30, 2026 and 2025" (L232); balance sheet "As of June 30, 2026, December
  31, 2025 and June 30, 2025" (L294); cash flows six months only (L336; no three-month cash flow
  table). Labels "2Q 2026", "second quarter 2026", "first six months of 2026" (L15). Guidance
  for full year 2026 (L41). Segment data on the recast structure.
- Entities and aliases: divisions North America(1), Latin America, Europe, Middle East &
  Africa(1), Asia Pacific(1), Hill's Pet Nutrition (L70-79). Table 5 labels the pet segment
  "Hill's Pet Nutrition" (L433, L449), whereas D09 Table 5, D10 and D11 Table 4 say "Pet
  Nutrition". "Total CP Products" (L501, L553); Emerging Markets defined L517/L569; Developed
  Markets L507/L559. Prime100 (L87, L513, L565, brand list L129). Private label pet: "lower
  private label pet food sales" (L15), "our exit from the private label pet food business"
  (L47). SGPP appears only by full name ("Strategic Growth and Productivity Program", L139,
  L145, L461, L585 onward). ERISA litigation matter only in 2025 comparatives (L145, L351, L465,
  L715, L724, L743, L750, L761, L826).
- Tables ($ millions unless noted):
  - L17-23 Q2 GAAP summary: Net Sales $5,361 vs $5,110, +4.9%; EPS (diluted) $0.86 vs $0.91,
    -5%. L25-31 Base Business: Organic +2.4%; Base Business EPS $0.99 vs $0.92, +8%.
  - L57-87 "Second Quarter Sales Growth By Division (% change 2Q 2026 vs. 2Q 2025 except % of
    Total Company Sales)", seven columns (% of sales / Net / Organic / As Reported Volume /
    Organic Volume / Pricing / FX; D09 and D11 versions of this table have no Organic Volume
    column): NA 17% -3.0% -3.0% -3.9% -3.9% +0.9% —% (L70); LA 26% +13.7% +5.3% +2.6% +2.6%
    +2.8% +8.4%; EMEA 21% +3.5% +2.0% +3.2% +3.2% -1.2% +1.6% (L76); AP 14% +4.9% +5.2% +4.1%
    +4.1% +1.1% -0.3%; Hill's 22% +3.4% +2.1% -1.2% -1.8% +3.9% +0.6%; Total Company 100% +4.9%
    +2.4% +0.9% +0.8% +1.6% +2.4% (L79). L83 recast footnote; L87 Prime100 effect 0.6% (Hill's)
    and 0.1% (Total Company).
  - L89-117 "Second Quarter Operating Profit By Division": NA $192 3% 21.6% +120; LA $418 14%
    30.4% —; EMEA $263 9% 23.4% +120; AP $209 3% 26.7% -40; Hill's $269 2% 22.5% -40; Total
    Company As Reported $1,016 -6% 19.0% -210; Total Company Base Business $1,145 5% 21.4% +10
    (L113-114).
  - L167-224 Table 1, Q2 income statement 2026/2025: Net sales 5,361/5,110; Cost of sales
    2,065/2,041; Gross profit 3,296/3,069; GP margin 61.5%/60.1% (L185); SG&A 2,130/1,963; Other
    (income) expense, net 150/26; Operating profit 1,016/1,080; OP margin 19.0%/21.1%;
    Non-service postretirement 21/23; Interest expense 62/71; Interest income 17/21; Income
    before taxes 950/1,007; Provision 231/234; ETR 24.3%/23.2% (L203); NI incl. NCI 719/773; NCI
    26/30; NI attributable $693/$743; Basic $0.87/$0.92; Diluted $0.86/$0.91; shares basic
    799.4/810.2, diluted 801.8/813.3; Advertising $777/$678 (L224).
  - L226-286 Table 2, six-month income statement 2026/2025: Net sales 10,686/10,021; Cost of
    sales 4,164/3,965; Gross profit 6,522/6,056; GP margin 61.0%/60.4%; SG&A 4,206/3,861; Other
    (income) expense 336/39; Operating profit 1,980/2,156; OP margin 18.5%/21.5%; Non-service
    postretirement 47/95; Interest expense 124/137; Interest income 33/35; Income before taxes
    1,842/1,959; Provision 441/460; ETR 23.9%/23.5%; NI incl. NCI 1,401/1,499; NCI 62/66; NI
    attributable $1,339/$1,433; Basic $1.67/$1.77; Diluted $1.67/$1.76 (L274); shares basic
    800.8/811.2, diluted 803.4/814.2; Advertising $1,511/$1,346 (L282). Note (1) L286: EPS
    computed independently for each quarter and year-to-date period; quarters may not sum.
  - L288-328 Table 3, balance sheet Jun 30 2026 / Dec 31 2025 / Jun 30 2025: Cash
    1,370/1,288/1,215; Receivables 1,962/1,675/1,773; Inventories 2,181/2,032/2,120; Other
    current assets 795/714/888; PP&E 4,639/4,660/4,529; Goodwill 3,100/3,122/3,696; Other
    intangibles 1,495/1,536/1,904; Other assets 1,248/1,303/1,345; Total assets
    16,790/16,330/17,470; Total debt 7,857/7,988/8,758; Other current liabilities
    6,114/5,736/5,161; Other non-current liabilities 2,253/2,241/2,499; Total liabilities
    16,224/15,965/16,418; CP shareholders' equity 236/54/702; NCI 330/311/350. L322 Debt less
    cash... $6,404/$6,593/$7,346; L323 Working capital % of sales (5.9)%/(7.0)%/(2.9)%. L328
    marketable securities $83/$107/$197. The Dec 31, 2025 column equals D09 Table 3 and D11
    Table 2.
  - L330-408 Table 4, six-month cash flows 2026/2025: Net cash provided by (used in) operations
    1,742/1,484 (L365); ERISA litigation matter —/65 (L351); Restructuring and termination
    benefits, net of cash 232/(13) (L352); D&A 311/299; Capex (266)/(232) (L371); Payment for
    acquisition, net of cash acquired —/(293) (L374); Proceeds from issuance of debt —/497;
    Dividends paid (879)/(880) (L385); Purchases of treasury shares (597)/(516) (L386); Proceeds
    from stock options 138/65; Free cash flow before dividends $1,476/$1,252 (L403); Income
    taxes paid $459/$530; Interest paid $127/$137.
  - L410-465 Table 5, Segment Information, three and six months (columns Q2 2026, Q2 2025, 6M
    2026, 6M 2025): net sales NA(1) 891/919/1,779/1,823; LA 1,372/1,207/2,685/2,350; EMEA(1)
    1,121/1,083/2,247/2,089; AP(1) 782/746/1,586/1,484; Total OP&HC 4,166/3,954/8,297/7,746;
    Hill's Pet Nutrition 1,195/1,157/2,389/2,275; Total 5,361/5,110/10,686/10,021 (L428-434).
    Operating profit NA 192/187/333/384; LA 418/367/819/715; EMEA 263/241/529/463; AP
    209/202/431/407; Total OP&HC 1,082/997/2,112/1,968; Hill's 269/264/549/523; Corporate(2)
    (335)/(181)/(681)/(334); Total 1,016/1,080/1,980/2,156 (L444-451). Notes L457-465.
  - L467-517 Table 6, Q2 geographic sales analysis: Total Company 4.9% 2.4% 0.9% 0.8% 1.6% 2.4%
    (L491); NA (3.0)% (3.0)% (3.9)% (3.9)% 0.9% —%; LA 13.7% 5.3% 2.6% 2.6% 2.8% 8.4%; EMEA 3.5%
    2.0% 3.2% 3.2% (1.2)% 1.6%; AP 4.9% 5.2% 4.1% 4.1% 1.1% (0.3)%; Total CP Products 5.4% 2.4%
    1.5% 1.5% 0.9% 2.9%; Hill's 3.4% 2.1% (1.2)% (1.8)% 3.9% 0.6%; EM 9.2% 4.8% 2.8% 2.8% 1.9%
    4.4%; DM 1.6% 0.5% (0.6)% (0.9)% 1.3% 0.9%. Note (1) L513 Prime100 0.1% / 0.6% / 0.3%
    (Total / Hill's / DM).
  - L519-569 Table 7, six-month geographic sales analysis: Total Company 6.6% 2.6% 1.0% 0.7%
    1.9% 3.8% (L543); NA (2.4)% (2.6)% (3.6)% (3.6)% 0.9% 0.2%; LA 14.3% 5.3% 2.3% 2.3% 3.1%
    8.9%; EMEA 7.5% 2.7% 2.7% 2.7% —% 4.9%; AP 6.9% 5.4% 4.3% 4.3% 1.1% 1.5%; Total CP Products
    7.1% 2.8% 1.4% 1.4% 1.3% 4.4%; Hill's 5.0% 2.1% (0.5)% (1.8)% 3.9% 1.7%; EM 11.0% 5.5% 3.2%
    3.2% 2.3% 5.5%; DM 3.2% 0.4% (0.7)% (1.3)% 1.6% 2.3%. Note (1) L565 Prime100 0.3% / 1.3% /
    0.6%.
  - L571-694 Table 8, Q2 non-GAAP reconciliations: Gross profit GAAP 3,296/3,069, SGPP 2/—,
    non-GAAP 3,297/3,069 (no gross-margin rows); SG&A GAAP 2,130/1,963, SGPP (7), non-GAAP
    2,122/1,963; SG&A % GAAP 39.7%/38.4% (+130), non-GAAP 39.6%/38.4% (+120); Other (income)
    expense GAAP 150/26, SGPP (120), acquisition-related costs —/(9), non-GAAP 30/17; Operating
    profit GAAP 1,016/1,080 (6)%, SGPP 129, acquisition-related —/9, non-GAAP 1,145/1,089 +5%
    (L606-612); OP margin GAAP 19.0%/21.1% (-210), SGPP 2.4%, acquisition-related 0.2% (2025),
    non-GAAP 21.4%/21.3% (+10) (L616). No non-service postretirement block for Q2. Continued:
    2026 As Reported $950 $231 $719 $26 $693 24.3% $0.86; SGPP 129 24 105 1 104 (0.7)% 0.13;
    Non-GAAP $1,079 $255 $824 $27 $797 23.6% $0.99 (L655-657). 2025 As Reported $1,007 $234 $773
    $30 $743 23.2% $0.91; acquisition-related 9 2 7 — 7 —% 0.01; Non-GAAP $1,016 $236 $780 $30
    $750 23.2% $0.92 (L682-686).
  - L696-839 Table 9, six-month non-GAAP reconciliations: Gross profit GAAP 6,522/6,056, SGPP
    2, non-GAAP 6,524/6,056; SG&A GAAP 4,206/3,861, SGPP (13), ERISA —/(15), non-GAAP
    4,194/3,845; SG&A % GAAP 39.4%/38.5% (+90), non-GAAP 39.2%/38.4% (+80); Other (income)
    expense GAAP 336/39, SGPP (285), acquisition-related —/(9), non-GAAP 51/30; Operating profit
    GAAP 1,980/2,156 (8)%, SGPP 300, ERISA —/15, acquisition-related —/9, non-GAAP 2,279/2,181
    +5% (L736-746); OP margin GAAP 18.5%/21.5% (-300), non-GAAP 21.3%/21.8% (-50) (L750-754);
    Non-service postretirement GAAP 47/95, SGPP (5), ERISA —/(50), non-GAAP 41/45 (L758-762).
    Continued: 2026 As Reported $1,842 $441 $1,401 $62 $1,339 23.9% $1.67; SGPP 305 61 244 2 242
    (0.5)% 0.30 (L800); Non-GAAP $2,147 $502 $1,645 $64 $1,581 23.4% $1.97 (L802). 2025 As
    Reported $1,959 $460 $1,499 $66 $1,433 23.5% $1.76; ERISA 65 12 53 — 53 (0.1)% 0.06 (L826);
    acquisition-related 9 2 7 — 7 —% 0.01 (L829); Non-GAAP $2,034 $475 $1,559 $66 $1,493 23.4%
    $1.83 (L831).
- Lists:
  - Brand list L129: identical to D09 L152 and D11 L132 (25 brands, last "Tom's of Maine").
  - Base Business exclusions L145: three items (SGPP charges; ERISA litigation matter;
    acquisition-related costs).
  - Dual-basis measures L153 begin "Gross profit, Selling, general and administrative expenses";
    Gross profit margin is not listed (D09 L180 lists both; D11 L156 lists neither).
  - Forward-looking conflicts L139: "such as in Ukraine and the Middle East".
- Forecasts, guidance, deadlines, effective dates:
  - Summary bullet L15: "The Company maintained its sales and GAAP earnings per share guidance
    and updated its gross profit margin and Base Business earnings per share guidance for full
    year 2026".
  - "Full Year 2026 Guidance" (L41); preface L43: "Based on current spot rates:" (no tariff
    clause, unlike D09 L75 and D11 L43).
    - Net sales L45: "The Company still expects net sales to be up 2% to 6%, including a
      low-single-digit positive impact from foreign exchange."
    - Organic L47: "The Company still expects organic sales growth to be 1% to 4%. This includes
      the impact from our exit from the private label pet food business."
    - GAAP L49: "the Company now expects gross profit margin to be roughly flat (versus down
      previously) and still expects advertising to be up on both a dollar basis and as a
      percentage of net sales and double-digit earnings per share growth."
    - Base Business L51: "the Company now expects gross profit margin to be roughly flat (versus
      down previously) and still expects advertising to be up on both a dollar basis and as a
      percentage of net sales; it also now expects mid-single-digit earnings per share growth
      (versus low- to mid-single-digit growth previously)."
    - Exclusion fact: no tax-rate, restructuring-charge or SGPP-estimate item; D12 does not
      restate the SGPP charge or savings estimates.
  - CEO L37: "a 15% increase in advertising this quarter"; "Strong levels of investment will
    continue in the back half of the year".
  - Recast "effective for the quarter ended March 31, 2026" (L83, L117, L457, L515, L567); L83
    adds "Recast historical geographic segment information can be found on the Company's
    website." D12 does not repeat D11's description of what moved (no "skin health", "Russia" or
    "Belarus" in D12).
  - Prepared materials "approximately 7:00 a.m. ET today" (L123); call "At 8:30 a.m. ET today"
    (L125).
  - Forward-looking basis L139: "These statements are made on the basis of the Company's views
    and assumptions as of July 31, 2026." (D09 L166 and D11 L142 add "except as otherwise noted
    with respect to tariffs"; D12 does not.)
  - Exclusion facts (searched): no annual-meeting sentence, no impairment, no Board action, no
    dividend declaration in D12.
- Hedged claims: L39 "While we expect the volatile market conditions to continue in the balance
  of 2026, we are confident that the strength of our global portfolio and clear business
  strategy should enable us to deliver consistent, compounded earnings per share growth" ("should"
  attaches to enabling EPS growth). Scope of the CEO quote: L35 opens "commented on the Base
  Business second quarter results" before "Gross profit margin, operating profit, operating
  profit margin, net income, earnings per share and free cash flow all increased year over year";
  GAAP operating profit 1,016 vs 1,080 (L191), GAAP OP margin 19.0% vs 21.1% (L193), GAAP net
  income attributable $693 vs $743 (L209) and GAAP diluted EPS $0.86 vs $0.91 (L215) decreased,
  while the Base Business figures increased (L612, L616, L657 vs L686). Free cash flow is printed
  only for six months ($1,476 vs $1,252, L403). L35 "grew in three of four categories and in four
  of five divisions" (no category table exists in D12); L35 "worldwide organic volume growth
  improving sequentially for the third consecutive quarter" (Total Company organic volume 0.8%,
  L79/L491).
- Rounded prose beside exact figures: L15 "Net sales increased 4.9%"; "Organic sales*
  increased 2.4%, including a 0.4% negative impact from lower private label pet food sales";
  "GAAP EPS decreased 5% to $0.86" (L22 -5%); "Base Business EPS* increased 8% to $0.99" (L31
  +8%); "increased 140 basis points to 61.5%" (L185 61.5% vs 60.1%); "Net cash provided by
  operations was $1,742 million for the first six months of 2026" (L365); toothpaste "41.3% year
  to date", manual toothbrush "32.7% year to date"; L37 "15% increase in advertising this
  quarter" (L224 $777 vs $678).
- Operative definitions, rules and scope exceptions:
  - Base Business L145: "Base Business operating results exclude, as applicable, charges related
    to the Strategic Growth and Productivity Program and the ERISA litigation matter and
    acquisition-related costs." (D11 L148 omits acquisition-related costs; D09 L172 also lists
    impairment charges and the 2022 Global Productivity Initiative.)
  - Organic L147, FCF L149, general exclusions L153: same wording as D09/D11.
  - Emerging Markets L517/L569: same wording as D11 L455.
  - Corporate L459 (same wording as D09 L489). L461: Q2 and six months 2026 Corporate included
    SGPP charges "of $129 and $300, respectively." L463: Q2 2025 included acquisition-related
    costs of $9. L465: six months 2025 included ERISA charges of $15 and acquisition-related
    costs of $9.
- Amendments or contradictions (stated changes, neutral):
  - Guidance: gross profit margin "roughly flat (versus down previously)" (L49, L51; D11 L49/L51
    had "down (versus up previously)"; D09 L81/L83 had "expansion"); Base Business EPS "mid-
    single-digit ... (versus low- to mid-single-digit growth previously)" (L51; D09 L83 and D11
    L51 had "low to mid-single-digit"); net sales, organic, advertising and GAAP EPS "still
    expects" (L45-49).
  - Base Business definition again differs from D11 (acquisition-related costs re-added).
  - Q2 2025 and six-month 2025 comparatives (Tables 1, 2, 5) equal D10's recast Q2 2025 (D10
    L222-229) and six-month 2025 (D10 L245-252) totals and segment rows; no figure differs.
  - SGPP amounts: Q2 2026 OP-level 129 (= GP 2 + SG&A 7 + Other 120; L585-610), pre-tax 129
    (L656); six months 2026 OP-level 300 (L742, L461), pre-tax 305 (L800, incl. non-service 5,
    L760); cash flow restructuring line 232 (L352). D11 shows Q1 2026 OP-level 171 and pre-tax
    176 (D11 L494, L548).
  - EPS: six-month diluted $1.67 (L274) vs Q1 $0.80 (D11 L218) and Q2 $0.86 (L215); note L286
    says quarters may not sum to the year-to-date figure.
- Coverage: full. Ledger: L1-110, L110-219, L219-368, L368-517, L517-666, L666-825, L825-840
  read (end of file L840). Spot-checks against the original: footnote "0.6% and 0.1% for Hill's
  Pet Nutrition and Total Company" (orig L85 = text L87); "Total Company, Base Business* $1,145
  5% 21.4% +10" (orig L112 = text L114); Table 5 "Corporate(2) | (335) | (181) | (681) |
  (334)" (orig L448 = text L450). Page count not applicable; HTML visual check unresolved.

## Shared ground for D09-D12 (navigation only; facts and locations)

- Provenance: notes/intake.json lists all twelve documents with "incomplete": false,
  "gap_characters": 0 and "matches_capture": true (capture sha256 ded187b3...). Manifest hashes
  D09 68ee2c32..., D10 17009e17..., D11 ccd8a3c9..., D12 3781d1b1... equal the intake
  source hashes. No gap markers in D09-D12.
- Issuer and people: Colgate-Palmolive Company issues all four. Noel Wallace (Chairman,
  President and CEO) quoted in D09 L63, D11 L35, D12 L35. Board of Directors action only in D11
  L39. Nielsen named in market-share boilerplate D09 L158, D11 L136, D12 L133.
- Segment names by edition: old structure in D09 (North America, Latin America, Europe, Asia
  Pacific, Africa/Eurasia, Hill's Pet Nutrition / "Pet Nutrition"); recast structure in D10, D11,
  D12 (North America, Latin America, "Europe, Middle East & Africa", Asia Pacific, Hill's Pet
  Nutrition / "Pet Nutrition"). Definition of the change: D11 L85 only; effective-quarter
  footnotes D11 L85/L120/L398/L453 and D12 L83/L117/L457/L515/L567; D10 has no explanatory text.
- Recast vs old-structure figures for the same periods (D10 vs earlier releases). FY2025 and
  FY2024 come from D09 Table 5 (full read; see D10 entry). The rest come from a TARGETED GREP of
  segment pipe rows only (D05-D08 are mapped elsewhere and were not read in this part):
  - Q1 2025: D06 L359-384 old NA 998 / Europe 690 / Asia Pacific 690 / Africa/Eurasia 271 net
    sales and OP NA 196 / Europe 172 / AP 198 / Africa/Eurasia 57, vs D10 L160-170 recast NA 904
    / EMEA 1,007 / AP 738 and OP 197 / 222 / 204. Latin America 1,143 / 348, OP&HC 3,792 / 971,
    Pet Nutrition 1,118 / 258, Corporate (153), Total 4,911 / 1,076 are the same in both.
  - Q2 2025 and 6M 2025: D07 L434-459 old NA 1,027 and 2,025, Europe 738 and 1,427, AP 687 and
    1,378, Africa/Eurasia 295 and 566 (net sales); OP NA 194 and 390, Europe 184 and 356, AP 187
    and 385, Africa/Eurasia 65 and 122. Recast D10 L222-252: NA 919 and 1,823, EMEA 1,083 and
    2,089, AP 746 and 1,484; OP NA 187 and 384, EMEA 241 and 463, AP 202 and 407. LA, OP&HC, Pet,
    Corporate and totals equal.
  - Q3 2025 and 9M 2025: D08 L419-444 old NA 999 and 3,024, Europe 801 and 2,228, AP 714 and
    2,092, Africa/Eurasia 297 and 863; OP NA 190 and 580, Europe 209 and 566, AP 188 and 573,
    Africa/Eurasia 68 and 190. Recast D10 L312-340: NA 922 and 2,745, EMEA 1,115 and 3,204, AP
    775 and 2,259; OP NA 199 and 583, EMEA 243 and 706, AP 213 and 620. LA, OP&HC, Pet, Corporate
    and totals equal.
  - FY2023: D05 L457-482 (FY2023 column) old NA 4,091, Europe 2,571, AP 2,782, Africa/Eurasia
    1,083; OP NA 871, Europe 573, AP 767, Africa/Eurasia 254. Recast D10 L93-104: NA 3,665, EMEA
    3,822, AP 3,041; OP NA 834, EMEA 754, AP 878. LA 4,640 / 1,417, OP&HC 15,167 / 3,882, Pet
    4,290 / 806, Corporate (704), Total 19,457 / 3,984 equal.
  - D05 (L457, L459), D06 (L359, L361) and D07 (L434, L436) mark "North America(1)" and
    "Europe(1)" with a footnote; D08 and D09 do not. The footnote text was not read in this
    part (merge item for the D05-D08 mapper).
- Same-period figures repeated across D09-D12 without change: Dec 31, 2025 balance sheet (D09
  L334-349 = D11 L243-258 = D12 L302-317); Q1 2025 totals and segments (D10 L160-170 = D11 L184,
  L194, L369-392); Q2 2025 and 6M 2025 totals and segments (D10 L222-252 = D12 L181, L191,
  L240, L250, L428-451); FY2025 totals (D09 L271, L282 = D10 L36); capex and D&A FY2025/FY2024
  totals (D10 L129, L144 = D09 L403, L382); Q1 2025 capex 124 and D&A 148 (D10 L189, L204 = D11
  L312, L291); 6M 2025 D&A 299 and capex 232 (D10 L294, L277 = D12 L350, L371).
- Guidance edition chain for full year 2026: D09 L73-83 (initial; tariffs as of January 28,
  2026) -> D11 L41-51 (tariffs as of April 29, 2026; GP margin changed to down) -> D12 L41-51
  (spot rates only; GP margin roughly flat; Base Business EPS mid-single-digit). No full-year
  2026 actual exists in D09-D12 (latest period is six months to June 30, 2026). No tax-rate
  guidance in any of the three.
- Definition chains: Base Business (D09 L172 -> D11 L148 -> D12 L145); Emerging Markets (D09
  L547/L597 -> D11 L455 -> D12 L517/L569); dual-basis measure list (D09 L180 -> D11 L156 -> D12
  L153); forward-looking conflict list (D09 L166 with Venezuela -> D11 L142 / D12 L139 without).
- Programmes and charges by period: SGPP charges $13 in Q4 2025 and FY2025 (D09 L491, L495); Q1
  2026 171 OP-level / 176 pre-tax (D11 L402, L494, L548); Q2 2026 129 / 129 (D12 L461, L610,
  L656); six months 2026 300 / 305 (D12 L461, L742, L800). SGPP expansion approved April 30,
  2026, charges estimate $350-$550 million "increased from $200 million to $300 million",
  substantially all by December 31, 2028, savings $200-$300 million annually (D11 L39 only). The
  original SGPP approval and first estimate are not in D09-D12. 2022 Global Productivity
  Initiative: D09 only (2024 charges $7 in Q4, $85 in FY; L493, L497). ERISA litigation matter:
  Q1 2025 SG&A 15, non-service 50, pre-tax 65 (D11 L472, L509, L575); six months 2025 the same
  (D12 L715, L761, L826); Q4 2025 SG&A 84 and non-service +84 (D09 L617, L660); FY2025 SG&A 99,
  non-service 34, pre-tax 65, cash flow 65 (D09 L774, L821, L862, L383).
- Prime100 and acquisition cash: acquisition date not stated in D09-D12. Payment for
  acquisition (293) in FY2025 (D09 L406) and six months 2025 (D12 L374); D11's Q1 2025 investing
  rows (L310-316) contain no acquisition-payment row. Acquisition-related costs $9 in Q2 2025
  (D12 L463), six months 2025 (D12 L465) and FY2025 (D09 L495). Prime100 volume-effect
  footnotes: D09 L116, L545, L595; D11 L89, L451; D12 L87, L513, L565.
- Private label pet: "lower private label pet volume" FY 0.7% / Q4 0.9% (D09 L17, L41); "lower
  private label pet food sales" 0.6% Q1 2026 (D11 L15), 0.4% Q2 2026 (D12 L15); exit named in
  guidance (D09 L79 with "approximately 20 basis point impact"; D11 L47 and D12 L47 without a
  figure). No exit date stated.
- Skin health / Filorga: impairment in Q4 2025 (D09 L69-71, pre-tax 919, after-tax 794);
  goodwill 3,272 -> 3,122 and other intangibles 1,756 -> 1,536 between Dec 31, 2024 and Dec 31,
  2025 (D09 L339-340); skin health moved from North America into EMEA by the recast (D11 L85).
- Narrative passages that repeat table results: headline bullets and summary boxes (D09
  L17-59; D11 L15-31; D12 L15-31) repeat the income-statement and non-GAAP tables; division
  summary tables (D09 L89-140; D11 L57-120; D12 L57-117) repeat the segment and geographic
  tables (D09 Tables 5-7; D11 Tables 4-5; D12 Tables 5-7). Sequential comparisons in prose: D11
  L35 gross margin "increased sequentially versus fourth quarter 2025" (D09 L212 60.2%, D11 L188
  60.6%); D12 L35 organic volume "improving sequentially for the third consecutive quarter"
  (Total Company organic volume D09 L523 (0.5)% for Q4 2025, D11 L430 0.6%, D12 L491 0.8%; the
  Q3 2025 figure is in D08, not read here).
- Market share year to date: toothpaste 41.3% (D09 L43), 41.1% (D11 L15), 41.3% (D12 L15);
  manual toothbrush 32.4%, 32.6%, 32.7% (same lines).
- Call times: 8:30 a.m. ET (D09 L148), 8:00 a.m. ET (D11 L128), 8:30 a.m. ET (D12 L125).
  Annual meeting "Friday, May 8, 2026" only in D09 L154.

## Gaps (this part)

- None in D09-D12 text: every line read (D09 1-908, D10 1-383, D11 1-586, D12 1-840).
- HTML originals are not in the workspace; visual checks of flattened multi-line headers and
  rows (D09 L509-521, L679-697; D10 L168, L227, L250, L317, L338; D11 L320, L432-445; D12
  L493-507) are unresolved and were read by order plus arithmetic.
- D05-D08 were touched only by the targeted segment-row grep above; their footnote (1) text on
  North America/Europe and the Q3 2025 organic volume figure remain for the D05-D08 part.
