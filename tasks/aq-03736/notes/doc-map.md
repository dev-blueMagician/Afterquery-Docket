# aq-03736 - document map

Maintained by the caller from `text/` (2026-10-13). Navigation only: where things are, not what to ask.
Questions quote the documents, never this map.

## Bundle

- What it is: the EU corporate sustainability due diligence file in three texts: the Commission's 2022
  proposal with its explanatory memorandum, the two-page executive summary of the impact assessment, and
  the directive as adopted in 2024.
- Documents: 3. Local id -> task page Doc number: **D01 = Doc 1** (proposal), **D03 = Doc 2** (impact
  assessment summary), **D02 = Doc 3** (adopted directive). The ids differ from the Doc numbers for two of
  the three; form fields cite Doc N.
- Gaps: none known. Capture header: "Documents: 3 of 3 read in full (505,656 characters)"; intake.json marks
  all three complete, `gap_characters: 0`. The capture carries the standing note "Docket has been updated.
  Reload this page..." (a page notice, not a document gap).
- Extraction spot-checks (plain-text capture, no pages): D01 line count and first/last lines against the
  capture (Doc 1 body ends with the annex, Part II point 12); footnotes (62)/(63) present at L1211/L1213 with
  their body markers at L155; D02 Article 37 (L1029-1047) and annex Part II point 16 present, three annex
  footnotes at the end; D03 ends "5 years after transposition". Tables: none in D01/D03; D02 has two one-row
  pipe tables (Articles 32, 33). No disagreement found.
- Provenance: notes/intake.json (capture sha256 2d8d9bec...; per-document source hashes).
- Reuse binding: D01 f607164e..., D02 b9e926a7..., D03 2c47ff8d... (text/manifest.json).
- Repeat check 2026-10-13: no document hash or file name matches any earlier bundle in 10.6, 10.7 or 10.8.
- Public texts: all three are published EU documents. Headline thresholds and dates of the adopted
  directive are widely reported; treat them as recallable (general-knowledge check).

## D01 (Doc 1) - Commission proposal COM(2022) 71 final, 23.2.2022

- Source: docs/com-2022-71-...txt | 231,251 chars, 1,535 lines, no pages.
- Written by: European Commission. Procedure 2022/0051(COD).
- Structure: explanatory memorandum L21-L359 (chars 0-75,700); recitals (1)-(71) L383-L525; articles 1-32
  L529-L1081 (from char 132,423); footnotes (1)-(130) L1089-L1361; annex L1363-L1533.
- Explanatory memorandum, figures: NFRD "approximately 12 000 companies" (L59); institutional investors
  38% (L133); SMEs "around 99 %" (L143); third-country thresholds "EUR 150 million for group 1 and EUR 40
  million for group 2", EU "above 500 employees in group 1 and above 250 employees in group 2" (L147);
  "about 13 000 EU companies 62 ... about 4 000 third-country companies 63" (L155); roadmap "114
  feedbacks" (L189); public consultation "473 461 responses and 122.785 citizen signatures ... and 149
  position papers" (L191); Regulatory Scrutiny Board dates 9 April 2021, 8 November 2021, 26 November 2021
  (L223); scope after the Board: 250 employees / EUR 40 million, 500 / EUR 150 million (L241).
- Footnotes with data: (3) France 2017, Germany 2021; (11) NFRD 500 employees; (15) CSRD "as of 2026";
  (50) German law 3000 employees, "1000 as from 2024"; (58)/(59) group definitions; **(62) "In group 1: 9
  400 companies, in group 2: 3 400 companies."** (L1211); **(63) "In group 1: 2 600 companies, in group 2: 1
  400 companies."** (L1213); (65)-(68) consultation percentages by stakeholder group; (73) "OJ C , , p. ."
- Timing statements: memorandum "After seven years following the end of the transposition period, the
  Commission shall report" (L285); group 2 "only 2 years after the end of the transposition period" (L145),
  "transition period of two years" (L241); recitals (21), (23) the same; Article 29 "7 years after the date
  of entry into force" (L1045); Article 30 transposition "2 years from the entry into force", application
  "2 years" for Article 2(1)(a) and 2(2)(a) companies, "4 years" for 2(1)(b) and 2(2)(b) (L1059-L1065);
  Article 31 twentieth day after publication (L1075).
- Operative rules with numbers: Article 2 scope (L549-L569): 500 employees / EUR 150 million; 250 / EUR 40
  million with 50% in listed sectors; third country EUR 150 million in the Union, or EUR 40-150 million
  with 50%; EU reference year "last financial year", third country "financial year preceding the last
  financial year"; part-time FTE and temporary agency workers (2(3)). Article 1 "at least every 12 months"
  (L539); Article 5(2) policy updated annually (L703); Article 6(2) group-2 companies only severe impacts
  (L711); Article 10 monitoring every 12 months (L815); Article 11 statement "by 30 April each year"
  (L821); Article 15 climate plan only for Article 2(1)(a) and 2(2)(a) companies (L853); Article 16
  authorised representative for 2(2) companies; Article 20(3) sanctions "based on the company's turnover"
  (L941); Article 21(3) "1 month" (L955); Articles 25-26 directors' duties, companies in Article 2(1) only
  (L1005, L1013).
- Lists: Article 3(a)(iv) regulated financial undertakings, 19 dashes (L587-L623); annex Part I section 1,
  21 points (L1379-L1449); section 2, 14 bullets plus the 8 ILO core conventions (L1453-L1497); Part II, 12
  points (L1503-L1531).
