# aq-00745 - table map, 2026 earnings releases (D07, D08, D10) - pass C2

Written 2026-10-05 by `bundle-mapper` pass C2 from the CURRENT `text/D07.txt`, `text/D08.txt`,
`text/D10.txt` (complete capture AQ-00745_2026-10-06_0256.md, re-split with
`tools/split_capture.py --force`). Navigation only: facts and locations. The pass-A sections of
`notes/doc-map.md` for D07/D08/D10 use OLD (clipped-text) line numbers; `notes/line-remap.md`
maps them. Every line number below is a current text line. D01-D04 figures are quoted only from
`notes/doc-map.md` (cited by section; their line numbers there are old-text lines).

## Conventions

- docs l. = text l. - 2 (header line + blank added by extraction) in all three documents.
- $ in millions unless labelled; EPS in dollars; growth % one decimal; parentheses = negative;
  "—" = nil, or a value that rounds to zero (also used as a growth value, e.g. D10 l.90, 144);
  "n/a" = not applicable; "n/m" = "Percent change is not meaningful".
- Values are listed in the column order stated for each table; "|" separates column groups.
- In quoted layout strings "\t" stands for a tab character in the text file.
- "NEW" = rows clipped in the 2026-10-05 capture and visible now (ranges from line-remap.md).
- Sales tables: geography rows printed after the last growth row are the organic (D07) or
  comparable (D08/D10) geography rows; their label is the preceding "Organic" / "Comparable
  sales growth" row (the old map's "label in gap" is resolved).

<!-- C2: D07 -->
## D07 - Abbott Q4 and Full-Year 2025 release (Jan. 22, 2026; 4Q25/12M25)

### Ledger and spot-checks

- Read in order, every line: l.1-110, 110-244, 244-363, 363-472, 472-601, 601-705, 705-836
  (836 = trailing empty line). Unread: none.
- NEW ranges (all read): 65-70, 92-98, 130-135, 155-161, 181-186, 212-217, 237-242, 266-271,
  291-296, 318-323 (sales growth rows); 393-402, 454-463 (statement top rows); 519-528, 538-547,
  561-570, 580-589 (non-GAAP reconciliation rows); 697-703, 735-741, 773-779, 811-817 (specified
  details body rows).
- Printed pages "Page 1 of 20" (l.43) ... "Page 20 of 20" (l.835). Charts: not applicable.
- Spot-checks vs docs/abt_ex991_2026-01-22.txt (833 lines): table row "| Gross Margin | 6,115 |
  428 | 6,543 |" docs l.519 = text l.521; footnote "c)Other includes $165 million ..." docs l.715 =
  text l.717; "| Gross Margin $ | — | $ 49 | ..." docs l.735 = text l.737. No gap markers in text or
  docs. Visual page: unresolved (the capture is the only original).

### Sales tables (D07)

- T1 Total company 4Q25, l.51-80, "Sales 4Q25 ($ in millions)"; columns Total Company /
  Nutrition / Diagnostics / Established Pharmaceuticals / Medical Devices.
  - U.S. 4,383 / 806 / 967 / — / 2,605 (l.55); International 7,076 / 1,134 / 1,490 / 1,382 /
    3,070 (l.57); Total reported 11,459 / 1,940 / 2,457 / 1,382 / 5,675 (l.59).
  - "% Change vs. 4Q24" (l.61): U.S. 0.9 / (13.2) / (8.4) / n/a / 10.7 (l.63). NEW l.65-70:
    International 6.7 / (5.6) / 1.8 / 9.0 / 13.7; Total reported 4.4 / (8.9) / (2.5) / 9.0 / 12.3;
    Impact of foreign exchange 1.4 / 0.2 / 1.1 / 2.0 / 1.9; Organic 3.0 / (9.1) / (3.6) / 7.0 / 10.4.
  - "Impact of COVID-19 testing sales 1" (0.8) / — / (3.4) / — / — (l.72); "Organic (excluding
    COVID-19 tests)" 3.8 / (9.1) / (0.2) / 7.0 / 10.4 (l.74); label "Organic" (l.76); U.S. 0.9 /
    (13.2) / (8.4) / n/a / 10.7 (l.78); International 4.3 / (5.9) / (0.2) / 7.0 / 10.1 (l.80).
- T2 Total company 12M25, l.80-110, "Sales 12M25"; same columns.
  - U.S. 17,126 / 3,606 / 3,535 / — / 9,968 (l.84); International 27,202 / 4,845 / 5,402 / 5,536 /
    11,419 and Total reported 44,328 / 8,451 / 8,937 / 5,536 / 21,387 (both l.86).
  - "% Change vs. 12M24" (l.88): U.S. 4.9 / (2.3) / (7.7) / n/a / 13.4 (l.90). NEW l.92-98:
    International 6.1 / 2.6 / (2.0) / 6.6 / 12.0; Total reported 5.7 / 0.4 / (4.3) / 6.6 / 12.6;
    Impact of foreign exchange 0.2 / (0.7) / 0.2 / (0.8) / 0.7; "Impact of business exit*" — /
    (0.1) / — / — / —; Organic 5.5 / 1.2 / (4.5) / 7.4 / 11.9.
  - "Impact of COVID-19 testing sales 2" (1.2) / — / (4.9) / — / — (l.100); Organic excl. COVID
    6.7 / 1.2 / 0.4 / 7.4 / 11.9 (l.102); "Organic" (l.104); U.S. 5.0 / (1.9) / (7.7) / n/a / 13.4
    (l.106); International 5.9 / 3.7 / (2.3) / 7.4 / 10.5 (l.108). Footnote * ZonePerfect
    discontinued "in March 2024" (l.110). The business-exit row exists only in 12M tables.
- T3 Nutrition 4Q25, l.116-139; columns Total / Pediatric / Adult.
  - U.S. 806 / 463 / 343; International 1,134 / 439 / 695; Total reported 1,940 / 902 / 1,038
    (l.120-124). % vs 4Q24: U.S. (13.2) / (17.7) / (6.3) (l.128). NEW l.130-135: International
    (5.6) / 0.3 / (8.9); Total reported (8.9) / (9.8) / (8.1); FX 0.2 / 0.3 / 0.1; Organic (9.1) /
    (10.1) / (8.2). Organic U.S. (13.2) / (17.7) / (6.3) (l.137); Intl (5.9) / (0.3) / (9.1) (l.139).
- T4 Nutrition 12M25, l.143-165.
  - U.S. 3,606 / 2,158 / 1,448 (l.147); International 4,845 / 1,816 / 3,029 and Total reported
    8,451 / 3,974 / 4,477 (l.149). % vs 12M24: U.S. (2.3) / (2.3) / (2.2) (l.153). NEW l.155-161:
    International 2.6 / 0.1 / 4.1; Total reported 0.4 / (1.2) / 2.0; FX (0.7) / (0.5) / (0.7);
    business exit* (0.1) / — / (0.3); Organic 1.2 / (0.7) / 3.0. Organic U.S. (1.9) / (2.3) / (1.4)
    (l.163); Intl 3.7 / 1.3 / 5.1 (l.165).
- T5 Diagnostics 4Q25, l.171-190; columns Total / Core Laboratory / Molecular / Point of Care /
  Rapid Diagnostics (pre-2026 grouping).
  - U.S. 967 / 376 / 39 / 107 / 445; International 1,490 / 1,085 / 102 / 51 / 252; Total reported
    2,457 / 1,461 / 141 / 158 / 697 (all l.175). % vs 4Q24: U.S. (8.4) / 3.6 / 2.9 / 6.5 / (19.7)
    (l.179). NEW l.181-186: International 1.8 / 5.9 / 3.3 / 9.8 / (14.1); Total reported (2.5) /
    5.3 / 3.2 / 7.5 / (17.8); FX 1.1 / 1.7 / 2.1 / 0.4 / 0.3; Organic (3.6) / 3.6 / 1.1 / 7.1 /
    (18.1). Organic U.S. (8.4) / 3.6 / 2.9 / 6.5 / (19.7) (l.188); Intl (0.2) / 3.6 / 0.4 / 8.3 /
    (14.9) (l.190). No COVID row in segment tables (COVID impact only in T1/T2).
- T6 Diagnostics 12M25, l.198-219.
  - U.S. 3,535 / 1,425 / 150 / 422 / 1,538 (l.202); International 5,402 / 3,935 / 367 / 184 / 916
    (l.204); Total reported 8,937 / 5,360 / 517 / 606 / 2,454 (l.206). % vs 12M24: U.S. (7.7) / 7.0
    / 0.4 / 3.4 / (20.8) (l.210). NEW l.212-217: International (2.0) / 0.8 / (1.1) / 2.5 / (13.3);
    Total reported (4.3) / 2.4 / (0.7) / 3.1 / (18.1); FX 0.2 / 0.3 / 0.5 / — / (0.1); Organic
    (4.5) / 2.1 / (1.2) / 3.1 / (18.0). Organic U.S. (7.7) / 7.0 / 0.4 / 3.4 / (20.8) and Intl (2.3)
    / 0.4 / (1.8) / 2.4 / (13.1) (both l.219).
- T7 Established Pharmaceuticals 4Q25, l.225-246; columns Total / Key Emerging Markets / Other.
  - U.S. — (l.229); International and Total reported 1,382 / 1,046 / 336 (l.231). NEW l.237-242:
    International 9.0 / 10.3 / 5.0; Total reported 9.0 / 10.3 / 5.0; FX 2.0 / 1.6 / 3.1; Organic
    7.0 / 8.7 / 1.9. Organic Intl 7.0 / 8.7 / 1.9 (l.246); U.S. rows n/a.
- T8 EPD 12M25, l.252-275: International and Total 5,536 / 4,167 / 1,369 (l.258-260). NEW
  l.266-271: International 6.6 / 8.0 / 2.5; Total reported 6.6 / 8.0 / 2.5; FX (0.8) / (1.5) /
  1.1; Organic 7.4 / 9.5 / 1.4. Organic Intl 7.4 / 9.5 / 1.4 (l.275).
- T9 Medical Devices 4Q25, l.281-300; columns Total / Rhythm Management / Electrophysiology /
  Heart Failure / Vascular / Structural Heart / Neuro-modulation / Diabetes Care (Amulet still in
  Structural Heart; no asterisk).
  - U.S. 2,605 / 340 / 340 / 283 / 287 / 304 / 208 / 843; International 3,070 / 365 / 390 / 92 /
    496 / 371 / 66 / 1,290; Total reported 5,675 / 705 / 730 / 375 / 783 / 675 / 274 / 2,133 (all
    l.285). % vs 4Q24: U.S. 10.7 / 12.8 / 13.1 / 11.7 / 6.5 / 4.8 / 1.9 / 14.9 (l.289). NEW
    l.291-296: International 13.7 / 13.4 / 13.9 / 17.9 / 8.9 / 16.3 / 23.8 / 14.2; Total reported
    12.3 / 13.1 / 13.5 / 13.2 / 8.0 / 10.8 / 6.5 / 14.5; FX 1.9 / 1.6 / 1.0 / 1.1 / 1.5 / 2.1 / 0.9
    / 2.8; Organic 10.4 / 11.5 / 12.5 / 12.1 / 6.5 / 8.7 / 5.6 / 11.7. Organic U.S. = reported U.S.
    (l.298); Intl 10.1 / 10.2 / 11.9 / 13.4 / 6.6 / 12.3 / 19.6 / 9.6 (l.300).
- T10 Medical Devices 12M25, l.308-327.
  - U.S. 9,968 / 1,334 / 1,283 / 1,107 / 1,118 / 1,172 / 773 / 3,181; International 11,419 /
    1,315 / 1,481 / 341 / 1,877 / 1,351 / 237 / 4,817; Total reported 21,387 / 2,649 / 2,764 /
    1,448 / 2,995 / 2,523 / 1,010 / 7,998 (all l.312). % vs 12M24: U.S. 13.4 / 15.7 / 12.4 / 12.2 /
    5.8 / 11.5 / 0.8 / 20.8 (l.316). NEW l.318-323: International 12.0 / 6.4 / 11.7 / 16.4 / 5.4 /
    13.0 / 21.5 / 15.4; Total reported 12.6 / 10.9 / 12.0 / 13.2 / 5.6 / 12.3 / 5.0 / 17.5; FX 0.7
    / 0.7 / 0.4 / 0.5 / 0.5 / 0.8 / 0.2 / 1.2; Organic 11.9 / 10.2 / 11.6 / 12.7 / 5.1 / 11.5 / 4.8
    / 16.3. Organic U.S. = reported U.S. (l.325); Intl 10.5 / 5.0 / 10.9 / 14.3 / 4.7 / 11.5 / 20.5
    / 13.5 (l.327).

