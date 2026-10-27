# aq-02405 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Local ids: D01 = page Doc 1, D02 = page Doc 3, D03 = page Doc 2, D04 = page Doc 4, D05 = page Doc 5,
D06 = page Doc 6 (notes/intake.json). Lnnn = line in text/Dnn.txt. Author: claude (Opus 5.5), 2026-10-09.
Target: medium (user: "no slot for Easy Tier ... target medium and high").

Bundle character: six DOJ proposed rules. Almost every printed number is internal to one rule's own
analysis; cross-document numbers are either identical reprints (leisure wage $1,214/$30.35/.86/$26.10/$26
in D02, D04, D06), different-scope counts (licensees 50,588 / ~130,000 / ~80,000 / 45,605 / 77,378), or
unconnected. The real cross-document links are (a) two proposals cutting burdens on the same NFA
applicant (D02 CLEO copy, D06 prints/photos), (b) D04's amendatory instructions written against D05's
rewritten 27 CFR 478.96 and 478.124, (c) one statute (Public Law 117-103) named differently in D01/D05,
(d) D05's state list vs D03's cited state statutes. D06 Tables 1-15 are omitted graphics (gap).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D06 L200 "$18" one card instead of two, L220 "$17" photo, L253 "up to 0.25 hours" photo time for NFA individual paper filers, L257 "$42 (rounded)"; D02 L141 "15 minutes (0.25 hours) for an individual to copy the relevant form", L165 "$7 (rounded)"; wage $26.10 (D02 L159-160, D04 L302, D06 L239) | Combined per-application savings of the 2026 proposals for one applicant type (individual, paper Form 1) = cash + time at a stated wage | Scatter the pieces; Calculate across documents; State the rounding | Wrong routes: D06 alone $41.53; printed sum $42+$7 = $49; $26 wage $48.00; PRA 18 min $49.36; RP route $106.15 (all recomputed, i01_calc) | Photo saving is optional; PRA 30->12 min is eForm+rule mixed (paper filer excluded); RP per-application CLEO model ambiguous, so use an individual | sketch i01 |
| h2 | D05 L470-506 rewritten 478.96: (a) applicability, (b) NOTC, (c) law enforcement notice with (c)(4) "at least seven days" (L498), (d) out-of-state; D04 L462-470 "Redesignating paragraphs (c) and (d) to (d) and (e)", new (c) (L476), "in paragraph (d)(4), redesignating the paragraph reference (c) as (d)" | Where the seven-day NOTC shipping delay sits once both proposals apply: 478.96(d)(4) | Same series, right edition (amendments in order) | Decoys: D05 printed (c)(4); D04 new (c)(4) NICS wait (not seven days); current 478.96(b) (D04 L68); D05 L536 state seven-day waiting period sits in 478.102(c) | Answer is a regulation paragraph (rule 10 allows regulations); D04 preamble/reg sworn-statement wording inconsistent, avoid that topic | sketch i02 |
| h3 | D05 L211 NDNA "Public Law 117-103" added county/city-limits item; D01 fn16 L137-138 same law "amended 18 U.S.C. 922(t) to reference firearm prohibitions imposed by local and Tribal governments" | Which governments' prohibitions the law behind the city-limits question added: local and Tribal | Linking across documents; mentions vs does | Decoy: D05's notification recipients "state, local, or tribal" | Platform suggested this ID join (originality risk); ID search finds it fast | hold |
| h4 | D05 fn13 L316 nineteen jurisdictions barring transfer on an open check after three business days; D03 L97-98 exemption examples Fla. Stat., Del. Code Ann., Md. Pub. Safety Code; fn6 L83 Florida | Delaware, Florida, Maryland | Match then exclude; entity resolution (Del./Md. abbreviations) | Decoys Alabama, Alaska, Michigan (named in D03, not in D05 list) | "cite as" framing near rule 10; examples are "e.g." so left-out states cannot be proven non-exempting | hold |
| h5 | D01 L329 FHC Form 5300.47 anticipated; D05 L196, L609 FHCs on Form 4473 with a box, kept 90 days | Form planned for handler checks changed 5300.47 -> 4473 | Same series, right edition | D01 decoy | Answer single-source once "2026" is named | reject |
| h6 | D01 L574-576 audit-log retention (110 years, <=90 days, 24 hours); D05 L188, L196 Form 4473 retention (90 days; denied 5 years) | Retention gaps | Calculate across documents | 90-day vs 5-year | Two lookups and one subtraction | reject (too direct) |
| h7 | D01 L83 2021 NICS Section firearm transactions 11,106,931; D05 Table 2 L309 2021 delayed denials 3,671 | Delayed denials per 100,000 transactions, 2021 | Temporal alignment | D05 22.5 million decoy | Documents never connect the two counts; scope (FBI vs POC) unclear | reject |
| h8 | D02 L29 comment deadline July 6, 2026 = D06 L3 publication date; D06 L30 Oct 5, 2026 | Date gaps | Calculate across documents | none | D06 alone gives the same 91 days (substitute route) | reject |
| h9 | D04 L279 "approximately 90 percent" resolved; D05 L136 91 percent instant (2022-2024) | Counterfactual travel hours | Calculate across documents | n/a | D04's own rounding (2.95M) gives two golds (32,800 vs 30,800) | reject |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
