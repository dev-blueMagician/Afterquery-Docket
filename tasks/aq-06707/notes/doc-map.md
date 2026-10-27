# aq-06707 - document map

Maintained by the caller from `text/` (plain-text originals). Navigation only: where things are, not
what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: nine Vertex Pharmaceuticals quarterly earnings releases (8-K Ex. 99.1), Q2 2024 - Q2 2026.
  Calendar fiscal year. Task page "Corporate filings · Hard only"; slots "Hard 0/5 · Medium closed · Easy 0/0".
- Documents (local id = page Doc): D01 = Doc 6 Q1 2025 (filed 2025-05-05); D02 = Doc 2 Q1 2026 (2026-05-04);
  D03 = Doc 9 Q2 2024 (2024-08-01); D04 = Doc 5 Q2 2025 (2025-08-04); D05 = Doc 1 Q2 2026 (2026-08-03);
  D06 = Doc 8 Q3 2024 (2024-11-04); D07 = Doc 4 Q3 2025 (2025-11-03); D08 = Doc 7 Q4 2024 (2025-02-10);
  D09 = Doc 3 Q4 2025 (2026-02-12). Ids sort by filename, not by date.
- Gaps: none. Capture "9 of 9 read in full"; every docs/ file matches its captured bytes (notes/intake.json).
- Extraction spot-checks: plain-text sources, so text/ equals docs/ plus a header. Checked per document: the
  income statement, revenue table with footnote, both reconciliation tables and the balance sheet render as
  pipe tables with labels, units ("in millions") and column years intact; page-number lines remain as bare digits.
- Coverage: all nine documents read in full by the caller on 2026-10-18 (every line).
- Reuse binding: corpus sha256 4c77cc3440878327 (notes/mine.md header); per-document hashes in text/manifest.json.

## Common layout (every release)

Headline bullets; quarter results prose (revenue, combined GAAP/non-GAAP opex, tax rates, net income, cash);
guidance prose + table; business highlights (CF, CASGEVY, JOURNAVX); pipeline; non-GAAP definitions; income
statement; product/total revenue table with footnote; two GAAP-to-non-GAAP reconciliation tables with notes;
balance sheet (two dates); About; forward-looking statements; contacts. Tables are in $ millions.

## Changes in presentation across the series (locations)

- Combined non-GAAP opex: 2024 releases print "Combined non-GAAP R&D and SG&A expenses" (D03 l.289, D06 l.283,
  D08 l.298), AIPR&D separate; 2025-26 releases print "Combined non-GAAP R&D, AIPR&D and SG&A expenses" and
  restate the 2024 comparatives (D01 l.280 Q1 2024 1,018.5; D04 l.270 Q2/H1 2024; D07 l.254; D09 l.275 Q4/FY
  2024 1,297.4 / 8,821.7). D03 l.48 footnote: May 6, 2024 guidance had used the AIPR&D-inclusive measure.
- Revenue: 2024 releases report "Product revenues, net" only; from D01 "Other revenues" (Q1 2025 10.0, Q2 2025
  20.7, none later) and "Total revenues". 2024 guidance = product revenue; 2025-26 guidance = total revenue.
- Revenue table: D03 "Other CF products"; D06 "Other product revenues" with no footnote although D06 l.83 says Q3
  2024 product revenue included revenue from the first CASGEVY patient infused; D08, D01, D04, D07, D09 footnote
  the CASGEVY/JOURNAVX amounts inside "Other product revenues"; D02, D05 print "Other CF product revenues",
  "Total CF product revenues, net", CASGEVY and JOURNAVX as separate lines.
- Interest: separate "Interest income" / "Interest expense" through D09; D02, D05 print "Interest income, net".
- Balance sheet: "Long-term finance lease liabilities" through D01 (Mar 31, 2025: 111.4); from D04 merged into
  "Other long-term liabilities" (Dec 31, 2024 shown as 1,014.6 in D04/D07/D09 vs 901.8 + 112.8 in D08/D01).
