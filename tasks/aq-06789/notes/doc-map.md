# aq-06789 - document map

Caller map, 2026-10-18 (Claude Opus 5.5, all nine `text/` files read in full this session). Navigation only:
questions quote the documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: nine unrelated GAO products, 2003-2008, on consumer-protection oversight (task page title
  "GAO Consumer Protection Oversight"). Same bundle as aq-01188 (2026-10-05/06): same file names; eight
  documents equal line for line after whitespace and Markdown-escape normalisation, D01 differing only in
  its two tables' layout (pipe rows then, tab rows now). The aq-01188 map (`tasks/aq-01188/notes/doc-map.md`)
  is valid for content; its line numbers are not (the old copies carried extra blank lines).
- Documents (local id = platform Doc): D01 = Doc 1 toy guns (GAO-03-1135R, Sep 30, 2003); D02 = Doc 2 NFIP
  testimony (GAO-05-532T, Apr 14, 2005); D03 = Doc 5 alternative mortgage products testimony (GAO-06-1112T,
  Sep 20, 2006); D04 = Doc 4 OCC consumer assistance (GAO-06-293, Feb 23, 2006); D05 = Doc 3 insurance-sector
  preparedness (GAO-06-85, Nov 18, 2005); D06 = Doc 6 bankruptcy credit counseling testimony (GAO-07-778T,
  May 1, 2007); D07 = Doc 9 long-term care insurance testimony (GAO-08-1016T, Jul 24, 2008); D08 = Doc 8 fair
  lending data testimony (GAO-08-1023T, Jul 17, 2008); D09 = Doc 7 NFIP wind/flood report (GAO-08-28, Dec 28, 2007).
- Gaps (absent from the originals, not extraction faults; carried from the aq-01188 map and seen again):
  D01 Table 1 body; D02 Appendix I chart values; D03 Figures 1-2; D04 footnote bodies, Figures 1-3 values,
  Appendix II letter; D05 footnote bodies, Figures 1-2, Appendix II letter; D09 Figures 1-2 bodies and
  Appendix II letter. None bears on i01 or i02.
- Extraction: plain-text capture split by `split_capture.py`, all nine `matches_capture: true`, no
  clipping; D01 Tables 2-3 rows checked against the capture (1985-1989 values and totals); D07 Figure 1
  written out as 46 state rows (CT ... WI) with its note and the Massachusetts sentence below "[End of figure]".
- Form number window: D09's figures from about L185 onward sit past character 27,000 (D09 L119-121
  repeat whole paragraphs), outside the form's reasoning number check.

## Shared ground (navigation only)

- NFIP, two editions: D02 (Apr 2005) and D09 (Dec 2007). FEMA NFIP staff "about 40" (D02 L67, L119, L170)
  vs "about 68" as of Sep 2007 (D09 L187); contractors "about 170" both; WYO share "about 95 percent" with
  the other 5 percent direct (D02 L172, fn 7 L186) vs "About 96 percent" (D09 L153); WYO claim allowance
  "about 3.3 percent of the incurred loss" (D02 L195) = "3.3 percent of each claim settlement amount" (D09
  L222); limits $250,000 / $100,000 in both; claims: program total "about $12 billion" since inception (D02
  L96), Isabel 23,770 claims for $454.2 million (L99), 2004 storms 59,125 claims, more than $1.3 billion,
  closed claims as of Mar 2005 (L101); Katrina over $15.7 billion as of Aug 31, 2007 (D09 L185, fn 21 L311),
  Katrina and Rita about $16.2 billion, averages over $95,000 and $47,000 "respectively" (L304); property-
  casualty Katrina payments about $22.4 billion excluding flood (L185). FEMA agency staff about 2,500 in
  Mar 2003 (D02 fn 1 L84).
- Federal bank regulators: D04 (OCC, Fed, FDIC, OTS: complaint process, outcome ranks L160-194, complaints
  per $billion L198-200, referral shares L179, feedback surveys L152-154, timeliness L208-211), D03 (five
  regulators' AMP steps L148), D08 (five ECOA regulators L126; four contacted L160). No figure is shared.
- State insurance regulators and NAIC: D05 (five unnamed states), D07 (ten named states, fn 4 L515; NAIC LTCI
  model and 2000 standards), D09 (eight coastal states L243, L282). No figure is shared.
- Hurricanes: Isabel (D02, D09 L300), 2004 storms (D02), Katrina (D05 L173, L203; D09), Rita (D04 L268; D09).
- Single-document structures with quiet levers but no partner document: D07 Figure 1 vs the Massachusetts
  phase-in sentence (L421) and Louisiana fn 19 (L546); D07 loss-ratio grandfathering (L132, fn 13 L534); D04
  reported vs complaints-only timeliness (L209-211) and 7 vs 8 phone hours (L97, L282); D03 fn 2 128% vs 44%
  (L206-207); D06 930,000 vs 650,000 certificates (L143, L170).
