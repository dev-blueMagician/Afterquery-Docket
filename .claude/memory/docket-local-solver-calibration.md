---
name: docket-local-solver-calibration
description: "The local Opus 5.5 blind solver beats every lever tried so far (numeric and qualitative) and checks prose against tables; it is the fairness check, not the difficulty target (the platform's reviewer model is); a local 'solved' means fair, and too-easy risk is read from its path. First platform pass (aq-00964 q01, Medium tier): an event reported in the latest release whose own later forecast is the decoy."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-09
  originSessionId: 0b3fd638-83b1-473b-8a9e-6c645eb2ec12
  modified: 2026-10-07T08:32:27.906Z
---

> **Frozen history (2026-10-14).** Measured mostly against the Low and Medium solvers. The current
> design rules are in [hard-playbook.md](reference/hard-playbook.md); where this note differs, the
> playbook wins. Open this note only for a specific case it records.

## Current rule

- A forecast amount derived as an outcome level minus a printed variance is no step for the high model (aq-04830 q01
  rev 0, 2026-10-14, Run 1, Version ad23aa, "Too easy", Low — · Medium — · High 3/3; attempt texts not recorded, routes
  unread). The larger of the two percentages by which 2024-25 tax and non-tax receipts exceeded the 2024-25 Budget's
  forecast amounts: Statement 8 prints each miss as growth rates (tax 3.9 vs 0.6, non-tax 7.1 vs 4.4) and as dollar
  gaps; only the Budget statement's flattened Table 3.1 prints the outcome levels; the growth gaps rank the wrong head
  (3.3%) against the gold 5.7%. It survived the quick test. My audit counted two unpointed steps; the premise's word
  "amounts" pointed at the level computation, so a noun naming the measure counts as pointing at the method. The page
  header read "Industry researchEasy or Hard only" and the check started at High. The page's note ("requiring no
  other document") does not describe a route to the gold. Record: tasks/aq-04830/questions/q01.md (Feedback log).
  Round 2 on the same bundle (two question-author agents reading every linked document in full, plus the caller)
  found no fair hook with an unpointed step for the high model. The shape that leaves none: three statements of one
  Budget that repeat each other's figures, an earlier Treasury paper whose figures are fair only with the edition
  named, an all-levels ABS release with no bridge to Commonwealth figures, and RBA research on other dates whose
  definitions must be named to be applied. Record: tasks/aq-04830/notes/hooks.md (h11-h28).
- Only Hard open: the check starts at the High level (aq-04469 q01 rev 0, 2026-10-14, Run 3, Version c8fc86, "Too easy",
  Low — · Medium — · High 3/3; the attempts' text was not recorded). Fifteen submissions to one review; a three-name list of
  submitters that cite one publisher's figures, the third citing the publisher's statistics handbook by title with no
  publisher named, the link printed only in another submission, plus a decoy that names the publisher without citing it.
  It survived the quick test (the easier solver missed); the high model was right three times in three, and the page said
  the citations "are all findable by searching the organisation name and its handbook title". A sibling hook (a report
  cited only by its chair's surname, the chair named in another submission) failed the quick test. So a hidden list member
  whose link is a name or title that another document prints is a search step: it held the easier solver once and the high
  solver never. Its "What to change" (ask which submitters use the statistics and which "merely refer to the organisation")
  is a cue toward a distinction the high model already made. Record: tasks/aq-04469/questions/q01.md.
  Second run on the bundle (q02 rev 0, Run 4, Version c6e762, same day): a three-name list defined by other submitters'
  mentions of a submitter's own submission, two members reached only through "their" in a dairy submission (one about
  41,000 characters in). Quick test survived; Too easy, High 3/3; Coach: "Reached the gold answer via a keyword scan: the
  three qualifying references all use the word 'submission'". So with only Hard open on a bundle of policy submissions,
  a member that reading for one word reaches is cleared by the high model whatever the link (title, surname, pronoun),
  and a sibling whose deciding step is the same passage (q03) is not worth a run. After three such rounds, report the
  options instead of a fourth search-type design; what is left needs a membership judgement, which risks "One
  defensible answer". A Too easy run is refunded ("Too easy, so you got an extra run"), so its cost is the user's time.
  Record: tasks/aq-04469/questions/q02.md, q03.md.
  Same pattern, aq-04466 q01 rev 0 (Run 1, Version 70e8a6, same day, "Too easy", Low — · Medium — · High 3/3, run refunded, attempt
  text not recorded): a two-member list of submitters backing a proposal from CAMAC's 2014 discussion paper while naming
  CAMAC, one member dated only by another submission's answer; the question's own "2014" reached that answer. The page's
  "What to change" (drop the naming condition) would have let three more submitters count on content, so it was not used.
  Record: tasks/aq-04466/questions/q01.md.
  Same morning on aq-04112 (q04 rev 0, Run 3, Version daf97b): measured Medium recipe 9's shape (a written-evidence
  list held against two hearing transcripts, minus the bodies that sent witnesses, one member named only by a short
  form in an MP's aside, one decoy whose witnesses sit only in the report's list of all hearings) went straight to the
  high model and was Too easy, High 3/3; the page's note: the lists "pre-compute the set difference, leaving only a
  literal string match". The same bundle's runs had started at Low (Run 1) and Medium (Run 2) the day before, and
  every run captured in the workspace on 2026-10-14 started at High (five runs, four bundles); the pages give no reason.
  So a recipe measured at Medium is no design for a high-level run, and a quick-test survival says nothing about it.
  Record: tasks/aq-04112/questions/q04.md. Next run there (q01 rev 1, Run 4, Version cfc84c), the aq-02157 q04 shape (a
  three-year cost built from a table's unit costs, one line paid once per company, the table's printed total for 50
  workers beside a case of 150): Too easy, High 3/3; the notes say the high model included the one-off fee and that
  the printed total "also allows direct scaling". One unscaled line inside a table is no step for the high model.
  Record: tasks/aq-04112/questions/q01.md.
  Academic-paper bundle, same day (aq-04819 q01 rev 0, Run 1, Version 833345, "Too easy", Low — · Medium — · High 3/3,
  attempts' text not recorded): a total over a systematic review's included studies in which parents took part, whose
  second member is counted only in the study's own results (review row: "59 family groups (at least 1 parent and 1
  adolescent ...)"; the study, also in the bundle: "59 parents and 61 adolescents"), 152 + 61 = 213. It survived the
  quick test; the high model was right three times in three, and the page's notes call it "two direct lookups plus
  trivial addition" with the question's set phrase "a strong pointer". The page had shown Medium 0/1 at capture three
  hours before the run, which still started at High. On the same bundle the quick test (easier solver) cleared a
  review row's missing setting supplied by the study (stadiums) and two citation links (a cited author misspelt in the
  review's table, "Russel"; an unsigned paper matched to its citation by content). So in a bundle of papers where a
  review summarises papers that are also in the bundle, a review-to-study link is a search step for the high model,
  and a citation link is one for the easier solver too; the Coach's rewrites (widen the set; count all participants)
  kept the same link with printed figures. Record: tasks/aq-04819/questions/q01.md, notes/ideas.md.
- Quick tests on seven unrelated EPA ozone/PM10 proposals (aq-04807, 2026-10-14, user: "only i03 survived", no panel):
  too easy for the easier solver were (i01) a truncation-slack pair, the smallest one-year change that makes one named
  monitor's design value violate and another's attain (1 and 5 ppb; rounding gives 0/6, the DV-unit shortcut 3/6), and
  (i02) a union of concurred smoke days over two areas whose prose says "July 17-18" while the concurrence table stops
  at July 17. The survivor (i03) was a two-area list whose second member is one background sentence of a proposal on
  another subject, worded "Indian country" where the question says "tribal lands". So the easier solver handles a
  printed rounding rule run backwards and a table-against-prose check; it misses a member under other wording in an
  off-topic document. Record: tasks/aq-04807/notes/ideas.md. The survivor, in the user's own wording (q01 rev 1), then
  ran straight to the high model: "Too easy", Low — · Medium — · High 3/3 (Run 1, Version 1d2bff; attempt texts not
  recorded; Coach: "answerable by keyword retrieval on 'tribal'/'Indian country'"). My step audit had counted no
  unpointed lookup and said so before the run; the count held. The page's "What to change" proposed adding the class the
  tribal lands kept, which one document never states (Coachella's Indian country), so it was not adopted.
  Record: tasks/aq-04807/questions/q01.md (Feedback log). The next design (q02: a member that exists only inside a citation
  footnote both 179B(b) proposals repeat, Imperial County, with no name or synonym in the question) survived its quick
  test and was again Too easy at the High level, High 3/3 (Run 2, Version 2b862e). So on this set the high model found a
  differently worded member and a footnote-only member every time; both designs had counted no unpointed lookup.
  Record: tasks/aq-04807/questions/q02.md.
- Measured Medium recipe 9, two lists matched with one member in an aside (aq-03707 q03 rev 1, 2026-10-13, Run 3,
  "In band — Medium tier", Low — · Medium 2/6 · High —, every ticked document "Needed", closed-book missed,
  submitted at Medium): a final report summary and twelve submissions on one market study. The set "countries
  any submission describes as a four-player supermarket market" has seven members over three submissions: four
  in one submission's quotation of its economists, four in another's list (with provinces and metro areas
  beside them), and one only in a third submission's aside, in a table row on another topic, under an informal
  name and with the number as a digit ("Even Aussie is a 4-player market"). It is matched against a lettered
  list of nine countries deep in the longest submission; gold two names. Two results bracket the band and show
  where each solver stops. Rev 0, "a submission ... credits with four main supermarket players": Between
  levels, Low 0/5 · Medium 1/7 · High 3/3 ("Too hard for the medium model but too easy for the high model").
  Rev 1, "any submission ... describes as a four-player supermarket market", nothing else changed and no
  clause added: Medium 2/6, in band (the check started at the Medium level). From the attempts' own text in
  both runs: every scored attempt found the lettered list; the middle solver nearly always found both
  prominent four-player lists; no low or recorded middle attempt found the aside, several after opening that
  submission by name (two assigned the other submission's list to it), and every wrong middle answer was the
  one-member answer. The right middle attempts have no recorded text, so it is not established that the
  closer term moved the result: one more right attempt out of one fewer. The region-against-country decoy
  caught nobody at any level; two low attempts read "a submission" as one particular submission. Use: (a) on
  "Too hard for the medium model but too easy for the high model" with Medium open, the page's heading says
  make it harder (for the high solver); the repair that measured in band went one notch the other way, by
  restating the membership test in the documents' own kind of term with "any", not by a clause such as the
  Coach's "(however phrased)"; (b) declare only the lazy-default wrong answer as the failure mode (here the
  one-member answer was every wrong answer in both runs; a predicted decoy mode was withdrawn after Run 2);
  (c) on the same bundle a derived figure with one unpointed step (q02, the complement of a cost share
  printed in a paragraph on another subject) measured the other side of the band, Low 0/5 · Medium 4/7: a
  fact a persistent re-read finds is too easy for the middle solver, an aside that survives a named check of
  its document is not. Records: tasks/aq-03707/notes/feedback-q02.md, feedback-q03.md.
- The difficulty check can start at the Medium level, with its own rule (aq-03736 q01 rev 1, 2026-10-13, Run 3,
  Version 6bde93, on a set whose Easy slots were full; the page gives no reason): the tiers line read "Low — ·
  Medium 5/6 · High —", the verdict "Too easy", and the page said "Medium model: three solvers try up to 3
  times each. Ready when at least two get it wrong twice and one gets it right twice. A level stops as soon as
  more attempts could not change the result." and "Too easy, so you got an extra run." So on such a set a
  Medium result needs the medium solver wrong about two times in three, and neither the quick test (easier
  solver) nor an earlier Low count says anything about that. What was measured: the same six-step dated case
  that held the low solver four times in five at one closing clause (Run 1) was solved by the medium solver in
  every attempt whose text is recorded; each quoted the clause. Its one miss (26 for 38) took the right year
  and read the proposal's first deadline as the first full calendar year (30 April 2028), the second reading
  already on file; the page's note again named the wrong step. The rewording that took the documents' phrase
  out of the question survived a quick test and changed nothing measurable. So: (a) when the open tier is
  Medium or higher, audit a design against the medium solver: a clause that only has to be read to its end is
  not a step for it, and what has held it elsewhere is an inference no sentence states or a member outside a
  complete-looking set; (b) a lone quick-test survivor whose sibling wording already measured below target is
  not evidence, and a second quick test or a different hook comes before a run; (c) the Coach's remedy here
  (write the interpretation into the gold, or use a 31 December year-end) would have changed nothing a solver
  did. Record: tasks/aq-03736/questions/q01.md.
- A join of two flattened address tables on a shared road name is solved by the high model (aq-04421 q01 rev 0, 2026-10-14,
  Run 16, version fa81d1: "Too easy", Low — · Medium — · High 3/3, the check going straight to the high model on a set
  whose Easy and, apparently, Medium slots were full). Which firms added to the Entity List in September 2025 have premises
  on the same road as a site on the October 2024 validated end-user list: two members, one on a road spelled alike in both
  tables (Guoshoujing), one needing a spaced variant ("Feila" against "Fei La"). It had survived the quick test. No attempt
  text was recorded (routes unread); the page's notes call it "a near-verbatim string match". So neither a spelling variant
  nor a retrieval through two long tables is a step for the high model. The one repair left on that hook adds a member whose
  partner address is split by the table's interleaved item column ("177 Bi 2B350.d, 2B350.g, Bo Road"). It survived the
  quick test and measured the same (rev 1, Run 17, version 511a2b: "Too easy", Low — · Medium — · High 3/3; the page:
  "Again matched the three roads verbatim"). So a surface obstacle on a join the high model has cleared (a spelling
  variant, a string split by table layout) is no step for it; the hook was closed. Evidence:
  tasks/aq-04421/verdicts/AQ-04421_difficulty_2026-10-14_0942.txt and _1033.txt.
- A list whose gold is the whole set one document shows, with the other document only confirming it
  (aq-03736 q02 rev 0, 2026-10-13, Run 2: Low 2/5, gate failed, "Your answer can still be reached without
  document 3"; screenshots only, routes unread): which guidance the adopted directive requires of the
  Commission where the proposal's articles only allowed it (two items). I had narrowed the ask from five
  discretionary steps to guidance to avoid an arguable item, and the narrowing made the gold equal to both
  of the proposal's optional guidance items, so "guidance became a duty" answers it with the adopted text
  deleted. The step audit (two unpointed closing sentences in different passages) said nothing about that.
  So: (a) before offering any sketch, delete each ticked document and write down what a solver would then
  answer, from the rest and from recall of a well-reported law; if it is the gold, the document is not
  needed; (b) redo that after every narrowing; (c) a filter document is guessed when the qualifying option
  is the natural one (as aq-02408 q01 already showed); (d) the page's own remedies (ask for article numbers
  and exact wording; put citations and an exclusion rationale into the gold) are untested wordings that
  break the short-answer rule; (e) "List the items in any order." drew the rule-10 advisory "an
  answer-protocol tail" while clearing "Answer format stated"; the floor now WARNs on it, and "List them
  alphabetically." (aq-03170) is the order wording with no recorded advisory. Record: tasks/aq-03736/
  questions/q02.md. Same bundle, same day, two list differences that passed delete-and-guess on both texts
  were quick-test failures (user report, no panel): the one kind added to a list, sitting inside a grouped
  entry of a 590-word sentence beside a look-alike name, and the treaties gaining an import ban, with one
  treaty named differently in the two texts. So the end-of-sentence miss measured on q01 does not carry
  over to comparing two lists: the easier solver tabulates them.
- A posed case run through two versions of one legal text, with five steps the question points at and one
  it does not (aq-03736 q01 rev 0, 2026-10-13, "In band — Easy tier", Low 1/5; one result): a company with
  a stated head-count, turnover and July-June year; months from its first statement deadline on the
  proposal's timetable to the end of the first financial year the adopted directive's statement must cover
  (38). All five low attempts cleared every pointed step: entry into force from the publication date, the
  proposal's 2-year offset, "by 30 April each year", and a two-threshold group test built so that the
  head-count alone fits the earlier group (nobody took it; three said why in words). Four then stopped at
  the head of the group's sentence ("from 26 July 2028 ...") and never reached its closing clause ("with the
  exception of ... Article 16 ... for financial years starting on or after 1 January 2029"): none of the four
  traces contains it, and one wrote "a transitional provision? Not in Article 37". The fifth quoted the
  clause and was right; the strongest solver quoted it. Closed-book, the low model recalled the adopted
  text's entry into force and all three phase-in dates and thresholds, not the clause, and two attempts
  without the adopted text answered from those recalled dates. So: (a) on a rule-chain scenario count only
  the steps no word in the question points at; one such step is Easy; (b) the easier solver's miss on a
  long provision is its end, so an exception closing a long sentence holds about four in five and no more;
  a second one must sit in a different passage, and a step added inside the same sentence makes solvers
  read it to the end (the aq-03143 warning); (c) a threshold trap with both figures stated catches nobody;
  (d) headline dates and thresholds of a well-reported law are recalled exactly, so a ticked document that
  supplies only those is exposed at the Document check; (e) the page's "Where it left your evidence" lines
  called all four misses "the wrong application phase" though each chose the right phase. Routes:
  tasks/aq-03736/questions/q01.md (Lever checks, Feedback log). tools/verdict_summary.py now prints, per
  attempt, how much of each Evidence quote the trace echoes and whether the quote's end is echoed.
- Recipe 7 does not carry over when the members outside the complete-looking set are a whole dated group in the
  list the question names (aq-03950 i01 and i04, 2026-10-13, quick tests, user report "i01, i04 failed", no
  panel): a committee report lists 24 witnesses by hearing date; the bundle's transcripts cover 21, the first
  panel of one hearing having no transcript. Asked how many witnesses "listed in the ... report" gave evidence
  at hearings one MP attended (attendance only in transcripts; gold 9, transcript headers give 6), and in a
  two-member difference form (gold 6), the easier solver answered both. On aq-02933 the outside member was one
  figure in prose that the solver had to accept beside a table; here the phrase sent the solver to a list in
  which the group simply sits under its date, so nothing had to be noticed. Check before using recipe 7: once
  the structural scope is followed, is there still a member to accept, or only a list to count? Same bundle,
  same day: a three-name list with one member shown only in another witness's answer (recipe 6 opening,
  "Judging by all the evidence the committee heard") and a two-condition filter (remote and sent written
  evidence, one year) both survived the quick test. The list then measured Medium (below).
- Measured Medium recipe 6, list form, in hearing transcripts (aq-03950 q02 rev 0, 2026-10-13, "In band — Medium
  tier", Low 0/5 · Medium 2/6, first run, submitted at Medium): a committee report and six transcripts; "Judging
  by all the evidence the committee heard, which witnesses, if any, held or had held a role at" a named body.
  Two members carry the body in their printed titles; the third is a hotel chief executive whose seat on its
  board is one sentence spoken by another witness three months after his own session. All 17 attempts read. Every
  low attempt went witness list by witness list and equated a role with a title; two wrote that they should check
  for other mentions and re-read titles. Three medium misses went one step further (a search for the body's name
  in the report, a look at what witnesses said about it) and stopped at what each witness says of himself; the
  member's own remarks mention working with the body and no seat. Nobody below the strongest solver used the
  report's unnamed pointer ("A Welsh representative sits on the ... board"). All nine recorded wrong answers
  were the titled pair, the one declared failure mode. The strongest solver found the sentence in two of three
  attempts that had its document, and with every document weighed five times whether a board seat is "a role"
  ("not really an employee") before including it: when the hidden member qualifies in a weaker form than the
  obvious ones, use the word that covers both, put its passage and a corroborating one in the evidence rows, and
  say so in a reasoning step. Against aq-03170 (Hard with the same opening under the five-attempt gate, then
  Medium on its re-run under this gate the same day, so the two bundles agree; thirteen letters): six transcripts
  and a plainer sentence gave Medium. Against aq-03423 q04 (too easy): there the sentence sat in a response
  about the asked property; here it sits in a third person's session whose own witness list already supplies
  a member. Two right medium attempts had no text recorded. Evidence:
  tasks/aq-03950/verdicts/AQ-03950_difficulty_2026-10-13_1354.txt; tasks/aq-03950/notes/feedback-q02.md.
- A printed period average of a stock beside the yearly balances it was built from (aq-03635 q03 rev 0,
  2026-10-13, "In band — Easy tier", Low 2/5; one result): a company's submission prints its three-year average
  capital employed (2,085) only as a number in jumbled chart text and lists the four year-end balances in an
  appendix. The average is of each year's opening and closing balance, so the plain mean of the last three
  balances is a different figure (2,292.67). Asked for a ratio on that company's "own average capital employed"
  with the years named, every attempt (five low, and the strongest solver with every document) computed both
  figures. Three low attempts kept their own mean; two low attempts and the strongest solver took the printed
  figure because the question's words were the chart's title. Nobody, the strongest solver included, worked out
  why the two differ (it tried the four-year mean and gave up). So: (a) never rest a gold on an averaging
  convention the document does not print as a figure; (b) with the label's words in the question, trusting the
  printed figure over one's own table average splits the easier solver about two in five, which is Easy; (c)
  the same solver averages flows (earnings) correctly, and in a quick test it built yearly ratios on
  opening-and-closing capital once the measure was spelled out as return on average capital employed (too
  easy), so the yearly form of such a hook is closed; (d) a declared printed look-alike (14%) and a
  rounded-prose route (22% less "approximately 9%") caught nobody while the operands were named. Rev 1, with
  only the chart-title words removed, was then blocked by the form's "One defensible answer" (its two solvers
  answered 4.4, the rounded prose, and 3.7, the own mean; "Each description fits one thing" named the open
  term). So such a hook has two states and nothing between: the printed figure named in its label's words is
  Easy, and without them the question is vague. Do not spend a run on a half step that restores the label word.
