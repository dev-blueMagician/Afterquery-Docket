# aq-02940 - document map

Maintained by the caller, with two `bundle-mapper` part files, from `text/`. It is for navigation,
like the form's bundle overview: where things are, not what to ask. Questions quote the documents,
never this map.

## Bundle

- What it is: the New Zealand Commerce Commission's June-July 2026 consultation on capping Mastercard
  and Visa commercial credit card interchange fees: the Draft Decision and Reasons Paper, the
  Commission's merchant survey results, and 14 submissions (six banks, Mastercard plus its Keystone
  economic report, Paymark, Revolut, the Financial Services Federation, Retail NZ, the Restaurant
  Association).
- Documents: 16; ids from `text/manifest.json`. Local ids are alphabetical by file name and differ
  from the task page's Doc numbers:

| Local | Platform | Author / document | Date | Chars |
| --- | --- | --- | --- | --- |
| D13 | Doc 1 | Commerce Commission, Draft Decision and Reasons Paper | 4 June 2026 | 157,141 |
| D09 | Doc 2 | Commerce Commission, Merchant Survey Results (slide pack) | published 23 July 2026 | 25,363 |
| D01 | Doc 3 | ANZ Bank New Zealand submission | 16 July 2026 | 10,637 |
| D02 | Doc 4 | ASB Bank submission | [20 July] 2026 | 19,874 |
| D03 | Doc 5 | Bank of New Zealand submission | 17 July 2026 | 7,939 |
| D04 | Doc 6 | Citibank N.A. New Zealand submission | 17 July 2026 | 13,878 |
| D05 | Doc 7 | Financial Services Federation submission | 13 July 2026 | 6,724 |
| D06 | Doc 8 | Keystone report for Mastercard ("Mastercard Submission to the NZCC") | May 21, 2026 | 165,770 |
| D07 | Doc 9 | Kiwibank submission | 17 July 2026 | 11,160 |
| D08 | Doc 10 | Mastercard submission | 16 July 2026 | 41,088 |
| D12 | Doc 11 | Retail NZ submission | 20 July 2026 | 15,694 |
| D14 | Doc 12 | Revolut Payments New Zealand submission | 20 July 2026 | 26,498 |
| D15 | Doc 13 | TSB Bank submission | 20 July 2026 | 14,221 |
| D16 | Doc 14 | Westpac New Zealand submission | 21 July 2026 | 15,184 |
| D10 | Doc 15 | Paymark submission | 30 June 2026 | 14,311 |
| D11 | Doc 16 | Restaurant Association of New Zealand submission | 20 July 2026 | 10,312 |

- Gaps: none known in the capture ("16 of 16 read in full (555,752 characters)"; `notes/intake.json`
  matches_capture true and gap_characters 0 for all 16). Figures are captions only: D13 Figures 1.1,
  1.2, 2.1, 4.1 (bars and the indicative timeline dates are not in the text); D06 Figure 1; D08
  Figures 1-2; D09 chart labels survive as number strings without axes. Redactions inside D02 (ASB's
  own figures) and D07 (terminal provider name, loss examples) are in the originals.
- Extraction spot-checks: plain-text captures, extraction is a copy with a one-line header (constant
  2-line offset between docs/ and text/). Checked: D13 Table 3.1 (L570-581) and Table C.1 (L1195-1206)
  against docs/ (same strings; column grid lost, values run in row order); D13 footnote 119 (L938);
  D06 fn 172 (L705); D09 Q22 slide (L358-367).
- Provenance: `AQ-02940_2026-10-11_1200.txt`, saved 2026-10-11 12:00; capture note "Docket has been
  updated. Reload this page so its checks and buttons keep working."; source hashes in
  `notes/intake.json` and `text/manifest.json`.
- Reuse binding: source sha256 per document in `text/manifest.json` (2026-10-11). No earlier task
  shares these bytes or this family (searched the workspace captures for "nzcc"/"Commerce Commission").
- Coverage: D13, D09, D01, D02, D04, D07, D08, D10, D11, D12, D14 (L20-206), D15, D16 and D03 read in
  full by the caller; D06 L641-854 read by the caller and L1-854 by the mapper
  ([doc-map-D06.md](doc-map-D06.md)); all 14 short documents also mapped line by line in
  [doc-map-submissions.md](doc-map-submissions.md). D05 (FSF) read by the mapper only.

## D13 (Doc 1) - Draft Decision and Reasons Paper

- Source: `docs/nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt`,
  72 printed pages (page numbers stand alone on lines).
