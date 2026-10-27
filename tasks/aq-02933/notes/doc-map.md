# aq-02933 - document map

Maintained by the caller (Claude Opus 5.5, 2026-10-11) from `text/`. Navigation only: questions quote
the documents, never this map. Offsets are character positions in the `docs/` originals.

## Bundle

- What it is: "Medicare Payment And Enrollment Rules", seven Federal Register texts. Three CMS
  nationwide enrollment-moratorium notices of 2026 (DMEPOS medical supply companies, hospices, HHAs)
  share one template and are the only documents that join. Two are corrections to consecutive
  Physician Fee Schedule rules (CY 2025 final, CY 2026 proposed). Two are unrelated (a Labor
  Department award list, a Federal IDR correcting amendment).
- Documents: 7; ids from `text/manifest.json`. **Local ids differ from the task page for two files:**
  D05 = Doc 6 (HHA notice, fr_2026_09717), D06 = Doc 5 (hospice notice, fr_2026_09718). All other
  Dnn = Doc n. Form fields cite Doc N.
- Gaps: none known. The capture says "7 of 7 read in full (429,602 characters)"; intake marks every
  document complete, `gap_characters: 0`.
- Extraction spot-checks: all seven are plain text; each `text/Dnn.txt` body equals its `docs/` file
  character for character (script comparison, 2026-10-11). Tables arrive flattened onto one or two
  lines (hospice Tables 1-2, D01 Tables 107/128, D02 Tables 87/B.2, D04 recipient list); row labels
  and values checked by reading (hospice Table 1: four States x CY 2019 / CY 2023 / percentage).
  Footnotes checked: D03 fn 28 (large-supplier definition), D05 fn 4 and fn 23, D06 fn 25.
- Provenance: `notes/intake.json`, capture `AQ-02933_2026-10-11_1120.txt`
  (sha256 6275c755...3b5b60), all `matches_capture: true`.
- Reuse binding (source sha256, first 12): D01 8c4abba9d836, D02 f81d5b276d6f, D03 226c3cf013fd,
  D04 e75553060227, D05 43564338a4d3, D06 7249cd72f8cb, D07 f1aae587347a.
- Coverage: D01, D02, D03, D05, D06, D07 read in full by the caller. D04: preamble and closing read
  in full; the 888-row recipient table (about 82,000 characters) read at its head and tail only.

## D03 = Doc 3 - DMEPOS medical supply company moratorium (CMS-6099-N)

- Source: fr_2026_03971.txt, 58,967 chars; 91 FR 9855-9862; published Friday February 27, 2026;
  filed 2-25-26, 4:15 pm.
- Author: CMS (HHS). Contact Frank Whelan. Signed for Administrator Dr. Mehmet Oz.
- Effective: "The moratorium takes effect February 27, 2026" (offset 1,117). Six months; extendable
  in 6-month increments (I.C.5).
- Scope (II.D, offset about 33,000): seven supplier types (medical supply company; with orthotics /
  pedorthic / prosthetics / prosthetic and orthotic personnel; with registered pharmacist; with
  respiratory therapist). "Principal function" test: grocery stores, pharmacies, hospitals, HHAs,
  physician offices are "generally" outside it. Personnel test: at least one such individual in an
  employment, advisory, contractual or other role. New practice locations count as initial
  enrollments (each DMEPOS location is separately enrolled, Sec. 424.57(b)(1); II.C).
