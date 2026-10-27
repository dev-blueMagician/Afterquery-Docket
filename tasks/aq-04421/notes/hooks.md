# aq-04421 - cross-document hooks

Target: medium (user 2026-10-13: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."; page: "Still open on this set: Hard, Medium", Hard 0/3 · Medium 0/2 ·
Easy 0/0, 8 submissions left, quick tests 0 of 15, runs 15 of 15).

## Same bytes as aq-02447: measured results read first

All six documents equal aq-02447's (2026-10-09). User, 2026-10-13, asked whether to go on: "Proceed".
Read with `tools/verdict_summary.py` on tasks/aq-02447/verdicts/AQ-02447_difficulty_2026-10-09_0913.txt:

- Run 1, Version 0cf427 (aq-02447 q01 rev 2): "Too easy", Low 5/5, Medium and High not run. All five low
  attempts were right (each enumerated the ten control numbers); the closed-book attempt committed "Five"
  and was marked as needing the documents. There is no wrong attempt, so no miss to design from.
- Quick tests there (user chat, no panels): two wordings of the control-number list difference too easy,
  one survived and then measured the Run 1 result; the net licence-application burden (-15 hours) too easy.

Families closed on these bytes by those results: a difference between two printed lists of control
numbers (D01 against D06); arithmetic on the Paperwork Reduction Act paragraphs (D02, D03, D06).
Not reopened below, however many cells are added.

## Hooks, this session (caller, Claude Opus 5.5, 2026-10-13)

aq-02447's inventory h1-h12 and its two independent authors' returns stand (tasks/aq-02447/notes/hooks.md).
New or re-examined:

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h13 | D04 L55-59, L1147-1161: HAS General Trading LLC and Smart Mail Services listed under the UAE, licence for all items. D06 L81-87, L191-197: G42 and Core42 approved for licence-free advanced computing items; MGX only "favorably review" | which named UAE companies still needed a licence for advanced chips after July 2026: three, from two documents | bury one list item late; mentions it vs does it; match, then exclude | G42, Core42 (approved); eight U.S. companies (not UAE-based) | one unprompted look into D04; MGX sits in the section about the asked property | sketch i01 |
| h14 | D03 Supp. 7 site addresses (L205-519); D04 Entity List addresses (L262-1161). Shared roads: Guoshoujing (D03 L485 Huahong Grace HFab 2; D04 L891 Sino IC, added); Fei La / Feila (D03 L374 Lam bonded warehouse; D04 L641 Jicun, added); Bi Bo (D03 L429-430 Lam office; D04 L608 Hexin Xingtong, corrected) | a listed firm on the same road as a trusted site | who belongs where; scatter the pieces | the Feila pair (wrong kind of site for i02), the Bi Bo pair (corrected entry), Jinghai 2nd against 3rd/4th Road | retrieval in two flattened tables; a reviewer may call it coincidence; Feila spelled two ways | sketches i02 (one firm, chip plant) and i04 (both firms); i04 = q01 rev 0, Run 16 "Too easy", High 3/3 (2026-10-14); repair i05 widens to corrected entries (adds the split Bi Bo Road pair) = q01 rev 1, Run 17 "Too easy", High 3/3: closed |
| h15 | D04 L32 effective September 12, 2025; D06 L30 effective July 10, 2026 | days between the two effective dates: 301 | calculate across documents | publication dates also give 301; mixed 297 or 305 | plain date count, a family quick-test too easy on other bundles | sketch i03, lowest priority |
| h16 | D03 Supp. 7 Samsung and SK hynix "Excluded from Sec. Sec. 744.6(c)(2)(i-iii)"; D01 L253-269 nine U.S.-person activities, (iv)-(vi) only where "you do not know", (vii)-(ix) "regardless of end use or end user" | how many of the nine still bind at an excluded plant for a person who knows what it makes: 3, not 9 - 3 = 6 | rule applied to an instance | 6 by subtraction | joins an October 2024 exclusion to January 2023 paragraphs; the bundle does not show those paragraphs still stood in 2024 | not offered (premise the documents do not confirm) |
| h17 | D02 L402-404 (744.8(c), (d): Entity List terms govern for a person on both lists); D04 review policy column | for which added entities the Entity List terms would displace the SDN section's defaults: Aerospace Information Research Institute, Atempo, Dentun, EB Teknoloji | match, then exclude | footnote 4 entities; Smart Mail (tied to an OFAC designee) | delete-and-guess fails: with D02 gone a solver lists the same four from D04's own columns | not offered (D02 not needed) |
| h18 | Savings clauses D01 L86, D02 L284, D04 L143 | goods on the dock, or shipped with no order, on each effective date | rule that differs between look-alike clauses | carrying one clause's terms into another | "on dock" outside the newer clause is a literal reading with a purposive rival; "actual orders" is a condition the question would have to name | not offered (two readings, or a pointed plain rule) |
| h19 | D06 L65-70 UAE in A:5; D01 L425, L467, L569 STA exclusions by Country Group | which 2023 STA exclusions reach an approved UAE agency | rule applied to an instance | A:6-only exclusions | 2023 entry text applied to 2026 status; one-of-three answer | not offered |
| h20 | D06 L74-77, L191-203 and Note 1 (L200-201) | which UAE-based companies may use License Exception STA | mentions it vs does it | G42, Core42 | Note 1 reads against the Authorization column: two readings | not offered |
| h21 | D02 L343-349 (what Sec. Sec. 744.2, 744.3, 744.4, 744.21 cover); D04 rows citing them (Nanjing Colpak, AHD International, Intertech Rus; Biopharmist and eight Russia rows) | decode an entry's review standard or status from the section its row cites | short references | rows citing more or fewer sections | the key is standing regulation text a solver knows without D02 | not offered (D02 not needed) |

