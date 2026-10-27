# aq-02505 - document map

Maintained by the caller from `text/` (2026-10-09). Navigation only: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: seven Federal Register texts filed under "Forced Labor Import Enforcement Filings". Three are
  editions of one series (DHS's UFLPA Entity List notices: Nov 25, 2024; Jan 15, 2025; Aug 3, 2026). The other
  four are unrelated rules or notices: DOL H-2B survey-wage NPRM (Nov 2024), NOAA seafood COA NPRM (Dec 2024),
  USTR Section 301 forced-labor determinations (Jun 2026), CBP supply-chain ANPRM (Sep 2026).
- Documents: 7; D01-D07 = page Doc 1-7 (alphabetical file order equals page order; notes/intake.json).
- Gaps: none in the capture ("7 of 7 read in full", 420,965 characters; all sha256 match the capture). The
  source itself omits D05's Annex A (pages 34277-34344 are "[GRAPHIC] [TIFF OMITTED]" product tables), so the
  HTSUS exclusion list is unreadable; it matters only to a question about excluded products. Capture warning
  carried forward: the page said "Docket has been updated. Reload this page so its checks and buttons keep
  working." (documents complete, so no recapture needed for the text).
- Extraction spot-checks: plain-text captures, no pages. Each D0n.txt equals its docs/ file plus a header;
  body start, FR citation line and closing "[FR Doc. ...]" line checked for all seven. Tables: D01 Exhibits 1-4
  are flattened onto single lines (values intact); D05 Annex A omitted at source (above). Footnotes kept inline
  (D01 \1\-\70\, D02/D04/D06 \1\, D07 \1\-\8\). The UFLPA consolidated lists are flattened: some lines hold two
  or three entries (e.g. D02 L172, L188, L189, L194, L198, L236, L240, L243, L248, L252, L276).
- Provenance: notes/intake.json (capture sha256 babbe971..., per-document hashes, matches_capture true).
- Reuse binding: map built from the hashes in notes/intake.json; no earlier bundle shares any document hash.
- Coverage: all seven texts read in full by the caller on 2026-10-09.

## D01 - DOL, Employer-Provided Survey Wage Methodology for the H-2B Program (NPRM)

- 89 FR 90646-90662, Monday, November 18, 2024 (filed 11-15-24); comments due January 17, 2025 (L34).
- Author: DOL Employment and Training Administration; signed José Javier Rodríguez (L691).
- Content: litigation history (CATA I-III, 2011 rule, 2013 IFR, 2015 Wage Rule, Williams v. Walsh Dec 23, 2022);
  proposed 20 CFR 655.10(f): 3 employers / 30 workers minimum, three follow-ups, 14 calendar days open, 24-month
  data age, Form ETA-9165 eliminated. Exhibit 2 (L534): H-2B PWD requests FY2020-2023 (11,629; 14,748; 24,914;
  24,715; avg 19,002) and survey requests (77; 161; 378; 267; avg 221). Exhibits 1/4 costs ($12,850 first year,
  $1,285 undiscounted annual cost, $5,359 savings); prose L514 says $5,466 / $1,285 and fn 63 $4,861 / $3,492
  (internal mismatch). PRA L614-617: 120,042 respondents, 462,470 responses, 211,425 hours, $191,769.
- Links to the rest of the bundle: none substantive (DHS named only as H-2B petition adjudicator).

## D02 - DHS, Notice Regarding the UFLPA Entity List (updated as of November 25, 2024)

- 89 FR 92953-92959, Monday, November 25, 2024. Signed Robert Silvers, Under Secretary (L72).
- Supersedes "the UFLPA Entity List published in the Federal Register on November 1, 2024 (89 FR 87391)" (L77).
- Update: adds five entities to the (ii) list and twenty-five to the (v) list; technical correction removes the
  alias "Xinjiang Nonferrous" from Xinjiang East Hope Nonferrous Metals (i list) (L21, L77-113, L163).
- Additions (ii) L78-82: Western Gold Co.; Western Gold Hami Gold Mine; Western Gold Karamay Hatu Gold Mine;
  Xinjiang Nonferrous Metals Industry Group; Xinjiang Zhonghe. Additions (v) L85-110 (25 names).
- Pre-existing entity among the additions: Xinjiang Daqo New Energy, added to (v) but "first listed on the UFLPA
  Entity List, pursuant to Section 2(d)(2)(B)(i), in June 2022" (L160); it is also on the (i) list (L177).
- "No removals are being made" (L164). Total: "One hundred and seven entities ... are specified" (L165).
- FLETF: seven member agencies, six observer agencies incl. USAID (L42-43).
- Consolidated list L167-294: (i) 9 entries, (ii) 39, (iv) none identified, (v) 72 (counted 2026-10-09).

## D03 - NOAA/NMFS, Seafood Import Procedures and Certification of Admissibility (NPRM)

- 89 FR 102091-102100, Tuesday, December 17, 2024; comments due February 18, 2025 (L31); signed Dec 6, 2024.
- COA for MMPA, Moratorium Protection Act and ATCA restrictions; new 50 CFR part 300 subpart S; COA image
  within 24 hours of CBP release (L68, L353); records 2 years (L87, L358). ANPR July 25, 2022, six comments
  (L122), twelve comment topics answered (Comment 4: forced labor, declined, L129-130). COA used for Mexico
  (vaquita) and New Zealand (Maui dolphin; ban lifted April 2, 2024) (L57-58, L151). RFA: 1,873 firms, 100
  impacted, 98 small; $54,899.77 total; ~$549 per firm; 410 firms (21.6 percent) $92.7M -> $118.2M; $288,292.
- Internal mismatches: L69 cites 300.206, the rule text L328 cites 300.205; L87 "date of the entry" vs L358
  "date of the import".

## D04 - DHS, Notice Regarding the UFLPA Entity List (updated as of January 15, 2025)

- 90 FR 3899-3906, Wednesday, January 15, 2025. Signed Robert Paschall, Acting Under Secretary (L74-75).
- Supersedes the November 25, 2024 list (89 FR 92953) (L80).
- Update: three to (ii) (L81-83), thirty-five to (v) (L85-119), one to both (Xinjiang Zijin Zinc, L121);
  technical correction renames Aksu Huafu Textiles Co. to Aksu Huafu Color Spinning Co., Ltd. (L122-123, L198-201).
- Pre-existing among the 35 (v) additions: Aksu Huafu Color Spinning (on (ii) since June 2022, L198) and
  Xinjiang Habahe Ashele Copper (on D02's (ii) list, L203; not flagged in D04's own text).
- Total: "One hundred and forty-four entities" (L203). 107 + 37 = 144.
- FLETF: six observer agencies incl. USAID (L44).
- Consolidated list L205-373: (i) 9, (ii) 43, (v) 108.

## D05 - USTR, Section 301 determinations on forced-labor import prohibitions (notice, request for comments)

- 91 FR 34272-34345, Friday, June 5, 2026; dockets USTR-2026-0265/0266; signed Jennifer Thornton (L187).
- 60 investigations initiated March 12, 2026 (91 FR 12884, March 17, 2026) (L23, L42); over 450 comments;
  hearings April 28-29, 2026, nearly 60 witnesses (L47). Consultations held with 46 numbered economies (L51-96).
- Determinations: 54 economies failed to impose and enforce (L116); six failed to effectively enforce: Canada,
  Ecuador, EU, Indonesia, Mexico, Pakistan (L117). Proposed rates (L127): 10% for those six, for ART-commitment
  economies (Argentina, Bangladesh, Cambodia, Ecuador, El Salvador, Guatemala, Indonesia, Malaysia, Taiwan) and
  for the UK (partial regime); 12.5% for all others. Dates: requests to appear June 22, written comments July 6,
  hearings July 7, 2026 (L27-29). Annex A omitted at source (L190-475).

## D06 - DHS, Notice Regarding the UFLPA Entity List (updated as of August 3, 2026)

- 91 FR 48913-48920, Monday, August 3, 2026. Signed Robert T. Law, Under Secretary (L71); contact Samuel Greene.
- Supersedes "the UFLPA Entity List published in the Federal Register on January 15, 2025 (90 FR 3899)" (L76).
- Update: "forty-three new entities ..., two of which appear on two separate sub-lists" (L21); four to (ii)
  (L78-81) and forty-one to (v) (L90-133); Xinjiang Nuziline and Xinjiang Tianyun Organic on both. Technical
  corrections: Xinjiang GCL -> Xinjiang Goens Energy Technology (i), Xinjiang Tianmian Foundation Textile ->
  Kuitun Yadasi Textile (ii) (L173-181).
- Total: "One hundred and eighty-seven entities" (L182). 144 + 43 = 187.
- FLETF: five observer agencies; USAID no longer named (L42).
- Consolidated list L184-391: (i) 9, (ii) 47, (v) 149.

## D07 - CBP, Heightened Import Disclosures for Supply Chain Visibility (ANPRM)

- 91 FR 56408-56414, Wednesday, September 2, 2026; comments due December 1, 2026 (L30); docket USCBP-2026-1058.
- Implements E.O. 14411 "Strengthening Customs Enforcement" (signed June 3, 2026; 91 FR 35125, June 10, 2026).
- Entry within 15 calendar days (19 CFR 141.5, L74); informal entry $2,500 or less (L74); CTPAT about 70% small
  businesses (L102); GBI test 2022 (87 FR 74157), four identifiers (D-U-N-S, GLN, LEI, Altana ID) (L196);
  questions Q1-Q64. Signed Susan S. Thomas for Commissioner Rodney S. Scott (L244-247).

## Shared ground (navigation only)

- UFLPA series D02 -> D04 -> D06: each supersedes the one before (D04 L80, D06 L76), so the bundle covers every
  list version from November 25, 2024 to August 3, 2026; D02 names the November 1, 2024 version it replaced.
- Printed totals 107 / 144 / 187 equal distinct entities across the (i), (ii), (v) lists, counting each entity
  once (placements 120 / 160 / 205 minus overlaps). Each notice reprints the whole list, so only the update
  paragraphs, totals, technical corrections and FLETF descriptions are edition-specific.
- Entities on more than one sub-list (Aug 2026): (i)+(v) Baoding LYSZD, Hetian Haolin, Hetian Taida, Hoshine
  and subsidiaries, Xinjiang Daqo, Xinjiang Junggar, XPCC; (ii)+(v) Aksu Huafu, Hefei Bitland, Lop County Hair
  Product Industrial Park, Lop County Meixin, No. 4 VSETC, XPCC, Ashele Copper, Xinjiang Tengxiang, Zijin Zinc,
  Nuziline, Tianyun Organic; XPCC on (i), (ii) and (v).
- Statutes shared: 19 U.S.C. 1307 / section 307 of the Tariff Act (D02, D04, D05, D06); Homeland Security Act
  (D01 116 Stat. 2135, D07 116 Stat. 2142); ACE (D03, D07). No document cites another bundle document except
  the UFLPA supersession chain.
- Fish link: D06 lists a salmon producer (Xinjiang Tianyun Organic); D03's COA covers only MMPA/Moratorium/ATCA.
