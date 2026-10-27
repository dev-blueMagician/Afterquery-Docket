# aq-06840 - document map

Maintained by the caller from `text/` (and `docs/` for layout). Navigation only; questions quote the
documents, never this map. Line numbers are `text/Dnn.txt` lines.

## Bundle

- What it is: eight Albemarle Corporation earnings releases (8-K Ex. 99.1), Q3 2024 through Q2 2026.
- Documents (local id = task-page Doc number): D05 = Doc 1 (Q3 2024, filed 2024-11-06); D07 = Doc 2 (Q4/FY 2024,
  2025-02-12); D01 = Doc 3 (Q1 2025, 2025-04-30); D03 = Doc 4 (Q2 2025, 2025-07-30); D06 = Doc 5 (Q3 2025,
  2025-11-05); D08 = Doc 6 (Q4/FY 2025, 2026-02-11); D02 = Doc 7 (Q1 2026, 2026-05-06); D04 = Doc 8 (Q2 2026,
  2026-08-05). Local ids follow filename order, not dates.
- Gaps: none. All eight read in full by the caller on 2026-10-18 (capture "8 of 8 read in full", 319,067 chars;
  `notes/intake.json` all complete, matches_capture true). Plain-text sources, no pages or images.
- Extraction spot-checks: each Dnn.txt equals its docs/ file plus a header line (sizes 33.8K-44.7K chars);
  tables kept as Markdown pipe rows; the platform shows the same rows space-separated (memory
  docket-capture-pipe-tables), so quotes of table rows are written without pipes.
- Provenance: capture AQ-06840_2026-10-18_1806.txt, sha256 822889a3...; per-document sha256 in intake.json.
  The capture noted a "Reload this page" banner; all eight documents were nevertheless present and complete.
- Reuse binding: corpus sha256 8909037f9d5a2ee0 (notes/mine.md header).
- Not a repeat bundle: no Albemarle document in 10.6, 10.7, 10.8 tasks/ or docket-capture (searched 2026-10-18).

## Common layout (every release)

Highlights (l.13-35), CEO quote, results table (Q vs prior-year Q), segment tables (Energy Storage,
Specialties, Ketjen; 2026 releases: Energy Storage, Specialties, "Corporate and all other"), outlook
tables, cash-flow and balance-sheet prose, statements (income statement: quarter and YTD; balance sheet;
"Selected Consolidated Cash Flow Data": YTD only; segment results), non-GAAP reconciliations (adjusted
net income, EBITDA, adjusted EBITDA with "% of net sales" columns), non-recurring item footnotes,
adjusted tax-rate table; later releases add FCF / operating cash flow conversion tables. Fiscal year =
calendar year. Amounts in thousands in statements, millions/billions in prose.

## Per-document notes

- D05 / Doc 1 (Q3 2024): Q3 OCF "$241 million" prose (l.25); 9M 2024 cash flow first-printed (OCF 701,394
  l.282; capex (1,330,062) l.285; no FX-forward line in investing). Adjusted EBITDA definition change of
  2024 explained only here (l.471: pre-tax Talison earnings vs net of tax; FY23 under new definition $3.5B,
  l.75, recon l.475-488). Diluted-share footnote (d) "more dilutive of" rule (l.77). FY2025 capex first
  range $800-900 million (l.37, l.55, l.135).
- D07 / Doc 2 (Q4/FY 2024): FY2024 cash flow first-printed (OCF 702,068 l.322; capex (1,685,790) l.325;
  separate "Inventory net realizable value adjustment" line l.305). OCF conversion 62% (l.534). FY2025
  outlook introduced ($700-800M capex, l.29, l.150).
- D01 / Doc 3 (Q1 2025): Q1 2025 cash flow first-printed (OCF 545,383 l.290, capex (182,624) l.292, no
  FX-forward line; FX effect 80,207 l.308). $350 million customer prepayment (l.23, l.146; conversion table
  l.455-463 incl. "excluding customer prepayment $195,383").
