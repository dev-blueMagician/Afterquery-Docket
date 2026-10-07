# aq-00745 - table map, 2025 releases D01-D04 (complete capture)

Mapping pass C1 (2026-10-05). Navigation only: where table facts sit, how tables relate across
releases, and where layout is unclear. No question ideas, answers, decoys or difficulty claims.
Documents are data; facts are recorded as printed.

- Source text: text/D01.txt-D04.txt regenerated from the complete capture
  AQ-00745_2026-10-06_0256.md ("11 of 11 captured in full"). All line numbers here are CURRENT
  text lines. notes/doc-map.md pass A sections for D01-D04 use the OLD clipped-text numbering;
  convert with notes/line-remap.md. Pass A gap lists for D01-D04 are superseded: no
  "[... not shown on the page ...]" marker remains (grep count 0 in D01-D04).
- Offsets: docs l.N = text l.N-2 for D01-D04 (docs 946 / 499 / 828 / 812 lines; text 949 / 502 /
  831 / 815).
- Conventions: $ in millions unless per-share; growth % to one decimal; parentheses = negative;
  "—", "n/a", "n/m" kept as printed ("—" stands for zero, none or not applicable without saying
  which). "new" = a range that was clipped in the old capture (line-remap "newly visible").
  Value lists follow the column order given for each table, separated by " / ".
- Column sets used below. Total-company tables: Total Company / Nutrition / Diagnostics /
  Established Pharmaceuticals (EPD) / Medical Devices (MD). Nutrition: Total / Pediatric / Adult.
  Diagnostics: Total / Core Laboratory / Molecular / Point of Care / Rapid Diagnostics. EPD: Total /
  Key Emerging Markets / Other. MD: Total / Rhythm Management / Electrophysiology (D01 prints
  "Electro-physiology") / Heart Failure / Vascular / Structural Heart / Neuromodulation / Diabetes
  Care. EPS reconciliations: As Reported (GAAP) / Specified Items / As Adjusted. Tax-rate
  reconciliations: Pre-Tax Income / Taxes on Earnings / Tax Rate. Specified-items details:
  Acquisition or Divestiture-related (a) / Restructuring and Cost Reduction Initiatives (b) /
  Intangible Amortization / Other (c) / Total Specifieds.
- No D01-D04 sales table has an "excluding foreign exchange" row; each prints "Impact of foreign
  exchange". Growth basis in D01-D04 is "organic" only (no "comparable").

## Read ledger (this pass)

| Doc | Lines read (chunks) | Newly visible ranges (all read) | Unread | Missing text |
| --- | --- | --- | --- | --- |
| D01 | 1-240, 240-439, 439-618, 619-788, 789-949 | 69-75, 97-103, 135-141, 167-173, 195-200, 230-235, 261-266, 290-295, 317-322, 350-356, 426-431, 439-444, 452-457, 465-470, 480-489, 531-540, 590-599, 611-620, 638-647, 659-668, 814-820, 850-856, 886-892, 922-928 | none | none |
| D02 | 1-260, 260-502 | 61-67, 97-103, 135-140, 172-177, 201-206, 284-293, 339-348, 360-369, 443-449, 477-483 | none | none |
| D03 | 1-230, 230-409, 409-597, 598-831 | 65-70, 94-100, 134-139, 161-167, 187-192, 220-225, 245-250, 274-279, 299-304, 332-337, 409-419, 463-472, 516-525, 537-546, 562-571, 583-592, 704-710, 738-744, 772-778, 806-812 | none | none |
| D04 | 1-230, 230-409, 409-608, 608-815 | 63-68, 92-98, 132-137, 159-165, 185-190, 216-221, 241-246, 270-275, 295-300, 324-329, 397-406, 442-451, 495-504, 516-525, 541-550, 562-571, 681-687, 715-720, 756-762, 790-796 | none | none |

Extraction spot-checks against docs/ (this pass): D01 newly visible 4Q24 "| International | 5.4 |
2.0 | (3.4) | 3.8 | 13.5 |" docs l.69 = text l.71; D01 12M24 details row "Other (income) expense,
net | (155) ..." docs l.889 = text l.891; D02 footnote 1 ("decrease of 1.4 percent and 5.4
percent") docs l.266 = text l.268; D04 3Q25 details footnote d) "$160 million" docs l.699 = text
l.701; D04 3Q24 EBT row docs l.720 = text l.722; D04 9M24 details row docs l.793 = text l.795.
Printed page counts ("Page N of M" lines in docs): D01 20, D02 15, D03 20, D04 20. No U+FFFD,
no-break space or zero-width character in D01-D04 (grep).

<!-- C1: D01 -->
## D01 - Q4 and full-year 2024 release (Jan. 22, 2025)

Periods: 4Q24 vs 4Q23; 12M24 vs 12M23 ("Twelve Months Ended December 31"); calendar year.

### Sales tables

- Total company 4Q24, l.55-83 (title l.55 "Fourth Quarter 2024 Results (4Q24)"; header l.57
  "Sales 4Q24 ($ in millions)"; l.65 "% Change vs. 4Q23").
  - $: U.S. (l.59) 4,341 / 928 / 1,055 / — / 2,353; International (l.61) 6,633 / 1,201 / 1,465 /
    1,268 / 2,699; Total reported (l.63) 10,974 / 2,129 / 2,520 / 1,268 / 5,052.
  - %: U.S. reported (l.67) 10.0 / 8.0 / 3.5 / n/a / 14.0. New l.69-75: International 5.4 / 2.0 /
    (3.4) / 3.8 / 13.5; Total reported 7.2 / 4.5 / (0.6) / 3.8 / 13.7; Impact of foreign exchange
    (1.4) / (1.7) / (1.6) / (4.7) / (0.3); "Impact of business exit*" (0.2) / (0.9) / — / — / —;
    Organic 8.8 / 7.1 / 1.0 / 8.5 / 14.0. Then l.77 "Impact of COVID-19 testing sales (3)" (1.3) /
    — / (5.1) / — / —; l.79 "Organic (excluding COVID-19 tests)" 10.1 / 7.1 / 6.1 / 8.5 / 14.0;
    l.81 U.S. 13.5 / 10.0 / 15.9 / n/a / 14.0; l.83 International 8.1 / 4.9 / 0.8 / 8.5 / 14.0
    (l.81-83 unlabelled; they follow the excl.-COVID row; organic incl. COVID by geography is
    printed only in the revenue reconciliation, l.764: U.S. 10.4, Intl 7.7).
- Total company 12M24, l.85-113 (title l.85 "Full-Year 2024 Results (12M24)"; header l.87; l.93
  "% Change vs. 12M23").
  - $: U.S. (l.89) 16,323 / 3,689 / 3,830 / — / 8,788; International and Total reported share
    l.91: 25,627 / 4,724 / 5,511 / 5,194 / 10,198 and 41,950 / 8,413 / 9,341 / 5,194 / 18,986.
  - %: U.S. (l.95) 5.6 / 8.1 / (11.5) / n/a / 14.2. New l.97-103: International 3.9 / (0.4) /
    (2.6) / 2.5 / 11.0; Total reported 4.6 / 3.2 / (6.5) / 2.5 / 12.4; FX (2.6) / (2.7) / (2.6) /
    (6.7) / (1.3); "Impact of business exit and acquisition*" 0.1 / (0.5) / — / — / 0.3; Organic
    7.1 / 6.4 / (3.9) / 9.2 / 13.4. l.105 COVID impact (2.5) / — / (9.1) / — / —; l.107 Organic
    excl. COVID 9.6 / 6.4 / 5.2 / 9.2 / 13.4; l.109 U.S. 10.9 / 9.2 / 6.3 / n/a / 13.5; l.111
    International 8.8 / 4.4 / 4.5 / 9.2 / 13.3 (unlabelled excl.-COVID geography rows; reconciliation
    organic U.S. 5.5, Intl 8.1 at l.780).
  - Footnote l.113 (applies to both tables): quarter reflects ZonePerfect discontinuation "in
    March 2024"; full year also "the acquisition of CSI on April 27, 2023. Organic sales growth
    excludes the impact of the acquired business from January through April 2024."
- Nutrition 4Q24, l.119-145 (header l.123; l.131 "% Change vs. 4Q23").
  - $: U.S. (l.125) 928 / 562 / 366; Intl (l.127) 1,201 / 438 / 763; Total (l.129) 2,129 / 1,000 /
    1,129.
  - %: U.S. (l.133) 8.0 / 11.3 / 3.2. New l.135-141: Intl 2.0 / (8.9) / 9.5; Total reported 4.5 /
    1.5 / 7.4; FX (1.7) / (1.0) / (2.3); business exit* (0.9) / — / (1.7); Organic 7.1 / 2.5 /
    11.4. Unlabelled organic geography: l.143 U.S. 10.0 / 11.3 / 8.1; l.145 Intl 4.9 / (6.7) /
    13.0.
- Nutrition 12M24, l.153-177 (header l.155; l.163 "% Change vs. 12M23").
  - $: U.S. (l.157) 3,689 / 2,208 / 1,481; Intl (l.159) 4,724 / 1,815 / 2,909; Total (l.161)
    8,413 / 4,023 / 4,390.
  - %: U.S. (l.165) 8.1 / 11.7 / 3.2. New l.167-173: Intl (0.4) / (7.3) / 4.5; Total 3.2 / 2.2 /
    4.0; FX (2.7) / (1.5) / (4.0); business exit* (0.5) / — / (0.9); Organic 6.4 / 3.7 / 8.9.
    l.175 U.S. 9.2 / 11.7 / 5.8; l.177 Intl 4.4 / (4.3) / 10.5, run together with footnote
    "*Reflects the impact of discontinuing the ZonePerfect(R) product line. This action was
    initiated in March 2024."
- Diagnostics 4Q24, l.183-208 (header l.187; l.191 "% Change vs. 4Q23").
  - $ (all on l.189): U.S. 1,055 / 363 / 38 / 100 / 554; Intl 1,465 / 1,024 / 99 / 47 / 295; Total
    2,520 / 1,387 / 137 / 147 / 849.
  - %: U.S. (l.193) 3.5 / 11.6 / (13.9) / (6.1) / 2.1. New l.195-200: Intl (3.4) / (1.9) / (9.1) /
    11.0 / (7.9); Total reported (0.6) / 1.3 / (10.5) / (1.3) / (1.6); FX (1.6) / (2.5) / (0.3) /
    0.1 / (0.6); Organic 1.0 / 3.8 / (10.2) / (1.4) / (1.0). l.202 COVID impact (5.1) / (0.2) /
    (2.8) / — / (17.4); l.204 Organic excl. COVID 6.1 / 4.0 / (7.4) / (1.4) / 16.4; l.206 U.S.
    15.9 / 11.9 / (7.2) / (6.1) / 30.0; l.208 Intl 0.8 / 1.5 / (7.5) / 10.7 / (0.6) (excl.-COVID
    geography, unlabelled).
- Diagnostics 12M24, l.216-241 (header l.218; l.226 "% Change vs. 12M23").
  - $: U.S. (l.220) 3,830 / 1,332 / 150 / 408 / 1,940; Intl (l.222) 5,511 / 3,903 / 371 / 180 /
    1,057; Total (l.224) 9,341 / 5,235 / 521 / 588 / 2,997.
  - %: U.S. (l.228) (11.5) / 7.2 / (12.7) / 3.1 / (23.0). New l.230-235: Intl (2.6) / (0.3) /
    (7.7) / 6.4 / (9.8); Total (6.5) / 1.5 / (9.2) / 4.1 / (18.8); FX (2.6) / (4.1) / (0.7) / — /
    (1.0); Organic (3.9) / 5.6 / (8.5) / 4.1 / (17.8). l.237 COVID impact (9.1) / (0.2) / (5.3) /
    — / (23.8); l.239 Organic excl. COVID 5.2 / 5.8 / (3.2) / 4.1 / 6.0; l.241 (one line) U.S. 6.3 /
    7.5 / (4.3) / 3.1 / 7.4 and International 4.5 / 5.3 / (2.8) / 6.5 / 3.8.
- EPD 4Q24, l.247-270 (header l.251): $ U.S. — / — / — (l.253); Intl and Total share l.255: 1,268 /
  948 / 320 each. % U.S. n/a (l.259); new l.261-266: Intl 3.8 / 3.3 / 5.2; Total 3.8 / 3.3 / 5.2;
  FX (4.7) / (5.5) / (2.6); Organic 8.5 / 8.8 / 7.8. l.268 U.S. n/a; l.270 Intl 8.5 / 8.8 / 7.8.
- EPD 12M24, l.276-299 (header l.278): $ U.S. — (l.280); Intl 5,194 / 3,858 / 1,336 (l.282);
  Total same (l.284). % U.S. n/a (l.288); new l.290-295: Intl 2.5 / 1.3 / 6.1; Total 2.5 / 1.3 /
  6.1; FX (6.7) / (8.2) / (2.3); Organic 9.2 / 9.5 / 8.4. l.297 U.S. n/a; l.299 Intl 9.2 / 9.5 /
  8.4.