### Statements, reconciliations and details (D07)

- T11 Statement of earnings, "Fourth Quarter Ended December 31, 2025 and 2024", l.381-420
  (page 9); columns 4Q25 / 4Q24 / % Change. NEW l.393-402: Net Sales $11,459 / $10,974 / 4.4;
  Cost of products sold, excluding amortization expense 4,922 / 4,942 / (0.4); Amortization of
  intangible assets 422 / 465 / (9.4); Research and development 735 / 749 / (1.9); Selling,
  general, and administrative 3,129 / 2,907 / 7.7; Total Operating Cost and Expenses 9,208 /
  9,063 / 1.6; Operating Earnings 2,251 / 1,911 / 17.8; Interest expense, net 42 / 45 / (8.0).
  Then Net foreign exchange (gain) loss (15) / (10) / n/m (l.404); Other (income) expense, net
  (134) / (154) / (13.0) (l.406); Earnings before taxes 2,358 / 2,030 / 16.1 (l.408); Taxes on
  earnings 582 / (7,199) / n/m, note 1) (l.410); Net Earnings $1,776 / $9,229 / n/m (l.412); NE
  excluding Specified Items $2,630 / $2,349 / 11.9, note 2) (l.414); Diluted EPS $1.01 / $5.27 /
  n/m (l.416); Diluted EPS excl. Specified Items $1.50 / $1.34 / 11.9 (l.418); Average shares
  1,747 / 1,746 (l.420). Notes l.422-428; footnotes 1)-2) l.432-438 (page 10).
- T12 Statement of earnings, "Twelve Months Ended December 31, 2025 and 2024", l.442-481 (page
  11); columns 12M25 / 12M24 / % Change. NEW l.454-463: Net Sales $44,328 / $41,950 / 5.7; Cost
  of products sold 19,319 / 18,706 / 3.3; Amortization 1,682 / 1,878 / (10.5); R&D 2,942 / 2,844
  / 3.5; SG&A 12,332 / 11,697 / 5.4; Total Operating Cost and Expenses 36,275 / 35,125 / 3.3;
  Operating Earnings 8,053 / 6,825 / 18.0; Interest expense, net 185 / 215 / (13.8). Then Net FX
  (50) / (27) / n/m (l.465); Other (income) expense, net (548) / (376) / 45.9 (l.467); EBT 8,466 /
  7,013 / 20.7 (l.469); Taxes 1,942 / (6,389) / n/m (l.471); NE $6,524 / $13,402 / n/m (l.473); NE
  excl. Specified $9,040 / $8,200 / 10.2 (l.475); Diluted EPS $3.72 / $7.64 / n/m (l.477); Diluted
  EPS excl. Specified $5.15 / $4.67 / 10.3 (l.479); shares 1,749 / 1,748 (l.481). Footnotes
  l.493-499 (page 12).
- T13 Non-GAAP Reconciliation of Financial Information, fourth quarter, l.503-549 (page 13);
  columns As Reported (GAAP) / Specified Items / As Adjusted.
  - 4Q25: Intangible Amortization $422 / $(422) / $— (l.517). NEW l.519-528: Gross Margin 6,115 /
    428 / 6,543; R&D 735 / (29) / 706; SG&A 3,129 / (254) / 2,875; Other (income) expense, net
    (134) / (17) / (151); Earnings before taxes 2,358 / 728 / 3,086; Taxes on Earnings 582 / (126)
    / 456; Net Earnings 1,776 / 854 / 2,630; Diluted EPS $1.01 / $0.49 / $1.50. Prose l.530:
    amortization $422m plus "other net expenses of $306 million" (restructuring, legal reserves,
    acquisitions); "See page 17".
  - 4Q24: 465 / (465) / — (l.536). NEW l.538-547: Gross Margin 5,567 / 673 / 6,240; R&D 749 /
    (59) / 690; SG&A 2,907 / (21) / 2,886; Other (income) expense, net (154) / 20 / (134); EBT
    2,030 / 733 / 2,763; Taxes (7,199) / 7,613 / 414; NE 9,229 / (6,880) / 2,349; EPS $5.27 /
    $(3.93) / $1.34. Prose l.549: $465m plus "other net expenses of $268 million" (restructuring
    actions, acquisitions and other); "See page 18".
- T14 Non-GAAP Reconciliation, twelve months, l.553-591 (page 14).
  - 12M25: 1,682 / (1,682) / — (l.559). NEW l.561-570: Gross Margin 23,327 / 1,824 / 25,151; R&D
    2,942 / (112) / 2,830; SG&A 12,332 / (312) / 12,020; Other (548) / (48) / (596); EBT 8,466 /
    2,296 / 10,762; Taxes 1,942 / (220) / 1,722; NE 6,524 / 2,516 / 9,040; EPS $3.72 / $1.43 /
    $5.15. Prose l.572: $1.682bn plus "$614 million" (incl. legal reserves, investment impairment
    charges); "See page 19".
  - 12M24: 1,878 / (1,878) / — (l.578). NEW l.580-589: Gross Margin 21,366 / 2,213 / 23,579; R&D
    2,844 / (140) / 2,704; SG&A 11,697 / (117) / 11,580; Other (376) / (163) / (539); EBT 7,013 /
    2,633 / 9,646; Taxes (6,389) / 7,835 / 1,446; NE 13,402 / (5,202) / 8,200; EPS $7.64 / $(2.97)
    / $4.67. Prose l.591: $1.878bn plus "$755 million" (intangible impairments, restructuring,
    acquisitions, a divestiture); "See page 19" (the 12M24 details table is on page 20, l.799-835).
- T15 Tax-rate reconciliations, l.595-669 (page 15); columns Pre-Tax Income / Taxes on Earnings /
  Tax Rate; rows As reported (GAAP) / Specified items / Excluding specified items.
  - 4Q25 (l.607-611): $2,358 / $582 / 24.7% [1)]; 728 / (126); $3,086 / $456 / 14.8%.
  - 4Q24 (l.623-627): $2,030 / $(7,199) / (354.6%) [2)]; 733 / 7,613; $2,763 / $414 / 15.0%.
  - 12M25 (l.645-649): $8,466 / $1,942 / 22.9% [3)]; 2,296 / (220); $10,762 / $1,722 / 16.0%.
  - 12M24 (l.661-665): $7,013 / $(6,389) / (91.1%) [4)]; 2,633 / 7,835; $9,646 / $1,446 / 15.0%.
  - Footnotes 1)-2) l.629-631, 3)-4) l.667-669 (same texts as statement footnotes l.432-434,
    493-495).
- T16 Non-GAAP Revenue Reconciliation, twelve months, l.673-687 (page 16); columns 12M25 Abbott
  Reported | 12M24 Abbott Reported / Impact from business exit (a) / Adjusted Revenue | % Change
  vs. 12M24: Reported / Adjusted / Organic. Rows (l.681-685): Total Company 44,328 | 41,950 / (13)
  / 41,937 | 5.7 / 5.7 / 5.5; U.S. 17,126 | 16,323 / (13) / 16,310 | 4.9 / 5.0 / 5.0; Intl 27,202
  | 25,627 / — / 25,627 | 6.1 / 6.1 / 5.9; Total Nutrition 8,451 | 8,413 / (13) / 8,400 | 0.4 /
  0.5 / 1.2; U.S. 3,606 | 3,689 / (13) / 3,676 | (2.3) / (1.9) / (1.9); Intl 4,845 | 4,724 / — /
  4,724 | 2.6 / 2.6 / 3.7; Adult Nutrition 4,477 | 4,390 / (13) / 4,377 | 2.0 / 2.3 / 3.0; U.S.
  1,448 | 1,481 / (13) / 1,468 | (2.2) / (1.4) / (1.4); Intl 3,029 | 2,909 / — / 2,909 | 4.1 / 4.1
  / 5.1. Footnote (a) ZonePerfect, "initiated in March 2024" (l.687). No 4Q revenue
  reconciliation in D07 (l.108 "Refer to page 16").
- T17-T20 Details of Specified Items; columns Acquisition or Divestiture-related (a) /
  Restructuring and Cost Reduction Initiatives (b) / Intangible Amortization / Other (c) / Total
  Specifieds; Taxes, Net Earnings and EPS lines print the Total column only.
  - T17 4Q25, l.691-719 (page 17). NEW l.697-703: Gross Margin $2 / $3 / $422 / $1 / $428; R&D —
    / (14) / — / (15) / (29); SG&A (38) / (51) / — / (165) / (254); Other (income) expense, net (8)
    / (3) / — / (6) / (17); EBT $48 / $71 / $422 / $187 / 728. Taxes (d) (126) (l.705); NE $854
    (l.707); EPS $0.49 (l.709). Footnotes a)-d) l.713-719: (c) "$165 million for legal reserves
    related to a certain agreed-upon settlement" + MDR/IVDR; (d) "recognition of a tax expense" +
    "approximately $150 million" deferred-tax adjustments.
  - T18 4Q24, l.723-757 (page 18). NEW l.735-741: Gross Margin — / $49 / $465 / $159 / $673; R&D
    (1) / (20) / — / (38) / (59); SG&A (5) / (22) / — / 6 / (21); Other (2) / — / — / 22 / 20;
    EBT $8 / $91 / $465 / $169 / 733. Taxes (d) 7,613 (l.743); NE $(6,880) (l.745); EPS $(3.93)
    (l.747). Footnotes l.751-757: (c) MDR/IVDR + "intangible asset impairment charges"; (d) "net
    tax benefit ... including non-cash valuation allowance adjustments".
  - T19 12M25, l.761-795 (page 19). NEW l.773-779: Gross Margin $3 / $128 / $1,682 / $11 /
    $1,824; R&D (1) / (56) / — / (55) / (112); SG&A (53) / (100) / — / (159) / (312); Other (26) /
    (3) / — / (19) / (48); EBT $83 / $287 / $1,682 / $244 / 2,296. Taxes (d) (220) (l.781); NE
    $2,516 (l.783); EPS $1.43 (l.785). Footnotes l.789-795: (c) same $165m legal reserves +
    "charges for investment impairments"; (d) "recognition of a tax benefit" + "$610 million".
  - T20 12M24, l.799-833 (page 20). NEW l.811-817: Gross Margin $2 / $125 / $1,878 / $208 /
    $2,213; R&D (5) / (21) / — / (114) / (140); SG&A (37) / (39) / — / (41) / (117); Other (155) /
    — / — / (8) / (163); EBT $199 / $185 / $1,878 / $371 / 2,633. Taxes (d) 7,835 (l.819); NE
    $(5,202) (l.821); EPS $(2.97) (l.823). Footnotes l.827-833: (a) "Includes the loss on the sale
    of a non-core business"; (c) "investment and intangible asset impairments".
- Arithmetic checks (all hold): segment sub-columns sum to segment totals; statement Total
  Operating Cost = COGS + amortization + R&D + SG&A; Operating Earnings - interest - net FX - other
  = EBT; recon Gross Margin = Net Sales - COGS - amortization (6,115; 5,567; 23,327; 21,366);
  specified-item columns sum to row totals; Adjusted = GAAP + Specified in every recon row.

### Flags (D07)

- Comparative columns 4Q24/12M24 repeat D01 (see Shared ground S1). D07 adds 4Q24/12M24 rows that
  doc-map.md's D01 section records as clipped (statement top rows, recon rows, details rows).
- Internal wording: 4Q24 recon prose l.549 lists "restructuring actions, acquisitions and other
  net expenses" (no impairments) while l.438 (2024 statement footnote) and l.755 (4Q24 (c)) name
  intangible impairments. Restructuring footnote (b) for 2025 periods (l.715, 791) lacks "and cost
  reduction initiatives"; 2024 periods (l.753, 829) keep it. 4Q25 (d) "tax expense" (l.719) vs
  12M25 (d) "tax benefit" (l.795), matching statement footnotes l.432 ($20m expense) and l.493
  ($70m benefit).
- 12M25 Other (c) SG&A (159) (l.777) is smaller in size than 4Q25 Other (c) SG&A (165) (l.701);
  both (c) footnotes cite the same $165m legal reserve (l.717, 793).
