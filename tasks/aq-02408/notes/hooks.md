# aq-02408 - cross-document hooks (caller, 2026-10-09)

Target: medium (hard where supported); user: "there is no slot for Easy Tier for this bundle, we
should target medium and high. do your best." Six unrelated Federal Register documents; no editions,
no proposal/final pair, no document cites another. Cross-document links are shared grid operators
(SPP in all six; PJM D01/D04/D05/D06; MISO D01/D02/D04/D06; ERCOT D04/D05/D06), Calpine (D05/D06),
Dynegy (D01/D04), Miles City (D02/D03) and FERC's burden methodology (D01/D06). Numeric overlap scan
(scratchpad shared.py): only years and coincidences repeat across documents.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D04 L131-203 plants by market (Coleto Creek ERCOT 650 MW; Kincaid IL 1,108 and Miami Fort OH 1,100 in PJM; Welsh TX 1,056 in SPP); D05 L122-131 relevant markets = ERCOT and PJM Coastal Mid-Atlantic (SE PA, NJ, DE, eastern shores MD/VA) | coal capacity of EPA's covered plants inside DOJ's relevant markets = 650 MW | Wrong jurisdiction or scope (PJM vs its Coastal Mid-Atlantic area; Texas vs ERCOT) | 2,858 (ERCOT + all PJM plants), 1,706 (+ Welsh as "Texas"), 3,914 | gold is one printed plant figure; low model may read the market headings | closed 2026-10-09: reversed form (q01, 660 MW) quick-test "too easy" |
| h2 | D01 fn124 L571 "$100/hour is used"; D06 fn64 L302 "$63.52/hour", table cells "$508.16/hr" (per-response cost for 8 hrs), "$762.24/hr", "$565.36/hr" | FERC's 2026 hourly labor cost minus its 2024 figure = -$36.48 | Rounding and sign; Document convention (per-response cost labelled /hr) | +$408.16 from the "$508.16/hr" label; +$662.24; +$465.36 | both rates sit in plainly labelled footnotes; FERC's $100/hour FY2024 rate may be recalled (Doc 1 removal risk) | sketch i02 (weak) |
| h3 | D01 L419 PJM capacity rules assume $2,546 per MW-year; D05 CIS L632-637 PJM divestitures 1,134 + 569 + 828 + 1,136 + 707 = 4,374 MW | imputed reactive revenue of the divested PJM units = $11,136,204 a year | Calculate across documents; Part vs total | Calpine's ">5,000 MW" PJM total; York counted once; ERCOT plants added | product of figures the documents never connect (guide's common mistake); two lookups plus one operation | park |
| h4 | D06 L230 ISOs commenting on MOD-026-2 (ERCOT, ISO-NE, MISO, "New York System Operator", PJM, SPP); D01 L234-242 payers PJM, ISO-NE, NYISO; non-payers CAISO, SPP, MISO | commenters FERC named as non-payers = MISO, SPP | Match then exclude; entity resolution | CAISO (not a commenter), ERCOT (status not given), SPP pays outside the dead band (fn78) | short printed lists = measured too-easy shape; payer variant loses D06 necessity | drop |
| h5 | D02 L21/L51 BLM MCFO ~10 mi and ARS Fort Keogh ~8 mi, both Miles City, MT; D03 L147 Miles City DC Tie | federal land managed from the DC-tie town = 18 route miles | Bury one list item (ARS location only in SUMMARY) | 10 (BLM keyword), 8, 28.3 (all federal) | "Miles City" keyword search returns both; D03 bridge guessable | drop |
| h6 | D02 L79-81 NPC eastern interconnections MISO (Oliver) and SPP (Morton); D04 L254-258 EPA: MISO ~3,200 MW, SPP 1,056 MW | coal capacity EPA keeps online in those RTOs ~4,256 MW | Calculate across documents | plant sums 3,750 / 3,170 for MISO | mixes an approximate and an exact figure; NPC endpoints public | drop |
| h7 | D01 L199/L167 small facility <= 20 MW, power factor = real/apparent, range 0.95; D06 fn15 category 2 >= 20 MVA | real power at 20 MVA and 0.95 pf = 19 MW | Unit or basis | 20 (MVA = MW), 21.05 | nameplate MVA vs operating pf is conceptually loose; one multiplication | drop |
| h8 | D03 L29-34/L112 schedules by period (WAPA-217 seven schedules to Sep 30, 2030; WAPA-218 three from SPP RTO West go-live, scheduled Apr 1, 2026); any later-dated event in D04-D06 | schedules in effect on an event date | Same series, right edition | WAPA-218's three schedules | anchor event unrelated to WAPA (contrived); small integer | drop |
| h9 | D04 plant cessation dates incl. updates (Baldwin Dec 31, 2025 -> Dec 31, 2027; Newton Jul 17 -> Sep 1, 2027) and a D05/D06 date | capacity still scheduled to burn coal on that date | Superseded date or version | Baldwin's original date | updates printed beside the originals (tied); Big Cajun II Unit 3 capacity not given; arbitrary anchor | drop |

Independent authors (question-author agents, 2026-10-09; both read all six texts):
- B (no notes access) found only the h1 join and reversed it: D04 decides which DOJ market counts, D05 gives
  Calpine-owned divested capacity there (557 + 0.285 x 365 = 661.025 -> 660 MW). Promoted as q01. Its i02 = i01.
- A (with the map) found no fair Medium design. Its holds: $2,546/MW-yr x D04's PJM coal (2,208 MW) =
  $5,621,568, and DOJ's 800 homes/MW x D04's MISO coal net of Big Cajun II (3,170 MW) = 2,536,000 homes; both
  multiply figures the documents never connect (Guide common mistake), with plain-sentence exclusions and EPA's
  3,200/2,200 check sums in the path. A did not consider DOJ's relevant-market scope against D04's plants.
- Both rejected: Dynegy and Calpine name links (no numbers; D05's divestitures are all Calpine's), ISO-list
  intersections, the FERC hourly rate, 20 MVA x 0.95, NPC as a seventh DC tie, Western Interconnection state
  lists, comment-window gaps, single-document traps (Gregory share, D06 GO 1,834 vs 1,343, D04 shares), and every
  typo trap.

Bundle-level finding: every candidate is a filter or lookup in one document plus a selecting fact
or rate from another; no edition series, no grouped figure split across documents, no rule in one
document with instances in another. Measured history puts this shape at Easy or Too easy; the
strongest available lever is a scope trap whose cheapest route lands on the decoy (h1).
