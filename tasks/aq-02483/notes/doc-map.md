# aq-02483 - document map

Maintained by the caller from `text/` (plain-text Federal Register captures). Navigation only;
questions quote the documents, never this map. Line numbers are `text/DNN.txt` lines.

## Bundle

- What it is: one OSMRE final rule (Pennsylvania SMCRA program amendment, outlier topic) and five
  EPA proposed approvals of state coal combustion residuals (CCR) permit programs built on one
  template: Wyoming (2025), Virginia, Louisiana, Alabama, Wisconsin (2026).
- Documents: 6; D01-D06 = task page Doc 1-6 (alphabetical file order matches page order).
- Gaps: none. Capture header "Documents: 6 of 6 read in full (456,650 characters)"; intake
  `incomplete: false`, 0 gap characters for every document. Page note at capture time: "Docket has
  been updated. Reload this page so its checks and buttons keep working." (stale-page warning, not a
  text gap).
- Extraction spot-checks (2026-10-09, caller): plain text, no pages/PDF. Each DNN.txt equals its
  docs/ source plus a one-line header; checked D01's 30 CFR 938.15 table (L299-L331), footnotes in
  D02 (\1\-\12\, L106-L285) and D05 (\1\-\13\), FR page markers present in all. No tables or
  charts beyond D01's amendment table. All six read in full by the caller.
- Provenance: notes/intake.json (capture sha256 ddc00991...330d), complete capture.
- Reuse binding (text sha256): D01 6fb99f06..., D02 f268a3b2..., D03 3cc5f13a..., D04 f307f1ef...,
  D05 c1f09108..., D06 9014006d....

## D01 - OSMRE: Pennsylvania Regulatory Program (final rule, approval of amendment)

- Source: docs/fr_2025_11907.txt; 90 FR 27459-27467, June 27, 2025; effective July 28, 2025 (L29).
- Written by: Office of Surface Mining Reclamation and Enforcement (Interior); signer Ben Owens
  (L275); contact Thomas J. Koptchak (L31). PADEP = Pennsylvania DEP.
- Dates: program conditionally approved July 30, 1982 (L46) but "effective July 31, 1982" (L123)
  (internal inconsistency); amendment letter March 16, 2020 (L50); receipt announced Dec 17, 2020,
  comment period ended Jan 19, 2021 (L51); EPA concurrence requested March 18, 2020, received July
  13, 2023 (L206).
- Figures: civil penalty mandatory threshold $1,100 replaced by 31 points; 31 points = $4,499
  ("more than triple", L126-L127); temporary cessation 90-day limit / 180-day extension deleted
  (L103); 30-day cessation notice (L105); permit renewal at least 180 days before expiration (L109);
  remining: no bond NOV within previous three years (L147), 25% forfeiture trigger (L152).
- Terms: "fly ash" -> "coal ash", "sewage sludge" -> "biosolids or residential septage" (L185).
- Links to D02-D06: none substantive (different statute and agency). EPA appears only as concurrer.
- Coverage: full.

## D02 - EPA proposed approval: Wyoming partial CCR permit program

- Source: docs/fr_2025_16801.txt; 90 FR 42347-42355, Sep 2, 2025; Docket EPA-HQ-OLEM-2025-0221.
- Agency WDEQ (SHWD division; Environmental Quality Council). EPA Region 8. Contact Michelle Lloyd,
  "Materials Recovery and Waste Management Division" (L36; later docs give another division).
- Dates (L27, L90, L97): comments due Nov 3, 2025; hybrid hearing Oct 30, 2025; pre-register by
  Oct 30; accommodations by Oct 16. Application Feb 6, 2023 (L110, L148); EPA letters Mar 27, 2023
  and Dec 5, 2023; WDEQ letter Jan 29, 2024 (review period expired claim); EPA questions May 16,
  2025; WDEQ response June 20, 2025 (L154-L159). EPA began work Sep 2019 (L148).