- MD 4Q24, l.305-326 (header l.309).
  - $ (all on l.311): U.S. 2,353 / 303 / 300 / 253 / 269 / 290 / 204 / 734; Intl 2,699 / 321 /
    343 / 78 / 456 / 319 / 53 / 1,129; Total 5,052 / 624 / 643 / 331 / 725 / 609 / 257 / 1,863.
  - %: U.S. (l.315) 14.0 / 6.0 / 7.7 / 11.5 / 9.7 / 25.7 / 4.2 / 22.0. New l.317-322: Intl 13.5 /
    8.2 / 8.8 / 5.0 / 5.7 / 19.5 / 23.9 / 18.8; Total reported 13.7 / 7.1 / 8.3 / 9.9 / 7.1 / 22.4 /
    7.7 / 20.1; FX (0.3) / (0.1) / (0.5) / 0.3 / 0.3 / (0.2) / (0.7) / (0.5); Organic 14.0 / 7.2 /
    8.8 / 9.6 / 6.8 / 22.6 / 8.4 / 20.6. l.324 U.S. 14.0 / 6.0 / 7.7 / 11.5 / 9.7 / 25.7 / 4.2 /
    22.0; l.326 Intl 14.0 / 8.4 / 9.8 / 4.1 / 5.2 / 20.0 / 27.8 / 19.7.
- MD 12M24, l.336-362 (header l.338).
  - $: U.S. (l.340) 8,788 / 1,154 / 1,141 / 986 / 1,056 / 1,051 / 767 / 2,633; Intl (l.342)
    10,198 / 1,236 / 1,326 / 293 / 1,781 / 1,195 / 195 / 4,172; Total (l.344) 18,986 / 2,390 /
    2,467 / 1,279 / 2,837 / 2,246 / 962 / 6,805.
  - %: U.S. (l.348) 14.2 / 6.3 / 13.2 / 11.1 / 8.0 / 19.0 / 5.9 / 23.6. New l.350-356: Intl 11.0 /
    5.7 / 11.6 / 7.3 / 4.6 / 12.6 / 18.4 / 14.9; Total 12.4 / 6.0 / 12.3 / 10.2 / 5.8 / 15.5 / 8.2 /
    18.1; FX (1.3) / (0.9) / (2.1) / (0.1) / (0.9) / (1.5) / (1.3) / (1.6); "Impact of
    acquisition*" 0.3 / — / — / — / 2.1 / — / — / —; Organic 13.4 / 6.9 / 14.4 / 10.3 / 4.6 / 17.0 /
    9.5 / 19.7. l.358 U.S. 13.5 / 6.3 / 13.2 / 11.1 / 2.5 / 19.0 / 5.9 / 23.6; l.360 Intl 13.3 /
    7.5 / 15.4 / 7.6 / 5.8 / 15.3 / 25.5 / 17.3. Footnote l.362 (CSI acquired April 27, 2023;
    excluded "from January through April 2024").

### Footnote-3 Diagnostics / COVID-19 test-sales tables (l.418-470)

Columns: Sales U.S. / Int'l / Total | COVID Tests Sales U.S. / Int'l / Total. Rows: Total
Diagnostics, Core Laboratory, Molecular, Rapid Diagnostics (no Point of Care row). All data rows
new.

- 4Q24 (l.420-431): Total Dx 1,055 / 1,465 / 2,520 | 134 / 42 / 176; Core Lab 363 / 1,024 / 1,387 |
  1 / 1 / 2; Molecular 38 / 99 / 137 | 1 / 1 / 2; Rapid Dx 554 / 295 / 849 | 132 / 40 / 172.
- 4Q23 (l.433-444): Total Dx 1,020 / 1,514 / 2,534 | 224 / 64 / 288; Core Lab 326 / 1,044 / 1,370 |
  1 / 3 / 4; Molecular 44 / 109 / 153 | 5 / 2 / 7; Rapid Dx 543 / 319 / 862 | 218 / 59 / 277.
- 12M24 (l.446-457): Total Dx 3,830 / 5,511 / 9,341 | 562 / 185 / 747; Core Lab 1,332 / 3,903 /
  5,235 | 4 / 6 / 10; Molecular 150 / 371 / 521 | 8 / 4 / 12; Rapid Dx 1,940 / 1,057 / 2,997 | 550
  / 175 / 725.
- 12M23 (l.459-470): Total Dx 4,329 / 5,659 / 9,988 | 1,255 / 331 / 1,586; Core Lab 1,243 / 3,916
  / 5,159 | 7 / 13 / 20; Molecular 172 / 402 / 574 | 24 / 19 / 43; Rapid Dx 2,518 / 1,172 / 3,690 |
  1,224 / 299 / 1,523.
- These are the only printed 2023 Diagnostics dollar figures (4Q23, 12M23) in D01-D04. The three
  listed COVID sub-business amounts sum to the COVID total in each period (e.g. 2 + 2 + 172 = 176).

### Statements of earnings

- 4Q24, l.476-511 (cols 4Q24 / 4Q23 / % Change; "(in millions, except per share data)"). New
  l.480-489: Net Sales $10,974 / $10,241 / 7.2; Cost of products sold, excluding amortization
  expense 4,942 / 4,556 / 8.5; Amortization of intangible assets 465 / 481 / (3.1); Research and
  development 749 / 700 / 7.0; Selling, general, and administrative 2,907 / 2,724 / 6.7; Total
  Operating Cost and Expenses 9,063 / 8,461 / 7.1; Operating Earnings 1,911 / 1,780 / 7.4;
  Interest expense, net 45 / 70 / (35.6). l.491 (one line): Net foreign exchange (gain) loss (10)
  / 24 / n/m; Other (income) expense, net (154) / (109) / n/m; Earnings before taxes 2,030 / 1,795
  / 13.1. l.493 Taxes on earnings (7,199) / 201 / n/m [1)]; l.495 Net Earnings $9,229 / $1,594 /
  n/m; l.497 NE excluding Specified Items $2,349 / $2,094 / 12.2 [2)]; l.499 Diluted EPS $5.27 /
  $0.91 / n/m; l.501 Diluted EPS excluding Specified Items $1.34 / $1.19 / 12.6 [2)]; l.503
  average shares 1,746 / 1,748. Footnotes l.517-521.
- 12M24, l.527-562 (cols 12M24 / 12M23 / % Change). New l.531-540: Net Sales $41,950 / $40,109 /
  4.6; COGS 18,706 / 17,975 / 4.1; Amortization 1,878 / 1,966 / (4.4); R&D 2,844 / 2,741 / 3.8;
  SG&A 11,697 / 10,949 / 6.8; Total Operating Cost and Expenses 35,125 / 33,631 / 4.4; Operating
  Earnings 6,825 / 6,478 / 5.4; Interest expense, net 215 / 252 / (14.5). l.542 (one line): Net
  FX (27) / 41 / n/m; Other (income) expense, net (376) / (479) / n/m; EBT 7,013 / 6,664 / 5.2.
  l.544 Taxes (6,389) / 941 / n/m; l.546 NE $13,402 / $5,723 / n/m; l.548 NE excl. specified
  $8,200 / $7,802 / 5.1; l.550 Diluted EPS $7.64 / $3.26 / n/m; l.552 adjusted $4.67 / $4.44 /
  5.2; l.554 shares 1,748 / 1,749. Footnotes l.568-574.

### EPS (non-GAAP) reconciliations (l.580-670)

Each block: "Intangible Amortization" line (tab text) then a new markdown block.

- 4Q24 l.582-601: Intangible Amortization $465 / $(465) / $— (l.588). New l.590-599: Gross Margin
  5,567 / 673 / 6,240; R&D 749 / (59) / 690; SG&A 2,907 / (21) / 2,886; Other (income) expense,
  net (154) / 20 / (134); EBT 2,030 / 733 / 2,763; Taxes on Earnings (7,199) / 7,613 / 414; Net
  Earnings 9,229 / (6,880) / 2,349; Diluted EPS $5.27 / $(3.93) / $1.34. l.601: "intangible
  amortization expense of $465 million and other net expenses of $268 million associated with
  intangible impairments, restructuring actions, acquisitions and other net expenses. See page 17".
- 4Q23 l.603-622: Amortization $481 / $(481) / $— (l.609). New l.611-620: GM 5,204 / 518 / 5,722;
  R&D 700 / (78) / 622; SG&A 2,724 / (35) / 2,689; Other (109) / (9) / (118); EBT 1,795 / 640 /
  2,435; Taxes 201 / 140 / 341; NE 1,594 / 500 / 2,094; EPS $0.91 / $0.28 / $1.19. l.622: $481m
  amortization + $159m other net expenses ("restructuring actions, acquisitions and other net
  expenses"; "See page 18").
- 12M24 l.630-649: Amortization $1,878 / $(1,878) / $— (l.636). New l.638-647: GM 21,366 / 2,213 /
  23,579; R&D 2,844 / (140) / 2,704; SG&A 11,697 / (117) / 11,580; Other (376) / (163) / (539); EBT
  7,013 / 2,633 / 9,646; Taxes (6,389) / 7,835 / 1,446; NE 13,402 / (5,202) / 8,200; EPS $7.64 /
  $(2.97) / $4.67. l.649: $1.878bn + $755m ("intangible impairments, restructuring actions,
  acquisitions, a divestiture and other net expenses"; "See page 19").
- 12M23 l.651-670: Amortization $1,966 / $(1,966) / $— (l.657). New l.659-668: GM 20,168 / 2,109 /
  22,277; R&D 2,741 / (222) / 2,519; SG&A 10,949 / (102) / 10,847; Other (479) / 25 / (454); EBT
  6,664 / 2,408 / 9,072; Taxes 941 / 329 / 1,270; NE 5,723 / 2,079 / 7,802; EPS $3.26 / $1.18 /
  $4.44. l.670: $1.966bn + $442m ("See page 20").
- Gross Margin in these blocks = Net Sales - COGS - amortization (10,974 - 4,942 - 465 = 5,567;
  41,950 - 18,706 - 1,878 = 21,366).

### Tax-rate reconciliations (l.676-746; complete in both captures)

- 4Q24 (l.688-692): As reported $2,030 / $(7,199) / (354.6%) [1)]; Specified items 733 / 7,613;
  Excluding specified items $2,763 / $414 / 15.0%.
- 4Q23 (l.704-708): $1,795 / $201 / 11.2% [2)]; 640 / 140; $2,435 / $341 / 14.0%.
- 12M24 (l.722-726): $7,013 / $(6,389) / (91.1%) [1)]; 2,633 / 7,835; $9,646 / $1,446 / 15.0%.
- 12M23 (l.738-742): $6,664 / $941 / 14.1% [2)]; 2,408 / 329; $9,072 / $1,270 / 14.0%.
- Footnotes l.744 ($7.497 billion valuation allowance adjustments, 2024) and l.746 (~$80 million
  net tax expense, 2023).

### Revenue reconciliation (l.752-792; complete in both captures; many rows per line)

- 4Q block l.758-772. Columns: 4Q24 Abbott Reported / Impact from business exit (b) / Adjusted
  Revenue / 4Q23 Abbott Reported / Impact from business exit (b) / Adjusted Revenue / % change
  Reported / Adjusted / Organic. No acquisition column.
  - l.764 Total Company 10,974 / (1) / 10,973 / 10,241 / (17) / 10,224 / 7.2 / 7.4 / 8.8; U.S.
    4,341 / (1) / 4,340 / 3,949 / (17) / 3,932 / 10.0 / 10.4 / 10.4; Intl 6,633 / — / 6,633 /
    6,292 / — / 6,292 / 5.4 / 5.4 / 7.7.
  - l.766 Total Nutrition 2,129 / (1) / 2,128 / 2,038 / (17) / 2,021 / 4.5 / 5.4 / 7.1; U.S. 928 /
    (1) / 927 / 860 / (17) / 843 / 8.0 / 10.0 / 10.0; Intl 1,201 / — / 1,201 / 1,178 / — / 1,178
    / 2.0 / 2.0 / 4.9.
  - l.768 Adult Nutrition 1,129 / (1) / 1,128 / 1,053 / (17) / 1,036 / 7.4 / 9.1 / 11.4; U.S. 366
    / (1) / 365 / 355 / (17) / 338 / 3.2 / 8.1 / 8.1; Intl 763 / — / 763 / 698 / — / 698 / 9.5 /
    9.5 / 13.0.
  - l.770 Total Medical Devices 5,052 / — / 5,052 / 4,443 / — / 4,443 / 13.7 / 13.7 / 14.0; U.S.
    2,353 / — / 2,353 / 2,065 / — / 2,065 / 14.0 / 14.0 / 14.0; Intl 2,699 / — / 2,699 / 2,378 /
    — / 2,378 / 13.5 / 13.5 / 14.0.
  - l.772 Vascular 725 / — / 725 / 677 / — / 677 / 7.1 / 7.1 / 6.8; U.S. 269 / — / 269 / 245 / —
    / 245 / 9.7 / 9.7 / 9.7; Intl 456 / — / 456 / 432 / — / 432 / 5.7 / 5.7 / 5.2.
