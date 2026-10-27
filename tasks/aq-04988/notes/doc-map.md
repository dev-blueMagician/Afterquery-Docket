# aq-04988 - document map

Maintained by the caller from `text/` (2026-10-14). Navigation only: questions quote the documents, never this map.

## Bundle

- What it is: ten unrelated academic papers on salt/sodium reduction (models, reviews, compliance and policy studies).
- Documents: 10; local ids alphabetical (text/manifest.json). Page Doc N -> local id:
  Doc 1 = D10 (Australia reformulation model), Doc 2 = D04 (Brazil microsimulation), Doc 3 = D08 (NZ HeartSAFE),
  Doc 4 = D03 (meat/fish five countries), Doc 5 = D06 (Japan Markov), Doc 6 = D09 (restaurant policy review),
  Doc 7 = D01 (2019 global review), Doc 8 = D07 (Durban snacks, SA Reg 214), Doc 9 = D05 (four LMICs), Doc 10 = D02 (Victorian partnership).
- Gaps: none in the capture ("10 of 10 read in full"). Figures and several tables were never in the platform text:
  D07 (Doc 8) Tables 1-4 (per-product data), D05 (Doc 9) Figure 1, D01 (Doc 7) Figures 1-5 and Supplemental Table 2,
  D09 (Doc 6) Tables 1-2 (policy lists), D10 (Doc 1) S1 File tables (HFP/UK target lists). Solvers see the same text.
- Extraction spot-checks: plain-text capture; text/ equals docs/ body (char counts match within header lines).
  Tables checked: D08 Table 2 rows, D03 Tables 1-3, D01 Table 1, D10 Tables 2-3, D04 Tables 2-3, D05 Table 2.
- Coverage: all ten texts read in full by the caller, 2026-10-14.
- Provenance: notes/intake.json; capture AQ-04988_2026-10-14_1417.txt (page said "Docket has been updated. Reload ...").

## Internal inconsistencies found (avoid as golds)

- D06 (Doc 5) l88: <5 g scenario averted cases 134,633 but IHD 50,734 + stroke 77,599 = 128,333 (2.9% fits 134,633; IHD likely 57,034).
- D04 (Doc 2): CVD deaths 2600 (abstract l15) vs 2500 (results l111); table CHD 1200 + stroke 1400 = 2600. Informal costs 71 (l15, Table 3) vs 70 (l142). Period "2011 to 2017" (l111) vs "between 2013 and 2017 ... 25 mg/day every year" (l172).
- D03 (Doc 4) Table 2: UK total 135 (26.6%) but the UK category denominators sum to 462 (29.2%); other countries consistent.
- D07 (Doc 8) l250-258: discussion swaps 2016/2019 failure shares; l217 vs l293: Savoury Snack 2 detected 118 vs 8.81 mg.
- D08 (Doc 3): female n 2655 (Table 1) vs 2505 (Table 3); abstract CI "(1024, 1027)" vs table (1024, 1072).
- D05 (Doc 9) l179 SA "National survey (24 h urine)" vs l249 "Argentina and South Africa conducted regional surveys".
- D01 (Doc 7) Table 1 Argentina 11.2 -> 9.2 (2011-2015, -18%) vs D05 (Doc 9) l144/l298 "none of the countries had reduced salt intake by 2018".
- SA regulation year: D03 (Doc 4) l206 "in 2012" vs D07 (Doc 8) l53 "March 2013" and D05 (Doc 9) l129 "2013".
- Portugal salt tax: D08 (Doc 3) l273 lists it as implemented; D01 (Doc 7) l146 "ultimately not approved".
- Australian HFP reduction: D10 (Doc 1) 107 mg/d vs D08 (Doc 3) l253 an "Australian study" 50 mg/day (identity unresolved).

## D10 (Doc 1) - Australia: health impact of sodium reformulation targets (Trieu et al., PLOS Med)

- HFP targets 2020: 27 food groups, 12 major categories, 4-year time frame (l84, l143). HFP formed 2015 (l83).
- UK 2017 targets (released 2014): 76 food groups, 27 major categories; 81% compliance in 2018 (l145).
- Optimistic scenario = sales-weighted 25th percentile in the 76 UK groups (l147).
- Baseline 2,908 -> 2,801 mg/d from nondiscretionary sources, -107 mg/d (3.7%); men 126, women 88 (l194).
  UK 221 mg/d (7.7%), optimistic 322 mg/d (11.2%) (l196). Nondiscretionary = 85% of urinary sodium (Table 1 l126).
- Deaths averted 514 (text "510"); CVD 422, IHD 252, stroke 99, other 70, CKD 38, stomach cancer 52 (Table 2 l223-248);
  incidences 1,921; DALYs 7,238. % averted = share of 2017 totals (l250). Inflammatory heart disease in deaths only (l172).
