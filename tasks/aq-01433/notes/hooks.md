# aq-01433 - cross-document hooks

Caller inventory (origin: claude), 2026-10-06, after a full read of D01-D06. Target: medium.
Local id -> platform Doc: D01=Doc 6 (mail response/Take 10), D02=Doc 3 (national partnership),
D03=Doc 2 (paid advertising), D04=Doc 4 (promotional materials), D05=Doc 5 (research),
D06=Doc 1 (ICP summary; cost Appendices C and D).

## Bundle traits that decide hook viability

- Six assessment reports of one program, all dated August 2012; no editions, forecasts or
  restatements. D06 (summary) repeats many component facts (452 ads, 28 languages, 167M,
  88 million items, 23 copy-test languages, 74%, 4,000 CBAMS interviews).
- Same quantity, different stated values across reports (contested; never build on them unless
  the question pins the source): contract budget 312.1M/371M/370M (D06) vs 362M (D03) vs App C
  $361,965,769 (rev 3/17/11) vs App D $371,242,775 (Nov 2010); ARRA to contract 100M (D06 prose)
  vs App D recovery 117,389,000; national/local ad split 88.3/78.7 (D03 Table 5) vs
  90,169,215/76,956,384 (D06 App C); rapid response 31.8 (D03 Table 6) vs 31,939,982 (App C);
  subcontractors 13 vs 14; promotional materials 288 (D04) vs ~300 (D06).
- Language-group footnotes conflict: D06 App C Emerging = Arabic, Farsi, Polish, Russian,
  Ukrainian; New Legacy = French, German, Greek, Italian, Portuguese, Yiddish. D03 Table 3 swaps
  them (Emerging = German, French, Italian, Greek, Portuguese, Yiddish; Legacy = Russian, Polish,
  Arabic, Farsi, Armenian, Ukrainian). D05 prose calls Russian/Polish/Arabic groups "Emerging",
  its Table 2 row "Legacy". Any membership-based question is ambiguous.
- Table defects: D04 App E Korean unusable printed "3009,410" (column remainder = 889,410,
  matching 7.8%/1.47%/0.75%); D04 App E German printed 30,000 but unusable 93,817 and App B
  ARRA rows sum to 300,000; Portuguese and Haitian Creole 900,000 (App E) vs 825,000 (App B).
  D03/D05 Table 2 glue footnote markers to NHPI/AIAN counts ("NHPI14", "AIAN28" = 4 and 8
  groups; D05 prints "NHPI34", "AIAN48").
- Flattened App D: "FY 2011 5,086,597" belongs to the Regional Partnerships column (contract
  base total 253,853,775 excludes it; regional base 186,445,697 includes it). Single-document.
- App C "Index vs. 2000" is against Census 2000 actual cost, not the inflated column; its
  percent column counts rapid response twice (80.9 includes the 9.5). Single-document.
- No document defines fiscal-year boundaries (only D06's "option years, ending September 30,
  2011"), so month-to-FY bridges rely on outside knowledge.

## Hooks

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D03 5.11 ad languages (14 base L316-317, 14 ARRA L319-322); D05 5.3b in-language focus groups by phase (L488-509) | Ad languages never copy-tested in-language: French, German, Hindi, Italian, Ukrainian, Yiddish (6 of 28 = 21.4%) | match then exclude; entity resolution | "Haitian (French)" tested vs ARRA "French"; Hindi buried in base list; 28 - 23 = 5 shortcut | D04 5.7 lists the same 28 languages ("also used for the Paid Advertising campaign"), so D03 is replaceable; "Haitian (French)" could be read as French | drop as framed (necessity); base-only variant = Hindi alone (easy) |
| h2 | D03 ARRA ad list; D04 5.7 base promo list (19) and ARRA promo list (9) | ARRA-added for ads but base for promo: Bengali, Hmong, Laotian, Thai, Urdu | match then exclude | 9 languages ARRA in both | two explicit lists; low-model intersection | weak (easy) |
| h3 | D03 ARRA ad list x D04 App E per-language quantities | Printed promo materials in ARRA ad languages (sum of 14) | aggregation; entity resolution | D04's own ARRA 9; Wave ARRA total 14,385,004; French vs Haitian Creole | German 30,000 vs 300,000 typo makes the sum contested | drop |
| h4 | D06 App D FY2011 column | Regional FY2011 = 5,086,597 | flattened table | contract column misread | single document; no fair cross-document partner found | park |
| h5 | D06 App C inflated vs actual 2000 | real growth vs printed index | printed decoy | index 173 etc. | single document | park |
| h6 | D04 App E Korean remainder x D06 questionnaire languages | unusable Korean items 889,410 | remainder | printed "3009,410" | bridge decides nothing; typo-based | park |
| h7 | D01 2000 response 67.4% x D06 2000 participation 74% | rate gap / UAA share | definition applied | 74 vs 67.4 | rounding makes derived UAA share imprecise; two lookups otherwise | drop |
