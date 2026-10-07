# aq-01432 - document map (index and cross-part shared ground)

Written once by four parallel `bundle-mapper` runs (2026-10-06) into part files, merged here by the
caller. Navigation only, like the form's bundle overview: where things are, not what to ask.
Questions quote `text/Dnn.txt`, never this map. Line numbers are `text/Dnn.txt` lines (L1 is the
inserted "# Dnn | docs/<file>" header).

## Bundle

- What it is: "Law and contracts", 11 plain-text consumer-protection documents. US (FTC): the
  16 CFR Part 465 reviews rule text, FTC staff Q&A on that rule (Nov 2024), FTC staff FAQ on the
  Endorsement Guides (June 2023), FTC staff ".com Disclosures" (March 2013). UK (CMA / gov.uk): CMA208
  fake reviews guidance (4 April 2025), short guide for review publishers, guidance for content
  creators on social media endorsements, "Who regulates hidden advertising?", CMA207 unfair commercial
  practices guidance, its worked-examples page, and the short business guide (all 2025).
- Documents (local id = platform Doc): D01 = Doc 1 (16 CFR 465), D02 = Doc 4 (.com Disclosures),
  D03 = Doc 2 (CRT Rule Q&A), D04 = Doc 5 (CMA208), D05 = Doc 3 (Endorsement Guides FAQ), D06 = Doc 6
  (short reviews guide), D07 = Doc 7 (creators' endorsements guidance), D08 = Doc 10 (UCP examples),
  D09 = Doc 9 (CMA207), D10 = Doc 11 (UCP business guide), D11 = Doc 8 (Who regulates hidden ads).
- Part files (complete, every line read; see each part's coverage ledger):
  - [doc-map-part1.md](doc-map-part1.md): D01, D03, D04, D06 (reviews: US rule + Q&A, UK CMA208 + short guide)
  - [doc-map-part2.md](doc-map-part2.md): D05, D07, D11 (endorsements and hidden advertising)
  - [doc-map-part3.md](doc-map-part3.md): D02 (.com Disclosures, 22 appendix examples, 30 notes)
  - [doc-map-part4.md](doc-map-part4.md): D08, D09, D10 (UK unfair commercial practices; all 32 banned practices indexed)
- Gaps: no unread ranges in any document. Source-absent material (not unread): D02 appendix mock-ad
  images (label text in Ex9/Ex12, Ex18 disclosures, Ex17 message count, page A-24), D07 two example
  images, D09 two alt-text tables (L103, L105) and one diagram (L319), D01 the Part 463 text before
  L5. List nesting depth is flat in the source at D09 L959-L1043, L537-L559, L873-L885.
- Extraction spot-checks: every text/Dnn.txt equals its docs/ original word for word after NFKC and
  whitespace collapse, except the inserted header line (caller check, all 11). Plain text: page
  count not applicable; no data tables; D02 printed folios (49) and page breaks (53) match the
  original; footnotes checked: D02 n22, D04 fn8, D09 fn38-39 and fn112, D11 fn1/fn4. NFKC changed two
  D02 characters ("80ºF" -> "80oF" L679; "¾" -> "3⁄4" L707).
- Provenance: notes/intake.json (capture AQ-01432_2026-10-06_1949.txt, sha256 f95b5fab...); all 11
  "incomplete": false, "matches_capture": true, gap_characters 0. Source total 427,653 chars vs the
  page's 427,642 (one trailing newline per document).
- Source-internal defects recorded by mappers (not resolved): D01 word-order garbling in
  § 465.2(a)/(b) L132-L161 and § 465.5(b)(1) L193-L195 (same in original); D09 chapter-10 footnote
  markers 116-123 misaligned with note texts; D09 fn39 repeated phrase and "10% or worldwide
  turnover"; D09 fn55 points to a section that is absent; D11 provision lists number "(ii)" twice.

## Shared ground across parts (navigation only)

Within-part shared ground is in each part file. Cross-part relationships:

- Same regulator, different instruments (US): D01 rule text; D03 staff Q&A on it (cites D01 sections,
  restates its definitions with small wording differences); D05 FAQ on the Endorsement Guides (16 CFR
  255, revised 2023; cited by section in D03 and D02, not in D05); D02 .com Disclosures (quoted by D05
  L331: "Use disclosures in each ad" = D02 L497, where it is addressed to space-constrained ads).
  Endorsement Guides history: D02 n10 L203 (2009 review added blog examples); D05 L27 (revised 2023,
  new definition of "clearly and conspicuously", not printed in D05). The rule's own "clear and
  conspicuous" definition is D01 § 465.1(c) L86-L100 ((c)(4) unavoidable; no hyperlink or hover),
  relevant only to § 465.5 per D03 L211. D02's factors: L274-L294 (hyperlinks allowed in some cases,
  Ex5/Ex6 adequate).
- Same regulator, different instruments (UK): D09 (CMA207 full guidance; replaces OFT1008 L21; 32
  banned practices L397-L763; offences chapter L1373-L1437; notes L1439-L1929) with its examples page
  D08 and short guide D10; D04 (CMA208; banned practice 13 in detail; D09 L573 and fn4 defer to it)
  with its short guide D06; D07 (content creators) and D11 (who regulates hidden ads). D09 fn94 L1813
  and D04 fn4 L113 / fn14 L245 name banned practices 12 and 25 as overlapping with 13; D11 lists BP12,
  BP13, BP25, professional diligence (ss225/229), misleading actions (ss225/226) and misleading
  omissions (ss225/227) for content creators (para 12 L69-L71), brands (para 17 L95-L98) and
  intermediaries (para 23 L123-L126); platforms: s225 professional diligence + BP13 (paras 20-21).
- Criminal and civil consequences (UK): D09 offences list L1387-L1411 (banned practices [fn112], ITP
  omissions, "most misleading actions" [fn113], misleading omissions, aggressive practices,
  professional diligence); strict liability except professional diligence (L1413, fn114 knew or
  reckless); fn112 L1885 and fn39 L1593: paragraphs 12, 13 and 30 of Schedule 20 are not criminal
  offences; fn39 civil penalties "up to the higher of £300,000 or 10% or worldwide turnover"; D10 L57
  "up to 10% of their worldwide turnover" (no £300,000); D09 L1381/L1419-L1433 criminal penalties;
  L1435-L1437 time limits (3 years / 1 year from discovery, whichever is earlier). No penalty text in
  D04, D06, D07 ("substantial fine" only, L15), D08 or D11.
- Penalties (US): D03 L9 civil penalties for knowing violations of the rule (no amount); D05 L91
  Notice of Penalty Offenses -> civil penalties; D01 no penalty text.
- Commencement and dates: UK provisions apply from 6 April 2025 (D09 L17, L115; D10 L63; D11 fn1
  L58); CMA208 dated 4 April 2025 (D04 L7); US rule SOURCE 89 FR 68077 Aug. 22, 2024 (D01 L79),
  effective October 21, 2024 (D03 L9 only), Q&A November 2024 (D03 L303); D05 June 2023 (L705); D02
  March 2013 (L3, L136), first edition May 2000 (L133), input sought from May 2011 (L135). D11 L75:
  January 2019 CMA undertakings from sixteen influencers (under the CPRs, fn3 L85).
- Previous-law relationships (UK): CPUTRs/CPRs 2008 replaced by DMCC Part 4 (D09 L15, D11 fn1);
  private redress stays under the CPUTRs until a new SI (D09 fn11 L1481); banned-practice numbers
  differ from CPUTRs Schedule 1, old numbers not given (D09 fn38 L1589); fake-review practice "new"
  (D04 L45; D09 L17, fn4).
- US vs UK treatments of the same conduct (locations only): incentives conditioned on sentiment (D01
  § 465.4 L185; D03 L141-L167) vs disclosed incentives allowed if genuine (D04 3.4-3.7 L251-L313) and
  D04 commissioning examples 1-6 (L285-L301); prize/contest entries (D01 (m) L120; D03 L155) vs prize
  draws "unlikely to amount to commissioning" (D04 fn8 L181); paying to change or remove reviews
  (D03 L161-L163, L261-L263) vs D04 commissioning example 4 (L295); soliciting only satisfied
  customers (D03 L113-L115) vs cherry-picking (D04 4.5 L368); hosting carve-out and no duty to
  investigate (D01 § 465.2(d)(2) L178; D03 L81-L83) vs positive duty to prevent and remove (D04 8.1-8.2
  L471-L473; D06 L63-L69; D11 para 21); platform responsibility (D05 L347) vs platforms' professional
  diligence (D11 para 20); own-brand posts (D05 L229 vs D07 L205); product placement (D05 L237 vs D07
  L57); label wording (D02 L499, Ex17 L810; D05 L357-L413; D07 L109-L169); detection red flags (D03
  L107 vs D04 8.19(b)(iii) L625).
- Issuers vs organisations merely named: FTC/FTC staff (D02, D03, D05; D01 has no issuer line); CMA
  (D04 by code; D09 by URL and self-references; D08, D10, D06, D07 gov.uk Crown copyright with CMA
  only mentioned; D11 no stated author). Named only: ASA, CAP, TSS, Buckinghamshire and Surrey TSS,
  Citizens Advice, Department for (the) Economy NI, FCC, CFPB, FDA, BBB, TikTok, ASA ruling subjects
  in D07 L207 (three named influencers).
- Overview exposure (capture BUNDLE OVERVIEW): Doc 1's summary lists "24 months recordkeeping period",
  which is the Part 463 tail (D01 L15), not Part 465. Doc 9 summary "32 specified banned practices";
  Doc 11 "10% of worldwide turnover fine"; Doc 8 "16 influencers undertakings, January 2019".
