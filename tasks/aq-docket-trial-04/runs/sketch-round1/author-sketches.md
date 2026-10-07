# Independent question-author sketches (other families), raw return, 2026-10-06

Fresh question-author agent (Claude Code, claude-opus-5-5), asked to avoid the request-column
comparison family and the FAA part I/II Haiti classification; target medium; no files written.
Raw return copied verbatim below; caller assessment at the end.

I ran one sketch round. Three sketches survive: two Colombia legislation questions and one table comparison. I ranked them by how likely they are to land in the Medium band, and I think only i01 has a real chance. Nothing has been solved or screened yet, so these are proposals; any Medium result has to be measured on the platform. I wrote no files. origin: claude.

---

**id: i01**
- **difficulty_target:** medium
- **question:** As of January 2025, what was the Senate Appropriations Committee's FY2025 aid level for Colombia minus the Colombia total in the most recent enacted State-Foreign Operations appropriations act whose Colombia total covered all aid accounts? Answer in millions of dollars, to one decimal place. (44 words)
- **answer:** −$107.4 million (380.0 − 487.4)
- **facts:**
  - Doc 8 (D08) L513: "$380.0 million for Colombia, which is $33.3 million (8.1%) less than the Administration".
  - D08 L413 Table 2: "Colombia 453.1 377.5b 413.3 208.5b 380.0" (columns: FY2023 est. actual, FY2024 enacted, request, House, Senate).
  - D08 L429 note b: "Totals may not be comprehensive because the legislation/explanatory statement and bills/reports do not specify funding levels for some foreign assistance accounts."
  - D08 L29: "As of January 14, 2025, Congress has not concluded action on FY2025".
  - Doc 3 (D05) L45: "do not specify comprehensive appropriations totals for the Latin American and Caribbean region as a whole or for some Administration funding priorities, including Central America, Haiti, and Mexico".
  - D05 L45: "the act and the explanatory statement designate more funding than the Administration requested for Colombia ($487.4 million)".
  - D05 L1329: "for assistance to Colombia".
- **documents:** Doc 3 (D05), Doc 8 (D08)
- **dependency:**
  - D05's anchor is the FY2023 act's Colombia total. D06's 487.4 (L627) is the FY2024 Senate bill, S. 2438, not the FY2023 act. D06 and D08 print only the FY2023 estimate (453.1).
  - D08's anchor is S. 4797's 380.0, the non-enactment as of January 14, 2025, and the incompleteness flag on the FY2024 total.
  - D06 is not listed. It only repeats the FY2024 total and its incompleteness (note c, L643; L663).
  - Without D05, the likely answer is −73.1 (printed in D08), or D06's implied "Congress appropriated" 453.1. Both differ from the gold. Without D08, there is no Senate FY2025 level.
- **selected_levers:** Match, then exclude; Same series, right edition
- **lever_checks:**
  - Without the exclusion, the latest enacted total is 377.5, giving +2.5 (+0.7%). That decoy sits in the same table row as 380.0 and is ruled out only by note b.
  - The FY2023 estimate route gives −73.1 (printed in D08 L513).
  - The request route gives −82.9.
  - The "may" in note b does not save the FY2024 total: its reason clause ("do not specify ... some ... accounts") is stated firmly.
- **arithmetic_check:** Decimal script: 380.0 − 487.4 = −107.4. As a percentage it is −22.0%. Both inputs are stated once each at one decimal (D05 table and prose agree; D08 table and prose agree), so the answer cannot flip on figure choice.
- **shortcut_search:**
  - Searched 487.4, 380.0, 377.5, "comprehensive" and "may not be comprehensive" across the whole bundle. No passage prints 107.4 or 22.0%.
  - The overview does not show 487.4 or 380.0.
  - Strongest surviving route: the D08 row plus note b, then D05 L1329.
