# aq-02564 - document map

Maintained by the caller from `text/` (and `docs/` for layout issues).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: "Data Broker Federal Register Filings", seven unrelated Federal Register texts joined by the word
  "broker": two FTC data-broker consent-order notices (Dec 6, 2024), an FMCSA freight-broker compliance-date
  rule (Dec 31, 2024), a CFPB request for information (Jan 15, 2025), two SEC notices of Cboe EDGX/BYX
  small-retail-broker market-data fee programs (Dec 1 and Dec 4, 2025) and an EOIR interim final rule on
  international marriage brokers (Aug 11, 2026).
- Documents: 7; ids from `text/manifest.json`. Local ids are alphabetical by file name, so D01/D02 are
  swapped against the task page: D01 = Doc 2 (Gravy), D02 = Doc 1 (Mobilewalla); D03-D07 = Doc 3-7.
- Gaps: none. Capture says "7 of 7 read in full (405,008 characters)"; every document is plain text and
  matches its captured bytes (notes/intake.json, matches_capture true, gap_characters 0). Capture note:
  "Docket has been updated. Reload this page..." (page-state warning, not a document gap).
- Extraction spot-checks: plain-text sources, extraction is a byte copy plus a header; checked D05 fee
  paragraph and footnote 12, D06 footnote 12, D03 penalty schedule (g)(24), D07 Sec. 68.54 against docs/.
- Provenance: notes/intake.json (capture sha256 ad322a4c...); source hashes there and in text/manifest.json.
- Reuse binding: map written 2026-10-09 against the manifest hashes; refresh only if a hash changes.
- Coverage: all seven documents read in full by the caller on 2026-10-09.

## D02 = Doc 1 - FTC, Mobilewalla Inc.; Analysis of Proposed Consent Order (FR Doc 2024-28745)

- Written by: Federal Trade Commission (Secretary April J. Tabor); statements by Chair Khan (joined by
  Bedoya), Commissioner Ferguson (concurring and dissenting, covers both Gravy and Mobilewalla), Holyoak
  (dissenting).
- Date: FR Dec 6, 2024; comments by Jan 6, 2025 (L25); 30-day comment period; File No. 202 3196.
- Complaint: five counts (L62): sale of sensitive location info, targeting on sensitive characteristics,
  RTB collection, collection without consent verification, retention.
- Order: 1,850-foot radius (L73); ten sensitive-location categories (L78, incl. LGBTQ+ services and
  protest gatherings); Provision VI supplier assessments within 30 days (L80); Provision VII one-year
  look-back (L85); Provision X deletion within 30 days (L85); 20 years (L87).
- "By direction of the Commission, Commissioner Holyoak dissenting." (L90).
- Figures: founded 2008 (L49); 3-5 apps reviewed (L55); RTB "every 30 seconds ... 747 times a day" (L104-105);
  "fifth case ... last 28 months" (L127, fn 7 lists Kochava, X-Mode, InMarket, Gravy).
- Ferguson (L145-252): concurs entirely in two counts against both firms and the Mobilewalla-only RTB count;
  dissents from the sensitive-categorization counts; "doubts" on the retention count. The same statement is
  reprinted in D01 (L375-481), with the count paragraph cites for both complaints.

## D01 = Doc 2 - FTC, Gravy Analytics, Inc. (and Venntel); Analysis of Proposed Consent Order (FR Doc 2024-28738)

- Written by: FTC; statements by Bedoya (joined by Khan, Slaughter in full, Holyoak in Part I), Holyoak
  (concurring, joined by Bedoya in Section I), Ferguson (same joint concurring/dissenting text as D02).
- Date: FR Dec 6, 2024; comments by Jan 6, 2025; File No. 212 3035.
- Complaint: three counts (L55): sale of sensitive location data, collection without consent verification,
  sale of sensitive inferences (Gravy Analytics only).
- Order: eight sensitive-location categories (L63) with national-security/data-security/imminent-harm
  exceptions (L64); Part IV handles LGBTQ+ locations, protests and homes (L66); Part VII assessments within
  30 days (L68); Part X cease collecting within 15 days of withdrawal (L74); Part XI deletion within 30 days
  (L79); Part XIII notify customers who received data within 3 years (L81); 20 years (L82).