- 12M block l.774-788. Columns: 12M24 Abbott Reported / Impact of acquisition (a) / Impact from
  business exit (b) / Adjusted Revenue / 12M23 Abbott Reported / Impact from business exit (b) /
  Adjusted Revenue / Reported / Adjusted / Organic.
  - l.780 Total Company 41,950 / (57) / (14) / 41,879 / 40,109 / (49) / 40,060 / 4.6 / 4.5 / 7.1;
    U.S. 16,323 / (53) / (14) / 16,256 / 15,452 / (49) / 15,403 / 5.6 / 5.5 / 5.5; Intl 25,627 /
    (4) / — / 25,623 / 24,657 / — / 24,657 / 3.9 / 3.9 / 8.1.
  - l.782 Total Nutrition 8,413 / — / (14) / 8,399 / 8,154 / (49) / 8,105 / 3.2 / 3.7 / 6.4; U.S.
    3,689 / — / (14) / 3,675 / 3,413 / (49) / 3,364 / 8.1 / 9.2 / 9.2; Intl 4,724 / — / — / 4,724
    / 4,741 / — / 4,741 / (0.4) / (0.4) / 4.4.
  - l.784 Adult Nutrition 4,390 / — / (14) / 4,376 / 4,220 / (49) / 4,171 / 4.0 / 4.9 / 8.9; U.S.
    1,481 / — / (14) / 1,467 / 1,436 / (49) / 1,387 / 3.2 / 5.8 / 5.8; Intl 2,909 / — / — / 2,909
    / 2,784 / — / 2,784 / 4.5 / 4.5 / 10.5.
  - l.786 Total Medical Devices 18,986 / (57) / — / 18,929 / 16,887 / — / 16,887 / 12.4 / 12.1 /
    13.4; U.S. 8,788 / (53) / — / 8,735 / 7,696 / — / 7,696 / 14.2 / 13.5 / 13.5; Intl 10,198 /
    (4) / — / 10,194 / 9,191 / — / 9,191 / 11.0 / 10.9 / 13.3.
  - l.788 Vascular 2,837 / (57) / — / 2,780 / 2,681 / — / 2,681 / 5.8 / 3.7 / 4.6; U.S. 1,056 /
    (53) / — / 1,003 / 978 / — / 978 / 8.0 / 2.5 / 2.5; Intl 1,781 / (4) / — / 1,777 / 1,703 / —
    / 1,703 / 4.6 / 4.4 / 5.8.
- Footnotes l.790 (a) CSI acquisition, organic excludes it "from January through April 2024";
  l.792 (b) ZonePerfect, "initiated in March 2024".
- Among D01-D04, only D01's reconciliation adjusts the CURRENT-year column (4Q24 business exit
  (1); 12M24 acquisition (57) and business exit (14)); D02-D04 adjust only the prior-year base.

### Details of specified items (l.798-944)

- 4Q24 (printed page 17), l.798-834. New l.814-820: Gross Margin — / 49 / 465 / 159 / 673 (label
  cell reads "Gross Margin $"); R&D (1) / (20) / — / (38) / (59); SG&A (5) / (22) / — / 6 / (21);
  Other (income) expense, net (2) / — / — / 22 / 20; EBT 8 / 91 / 465 / 169 / 733. l.822 Taxes on
  Earnings (d) 7,613 and Net Earnings $(6,880) on one line; l.824 Diluted EPS $(3.93). Footnotes
  l.828 a) integration costs only; l.830 b); l.832 c) "European Union's Medical Device Regulations
  (MDR) and In Vitro Diagnostics Medical Device Regulations (IVDR) requirements for previously
  approved products and intangible asset impairment charges"; l.834 d) "net tax benefit ...
  including non-cash valuation allowance adjustments".
- 4Q23 (page 18), l.840-870. New l.850-856: GM 1 / 29 / 481 / 7 / 518; R&D (6) / (4) / — / (68) /
  (78); SG&A (15) / (5) / — / (15) / (35); Other (6) / — / — / (3) / (9); EBT 28 / 38 / 481 / 93 /
  640. l.858 Taxes (d) 140, NE $500; l.860 EPS $0.28. Footnotes l.864 a) "... as well as legal
  and other costs related to business acquisitions"; l.868 c) "... charges for intangible asset
  impairments"; l.870 d) plain.
- 12M24 (page 19), l.876-906. New l.886-892: GM 2 / 125 / 1,878 / 208 / 2,213; R&D (5) / (21) / —
  / (114) / (140); SG&A (37) / (39) / — / (41) / (117); Other (155) / — / — / (8) / (163); EBT
  199 / 185 / 1,878 / 371 / 2,633. l.894 Taxes (d) 7,835, NE $(5,202); l.896 EPS $(2.97).
  Footnotes l.900 a) "Includes the loss on the sale of a non-core business. ... as well as other
  costs related to business acquisitions"; l.904 c) "... charges for investment and intangible
  asset impairments"; l.906 d) includes valuation allowance adjustments.
- 12M23 (page 20), l.912-944. New l.922-928: GM 16 / 80 / 1,966 / 47 / 2,109; R&D (19) / (9) / —
  / (194) / (222); SG&A (58) / (33) / — / (11) / (102); Other 40 / — / — / (15) / 25; EBT 53 /
  122 / 1,966 / 267 / 2,408. l.930 Taxes (d) 329; l.932 NE $2,079; l.934 EPS $1.18. Footnotes
  l.938 a) "legal and other costs ... as well as integration costs"; l.942 c) intangible asset
  impairments; l.944 d) plain.
- Prose totals of the same items: l.519 (4Q24 "net after-tax benefits of $6.880 billion, or $3.93
  per share"), l.521 (4Q23 "net after-tax charges of $500 million, or $0.28"), l.572 (12M24
  benefits "$5.202 billion, or $2.97", incl. "acquisitions and a divestiture"), l.574 (12M23
  charges "$2.079 billion, or $1.18").

### Footnotes that change what a row or column covers (D01)

- Business exit / acquisition rows: l.113, l.177, l.362, l.790-792 (above).
- COVID rows carry "(3)" (l.77, 105, 202, 237) pointing to the footnote-3 tables l.418-470;
  footnotes 1-2 (l.414, 416) give exact totals and COVID amounts: 4Q24 $10.974bn / $176m; 4Q23
  $10.241bn / $288m; FY2024 $41.950bn / $747m; FY2023 $40.109bn / $1.586bn.
- Tax footnotes l.517, 568, 744 (2024 $7.497bn valuation allowance) and l.570, 746 (2023 ~$80m net
  tax expense); the 4Q23 and 12M23 tax-rate rows both carry footnote 2).

### Rounded prose vs table (D01)

- l.17 / l.27 "$11.0 billion", "$42.0 billion" vs 10,974 (l.63), 41,950 (l.91); exact in footnotes
  l.414, 416.
- l.212 "Excluding COVID-19 testing-related sales, global Diagnostics sales increased 4.3 percent
  on a reported basis and increased 6.1 percent on an organic basis." The 6.1 equals l.204; the
  reported excl.-COVID rate is not a table row. From footnote-3 $ figures (l.428, 441): (2,520 -
  176) / (2,534 - 288) = 2,344 / 2,246 = +4.36% (arithmetic on rounded $m).
- l.29 FY2024 gross margin "+60 basis points" GAAP / "+70" adjusted: prose only. Inputs l.533,
  l.640, l.661: GAAP 21,366 / 41,950 = 50.93% vs 20,168 / 40,109 = 50.28%; adjusted 23,579 /
  41,950 = 56.21% vs 22,277 / 40,109 = 55.54% (arithmetic).
- l.332 continuous glucose monitors "$1.8 billion", +22.7% reported / +22.8% organic; CGM is not a
  table row; the Diabetes Care column is 1,863, +20.1% / +20.6% (l.311, 320, 322).
- l.334 Medical Devices FY "$19 billion and increased more than $2 billion" vs 18,986 (l.344) and
  12M23 16,887 (l.786): difference 2,099.
- l.210 COVID "$176 million" vs "$288 million" = footnote-3 totals (l.428, l.441).
- Segment prose matching tables exactly: l.23, 27 (total), l.147-151 (Nutrition), l.272-274 (EPD,
  KEM), l.328 (MD 13.7 / 14.0).

### Layout notes (D01)

- Each formerly clipped % block is a markdown table with empty header cells ("|  |  | ..."); the
  "% Change" heading and U.S. row sit above it as tab text and the COVID / geography rows below it.
- No "Organic" label precedes geography rows in any D01 table. Rows after "Organic (excluding
  COVID-19 tests)" (l.81-83, 109-111, 206-208, 241) are excl.-COVID; rows after "Organic" (l.143-145,
  175-177, 268-270, 297-299, 324-326, 358-360) are organic.
- Rows merged on one line: l.91, 111 (row + "Refer to page 16 ..."), 177 (row + footnote), 189,
  241, 255, 311, 491, 542, 764-788 (each line = segment total + U.S. + Intl), 822, 894.
- l.11 "Exhibit 99.1 9.1" (stray "9.1"). Tax-rate column headers split over l.680-686 ("Pre-Tax /
  Income Taxes on / Earnings Tax / Rate"); details headers split over l.802-812.
- Page pointers checked: "page 13"/"page 14" (EPS reconciliations, l.25, 31, 507, 558), "page 16"
  (revenue reconciliation, l.111), "page 17"-"page 20" (details, l.601, 622, 649, 670) all land on
  the matching printed page.

<!-- END C1 D01 -->

<!-- C1: D02 -->
## D02 - Q1 2025 release (April 16, 2025)

Periods: 1Q25 vs 1Q24 only (no year-to-date tables).

### Sales tables

- Total company 1Q25, l.47-75 (header l.49; l.57 "% Change vs. 1Q24").
  - $: U.S. (l.51) 4,168 / 955 / 871 / — / 2,339; Intl (l.53) 6,190 / 1,191 / 1,183 / 1,260 /
    2,556; Total reported (l.55) 10,358 / 2,146 / 2,054 / 1,260 / 4,895.
  - %: U.S. (l.59) 8.4 / 8.8 / (6.4) / n/a / 15.0. New l.61-67: Intl 1.2 / 0.1 / (7.8) / 2.7 / 5.7;
    Total reported 4.0 / 3.8 / (7.2) / 2.7 / 9.9; FX (2.8) / (2.4) / (2.3) / (5.1) / (2.7);
    "Impact of business exit*" (0.1) / (0.6) / — / — / —; Organic 6.9 / 6.8 / (4.9) / 7.8 / 12.6.
    l.69 U.S. 8.8 / 10.4 / (6.4) / n/a / 15.0; l.71 Intl 5.7 / 4.2 / (3.8) / 7.8 / 10.5
    (unlabelled; organic, = reconciliation l.423-425).
  - No COVID-impact row and no excl.-COVID row in any D02 table; COVID figures are footnote prose
    only (l.268). l.73 "Refer to page 13"; l.75 footnote "*Quarter to date March 31, 2025,
    reflects the impact of discontinuing the ZonePerfect(R) product line in the Nutrition business
    in March 2024."
- Nutrition 1Q25, l.81-109 (header l.85): $ U.S. (l.87) 955 / 588 / 367; Intl (l.89) 1,191 / 453 /
  738; Total (l.91) 2,146 / 1,041 / 1,105. % U.S. (l.95) 8.8 / 14.2 / 1.1; new l.97-103: Intl 0.1 /
  (8.4) / 6.1; Total 3.8 / 3.2 / 4.4; FX (2.4) / (1.7) / (2.9); business exit* (0.6) / — / (1.4);
  Organic 6.8 / 4.9 / 8.7. l.105 U.S. 10.4 / 14.2 / 4.8; l.107 Intl 4.2 / (4.8) / 10.6. Footnote
  l.109 ("initiated in March 2024").
- Diagnostics 1Q25, l.119-144 (header l.123): $ U.S. (l.125) 871 / 332 / 40 / 100 / 399; Intl
  (l.127) 1,183 / 845 / 82 / 42 / 214; Total (l.129) 2,054 / 1,177 / 122 / 142 / 613. % U.S.
  (l.133) (6.4) / 7.1 / (4.4) / 1.5 / (16.9); new l.135-140: Intl (7.8) / (5.6) / (6.7) / 4.4 /
  (17.9); Total (7.2) / (2.3) / (5.9) / 2.4 / (17.3); FX (2.3) / (3.2) / (2.4) / (0.8) / (1.2);
  Organic (4.9) / 0.9 / (3.5) / 3.2 / (16.1). l.142 U.S. (6.4) / 7.1 / (4.4) / 1.5 / (16.9); l.144
  Intl (3.8) / (1.3) / (3.1) / 7.3 / (14.6).
- EPD 1Q25, l.156-181 (header l.160): $ U.S. — (l.162); Intl 1,260 / 965 / 295 (l.164); Total same
  (l.166). % U.S. n/a (l.170); new l.172-177: Intl 2.7 / 4.0 / (1.2); Total 2.7 / 4.0 / (1.2); FX
  (5.1) / (5.3) / (4.3); Organic 7.8 / 9.3 / 3.1. l.179 U.S. n/a; l.181 Intl 7.8 / 9.3 / 3.1.
- MD 1Q25, l.189-210 (header l.193, "Electrophysiology").
  - $ (all on l.195): U.S. 2,339 / 304 / 299 / 262 / 268 / 282 / 176 / 748; Intl 2,556 / 281 / 330
    / 77 / 442 / 295 / 52 / 1,079; Total 4,895 / 585 / 629 / 339 / 710 / 577 / 228 / 1,827.
  - %: U.S. (l.199) 15.0 / 12.3 / 11.1 / 10.6 / 5.5 / 20.9 / (2.8) / 27.1. New l.201-206: Intl 5.7
    / (3.7) / 4.0 / 14.3 / 1.6 / 4.6 / 16.3 / 10.1; Total 9.9 / 4.0 / 7.3 / 11.4 / 3.0 / 11.9 / 1.0
    / 16.5; FX (2.7) / (2.1) / (2.6) / (1.0) / (2.7) / (2.8) / (1.2) / (3.3); Organic 12.6 / 6.1 /
    9.9 / 12.4 / 5.7 / 14.7 / 2.2 / 19.8. l.208 U.S. = l.199 values; l.210 Intl 10.5 / 0.3 / 8.8 /
    19.1 / 5.8 / 9.6 / 22.7 / 15.4.
  - Structural Heart 1Q25 577 (U.S. 282, Intl 295) is the pre-2026 composition (see Shared ground).

### Statement of earnings 1Q25, l.272-315 (cols 1Q25 / 1Q24 / % Change)

New l.284-293: Net Sales $10,358 / $9,964 / 4.0; COGS 4,468 / 4,463 / 0.1; Amortization 420 / 472 /
(11.0); R&D 716 / 684 / 4.6; SG&A 3,061 / 2,959 / 3.5; Total Operating Cost and Expenses 8,665 /
8,578 / 1.0; Operating Earnings 1,693 / 1,386 / 22.1; Interest expense, net 49 / 61 / (18.6). l.295
(one line): Net FX (gain) loss (7) / — / n/m; Other (income) expense, net (127) / (111) / 14.9; EBT
1,778 / 1,436 / 23.8. l.297 Taxes 453 / 211 / n/m [1)]; l.299 NE $1,325 / $1,225 / 8.2; l.301 NE
excl. specified $1,919 / $1,729 / 10.9 [2)]; l.303 Diluted EPS $0.76 / $0.70 / 8.6; l.305 adjusted
$1.09 / $0.98 / 11.2 [2)]; l.307 shares 1,747 / 1,750. Footnotes l.319-325.

