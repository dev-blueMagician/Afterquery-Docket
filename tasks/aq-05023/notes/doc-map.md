# aq-05023 - document map

Maintained by the caller from `text/`. Navigation only, like the form's bundle overview: where things are,
not what to ask. Questions quote the documents, never this map.

## Bundle

- What it is: eight Cars.com Inc. (NYSE: CARS) filings, four Form 10-Qs and four earnings releases, for the
  quarters ended June 30, 2025, September 30, 2025, March 31, 2026 and June 30, 2026. Fiscal year = calendar
  year. No Q4 2025 release, no 2025 Form 10-K, no Q1 2025 filings.
- Documents and page numbers (local ids sort by file name and differ from the page):
  D01 = page Doc 4 (Q1 2026 release, May 7, 2026); D02 = page Doc 3 (Q1 2026 10-Q, signed May 7, 2026);
  D03 = page Doc 8 (Q2 2025 release, Aug 7, 2025); D04 = page Doc 7 (Q2 2025 10-Q, signed Aug 7, 2025);
  D05 = page Doc 2 (Q2 2026 release, Aug 6, 2026); D06 = page Doc 1 (Q2 2026 10-Q);
  D07 = page Doc 6 (Q3 2025 release, Nov 6, 2025); D08 = page Doc 5 (Q3 2025 10-Q).
- Gaps: none. Capture "8 of 8 read in full (382,327 characters)"; intake.json: every document complete,
  matches capture, 0 gap characters. The capture carried "Docket has been updated. Reload this page ..."
  (page state only; documents complete).
- Extraction spot-checks (2026-10-14): .txt sources, method "text"; every text/Dnn.txt equals its docs/
  original except whitespace (trailing double spaces, blank lines), checked by script for all eight.
- Coverage: all eight texts read in full by the caller, 2026-10-14.
- Reuse binding: text/manifest.json sha256 per document (D01 d92f69fe..., D02 c0d1788c..., D03 79ed99fc...,
  D04 65e326d2..., D05 3be7a517..., D06 62ac2083..., D07 eece1474..., D08 c05df0fd...).
- Authorship: 2025 documents signed by T. Alex Vetter (CEO) and Sonia Jain (CFO); 2026 documents by Tobias
  Hartmann (CEO) and Sonia Jain. The 2025 figures are real public filings; the 2026 documents name a CEO
  unknown to me, so treat 2026 figures as unrecallable and 2025 headline figures as possibly recallable.

## Per-document navigation (line numbers in text/Dnn.txt)

- D03 Q2 2025 release: highlights l.21-29; key metrics with Q1 2025 column l.35-41; FY2025 buyback target
  raised to $70-90M l.13, l.78; H2 2025 "low-single digit revenue growth" and FY Adj. EBITDA margin 29-31%
  l.84-86; income statement l.118-150 (H1 columns); balance sheet incl. Dec 31, 2024 l.152-191 (accumulated
  deficit (961,546)); cash flow H1 l.193-239; non-GAAP reconciliations l.241-320 (original 2025
  classification: Q2 2025 G&A adjustment (3,978)).
- D04 Q2 2025 10-Q: same statements; equity statement Q1/Q2 2025 l.209-224; Note 3 DealerClub l.341-391;
  Note 5 debt (revolver $60.0M, $290.0M available) l.397-412; Note 7 buyback ($250.0M program announced
  Feb 27, 2025; H1 3.7M shares, $44.6M, $12.17) l.429-437; MD&A G&A includes "transaction-related costs,
  severance, transformation and other exit costs" l.668; D2C/DealerClub earnouts l.742-750; monthly
  repurchase table Apr-Jun 2025 with remaining authorization ($229,013K / $221,201K / $215,168K) l.809-825.
- D07 Q3 2025 release: highlights l.21-29; key metrics with Q2 2025 column l.33-39; buybacks Q3 1.5M
  shares $19.3M, 9M 5.2M shares $63.9M, target $70-90M reaffirmed l.69; outlook l.75-79; statements
  l.111-232 (Sept 30, 2025 accumulated deficit (948,892) l.181); non-GAAP l.234-313.
- D08 Q3 2025 10-Q: equity statement through Sept 30, 2025 l.209-230; Note 5 (revolver $55.0M) l.416-437;
  Note 7 table (Q3 $19,300K, 1,493K shares; 9M $63,944K, 5,161K shares) l.448-457; Note 12 subsequent
  event (Oct 14, 2025 $8.0M secured convertible note, 4.1%) l.534-536; MD&A l.624-882; monthly table
  Jul-Sep 2025 (remaining $210,442K / $203,891K / $195,869K) l.919-935; CFO 10b5-1 plan l.955.