- "By direction of the Commission, Commissioner Ferguson dissenting." (L85), while Ferguson's statement says
  his concurrences justify "my vote in favor of submitting the complaints" (L394): an unresolved
  inconsistency, not a usable fact.
- Figures: ~1 billion devices (L123); 1,100 labels (L137); "fourth recent Commission action and third
  settlement" (L155); Carpenter 129 days / seven days, 5 years, three years, 90 days (L191); 17 billion
  signals daily (L256). Holyoak supports Sections II, III, IV, XI and questions VI, VII, IX (L300-325).

## D03 = Doc 3 - FMCSA, Broker and Freight Forwarder Financial Responsibility; Extension of Compliance Date (FR Doc 2024-30509)

- Final rule, effective Dec 31, 2024; compliance date Jan 16, 2025 -> Jan 16, 2026; petitions by Jan 30, 2025
  (L28-34). 2023 rule published Nov 16, 2023, effective Jan 16, 2024 (L122).
- $75,000 financial security floor (L74, L311); 7 calendar days (L149, L311); surety penalty $12,882 per
  violation and 3 years ineligibility (L283-284); < 0.5 percent of brokers (L84).
- NPRM Nov 4, 2024; comments to Nov 19, reopened Nov 21 for 7 days to Nov 29, 2024 (L124-125).
- 13 comments: 9 opposed (NOOA, OOIDA, 7 individuals), 2 supported (First Century Financial, 1 individual),
  1 extension request (SBTC), 1 out of scope (L129).
- UMRA threshold "$200 million (which is the value equivalent of $100 million in 1995, adjusted for inflation
  to 2023 levels)" (L215).

## D04 = Doc 4 - CFPB, RFI on Collection, Use and Monetization of Consumer Payment and Personal Financial Data (FR Doc 2025-00811)

- Notice, FR Jan 15, 2025; comments by Apr 11, 2025 (L27). Director Rohit Chopra.
- Survey figures only (L118-143): 89%, 94%, >75%, 69%, 78% vs 46%, mobile banking 95/90/85/60%, 70% and 72%
  (Atlanta Fed 2023), 20% and 24%.
- Inquiry orders (2021, 2023) to six firms: Block, PayPal, Alphabet, Amazon, Apple, Meta (L150-151);
  "over one thousand data fields", one "tens of thousands" (L158). 15 numbered questions (L193-254).
- Mentions the CFPB's Dec 2024 FCRA data-broker proposal (89 FR 101402, Dec 13, 2024; L89, fn 19).

## D05 = Doc 5 - SEC notice, Cboe EDGX: Small Retail Broker Hosted Solutions Program (FR Doc 2025-21640)

- Written by: the Exchange (Cboe EDGX Exchange, Inc.); SEC Release No. 34-104265, notice dated Nov 25, 2025,
  FR Dec 1, 2025; filed Nov 19, 2025; effective on filing (19(b)(3)(A)); comments by Dec 22, 2025.
- Filing history fn 3 (L42): eight filings May 8 - Nov 19, 2025 (038, 043, 044, 045, 050, 070, 077, 081).
- Existing Small Retail Broker Distribution Program (L48): discounted Distribution Fee $750/month EDGX Top,
  $3,500 Cboe One Summary, Data Consolidation Fee $350 (Cboe One); criteria: broker-dealer to Non-Pro users,
  >= 90% Non-Pro, <= 5,000 Non-Pro users (raised to 10,000, L48 and L81).
- Existing structure for hosts and hosted subscribers (L62): both pay the discounted Distribution Fee; "These
  fees are in addition to the standard Professional and Non-Professional User fees."
- Hosted program (L73-74): host's Distribution Fee credited ($750 EDGX Top) with >= 1 hosted subscriber;
  hosted subscriber's Distribution Fee waived ($750), Consolidation Fee waived (Cboe One, $350), set monthly
  fee $750 EDGX Top / $850 Cboe One in lieu of Non-Pro user fees; Professional User fees unchanged; cap
  10,000 Non-Pro users per firm, counted separately for host and each subscriber.
- fn 12 (L77): "maximum, savings of $250 (10,000 Users x 0.10/Non-Professional User = $1,000 and $1,000-$750 =
  $250) for EDGX Top Data Feed and $1,650 (10,000 Users x 0.25 ...) for Cboe One Summary Feed": the only
  place the per-user rates appear; savings on user fees only (the waived Distribution Fee is not counted).