### EPS reconciliations (l.329-371)

- 1Q25 l.331-350: Amortization $420 / $(420) / $— (l.337). New l.339-348: GM 5,470 / 448 / 5,918;
  R&D 716 / (27) / 689; SG&A 3,061 / (10) / 3,051; Other (127) / (35) / (162); EBT 1,778 / 520 /
  2,298; Taxes 453 / (74) / 379; NE 1,325 / 594 / 1,919; EPS $0.76 / $0.33 / $1.09. l.350: $420m
  amortization + $100m other net expenses ("restructuring actions, costs associated with
  acquisitions, investment impairment charges and other net expenses"; "See page 14").
- 1Q24 l.352-371: Amortization $472 / $(472) / $— (l.358). New l.360-369: GM 5,029 / 518 / 5,547;
  R&D 684 / (21) / 663; SG&A 2,959 / (34) / 2,925; Other (111) / (26) / (137); EBT 1,436 / 599 /
  2,035; Taxes 211 / 95 / 306; NE 1,225 / 504 / 1,729; EPS $0.70 / $0.28 / $0.98. l.371: $472m +
  $127m ("See page 15").
- In 1Q25 the specified tax column is negative ((74)), so after-tax specified items (594) exceed
  pre-tax (520); footnote d) l.463 ties this to "approximately $200 million in adjustments related
  to prior recognition of a significant non-cash deferred tax benefit".

### Tax-rate reconciliation (l.375-411)

- 1Q25 (l.387-391): $1,778 / $453 / 25.5% [1)]; Specified 520 / (74); Excluding $2,298 / $379 /
  16.5%.
- 1Q24 (l.403-407): $1,436 / $211 / 14.7% [2)]; 599 / 95; $2,035 / $306 / 15.0%.
- Footnotes l.409 (~$200m deferred-tax adjustments, 2025), l.411 (~$10m net tax expense, 2024).

### Revenue reconciliation 1Q (l.415-429; complete in both captures)

Columns: 1Q25 Abbott Reported / 1Q24 Abbott Reported / Impact from business exit (a) / Adjusted
Revenue / % change Reported / Adjusted / Organic.

- l.423 Total Company 10,358 / 9,964 / (13) / 9,951 / 4.0 / 4.1 / 6.9; U.S. 4,168 / 3,846 / (13) /
  3,833 / 8.4 / 8.8 / 8.8; Intl 6,190 / 6,118 / — / 6,118 / 1.2 / 1.2 / 5.7.
- l.425 Total Nutrition 2,146 / 2,068 / (13) / 2,055 / 3.8 / 4.4 / 6.8; U.S. 955 / 878 / (13) / 865
  / 8.8 / 10.4 / 10.4; Intl 1,191 / 1,190 / — / 1,190 / 0.1 / 0.1 / 4.2.
- l.427 Adult Nutrition 1,105 / 1,059 / (13) / 1,046 / 4.4 / 5.8 / 8.7; U.S. 367 / 364 / (13) /
  351 / 1.1 / 4.8 / 4.8; Intl 738 / 695 / — / 695 / 6.1 / 6.1 / 10.6.
- Footnote l.429 (a) ZonePerfect. No MD or Vascular rows (no acquisition in this period).

### Details of specified items (l.433-499)

- 1Q25 (page 14), l.433-463. New l.443-449: Gross Margin — / 26 / 420 / 2 / 448 ("Gross Margin $"
  label cell); R&D (1) / (16) / — / (10) / (27); SG&A (3) / (7) / — / — / (10); Other (income)
  expense, net (24) / — / — / (11) / (35); EBT 28 / 49 / 420 / 23 / 520. l.451 Taxes (d) (74), NE
  $594; l.453 EPS $0.33. Footnotes l.457 a) integration costs "as well as a fair value adjustment
  to contingent consideration related to a business acquisition"; l.461 c) MDR/IVDR "and
  investment impairment charges"; l.463 d) adds the ~$200m deferred-tax adjustment.
- 1Q24 (page 15), l.467-499. New l.477-483: GM 1 / 42 / 472 / 3 / 518; R&D (3) / (2) / — / (16) /
  (21); SG&A (14) / (9) / — / (11) / (34); Other 12 / — / — / (38) / (26); EBT 6 / 53 / 472 / 68
  / 599. l.485 Taxes (d) 95; l.487 NE $504; l.489 EPS $0.28. Footnotes l.493 a) "... as well as
  other costs related to business acquisitions"; l.497 c) "various investment impairment charges
  and incremental costs to comply with ... (MDR) ... (IVDR) ..."; l.499 d) plain.
- Prose totals: l.323 1Q25 "net after-tax charges of $594 million, or $0.33 per share, for
  intangible amortization, charges related to investment impairments, charges related to
  restructuring and cost reduction initiatives, expenses associated with acquisitions, and other
  net expenses"; l.325 1Q24 "net after-tax charges of $504 million, or $0.28 per share".

### Footnotes that change coverage (D02)

- l.75, 109, 429: ZonePerfect business exit (prior-year base only).
- l.268 footnote 1: 1Q25 totals "$10.358 billion", Diagnostics "$2.054 billion", COVID "$84
  million"; 1Q24 "$9.964 billion", "$2.214 billion", "$204 million"; COVID impact "a decrease of
  1.4 percent and 5.4 percent" (Abbott, total Diagnostics); organic excl. COVID "8.3 percent for
  Abbott and 0.5 percent for total Diagnostics". These COVID percentages appear in no D02 table.
- Tax footnotes l.319-321, 409-411, 463.

### Rounded prose vs table (D02)

- l.19 margins (gross 52.8%, adjusted gross 57.1% "+140 basis point"; operating 16.3%, adjusted
  operating 21.0% "+130 basis point"): prose only; inputs l.286, 292, 341-344, 362-365.
- l.25 adjusted EPS "reflects double-digit growth" vs +11.2% (l.305).
- l.218 continuous glucose monitors "$1.7 billion", +18.3% reported / +21.6% organic vs Diabetes
  Care column 1,827, +16.5% / +19.8% (l.195, 204, 206).
- l.214 MD growth "led by Diabetes Care, Structural Heart, Heart Failure and Electrophysiology":
  these are the four highest organic rates in l.206 (19.8, 14.7, 12.4, 9.9), listed in that order.
- l.146, 150, 152, 183-185, 212 match the table rows.

### Layout notes (D02)

- One-line merges: l.195 (MD $ rows), l.295, l.423-427 (reconciliation), l.451.
- Unlabelled geography rows after "Organic": l.69-71, 105-107, 142-144, 179-181, 208-210.
- l.11 "Exhibit 99.1 9.1". l.295 1Q24 net FX printed "—".
- Page pointers checked: l.73 "page 13" (revenue reconciliation, page 13), l.311 "page 11", l.350
  "page 14", l.371 "page 15", l.455/491 "page 11" all land on the matching printed page.

<!-- END C1 D02 -->

<!-- C1: D03 -->
## D03 - Q2 2025 release (July 17, 2025)

Periods: 2Q25 vs 2Q24; first half 1H25 vs 1H24 ("First Half Ended June 30").

### Sales tables

- Total company 2Q25, l.51-80 (header l.53; l.61 "% Change vs. 2Q24").
  - $: U.S. (l.55) 4,276 / 957 / 811 / — / 2,503; Intl (l.57) 6,866 / 1,255 / 1,362 / 1,383 /
    2,866; Total reported (l.59) 11,142 / 2,212 / 2,173 / 1,383 / 5,369.
  - %: U.S. (l.63) 8.7 / 2.6 / (0.1) / n/a / 14.6. New l.65-70: Intl 6.6 / 3.1 / (1.5) / 6.9 /
    12.4; Total reported 7.4 / 2.9 / (1.0) / 6.9 / 13.4; FX 0.5 / (0.5) / 0.4 / (0.8) / 1.2;
    Organic 6.9 / 3.4 / (1.4) / 7.7 / 12.2. l.72 "Impact of COVID-19 testing sales 1" (0.6) / — /
    (2.2) / — / —; l.74 Organic (excl. COVID) 7.5 / 3.4 / 0.8 / 7.7 / 12.2; l.76 explicit label
    "Organic"; l.78 U.S. 8.7 / 2.6 / (0.1) / n/a / 14.6; l.80 Intl 5.8 / 4.0 / (2.2) / 7.7 / 10.1.
  - No business-exit row (none needed for 2Q). FX is positive for Total, Dx and MD (reported above
    organic).
- Total company 1H25, l.82-114 (header l.84; l.90 "% Change vs. 1H24").
  - $: U.S. (l.86) 8,444 / 1,912 / 1,682 / — / 4,842; Intl and Total share l.88: 13,056 / 2,446 /
    2,545 / 2,643 / 5,422 and 21,500 / 4,358 / 4,227 / 2,643 / 10,264.
  - %: U.S. (l.92) 8.5 / 5.6 / (3.5) / n/a / 14.8. New l.94-100: Intl 3.9 / 1.6 / (4.5) / 4.9 /
    9.1; Total 5.7 / 3.3 / (4.1) / 4.9 / 11.7; FX (1.1) / (1.5) / (0.9) / (2.9) / (0.7); business
    exit* (0.1) / (0.3) / — / — / —; Organic 6.9 / 5.1 / (3.2) / 7.8 / 12.4. l.102 COVID impact 2
    (1.0) / — / (3.9) / — / —; l.104 Organic excl. COVID 7.9 / 5.1 / 0.7 / 7.8 / 12.4; l.106
    "Organic"; l.108 U.S. 8.7 / 6.4 / (3.5) / n/a / 14.8; l.110 Intl 5.8 / 4.1 / (3.0) / 7.8 / 10.3.
    l.112 "Refer to page 16"; l.114 ZonePerfect footnote.
  - The "Organic" geography rows are organic incl. COVID: 1H25 U.S. 8.7 / Intl 5.8 equal the
    reconciliation organic column (l.684). The 2Q25 and 1H25 total-company geography rows print the
    same pair (U.S. 8.7, Intl 5.8).
- Nutrition 2Q25, l.118-143 (header l.122): $ U.S. (l.124) 957 / 587 / 370; Intl (l.126) 1,255 / 467
  / 788; Total (l.128) 2,212 / 1,054 / 1,158. % U.S. (l.132) 2.6 / 4.2 / 0.2; new l.134-139: Intl
  3.1 / (5.7) / 9.2; Total 2.9 / (0.4) / 6.1; FX (0.5) / (0.6) / (0.5); Organic 3.4 / 0.2 / 6.6.
  l.141 U.S. 2.6 / 4.2 / 0.2; l.143 Intl 4.0 / (4.5) / 9.8. No business-exit row.
- Nutrition 1H25, l.149-171 (header l.151): $ U.S. (l.153) 1,912 / 1,175 / 737; Intl and Total share
  l.155: 2,446 / 920 / 1,526 and 4,358 / 2,095 / 2,263. % U.S. (l.159) 5.6 / 9.0 / 0.6; new
  l.161-167: Intl 1.6 / (7.0) / 7.7; Total 3.3 / 1.3 / 5.3; FX (1.5) / (1.2) / (1.6); business
  exit* (0.3) / — / (0.7); Organic 5.1 / 2.5 / 7.6. l.169 U.S. 6.4 / 9.0 / 2.4; l.171 Intl 4.1 /
  (4.6) / 10.2 plus the ZonePerfect footnote on the same line.
- Diagnostics 2Q25, l.175-196 (header l.179): $ (all on l.181) U.S. 811 / 351 / 35 / 104 / 321;
  Intl 1,362 / 1,007 / 88 / 44 / 223; Total 2,173 / 1,358 / 123 / 148 / 544. % U.S. (l.185) (0.1)
  / 7.3 / 5.5 / (2.0) / (7.1); new l.187-192: Intl (1.5) / 0.5 / (5.6) / (11.9) / (6.1); Total
  (1.0) / 2.2 / (2.7) / (5.1) / (6.7); FX 0.4 / 0.6 / 0.7 / 0.1 / 0.1; Organic (1.4) / 1.6 / (3.4)
  / (5.2) / (6.8). l.194 U.S. = l.185 values; l.196 Intl (2.2) / (0.3) / (6.5) / (12.1) / (6.3).
  No COVID rows in the Diagnostics tables (Dx COVID impact (2.2) and excl.-COVID 0.8 are in the
  total-company table, l.72-74).
