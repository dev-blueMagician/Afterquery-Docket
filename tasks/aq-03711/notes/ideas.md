# aq-03711 - lean candidate sketches

Current target: medium (hard welcome); the user states there is no Easy slot. Measured platform result: two
quick tests, both too easy (q01, i11; user chat 2026-10-13, no panels). No difficulty run spent. Sketch round 1
of 3 used. Origin of every sketch: claude. Hooks are in notes/hooks.md.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md); written up as questions/q01.md | h1 | Ambiguity: 74 (every site) and 35 (villages) fail the condition that Bupa itself owes the duty: it supplies no landline in its villages (D04 L47), and care homes are health care services (D06 L570). "Fell under the Code" was open (a village is still under the Code through the resident's own retailer), so the wording asks where "Bupa itself" owed duties. Necessity: D04 alone has the counts and the supply facts; D06 or D05 the final exclusion. | promoted to q01 rev 0 (floor 0 FAIL, 1 WARN origin). Quick test 2026-10-13 (user chat): too easy. Dropped; no repair (questions/q01.md, Outcome) |
| i03 | this file, below | h2 | Ambiguity: "3 months" counted from commencement (1 October 2024) fails "following the publication" (D08 L37). Necessity: D08 or D04 for the clause; D05 or D06 for the dates. Every input is also in the bundle overview. | quick test survived 2026-10-13; promoted to q02 rev 0 (floor 0 FAIL, 1 WARN origin) |

## i01 wording notes

- Tested wording (q01 rev 0, 30 words): "At how many of its retirement villages and care homes did Bupa itself owe
  111 Contact Code duties on the Commission's preliminary view, and how many under its final decision?"
- Gold: 39 (preliminary view) and none (final decision).
- One-reading repair held in reserve, to be used only if the form's "One defensible answer" check returns a
  different count for either part: open with the evidence named by its source, "On Bupa's own account of where
  it supplies landlines, ...". It adds no counting clause.
- Words a paraphrase must keep: "Bupa itself", "retirement villages and care homes", "preliminary view",
  "final decision", and both asks in that order.

## i03 (spare)

- Question: "Had the draft Code's own commencement clause been kept, how many days later than they did would the
  amendments have come into force?"
- Gold: 87 days (26 September 2024 against 1 July 2024).
- Inputs: D08 L37 "This Amended Code comes into force on a date that is 3 months following the publication of the
  Amended Code." (= D04 L92); D05 L13 "Date of publication: 26 June 2024"; D05 L20 "which comes into force on
  1 July 2024".
- Careless route: three months from 1 July 2024 gives 1 October 2024, 92 days.
- Script check 2026-10-12: 26 June + 3 months = 26 September 2024; minus 1 July 2024 = 87 days.

## Independent author runs (2026-10-12)

Two question-author agents, briefed with the hooks already held so that they would look elsewhere: one on the
nine party submissions, one on the Code's three states and the Request for Views.

### Run 2 (Code states and Request for Views), returned

Finding: every "rule changed between states" design collapses to D06 alone, because D06 restates the 2020 rule,
the draft decision and the final rule for each amended topic. Two date sketches, both resting on process facts
only D02 or D01 print. The author itself calls their shape plain (two lookups and a date count).

- i21 (h13), spare. Question: "The provisional timetable published in May 2023 for reviewing New Zealand's 111
  Contact Code gave a month later that year for the final decision. How many days after that month's last day
  was the final decision actually published?" Gold: 239 days (31 October 2023 to 26 June 2024; caller's script
  2026-10-12 agrees). Necessary: Doc 1; Doc 3 or Doc 14. Competing answers and the condition each fails: 270
  (September is the cross-submissions row, D02 L139); 244 (in force 1 July 2024, not "published"); 300 (draft
  row); 238 (2024 is a leap year). Open point: 239 is also the section of the Act cited throughout.
- i22 (h14), held, not offered. "How many more days after publication did the public have to make submissions
  on the draft decision than on the opening request for views?" Gold: 45 days (74 against 29). Both deadlines
  can be guessed from the submission dates D06's footnotes print, so Doc 2 may be reported as not needed.
- Searched and rejected by that run (all confirm hooks.md): section-letter change, 36-month date, counts across
  states, TCF mark-up outcomes, disclosure-year joins, record retention, the 10 February 2021 deadline, Spark's
  four-hour unit against outage shares, copper connections, Attachment A scenarios.

### Run 1 (party submissions), returned

Finding: one submission-based design beyond the held hooks meets the two-document test; no second one. The
near-misses it lists (rental months, letter dates, Age Concern against Grey Power, care-type lists, the cyclone
customer, copper against One NZ's ten years, rules applied to described cases, proposals against outcomes,
clause-number editions) all match hooks.md or fail because D01 Appendix B already quotes the submission.