- Page cross-reference l.591 "See page 19" for 12M24 details, which print on page 20.
- Printed % vs ratio of printed millions: NE excl. Specified 4Q25 growth 11.9 (l.414) vs 2,630 /
  2,349 = +11.96%; adjusted EPS 11.9 (l.418) matches 1.50/1.34. Nutrition 12M25 reported 0.4
  (l.95, 158, 683) vs 8,451/8,413 = +0.45%; adjusted 0.5 (l.683) vs 8,451/8,400 = +0.61%. EBT 4Q25
  16.1 (l.408) vs 2,358/2,030 = +16.16%.
- Rounded prose: adjusted EPS "growth of 12 percent" (l.17, 23) vs 11.9 (l.418); "growth of 10
  percent" (l.17, 27) vs 10.3 (l.479); FY sales "$44.3 billion" (l.25) vs 44,328 (l.86, 456) and
  "$44.328 billion" (l.377); 2026 EPS guidance "$5.55 to $5.80 ... 10 percent growth at the
  midpoint" (l.17, 31; midpoint $5.675 / $5.15 = +10.2%); CGM "$2.0 billion" (l.306) vs Diabetes
  Care 2,133 (l.285; CGM is not a table row). Prose growth figures in l.21, 25, 139, 192, 196, 248,
  250, 302 equal the table values.
- MD leader sentence l.304 ("double-digit growth in Electrophysiology, Heart Failure, Diabetes
  Care, and Rhythm Management"): organic 12.5 / 12.1 / 11.7 / 11.5; Structural Heart organic 8.7
  but reported 10.8 (l.294-296). The sentence does not state its basis.
- Segment columns of T1/T2 do not sum to Total Company: U.S. 806+967+2,605 = 4,378 vs 4,383 (4Q25);
  3,606+3,535+9,968 = 17,109 vs 17,126 (12M25); International columns sum exactly. No "Other"
  column printed.
- No margin percentages printed anywhere in D07; see Shared ground S5 for the rows that hold the
  components.

### Layout (D07)

- NEW rows render as Markdown tables with an empty header row ("|  |  | ...") and a "| --- |"
  separator; the label is the first cell. Rows after each Markdown block are tab-separated.
- Several rows share one line: l.80 (Intl organic row + "Full-Year 2025 Results (12M25)"), l.86
  (Intl + Total reported), l.108 (Intl organic + "Refer to page 16 ..."), l.139 (Intl organic +
  prose), l.149, 231 (Intl + Total), l.165 (Intl organic + "*" footnote), l.175, 285, 312 (U.S.,
  Intl and Total on one line), l.219 (U.S. and Intl organic rows), l.553 (page title run-on),
  l.681-685 (Total/U.S./Intl recon rows run together).
- Footnote markers inside rows: "Impact of COVID-19 testing sales 1" (l.72) and "... 2" (l.100)
  carry marker digits before the values; "n/m\t1)" (l.410, 471), trailing "2)" (l.414, 418, 475,
  479); "sales1." / "sales2." in bullets (l.21, 25).
- Tax tables split their header over four lines ("Pre-Tax" / "Income Taxes on" / "Earnings Tax" /
  "Rate") and put "%" in a separate cell ("24.7\t%", "(354.6\t%)").
- l.737 "| Gross Margin $ | — | $ 49 | ...": the "$" sits in the label cell and the Acquisition
  cell is "—" (column sums confirm: 0+49+465+159 = 673). "Intangible Amortization\t$\t422 $\t(422)
  $\t—" style rows (l.517, 536, 559, 578) split "$" into separate cells.
- No U+FFFD or other stray symbols (non-ASCII = em/en dash, bullet, (R) only).

### Prose anchors (current lines, D07)

- Headline l.15; sub-bullets l.17; dateline l.19; bullets l.21-39 (Exact Sciences l.33; Volt l.37;
  TactiFlex Duo l.39); Ford l.41; organic definition l.47; FX method note l.49; Nutrition prose
  l.139-141; Diagnostics l.192-196 (COVID $89m vs $176m l.194; China VBP l.196); EPD l.248-250; MD
  l.302-306; guidance l.331-337 (FY2026 organic l.333; FY EPS and 1Q26 range l.335); dividend
  l.339-343; employees l.347; call l.351; forward-looking caution l.359; contacts l.361-373;
  footnotes 1-2 l.375-377; statement footnotes l.432-438, 493-499.

<!-- END C2 D07 -->

<!-- C2: D08 -->
## D08 - Abbott Q1 2026 release (April 16, 2026; 1Q26 only, no year-to-date tables)

### Ledger and spot-checks

- Read in order, every line: l.1-110, 109-218, 218-327, 327-436, 436-530 (530 = trailing empty
  line). Unread: none.
- NEW ranges (all read): 65-70, 92-97, 167-172, 196-201 (sales growth rows); 281-290 (statement
  top rows); 346-355, 365-374 (non-GAAP reconciliation rows); 467-473, 505-511 (specified details
  body rows). Capture artifact: code fence "```text" l.426 and "```" l.429 around part of the
  revenue-reconciliation column header (one blank line inside the old header was dropped); not
  content.
- Printed pages "Page 1 of 15" (l.41) ... "Page 15 of 15" (l.529). Charts: not applicable.
- Spot-checks vs docs/abt_ex991_2026-04-16.txt (527 lines): "| Gross Margin | 5,852 | 432 | 6,284
  |" docs l.346 = text l.348; Structural Heart recon row with the extra "—" docs l.441 = text
  l.443; code fence docs l.424/427 = text l.426/429 (present in docs too); footnote "(b) Reflects
  the impact of compensation payments ..." docs l.451 = text l.453. No gap markers. Visual page:
  unresolved.

### Sales tables (D08)

- T1 Total company 1Q26, l.51-74, "Sales 1Q26 ($ in millions)"; columns Total Company /
  Nutrition / Diagnostics / Established Pharmaceuticals / Medical Devices.
  - U.S. 4,274 / 844 / 905 / — / 2,523 (l.55); International 6,890 / 1,173 / 1,275 / 1,426 /
    3,016 (l.57); Total reported 11,164 / 2,017 / 2,180 / 1,426 / 5,539 (l.59).
  - "% Change vs. 1Q25" (l.61): U.S. 2.5 / (11.6) / 3.8 / n/a / 7.9 (l.63). NEW l.65-70:
    International 11.3 / (1.5) / 7.8 / 13.2 / 18.0; Total reported 7.8 / (6.0) / 6.1 / 13.2 / 13.2;
    "Total reported excl. foreign exchange impact" 3.8 / (7.7) / 2.5 / 9.0 / 8.1; "Comparable sales
    growth" 3.7 / (7.7) / 1.8 / 9.0 / 8.5. Comparable U.S. 2.5 / (11.6) / 2.0 / n/a / 8.7 and Intl
    4.6 / (4.7) / 1.6 / 9.0 / 8.3 (both l.72). "Refer to page 13" (l.74).
- T2 Nutrition 1Q26, l.80-101; Total / Pediatric / Adult. U.S. 844 / 511 / 333 (l.84);
  International 1,173 / 442 / 731 and Total reported 2,017 / 953 / 1,064 (l.86). % vs 1Q25: U.S.
  (11.6) / (13.0) / (9.2) (l.90). NEW l.92-97: International (1.5) / (2.6) / (0.9); Total reported
  (6.0) / (8.5) / (3.6); excl. FX (7.7) / (9.7) / (5.9); Comparable (7.7) / (9.7) / (5.9).
  Comparable U.S. (11.6) / (13.0) / (9.2) (l.99); Intl (4.7) / (5.3) / (4.3) (l.101).
- T3 Diagnostics*, 1Q26, l.109-139 (complete in both captures; tab rows, no Markdown); columns
  Total / Core Laboratory / Cancer Diagnostics / Rapid/Molecular Diagnostics. U.S. 905 / 347 / 93
  / 465; International 1,275 / 925 / 3 / 347; Total reported 2,180 / 1,272 / 96 / 812 (l.115-119).
  % vs 1Q25: U.S. 3.8 / 4.5 / n/a / (13.8); International 7.8 / 9.5 / n/a / 2.8; Total reported
  6.1 / 8.1 / n/a / (7.4); excl. FX 2.5 / 3.3 / n/a / (9.6); Comparable 1.8 / 3.3 / 13.4 / (9.6)
  (l.123-131); comparable U.S. 2.0 / 4.5 / 13.2 / (13.8) (l.133); Intl 1.6 / 2.8 / 19.2 / (2.7)
  (l.135). Footnote * l.137 (regrouping "Beginning in 2026"; Exact Sciences sales presented as
  Cancer Diagnostics after the March 23, 2026 acquisition).
- T4 EPD 1Q26, l.153-176; Total / Key Emerging Markets / Other. International and Total reported
  1,426 / 1,089 / 337 (l.159-161). NEW l.167-172: International 13.2 / 12.9 / 14.1; Total reported
  13.2 / 12.9 / 14.1; excl. FX 9.0 / 9.4 / 7.9; Comparable 9.0 / 9.4 / 7.9. Comparable Intl 9.0 /
  9.4 / 7.9 (l.176); U.S. rows n/a.
- T5 Medical Devices 1Q26, l.186-209; Total / Rhythm Management / Electrophysiology* / Heart
  Failure / Vascular / Structural Heart* / Neuromodulation / Diabetes Care.
  - U.S. 2,523 / 339 / 378 / 292 / 291 / 224 / 177 / 822; International 3,016 / 345 / 410 / 97 /
    486 / 354 / 66 / 1,258; Total reported 5,539 / 684 / 788 / 389 / 777 / 578 / 243 / 2,080 (all
    l.190). % vs 1Q25: U.S. 7.9 / 11.5 / 13.7 / 11.4 / 8.6 / (9.5) / 0.7 / 9.8 (l.194).
  - NEW l.196-201: International 18.0 / 22.9 / 19.6 / 25.2 / 10.0 / 25.2 / 27.2 / 16.6; Total
    reported 13.2 / 17.0 / 16.7 / 14.6 / 9.5 / 9.0 / 6.8 / 13.8; excl. FX 8.1 / 12.5 / 12.5 / 12.2
    / 4.9 / 3.6 / 4.1 / 7.4; Comparable 8.5 / 12.5 / 12.5 / 12.2 / 4.9 / 6.8 / 4.1 / 7.4.
    Comparable U.S. 8.7 / 11.5 / 13.7 / 11.4 / 8.6 / (3.6) / 0.7 / 9.8 (l.203); Intl 8.3 / 13.5 /
    11.2 / 14.9 / 2.7 / 15.0 / 15.5 / 5.7 (l.205). Footnote * l.207 (Amulet transfer "on Jan. 1,
    2026"; "$46 million of sales in the first quarter of 2025 were moved").

### Statements, reconciliations and details (D08)

- T6 Statement of earnings, "First Quarter Ended March 31, 2026 and 2025", l.269-308 (page 9);
  columns 1Q26 / 1Q25 / % Change. NEW l.281-290: Net Sales $11,164 / $10,358 / 7.8; Cost of
  products sold 4,890 / 4,468 / 9.5; Amortization 422 / 420 / 0.3; R&D 767 / 716 / 7.2; SG&A 3,740
  / 3,061 / 22.2; Total Operating Cost and Expenses 9,819 / 8,665 / 13.3; Operating Earnings 1,345
  / 1,693 / (20.6); Interest expense, net 68 / 49 / 37.4. Then Net FX (13) / (7) / n/m (l.292);
  Other (income) expense, net (159) / (127) / 24.8 (l.294); EBT 1,449 / 1,778 / (18.5) (l.296);
  Taxes on Earnings 372 / 453 / (18.0) [1)] (l.298); NE $1,077 / $1,325 / (18.7) (l.300); NE excl.
  Specified $2,022 / $1,919 / 5.4 [2)] (l.302); Diluted EPS $0.61 / $0.76 / n/m (l.304); Diluted
  EPS excl. Specified $1.15 / $1.09 / 5.5 [2)] (l.306); shares 1,747 / 1,747 (l.308). Footnotes
  l.320-326 (page 10).
