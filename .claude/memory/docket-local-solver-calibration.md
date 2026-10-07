---
name: docket-local-solver-calibration
description: "The local Opus 5.5 blind solver beats every lever tried so far (numeric and qualitative) and checks prose against tables; it is the fairness check, not the difficulty target (the platform's reviewer model is); a local 'solved' means fair, and too-easy risk is read from its path. First platform pass (aq-00964 q01, Medium tier): an event reported in the latest release whose own later forecast is the decoy."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-04
  originSessionId: 0b3fd638-83b1-473b-8a9e-6c645eb2ec12
  modified: 2026-10-07T08:32:27.906Z
---

## Current rule

- Role (the user, 2026-10-04: "the high model is not the claude model. it's the Docket platform
  reviewer model"): the local blind solver is the fairness check, not the difficulty target.
  Its `match` shows the documents settle the key. Its path is the difficulty evidence, read
  against the gate's D1-D7 and the "too easy" signals below. See [[docket-maximum-difficulty]].
- Expect the local blind solver to solve fair numeric sketches. It finds dates scattered across
  documents, reads flattened chart tables, recomputes by hand, checks the prose against the
  table, and names the decoys in its readings.
- For a local miss, reach for the guide's qualitative levers (mentions it vs does it, does the
  hedge apply, match then exclude) where the bundle supports them across documents.
- When the bundle has no cross-document lists or hedges, for example independent articles
  joined only by shared dates and series, stop after two sketch rounds. Write up the strongest
  fair sketches by gate quality: a decoy that changes the answer, each document holding a unique
  fact, the lowest ambiguity. Tell the user the platform's quick test, which runs an easier
  solver, is the real screen. A local "solved" means "fair", not "too easy for the platform".
- Exception, from the first platform verdict: a solved sketch whose path is only lookups is "too
  easy". This means every fact is one plainly stated sentence, the lever is labelled in the text
  ("we treat X as our main analysis"), and one obvious calculation follows. The platform reviewer
  returned such a question: "too easy: it can be answered without careful work across the
  documents". Among solved sketches, write up one whose path needs close reading. That means a
  bridge, where a fact in one document decides which fact to take from another. It also means
  facts that must be put together from two passages (an appendix number, a flattened figure
  label read against the prose), and a decoy a quick reader takes.
- Two more "too easy" signals, from aq-docket-trial-07 q01. (1) The bridge is common knowledge.
  Official recession dates are an example: a model supplies them without the bridging document.
  (2) A passage names the answer's items, even for a different but overlapping period. The rail
  article's prose named the top two of the three groups by share of losses over 2018-20, so
  only the third place was left to compute. Before write-up, check that the bridge fact is only
  in the bundle. Also check that no narrative sentence ranks, lists or highlights the answer's
  items.
- A third signal, from aq-docket-trial-02 q01: labelled figures plus one standard
  transformation are too easy, even with a trap that flips the sign. Year-to-date to quarter
  is an example: nine months minus six months, in four releases. The low model knows the
  transformation and runs it. Close reading has to come from the documents (a bridge, a
  footnote that changes what a figure covers), not from arithmetic the solver already knows.
  Wording: when the documents report year-to-date, say "three months ended". The Coach flagged
  "quarter ended September 30" as open to a year-to-date reading.
- A segment-recast trap is too easy when the pin it needs points at the recast. Naming the
  restatement was "Too easy" in two quick tests (aq-docket-trial-02 q04). Quoting the release's own
  restated comparison as the premise did the same (aq-01333 q02, difficulty check "Too easy", Low 4/5).
  The question said "On that same segment structure", and the low model followed it to the release
  that prints the restated figure, the recast note and the recast column. Only 1 of 5 attempts took
  the printed old-basis decoy. Without the pin the old-basis figure becomes a defensible answer.
  So when the recast is stated plainly in the release that holds the needed columns, this mechanism
  has no fair Medium form; use an event-to-edition bridge instead. One measured result per wording.
- The platform's bars, from the Question Coach (2026-10-04, shared by the user in
  aq-docket-trial-02). The quick test runs only the low model, so "survived" is the minimum bar.
  The maximum bar is a question where one or two evidence-based levers make even the high model
  struggle. The three the guide marks most effective are mentions it vs does it, does the hedge
  apply, and match then exclude. Stacking three or more conditions does not raise the bar: it
  makes a rulebook, which the guide rejects ("hard to reason through, not hard to parse").
  Name the lever each write-up rests on, and reach for one of the three first.

- A fourth signal, from aq-docket-trial-07 q05 (platform quick test, low model solved it): values
  that are single readable cells in exhaustive data tables are lookups, even when they sit in two
  documents and a chart extreme decides which cell to read. A prose decoy that the question's
  wording sidesteps ("highest level" leads straight to the table maximum) is no decoy. The
  Coach: "no prose to parse, no rounding to reconcile, no decoy to trip on". Its suggested
  levers: an exact table figure set against a visibly approximate prose figure, and pieces
  scattered so no single passage has the answer.
- A fifth signal, from aq-00745 q01 (platform quick test, low model 5/5): a filter whose
  qualifying property is printed per item with a direction word is a keyword filter, even when
  the question paraphrases it. The question asked which quarters' resolutions of prior-year tax
  positions "increase[d] Abbott's taxes"; each quarter's own footnote says "net tax expense" or
  "net tax benefit". The Coach: "a simple keyword match for 'tax expense' ... surfaces the two
  correct quarters immediately." Paraphrase defeats exact-token search (rule 3), not a search for
  the concept. Year-to-date totals and look-alike items that the question's own unit word rules
  out ("calendar quarters") are not decoys either. Ask for something no item's own passage
  states.
- First platform pass, aq-00964 q01 (difficulty check 2026-10-05: "In band — Medium tier",
  Low 0/5, Medium 1/5): an edition bridge with three parts. (1) The bridging event (a subsidiary
  sale on June 15, 2026) is reported only in the latest release. (2) That release prints its own
  outlook, dated after the event (July 28), with a different value: a decoy in the same
  document. (3) The value current at the event sits in the previous, middle edition (April 28).
  All nine wrong platform attempts took the same-document post-event outlook ($1,630M vs the gold
  $1,605M). Locally, both Opus solves and the auditor matched with high confidence and review
  rated it "easy (marginal)", so the local path underestimated it. Where a bundle holds dated
  forecast editions, look for an event reported in a later edition whose own forecast postdates
  it and differs. One result: evidence for this mechanism, not a model capability claim.
- Platform gate wording (difficulty check page, seen 2026-10-06, aq-00998): "Ready when 1–3
  attempts at a level are right, out of up to 5. A level can settle early, for example at 1 right out
  of 3." So an Easy result needs the low model to miss at least two of five attempts; "5/5 right" is
  "Too easy". These are the page's own words for this run, not a hidden threshold we inferred.
- A plainly dated event bridge is crossed by the low model (aq-00998 q03 rev 1, Low 5/5): "in April
  2025" plus the question's "calendar quarter", then both inputs in one sentence of the next release.
  A same-label previous-quarter decoy in the event's own release caught no attempt. The aq-00964
  decoy worked because it was issued after the event and looked current; a decoy that predates a
  printed month does not. A quick-test pass (q03) did not predict the difficulty check.
- Decoys must survive the question's own wording (local reviews, aq-00998, 2026-10-05). Asking
  "how many points higher was A than B" told solvers which edition's figures fit: only the gold pair
  had A > B, so the wording defused a same-release decoy. When the decoy flips direction, ask
  direction-neutrally ("A minus B"). A "which of A or B" wording fails the form's giveaway block,
  because the answer name appears in the question. Reviews rated three other decoys weak: one ruled
  out by the exact line-item label (crude oil vs crude unit inputs), one by the question's own verbs
  ("signed", "20-year"), and an event that resolved to the bundle's latest quarter. In the one
  platform pass, the decoy carried the asked figure's own label and only timing ruled it out.
- A rule stated in one plain sentence and applied to labelled rows is a lookup path (aq-00949
  q03, Low 5/5). The 2020 plan's "Net cash from operating activities is expected to fund both
  capital expenditures and dividend payments" was applied to six quarters of the latest
  supplement. A free-cash-flow decoy sat in the same table and an acquisition decoy in the
  investing section, but every attempt quoted the rule sentence, read the matching row labels
  and added. Removing the question's cues (rev 1) changed nothing. When the target is chosen by
  applying a definition, the definition itself has to need close reading.
- Exact table vs rounded prose does not trap the low model when the exact figure sits beside the
  prose in the same document (aq-00949 q04).
  - Rev 2 reached the Easy window, Low 3/5 (user report). It asked "EOG's total debt at June 30,
    2026 was what percentage of its total debt at the end of 2019?" to one decimal.
  - The platform reviewer then returned that wording as ambiguous about which figure to divide by.
  - Rev 5 removed the ambiguity: "end-2019 debt divided by June 30, 2026 debt", two decimals. It was
    "Too easy", Low 5/5. Three of the five attempts quoted the rounded "total debt outstanding was
    $5.2 billion" sentence and still used the exact 5,175 from the table.
  - So the earlier Easy result most likely came from the parse ambiguity, which the guide rejects
    ("hard to parse"), not from the lever. A visibly rounded prose figure next to its own exact
    table is no trap. The rounding lever needs the exact figure to be somewhere a quick reader
    does not look: another document, or a component sum.