- Ownership: exemption bullet in I.C.4 names only HHAs as the exception ("except changes in
  ownership of home health agencies that would require an initial enrollment"); II.D's last
  paragraph (offset 36,372) says a non-exempt change in majority ownership within 36 months
  (Sec. 424.551) is an initial enrollment the moratorium prohibits.
- Figures (all deep in the file): 85 percent of payments to small suppliers (fn 28: large = TIN with
  25 or more enrollments); 17 percent revocation rate for medical supply specialties, "nearly
  triple" other types (40,382); 7 types in top 20 / 5 in top 10 / 6 in top 10 / all in top 15 of
  "over 80" types; "nearly 80,000" suppliers as of October 2025, medical supply companies "more than
  6,000 enrollments, or 7.5 percent" (42,188); "approximately 600 ... each year (or 300 over a
  6-month period)" (42,382); Master List: 32 prefabricated brace codes, 9 off-the-shelf, more than
  70 percent of more than 2.1 million claim lines, more than 80 percent of more than 1.5 million
  (47,375); RFA: 79,360 enrollments in 2025, "8.3 percent decrease since 2023" (54,573); small
  entity revenue "$37.5 million to $41 million"; UMRA 2026 threshold "approximately $187 million".
- Consultation: "both the OIG and the Department of Justice". Alternatives: three (forgo; all DMEPOS
  types; certain States). Medicaid/CHIP: left to each State.
- Hedges: "would generally not apply" (non-medical-supply DMEPOS suppliers).

## D06 = Doc 5 - Hospice moratorium (CMS-6102-N)

- Source: fr_2026_09718.txt, 61,687 chars; 91 FR 27946-27954; published Friday May 15, 2026; filed
  5-13-26.
- Effective: "This moratorium is effective on May 13, 2026" (offset 912), two days before publication.
- Scope (II.D): all hospices and hospice practice locations, nationwide; non-exempt CIMO within 36
  months (Sec. 424.550(b)) is a new enrollment and is blocked. Exemption bullet names HHAs,
  hospices and DMEPOS suppliers.
- Table 1 (offset about 16,100), enrolled hospices CY 2019 / CY 2023 / percentage increase: Arizona
  152 / 311 / 105; California 1,130 / 2,559 / 126; Nevada 55 / 138 / 151; Texas 718 / 1,081 / 51.
- Table 2 (offset 44,272), newly enrolling hospices CY 2023 / CY 2025: Arizona 53 / 3; California
  362 / 29; Texas 164 / 67. Nevada has no row: prose gives 5 new in CY 2019 and "between 35 and 39
  ... in each of the last 4 calendar years"; enrolled Nevada hospices 138 (CY 2023) to 188 (CY 2025),
  "36 percent". Georgia 221 (CY 2019) to 273 (CY 2025), "24 percent"; beneficiaries up 6 percent.
- Oversight (II.A.3): hospices moved from "moderate" (2011) to "high" screening beginning 2024;
  36-month rule extended to hospices; PPEO from 2023 on new hospices in Arizona, California, Nevada
  and Texas, "as of June 2025 approximately 670 hospices were subject to medical review with 122 of
  them revoked", "18 percent" against an average of "about 1 to 3 percent" (37,342); PPEO expanded in
  2025 to Ohio and Georgia (46,263); RFA calls them "the six States" (59,406).
- RFA (57,975): excluding Arizona, California, Georgia, Nevada and Texas, new enrollments CY 2023 to
  CY 2025 "roughly 500 (166 per year)"; "approximately 7,000 currently enrolled hospices"; small
  entity revenue "$19 million to $41 million"; UMRA 2026 threshold "approximately $193 million".
- Consultation: OIG only. Alternatives: says "two principal", lists three (forgo; the six PPEO
  States; require States to act).
- Slips in the source: fn 25 says the California licence moratorium cut "new HHAs" (means
  hospices); "a similar number would seek to enroll during the moratorium" leaves the period open.
- Cross-reference: says the February 27, 2026 medical supply moratorium "remains in effect".

## D05 = Doc 6 - HHA moratorium (CMS-6101-N)

- Source: fr_2026_09717.txt, 54,123 chars; 91 FR 27954-27961; published Friday May 15, 2026.
- Effective: "This moratorium is effective May 13, 2026" (offset 949).
- Scope (II.D): all HHAs, branches and practice locations; subunits not included (designation ended
  2018); non-exempt CIMO within 36 months blocked.
- Figures: Los Angeles County HHAs up "more than 40 percent" 2019-2023, "Well over 1,000" new since
  2019, "roughly 12-15 percent of all HHAs nationwide", about 3 percent of beneficiaries (17,725);
  Ohio: "at least nine cases" of at least five HHAs at one address, four with at least nine, one
  with 18 (18,636); similar in Texas, Michigan, North Carolina, Nevada; fn 23 (36,942): "Between 2019
  and 2025, the number of enrolled HHAs in Michigan dropped from 485 to 361 (over 25 percent) and
  from 2,269 to 1,893 in Texas (roughly 17 percent)"; "over 11,500 HHAs nationwide" (44,246); RFA:
  outside California "generally been less than 400" new HHAs a year "(or an average of roughly 150
  to 200 over a 6-month period)" (50,192); UMRA "$193 million".