- T7 Non-GAAP Reconciliation, l.330-376 (page 11); As Reported (GAAP) / Specified Items / As
  Adjusted.
  - 1Q26: 422 / (422) / — (l.344). NEW l.346-355: Gross Margin 5,852 / 432 / 6,284; R&D 767 /
    (24) / 743; SG&A 3,740 / (473) / 3,267; Other (159) / (7) / (166); EBT 1,449 / 936 / 2,385;
    Taxes 372 / (9) / 363; NE 1,077 / 945 / 2,022; EPS $0.61 / $0.54 / $1.15. Prose l.357: $422m
    plus "other net expenses of $514 million"; "See page 14".
  - 1Q25: 420 / (420) / — (l.363). NEW l.365-374: Gross Margin 5,470 / 448 / 5,918; R&D 716 /
    (27) / 689; SG&A 3,061 / (10) / 3,051; Other (127) / (35) / (162); EBT 1,778 / 520 / 2,298;
    Taxes 453 / (74) / 379; NE 1,325 / 594 / 1,919; EPS $0.76 / $0.33 / $1.09. Prose l.376: $420m
    plus "$100 million" (restructuring, acquisitions, investment impairments); "See page 15".
- T8 Tax-rate reconciliations, l.380-416 (page 12): 1Q26 (l.392-396) $1,449 / $372 / 25.6% [1)];
  936 / (9); $2,385 / $363 / 15.2%. 1Q25 (l.408-412) $1,778 / $453 / 25.5% [2)]; 520 / (74);
  $2,298 / $379 / 16.5%. Footnotes l.414-416.
- T9 Non-GAAP Revenue Reconciliation, l.420-453 (page 13). Columns (header l.424-431): 1Q26 Abbott
  Reported / Impact of acquisition (a) / Impact of multi-year agreement (b) / Foreign exchange /
  Comparable Revenue | 1Q25 Abbott Reported / Impact of acquisition (a) / Impact of multi-year
  agreement (b) / Comparable Revenue | % Change vs. 1Q25: Reported / Comparable.
  - Total Company 11,164 / 706 / (8) / (414) / 11,448 | 10,358 / 707 / (24) / 11,041 | 7.8 / 3.7;
    U.S. 4,274 / 681 / (8) / — / 4,947 | 4,168 / 684 / (24) / 4,828 | 2.5 / 2.5; Intl 6,890 / 25 /
    — / (414) / 6,501 | 6,190 / 23 / — / 6,213 | 11.3 / 4.6 (l.433).
  - Total Diagnostics 2,180 / 706 / — / (76) / 2,810 | 2,054 / 707 / — / 2,761 | 6.1 / 1.8; U.S.
    905 / 681 / — / — / 1,586 | 871 / 684 / — / 1,555 | 3.8 / 2.0; Intl 1,275 / 25 / — / (76) /
    1,224 | 1,183 / 23 / — / 1,206 | 7.8 / 1.6 (l.435).
  - Total Cancer Diagnostics 96 / 706 / — / (1) / 801 | — / 707 / — / 707 | n/a / 13.4; U.S. 93 /
    681 / — / — / 774 | — / 684 / — / 684 | n/a / 13.2 (l.437); Intl 3 / 25 / — / (1) / 27 | — / 23
    / — / 23 | n/a / 19.2 (l.439).
  - Total Medical Devices 5,539 / — / (8) / (249) / 5,282 | 4,895 / — / (24) / 4,871 | 13.2 / 8.5;
    U.S. 2,523 / — / (8) / — / 2,515 | 2,339 / — / (24) / 2,315 | 7.9 / 8.7; Intl 3,016 / — / — /
    (249) / 2,767 | 2,556 / — / — / 2,556 | 18.0 / 8.3 (l.441).
  - Total Structural Heart* 578 / — / (8) / (29) / 541 | 531 / — / (24) / 507 | 9.0 / 6.8; U.S.
    224 / — / (8) / — / 216 | 248 / — / (24) / 224 | (9.5) / (3.6); Intl 354 / — / — / (29) / 325
    | 283 / — / — / 283 | 25.2 / 15.0 (l.443; see Layout for the extra "—").
  - Footnotes: * l.445-447 ($46m of 1Q25 sales moved); (a) l.449-451 "The adjustment includes
    historical sales for Exact Sciences prior to the acquisition date"; (b) l.453 compensation
    payments under a multi-year agreement with a competitor, "final payment ... recognized in the
    first quarter of 2026". The multi-year amounts are U.S.-only ((8), (24)).
- T10 Details of Specified Items 1Q26, l.457-489 (page 14). NEW l.467-473: Gross Margin $2 / $7 /
  $422 / $1 / $432; R&D (1) / (10) / — / (13) / (24); SG&A (444) / (33) / — / 4 / (473); Other (2)
  / (2) / — / (3) / (7); EBT $449 / $52 / $422 / $13 / 936. Taxes (d) (9) (l.475); NE $945
  (l.477); EPS $0.54 (l.479). Footnotes l.481-489: (a) "stock-based compensation recognized as
  expense from equity awards accelerated in connection with the Exact Sciences acquisition",
  integration and other acquisition costs; (b) "specific restructuring plans" (no "cost reduction
  initiatives"); (c) MDR/IVDR only (no legal reserve, no impairments); (d) "tax benefit" +
  "approximately $200 million".
- T11 Details of Specified Items 1Q25, l.493-527 (page 15). NEW l.505-511: Gross Margin — / $26 /
  $420 / $2 / $448; R&D (1) / (16) / — / (10) / (27); SG&A (3) / (7) / — / — / (10); Other (24) /
  — / — / (11) / (35); EBT $28 / $49 / $420 / $23 / 520. Taxes (d) (74) (l.513); NE $594 (l.515);
  EPS $0.33 (l.517). Footnotes l.519-527: (a) integration costs "as well as a fair value adjustment
  to contingent consideration related to a business acquisition"; (b) "and cost reduction
  initiatives"; (c) MDR/IVDR "and investment impairment charges"; (d) "2025 ... approximately $200
  million".
- Arithmetic checks (all hold): sub-columns sum to segment totals; statement and recon identities
  as in D07; recon rows: Reported + adjustments = Comparable in every row; specified columns sum.

### Flags (D08)

- 1Q25 comparative columns repeat D02 values recorded in doc-map.md (Shared ground S1), except the
  recast Structural Heart (531 vs 577) and the new grouping of Diagnostics sub-businesses.
- 1Q25 specified items: statement footnote l.326 says "net after-tax benefits of $594 million, or
  $0.33 per share"; D08's own recon (l.373) adds 594 to GAAP NE 1,325 to reach 1,919, the same
  direction as the 1Q26 "charges" (l.324, 354); doc-map.md D02 section records D02 calling it
  "net after-tax charges". Neither release states precedence.
- Printed % vs ratio of printed millions (one-decimal differences): Cancer Diagnostics comparable
  13.4 (l.131, 437) vs 801/707 = +13.30%; MD comparable 8.5 (l.70, 201, 441) vs 5,282/4,871 =
  +8.44%; MD U.S. comparable 8.7 vs 2,515/2,315 = +8.64%; Structural Heart reported 9.0 vs 578/531
  = +8.85% and comparable 6.8 vs 541/507 = +6.71%; Dx Intl comparable 1.6 vs 1,224/1,206 = +1.49%;
  Interest expense 37.4 (l.290) vs 68/49 = +38.8%; GAAP tax rate 25.6% (l.392) vs 372/1,449 =
  25.67%. Total company comparable 3.7 and Dx 1.8 match.
- Rounded prose: adjusted EPS "growth of 6 percent" (l.17, 25) vs 5.5 (l.306); NE excl. Specified
  +5.4 (l.302). CGM growth 14.2% reported / 7.6% comparable (l.215) has no table row or dollar
  figure. Other prose growth figures (l.23, 103, 141, 178, 180, 211) equal the table values.
- MD leader sentence l.213 ("double-digit growth in Electrophysiology, Heart Failure and Rhythm
  Management"): comparable 12.5 / 12.2 / 12.5; Diabetes Care reported 13.8 but comparable 7.4;
  Structural Heart reported 9.0. The sentence does not state its basis.
- Dx comparable U.S. 2.0 vs reported U.S. 3.8: the comparable base adds Exact Sciences
  pre-acquisition sales to both years (681 / 684, l.435). MD comparable 8.5 exceeds MD excl. FX
  8.1 because the multi-year payments ((8) vs (24)) are excluded in both years.
- 1Q26 Exact Sciences pre-acquisition sales 706 (l.433; "prior to the acquisition date", l.451)
  plus reported Cancer Diagnostics 96 (post-acquisition sales, l.137; acquisition March 23, quarter
  ended March 31) = 802; comparable 801 after FX (1).
- Segment columns of T1 do not sum to Total Company: U.S. 844+905+2,523 = 4,272 vs 4,274; total
  11,162 vs 11,164; International sums exactly.
- Restated 1Q25 Electrophysiology dollars are not printed (only 2026 dollars and growth rates).
  1Q25 totals for Diagnostics (2,054; U.S. 871; Intl 1,183) and MD (4,895; U.S. 2,339; Intl 2,556)
  are printed only in T9.
- Footnote marker "1" on the FY2026 comparable guidance (l.17 "7.5%1", l.29) points to footnote 1
  (l.265): 2025 totals $44.328bn (U.S. $17.126bn, Intl $27.202bn), Structural Heart "$89 million
  of compensation payments" in 2025, Exact Sciences 2025 sales "$3.247 billion" (U.S. $3.145bn,
  international $102m).

### Layout (D08)

- NEW Markdown blocks as in D07. Rows sharing one line: l.72 (comparable U.S. and Intl rows), l.86
  (Intl + Total), l.190 (U.S., Intl, Total), l.433-443 (Total/U.S./Intl recon rows per line; l.437
  holds Cancer Dx Total and U.S., l.439 Intl).
- l.426-431: the recon header is split across the code fence. "Impact" ends l.427 and continues
  as "of multi-year agreement (b)" at the start of l.428; "Impact" ends l.428 again and continues
  at the start of l.431 (after the closing fence l.429).
- l.443 Structural Heart rows carry an extra "—" before each 1Q25 reported figure ("541 — 531 —
  (24) 507"; "216 — 248 — (24) 224"; "325 — 283 — — 283"); the arithmetic (531 - 24 = 507; 248 -
  24 = 224) places 531 / 248 / 283 in the 1Q25 Abbott Reported column. Cancer Dx (l.437) and the
  D10 Structural Heart rows have no extra token.
- l.507 "| Gross Margin $ | — | $ 26 | ...": "$" in the label cell, Acquisition cell "—" (sum
  0+26+420+2 = 448).
- Footnote markers on their own lines: "*" l.445, "(a)" l.449; "(b)" l.453 shares its line.
- Footnote marker "1" fused to "7.5%" (l.17 "7.5%1", l.29 "7.5%1.").
- No U+FFFD; curly apostrophe "Abbott’s" in footnote 1 (l.265) only.

### Prose anchors (current lines, D08)

- Headline l.15; sub-bullets l.17-19; dateline l.21; bullets l.23-37 (Exact closing l.27; FY
  comparable guidance l.29; FY EPS guidance with "$0.20 of dilution" l.31; AtaCor l.33; VERITAS
  l.35; FreeDM2 l.37); Ford l.39; comparable definition l.45-47; FX note l.49; Nutrition prose
  l.103-105; Diagnostics l.141-147; EPD l.178-180; MD l.211-215; guidance l.219-227 (2Q26 range
  l.225); dividend l.229-233; employees l.237; call l.241; forward-looking caution l.249 (10-K for
  year ended Dec. 31, 2025); contacts l.251-263; footnote 1 l.265; statement footnotes l.320-326;
  tax footnotes l.414-416.

<!-- END C2 D08 -->

<!-- C2: D10 -->
## D10 - Abbott Q2 2026 release (July 16, 2026; 2Q26 and first half 1H26)

### Ledger and spot-checks

- Read in order, every line: l.1-100, 100-199, 199-308, 308-407, 407-516, 516-625, 625-714,
  714-803, 803-879 (879 = trailing empty line). Unread: none.
- NEW ranges (all read): 67-72, 88-93, 115-120, 142-147, 223-228, 252-257, 277-282, 308-313
  (sales growth rows); 387-395, 449-457 (statement top rows through Operating Earnings); 499-508,
  518-527, 543-552, 564-573 (non-GAAP reconciliation rows); 740-746, 778-784, 816-822, 854-860
  (specified details body rows). Capture artifact: code fence "```text" l.699 and "```" l.702
  around part of the 1H revenue-reconciliation header; not content.
- Printed pages "Page 1 of 21" (l.43) ... "Page 21 of 21" (l.878). Charts: not applicable.
- Spot-checks vs docs/abt_ex991_2026-07-16.txt (876 lines): "| Gross Margin | 6,610 | 697 | 7,307
  |" docs l.499 = text l.501; footnote "c)Other includes $385 million ..." docs l.758 / 834 = text
  l.760 / 836; merged 1H statement row docs l.457 = text l.459; code fence docs l.697/700 = text
  l.699/702. No gap markers. Visual page: unresolved.

