# aq-04807 - document map

Maintained by the caller from `text/`. Navigation only; questions quote the documents, never this map.

## Bundle

- What it is: AQ-04807 "Ozone Nonattainment Area Determinations": seven EPA Federal Register proposed rules
  (2023-2026). Six concern ozone areas (five under the 2015 standard, one under the 1997 standard); one
  (D01) is a PM10 maintenance plan.
- Documents: 7; local D01-D07 = page Doc 1-7 (same order, by file name).
- Gaps: D07 tables 1-4 are omitted images ("[GRAPHIC] [TIFF OMITTED] TP30AP26.004-.007"): no NWF
  per-monitor DVs, FDVadj or FDVadj-atyp values in the text. Everything else is text.
- Extraction: plain-text captures; capture says "7 of 7 read in full"; intake.json shows no gaps; text
  matches docs byte for byte apart from the header line. Capture carried "Docket has been updated.
  Reload this page so its checks and buttons keep working."
- Provenance: notes/intake.json (capture_sha256 57445872...). Repeat check 2026-10-14: no source hash or
  file name shared with any bundle in 10.6, 10.7 or 10.8.
- Coverage: all seven texts read in full by the caller, 2026-10-14.

## D01 - Sacramento County second 10-year PM10 maintenance plan (EPA Region IX, proposed)

- FR 2023-20555, published Friday September 22, 2023; comments by October 23, 2023; signed Sept 18, 2023
  by Martha Guzman Aceves.
- PM10 24-hour standard 150 ug/m3; exceedance = value above 150 after rounding to nearest 10 (154 no, 155
  yes; fn 6); expected-exceedance rate compared rounded to nearest tenth (1.05 -> 1.1; fn 7).
- Table 1/4 monitor DVs 2011-2022 with and without the 2018 events; Table 2: 13 exceedances Nov 10-12 and
  14-16, 2018 (two rows are the collocated Del Paso Manor POC 2, not used for NAAQS comparison); Table 3:
  2020 exceedances (8 rows; text "a total of seven recorded exceedances").
- EE: CARB submitted April 26, 2021; EPA concurrence "August 1, 2022" (summary) vs letter dated July 27,
  2022 (fn 26).
- Tables 5-6 inventories 2017/2024/2027/2033 (PM10 total 33.58/33.78/35.15/36.43; NOx 35.84/23.57/
  "21,96"/20.08 tpd); Table 7 rollback (149/142/144/146); Table 8 budgets (NOx 11.2/9.6/8.4, PM10
  14.7/15.4/16.4; "rounded up to the nearest tenth", 0.5 tpd NOx safety margin in 2024 only).
- Contingency trigger: exceedances averaged over three years greater than 1.05.

## D02 - Washington, DC-MD-VA: determination of attainment by Aug 3, 2024 + re-proposed CDD (Region III)

- FR 2024-26423, Nov 15, 2024; comments by Dec 16, 2024; contact Ian Neiswinter; signed Adam Ortiz.
- "Effective August 3, 2018 ... designated 52 areas"; Marginal date Aug 3, 2021; 22 Marginal areas failed
  (effective Nov 7, 2022); Moderate date Aug 3, 2024.
- EE: DOEE (for DC) submitted March 20, 2024; EPA concurred July 17, 2024 on McMillan (110010043) June 29,
  2023; fn 8: DC also requested June 1-2, 2023, deferred "due to a lack of regulatory significance".
- Feb 1, 2023 CDD proposal (2019-2021 data) not finalized: monitored violation (fn 4, preliminary data).
- Truncation rule fn 10; completeness rule (90% average, 75% minimum) and Takoma (110010050) gaps.
- Table 1 completeness; Table 2 fourth-highest values 2019-2023 for 14 monitors; Table 3 DVs 2019-21,
  2020-22, 2021-23 (McMillan 0.070 in 2021-23 = (0.072+0.066+0.072)/3).

## D03 - Coachella Valley: one-year extension of the 1997-standard Extreme date (Region IX)

- FR 2025-04035, March 17, 2025; comments by April 16, 2025; signed Cheree D. Peterson (acting) March 4.
- 1997 standard 0.08 ppm; misprint "once more to 0.70 ppm" for the 2015 revision (line 99).
- Timeline: designated eff. June 15, 2004; Serious (June 15, 2013); Severe-15 eff. June 4, 2010 (June 15,
  2019); Extreme (June 15, 2024); proposed extension to June 15, 2025.
- Extension test (1997 std): attainment-year fourth-highest at the "design value monitor" 0.084 ppm or
  less (40 CFR 51.907); at most two one-year extensions.
- EE: CARB submitted Oct 11, 2024 (Palm Springs--Fire Station, July 14-15, 2023; Highland, Rabbit, Reche
  fires); EPA concurred Dec 10, 2024. 2023 DV 0.085; 2023 fourth-highest 0.083 after exclusion.