- UK +660 deaths (+2,341 cases, +8,748 DALYs); optimistic +1,065 deaths (summary "1,070"), +3,929 cases, +14,435 DALYs (l262-264).
  "1,174 premature deaths each year" for UK targets (l303).
- By food: processed meat 26.2% (n=134), sausages 20.6% (107), bread 19.1% (98) (l206, l217).
- Top 5 companies (Table 3 l276-284): 95, 94, 47 (retailers), 39, 30 (manufacturers), others 209; 59% to top 5.
- TMREL 1.0 -> 575 deaths, 3.0 -> 415 (l290). Food and Health Dialogue: 67% bread, 47% processed meat met by 2013 (l308).
- Sodium intake ~4,000 mg men / 2,900 mg women; 34% adults hypertensive (l81-82). 96 countries in 2019; 57 of 68 (l73-75).

## D04 (Doc 2) - Brazil: voluntary sodium targets, IMPACTNCD-BR, 2013-2032

- Voluntary targets since 2011, 34 food categories (l83); committed industry = 70% market share (l42).
- 0.1 g/day sodium (0.25 g salt) decline (l111, l172); "a reduction of just 2%"; 25 mg/day per year (l172).
- Table 2 (l117-124): CHD cases 98,000; stroke cases 84,000; CHD deaths 1,200; stroke deaths 1,400; all deaths 14,000.
  "cases prevented or postponed" = case-years (l97). Adults 30-79.
- Costs (Table 3): total 290 m; SUS 220 m; informal 71 m; US$1 = R$3.876 (31 Dec 2018); 3% discount (l101).
- Review figures (l166-168): Finland and Japan 1.6 g/day, Turkey 1.2, UK 0.52; mandatory reformulation 0.58, voluntary 0.32 ...
- UK 2003-2010 annual reductions 80 mg men / 50 mg women (l172); ~35% of Brazil's sodium from industrial foods, >55% table salt.

## D08 (Doc 3) - NZ HeartSAFE 2020 simulation (2008/09 NZANS, n = 4721)

- 840 foods, 17 categories, 35 sub-categories (l11, l87). Table 2 (l134-171): baseline content, HeartSAFE target, eating
  occasions, baseline/simulated/reduction intake per sub-category (e.g. bacon 1589 -> target 1090; S&V target 740).
- 1307 -> 1048 mg/day, -260 (20%) from targeted foods (l15, Table 3 l203); men 1464/-288, women 1162/-233.
- Total intake 3100-3500 mg/day; <8% of total (l231-232). 24-h urine: 3100 (1998), 3459 (2011), 3386 (2012) mg/day (l33).
- Cites: US 260 mg/day 2000-2014; NSRI 62 categories; Australian study 27 HFP categories, 50 mg/day (l251-253);
  NZ study with UK targets 628 mg/day (l268); UK 15% urinary reduction by 2011 (l265).

## D03 (Doc 4) - processed meat/fish sodium, China/UK/Australia/SA/USA (FoodSwitch 2012-2018)

- 26,500 products (19,601 meat, 6,899 fish): China 1,898; UK 885; Australia 5,673; SA 946; USA 17,098 (l11).
- Table 1 medians by country and 20 subcategories (l89-114). Table 2: 2017 UK targets for 13 categories, n (%) meeting (l141-156);
  bacon, frozen meat, salami, whole hams, canned fish use AVERAGE targets (dagger). Table 3 contribution values (l168-190).
- Traffic light: low <120, medium 120-600, high >600 mg/100 g (l71). Salt/2.5 = sodium (l69). Contribution = median/2000 (l73).
- UK four target sets since 2006; NSRI 2008; Food and Health Dialogue 2010; SA legislated limits 2012 (l206).
- Collection periods by country (l226).

## D06 (Doc 5) - Japan Markov model, adults 40-79 in 2019 (n = 66,955,000), 2019-2029

- 9.7 g/day in 2019 (l18); targets 8 g (2012 campaign), <6 (JSH 2019), <5 (WHO); DRI 2020 <7.5 men/<6.5 women (l21-22).
- Annual reduction rates 2.1%, 4.9%, 6.8% to reach targets in 2029 (age-adjusted, 2010 standard population) (l58).
- Base case (l84): IHD 2,000,792 incident (3.0%), stroke 2,595,308 (3.9%); deaths 747,314 / 398,255; costs USD 61.6 bn / 104.6 bn.
- Averted (l88-94): see inconsistency above. 109.01 yen/USD (2019); 2% discount (l70).

## D09 (Doc 6) - restaurant salt policy review

- 78 works; 58 countries/regions; 62 policies; 27 mandatory (3 with fines) (l9, l61-64). Strategies: menu labelling 40,
  target setting 23, reformulation 13, education 6, chef training 4, government assistance 3, toolkits 2, table salt removal 5,
  media 3 (l63). Target setting/reformulation in 32 countries/regions; six mandatory, one with fines (California) (l83-85).