### Sales tables (D10)

- T1 Total company 2Q26, l.53-76; columns Total Company / Nutrition / Diagnostics / Established
  Pharmaceuticals / Medical Devices.
  - U.S. 5,216 / 871 / 1,660 / — / 2,680 (l.57); International 7,377 / 1,273 / 1,432 / 1,499 /
    3,173 (l.59); Total reported 12,593 / 2,144 / 3,092 / 1,499 / 5,853 (l.61).
  - % vs 2Q25: U.S. 22.0 / (9.0) / 104.8 / n/a / 7.0 (l.65). NEW l.67-72: International 7.5 / 1.4
    / 5.1 / 8.4 / 10.7; Total reported 13.0 / (3.1) / 42.3 / 8.4 / 9.0; excl. FX 12.2 / (3.6) /
    41.3 / 8.7 / 7.9; Comparable 4.8 / (3.6) / 2.9 / 8.7 / 8.4. Comparable U.S. 3.5 / (9.0) / 4.0
    / n/a / 8.0 (l.74); Intl 5.8 / 0.6 / 1.6 / 8.7 / 8.7 (l.76).
- T2 Total company 1H26, l.78-97. U.S. 9,490 / 1,715 / 2,565 / — / 5,203; International 14,267 /
  2,446 / 2,707 / 2,925 / 6,189; Total reported 23,757 / 4,161 / 5,272 / 2,925 / 11,392 (all
  l.82). % vs 1H25: U.S. 12.4 / (10.3) / 52.5 / n/a / 7.4 (l.86). NEW l.88-93: International 9.3
  / — / 6.4 / 10.7 / 14.2; Total reported 10.5 / (4.5) / 24.7 / 10.7 / 11.0; excl. FX 8.2 / (5.6)
  / 22.4 / 8.9 / 8.0; Comparable 4.3 / (5.6) / 2.4 / 8.9 / 8.4. Comparable U.S. 3.0 / (10.3) / 3.0
  / n/a / 8.3 and Intl 5.3 / (1.9) / 1.6 / 8.9 / 8.5 (both l.95). "Refer to pages 16 and 17"
  (l.97).
- T3 Nutrition 2Q26, l.103-124; Total / Pediatric / Adult. U.S. 871 / 525 / 346 (l.107);
  International 1,273 / 500 / 773 and Total 2,144 / 1,025 / 1,119 (l.109). % vs 2Q25: U.S. (9.0)
  / (10.7) / (6.4) (l.113). NEW l.115-120: International 1.4 / 7.3 / (2.0); Total reported (3.1) /
  (2.7) / (3.4); excl. FX (3.6) / (3.1) / (4.0); Comparable (3.6) / (3.1) / (4.0). Comparable
  U.S. (9.0) / (10.7) / (6.4) (l.122); Intl 0.6 / 6.4 / (2.8) (l.124).
- T4 Nutrition 1H26, l.130-151. U.S. 1,715 / 1,036 / 679 (l.134); International 2,446 / 942 /
  1,504 and Total 4,161 / 1,978 / 2,183 (l.136). % vs 1H25: U.S. (10.3) / (11.9) / (7.8) (l.140).
  NEW l.142-147: International — / 2.4 / (1.5); Total reported (4.5) / (5.6) / (3.5); excl. FX
  (5.6) / (6.4) / (4.9); Comparable (5.6) / (6.4) / (4.9). Comparable U.S. (10.3) / (11.9) / (7.8)
  (l.149); Intl (1.9) / 0.7 / (3.5) (l.151).
- T5 Diagnostics* 2Q26, l.155-175 (complete in both captures); Total / Core Laboratory / Cancer
  Diagnostics / Rapid/Molecular Diagnostics. U.S. 1,660 / 377 / 890 / 393 (l.161); International
  1,432 / 1,041 / 29 / 362 and Total 3,092 / 1,418 / 919 / 755 (l.163). % vs 2Q25: U.S. 104.8 /
  7.5 / n/a / (14.5) (l.167); International 5.1 / 3.4 / n/a / 2.0, Total reported 42.3 / 4.4 / n/a
  / (7.3) and excl. FX 41.3 / 3.2 / n/a / (8.0) (all l.169); Comparable 2.9 / 3.2 / 13.3 / (8.0)
  (l.171); comparable U.S. 4.0 / 7.5 / 13.3 / (14.5) (l.173); Intl 1.6 / 1.7 / 13.8 / 0.5 (l.175).
- T6 Diagnostics 1H26, l.185-205. U.S. 2,565 / 724 / 983 / 858 (l.189); International 2,707 /
  1,966 / 32 / 709 and Total 5,272 / 2,690 / 1,015 / 1,567 (l.191). % vs 1H25: U.S. 52.5 / 6.0 /
  n/a / (14.1) (l.195); International 6.4 / 6.1 / n/a / 2.4, Total reported 24.7 / 6.1 / n/a /
  (7.4), excl. FX 22.4 / 3.2 / n/a / (8.8) (all l.197); Comparable 2.4 / 3.2 / 13.3 / (8.8)
  (l.199); comparable U.S. 3.0 / 6.0 / 13.2 / (14.1) (l.201); Intl 1.6 / 2.2 / 16.5 / (1.1)
  (l.203). Footnote * l.203 (same text as D08 l.137).
- T7 EPD 2Q26, l.211-232: International and Total 1,499 / 1,164 / 335 (l.217). NEW l.223-228:
  International 8.4 / 9.8 / 3.7; Total reported 8.4 / 9.8 / 3.7; excl. FX 8.7 / 10.7 / 2.1;
  Comparable 8.7 / 10.7 / 2.1. Comparable Intl 8.7 / 10.7 / 2.1 (l.232).
- T8 EPD 1H26, l.238-261: International and Total 2,925 / 2,253 / 672 (l.244-246). NEW l.252-257:
  International 10.7 / 11.3 / 8.6; Total reported 10.7 / 11.3 / 8.6; excl. FX 8.9 / 10.1 / 4.9;
  Comparable 8.9 / 10.1 / 4.9. Comparable Intl 8.9 / 10.1 / 4.9 (l.261).
- T9 Medical Devices 2Q26, l.267-292; Total / Rhythm Management / Electro-physiology* / Heart
  Failure / Vascular / Structural Heart* / Neuro-modulation / Diabetes Care.
  - U.S. 2,680 / 377 / 420 / 313 / 294 / 225 / 189 / 862; International 3,173 / 366 / 441 / 88 /
    509 / 372 / 71 / 1,326; Total reported 5,853 / 743 / 861 / 401 / 803 / 597 / 260 / 2,188 (all
    l.271). % vs 2Q25: U.S. 7.0 / 10.7 / 15.9 / 10.9 / 3.9 / (9.8) / (2.1) / 8.6 (l.275).
  - NEW l.277-282: International 10.7 / 10.0 / 12.3 / 3.0 / 7.5 / 12.1 / 14.7 / 11.7; Total
    reported 9.0 / 10.4 / 14.0 / 9.0 / 6.1 / 2.7 / 2.0 / 10.5; excl. FX 7.9 / 9.5 / 13.4 / 8.7 /
    5.1 / 1.7 / 1.2 / 9.0; Comparable 8.4 / 9.5 / 13.4 / 8.7 / 5.1 / 5.7 / 1.2 / 9.0. Comparable
    U.S. 8.0 / 10.7 / 15.9 / 10.9 / 3.9 / (0.9) / (2.1) / 8.6 (l.284); Intl 8.7 / 8.3 / 11.1 / 1.3
    / 5.8 / 10.2 / 11.3 / 9.2 (l.286).
- T10 Medical Devices 1H26, l.294-321.
  - U.S. 5,203 / 716 / 798 / 605 / 585 / 449 / 366 / 1,684 (l.298); International 6,189 / 711 /
    851 / 185 / 995 / 726 / 137 / 2,584 (l.300); Total reported 11,392 / 1,427 / 1,649 / 790 /
    1,580 / 1,175 / 503 / 4,268 (l.302). % vs 1H25: U.S. 7.4 / 11.1 / 14.8 / 11.1 / 6.2 / (9.6) /
    (0.7) / 9.2 (l.306).
  - NEW l.308-313: International 14.2 / 15.9 / 15.7 / 13.5 / 8.7 / 18.1 / 20.4 / 14.0; Total
    reported 11.0 / 13.4 / 15.3 / 11.7 / 7.7 / 5.7 / 4.3 / 12.1; excl. FX 8.0 / 10.9 / 13.0 / 10.4
    / 5.0 / 2.6 / 2.6 / 8.2; Comparable 8.4 / 10.9 / 13.0 / 10.4 / 5.0 / 6.2 / 2.6 / 8.2.
    Comparable U.S. 8.3 / 11.1 / 14.8 / 11.1 / 6.2 / (2.2) / (0.7) / 9.2 (l.315); Intl 8.5 / 10.7 /
    11.2 / 7.8 / 4.3 / 12.4 / 13.2 / 7.5 (l.317).
  - Footnote * l.319: Amulet transferred "on January 1, 2026"; "$55 million of sales in the second
    quarter of 2025 and $101 million of sales in the first half of 2025 were moved".

### Statements, reconciliations and details (D10)

- T11 Statement of earnings, "Second Quarter Ended June 30, 2026 and 2025", l.375-415 (page 9);
  2Q26 / 2Q25 / % Change. NEW l.387-395: Net Sales $12,593 / $11,142 / 13.0; Cost of products
  sold 5,325 / 4,854 / 9.7; Amortization 658 / 420 / 56.8; R&D 892 / 725 / 22.9; SG&A 4,025 /
  3,091 / 30.3; Total Operating Cost and Expenses 10,900 / 9,090 / 19.9; Operating Earnings 1,693
  / 2,052 / (17.5). Then Interest expense, net 299 / 50 / n/m (l.397); Net FX 4 / (11) / n/m
  (l.399); Other (income) expense, net (134) / (137) / (2.5) (l.401); EBT 1,524 / 2,150 / (29.1)
  (l.403); Taxes on Earnings 596 / 371 / 60.8 [1)] (l.405); NE $928 / $1,779 / (47.8) (l.407); NE
  excl. Specified $2,290 / $2,213 / 3.5 [2)] (l.409); Diluted EPS $0.53 / $1.01 / n/m (l.411);
  Diluted EPS excl. Specified $1.31 / $1.26 / 4.0 [2)] (l.413); shares 1,743 / 1,751 (l.415).
  Footnotes l.427-433 (page 10).
- T12 Statement of earnings, "First Half Ended June 30, 2026 and 2025", l.437-469 (page 11); 1H26 /
  1H25 / % Change. NEW l.449-457: Net Sales $23,757 / $21,500 / 10.5; Cost of products sold 10,215
  / 9,322 / 9.6; Amortization 1,080 / 840 / 28.5; R&D 1,659 / 1,441 / 15.1; SG&A 7,765 / 6,152 /
  26.2; Total Operating Cost and Expenses 20,719 / 17,755 / 16.7; Operating Earnings 3,038 / 3,745
  / (18.9). l.459 (one line): Interest expense, net 367 / 99 / n/m; Net FX (9) / (18) / n/m; Other
  (293) / (264) / 10.6; EBT 2,973 / 3,928 / (24.3); "Taxes on earnings" 968 / 824 / 17.5 [1)]. NE
  $2,005 / $3,104 / n/m (l.461); NE excl. Specified $4,312 / $4,132 / 4.4 (l.463); Diluted EPS
  $1.14 / $1.77 / n/m (l.465); Diluted EPS excl. Specified $2.46 / $2.35 / 4.7 (l.467); shares
  1,745 / 1,749 (l.469). Footnotes l.481-487 (page 12).
