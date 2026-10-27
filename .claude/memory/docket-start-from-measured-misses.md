---
name: docket-start-from-measured-misses
description: "On a bundle whose bytes (or family) already have difficulty captures, design from the misses the solvers actually made before re-reading sources or writing anything up"
metadata:
  type: feedback
  updated: 2026-10-11
---

> **Frozen history (2026-10-14).** Measured mostly against the Low and Medium solvers. The current
> design rules are in [hard-playbook.md](reference/hard-playbook.md); where this note differs, the
> playbook wins. Open this note only for a specific case it records.

## Current rule

When a bundle's documents match an earlier task (same text hashes) or its family has verdict captures, the first
working step is the captures, not the documents:

1. Run `tools/verdict_summary.py` on every earlier capture and write down, per wrong attempt, the committed answer
   and the one step where it left the gold. Count only real misses; a declared trap nobody fell into is not one.
   Read that step in the attempt's own Full answer and Reasoning, at the line span the tool prints. A number that
   equals a wrong route I predicted, or the platform's one-line note, is not the route. If the tool says a
   Reasoning block was not loaded, write "route unread" and ask for a new capture; do not fill the gap.
2. Pick the miss that recurs and ask what makes it cheap to avoid in that question (a default that happens to be
   right, a single cell, a keyword hit). Redesign so the same miss decides every counted cell and the lazy default
   is wrong: ask from the complement side, or scale one entry up to the whole table.
3. Sketch only (question and short answer, screened quotes). No full write-up, prepare or hand-over before a quick
   test survives. Offer the sibling wordings together and run the one where the weak inference is active.
   This holds on a new bundle with no captures too, whenever the page shows quick tests left: the first
   hand-over is the sketch table and nothing else (aq-03950, 2026-10-13: q01 was written up in full before its
   quick test, 15 evidence rows and a hand-over, and failed the test within the hour; the two sketches that
   survived were written up afterwards and one passed at Medium on its first run).
   The survivor's sentence and short answer then go into the question file word for word. A changed sentence
   is a new sketch: send it back for a quick test, with the reason in one line, before any form. Do not change
   a tested sentence to get ahead of a form check or local warning that has not fired on it (aq-04112 q03,
   2026-10-13: the opening and the order phrase were changed at write-up, the user quick-tested the changed
   sentence and it failed; user: "why is q3 different from i06?"). `.claude/commands/docket-add.md` step 3.
4. Do not spend a round on a family the captures show the low model solves (plain rule sentences, date counts,
   label beside its rule), however many cells are added.

5. When a run's counts are in band but the gate fails ("Answer not supported") or the form blocks it, read the
   strongest solver's every-document attempts. If they share the weaker solvers' reading, the term is open: give
   it one reading and change nothing else. Do not add a cue to calculate, and do not recommend release or quote
   odds while that one-reading, no-cue wording is untested.
6. When a fair wording lands one tier low because one attempt in five clears it (Low 1/5), lengthen the step
   that places the item (an event dated after the period, the date in a footnote), not the arithmetic and not
   the answer form.
7. When the misses are a base or list read off a complete-looking table while one member sits only in prose,
   do not tune a cue word: none, "every", "wherever" and "only in text" each gave a different wrong
   result. Name the universe the member sits in ("whose ... total appears in <the notice>") before the
   first run, screen that wording in the form's Checks, and do not call the hook finished or tell the user
   a next miss will end it while that wording is untested. Removing a cue is not naming the scope: when a
   completeness word comes out ("anywhere", "wherever"), the scope it carried goes back in as the name of
   the document or section set (aq-03169: cue Between levels, scope dropped not supported, scope named
   Hard). The platform's "What to change" wording is an explanation of one run, not a tested design:
   check it against this list before using it. `check_questions.py` WARNs `cue` on those two words.

8. A gold must not depend on an item the documents only report and do not include (an earlier letter named in a
   footnote, a table cited but not reproduced) when the question names a set of such items. The solvers are told to
   answer "using the input documents provided above", and the strongest solver reads the set as the items provided
   (aq-03570 q01 rev 1: 0 of 3 every-document attempts counted the reported letter, "Answer not supported"). Either
   ask for the reported item itself, or choose a quantity that is the same with and without it.