- Diagnostics 1H25, l.206-227 (header l.208): $ U.S. (l.210) 1,682 / 683 / 75 / 204 / 720; Intl
  (l.212) 2,545 / 1,852 / 170 / 86 / 437; Total (l.214) 4,227 / 2,535 / 245 / 290 / 1,157. % U.S.
  (l.218) (3.5) / 7.2 / — / (0.3) / (12.8); new l.220-225: Intl (4.5) / (2.4) / (6.1) / (4.5) /
  (12.3); Total (4.1) / 0.1 / (4.4) / (1.6) / (12.6); FX (0.9) / (1.2) / (1.0) / (0.4) / (0.6);
  Organic (3.2) / 1.3 / (3.4) / (1.2) / (12.0). l.227 (one line) U.S. (3.5) / 7.2 / — / (0.3) /
  (12.8) and Intl (3.0) / (0.7) / (4.9) / (3.3) / (10.7).
- EPD 2Q25, l.231-254 (header l.235): $ U.S. — (l.237); Intl and Total share l.239: 1,383 / 1,059 /
  324 each. % U.S. n/a (l.243); new l.245-250: Intl 6.9 / 7.3 / 5.9; Total 6.9 / 7.3 / 5.9; FX
  (0.8) / (1.4) / 1.4; Organic 7.7 / 8.7 / 4.5. l.252 U.S. n/a; l.254 Intl 7.7 / 8.7 / 4.5.
- EPD 1H25, l.260-283 (header l.262): $ U.S. — (l.264); Intl 2,643 / 2,024 / 619 (l.266); Total
  same (l.268). % U.S. n/a (l.272); new l.274-279: Intl 4.9 / 5.7 / 2.4; Total 4.9 / 5.7 / 2.4;
  FX (2.9) / (3.3) / (1.4); Organic 7.8 / 9.0 / 3.8. l.281 U.S. n/a; l.283 Intl 7.8 / 9.0 / 3.8.
- MD 2Q25, l.287-308 (header l.291).
  - $ (all on l.293): U.S. 2,503 / 340 / 322 / 282 / 283 / 289 / 193 / 794; Intl 2,866 / 333 / 378
    / 86 / 474 / 347 / 61 / 1,187; Total 5,369 / 673 / 700 / 368 / 757 / 636 / 254 / 1,981.
  - %: U.S. (l.297) 14.6 / 16.5 / 12.2 / 15.8 / 3.0 / 12.2 / 0.4 / 24.5. New l.299-304: Intl 12.4 /
    5.7 / 10.9 / 11.2 / 5.4 / 13.7 / 20.4 / 17.5; Total 13.4 / 10.9 / 11.5 / 14.7 / 4.5 / 13.0 /
    4.6 / 20.2; FX 1.2 / 1.1 / 1.2 / 0.7 / 1.0 / 1.3 / 0.3 / 1.7; Organic 12.2 / 9.8 / 10.3 / 14.0
    / 3.5 / 11.7 / 4.3 / 18.5. l.306 U.S. = l.297 values; l.308 Intl 10.1 / 3.6 / 8.8 / 8.4 / 3.8 /
    11.4 / 18.7 / 14.7.
- MD 1H25, l.318-341 (header l.320).
  - $: U.S. (l.322) 4,842 / 644 / 621 / 544 / 551 / 571 / 369 / 1,542; Intl (l.324) 5,422 / 614 /
    708 / 163 / 916 / 642 / 113 / 2,266; Total (l.326) 10,264 / 1,258 / 1,329 / 707 / 1,467 /
    1,213 / 482 / 3,808.
  - %: U.S. (l.330) 14.8 / 14.4 / 11.7 / 13.2 / 4.2 / 16.3 / (1.1) / 25.7. New l.332-337: Intl 9.1
    / 1.2 / 7.6 / 12.6 / 3.5 / 9.3 / 18.5 / 13.8; Total 11.7 / 7.6 / 9.5 / 13.1 / 3.8 / 12.5 / 2.9
    / 18.4; FX (0.7) / (0.4) / (0.6) / (0.2) / (0.7) / (0.7) / (0.4) / (0.7); Organic 12.4 / 8.0 /
    10.1 / 13.3 / 4.5 / 13.2 / 3.3 / 19.1. l.339 U.S. = l.330 values; l.341 Intl 10.3 / 2.0 / 8.8 /
    13.4 / 4.8 / 10.5 / 20.5 / 15.0.
  - Structural Heart 2Q25 636 (U.S. 289, Intl 347) and 1H25 1,213 (U.S. 571, Intl 642) are the
    pre-2026 composition (see Shared ground).
- Footnotes 1-2 l.391-393: 2Q25 "$11.142 billion" / Dx "$2.173 billion" / COVID "$55 million";
  2Q24 "$10.377 billion" / "$2.195 billion" / "$102 million"; 1H25 "$21.500 billion" / "$4.227
  billion" / "$139 million"; 1H24 "$20.341 billion" / "$4.409 billion" / "$306 million". No COVID
  percentages in these footnotes (the percentages are table rows l.72-74, 102-104).

### Statements of earnings

- 2Q25, l.397-441 (cols 2Q25 / 2Q24 / % Change). New l.409-419: Net Sales $11,142 / $10,377 / 7.4;
  COGS 4,854 / 4,603 / 5.5; Amortization 420 / 471 / (10.7); R&D 725 / 698 / 3.9; SG&A 3,091 /
  2,936 / 5.3; Total Operating Cost and Expenses 9,090 / 8,708 / 4.4; Operating Earnings 2,052 /
  1,669 / 23.0; Interest expense, net 50 / 58 / (14.2); Net foreign exchange (gain) loss (11) / (6)
  / 55.6. l.421 (one line): Other (income) expense, net (137) / 10 / n/m; EBT 2,150 / 1,607 /
  33.8. l.423 Taxes 371 / 305 / 21.3 [1)]; l.425 NE $1,779 / $1,302 / 36.7; l.427 NE excl.
  specified $2,213 / $2,003 / 10.5 [2)]; l.429 Diluted EPS $1.01 / $0.74 / 36.5; l.431 adjusted
  $1.26 / $1.14 / 10.5 [2)]; l.433 shares 1,751 / 1,751. Footnotes l.445-451.
  - Printed % changes on small lines differ from ratios of the rounded $m figures (interest 50 /
    58 = -13.8% vs printed (14.2); net FX (11) / (6) vs printed 55.6).
- 1H25, l.455-492 (cols 1H25 / 1H24 / % Change). New l.463-472: Net Sales $21,500 / $20,341 / 5.7;
  COGS 9,322 / 9,066 / 2.8; Amortization 840 / 943 / (10.8); R&D 1,441 / 1,382 / 4.3; SG&A 6,152 /
  5,895 / 4.4; Total Operating Cost and Expenses 17,755 / 17,286 / 2.7; Operating Earnings 3,745 /
  3,055 / 22.6; Interest expense, net 99 / 119 / (16.4). l.474 (one line): Net FX (18) / (6) / n/m;
  Other (income) expense, net (264) / (101) / n/m; EBT 3,928 / 3,043 / 29.1; Taxes 824 / 516 /
  59.5 [1)]. l.476 NE $3,104 / $2,527 / 22.9; l.478 NE excl. $4,132 / $3,732 / 10.7 [2)]; l.480 EPS
  $1.77 / $1.44 / 22.9; l.482 adjusted $2.35 / $2.12 / 10.8 [2)]; l.484 shares 1,749 / 1,750.
  Footnotes l.496-502.

### EPS reconciliations (l.506-594)

- 2Q25 l.508-527: Amortization $420 / $(420) / $— (l.514). New l.516-525: GM 5,868 / 478 / 6,346;
  R&D 725 / (20) / 705; SG&A 3,091 / (1) / 3,090; Other (137) / (1) / (138); EBT 2,150 / 500 /
  2,650; Taxes 371 / 66 / 437; NE 1,779 / 434 / 2,213; EPS $1.01 / $0.25 / $1.26. l.527: $420m +
  $80m other net expenses ("restructuring actions, costs associated with acquisitions, and other
  net expenses"; "See page 17").
- 2Q24 l.529-548: Amortization $471 / $(471) / $— (l.535). New l.537-546: GM 5,303 / 506 / 5,809;
  R&D 698 / (41) / 657; SG&A 2,936 / (57) / 2,879; Other 10 / (145) / (135); EBT 1,607 / 749 /
  2,356; Taxes 305 / 48 / 353; NE 1,302 / 701 / 2,003; EPS $0.74 / $0.40 / $1.14. l.548: $471m +
  $278m ("restructuring actions, acquisitions, a divestiture and other net expenses"; "See page
  18").
- 1H25 l.554-573: Amortization $840 / $(840) / $— (l.560). New l.562-571: GM 11,338 / 926 / 12,264;
  R&D 1,441 / (47) / 1,394; SG&A 6,152 / (11) / 6,141; Other (264) / (36) / (300); EBT 3,928 /
  1,020 / 4,948; Taxes 824 / (8) / 816; NE 3,104 / 1,028 / 4,132; EPS $1.77 / $0.58 / $2.35. l.573:
  $840m + $180m ("See page 19").
- 1H24 l.575-594: Amortization $943 / $(943) / $— (l.581). New l.583-592: GM 10,332 / 1,024 /
  11,356; R&D 1,382 / (62) / 1,320; SG&A 5,895 / (91) / 5,804; Other (101) / (171) / (272); EBT
  3,043 / 1,348 / 4,391; Taxes 516 / 143 / 659; NE 2,527 / 1,205 / 3,732; EPS $1.44 / $0.68 /
  $2.12. l.594: $943m + $405m ("See page 20").

### Tax-rate reconciliations (l.598-672; complete in both captures)

- 2Q25 (l.610-614): $2,150 / $371 / 17.3% [1)]; Specified 500 / 66; Excluding $2,650 / $437 /
  16.5%.
- 2Q24 (l.626-630): $1,607 / $305 / 19.0% [2)]; 749 / 48; $2,356 / $353 / 15.0%.
- 1H25 (l.648-652): $3,928 / $824 / 21.0% [3)]; 1,020 / (8); $4,948 / $816 / 16.5%.
- 1H24 (l.664-668): $3,043 / $516 / 17.0% [4)]; 1,348 / 143; $4,391 / $659 / 15.0%.
- Footnotes l.632 (2Q25 ~$90m benefit + ~$100m deferred-tax adjustments), l.634 (2Q24 ~$25m
  expense), l.670 (1H25 ~$90m + ~$300m), l.672 (1H24 ~$35m expense).

### Revenue reconciliation 1H (l.676-690; complete in both captures; no 2Q reconciliation)

Columns: 1H25 Abbott Reported / 1H24 Abbott Reported / Impact from business exit (a) / Adjusted
Revenue / Reported / Adjusted / Organic.

- l.684 Total Company 21,500 / 20,341 / (13) / 20,328 / 5.7 / 5.8 / 6.9; U.S. 8,444 / 7,780 / (13)
  / 7,767 / 8.5 / 8.7 / 8.7; Intl 13,056 / 12,561 / — / 12,561 / 3.9 / 3.9 / 5.8.
- l.686 Total Nutrition 4,358 / 4,218 / (13) / 4,205 / 3.3 / 3.6 / 5.1; U.S. 1,912 / 1,811 / (13) /
  1,798 / 5.6 / 6.4 / 6.4; Intl 2,446 / 2,407 / — / 2,407 / 1.6 / 1.6 / 4.1.
- l.688 Adult Nutrition 2,263 / 2,150 / (13) / 2,137 / 5.3 / 6.0 / 7.6; U.S. 737 / 733 / (13) /
  720 / 0.6 / 2.4 / 2.4; Intl 1,526 / 1,417 / — / 1,417 / 7.7 / 7.7 / 10.2.
- Footnote l.690 (a) ZonePerfect "in March 2024".

### Details of specified items (l.694-828)

- 2Q25 (page 17), l.694-724. New l.704-710: GM 1 / 55 / 420 / 2 / 478; R&D — / (7) / — / (13) /
  (20); SG&A (3) / 1 / — / 1 / (1); Other (income) expense, net (1) / — / — / — / (1); EBT 5 / 61
  / 420 / 14 / 500. l.712 Taxes (d) 66, NE $434; l.714 EPS $0.25. Footnotes l.718 a) integration
  costs only; l.722 c) MDR/IVDR only (no impairment); l.724 d) "net tax benefit associated with the
  specified items and the recognition of a tax benefit as a result of the resolution of various tax
  positions related to prior years" plus ~$100m deferred-tax adjustments.
- 2Q24 (page 18), l.728-758. New l.738-744: GM 1 / 32 / 471 / 2 / 506; R&D (1) / 1 / — / (41) /
  (41); SG&A (11) / (10) / — / (36) / (57); Other (147) / — / — / 2 / (145); EBT 160 / 41 / 471 /
  77 / 749. l.746 Taxes (d) 48, NE $701; l.748 EPS $0.40. Footnotes l.752 a) "Includes the loss on
  the sale of a non-core business. ..."; l.756 c) "... and an intangible asset impairment charge";
  l.758 d) "... and tax expense as a result of the resolution of various tax positions related to
  prior years".