- Measured Medium recipe 8, a total in which a rival's sentence releases a grouped count (aq-03557 q01 rev 2,
  2026-10-12, Low 0/5, Medium 1/5, both documents needed, closed-book missed, submitted): nine submissions to one
  market study. One retailer's submission holds every store count: two rival banners in its opening, its own two
  franchise banners as one figure, and a small rival's four stores in a list that resumes after a block of
  footnotes. Which banners run no loyalty programme is said partly there and partly in a rival's parallel answer,
  whose second sentence covers the first retailer's two franchise banners. Asked as one total, with the source of
  the counts named and the rule named as a kind ("that any retailer's submission says have no loyalty programme").
  From each attempt's own text: all five low attempts found the first retailer's statements or the rival's first
  sentence; none read the rival's next sentence, one line below, so none could take the grouped figure (four
  answered with the two plainly counted banners); none found the small rival's count, and four said outright that
  the document gives none. The medium solver assembled every input once and then looped on a split it did not
  need; one attempt was right. The strongest solver reached the total after first stopping four short. A decoy of
  the wrong kind (a pharmacy chain named in the same sentence as the qualifying banners, with its own store count)
  caught nobody at any level: the easier solver sets such an entity aside. Three attempts (one low, two medium)
  read the source phrase "the number of stores Woolworths provides" as that retailer's own stores and gave its
  franchise figure; the strongest solver weighed that reading four times and rejected it from the rule clause and
  from the rivals' counts in the same document. So the holding steps were a deciding sentence about the other
  party's banners, adjacent to the sentence the easier solver quotes, with a grouped count that is unusable
  without it, and a count in a list broken up by footnotes. This is recipe 6's dependency in numeric form: on
  aq-03423 q04 a plain deciding sentence was quick-test too easy as a list of names, while here a missed sentence
  changes a sum and the solver has no list to notice a gap in. A source phrase naming a party that has figures of
  its own keeps an own-figure reading however it is worded (as aq-02028 q02): here it added medium misses, which
  is difficulty from the question's wording and a point a reviewer may raise. Evidence:
  tasks/aq-03557/verdicts/AQ-03557_difficulty_2026-10-12_2319.txt; tasks/aq-03557/notes/feedback-q01.md.
- Recipe 8 measured Medium again, against the list form of the same member (aq-03993 q02, 2026-10-13; a
  committee report and three hearing transcripts; three-solver medium gate; submitted at Medium). The report
  prints how many scheme-funded reporters each of three publishers took, and its witness list shows that one of
  them sent a witness. A community publisher's director says in a clause of an answer about grant funds, in
  another document, that his firm has two such posts. Asked as a list of witnesses whose own organisation has
  such reporters (rev 0, three names among eight look-alikes): "Between levels", Low 0/5 · Medium 4/7. Asked
  as the number of such reporters "the evidence place[s] on the staff of organisations that sent a witness"
  (rev 1, gold 77 = 75 + 2): "In band — Medium tier", Low — · Medium 2/6, both documents needed, closed-book
  "About 30". In both runs every recorded miss lacked that one clause and nothing else: the list misses
  left the name out, the total misses answered the report's 75, and every recorded medium attempt set the
  look-alikes aside (a membership body's "our members employ perhaps a dozen", a television station with a
  contract and no witness, the funder). The strongest solver also took 75 for the answer first and found the
  clause on a later pass. So with a member stated in the candidate's own testimony, a per-candidate list
  was too easy for the medium solver and the total against a complete-looking printed figure was in band.
  Against aq-03950 q02 (list form, Medium): there the member was shown only in another witness's answer.
  The same bundle's other design, a figure whose correcting part sits in one witness's sentence with nothing
  in the question pointing past the report (average grant, fund £2 million but "about £1 million was grant
  funding"), was Between levels the other way twice: Low 0/10, Medium 1/13, High 6/6. Limits: one run per
  form; the low level was not run on the total; the recall risk on record (the publisher's allocation is a
  trade-press figure) did not show in two attempts without the report. Evidence:
  tasks/aq-03993/verdicts/AQ-03993_difficulty_2026-10-13_2056.txt (total) and
  tasks/aq-03993/verdicts/AQ-03993_difficulty_2026-10-13_1739.txt (list); tasks/aq-03993/notes/feedback-q02.md.

- Measured Medium recipe 6, an unprinted period remainder across two documents (aq-03120 q02 rev 2, 2026-10-12,
  Low 0/5, Medium 2/5, both documents needed, submitted): one organisation's results are quoted for the first
  half in one document and for the full year in another, and no document prints the second half. Ask for that
  remainder as a plain amount, in the form of the printed look-alikes, with no cue to calculate, and name the
  period by its structure through an event dated after it: "the half of its financial year that last ended
  before" an announcement whose date sits only in a footnote. Seven versions of the hook show what each change
  does: a plain event inside the period, taken from a third document, was Easy at Low 1/5 (the low model
  placed it four times in five and then gave the printed half-year figure); an event whose name carries the
  other period's label ("first-half results") was blocked twice by "One defensible answer"; a cue to calculate
  (a percentage "on reported figures", or "stated or implied") was quick-test too easy twice; a period term that
  is also a reporting label ("financial half-year") gave the same Medium counts with "Answer not supported",
  because the high model took the label's period too. In the passing run the misses were of two kinds: taking
  the half with its own printed results as the one that last ended, and placing the half correctly but giving
  a printed figure. The form's "Answer matches a stated figure" advisory warns on this shape; it is advisory.
- Measured Medium recipe 6, a list member shown only by another document (aq-03170 q01 rev 3, 2026-10-12, Low 0/5,
  Medium 1/5): thirteen comment letters on one proposal; each commenter states its own earlier letters, and one
  commenter's second letter is named only in a different commenter's body text. Asked as "which commenters had sent
  more than one earlier comment letter", with the counting rule stated as a kind ("including letters only others
  mention"). Without the rule the form's "One defensible answer" check blocked it (both form solvers on the
  own-account pair). With it, nine of ten low and medium attempts still went document by document through each
  sender's own account and summarised the deciding letter by its opening paragraph; the low attempts spent the
  clause on third parties cited in footnotes, two medium attempts read it as letters not included in the bundle, and
  the one right attempt re-read the clause and then scanned. The strongest solver's every-document attempt
  compiled every cited letter per document and found it. So a member evidenced in another document's body text has
  three measured states here: no rule = blocked, rule named as a kind = Medium, and the evidence named by its
  structure with no word about what to count (rev 4, "Judging by all these letters together") = Hard, Low 0/5,
  Medium 0/5, High 1/5 (Run 2, 2026-10-12, submitted at Hard). In that run all fourteen wrong attempts gave the
  own-account pair. Twelve never mention the deciding letter; one strong attempt half-remembered it and looked in
  the wrong document; one quoted the sentence three times and set it aside (it read the question as what each
  sender says of itself and doubted that the letter was a second one). Both right attempts quote the opening
  phrase as their reason to count another letter's reference, and both prove the second letter is separate from
  two different links, one of them in the either-or document. So on this shape an "including ..." clause is a
  cue worth a whole tier, and the gold needs a second passage that shows the hidden member is distinct. Single-
  source filler members cost no attempt anything, and the form's document check would not let their documents be
  marked, which leaves the explanation naming unticked documents (a known reviewer send-back; unresolved here).
  Outcome, 2026-10-13: the reviewer returned it for those ticks and the forced re-run of the same question (Run 3,
  three-solver medium gate) was Medium, Low 0/5 · Medium 2/6: the two recorded medium solvers gave the own-account
  pair twice each and the third, whose text the page does not keep, was right on both tries. With aq-03950 q02
  that is two Medium results for the evidence-named opening under the three-solver gate; its one Hard result was
  under the five-attempt gate. Do not plan a Hard result on this opening.

- A count over lists that share printed ids is Between levels (aq-03423 q03, 2026-10-12, Low 0/5 · Medium 5/5,
  after surviving the quick test): three respondents to one consultation each print the numbers of the questions
  they answer (22, 12 and 9 of 47); asked how many none set out to answer, and the lowest. Every low attempt gave
  the lowest (Q8) and missed the count (13, 3, 5, 5, 13) by mixing up which document carried which headings; every
  medium attempt listed the 47 and ticked each list. Unlike recipe 5, nothing had to be matched by content or
  inferred, so care alone solved it. No fair second condition was found: each either states a rule the careful
  solver then applies or shrinks the enumeration that stopped the low solver. On the same bundle (policy
  submissions with few connected figures) six calculation designs were quick-test too easy: a printed look-alike
  figure with a subtraction, a time-limited offer priced over a year, a base backed out of a growth rate (as a
  share and as a ratio), a sign that reverses against a benchmark row, and a ranking split across two documents.
  Recipe 6's list form did not carry over at the quick test (aq-03423 q04 rev 0, 2026-10-12, user report "too
  easy", no panel): three submitters had become an MVNO or tried to, one of them shown only in another
  submitter's response, asked with the rule named as a kind ("including any whose attempt only another submitter
  reports"). There the deciding report is one plain sentence naming the member and the asked property, in a
  response that discusses that property throughout; on aq-03170 the deciding letter sat among thirteen and the
  property was one each sender reports for itself. Rev 1 (pooled-evidence phrase) and the no-rule wording were
  both quick-test too easy as well (user, 2026-10-12: "both are too easy"), so the member was never hidden there:
  check, before using recipe 6, that the deciding report does not name the member and the asked property together
  in a document about that property. Bundle closed after three rounds with no candidate; release recommended.
  Evidence: tasks/aq-03423/verdicts/AQ-03423_difficulty_2026-10-12_1737.txt; tasks/aq-03423/notes/ideas.md.

- Measured Medium recipe 5, membership matrix across templated documents (aq-02749 q02, 2026-10-11, Low 0/5,
  Medium 3/5, the first Medium on bytes where sixteen earlier designs were Easy or too easy): four near-identical
  proposals each enumerate the amendments EPA approves as the State's version (20, 20, 17, 11 entries, the shorter
  two not nested) and a fifth states its position as one grouped item that only the others itemise. Ask one count
  that needs every entry's set of States, from the side on which the grouped document counts in every entry
  ("lack an approved State version in exactly two States"). Every low attempt read the grouped item as covering
  only the provisions it names (answers 0, 0, 0, 0, "One"); they also read the shortest
  enumerated list as approving everything. Both medium misses misread the middle list (17 entries taken as the
  full 20: 9; the wrong three taken as missing: 6). The low model reads an explicit "not being approved" list (4 of
  5 did) but not non-approval it has to infer, from a grouped item or from absence in an enumerated list. The same matrix asked for one entry was Easy (aq-02626 q04, Low 3/5). Build it by finding the
  one miss earlier runs on those bytes actually show and making it decide every counted cell
  ([[docket-start-from-measured-misses]]).
- Measured Medium recipe without editions (aq-02501 q01, 2026-10-09/10, two runs): ask which items a rule
  actually helps ("mentions it vs does it") when its preamble discusses the obvious items at length and names
  one more only in a late clarifying section (character 72,900 of 92,900), beside two look-alikes it says the
  rule does not apply to or impact. Low 0/5 both runs (it answered with the rule's bars and procedure, or whole
  categories, never the item types); Medium 2/5 then 1/5 (most stopped at the two obvious items). A plain second
  ask (a date every attempt got right) did not move the band. The quick test separated it from two-lookup
  arithmetic and list counts on the same bundle (both "too easy"). Rest the condition on what the document
  itself says about the rule's effect: the same hook asked through public regulation text failed "Needs the
  documents" ([[docket-general-knowledge-check]]), and its second document must carry its own gold component
  ([[docket-series-editions-necessity]]).
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
- A one-to-one join from a plain-language list into a numbered list that restates each item is a lookup (aq-01432 q03,
  platform difficulty check 2026-10-07: "Too easy", Low 5/5). The question named the short guide's theme heading. All five
  attempts quoted it, matched its seven clauses to the full guidance's numbered banned practices (five almost word for word,
  two by ordinary meaning) and sorted. The full saved page shows every low attempt weighing the adjacent same-topic decoy
  (practice 21 beside 22) and setting it aside on its wording; one first wrote it into its list. Every local solve had done
  the same, and only the committed answer counts. So a decoy the local solvers raise and reject is no trap for the low model
  either, and a which-items join needs at least one member whose counterpart its own wording does not identify. Check the Coach's account of the documents before acting on it. Here it said the guide prints the paragraph
  numbers, but the guide prints none and the traces say the full guidance supplied them. Likewise aq-01333 q02's Coach cited
  a restated total that does not exist.
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

- Measured Medium recipe (aq-02157 q04, 2026-10-09, "In band — Medium tier", Low 0/5, Medium 2/5): a derived figure
  that no document prints, taken from a table rule the document never names in the question's words (Doc 4's
  "Highest of" duty table makes £347.86 per 1,000 the floor, "MET" never expanded; per 1,000 to per 20), set against
  a printed figure in another document ("at least a £8.46 excise duty on a packet of 20"), with two printed same-label
  decoys: a look-alike beside the table (the IA's £7.98 average-pack duty) and the same series' other edition (the
  consultation's £7.87). Low took the explicitly printed per-pack decoys (Doc 1's £7.87 as the start 4/5, £7.98 1/5);
  Medium split between the look-alike (3/5) and the derived floor (2/5); High had solved the same route 5/5 in Run 2.
  Printed per-pack figures attract the weaker models, and a floor that must be derived separates Medium.
- Measured Medium recipe 2 (aq-02486 q01 rev 2, 2026-10-09, "In band — Medium tier", Low 0/5, Medium 2/5): two agencies'
  parallel fee rules applied to one stated request (a news reporter's 216 photocopies from each), asking the total paid.
  One agency forgoes totals of "$25.00 or less" in the paragraph after its free-page rule; the other prints the same $25
  only as a notice threshold ("mentions it vs does it"). Low overgeneralised the no-fee rule to both agencies (3/5) or read
  one agency's paragraphs as the other's; Medium missed the rule (2/5) or overgeneralised it (1/5); the high model missed it
  on its first every-document attempt and the platform retried. What made it count: every trap route has its own magnitude
  (missed rule 34.80, both waived 0, linked rates 46.40, gold 11.60). The same content asked as "A minus B" was Easy (Low
  2/5) because the rates were 2:1, so the missed-rule route was the negated gold and the grader ignores the sign. Two
  independent authors had called this family "too easy-shaped"; the measured lesson is that a rule application is not a
  lookup when one document's rule is absent from the other and the look-alike mention invites carrying it over.
- Measured Hard recipe (aq-02562 q01 rev 1, 2026-10-10, "In band — Hard tier", Low 0/5, Medium 0/5, High 1/5; submitted
  at Hard Tier): recipe 2's shape on two USDA payment programs. One stated case (a four-partner general partnership, one
  partner over the $900,000 AGI bar), asked as the most both programs could pay combined. MASC (Doc 2) has a 75 percent
  farm-income exception; ASCF (Doc 7) prints the same bar without one. The partner's income (70 percent crops, the rest
  seed sold to farmers) clears the exception only through Doc 2's definitions: a 66.66 percent gate admits production
  inputs, which include seeds. 13 of 15 attempts carried the exception into ASCF ($1,500,000); the high model argued that
  Doc 7's "7 CFR part 1400, subpart F" reference imports it. That showed as a non-blocking "may be too vague" advisory, and
  the gold was kept on the documents. Only one attempt took the crops-only route ($1,125,000). The same family with "all
  from farming" in the question (rev 0) was quick-test too easy: every rule was reachable from the question's own words.
  Lesson: untie the step the question would otherwise settle, so a definitions section decides it. The asymmetry trap,
  which the strong models then fell into, did the separating.
- Measured Medium recipe 3 (aq-02564 q02 rev 1, 2026-10-10, "In band — Medium tier", Low 0/5, Medium 3/5; submitted at
  Medium Tier): for parallel documents that share every rule, so there is no asymmetry to carry over and no single step
  is a trap. One natural billing scenario in which each party-and-feed cell follows a different stated rule: a host with
  two hosted subscribers, one on one exchange's feed only, the other over one exchange's user cap but within the other's,
  asked as the host's total monthly bill ($2,375). Four independent steps, each easy alone: caps applied per feed; the
  host's credit decided per program; the host pays its hosted subscribers' set fees; its own users priced from a rate
  printed only inside a footnote calculation. Low: three attempts left the subscribers' set fees off the host's bill
  ($875), one left user fees unpriced ($1,750), one kept the credit ($2,125). Medium kept all four steps 3 of 5 times.
  The same rules with one or two steps were solved: a footnote decoy and a host bill with per-firm counting were
  quick-test too easy, and the one-inference version (rev 0) was Easy, Low 2/5. Lesson: when parallel documents have no
  asymmetric rule, raise the number of independent, document-grounded steps inside one scenario (never conditions in the
  question's wording), and give every wrong route its own magnitude. Keep scenario numbers the documents do not print out
  of the reasoning by naming the printed threshold instead ("over the 10,000 maximum").
- Read the traces before designing a repair, and do not trust a predicted trap. On aq-02564 the declared trap missed
  three times: the footnote decoy (quick test too easy), the eligibility inference (Run 1: all five low attempts made it)
  and the per-feed scope trap (Run 2: no attempt of ten fell for it). Each time the real separator was an undeclared,
  ordinary step. So after any difficulty run, list every attempt's committed number and name its route first
  (`python tools/verdict_summary.py <capture>`); the platform's own "Final answer" pick and "Where it left your evidence"
  line were wrong for several attempts. One quick test is one draw: the host-pays design was "too easy" once and then
  lost 3 of 5 low attempts inside recipe 3, while the quick-test survivor measured Easy. Failure modes sit outside the
  tested content, so when a run arrives before Submit, offer to re-declare them from the observed wrong answers.
- A scenario question must not print the share (or other figure) on the deciding metric. On aq-02686 q01 rev 1
  (2026-10-10, Easy, Low 3/5) the trap was a clarification in a final rule's responses to comments (a board seat
  counts at its board voting power); the scenario said two of five directors "casting 20% of board votes", and
  three of five low attempts took that 20% at face value and were right without reading the clarification, while
  the two that counted seats were wrong. Four other explicit rule steps were each 5 of 5. So give the facts from
  which the deciding figure is derived, and count on a rule lookup to separate nothing. Derived is not enough
  either when the derivation is just putting the question's own pieces together: rev 3 (10% owned plus notes
  convertible into another 20%; one director of seven who alone has two votes) was "too easy" at the quick
  test the same day (user chat, one draw, no trace). A clarification that confirms the natural computation is
  no trap; it would have to overturn it.
- A quick-test survival or a low score can be produced by the question's own ambiguity. On aq-02686 q02 rev 0
  (2026-10-10, "Answer not supported", Low 2/5) every attempt did each document step; the misses, and all three
  high-model attempts, came from reading "Barring FEOCs, it exports ..." as "leaving FEOC status aside". Before
  treating a survival as difficulty, check that no route to a wrong answer runs through a phrase of the question
  (a local blind solve does not show this: it read the phrase the intended way). In a scenario, state a policy
  as its own plain sentence and list candidates as orders or prospects; never assert the action the policy is
  meant to rule out.
- A scenario about a real, named actor must not state invented events as fact where the bundle records the
  real ones. aq-02750 q04 gave CDC 43 and 19 comments on two orders whose later notices report five and
  none; the author found it only on reading Run 4's traces, after four runs (one low attempt used the
  record to drop a batch). At sketch time search the bundle for the real counterpart of every invented
  figure; if one exists, write the case as a supposition ("Suppose ...", "would meet") or use an unnamed
  actor. Guide rule 9(a): the question asserts nothing the documents do not confirm.
- A rule that differs between two look-alike procedures holds the low model and not the medium one. On
  aq-02750 q04 rev 0 (2026-10-10, Between levels, Low 0/5 · Medium 5/5) every low attempt carried the orders'
  mail rule into the interim rule's portal-only block, and every medium attempt read the block. Printed
  deadlines, a boundary day and a label lure cost neither level anything. To land Medium from there, give
  the medium model work of another kind (values it has to derive, not more printed lookups); do not add
  groups of the kind it already clears.
  Derived dates did not do it either: with arrival dates the solver must work out, the low model read the
  block 4 of 5 (rev 1, Too easy) and 3 of 5 (rev 2), against 0 of 5 with explicit dates (rev 0). The same
  trap swings between Between levels and Easy or Too easy on how much lookup the rest of the question makes
  the low model do; it has no measured Medium form.