- Written by: Commerce Commission. Date 4 June 2026. Submissions due 12pm Monday 13 July 2026 (L117,
  L212, L1132); merchant survey open until 5pm Monday 29 June 2026 (L1129).
- Period of the data: monitoring data December 2024 to November 2025 (fn 17 L194, fn 31 L276, fn 68
  L565); base period December 2023 to November 2024 (fn 32 L278); acquirer fee data April 2023 to
  March 2024 (fn 9 L133, fn 119 L938).
- Headline money (annual, Mastercard and Visa commercial credit, domestic plus foreign-issued):
  interchange "approximately $125 million" (X4 L66, 1.4 L132, 2.8 L272) = "around 19% of total
  interchange fees paid" on "8% of the total value of transactions"; merchant service fees
  "approximately $170 million" (1.4 L131); draft decision reduces interchange "by $50 million" (X14
  L105, 1.15 L175) and merchant service fees "by approximately $40 million" (X14 L105, 2.14 L324, 4.2
  L932, 4.3 L936: "imperfect cost pass-through"); fn 119 L938: pass-through assumptions "more
  conservative compared to the 90% in the Final Decision published in July 2025".
- Proposed caps (Table X1 L98-103, 1.14 L169-174, Table 3.1 L570-581): domestic in-person 0.50%,
  online 0.90%; foreign-issued in-person 0.70%, online 1.50%. Column note "Or interchange fees per
  transaction as at 1 December 2025, whichever is lower" (fns 7, 16, 67).
- Table 3.1 (L570-581; grid lost). Columns: Current rates | Australia caps | December 2024 Draft
  decision | Proposed caps May 2026 | Current weighted average | Implied weighted average | Australia
  weighted average. Domestic in-person 0.20-2.20% | 0.80% | 0.20% | 0.50%; online 0.20-2.20% | 0.80%
  | 0.40% | 0.90%; domestic Total 1.39% | 0.78% | 0.78%. Foreign-issued in-person 1.85%-2.05% | 1.00%
  | 0.60% | 0.70%; online 1.85%-2.05% | 1.00% | 1.15% | 1.50%; foreign Total 1.99% | 1.37% | NA. "All
  foreign-issued cards" 1.77% | 1.09% | 1.75%.
- Shares: foreign-issued card-not-present share "(83%)" (3.47 L806); no domestic online share is
  printed. SMEs 86% of domestic commercial credit transaction value (2.36 L416, 3.18 L636); "small and
  medium - defined as less than 20 employees", 97% of businesses (2.35 L403). Foreign-issued cards 11%
  of total transactions vs 3% in Australia, 30% vs 20% of interchange (3.52 L821). fn 82 L665:
  commercial credit about 7% of domestically issued card value, interchange share 19% to 20%.
- Premium structure: base debit 0.20% in person (2.25.1 L366); +0.10% personal credit (2.25.2 L368);
  +0.40% online (2.25.3 L369); commercial +0.20% over personal credit (X8 L77, 3.6 L588) = 0.10% for
  issuer costs and trade-account benefit (3.7.1 L591) + 0.10% for stable market outcomes / Australia /
  American Express (3.7.2 L593). Foreign-issued commercial credit = foreign personal credit caps, no
  extra premium (X10 L91, 3.43 L786). "%" for caps and premiums means percentage points (fn 5 L88).
- Limiting mechanism (X16 L114, 3.2 L552, 3.66-3.76 L876-910): lower of the applicable cap or the
  published category rate at the reference date 1 December 2025 (3.71 L897-900, 3.74 L906), including
  changes back-dated to that date (3.69 L893); category level (3.72 L902); "domestic commercial credit
  card transactions only" (3.73 L903; Attachment B Q6 L1171). Earlier mechanism: initial pricing
  standard in force 13 November 2022, anchor 1 April 2021, removed July 2025 (3.66 L876).
- Implementation: "two to three-month implementation period from our final decision" (3.80 L921);
  "final quarter of 2026" (X15 L112). Previous decision issued 17 July 2025, implemented 1 December
  2025 (3.74 L906).
- Other rates: current weighted average domestic "around 1.40%" and foreign "around 2%" (2.3 L246-248);
  June 2025 ranges 0.45%-2.20% and 1.85%-2.35% (fn 27 L257); Australia 0.80% cap retained, 1.0% on all
  foreign-issued from 1 April 2027 (2.28 L381, 3.46 L802); growth December 2024-November 2025:
  interchange on domestic commercial credit +9% vs transaction value +6% (2.9 L273).