- 1H25 (page 19), l.762-792. New l.772-778: GM 1 / 81 / 840 / 4 / 926; R&D (1) / (23) / — / (23) /
  (47); SG&A (6) / (6) / — / 1 / (11); Other (25) / — / — / (11) / (36); EBT 33 / 110 / 840 / 37 /
  1,020. l.780 Taxes (d) (8), NE $1,028; l.782 EPS $0.58. Footnotes l.786 a) "... as well as other
  costs related to business acquisitions" (no contingent-consideration wording, cf. D02 l.457);
  l.790 c) "... charges for investment impairments"; l.792 d) prior-year benefit + ~$300m.
- 1H24 (page 20), l.796-828. New l.806-812: GM 2 / 74 / 943 / 5 / 1,024; R&D (4) / (1) / — / (57) /
  (62); SG&A (25) / (19) / — / (47) / (91); Other (135) / — / — / (36) / (171); EBT 166 / 94 / 943
  / 145 / 1,348. l.814 Taxes (d) 143; l.816 NE $1,205; l.818 EPS $0.68. Footnotes l.822 a) "Includes
  the loss on the sale of a non-core business. ..."; l.826 c) "... investment and intangible asset
  impairments"; l.828 d) "... tax expense ...".
- Prose totals: l.449 2Q25 "net after-tax charges of $434 million, or $0.25 per share, for
  intangible amortization, charges related to restructuring and cost reduction initiatives, and
  other net expenses" (no acquisitions wording, while l.527 names "costs associated with
  acquisitions" and the details table shows acquisition EBT 5, l.710); l.451 2Q24 "$701 million, or
  $0.40" incl. "acquisitions and a divestiture"; l.500 1H25 "$1.028 billion, or $0.58"; l.502 1H24
  "$1.205 billion, or $0.68".

### Rounded prose vs table (D03)

- l.17 / 23 2Q25 growth 7.4 / 6.9 / 7.5 and l.27 1H25 5.7 / 6.9 / 7.9 match l.68-74, 97-104.
- l.19 margins (gross 52.7%, adjusted 57.0% "+100 basis point"; operating 18.4%, adjusted 22.9%
  "+100 basis point"): prose only; inputs l.411, 417, 518-521, 539-542.
- l.25 adjusted EPS "double-digit growth" vs +10.5% (l.431).
- l.316 continuous glucose monitors "$1.9 billion", +21.4% / +19.6% vs Diabetes Care 1,981, +20.2%
  / +18.5% (l.293, 302, 304).
- l.312 "double-digit growth in Diabetes Care, Heart Failure, Structural Heart and
  Electrophysiology": organic l.304 18.5 / 14.0 / 11.7 / 10.3; Rhythm Management is 10.9 reported
  (l.302) but 9.8 organic (l.304) and is not listed.
- l.41 Ford "high single-digit organic sales growth" (first half) vs 1H25 organic 6.9 / excl.
  COVID 7.9 (l.100, 104).
- l.145-147 (Nutrition, Adult), l.198-204 (Diagnostics, COVID $55m vs $102m, Core Lab), l.256-258
  (EPD, KEM), l.310 (MD) match the tables.

### Layout notes (D03)

- One-line merges: l.88, 155, 171 (row + footnote), 181, 227, 239, 293, 421, 474, 684-688, 712,
  746, 780.
- Explicit "Organic" label lines l.76 and l.106 (total-company tables only); segment-table
  geography rows are unlabelled (l.141-143, 169-171, 194-196, 227, 252-254, 281-283, 306-308,
  339-341).
- Statement 2Q25 net FX row sits inside the markdown block (l.419) while 1H25's sits in tab text
  (l.474).
- "—" as a growth value: l.218 / 227 Molecular U.S. 1H25; l.707 R&D acquisition 2Q25.
- Page pointers: l.112 "page 16", l.437 "page 13", l.488 "page 14", l.527-594 "page 17"-"page
  20", l.716/750 "page 13", l.784/820 "page 14" all land on the matching printed page.

<!-- END C1 D03 -->

<!-- C1: D04 -->
## D04 - Q3 2025 release (Oct. 15, 2025)

Periods: 3Q25 vs 3Q24; nine months 9M25 vs 9M24 ("Nine Months Ended September 30").

### Sales tables

- Total company 3Q25, l.49-78 (header l.51; l.59 "% Change vs. 3Q24").
  - $: U.S. (l.53) 4,299 / 888 / 886 / — / 2,521; Intl (l.55) 7,070 / 1,265 / 1,367 / 1,511 /
    2,927; Total reported (l.57) 11,369 / 2,153 / 2,253 / 1,511 / 5,448.
  - %: U.S. (l.61) 2.3 / (6.5) / (14.1) / n/a / 13.8. New l.63-68: Intl 9.9 / 13.3 / (1.0) / 7.5 /
    15.6; Total reported 6.9 / 4.2 / (6.6) / 7.5 / 14.8; FX 1.4 / 0.2 / 1.2 / 0.4 / 2.3; Organic
    5.5 / 4.0 / (7.8) / 7.1 / 12.5. l.70 COVID impact 1 (2.0) / — / (8.2) / — / —; l.72 Organic
    excl. COVID 7.5 / 4.0 / 0.4 / 7.1 / 12.5; l.74 "Organic"; l.76 U.S. 2.3 / (6.5) / (14.1) / n/a
    / 13.8; l.78 Intl 7.6 / 13.0 / (3.1) / 7.1 / 11.3. No business-exit row.
- Total company 9M25, l.80-112 (header l.82; l.88 "% Change vs. 9M24").
  - $: U.S. (l.84) 12,743 / 2,800 / 2,568 / — / 7,363; Intl and Total share l.86: 20,126 / 3,711 /
    3,912 / 4,154 / 8,349 and 32,869 / 6,511 / 6,480 / 4,154 / 15,712.
  - %: U.S. (l.90) 6.4 / 1.4 / (7.4) / n/a / 14.4. New l.92-98: Intl 6.0 / 5.3 / (3.3) / 5.8 /
    11.3; Total 6.1 / 3.6 / (5.0) / 5.8 / 12.8; FX (0.3) / (0.9) / (0.2) / (1.7) / 0.4; business
    exit* — / (0.2) / — / — / —; Organic 6.4 / 4.7 / (4.8) / 7.5 / 12.4. l.100 COVID impact 2
    (1.3) / — / (5.4) / — / —; l.102 Organic excl. COVID 7.7 / 4.7 / 0.6 / 7.5 / 12.4; l.104
    "Organic"; l.106 U.S. 6.5 / 1.9 / (7.4) / n/a / 14.4; l.108 Intl 6.4 / 6.9 / (3.0) / 7.5 /
    10.7. l.110 "Refer to page 16"; l.112 ZonePerfect footnote. Total-company business-exit cell
    prints "—" although the reconciliation base carries (13) (l.661).
- Nutrition 3Q25, l.116-141 (header l.120): $ U.S. (l.122) 888 / 520 / 368; Intl (l.124) 1,265 / 457
  / 808; Total (l.126) 2,153 / 977 / 1,176. % U.S. (l.130) (6.5) / (8.4) / (3.8); new l.132-137:
  Intl 13.3 / 17.9 / 10.9; Total 4.2 / 2.3 / 5.8; FX 0.2 / (0.1) / 0.4; Organic 4.0 / 2.4 / 5.4.
  l.139 U.S. (6.5) / (8.4) / (3.8); l.141 Intl 13.0 / 18.2 / 10.2.
- Nutrition 9M25, l.147-169 (header l.149): $ U.S. (l.151) 2,800 / 1,695 / 1,105; Intl and Total
  share l.153: 3,711 / 1,377 / 2,334 and 6,511 / 3,072 / 3,439. % U.S. (l.157) 1.4 / 3.0 / (0.9);
  new l.159-165: Intl 5.3 / — / 8.8; Total 3.6 / 1.6 / 5.5; FX (0.9) / (0.9) / (0.9); business
  exit* (0.2) / — / (0.4); Organic 4.7 / 2.5 / 6.8. l.167 U.S. 1.9 / 3.0 / 0.3; l.169 Intl 6.9 /
  1.8 / 10.2 plus footnote.
- Diagnostics 3Q25, l.173-194 (header l.177): $ (all on l.179) U.S. 886 / 366 / 36 / 111 / 373;
  Intl 1,367 / 998 / 95 / 47 / 227; Total 2,253 / 1,364 / 131 / 158 / 600. % U.S. (l.183) (14.1) /
  10.4 / (1.5) / 7.9 / (33.5); new l.185-190: Intl (1.0) / 1.6 / 4.3 / 8.9 / (14.2); Total (6.6) /
  3.8 / 2.6 / 8.2 / (27.3); FX 1.2 / 1.6 / 1.8 / 0.4 / 0.4; Organic (7.8) / 2.2 / 0.8 / 7.8 /
  (27.7). l.192 U.S. = l.183 values; l.194 Intl (3.1) / (0.6) / 1.7 / 7.7 / (15.6). No COVID rows in
  the Diagnostics tables.
- Diagnostics 9M25, l.202-223 (header l.204): $ U.S. (l.206) 2,568 / 1,049 / 111 / 315 / 1,093;
  Intl (l.208) 3,912 / 2,850 / 265 / 133 / 664; Total (l.210) 6,480 / 3,899 / 376 / 448 / 1,757.
  % U.S. (l.214) (7.4) / 8.3 / (0.5) / 2.4 / (21.2); new l.216-221: Intl (3.3) / (1.0) / (2.7) /
  (0.1) / (12.9); Total (5.0) / 1.3 / (2.0) / 1.7 / (18.2); FX (0.2) / (0.3) / — / (0.1) / (0.2);
  Organic (4.8) / 1.6 / (2.0) / 1.8 / (18.0). l.223 (one line) U.S. (7.4) / 8.3 / (0.5) / 2.4 /
  (21.2) and Intl (3.0) / (0.7) / (2.7) / 0.3 / (12.4).
- EPD 3Q25, l.227-250 (header l.231): $ U.S. — (l.233); Intl and Total share l.235: 1,511 / 1,097 /
  414 each. % U.S. n/a (l.239); new l.241-246: Intl 7.5 / 10.3 / 0.6; Total 7.5 / 10.3 / 0.6; FX
  0.4 / (0.8) / 3.1; Organic 7.1 / 11.1 / (2.5). l.248 U.S. n/a; l.250 Intl 7.1 / 11.1 / (2.5).
- EPD 9M25, l.256-279 (header l.258): $ U.S. — (l.260); Intl 4,154 / 3,121 / 1,033 (l.262); Total
  same (l.264). % U.S. n/a (l.268); new l.270-275: Intl 5.8 / 7.3 / 1.7; Total 5.8 / 7.3 / 1.7; FX
  (1.7) / (2.4) / 0.5; Organic 7.5 / 9.7 / 1.2. l.277 U.S. n/a; l.279 Intl 7.5 / 9.7 / 1.2.
- MD 3Q25, l.283-304 (header l.287).
  - $ (all on l.289): U.S. 2,521 / 350 / 322 / 280 / 280 / 297 / 196 / 796; Intl 2,927 / 336 / 383
    / 86 / 465 / 338 / 58 / 1,261; Total 5,448 / 686 / 705 / 366 / 745 / 635 / 254 / 2,057.
  - %: U.S. (l.293) 13.8 / 21.1 / 13.2 / 10.7 / 8.5 / 10.1 / 3.3 / 18.4. New l.295-300: Intl 15.6 /
    9.3 / 17.6 / 22.6 / 5.5 / 16.9 / 24.9 / 19.9; Total 14.8 / 15.0 / 15.6 / 13.3 / 6.6 / 13.6 /
    7.6 / 19.3; FX 2.3 / 2.0 / 1.9 / 1.2 / 1.9 / 2.3 / 0.8 / 3.1; Organic 12.5 / 13.0 / 13.7 / 12.1
    / 4.7 / 11.3 / 6.8 / 16.2. l.302 U.S. = l.293 values; l.304 Intl 11.3 / 5.5 / 14.1 / 17.2 / 2.5
    / 12.4 / 21.2 / 14.7.
- MD 9M25, l.312-333 (header l.314).
  - $: U.S. (l.316) 7,363 / 994 / 943 / 824 / 831 / 868 / 565 / 2,338; Intl and Total share l.318:
    8,349 / 950 / 1,091 / 249 / 1,381 / 980 / 171 / 3,527 and 15,712 / 1,944 / 2,034 / 1,073 /
    2,212 / 1,848 / 736 / 5,865.
  - %: U.S. (l.322) 14.4 / 16.7 / 12.2 / 12.4 / 5.6 / 14.1 / 0.3 / 23.2. New l.324-329: Intl 11.3 /
    3.9 / 10.9 / 15.9 / 4.2 / 11.8 / 20.6 / 15.9; Total 12.8 / 10.1 / 11.5 / 13.2 / 4.7 / 12.9 /
    4.4 / 18.7; FX 0.4 / 0.4 / 0.2 / 0.3 / 0.1 / 0.4 / (0.1) / 0.6; Organic 12.4 / 9.7 / 11.3 / 12.9
    / 4.6 / 12.5 / 4.5 / 18.1. l.331 U.S. = l.322 values; l.333 Intl 10.7 / 3.2 / 10.5 / 14.6 / 4.0
    / 11.2 / 20.8 / 14.9.
  - Structural Heart 3Q25 635 (U.S. 297, Intl 338) and 9M25 1,848 are the pre-2026 composition; no
    recast of 3Q25 or 9M25 is recorded for D07/D08/D10 in notes/doc-map.md.