- i11 (h15), spare. Question (42 words as returned): "Valuing each battery back-up at the GST-inclusive retail
  price Spark quoted, how many dollars higher or lower was battery cost per appropriate means supplied (of any
  kind) in 2022 than in 2021, on the battery shares the Commission reported for those years?" Gold: $111.93
  higher ((15% - 8%) x $1,599; caller's script 2026-10-12 agrees). Inputs: D01 L750 (8% and 15%, only there);
  D11 L92 ($1,599, only there). The Commission links the two itself: D01 L732 and fn 72 (L742) cite Spark's
  price paragraph, and L749-750 answers the cost concern with the battery shares. Careless routes: mobile
  shares (D01 L767) $47.97; WISPANZ's $1000.00 (D14 L80 = D01 L1323) $70.00; half-price unit $55.965.
  Open points, the author's and mine: the valuation is posed (industry shares at one retailer's retail quote),
  so a reviewer could call the product unconnected; the wording states its own method, the kind of cue that
  measured too easy on sister bundles; a share from one document applied to another's amount is a family the
  easier solver has handled; the shares sit about 71,000 characters into Doc 2 (check the form's number flags
  at write-up).

## Outcome of round 1 (2026-10-13)

| Sketch | Mechanism | Quick test | Decision |
| --- | --- | --- | --- |
| q01 / i01 | rule applied to one operator's stated facts, preliminary view against final decision, two asks | too easy (user chat; wording taken to be the hand-over) | dropped; h1 closed |
| i11 | share from one document times a price from another, two-year difference | too easy (user pasted the tested wording and "$111.93 higher") | dropped; h15 closed |
| i21 | scheduled month against actual publication, days | result not stated (the user reported only that the last sketch survived) | not pursued |
| i03 | draft commencement clause against grace period, date and days | survived (user chat 2026-10-13: "last one survived"; wording taken to be the sketch as offered) | written up as questions/q02.md rev 0 |
| i22 | difference of two submission windows | not tested | held (a ticked document may be reported as not needed) |

Round-2 search by the caller (2026-10-13), nothing sketched:
- Cost-bearers proposed besides retailers (Chorus and local fibre companies; the Government; "'nonstandard'
  customers", D11 L111 only, absent from D01): a list with one member outside the Commission's summary, but its
  membership is open at two edges (businesses providing their own backup, D14 L90-94; "the industry" through a
  funding model, D11 L108, D13 L52-53). More than one defensible list.
- Equipment suggested for people outside the scheme (D11 L24: battery backup, mobile, medical alarm; D13 L20:
  battery backup, mobile, satellite phones, generator) minus the means clause 25 of the 2024 Code lists: the
  match rests on calling a battery backup an uninterruptable power supply by function while refusing a
  generator the same, which the documents do not settle.
- TCF members with their own submission in each round (4 and 1): exact-name tabulation over printed lists.
- Total or difference of the two submission windows, and other date sums: date-count family; inclusive and
  elapsed counting give different totals.
- Complement of q01 (sites with no duties, 74) and Bupa plus Ryman totals: the reasoning the easier solver has
  already done; Ryman's "in situations where Ryman on-sells" gives no count.
No fair design with a mechanism outside the two tested families and the date-count family was found by the
caller or by either independent author run.

## After the quick tests of the spares (2026-10-13)

i03 survived and is q02 rev 0, tested_sha256 e9c7bf46.... The earlier note that date counts had not held on
sister bundles was history for that family, not a result for this sketch; the survival is a first screen and
sets no tier. Next: form Checks ("One defensible answer" and the necessary-documents check first), one
difficulty run, then read every attempt in the saved page before naming any route.
One-reading repair held in reserve for q02, to be used only if "One defensible answer" returns 18 March 2024:
name the publication structurally, "counted from the publication of the Code those amendments were made by",
and change nothing else.

## q02 rev 1 (2026-10-13)

Form Checks on the user's own-words version of rev 0: "One defensible answer" Failed, both solvers "18 March
2024, 289 days before the grace period ended" (three months counted from the draft's own cover date). That is the
reading rev 0 left open; the quick-test survival was measured on the same open wording, so it does not carry over.
Rev 1 (tested_sha256 73468c0f...): "Had the final 111 Contact Code amendments kept their draft's rule on when they
start, on what date would they have come into force, and how many days before the grace period ended is that?"
Gold unchanged. Two context quotes removed after the advisory "Evidence supports its component".
Still in reserve, to be used only if "One defensible answer" again returns 18 March 2024: say whose publication
outright ("counted from the day the final amendments were published"). Not offered now: it tells the solver which
date to start from.
Observed so far: both form solvers found the clause, added three months and counted the days correctly from the
date they chose. Nothing observed yet separates solvers once the starting date has one reading.

## Outcome after q02 rev 1 (2026-10-13)

User chat: "too easy for quick teset" on rev 1. q02 dropped, h2 closed; no difficulty run spent on this bundle.

| Sketch | Result | State |
| --- | --- | --- |
| q01 (Bupa sites, two views) | quick test too easy | dropped |
| i11 (battery cost per means) | quick test too easy | dropped |
| i21 (239 days) | taken as not surviving: the user reported only that the last of the two spares survived and did not correct that reading | closed |
| q02 rev 0 (draft commencement rule, open starting date) | quick test survived; form "One defensible answer" Failed, both solvers on 18 March 2024 and 289 days | superseded |
| q02 rev 1 (starting date given one reading) | quick test too easy | dropped |
| i22 (45 days between the two submission windows) | not offered | not a fair sketch: the draft round's deadline can be inferred from the submission dates the final paper prints, so a ticked document would not be needed |

Every sketch that met the two-document test has a result. What held solvers on this bundle was one open
reading, not a step of reasoning. Families measured on these bytes: a rule applied to stated facts, a share
times a price, a date derived from a rule and counted. Nothing else that the caller or the two author runs
found meets the two-document test with one defensible answer (hooks.md).
