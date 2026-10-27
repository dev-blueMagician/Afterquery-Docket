# aq-05177 - document map

Maintained by the caller from `text/`. Navigation only, like the form's bundle overview: where things
are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: eight RadNet, Inc. earnings-call transcripts (SEC Exhibit 99.2, ViaVid), Q1 2023 to
  Q4 2024. Speakers: Howard Berger (CEO), Mark Stolper (CFO); sell-side analysts in Q&A.
- Documents: 8; Dnn = page Doc n (D01 = Doc 1 ... D08 = Doc 8), `text/manifest.json`.
- Gaps: none. Capture says "8 of 8 read in full (497,297 characters)"; intake shows every document
  `incomplete: false`, `matches_capture: true`. The page carried a stale-page notice ("Docket has been
  updated. Reload this page"); documents were complete.
- Extraction spot-checks: plain-text sources; Dnn.txt equals the captured body plus a header line. No
  tables (bullet lists in D03 only), no footnotes, page numbers inline. Not applicable: PDF pages/charts.
- Provenance: notes/intake.json (capture_sha256 63fe6258...).
- Coverage: all eight read in full by the caller on 2026-10-14 (this session).
- Fiscal year = calendar year throughout.

## Per document (key locations; Lnn = line in Dnn.txt)

- D01 Q1 2023 call (2023-05-11). IC (imaging center) rev 388.4, Adj EBITDA ex-AI 52.7; AI rev 2.1, AI
  EBITDA loss 4.5; total rev 390.6, Adj EBITDA 48.2 (L126-128). Procedures by modality, Q1 23 vs Q1 22
  (L144). Net debt 789.2 incl. NJIN debt 148.1 (L149). Capex 75.7 "includes $19.8 million spent under
  capital leases" (L153). 2023 guidance raised by stated increments, AI "remain unchanged" (L156).
- D02 Q2 2023 call (2023-08-09). IC 401.3 / 63.7; total 403.7 / 60.4 (L108). $246M net equity proceeds
  June 16 (L92). Net cash interest Q2 12.4, "29.9 for that same period last year" (L122; 29.9 equals
  H1 2023 by other figures: transcript label risk). 2023 guidance: revenue +25 low/+10 high, EBITDA +7,
  AI revenue lowered 5 to 11-13, AI loss raised 2 to 11-13 (L135). Medicare 2024 proposal: CF 33.89 to
  32.75, $7-9M hit (L147). 67 PET scanners, 60,000 scans, 255 workdays (L343).
- D03 Q3 2023 call (2023-11-13). IC 399.1 / 60.4; AI 2.9 / -2.5; total 402 / 57.9 (L128). Net cash
  interest Q3 11.7, nine months 41.7 (L171). Net debt 532.7 incl. NJIN 144.4 (L174). Capex 9M 117.9,
  excludes NJIN 13.6, the $19.8M note purchase and $5M software (L178). 2023 guidance (L184-192): FCF
  printed "65-75" though D01 said 65-70 (transcript conflict). Cedars-Sinai JVs (L92); 130 of 366 JV.
- D04 Q4 2023 call (2024-03-05). Q4: IC 415.3 / 68.3, AI 5.1 / -2.5, total 420.4 / 65.8 (L127-129). Q4
  "Cash paid for interest ... excludes ... payments to and from swap counterparties was $5.6 million"
  (L141). FY23: IC 1.604B / 245.1, IC margin 15.3%, total 1.617B / 232.3, AI rev 12.5, AI loss 12.8
  (L143-152); FY net cash interest 38.3 (L158; Q&A L659). Net debt 465.3 incl. "RadNet's ownership
  percentage of NJIN's net debt of $63.2 million" (L161). FY capex 153 (L165). Segment change: eRAD and
  informatics moved from IC to new Digital Health (DH) from Q1 2024; they had 37.1 rev, 20.7 Adj EBITDA
  in 2023; 2023 restated (L167-171). 2024 outlook as growth rates: IC revenue "as much as 8.5%", IC
  EBITDA 11.4%-15.8%, DH revenue 21%-41%, DH EBITDA 51%-77% (L173-179). Q&A: EBITDA "$250 million to
  $260 million" (L345-347), DH revenue "$60 million to $70 million" (L356), analyst "8% to 8.5%"
  (L475) and CFO "8.5-plus percent" (L484); HMI Houston 7 centers ~$30M (L88, L576).
- D05 Q1 2024 call (2024-05-13). Total 431.7 / 58.5; IC 417 / 54.9 (+37.6, +6.8); DH 14.7 / 3.5; AI 4.7
  (L108-113). Net cash interest 10.5 vs 17.5 (L127). Net debt 317.1 incl. NJIN debt 142.5 (L130). 2024
  guidance increments: IC revenue +25 both ends (no range printed), IC EBITDA to 255-265, capex +5, cash
  interest -3 to 37-42, FCF +3 to 68-78, DH EBITDA +1 to 13-15, R&D +1 to 12-14 (L138-143). Medicare
  CAA: 1.72% of 3.4% cut removed from March 9; +$3.4M (L147). $219M net offering proceeds (L93).
- D06 Q2 2024 call (2024-08-09). Total 459.7 / 72.3; IC 443.9 / 69.1; DH 15.8 / 3.3; AI 5.6, typo "second
  quarter of 2023" (L113-119). Net cash interest 3.8 vs 12.4 (L134). Net debt 301.6 incl. NJIN debt 140.6
  and NJIN cash 86.5 (L137). 2024 guidance: revenue +10 both ends to "$1.685,000,000 to $1,735,000,000";
  EBITDA +2 "to $257 million to $260 million" (sic); capex +5 to 135-145; cash interest -5 to 32-37; FCF +4
  "to $72 million to $80 million" (sic) (L149). Medicare 2025 proposal CF 33.29 to 32.36 (L159). eRAD
  "about $37 million of revenue and $20 million of EBITDA" (L460).
- D07 Q3 2024 call (2024-11-12). Total 461.1 / 73.7; IC 452.4 / 70.4 (IC + DH revenue do not sum to
  total: transcript risk); DH 16.4 / 3.2; AI 5.1, typo "third quarter of 2023" (L116-119). Net cash
  interest 4.3 vs 11.7 (L136). Net debt 261 on a 49% NJIN basis, prior year re-based to 498.3 (L139-140).
  2024 guidance: revenue 1.71-1.76B, IC EBITDA "262 to 270", capex 145-155, cash interest 25-30, FCF 83-93
  (L151-155). Q2 AI had a $600K implementation fee (L316).
- D08 Q4 2024 call (2025-03-05). Q4 only: total 477.1 / 75.0; DH 18.9 / 4.5 (L82-85); AI 6.5 then
  corrected to 6.7 (L342-357, L437). No FY 2024 totals, no Q4 IC figures, no interest figures. Nine de
  novos in 2024 (L95); 153 of 398 JV (L97). Net debt 268.8 incl. ownership % of NJIN net debt 41.4
  (L143). $230M stock offering (L111). 2025 weather/wildfire hit $22M revenue / $15M EBITDA (L157).

## Shared ground (navigation only)

- Forecast/actual pairs: 2023 guidance (D01-D03) vs FY23 (D04); 2024 guidance (D04 rates, D05-D07
  increments/ranges) vs quarterly 2024 actuals (D05-D08, no FY sum printed).
- Restated comparatives: 2024 calls compare IC/DH with 2023 restated for the eRAD move; D04 gives the
  annual eRAD figures. Quarterly restated IC EBITDA bases (from 2024 increments) sum to ~225.8, not
  D04's 245.1 - 20.7 = 224.4 (inconsistent; avoid restated EBITDA). DH revenue restatement is consistent.
- Net cash interest series (net of swaps and interest income): Q1-Q3 2023 in D05-D07 comparatives, Q2
  and Q3 2023 in D02/D03, 9M 2023 in D03, FY 2023 in D04, Q1-Q3 2024 in D05-D07; Q4 2023 and Q4 2024
  never printed on that basis (D04 Q4 figure is gross of swaps and interest income).
- Net debt basis for NJIN changes by call (100% of NJIN debt/cash vs 49% share).
- Transcript errors to avoid: D02 L122 label; D06 EBITDA/FCF ranges; D07 IC revenue; D06/D07 AI-revenue
  year typos; D03 FCF range; D05 "450 cancers" vs D03 "over 500"; de novo counts (D06 5 vs 3).