- Footnotes 1-2 l.379-381: 3Q25 "$11.369 billion" / Dx "$2.253 billion" / COVID "$69 million";
  3Q24 "$10.635 billion" / "$2.412 billion" / "$265 million"; 9M25 "$32.869 billion" / "$6.480
  billion" / "$208 million"; 9M24 "$30.976 billion" / "$6.821 billion" / "$571 million".

### Statements of earnings

- 3Q25, l.385-426 (cols 3Q25 / 3Q24 / % Change). New l.397-406: Net Sales $11,369 / $10,635 / 6.9;
  COGS 5,075 / 4,698 / 8.0; Amortization 420 / 470 / (10.8); R&D 766 / 713 / 7.5; SG&A 3,051 /
  2,895 / 5.4; Total Operating Cost and Expenses 9,312 / 8,776 / 6.1; Operating Earnings 2,057 /
  1,859 / 10.6; Interest expense, net 44 / 51 / (12.6). l.408 (one line): Net FX (17) / (11) / n/m;
  Other (income) expense, net (150) / (121) / 23.7; EBT 2,180 / 1,940 / 12.3; Taxes 536 / 294 /
  82.0 [1)]. l.410 NE $1,644 / $1,646 / (0.1); l.412 NE excl. specified $2,278 / $2,119 / 7.5
  [2)]; l.414 Diluted EPS $0.94 / $0.94 / —; l.416 adjusted $1.30 / $1.21 / 7.4 [2)]; l.418 shares
  1,749 / 1,748. Footnotes l.430-434 (3Q24 has no tax footnote).
- 9M25, l.438-471 (cols 9M25 / 9M24 / % Change). New l.442-451: Net Sales $32,869 / $30,976 / 6.1;
  COGS 14,397 / 13,764 / 4.6; Amortization 1,260 / 1,413 / (10.8); R&D 2,207 / 2,095 / 5.4; SG&A
  9,203 / 8,790 / 4.7; Total Operating Cost and Expenses 27,067 / 26,062 / 3.9; Operating Earnings
  5,802 / 4,914 / 18.1; Interest expense, net 143 / 170 / (15.3). l.453 (one line): Net FX (35) /
  (17) / n/m; Other (income) expense, net (414) / (222) / 86.8; EBT 6,108 / 4,983 / 22.6; Taxes
  1,360 / 810 / 67.7 [1)]. l.455 NE $4,748 / $4,173 / 13.8; l.457 NE excl. $6,410 / $5,851 / 9.6
  [2)]; l.459 EPS $2.70 / $2.38 / 13.4; l.461 adjusted $3.65 / $3.33 / 9.6 [2)]; l.463 shares 1,749
  / 1,749. Footnotes l.475-481.

### EPS reconciliations (l.485-573)

- 3Q25 l.487-506: Amortization $420 / $(420) / $— (l.493). New l.495-504: GM 5,874 / 470 / 6,344;
  R&D 766 / (36) / 730; SG&A 3,051 / (47) / 3,004; Other (150) / 5 / (145); EBT 2,180 / 548 /
  2,728; Taxes 536 / (86) / 450; NE 1,644 / 634 / 2,278; EPS $0.94 / $0.36 / $1.30. l.506: $420m +
  $128m ("restructuring actions, costs associated with acquisitions, and other net expenses"; "See
  page 17").
- 3Q24 l.508-527: Amortization $470 / $(470) / $— (l.514). New l.516-525: GM 5,467 / 516 / 5,983;
  R&D 713 / (19) / 694; SG&A 2,895 / (5) / 2,890; Other (121) / (12) / (133); EBT 1,940 / 552 /
  2,492; Taxes 294 / 79 / 373; NE 1,646 / 473 / 2,119; EPS $0.94 / $0.27 / $1.21. l.527: $470m +
  $82m ("charges related to intangible impairment, acquisitions, a divestiture and other net
  expenses"; "See page 18").
- 9M25 l.533-552: Amortization $1,260 / $(1,260) / $— (l.539). New l.541-550: GM 17,212 / 1,396 /
  18,608; R&D 2,207 / (83) / 2,124; SG&A 9,203 / (58) / 9,145; Other (414) / (31) / (445); EBT
  6,108 / 1,568 / 7,676; Taxes 1,360 / (94) / 1,266; NE 4,748 / 1,662 / 6,410; EPS $2.70 / $0.95 /
  $3.65. l.552: $1.260bn + $308m ("See page 19").
- 9M24 l.554-573: Amortization $1,413 / $(1,413) / $— (l.560). New l.562-571: GM 15,799 / 1,540 /
  17,339; R&D 2,095 / (81) / 2,014; SG&A 8,790 / (96) / 8,694; Other (222) / (183) / (405); EBT
  4,983 / 1,900 / 6,883; Taxes 810 / 222 / 1,032; NE 4,173 / 1,678 / 5,851; EPS $2.38 / $0.95 /
  $3.33. l.573: $1.413bn + $487m ("See page 20").

### Tax-rate reconciliations (l.577-649; complete in both captures)

- 3Q25 (l.589-593): $2,180 / $536 / 24.6% [1)]; Specified 548 / (86); Excluding $2,728 / $450 /
  16.5%.
- 3Q24 (l.605-609): $1,940 / $294 / 15.2% (no footnote marker); 552 / 79; $2,492 / $373 / 15.0%.
- 9M25 (l.625-629): $6,108 / $1,360 / 22.3% [2)]; 1,568 / (94); $7,676 / $1,266 / 16.5%.
- 9M24 (l.641-645): $4,983 / $810 / 16.3% [3)]; 1,900 / 222; $6,883 / $1,032 / 15.0%.
- Footnotes l.611 (3Q25: "2025 Taxes on Earnings also includes approximately $160 million ..."; the
  word "also" follows no first item, same at l.430), l.647 (9M25 ~$90m benefit + ~$460m), l.649
  (9M24 ~$35m expense). Rates printed with a tab before "%" (e.g. l.589 "24.6	%").

### Revenue reconciliation 9M (l.653-667; complete in both captures; no 3Q reconciliation)

Columns: 9M25 Abbott Reported / 9M24 Abbott Reported / Impact from business exit (a) / Adjusted
Revenue / Reported / Adjusted / Organic.

- l.661 Total Company 32,869 / 30,976 / (13) / 30,963 / 6.1 / 6.1 / 6.4; U.S. 12,743 / 11,982 /
  (13) / 11,969 / 6.4 / 6.5 / 6.5; Intl 20,126 / 18,994 / — / 18,994 / 6.0 / 6.0 / 6.4.
- l.663 Total Nutrition 6,511 / 6,284 / (13) / 6,271 / 3.6 / 3.8 / 4.7; U.S. 2,800 / 2,761 / (13) /
  2,748 / 1.4 / 1.9 / 1.9; Intl 3,711 / 3,523 / — / 3,523 / 5.3 / 5.3 / 6.9.
- l.665 Adult Nutrition 3,439 / 3,261 / (13) / 3,248 / 5.5 / 5.9 / 6.8; U.S. 1,105 / 1,115 / (13) /
  1,102 / (0.9) / 0.3 / 0.3; Intl 2,334 / 2,146 / — / 2,146 / 8.8 / 8.8 / 10.2.
- Footnote l.667 (a) ZonePerfect, "initiated in March 2024".

### Details of specified items (l.671-812)

- 3Q25 (page 17), l.671-701. New l.681-687: GM — / 44 / 420 / 6 / 470 ("Gross Margin $" label
  cell); R&D — / (19) / — / (17) / (36); SG&A (9) / (43) / — / 5 / (47); Other (income) expense,
  net 7 / — / — / (2) / 5; EBT 2 / 106 / 420 / 20 / 548. l.689 Taxes (d) (86), NE $634; l.691 EPS
  $0.36. Footnotes l.695 a) integration costs only; l.699 c) MDR/IVDR only; l.701 d) "net tax
  benefit associated with the specified items" plus ~$160m deferred-tax adjustments.
- 3Q24 (page 18), l.705-738. New l.715-720: GM — / 2 / 470 / 44 / 516 ("Gross Margin $" label
  cell); R&D — / — / — / (19) / (19); SG&A (7) / 2 / — / — / (5); Other (5) / — / — / (7) / (12).
  l.722 EBT row printed as tab text outside the markdown block: "$ 12 $ — $ 470 $ 70 552"
  (restructuring nets to "—": GM 2 offset by SG&A +2). l.724 Taxes (d) 79; l.726 NE $473; l.728 EPS
  $0.27. Footnotes l.732 a) integration costs only (no "loss on the sale of a non-core business",
  although the 3Q24 descriptions l.434 and l.527 name "a divestiture"); l.736 c) MDR/IVDR "and
  investment and intangible asset impairment charges"; l.738 d) plain.
- 9M25 (page 19), l.742-776. New l.756-762: GM 1 / 125 / 1,260 / 10 / 1,396; R&D (1) / (42) / — /
  (40) / (83); SG&A (15) / (49) / — / 6 / (58); Other (18) / — / — / (13) / (31); EBT 35 / 216 /
  1,260 / 57 / 1,568. l.764 Taxes (d) (94), NE $1,662; l.766 EPS $0.95. Footnotes l.770 a) "... as
  well as other costs related to business acquisitions"; l.774 c) "... charges for investment
  impairments"; l.776 d) prior-year benefit + ~$460m.
- 9M24 (page 20), l.780-812. New l.790-796: GM 2 / 76 / 1,413 / 49 / 1,540; R&D (4) / (1) / — / (76)
  / (81); SG&A (32) / (17) / — / (47) / (96); Other (140) / — / — / (43) / (183); EBT 178 / 94 /
  1,413 / 215 / 1,900. l.798 Taxes (d) 222; l.800 NE $1,678; l.802 EPS $0.95. Footnotes l.806 a)
  "Includes the loss on the sale of a non-core business. ..."; l.810 c) "... investment and
  intangible asset impairments"; l.812 d) "... tax expense ...".
- Prose totals: l.432 3Q25 "net after-tax charges of $634 million, or $0.36 per share, for
  intangible amortization, charges related to restructuring and cost reduction initiatives, and
  other net expenses" (no acquisitions wording; l.506 names "costs associated with acquisitions";
  details acquisition EBT 2, l.687); l.434 3Q24 "$473 million, or $0.27" ("charges related to
  intangible impairment, expenses associated with acquisitions and a divestiture"; no restructuring
  wording, matching the "—" restructuring EBT at l.722); l.479 9M25 "$1.662 billion, or $0.95";
  l.481 9M24 "$1.678 billion, or $0.95".

### Rounded prose vs table (D04)

- l.17 / 23 3Q25 growth 6.9 / 5.5 / 7.5 and l.27 YTD 6.1 / 6.4 / 7.7 match l.66-72, 95-102.
- l.19 operating margin 18.1%, adjusted 23.0% "+40 basis point": prose only; inputs l.399, 405,
  497-500, 518-521. No gross-margin bullet.
- l.25 adjusted EPS bullet states no growth; table +7.4% (l.416).
- l.310 continuous glucose monitors "$2.0 billion", +20.5% / +17.2% vs Diabetes Care 2,057, +19.3%
  / +16.2% (l.289, 298, 300).
- l.308 "double-digit growth in Diabetes Care, Electrophysiology, Rhythm Management, Heart Failure
  and Structural Heart": the order follows the organic row l.300 (16.2 / 13.7 / 13.0 / 12.1 /
  11.3); on the reported row l.298 Structural Heart 13.6 is above Heart Failure 13.3.
- l.143-145, 196-200 (Dx -6.6 / -7.8 / +0.4; COVID $69m vs $265m; Core Lab 3.8 / 2.2), l.252-254,
  l.306 match the tables.

### Layout notes (D04)

- One-line merges: l.86, 153, 169 (row + footnote), 179, 223, 235, 289, 318, 408, 453, 661-665,
  689, 764.
- l.722 EBT row outside its markdown block (above). Explicit "Organic" label lines l.74, l.104.
- "—" as a value: l.97 total business exit 9M25; l.161 Pediatric Intl 9M25 growth; l.220 Molecular
  FX 9M25; l.414 EPS % change; detail-table cells l.683-684, 717-718, 722.
- Page pointers: l.110 "page 16", l.422 "page 13", l.467 "page 14", l.506-573 "page 17"-"page 20",
  l.693/730 "page 13", l.768/804 "page 14" all land on the matching printed page.

<!-- END C1 D04 -->

<!-- C1: shared -->
## Shared ground (tables, 2025 releases)

Facts and locations only. Arithmetic below is addition/subtraction of printed figures, done in
this pass. D07/D08/D10 figures are cited from notes/doc-map.md sections, not re-read here.

### A. Year-to-date tables vs quarterly tables

- Sales $: every U.S. / Intl / Total cell of D03's 1H25 tables (total company, Nutrition,
  Diagnostics, EPD, MD) equals D02 1Q25 + D03 2Q25, and every cell of D04's 9M25 tables equals D03
  1H25 + D04 3Q25 (e.g. Total 10,358 + 11,142 = 21,500; 21,500 + 11,369 = 32,869; Diabetes Care
  1,827 + 1,981 = 3,808; 3,808 + 2,057 = 5,865; Structural Heart 577 + 636 = 1,213; 1,213 + 635 =
  1,848).