- Non-GAAP exclusion lists: D03/D06/D08 six items; D01/D04/D07/D09 add "(vi) an intangible asset impairment
  charge"; D02/D05 drop "acquisition-related costs".

## CASGEVY and JOURNAVX facts (navigation)

- CASGEVY revenue ($M): Q3 2024 2.0 (D07 l.227 prior-year; not in D06); Q4 2024 8.0, FY 2024 10.0 (D08 l.272,
  D09 l.248); Q1 2025 14.2 (D01 l.255, D02 l.224); Q2 2025 30.4, H1 44.6 (D04 l.243, D05 l.240); Q3 2025 16.9,
  9M 61.5 (D07 l.227); Q4 2025 54.3, FY 115.8 (D09 l.248; prose "$54 million", "$116 million" D09 l.83);
  Q1 2026 42.9 (D02 l.224; "$43 million" l.75); Q2 2026 76.4, H1 2026 119.3 (D05 l.240; "$76 million" l.71).
- CASGEVY infusions: D06 l.83 first patient infused in Q3 2024 (no count); D04 l.72 since launch through June 30,
  2025: 29, incl. 16 in Q2 2025; D07 l.74 since launch through Sep 30, 2025: 39, incl. 10 in Q3 2025; D09 l.83
  in 2025: 64, incl. 30 in Q4 2025. No count for Q1 2025, 2024, or 2026 anywhere.
- CASGEVY first cell collections (approximate except D09): D08 l.96 "more than 50" by end 2024; D01 l.76 ~90 by
  May 1, 2025; D04 l.72 ~115 by June 30; D07 l.74 ~165 by Sep 30 incl. 50 in Q3; D09 l.83 147 in 2025.
- JOURNAVX revenue ($M): Q1 2025 "an insignificant amount" (D01 l.255), 1.3 in D02 l.225; Q2 2025 12.0, H1 13.3
  (D04 l.243); Q3 19.6, 9M 32.9 (D07 l.227); Q4 26.7, FY 59.6 (D09 l.248); Q1 2026 29.0; Q2 2026 49.6.
  Prescriptions are all approximate ("more than", "approximately").

## Guidance series (navigation)

- FY2024: product revenue 10.55-10.75 -> 10.65-10.85 (D03) -> 10.8-10.9 (D06); non-GAAP R&D+SG&A 4.2-4.3 (D03,
  D06); AIPR&D ~4.6B; non-GAAP ETR ~100% (D03) -> ~90% (D06).
- FY2025: total revenue 11.75-12.0 (D08) -> 11.85-12.0 (D01, D04) -> 11.9-12.0 (D07); combined non-GAAP
  R&D+AIPR&D+SG&A 4.9-5.0 -> 5.0-5.1 (D07); GAAP 5.55-5.7 -> 5.65-5.8 (D07); ETR 20.5-21.5% -> 17-18% (D07).
- FY2026: total revenue 12.95-13.1 (D09, D02) -> 13.1-13.2 (D05); non-CF >= $0.5B; non-GAAP opex 5.65-5.75;
  ETR 19.5-20.5%; D05 excludes the pending Crinetics acquisition ($85.00/share, ~$10.0B equity value).

## Shared ground (navigation only)

- Every release prints the prior-year quarter (and YTD) as comparatives, so each quarter Q1 2024 - Q2 2026 is
  printed somewhere; Q1 2024 only as D01's comparative; 2023 periods only in the 2024 releases.
- Balance sheets: each release prints its quarter-end and the prior December 31. The prose "cash, cash
  equivalents and total marketable securities" (rounded, $B) equals the first balance-sheet line plus
  "Long-term marketable securities".
- Pipeline facts repeat with edits (mine.md section 1), e.g. AGLOW "24-patient" (D02, D07, D09) vs "26-patient"
  (D05); ADPKD population 250,000 (D03, D06) vs 300,000 (D08).
