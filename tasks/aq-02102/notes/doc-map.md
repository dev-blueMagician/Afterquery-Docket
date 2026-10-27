# aq-02102 - document map

Maintained by the caller (Opus 5.5, 2026-10-08) from `text/`. Navigation only, like the form's bundle
overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: five UK Cabinet Office papers. Four cover the Civil Service Pension Scheme 2015 (McCloud) remedy:
  the 2021-22 prospective-remedy consultation and its response, and the 2023 retrospective-remedy consultation
  and its response. The fifth is a 2017 consultation on reforming the Civil Service Compensation Scheme.
- Documents: 5. Local ids are alphabetical by file name and differ from the task page's Doc N:
  D02 = Doc 1, D01 = Doc 2, D04 = Doc 3, D03 = Doc 4, D05 = Doc 5 (notes/intake.json).
- Gaps: none. Capture says "5 of 5 read in full (407,424 characters)"; intake.json marks every document complete and
  matching the capture. All five texts read in full by the caller on 2026-10-08.
- Extraction spot-checks: plain-text captures (method text, no pages). Each Dnn.txt was compared with its docs/ file
  (same body; the extractor adds only a header line). Tables are flattened: D02/D01 EQIA Table 1 (protection status)
  reads in label/value order and sums check (D01 L709-754 is the cleaner layout); D02/D01 Table 3 (age by
  protection type) is scrambled in both and is not used. D03 Tables 1-2 are Markdown pipe tables. Footnotes are
  URL lists (D02 L1034-1060, D01 L1231-1251, D03 L639-689).
- Provenance: notes/intake.json (capture AQ-02102_2026-10-08_1256.txt, sha256 fc4ca8ab...), no history.
- Reuse binding: text/manifest.json sha256 per document (D01 77077ea6..., D02 5d065d3a..., D03 7784dcae...,
  D04 a29c7636..., D05 19937e7b...).

## D02 - Doc 1 - Civil Service Pension Scheme: 2015 Remedy and civil service member contributions (consultation)

- Source: docs/Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt (1,430 lines)
- Written by: Cabinet Office (L20). Back cover reads "Crown copyright 2018" (L1413), an artefact.
- Dates: begins 22 November 2021 (L8); cover says "ends on 17 January 2021" (L9, a typo); duration "From 22/11/2021
  to 17/01/2022" (L32); "Please send your response by 16 January 2022" (L356); response "due to be published by
  10 February 2022" (L56). Draft regulations come into force 1 April 2022, reg 3 effective from 1 April 2015 (L1185).
- Content: prospective remedy (move all active PCSPS members to alpha from 1 April 2022, L130, L209-211); added
  pension 12-month bar (L213-221); ill-health underpin incl. classic commutation comparison (L223-269); six
  consultation questions (L272-346); member contributions 2022/23 rollover (L284-323); technical amendments to regs
  121, 142, 173, Sch 1 para 7, Sch 2 paras 16/17/25/26 (L295-318).
- Tables: Annex C 2022/23 bands and rates (L1064-1099: £0-£23,100 4.60%; £23,101-£56,000 5.45%; £56,001-£150,000
  7.35%; £150,001+ 8.05%); same table in draft reg 4 (L1195-1209). Only Doc 1 prints the rates.
- EQIA (Annex B, L461-1060): 419,000 in scope (L474); Table 1 protection status at 31 March 2016 (L512-561; components
  sum to 464,001 against a printed 464,002); "39,000 active members of the legacy scheme" at 30 June 2021 (L577);
  30,000-40,000 to move by 1 April 2022 (L583); Table 4 sex by scheme, Civil Service 47% male / 53% female (L788-829);
  "53.8% of Civil Servants are women" (L836); diversity statistics (L845, L917, L957, L962).