- Statements, EPS reconciliations and specified-items details: D03 1H25 and 1H24 = D02 1Q + D03 2Q
  in every cell, per-share included ($0.76 + $1.01 = $1.77; $0.70 + $0.74 = $1.44). D04 9M24 = D03
  1H24 + D04 3Q24 in every cell. D04 9M25 = D03 1H25 + D04 3Q25 in every dollar cell; per-share
  exceptions: GAAP EPS $1.77 + $0.94 = $2.71 vs printed $2.70 (D04 l.459, 550); specified items per
  share $0.58 + $0.36 = $0.94 vs printed $0.95 (D04 l.550, 766). Adjusted EPS sums ($2.35 + $1.30 =
  $3.65).
- FY2024 (D01) vs 9M24 (D04) + 4Q24 (D01): all statement dollar lines sum (e.g. Net Sales 30,976 +
  10,974 = 41,950; taxes 810 + (7,199) = (6,389)); per-share exceptions GAAP EPS $2.38 + $5.27 =
  $7.65 vs $7.64 (D01 l.550) and specified $0.95 + $(3.93) = $(2.98) vs $(2.97) (D01 l.647, 896);
  adjusted $3.33 + $1.34 = $4.67. Footnote and reconciliation dollars chain: Diagnostics 6,821 +
  2,520 = 9,341; COVID 571 + 176 = 747; U.S. 11,982 + 4,341 = 16,323; Intl 18,994 + 6,633 = 25,627;
  Nutrition 6,284 + 2,129 = 8,413; Adult Nutrition 3,261 + 1,129 = 4,390. 2024 quarter totals
  9,964 (D02 l.268) + 10,377 (D03 l.391) + 10,635 (D04 l.379) + 10,974 (D01 l.414) = 41,950; COVID
  204 + 102 + 265 + 176 = 747; 2025 COVID 84 + 55 + 69 = 208 (D04 l.381).
- Exception in the 2024 specified-items category split: see C2.
- Within D01-D04 no prior-year column covers a period that an earlier D01-D04 release printed as
  its current period (D01 prior year = 4Q23/12M23; D02 = 1Q24; D03 = 2Q24/1H24; D04 = 3Q24/9M24),
  so there are no direct comparative repeats among these four; the overlaps are the YTD sums above.
- Excluding-specified tax rate: 15.0% in every 2024 period printed (D01 l.692, 726; D02 l.407; D03
  l.630, 668; D04 l.609, 645); 14.0% for 4Q23 and 12M23 (D01 l.708, 742); 16.5% in every 2025 period
  (D02 l.391; D03 l.614, 652; D04 l.593, 629).
- 2024 prior-year-tax-position items appear only as comparatives in D02-D04 (1Q24 ~$10m expense
  D02 l.411; 2Q24 ~$25m D03 l.634; 1H24 ~$35m D03 l.672; 9M24 ~$35m D04 l.649; 3Q24 none, D04
  l.605); D01's 2024 footnotes (l.517, 568, 744) name only the $7.497bn valuation-allowance item.

### B. Quarters derivable from year-to-date bases (not printed as such in D01-D04)

- 2Q24 = D03 1H24 base (l.684-688) - D02 1Q24 base (l.423-427): Total 20,341 - 9,964 = 10,377
  (printed in D03 l.391, 411); U.S. 7,780 - 3,846 = 3,934; Intl 12,561 - 6,118 = 6,443; Nutrition
  4,218 - 2,068 = 2,150; Adult Nutrition 2,150 - 1,059 = 1,091.
- 3Q24 = D04 9M24 base (l.661-665) - D03 1H24 base: Total 30,976 - 20,341 = 10,635 (printed D04
  l.379, 399); U.S. 11,982 - 7,780 = 4,202; Intl 18,994 - 12,561 = 6,433; Nutrition 6,284 - 4,218 =
  2,066; Adult 3,261 - 2,150 = 1,111.
- 2Q24 and 3Q24 Diagnostics totals and COVID sales are printed only in footnotes (D03 l.391 $2.195bn
  / $102m; D04 l.379 $2.412bn / $265m). 2Q24 and 3Q24 sub-business, EPD and MD dollars are not
  printed in D01-D04 (growth % only).
- 4Q24 (printed in D01) equals D01 12M24 - D04 9M24 for the rows above.
- 4Q25: notes/doc-map.md "D07" Tables bullet records 12M25 Total 44,328, U.S. 17,126, Intl 27,202,
  Nutrition 8,451, Diagnostics 8,937, EPD 5,536, MD 21,387, Diabetes Care 7,998; minus D04 9M25
  (l.84-86, 318) gives 11,459 / 4,383 / 7,076 / 1,940 / 2,457 / 1,382 / 5,675 / 2,133, the D07
  4Q25 values recorded in that same bullet.

### C. Same-period figures that differ between releases

1. ZonePerfect "business exit" impact for 2024 periods. D01 current-year columns: 4Q24 (1)
   (l.764-768), 12M24 (14) (l.780-784). D02-D04 prior-year bases: 1Q24 (13) (D02 l.423-427), 1H24
   (13) (D03 l.684-688), 9M24 (13) (D04 l.661-665). D07's 12M24 base is (13) per notes/doc-map.md
   D07 "Tables" (revenue reconciliation bullet) and Shared ground item (3). So 12M24 = (14) in D01
   vs (13) in D07; no release states a revision or precedence. Prior-year amounts 4Q23 (17) and
   12M23 (49) appear only in D01.
2. Specified-items category split, 2024. "Other (income) expense, net" row: D01 12M24
   Acquisition (155) / Other (8) (l.891) minus D01 4Q24 (2) / 22 (l.819) = (153) / (30), vs D04
   9M24 (140) / (43) (l.795); the row total agrees ((163) - 20 = (183)). EBT by category: D01 12M24
   Acquisition 199 / Other 371 (l.892) vs D04 9M24 178 / 215 (l.796) + D01 4Q24 8 / 169 (l.820) =
   186 / 384; total 2,633 = 1,900 + 733. Every other cell of the 2024 details chains exactly (D02
   1Q24 + D03 2Q24 = D03 1H24; + D04 3Q24 = D04 9M24). No release mentions a reclassification.
   D07 prints 12M24 details as comparatives; that block should be compared with D01 l.886-896.
3. Specified-items wording for the same items: 3Q24 prose names "a divestiture" (D04 l.434, 527)
   but the 3Q24 details footnote a) (D04 l.732) has no "loss on the sale of a non-core business"
   (present for 2Q24 D03 l.752, 1H24 D03 l.822, 9M24 D04 l.806, 12M24 D01 l.900). Within a
   release: 2Q25 (D03 l.449) and 3Q25 (D04 l.432) prose totals omit acquisitions while the
   EPS-reconciliation prose (D03 l.527; D04 l.506) and details tables (acquisition EBT 5, D03 l.710;
   2, D04 l.687) include them.
4. No 2025 period is printed twice within D01-D04, and every 2025 YTD cell equals the sum of the
   printed quarters except the per-share items in A.

### D. Repeats and conflicts with D07, D08, D10 (as recorded in notes/doc-map.md)

- D01 -> D07 comparatives: doc-map D07 Tables ("The 4Q24/12M24 columns repeat D01 l.407-461", old
  numbering = current D01 l.480-554, now including the top statement rows l.480-489, 531-540) and
  doc-map Shared ground "Repeated comparatives" (4Q24/FY2024 statement lines, tax rates,
  $6.880bn / $5.202bn specified items, $7.497bn footnote; 4Q24 COVID $176m, Dx $2.520bn; FY2024
  $41.950bn / Dx $9.341bn / COVID $747m). Current D01 locations: l.480-554, 517-574, 688-746, 210,
  414-416, 428, 454.
- D07 vs D01 wording for 4Q24 (doc-map D07 "Amendments or contradictions"): D07 4Q24 (a) adds "as
  well as other costs related to business acquisitions" (absent at D01 l.828); D07 4Q24
  other-net-expense prose omits "intangible impairments" (present at D01 l.601). Business-exit
  (14) vs (13): C1.
- D02 -> D08: doc-map D08 Tables says the 1Q25 statement column repeats D02 (old l.259-271 =
  current l.284-307, top rows newly visible at l.286-293) and the 1Q25 tax rates 25.5% / 16.5%
  (current D02 l.387-391). Recast: D08 1Q25 Structural Heart 531 (U.S. 248 / Intl 283) vs D02 577
  (U.S. 282 / Intl 295) at current D02 l.195 ("$46 million" moved with the Amulet transfer "on Jan.
  1, 2026", doc-map D08). D08 1Q25 comparable base 10,358 + 707 - 24 = 11,041; D02's own
  reconciliation shows 1Q25 with no adjustment (l.423). Wording conflict (doc-map D08 "Amendments
  or contradictions"): D08 "net after-tax benefits of $594 million" vs D02 l.323 "net after-tax
  charges of $594 million, or $0.33 per share".
- D03 -> D10: doc-map D10 Tables records 2Q25 "Interest expense, net" 50 and net FX (11) and 1H25
  interest expense 99 as D10 comparatives; D03 now shows the same values at l.418, 419 and 472
  (doc-map Shared ground's remark that these rows had "no visible D03 counterpart" is superseded).
  Recast: D10 2Q25 Structural Heart 581 (U.S. 249 / Intl 332) vs D03 636 (U.S. 289 / Intl 347) at
  current l.293; 1H25 1,112 vs D03 1,213 at current l.326 ($55m and $101m moved, doc-map D10). D10
  comparable bases 2Q25 11,142 + 811 - 22 = 11,931 and 1H25 21,500 + 1,518 - 46 = 22,972; D03's 1H
  reconciliation shows 1H25 with no adjustment (l.684).
- D04 -> D07: 4Q25 derivable (B). doc-map D07 Notes: FY2025 specified $2.516bn = D04 9M25 $1.662bn
  (l.479) + D07 4Q25 $854m; per share $1.43 vs $0.95 + $0.49 (doc-map Shared ground).
- D01-D04 contain no "comparable", Exact Sciences or multi-year-agreement columns (those are in
  D08/D10 per doc-map).

### E. Basis and coverage differences across D01-D04 tables

- Geography rows under organic headings: D01 total-company and Diagnostics tables = excl.-COVID
  (unlabelled); D02 total company = organic (no COVID rows at all); D03/D04 total company =
  organic under an explicit "Organic" label (l.76/106; l.74/104); segment tables in all four =
  organic (unlabelled). Organic incl. COVID by geography for 4Q24/12M24 is only in D01's revenue
  reconciliation (l.764, 780).
- COVID rows: D01 total-company and Diagnostics tables plus footnote-3 dollar tables; D02 none
  (footnote prose l.268); D03 and D04 total-company tables only.
- Business-exit / acquisition rows: D01 4Q24 and 12M24 ("business exit and acquisition"; MD
  "Impact of acquisition"); D02 1Q25; D03 1H25 only (not 2Q25); D04 9M25 only (total cell "—").
- Revenue reconciliations: D01 4Q and 12M (Total, Nutrition, Adult Nutrition, MD, Vascular;
  current-year adjustments); D02 1Q, D03 1H, D04 9M (Total, Nutrition, Adult Nutrition; prior-year
  exit only). No 2Q or 3Q reconciliation.
- MD column label "Electro-physiology" in D01 (l.309, 338), "Electrophysiology" in D02-D04.
- Definitions governing the FX and organic rows: FX method note, identical wording (current-year
  U.S. dollar sales restated at prior-year average rates): D01 l.53, D02 l.45, D03 l.49, D04 l.47.
  Organic = excludes FX and the ZonePerfect discontinuation: D01 l.51, D02 l.43, D03 l.47, D04
  l.45; the excl.-COVID rationale sentence is in D01 l.51, D03 l.47, D04 l.45 and absent in D02.
  No D01-D04 footnote states a reclassification or restatement; divestiture wording ("loss on the
  sale of a non-core business") is limited to the 2024 details footnotes listed in C3.
- Narrative passages repeating table results are listed in each document's "Rounded prose vs
  table" subsection; CGM dollar figures ($1.8bn, $1.7bn, $1.9bn, $2.0bn) are prose only, beside
  Diabetes Care columns 1,863 / 1,827 / 1,981 / 2,057. Margin percentages (D01 l.29 bp changes;
  D02, D03, D04 headline l.19) are prose only; their inputs are in the statements and EPS
  reconciliations.

### F. Layout summary (D01-D04)

- Formerly clipped ranges render as markdown blocks with empty header cells; rows before and
  after are tab text. No merged cells inside the blocks.
- Several rows per line in the revenue reconciliations (D01 l.764-788; D02 l.423-427; D03
  l.684-688; D04 l.661-665) and in Diagnostics/MD dollar rows (D01 l.189, 311; D02 l.195; D03 l.181,
  293; D04 l.179, 289); full lists per document above.
- "Gross Margin $" label cell (D01 l.816; D02 l.445; D04 l.683, 717); D04 l.722 EBT row outside
  its block; "—" used for zero, none or not applicable; D01/D02 l.11 "Exhibit 99.1 9.1".
- No U+FFFD and no gap markers in D01-D04.

### G. Gaps

- D01-D04: none. Every line read; no missing source text. Out of scope here: D07, D08, D10
  newly visible blocks (parallel mapper), including D07's 12M24 specified-items comparative needed
  to place C2.

<!-- END C1 shared -->