- Tier mechanics (platform difficulty check, aq-00745 q01, 2026-10-06): each level runs up to 5
  attempts and is "Ready when 1–3 attempts at a level are right"; Low 1-3/5 places the question in
  the Easy tier ("In band — Easy tier"), Low 0/5 moves on to Medium (Medium 1-3/5 = Medium tier,
  as aq-00964 q01: Low 0/5, Medium 1/5). A quick-test survival is not a Medium placement. A
  difficulty-check result is final for its version, and runs are budgeted ("6 of 8 runs left").
  A result can fall "Between levels" (aq-01431 q01 rev 0: Low 0/5 · Medium 4/5 · High —, "Too hard
  for the low model but too easy for the medium model. Make it a little harder, so the medium model
  reaches your answer only some of the time"): the gate does not pass. Low 0/5 with Medium 4-5/5
  means the trap works on the low model only; remove the cue the medium model followed, keeping
  the trap, rather than adding a second trap (which overshot to Too hard in aq-00745 q08).
- A printed grouped figure beside the runner-up's figure caught the low model even when the
  question's label matched the other letter's split figure exactly (aq-01431 q01 rev 0: 4 of 5 low
  attempts used Doc 7's "combined $4.8 trillion" for "climate change/carbon", one took the D12
  same-sentence neighbour). Local review had called the decoy disarmed by the label (Medium 6-8%);
  as with aq-00964 q01, aq-00745 q09 and aq-00998 q05, the local estimate was too pessimistic. The
  medium model followed the exact label and the "ranked second" cue (4/5). Removing the label
  entirely (rev 1, "largest single ESG issue") overshot: the task form's blocking "One defensible
  answer" check returned "This question is too vague to submit: two independent solvers ... Both
  answered "3.00 trillion dollars"" although "single" excluded the grouped figure. The form's check
  is a free screen: try each wording there before spending a difficulty run, and move the pointer
  in half steps (rev 2 kept rev 0's wording with "climate change" for "climate change/carbon").
- One same-document edition trap sits at the Easy/Medium border: aq-00745 q01 (range in force at
  the Exact closing vs the release's own post-closing range) drew Low 1/5, 4 wrong attempts all
  taking the post-closing range. Chaining a second date trap overshot (aq-00745 q08, "Too hard",
  Low 0/5 · Medium 0/5 · High 0/5): the closing-day trap caught Low 5/5 but Medium and High passed
  it 9/10, then 9/10 fell into the second anchor (a dividend's payment vs declaration date). So the
  closing trap alone is too easy for Medium (the release's "Updates Guidance to Reflect
  Acquisition" headline tips careful models off), and a second date trap is too hard. For Medium,
  use one same-document edition trap without such a tip-off, as in aq-00964 q01 (event reported in
  the release whose own later value is the decoy; Medium 1/5).
- Measured ladder on one bundle (aq-00745, same three FY2026 guidance editions, same July
  endpoint): event tied to the guidance change by the release's headline (the acquisition closing)
  -> Easy (Low 1/5); same layout with an event the release never ties to its guidance (FreeDM2
  results "In March", beside the release's own later range) -> High tier (user report, q09); two
  chained traps with an ambiguous second anchor -> Too hard. To land exactly Medium, start from the
  untied single trap and weaken it slightly (e.g. a date-explicit anchor), not from the tied one.
  Weakened too far (aq-01320 q01, user report "Easy Tier", tier line not supplied): an untied anchor
  that is a quarter boundary printed in the decoy release's own first sentence beside its release
  date ("March 19, 2026 ... third quarter ended February 22, 2026") makes the disarming check cost
  one sentence. Keep the anchor's date out of the decoy release's dateline, as aq-00964's body-text
  sale date was.
- Date anchors must survive rewording: q08's tested wording (reworded on the form) put "in June
  2026" next to "distributed", and the Coach called the question ambiguous (R4, R9c "PIN2"). Write
  anchors whose scope cannot move ("the range in force when ..."), and ask the user to paste the
  question verbatim.
- The anchor's verb sets how strong the trap is. It can also push the trap past the High tier.
  aq-01333 q01 rev 1 asked for "the full-year forecast it was guiding to when it finished selling"
  its H3C stake. The sale was reported in the June release beside its own later range. Result:
  "Answer not supported", Low 0/5 · Medium 0/5 · High 1/5. In the every-document check the high model
  took the decoy 3 of 3 times. "Guiding to when" read as "what the release reporting the event
  guided". The platform's notes describe the right reading as "in effect when the sale finished" and
  "current on May 28". With the same layout, "then-current" passed at Medium (aq-00964 q01) and
  "in force when" passed at High (aq-00745 q09). Use a firm timing verb ("in force", "then-current",
  "in effect on the day"), and keep it when rewording to avoid a near copy. Four local Opus solves
  matched at high confidence on the softer wording too, so local checks cannot see this risk.
  The high model must still reach the gold with every document, or the gate fails at any tier.
  The firm end overshoots too. The same content with "the full-year forecast in effect on the day it
  finished selling" (rev 2) was "Too easy", Low 5/5. Every low attempt found May 28 in the
  reporting release and took the forecast in effect that day. So in this layout, a day-level status
  cue lets every model through, and an action verb ("guiding to") lets none through. The measured
  middle is "in force when" (q09, High) or "then-current" (aq-00964, Medium). Measured on aq-01333 q01:
  "in force when" (rev 3 wording, run as rev 4) passed at the Easy tier (user report, 2026-10-07; tier line
  not supplied). So on identical content the ladder was: "was guiding to when" -> Answer not supported;
  "in force when" -> Easy; "in effect on the day" -> Too easy. In a layout where the event's exact day
  sits in the decoy release's body four days before its dateline, even "in force when" let the low model
  through sometimes. A Medium needs extra difficulty beyond the anchor.
- An exception stated in one plain sentence is a lookup even when it sits in end notes far from the rule it
  reverses (aq-01432 q01 rev 1, platform difficulty check 2026-10-07: "Too easy", Low 5/5). The body offences
  list made every banned practice an offence; note 112, marked on that very line, excluded one theme member. "4 of
  5 solver attempts got it by quoting the same passage" (the note). When the question's concept ("prosecuted")
  leads to the exception's own words ("criminal offence"), distance and footnote placement protect nothing. The
  low model has failed instead on a printed grouped figure answer-shaped for the ask, with the split only in another
  document and no marker or keyword tying them (aq-01431 q01: Low 0/5).
- A definition trap across editions passed at Medium (aq-01278 q02, platform difficulty check 2026-10-06: "In
  band — Medium tier", Low 0/5 · Medium 1/5). The earlier release states a growth figure whose scope only its own
  numbers reveal, and the later release prints the same label on a narrower scope. Chubb's Q1 bullet "2.8% in
  commercial insurance" counts agriculture (North America minus personal; the commercial segment row in the same
  release is 2.3%), while the Q2 release prints "North America Commercial was down 2.3%" for the segment alone, three
  times (bullet, CEO quote, table). The question quoted the Q1 figure and asked for Q2 "On that same basis" (the phrase
  is needed for one answer). All 5 low and 4 of 5 medium attempts answered the printed -2.3%; the right medium attempt
  reconciled the Q1 segment row ("7.3% excluding large account property") against the bullet. The high model reached
  the gold in 1 of 3 every-document attempts, and the platform added its "may be too vague" advisory while the gate
  passed. Local reviews had put Medium at 15-28% ("easy, marginal toward medium"), pessimistic again. Where a bundle
  holds two editions of one issuer, look for stated aggregates whose components the later edition regroups.
  The pass leaned on an undefined tie phrase: the platform reviewer returned the submission ("Revision
  requested": "On the same basis" undefined, -2.3% defensible) and asked for "the business lines behind the 2.8%";
  see [[docket-one-clear-answer-precision]]. Whether the trap still holds once the scope is named is unmeasured.
**Why:** extra sketch rounds against a solver stronger than the platform's screen cost time
without telling us which sketches would pass that screen.

**How to apply:** at sketch time, aim for at least one qualitative-lever sketch if the bundle
allows it. Record each local result in `notes/ideas.md` with the solver's readings and the
status the gate's sketch screen gives it (`lever miss`, `hard path`, `shortcut`, `exposed`,
`ambiguous`), and say plainly in the hand-over which sketches showed a hard path or a lever miss.
- An Easy pass on a labelled-figure bundle (aq-00998 q05, one question): Chevron's full-year ROCE
  method applied to a period no release reports (the twelve months ended June 30, 2026), at a stated
  precision where about ten near-miss methods give different values. Low 2/5 at two decimals, then
  "In band — Easy tier", Low 3/5 at three decimals, after four event-defined-quarter lookups were
  too easy. Misses came from building the period or the earnings wrongly (10.697%, 11.343%), not
  from a trap. Local review had predicted marginal, high too-easy risk.

## Evidence and history

- 2026-10-07 (aq-01322 q01 rev 3, user report "set q01 status as submitted and accepted_tier as
  medium"; tier line and platform words not supplied): the untied edition trap reached the Medium
  target. The U.S. Consulting Services divestiture is dated only in the latest release ("divested in
  April 2026"), whose own outlook ("~10% growth") and the intermediate May edition ("High-single digit
  growth") carry the asked row's label; the answer ("Flat") sits two editions back. Anchor worded as
  the completion ("closed the divestiture") after a probe reached the gold under "divested"; the group
  described as "the reporting category that then included the unit". Local reviews: Medium or better
  ~45-50%. Second measured Medium-or-better for this family (aq-00964 q01 Medium, aq-00745 q09 High);
  the same day's restatement carve-out (q03) was Too easy.
- 2026-10-06 (aq-01322 q03 rev 1, platform difficulty check Run 1 pasted by the user): "Too easy",
  "Low 4/5 · Medium — · High —"; closed-book "Needed the documents". A restatement carve-out over a
  calendar period no release reports (January-June 2025 = fiscal Q2+Q3): eight labelled segment cells
  from four releases (original vs restated U.S. rows), four subtractions, two sums, one division. Four
  attempts did exactly that; the miss used the fiscal six-month tables (5.7%), the calendar decoy.
  Coach: the wording ("segment restatement", the segment, the dates, "operating margin") maps by
  keyword to the restated columns. Local review had predicted Too easy ~45-50%. Lesson: naming the
  restatement and the exact period turns a carve-out into routine arithmetic for the low model, however
  many steps; the Medium mechanism here remains the untied edition trap (q01, unmeasured when filed).
- 2026-10-04 (aq-docket-trial-07, seven BLS Monthly Labor Review articles): 7 of 7 sketches were
  solved, each with the decoys named. They covered NBER-dated windows applied to another
  article's monthly series (a third-place decoy that only the right window rules out), a
  rounded-prose total, a prose month contradicted by the chart, and a 24-difference
  co-movement count. Two were written up (q01, q02); both matched again on fresh solves and
  passed review. Platform outcome for q01, the same day: "Too easy". The explanation said "the
  low model found it all in Doc 5". The bridge was the NBER months of the 2020 recession, which
  models know, and Doc 5's prose named the top two of the three answer items (see the rule
  above). q02, whose bridge is the NBER end of the Great Recession, has the same weakness and
  was not submitted. Replacement round: q03 (a D05 chart month, contradicted by D05's prose,
  decides which D04 rail value to read) passed review with no too-easy signal. q04 (a
  24-difference co-movement count) passed the guide, but the review gave it the "printed
  figures plus one standard calculation" signal, so it was dropped unsubmitted.
- 2026-10-04 (aq-docket-trial-02, ten Colgate-Palmolive earnings releases plus a recast segment
  exhibit): 5 of 5 sketches were solved, each with high confidence and the decoys named. They
  covered year-to-date de-cumulation with a sign flip, a cumulative charge total across three
  editions under changing program names, a prose "second consecutive quarter" claim versus the
  next quarter's table, a beat-the-company-rate filter with a late decoy, and a segment move
  across two recasts. The releases have no hedged findings or cross-document lists, so no
  qualitative lever applied. Two were written up (q01, q02) and matched on every fresh solve.
  Platform quick test for q01, the same day: "Too easy". "The low model reached your reference
  answer of +$94 million ... This is a clean two-step subtraction with no ambiguity in the
  figures, no decoy, and no tricky alignment. Every number is clearly labeled in a supplemental
  cash-flow table." The Coach suggested scattering the pieces across more documents or asking
  for a ratio or percentage. It confirmed that the 2025 releases print the 2024 year-to-date
  comparatives in rows cut from our capture. q01 was set to rejected and replaced by round-2
  bridge sketches. q02 (a cumulative charge sum, also a lookup path) is at the same risk.
- 2026-10-04 (aq-docket-trial-01, six unrelated arXiv papers): the first platform outcome. q01
  compared the share of measured genes modelled in two papers' main analyses: four stated counts,
  two divisions, and a "main analysis" lever the brain paper labels outright. All 5 sketches were
  solved locally and q01 passed every local check. The platform reviewer wrote: "Returned for one
  revision ... This is your last attempt. The question is too easy: it can be answered without
  careful work across the documents. Ask something that needs close reading and combining facts
  from more than one document." It came from review, not the quick test (none was run). The
  revision uses bridge sketches (round 2 in that bundle's ideas.md). No floor check could catch
  this; the path the solver reports (all lookups) is the signal. One verdict, but it bears on
  every lookup-path write-up, including those in trial-02 and trial-07.
- 2026-10-04 (aq-docket-trial-05, ten unrelated federal court rulings): 9 of 9 sketches were
  solved over two rounds, although most used the qualitative levers. Match-then-exclude
  sketches had four to six near-miss decoys. Others set equal-protection findings against a
  plaintiff's concession, hinged on a court's hedge about whether a claim was raised at all,
  buried one item in a prior-case list, or stacked a partial-motion decoy on a
  state-versus-federal-claim decoy. Two were written up: q01 (still face a federal claim after
  moving to dismiss everything) and q02 (dismissed with prejudice by a court saying it lacked
  jurisdiction). Each matched on every fresh solve. So qualitative levers did not buy a local
  miss here either. Round 3 followed after the user restated the platform's bar: one or two
  levers, single-condition sketches, no stacking. i10 asked which plaintiffs a court treated as
  conceding a state's immunity. Its hedge was Hill's "appears to concede", settled two
  paragraphs later; its mentions-vs-does decoy was Howard's silence, which his court never
  calls a concession. i11 asked which prison officials won on lack of personal involvement. Its
  hedge was a side-clause "not clear" over a firm holding; its decoys were movants whose
  personal-involvement argument the court never decided. Both were solved with high
  confidence, so 11 of 11 overall. i10 became q03, the cleanest fit to the bar, but it is below
  maximum. Under the stricter protocol all three questions are `checked`, and the bundle hit
  the three-round limit with no survivor.
  Under the D1-D7 gate (same day, user via docket-88): q01-q03 dropped; round 4 wrote up q04
  (plaintiffs who sued an official who had ruled in a proceeding involving them: a hedge decoy,
  Mulvilhill, plus a buried two-item fact, Langworthy's prior cases vi and xi). Two blind matches,
  closed-book miss, but review rated it below maximum: D4 fails because the decoy is ruled out in
  its own paragraph, and D2 is weak because two items are found from single passages. Review's
  diagnosis: in a bundle of rulings that never cite each other, D4 is met only by facts assembled
  from two dated statements or buried late in the longest document. A closed-book solve reached a
  near answer on a state-vs-local immunity sketch (i14): legal-status facts are general knowledge. q01
  packs "still faces a claim" and "under federal law" into its second condition, at the edge
  of stacking. q02 is exposed by the task page's overview. In a bundle of unrelated rulings,
  the local high model was not beaten by any fair lever. Platform outcome not yet known.
- 2026-10-04 (aq-docket-trial-06, six GAO consumer-protection reports joined only by shared
  agencies): 8 of 8 sketches were solved over two rounds, each with high confidence. They
  covered match then exclude (regulators that claimed predatory-lending preemption against those
  that objected to a deposit-insurance role), mentions it vs does it (which of OCC's two
  "preemption rules" actually preempts), a late-buried item (two agencies GAO rules out only in
  its reply to agency comments), and bridges into a flattened enforcement table. Written up: q03
  (rejected agencies minus the preemption claimant; ready after four review-driven revisions) as
  the primary hand-over, and q01 (Fed bridge into the table; ready). q02, a two-lookup
  subtraction, was dropped at review as thin. q01's bridge, that the Federal Reserve oversees
  holding companies, is near common knowledge (signal 1 above). Platform outcome not yet known.
  Round 3 aimed at the maximum bar the user pasted (one or two evidence-based levers that make
  even the high model struggle). Two more sketches were both solved: mentions it vs does it, where
  the agency that writes a law's rules was the decoy for the agency that enforces it, and match
  then exclude, with a decoy GAO rejects for a different reason. A table-only trap was defused by
  an explicit sentence elsewhere in the same report, so search each candidate trap's subject in
  the body before testing. Closed-book solves then dropped q01 and one sketch as general knowledge
  (see [[docket-general-knowledge-check]]). q03 is the sole hand-over.
- 2026-10-04 (aq-docket-trial-04, eight CRS foreign-aid reports incl. three Latin America
  editions): 7 of 7 sketches were solved over two rounds, each with the decoys named. They
  covered requests vs allocations across editions, a prose-baseline trap, two-condition match
  then exclude, enacted withholdings vs pending bills, and exact vs rounded figures. Three were
  written up and passed review. The user submitted q03, a Venezuela request percentage change
  "to one decimal place". Platform verdict: returned, "answered inconsistently". This is not a
  "too easy" verdict: the gold flipped between -2.2% and -2.3% depending on which of two stated
  figures was used. See [[docket-one-clear-answer-precision]].
- 2026-10-04 (aq-docket-trial-03, DOT agendas plus a 2025 proposal and 2026 final rule): q01 rev 2
  bridged from a 2026 footnote (refund-rule docket) to the first agenda after that rule's hearing.
  It passed two blind solves, a closed-book solve and review, with too-easy risk rated moderate.
  Platform difficulty gate: "Too easy -- solver got it ... Answered from one passage in Doc 6.
  That's the shortcut to close." The hearing date and rule name were also printed together in
  the 2025 proposal's footnote. "First agenda after the hearing" was simply the earliest edition,
  so the bridge decided nothing. Lessons: (1) a bridge fact printed in any single passage, even in
  a document the question does not point at, is a shortcut; (2) an edition choice that coincides
  with the earliest or latest edition tests nothing. The Coach then offered "places to make it
  harder" (passages pre-tested in the background): the two agendas' sentences naming the edition
  that holds the most recent review results. Revision 3 names "DOT's Fall 2023 agenda", which only
  the August 2024 agenda dates (February 9, 2024). Local review then sent back rev 3 (the target month
  equalled the agenda's own publication month) and rev 4 (only one same-month final-rule pair, so the
  question's own words bypassed the bridge). Rev 5 counts the other agenda items sharing the refund
  rule's target month (4). Both hearing rules are live candidates there, giving 4 or 0. It passed
  review, but too-easy risk is still rated moderate to high, because every step is a lookup.
  Platform outcome pending.
- 2026-10-04 (aq-docket-trial-04 q05, platform quick test): "Too easy — solver got it"; the low model named the CBSI funds-use report without quoting. The question asked which 45-day report the House committee reports required in both FY2023 and FY2024; "45 days" echoed the documents, so one search returned all four candidates. The local review had rated it below maximum (D3, D4, D7 failed; D1, D5, D6 held; closed-book missed). First platform result recorded against the D-checks: the failed D3/D4/D7 predicted the verdict. A closed-book miss (D1) alone does not lift an obscure but searchable fact above the low model. The user's reaction ("is this your max difficulty?"): do not hand over or quick-test a below-maximum question as a candidate; report it as below maximum and keep designing or stop.
- 2026-10-04 (aq-docket-trial-07 q05, platform quick test): the low model solved a chart-peak
  bridge (Midwest peak month May 1998 from Doc 4's chart, then rail's change from Doc 5's chart)
  that local review had rated maximum. The Coach's words are logged in q05. Local D-checks: D1,
  D2, D3, D5, D6 and D7 held, D4 not met. One quick-test result.
- 2026-10-05 (aq-00745 q01 rev 1, platform quick test pasted by the user with five solver tracks
  in tasks/aq-00745/verdict/): "Too easy", low model 5/5. The closed-book check "needed the
  documents". Each track read every release's tax footnote and listed the quarters whose own note
  says "net tax expense" (Q4 2025, Q2 2026). Each also set aside the year-to-date notes, the
  deferred-tax adjustments and the 2024 comparatives. The local review had rated it below
  maximum: D3, D4 and D7 failed; D1, D2, D5 and D6 held. This is the third platform result where
  the failed D-checks predicted the verdict (with trial-04 q05 and trial-07 q05). The Coach's
  reframing asked for each quarter's amount plus which were "material", a judgment call. Its
  objective part is the same per-quarter lookup the tracks already did correctly, so it was not
  adopted. One result. It generalises to per-period footnote filters in any earnings-release
  bundle.
- 2026-10-05 (aq-00964 q01 rev 0, platform difficulty check Run 1 pasted by the user; raw output in
  tasks/aq-00964/runs/q01-r0-cd873980.../results/platform-difficulty-check-run1.md): "In band —
  Medium tier", "The difficulty check passes on the current content", tiers "Low 0/5 · Medium
  1/5 · High —". The first positive platform result in this workspace. Question: the Africa &
  APAC 2026 property revenue midpoint in the outlook current when the Philippines subsidiary was
  sold. Every wrong attempt (Low 5, Medium 4) answered $1,630M from the July 28 outlook in the
  same release as the sale; the Coach: "It relied on Doc 7's post-sale outlook instead of Doc
  6's pre-sale outlook". Closed-book "Needed the documents"; document check needed Doc 6 and Doc
  7. Local record: Opus solvers A/B and auditor matched (high confidence), closed-book missed,
  review "easy (marginal)" with D4 weak ("then-current" signposts the check). The same round's
  other candidates (q02, q04-q06) were still unmeasured when this was filed.
- 2026-10-05 (aq-00949, EOG rolling quarterly supplemental data plus two press releases; user
  reports, not verbatim platform text). Two failures with no local warning beyond "easy
  (marginal)": q01, a classification inferred across two editions' footnotes, drew the form's
  document check "Doc 7 on its own may give enough to compute the answer" (a reader of the
  latest edition guesses from a visible jump in the row). q02, a press release's dividend
  payable date selecting the one edition-unique EPS-walk step, was solved "too easily" in the
  quick test, "answer from only Doc 6". Both had two Opus matches, a clear audit and a
  removal test showing two necessary documents. Lesson: a bridge stated in one plain sentence
  (a date) costs nothing to cross, and the platform then sees a one-passage answer in the target
  document; a heuristic that lands on the truth counts as one-document sufficiency. In a series
  with no outlooks or restatements, the pattern that passed elsewhere (an event plus a
  same-document decoy that a quick reader takes) needs a plan or forecast figure beside the
  actual, here only available in the capture's hidden balance-sheet and cash-flow rows.
- 2026-10-05 (aq-00949, later complete capture AQ-00949_2026-10-06_0251.md): the task page's
  "Question drafts" panel shows the quick-test lines verbatim. q01: "Too easy — solver got it",
  the low model answered both quarters and "doesn't quote the documents". q02: "Too easy — solver
  got it ... Answered from one passage in Doc 2. That's the shortcut to close." The panel names
  Doc 2 although the solver's own text cites Document 6 (the user had reported "only Doc 6"); the
  capture cuts the quoted passage. Read the verbatim panel from a fresh capture when available
  rather than a paraphrase. With the full tables visible, every 2025 quarter repeats in the 1Q26
  and 2Q26 editions and no figure is restated, so the replacement (q03) applies the 2020 plan's
  funding test (operating cash covers capex plus dividends, acquisitions excluded) to the latest
  edition's quarters; its wrong routes (free cash flow; acquisitions included) give different
  answers. Platform result, same day: difficulty check Run 1 "Too easy", Low 5/5 · Medium — ·
  High —, all five attempts quoting the Doc 1 rule sentence and computing 2,032 against 2,051;
  closed-book "Needed the documents". Local review had rated it easy (marginal) with
  moderate-to-high too-easy risk. Dropped; the next candidate tests exact table vs rounded prose.
- 2026-10-05 (aq-00998, Chevron releases 4Q23-2Q26 plus the Hess closing release, complete capture
  after an earlier clipped one). Four questions were written up, each with two matching Opus solves,
  a closed-book miss and a clear audit:
  - q01: net debt change over the quarter of a 2026 power agreement (start balance only in the
    previous release);
  - q02: 2Q26 crude unit inputs minus an acquisition quarter's (older edition prints a narrower
    "crude oil inputs" row);
  - q03: Gulf minus Permian growth in an April-2025 event quarter (the event's own release prints
    same-label figures for the previous quarter);
  - q04: a later-defined adjusted free cash flow in a dated completion quarter.
  All four reviews returned ready, "easy (marginal), high too-easy risk": one-sentence bridges into
  labelled cells (the aq-00949 q02 profile). The q03 rev 1 review called it the set's strongest trap.
  The event's own release prints same-label figures for the wrong quarter, giving a coherent -5.
  But the trap is cheaper to escape than aq-00964's: the bridge sentence prints "April 2025", and
  the decoy predates the event rather than looking current. Rev 0 of q03 drew the wording finding
  above. Platform results pending.
- 2026-10-06 (aq-00998 platform results, pasted by the user). q03 rev 1 difficulty check Run 1:
  "Too easy", "Low 5/5 · Medium — · High —". Solver summary: "5 of 5 solver attempts got it by quoting
  the same passage: Doc 6, p. 2". Closed-book: "Needed the documents". Coach: "The question wording
  'minus that of its Permian Basin operations' points straight at the two specific growth
  statistics ... a simple subtraction of two adjacent numbers rather than requiring synthesis across
  different reports or tables." Its suggested fix (a ratio of the same two growth rates) changes only
  the arithmetic, so it was not adopted. The user reported that q01, q02 and q04 also failed the
  quick test (too easy; no verbatim output). All four had local "easy (marginal), high too-easy
  risk" reviews. The event-defined-quarter frame with a plainly dated bridge is measured too easy on
  this bundle. Raw output: tasks/aq-00998/runs/q03-r1-v2-62f3d14a.../results/.
- 2026-10-06 (aq-00745 q01 rev 1, platform difficulty check Run 2 pasted by the user; raw in
  tasks/aq-00745/runs/q01-r1-v2-dbae27b2.../results/platform-difficulty-check-run2.md): "In band —
  Easy tier", Low 1/5 · Medium — · High —. Wrong low attempts 1, 3, 4, 5 "used Doc 8's $5.38–$5.58
  range as the one in force at acquisition completion" (+$0.05); the platform added "This question
  may be too vague: several solvers agreed on an answer that is not your gold" (a warning; the
  check still passed). Closed-book "Needed the documents" (-$0.05). Local review had rated it easy
  (marginal). The user reported that q01 was the only quick-test survivor of the round (q03 and q05,
  table lookups/computations, did not survive; platform words not supplied).
- 2026-10-05 (aq-docket-trial-03 fresh intake, user report "two questions are not passed in quick
  test", no verbatim platform text): both Easy write-ups were solved by the quick test's easier
  solver. q01 rev 3 asked an agenda rulemaking's stage on two dates (proposal publication and
  extended comment close) in "the latest ... agenda published in the Federal Register by that
  day": wording that spells out the edition check turns the aq-00964 edition bridge into a
  procedure the low model follows. q02 rev 1 joined a proposal's comment deadline to the final
  rule's effective date plus an opposing-comment count (the Guide's worked example 2 shape) with
  a joint-comment trap and a footnote decoy date; also solved. Locally both had two Opus matches,
  a clear audit, a closed-book miss and review "easy (marginal)". The user then raised the
  target to Medium.
- 2026-10-06 (aq-00745 q08, Coach analysis pasted by the user; raw in tasks/aq-00745/runs/q08-r0-v2-
  b25a2531.../results/platform-difficulty-check.md): "No solver at any level reached your answer of
  -$0.10. The low model went 0 of 5, the medium 0 of 5, the high 0 of 5. That is why it came back
  Too hard." Low 5/5 took Doc 8's post-closing range (+$0.07); medium and high 9/10 used Doc 7's
  $5.55 then Doc 8's $5.38 (-$0.17). The Coach also reported "The 'No single passage gives the
  answer' check also failed": Doc 10 alone yields +$0.07 from its own previous-vs-new sentence. The
  measured wording was a rewording of q08 rev 0, so the result is not bound to rev 0's fingerprint.
- 2026-10-06 (aq-00745 q09 rev 1, user report "great! you passed as a High tier."; tier line not
  supplied): percentage change of the FY2026 adjusted EPS guidance midpoint from the range in force
  when the FreeDM2 results were announced (March, reported only in the April release beside its own
  later range) to the July range; gold -2.6%, decoy +0.8%. Local: two Opus matches (high
  confidence), closed-book "unknown", audit clear, review medium (marginal); the local path
  underestimated it again, as on aq-00964 q01. First High-tier pass in this workspace.
- 2026-10-06 (aq-00998 q05 rev 3, platform difficulty check Run 2, screenshot supplied by the user):
  Chevron's full-year ROCE method applied to the twelve months ended June 30, 2026, two decimals
  (10.87%; documents Doc 10 and Doc 12). "Low model 2/5 right", inside the stated 1-3 window: the
  first in-window result on this bundle, after four event-defined-quarter lookups were too easy (q03
  Low 5/5). A definition applied to a period no release reports, with near-miss methods that differ
  at the stated precision, moved the low model into the window. The gate still failed on the
  platform's removal test ("A marked document may not be needed ... without document 10"); see
  [[docket-series-editions-necessity]]. Local: two Opus matches, closed-book unknown, audit clear,
  review easy (marginal, high too-easy risk), so the local prediction was again too pessimistic.
- 2026-10-06 (aq-docket-trial-01 rebuilt from scratch, target Medium, one attempt; six unrelated
  arXiv papers, no cross-citations). Nine sketches over two rounds were all fair locally (fresh Opus
  solves matched, closed-book missed), but independent reviews predicted Easy for every write-up:
  q01 (iterations derived as runtime / time per iteration, minus another paper's count) because each
  wrong value was excluded by the question's own wording; q03 (a paper's own definition of
  "observations" as genes, not spots) because the definition is a plain sentence containing the
  question's keyword and the decoy carries the asked label only through field convention, not inside
  the document (reviewer: Medium "about one in ten"). Lesson for unrelated-paper bundles: the
  cross-document step is arithmetic over analogous figures, so the Medium mechanism (a same-label
  wrong value inside a document, ruled out only by a fact that needs close reading) must come from
  one paper's internals; look for it at intake and quick-test before spending the single attempt.
  Platform quick tests (same day, user screenshot): both "Too easy — solver got it" (q03: the low
  model read the paper's n x m notation and took 14,638 genes as observations; q01: it did the 65 /
  5.91 division). Coach on both: "two lookups and one subtraction"; it quotes the guide's
  "Calculate across documents" lever as "One lookup plus one operation is usually solved", says a
  decoy counts only if the wording does not already select the right figure, flags inputs read
  from a chart or printed with "∼" as approximations (R9/PIN1), and recommends "Scatter the
  pieces", "Restated figures" and three or more dependent steps. The user then accepted Easy for
  this trial. Raw words: tasks/aq-docket-trial-01/notes/feedback-coach-2026-10-06.md.
  Asked for a question "like Trial 2's q01 or Trial 6's q02" (a share built from unprinted figures,
  where an exclusion or remainder sits in a note or appendix), the bundle had no shared entity for
  a bridge, so the parallel was two papers each trimming genes with a threshold of 20. q04 measured
  each share against the step's own input ("genes each step started from"): review Too easy ~65%,
  because that wording pointed at the appendix figure and "exceed" disarmed the negative routes.
  q05 measured both against all genes with expression data and asked for a ratio with no direction
  word, so the module step's discards (3000 - 979) must be separated from the earlier MAD screen
  unprompted: review Too easy ~50%, Easy ~40%, Low 0/5 ~10%. Wording that names the right base is
  itself the signpost the Coach warned about. Platform result pending.
- 2026-10-06 (aq-docket-trial-06 rebuilt from scratch, target Medium, one attempt; six unrelated GAO
  reports, no cross-citations). Applying the lesson above, two independent authors each found one
  Medium-plausible design, and both used the same in-document trap: a total no passage prints that
  needs a remainder named only in a footnote and an appendix (two uninsured credit unions beside
  9,688 federally insured and 212 privately insured). q01 asked how many more credit unions the U.S.
  had at the end of 2002 than banks on September 30, 2005 (2,361; decoys 2,359 and 2,147). Two Opus
  solvers matched, but one of them and one removal probe took 9,900 or called the footnote undated
  until reaching the appendix sentence; two independent reviews returned ready, medium (marginal),
  tier estimate Easy about 45%, Medium about 40%. The sibling q02 (one state's share) was dropped
  (see [[docket-one-clear-answer-precision]] and [[docket-series-editions-necessity]]). Platform
  result pending.
  Round 2 (user: "make QA like Trial 2's q01 or Trial 6's q02"): q03 asked q01's hook as a percentage
  to two decimals (31.31%, decoy 31.28%); review ready, same tier odds as q01 (the percentage adds
  arithmetic, not evidence; two decimals are needed for the remainder to matter). q04 (the bridged
  state's share of credit unions with noncompliant Web sites, 25.0% against the row's printed 71%)
  was reviewed Too easy 55-65%: the opening "Of the privately insured credit unions" repeats the
  table's own column heading. The deciding appendix sentence ("lacked federal deposit insurance,
  and all but two were privately insured") never says "uninsured", so readers who search for that
  word find only the undated footnote: 3 of 10 fresh Opus runs took 9,900, all of them auditor or
  probe roles that never read the sentence; all four blind solvers found the remainder.
- 2026-10-06 (aq-docket-trial-02 rebuilt, target Medium; one company's releases Q1 2024-Q2 2026 plus a
  2026 segment-recast exhibit and an unrelated 2019 award form). Local only, platform pending. Every
  guidance or estimate update restates the prior value in the same release ("versus ... previously",
  "increased from"), so an edition trap there is tied; quarterly recast rebuilds split by $1M rounding.
  The two strongest fair designs were each reviewed Easy-leaning: a carve-out derived from original vs
  recast segment rows (q01, the exclusion sits in the defining parenthesis the question's own terms
  retrieve; Medium+ about 20%) and an estimate midpoint minus pretax charges whose salient prose figure
  covers operating profit only (q02; Medium+ about 15%). Both reviews: quick-test before the attempt.
- 2026-10-06 (aq-docket-trial-05 rebuilt from scratch, target Medium, one attempt; ten unrelated
  September 2026 federal rulings with no cross-citations and no shared parties). Six round-1
  sketches were all fair locally (fresh Opus solves matched, closed-book missed). Four were written
  up with full checks (two matches, closed-book miss, clear audit each), and independent reviews
  rated every one Easy or Too easy: disposition and role filters across rulings (plaintiffs who sued
  a judge who had ruled against them; counts still pending in two officers' suits; defendants
  dismissed with prejudice; state police held Eleventh-Amendment shielded) print the deciding fact
  per item, and each decoy is ruled out in its own passage. A judges-sued variant was dropped when
  its audit found case-number initials ("DHU") supplying a second answer. A fresh author then read
  all ten rulings and found no fair Medium design: the only untied same-label trap (Hill: Jones and
  Quade "ranked first and second" at a 2023 meeting, originally 7th and 8th) has no second-ruling
  partner. Lesson: at intake, list each same-label trap with its possible cross-document partner;
  if none exists, tell the user early that Medium is unlikely and quick-test before the single
  attempt. Platform result pending.
- 2026-10-06 (aq-docket-trial-07 rebuilt from scratch, target Medium, one attempt; the same seven
  2021 BLS Monthly Labor Review articles as the earlier trial-07 session). Local only, platform pending.
  Two independent authors: none of 25 links outside the rail/Midwest/BED time series is a fair hook (no
  partner data for D02's thresholds, D03's wage cutoffs or D07's regions; partners that are general
  knowledge; manufactured links); inside the time series every link is calendar alignment. Every
  article's prose disagrees with its own charts somewhere (Midwest "bottomed out in February 2010" vs a
  December 2009 chart low; "17.1-percent" from rounded 4.1/3.5 vs 15.7%; "47,000" vs a table -37; Cyprus
  listed under two regions). A design whose decoy is such a conflict on the asked fact drew a blind
  solver's "if you trust the text, 178.2" reading, so it risks two defensible answers; a conflict that
  sits on a different series or base (q01: nondurable low in March 2010 against the total-manufacturing
  February 2010 sentence and the nondurable June 2009 recovery framing) is fair but was still reviewed
  Easy (two reviews: Medium 10-12%), because it repeats the q05 chart-extreme path the low model solved.
  Lesson: in an unrelated-article bundle with chart data, say early that Medium is unlikely, hand over a
  quick-test batch, and keep document-error decoys out of the single submission. Removal-probe packets
  built as byte copies minus one document should renumber or keep ids neutral: a probe inferred "the
  source looks like it was dropped (no D05)" from the gap in the id sequence.
- 2026-10-06 (aq-01333, six HPE earnings releases Q2 FY25-Q3 FY26; target medium; local only,
  platform pending). Two untied event-to-prior-edition traps were found and checked (two Opus matches,
  closed-book miss, clear audit, review ready each): q01, the FY26 non-GAAP EPS midpoint change from the
  range in force at the H3C stake sale (May 28, reported in the June 1 release beside its own raised
  range) to the September range (review: medium marginal, Medium-or-higher about 40-50%); q03, actual
  FY25 non-GAAP operating-profit growth vs the midpoint in force at the Juniper closing (July 2, 2025,
  reported in the September release directly under its own range; review: Easy most likely,
  Medium-or-higher about 30-35%, because that release's narrative centres on the closing). A recast-basis
  margin with a printed old-basis decoy (q02) was fair but reviewed Easy-leaning: the pin "on that same
  segment structure" is needed for one answer and itself signposts the recast. Only two dated events in
  the bundle had a post-event value in their own release. Platform, the same day (user paste; raw in
  tasks/aq-01333/runs/q02-r0-v2-d81d8a8b.../results/platform-difficulty-check-run1.md): q02 difficulty check
  Run 1 "Too easy", "Low 4/5 · Medium — · High —", version ef0be5. Solver summary: "3 of 5 solver attempts
  got it by quoting the same passage: Doc 4 (“Segment Operating Margin Summary Data”)". The one miss took
  Doc 3's printed 23.31%. Closed-book "Needed the documents". The review had predicted Too easy ~25%, Easy ~50%.
  The Coach suggested reconciling "the restated full-year total" with the four restated quarters, but no
  restated full-year total exists, so that suggestion was not adopted. q02 dropped.
  Then q01 rev 1, difficulty check Run 2 (version ed7950; raw in tasks/aq-01333/runs/q01-r1-v2-b98e240c.../
  results/platform-difficulty-check-run2.md): "Answer not supported", "Low 0/5 · Medium 0/5 · High 1/5".
  14 of 15 attempts and all three every-document checks answered 11.8% from the June decoy range. The
  advisory read "This question may be too vague". The local review had predicted medium (marginal), Too hard ≤5%.
  This overshoot is the reverse of the earlier under-calls (aq-00964 q01, aq-00745 q09). Rev 2 restored
  a firm anchor ("in effect on the day it finished selling"), was reviewed ready (medium marginal), and
  Run 3 was "Too easy", "Low 5/5 · Medium — · High —" (version 3e94b7). The Coach: "three
  straightforward lookups and a simple midpoint calculation". Its suggested indirect event ("the date
  HPE first recognized gains from the H3C divestiture") is ambiguous, because the 2024 sale also
  produced a gain. Rev 3 (user: "plz make strongest one") used the in-between anchor "in force when".
  Rev 4 had the same question with Doc 5 ticked as "Exclusion / condition source" plus a note. It passed
  at the Easy tier and the user submitted it (2026-10-07: "set q01 status as submitted and accepted_tier as
  Easy Tier"; tier line and document-check lines not supplied; no removal flag reported). The review had
  predicted Too easy about 2 in 5 and Easy about 1 in 4, so the outcome sat inside the predicted band.
  The platform reviewer then returned rev 4 ("Revision requested", 2026-10-07). The question and gold
  were "correct", but Doc 5 was "not necessary" ("Without document 5 — 58.3%"). Rev 5 unticks Doc 5 and
  dates the sale from Doc 6, with the question unchanged.
  q03 unmeasured.
- 2026-10-05 (aq-00949 q04 rev 2, user report "Good job, You passed in Easy tier, low model solve
  3/5 attempt"; platform block, solver summary and document-check line not supplied): EOG's June
  30, 2026 total debt (Doc 7, 7,926) as a percentage of its end-2019 total debt (Doc 1 table 5,175;
  Doc 1 prose "$5.2 billion"), one decimal: 153.2%. The fourth candidate on the bundle after three
  lookup-and-calculate failures (q01, q02 quick tests; q03 Low 5/5). Local: two Opus matches (high
  confidence), audit clear, closed-book miss that recalled 5,175 exactly (4 of 4 runs), review
  ready "easy (marginal)" predicting Low 4-5/5. The review's moderate risk that the platform's
  removal test would find Doc 1 not needed (the input is recalled) was not reported as firing.
  Local predictions were too pessimistic in the same direction as aq-00964 q01, aq-00745 q09 and
  aq-00998 q05. One result. Superseded on 2026-10-06 (next entry): the pass did not survive the
  wording fix.
- 2026-10-06 (aq-00949 q04 rev 5, platform difficulty check Run 4 pasted by the user; raw in
  tasks/aq-00949/runs/q04-r5-v2-5a596dd1.../results/platform-difficulty-check-run4.md): "Too easy",
  "Low 5/5 · Medium — · High —", version 8f4589. This followed the platform reviewer's "Revision
  requested" on the submitted rev 2: ""was what percentage of its total debt" can be interpreted
  to put Q2 2026 numbers in numerator or denominator. This is ambiguous". Rev 5 asked for end-2019
  debt divided by June 30, 2026 debt, two decimals (65.29%). Solver summary: "3 of 5 solver attempts
  got it by quoting the same passage: Doc 1 (“At December 31, 2019, EOG’s total debt outstanding was
  $5.2 billion ...”)". All five still used 5,175. Coach: "derive one or both debt figures from
  components scattered across multiple documents ... or ask for a trend/comparison that forces
  reading across several quarterly reports rather than pulling two stated totals." Local reviews of
  rev 3-5 had predicted exactly this: making the order explicit removes the misreading routes and
  leaves a two-lookup division. Lesson: re-measure after any wording fix. A pass that rests on a
  misreading is not the lever's.
- 2026-10-05 (aq-00949 round 4, target medium; user screenshot plus local reviews, no difficulty check
  yet): all four quick-tested drafts showed "Survived — worth writing up", so a quick-test survival did
  not separate them. The two promoted ones were reviewed easy (revise): q05, two rounded prose figures
  from one sentence (one decision, q04's measured-Easy lever), and q06, a stated bridge method applied
  to a year-over-year pair (the aq-00998 q05 shape, Low 2/5) behind a public, inferable date anchor.
  A same-document printed value for a different comparison (the sequential 0.14) is not an aq-00964
  decoy when the question's own words ("same quarter a year later") rule it out.
- 2026-10-06 (aq-00998 q05 rev 4, platform difficulty check Run 3, pasted by the user): "In band —
  Easy tier", "Low 3/5 · Medium — · High —", closed-book "Needed the documents ✓", both necessary
  documents confirmed by the document check. First Easy pass on this bundle and the first pass under
  the Easy objective. Low-model misses: 10.697% and 11.343% (ROCE earnings 23,217 instead of 22,247).
- 2026-10-06 (aq-docket-trial-02 rebuilt, user report, no platform words or tier line): "q01 passed in
  pipeline, but q03 not passed in even quick-test". Both use the same carve-out (Africa/Eurasia minus
  Russia and Belarus, whose figures come from the Asia Pacific recast difference; the exclusion is
  stated only in D11). q01 rev 2 asked the 2024-to-2025 net sales change (+7.85%), with D09's printed
  whole-segment +7.0% as a same-label, answer-shaped decoy in the path. q03 rev 1 asked the 2024
  operating margin (19.68%): one year, no printed whole-segment margin. Local reviews rated both
  Easy-leaning and did not separate them. Working lesson: the low model can derive a carve-out from
  original vs recast rows by itself; keep a printed answer-shaped decoy in the solver's path, and
  quick-test drafts before full write-ups. Same day, the user accepted q01 ("previous version is
  accepted"). q04 (North America operating margin for the twelve months ended June 30, 2026 "as the
  company defined that segment from 2026"; recast full year in D10, halves in D12, the pre-2026 D09 row
  as decoy) was "Too easy — solver got it" in two quick tests: the pin sent the low model straight to
  the recast tables and the twelve-month build is routine for it. A restatement trap whose question
  names the restatement is no trap.
- 2026-10-06 (aq-docket-trial-04 rebuilt, user report, no platform words or tier line): "q03 passed in
  pipeline of Docket". q03 rev 2: the FY2025 priority set ("nearly 75%", Doc 8) rebuilt in the FY2023
  request (Doc 3) from twelve amounts and two exact totals, share change -6.6 percentage points. The
  printed same-label decoy was Doc 3's $986.8 million FY2023 Central America request (summary, Table
  4, bundle overview), of which only $959.0 million falls within the regional total (L481, footnote
  15); the question's premise ("nearly 75% of that request") fixed the regional base without naming
  the carve-out. Second pipeline pass for the shape the user asks for (trial-02 q01 was the first).
  Rev 1 of the same set on the FY2024 base, where every trap was a visible approximation, had been
  reviewed easy and was never tested; rev 2's local review said medium (marginal, Easy 45-55%).

- 2026-10-06 (aq-01428, Eni Q1 (Apr 24) and Q2/H1 (Jul 29) 2026 releases plus two Occidental releases
  with no numeric guidance; target Medium; local only, platform pending). Eni's July release restates the
  prior value for production, buyback and Enilive guidance (tied, unusable) but not for GGP EBIT (~€1.3 bln
  -> over €1.4 bln) or CFFO (€13.8 -> €15 bln). Two checked write-ups on that edition pair: q01, the GGP
  guidance in force in the month of a June event printed only in the July release (aq-00964 shape; review
  medium marginal, Medium+ ~45%); q02, second-half CFFO needed = guidance in place at end-June minus H1
  actual (review easy, Medium+ ~20%: the plain period-end date in the question signposts the edition check).
  Lessons: (1) with only two editions, removing the later release leaves the earlier release's figure as the
  only candidate, so forced-guess removal probes chose the gold (p 0.6, two of two); the platform's unforced
  check refused in aq-00964, so this is a 15-35% risk, not a violation; (2) making the later release supply a
  number (H1 actual) fixes necessity but first-half/full-year splits sit on a half-year prior (closed-book
  "about 55%" vs 53%; "about €6.5 bln" vs €6.45 bln, protected only by two decimals); (3) an event anchor the
  solver must date beats a period-end date written into the question.
- 2026-10-06 (aq-01433, six 2010 Census ICP assessment reports, all August 2012; target Medium).
  Platform result (user paste, difficulty check Run 1, version 55d10a, run without a quick test):
  q01 rev 1 "In band — Easy tier", "Low 2/5 · Medium — · High —"; all three wrong low attempts
  answered 4,735,573 (the late misspelled Thai row missed); closed-book "Needed the documents";
  document check needed both marked documents. The local reviews' Easy forecast (Easy ~65%, Medium
  ~17%) was right this time. Measured: one late, misspelled list member catches the low model about 3
  times in 5 (Easy), not 5 in 5; Medium would need a second independent trap or a printed decoy.
  Round 2 (two more independent authors aimed at exactly that) found none above ~15% Medium: every
  strong trap here is single-document (App D FY2011 column, App C index divided by unadjusted 2000
  cost, App E typos, fused footnote digits) and each cross-document partner duplicates or poisons
  it; the user submitted q01 to the open Easy slot (confirmed 2026-10-07; frontmatter
  accepted_tier: Easy Tier).
  Local findings that led to it: no edition, forecast or restatement exists, and two independent authors
  confirmed no measured-Medium mechanism. Most numeric joins are poisoned: the reports disagree on the
  same quantity (contract budget 312.1/362/371M, national/local ad split, rapid-response spend), the
  summary repeats most component facts, the paid-ad and promotional reports print the same 28 languages
  (so a language list in one is replaceable by the other), and appendix tables carry typos (German
  30,000 vs 300,000, Korean "3009,410", swapped Emerging/Legacy footnotes). The strongest fair design:
  a per-item award list in the summary's appendix picks one printed piece (3 awards vs 1), whose
  quantities sit in another report's distribution appendix, one version listed late in a later wave
  under a misspelled title (q01, 4,821,423; omitting it gives 4,735,573). Two reviews: ready, Easy
  (Medium ~17-20%): a single missed-row trap has no printed answer-shaped decoy, and full-text readers
  catch the misspelling via other words. A program's language list filtering the other report's ARRA
  wave (q02, decoy the target report's own different list) reviewed Easy (Medium ~10%), because the
  question's "paid advertising" neutralises the in-document decoy. Lesson: in program-assessment
  bundles, per-item award/recognition lists are usable bridges into per-item quantity tables; say early
  that Medium is unlikely and quick-test before any difficulty run.
- 2026-10-06 (aq-01428 q01 rev 1, form model check, user screenshot, before any quick test or difficulty
  run): the soft anchor "In the month Eni secured ... how much ... was its guidance expecting" was blocked:
  "This question is too vague to submit: two independent solvers ... Both answered "€1.40 billion"" (the
  event release's own raised guidance; the form box also carried a stray "two decimal places" sentence).
  Same direction as aq-01333 q01 rev 1 (soft anchor -> high model took the decoy, "Answer not supported")
  and the reverse of its firm-anchor rev 2 (Too easy). Rev 2 here uses the in-between anchor "the guidance
  then in force" during the event's month, plus the source's own precision (one decimal). Pending.
- 2026-10-06 (aq-01321, four chipmakers' quarterly releases, three each; target Medium; local only,
  platform pending; golds deliberately not stated here). Every outlook covers only the next quarter and
  no event in a later release is dated, so the measured edition trap (aq-00964 q01) has no fair analogue;
  an independent author confirmed this. Two write-ups passed every local check but were reviewed
  Easy-leaning: q01, a cumulative inventory reduction printed "now" in the March-quarter release asked as
  of the next quarter-end (stale same-label decoy; Medium about 9%: the asked quarter and the later
  release's own dates date the decoy); q02, a trailing-twelve-month (R&D + SG&A) / revenue ratio whose
  latest release prints the same-window total only as a rounded "$3.9 billion", with the exact figure
  rebuilt across three releases (Medium about 12%, High about 3%; stronger than aq-00949 q04 because the
  exact numerator is printed nowhere). Calendar-window sums (onsemi's Q1 ends near April 3) were fair
  but the alignment is known to strong models. Lesson: when every forecast is next-quarter only, look
  first for a same-window rounded statement whose exact value needs a multi-release rebuild.
- 2026-10-06 (aq-01321 q02, form model check on a user rewording, before any quick test or difficulty
  run): two platform solvers both answered the rounded same-window prose route (20.05%) and the form
  blocked the question as "too vague to submit". The pull of a same-label, same-window rounded statement
  is real for the platform's solvers, but the platform scores it as ambiguity, not as a trap: such a
  decoy must be excluded by the question's description, which disarms it. See
  [[docket-one-clear-answer-precision]].
- 2026-10-06 (aq-01321 q02, user report "passed and is evaluated as Easy Tier"; tier line and exact
  tested wording not supplied): after the description was narrowed to exclude the same-window rounded
  "$3.9 billion", the twelve-month (R&D + SG&A) / revenue ratio rebuilt across three releases reached
  the Easy tier, as both local reviews predicted (Easy most likely, Medium ~12%). The rounding lever
  either blocks as "too vague" (decoy matches the description) or disappears (decoy excluded); a
  three-release roll-forward alone is an Easy mechanism here. For Medium the decoy must be one a
  careful reader excludes from the question's own words while a quick reader still takes it (timing or
  basis), not a figure the description matches outright.
- 2026-10-06 (aq-01320 q01 rev 2, Darden FY2026 outlook editions; platform difficulty check, user
  report "your q01 is passed and is evaluated as Easy Tier on Docket Platform.", no tier line or traces
  pasted): actual FY2026 reported diluted EPS from continuing operations minus the midpoint of the
  reported range in the outlook "as it stood when that fiscal year's fourth quarter began" (December
  18 edition, $10.62-$10.82; actual $10.44; gold -$0.28). Decoy: the March 19 release's own later
  range (-$0.01), with the reported range only in reconciliation tables and adjusted figures in the
  bullets and overview. Local: three rounds of two Opus matches, closed-book misses, clear audits; two
  reviews put Easy as the modal outcome (40-50%) and Medium about 25%, so the local prediction was
  right this time. A removal probe without the December release forced-guessed the decoy (-$0.01).
  The independent author and the caller found no other untied numeric edition in this bundle
  (Wendy's editions identical, Chipotle's change qualitative, Yum no annual outlook).
- 2026-10-06 (aq-01431, twelve public comment letters to the SEC on the fund/adviser ESG proposal and
  related rules, Nov 2022-Apr 2024; target Medium; local only, platform pending). The caller and two
  independent authors found no fair Medium design: no dated forecast series (one agenda projection,
  no later edition); the one repeated figure series (ICI member assets per letter) is snapshots, not
  values in force; rule 10 bars answers naming bundle authors (ICI, MFA, Sierra Club, AFR, ...); list
  and filter hooks resolve inside one letter or are "who cites whom"; the attached research paper
  (D10) has rich internal traps but no second-document partner. The best fair design was a grouped
  figure in one letter against a split in another: US SIF 2022 data, climate change/carbon ($3.45T,
  AFR letter, beside fossil fuel divestment $1.23T) minus the issue ranked second (military/weapons
  $1.8T, Sierra Club letter, which groups climate and fossil fuel at "a combined $4.8 trillion"),
  gold $1.65T, decoys 2.22 and 3.00. Two Opus matches, clear audit, closed-book miss, removal probes
  forced the decoys (3.00 without the split, 2.22 without the ranking); review ready but Easy (Too
  easy 40-45%, Easy ~45%, Medium 6-8%): the label "climate change/carbon" needed for fairness rules out
  the grouped figure, and the 2.22 route is a misreading, not a printed answer-shaped value. Lesson:
  in advocacy-letter bundles, figures are cited secondhand and rarely in force at a date; say early
  that Medium is unlikely and ask for a quick test.
  Platform result the same day (user paste; raw in tasks/aq-01431/runs/q01-r0-v2-a3bea189.../results/
  platform-difficulty-check-run1.md): difficulty check Run 1 "Between levels", "Low 0/5 · Medium 4/5 ·
  High —", version 550ca2, advisory "This question may be too vague: several solvers agreed on an answer
  that is not your gold" (four low attempts answered 3.00). Closed-book "Needed the documents" (1.30).
  The user ran the check without a quick test. Rev 1 removed the label so the solver must identify the
  largest single issue itself (sibling wording i01, same gold); its platform result is pending.
- 2026-10-06 (aq-01430, eight Ember electricity publications: reviews of 2020, 2021, 2024 and 2025
  data, mid-year reports for H1-2023 and H1-2025, a Q1-Q3 2025 report with a full-year forecast and a
  June 2026 gas review; target Medium; local only, platform pending). Two independent authors and both
  reviews found no "looks current" same-document decoy: Ember's only numeric forecasts sit in one edition
  (the Q1-Q3 report), and the 2025-data review restates many 2024 figures of the 2024-data review (demand
  growth 4.0% -> 4.3%, gas +103 -> +183 TWh), so same-quantity asks across editions have two answers.
  Two derived-numeric write-ups passed every local check (two Opus matches, clear audit, closed-book
  misses, removal probes) but were reviewed Easy: q01, overlapping windows across editions (EU coal
  2019 -> 2021 = -34 TWh from the 2024 review's "last five years" -182 and the 2025 review's "since 2021"
  -162 net of 2025's -14; Medium ~12%), and q02, full year minus an unprinted first-half total (China
  fossil July-December 2025 = +2.8 TWh; the first-half coal fall equals the full-year fossil fall, -56;
  Medium ~7%). Lesson: in a single-publisher annual series with restatements, overlapping windows are the
  strongest fair derived mechanism found, but window arithmetic reads like the measured Too easy
  partial-period step; quick-test before any difficulty run.
- 2026-10-06 (aq-01432, eleven FTC and CMA consumer-protection guidance documents, 2013-2025; target Medium; local only,
  platform pending; golds not stated here). An independent author and the caller found no fair derived-numeric design:
  every figure is a one-document hypothetical or a rule constant needing an input no document gives (a penalty floor
  without a turnover, time limits without dates). Two write-ups passed every local check and were reviewed Easy-leaning.
  q01 counts the short business guide's own pressure-selling behaviours a trader could be prosecuted for; the full
  guidance's body offences list covers every banned practice, and only its end notes exclude one theme member (rev 1
  review: Too easy ~40%, Easy ~45%, Medium ~10%). The trap is tied: the note marker sits on the very line the decoy comes
  from, and "prosecuted" leads to a "criminal offence" search that lands on both notes. Pinning the universe to the theme
  heading removed the wrong-reading routes and with them some difficulty (the aq-00949 q04 lesson again). q02 judges
  CMA208's commissioning examples by the FTC staff reading of the US reviews rule; its decoy is excluded by a staff answer
  in the section the solver reads (Too easy ~45%, Easy ~40%, Medium ~8%). Lesson: in legal-guidance bundles a footnote
  that reverses a body rule is a tied trap when the body line carries the marker. Statute exceptions are also partly
  recalled, which threatens both the closed-book check and the law document's platform necessity. Say early that Medium
  is unlikely and quick-test first.
- 2026-10-07 (aq-01432 q01 rev 1, platform difficulty check Run 1 pasted by the user; version e5d715; raw in
  tasks/aq-01432/runs/q01-r1-v2-38a28e32.../results/platform-difficulty-check-run1.md): "Too easy", "Low 5/5 · Medium —
  · High —"; all five low attempts listed the short guide's seven pressure-selling behaviours, mapped them to the full
  guidance's banned practices and excluded paragraph 30 via note 112; closed-book "Needed the documents" (3). Local
  reviews had put Too easy at 30-40% and Easy at 45-50%. Dropped with its sibling sketch (same carve-out).
- 2026-10-06 (aq-01278 q02, Chubb Q1 and Q2 2026 releases inside a four-insurer peer bundle; platform difficulty
  check Run 1 pasted by the user; version 4093c3; raw in tasks/aq-01278/runs/q02-platform-4093c3/
  platform-difficulty-check-run1.md): "In band — Medium tier", "Low 0/5 · Medium 1/5 · High —", "The difficulty check
  passes on the current content.", plus "This question may be too vague: several solvers agreed on an answer that is not
  your gold "-1.3%"". Closed-book "Needed the documents" (answered +3.9%); document check needed Doc 4 (-2.3% twice
  without it) and Doc 9 (cannot be determined twice). Local record: two Opus matches (high confidence), audit clear,
  closed-book +2.4%, removal probes -2.3% (Q1 release withheld) and +2.0% (Q2 release withheld), review revise for
  reasoning/evidence only with tier odds Too easy 8%, Easy 65%, Medium 15%. The bundle's other measured candidate
  shapes were all local Easy-leaning (Travelers worldwide auto premiums with a domestic-only printed row: review
  Medium+ about 13-15%, platform pending). Tested form fields were not yet bound to a local fingerprint when filed.
- 2026-10-06 (aq-01278 q02, platform review after submission, screenshot from the user): "Revision requested". "Gold
  maths is correct, but "same basis" lets solvers use Chubb's own Q2 commercial figure (−2.3%, Doc 9). Asking for the
  business lines behind the 2.8% keeps Doc 4 necessary and makes −1.3% the only answer." Issues: ambiguous wording
  (blocking, major) and an undefined comparison term. Rev 2 names the business lines and "percentage change in net
  premiums written ... from a year earlier"; its difficulty is unmeasured (raw: tasks/aq-01278/notes/feedback-q02.md).
- 2026-10-07 (aq-01430 q01, user report: "set q01 status as submitted and accepted_tier as Easy
  Tier"; tier line and tested wording not supplied): the overlapping-windows mechanism (EU coal
  2019 -> 2021 = -34 TWh from two editions' windows net of the 2025 step) reached the Easy tier, below
  the bundle's Medium target and as the local review predicted (Easy ~47%, Medium ~12%). First platform
  result for window arithmetic across editions: it behaves like the partial-period family (Easy), not
  like an edition trap.