9. Before the first run of a posed case run through stated rules, do the audit that step 4 asks for after a
   run: list the steps, mark each one a word in the question points at, and count the rest. The family
   captures already said pointed steps are cleared; a design with one unpointed step is an Easy design,
   however many pointed steps surround it. Look for the second unpointed step in a different passage before
   writing up, and say in the hand-over how many unpointed steps the design has.

10. When sibling wordings of one hook go to the quick test together and the survivor needs the same steps as
    the ones that failed, the survival is noise from one screen, not a harder form. Quick-test the survivor a
    second time before writing it up or spending a difficulty run, and say so in the hand-over. Step 3's "run
    the one where the weak inference is active" applies only when the survivor has a step the failed siblings
    lack (aq-04045 q02: two share forms too easy, the dollar form survived, then Too easy at Low 5/5).

11. In the step audit of rule 9, a step is pointed at when a lookup of any word in the question reaches it,
    however many paragraphs the lookup crosses. A premise that names a body's advice, a status or a condition
    points at the rule that advice triggers and at the rule's figure; the easier solver walked such a chain
    five times in five (aq-04112 q02: "Had the ... Committee's advice on butchers been accepted" led every
    attempt to the list and its 20% rule). A counterfactual or scoping clause is also read as the instruction
    for the method, so a clause that settles the one unnamed step ("one company" beside a per-company fee)
    leaves no unpointed step. Take such words out before the first run when the sentence keeps one reading
    without them, and do not count a chain behind a named premise as unpointed.

12. "Between levels" with the medium solver near zero and the strongest solver right every time is the
    hook's position, not a near miss: one medium attempt in seven is not a solver that "gets it right twice".
    Do not send an equivalent wording to a second run (aq-03993 q01: Medium 1/7 then 0/6, High 3/3 both
    times). Either change the dependency so that solvers scan the documents by default (a total or a list
    over witnesses or parties; see step 13 for which), or put the one more explicit wording to a free quick
    test first; if neither exists, leave the hook. A single unprompted look in a second document, where the
    first document's figures already give a complete-looking answer, held everything below the strongest
    solver and nothing at it.