- Table 1: Palm Springs 0.083, Joshua Tree NP 0.071, Indio N/A ("Two ozone monitoring sites were located
  in the Coachella Valley in 2023").

## D04 - Phoenix-Mesa: attainment by Aug 3, 2024 but for international emissions (CAA 179B(b)) (Region IX)

- FR 2025-20357, Nov 19, 2025; comments by Dec 19, 2025; signed Michael Martucci (acting) Nov 13, 2025.
- "Effective on August 3, 2018, the EPA designated 51 areas" + fn 7 San Antonio effective Sept 24, 2018.
- fn 19: DVs greater than 0.070 ppm valid regardless of completeness; "attainment must occur no later than
  December 31 of the year prior to the attainment date"; determination due Feb 3, 2025.
- Table 1: 25 monitors, 2021/2022/2023 fourth-highest and 2021-2023 DV (Mesa and JLG Supersite 0.080;
  Buckeye 0.069 and Humboldt Mountain 0.070 attain; Senior Center invalid).
- MAG demonstration Sept 24, 2025; 76 potentially wildfire-influenced exceedance days, 31 excluded.
- Table 2 source apportionment (avg 75/60/15; max 80/66/14; wildfire-excluded 73/57/16, 77/62/15);
  zero-out 80 -> 70 (65/64 wildfire-excluded); Table 3 EPA 2021 modeling (2018-2020 DV 79, IA 8.5, DV
  without IA 70; "70.5 ppb"); Table 4 projected/actual source contributions; HYSPLIT 160 exceedance days
  (26/44/51/39); "potential transport from Mexico (i.e., all days with easterly, southerly, or westerly
  patterns)"; Tables 5-6 NOx/VOC 2017/2023 Maricopa vs Mexico border states.
- 179B Guidance rescinded April 7, 2025.

## D05 - Greater Connecticut tribal portions: failure to attain, reclassify to Serious (Region 1)

- FR 2025-20497, Nov 20, 2025; comments by Dec 22, 2025; signed Mark Sanborn Sept 29, 2025.
- "Effective on August 3, 2018, the EPA designated 52 areas"; offsets 3/6/9 years; CT voluntarily Serious
  (89 FR 60827, July 29, 2024), tribal portions stayed Moderate; deadline Feb 3, 2025.
- Table 1: five monitors 2021-2023 + DV (Groton 090110124: 0.075/0.071/0.071, DV 0.072; East Hartford
  0.066/0.074/0.07, DV 0.07).
- EE: initial notification Jan 10, 2024; demonstration July 1, 2024; requested Groton Apr 13-14, June 30 -
  July 1, July 12, 2023 + July 1 at East Hartford and Cornwall ("five days"); EPA July 22, 2024 concurred
  on Groton June 30 and July 1 and East Hartford/Cornwall July 1; nonconcurred Apr 13-14 and July 12.
- fn 17: tribes already Serious under the 2008 standard (Aug 23, 2019).

## D06 - Baltimore, MD: Clean Data Determination, 2022-2024 data (Region III)

- FR 2026-01314, Jan 23, 2026; comments by Feb 23, 2026; contact Ian Neiswinter; signed Amy Van
  Blarcom-Lackey.
- "Effective August 3, 2018 ... designated 52 areas"; voluntary Serious (MD request July 18, 2024; EPA Aug
  1, 2024, 89 FR 62663); attainment date Aug 3, 2027.
- EE: MDE submitted three demonstrations Feb 2, 2024 (June 2, June 29-30, July 17-18, 2023); extra info
  May 6, 2025; EPA concurred on portions Nov 12, 2025; Table 1 = 15 concurred monitor-days (none on July
  18); fn 5 two further demonstrations not acted on; fn 9 deferrals.
- Table 2 completeness 2022-2025; Table 3 fourth-highest 2022-2025 and DVs 2022-24 / 2023-25 (Edgewood
  0.066/0.073/0.073/0.066, DVs 0.070 and 0.070); MD to certify 2025 data by May 1, 2026.

## D07 - Northern Wasatch Front, Utah: repeal Dec 2024 failure finding; attain but for international emissions (Region 8)

- FR 2026-08372, April 30, 2026; comments by June 1, 2026; signed Cyrus M. Western April 20, 2026.
- "Effective August 3, 2018, the EPA designated 51 areas" + fn 12 San Antonio. Dec 9, 2024 final rule:
  failed; no extension "because at least one monitor had a 2023 fourth highest MDA8 that was greater than
  0.070 ppm"; reclassified Serious effective Jan 8, 2025; petitions Jan 14 / Jan 22 / Feb 4, 2025; granted
  March 5, 2025; 10th Cir. stay April 30, 2025; boundary + 12 townships (Jan 6, 2026).
- 11 regulatory monitors, all above 70 ppb in each of 2021-2023; exceedance days per monitor 1 to 28;
  wildfire-smoke exceedance days 27 (2021), 6 (2022), 8 (2023); 33 exceedance days without smoke, 29 (88%)
  Asia (40%) or Mexico (48%).
- Contributions: Utah 4.3-5.2 ppb, EPA 8.2-9.8 ppb; three monitors (Copperview, Inland Port, Near Road)
  needed atypical-day exclusion; six days in 2021 (July 11, 12, 24; Aug 7, 8, 16).

## Shared ground (navigation only)

- 2015 standard timeline (Marginal 2021, Moderate 2024, Serious 2027; 22 areas reclassified Oct 2022):
  D02, D04, D05, D06, D07. Count of areas designated effective Aug 3, 2018: 52 in D02/D05/D06; 51 plus San
  Antonio (Sept 24, 2018) in D04/D07.
- Truncation convention: D02 fn 10, D04 fn 6, D05 I.A.4, D06 fn 16, D07 fn 8 (and D04 Table 3 note).
- 2023 wildfire exceptional events: D02 (DC), D03 (Coachella), D05 (CT), D06 (MD). Atypical (modeling-only)
  wildfire days: D04 (Phoenix), D07 (NWF). D01: 2018 PM10 events.
- 179B(b) demonstrations: D04 and D07 (same policy text, rescinded guidance).
- Same contact (Ian Neiswinter) D02 and D06; Region IX D01, D03, D04.
- No two documents concern the same area; no document cites another document in the bundle.