- Document check, restated notices (aq-02750 q04 rev 2, Run 3, 2026-10-11): when a later edition restates an
  earlier one's rule loosely ("a 15-day comment period") and only the earlier edition prints the exact date,
  the high model without that edition computes a fallback date from the loose phrase and carries on. The
  earlier edition counts as needed only if some item falls between the fallback date and the printed date,
  so that the two give different verdicts. An item that is in (or out) under both leaves the document "not
  needed" even though it is the only place the date is printed. Check each ticked document this way at
  sketch time; "the answer holds a day either way" is a warning sign for necessity, not a strength.
- Before acting on a "Too hard" run, read what the solvers were asked (they quote the question) and what the High
  model answered. In aq-02157 q04 both Too-hard runs (0/15 each) came from user paraphrases that changed the referent,
  then the asked quantity, while the gold stayed put. In Run 2 the High model gave the literal answer to the tested
  wording 5 of 5. Aligning the gold to that wording passed at Medium on the next run. The Coach's "Make it solvable"
  advice (name the MET, point to the table) read 0/15 as unsolvable; following it would have removed the look-alike step.
- On a set question the low model lists members from the table and finds whatever is tied to those entities; it
  drops a member printed only in prose elsewhere. On aq-02933 q03 (2026-10-11, Easy, Low 1/5) all five low
  attempts built the member split across a table and later prose (Nevada: 55 in Table 1, 188 in prose 29,000
  characters on), and four left out the member printed whole in one prose sentence 700 characters further
  (Georgia). So "assemble it from two passages" is no trap when the entity sits in the table, and one
  prose-only member is cleared about one time in five, which the gate reads as Easy (as aq-02505). No ask on
  the same members changes that. Whether anyone looks for the prose-only member depends on the frame, not on
  the solver's level: when a table fits the question's description on its face ("2019 hospice totals for
  several States", a table titled with that year), no solver at any level looked past it (aq-02933 q04 rev 1,
  Too hard, 0 of 15, three medium attempts with the sentence on screen); when the asked years are ones no
  table covers, the high model found it and the low model did one time in five. A step that asks which
  items a second document names in one explicit sentence separates nobody (15 of 15 right), even with a
  member named once. Stating the counting rule ("tabulated or only in text") then sent it straight to Easy,
  Low 3/5 (rev 2): one retrieval is found none, one or three times in five by the low model as the cue
  strengthens. A wording between those two, "Wherever CMS gives a State's 2019 hospice total" (rev 3), then
  measured Between levels, Low 0/5 and Medium 4/5: the low model read "Wherever" as the table, while four
  medium attempts stopped on the word, asked whether there was data elsewhere, re-read and found it. So the
  low and medium models differ in whether a single word in the question triggers a completeness re-check,
  and a hidden member does have a region where only the medium model finds it; the earlier conclusion here
  ("no Medium point") was wrong after three points. Tuning the cue word was the wrong
  repair: a softer completeness word ("Across every State with a 2019 hospice total from CMS", rev 4) was
  blocked by "One defensible answer", both form solvers on the table figure. What passed was naming the
  universe the member sits in, with no word telling the solver to look ("every State whose 2019 hospice
  total appears in CMS's hospice notice", rev 5): In band, Medium tier, Low 0/5 and Medium 1/5, the high
  model 1 of 3 on the every-document check; submitted. Measured Medium recipe 7: a share or total over a
  base with one member printed only in prose outside a complete-looking table, the base named by the
  document it appears in. In that run three of five medium attempts re-checked for other members with no
  cue: one counted the prose total, one looked only around the table, one found it and left it out because
  the table looked like the authoritative list. So the holding step is accepting a total outside the table,
  not only finding it. Write the structural scope before the first run and screen it in the form's Checks;
  recipe 4 (aq-02673) had already described rev 1 (no scope, Too hard) and rev 2 (a clause saying where
  totals sit, Easy), and each cost a run. A plain count over
  many prose items is no substitute: thirteen of about thirty-five cited cases, filtered by outcome and year
  across three notices, was quick-test too easy (aq-02933 q05, one draw). On this bundle the easier solver
  failed only at noticing that something belongs, never at reading, matching or counting what the question
  points to.
- Consultation bundles whose decision papers restate everything (aq-03711, 2026-10-13, two quick tests, no
  panels): when the regulator's draft and final papers summarise every submission and every rule is printed
  twice (final paper and final code; draft paper and draft code), the only single-source facts are the
  submitters' own facts and a few figures. Check this at mapping time and say so before sketching. Two
  designs built on those facts were quick-test too easy: a rule applied to one operator's stated facts
  under the preliminary view and the final decision, two asks (the gates were two plain sentences in the
  operator's letter and the paper's own worked examples), and one party's quoted price applied to the
  regulator's yearly shares, asked as a two-year difference with the method stated. A fact that overturns the
  natural reading does not hold the easier solver when it is one plain sentence in a short letter.

## Evidence and history

- 2026-10-13 (aq-03707 q03 rev 0, difficulty Run 2, Version 752eb7, raw
  tasks/aq-03707/verdicts/AQ-03707_difficulty_2026-10-13_1607.txt; read-out tasks/aq-03707/notes/feedback-q03.md):
  "Between levels", this time "Too hard for the medium model but too easy for the high model": Low 0/5 (2 not
  scored) · Medium 1/7 · High 3/3, closed-book missed. The page states the gate in new words: "Medium model:
  three solvers try up to 3 times each. Ready when at least two get it wrong twice and one gets it right
  twice. High model: two solvers try up to 3 times each. Ready when both get it wrong at least once and not
  every attempt is wrong. A level stops as soon as more attempts could not change the result." So a Medium
  result now needs one middle solver right twice, which 1 of 7 does not give, and a Hard result needs each of
  the two strongest solvers to miss at least once. The question asked which countries "a submission ... credits
  with four main supermarket players" are also on one submission's list of countries with competition
  concerns (gold two names). One member is credited only by an aside in a third submission, in an unrelated
  table row, under an informal name and with the number as a digit ("Even Aussie is a 4-player market").
  From each attempt's own text: every scored attempt found the list; the middle solver always found both
  prominent four-player lists; no low or recorded middle attempt reached the aside, one of them after
  checking that document three times by name; the strongest solver was right three times with no text
  recorded. A region-versus-country decoy (provinces and metro areas beside listed countries) caught nobody
  at any level. Two low attempts read "a submission" as one particular submission. So a member stated only in
  a passing aside whose wording shares nothing but the number with the question sits between the middle and
  the strongest solver, where recipe 6's member (stated in a sentence of the second document's argument) sat
  between the easier and the middle one. Rev 1 restates the test in the sources' term ("any submission ...
  describes as a four-player supermarket market"), no clause added. Result, Run 3 (Version 994c72, raw
  tasks/aq-03707/verdicts/AQ-03707_difficulty_2026-10-13_1933.txt): "In band — Medium tier", Low — · Medium 2/6
  · High —, documents 3, 5 and 8 each "Needed"; submitted at Medium the same day. All four wrong medium
  attempts answered with the one member the prominent list gives; three of them opened the third submission
  by name and still missed the aside, where the page's notes say they "never checked" it. See recipe 9 above.

