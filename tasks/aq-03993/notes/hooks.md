# aq-03993 - cross-document hooks

Target: medium, hard open too (user, 2026-10-13: "no slot for Easy Tier ... target medium and high").
No earlier capture on these bytes (repeat-bundle check, 2026-10-13: no match in 10.6, 10.7, 10.8). Same
family as aq-03950 (committee report plus hearing transcripts), which has no platform result yet. Family
evidence used instead: policy bundles with few connected figures gave six quick-test "too easy" calculation
designs on aq-03423 (two lookups and a subtraction, a ranking across two documents, a base backed out of a
rate); the designs that held the easier solver there and elsewhere needed a step the question does not
name: a part that only a second document separates from a headline total (aq-03120, aq-03557), or a rule
whose stated minimum is not the figure that binds the case (aq-02486, aq-02562).

Doc numbers are the task page's (Doc 1 = D04 report, Doc 2 = D01, Doc 3 = D02, Doc 4 = D03).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 1 para 41: Future News Pilot Fund "£2 million", "178 applications", "grants to 20 projects". Doc 4 Q254 (Floyd, who worked on the fund): "That was £2 million and about £1 million was grant funding". | Average grant per funded project: about £1 million / 20 = about £50,000. | Calculate across documents; Scatter the pieces | Headline fund divided by projects: £2 million / 20 = £100,000 (Doc 1 alone). | Both inputs sit past character 45,000 of their documents (form number check will show false alarms). "about £1 million" is approximate. A round gold: pair with a document-only second ask. | sketch i01, written up as q01 |
| h2 | Doc 3 Q176-224: Rhodri Talfan Davies answers Brennan, Huq, the Chair, Elliott and Jupp; Brine and Green question only Google and Meta. Doc 1 formal minutes: present on 17 January 2023 Brennan, Brine, Efford, Green, Huq, Jupp. | Which MPs who agreed the report had a question answered by the BBC's witness in Cardiff: Brennan, Huq, Jupp. | Mentions it vs does it; Match, then exclude | Brine greets "Rhodri, Tom and John" and Green picks up "that point", both in the BBC's panel, but neither gets an answer from Davies. Knight and Elliott were answered but did not agree the report. Skipping the exclusion gives five names. | Doc 3's Q222 answer is headed "Tom Morrison-Bell" though the BBC is speaking (Jupp's Q221, Q223, Q224 are headed correctly, so the list does not change). Formal-minutes names sit on short lines. | sketch i02 |
| h3 | Doc 3 Q222 (BBC): LDRS minimum salary £24,000, each role "benchmarked against a senior reporter on the same publication". Doc 3 Q161 (Higgerson): "impossible for you to pay less than what you are paying your existing seniors". Doc 3 Q143 and Doc 1 para 49: Reach senior minimum £25,000. Doc 1 para 33: Reach took 75 of the 165 reporters allocated in July 2021. | Least yearly salary bill for Reach's allocated reporters: 75 x £25,000 = £1,875,000. | Calculate across documents; apply a rule to a case | Scheme-wide minimum applied to Reach: 75 x £24,000 = £1,800,000. | Whether the benchmark binds is said by the BBC as an expectation and by Reach as a rule; a solver may defend £24,000. Allocation dated July 2021, salaries stated June 2022. | sketch i03 |
| h4 | Doc 1 formal minutes: Damian Green in the chair on 17 January 2023. Docs 2, 3: Green's numbered questions (15 and 14). Docs 2, 3, 4: the Chair's (14, 15, 8). | Numbered questions put by the MP who chaired the report meeting: 29 (lure 37, Julian Knight). | Who belongs where | Chair of the hearings taken for chair of the report meeting: 37. | A tally of question numbers: care alone solves it (aq-03423 q03, Between levels). Doc 4 only shows a zero. | hold |
| h5 | Doc 1 witness list: four sessions, Q1-331. Doc 3 header: "28 June 2022, Cardiff", "Questions 124 - 224". | Share of the inquiry's numbered questions asked in Cardiff: 101 / 331 = 30.5% (bundle transcripts only: 101 / 274 = 36.9%). | Bury one list item late | Fourth session listed only in the report. | Doc 1 alone gives both counts; Doc 3 only identifies the session. | rejected: one document carries the answer |
| h6 | Doc 2 Q108: Bristol's LDRs "are with the Reach plc publication". Doc 3 Q138: Bedford's "are managed by National World". Doc 1 para 33: Reach 75, JPI Media (now National World) 35.5. | Reporters allocated to those two publishers: 110.5. | Scatter the pieces; Entity resolution | none that changes the answer | Every step is a name match the question points at (solved family: aq-02408, aq-01433). | rejected |
| h7 | Doc 2 Q63: public notices "about £40 million" (NMA). Doc 2 Q119-122: Heawood reports the NMA figure as "£250 million". Doc 1 para 51: IMPRESS, "around £50 million per year". | Gap between the report's figure and the NMA's own: £10 million. | Reconcile documents that disagree | Heawood's account taken for the NMA's figure: £200 million. | The NMA's own words are the first hit and the low solver trusts an own account (aq-03170). Two lookups and a subtraction. | rejected |
| h8 | Doc 3 header declarations (Jupp, Chair, Green; Brennan at Q125: hospitality), Doc 4 (Chair, Nicolson), Doc 1 formal minutes. | MPs who agreed the report and had declared past work for the BBC: Green, Jupp. | Match, then exclude | Brennan's hospitality declaration; Knight and Nicolson absent on 17 January 2023. | Short lists side by side; set operations (solved family). | hold as a spare |
| h9 | Doc 2 Q69: TuneIn removed stations "the day the White Paper was released". Doc 1 footnotes 205, 227: "Up next", 28 April 2022. | Date of the removal, or days before the hearing (19). | Period identified by an event | Queen's Speech of 10 May 2022; the 2020 planning White Paper | Date count (solved family); a number under twenty. | rejected |
| h10 | Doc 1 PINF arithmetic (£1.30 a month, £250,000); Doc 2 Bristol Cable (2,800 members, £3.50); Doc 4 Barnet (2,000 people, £5). | What-if ratios between them. | Calculate across documents | none | Figures the documents never connect (Guide, common mistakes). | rejected |

