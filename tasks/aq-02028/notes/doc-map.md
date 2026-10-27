# aq-02028 - document map

Maintained by the caller from four bundle-mapper parts (notes/map/partA-D.md, merged below) and the
caller's own targeted reads. Navigation only, like the form's bundle overview: where things are, not
what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: twenty submissions (February 2022) to the Productivity Commission's inquiry into the
  long-term productivity of Australia's maritime logistics system, each by a different organisation
  (terminal operator, road/transport and freight associations, farm, food, wine, meat, steel, aluminium,
  cement, housing, mining, competition regulator ACCC, National Competition Council, ship operators).
  Unrelated authors on one topic; no editions of one series.
- Documents: 20; ids D01-D20 from `text/manifest.json`; page Doc N = Dnn (alphabetical file order equals
  page order: sub007 ... sub048).
- Gaps: none in the capture (intake.json: every document `incomplete: false`, `gap_characters: 0`,
  `matches_capture: true`; page: "20 of 20 read in full (541,861 characters)"). Charts/figures exist in
  the originals only as captions or flattened axis numbers (e.g. D11 TAC chart, D07 Figures 1-3, D12
  Figure 1 values as a flattened row, D20 Attachment 1); their plotted values are unavailable unless
  printed in text. Treat any chart-only value as a gap.
- Extraction spot-checks (2026-10-08, caller): plain-text sources, no pages. For all 20, text/Dnn.txt
  equals tools/extract_text.py normalise(source) exactly (header line added). Only normalised characters:
  U+2026 ellipsis -> "..." twice in D06 and five times in D07 (avoid quoting those spans). Each source file
  ends with the capture's "-----" separator. Representative flattened table checked: D02 Attachment A
  (L174-178, rows run together on 5 lines; values and effective dates intact) and D05 Figure 2 (L88-102,
  tab-separated). Footnotes present inline (e.g. D10 L29-31, L52-62).
- Provenance: notes/intake.json (capture AQ-02028_2026-10-08_0734.txt, capture_sha256 feafc31c1ee6...),
  source sha256 per document there; no recovered-source history.
- Reuse binding (source sha256 prefix / text sha256 prefix):
  D01 e6b76e53/ada3a4fd · D02 e2b35709/098d5cd6 · D03 1df70ca9/5e81661f · D04 78cdee4b/39b2c52f ·
  D05 1d652c64/c24ace02 · D06 632dd4a7/a6570993 · D07 9d7abd14/c5cc19d2 · D08 d3c0863e/d7ef93dd ·
  D09 e742cfaa/74f7bd8e · D10 24c68e24/0ef7f259 · D11 728999cc/e49287fb · D12 92d27314/1b222448 ·
  D13 ba7d1739/759956fd · D14 eed81ecf/58dc4c93 · D15 28ccb908/147d82a5 · D16 410297dc/06199465 ·
  D17 3afe656b/3af0b826 · D18 b30734e0/1ace7c37 · D19 c86be22b/6fc8c79a · D20 ae04a84e/28ee851d

## Caller's targeted reads (2026-10-08)

- D01 full read (L1-109). D18 full read (L1-94). D02 L1-140 and L168-286 (all but L141-167). D10 full
  read (L1-128). D12 L19-62. D06 L36-44, L110-118, L136-156. D08 L125-136, L200-240. D11 L40-66.
  D13 L215-256, L326-348. D09 L15-20, L55-100, L150-162. D07 L99-150, L340-372, L418-470.
  D05 L84-118. D19 L76-100, L326-350. D20 L9-14 (via grep), L76-86, L115-207. D14 L9-14.
- Mapper parts below supersede these notes for completeness; these reads verify specific passages.

<!-- Mapper parts merged below this line. -->

## Mapper parts (full per-document entries; bound to the source hashes above)

Each part holds the template's per-document entries with line-cited facts, a shared-ground section and
a whole-bundle "Repeats elsewhere" section. All 20 documents were read in full, line by line:

- [part A](map/partA.md): D01 L1-110, D04 L1-78, D07 L1-704 (8 chunks), D14 L1-58, D18 L1-95.
- [part B](map/partB.md): D11 L1-128, D12 L1-111, D15 L1-142, D17 L1-139, D19 L1-703 (8 chunks).
- [part C](map/partC.md): D02 L1-287, D10 L1-129, D13 L1-381, D16 L1-170, D20 L1-208.
- [part D](map/partD.md): D03 L1-263, D05 L1-312, D06 L1-170, D08 L1-324, D09 L1-177.

Unresolved (no visual originals; not unread): chart data in D07 Figures 1-5, D11 charts, D12 Figure 1
colours/bars and Figure 2, D20 Figure 1 and Attachment 1, D01 images; D16 Attachments 1-2 and link;
D13 footnote 1 text and a truncated bullet (L308); D02 Attachment B column alignment and the "bolded"
sentence; D05 survey-table alignment (L119-127); D17 contact list (empty in source).

## Shared ground (navigation only; details and locations in the parts)

- Stevedore infrastructure surcharges / terminal access charges: per-terminal rates only in D02 Attachment A
  (L174-182, as at 25 January 2022, Patrick rates dated 7/03/2022, Flinders Adelaide 1/04/2022; prose L137
  "1 March 2022"); histories and approximations in D02 Table 1 (L106-113), D03 L96, D08 L131/L206, D13 L222,
  D19 L336; definitions D11 L54, D16 L153, D13 L222.
- Coastal Trading Act and the January 2022 flood exemption: D06 L40/L152 (until 31 March 2022, only dated
  source), D19 L205, D17 L24; licensing D14 L28-48, D20 L27-196, D19 L86-97; scope tension D14 L29 vs D20 L81.
- ACCC Container Stevedoring Monitoring Report 2020-21: D10 (own submission; release 3 Nov in text, 4 Nov in
  fn 1) vs D05/D09 "October 2021"; quoted in D02, D06, D11, D13, D15, D16.
- World Bank/IHS Markit CPPI: D10 L39, D06 L133, D13 L120, D05 L209, D09 L86, D16 L112-118 (no exact ranks).
- Port Botany volumes: D09 L107 (2.6m TEU in 2019; capacity at least 7.2m) vs D13 L167-174 (2.7m today to 8.4m
  by 2045; road/rail shares inconsistent with volumes).
- Port of Melbourne volume: D01 L33 (over 2.88m TEU) vs D08 L147 (about 3m TEU, VPMF Q3).
- Seafarer shortage: D17 L42 vs D19 L256/L558 (MIAL 2018 census, different figures).
- Patrick/MUA and Svitzer events: D10 L43-44, D05 L251, D19 L322.
- Same numeral, different label: 68% (D05 SA wine share; D09 resources share); 430,000 (D07 vehicles; D13
  Port Botany rail); $140 (D08 per TEU; D19 $140m; D03 $140 million).