- Glossary (L1103-1150): alpha accrual 1/43 or 2.32% (L1105); tapered protection 10 to 13.5 or 14 years (L1146).
- Draft regulations (Annex E, L1156-1400): reg 3 omits "if it is impractical to pay it" from reg 121(4); reg 5
  reg 142(4) "95(2)" to "95(2A)"; reg 6 reg 173(2) "31st July" to "6th October".
- Coverage: full.

## D01 - Doc 2 - consultation response (prospective remedy and 2022/23 contributions)

- Source: docs/Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt (1,254 lines)
- Written by: Cabinet Office (L11). "This response is published on 4 March 2022" (L6).
- Dates: consultation 22 November 2021 to 17 January 2022 (L59, L121, L131); union meetings 7 and 9 December 2021
  (L148); 2016 valuation results 17 December 2021 (L102, L542); High Court dismissed PSA claim "On Wednesday 15
  December" (L370-371); pay pause 25 November 2020 with £250 rise under £24,000 (L570); Royal Assent expected
  early March (L626); DCU planned October 2023 (L379, L473).
- Response statistics: 3.7 (L174): 1,268 responses which directly addressed the questions (1,263 individuals, five
  unions: Prospect, FDA, PCS, DPF, GCG a branch of PCS), plus Audit Wales, plus 32 individuals who did not address the
  questions. Table 1 by question (L181-237). Table 2 (L239-278): Individuals 1,295 / of which queried the effect 32 /
  of which personalised 24 / Unions 5 / Other organisations 1 / Total Received 1,301. Template used by 1,239 of
  1,268 (L282). Annex A respondent organisations (L631-649; "Individuals - 1295").
- Table/text conflicts: Table 1 Q4 "5 raised additional considerations" (L213) vs 4.34 "Seven respondents" (L483).
- Policy changes against Doc 1: reg 121 redrafted (L611-617); reg 142 amendment dropped (L619); survivor benefits
  rule reworded (L420, L452); SMA receipt date added (L404, L448); contributions unchanged after the valuation found
  "0.4% below the employer cost cap" within the "2% corridor" (L102, L542, L568, L627).
- EQIA (L653-1229): same tables as Doc 1 but "39,000 deferred members" (L769) and remedy period "(31 March 2015 - 31
  March 2022, for most civil servants)" (L696); LFS sources differ.
- Coverage: full.

## D04 - Doc 3 - Civil Service Pensions 2015 Remedy (McCloud) consultation (retrospective remedy, 2023)

- Source: docs/Civil-Service-Pensions-2015-Remedy-McCloud-consultation.txt (1,333 lines)
- Written by: Cabinet Office (L4). No launch date printed; respond "by 23:59 on 14 May 2023" (L1220).
- Figures: around 420,000 offered a choice; nearly 120,000 immediate choice (L84-86); RSS within 18 months of 1
  October 2023 (L22, L452, L522); immediate choice within 12 months of the RSS (L146); opted-out election after 1
  October 2023 and before 30 September 2024 (L358); partnership contributions 0 to 3% (L366, L380); deferred choice
  windows (L237-257); pension credit request 6 months after the statement, default PCSPS, one scheme only (L616-630);
  Judgments Act rate "currently 8%" for money the scheme owes (L1142); first ABS-RSS by 31 August 2024 (L534).
- Issued to: NTUC, non-affiliated unions, Civil Service Pensioners Alliance, employers, Network Voice Advisory Group
  (L100-110). Three consultation questions (L1182-1192).
- Coverage: full.

## D03 - Doc 4 - Civil Service Pensions 2015 Remedy consultation response (2023)

- Source: docs/Civil-Service-Pensions-2015-Remedy-consultation-response.txt (689 lines)
- Written by: Cabinet Office. Consultation 6 March to 14 May 2023 (L28, L87); in force 1 October 2023 (L67), laid
  early September (L543).