- Internal inconsistencies (not gold material): memorandum vs Article 29 on the review (seven years after
  transposition vs after entry into force); recital (21) reference year vs Article 2(1); recital (23) "at
  least EUR 150 million" vs "more than"; memorandum's article summary numbers two articles "23".
- Coverage: memorandum, articles, footnotes and annex read in full (annex and footnote lines over 700
  characters read in part, then the long annex points in full); recitals read by keyword (21-25, 28-31, 46,
  49, 53, 61, 70 in full; the rest scanned for numbers and dates only).

## D03 (Doc 2) - impact assessment executive summary SWD(2022) 43 final, 23.2.2022

- Source: docs/swd-2022-43-...txt | 11,096 chars, 83 lines. Written by: European Commission staff.
- Figures (all L59-L81): one-off compliance costs "EUR 500 to 680 million"; recurrent "EUR 1.72 to 2.37
  billion" a year, both "depending on the selected employee number / turnover criteria"; directors' duties
  one-off "EUR 445 million"; supervisory one-off "EUR 0.13 million", recurrent "EUR 7.86 to 11.2 million";
  science-based-target duties for companies "with more than 1000 employees" (L45); consultation "almost
  half a million responses" (L49); review "5 years after transposition" (L81).
- Describes the impact assessment's preferred package, which D01's memorandum says was "significantly
  revised" for the proposal (D01 L239-L249): its cost figures are not costs of the proposal as tabled.
- Coverage: read in full.

## D02 (Doc 3) - Directive (EU) 2024/1760, OJ L 5.7.2024

- Source: docs/directive-eu-2024-1760-...txt | 263,324 chars, 1,283 lines. Adopted by the European
  Parliament and the Council; "Done at Brussels, 13 June 2024" (L1063); Articles 32-33 call it the
  directive "of 13 May 2024" (L969, L978).
- Structure: recitals (1)-(99) L31-L227 (chars 912-126,400); articles 1-39 L231-L1061; footnotes L1077-
  L1171; annex L1173-L1271.
- Dates: entry into force twentieth day after publication (Article 38, L1055); "25 July 2024" printed in
  Article 34(2) (L987) and 36(1) (L1011); transposition 26 July 2026 (L1033); application 26 July 2027,
  2028, 2029 by size (Article 37, L1037-L1045), with Article 16 applying "for financial years starting on or
  after" 1 January 2028 or 2029; supervisory authorities notified by 26 July 2026 (L787); model clauses 26
  January 2027 (L671); guidelines 26 January 2027 and 26 July 2027 (L695); delegated acts 31 March 2027
  (L639); single access point 1 January 2029, collection body 31 December 2028 (L647, L657); financial
  services report by 26 July 2026 (L1011), which the recital calls "no later than two years after" entry
  into force; review "By 26 July 2030, and every three years thereafter" (L1013).
- Scope (Article 2, L251-L281): 1 000 employees and EUR 450 000 000; ultimate parent of a group reaching
  them; franchising royalties EUR 22 500 000 with turnover EUR 80 000 000; third country EUR 450 000 000
  in the Union; two consecutive financial years (2(5)); AIFs and UCITS excluded (2(8)). Recital (18) L65
  adds that the directive "does not apply to pension institutions operating social security systems under
  Union law". Recital (27) adds counting rules (seasonal workers, posted workers, branches, individual
  basis). Recital (62) L153 gives a publication deadline for the annual statement that differs from Article
  16(1)(b) for companies outside sustainability reporting.
- Other numbers: documentation kept 5 years (L375); policy reviewed every 24 months (L413); monitoring
  every 12 months (L623); statement within 12 months of the balance sheet date (L633); transition plan
  targets "for 2030 and in five-year steps up to 2050", updated every 12 months (L741, L753); penalties
  "not less than 5 %" of net worldwide turnover (L877); decisions public "at least five years" (L881; the
  recital says three); assistance reply 1 month, extendable by two (L895); limitation "at least five years"
  (L931).
- Lists: Article 3(1)(a)(iii) financial undertakings, 16 dashes (L289); annex Part I section 1, 16 points
  (L1179-L1209); section 2, 3 instruments plus the 8 ILO core conventions (L1213-L1233); Part II, 16 points
  (L1241-L1271).
- No company counts and no cost figures anywhere in D02.
- Coverage (caller): articles 1-9 and 14-39, annex and recitals (18), (26)-(30), (62), (97)-(99) read in
  full; articles 10-13 and the other recitals scanned for numbers and dates only. That scan missed recital
  (18), which author run 2 found; treat any claim that the adopted text is silent on something as unproven
  until the recitals have been searched for it. Author runs 1 and 2 read articles 1-39 and the annex in full
  and recitals 18, 24-35, 62 and 95-99; the remaining recitals by keyword.

## Shared ground (navigation only)

- D01 and D02 are two versions of one legal text: article by article the same subjects, different
  numbers (scope thresholds, timing, policy update cycle, statement deadline, review) and different lists
  (financial undertakings, annex instruments and prohibitions).
- D01's timing is relative to entry into force; D02 prints the actual dates and the entry-into-force date.
- D03 summarises the assessment behind D01; D01's memorandum (L217-L251) says how the proposal departs
  from it. D03 and D01 both state a review period, on different bases.
- Company-count estimates exist only in D01 (body L155, footnotes 62-63).