- Table-salt-on-request policies: Buenos Aires (Argentina), Costa Rica, France, Mexico City, Uruguay (l99).
- Limits 750-2300 mg sodium per meal (l88). 17 evaluations: 6 positive, 8 little/no effect, 3 overall (l106).

## D01 (Doc 7) - 2019 global review of national salt reduction initiatives

- 96 initiatives (68 ongoing + 28 new), 16 planning; 75 in 2014 (+28%); 2010->2014 +134% (l94, l152, l266).
- Strategies 2019 (2014): settings 74 (52), reformulation 68 (61), education 50 (71), FOPL 48 (31), tax 5 (3) (l104, l152).
- 57 with salt targets: 19 mandatory (10 bread-only, 9 wider, listed l116), 48 voluntary, 10 both (l113-118).
- Taxes: Fiji, Hungary, Mexico (8%), SVG (15% VAT 2016), Tonga (2015); 5 considering; Portugal not approved (l137-146).
- By region and income (l158-198). Table 1 (l209-249): salt intake change by country, method, years (Australia row = Victoria;
  Finland regional). 3 substantial, 9 moderate, 5 slight, 1 increase, 7 minimal (l205).
- 2017 GBD: high BP 10.4 m deaths; excess salt 3.2 m deaths, 70 m DALYs (l24). Questionnaire 35/70 (50%) vs 79% (l94, l277).

## D07 (Doc 8) - Durban savoury snacks vs Regulation 214 (published March 2013; targets June 2016 and June 2019)

- 90 products: C1 RTE savoury snacks 40, C2 flavoured potato crisps 40, C3 salt-and-vinegar 10 (l115).
- Targets 2016/2019: C1 800/700, C2 650/550, C3 1000/850 mg/100 g (l165). Failures: C1 3 and 11; C2 0 and 8; C3 1 and 4.
- Means: C1 532, C2 507, C3 799; extremes l167-203. Claims: low <=120, very low 40, free 5 (l292).
- Australia S&V target 810, NZ 740 (NIHI, l225). Retail shares l48. Africa-Predict -1.2 g/day sodium (l312).

## D05 (Doc 9) - Argentina, Mongolia, South Africa, Vietnam (2018 analysis)

- Interviews: Argentina 7, Mongolia 13, SA 4, Vietnam 11 (l91). Strategies 32 (2010), 75 (2014), 96 (2019) (l40).
- Targets: <5 g SA and Argentina; 7 g Vietnam (+30%); 7.8 g Mongolia (l157). Table 2 surveillance (l174-180):
  Argentina 11 g (2011), Mongolia 11.1 g (2011) and 10.5 g (2019 spot), SA median 6.8 g (2015), Vietnam 9.4 g (2015).
- SA: draft 2012, mandated 2013 for 2016, more by 2019 (l128-129); 67% compliant with first round in 2016 (l146).
- Argentina: voluntary 2009/2011, Sodium Law 2013, restaurants 2017 (l127, l193, l222). Mongolia pilot -2.8 g (l124).

## D02 (Doc 10) - Victorian Salt Reduction Partnership (VSRP) advocacy evaluation

- VSRP est. 2014 by VicHealth; goal -1 g in Victoria by 2020 (l40). 2012 Victoria: 8.6 g men, 6.3 g women (l66).
- Business case: 787 lives/yr, $47 m/yr from a 3 g reduction (l76). 10 member organisations (l100).
- Interviewees 14 VSRP (4 research, 6 NGO, 4 SGSA) + 7 industry (l52). HFP 2015, Reformulation Working Group 2016,
  2018 consultation (l202-205); targets released May 2020 (l222). Health Star Rating 2014, ~40% uptake (l34-35).

## Shared ground (navigation only)

- Same countries across papers: Australia (D10, D03, D02, D01 Victoria row, D08 cites); NZ (D08, D01 row, D07 S&V target);
  Japan (D06, D01 row, D04 review); Argentina (D05, D01 row and mandatory list, D09 Buenos Aires); South Africa (D07, D05,
  D03, D01); UK (D10 targets, D03 targets, D01 row, D04, D08); Turkey (D01 row 18.0->15.0 salt; D04 1.2 g/day sodium).
- Target sets: UK 2017 targets in D10 (76 groups) and D03 (13 meat/fish categories); NZ HeartSAFE in D08 and D07 (S&V 740);
  SA Reg 214 in D07 (snacks), D05, D03, D01; Australia HFP in D10, D02, D08.
- Count series: national initiatives 32/75/96 (D05, D01, D10).
- No forecast/actual or proposal/final pair across papers; no paper analyses another paper's data.