- **tags:** Cross-document join; Temporal alignment; Conditional filter
- **completeness:** All 8 documents were read in full, and the capture is complete. No gaps.
- **portfolio:** This shares D08's adjacent Colombia House/Senate paragraphs with i02. Submit only one of the two. It is distinct from families (a) and (b).
- **unresolved:**
  - Coverage of the FY2023 total is implied (D05 L45 and Table 4 note), not stated outright.
  - D06 L663 ("$75.6 million less than Congress appropriated ... in FY2023") gives a competing 453.1 reading. The question's "act ... total" wording is meant to exclude it.
  - Memory risk is low to moderate: 487.4 got some press, while 380.0 (July 2024) is obscure.

---

**id: i02**
- **difficulty_target:** medium
- **question:** Under the House Appropriations Committee's report on its FY2025 State-Foreign Operations bill, how much Economic Support Fund aid would Colombia receive? Answer in millions of dollars to one decimal place. (30 words)
- **answer:** $64.5 million (0.5 × 129.0)
- **facts:**
  - D08 L497: "therefore would reduce DA, ESF, and INCLE funding for Colombia by 50% compared with the FY2024 enacted appropriation".
  - Doc 6 (D06) L663: "The explanatory statement designates at least $377.5 million in assistance for Colombia" … "$129.0 million in ESF aid".
- **documents:** Doc 6 (D06), Doc 8 (D08)
- **dependency:**
  - D08's anchor is the 50% rule (D08-only). D08's FY2024 column gives only the 377.5b total.
  - D06's anchor is the FY2024 enacted ESF of 129.0 (searched: D06 L663 is the only occurrence).
  - Without D06, the route through D08's FY2025 request ESF (128.5) gives 64.25, so 64.3 (or 64.2 under half-even rounding). The FY2023 estimate (144.0) gives 72.0. Both differ from 64.5.
- **selected_levers:** Same series, right edition; Calculate across documents
- **lever_checks:** Same-label decoys for Colombia ESF:
  - FY2024 request 122.0 (D06 A-3) gives 61.0.
  - FY2025 request 128.5 gives 64.3.
  - FY2023 estimate 144.0 gives 72.0.
  - Skipping the cut gives 129.0.
- **arithmetic_check:** 0.5 × 129.0 = 64.50. At whole millions the gold splits 65/64 and collides with the request decoy, so one decimal is required.
- **shortcut_search:** 129.0 occurs only at D06 L663. "50%" also appears for Venezuela (D06 L719, D08 L601), but those are different rules. 64.5 occurs only as unrelated CBSI or Guatemala figures. Strongest route: D08 L497 then D06 L663.
- **tags:** Cross-document join; Temporal alignment
- **completeness:** Full read; no gaps.
- **portfolio:** Shares a family with i01. This one is likely easier: a stated rule applied to a prose figure (the aq-00949 q03 risk).
- **unresolved:**
  - The House total does not reconcile exactly. Halving D06's designations (taking the "$77.0 million in IMET aid" as DA) gives 170.25, which leaves 38.25 for FMF against 37.0 or 38.5. The per-account reading of the 50% cut is natural but could be challenged.
  - The IMET/DA label oddity sits next to the input.
  - Memory risk is low.

---

**id: i03**
- **difficulty_target:** medium
- **question:** Leaving aside countries whose actual FY2022 Economic Support Fund figure included 2022 Ukraine supplemental funds, which country's FY2022 ESF allocation differed between the State Department's FY2022 estimate and its actual figures, and by how much? Give actual minus estimate in millions of dollars. (44 words)
- **answer:** Mexico (−$1.0 million: 57.8 → 56.8)
- **facts:**
  - D05 A-2 (L2479–2497), one cell per line: "Mexico / 4.0 / 57.8 / … / 128.2".
  - D06 A-1 L810: "Mexico | 4.0 | 56.8 | — | — | 64.0 | 1.2 | 1.2 | — | 127.1".
  - D06 L877: "ESF figures for noted countries include a combined $64.0 million of supplemental assistance appropriated in the Additional Ukraine Supplemental Appropriations Act, 2022".
