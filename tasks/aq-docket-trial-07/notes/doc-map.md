# aq-docket-trial-07 - document map

Navigation only; questions quote `text/Dnn.txt`, never this map. Full per-document maps (bundle-mapper
subagents, 2026-10-06, full read of every captured line, ledgers inside) are in `notes/map/Dnn.md`.
This file is the caller's merge: bundle facts, per-document summary and shared ground.

## Bundle

- What it is: seven unrelated 2021 BLS Monthly Labor Review articles (platform bundle "Surveys and
  polls"). No article cites another; no shared states, companies or people except cited authors
  Dey and Loewenstein (D06 note 7, D07 note 2; different works).
- Documents (local id = platform Doc): D01 = Doc 3 Indian Country (Payson, Nov 2021); D02 = Doc 2
  Consumer Expenditure Surveys data quality (Nov 2021); D03 = Doc 1 BED by wage class (Sadeghi and
  Cooksey, Dec 2021); D04 = Doc 5 rail employment Nov 2018-Dec 2020 (Ansell, Oct 2021); D05 = Doc 4
  Midwest manufacturing 1990-2019 (Arden and DeCarlo, Nov 2021); D06 = Doc 6 EP/O*NET mapping
  (Hopson, Aug 2021); D07 = Doc 7 nonstandard schedules in 29 European countries (Gracia, Han, Li,
  Jul 2021). Local ids are alphabetical by file name; form fields must use the platform Doc numbers.
- Gaps: every document lacks only its page header before the date line (D01 973, D02 1,488, D03
  1,452, D04 970, D05 1,408, D06 1,310, D07 3,086 characters) and a 34-character tail. The capture
  marks both (`[... N characters not captured ...]`, text line 3 and the last line); head + tail
  equals each shortfall exactly (checked by script). `tools` labels them "unlocated omitted range"
  because the splitter does not parse the U+2026 marker; the location is nevertheless printed.
  Authorship rests on the suggested-citation line in each document. No body text is missing.
- Extraction spot-checks: plain-text sources (no pages). Mappers compared tables, footnotes and both
  gap markers with `docs/` originals for every document; identical except "…" -> "..." (NFKC).
- Provenance: notes/intake.json (capture sha256 b8aa2366...c33d; all seven docs incomplete only at
  the edges; matches_capture true).

## Per-document summary (details in notes/map/Dnn.md)

- D01 (Doc 3): Table 1 CPS 2016-18 AIAN-AOIC labor force (5,086K; 939K = 18.5% in AIAN areas;
  unemployment 10.9% vs 6.6%; no Total-column rate printed); Table 2 nine Indian Country domains
  (GL, GS, GC, PW geographic; PT, PA, PC population; LT, LM ownership); Table 3 QCEW tribal
  establishments Q4 2017 (334.5K employment Dec 2017; casinos 168.0K = 50.2%, sub-row of leisure and
  hospitality; tribal government 110.4K sub-row of public administration); Meister 296,000 (2020),
  "76.2 percent higher"; 695 / 582 / 113 / 75 tribal-area counts; April 6, 2017 LFR amendment.
- D02 (Doc 2): Table 1 nine rows for "eight" agencies (Census twice); CE component per use
  (Interview: DOD, DOS, SPM; integrated: CMS, IRS sales tax); thresholds OMB response rate < 80%,
  DOD CONUS COLA > 8%, DOS post allowance >= 3% above Washington; data spans 2, 3, 5 years and prior
  12 months; CPI 7,776 = 243 x 32; ~70 expenditure classes; TPOPS timing conflict (2018 vs 2019).
- D03 (Doc 1): QCEW/BED quarterly Q3 1992-Q1 2020; wage classes by establishment-wage quartiles,
  re-ranked every quarter; Charts 1-9 and Tables A-1/A-2 (full values in map). Prose vs data
  conflicts: Q1 2020 high-paying net "47,000" vs -37 (chart and table); Q1 2019 cutoffs $346/$1,138
  vs 354.7/1,164.9; prose "33.8 percent in 2019" and "52.5" are the 2020 rows (2019: 33.2, 53.1);
  1992 ratio 2.89 vs 2.88; "consistently" vs 11 quarters below 1.00. Fn 8 NBER Feb-Apr 2020.
- D04 (Doc 5): CES rail Jan 1980-Dec 2020 SA (Nov 2018 184.1, Dec 2020 144.5, series min Nov 2020
  143.3); Chart 2 OTM changes = differences of Chart 1; Chart 3 coal carload OTM % 2016-2020; Chart 4
  STB Class I by six occupations (Nov 2018 148,981 -> Dec 2020 117,770 = 31,211; T&E 45.5% of loss;
  T&E low Jun 2020); Chart 5 carloads; Table 1 T&W composition Nov 2018. Prose vs data: coal "April
  and May 2020" largest declines vs Apr -12.7, Feb -9.0, Mar -8.9, May -8.2; carloads "began to
  increase again in May" vs May low; "declined consistently throughout 2019" vs Jan +200; "between 3
  and 15 percent" vs 2.81%; CES 40,000 vs STB 31,000 (different universes).
- D05 (Doc 4): CES Midwest manufacturing monthly SA 1990-2019 (max May 1998 5,508.7; min Dec 2009
  3,528.4); durable/nondurable Chart 5 (Chart 1 total != Chart 5 sum, e.g. Dec 2019 4,083.7 vs
  4,130.5); state Charts 2-4 for 1990 and 2019 (shares, location quotients, levels); prose vs data:
  "Through the end of 2000 ... roughly 278,000 (5.4 percent)" fits Dec 1999 (Dec 2000 = +176.4);
  "bottomed out in February 2010" vs Dec 2009 min; "17.1-percent increase" = rounded 4.1/3.5 (data
  15.7%); small-state gains (+4,300 etc.) vs Chart 4 (+7.0K etc.); "Six states" vs note 12's seven.
- D06 (Doc 6): Table 1 taxonomy timeline 1998-2022; Table 2 mapping types (Match 698/698/87.4;
  subset rows "with residual"; totals 790 / 923 / 100.0); Steps 1-3; Tables 3-5 weights (Table 5
  printed total 841.3 vs sum 839.3); OEWS semiannual panels, six combined, 2018 SOC from the November
  2018 panel, hybrid estimates May 2019 and May 2020.
- D07 (Doc 7): EWCS 2005/2010/2015, 93,879 workers, five regions (L23 membership); Chart 1 country
  percentages (one decimal); Table 2 pooled region integers; Chart 2 adjusted region-by-year; Charts
  3-4 and Tables 3-6. Prose vs data: Cyprus labelled Central-Eastern at L69 but Southern at L23;
  Germany 35.3 omitted from the "nine countries ... 35 to 40 percent"; Greece "56" vs 58.1; Table 3
  vs prose significance; Table 5 direction note. Note 12: NBER Dec 2007-Jun 2009; 2010 = recession
  year.

## Shared ground (navigation only)

- Time series overlap: D04 Chart 1 (rail, monthly 1980-2020) and D05 Charts 1/5 (Midwest
  manufacturing, monthly 1990-2019) share every month Jan 1990-Dec 2019 (value table at the end of
  notes/map/D05.md); D04 Charts 2-5 overlap D05 for 2018-2019; D03 quarterly Q3 1992-Q1 2020 (BED
  uses third-month employment, D03 L19) overlaps both; D03 Q1 annual series 1993-2020.
- Recession dating: D03 fn 8 (NBER, Feb-Apr 2020); D05 L1465 (2001 recession ends Nov 2001; Dec 2007
  peak; Jun 2009 trough; no dating body named); D07 note 12 (NBER Dec 2007-Jun 2009; 2010 treated as
  a recession year). D04 dates COVID events (Mar 13, 15, 26, Apr 20, end of May 2020) but no cycle.
- BLS programs: QCEW (D03; D01 Table 3 tribal establishments); CES (D04, D05; D03 says QCEW
  benchmarks CES and OEWS); OEWS (D06); CPS (D01); CE (D02); BEA NIPA input from CE (D02) and QCEW
  (D03); BEA I-O accounts used by D05 note 11 and fed by CE (D02).
- Manufacturing: D05 throughout; D04 L3010 (freight demand from manufacturing hit by 2019 U.S.-China
  disputes); D01 Table 3 "other private industry" includes manufacturing; D06 L351 (OEWS began in
  1971 as a manufacturing survey).
- "Midwest": D05 region (12 Census states); D04 Chart 3 note and fn 6 (March-April 2019 flooding,
  "probably").
- No forecast/actual pairs, editions, amendments across documents, or cross-citations.