- Engagement: meetings 21 March, 19 April, 4 May, 23 April, 3 May, 18 April 2023 (L127-133). "Unions engaged during
  the consultation process" (L137-161): NTUC unions PCS, Prospect, FDA, GMB, POA UK (Prison Officers' Association),
  Unite; non-affiliated DPF, ISU, NCOA, Prison Governors' Association. (L131 calls the CSPA "CPSA".)
- Response statistics: 3.9 (L189): 107 responses which in some way addressed the questions (102 individuals, five
  organisations) plus ten individuals who did not address the questions. Table 1 by question (L195-199); Table 2
  (L201-209): Individuals 102 / of which queried the effect (i.e. didn't answer the consultation questions in all
  respects) 68 / Unions Prospect PCS DPF 3 / Other organisations CSPA, Pen-gage 2 / Total 107. Annex A (L549-563)
  with memberships (CSPA over 40,000; Prospect over 155,000; PCS 194,000). Themes 17/14/10/10% (L177-183).
- Table/text conflicts: Q2 text "nine ... sufficient" (L509) vs Table 1 10 + 2; Q3 text "ten had no concerns; 11 did"
  (L527) vs Table 1 14 no / 10 yes.
- Policy changes against Doc 3: pension credit members keep both accounts, choice within 12 months of 1 October 2023
  (L491); interest owed to members at the Employment Tribunals regulations rate up to 28 days after the RSS (L487);
  partial-retirement clarification and aggregation provision (L515-521).
- Other: WPS 1.5% within the equalised rates (L271); added-pension buyers 49% male / 51% female (L535); added years
  contracts until February 2008 (L375).
- Coverage: full.

## D05 - Doc 5 - Consultation on reform of the Civil Service Compensation Scheme (2017)

- Source: docs/Consultation-on-reform-of-the-Civil-Service-Compensation.txt (395 lines)
- Written by: Cabinet Office (L24). Launched 25 September 2017; respond by 6 November 2017 (L6-8, L114).
- 2016 history (L61-71): offer 26 September 2016, "agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON,
  Unite, NCOA, the Defence Police Federation and PGA)" (L65); not agreed by POA and PCS; PCS judicial review July
  2017 (L67); reformed scheme of 9 November 2016 quashed (L71). PGA is never spelled out.
- Proposals (L289-305): tariff three weeks' pay per year; VE and VR capped at 15 months; CR 9 months; employer-funded
  top-up from 55, ten years behind State Pension Age. HMT framework incl. £80,000 salary cap (L198-216); 2016 proposal
  VE 18 / VR 12 months (L269); savings around a third (L338).
- Coverage: full.

## Shared ground (navigation only)

- Respondent and union entities: Doc 2 L174/L631-649 (2021-22 respondents); Doc 4 L137-161 (engaged), L201-209 and
  L549-563 (2023 respondents); Doc 5 L65-67 (2016 offer). Name variants: "Public and Commercial Services Union" vs
  "Public and Communication Services Union" (Doc 2 L639, Doc 4 L559); "The Association of First Division Civil
  Servants FDA" (Doc 2 L637); "POA UK" vs "Prison Officers Association (POA)"; "PGA" (Doc 5 only) vs "Prison
  Governors' Association" (Doc 4 only); "Network Voice Advisory Group" (Doc 3 L110) vs "Civil Service Network
  Advisory Group" (Doc 4 L103).
- Proposal/response pairs: Doc 1 -> Doc 2 (2021-22); Doc 3 -> Doc 4 (2023). Doc 2 and Doc 4 each print a Table 2
  "response method and source" with an "Individuals" row and a total, under different inclusion conventions.
- Repeated EQIA: Doc 1 and Doc 2 Annex B share Table 1, Table 2, Table 4-6 and the diversity prose.
- Dates across documents: Doc 1's promised response date (10 February 2022) vs Doc 2's publication (4 March 2022);
  Doc 3's deadline (14 May 2023) vs Doc 4's dates (6 March-14 May 2023, 1 October 2023).
