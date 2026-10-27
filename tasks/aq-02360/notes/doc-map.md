# aq-02360 - document map

Maintained by the caller (Opus 5.5, 2026-10-09) from `text/`. Navigation only, like the form's bundle
overview: where things are, not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: the same five UK Cabinet Office papers as tasks/aq-02102, aq-02165 and aq-02198 (fourth task on these
  bytes). Docs 1-4: Civil Service Pension Scheme 2015 (McCloud) remedy, 2021-22 prospective consultation (Doc 1) and
  response (Doc 2), 2023 retrospective consultation (Doc 3) and response (Doc 4). Doc 5: 2017 Civil Service
  Compensation Scheme consultation.
- Documents: 5. Local ids are alphabetical by file name: D02 = Doc 1, D01 = Doc 2, D04 = Doc 3, D03 = Doc 4,
  D05 = Doc 5 (notes/intake.json).
- Gaps: none. Capture AQ-02360_2026-10-09_0125.txt (sha256 c7e9069b...) "5 of 5 read in full (407,424 characters)";
  its DOCUMENTS section is byte-identical to the three earlier captures (md5 5487f9c5...). All five texts read in full by
  the caller on 2026-10-09.
- Extraction spot-checks: as tasks/aq-02198/notes/doc-map.md (plain-text captures; Dnn.txt = docs/ file plus a header;
  Doc 1/2 EQIA Table 1 reads label/value, components sum to 464,001 vs printed 464,002; Table 3 scrambled; Doc 4 Tables
  1-2 pipe tables; footnotes are URL lists).
- Reuse binding: text/ sha256 per document equal to tasks/aq-02198/text (checked 2026-10-09), so its map and
  tasks/aq-02102/notes/doc-map.md apply unchanged, with their measured platform results.
- Twin check (this session): a word diff of the two EQIAs (Doc 1 Annex B vs Doc 2 Annex B) finds no figure difference,
  only wording, sources (LFS Q1 2021 vs Q1/Q3 2020), "39,000 active" vs "deferred", and Doc 2's "(31 March 2015 – 31
  March 2022 ...)". No EQIA figure can make Doc 1 or Doc 2 necessary.

## Facts relevant to this session's sketches

- Doc 1 (D02): draft amending regulations "come into force on 1st April 2022 but regulation 3 has effect from 1st April
  2015" (L1185); draft regulation 5, heading "Amendment of regulation 142 (transfer of payments made to other schemes or
  pension arrangements)" (L1219), text "In regulation 142(4), for “95(2)” substitute “95(2A)”." (L1220); paragraph 3.3
  describes it as correcting "a cross reference to the wrong subsection of the Pension Schemes Act 1993" (L308-310).
  These are the only printings of "95(2)", "95(2A)" and of regulation 142's heading.
- Doc 2 (D01): same list of proposals (L583-585, no subsection numbers); paragraph 4.61 "Cabinet Office has decided not
  to proceed with the amendment of regulation 142 ..." (L619), the only statement of the drop. Regulation 121 redrafted
  (L611-617). No other technical amendment is said to be dropped.
- Doc 3 (D04): opted-out service election "received by the scheme manager after 1st October 2023 but before 30
  September 2024, or later if the scheme manager considers there are reasonable circumstances to extend the deadline"
  (L358), the only statement of the window. No launch date; respond "by 23:59 on 14 May 2023" (L1220).
- Doc 4 (D03): consultation "began on 6 March 2023 and closed on 14 May 2023" (L28), also L87 and L109 ("launched on 6
  March 2023"), the only printings of the launch date; advance notice "In February 2023" (L99); look-alike date "members
  retiring up to 30 September 2023" (L441); opt-in process "not yet been finalised" (L465), no window dates.

## Shared ground (navigation only)

- See tasks/aq-02198/notes/doc-map.md (entities, proposal/response pairs, draft -> final changes, differing
  definitions, pay and contributions, dates across documents).
