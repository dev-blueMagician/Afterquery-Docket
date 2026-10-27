# aq-01540 - cross-document hooks

Find facts that combine into a world answer before drafting wording. Record sources/locations,
input quantities and units/periods, the relationship, a possible ask and one or two selected levers.
Explore forecast/actual, proposal/final dates, changed/conflicting tables, amendments, hedge scope,
mentions/actions, entity/edition joins, ordered/late items, exclusions and ordinary cross-document
calculations. Find more viable hooks than questions requested without inventing a quota.

Target: medium (task page 2026-10-07: "Still open on this set: Medium."; "Easy and Hard questions are full
on this set"; slots "Hard 1/2 · Medium 1/3 · Easy 2/1", "In review: Hard 1"; 4 submissions left).
Ids: D01 = Doc 6, D02 = Doc 8, D03 = Doc 7, D04 = Doc 5, D05 = Doc 2, D06 = Doc 4, D07 = Doc 1, D08 = Doc 3.
Caller hooks written 2026-10-08 after the caller's own full read of D01-D08 (not the mapper's).

Bundle character: eight unrelated federal opinions (Sept 11-15, 2026). No shared parties, no cross-citations
between the eight cases. Cross-document links are doctrinal only: FNC decided (D04 granted, D07 denied), FNC
raised but not reached (D03), FNC waived (D05), FNC precedent mentions (D01 Gulf Oil, D02 Azima, D08 Chick Kam
Choo); FSIA (D02, D03, same court and day); personal jurisdiction (D02, D07); insurance (D01, D06); forum
clauses (D04, D06, D08 background); maritime law (D04, D06); forfeiture (D01, D03). Every disposition is
printed in its own ruling, so plain disposition filters are keyword lookups (trial-05 lesson).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D04 l.15, l.121-123 (RCCL's forum-clause FNC motion GRANTED, England and Wales); D08 l.42 (JLF Defendants moved to transfer "based on certain provisions within their engagement agreement with Moreno"; D.R.I. granted; case assigned to N.D. Tex. May 3, 2023), l.21 (JLF = Steven Johnson and his law firm) | Defendants that got a federal court to dismiss or transfer the lawsuit away from its court by invoking contract terms: Royal Caribbean and the JLF Defendants | Bury one list item late; Mentions it vs does it | DUAL/Chaucer/Houston (D06 l.14, l.173, l.260: forum-clause transfer DENIED); OEC (D07 l.225, l.451: FNC DENIED, no forum clause); Ofcom (D03 l.97: FNC not reached); JLF arbitration request (D08 l.172 DENIED); JLF removal (D08 l.42, diversity, not a court order). Wrong answers: "Royal Caribbean" only; "Royal Caribbean and DUAL" | late-item questions measured Easy before (aq-01433 Low 2/5); form "too vague" risk if both form solvers omit JLF; cited precedents (Turner, Lebedinsky, Aviation One, Azima) also won forum-clause/FNC dismissals, so scope to the eight disputes' own defendants | sketch i01 |
| h2 | D06 l.86 ("The parties agree that New York law governs this contract dispute"), l.188 (parties assert Kansas law), l.191 (court analyzes breach claim under federal maritime common law); D07 l.60 (Delaware clause), l.344-352 (court applies Ohio law, no conflict) | Law each court applied to the breach-of-contract claim: federal maritime common law (Kansas), Ohio law (Ohio) | Who belongs where (two laws in one ruling); two parallel asks | NY or Kansas law (D06), Delaware law (D07) | each gold sits in its own breach section (tied); two parallel lookups may read as stapled | park (two-ask fallback) |
| h3 | D06 l.84-88 (meaning of "issued" construed under New York law), l.191 (maritime law for the breach claim); D04 l.58 (forum clause validity "Under federal maritime law"), l.106 (ticket contract designates English law) | Law each court used for the forum-clause question: New York law (Kansas), federal maritime law (Florida) | Who belongs where; swap trap (each contract designates the law the other court used) | maritime (D06), English (D04) | explicit in each forum section; two parallel asks | park |
| h4 | D02 l.98-115 (five counts, all naming the UAE); D03 l.243 fn 4 ("listing four counts"), l.95 (body lists six-seven theories) | Counts pleaded in the two suits the D.C. court dismissed on FSIA grounds on Sept 15, 2026: 9 | Bury one item in a footnote; Aggregation | 3+4, 5+6, 5+7 from body theories | counting counts is trivia; sum across unrelated suits contrived | reject (trivia) |
| h5 | D02 l.39, l.564 (UAE immune, FSIA), fn 6 l.107 (U.S. suggestion of immunity for MBZ; court's show-cause order; MBZ dropped); D03 l.250 (Ofcom, FSIA) | Defendants held immune or formally suggested immune by the U.S.: UAE, MBZ, Ofcom | Bury one list item late | Matar al-Neyadi and ADNOC (dropped, no immunity statement) | needs an OR-condition that points at the buried item; "treated as immune" ambiguous for MBZ | reject (two readings) |
| h6 | D03 l.208-217 (jurisdictional discovery denied as futile); D07 fn 6 l.206-219 (ATP's request DENIED); D01 l.99 (remanded FOR jurisdictional discovery) | Plaintiffs refused jurisdictional discovery: 4chan, Lolcow, ATP | Bury one item in a footnote | Megalomedia/Philadelphia (granted on remand) | the concept's own term finds all three passages; omission-only trap | reject (keyword lookup) |
| h7 | D04 l.98 (England and Wales adequate); D07 l.225 ("Although India may be an alternative forum"), l.240 ("carried its burden to provide an adequate alternative forum") | Foreign forums held adequate: England and Wales, India | Does the hedge apply? | India excluded because FNC was denied or the summary hedges | "adequate alternative forum" printed in both findings | reject (keyword lookup) |
| h8 | D01 l.132 and D03 l.140 (arguments forfeited) | Parties held to have forfeited an argument: Megalomedia; 4chan and Lolcow | Mentions it vs does it | Bagga (D04 fn 1, fn 2: abandoned/not argued, not called forfeiture), ATP (D07 fn 7) | "forfeit" printed in both holdings; Bagga membership arguable | reject |
| h9 | D04 l.58 and D06 l.191 (federal maritime law) | Disputes decided under federal maritime law | Mentions it vs does it | D06 l.86 NY law; D01 l.52 "inland marine coverage" | keyword "maritime" | reject |
| h10 | D02 l.564 (six defendants dismissed for lack of PJ) + D07 l.449 (OEC USA) | 7 defendants dismissed for lack of personal jurisdiction | Aggregation | "Alp defendants" counted once (2) | explicit lists; Low 5/5 profile | reject |
| h11 | D02 filing Jan 24, 2024; D03 filing Aug 27, 2025; both dismissed Sept 15, 2026 | Difference in pendency: 581 days | Calculate across documents | amended complaint Aug 6, 2024 | plainly dated bridge (aq-00998 q03 Too easy) | reject |
| h12 | D08 Chick Kam Choo rule (l.81) applied to D04's FNC dismissal | Relitigation exception unavailable after an FNC dismissal | Apply a rule to a case | none | general legal knowledge: closed-book reach; yes/no | reject |
| h13 | D02 l.515 (PJ over Vidino, dismissed on 12(b)(6)) + D07 l.182 (PJ over OEC India) | Defendant each court held within PJ: Vidino, OEC India | Mentions it vs does it | "none" for D02 (all dismissed) | two parallel lookups; joint low-model odds high | park |
| h14 | D07 l.453-455 (Counts I, III, V, VII capped; II, IV, VI, VIII uncapped; IX dismissed) | Counts surviving with no price-paid cap | Match then exclude | I-VIII (ignoring cap); I, III, V, VII | single document; no natural second-document partner | reject (one source) |
| h15 | D05 l.136 (injunction "Effective as of May 18, 2026") vs order Sept 11, 2026 | Injunction start date | Superseded date | Sept 11, 2026 | single document; cross-case date arithmetic contrived | reject (one source) |
| h16 | D03 l.73-76 (£20,000 plus £100/day up to 60 days = £26,000) vs £18 million threat (l.66, l.179) | Most 4chan could owe under the provisional notice | Figure that must be computed | £18 million; £20,100 | single document | reject (one source) |

Other numeric routes examined and rejected as manufactured cross-case arithmetic (no document connects the
figures): D07 $5.8M/$370,000, D06 $245,721.72 vs $300,000/$50,000 (one vs two occurrences also unresolved),
D08 $1,000,000 vs $135,000, D04 Lebedinsky $750,000 vs $64,000, D02 $150M valuation, Vidino $2,000-$4,000 and
EUR 3,000, D03 20 million visitors and 7%. Internal date conflicts (D08 March 3 vs March 4, 2024 and "Texas
arbitration of 2024"; D02 New Yorker 2024 text vs Mar. 27, 2023 footnote) are source inconsistencies to avoid.

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