- T13 Non-GAAP Reconciliation, second quarter, l.491-529 (page 13).
  - 2Q26: 658 / (658) / — (l.497). NEW l.499-508: Gross Margin 6,610 / 697 / 7,307; R&D 892 /
    (25) / 867; SG&A 4,025 / (428) / 3,597; Other (134) / (27) / (161); EBT 1,524 / 1,177 / 2,701;
    Taxes 596 / (185) / 411; NE 928 / 1,362 / 2,290; EPS $0.53 / $0.78 / $1.31. Prose l.510: $658m
    plus "other net expenses of $519 million" (acquisitions, legal reserves, investment
    impairments); "See page 18".
  - 2Q25: 420 / (420) / — (l.516). NEW l.518-527: Gross Margin 5,868 / 478 / 6,346; R&D 725 /
    (20) / 705; SG&A 3,091 / (1) / 3,090; Other (137) / (1) / (138); EBT 2,150 / 500 / 2,650; Taxes
    371 / 66 / 437; NE 1,779 / 434 / 2,213; EPS $1.01 / $0.25 / $1.26. Prose l.529: $420m plus "$80
    million"; "See page 19".
- T14 Non-GAAP Reconciliation, first half, l.533-575 (page 14).
  - 1H26: 1,080 / (1,080) / — (l.541). NEW l.543-552: Gross Margin 12,462 / 1,129 / 13,591; R&D
    1,659 / (49) / 1,610; SG&A 7,765 / (901) / 6,864; Other (293) / (34) / (327); EBT 2,973 /
    2,113 / 5,086; Taxes 968 / (194) / 774; NE 2,005 / 2,307 / 4,312; EPS $1.14 / $1.32 / $2.46.
    Prose l.554: $1.080bn plus "$1.033 billion"; "See page 20".
  - 1H25: 840 / (840) / — (l.562). NEW l.564-573: Gross Margin 11,338 / 926 / 12,264; R&D 1,441 /
    (47) / 1,394; SG&A 6,152 / (11) / 6,141; Other (264) / (36) / (300); EBT 3,928 / 1,020 /
    4,948; Taxes 824 / (8) / 816; NE 3,104 / 1,028 / 4,132; EPS $1.77 / $0.58 / $2.35. Prose
    l.575: $840m plus "$180 million"; "See page 21".
- T15 Tax-rate reconciliations, l.579-653 (page 15): 2Q26 (l.591-595) $1,524 / $596 / 39.1% [1)];
  1,177 / (185); $2,701 / $411 / 15.2%. 2Q25 (l.607-611) $2,150 / $371 / 17.3% [2)]; 500 / 66;
  $2,650 / $437 / 16.5%. 1H26 (l.629-633) $2,973 / $968 / 32.5% [3)]; 2,113 / (194); $5,086 /
  $774 / 15.2%. 1H25 (l.645-649) $3,928 / $824 / 21.0% [4)]; 1,020 / (8); $4,948 / $816 / 16.5%.
  Footnotes l.613-615, 651-653.
- T16 Non-GAAP Revenue Reconciliation, second quarter, l.657-687 (page 16). Columns (l.661-667):
  2Q26 Abbott Reported / Foreign exchange / Comparable Revenue | 2Q25 Abbott Reported / Impact of
  acquisition (a) / Impact of multi-year agreement (b) / Comparable Revenue | % Change vs. 2Q25:
  Reported / Comparable. (No acquisition or multi-year column for 2Q26.)
  - Total Company 12,593 / (86) / 12,507 | 11,142 / 811 / (22) / 11,931 | 13.0 / 4.8; U.S. 5,216 /
    — / 5,216 | 4,276 / 786 / (22) / 5,040 | 22.0 / 3.5; Intl 7,377 / (86) / 7,291 | 6,866 / 25 /
    — / 6,891 | 7.5 / 5.8 (l.669).
  - Total Diagnostics 3,092 / (22) / 3,070 | 2,173 / 811 / — / 2,984 | 42.3 / 2.9; U.S. 1,660 / —
    / 1,660 | 811 / 786 / — / 1,597 | 104.8 / 4.0; Intl 1,432 / (22) / 1,410 | 1,362 / 25 / — /
    1,387 | 5.1 / 1.6 (l.671).
  - Total Cancer Diagnostics 919 / — / 919 | — / 811 / — / 811 | n/a / 13.3; U.S. 890 / — / 890 |
    — / 786 / — / 786 | n/a / 13.3; Intl 29 / — / 29 | — / 25 / — / 25 | n/a / 13.8 (l.673).
  - Total Medical Devices 5,853 / (57) / 5,796 | 5,369 / — / (22) / 5,347 | 9.0 / 8.4; U.S. 2,680
    / — / 2,680 | 2,503 / — / (22) / 2,481 | 7.0 / 8.0; Intl 3,173 / (57) / 3,116 | 2,866 / — / —
    / 2,866 | 10.7 / 8.7 (l.675).
  - Total Structural Heart* 597 / (6) / 591 | 581 / — / (22) / 559 | 2.7 / 5.7; U.S. 225 / — / 225
    | 249 / — / (22) / 227 | (9.8) / (0.9); Intl 372 / (6) / 366 | 332 / — / — / 332 | 12.1 / 10.2
    (l.677).
  - Footnotes: * l.679-681 (only "$55 million ... second quarter of 2025"); a) l.683-685; b) l.687.
- T17 Non-GAAP Revenue Reconciliation, first half, l.691-724 (page 17). Columns (header l.695-704,
  split by the code fence): 1H26 Abbott Reported / Impact of acquisition (a) / Impact of
  multi-year agreement (b) / Foreign exchange / Comparable Revenue | 1H25 Abbott Reported / Impact
  of acquisition (a) / Impact of multi-year agreement (b) / Comparable Revenue | % Change vs.
  1H25: Reported / Comparable.
  - Total Company 23,757 / 706 / (8) / (500) / 23,955 | 21,500 / 1,518 / (46) / 22,972 | 10.5 /
    4.3; U.S. 9,490 / 681 / (8) / — / 10,163 | 8,444 / 1,470 / (46) / 9,868 | 12.4 / 3.0; Intl
    14,267 / 25 / — / (500) / 13,792 | 13,056 / 48 / — / 13,104 | 9.3 / 5.3 (l.706).
  - Total Diagnostics 5,272 / 706 / — / (98) / 5,880 | 4,227 / 1,518 / — / 5,745 | 24.7 / 2.4;
    U.S. 2,565 / 681 / — / — / 3,246 | 1,682 / 1,470 / — / 3,152 | 52.5 / 3.0; Intl 2,707 / 25 / —
    / (98) / 2,634 | 2,545 / 48 / — / 2,593 | 6.4 / 1.6 (l.708).
  - Total Cancer Diagnostics 1,015 / 706 / — / (1) / 1,720 | — / 1,518 / — / 1,518 | n/a / 13.3;
    U.S. 983 / 681 / — / — / 1,664 | — / 1,470 / — / 1,470 | n/a / 13.2; Intl 32 / 25 / — / (1) /
    56 | — / 48 / — / 48 | n/a / 16.5 (l.710).
  - Total Medical Devices 11,392 / — / (8) / (306) / 11,078 | 10,264 / — / (46) / 10,218 | 11.0 /
    8.4; U.S. 5,203 / — / (8) / — / 5,195 | 4,842 / — / (46) / 4,796 | 7.4 / 8.3; Intl 6,189 / — /
    — / (306) / 5,883 | 5,422 / — / — / 5,422 | 14.2 / 8.5 (l.712).
  - Total Structural Heart* 1,175 / — / (8) / (35) / 1,132 | 1,112 / — / (46) / 1,066 | 5.7 / 6.2;
    U.S. 449 / — / (8) / — / 441 | 497 / — / (46) / 451 | (9.6) / (2.2); Intl 726 / — / — / (35) /
    691 | 615 / — / — / 615 | 18.1 / 12.4 (l.714).
  - Footnotes: * l.716-718 (only "$101 million ... first half of 2025"); a) l.720-722; b) l.724.
- T18-T21 Details of Specified Items (columns as D07 T17).
  - T18 2Q26, l.728-762 (page 18). NEW l.740-746: Gross Margin $32 / $4 / $658 / $3 / $697; R&D
    (10) / — / — / (15) / (25); SG&A (42) / (1) / — / (385) / (428); Other 1 / (1) / — / (27) /
    (27); EBT $83 / $6 / $658 / $430 / 1,177. Taxes (d) (185) (l.748); NE $1,362 (l.750); EPS
    $0.78 (l.752). Footnotes l.754-762: (a) adds "including inventory step-up amortization" (no
    accelerated equity awards); (c) "$385 million for legal reserves related to an
    agreed-in-principle settlement, subject to satisfaction of certain contingencies" + investment
    impairments + MDR/IVDR; (d) "tax expense" + "approximately $240 million".
  - T19 2Q25, l.766-800 (page 19). NEW l.778-784: Gross Margin $1 / $55 / $420 / $2 / $478; R&D —
    / (7) / — / (13) / (20); SG&A (3) / 1 / — / 1 / (1); Other (1) / — / — / — / (1); EBT $5 / $61
    / $420 / $14 / 500. Taxes (d) 66 (l.786); NE $434 (l.788); EPS $0.25 (l.790). Footnotes
    l.792-800: (a) integration costs only; (b) "and cost reduction initiatives"; (c) MDR/IVDR only;
    (d) "tax benefit" + "2025 ... approximately $100 million".
  - T20 1H26, l.804-838 (page 20). NEW l.816-822: Gross Margin $34 / $11 / $1,080 / $4 / $1,129;
    R&D (11) / (10) / — / (28) / (49); SG&A (486) / (34) / — / (381) / (901); Other (1) / (3) / —
    / (30) / (34); EBT $532 / $58 / $1,080 / $443 / 2,113. Taxes (d) (194) (l.824); NE $2,307
    (l.826); EPS $1.32 (l.828). Footnotes l.830-838: (a) accelerated Exact Sciences equity awards
    + "inventory step-up amortization"; (c) same $385m text; (d) "tax expense" + "$440 million".
  - T21 1H25, l.842-876 (page 21). NEW l.854-860: Gross Margin $1 / $81 / $840 / $4 / $926; R&D
    (1) / (23) / — / (23) / (47); SG&A (6) / (6) / — / 1 / (11); Other (25) / — / — / (11) / (36);
    EBT $33 / $110 / $840 / $37 / 1,020. Taxes (d) (8) (l.862); NE $1,028 (l.864); EPS $0.58
    (l.866). Footnotes l.868-876: (a) integration "as well as other costs related to business
    acquisitions"; (c) MDR/IVDR "and charges for investment impairments"; (d) "tax benefit" +
    "$300 million".
- Arithmetic checks (all hold): sub-columns sum to segment totals; statement, recon and details
  identities as in D07; Reported + adjustments = Comparable in every revenue-recon row.

### Flags (D10)

- 1H26 = D08 1Q26 + D10 2Q26 in every checked cell: segment and sub-business sales (U.S., Intl,
  Total), statement rows (incl. GAAP EPS $0.61 + $0.53 = $1.14; adjusted $1.15 + $1.31 = $2.46),
  recon rows, every specified-details cell, FX (414 + 86 = 500; Dx 76 + 22 = 98; MD 249 + 57 =
  306; Structural Heart 29 + 6 = 35), and tax footnotes (~$50m benefit + ~$110m expense = ~$60m
  expense; ~$200m + ~$240m = ~$440m).
- 1H25 = D08 1Q25 + D10 2Q25 in every checked cell: statement, recon and details rows; Exact
  Sciences 707 + 811 = 1,518 (U.S. 684 + 786 = 1,470; Intl 23 + 25 = 48); multi-year (24) + (22)
  = (46); restated Structural Heart 531 + 581 = 1,112 (U.S. 248 + 249 = 497; Intl 283 + 332 =
  615); Dx 2,054 + 2,173 = 4,227 (U.S. 871 + 811 = 1,682; Intl 1,183 + 1,362 = 2,545); MD 4,895 +
  5,369 = 10,264.
- 2Q25/1H25 comparatives repeat D03 values recorded in doc-map.md (Shared ground S1) except the
  recast Structural Heart and the Diagnostics regrouping.
- Specified footnote (a) wording for 2025 comparatives differs by period/edition: 2Q25 (l.794)
  integration costs only; 1H25 (l.870) adds "other costs related to business acquisitions"; the
  1Q25 (a) in D08 (l.521) names "a fair value adjustment to contingent consideration", which the
  1H25 text does not mention.