13. When a hook is a set with one member that only a passage in a second document shows, check before the
    first sketch whether the members carry a count or an amount, and whether one document prints a figure
    for the visible members that looks complete. If both hold, sketch the total first and take the list
    form to the quick test only beside it. A list gives the solver a row for every candidate and so an empty
    row to notice; a total against a printed figure gives none (aq-03993 q02: as a list Medium 4/7, "Between
    levels"; as a total over the same member Medium 2/6, in band; aq-03557 q01 before it). A list result on
    a sibling bundle is not a reason to skip this: on aq-03950 q02 the member sat in another witness's
    answer and the list measured Medium, while here it sat in the witness's own answer, where a per-witness
    scan reaches it. Under the three-solver medium gate, write in the sketch what the form does to each
    solver, not to a pooled rate: the gate passes only when one solver finds the step twice and two miss it
    twice. Look-alike decoys do not move that split (every recorded medium attempt set all of them aside in
    both aq-03993 runs), so do not count them as a step.

**Why:** user, 2026-10-11 (aq-02749), after q02 passed at Medium: "Check the verdict and improve your performance."
On that task I re-read every State procedure section and fully wrote up a four-cell rule scenario first; it was
quick-test too easy, as two-cell rule cases already had been on the same bytes. The pass came in round 2 from the
earlier captures: aq-02626 q04's only low misses were on Wyoming's grouped item (2 of 5, one list entry). Asking the
whole State-by-amendment matrix from the "lacking" side made that miss fatal in every entry: Low 0/5, Medium 3/5.
The evidence was on disk before I opened a document.

**How to apply:** at intake, after the hash check, list earlier captures for the same bytes in hooks.md with each
wrong attempt's route, before any re-read. For a new bundle with no captures, apply step 2's question to the family's
captures in [[docket-local-solver-calibration]]. After any difficulty run, add the routes to the bundle's
feedback note the same way, so the next task on those bytes starts from them. My reading, not the user's words: the
user's instruction was the one sentence quoted above; the four steps are how I am applying it.

## Evidence and history

- 2026-10-13, aq-04112 q02 rev 0 (user: "plz check arrived verdicts by using your feedback skill and fix"): a new
  bundle (committee report plus two hearing transcripts). Five sketches went out first, sketch only; the user
  reported "i02, i01 survived. others not tested". My step audit for i02 said the chain from a named advisory
  body's advice to a 20% rule ran "through two paragraphs the question does not name" and I put it first in
  the order. Run 1: "Too easy", Low 4/5, run returned. All five low attempts walked the chain; the one miss was a
  reading of the question's own phrase. Rule 11 is the correction. Applied the same day to the other survivor
  before its first run: q01 rev 1 drops "one company", the words that pointed at its only unnamed step. Two
  untested sketches were withdrawn on the delete-and-guess test (a published headline allocation; a scheme the
  report hints at). Interpretation mine; the user's words are the quoted request. Routes:
  tasks/aq-04112/questions/q02.md.
- 2026-10-13, aq-04045 q02 rev 0 (user: "plz check arrived verdicts by using your feedback skill and fix"): a new
  bundle, no earlier capture. Three wordings of one fee hook went to the quick test; the user reported "1, 3 too
  easy, 2 survived". I wrote the survivor up and handed it over for the Checks and a difficulty run, telling the
  user the survival was "a screen only" but not asking for a second quick test. Run 1: "Too easy", Low 5/5 (2 not
  scored). Every scored attempt did the whole chain, as the two failed siblings had already shown the easier
  solver could. The platform returned the run ("Too easy, so you got an extra run"), so the cost was the round
  trip. My hypothesis before any test (a carve-out the question does not point at would hold the easier solver)
  was wrong on all three forms. Step 10 is the check that would have saved the run. Interpretation mine; the
  user's words are the quoted request. Routes: tasks/aq-04045/questions/q02.md.
- 2026-10-13, aq-03993 q01 rev 0 (user: "plz check arrived verdicts by using your feedback skill and fix"; new
  bundle, committee report plus three hearing transcripts): an average grant whose grant total only a witness
  separates from the report's headline fund (report: £2 million, 20 projects; witness in another document:
  "about £1 million was grant funding"), asked with nothing named, paired with a count. Run 1 "Between
  levels", Low 0/5 · Medium 1/7 · High 3/3 ("Too hard for the medium model but too easy for the high
  model"). From the traces: every low attempt wondered whether the whole fund was paid out and assumed it;
  none opened the witness's document. Of the three medium solvers (told apart by their wording) two never
  left the report and the third found the sentence once in three tries; the gate wanted it twice. Scope of
  what this shows: a single unprompted look in a second document holds the easier solver and two of the
  three medium solvers, and the result then turns on one solver's three tries. A phrase that names the
  evidence or the split would reach all three medium solvers, and the three-solver gate needs two of them
  wrong twice, so the page's "pin the basis" wording was not taken. Rev 1 kept the trap and dropped the
  paired count (every attempt got it, the closed-book one from memory). Run 2 on rev 1, same day (user,
  again: "plz check arrived verdicts by using your feedback skill and fix"): "Between levels", Low 0/5 ·
  Medium 0/6 · High 3/3; no recorded attempt opened the second document. Over the two runs: easier solver
  0 of 10, medium 1 of 13, strongest 6 of 6. What I got wrong: rev 1 changed the wording and left the
  dependency as it was, so the second run measured the same thing; I had told the user it "sits where Run 1
  measured" and sent it to a run anyway. Mine, not the user's words: on this gate, work out what a wording
  does to each medium solver, not to their pooled rate, and see step 12.
  Third run, same day, on a new hook (q02 rev 0, written up after its quick test survived): which witnesses
  worked for an organisation with local democracy reporters on its own staff (three names, each resting on
  the witness's own words, among eight look-alikes). "Between levels" on the other side: Low 0/5 · Medium
  4/7, "Too hard for the low model but too easy for the medium model". Every wrong attempt left out the
  one member whose only evidence is a clause in his own answer; every recorded medium attempt set aside
  all eight look-alikes, and two low attempts added one. So decoys of the mentions-versus-does kind were a
  cleared family at the medium level here, and a member stated in the witness's own testimony is found by
  a per-witness scan (two of the three medium solvers); on aq-03950 q02 the member sat in another
  witness's answer and measured Medium. Two errors of mine the capture showed: I had ticked the transcript
  with a witness's own statement although the report's witness list and allocation sentence gave the same
  member with that transcript deleted (the run stopped before the document check), and I had declared the
  look-alike mode instead of the omission, the answer the easiest reading gives. Rev 1 asks for the total
  the hidden member changes (recipe 8's form): the report prints 75 reporters for the one listed publisher
  that sent a witness, and the hidden member adds 2.
  Fourth run, same day, rev 1 (user: "Successfully submitted as a medium tier. plz check arrived verdicts
  by using your feedback skill and improve your performance."): "In band — Medium tier", Low — · Medium
  2/6, both documents "Needed ✓", closed-book "About 30". Both recorded wrong answers were 75 and neither
  attempt found the clause (one wrote "no evidence of LDRs, likely 0" after weighing and correctly
  excluding two look-alikes); both right attempts quoted it; two wrong attempts have no text. Grouped by
  opening words and order, each run shows three pairs: on the list one wrong twice, one right twice of
  three, and a textless pair right twice; on the total one right twice, one wrong twice, and a textless
  pair wrong twice. The opening words differ between the runs, so no solver can be followed from one form
  to the other. The strongest solver's every-document attempt first concluded that the publisher's figure
  was the whole answer and found the clause on a later pass. The page's line for one miss said it
  "treated ... two LDR posts ... as irrelevant or already included"; the trace shows it never found them.
  Scope: one run per form, one bundle, and the pair whose result differs is the one whose text the page
  does not keep, so the direction is observed and the size of the list-to-total shift is not. What I
  got wrong: both inputs of the total were in my notes when I sketched the list, and the workspace's
  first instruction on shape is one number derived across documents; I reached for the list because its
  form had just measured Medium on the sibling bundle, and spent a run finding out it did not carry over.
  Step 13 is the check. Mine, not the user's words. Routes: tasks/aq-03993/notes/feedback-q02.md.

- 2026-10-13, aq-03736 q01 rev 0 (user: "easy tier. but slots full for easy. plz check arrived verdicts by
  using your feedback skill and upgrade"): a new bundle, no earlier capture. I handed over a six-step dated
  case and told the user it was the lead because it was "the only design here with several independent rule
  steps". Run 1: "In band — Easy tier", Low 1/5. All five low attempts cleared the five steps the question's
  own facts point at, including the two-threshold trap I had declared as a failure mode (it caught nobody).
  The one step nothing pointed at, an exception closing the phase-in sentence, held four of five. The family
  notes already said a stated case whose deciding rules the question's conditions name is no trap (aq-02626,
  aq-03143); I counted steps instead of counting unpointed steps. Step 9 is the check that would have told me
  before the run that the design had one holding step. I did not repair: the only second step I found sits
  in the same sentence as the one that held (a turnover that changes between the groups' reference years),
  and aq-03143 shows what that does. Interpretation mine; the user's words are the quoted request. Routes
  and the re-picked failure mode: tasks/aq-03736/questions/q01.md.
- 2026-10-12, aq-03570 q01 rev 0 (same bytes as aq-01431; user: "plz check arrived verdicts by using your feedback
  skill and fix"): a mean gap between one commenter's letters, opened with the clause "Counting co-signed letters",
  measured Between levels, Low 0/5 · Medium 5/5. I had designed from aq-03170's miss (trust in a commenter's own
  account) and predicted the co-signed letter as the gate. The traces show the opposite low miss: four of five low
  attempts found the co-signature and dropped the one letter that is stated in a footnote but is not itself a
  document; none of them trusted or even weighed the own account. Every medium attempt first called the coalition
  letter "not solely from" the commenter and counted it because the clause said to. Two things to carry: a miss
  measured on a sister bundle is a hypothesis for this one, so name in the hand-over which gate is expected to
  hold which solver and check it against the first capture; and a clause that says what to count is a cue, so
  name the set by its membership test before the first run (WORKFLOW section 6, repair order 5). Two of the page's
  "How it got there" lines said attempts missed the co-signers when their Full answers listed that letter. Rev 1
  (set named as letters the commenter "signed", no clause) measured "Answer not supported" on 2026-10-12 (Run 2,
  Low 0/5 · Medium 2/4, all three every-document attempts on 266). Without the clause no low attempt found the
  co-signature (0 of 5) and every medium and every-document attempt did (7 of 7): the clause had been worth four
  low attempts in five. The gold then failed on something else: it counted a letter the documents report in a
  footnote but do not include, and the strongest solver left it out all three times, once quoting its own
  instruction "using the input documents provided above" (one low and one medium attempt quoted it too). I had
  weighed that reading of "signed" before the run and written "no second reading". With the letter settled either
  way nothing divided the middle solver, so q01 was dropped after two runs and another hook (q02) written up.
  q02 rev 0 on the same bundle then named the identifier that decides its set ("the three proposals under whose file
  numbers it was filed") and was quick-test too easy (user report, 2026-10-13, no panel): pointed at the identifier,
  the easier solver did the mapping and the elimination. I had chosen the explicit wording because the run before had
  ended "Answer not supported"; the least explicit one-reading wording should have gone to the quick test first.
  Rev 1 then named nothing ("the three proposals it covered") and the form blocked it: both form solvers took the three
  proposals a commenter names in the sentence before its citation (91.7 against 84.3). So on an identifier-against-
  narrative hook the two ends are "identifier named = too easy" and "nothing named = blocked"; rev 2 names the evidence
  instead ("Judging by all these letters together") and was quick-test too easy (user report, 2026-10-13). That
  opening measured Hard on aq-03170, where the deciding letter sat in another commenter's text; here the deciding file
  numbers sit in the same citation as the lure, so any wording that gets the form's solvers to them gets the easier
  solver there too. Hook closed after three wordings; the old US SIF hook became q03.
  q03 (US SIF grouped figure against its split) then measured "Between levels" on the other side: Low 0/5 · Medium
  0/6 · High 5/6 with the label "climate change", where aq-01431 had Low 0/5 · Medium 4/5 with the exact label
  "climate change/carbon". One token moved the medium solver from four in five to none in six. Eight of nine
  recorded wrong attempts never opened the second letter; the ninth read it and set the split aside as a reading
  of the label. The page's "What to change" proposed the exact label, the wording already measured too easy. Rev 1
  names the scope instead ("figures ... by issue"); result pending. The page now prints its gate: medium is three
  solvers with up to three tries each, ready when at least two are wrong twice and one is right twice; high is
  two solvers, ready when both are wrong at least once and not every attempt is wrong. So a Medium result needs
  one medium solver that gets it reliably, not a share of all attempts.
  Rev 1 (short label, scope named "by issue") did not reach a run: the form's "One defensible answer" failed it with
  "Two materially different answers are defensible", although rev 0 with the same label had passed that check and
  run. So that check's verdict on one label is not stable from one wording to the next, and a run on a label the
  page later calls open should not be read as a difficulty result. Rev 2 gives the term one reading without the
  report's own label ("as a stand-alone issue"); result pending.
  Run 4 on rev 2 did not measure it: "Answerable without the documents" (closed-book 3.41 - 1.76 = 1.65), so the
  wording's difficulty is still unknown. Rev 3 keeps the wording and asks the gap as a percentage (91.7%).
  Rev 3 was quick-test too easy (user, 2026-10-13). So Run 3's Medium 0/6 · High 5/6 on the short label measured
  the open term, not a step: when the page adds "This question may be too vague" to a between-levels result, give
  the term one reading and quick-test that wording before treating the counts as the hook's difficulty.
  q04 (two named organisations, the last two letters each signed): three quick-test survivals, then Run 5 "Too
  easy", Low — · Medium 5/6. The check started at the Medium level, the question file's own audit had counted no
  step the question does not point at, and Runs 1 and 2 had shown the medium solver clearing a co-signature and
  an in-hand multi-proposal letter. A quick test screens the easier solver only: when Easy is closed it cannot
  outweigh a zero count or the same page's captures on the same kind of step.
  q05 (signers of a joint letter that commented, two shown only in other commenters' letters, opening "Judging
  by all these letters together"): Run 6 "Too easy", Medium 5/9, one attempt short of the band; two right
  attempts quote the opening as their reason to take cited commenters in. Repair sketch: the cue out, the scope
  kept ("do these letters show"). Rev 1: Run 8 "Too easy", High 3/3 (only the High level ran), after a Run 7
  the page also called too easy. On this bundle the medium and high solvers sweep every listed name through all
  twelve letters, so a hidden member in a footnote or body sentence is not a step for them; the only medium
  splits came from an open term or a letter the set merely reports. Bundle released on that record.

- 2026-10-13, aq-03169 q02 (user: "plz check arrived verdicts by using your feedback skill and fix", three
  captures in a row): step 7 was on file and I did not apply it. Run 3 on "say anywhere in its response" was
  Between levels (Low 0/5 · Medium 4/5). I read the cue correctly and then removed the scope altogether, taking
  the platform's "What to change" wording, although I had weighed the structural form ("Grant Thornton's
  response") and set it aside as equivalent. Run 4 on the bare wording: "Answer not supported", the high model 0
  of 3 with every document, all three inside the annex table. Check to run before any scope repair goes to a
  difficulty run: if one member sits outside a complete-looking table, the repaired question must still name
  the document or section set the members are drawn from; the platform's suggested wording is an explanation,
  not a tested design. Interpretation mine; the user's words are the quoted request.
  Outcome, same day: rev 4, "does Grant Thornton's response say", Run 5 "In band — Hard tier" (Low 0/5 ·
  Medium 1/7 · High 3/6), submitted; user: "submitted as Hard tier. please check the arrived verdicts by
  using your feedback skill and improve your performance". Also mine: on revs 3 and 4 I told the user the
  next miss would end the hook, which step 7 forbids while the named-scope wording is untested; and I had
  not opened the matching note in full before the repair because its index line read as being about
  derived golds. Open every note whose index line names the failure (gate failed, Between levels, list
  with a member outside a table) before choosing a repair.
- 2026-10-12, aq-02933 q04 (user after the Medium pass: "find out what you missed and upgrade your
  performance"): one hook took six versions, four difficulty runs and two form blocks. Recipe 4 in
  [[docket-local-solver-calibration]] (aq-02673: no scope phrase Too hard, a clause naming the item too
  easy, a phrase naming the kind of thing that counts Medium) was on file and described revs 1 and 2
  before I ran them. After rev 2 I wrote "no Medium point" into memory and recommended release; the user
  quick-tested a wording I had listed as untried and it survived. I then tuned cue words ("Wherever"
  Medium 4/5, "every" form block) and only on rev 5 named the base by its document, which passed (Low
  0/5, Medium 1/5). Three times I told the user the next miss would end the hook. Step 7 is the order that
  would have reached the pass in one or two runs. Interpretation mine; the user's words are the quoted
  request. Routes: tasks/aq-02933/notes/feedback-q04.md.
- 2026-10-12, aq-03120 (user after the Medium pass: "plz check arrived verdicts by using your feedback skill and
  upgrade your skill"): one hook took seven versions, three difficulty runs, two form blocks and three failed
  quick tests. Run 1 (Easy, Low 1/5) already showed the holding step (four low attempts gave the printed
  half-year figure, three after placing the period correctly). My next three versions changed the wrong things:
  a dating event carrying the decoy's label (blocked twice) and a percentage form (too easy). After Run 2 (counts
  in band, gate failed) I added "stated or implied" (too easy) before trying the one-reading term that passed.
  Steps 5 and 6 are the order that would have reached the pass in two runs. Interpretation mine; the user's
  words are the quoted request.
- 2026-10-12, aq-02749 q02 (user: "plz check arrived verdicts, find out what you missed and improve your
  performance", with a second capture of the same run, every Reasoning block loaded): my first read-out had named
  the two medium misses from their numbers. 6 was not 17 - 11 but Alabama's list mapped to the wrong members; 9 was
  not a miscount but Alabama's 17 entries taken as all 20. Both blocks were already loaded in the first capture. I
  had also reduced the low failure to Wyoming, when all five attempts failed on Wisconsin's shorter list as well,
  and told the user a declared mode caught nobody when its mechanism caught both medium misses. The wrong routes
  had gone into memory and the report. Fix: step 1's last three sentences; verdict_summary.py prints spans, an
  unloaded-reasoning warning and a bare-answer note.

- 2026-10-11, aq-02749: round 1 (q01 full write-up, i02) both quick-test too easy; round 2 (i03, i04 sketches) both
  survived; q02 = i04 "In band — Medium tier", submitted. Sixteen earlier designs on these bytes (aq-02483, aq-02626)
  were Easy or too easy; none had been built from the Wyoming miss.
- 2026-10-12, aq-03143: step 4 not applied, and it cost a run. Run 1 on q01 rev 0 (Easy, Low 2/5) showed all five
  low attempts clearing the stated escape rule and every miss sitting in one table-against-rule cell. I named that
  correctly and then repaired by adding two more stated-rule cells (commencement, scope), the family the capture
  had just shown solved. Run 2 on rev 1: Too easy, Low 5/5, and the one cell that had split the solvers split none.
  Check to run before any repair goes to a difficulty run: list the gates the repaired question adds; if each is a
  rule the documents state in a sentence and the question's own words point at (a date, a category, a status),
  it is the solved family and the repair is not worth the run. Also check that an added item does not draw on the
  same table row or passage as the gate that worked, since it can show the solver the row's structure.
