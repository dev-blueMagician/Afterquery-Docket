# aq-02562 - document map

Navigation only (caller, 2026-10-09). Questions quote `text/Dnn.txt`, never this map.

## Bundle

- What it is: seven unrelated Federal Register texts filed as "Dietary Guidelines Federal Register
  Filings" (FDA, USDA FSA/CCC, USDA FNS, HHS). Two loose pairs: D02/D07 (USDA specialty-crop
  assistance, MASC 2024 then ASCF 2026) and D03/D06 (FNS Child Nutrition Programs, 2024 RFI then
  2026 milk rule); D01/D04 share only FDA front-of-package (FOP) labeling; D05 (SNAP retailers) stands alone.
- Documents: 7; D01-D07 = task page Doc 1-7 (file names sort in page order; notes/intake.json).
- Gaps: none. Capture "7 of 7 read in full (391,133 characters)"; splitter matches_capture true for all
  seven, no incomplete flags. Capture warned "Docket has been updated. Reload this page".
- Extraction spot-checks: plain-text captures, extracted 1:1 (D01 52,686 chars ... D07 51,404); tables are
  dot-leader/tab text (D01 Table 1, D02 Tables 1-2, D05 PRA table, D06 meal-pattern tables, D07 Table 1
  and PRA table) and read correctly; footnotes inline with `\N\` markers.
- Coverage: caller read all seven texts in full on 2026-10-09.
- Reuse binding: source sha256 in notes/intake.json (D01 e9c0706d..., D02 f43163ba..., D03 2f87ec41...,
  D04 48907164..., D05 17758b84..., D06 fe07bfbe..., D07 14df7f7f...).

## D01 - FDA PRA notice: Quantitative Research on FOP Labeling (88 FR 39257, June 15, 2023)

- Author: FDA (HHS); Docket FDA-2023-N-0155; OMB 0910-NEW; signed June 9, 2023 (Lauren K. Roth).
- Dates: comments to OMB by July 17, 2023; 60-day notice January 26, 2023 (88 FR 5005).
- Comments: 26 received, 2 duplicates; of the other 24, 20 PRA-related; Comments/Responses 1-37.
- Study: 15-minute web questionnaire, 9,000 U.S. adults; 10 label conditions, 3 food types (breakfast
  cereal, frozen meal, canned soup), no-scheme control; sample raised from 3,000 (Response 30).
- Table 1 (line ~204-211): Pretest 1/2 screeners 800 x 0.05 = 40 h each; pretests 200 x 0.25 = 50 h each;
  experiment screener 40,000 x 0.05 = 2,000 h; experiment 9,000 x 0.25 = 2,250 h; total 4,430 h.
  Prose: participants "increased from the 3,000 respondents ... to 41,600"; burden "from 3,205 responses
  and 801 hours to 51,000 responses and 4,430 hours" (41,600 = the three screener rows).
- Other figures: Pew 93% of adults online; 312 million of ~330 million in library service areas.
- Cites DGA 2020-2025, 9th Edition, December 2020 (Ref. 8). "healthy" symbol FDA is studying (Comment 33).

## D02 - USDA FSA/CCC NOFA: Marketing Assistance for Specialty Crops (89 FR 99212, Dec 10, 2024)

- Applications December 10, 2024 through January 8, 2025; new producers' FSA-1141 by January 8, 2025;
  eligibility forms by January 8, 2026. Documentation within 15 days of request; records kept 3 years.
- Funding "up to $2 billion"; fn 13: "$1,886,000,000 ... after sequestration of 5.7 percent".
- Payment limitation $125,000 per person/legal entity other than JV/GP; Indian Tribes not subject to it;
  average AGI > $900,000 (2021-2023) ineligible unless farm AGI at least 75 percent of AGI.
- Ineligible: Federal, State and local governments incl. public schools. Foreign persons eligible if they
  meet 7 CFR 1400. Specialty-crop list and expressly excluded crops (amaranth for grain, corn other than
  sweet corn, mustard seed, rapeseed, peanuts, sugar beets, ...).
- Payment = sales in Table 1 ranges (a: up to $49,999; b: $50,000-$99,999; c: $100,000-$499,999;
  d: $500,000-$999,999; e: over $1 million) x factors; Table 2 example factors for 57,000 / 113,000 /
  170,000 / 227,000 applicants (11.3/5.7/3.8/2.8 ... 9.3/4.7/3.1/2.3); worked example $450,000 =
  $49,999 a + $50,000 b + $350,001 c. Eligible sales = 2023 or 2024 CY sales + indemnities/NAP; value
  added excluded (pickle example). OMB 0503-0028; Assistance Listing 10.096.
- Background: labor ~45% of variable costs vs 9%; fruit/nut receipts 25% below 10-year average; NCFI 11%
  below; 127 counties > 40%; fruit/vegetable consumption 40%/70% of DGA 2020-2025 recommendations.

## D03 - FNS RFI: Grain-Based Desserts and High-Protein Yogurt Crediting (89 FR 104965, Dec 26, 2024)

- Comments by March 26, 2025. Contact School Meals Policy Division 703-305-2054.
- Rules as of Dec 2024: SBP K-12 bars cookies, dessert pies, cobbler, brownies, all cakes except coffee
  cake toward grains; NSLP K-12 up to two ounce equivalents of grain-based desserts weekly; preschool and
  CACFP: none credit; NSLP afterschool snack: none from SY 2025-2026. 2023 proposal (SBP 2 oz eq/week)
  not finalized in the April 25, 2024 final rule (89 FR 31962).
- Product added-sugar limits (cereal, yogurt, flavored milk) by July 1, 2025; weekly <10% of calories
  by July 1, 2027 (SY 2027-2028), NSLP/SBP only.
- FDA "high" = 20% DV per RACC; added sugars DRV 50 g (4+), 25 g (1-3): high at 10 g / 5 g per RACC;
  protein DRV 50 g / 13 g: high-protein yogurt at least 6.7 g / 2.6 g per four-ounce serving
  (fn 29: FDA yogurt RACC 6 oz for 4+; FNS uses 4 oz for ages 1+).
- Yogurt: 4 oz or 1/2 cup = 1 oz eq meat alternate (NSLP, SBP, CACFP); SFSP lunch/supper 8 oz = 2 oz.
  Crediting set 1997; Greek-style pilot 2013 (4 States), SY 2014-2015 (+8 States), SY 2015-2016 all;
  ~1.8 million lb a year; 2017 RFI 437 comments; meal cost study: yogurt in 10% of lunch, 25% of breakfast menus.

## D04 - HHS Semiannual Regulatory Agenda, Fall 2025 (90 FR 45510, Sept 22, 2025)

- 27 sequence items (OCR 1; CDC 2; FDA 3-16; CMS 17-23; ACF 24-27), each with timetable and
  "Regulatory Flexibility Analysis Required: Yes/No" (No: 1, 24-27 despite the summary's small-entity line).
- FDA FOP Nutrition Labeling 0910-AI80 (Final Rule Stage): NPRM 01/16/25 90 FR 5426; comment end
  05/16/25; final 05/00/26. "Healthy" 0910-AI13 completed: final 12/27/24 89 FR 106064, effective delay
  02/25/25 90 FR 10592, effective 04/28/25. Nicotine NPRM 01/16/25 90 FR 5032 withdrawn 04/21/25;
  menthol withdrawn 07/25/25. TANF $35 a month, base year 2005 to 2015, from October 1, 2025.

## D05 - FNS NPRM: Updated Staple Food Stocking Standards for SNAP Retailers (90 FR 46081, Sept 25, 2025)

- Comments by November 24, 2025; RIN 0584-AF12. 2016 final rule Dec 15, 2016; 2019 proposal April 5,
  2019 (almost 9,000 comments).
- Now: 3 varieties x 4 categories, 3 stocking units each, perishables in 2 categories. Proposed reg text:
  7 x 4 = 28 varieties, 84 units, 3 perishable varieties / 9 perishable units. Group 1 (3 types),
  group 2 (17 types); protein 7 groupings, dairy "twelve" (9 + up to 3 plant-based), grains 6.
- 121,294 small-format stores = 64% of small / 45% of all retailers; stocked enough: grains 81%, F&V 83%,
  protein 63%, dairy 52%. 269,217 retailers (April 30, 2025).
- Costs: Federal ~$4 million FY2027; retailers ~$55 million year 1, ~$2 million/yr for 4 years; small
  stores ~$262 year 1, $374 over five years. PRA table: 269,217 x 4.00 h = 1,076,868 h at $49.89; grand
  total with existing 49,299.85 h = 1,126,167.85 h, which the prose calls the one-time retailer burden.
- Accessory list (proposed 278.1(b)(7)): snack bars, non-whole-muscle jerky, cheese/fruit spreads added;
  sweeteners incl. honey, maple syrup. Stock documentation within 21 calendar days. UMRA $100 million.

## D06 - FNS final rule with comment: Expanding Fluid Milk Options in CNPs (91 FR 25073, May 8, 2026)

- Effective June 8, 2026; comments by June 8, 2026. DGA 2025-2030 released January 7, 2026; WMFHKA
  (Pub. L. 119-69) enacted January 14, 2026 (NSLP lunch whole/2% milk; milk saturated fat exclusion at lunch).
- Old rule: 1-year-olds unflavored whole; 2-5 unflavored low-fat/fat-free (fn 9: 24-25 months may get
  whole/reduced-fat); 6+ and adults low-fat/fat-free, flavored allowed. New: 2+ whole, reduced-fat,
  low-fat or fat-free (2-5 unflavored); SBP gets the saturated-fat exclusion; NSLP afterschool snack,
  preschool, Smart Snacks, SMP, CACFP covered.
- Limits: flavored milk 10 g added sugars per 8 fl oz (competitive middle/high 15 g per 12 fl oz), by
  July 1, 2025 at SBP; yogurt 12 g added sugars per 6 oz from October 1, 2025 (23 g total sugars per
  6 oz through September 30, 2025) in preschool/CACFP tables; cereal 6 g added sugars per dry oz.
- Meal-pattern tables (NSLP, SBP, preschool, afterschool snack, CACFP breakfast/lunch/snack); CACFP adults
  may use 6 oz (3/4 cup) yogurt for 8 oz milk once a day, not as both milk and meat alternate.
- Economics: third scenario ~$15 million average annualized savings over five years. RFA: 11,000 of
  19,000 SFAs < 1,000 students; >14,000 < 2,500; CACFP 19,000 sponsors/centers, 68,000 day care homes.
  UMRA $146 million. PRA menus 0.25 h lunch / 0.12 h breakfast x 180 days.

## D07 - CCC final rule: Assistance for Specialty Crop Farmers (91 FR 32307, June 1, 2026)

- Effective June 1, 2026; ~$1.625 billion; 2025 crop year acres reported by April 24, 2026.
- Table 1 (lines ~103-107, repeated in reg text ~326-331): Tier 1 $650 (revenue > $10,000/acre), Tier 2
  $225 (> $2,300 to $10,000), Tier 3 $65 (<= $2,300), Beans and Peas $25. Same crop split across tiers:
  peaches (freestone, semi-freestone cling: T1; cling: T2), cherries (sweet T1, tart T2, chokecherry/
  Jamaica T3), blueberries, grapes (fresh T1, processed T2), cabbage, peppers, greens.
- Eligible acres: initial, double, repeat and subsequent crops; non-bearing fruit/nut acres; excludes
  controlled-environment acres except mushrooms, cover crop, prevented planted, grazing, etc.
- Applications: portal from June 1, 2026, others June 8, 2026; CCC-556 by August 7, 2026; eligibility
  forms by August 9, 2027. Limit $250,000 per person/entity incl. JV/GP members; public schools $250,000
  each, all schools in a State over 1,500,000 people $500,000; AGI > $900,000 (2021-2023) ineligible, no
  farm-income exception printed; foreign-person provisions do not apply (entities solely citizens/resident aliens).
- PRA: OMB 0503-0028 (same as MASC); 60,000 respondents, 107,600 responses, 30,320 h (AD-1026 584.5 h
  EXEMPT, excluded); "time per respondent" 0.28178439 h is hours per response. Assistance Listing 10.991.

## Shared ground (navigation only)

- D02/D07: CCC/FSA specialty-crop payments; same OMB 0503-0028, same AGI test years 2021-2023 and
  $900,000; limits $125,000 vs $250,000; MASC sales-based factors vs ASCF per-acre rates; public schools,
  foreign persons and the 75% farm-income exception differ.
- D03/D06: CNP meal patterns; yogurt crediting (D03) vs yogurt/milk sugar limits and tables (D06);
  grain-based dessert rules; added-sugar timeline July 1, 2025 / October 1, 2025 / July 1, 2027.
- D01/D04: FDA FOP research (2023) vs FOP NPRM (01/16/25) and planned final rule (05/00/26); "healthy".
- DGA editions: 2020-2025 cited by D01, D02, D03, D05; 2025-2030 by D06 (released January 7, 2026), D07.
- D05/D02/D07: honey, maple syrup (SNAP accessory) vs MASC specialty crops; nuts, beans, peas move to
  SNAP protein. D05/D06: one "perishable liquid milk" variety covers whole/2%/1%/skim.
- PRA tables: D01, D05, D07; UMRA thresholds $100 million (D05, D07) vs $146 million (D06).