| h11 | Doc 3 Q138, Q157 (Higgerson: Reach "spends more on delivering the LDRS scheme than it receives", "we have the Teesside contract"). Doc 4 Q257 (Breslin: "we support our LDRs, our political editor manages them"). Doc 4 Q255 (Floyd: "the Local Democracy Reporter scheme funds posts—we have two of them"). | Which witnesses worked for an organisation with local democracy reporters on its own staff: Breslin, Floyd, Higgerson. | Mentions it vs does it; Who belongs where | Hutchinson ("We are part of the LDRS", "our LDRS reporters ... managed by National World"); Davies (BBC funds, "employed by local commercial operators"); Abbott, Powell, Meredith (bodies whose members employ them); Hancock, Cantwell-Corn (access only). | Exact three-name set. Powell is the weakest exclusion. Doc 2 holds decoys only and is not ticked. | sketch i04 (added after q01's two runs) |

Measured on h1 (2026-10-13, q01 rev 0 and rev 1, nothing named): "Between levels" twice, Low 0/5 · Medium 1/7 ·
High 3/3 and Low 0/5 · Medium 0/6 · High 3/3. Every recorded wrong attempt answered £100,000 from Doc 1; one
medium attempt in thirteen opened Doc 4. As posed the hook sits between Medium and Hard. Its one untried fair
wording names the evidence by its structure (sketch i05, quick test first).

Measured on h11 (2026-10-13, q02 rev 0, the three names): "Between levels", Low 0/5 · Medium 4/7. Every wrong
attempt omitted Floyd; no medium attempt took a look-alike. Rev 1 asks for the total (Reach 75 in Doc 1 plus
Social Spider 2 in Doc 4 = 77), so the report's own figure is the complete-looking answer.
Measured on h11, total form (2026-10-13, q02 rev 1, Run 4): "In band — Medium tier", Low — · Medium 2/6. Both
recorded wrong answers were 75 and neither attempt found Floyd's clause; both right attempts quoted it. With
Doc 4 left out the strongest solver answered 75 twice, with Doc 1 left out 2 twice. Submitted at Medium.
Routes: feedback-q02.md. For the next task on these bytes: three ways of asking for one unprompted look in a
second document gave three results here (h1, nothing named: Medium 1/13, High 6/6; h11 as a list: Medium 4/7;
h11 as a total against a complete-looking printed figure: Medium 2/6). The same look-alikes were set aside by
every recorded medium attempt in both h11 runs.

Calculation hooks h6, h7, h9 and h10 are closed for the reason in the first paragraph. h1 and h3 are the two
places where a second passage changes a number a single passage seems to settle; h2 is the same idea for a
list of people, and the form lists "who took part in an event" among the shapes it is short of.