- Screening: fn 4 lists the six "high" types (HHAs, DMEPOS suppliers, hospices, Medicare diabetes
  prevention programs, skilled nursing facilities, opioid treatment programs); HHAs one of two
  assigned "high" in 2011. PPEO on new HHAs 2019, expired 2020. Capitalization rule Sec. 489.28(a).
- Consultation: OIG. Alternatives: says two, lists three (forgo; southern California; require States).

## D01 = Doc 1 - CY 2025 PFS final rule corrections (CMS-1807-F2 / CMS-4204-F3)

- 90 FR 20801-20808, May 16, 2025. Corrects the December 9, 2024 final rule (89 FR 97710) and a
  December 30, 2024 appeals correcting amendment.
- Figures: Q3014 facility fee "$31.04" corrected to "$31.01"; APP Plus measures 11 (PY 2024) to 6
  (PY 2025); rebate forms "310 hours (31 hr per form * 10 forms)" twice; Table 107 corrected rows
  (QPP: 51,986 respondents, 68,954 responses, (7,570) hours, (913,176); Total: 52,006, 68,974,
  (6,950), (838,420)); Table 128 (594,447 hours / $71,079,848 down to 586,877 / 70,166,672; change
  -7,570 / -913,176; six MVP lines).

## D02 = Doc 2 - CY 2026 PFS proposed rule correction (CMS-1832-CN)

- 90 FR 39155-39161, August 14, 2025; corrects the July 16, 2025 proposal (90 FR 32352); comments
  by September 12, 2025; final rule due November 1, 2025.
- Figures: KX modifier threshold $2,410 (CY 2025) x 1.027 rounded to nearest $10 = $2,480; targeted
  medical review threshold $3,000 through CY 2027; CPT 95800 survey (60 percent disposable, 25
  responses, 12 percent, 17 days); "32 MIPS quality measures" (was 42); budget neutrality 0.55
  percent (1.0055); Table 87 (rebate row 6,500 / 26,000 / 8 / 208,000 / 23,195,120; Total 64,683 /
  91,667 / 197,909 / 22,698,711).

## D04 = Doc 4 - HIRE Vets Medallion 2025 recipients (Labor Department, VETS)

- 91 FR 11564-11577, March 10, 2026. 891 applications, 888 approved (233 SG, 154 SP, 251 MG, 155 MP,
  80 LG, 15 LP), 1 denied, 2 withdrawn; inflation 28.7% (Apr 2017 to Apr 2025); 2026 fees Small
  $120, Medium $250, Large $640. No link to the CMS documents.

## D07 = Doc 7 - Federal IDR operations correcting amendment (Treasury, Labor, HHS, OPM)

- 91 FR 55462-55473, August 28, 2026; corrects the June 4, 2026 IDR final rule (91 FR 33900),
  effective August 3, 2026. Regulation text for open negotiation (30 business days, response by the
  15th), IDR initiation (4-business-day window), entity selection (3 / 5 / 6 business days),
  batching (up to 50 items), offers (10 business days), determination (30 business days), 90-day and
  30-business-day suspension periods, 6-year records. No link to the other documents.

## Shared ground (navigation only)

- Texas is the only State with counts in two documents: enrolled hospices (Doc 5, Table 1) and
  enrolled HHAs (Doc 6, fn 23). Nevada, Ohio and Michigan appear in both May notices without paired
  figures.
- All three moratorium notices reprint the same history (2013 notice through the January 30, 2019
  expiry) and the same Sec. 424.570 rules (six months, lifting, "high" screening for six months
  after lifting, fee refund, limited appeal): none of that carries single-document necessity.
- Docs 5 and 6 both print the February 27, 2026 Federal Register date of Doc 3's notice, so Doc 3's
  date is replaceable; its scope, its figures and its Sec. 424.551 paragraph are not.
- Template departures: only Doc 5 gives its would-be-entrant figure per year; Doc 3's ownership
  bullet omits hospices and DMEPOS; Docs 5-6 take effect before publication; UMRA and small-entity
  thresholds differ between February and May.
- Docs 1-2: consecutive years of one rule series; no figure for one period appears in both.
