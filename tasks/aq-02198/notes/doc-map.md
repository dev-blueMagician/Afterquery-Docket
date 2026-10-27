# aq-02198 - document map

Maintained by the caller (Opus 5.5, 2026-10-08) from `text/`. Navigation only, like the form's bundle
overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: the same five UK Cabinet Office papers as tasks/aq-02102 and tasks/aq-02165 (byte-identical sources and
  extractions). Docs 1-4 are the Civil Service Pension Scheme 2015 (McCloud) remedy papers: 2021-22 prospective-remedy
  consultation and response, 2023 retrospective-remedy consultation and response. Doc 5 is the 2017 Civil Service
  Compensation Scheme consultation.
- Documents: 5. Local ids are alphabetical by file name and differ from the task page's Doc N:
  D02 = Doc 1, D01 = Doc 2, D04 = Doc 3, D03 = Doc 4, D05 = Doc 5 (notes/intake.json).
- Gaps: none. Capture AQ-02198_2026-10-08_1809.txt (sha256 f76ef596...) says "5 of 5 read in full (407,424
  characters)"; intake.json marks every document complete and matching the capture. All five texts read in full by
  the caller on 2026-10-08 (this session, not only via the reused maps).
- Extraction spot-checks: plain-text captures (method text, no pages); each Dnn.txt equals its docs/ file plus a header
  line. Tables are flattened: Doc 1/2 EQIA Table 1 (protection status) reads in label/value order (Doc 2 L709-754 is the
  cleaner layout; components sum to 464,001 against the printed 464,002); Table 3 is scrambled in both and is not used;
  Doc 4 Tables 1-2 are pipe tables. Footnotes are URL lists. Doc 1 Annex C (L1064-1099) checked against draft reg 4
  (L1195-1209): same four bands and rates.
- Reuse binding: text/manifest.json sha256 per document equals tasks/aq-02102's and tasks/aq-02165's (D01 77077ea6...,
  D02 5d065d3a..., D03 7784dcae..., D04 a29c7636..., D05 19937e7b...). Their maps
  (tasks/aq-02102/notes/doc-map.md, tasks/aq-02165/notes/doc-map.md) and their measured platform results apply to
  these bytes.

## Facts added by this session's full read (not in the reused maps)

- Doc 1 (D02): pay pause "above £24,250" (L323); 2021/22 rates rolled into 2022/23 (L321-323), so Annex C is also the
  2021/22 table; draft reg 4 inserts after the table headed "Scheme Year 1st April 2021 to 31st March 2022" (L1195),
  band 1 "Up to but not including £23,101" (L1200). Classic commutation comparison for the IHR underpin (L257-263), absent
  from Doc 2's restatement. EQIA sources LFS Q1 2021 (L884, L940, L991). Draft reg 3 (reg 121) effective 1 April 2015
  (L1185). Glossary: CARE "The Civil Service version is alpha" (L1113); unprotected = moved 1 April 2015 or joined after
  (L1150).
- Doc 2 (D01): £250 rise for workers earning under £24,000, pay pause announced 25 November 2020 (L570); two members
  pushed into the next band by pay rises (L564). PCS asks for remedy within 90 days of the regulations becoming law
  (L347). Exec summary misdates the HMT consultation close as February 2021 (L51); EQIA gives 16 July-11 October 2020
  (L694). IHR application date = receipt by the Scheme Medical Adviser on or before 31 March 2022 (L404, L448). EQIA
  sources LFS Q1 2020 / Q3 2020 (same values as Doc 1). "39,000 deferred members" (L769) vs Doc 1 "39,000 active".
- Doc 3 (D04): rollback population described as members "too young to receive transitional protection and ...
  compulsorily transferred ... on or after 1 April 2015", then "This applies to all members who were moved to the new
  scheme on or after 1 April 2015" (L130). Opted-out election window after 1 October 2023 and before 30 September 2024
  (L358). Club transfers: LGPS exception (L882). EEPA list = certain NOMS and Scottish Prison Service grades (L778).
  Classic members could not join partnership on opting out until 2018 (L412). Statutory RSS deadline = the day after
  the 18-month period starting 1 October 2023 (L522).
- Doc 4 (D03): ET-rate interest to 28 days after the RSS "or if later, the date of payment" (L287, ambiguous end);
  member-owed interest at NS&I Direct Saver (L285); employer-funded EPA neither refunded nor converted if PCSPS is
  chosen (L369); members retiring up to 30 September 2023 get an immediate choice later (L441); pension credit
  members keep both accounts, top-up choice "must be given within 12 months of 1 October 2023" (L491); club transfers
  only with schemes reformed 2014-2016 (L399); LGPS handled differently (L407); glossary CARE = nuvos and alpha (L577),
  unprotected = "Members who were moved to alpha on 1 April 2015" (L635), EEPA 65 to 60 (L589); Annex A misnames PCS
  "Public and Communication Services Union" (L559), as Doc 2 Annex A does (L639).
- Doc 5 (D05): HMT framework vs CSCS proposal: the £80,000 salary cap is in the cross-public-sector framework list
  (L206) but not in the CSCS proposal list (L289-305); EQIA: under 15 years' service lose via tariff, 15-22 years via
  tariff and cap (L375).

## Shared ground (navigation only)

- Respondent and union entities: Doc 2 L174/L631-649; Doc 4 L137-161, L201-209, L549-563; Doc 5 L65-67.
- Proposal/response pairs: Doc 1 -> Doc 2 (2021-22); Doc 3 -> Doc 4 (2023). EQIA repeated in Doc 1 and Doc 2.
- Draft -> final changes: Doc 1 reg 121(4) wording -> Doc 2 L611-617 redraft; Doc 1 reg 142 -> Doc 2 L619 dropped;
  Doc 3 pension credit (L616-630, one scheme, 6 months after statement) -> Doc 4 L491; Doc 3 JA-rate interest (L1142)
  -> Doc 4 ET-rate period (L287).
- Definitions that differ: "unprotected" Doc 1 L1150 vs Doc 4 L635; "CARE" Doc 1 L1113 vs Doc 4 L577.
- Pay and contributions: Doc 1 bands (L1064-1099, L1195-1209), pay pause £24,250 (Doc 1 L323, Doc 2 L145/L540);
  £250 rise under £24,000 (Doc 2 L570 only).
- Dates across documents: Doc 1's promised response date vs Doc 2's publication; Doc 3's deadline vs Doc 4's dates;
  HMT 2020 consultation (Doc 1 L496, Doc 2 L694); Doc 5 timetable.