- Federal amendment list: six (Aug 5 2016 ... Nov 8 2024), no Feb 10 2026 rule (L127).
- Units/resources (L267-L268): 19 disposal units (3 landfills, 16 surface impoundments) at 4
  facilities; STAG FY2021-2023, received $571,396.
- State rules: SWR ch. 18 effective Aug 19, 2022; adopts federal rules through Dec 14, 2020 (L278).
  Landfills regulated since 1990; impoundments since 1975 water rules.
- Partial program (L280-L290): four requirements not sought: (1) Legacy Rule amendments incl.
  257.50(e); (2) vegetative cover 257.73(a)(4) etc.; (3) 257.90(g); (4) 257.95(h)(2).
- State permits: none issued under ch. 18 (L302-L303). Existing SIs apply within 12 months of the
  State rule; landfills renew 12 months before permit expiry (L202). Two 30-day comment periods
  (L218-L221; each runs until 30 days after the second weekly notice). Penalty <= $10,000 per
  violation per day (L252). Tribes: Eastern Shoshone, Northern Arapaho; neither sought consultation.
- "entirety" of partial application approved (L179). Coverage: full.

## D03 - EPA proposed approval: Virginia partial CCR permit program

- Source: docs/fr_2026_08662.txt; 91 FR 23924-23934, May 4, 2026; Docket EPA-HQ-OLEM-2025-3325.
- Agency VADEQ (six regional offices; DCR dam safety). EPA Region 3.
- Dates: comments due July 6, 2026; hybrid hearing June 24; pre-register June 22; accommodations
  June 10 (L32, L84, L94). Application June 6, 2025, revised March 4, 2026 (L108, L144); EPA
  questions Sep 25, 2025 (L144, L333). Tribes: seven; letters Oct 8, 2025; Monacan and Rappahannock
  requested consultation; meeting Dec 1, 2025; Rappahannock withdrew Jan 26, 2026; Monacan done
  Mar 18, 2026 (L114).
- Federal amendment list: seven incl. Feb 10, 2026 (91 FR 5806) (L119).
- Units/resources (L226): 25 disposal units (7 landfills, 18 SIs) at 8 facilities; STAG FY2023-2025,
  received $571,396.00 (same figure as D02).
- State rules: incorporated by reference eff. Jan 27, 2016; May 3, 2017; Jan 15, 2025 (through Dec
  14, 2020) (L143, L242). Does not incorporate vegetative height or 257.90(g); reserves 257.50(e)
  (L243).
- Partial program (L245-L323): 20 Legacy amendments approved as State versions (L247-L272);
  not approved: 3 (veg cover; 257.90(g); 257.95(h)(2) - VADEQ SOUGHT approval but provision under
  reconsideration, L277); 12 "more prescriptive" (L279-L290); 10 legacy-SI items incl. 257.102(e)(4)
  (vi)/(vii) and 257.102(f)(1)(ii) (L292-L301); 17 CCRMU items (L306-L323).
- "majority" of application approved (L165). Existing permits: all CCR units permitted (applications
  due Oct 17, 2017, L329); excluded from review at VADEQ's request (L334-L349).
- State permit procedure: comment period >= 45 days, hearing >= 30 days after notice, >= 15 days after
  hearing (L195); major mods >= 30 days, may extend to 45 (L198); inspections at least yearly (L213);
  30 days comment on enforcement settlements (L220). Coverage: full.

## D04 - EPA proposed approval: Louisiana partial CCR permit program

- Source: docs/fr_2026_11312.txt; 91 FR 34189-34201, June 5, 2026; Docket EPA-HQ-OLEM-2025-3324.
- Agency LDEQ. EPA Region 6. Tribes on Feb 12, 2026 call: Chitimacha, Coushatta, Jena Band of
  Choctaw, Tunica-Biloxi; Jena Band asked notification re Cleco Brame Power Plant (L117).