- **documents:** Doc 3 (D05), Doc 6 (D06)
- **dependency:**
  - D05's anchor is the FY2022 estimate by account (D05-only).
  - D06's anchor is the FY2022 actual by account plus the "a" marks (D06-only). D08 has only country totals.
  - Without D06, Mexico's total change (128,205 → 127,107 thousand) gives about −1.1 and cannot isolate ESF.
- **selected_levers:** Match, then exclude; Same series, right edition
- **lever_checks:**
  - Without the exclusion, the list is Colombia +6.0, Dominican Republic +3.0, Guatemala +20.0, Haiti +15.0, Honduras +10.0, (Barbados/Eastern Caribbean +10.0) and Mexico. The "a" deltas sum to 64.0, which checks the note.
  - USAID LAC Regional (+1.0) is a decoy that changed but is a program, not a country.
- **arithmetic_check:** Both tables were parsed by script, and ESF deltas were computed for every row. 56.8 − 57.8 = −1.0. Both tables are at one decimal and no alternative figure exists.
- **shortcut_search:** 56.8 appears only at D06 L810. 57.8 also appears as unrelated State Western Hemisphere FY2023 ESF. No passage states the change.
- **tags:** Cross-document join; Conditional filter; Temporal alignment
- **completeness:** Full read; no gaps.
- **portfolio:** Independent family (allocation revisions); no shared path with i01 or i02.
- **unresolved:**
  - The capture renders D05 A-2 one cell per line, so a 12+ character verbatim quote that carries 57.8 with its label may fail the form's check. D06's row is a pipe table.
  - The per-row footnote filter is close to the keyword-filter signal, so the risk of "Too easy" is real.
  - No memory risk.

---

**Rejected directions:**
- **Docs 1, 2, 4, 5 and 7:**
  - D02's allocated-account list against D01's or D06's supplementals (685; 400): a strong model classifies the accounts without D02, so D02 would fail the removal test, and the COVID amounts are public.
  - D05/D04 Kemp-Kasten → UNFPA $32.5M: widely known.
  - D04 §516 excess-defense-articles $500M cap, or the Global Fragility Act fund's $200M, via D08: two-hop lookups of public figures.
  - D07's $66.1B or $15.89B combined with D04: two-lookup arithmetic.
  - The 653(a) "30 days after enactment" rule (D02) against enactment dates: the dates are public and duplicated in D04 and D05.
  - FAA part classification: avoided, as it is family (b).
- **Other routes in the Latin America editions:**
  - The FY2025 continuing-resolution bridge (D08) into FY2024 provisions (D06): the Senate bill's withholding shares equal FY2024's (15%, 20%, 60%), and the continuing-resolution concept is public. The counter-fentanyl version (175 − 125) reduces to two lookups.
  - Costa Rica designations (46.0 vs 40.7): found by keyword search.
  - Venezuelan-migrant shares: the inputs are approximate.

## Caller assessment (2026-10-06)

- a-i01 (Colombia Senate FY2025 minus "most recent enacted act whose Colombia total covered all
  aid accounts", -107.4): rejected. The question carries its own filter clause (rulebook risk), the
  FY2023 act total's completeness is only implied, and D06's "$75.6 million less than Congress
  appropriated for the country in FY2023" makes 453.1 a second defensible base (one-answer risk).
- a-i02 (House FY2025 ESF for Colombia = 0.5 x 129.0 = 64.5): rejected. A stated rule applied to a
  prose figure (measured too easy before, aq-00949 q03), the House total does not reconcile, and
  the input sits beside D06's "$77.0 million in IMET aid" label error.
- a-i03 (Mexico FY2022 ESF estimate vs actual, excluding Ukraine-supplemental rows, -1.0): held as
  a different-family fallback only. Risks: exclusion clause in the question, per-row footnote
  filter close to the measured keyword-filter signal, D05 one-cell-per-line quotes, and a narrow
  data-revision fact.
- None is stronger than q01 rev 1 (clean wording, robust precision, probe-verified necessity,
  closed-book miss, natural same-row decoy). Plan B for q01 stays the timing-anchor variant.
