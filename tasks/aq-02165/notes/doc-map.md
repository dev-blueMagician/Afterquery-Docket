# aq-02165 - document map

Maintained by the caller (Opus 5.5, 2026-10-08) from `text/`. Navigation only, like the form's bundle
overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: the same five UK Cabinet Office papers as tasks/aq-02102 (byte-identical sources). Docs 1-4 are the
  Civil Service Pension Scheme 2015 (McCloud) remedy papers: 2021-22 prospective-remedy consultation and response,
  2023 retrospective-remedy consultation and response. Doc 5 is the 2017 Civil Service Compensation Scheme consultation.
- Documents: 5. Local ids are alphabetical by file name and differ from the task page's Doc N:
  D02 = Doc 1, D01 = Doc 2, D04 = Doc 3, D03 = Doc 4, D05 = Doc 5 (notes/intake.json).
- Gaps: none. Capture AQ-02165_2026-10-08_1602.txt says "5 of 5 read in full (407,424 characters)"; intake.json marks
  every document complete and matching the capture. All five texts read in full by the caller on 2026-10-08.
- Extraction spot-checks: plain-text captures (method text, no pages); each Dnn.txt equals its docs/ file plus a header
  line. Tables are flattened (Doc 1/2 EQIA Table 1 reads in label/value order; Table 3 scrambled, not used); Doc 4
  Tables 1-2 are pipe tables. Footnotes are URL lists.
- Provenance: notes/intake.json (capture sha256 98a7aeca...), no history. Reuse binding: text/manifest.json sha256 per
  document equals tasks/aq-02102's (D01 77077ea6..., D02 5d065d3a..., D03 7784dcae..., D04 a29c7636..., D05 19937e7b...),
  so that bundle's map (tasks/aq-02102/notes/doc-map.md) and its measured results apply to these bytes.

## D02 - Doc 1 - 2015 Remedy and civil service member contributions (consultation, Nov 2021)

- Cabinet Office. Begins 22 November 2021 (L8); cover "ends on 17 January 2021" (L9, typo); "From 22/11/2021 to
  17/01/2022" (L32); "send your response by 16 January 2022" (L356); response "due ... by 10 February 2022" (L56).
- Contributions: rollover of 2021/22 rates and thresholds for 2022/23 (L321-323); history of extensions (L288-291);
  pay pause "above £24,250" (L323). Annex C bands/rates (L1064-1099) and draft reg 4 (L1195-1209): 4.60% / 5.45% /
  7.35% / 8.05% at £23,100 / £56,000 / £150,000. Only Doc 1 prints the rates.
- EQIA Annex B (L461-1060), shared with Doc 2: Table 1 protection status at 31 March 2016 (L512-561); 419,000 in scope
  (L474); "39,000 active members" (L577); civil service statistics (L836, L845, L917, L957, L962).
- Glossary: alpha 1/43 = 2.32% (L1105); tapered protection 10 to 13.5 or 14 years (L1146).

## D01 - Doc 2 - response (published 4 March 2022)

- Response statistics 3.7 and Tables 1-2 (L174-278); template 1,239 of 1,268 (L282).
- DPF extract (L349-365): Home Office police NPA "age 60" (L357); "The MOD has agreed to fund a lower NPA for MDP
  officers by paying for an effective pension age equal to three years below State pension age" (L359); "about 5% of
  pay" (L363). Only Doc 2 states the MDP arrangement.
- EPA answer 4.36 (L510): "In alpha the NPA is the same as the State Pension Age (SPA), or 65 if the SPA is over 65"
  (wording garbled against the real rule; do not build on its "65" clause).
- Member quote 4.34 (L496): "retiring before age 67 (the new NPA under Alpha rules)".
- Contributions decision: valuation "0.4% below the employer cost cap", "2% corridor" (L102, L542); pay pause 25
  November 2020 with "£250 rise for workers earning under £24,000" (L570); 2022/23 "same percentages and salary bands
  as the current year" (L627), no rates printed.
- Drafting changes: reg 121 redrafted (L611-617), reg 142 dropped (L619). EQIA repeats Doc 1 (L653-1229) with "39,000
  deferred members" (L769) and different LFS dates.

## D04 - Doc 3 - retrospective-remedy consultation (2023; no launch date printed)

- 420,000 offered a choice; nearly 120,000 immediate choice (L84-86). RSS within 18 months of 1 October 2023 (L22,
  L452, L522); immediate choice within 12 months of the RSS (L146); opted-out election window to 30 September 2024
  (L358); partnership contributions 0 to 3% (L366, L380); pension credit request 6 months after statement (L626-630);
  Judgments Act interest "currently 8%" (L1142); contributions equalised in 2015, four earnings bands (L724).
- Respond by 23:59 on 14 May 2023 (L1220).

## D03 - Doc 4 - response (2023)

- Consultation 6 March to 14 May 2023 (L28, L87); in force 1 October 2023 (L67). Unions engaged (L137-161); response
  statistics (L189-209); themes 17/14/10/10% (L177-183); WPS "basic 1.5% ... accounted for in the equalised contribution
  rates" (L271, only source); ET-rate interest to 28 days after the RSS (L287); pension credit top-up choice within 12
  months of 1 October 2023 (L491); added years contracts until February 2008 (L375); added-pension buyers 49% male /
  51% female (L535); DPF "representing the federated ranks of the Ministry of Defence Police (MDP)" (L561).

## D05 - Doc 5 - Civil Service Compensation Scheme consultation (2017)

- Launched 25 September 2017, respond by 6 November 2017 (L6-8). 2016 offer agreed by eight of ten unions incl. "the
  Defence Police Federation" (L65); 2016 scheme quashed, 2010 terms in force (L71).
- HMT framework (L198-216) incl. £80,000 salary cap (only source). Proposals (L289-305): three weeks' pay per year; VE
  and VR 15 months; CR 9 months; "employer funded top up to pension from age 55 and for this to track 10 years behind
  State Pension Age" (L301-305); restated L328 and L344 (only source of the top-up rule). 2016 proposal VE 18 / VR 12
  (L269); early access "for those aged as young as 50" under the 2010 terms (L252).

## Shared ground (navigation only)

- Respondent and union entities: Doc 2 L174/L631-649; Doc 4 L137-161, L201-209, L549-563; Doc 5 L65-67.
- Proposal/response pairs: Doc 1 -> Doc 2 (2021-22); Doc 3 -> Doc 4 (2023). EQIA repeated in Doc 1 and Doc 2.
- Pension-age rules relative to State Pension age: Doc 5 (top-up age, SPA minus 10), Doc 2 (MDP effective pension age,
  SPA minus 3; alpha NPA = SPA). DPF links Doc 2 (respondent), Doc 4 (MDP staff association) and Doc 5 (2016 offer).
- Dates across documents: Doc 1's promised response date vs Doc 2's publication; Doc 3's deadline vs Doc 4's dates.