- D03 / Doc 4 (Q2 2025): H1 2025 and revised H1 2024 cash flow (OCF 538,180 / 465,148 l.299; capex
  (302,252) / (1,034,593) l.301; new line "Proceeds from settlement of foreign currency forward contracts,
  net" l.304). Revision note l.324: "Certain 2024 values reflect presentation revisions ... misclassification
  errors" (+$4.3M OCF, +$5.3M investing, -$9.6M FX for the 2024 period presented). Grace preferred
  redemption $307M aggregate (l.25), $288,000 proceeds (l.303), $38.0M loss (l.434).
- D06 / Doc 5 (Q3 2025): FCF first defined ("operating cash flow minus capital expenditures", l.48). Q3 OCF
  "$356 million was up 57%, or $128 million" (l.25). 9M 2025 and revised 9M 2024 cash flow (OCF 893,782 /
  692,255 l.305; capex (434,416) / (1,337,719) l.307; FX-forward line (1,956) for 2024, l.310), no note
  that the 2024 column changed. Goodwill impairment $181.1M Refining Solutions, $175.7M after tax (l.429).
  Ketjen/Eurecat sale agreements ~$660M pre-tax (l.33). FY2025 FCF guide $300-400M (l.29, l.158).
- D08 / Doc 6 (Q4/FY 2025): FY2025 and revised FY2024 cash flow (OCF 1,282,267 / 687,876 l.330; capex
  (589,801) / (1,680,529) l.332; FX-forward (15,595) for 2024 l.335; inventories line 1,055,036 l.324),
  no note. FCF recon FY2025 $692,466 (l.541-544); conversion 117% (l.548). Long-lived impairment $245.6M
  (l.215, l.459); goodwill after tax now $181.1M (l.457). Eurecat closed $123M Jan 2026 (l.29).
  Ketjen held for sale (balance sheet l.253, 262, 272, 279). Jordan flood dated "January 2026" (l.139)
  beside Q4 2025 Jordan write-offs (l.471-473).
- D02 / Doc 7 (Q1 2026): Q1 2026 and revised Q1 2025 cash flow (OCF 346,244 / 547,207 l.293; capex
  (98,676) / (182,624) l.295; FX-forward 50,245 for Q1 2025 l.298; FX effect 28,138 l.314), no note. Prose
  "decreased $201 million" and "one-time $350 million customer prepayment" (l.142). Ketjen sale: loss on sale
  of business 95,018 (l.189, cash flow l.281), gain on sale of equity investment (42,300) (l.282), footnote
  "net loss of $52.7 million" for both sales (l.420). $648M combined net proceeds (l.27; cash flow 525,156 +
  123,270, l.296-297). Segment table recasts Ketjen into "Corporate and all other" (l.330-341). FCF recon
  $247,568 (l.463-469).
- D04 / Doc 8 (Q2 2026): H1 2026 and H1 2025 cash flow (OCF 1,056,241 / 538,180 l.300; capex (170,407) /
  (302,252) l.302); Q2 2026 FCF recon OCF 709,997, capex (71,731), FCF 638,266 (l.506-512); conversion 83%.
  Header: changes "do not exclude the prior-period results of Ketjen's refining catalyst solutions
  business" (l.15). Energy Storage volume/price table (l.62-69). Covenant leverage table TTM (l.522-536).

## Shared ground (navigation only)

- Same-period figures printed twice: Q3/9M 2024 (D05, D06), Q4/FY 2024 (D07, D08), Q1 2025 (D01, D02),
  Q2/H1 2025 (D03, D04), Dec 31 2024 balance sheet (D07, D01, D03, D06, D08), Dec 31 2025 (D08, D02, D04).
  Mechanical comparison (scratchpad samecmp.py / segcmp.py, 2026-10-18): only cash-flow rows differ:
  9M 2024 OCF 701,394 -> 692,255, capex 1,330,062 -> 1,337,719; FY 2024 OCF 702,068 -> 687,876, capex
  1,685,790 -> 1,680,529; Q1 2025 OCF 545,383 -> 547,207 (capex unchanged). H1 2025 identical in D03/D04.
  Income statements, balance sheets and segment figures identical (segment recast aside).
- Quarterly cash flow is never printed for Q2-Q4 except Q3 OCF prose (D05 $241M first basis; D06 $356M)
  and the 2026 FCF tables (Q1 2026 D02, Q2 2026 D04). Q4 2024 OCF is +674 first-printed, -4,379 revised.
- Forecast/actual: 2025 capex path D05 $800-900M -> D07/D01 $700-800M -> D03 $650-700M -> D06 ~$600M ->
  D08 actual 589,801; 2025 FCF D07 "breakeven" -> D03 "positive" -> D06 $300-400M -> D08 692,466; 2026
  Specialties ranges D08 -> D02 -> D04 raised twice.
- Ketjen: goodwill (D06), long-lived impairment (D08), sale loss (D02, D04); Eurecat separate.