Shared-ground summary: cross-document facts that a solver cannot recall sit in D04 (table detail, September
2025), D05 and D06 (2026). D01-D03 mostly restate standing regulation text, so a design whose second document
only supplies such text fails the removal test. D05 links to nothing.

## Round 3 (2026-10-14, caller): looking for a step the high model has not cleared

Both difficulty runs went straight to the high model (Low — · Medium — · High 3/3 twice), so the open tier
now looks to be Hard only. The high model cleared, three times in three each run, a road-name join between
two long flattened tables, a spelling variant ("Feila" / "Fei La") and a road split by the table's
interleaved columns ("177 Bi 2B350.d, 2B350.g, Bo Road"). Searched again for a fair hook with a step of
another kind (a rule carried across look-alike provisions, a member outside a complete-looking set in
another document, a derived figure beside printed look-alikes):

| Hook | Idea | Why not offered |
| --- | --- | --- |
| h14 corrections only (page's item 1) | Hexin Xingtong alone, or added and corrected asked apart | the same join, failed twice at the high level; a third wording of a closed hook |
| h22 | added entities listed only for a risk, not for an act (D04: three biotech firms, four NetForward firms) | one document; no second document carries any part of it |
| h23 | entries carrying footnote 3 in D04's table (14) against the two the preamble names | one document; a filter from D02 (Russia, Belarus) is guessable without it |
| h24 | cost per burden hour implied by D06 ($950 for 25 hours or 50 applications) applied to D02's added applications | three defensible routes ($380, $374.93, $378.72); the burden family was quick-test too easy on these bytes |
| h25 | corrected entries already listed while D01's temporary general licence ran | a date filter; AHD International's first-added date differs between D04's preamble (2018) and table (2023) |
| h26 | whether a UAE data-centre operator could still get a Data Center VEU after July 2026 | yes or no; D06 states the continuing licence requirement outright |
| h27 | an STA shipment to an approved UAE entity with a blocked or listed purchaser | yes or no; D02 and D06 each state their rule outright |
| h28 | named UAE companies in D04 and D06, as a total (printed 2 and "two", MGX in prose) | the i01 family (quick-test too easy); "G42 Cloud Technology LLC" makes the count 5 or 6 |

Result: no fair design found whose step is of a kind the high model has not cleared. The untested i02
and i03 need fewer steps than i04, which the high model solved.