- 2026-10-13 (aq-03707 q02 rev 2, difficulty Run 1, Version 3a92ac, raw
  tasks/aq-03707/verdicts/AQ-03707_difficulty_2026-10-13_1256.txt; read-out tasks/aq-03707/notes/feedback-q02.md):
  "Between levels", Low 0/5 · Medium 4/7, no high rung, closed-book missed. The question asked one
  co-operative's margin "using a measure" a consultant accepts as comparable (gross profit margin or EBITDAR
  margin), picked by the higher of two printed ROACEs. No document prints that margin: it is the complement of
  a cost-of-goods share that a third party's submission prints, deep in a 164,000-character document, in a
  paragraph about exchange rates. From each attempt's own text: every attempt cleared the two steps a word in
  the question points at (which co-operative, which kinds of margin). No low attempt reached the cost-share
  sentence; they answered with the consultant's worked-example margins (15%, 10%), the ROACE itself or the
  printed NPAT margin. Each recorded medium attempt was right exactly when it went back to that document and
  found the sentence (one after re-reading the question's period phrase), and nobody who found it failed to
  take the complement. So one unpointed step sets the low floor at zero and lets the medium solver through
  about half the time, which the gate called too easy at 4 of 7. A printed look-alike of the wrong kind in a
  worked example was the commonest wrong answer; the declared similar-name trap (the other co-operative) caught
  nobody. No sound second unpointed step in another passage existed (the neighbouring figure hangs on the same
  sentence), so the hook was dropped after one run. The quick test had passed this question, as it must when
  the low solver misses the step.

- 2026-10-13 (aq-03707, round 3 of the grocery study whose round 1 is aq-03557: the final report's executive
  summary and twelve post-conference submissions; form quick test, user chat "too easy for quick test", no panel,
  route unread): q01 rev 0 set one co-operative's printed final ROACE (13.1%) against whichever of a consultant's
  two printed ranges for overseas grocers (9 to 11 per cent unlevered, 22 to 25 per cent at a renter's leverage)
  matches the way the final report measured it; the consultant's own document says the Commission meant to use
  the renter measure, and the final report says it did not. Gold 2.1 points above (11.9 below on the other
  range). Too easy. One outcome, so no rule: a choice between two labelled benchmark ranges did not hold the
  easier solver even with a superseded account of the basis beside the wrong range. The correct range was also
  the document's first and preferred one, so a solver that never weighed the choice lands on the gold; a design
  of this kind needs the default to be the wrong one. Sibling wording on the other retailer closed unrun.

- 2026-10-12 (aq-03557 q01 rev 2, difficulty Run 1, Version d8243a, raw
  tasks/aq-03557/verdicts/AQ-03557_difficulty_2026-10-12_2319.txt): "In band — Medium tier", Low 0/5 · Medium 1/5,
  no high rung run. Low: 301, 301, 71, 301, 301. Medium: no answer (output loop after finding all four counts),
  71, 372 (bare value, Reasoning not loaded: route unread), 71, right (text not recorded). Document check: 376
  with every document; 301 twice without Doc 3; no count without Doc 7. Closed-book: Aldi's Australian stores,
  about 590. The first hand-over's two declared modes predicted 372 and 392; observed wrong answers were 301, 71
  and one 372, and 392 never appeared. Rev 0's sentence had passed "One defensible answer"; the measured wording
  was the user's rewording of its opening (origin user+claude).

- 2026-10-13 (aq-03170 q01 rev 5, difficulty Run 3, Version a6c99b, raw
  tasks/aq-03170/verdicts/AQ-03170_difficulty_2026-10-13_1511.txt): "In band — Medium tier", Low 0/5 · Medium 2/6,
  High not run; user: "medium tier, but no slot left". Same question, answer, reasoning and evidence as Run 2;
  only two necessary-document ticks changed, at the reviewer's request, and the solvers had those documents in
  Run 2 as well. Run 2's page printed the five-attempt gate, Run 3's the three-solver gate. Low: the own-account
  pair four times, eight names once ("one or more"). Medium 1, 2, 4, 5: the own-account pair, no mention of the
  deciding letter. Medium 3 and 6: Right, text not recorded, route unread. Strongest solver with both deciding
  documents: found the letter in three of six attempts. The page's note on Medium 4 named three missed members;
  its Full answer lists two of them. Scope: one question measured under both gates, one day apart.

- 2026-10-12 (aq-03170 q01 rev 4, difficulty Run 2, Version 4e9f31, raw
  tasks/aq-03170/verdicts/AQ-03170_difficulty_2026-10-12_2028.txt): "In band — Hard tier", Low 0/5 · Medium 0/5 ·
  High 1/5; closed-book answered "None"; documents 6 and 8 both needed; submitted at Hard. Only change from the
  Medium version (Run 1): the clause "including letters only others mention" became the opening phrase "Judging
  by all these letters together". The page reports "4 of 15 gave the same wrong answer" and notes that five low
  and two high attempts lacked the Blockchain Association; all fourteen wrong Full answers list it with MFA.
  The author's own misses on the way, each now a floor WARN or a note: a predicted order advisory left in place
  (rev 0); an order sentence the form did not read as one, with an ordinal it took for a pointer (rev 1); no
  counting rule in the first wording although the notes ask for it before the first paste (rev 0-1); a cue
  clause chosen for the repair while the page showed Medium full (rev 2), costing one run; two documents unticked
  on the form's demand while the steps still name them (rev 3-4). Scope: one bundle, two runs.

- 2026-10-12 (aq-03120 q02 rev 2, difficulty Run 3, Version 6243da, raw
  tasks/aq-03120/verdicts/AQ-03120_difficulty_2026-10-12_1742.txt): "In band — Medium tier", Low 0/5 · Medium 2/5,
  closed-book needed the documents, high model reached the gold on its second every-document attempt, Docs 3 and
  4 each needed; submitted at Medium (user report). Wording: "How much did Kiwibank's home lending book grow in
  the half of its financial year that last ended before its owner announced a $225 million capital injection?"
  Routes, each read from the attempt's own Full answer and Reasoning: low 1 and 2 took the six months to December
  2022 as the half that last ended before the 1 August 2023 announcement; low 3 placed January-June 2023 and
  still gave the printed $0.6 billion; low 4 never settled the half and looked for a stated figure; low 5 placed
  January-June 2023 and gave the full-year $1.1 billion; medium 1 and 5 took the December half; medium 4 placed
  the June half, wrote that the documents give a figure only for the December half, and gave it; medium 2 and 3
  subtracted; high attempt 1 counted the December half as the last to end, attempt 2 derived the gold. Before the
  run I had told the user Easy was the likelier result ("roughly one in four" for Medium) and recommended
  releasing the bundle; both were wrong, and the workspace rule against tier odds already existed.
- 2026-10-12 (aq-03170 q01 rev 3, difficulty Run 1, Version bbce17, raw
  tasks/aq-03170/verdicts/AQ-03170_difficulty_2026-10-12_1700.txt): "In band — Medium tier", Low 0/5 · Medium 1/5,
  High not run; closed-book needed the documents (answered IAA, SIFMA); documents 6 and 8 both needed. Every
  attempt read in full. All five low and four medium attempts committed to "Blockchain Association, Managed Funds
  Association". The page's own "Final answer" pick ("2. Managed Funds Association (MFA)") and "Where it left your
  evidence" lines say the low attempts missed the Blockchain Association; each low Full answer lists it, so the
  page's "4 of 10 gave the same wrong answer" is 9 of 10. User: Medium slots full on this set, so the pass is not
  submittable; rev 4 weakens the rule phrase to aim at Hard, result pending. Scope: one run, one bundle.

- 2026-10-12 (aq-03120 q02 rev 0, difficulty Run 2, Version cf8658, raw
  tasks/aq-03120/verdicts/AQ-03120_difficulty_2026-10-12_1447.txt): "Answer not supported", Low 0/5 · Medium 2/5,
  the high model 0 of 3 with every document. Same hook as q01 (one bank's home lending growth: full year in one
  submission, first half in another, second half unprinted), asked as a dollar amount with no call for a
  calculation, the half named as "its last completed financial half-year before its owner announced a $225
  million capital injection" (the announcement is dated 1 August 2023 in footnotes only). Routes read from each
  attempt's own text: low 4 of 5 and medium 3 of 5 took the half that has its own printed "half-year results" (to
  31 December 2022) as the last completed one; medium 2 of 5 placed the June 2023 half and subtracted. The high
  attempts all gave the printed figure: one mis-placed the half, one derived the gold and dropped it ("this is a
  calculation, not stated directly ... that's the specific half-year figure reported"), one found "no data" for
  the June half and chose "completed and reported". So a period phrase that leans on a look-alike reporting term
  gives the Medium counts and fails the gate together: the high model will not offer a figure the documents only
  imply when a stated one fits a looser reading (as on aq-02673 q04 rev 0, "a stretch"). Rev 1 added "stated or
  implied" and nothing else: quick-test too easy (2026-10-12). So on this hook the two wordings bracket the target
  with nothing between: the Medium counts on rev 0 came from "financial half-year" being readable as the interim
  reporting period (one high attempt: "a 'financial half-year' in banking typically refers to a reporting
  period"), not from reasoning, and any word that admits a derived figure lets the low model solve it. My reading:
  when the high model's traces show it taking the same reading as the low model's misses, the difficulty is the
  wording, and the fair form is the one with a single reading (here q01 rev 0's, measured Easy).
- 2026-10-11 (aq-03120 q01 rev 0, difficulty Run 1, Version 2dbdc7, raw
  tasks/aq-03120/verdicts/AQ-03120_difficulty_2026-10-11_2321.txt): "In band — Easy tier", Low 1/5, below the
  Medium target; closed-book needed the documents and all three ticked documents were needed. Design: six bank and
  lobby submissions on one NZ Commerce Commission paper; one bank's home lending growth printed for its first half in
  one submission ($0.6b, half dated by a footnote) and for the full year in another ($1.1 billion); the question named
  the half only by an event a third submission dates plainly (April 2023), so the gold is the unprinted second half
  (0.5). All four wrong low attempts answered 0.6. Read from their full answers, three of them had dated the event,
  placed it in the second half and still returned the only printed half-year figure; one never placed it. So on this
  shape the low model clears a plainly dated event bridge about four times in five, and what holds it is having to
  compute a period no document prints (it looks for a printed half-year figure). The page's "Where it left your
  evidence" lines described two of those attempts as failing to place the event, which their text contradicts: read
  the full answers. The same sketch had survived the form's quick test, so quick-test survival again did not mean Low
  0/5 (as on aq-02447 and aq-02483). Three repairs followed, none measured at the difficulty check (2026-10-12).
  Revs 1 and 2 dated the half by the bank's own first-half results announcement (label first half, release date in
  the second half): the form's "One defensible answer" check failed both, rev 2 with "Both answered 55%", so that
  label draws even the form's solvers to the wrong half. Rev 3 kept rev 0's event and asked for a percentage "On
  [the bank]'s reported figures": quick-test too easy. Rev 0 and rev 3 differ only in the form of the ask, so on
  this shape the step that holds the low model is a subtraction the wording does not ask for; once the question
  calls for a calculation the low model does it. q01 dropped.
- 2026-10-11 (aq-02933 q04 rev 1, difficulty Run 2, Version f40b71, raw
  tasks/aq-02933/verdicts/AQ-02933_difficulty_2026-10-11_2048.txt): "Too hard", Low 0/5 · Medium 0/5 · High 0/5,
  with the page's "may be too vague" advisory. Question: "CMS gives 2019 hospice totals for several States. Leaving
  California out, what percentage of those hospices were in States it names for home health agencies sharing an
  address? Two decimal places." (gold 67.45% = 773 / 1,146, the base including Georgia's 221, printed only in prose
  30,000 characters after Table 1). All fifteen attempts answered 83.57% = 773 / 925: Table 1 taken as every State
  with a 2019 total, and Texas and Nevada found in the other notice's one-sentence list by every attempt. Three
  medium attempts quoted Georgia's sentence while hunting for shared-address States and still left it out of the
  base. The Coach proposed rewording the clause no attempt misread. The author had predicted two independent
  membership steps (about 0.12 for the low model); in fact one step cost nothing and the other was total. Rev 2
  states the counting rule ("tabulated or only in text"): difficulty Run 3 (Version 25d15f, raw
  tasks/aq-02933/verdicts/AQ-02933_difficulty_2026-10-12_0055.txt) "In band — Easy tier", Low 3/5, the high
  model reaching the gold and both documents needed; the two low misses still stopped at the table. Three
  wordings of one hook: Easy (Low 1/5), Too hard (0/15), Easy (Low 3/5); hook retired. A separate hook with no
  table (prison sentences of 2024 or 2025 over three prose case lists, 13 of about 35 cases, with a 2024
  verdict and conviction as look-alikes) was quick-test too easy on 2026-10-12 (user chat, one draw, no trace,
  route unread) and dropped. Then the user quick-tested a middle wording of q04 ("Wherever CMS gives a
  State's 2019 hospice total"): survived, and difficulty Run 4 on it (rev 3, Version 1c833c, raw
  tasks/aq-02933/verdicts/AQ-02933_difficulty_2026-10-12_1451.txt) was "Between levels", Low 0/5 · Medium
  4/5. All five low attempts took "Wherever" to mean Table 1; four medium attempts worked the table figure
  first, then re-read because of the word ("The table only shows 4 states. But maybe there's more data
  elsewhere?") and added Georgia; one medium read it as the table. Rev 4 ("Across every State with a 2019
  hospice total from CMS") was the half step back: the form's "One defensible answer" check failed it before
  any run ("Both answered "83.57%"", screenshots in tasks/aq-02933/notes/platform-feedback/, 2026-10-12).
  Rev 5 names the scope ("whose 2019 hospice total appears in CMS's hospice notice"): difficulty Run 5
  (Version 162781, raw tasks/aq-02933/verdicts/AQ-02933_difficulty_2026-10-12_1903.txt) "In band —
  Medium tier", Low 0/5 · Medium 1/5; every-document check 1 of 3 reached, both documents needed;
  submitted by the user 2026-10-12. Low: all five on Table 1 (two asked whether other States had totals
  and checked tables only). Medium: 1 found and counted Georgia; 2 re-checked near the table only; 4 found
  Georgia's sentence and excluded it; 3 and 5 never re-checked. Wordings of one sentence: none 0/0/0,
  "every State ... from CMS" form block, structural scope Low 0 · Medium 1, "Wherever" Low 0 ·
  Medium 4, "tabulated or only in text" Low 3; plus the both-year frame (q03) Low 1. Cost: five
  difficulty runs, two form blocks and a wrong release recommendation after rev 2. Routes table:
  tasks/aq-02933/notes/feedback-q04.md. Scope: one bundle.

- 2026-10-11 (aq-02933 q03 rev 0, difficulty Run 1, Version 1acbee, raw
  tasks/aq-02933/verdicts/AQ-02933_difficulty_2026-10-11_1708.txt): "In band — Easy tier", Low 1/5 (Medium and High
  not run; target Medium, no Easy slot per the user). Question: from 2019 to 2025, across States with CMS-reported
  enrolled totals for both years, by how many HHAs lost exceed hospices gained (315 = 500 - 185; two HHA pairs in one
  footnote of the HHA notice, Georgia's hospice pair in one prose sentence of the hospice notice, Nevada's split
  between Table 1 and later prose beside a printed CY 2023 to CY 2025 pair). Per attempt: four low attempts answered
  367 = 500 - 133, with Nevada right and Georgia missing ("Only Nevada has reported enrolled totals for both 2019 and
  2025"; one recalled "Ohio and Georgia mentioned but no 2019 totals"); one answered 315. No attempt took the
  declared lure (Nevada from its printed pair, 398) or Table 2's newly-enrolling column. The high model with every
  document listed all four States; both documents "Needed"; closed-book guessed "roughly 200". The page's "Where it
  left your evidence" line for all four misses ("It treated Nevada's CY 2023 figure of 138 as the CY 2019 baseline")
  contradicts the attempts' own answers, so read committed answers, not that line. An independent author and the
  caller had both ranked the Nevada assembly as the trap. Follow-up, pending: q04 keeps the prose-only member
  (Georgia's 2019 total) and adds an exclusion from the other notice whose second State is named once (1,503; routes
  1,282, 1,558, 2,276). Scope: one run, one bundle.

- 2026-10-11 (aq-02770 q01 rev 1, difficulty Run 1, Version 6f4ab4, raw
  tasks/aq-02770/verdicts/AQ-02770_difficulty_2026-10-11_1119.txt): "In band - Easy tier", Low 3/5 (target Medium, no
  Easy slot per the user). Design: lowest TE2 for a gas-fired furnace built at the federal minimum "on the day DOE
  published its final determination not to amend" the standards (Doc 2, December 23, 2022, nine days before the 81
  percent level began; effective date January 23, 2023 as the look-alike), with DOE's part-load estimate re-weighted
  from its 50 percent to the largest share in NEEA's modeling (Doc 4), gold 76.0. Per attempt: all five low attempts
  did the re-weighting what-if correctly (weighted average, 2.5 + 1.5), so an explicit what-if on a stated weighting
  is no barrier for the low model. Three opened Doc 2 because the question named its determination, read the
  publication date and the "until January 1, 2023" rule together and were right; two took 81 (one judged "the base
  TE they used for range example is 81", one took Doc 4, also titled "Final Determination", as the event). Document
  check as the local probes predicted: every document 76.0; without Doc 2 77.0 twice (81 inferred from "went from
  80 to 81 percent", no recall); without Doc 4 76.5 twice; closed-book 78.7. Lessons, one run: (1) an event anchor
  that is the publication of the very document holding the date rule is a tied anchor (as aq-00745's headline-tied
  closing, Low 1/5, and aq-01320): the question walks the solver to the rule; (2) a same-titled look-alike document
  and an effective date a month later each cost the low model about one attempt in five, not more; (3) the
  author's "harder alternate" judgment was wrong about what separates: the computation step added nothing.
  Repair tried: untie the anchor with an event dated only in the documents that print the decoy (rev 3: the
  webinar on the TE2 proposal, March 29, 2022). Measured the same day, Run 2, Version cf23fa, raw
  tasks/aq-02770/verdicts/AQ-02770_difficulty_2026-10-11_1829.txt: "Too easy", Low 4/5. All five low attempts
  dated the webinar and all five took the 80 percent minimum ("the 81 percent level did not take effect until
  January 1, 2023"); the one miss applied 4.0 points as a relative 4 percent (76.8). So untying made it easier:
  it removed the event look-alikes that had caused Run 1's two misses, and the temporal step was never hard.
  Reading for this layout: when the question says "at the [rule's] minimum on the day X" and the rule is one
  dated sentence, the low model resolves X to a date and applies the sentence (10 of 10 over two runs), whether
  or not the question leads to the rule's document. This repeats aq-00998 q03, aq-01333 q01 rev 2 and aq-02750;
  the caller weighed aq-00964 instead, where no dated rule sentence existed and the decoy was printed as
  current. Do not expect an event-to-date bridge onto a plainly dated rule to exceed Easy; what cost the low
  model attempts here was telling two same-titled documents apart. Family retired, q01 dropped.
  Same bundle, same day (user chat "too easy for quick test", no panel, one draw, wording taken as q02 rev 0): a
  match-then-exclude over three commenter tables (in the 2022 and 2025 lists, not in the 2024 list; four names) in
  which two tables reuse the label "Joint Advocates" for different groups was quick-test too easy. Names spelled
  out in every table make a same-label group no trap; third list-join result of this kind. Bundle outcome: three
  rounds, one Easy, two too easy, no Medium design; release recommended.

- 2026-10-11 (aq-02749 q02 rev 0, difficulty Run 1, Version 94672c, raw
  tasks/aq-02749/verdicts/AQ-02749_difficulty_2026-10-11_1128.txt): "In band — Medium tier", Low 0/5 · Medium 3/5,
  submitted at Medium. Question: "Under EPA's five proposed State coal-ash program approvals, how many of the 2024
  Legacy Rule's all-unit amendments would lack an approved State version in exactly two States?", gold 10 (27 words,
  Docs 2, 5, 6). Low: four "0" and one "One (40 CFR 257.90(g))"; all took Wyoming to lack only the provisions its
  proposal names and Wisconsin's eleven-entry list to approve all twenty; four of five did read Alabama's explicit
  "not being approved" trio; three mixed in provisions outside the 2024 rule.
  Medium: 10, 9, 10, 6, 10. Document check: 9 without Doc 5, 3 without Doc 6, 1 without Doc 2; closed-book "Two.".
  Both quick-tested siblings survived (this one and "approve ... in exactly three States"); the one with the grouped
  document active was run. Medium 2 (9) read Alabama's list as "the same 20"; Medium 4 (6) mapped its seventeen entries
  to the wrong members. Declared trap numbers (1 and 8) were not what the solvers wrote (0, 6, 9), though both declared
  mechanisms occurred. Correction 2026-10-12: my first reading called the 6 a list-length subtraction (17 - 11) and
  the 9 a miscount without reading either Reasoning block; the second capture of the same run
  (AQ-02749_difficulty_2026-10-12_0028.txt) and the blocks already loaded in the first show otherwise. High with
  every document built the same five-column table and answered 10.
- 2026-10-11 (aq-02743 q03 rev 0, difficulty Run 1, Version 90fd80, raw
  tasks/aq-02743/verdicts/AQ-02743_difficulty_2026-10-11_1011.txt): "In band — Easy tier", Low 3/5 (Medium and High
  not run; target Medium, no Easy slot per the user). Question: for an HHS-funded county in DOJ's larger population
  tier and HHS's larger staff tier, how many more days HHS's interim rule gave it "before any federal rule required
  it to meet WCAG 2.1" (350: HHS's old date May 11, 2026 to DOJ's extended April 26, 2027). Per attempt: three low
  attempts tabulated the earlier of the two dates before and after HHS's rule, "with DOJ's extension in place", and
  were right; two concluded that DOJ's date controls throughout and answered 0. The declared traps (HHS's own 365;
  DOJ's superseded date as the start, 367) caught no one, and the order of the two effective dates was never needed:
  holding the other rule as it now stands gives the same answer. Document check passed and showed the rebuild route
  exactly: without the DOJ document the high model built April 24, 2027 from the HHS document's "by one year" plus
  the recalled 2024 date and answered 348, so building on the date that breaks the one-year pattern kept its
  document necessary (measured; the 2026-10-10 entry below had it as an inference). Closed-book: the low model
  recalled both 2024 compliance dates to the day and answered 17, so a gold built only from the 2024 dates would
  fail the closed-book check. Lessons, one run: (1) an earlier-of comparison across two rules, once the question
  states it, is tabulated correctly by the low model about 3 times in 5; (2) a sequencing step is no step when the
  default "everything else as it stands" reading agrees with the history. Rev 1 (one focused repair) asked the
  same gain for one county in each of the four tier combinations as one total (350 + 0 + 365 + 352 = 1,067), four
  different patterns, after the aq-02564 recipe: quick test "too easy" the same day (user chat, one draw, no
  trace). So multiplying cells did not help when every cell is solved by the same tabulation (the earlier of two
  printed dates, before and after); on aq-02564 the cells differed in kind and the misses were items left off a
  bill. Family retired; bundle outcome: two designs too easy (a derived cost ratio, a definition gate), one Easy
  (Low 3/5) and its repair too easy, no Medium. Scope: one bundle whose only related pair is two rules that each
  print their dates in a SUMMARY.

- 2026-10-10 (aq-02750 q04 rev 0, difficulty Run 1, Version b8861d, raw
  tasks/aq-02750/verdicts/AQ-02750_difficulty_2026-10-10_2058.txt): "Between levels", Low 0/5 · Medium 5/5 · High
  not run. Design: five groups of comments (letters and portal filings, two dates) run through two CDC comment
  procedures with different rules, an interim rule (portal only, received by June 26) and an order (portal or
  mail, received on or before July 10), asked as one count, 61. Per attempt: all five low attempts answered 91.
  They applied both deadlines correctly, the on-deadline group included, and counted the 30 letters on the rule;
  the low model says it searches "mental/text" and recited the rule's methods from the look-alike blocks (the
  orders' "portal or mail", once another agency's postmark rule from an unrelated document in the bundle). All
  five medium attempts answered 61, quoting the rule's own "all comments must be submitted electronically"; one
  also gave the rule the order's email ban, harmlessly. The 15-day label beside the printed deadline caught no
  attempt. Lessons, one run: (1) a rule that differs between two look-alike procedures of one agency separates
  the low model from the medium model completely, because the low model answers from a blended memory of the
  template and the medium model reads the block; (2) so it gives Between levels by itself, and more groups
  settled by printed dates would not move the medium model; (3) the count shape, which was too easy on aq-02706
  q01, is not too easy when the rule sits in a look-alike block. Rev 1 keeps the trap and replaces printed
  order dates with one arrival date per order derived from a common lag (19 days after issue against deadlines
  that fall 19, 18 and 20 days after issue); result pending.
  Rev 1, 2026-10-11 (user chat "too easy to pass quick test"; a form screenshot the same day shows "Last
  result: Too easy" on the difficulty panel with one more run used, so it was probably a difficulty run; no
  capture, version id or tier counts, identity unresolved): the low model reached the gold too often, so the
  derived dates did not stop it and neither did the method rule that had stopped it six draws of six on rev 0. The rule-side wording was identical; what rev 1 had dropped was the
  group of valid letters on the sibling order. Author's inference, one draw: the carry-over trap needs the
  scenario to show the lure as valid for the sibling procedure (letters that do count on the order); when
  the letters appear only on the procedure that refuses them, they stand out and get checked. Rev 2
  restored the group and the low model still read the block 3 of 5 (Run 3, entry of 2026-10-11 below),
  so this inference is not supported; the group is not known to matter.

- 2026-10-10 (aq-02749, the third task on aq-02483's six files; form quick tests, user chat "both of them too easy to
  pass quick test", no panels): q01, a multi-cell scenario total built on the aq-02564 recipe (minimum public-comment
  days for four permit actions in Wyoming, Virginia and Alabama, 169; two classification steps and a zero cell), and
  i02 (Virginia's 15 days after a hearing applied to EPA's five hearing and deadline pairs, 33) were both too easy.
  Scope of the lesson: the recipe's cells held on aq-02564 because two notices' caps and credits interact; four cells
  that are each one plain sentence in its own State's section do not add up to difficulty. Count the rule interplay
  between documents, not the number of cells.

- 2026-10-10 (aq-02750, three asylum-bar rules, a CDC interim rule and three editions of one Ebola entry order; form
  quick tests, user chat "three of them too easy to pass quick test", no panel or trace, wordings taken as q01-q03
  rev 0): three firm-anchored designs on one order series were all too easy. q01: an event dated in a later order's
  body selects the earlier order ("in force when ..."), whose two printed counts give a percentage (819.8%; the
  later orders' own pairs as decoys). q02: an event in the latest order selects the previous order, whose printed
  comment deadline gives a 3-day gap, beside a "15-day" label that yields 0. q03: comments answered in a later
  notice identify the earlier order; its printed deadline against an interim rule's, three documents, 14 days. Two
  independent authors had ranked q02 and q03 first. Author's reading, unmeasured: when the question names the order
  by status ("then in force") or by what was commented on, and the inputs are first-line DATES entries or printed
  counts, the easier solver dates the event and opens the right edition; a second document or a label lure adds
  nothing. Consistent with aq-01333 q01 rev 2 and aq-02706 q02 rev 1. Scope: one draw each, one bundle.
  Round 2, same day (user chat "q01 q02 too easy to pass quick test. i08 survived. rest not tested", no panel): one
  focused repair each was too easy again: q01 rev 1 dated the event only through a footnoted memo that two later
  orders cite beside their own counts, and q02 rev 1 dropped the status cue ("how many days remained to comment
  ... when Uganda declared its outbreak over"). So neither an undated event nor a soft anchor stopped the easier
  solver on this series; five designs of the family, none survived. The survivor, i08 (written up as q04), has no
  edition choice: five groups of comments (letters and portal filings on two dates) run through two CDC comment
  procedures whose rules differ (an interim rule: portal only, by June 26; an order: portal or mail, received on
  or before July 10), asked as one count, 61. It is a count, the shape that was too easy on aq-02706 q01, but with
  rules that differ between look-alike procedures, as on aq-02486 and aq-02564. Which group the solver missed is
  unknown. One draw; a quick-test survival has not predicted the difficulty check here before.

- 2026-10-10 (aq-02743, seven "web accessibility" Federal Register texts of which only the DOJ title II and HHS
  section 504 compliance-date extensions join; form quick tests, user chat "q01 i05 too easy, i04 survived, i06 not
  tested", no panel or trace, wordings taken as handed over). Too easy: q01, each rule's annualized benefits minus
  costs on the delayed schedule, DOJ's divided by HHS's, 524% (DOJ's exact pair only in a footnote under a rounded
  "$1.3 billion"; HHS's delayed-schedule figures only in flattened table columns while its prose prints the
  original-schedule pair). Too easy: i05, two special districts told apart by a definition quoted far from the
  dates (a direct Federal procurement contract is not Federal financial assistance), 351 days. Survived: i04, days
  from HHS's effective date to an HHS-funded large county's first deadline, which is DOJ's (354; HHS's own date
  gives 369, the Federal Register date 350); promoted as q02, difficulty pending. Author's reading, unmeasured:
  q01 had the derived-figure-beside-printed-decoys shape, but one trap step, and the prose printed the changes
  that lead to the right figure; i05's question contrasted "grant" with "procurement contract", so the
  definition did not have to be found. Scope: one draw each, one bundle.
  Design notes from the same bundle (author's inference, not measured): in a rule-and-extension pair, a new date
  that equals the public original plus an interval the sibling document states ("by one year") does not make its
  own document necessary, so build on the date that breaks the pattern (DOJ's April 24, 2026 became April 26,
  2027); and check every gap or maximum against plain pairings of the headline dates, because a gold that equals
  one is reached without the reasoning.

- 2026-10-10 (aq-02706 q02 rev 0, difficulty Run 1, Version 14960d, raw
  tasks/aq-02706/verdicts/AQ-02706_difficulty_2026-10-10_1603.txt): "Answer not supported", Low 1/5, the gate's high
  model 558 on all three every-document attempts (gold 583). Edition trap in the aq-00964 layout: the Office of
  Advocacy's comment is reported only in the final rule, which restates it as "all of the 636 small entities may have
  been impacted by the proposed rule" (636 from data dated after the comment period); the count current at the comment
  is the proposal's 661. Question: "every small entity the OCC then counted". Traces: every attempt that reasoned at
  length saw both counts and the timeline and chose 636 because the later document attributes that figure to the
  event in its own sentence ("I think there's some ambiguity"). Lesson for this layout: the decoy must be a value the
  later edition merely prints, as in aq-00964; when the later edition itself ties its value to the event, the decoy
  is document-supported and the gold reads as unsupported at every level. Ask for the count by its own status
  (published, in force) instead of through the event's reported content. Scope: one run.
  Rev 1 did that ("On the count the OCC had published by then"): difficulty Run 2, Version 1c9adf, raw
  tasks/aq-02706/verdicts/AQ-02706_difficulty_2026-10-10_1749.txt, "In band - Easy tier", Low 3/5, every-document
  attempt right first time, both documents needed. Ladder on identical content: soft anchor -> Answer not supported
  (low 1 of 5, high 0 of 3); firm anchor -> Easy (low 3 of 5, high 1 of 1). The two levels moved together, so one
  such judgment has no Medium point; it needs an independent capability-dependent step beside it, and this bundle
  offered none (as aq-02505: say so instead of trying a third wording).

- 2026-10-10 (aq-02686 q01 rev 1, difficulty Run 1, Version bac61b, raw tasks/aq-02686/verdicts/AQ-02686_difficulty_2026-10-10_1539.txt):
  "In band — Easy tier", Low 3/5 (target Medium, no Easy slot per the user). Design: recipe 3's shape across two
  regimes, one recycler under EPA's 2026 proposed SNURs (Doc 7: SNUN $45,496 because dust controls are under 99%,
  plus about $106 per export country) exporting only to prospects that are not FEOCs under DOE's final
  interpretation (Doc 4): a Polish firm 50% city-held (FEOC), the Indonesian subsidiary of a private Shanghai
  company (not), a Japanese firm where a province picks two of five directors "casting 20% of board votes" (not,
  by a comment-response sentence valuing a board seat at its board voting power); gold $45,708. Per attempt: all
  five got the SNUN trigger, both costs, the plain holding and the jurisdiction-only subsidiary right. Two
  counted seats (40%) and gave $45,602, the declared trap. Three were right without citing the clarification:
  they took the question's printed 20% as the control share ("the problem frames the government's power as 20%
  of board votes"). No low attempt cited the comment response; the high model's every-document attempt did.
  Document check as the local removal probe had predicted: without Doc 4 $45,602 twice, without Doc 7 "$0" and
  "cannot be calculated" (the high model did not supply EPA's boilerplate $106 or the SNUN cost from memory);
  closed-book $37,000. Lessons, one run: (1) four explicit rule steps in a scenario were each 5 of 5 for the low
  model, so recipe 3's separation on aq-02564 came from what a bill leaves out, not from the number of rule
  lookups; (2) when the scenario prints a share on the deciding metric, the weaker solver takes it at face value
  and is right without the reading, so a trap built on a clarification must give facts from which the share is
  derived, never the share; (3) the weaker solver read the operative section and skipped the responses to
  comments, the stronger one read both. Rev 2 applies (2): convertible notes counted as contingent equity
  (10% + 20%) and one seat of seven with two of eight votes (25%), with a plain 15% holding as the only eligible
  prospect; gold $45,602. Quick test of rev 3 (same day, user chat "too easy for quick test", no panel):
  too easy; q01 dropped after Easy and too easy on one hook.
  Round 2 on the same two documents changed the dependency from classifying buyers to counting a bill
  (q02: one SNUN, because only one of two oxides is reclaimed under the 99% minimum, plus export notices
  counted per chemical and per country, with one buyer excluded as a FEOC; $45,920): quick test "survived"
  (user chat, one draw, no trace; difficulty pending). Consistent with the aq-02706 reading that the easier
  solver needs something to omit or misprice, not something to classify; not yet a tier result.
  Difficulty Run 2 on q02 rev 0 (Version a9ec06, raw tasks/aq-02686/verdicts/AQ-02686_difficulty_2026-10-10_1904.txt):
  "Answer not supported", Low 2/5, the high model with every document $46,026 three times. All eight attempts
  (five low, three high) got the one SNUN, the per-chemical per-country notice count and the contingent-equity
  classification right. They split on the question's phrase "Barring FEOCs, it exports ... one to a Thai buyer":
  two low attempts read "except to FEOCs"; three low and all three high read "FEOC status aside" and kept the
  Thai notice. So the quick-test survival and the Low 2/5 measured a parse ambiguity, and the counting bill did
  not trouble the low model either. Rev 1 states the policy as its own sentence ("It refuses FEOC buyers.
  Orders: ..."); platform pending, with nothing left that separated the solvers.

- 2026-10-10 (aq-02780): its seven files are byte-identical to aq-02706's (sha256 compared on intake), so the
  aq-02706 results below and above apply to it and its map was reused. A second full read found one untested
  mechanism, written up as q01 (a three-institution plan counted against the reach of three exemptions in the
  OCC's 2026 rule and the FDIC's 2025 proposal, 9 changes). Author's note for any further copy of these bytes:
  priceable figures sit almost wholly in the FDIC branch proposal, so the two-regulator scenario can only be a
  count, and the 2024 merger policies' size lines are recallable. 2026-10-11: rev 0's difficulty Run 1 was
  "Answerable without the documents" because the gold equalled the sum of the question's opening counts (lesson
  and evidence in [[docket-general-knowledge-check]]). Rev 1 (counts changed, one count per agency: 4 by the OCC,
  6 by the FDIC), difficulty Run 2, Version fb0985, raw tasks/aq-02780/verdicts/AQ-02780_difficulty_2026-10-11_1351.txt:
  "In band — Easy tier", Low 1/5 (Medium and High not run), closed-book "Needed the documents" (it answered 0 and
  0), every-document attempt right at once, both documents needed. Per attempt: the four wrong low attempts all gave
  OCC 12 and FDIC 6. They took the rule's whole list of "expedited or reduced filing procedures" as filings that are
  still made and then expedited, and missed the one sentence saying a savings association "need not file an
  application" for a branch; the right attempt and the high model read it. The two scope limits the author had
  declared as the traps caught no one: all six document attempts kept the de minimis exemption to branches ("applies
  only to branches, not to a main-office relocation") and counted the association's home office. The page's
  one-line notes on the wrong attempts ("omitted the OCC count entirely", "stopped before producing any numeric
  totals") contradict the attempts' own full answers, which state both numbers. Lessons, one run: (1) in a preamble
  that lists expedited-review provisions beside no-application ones, the weaker solver flattens the list to
  "expedited", so the no-application item is the separator, while a limit written into a definition is read
  correctly; (2) one such separator, read by one low attempt in five, settles Easy, as on aq-02505; (3) asking one
  count per agency made each document's necessity clean in the Document check. Rev 2 makes the notice-or-application
  distinction count twice in opposite directions (a bank's qualifying operating subsidiaries need only notice, a
  savings association's needs an application; 3 by the OCC, 7 by the FDIC); checked, platform pending.

- 2026-10-10 (aq-02706, seven Bank Merger Act / licensing Federal Register texts; form quick tests, user chat "both
  are too easy to pass quick test", no panel or trace, wordings taken as q01 rev 0 and sketch i02): two more
  shapes the easier solver cleared. q01: one bank profile run through the OCC's 2026 covered-community-bank rule
  and the FDIC's 2025 branch proposal, four cells summed (14 moves), with one step left to a definitions section
  (a branch moved outside its "immediate neighborhood" is an establishment, not a relocation). i02: a ratio whose
  2023 denominator sits in the next edition's footnote, with the sizing date named in the question (48.03%).
  Author's reading, unmeasured: a definitions gate printed in the paragraph next to the rule it limits is found
  as easily as a plain exception, and a count of qualifying items gives the easier solver nothing to omit or
  misprice (the Medium scenarios on aq-02486 and aq-02564 were totals built from extracted rates). Scope: one
  quick-test draw each, one bundle.

- 2026-10-10 (aq-02626, capture tasks/aq-02626/verdicts/AQ-02626_difficulty_2026-10-10_1132.txt, which holds all three
  runs): q06 Run 3 (Version 8bf6fe) "Too easy", Low 4/5: four attempts quoted each State's duration sentence and summed
  3 + 7 + 6; the one miss left Wyoming out (13). q03 Run 2 (Version 564142) Too easy, Low 5/5, every attempt 1,271 days.
  The Coach's "Make it harder" named the cause as wording that echoes the source ("'carry no set expiry' maps almost
  verbatim onto the documents' own wording") and proposed a second, scattered condition (States that have actually
  issued permits). Checked against the text, its facts were right; but the condition removes the one State the weaker
  solver missed, so vet a Coach variation for which errors it turns into correct answers, not only for fairness.
  A later page lists an earlier in-band run as "Earlier version — does not count" once the form holds another question.

- 2026-10-10 (aq-02626, user chat, no captures): q06 (landfills in States whose permits have no set expiry, 16; five
  duration statements with look-alike wording) survived its quick test and was too easy at the difficulty check; its
  held repair i10 (units instead of landfills, adding Wisconsin's landfill-only scope, 50) was quick-test too easy.
  Bundle outcome over three rounds: seven designs too easy, one Easy (q04, Low 3/5), none at Medium; on this bundle a
  quick-test survival did not carry to the difficulty check in any of three cases (q03, q04, q06). Scope: one bundle
  of five templated proposals whose every State-specific fact is one plain sentence or one enumerated list.

- 2026-10-10 (aq-02626, user chat reports, no captures): q03, the stale-edition question (days from Wyoming's rule
  taking effect to EPA's latest amendment "as of September 2026", 1,271; Wyoming's own proposal lists amendments only
  to 2024, 812) survived its quick test and then measured too easy at the difficulty check. The newer amendment is
  printed in four of the five sibling proposals, so the edition trap sat in one document against four. q05 (days from
  publication to comment deadline summed over five proposals, 307, against the printed "60-day" label, 300) and i09
  (renewals over 25 years in three States, the ten-year figure being a permit cap in two and a plan-update interval
  in the third) were quick-test too easy; i08 (landfills in States whose permits have no set expiry, five duration
  statements with look-alike wording) survived the quick test. Scope: one result each. On this bundle three of four
  quick-test survivors so far measured Easy or too easy, so a survival is weak evidence.

- 2026-10-10 (aq-02626 q04 rev 0, difficulty Run 1, Version d686ca, raw tasks/aq-02626/verdicts/AQ-02626_difficulty_2026-10-10_0806.txt):
  "In band — Easy tier", Low 3/5 (Medium and High not run), after a quick-test "survived". The question summed surface
  impoundments in States where EPA approves the State's own version of one named definition across five templated
  proposals (Virginia 18 + Louisiana 6 = 24). The declared decoy, Alabama's identical entry under a "not being approved"
  heading, caught no low attempt. Both misses (43 and 40) counted Wyoming, whose proposal has no such list at all: the
  low model worked from memory of the long documents ("search mental text of Doc 3") and carried the sibling proposals'
  list into it. Document check and closed-book check both passed. Scope: one run. Reading: on a templated series the
  weaker model's error is carrying the template into the document that departs from it, not falling for a printed
  look-alike entry; a named list item plus two printed counts still leaves a clean route most attempts take.

- 2026-10-10 (aq-02626, the same six files as aq-02483; form quick tests, user chat "both turned out to be too easy for
  quick test", no panel pasted, wordings taken as q01 rev 0 and q02 rev 0): two designs built toward recipe 2 were too
  easy. q01: one stated case run through two States' parallel permit rules (Wyoming's two comment periods, each to 30
  days after the second weekly notice though labelled "30-day"; Virginia's comment at least 15 days after a hearing
  held 40 days after notice), asked as a difference, 19 days. q02: Alabama's awarded STAG total beside a larger total
  with anticipated money, divided by a facility count that exists only as a numbered permit list, against Virginia's,
  $62,260. Author's reading (no solver trace seen): in q01 each rule sits in the sentence beside the label it
  overrides and the question's own conditions ("notices a week apart", "hearing 40 days after notice") name both
  rules, so nothing invites carrying a rule across documents; in q02 the measure choice is settled inside one
  sentence. Scope: one quick test each, one bundle. It supports the Hard-recipe lesson already in Current rule: a
  stated case is not a trap when every deciding rule is reachable from the question's words.

- 2026-10-10 (aq-02505 q03 rev 0, difficulty Run 5, Version 704f4c, raw tasks/aq-02505/verdicts/AQ-02505_difficulty_2026-10-10_0750.txt):
  "Between levels", Low 0/5 · Medium 0/5 · High 5/5, for q02 widened to "mine or source copper or lithium" (five names; decoys
  Ashele, SDIC Lop Nur via "respectively", Tianhongji). Per level on a hidden already-listed member: the medium model takes each
  notice's "adds" sentence as first placement and never checks an earlier list (Ashele in four printed final answers, the fifth
  attempt skipped Doc 4's (v) descriptions; Daqo missed 3 of 3 on q01 rev 1); the low model checked in 3 of 20 attempts (Runs 1,
  3, 4, 5); the high model checked every time (Ashele 5 of 5; q01's every-document Document-check attempts reached the 78 base).
  So one such check lands Easy (when a low attempt checks) or Between levels (when none does), never Medium, and Hard only if
  something else stops the high model. The mentions-vs-does decoys cost the high model nothing. Caller's inference, unmeasured:
  the Run 4 note below that stacking such checks "does not lower" the low model's rate. First measurement of two stacked checks:
  q04 (Ashele in the set, Daqo in the base, one percentage, 5 / 109 = 4.6%) was "too easy" in the user's quick test the same day
  (chat report, no panel, route unseen; one draw). Reading for series-edition bundles: a hidden prior-state check, single or
  stacked, gives Easy or Between levels, because medium never makes the check and high always does; look for a mechanism that
  needs no such check (a derived figure against printed decoys, an asymmetric rule, a multi-step scenario) or tell the user early.
- 2026-10-10 (aq-02505 q02 rev 0, difficulty Run 4, Version b94f39, raw tasks/aq-02505/verdicts/AQ-02505_difficulty_2026-10-10_0256.txt):
  "In band — Easy tier", Low 1/5, for "which entities first placed on the UFLPA Entity List from November 25, 2024 through
  August 3, 2026 mine, process or source copper" (four names, one member set per notice; decoy Ashele Copper, a Doc 4
  addition already on Doc 2's list outside its five additions). Low: 2 attempts included Ashele, 2 were incomplete (one
  stopped after Doc 2, one returned a single name), 1 cross-checked the three appendices and was right. Document check: all
  three documents needed; closed-book wrong. Cross-run lesson (four runs on this bundle, three at exactly Low 1/5 over two
  mechanisms, undirected Daqo and directed Ashele): the low model runs a thorough list cross-check in about one attempt in
  five, and that attempt clears any fair hidden-prior-state design, directed or not, so stacking such steps does not lower
  its rate. With five attempts that settles Easy more often than not (0/5 about one time in three). A bundle whose only
  untied trap is of this kind cannot be steered to Medium by wording; say so after the second Easy instead of redesigning.
- 2026-10-09 (aq-02505 q01 rev 0, difficulty Run 1, Version 95fd92, raw tasks/aq-02505/verdicts/AQ-02505_difficulty_2026-10-09_1639.txt):
  "In band — Easy tier", Low 1/5, for the % growth of the UFLPA Entity List from November 1, 2024 to August 3, 2026 (gold
  139.7%). The November 1 count is printed nowhere: Doc 2's update names 5 + 25 additions, but one (Xinjiang Daqo) had been
  listed since June 2022, stated only in its own description paragraph, so 29 were new (base 78). Four low attempts took 30
  (base 77, 142.9%), three of them noticing the next edition's 107 + 39 = 146 vs printed 144 without resolving it; the right
  one counted Doc 2's lists. Every attempt found the base edition by matching the question's "November 1, 2024" to Doc 2's
  supersession sentence. The closed-book attempt recalled "about 78 entities on November 1, 2024" (84.6% with a guessed 144):
  2024 UFLPA totals are in the low model's memory. A hidden already-listed member among an update's named additions is a
  strong low-model trap (4/5) but alone did not hold Low at 0/5. Rev 1 asked from November 15, 2024 (printed nowhere) and
  was "Too hard", 0/15 (Run 2, Version 4200aa, raw ...AQ-02505_difficulty_2026-10-09_1719.txt): all 5 high, 2 medium and
  2 low attempts read the bare date as a typo for the nearest printed one ("There's no November 15 UFLPA count in the
  documents", "This is the closest update") and used November 25's 107 (74.8%); the 6 that placed it in the November 1
  version all missed Daqo (142.9%), medium included (0/3). The Coach called the base a missing document. Lesson: a date no
  document prints is read as an error, not a temporal-alignment cue; say what the date selects ("the list in force on").
  Rev 2 did that and was Easy again (Run 3, Version 0b7d6e, Low 1/5: every low attempt placed the date, 3 missed Daqo, 1
  cleared it, 1 miscounted), so the family was retired (q01 dropped 2026-10-10). Profile of a hidden already-listed member:
  low clears it about 1 time in 5 (2 of 13), medium 0 of 3, high 3 of 3 (every-document attempts). A trap that only the
  high model clears cannot land Medium: Low hits 1/5 often enough to settle Easy, and a harder anchor tips all levels
  to Too hard. Look for a step medium clears and low does not; the traces show medium "trusts the stated totals" when an
  update's own summary conflicts with them, while low notices the conflict and leaves it unresolved.
- 2026-10-09 (aq-02486 q01 rev 1, difficulty Run 1, Version 5344ab, raw tasks/aq-02486/verdicts/AQ-02486_difficulty_2026-10-09_1631.txt):
  "In band — Easy tier", Low 2/5, for "ONCD's proposed FOIA charge minus the Access Board's" for 216 photocopies (gold $11.60;
  the Board forgoes totals of "$25.00 or less", ONCD's $25 is a notice). Three low attempts read the Access Board's paragraphs
  as ONCD's rule (both agencies at $0.20: $0.00). The grader is sign-insensitive here: low attempt 2 and the high model's
  every-document attempt missed the no-fee rule, answered -$11.60, and were marked right ("Reached your answer ✓"), because
  the Board's rate is exactly twice ONCD's, so the missed-rule difference is the negated gold. Lessons: in an "A minus B"
  design, check that no trap route gives the gold's magnitude with the other sign; and the high model applied a rule printed
  one paragraph after the free-page rule in only 1 of 3 attempts that computed the Board's fee, so such a rule is a strong
  trap even for the high model (an "Answer not supported" risk once the trap route is graded wrong). Rev 2 asks the total.
- 2026-10-09 (aq-02486 q01 rev 2, difficulty Run 2, Version c47c1a, raw tasks/aq-02486/verdicts/AQ-02486_difficulty_2026-10-09_1742.txt):
  "In band — Medium tier", Low 0/5 · Medium 2/5, "You can submit now.", "+$20 Medium+ bonus if accepted", for "what would a
  news reporter pay ONCD and the Access Board together for 216 photocopied pages from each" (gold $11.60). Low: $66.40 (rates
  never extracted), $46.40 (the Board's $0.20 applied to ONCD), $0.00 x3 (the Board's no-fee rule applied to ONCD too).
  Medium: $11.60 x2, $34.80 x2 (rule missed; one quoted it), $0.00. Document check: every-document attempt 1 $34.80 "Did not
  reach your answer ✗", attempt 2 $11.60 "Reached your answer ✓" (the platform retries); both documents needed; closed-book
  $23.20. The risk named in Run 1's lesson (high-model misses once the trap grades wrong) cost one retry, not the gate.

- 2026-10-09 (aq-02447 q01, user quick-test reports, no panel text): a counting-unit pin that settles a normalisation step in the
  question removes that step's difficulty. "How many distinct five-character ECCNs named in ... were absent from ..." was "too easy",
  while the same count worded "How many distinct ECCNs does ... name ... that ... did not?" survived. The pin told the solver to
  collapse paragraph designations (5A992.z.2 -> 5A992) and so to link them to the earlier rule's ECCNs. It was added to
  close a paragraph-level counting reading that local probes had raised; prefer leaving such a unit to the documents' own
  usage when the documents settle it (here Doc 6's own amendment lists "ECCNs 3A001, 3A090, ...").
- 2026-10-09 (aq-02447 q01 rev 2, difficulty Run 1, Version 0cf427, raw tasks/aq-02447/verdicts/AQ-02447_difficulty_2026-10-09_0913.txt): the
  quick-test survivor came back "Too easy", Low 5/5. The question cited both provisions by CFR paragraph ("§ 742.6(a)(6)(iii)(B)", "§ 742.6(a)(6)");
  every low attempt went straight to both lists, collapsed paragraphs to base ECCNs and diffed them, and the preamble's look-alike list of
  seven ECCNs caught no attempt. Coach: "Drop the paragraph-level citations ... so solvers must locate the provisions themselves." A precise
  citation that names the answer-bearing passage turns a list diff into a lookup even when a look-alike list sits nearby; name the provision
  by what it is instead, and check that the wording still excludes every other list. Measured on rev 3 (same day, user report): naming
  the provisions in words ("the UAE license requirement of BIS's July 2026 rule", "the China-and-Macau license requirement of its January
  2023 Macau rule") was also quick-test "too easy": a precise description echoes the provisions' own headings, so it points as well as
  a citation does. A list diff whose lists are findable by their headings has no fair Medium form; the family was retired.
- 2026-10-09 (aq-02405, six DOJ/ATF firearm proposed rules; user reports without panels): three designs were "too easy"
  for the easier solver. q01 rev 1: one paper Form 1 filer's combined savings from two proposals revalued at $26.10
  ($48.05; Doc 6 prints its own $42, Doc 3 holds the 0.25 h CLEO copy) once the question said the proposals' savings
  combine; rev 0, which left that unsaid, was form-blocked as too vague. i03: states on Doc 5's open-check list that Doc 2
  cites for permit-check exemptions (Delaware, Florida, Maryland; two only as "Del."/"Md." citations). i04: Public Law
  117-103 under two names (NDNA in Doc 5, appropriations act in Doc 1), answer local and Tribal against the denial-report
  decoy "state, local, or tribal". A stated combination, a two-list intersection and an ID join were each a lookup path.
- 2026-10-09 (aq-02360 q02, fourth task on the Civil Service McCloud bytes; platform difficulty Run 1, Version 6009d1 =
  the user's paraphrase of rev 0, raw tasks/aq-02360/verdicts/AQ-02360_difficulty_2026-10-09_0531.txt): an exclusive end
  date across two documents (consultation opening only in Doc 4; opted-out election window "after 1st October 2023 but
  before 30 September 2024" only in Doc 3; gold 573 to 29 September) gave "Between levels": Low 0/5 (all 574, taking 30
  September), Medium 4/5. First survivor on these bytes after five too-easy families. The Coach blamed an endpoint
  convention and called 30 September the last day, while the per-attempt notes named the exclusive "before"; trust the
  traces. A boundary trap alone holds the low model but not the medium one; rev 1 adds a filtered latest-date anchor
  (last union meeting in an out-of-order list): Run 2 "Answer not supported" (Low 0/5, Medium 3/5; the gate's high model
  read 30 September as the last day), so the boundary hook is exhausted (see [[docket-one-clear-answer-precision]]). The same task's q01 (superseded draft subsection) survived
  its quick test untied, failed the form's closed-book check, and was too easy once the gold named the paragraph.
- 2026-10-09 (aq-02408 q01, user report "q01 too easy for quick test", no panel): six unrelated Federal Register texts
  joined only through grid markets. A filter (DOJ's two relevant markets, Doc 5, against EPA's covered coal plants by
  market and state, Doc 4: only ERCOT holds one) followed by an ownership-weighted sum (557 + 28.5% x 365 = 661 -> 660 MW)
  was solved by the easier solver. Both traps were tied: the Coastal Mid-Atlantic scope is printed in the sentence naming
  DOJ's PJM market and Doc 4 prints each plant's state beside its market; the 28.5% share follows Gregory's 365 MW and the
  question's "Calpine-owned" points at it. A scope filter plus a weighted sum over labelled figures is a lookup path when
  each disarming fact sits next to the figure it corrects.
- 2026-10-09 (aq-02157 q04, UK smokefree response vs pack-insert impact assessment; three difficulty runs, raw in
  tasks/aq-02157/verdicts/): Run 1 "Too hard" 0/15 on the user's paraphrase "...to the smoke free consultation?"
  (dropped "response"; 13/15 gave 13.1%, the literal answer, every Medium/High attempt computing the MET floor);
  Run 2 "Too hard" 0/15 on the paraphrase "What is the increase in ..." with the percentage gold (High 5/5 £1.5, the
  literal answer; Medium £7.98 look-alike x3, £7.87 edition x1, £1.5 x1; Low £7.87-as-start x5); Run 3, same question
  with gold £1.5 (rev 3, origin user+claude): "In band — Medium tier", "Low 0/5 · Medium 2/5 · High —", "You can submit
  now." (Low £0.6 x4, £0.5 x1; Medium £0.5 x3, £1.5 x2). Removal probes on rev 0 had missed (7.5%, 13.1%). Lessons:
  the recipe and the triage rule in Current rule; one run per version, so two paraphrase slips cost two runs (see
  [[docket-handover-all-form-fields]]).
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
- 2026-10-07 (aq-01432 q03 rev 0, platform difficulty check Run 2 pasted by the user 2026-10-08; version 6c76af; raw in
  tasks/aq-01432/runs/q03-r0-v2-e4fa2914.../results/platform-difficulty-check-run2.md):
  - Result: "Too easy", "Low 5/5 · Medium — · High —". "5 of 5 solver attempts got it by quoting the same passage: Doc 11
    (“Misleading promotional claims”)".
  - Closed-book: "Needed the documents". It answered 5, 6, 7, 19, 20 and 31; its own reasoning recites the predecessor 2008
    Schedule 1 list (full saved page, tasks/aq-01432/verdicts/AQ-01432_difficulty_2026-10-07_1307.txt).
  - That page also shows all five low attempts weighing 21 against 22 before committing to 22; attempt 1 first wrote
    "5,6,7,11,17,21,22,23".
  - Local odds had made Too easy the modal outcome (review ~55%, author ~45%), so the prediction held.
  - This is the second Too easy on the bundle. The theme-to-paragraph family is retired with its sketches (j03/i08).
  - Round 3 (an independent author, 2026-10-08) read all eleven documents and found one sketch, Easy at best (i09: the same
    UK-examples-versus-FTC-staff-reading family as q02; author odds Too easy ~50%, Easy ~28%, Medium ~7%). Its diagnosis: the
    summaries restate the full guidance item by item, and the full guidance cites provisions on the lines a solver reads.
    So every join is a lookup or a one-sentence exception, and no mechanism that has beaten the low model elsewhere is
    present.
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
- 2026-10-08 (aq-01650, seven unrelated financial-literacy papers; target Medium; local only, platform pending).
  The only Medium-plausible design two independent authors found is a hidden-scope figure inside one paper: the BoJ
  2016 survey paper's descriptive table prints its only overall literacy mean (15.2 of 25) for 15,228 complete cases,
  while its regressions and decomposition cover all 23,788 non-students; q01 rebuilds the non-student mean from the
  decomposition's sex-specific means and counts (14.0872) and subtracts the CHFS 2015 share (1.414 of 3), gold 9.2
  points, wrong routes 13.7 (complete cases) and 9.3 (unweighted). Pairing matters: the same trap paired with the
  Osaka panel's mean (0.62 prose vs 0.6185 table) flips the gold with the figure chosen; the CHFS 1.414 is identical
  in prose and table. Three Opus solves matched (each named and refuted 13.7 and 9.3), closed-book missed twice
  (recalling only Japan's published 55.6%), both removal probes missed. Two reviews: Medium marginal, Too easy 15%,
  Easy 45%, Medium 22%, Between levels 10%; the trap is tied, because any wording naming the non-student population
  retrieves the sentence and table title that disarm the decoy. Lesson for academic-paper bundles: look for papers
  whose descriptive table covers a complete-case subset while analyses use a larger imputed sample; the tie is
  structural, so expect Easy unless the platform's low model takes the table mean.
  Platform, same day (form's free "One defensible answer" check, user screenshot): rev 0 blocked "too vague", both
  form solvers answered 13.7 (the complete-case route). The local reading that the trap was tied was wrong for the
  platform's solvers: "non-student respondents" fits the complete cases too, because they are non-students and the
  paper calls them "the final usable number". Calibration error, not a new mechanism: see
  [[docket-form-vague-block]]. Rev 1 states the separating condition ("all non-student respondents").
  Platform difficulty check, same day (user-edited version 1923ac: rev 1 plus ", including those with missing
  background information,"; saved page tasks/aq-01650/archive/round1-q01/verdicts/AQ-01650_difficulty_2026-10-08_1000.txt): "Answer not
  supported", "Low 3/5 · Medium — · High —". The low model found the decomposition table's sex-specific means 3 of 5
  times (9.2) and took 15.2 twice; the high model took 15.2 in 3 of 3 every-document attempts and never consulted
  that table, concluding the 23,788 mean "is only reported for 15,228". Inverted difficulty: a pointer to the means
  would lift the high model but also the low model (already 3 of 5), giving Easy or Too easy, and Easy was full, so q01
  was dropped for the Medium target. Eleven local Opus runs found the table every time and three reviews put "Answer not
  supported" at 5-7%: the platform's high model is not a stronger Opus; it can miss a gold input in a non-descriptive
  table that weaker models find. See reference/platform-quality-checks.md ("Answer not supported").
- 2026-10-07 (aq-01430 q01, user report: "set q01 status as submitted and accepted_tier as Easy
  Tier"; tier line and tested wording not supplied): the overlapping-windows mechanism (EU coal
  2019 -> 2021 = -34 TWh from two editions' windows net of the 2025 step) reached the Easy tier, below
  the bundle's Medium target and as the local review predicted (Easy ~47%, Medium ~12%). First platform
  result for window arithmetic across editions: it behaves like the partial-period family (Easy), not
  like an edition trap.
- 2026-10-08 (aq-01541, seven rulings from one FCRA class action, Brooks v. Trans Union, July 2024 - July 2026;
  target Medium, Easy slot full; local only, platform pending). The only Medium-type mechanisms were a superseded
  expert-report version and a printed share on a wider base. The settlement (Doc 7) defines its payment groups by
  the plaintiff expert's April 22, 2025 report; the decertification ruling (Doc 6) prints the superseded March split
  first with the groups' own descriptions, says one sentence later that the April re-run eliminated 920 and left a
  list of 57,233, and gives the April split only in the expert-sampling passages. Three write-ups, each with two Opus
  matches, a closed-book miss, a clear audit and both removal probes off the gold: q01 (points-weighted share of the
  claims reserve if every member claims, 63.3%), q02 (one point's value, $29.1, adding the printed "$350" estimate at
  typical claim rates as a look-alike) and q03 (an independent author's design: no-record share of class members on
  the list in force at the decertification motion minus the June 2022 test month, -10.0 pp; the printed 27.7% is a
  share of 973 searched files, not of the 581 class members). Reviews: all easy, marginal toward medium (usable
  Medium-or-High ~15-20%), because the decoy's supersession is stated in its own paragraph (tied) and the question's
  terms lead to the right sentences. Dates, sealing appendices, Rule 23 lists and thresholds gave only one-document or
  two-answer hooks. Lesson: in a single-case docket bundle, the cross-document numerics run through the latest ruling's
  restatement of earlier expert reports; say early that Medium is unlikely and quick-test before any difficulty run.
- 2026-10-08 (aq-01431 restart, user: no Easy slot, "target medium and high"; local only, platform pending). After two
  independent author rounds found nothing above ~10% Medium outside the removed US SIF family, one new mechanism survived:
  a citation's identifiers contradict the narrative list printed beside it. ICI's footnote names three equity-market
  proposals and then cites the Justice Department's letter by file numbers that cover a different trio (one named
  proposal out, one proposal identifiable only by elimination from another letter's list of four). Asked as the average
  days from Federal Register publication to the letter (84.3; the narrative trio gives 91.7). Locally: four Opus solves
  matched at high confidence and named the decoy; closed-book missed; review medium (marginal): estimate Easy 35%, Medium
  40%, High 8%, Between levels 10%; partly tied because the file numbers sit in the decoy's own sentence; removal-flag
  risk because the second letter's only input (a Federal Register date) is recalled. Look for this "IDs vs adjacent
  narrative" pattern in citation-heavy bundles (comment letters, briefs): it gives an answer-shaped decoy in the path
  without manufactured wording.
- 2026-10-08 (aq-01539, fourteen orders from the Snowflake MDL; target Medium, Easy slot full; local only, platform
  pending). No forecasts, restatements or values that change between orders, and two independent authors' other designs
  all leaned Easy (list joins whose items print the deciding property, plainly dated bridges, repeated figures). The one
  Medium-capable design is an untied derived count from the JPML transfer order's counting footnote: "Even counting all
  actions in the District of Montana as a single action and all actions in the Eastern District of North Carolina as a
  single action, there still are 42 related actions pending in twelve districts", with the order's totals (45 actions on
  the motion, 34 potential tag-alongs, Montana's printed fourteen + twelve) and Schedule B (ten E.D.N.C. actions), fixes
  E.D.N.C.'s potential tag-alongs at 3, printed nowhere; Montana's "twelve potential tag-along actions are pending in this
  district" is the same-label decoy in the path. q01 rev 1 (district picked through a settlement fact only Doc 3 holds):
  five full-document Opus solves across wordings all derived 3; review ready, medium (Easy 30%, Medium 40%, Between 9%,
  High 7%, Too hard / not supported 12%). Look for counting-convention footnotes in JPML/MDL transfer orders: with the
  order's totals they define per-district counts no passage prints.
- 2026-10-08 (aq-01960 q01, user report "q01 is too easy for a quick test"; tested wording not supplied):
  a single-quarter derived numeric, non-GAAP gross profit computed from D14's statement of operations
  plus the pre-tax table's cost-of-revenues line, against revenue x non-GAAP margin guidance midpoints
  from D13, was solved by the form's easier solver. Neither the bundled "Acquisition-related charges"
  total (33,069, with SG&A and a -11,601 interest release) nor the release's own next-quarter guidance
  caught it: a labelled adjustment table beside the statement is no trap. q01 dropped; the four-quarter
  GAAP version (q02) and a split-anchored guidance-in-force sketch (i03) remain, platform pending.
- 2026-10-08 (aq-01937 q02 and q03, user report "q02 and q03 are too eash to pass quick test"; tested
  wording not supplied, rev 1 of each assumed): both were solved by the form's easier solver. q02: a renamed
  caption (2026 "Software services" = 2024 "Front office software and data", not the old caption's total)
  whose mapping a third release's reclassification note states, then two lookups and a ratio. q03: a
  restated quarter pinned by another line's printed value ($127 million other fee revenue), with the
  old-basis rate printed in the natural place (Doc 6's 19.1% QoQ). A pin that is one unique printed cell
  leads straight to the restated column, and a note that states the mapping is a lookup. Both dropped; the
  replacements avoid that note: an unprinted half-year backed out of a slide-footnote full-year total beside
  a non-GAAP headline (q04), and a backlog figure chosen by publication date when the event's own release,
  dated one day later, prints the next quarter (q05). Platform pending.

- 2026-10-08 (aq-02028 q01, twenty Productivity Commission maritime-logistics submissions; user screenshot plus
  "Too easy to pass quick test" on rev 4, after "too easy" on rev 2): an untied date anchor (only Doc 6 dates the WA
  coastal-trading exemption's end, 31 March 2022) selecting rate versions in Doc 2's surcharge table, where the day fell
  after Patrick's scheduled rises (7/03/2022) and one day before Flinders Adelaide's (1/04/2022), with the answer a mean
  of all 13 import rates ($117.39), was solved by the form's easier solver. Effective dates printed beside each value
  are lookups, even with a one-day boundary and a 13-row aggregate; no printed figure answered the surface question, so
  nothing lured the solver. q01 dropped; replacement q02 puts a printed same-scenario result beside the method (Doc 8's
  342,857 fewer truck trips on its own 3 million TEU) and fixes a different base found only in another document (Doc 1:
  2.88 million, stated by the port's newest terminal). Platform pending.
- 2026-10-08 (aq-01960, user report "both of q02 and i03 are too easy to pass quick test"): two more quick-test
  failures in the same bundle. q02 summed four guidance-implied gross profits (revenue x GAAP margin midpoints from
  D10-D13, each block naming its quarter) against D14's fiscal-year GAAP gross profit; the off-by-one edition pairing
  did not catch the easier solver, so volume plus labelled pairing is no trap (as aq-01322 q03). i03 asked the GAAP
  EPS guidance midpoint in force when the June 11, 2026 split took effect, per post-split share ($0.966 from D13);
  the decoy, D14's own post-split guidance, names a later quarter ("ending in September"), which disarms it. An
  event-to-edition trap needs a same-target decoy (full-year outlook in aq-00964), which per-quarter guidance
  cannot supply. Round 3 offered i04, a fiscal-year figure whose printed grouped input (178,075) is the decoy.
- 2026-10-08 (aq-01543, twenty ITA country energy chapters; target Medium, no Easy slot; user reports without tier
  lines). q01 rev 9: Bulgaria's 2024 coal share built as baseload "(coal, nuclear)" minus nuclear, with the printed
  Sep 2024-Aug 2025 27.6% as the decoy; once "calendar year 2024" was stated (needed after the form's "does not give
  this answer" on "In 2024"), the Quick test read "Too easy. Solver got it". A decoy whose window shows in its own
  sentence is disarmed by the condition that makes the question fair. q04 rev 0: Koeberg's 1,830 MW divided by South
  Korea's in-operation capacity, a 23-row status-filtered sum (23,500 MWe) against the prose's "approximately 26"
  GW(e) total installed in the same sentence, plus "Expected to be in operation" rows and two blank-status Kori rows:
  "passed the test and estimated as Easy tier". A part-vs-total lure plus row-membership traps in one table reached
  Easy, not Medium. Verbatim (saved page tasks/aq-01543/verdicts/AQ-01543_difficulty_2026-10-08_1236.txt, version
  a39f39, Run 1): "In band — Easy tier", Low 1/5 · Medium — · High —, with "This question may be too vague" (7.20% x3,
  7.04% x1). Every wrong attempt summed the table, counted 25 reactors (Kori-3 and Kori-4 have no status of their own;
  Kori-2's one cell lists three offline dates) and saw the conflict with the prose's "23 of which are currently in
  operation"; three kept 25 and one fell back on the prose's 26 GW. The one right attempt also counted 25 first and
  dropped the two Kori rows only to match the printed 23. The "Expected to be in operation" rows caught nobody. Lesson:
  a printed count that settles a membership trap fairly is also the low model's check sum, so roughly one attempt in
  five uses it and the run lands Easy; for Medium, the fact that settles the trap has to sit in another passage or
  document than the one the solver is already reading. The high model with Doc 4 counted the two Kori rows in one of
  three runs.
- 2026-10-08 (aq-01937 q01, platform difficulty check Run 1, version d017fd = the rev 1-3 question and gold;
  raw tasks/aq-01937/verdicts/AQ-01937_difficulty_2026-10-08_1238.txt): "Too hard", Low 0/5 · Medium 0/5 · High 0/5, all 15
  attempts at 22.69% (total AUM growth), with the run note "This question may be too vague". The question named the gold's
  scope exactly ("the assets for which State Street was the investment manager", the release's own note (2) wording) but
  gave no sign that it differs from the printed AUM total, so no attempt at any level looked for the carve-out notes. Eight
  local Opus solves across revs 0-3 had all applied it, and local reviews predicted Easy: an untied scope phrase that reads as
  a synonym of the printed total can overshoot past High. Rev 4 adds a half-step cue ("as opposed to all of its reported assets
  under management") without naming the excluded products, their amounts or their documents; platform pending.
- 2026-10-08 (aq-02028 q02 rev 1, platform difficulty check Run 1, version cdda71 = rev 1's question and gold; raw
  tasks/aq-02028/verdicts/AQ-02028_difficulty_2026-10-08_1348.txt): "Too hard", Low 0/5 · Medium 0/5 · High 0/5, with
  "This question may be too vague". The question asked for the truck trips saved "using the port throughput Melbourne's
  newest container terminal states"; that terminal's submission prints the whole port's throughput (2.88 million TEU) in
  one sentence and its own (800,000 TEU, "a third of the market") in another. 9 of 15 attempts at every level took the
  terminal's own figure (120,000), 1 its design capacity, and 5 the method document's printed 450,000 on its own 3 million
  base, the declared trap (two Medium attempts merged 2.88 with 3 million). One Medium attempt computed the gold and
  dropped it, asking whether the trips saved were the terminal's or the port's. Lesson: when a part-entity's document
  states the whole entity's figure beside its own, a source-attribution phrase ("the X the terminal states") reads as the
  part's own figure at every level; name the scope ("whole-port") in the question. Rev 2 does; platform pending.
- 2026-10-08 (aq-01937, user report "q01 and q04 is too easy to pass quick test"; wording not supplied): q01 rev 4
  ("...the investment manager, as opposed to all of its reported assets under management...") was solved by the easier
  solver: once told the asked figure is not the reported total, finding both dated carve-out amounts is a search. With
  rev 1-3's untied wording Too hard (0/15), one cue word separates the extremes, so rev 5 tries a midpoint ("actually the
  investment manager") as the family's last step. q04 (a half-year backed out of a full-year footnote total, the non-GAAP
  decoy printed in the same sentence as its GAAP figure) was solved too: a short identity on labelled figures, with the
  decoy disarmed in its own sentence, is a lookup path. Dropped.
- 2026-10-08 (aq-02102 q02, user screenshot, quick test "Too easy — solver got it"): two short explicit union lists
  in different documents (2016 acceptors; 2023 engaged unions) minus the three that wrote, with an acronym alias
  (Doc 5's PGA = Doc 4's Prison Governors' Association) and a look-alike (POA). The low model resolved the alias
  unprompted and applied both filters. A match-then-exclude over short printed lists is a lookup path even with an
  alias; local removal probes and a full-corpus Opus solve (match, high) said nothing about this. Dropped.
- 2026-10-08 (aq-02102 q01, user report "q01 is too easy to pass quick test"): a cross-document convention trap (two
  response tables, one counting off-topic responses and one not) with the separating condition stated in the question
  ("including those addressing no question") was solved by the low model; the untied wording had drawn a second-reading
  flag from a full-corpus solve (Doc 4's printed 107). Same two-state dead end as aq-01543 q01. Dropped.
- 2026-10-08 (aq-02086, UK housing policy, user reports "too easy" x4, no screenshots): four designs on one bundle all
  failed the quick test. q01: a landlord's stock from one document's glossary through another's stated per-home rates
  (5 multiplications). q02 rev 1: annexed examples vs a phased rule whose first phase takes every emergency (instance
  level); its rev 0 type-level wording was form-blocked with one form solver taking the emergency decoy. q03: a count
  from one table over a population summed from four counts in another document's cost section, with omission and
  inclusion traps. q04: the same phase rule asked by hazard type. The low model reads glossaries and cost sections,
  applies explicit exceptions and aggregates cleanly; explicit rules, stated rates and labelled table rows are lookup
  paths however many steps they take. Stopped after three rounds (WORKFLOW section 6).
- 2026-10-08 (aq-02165 q01, user report "it's too easy to pass quick test", no screenshot): two age rules in two
  documents, each stated relative to State Pension age (employer top-up from SPA - 10 in a 2017 proposal; an MOD-funded
  pension age of SPA - 3 in a response's union extract), asked as the gap so the unknown SPA cancels (7 years), with the
  Home Office police NPA 60 one bullet above as the look-alike. The low model crossed it: a cancelling reference is
  still two plain rule sentences and one subtraction, and a decoy in the target's own extract that the question's
  noun ("MOD-funded") excludes catches nothing. Dropped before any difficulty run.
- 2026-10-08 (aq-02147 q01, platform Run 1, version 8b4bdc; raw tasks/aq-02147/verdicts/): a rate printed only in the
  government response (employee respondents' median, 90%) applied to the consultation's break-even measure, which its
  table prints only for 60/70/80% (2, 3 and 4 weeks). The cumulative waiting-day computation gives week 12. Low 2/5
  (Easy band): three low attempts extended the printed 2-3-4 pattern to week 5, and so did two of the high model's three
  every-document attempts. A printed series one step short of the asked input invites the same extrapolation at every
  level, so it does not separate tiers, and the high model's every-document answer is at risk too. The run ended on the
  Document check (an identical case study in a second document), so Medium and High did not run.
- 2026-10-08 (aq-02165 round 2, user report "i03 and i02 are all easy to pass quick test"): a missed-election rule from
  the 2023 papers (only taper-protected mixed pensions change) applied to a 2016 count printed in the 2021-22 papers
  (54,807; deemed-election decoy 222,424), and a 1.5% element inside a printed 7.35% band rate (20.4%). Both are a rule
  or rate in one plain sentence plus a labelled cell. With aq-02102 q01/q02 and aq-02165 q01, five designs on these
  bytes measured too easy; the bundle has no dated edition series and no grouped figure split across documents.
- 2026-10-08 (aq-02147 q03, quick test, user screenshot in tasks/aq-02147/notes/platform-feedback/): "Too easy — solver got
  it". Two labelled table lookups in two documents (the 2021 response annex's median retention saving, £8,000; the 2024
  consultation's current and 80% SSP cost totals) plus a subtraction and a division, with look-alikes in the cost document
  (an average £30,614 cost of losing an employee, the £1.07bn total). The low model went straight to both tables and named
  the right total row; look-alikes that the question's own nouns ("median", "rise over current") exclude catch nothing.
- 2026-10-08 (aq-02208, two quick tests in one batch, user report "q01 too easy, i11 survived"; Federal Register rules,
  an FCC Bureau proposal (Doc 2) and its final procedures (Doc 4)). q01 (list of proposed coordination-request items
  required of no licensee in the final lists: two silently dropped items, with moved-item, suborbital-exemption and
  "none" decoys) was too easy: the easier solver diffs two long lettered lists across editions. i11 (how many more
  items one identically headed list holds in the final edition than in the proposal, 17 - 12 = 5) survived: Doc 4's
  discussion names three of the five additions (two items moved silently from proposed registration), so a solver
  that takes the final document's own account of its changes answers 3. Quick test only; no tier measured yet.
- 2026-10-09 (aq-02208 q02, difficulty check, user report "Passed difficult check as Easy tier"; tier line not captured): the
  i11 count that survived the quick test (17 - 12 = 5; Doc 4's prose explains three of five additions) measured only Easy, so
  the low model reached 5 in some of its attempts. One quick-test miss is one easier-solver attempt, not Low 0/5: a survivor
  can still land Easy. Here the cheapest mechanical route (count the letters a-l and a-q in two identically headed lists and
  subtract) reaches the gold, and only solvers that reason from the prose take the decoy. Untested design inference: for
  Medium, make the cheapest mechanical route land on the decoy and keep the gold behind a check another document supplies.
- 2026-10-09 (aq-02220, four UK heat network zoning papers; user reports without panels: "q01, i02 too easy. i03 survived",
  then "q03 too easy", stage not stated). Three cross-document numeric joins on the impact assessment were solved by the low
  model: q01 (benchmark heat shares, Doc 4, turned into input shares with the IA's Table 24 efficiencies), i02 (the IA's
  2035 deployment as a share of the 2035 target) and q03 (the latest 2050 share, "a fifth" in Doc 4, times the IA's 439 TWh
  England 2050 demand). q03 had survived its quick test with identical wording, a second case after aq-02208 i11 where one
  easier-solver miss did not hold. q03 rev 0 copied Doc 4's verb ("now expected to supply" vs "expected to provide a
  fifth"), so the cheapest route led straight to the gold; rev 1 paraphrases it ("most recently stated 2050 share") so
  the cheapest route stays inside Doc 2, whose own paragraph 4 gives the older CCC 18% (79.0 TWh decoy). Rev 1 was also
  "too easy" at the quick test (2026-10-09), as were i06 (IA waste-heat mix x 2050 deployment against the consultation's
  economic waste heat, 42%) and i07 (respondents' top per-zone staffing x the IA's 510 zones). Removing the copied verb
  did not move the low model off the gold: the share sits in the first paragraph of the bundle's shortest document, so
  a whole-context reader meets it anyway. Bundle closed with no fair Medium design (seven designs).

- 2026-10-09 (aq-02483, user quick-test report "q01, i03 too easy. i04 survived", no panels): a version cutoff ("promulgated
  through December 14, 2020") that the solver had to map onto EPA's dated amendment list, then subtract from another
  state's cutoff, was too easy, as was a count of Legacy-Rule definitions one state keeps federal and another approves.
  A deadline rule ("within 12 months of the effective date of the State rule") in one section, applied to an effective
  date stated in another section of the same notice, then compared with a second notice's printed deadline and rounded
  to weeks (28; decoy 24 from the effective date), survived. Quick-test results only; no tier measured yet.
- 2026-10-09 (aq-02483 q02, difficulty Run 1, Version 7ed75f, raw tasks/aq-02483/verdicts/AQ-02483_difficulty_2026-10-09_1025.txt):
  the quick-test survivor above was "Too easy", Low 5/5. All five low attempts quoted the Wisconsin deadline and the Wyoming
  rule, then chained the rule's own pointer ("within 12 months of the effective date of the State rule") to the effective
  date several paragraphs away; none took the effective date as the deadline. Platform notes: "the only inference required,
  and it sits a few paragraphs from the deadline sentence"; "the state names in the question made retrieval immediate". A rule
  that names its own missing input is no trap, whatever the distance. With aq-02447 q01 rev 2 (quick test survived, then Low
  5/5), two quick-test survivors in a row failed the difficulty check: a survival is a weak signal, not evidence of Medium.
- 2026-10-09 (aq-02564, user quick-test report "q01, i02 too easy for quick test", no panels): two word-for-word parallel SEC
  notices (Cboe EDGX and BYX hosted-subscriber fee programs) differing only in their own feed's fees. Too easy: (1) a hosted
  subscriber's total monthly fee reduction across both notices at 10,000 users ($1,400), whose decoy was each notice's
  footnote "maximum, savings" ($250 + $150, user fees only); the footnote's own arithmetic shows its scope, and the question's
  "total ... than under the existing programs" pointed at the waived Distribution Fee; (2) a host's bill using the host-pays
  and per-firm user-count rules ($1,475), both stated in the fee paragraph. Unlike aq-02486 (one agency's no-fee rule
  absent from the other's text), the two notices share every rule, so there was no rule to misattribute; plain parallel fee
  arithmetic stayed within the easier solver's reach. Quick-test results only; no tier measured. Round 2 (user,
  2026-10-10: "i03 survived"): a host whose only hosted subscriber passes the 10,000-user cap loses its credit and
  returns to the existing discounted fees ($1,250 at 2,000 host users), an inference from the notices' two-subscriber
  example rather than a stated case, survived the quick test. A survival is a weak signal (aq-02447, aq-02483).
- 2026-10-10 (aq-02564 q02 rev 0, difficulty Run 1, Version be6014, raw tasks/aq-02564/verdicts/AQ-02564_difficulty_2026-10-10_0227.txt):
  that survivor (host at 5,000 users, $1,625) was "In band — Easy tier", Low 2/5. All five low attempts made the
  eligibility inference (the rule states its own condition, with an example), so the declared trap caught no one. The three
  misses answered "$1,000 ... plus the usual per-user fees" and never priced the users; the two hits took the rate from a
  footnote's arithmetic ("10,000 Users x 0.10/Non-Professional User"). A rate printed only inside a footnote calculation is
  found by the low model about half the time (2 of 5 here, 2 of 3 quick tests on this bundle), which by itself gives Easy,
  not Medium; an unquantified answer is graded wrong. The low model also treats two parallel notices as "the Program".
  Third quick-test survivor in a row below target at the difficulty check. Rev 1 makes the two notices two programs (one
  subscriber on one exchange only, another over one exchange's cap), $2,375; platform pending.
- 2026-10-10 (aq-02564 q02 rev 1, difficulty Run 2, Version 8ce393, raw tasks/aq-02564/verdicts/AQ-02564_difficulty_2026-10-10_0356.txt):
  "In band — Medium tier", Low 0/5 · Medium 3/5, "+$20 Medium+ bonus if accepted"; submitted by the user at Medium.
  Low 1 $1,750 (own user fees unpriced); Low 2, 3 and 4 $875 (per-feed analysis and both footnote rates right, but the
  two $750 set fees left off the host's bill: "The hosted subscribers pay their own flat fees"); Low 5 $2,125 (BYX credit
  kept). Medium 1, 2 and 4 right; Medium 3 $1,750; Medium 5 $2,387.50 (credit kept, over-cap users billed per user).
  Both documents needed, closed-book missed ($28,500), no advisory. The step I had rated safest (host pays) did most of
  the separating and the declared scope trap none: see recipe 3 and the trace rule above. Acceptance not observed.
- 2026-10-10 (aq-02631 q01 rev 0, difficulty Run 1, Version 45cf69, raw tasks/aq-02631/verdicts/AQ-02631_difficulty_2026-10-10_1045.txt):
  "Too easy", Low 5/5. Design: an edition choice between an original filing and its amendment, fixed by a procedural
  event the question names ("when the SEC instituted proceedings on it") and dated only in the amendment's notice, joined
  to another fund's printed weight (gold 0.35%, the wrong version gives zero). All five low attempts named both versions,
  dated the event against the amendment and chose the original for that stated reason; attempt 4 wrote that the amended
  list "would give 0%. That can't be the intended answer". The Coach said solvers "simply used whichever list they
  retrieved first"; the traces contradict it. Scope of the lesson: this is not the untied event trap that measured Medium
  (aq-00964 q01, aq-01322 q01), where the event belonged to the business, not to the document's own history, and several
  editions preceded it. When the anchor is a step in the filing's own procedure and only two versions exist, the timeline
  check is the obvious first move; and a wrong route that ends in zero or "none" tells the solver to look again. The same
  choice on another fact (launch minimum, 2.5 times) and a two-lookup date gap whose date sits in the twin order (31 days)
  were too easy at the quick test, as was a cap-derived weight whose method and eligibility test the question named.
- 2026-10-10 (aq-02631 q03 rev 0, difficulty Run 2, Version 45cf7c, raw tasks/aq-02631/verdicts/AQ-02631_difficulty_2026-10-10_1309.txt):
  "In band — Easy tier", Low 2/5 (target Medium, no Easy slot per the user). Design: a rule from one filing (Nasdaq's
  proposed 90% surveillance test, with a printed weight table) applied to a dated event printed only in an unrelated
  filing the question never names (CME Solana futures, March 18, 2025, in a T. Rowe Price notice's asset background);
  gold a date. All five low attempts found the rule, summed the covered weights (88.43) and identified Solana as the
  cure, unprompted. Two read the other filing and gave its date. Three answered "March 17, 2025" from memory, the
  real-world launch date, one day before the date the document prints, and were marked wrong. So the bridge to an
  unnamed document did not stop the reasoning; the only separator was grounding against recall, on a fact where the
  document and the world differ by a day. With q01 (5 of 5) this makes every low attempt that read the deciding passage
  right on this bundle (7 of 7): where the low model reads, plain rule application, list comparison and date logic do
  not fail it, and a question then lands at whatever rate it skips the reading (here about 3 in 5), which is Easy, not
  Medium. A document date that differs from a recallable real-world date is a grounding trap, not a reasoning step:
  note it at sketch time (check dated events against memory) and do not count on it for a tier.
- 2026-10-10: aq-02673 q04/q05 (NOAA bluefin quota proposal D03 and final rule D06), one hook measured at four
  strengths of scope phrase, same gold (168.84 mt), documents and evidence throughout. The gold lies between two
  differences the final rule's table prints as rows: Baseline 193.84 below it, Total 231.34 above it; one sentence
  in the proposal says the earlier set-aside was drawn from the western catch limit and the new one is not.
  - No scope phrase ("... total allowable catch was the United States allocated ..."): Run 1 Too hard, Low 0/5 ·
    Medium 0/5 · High 0/5, all 15 at 193.84, "may be too vague".
  - "in total": Run 2 Between levels, Low 0/5 · Medium 0/5 · High 4/5 (low and medium still 193.84, one low and
    one high at 231.34).
  - "whatever fishery the tonnage was reserved for" (names the kind of thing that counts, not the item or the
    test): Run 3 In band - Medium tier, Low 0/5 · Medium 1/5; wrong answers 231.34 (5 of 10) and 193.84 (4 of 10);
    Document check: both documents needed.
  - "counting any longline bycatch allocation drawn from that TAC" (item and test named): too easy at the quick
    test (user report, no capture).
  Reading: this is measured Medium recipe 4. The step from Too hard to Medium was a phrase, not a new fact; the
  quick test passed both midpoints and did not tell them apart, the difficulty check did. Working rule drawn from
  it: (1) when the deciding condition sits only in a document, never run the question with no scope phrase (that
  run was wasted and the risk had been written down beforehand); (2) prepare two or three scope phrases of
  different strength for one quick-test pass and take the most explicit survivor to the difficulty check; (3) a
  phrase naming the kind of thing that counts beats both a bare "in total" and a clause naming the item.
  One hook on one bundle: evidence for this mechanism, not a rule for other shapes.

- 2026-10-11, aq-02940 (NZ Commerce Commission draft decision on commercial credit interchange caps plus a survey
  and 14 submissions; user: "three all too easy for quick test", no panels pasted): quick-test too easy were
  (1) a response rate stated in one document (0.39% lower merchant fees per 1% lower interchange) applied to the
  other's percentage cut and fee base, gold $26.5 million against the wrong-base 19.5, in an explicit wording and
  in one that left the percentage reading to the source sentence; (2) a share built from one document's total
  ($170 million of $1 billion = 17%) beside the other's printed look-alike pair (19% and 8%), gold 9 points
  against 11. My reading, not a platform statement: on a one-rulebook-plus-commentary bundle, a two- to four-step
  numeric join whose ingredients the question names is solved by the easier solver even with a wrong-base or
  look-alike route beside it; the phrase that excludes the decoy is also the phrase that finds the input.
  Three results on one bundle: evidence for these two shapes, not a rule for others.
- 2026-10-11 (aq-02750 q04, capture tasks/aq-02750/verdicts/AQ-02750_difficulty_2026-10-11_1820.txt). Run 2,
  rev 1, Version 0e525b: "Too easy", Low 4/5 (this is the result logged above from chat as a quick test; the
  capture settles it as a difficulty run). Run 3, rev 2, Version bd63c0: "A marked document may not be
  needed", Low 3/5, Medium and High not run; reached the gold without Doc 5 and without Doc 7, needed Doc 4
  and Doc 6. Rev 2 had restored the valid letters on the sibling order and timed three batches "20 days after
  comments closed on the prior order". Every wrong scored attempt in Runs 1-3 counted the rule's letters; none
  was lost on dates. So the earlier inference that the valid letters on the sibling order are what arms the
  trap is not supported: with them back the low model still read the block 3 of 5. What separates rev 0
  (0 of 5) from revs 1-2 is explicit against derived dates, on 15 attempts, cause not isolated. Without Doc
  6 the high model wrote "15-day comment period → deadline July 28, 2026 (July 13 + 15)" and dropped the
  batch of July 30; without Doc 5 it used "~July 6" and nothing changed, because no batch lay between July 6
  and July 10. Rev 3 (lag from each order's issue date, 18 days; August order and Doc 7 dropped; gold 89)
  pending.
- 2026-10-11, aq-02940 q04 rev 0, difficulty Run 1 (Version 659f9e): "Between levels", Low 0/5, Medium 5/5. One
  dated case (decision on the submission deadline) run through two named banks' timing requests, asked as a day
  count (262). All five low attempts stopped at the first bank's lead time (243) and never read the second
  bank's first-of-month sentence, which sits two paragraphs below its six-month request; all five medium
  attempts read it. My reading: a rule in a separate paragraph of a party the question names separates low
  from medium completely, so it sets the floor (Low 0/5) but cannot by itself give Medium; the medium solver
  needs a second gate it does not reliably pass (rev 1 adds a rule that depends on which items are meant;
  result pending). The quick test had passed this design ("i09 survived"), as it only measures the low solver.
- 2026-10-11 (aq-02750 q04 rev 3, difficulty Run 4, Version b97466, raw
  tasks/aq-02750/verdicts/AQ-02750_difficulty_2026-10-11_2048.txt): "In band — Easy tier", Low 2/5 (target
  Medium, no Easy slot per the user; the form shows Easy 0/1). Rev 3 timed two batches 18 days after each
  order's issue date, so each landed between the 15-day fallback date and the notice's printed deadline, and
  dropped the third order. Document check: each of the three ticked documents needed twice, with exactly the
  answers computed beforehand for the fallback routes (67, 70) and for the rule's notice missing (62). So the
  between-fallback-and-printed test predicted the Document check on its first use. All three wrong low
  attempts counted the rule's letters. Low-model record across the four versions of this one trap: 0/5, 4/5,
  3/5, 2/5; treat any single count as a draw from a wide range.
- 2026-10-11, aq-03066 (NZ Commerce Commission fibre input methodologies: six December 2018 submissions plus the
  Commission's May 2019 summary paper and June 2019 workshop pack; user "no slot for Easy Tier ... target medium
  and high"). Four sketches, all quick-test "too easy" (user chat, two messages, no panels pasted):
  - a ten-year rerun of the workshop pack's illustrative loss table at a rate printed only in one submission,
    where the rate is used twice (return on capital and discounting), gold a 6% fall;
  - a first-period write-off of that table's loss asset over four regulatory periods with the first fixed at
    three years, gold 257;
  - a three-company membership over six quality dimensions with one company's position stated as a single
    grouped clause ("the full lifecycle dimensions set out in the CEPA report"), asked as the "exactly two"
    list and as a total of 14.
  What this adds: recipe 5's grouped item worked on templated proposals with long parallel lists; one grouped
  clause that a footnote in another document resolves in a single step is no trap. A what-if whose rule or
  parameter the question names is solved even with ten compounding terms. Policy-consultation bundles whose
  figures never share a period or basis (each submission's numbers its own) offered no numeric join outside the
  regulator's one worked example. My reading, from quick tests only; no difficulty run was spent.
- 2026-10-11, aq-02940 q06 rev 0, difficulty Run 2 (Version 7017d1): "In band - Easy tier", Low 3/5, all three
  documents needed. Same hook and buried first-of-month clause as q04 rev 0 (Low 0/5, Medium 5/5), with the
  first party changed from ASB (one lead time) to Mastercard (nine months domestic, twelve cross-border) and
  two asks. Quick tests in between: the single-ask Mastercard wording was too easy twice and survived once.
  My reading, from the traces: with ASB the lead date (13 March 2027) fell twelve days past the other party's
  printed "1 March 2027 at the earliest", and every low attempt stopped once that comparison was settled;
  with Mastercard the lead dates fell months past it and three of five low attempts read on to the clause. So
  a buried clause holds the low solver only while a near-miss printed figure absorbs it, the medium solver
  reads the clause every time, and one quick-test survival did not carry to a sibling wording. One bundle,
  two runs: evidence for this hook, not a rule.
- 2026-10-12 (aq-02750 q06 rev 1, quick test, user chat "too easy for quick test", no panel or trace, one draw;
  route unread): a list of the CFR sections amended by one rule's instructions or by the surviving parts of
  another (six of eight candidates across two documents), with one member amended only in the last instruction
  of an 84,000-character document beside a footnote calling its amendment "unnecessary", did not stop the
  easier solver. This was built on the late-member shape of aq-02501 q01; what differs here (author's
  inference, untested): the late member sits under its own "Sec. ... [Amended]" header in numbered
  amendatory text, where that bundle's sat in a prose clarification, so a scan of the instructions finds
  it. Bundle tally: eleven versions in four families, seven quick tests too easy, four difficulty runs on
  the one survivor, nothing at Medium; release recommended after three rounds.
- 2026-10-12 (aq-03143 q01 rev 0, difficulty Run 1, Version 45b6c4, raw
  tasks/aq-03143/verdicts/AQ-03143_difficulty_2026-10-12_1221.txt): "In band — Easy tier", Low 2/5 (target
  Medium, no Easy slot, not submitted). A stated bill outside London under the UK civil legal aid fee changes:
  two legal help matters whose equal hourly claims fall on opposite sides of category-specific escape
  thresholds (housing three times the fee, immigration twice, the second threshold unprinted; rule only in the
  consultation) plus a court attendance rate the response raised. Read from every wrong attempt's own Full
  answer and Reasoning: all five low attempts applied both thresholds correctly, and the quick test had
  already solved the same case without the phrase naming the kinds of payment. The three misses were all in
  the attendance cell: two attempts saw the response's single printed lower-courts rate (£52.00), noticed it
  equals 75% of the London rate and paid 75% of the non-London rate instead (£49.00) because the question says
  outside London; one took the 50% row, the consultation's proposal. The strongest solver weighed the same
  two readings at length before taking the printed rate, and without the response it took the rule's £49.00.
  My reading: on this bundle a rule with printed inputs is no gate, even stated twice with different
  multiples; what separated attempts was a printed table value set against a general rule that the question's
  qualifier seems to trigger, and that is a choice made once per attempt, so repeating the cell would not
  compound it the way aq-02749's per-entry misread did. Round 2 keeps that cell and adds gates of another
  kind (work the increase does not reach); unmeasured. One run on one bundle: evidence for this hook.
- 2026-10-12 (aq-03169 q01, ten responses to the CMA audit-market invitation to comment; quick test, user chat
  "too easy for quick test", no panel or trace, wording not stated, one draw). The design was a five-step chain across
  two responses: a per-firm client cap turned into a total (4 x 65 = 260), the Big Four's present audits from a count
  of the audits other firms hold (350 - 11), the difference timed at the yearly rate another estimate implies
  (60 wins in five years), rounded to whole years, with a two-part gold ("260 audits and 7 years"). The gold lay
  between the two obvious short cuts (6 by scaling shares, 8 without the 11 held). The easier solver reached it.
  My reading: a gold between two wrong answers is a gate only when a sentence in the other document decides which
  reading applies (aq-02673 q05); when the offset is a printed count in the paragraph that also gives the rate, it is
  one more arithmetic step. Round 2 on the same bundle moved to a two-table membership filter with a carried-over
  benefit ("All other benefits of 1 above"), the aq-02749 kind of step; unmeasured. One draw on one bundle.
- 2026-10-12 (aq-03143 q01 rev 1, difficulty Run 2, Version c26715, raw
  tasks/aq-03143/verdicts/AQ-03143_difficulty_2026-10-12_1644.txt): "Too easy", Low 5/5. The repair of the entry
  above kept one escape matter and the attendance cell and added two cells that turn on whether the fee increase
  reaches the work at all: a matter opened before commencement (stays on the old fee, rate and threshold) and
  the same attendance in a category outside the increase (stays on the old rate). Read from all five Full
  answers: every attempt got all four cells, and no attempt took the 75%-of-non-London rate or the proposed rate
  that three of five had taken on rev 0. So on this bundle every stated-rule gate tried (two escape multiples,
  commencement, scope) was cleared 15 times in 15, flagged in the question or not, and stacking four of them made
  the question easier than two. The only gate that ever split the solvers was the table-against-rule choice, and
  it did not recur once a second item from the same table row was in the bill (attempt 2's reasoning uses the
  row's single current rate; whether that is the cause is my inference, five attempts each way). Workspace rule
  already on file and not applied: start-from-measured-misses step 4, a family the capture shows solved stays
  closed however many cells are added. Bundle tally: six sketches quick-tested (four too easy), two difficulty
  runs on the survivor's hook (Easy, no slot; Too easy), nothing at Medium; hook retired, release recommended.
- 2026-10-12 (aq-03169 q02 rev 0, difficulty Run 2, Version 3beb81, raw
  tasks/aq-03169/verdicts/AQ-03169_difficulty_2026-10-12_1739.txt): "In band — Easy tier", Low 2/5, closed-book and both
  Document checks passed. A two-table membership filter: seven measures one response rates High for costs and Low for
  benefits, kept when another response's annex lists an independence benefit, one member only through "All other benefits
  of 1 above" (announced in the question as "stated outright or carried over"). Read from each wrong attempt's own Full
  answer and Reasoning: all five low attempts read the ratings table correctly, group headings included; the two right
  ones found the annex at the end of the longest document (after a long unrelated annex), used it alone and followed the
  cross-reference; the three wrong ones concluded the annex "is not included in the text", fell back on the reply, linked
  a ban for audit clients to the wider all-clients prohibition (3 of 3) and took another respondent's same-numbered answer
  for this respondent's (2 of 3). The strongest solver read the annex row by row. My reading: on parallel responses to one
  questionnaire the low model (a) loses content that sits after an unrelated annex and (b) blends same-numbered answers
  across respondents; a table it has found, cross-reference included, it reads well. Both declared failure modes missed.
  Rev 1 keeps the tables and splits the members between the annex and the reply so that neither place alone answers;
  unmeasured. One run on one bundle.
- 2026-10-13 (aq-03169 q02 rev 2, difficulty Run 3, Version 2277b0, raw
  tasks/aq-03169/verdicts/AQ-03169_difficulty_2026-10-12_2314.txt): "Between levels", Low 0/5 · Medium 4/5. Rev 1/2
  had rebuilt rev 0 (Easy) so that neither the respondent's annex nor its reply answers alone: two asks over the seven
  measures another response rates High for costs and Low for benefits, three members for "less concentrated" (two annex
  rows, one reply sentence) and two for "reduce or destabilise audit quality" (annex cost lines after page breaks), asked
  with "say anywhere in its response". Read from every wrong attempt and the three recorded right ones: the low model
  listed the seven table rows correctly every time (10 of 10 over two runs), never used the annex in four attempts and
  used only the annex in the fifth, so the either-place gate held it at 0; the medium model found the annex every time,
  joined it with the reply, and lost one attempt on a continuation line after a page break. All four visible medium
  attempts took the rating set from the table's last block, headed "Measures that we do not support", and never listed
  the one High-then-Low row that sits under "appear to have merit"; it cost nothing because that row is in neither
  group. My reading: on a ratings table split under headings, the low model reads rows and the medium model reads the
  heading that matches the question's sense; and "anywhere in its response" is a completeness cue of the "Wherever"
  kind. Also seen: the advisory "the grading could not settle which answers match your gold" fired on a two-group list
  answer because a wrong and a right attempt shared the same picked-out last line; it is not a finding about the gold.
  Rev 3 removes the cue and adds nothing; result pending. One run on one bundle.
- 2026-10-13 (aq-03711, fourteen papers from the NZ Commerce Commission's 111 Contact Code review; quick tests, user
  chat "q01 too easy for quick test. and the following one, too", no panel pasted, so the easier solver's routes are
  unread). q01 rev 0: "At how many of its retirement villages and care homes did Bupa itself owe 111 Contact Code
  duties on the Commission's preliminary view, and how many under its final decision?", gold 39 and none (Bupa
  supplies no landline in its 35 villages; its 39 care homes are health care services under the final decision).
  Sketch i11: Spark's $1,599 battery price times the Commission's battery shares of means (8% in 2021, 15% in 2022),
  $111.93 higher. Both too easy. No difficulty run was spent. The caller and two independent author runs found no
  other two-document design outside the date-count family: the final paper restates the old rule, the draft
  decision and the final rule for every amended topic, and the draft paper's appendix quotes each submission. Two
  date sketches (239 days from the scheduled month to publication; the draft's 3-month commencement clause against
  the grace period) were left untested. One result per design on one bundle.
- 2026-10-13, later the same day (aq-03711; user chat "last one survived", no panel): of the two date sketches,
  the one that derives a date from the draft's "3 months following the publication" clause and counts the days to
  the end of the grace period (26 September 2024 and 97 days, two asks; i03, now q02 rev 0) survived the quick
  test. The other date sketch's result was not stated. I had told the user this family "did not hold on sister
  bundles" and recommended release with both sketches untested; the survivor was one of them. A family's history
  is not a result for an untested sketch: when quick tests are plentiful, offer the untested sketches without a
  release recommendation attached. Difficulty result pending; a quick-test survival sets no tier.
- 2026-10-13 (aq-03635, NZ Commerce Commission retail fuel study, eleven papers; user: "Easy tier, but not
  submitted as no easy slot open. please check the arrived verdicts and analyze it using your feedback skill and
  upgrade it."): quick tests (user chat, no panel) i06 failed, i07 survived; i07 became q03 rev 0 and difficulty
  Run 1 (Version 0d7da7) was "In band — Easy tier", Low 2/5, both documents needed, closed-book missed (1.0).
  Read in every attempt's own Full answer and Reasoning (capture lines 342-1977): all five low attempts took the
  earnings average (283) from the appendix, the range top (8.6%) from the other document and the pairing
  correctly; low 1, 4 and 5 answered 3.7 from the mean of three year-end balances, having seen the chart's 2,085
  ("might be for one year"; one read the document's "approximately 9%" as confirming its own 12.3%); low 2 and 3
  took 2,085 on the wording match. The strongest solver took 2,085 and cross-checked the nine-point claim. The
  platform's one-line notes agreed with the traces here. What I had wrong beforehand: I ranked the yearly
  peak-year form (i06) first when I believed no quick test was left, and the quick test then called it too easy;
  the trap I declared on q03 (a printed 14%) caught nobody, and the separator was a step I had treated as
  settled by the printed label. A quick-test survival again preceded a below-target run (as on aq-02447,
  aq-02483): one survival does not show Low 0/5. Repair handed over: rev 1 with the chart-title words removed,
  no gate added, same gold. Result pending.
- 2026-10-13, later (aq-03635 q03 rev 1; user screenshots of the form Checks): "One defensible answer" Failed,
  "They answered "4.4 percentage points" and "3.7 percentage points"", the two routes named in the hand-over
  before the check; advisory "Each description fits one thing": "Z's own capital employed" has two matches (the
  appendix row and the chart figure). No run was spent. The half step I had announced as the fallback (put
  "average" back) was withdrawn after re-reading Run 1: the right low attempt quoted that phrase as its reason for
  taking the printed figure, so the half step is the measured Easy configuration. q03 dropped for the stated
  tiers; untested sketches on other document pairs offered for quick tests without a release recommendation.
- 2026-10-13, aq-03711 q02 (user: screenshots with "three checks failed", then "too easy for quick teset"; raw
  tasks/aq-03711/notes/platform-feedback/2026-10-13-q02-checks*.png and .txt). Rev 0, "Under the draft amended 111
  Contact Code's own commencement clause, on what date would the amendments have come into force, and how many
  days before the grace period ended is that?", gold 26 September 2024 and 97 days: quick test survived, then the
  form's "One defensible answer" Failed, both solvers "18 March 2024, 289 days before the grace period ended"
  (three months from the draft's own cover date instead of the final Code's publication). Rev 1 gave the starting
  date one reading by making the final amendments the subject, added no cue, kept the gold: quick test too easy.
  So the survival measured the open term, as on aq-03120, and here no one-reading wording held the easier solver:
  the reasoning left was a clause lookup, a publication date, three months and a day count, which both form solvers
  had already done correctly from their own date. Carry forward: a quick-test survival on a derived gold is not
  evidence of difficulty until "One defensible answer" has passed on the same wording; and before offering a
  sketch whose rule is anchored on an event ("publication", "commencement"), list every dated instance of that
  event in the bundle (here the draft's and the final's publication dates, and two "Commencement" headings). Tool
  gap: `docket_agent.py screen` warns on period words only, not on an anchoring event with two dated instances.
  One bundle, routes of the easier solver unread.
- 2026-10-13 (aq-03169 q02 rev 3, difficulty Run 4, Version 86b24a, raw
  tasks/aq-03169/verdicts/AQ-03169_difficulty_2026-10-13_0743.txt): "Answer not supported", Low 0/5 · Medium 1/4, the
  high model 0 of 3 with every document. Rev 3 was rev 2 (Between levels, Medium 4/5) with the scope words "anywhere in
  its response" removed, as the platform's first "What to change" item proposed. All three high attempts answered from
  the respondent's costs-and-benefits annex table and left out the one member that only the reply states (joint audits,
  "a more dynamic and less concentrated market" in France); two said so ("per ... Annex 2", "not ... in the annex").
  The medium model read the reply first, found that member three times in four and failed elsewhere (a truncated
  rating set, a reply-only answer, a partly read annex). So on a list with one member outside a complete-looking table
  the high model is the one that stays in the table, and removing a completeness cue outright took the question from
  too easy for medium to unreachable for high in one step. This is WORKFLOW section 6 item 5 again (aq-02933): the
  scope has to be named ("Grant Thornton's response", rev 4, pending), not cued and not dropped. One run, one bundle.
- 2026-10-13, later still (aq-03635; user chat "all are too easy for quick test", no panel): four more designs on the eleven fuel-study
  papers were quick-test too easy, each on a different document pair: sites counted from one party's list for
  the chains in a nine-name list that only another party's schedule quotes (47; decoy chain named in the next
  sentence with "perhaps"); the same counts filtered by a stance two chains state in their own submissions, one
  of them only as "a waste of time" (26, three documents); the mean of three publication-to-submission gaps for
  one submitter, two dates in a footnote (41 days); a margin rebuilt on another party's tax total (28.65 cents).
  Six of seven designs tested on this bundle were too easy at the quick test; the seventh was Easy at Low 2/5 and
  blocked once its label words were removed. The bundle was reported as having no fair Medium or Hard design.
- 2026-10-13 (aq-03169 q02 rev 4, difficulty Run 5, Version 96eed6, raw
  tasks/aq-03169/verdicts/AQ-03169_difficulty_2026-10-13_1118.txt): "In band — Hard tier", Low 0/5 · Medium 1/7 · High
  3/6; submitted by the user at Hard. Rev 4 is rev 3 with one term changed, "does Grant Thornton say" to "does Grant
  Thornton's response say". Third rung of the scope ladder on one gold and one evidence set: completeness cue
  ("anywhere in its response") Between levels, Medium 4/5; no scope word, not supported, high 0 of 3; scope named with
  no search word, Hard. With the scope named both every-document attempts cited "Annex 2 and main response" and weighed
  the reply-only member; one accepted it and one called it "not explicit enough", and neither quoted the explicit
  sentence, which sits two sentences into the paragraph they quoted. Medium misses were single members either way
  round (a table row left out twice, the reply member left out once, one member added from a narrower measure's
  remark). The low model never used the annex rows. So this shape (members split between a costs-and-benefits table
  and the prose of the same response, set defined by another response's ratings) has a Hard point when the scope is
  named and nothing points at either place. Whole path: five difficulty runs and one form round; with the scope named
  and a plain comma-list gold from the first write-up it would have been two runs. One bundle.
- 2026-10-13 (aq-04045 q02 rev 0, difficulty Run 1, Version ce30ee, raw
  tasks/aq-04045/verdicts/AQ-04045_difficulty_2026-10-13_1602.txt): "Too easy", Low 5/5 (2 not scored). Three FCC
  fee rules of one proceeding: unit counts only in the further notice, per-unit fees only in the next year's order,
  one category's fee printed nowhere. One hook, three forms: the named category's share of all fees (31.5%, beside
  the rule's round 40% x 80% = 32%) and a carve-out under the printed 40% (39.4%) were both quick-test too easy; the
  dollar total for the unpriced category ($20.2 million) survived the quick test and then measured Low 5/5. Every
  scored low attempt found units and fees in different rules, put the small category's fees inside the larger share
  on the strength of an "after subtracting" clause, and scaled through the stated 60/40 split. One of them skipped
  the chain and multiplied the printed unit count by a per-station fee it remembered (about $144,000; the
  schedule's figure is within $150), while the closed-book attempt missed ($14.5 million): with the documents
  open the low model recalls a published fee it cannot recall cold. Two attempts credited one rule's passages to
  the other and still reached the gold. So on this shape: a chain of plainly labelled figures and stated splits
  is solved whatever the answer form, a step to a figure no document prints included; a round share one
  multiplication from the gold is no lure; a lone quick-test survivor whose sibling wordings failed on the same
  steps is noise (third survivor to fail the difficulty check, after aq-02447 and aq-02483). One bundle.
- 2026-10-13 (aq-04112 q02 rev 0, difficulty Run 1, Version 402a46, raw
  tasks/aq-04112/verdicts/AQ-04112_difficulty_2026-10-13_1701.txt): "Too easy", Low 4/5, run returned. A committee
  report plus two hearing transcripts. The gold was a margin over a threshold no document prints (the salary
  threshold as it would have stood had an advisory body's advice been accepted: the printed £25,600 less the 20%
  the report says a shortage listing brings), with the salary only in a transcript and the unreduced £25,600
  printed three times beside the occupation. The question named the advice and neither the list nor the 20%. All
  five low attempts found both figures and went straight from the named advice to the list and its rule; two
  computed the gold without hesitation, two weighed the printed-threshold answer (£900) and rejected it because of
  the question's opening clause ("the inclusion of MAC acceptance points to applying the SOL reduction"), and one
  took £900 after reading "the Skilled Worker Visa salary threshold" as the general one. Closed-book missed (it
  recalled the 2024 threshold). So on this shape: a derived floor beside its printed look-alike is no gate when
  the question's premise names the condition that produces it; a counterfactual clause is read as the method; a
  chain of lookups behind a named body is walked five times in five. The form of aq-02157 q04 (Medium) that this
  was modelled on did not carry over, and the quick-test survival did not predict the run (fourth such survivor).
  One bundle.
- 2026-10-13 (aq-04045 q03 rev 0, difficulty Run 2, Version 84ce0b, raw
  tasks/aq-04045/verdicts/AQ-04045_difficulty_2026-10-13_2012.txt): "Too easy", Low — · Medium 5/8; the check
  started at the Medium level on a set with no Easy slot. Shape: one boilerplate paragraph repeated in three
  rules with a different year-end each time; the earliest and latest editions sit once each in two rules on other
  subjects, the middle one three times in the on-topic rule; asked as the change in a share between the "earliest
  and latest year-end counts", no year named. The one unpointed step, finding both end editions, held three of the
  six medium attempts whose text is recorded: each took the thrice-printed middle edition as the earliest and said
  it had checked the document that holds the earlier one. Every attempt with the right editions computed
  correctly. One right attempt had missed the latest edition, got a fall, and re-read only because the question
  said "rise": a direction word in the question is a check the solver uses, as a printed count is (aq-01543 q04).
  By the page's rule (two solvers wrong twice, one right twice) one solver was wrong twice and two were right
  twice, grouping attempts by their opening sentences (inference; the page does not label solvers). The page
  counted two answers of 5.6 where the Full answers show three. Repair sent as a sketch: the same question asking
  for the signed change, nothing added. The first wording had survived one quick test. One bundle.
- 2026-10-13 (aq-04112 q03 rev 1, difficulty Run 2, Version baa047, raw
  tasks/aq-04112/verdicts/AQ-04112_difficulty_2026-10-13_2122.txt): "Too easy", Low — · Medium 4/6; the check
  started at the medium level, where Run 1 on the same set four hours earlier had started at the low one. Shape:
  witnesses who put a figure on how long training takes, three members in three answers across two transcripts,
  no trade, witness or hearing named. Every recorded medium attempt (four; two unrecorded) went through both
  transcripts for training times and found all three, an awkward sentence included, and set aside the other
  "18 months" and "two-year" figures; none stopped at the first hearing. So on this shape: a list whose members
  each carry the asked property word beside a number is a scan for the medium solver, however far apart the
  members sit. The sentence had survived two quick tests, which use the easier solver. One bundle.
- 2026-10-14 (aq-04045 q03 rev 1, difficulty Run 3, Version 790376, raw
  tasks/aq-04045/verdicts/AQ-04045_difficulty_2026-10-14_0816.txt): "Too easy", Low — · Medium 4/8, after the one
  repair (the question asked for the signed change instead of stating a rise). Same misses as Run 2 (the thrice-
  printed middle edition taken as the earliest). Four wrong in eight still failed the page's rule (two solvers
  wrong twice, one right twice), which fits the misses being spread one solver wrong twice and two solvers wrong
  once each, as in Run 2. So a single find-the-buried-edition step held the medium solver about half the time in
  two runs (3/8, 4/8) and could not open the band: on the three-solver rule one unpointed step of this kind is
  not enough, and removing a self-check moved one attempt, not the band. Hook closed after its one repair. One
  bundle.
- 2026-10-14 (aq-04045 i08, quick test, user chat "too easy for quick test", no panel): a which-company question whose
  answer is the one member of a six-company joint petition named in another document, where the section the
  question points at lists five of the six as the ones who "argued" and omits the answer; the petition's full
  membership and scope are in the order's first paragraph. The easier solver answered it. An explicit-list lure in
  the pointed section did not hold when the collective is defined in the same document's opening paragraph.
- 2026-10-14 (aq-04466 i01-i05, quick test, user chat "all too easy for quick test", no panel, routes unknown):
  fifteen submissions to one Treasury paper, only Hard open. All five first-round sketches were answered by the
  easier solver: (1) submitters holding exactly one of two positions, where one member states its position
  without the topic's usual word (Allens: "prospective only ... preserved for the life of their investment",
  no "grandfather") and one candidate drops out through a conditional sentence in a submission that argues
  the other way (AIMA opposes excluding assets but "supports a corresponding reduction" if they are); (2) the
  same six submitters asked for both positions; (3) a stated case (AIMA's $6m home, $3m loan) run through
  every submitter's own threshold and exclusion, the answer resting on one proposal taking no position on
  exclusions; (4) a list member completed only from another document (Angas: "mirror those of listed
  schemes"); (5) a count joined across two documents by day-first dates and July-June years. So on a
  positions bundle the easier solver scans every submission's matching answer, reads conditional sentences
  to their end and completes a member from a second document; hidden wording and a cross-document
  completion are not steps for it. Record: tasks/aq-04466/notes/ideas.md.
- 2026-10-14 (aq-04466 round 2 quick test, user chat "only i09 survived"; then q01 = i09, Run 1 "Too easy", Low — · Medium — ·
  High 3/3): too easy at the quick test were Aussie Angels' parental-leave rule applied to another submission's worked
  example with two incomes to infer, a monthly complaint rate that needs AFCA's first year to be eight months, and a day
  count whose day is printed only in a third submission. The survivor (a 2012-report vs 2014-paper attribution, one
  member dated only in another submission) held the easier solver and none of the strongest solver's three attempts.
  Record: tasks/aq-04466/questions/q01.md, notes/feedback-index.md.
- 2026-10-14 (aq-04466 q02 rev 0, Run 2, Version 010420, raw tasks/aq-04466/verdicts/AQ-04466_difficulty_2026-10-14_1338.txt):
  "Too easy", Low — · Medium — · High 5/6, refunded; no attempt kept its text. Shape: which submitters gave a view on every one
  of Treasury's 24 questions (two of five full responders): one member hidden by its numbering (answers 1-23, the consent pair
  inside answer 3), three look-alikes each declining one or more questions in a short line. The strongest solver did the
  coverage check five times in six; by the page's rule one high solver missed once and the other never, so the gate missed by
  one wrong attempt. Coach: the question's "24" mapped onto one member's own 1-24 numbering. Repair sent as a quick-test
  sketch: the same sentence without the number. Record: tasks/aq-04466/questions/q02.md.
- 2026-10-14 (aq-04466 q03 rev 0, Run 3, Version d07118, raw tasks/aq-04466/verdicts/AQ-04466_difficulty_2026-10-14_1457.txt):
  "Too easy", Low — · Medium — · High 3/3, refunded. Shape: the span between the earliest and latest publications of one body
  that the submissions cite (14 years), the earliest only as a lower-case file name inside a footnote's web address. The page's
  notes: "A direct search for 'CAMAC' ... returns ... the March 2000 liability paper (dated in the footnote URL)". A member buried
  in a URL is a search step for the strongest solver. After this third Too easy run in a row the page added "Your last 3 runs
  all came back Too easy. Ask the Coach before running again." Record: tasks/aq-04466/questions/q03.md.