- Printed % vs ratio of printed millions (one-decimal differences): Dx U.S. reported 104.8 (l.65,
  167, 671) vs 1,660/811 = +104.69%; Structural Heart reported 2.7 (l.280, 677) vs 597/581 =
  +2.75%; Dx 1H comparable 2.4 (l.93, 199, 708) vs 5,880/5,745 = +2.35%; Dx 2Q U.S. comparable
  4.0 vs 1,660/1,597 = +3.94%; Dx 2Q Intl comparable 1.6 vs 1,410/1,387 = +1.66%; Cancer Dx U.S.
  2Q 13.3 vs 890/786 = +13.23%; Taxes 2Q % change 60.8 (l.405) vs 596/371 = +60.65%; GAAP tax rate
  1H26 32.5% (l.629) vs 968/2,973 = 32.56%. Total comparable 4.8 / 4.3, Cancer Dx 13.3 (2Q and
  1H), MD 8.4 match.
- Rounded prose: l.183 "mid-teens growth of Cologuard" (no Cologuard row; Cancer Dx comparable
  13.3); l.128 "Nutrition sales increased $127 million on a sequential basis" = 2,144 (l.61) -
  2,017 (D08 l.59); l.25 adjusted EPS bullet has no growth claim (table 4.0, l.413); l.17 headline
  growth 13.0 / 4.8 = table. CGM 11.0% reported / 9.5% comparable (l.292), no table row.