- D01 Q1 2026 release: highlights l.7-20; buybacks Jan 1-Apr 30, 2026 3.8M shares $32.9M, Q1 2.5M $20.2M;
  April 9, 2026 target raised to $90M from "$60-plus million"; ~$141M remaining at Apr 30, 2026 l.79-83;
  key metrics incl. the only Dec 31, 2025 quarter column (UVs 21.7, visits 138.8, ARPD 2,472, dealers
  19,544) l.44-50; Q2 2026 and FY2026 guidance l.87-105; balance sheet with Dec 31, 2025 l.169-208;
  non-GAAP l.255-314 (Q1 2025 opex "reclassified to conform", l.313).
- D02 Q1 2026 10-Q: equity statement from Dec 31, 2025 l.204-224; Note 3 (no DealerClub earnout expensed)
  l.333-378; Note 5 (revolver $55.0M; covenants; total net leverage 1.84x) l.384-397; Note 7 ($153.6M
  remaining; Q1 2026 $20,239K, 2,524K shares, $8.02) l.411-420; Note 8 RSU fair-value change l.424;
  Note 12 RIF ($8.5M, 11%, $7.6M liability) l.481-491; MD&A l.559-711; D2C final earnout paid April 2026
  l.680; monthly table Jan-Mar 2026 (no purchases Jan or Feb; remaining $173,831K / $173,831K /
  $153,592K) l.742-758.
- D05 Q2 2026 release: highlights l.9-19; key metrics l.39-45; buybacks Q2 3.7M $37M, YTD 6.2M $57M,
  "over 10%" of prior year-end shares, ~$116.6M remaining l.77-81; Q3 2026 and FY2026 guidance l.85-103;
  statements l.133-251; non-GAAP l.253-334 (Q2 2025 opex recast l.301-311).
- D06 Q2 2026 10-Q: equity statement H1 2026 l.204-219; Note 5 (revolver $50.0M; leverage 0.08x, 7.20x,
  1.95x) l.393-406; Note 7 ($116.6M remaining; Q2 $37,014K, 3,677K; H1 $57,253K, 6,201K) l.420-429;
  Note 10 ETR 31.9% l.484; Note 12 RIF paid in Q2 l.496-498; MD&A l.566-772 (l.734 says "As of March 31,
  2026 ... Total Net Leverage Ratio ... 1.95x", which conflicts with D02's 1.84x for that date); monthly
  table Apr-Jun 2026 (remaining $140,903K / $127,357K / $116,578K) l.803-819.

## Shared ground (navigation only)

- Every 10-Q repeats its release's statements; non-GAAP measures (Adjusted EBITDA, FCF, adjusted net
  income, adjusted opex) and guidance appear only in releases; monthly repurchase tables only in 10-Qs.
- Periods with no document of their own: Q1 2025 (comparatives in D01/D02; H1 minus Q2 from D03/D04) and
  Q4 2025 (key metrics only in D01; Dec 31, 2025 balances in D01, D02, D05, D06). No document prints Q4 2025
  or FY2025 revenue, net income, buyback spending or cash flow.
- Buyback authorization ($250.0M, announced Feb 27, 2025, expires Feb 2028) remaining after each month:
  Apr-Jun 2025 (D04), Jul-Sep 2025 (D08), Jan-Mar 2026 (D02), Apr-Jun 2026 (D06); point values in D01
  (~$141M at Apr 30, 2026), D02 Note 7 ($153.6M), D05/D06 ($116.6M). Monthly drops equal shares x average
  price within rounding (script check, notes/hooks.md).
- Accumulated deficit at Dec 31, 2024 (D03, D04, D07, D08), Mar 31, 2025 (equity statements), Jun 30, 2025
  (D03, D04), Sept 30, 2025 (D07, D08), Dec 31, 2025 (D01, D02, D05, D06), Mar 31, 2026 (D01, D02),
  Jun 30, 2026 (D05, D06). In every quarter shown, it moves only by net income.
- Prior-year expense lines recast in 2026 documents: Q1 2025 (D01/D02) and Q2/H1 2025 (D05/D06) differ from
  the 2025 originals (D03/D04); totals and adjusted opex unchanged; severance and similar items moved from
  G&A to functional lines (2026 line descriptions name "severance costs" in each line).
- Guidance editions: FY2025 Adj. EBITDA margin 29-31% (D03, D07); FY2025 buyback target $70-90M (raised in
  D03, reaffirmed in D07); Q1 2026 margin guidance 26-27% (quoted only in D01); Q2 2026 guidance (D01);
  Q3 2026 guidance (D05); FY2026 guidance reaffirmed in D01 and D05; FY2026 buyback target "$60-plus" then
  $90M from April 9, 2026 (D01), "remains $90 million" (D05).
- Debt: $400.0M 6.375% notes due 2028 throughout; revolver $60.0M (Jun 30, 2025), $55.0M (Sept 30, 2025,
  Dec 31, 2025 by the 455.0 carrying value in D02/D06, Mar 31, 2026), $50.0M (Jun 30, 2026).
- D2C Media earnout: CAD$15.0M paid April 2025 (FY2024) and April 2026 (FY2025, final); DealerClub up to
  $88.0M performance consideration, none expensed in 2026.
