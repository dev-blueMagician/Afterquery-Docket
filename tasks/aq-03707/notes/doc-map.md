# aq-03707 - document map

Navigation only, written by the caller from `text/` on 2026-10-12. Questions quote the documents, never this map.

## Bundle

- What it is: the NZ Commerce Commission's grocery market study, round 3: the final report's executive summary
  and twelve post-conference submissions (November to December 2021) on the draft report of 29 July 2021.
- Documents: 13. Local ids are alphabetical by file name and differ from the task page's Doc numbers:

| Local | Doc | Who wrote it | What it is | Chars |
| --- | --- | --- | --- | --- |
| D08 | 1 | Commerce Commission | Final report, executive summary (14 recommendations) | 51,963 |
| D01 | 2 | Consumer NZ | Cross submission, 18 November 2021 | 7,812 |
| D02 | 3 | Coriolis Ltd (Tim Morris) | Submission with six exhibits (US store formats, Texas prices) | 37,390 |
| D07 | 4 | Kore Hiakai Zero Hunger Collective | Submission, 23 November 2021 | 7,668 |
| D09 | 5 | Monopoly Watch NZ | Post-conference commentary | 41,998 |
| D10 | 6 | Ngati Porou Holding Company | Submission, 23 November 2021 | 14,353 |
| D11 | 7 | Northelia | Final submission, November 2021 | 67,937 |
| D12 | 8 | NZ Food & Grocery Council (NZFGC) | Post-conference submission, 25 November 2021, with Attachment A (AU and UK codes side by side) | 164,306 |
| D13 | 9 | The New Zealand Initiative | Submission, 18 November 2021 | 21,218 |
| D06 | 10 | Frugl Group | "Fair Fare NZ" introduction (slide text) | 10,154 |
| D03 | 11 | Incenta Economic Consulting, for Foodstuffs | Profitability report, December 2021 | 36,292 |
| D05 | 12 | HoustonKemp, for Foodstuffs | International price comparisons, further report, 3 December 2021 | 28,754 |
| D04 | 13 | HoustonKemp, for Foodstuffs | Private label products report, 3 December 2021 | 43,431 |

- Gaps: none. `notes/intake.json`: all 13 complete, each matches the capture. Capture note carried forward: the
  page said "Docket has been updated. Reload this page so its checks and buttons keep working."
- Extraction spot-checks: plain-text captures, so text/ equals docs/ plus a header line (character counts differ
  by the header only). Checked against the capture: Doc 11's Table 1 (rows 25 to 31 keep tab-separated columns;
  rows 10 to 23 lose their column positions), Doc 3's Exhibit 2 (rows wrap, "1.394 sqm" is printed for 1,394),
  Doc 6's income table (four rows, footnote marks in brackets), Doc 8's footnotes (inline, numbered to 135).
  Charts and schematics are absent as text (Doc 10's solution schematic, Doc 3's Exhibits 4 to 6 keep only labels).
- Reuse binding: source hashes in `text/manifest.json` and `notes/intake.json` (capture
  19407e9aac5d542d352c472ee0d007954e779ab2bbaa2550e0a6f9d895566b03). Not a repeat bundle: 548 earlier source
  hashes in 10.6, 10.7 and 10.8 searched, none equal. Nearest family: aq-03557 (round 1 of the same study).
- Coverage: all 13 read in full by the caller.

## Where the figures are

- Doc 1 (D08): l38 $22 billion (year to September 2021), $234 a week (year to June 2019); l79-83 store counts
  (more than 180 Countdown, 71 SuperValue and FreshChoice, more than 400 Foodstuffs); l149 covenants; l172 ROACE
  2015 to 2019 (12.7% Woolworths NZ, 12.8% Foodstuffs SI, 13.1% Foodstuffs NI); l174 normal return 5.5% (WACC);
  l178-180 what changed since the draft (Foodstuffs on a whole of business basis with store property; Woolworths
  NZ with right of use assets for leased property); l195 fifth most expensive in the OECD in 2017, 66% market
  exchange rates and 34% PPP; l299 code based on the Australian code; l387-402 the 14 recommendations.
- Doc 2 (D01): surveys of 1030 (February 2021) and 1002 (November 2020); $2000 and $2100 per $15 voucher.
- Doc 3 (D02): Exhibit 1 format definitions (l91-128), Exhibit 2 US metrics (l130-170), Exhibit 3 NZ presence
  (l172-214); 27% cap strawman by January 1, 2024 (l265); Woolworths ca 45% of scan, ca 18% to divest (l280);
  four-player markets (l287); Texas price exhibits (l311-330).
- Doc 4 (D07): food stress above 30% of income (l15-17).
- Doc 5 (D09): 15% share, about $3.2bn, seven cities, $500m to $1bn (l96-98); "Even Aussie is a 4-player
  market" (l89); 150 to 175 supermarkets (l333); Woolworths NZ 10% of revenue, 13% of free cash flow (l239).
- Doc 6 (D10): Kaiti income table (l77-84), 240-kilometre trip (l85).
- Doc 7 (D11): $22bn, $18bn, $3.5bn, 150 to 175 stores, 15% (l136, l159-175, l402, l474); internally
  inconsistent on separation periods, SMP thresholds and HHI radii.
- Doc 8 (D12): conference quotes with speakers in footnotes 4 to 51; Castalia's four-chain countries (l256,
  l381); acquisitions list (l404); cost of goods shares 77.8%, 77.6%, 76% and the 24.4% footnote (l702, l719);
  FSNI $7.5b, NPAT margins 4% and 2.4% (l689-690); private label 13.8% to 14.2% (l834); Attachment A from l966.
- Doc 9 (D13): six named would-be entrants (l97); 2000 and 4000 square metre stores (l72).
- Doc 11 (D03): Table 1 (l95-144); option (a) leased assets included, option (b) levered benchmark (l152-171);
  overseas ranges 9 to 11 and 22 to 25 per cent (l159, l162); benchmarks need matching leverage (l277);
  NZX50 ownership and sector ROACEs (l282, l310-316); Deloitte margins, Tesco and Kroger (l322-342).
- Doc 12 (D05): draft's "top 10 ... out of all 38 OECD countries" (l30); conference Day 4, 27 October 2021.
- Doc 13 (D04): private label 15 and 10 per cent in 2020, UK 52 per cent (l272); almost ten per cent in 2000
  (l302); pass-through ranges (l320-322).

## Shared ground (navigation only)

- Draft against final: Docs 2 to 13 answer the draft; Doc 1 is the final report. Doc 1 l176-180 says how the
  profitability method changed; Doc 11 l72 records what the Commission said at the conference it intended.
- Third parties quoted by more than one document: Castalia (Docs 8, 13), Deloitte's retail report (Docs 8, 11),
  Coriolis's older papers (Doc 13; Coriolis itself wrote Doc 3), The Warehouse (Docs 3, 5, 7, 8), Night 'n Day
  (Docs 5, 7, 8), Aldi and Costco (Docs 1, 3, 8, 9), Tex Edwards (Docs 3, 5, 8, 9; Northelia is Doc 7).
- Same text in two documents: Docs 5 and 7 share the Fels appendix, the Bagrie quotes and three key points.
- No series is quoted for different periods by two documents (no first-half / full-year pair).