- MD leader sentence l.290 ("low-teens growth in Electrophysiology and high-single-digit growth in
  Rhythm Management, Diabetes Care, and Heart Failure"): comparable 13.4 / 9.5 / 9.0 / 8.7;
  reported 14.0 / 10.4 / 10.5 / 9.0 (l.280-282). The sentence does not state its basis.
- Structure: 2Q recon has no acquisition column for 2Q26 (Exact Sciences is in reported Cancer Dx
  919) and no multi-year column for 2Q26; the 1H recon carries both. The * footnote under the 2Q
  recon (l.681) gives only $55m, under the 1H recon (l.718) only $101m; MD table footnote l.319
  gives both.
- 1H statement prints NE % change "n/m" (l.461) where the 2Q statement prints (47.8) (l.407).
- 2Q26 Other (c) SG&A (385) (l.744) equals the $385m legal reserve (l.760); 1H26 Other (c) SG&A
  (381) (l.820) because 1Q26 Other (c) SG&A was +4 (D08 l.471). 2Q26 Acquisition gross margin $32
  (l.742) beside the "inventory step-up amortization" wording (l.756); 1Q26 $2 (D08 l.469).
- Interest expense, net: 299 (2Q26, l.397) vs 50 (2Q25); 367 vs 99 for 1H (l.459); 68 in 1Q26
  (D08 l.290); % change n/m; no reason stated.
- Segment columns of T1/T2 do not sum to Total Company: U.S. 871+1,660+2,680 = 5,211 vs 5,216
  (2Q26); 1,715+2,565+5,203 = 9,483 vs 9,490 (1H26); International sums exactly.
- Tax footnotes 2Q26 / 1H26 say "net tax expense primarily as a result of" (l.427, 481, 613,
  651); D07 and D08 tax footnotes lack "primarily".

### Layout (D10)

- NEW Markdown blocks as in D07. In T11 the Markdown block ends at Operating Earnings (l.395);
  Interest expense (l.397) onward is tab-separated. In T12 five rows share l.459 (Interest expense
  through Taxes, with lower-case "Taxes on earnings").
- Rows sharing one line: l.82 (U.S., Intl, Total), l.95 (comparable U.S. + Intl), l.109, 136, 163,
  191, 217 (Intl + Total), l.169, 197 (Intl + Total reported + excl. FX in Dx tables), l.203 (Intl
  comparable row + "*" footnote), l.271 (U.S., Intl, Total), l.491, 533 (page titles run-on),
  l.669-677, 706-714 (Total/U.S./Intl recon rows per line).
- "—" as a growth value: Nutrition Intl 1H26 (l.90, 144) - rounds to zero.
- Headers split: l.537-539 and 558-560 ("As" / "Reported (GAAP) Specified Items As Adjusted");
  l.663-667 ("Non-GAAP" and "Impact" / "of multi-year agreement (b)"); l.695-704 with the code
  fence l.699-702.
- Footnote markers on their own lines: "*" l.679, 716; "a)" l.683, 720. Marker "1" fused to the
  guidance range (l.19 "7.5%1", l.27, l.327).
- Column heads hyphenated "Electro-physiology*", "Neuro-modulation" (l.269, 296); D08 uses
  "Electrophysiology*", "Neuromodulation" (l.188); D07 "Electrophysiology", "Neuro-modulation".
- No U+FFFD; curly apostrophe only in footnote 1 (l.371).

### Prose anchors (current lines, D10)

- Headline l.15; sub-bullets l.17-19 ("$2.1 billion" returned l.19); dateline l.21; bullets
  l.23-39 (comparable guidance l.27; EPS raise "compared to previous range of $5.38 to $5.58" l.29;
  TECTONIC l.31; HRS l.33; Libre Duo l.35; Amulet 360 FDA submission l.37; ACS guidelines l.39);
  Ford l.41; comparable definition l.47-49; FX note l.51; Nutrition l.126-128; Diagnostics
  l.177-183; EPD l.234-236; MD l.288-292; guidance l.325-333 (FY EPS $5.45-$5.60 l.329; 3Q26
  $1.38-$1.46 l.331); dividend l.335-339; employees l.343; call l.347; forward-looking caution
  l.355; contacts l.357-369; footnote 1 l.371 (verbatim = D08 l.265); statement footnotes
  l.427-433, 481-487.

<!-- END C2 D10 -->

<!-- C2: shared -->
## Shared ground (tables, 2026 releases)

Facts and locations only. D01-D04 values are quoted from `notes/doc-map.md` (section named; its
line numbers are old-text lines). D07/D08/D10 lines are current.

### S1 Prior-period columns that repeat earlier releases

- D07 4Q24 / 12M24 vs D01 (doc-map.md "D01" section): Net Sales 10,974 / 41,950 (D07 l.395, 456);
  EBT 2,030 / 7,013; taxes (7,199) / (6,389); NE $9,229 / $13,402; GAAP EPS $5.27 / $7.64;
  adjusted EPS $1.34 / $4.67; 4Q24 shares 1,746 (l.408-420, 469-481); amortization 465 / 1,878;
  other net expenses $268m / $755m (l.549, 591); tax rates (354.6%) / 15.0% and (91.1%) / 15.0%
  (l.623-627, 661-665); specified pre-tax 733 / 2,633, tax 7,613 / 7,835, net $(6,880) /
  $(5,202), EPS $(3.93) / $(2.97) (l.741-747, 817-823); "$7.497 billion" footnote (l.434, 495, 631,
  669); 4Q24 $10.974bn / Dx $2.520bn / COVID $176m and FY2024 $41.950bn / Dx $9.341bn / COVID
  $747m (l.375-377); 12M24 U.S. 16,323, Intl 25,627 (l.681). All equal.
  - D07 also prints 4Q24/12M24 rows that doc-map.md records as clipped in D01: D07 l.393-402,
    454-463 (statement top rows), 538-547, 580-589 (recon rows), 735-741, 811-817 (details rows).
    Their D01 counterparts are now visible at D01 l.480-489, 531-540 (statement), 590-599, 638-647
    (4Q24, 12M24 EPS recon) and 814-820, 886-892 (4Q24, 12M24 details) per line-remap.md; not
    compared in this pass.
- D08 1Q25 vs D02 (doc-map.md "D02" section): Net Sales 10,358 (D08 l.283); U.S. 4,168, Intl 6,190
  (l.433); Diagnostics 2,054 (l.435); MD 4,895 (l.441); EBT 1,778; taxes 453; NE $1,325; NE excl.
  Specified $1,919; EPS $0.76 / adjusted $1.09; shares 1,747 (l.296-308); amortization 420; other
  net expenses $100m (l.376); tax rates 25.5% / 16.5% with 520 / (74) (l.408-412); specified (74)
  / $594 / $0.33 (l.513-517); "$200 million" deferred-tax item (l.322, 416, 527); 1Q25 (a)
  contingent-consideration and (c) investment-impairment wording (l.521, 525). All equal except
  the S2 items. D02 counterparts of D08 l.281-290, 365-374, 505-511 are now visible at D02
  l.284-293, 339-348, 443-449 per line-remap.md; not compared in this pass.
- D10 2Q25 / 1H25 vs D03 (doc-map.md "D03" section): Net Sales 11,142 / 21,500; U.S. 4,276 / 8,444;
  Intl 6,866 / 13,056 (D10 l.669, 706); Diagnostics 2,173 / 4,227 (l.671, 708); MD 5,369 / 10,264
  (l.675, 712); 2Q25 other (income) expense (137) (l.401); EBT 2,150 / 3,928; taxes 371 / 824; NE
  $1,779 / $3,104; GAAP EPS $1.01 / $1.77; adjusted $1.26 / $2.35; 1H25 NE excl. Specified $4,132;
  2Q25 shares 1,751 (l.403-415, 459-469); amortization 420 / 840; other net expenses $80m / $180m
  (l.529, 575); tax rates 17.3% / 16.5% (500 / 66) and 21.0% / 16.5% (1,020 / (8)); specified 66 /
  $434 / $0.25 and (8) / $1,028 / $0.58; tax items "$90 million" benefit with "$100 million" /
  "$300 million" adjustments (l.429, 483, 615, 653). All equal except the S2 items. D03
  counterparts of D10 l.387-395, 449-457, 518-527, 564-573, 778-784, 854-860 are now visible at D03
  l.409-419, 463-472, 516-525, 562-571, 704-710, 772-778 per line-remap.md; not compared here.
- FY2025 totals: D07 $44.328bn / U.S. 17,126 / Intl 27,202 (l.84-86, 377, 456, 681) repeated in
  footnote 1 of D08 (l.265) and D10 (l.371), which are verbatim identical.

### S2 Same-period figures that differ between releases

- Structural Heart recast for the Amulet transfer "on Jan. 1, 2026" (D08 l.207, 447; D10 l.319,
  681, 718): 1Q25 D02 577 (U.S. 282 / Intl 295; doc-map.md D08 section and Shared ground
  "Changed or restated figures" item (1)) vs D08 531 (248 / 283, l.443), "$46 million"; 2Q25 D03
  636 (289 / 347; doc-map.md D10 section) vs D10 581 (249 / 332, l.677), "$55 million"; 1H25 D03
  1,213 (doc-map.md D10 section) vs D10 1,112 (497 / 615, l.714), "$101 million". Moved amounts by geography (arithmetic from the pairs): 1Q25 U.S. 34 /
  Intl 12; 2Q25 U.S. 40 / Intl 15. MD totals unchanged (4,895; 5,369; 10,264). Restated 2025
  Electrophysiology dollars appear in no release. The D08/D10 notes state the transfer and the
  moved amounts; no release states which edition's 2025 figure governs.
- D07's 4Q25 / FY2025 Structural Heart 675 / 2,523 and Electrophysiology 730 / 2,764 (l.285, 312)
  are on the pre-transfer basis; no 2026 release restates 4Q25 or FY2025 sub-business sales.
- Diagnostics regrouping "Beginning in 2026" (D08 l.137; D10 l.203): D07 columns Molecular / Point
  of Care / Rapid Diagnostics (4Q25 141 / 158 / 697; FY2025 517 / 606 / 2,454; l.175, 206) vs
  D08/D10 Rapid/Molecular Diagnostics (1Q26 812; 2Q26 755; 1H26 1,567). 2025-period sub-business
  dollars on the new grouping are not printed (growth rates only). Core Laboratory keeps its name
  (4Q25 1,461; FY2025 5,360; 1Q26 1,272; 2Q26 1,418; 1H26 2,690). Diagnostics totals unchanged.
- Exact Sciences adjustment (comparable bases; reported prior-year figures are not restated):
  1Q25 10,358 -> 11,041 (D08 l.433); 2Q25 11,142 -> 11,931 (D10 l.669); 1H25 21,500 -> 22,972
  (D10 l.706). Exact pre-acquisition sales: 1Q25 707 (U.S. 684 / Intl 23), 2Q25 811 (786 / 25),
  1H25 1,518 (1,470 / 48), 1Q26 706 (681 / 25; to the March 23, 2026 acquisition date); 2Q26 none
  (Exact inside reported Cancer Dx 919). Exact 2025 sales $3.247bn (U.S. $3.145bn / Intl $102m;
  D08 l.265, D10 l.371); 2H25 Exact sales are not printed (arithmetic 3,247 - 1,518 = 1,729).
- 1Q25 specified items: "net after-tax charges of $594 million" (D02, doc-map.md D02 section) vs
  "net after-tax benefits of $594 million" (D08 l.326); D08's table (l.373) adds 594 to GAAP NE.
- FY2024 ZonePerfect adjustment: (13) in D07 l.681-685 vs (14) in D01 (doc-map.md Shared ground,
  "Changed or restated figures" item (3)).
- 4Q24 footnote wording (doc-map.md D07 section, now at D07 l.751 and l.549): D07 4Q24 (a) adds
  "as well as other costs related to business acquisitions"; D07 4Q24 recon prose omits
  "intangible impairments" (D01 includes it, per doc-map.md).
- Metric basis: organic (D07 l.47: FX + ZonePerfect; separate excl.-COVID rows) vs comparable (D08
  l.45-47, D10 l.47-49: FX + multi-year agreement excluded, Exact Sciences included in both years).
  Row labels change from "Impact of foreign exchange" / "Organic" to "Total reported excl. foreign
  exchange impact" / "Comparable sales growth"; COVID and business-exit rows appear only in D07.

### S3 Period tables that yield a quarter (arithmetic)

- D07 12M25 minus D04 9M25 (doc-map.md D04 section) equals D07's printed 4Q25: sales 44,328 -
  32,869 = 11,459; U.S. 17,126 - 12,743 = 4,383; Intl 27,202 - 20,126 = 7,076; MD 21,387 - 15,712
  = 5,675; Diabetes Care 7,998 - 5,865 = 2,133; EBT 8,466 - 6,108 = 2,358; taxes 1,942 - 1,360 =
  582; NE 6,524 - 4,748 = 1,776; NE excl. Specified 9,040 - 6,410 = 2,630; adjusted EPS $5.15 -
  $3.65 = $1.50; amortization 1,682 - 1,260 = 422; specified pre-tax 2,296 - 1,568 = 728, tax
  (220) - (94) = (126), net 2,516 - 1,662 = 854; other net expenses 614 - 308 = 306; COVID $297m -
  $208m = $89m; Dx $8.937bn - $6.480bn = $2.457bn. GAAP EPS $3.72 - $2.70 = $1.02 vs printed
  $1.01 (doc-map.md Shared ground notes per-share non-additivity).
- D07 12M24 minus D04 9M24 (doc-map.md) equals 4Q24: EBT 7,013 - 4,983 = 2,030; taxes (6,389) -
  810 = (7,199); NE 13,402 - 4,173 = 9,229; NE excl. 8,200 - 5,851 = 2,349; adjusted EPS $4.67 -
  $3.33 = $1.34; amortization 1,878 - 1,413 = 465; specified 2,633 - 1,900 = 733, 7,835 - 222 =
  7,613, (5,202) - 1,678 = (6,880); other net 755 - 487 = 268; sales 41,950 - 30,976 = 10,974.
  GAAP EPS $7.64 - $2.38 = $5.26 vs $5.27.
- D07 12M25 details minus 4Q25 details give implied 9M25 cells, e.g. Other (c) SG&A (159) - (165) =
  +6; Acquisition EBT 83 - 48 = 35; Restructuring 287 - 71 = 216; Other 244 - 187 = 57 (total 1,568
  = D04 9M25 per doc-map.md). D04's own 9M25 details rows are at D04 l.756-762 per line-remap.md
  (not read here).
- D10 1H - 2Q = D08 1Q for both years (D10 Flags). Restated 1Q25 Structural Heart is printed in D08
  (531) and also derivable from D10 (1,112 - 581).

### S4 Forecast / actual locations in the 2026 releases

- Next-quarter adjusted EPS: 1Q26 $1.12-$1.18 (D07 l.335) -> $1.15 (D08 l.17, 25, 306, 355); 2Q26
  $1.25-$1.31 (D08 l.225) -> $1.31 (D10 l.17, 25, 413, 508); 3Q26 $1.38-$1.46 (D10 l.331) -> no
  actual in the bundle's releases.
- FY2026 adjusted EPS: $5.55-$5.80 (D07 l.17, 31, 335) -> $5.38-$5.58 "which includes $0.20 of
  dilution related to the acquisition of Exact Sciences" (D08 l.19, 31, 223) -> raised to
  $5.45-$5.60 "compared to previous range of $5.38 to $5.58" (D10 l.19, 29; l.329 range only).
  FY2026 sales growth 6.5%-7.5%: "organic" (D07 l.17, 29, 333) -> "comparable" (D08 l.17, 29, 221;
  D10 l.19, 27, 327 "reaffirms"). 1H26 actuals: comparable +4.3% (D10 l.93, 706), adjusted EPS
  $2.46 (l.467); no FY2026 actual in the bundle's releases.
- FY2025: adjusted EPS actual $5.15 (D07 l.27, 479, 570) against the 2025 guidance editions listed
  in doc-map.md Shared ground; adjusted operating margin guidance (doc-map.md: D01/D02 "23.5% to
  24.0%", D03 "approximately 23.5%") has no printed FY2025 actual in D07 (components in S5).
- Exact Sciences: expected close "in the second quarter of 2026" (D07 l.33) -> completed "On March
  23, 2026" (D08 l.27, 47, 137, 147, 451; D10 l.49, 203, 685, 722).

### S5 Margin components (no margin percentages printed in D07, D08 or D10)

- The non-GAAP reconciliations print GAAP and adjusted Gross Margin, R&D and SG&A; the statements
  print Operating Earnings. Check of method: (adjusted Gross Margin - adjusted R&D - adjusted
  SG&A) / Net Sales on D08's 1Q25 rows (l.367-369) gives 21.03% and on D10's 2Q25 rows (l.520-522)
  22.90%; Gross Margin / Net Sales gives 52.81% / 57.13% (1Q25) and 52.67% / 56.96% (2Q25);
  Operating Earnings / Net Sales gives 16.34% (1Q25) and 18.42% (2Q25). These equal at one decimal
  the prose margins doc-map.md records for D02 (52.8 / 57.1 / 16.3 / 21.0) and D03 (52.7 / 57.0 /
  18.4 / 22.9).
- Same arithmetic, not printed anywhere (GAAP gross / adjusted gross / GAAP operating / adjusted
  operating, % of Net Sales): 4Q24 50.73 / 56.86 / 17.41 / 24.28 (D07 l.395-401, 540-542); 4Q25
  53.36 / 57.10 / 19.64 / 25.85 (l.395-401, 521-523); 12M24 50.93 / 56.21 / 16.27 / 22.16
  (l.456-462, 582-584); 12M25 52.62 / 56.74 / 18.17 / 23.24 (l.456-462, 563-565); 1Q26 52.42 /
  56.29 / 12.05 / 20.37 (D08 l.283-289, 348-350); 2Q26 52.49 / 58.02 / 13.44 / 22.58 (D10
  l.389-395, 501-503); 1H25 52.73 / 57.04 / 17.42 / 22.00 (l.451-457, 566-568); 1H26 52.46 / 57.21
  / 12.79 / 21.54 (l.451-457, 545-547).
- doc-map.md (D01 section) records FY2025 margin guidance "increase of 150 basis points at the
  midpoint compared to 2024" (midpoint 23.75% implies 22.25% for 2024); the 12M24 rows in D07 give
  22.16%. No release prints a FY2024 adjusted operating margin.

### S6 Rounded prose, unstated bases and printed-% differences

- Adjusted EPS growth prose vs table: "12 percent" vs 11.9 (D07 l.17, 23 / l.418); "10 percent" vs
  10.3 (D07 l.17, 27 / l.479); "6 percent" vs 5.5 (D08 l.17, 25 / l.306); D10 bullet gives none
  (4.0, l.413). FY2025 sales "$44.3 billion" (D07 l.25) vs 44,328.
- Medical Devices leader sentences name businesses without stating reported vs organic/comparable:
  D07 l.304, D08 l.213, D10 l.290 (values listed in each document's Flags).
- Cologuard "double-digit growth" (D08 l.147) and "mid-teens growth" (D10 l.183) have no table row;
  Cancer Dx comparable 13.4 (1Q26), 13.3 (2Q26, 1H26).
- Printed percentages that differ by 0.1 or more from ratios of printed millions are listed under
  each document's Flags (D07: NE excl. Specified 4Q25, Nutrition 12M25; D08: Cancer Dx, MD,
  Structural Heart, interest expense, GAAP tax rate; D10: Dx U.S., Structural Heart, Dx 1H
  comparable, taxes, GAAP tax rate 1H26).

### S7 Same number, different meaning

- "$89 million": 4Q25 COVID-19 testing-related sales (D07 l.194, 375) and 2025 Structural Heart
  compensation payments (D08 l.265; D10 l.371).
- 811: 2Q25 Diagnostics U.S. reported and 2Q25 Exact Sciences pre-acquisition sales (D10 l.671,
  669, 673).
- 1,693: 1Q25 Operating Earnings (D08 l.289) and 2Q26 Operating Earnings (D10 l.395).
- 422: amortization 4Q25 (D07 l.397) and 1Q26 (D08 l.285). (134): Other (income) expense 4Q25
  (D07 l.406) and 2Q26 (D10 l.401). $1.01: GAAP EPS 4Q25 (D07 l.416) and 2Q25 (D10 l.411). 1,747:
  shares 4Q25 (D07 l.420), 1Q25 and 1Q26 (D08 l.308). 706 (Exact 1Q26 to March 23; also the 1H26
  acquisition impact) vs 707 (Exact 1Q25).

### S8 Specified items and footnotes across the 2026 releases

- Total Specifieds EBT: 4Q24 733 (D07 l.741), 12M24 2,633 (l.817), 4Q25 728 (l.703), 12M25 2,296
  (l.779), 1Q25 520 (D08 l.511), 1Q26 936 (l.473), 2Q25 500 (D10 l.784), 2Q26 1,177 (l.746), 1H25
  1,020 (l.860), 1H26 2,113 (l.822).
- Legal reserves: $165m "related to a certain agreed-upon settlement" in Other (c), SG&A (165) in
  4Q25 (D07 l.701, 717) and in the 12M25 (c) text (l.793); $385m "related to an
  agreed-in-principle settlement, subject to satisfaction of certain contingencies" in Other (c),
  SG&A (385) in 2Q26 (D10 l.744, 760) and the 1H26 (c) text (l.836). None in D08. Neither names the
  matter.
- Exact Sciences costs in Acquisition (a): accelerated equity awards 1Q26 (D08 l.483; SG&A (444)
  l.471) and 1H26 (D10 l.832; SG&A (486) l.820); inventory step-up amortization 2Q26 / 1H26 (D10
  l.756, 832; Gross Margin $32 / $34, l.742, 818).
- Coverage-changing footnotes: business exit * (D07 l.110, 165; recon (a) l.687); COVID 1-2 (D07
  l.375-377); Diagnostics * (D08 l.137; D10 l.203); Amulet * (D08 l.207, 447; D10 l.319, 681,
  718); recon (a) Exact pre-acquisition sales (D08 l.451; D10 l.685, 722); recon (b) multi-year
  agreement (D08 l.453; D10 l.687, 724); footnote 1 on FY2026 comparable guidance (D08 l.265; D10
  l.371).

### S9 Layout patterns shared by D07, D08, D10

- NEW rows render as Markdown tables with blank header rows; other rows are tab-separated; many
  rows share one line (per-document Layout lists).
- "$" moves into the label cell when the first value is "—" (D07 l.737; D08 l.507).
- Code fences only in D08 l.426-429 and D10 l.699-702 (capture artifact, also present in docs/).
- Extra "—" token only in D08 l.443 (Structural Heart recon rows).
- Footnote digits fused to values or labels (D07 l.21, 25, 72, 100; D08 l.17, 29; D10 l.19, 27,
  327).

## Gaps (pass C2)

- D07 l.1-836, D08 l.1-530, D10 l.1-879: read in full; no gap markers, no U+FFFD, no unread range.
- Unresolved (no visual original beyond the capture): whether the D08 l.443 extra "—", the "$" in
  label cells (D07 l.737, D08 l.507) and the code fences reflect the source page or the capture.
- Not compared in this pass (C1 scope): D01-D03 newly visible rows paired with D07/D08/D10
  comparatives (locations in S1) and D04 9M25 details (S3).
- notes/doc-map.md pass-A sections for D07, D08, D10 still carry old-text line numbers; use
  notes/line-remap.md or the current lines above.

<!-- END C2 shared -->