- Dates: comments Aug 4, 2026; hybrid hearing July 21; pre-register July 17; accommodations July 7.
  Application May 20, 2025; EPA questions Sep 12, 2025; draft Dec 16, 2025; Feb 2, 13, 20, 23, 2026
  exchanges; revised Mar 2 and Mar 19, 2026 ("final" application Mar 19, L111, L147-L148). Work began
  June 2017 (L146).
- Units/resources (L290-L291): 9 disposal units (3 landfills, 6 SIs) at 4 facilities; STAG FY2023-
  2026, received $517,396 (digit order differs from D02/D03's $571,396).
- State rules: adopted Oct 20, 2024 (La. Reg. Vol 50 No 10); L308 says federal rules "as amended
  through July 1, 2022" with exceptions, L315 says "through December 14, 2020" (internal mismatch).
- Partial program: 20 Legacy amendments approved (L317-L338, same as D03); First: 3 State provisions
  not sought (veg cover; GWPS cobalt/lead/lithium/molybdenum - adopted but not sought; variances)
  (L340-L342); Second: 257.90(g) (L344); Third: 12 (L349-L360); Fourth: 8 legacy (L362-L369); Fifth:
  17 CCRMU (L371-L392); Sixth: exclusion of SIs that no longer contain water, not approved (L393-L394).
- Permits: none issued under Chapter 10 (L400-L401); apply within 365 days of program approval (L182,
  L400); renewal 365 days before expiry (L193-L194); term max 10 years (L202-L203). Public comment
  minimum 30 days, extendable to 45 or 60 (L225-L226); hearing request within 30 days; hearing notice
  20 days. Penalties <= $32,500 per day; <= $50,000 per day after order (L269-L270); settlement
  comment 45 days; hearing request by 25 persons. "entirety" approved (L169). Coverage: full.

## D05 - EPA proposed approval: Alabama partial CCR permit program

- Source: docs/fr_2026_14118.txt; 91 FR 43054-43066, July 14, 2026; Docket EPA-HQ-OLEM-2022-0903.
- Agency ADEM (EMC appellate body). EPA Region 4. Tribe: Poarch Band; letter May 26, 2026, declined
  June 2, 2026 (L117).
- Dates: comments Sep 14, 2026; virtual hearing Sep 3; pre-register Sep 1; accommodations Aug 20.
  Application May 18, 2026 (L25, L106, L162). History: applications July 12, 2018, Feb 26, 2021,
  Dec 29, 2021 (fn 7, L154); proposed denial Aug 14, 2023 (88 FR 55220); final denial June 7, 2024
  (89 FR 48774) (L158-L159). North Dakota final approval 90 FR 51168, Nov 17, 2025 (L161); ND proposal
  "94 FR 20985, 20995 (May 16, 2025)" (L402). Completeness letter July 2026 (fn 9).
- Units/resources (L276): 16 CCR units (3 landfills, 13 SIs) - no facility count; STAG awarded
  $1,069,479 + anticipated $203,390 = $1,272,869.
- State rules: ch. 335-13-15 effective June 8, 2018 (L396); mirror federal rules through Aug 28, 2020
  plus Nov 12, 2020 changes to 257.102(d)(3)(ii), 257.103(f)(1)(vi), excluding some 2018 provisions
  (L307). Variances limited to seven State-only provisions (L296-L303: 100-foot buffer; markers; six
  inches weekly cover; slope <= 4:1 (25 percent); final grade >= 5 and <= 25 percent; terraces every
  20 feet of rise on slopes longer than 25 feet).
- Partial program: 17 Legacy amendments approved (L309-L329; lacks Contains both CCR and liquids,
  Infiltration, Liquids); First: 4 not sought (GWPS; 257.103(f) analog; general definitions;
  unrelated regs) (L331-L336); Second: 5 not approved (3 definitions; 257.71(d); 257.90(g)) (L338-
  L343); Third 12; Fourth 8 legacy; Fifth 17 CCRMU.
- Existing permits (L397-L398): eight facilities, issue dates Dec 18 2020 (Miller, Greene County,
  Gadsden), May 25 2021 (Gaston), July 1 2021 (Barry), Aug 30 2021 (Lowman), Feb 28 2022 (Gorgas),
  Oct 25 2022 (TVA Colbert); listed out of date order. Excluded from review; no permit shield until
  reissued (fn 3; L421-L427).
- State permit procedure: term design life, max ten years (L208); renewal >= 180 days before expiry
  (L210); transfer notice >= 30 days; modification application >= 120 days before change (L214);
  notice >= 35 days; 35-day comment period (L240); EMC hearing request within 30 days; civil
  penalties up to $25,000 per violation (L265). "majority" approved (L106, L179). Coverage: full.

## D06 - EPA proposed approval: Wisconsin partial CCR permit program (landfills only)

- Source: docs/fr_2026_18552.txt; 91 FR 57842-57854, Sep 11, 2026; Docket EPA-HQ-OLEM-2026-4324.
- Agency WDNR. EPA Region 5. 14 tribal letters, July 2026 (fn 3, L120) - letters, not a tribe count.
- Dates: comments Nov 10, 2026; online hearing Nov 9; pre-register Nov 5; accommodations Oct 26.
  Application Feb 24, 2026 (cover letter dated Feb 20, 2026, fn 5); supplement Aug 13, 2026 (L152);
  completeness letter "signed September 2026" (fn 8). Work began 2020.
- Units/resources (L290-L294): 9 CCR units (6 landfills, 3 SIs) at 6 facilities; the 3 SIs stay with
  EPA; STAG FY2021-2025, received $1,303,485 "from EPA".
- State rules: solid waste program since 1992; CCR updates effective Aug 1, 2022 (L306); reflect
  federal rules through Aug 28, 2020 for landfills (L308); no SI rules.
- Partial program: 11 Legacy amendments approved (L310-L320); First: State provisions not approved
  (NR 504.04(2) exemptions a-e, 289.43(7), CCR pile definition) (L324-L338); Second: SI provisions stay
  federal, 30-item non-exhaustive list (L339-L396); then 1-3 (veg cover, 257.90(g), 257.95(h)(2)),
  4: 12 more prescriptive, 5: 8 legacy, 6: 17 CCRMU (L398-L449).
- Permits (L456): six landfills had to submit plan-of-operation modifications by Feb 1, 2023; text says
  WDNR "issued permits" to all six, then "As of February 2026" only three approved, two on comment,
  one gathering information (internal mismatch). Existing plans excluded from review (L462-L474).
- Procedure: no license expiry; plan updated every 10 years (L192); modification review 65 business
  days, expedited 30 calendar days (L202-L204); 60-day/30-day comment periods with a draft-decision
  60-day (L217) vs 30-day (L228) mismatch; 6 or more persons may request a meeting; forfeiture $10 to
  $25,000 per violation, each day separate (L266-L268). "entirety" approved (L174). Coverage: full.

## Shared ground (navigation only)

- Template boilerplate repeated in D02-D06: statutory 180-day, 12-year/3-year/1-year reviews, 60-day
  comment period, five/three-minute testimony, 40 CFR part 239 framework, permit-shield text.
- Series: D02 lists six federal amendments; D03-D06 list seven (Feb 10, 2026 rule added).
- Identical figure across documents: $571,396 (D02, D03); look-alike $517,396 (D04).
- Identical lists: Legacy "approved" list D03 = D04 (20); "more prescriptive" 12 and CCRMU 17 lists
  identical in D03-D06; legacy-SI list 10 in D03 vs 8 in D04-D06.
- Cross-citations: D05 cites EPA's North Dakota approval (not in bundle); no document cites another
  bundle document. D01 has no CCR-program link.
- Scope relationships: D06 landfill-only scope; D03/D05/D06 exclude existing permits; D02/D04 have
  issued none.