- fn 13 (L78): host's fees prorated if it joins mid-month; hosted subscriber's fees not prorated.
- Host pays all fees for itself and its hosted subscribers (L70). Host keeps paying the Consolidation Fee (L194).
- NYSE comparison (L90-100): General Access Fee $1,500, Redistribution Fee $1,000, Pro $4, Non-Pro $0.20,
  Per User Access Fee $100, Access Fee "reduced by more than 93%", BQT per-user fees total $850; Release
  No. 90407 (fn 14). EDGX-only paragraphs L160-178 (host as vendor/redistributor; fn 29-30).

## D06 = Doc 6 - SEC notice, Cboe BYX: Small Retail Broker Hosted Solutions Program (FR Doc 2025-21890)

- Same text as D05 with BYX figures (diff in session scratch; summary here). SEC Release No. 34-104279,
  notice dated Dec 1, 2025, FR Dec 4, 2025; filed Nov 19, 2025; comments by Dec 26, 2025.
- Filing history fn 3 (L44): six filings May 8 - Nov 19, 2025 (011, 014, 017, "SR-Cboe-2025-017", 029, 033).
- Existing program (L50): discounted Distribution Fee $250/month BYX Top; Cboe One $3,500 and $350 as in D05.
- Hosted program (L75-76): host credit $250 BYX Top; hosted subscriber waiver $250, set fee $100 BYX Top,
  $850 Cboe One; same 10,000 per-firm cap, same Professional-fee and host-pays rules.
- fn 12 (L79): "maximum, savings of $150 (10,000 Users x 0.025/Non-Professional User = $250 and $250-100 =
  $150) for BYX Top Data Feed and $1,650 ... for Cboe One Summary Feed".
- fn 9 (L58) gives Release No. 88221 for the 2020 BYX program (D05's fn 9 lacks a release number).
- Lacks D05's L160-178 paragraphs; otherwise wording edits only.

## D07 = Doc 7 - DOJ/EOIR interim final rule, Adjudication of Civil Penalties Against International Marriage Brokers (FR Doc 2026-16290)

- FR Aug 11, 2026; effective Sep 10, 2026; comments by Sep 10, 2026 (L28-29). Acting Director Sirce E. Owen.
- IIRIRA (1996) penalty up to $20,000 (L68); IMBRA $5,000-$25,000 per violation (L119, L378), subject to
  inflation adjustment under 28 CFR 85.5 (amounts not given); 8,000-12,000 individuals a year (L76).
- IMBRA vs 274A/274C time limits, side by side: answer 30 + 30 days (L350); motion responses 10 vs 20 days
  (L359); clerical corrections 30 vs 60 days (L379); interlocutory review 30 vs 60 days (L399-401); review
  request 10 vs 20 days (L411-412); briefs 21 vs 40 days (L415-416); CAHO order 30 vs 60 days (L419); final
  agency order 60 days after entry (L380); AG referral within 30 days after the 68.54(d)(1) deadline
  (L427); AG acceptance within 60 days (L433). fn 11 (L147) prints the 274A/274C 30 + 30 = 60 total.
- UMRA "$100 million or more in any one year (adjusted annually for inflation)" (L213).

## Shared ground (navigation only)

- Entities in more than one document: Gravy/Mobilewalla and Commissioners Khan, Bedoya, Slaughter, Holyoak,
  Ferguson (D01, D02); Ferguson's joint statement is printed in both. Cboe EDGX/BYX/BZX/EDGA and NYSE (D05,
  D06). UMRA thresholds in D03 ($200M, 2023-adjusted) and D07 ($100M base).
- Same series/period: D05 and D06 are parallel filings of one program (same filing date Nov 19, 2025, same
  rules); exchange-specific figures differ only for the Top feeds; Cboe One figures are identical in both.
- Cross-references: D02 fn 7 and D01 fn 19 list the FTC's earlier location-data cases (Kochava, X-Mode,
  InMarket). D04 cites the CFPB data-broker proposal (Dec 2024). No document amends another.
- Repeated tables/same-label figures: D05/D06 fn 12 "maximum savings" (user-fee savings at 10,000 users),
  beside the waived Distribution Fee stated in the text; NYSE fee comparison reprinted in both.