- Virtual card numbers: processed card-not-present, so online caps apply (3.64 L863).
- Footnote cost data: fraud losses about 20% higher for commercial, 0.01-0.02% of transaction volume
  (fn 94 L724); RBA cost study admin costs 0.22%/0.28% (excluding majors) and 0.57%/0.40% (all issuers)
  (fn 96 L738).
- Attachment B: nine targeted questions (L1138-1191). Attachment C Table C.1 current caps (L1195-1206):
  domestic debit in-person contacted 0.00%, contactless 0.20%, online 0.60%; personal credit 0.30% /
  0.70%; foreign-issued debit 0.60% / 1.40%; personal credit 0.70% / 1.50%.
- Internal inconsistency: the December 2024 draft decision is dated 18 December 2024 in "Associated
  documents" (L30-31) and 13 December 2024 in fn 66 (L562).
- Coverage: full (L1-1210 read by the caller).

## Other documents

Per-document entries with line numbers are in the part files:

- [doc-map-D06.md](doc-map-D06.md): D06 (Doc 8) Keystone report, L1-854 in full, with indexes of
  tables, lists, hedges, regulator figures, year-tied events and repeated or conflicting figures.
- [doc-map-submissions.md](doc-map-submissions.md): D01-D05, D07-D12, D14-D16, each in full.

## Shared ground (navigation only)

- Restated Draft Decision figures: four proposed caps, the 0.20-point premium and its 0.10 + 0.10
  split, $170 million, $125 million and $40 million in D11 L17-36 (which alone prints "approximately
  $1 billion per year overall to accept Visa and Mastercard payments"); $125 million and $40 million
  in D10 L26; $40 million in D16 L39; 0.78% implied weighted average in D07 L54 and "78bps" in D04
  L104. The $50 million interchange reduction, the other Table 3.1 averages and the 83% share appear
  only in D13.
- Pass-through of interchange cuts to merchant service fees: D13 ($40 million of $50 million; 90% in
  July 2025, fn 119); D06 L694 and fn 172 L705 (Spanish study, 1% lower interchange with 0.39% lower
  merchant service fees in the long run; EC 2020 review, L694 and fn 171); D16 L39 (Westpac: "passed on
  fully"); D08 L36-49 (three-step chain, Richmond Fed 77/22/1 per cent); D14 L95-101.
- Implementation periods requested: Commission two to three months (D13 L921); ANZ April 2027 release
  or minimum 6 months (D01 L29); ASB no earlier than 8 months (D02 L48, L137); BNZ at least six months
  (D03 L46); Citi minimum twelve months (D04 L133); Kiwibank at least six months (D07 L84); Mastercard
  nine months domestic, twelve cross-border (D08 L123, L236); Westpac minimum six months, 1 March 2027
  at the earliest (D16 L91); Retail NZ and the Restaurant Association support two to three months (D12
  L106, D11 L59).
- Cap levels proposed by submitters: ASB flat 1.1% everywhere and 50 bps over personal credit caps as
  a starting point (D02 L22, L32); Mastercard interim differential matching an observed gap "in the
  order of 40 basis points" in place of the 10-point one (D08 L80, L140, L172); Retail NZ same level as
  personal cards (D12 L65, L102); Restaurant Association align with personal caps or keep only the
  evidenced premium (D11 L32); Kiwibank: own implied average 0.63%, Government interchange 0.20% (D07
  L52-54).
- Limiting mechanism positions: remove (D01 L42, D08 L110, L142); support (D11 L44, D12 L104);
  accounted for in averages (D07 L52, D04 L104).
- New Zealand commercial card spend: "$7.2bn in 2023 to $8.2bn in 2026" (D06 L307); "NZD8.2 billion"
  against AUD119 billion (D16 L56); 1.9 per cent of GDP against 4.3 per cent (D08 L92, L169); GDP USD
  260 billion and USD 1.76 trillion (D04 L45).
- Surcharging figures: D01 L50-52 (8% to 26% of terminals; fee 1.35% to 0.91%; surcharge 2.24% to
  2.02%; 91% to 94%); D08 L41-46 (20%, 49%, 57% of merchants; "more than $90 million"); D16 L43 and D14
  L105 ("~$150 million", "$45-65 million"); D14 L108 (44%, 1.50%); D12 L38 (66% do not surcharge).
- Small-business definitions: D13 L403 ("small and medium - defined as less than 20 employees"); D06
  L311 ("Small businesses (those with fewer than 20 employees)"); D09 L51 size groups 0-19, 20-99, 100+.
- Australia: 0.80% commercial cap retained, consumer cap 0.3%, averages 0.78 and 0.47 per cent (D06
  L791-794); "50-bps interchange premium" and July 2017 cap history (D02 L25, L62); D13 Table 3.1.
