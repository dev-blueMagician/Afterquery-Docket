---
name: docket-form-vague-block
description: "The task form blocks Submit as \"too vague\" when both of its solvers take a printed figure the question's words also fit; four blocks by 2026-10-08, each a built gold beside a printed same-label decoy, plus one red \"does not give this answer\" message on the same design; state the separating condition in the question, and do not expect local matches to predict the block."
metadata:
  type: project
  updated: 2026-10-09
---

## Current rule

Two wording faults produced this block, and the difficulty gate's "Answer not supported", on one hook
(aq-03120, 2026-10-12), and both are checkable before any test. First, a period or population term in the
question that a document also prints as a label for a different item ("financial half-year" beside
"half-year results"): strong solvers take the labelled item. Second, a dating event whose own name carries
the decoy period's label ("the half in which it announced its first-half results"): both form solvers took
the first half. Search the bundle for every such phrase before a sketch is tested; `docket_agent.py screen`
warns on the common period words. The repair is a structural description with one reading ("the half of its
financial year that last ended before ..."), never a cue to calculate: a percentage form and "stated or
implied" each made the same question quick-test too easy, and the one-reading wording with no cue passed
at Medium.

A ninth block, of a different kind (aq-03170 q01 rev 1, 2026-10-12): a three-name list in which one member is
shown only by another document (a commenter's second letter, quoted in a different commenter's letter). Both form
solvers returned the two members that each sender's own letter states, and the check blocked with the usual words.
No printed decoy was involved: a member that needs a second document, with no counting rule in the question, is
enough. State the rule in the question before the first paste ("including letters only others mention", rev 2:
the check then passed, and the difficulty run was Medium, Low 0/5 · Medium 1/5; rev 4 named only the evidence,
"Judging by all these letters together", passed the check as well and measured Hard, so the check needs the
reading closed, not the member pointed at), as for aq-02673 q04 and aq-02933 q04. The solvers' reasoning is not shown by this check, so do not
name their route beyond the answers quoted.

The form's blocking "One defensible answer" check runs two solvers on the question and documents.
If both give the same non-gold answer, Submit is blocked: "This question is too vague to submit:
two independent solvers, working from the documents alone, did not reach your gold ... Both
answered ...". The platform scores that agreement as a second defensible answer, not as a trap
that worked. It runs before any difficulty run, so a block costs no run but needs a new revision.

In all four recorded blocks the gold was a figure no document prints, built from other figures,
and both form solvers instead took a figure the documents do print for the same label and, on a
loose reading, the same window or population. The condition separating gold from decoy was absent
from the question's words, or was one soft word the decoy's own context did not visibly break; it
lived only in the documents (an N column, a release date, "combined", rounding). Each orange
"N matches ... Narrow the description" advisory listed the decoy's source among its matches.
Read those advisories by what they list: a match on a competing figure (another scope, window or
grouping) is the warning sign; matches that are only repeat mentions of the one intended source, or
that source plus its own figure, are noise and need no rewording.

A second red message under the Question box, without solver answers, has the same design behind it
(one case, aq-01543 q01): "Working the question from the documents does not give this answer. Check
which figure, period and entity the question asks for, and that each value comes from the right row
and column." Treat it as this check until a result separates them, and apply the same fix.

So a printed figure that the question's words fit on a loose reading is a second answer unless
the question states a condition it fails. Put the separating condition in the question (a named
population, a timing state such as "then in force", an exact label), and let the documents be
needed to see that the decoy fails it (its N, its release date, its "combined" scope). The trap
then still catches careless readers, and gate Q15 ("none the wording already rules out") holds,
because the wording alone does not show which figure fails.

Local fresh Opus solvers are no guide to this check: they matched the gold, naming and rejecting
the decoy, on all three blocked wordings they saw, and the two reviews that estimated the block
put it at 5-10% and 10-15%. When a write-up's main trap is a printed figure that fits the
question's words, treat the block as likely, not as a tail risk.

**Why:** four questions were blocked before any difficulty run. Guide rule 4: "If two readings of
the question lead to two defensible answers, tighten the wording." The newer guide lists "a
description that fits more than one thing" among common send-back reasons, and the form's
"Answer matches a stated figure" advisory expects a stated figure for the asked quantity to be the
answer unless "the question says how to work it out instead".

**How to apply:** at sketch and review time, list every printed figure that the question's words
fit on a loose reading (same label, same window or population) and check that a condition stated
in the question, not only one the documents reveal, excludes each. If none does, tighten the
wording before hand-over, or hand over a short ladder of wordings, weakest first, for the user to
screen in the form's free check; then file the one that clears as a new revision and run the full
checks on it. Expect the fix to cost difficulty: aq-01321 q02 cleared once narrowed and then
reached only Easy, and aq-01543 q01 cleared with "calendar year" and came back Too easy. When the
decoy's failure shows in its own sentence (a printed window or scope), the stated condition gives the
trap away; look instead for a decoy whose failure needs another passage (a table's statuses, an event
date printed elsewhere). A "Scatter the pieces" total is the same case: when one source prints a complete-looking
total for its own part (one proposal's per-applicant savings), the question must say the parts are combined ("all of
... proposals"); otherwise that part is a second answer (aq-02405 q01, 2026-10-09). An amendments-in-order question needs the later
document to state which text it amends; matching words alone left "cannot be determined" defensible (aq-02405 q02).
Stating the condition is not always enough: when the passage that defeats the decoy is terse (an amendatory instruction),
both form solvers can still take the decoy, and any wording strong enough to steer them also gives the trap away
(aq-02405 q02 rev 1). Treat that design as unlikely to clear the form and retire it after one repair. See [[docket-one-clear-answer-precision]],
[[docket-local-solver-calibration]] and the form check list in reference/platform-quality-checks.md.
A negative membership condition ("States it does not name for X") is a second-answer risk when the other document
discusses one candidate at length for a different reason: the form would not accept that the candidate is "not named"
(aq-02933 q04 rev 0, California and Los Angeles County's HHA growth), and that candidate held most of the total. Build
match-then-exclude questions on the list's positive members (the named items' share or total), or put the doubtful
candidate out of scope in the question; keep "does not name" for candidates the other document never mentions at all.

## Evidence and history

- 2026-10-12 (aq-03120 q01 rev 1, user screenshot tasks/aq-03120/notes/platform-feedback/checks-rev1-2026-10-12.png;
  the failed check quotes rev 1's question): "One defensible answer" Failed with a critique, no solver answers shown
  in the visible text: the check places the question's dating event correctly ("announced in February 2023, which
  falls in the second half") and then objects that "The documents give first-half growth ($0.6b) and full-year
  growth ($1.1b), but do not explicitly state the second-half growth figure, leaving" (cut off). Beside it the
  advisory "Answer matches a stated figure" warned twice: "Doc 3 states $1.1 billion; your answer has $0.5
  billion. Use it, or say in the question to compute it from the other figures." So the block can fall on a gold
  that is one period subtracted from another even when the period is pinned and understood: the question asked for a
  dollar growth figure, two figures with that label are printed, and the wording did not call for a calculation. Rev 0
  of the same hook (another dating event, same subtraction) had been run for difficulty without its Checks being
  seen, so a difficulty result does not show this check passed. Rev 2 kept the same dating event (the bank's own
  first-half results announcement, dated in the second half) and asked for a percentage of the year's growth "On
  [the bank]'s reported figures" (screenshot checks-rev2-2026-10-12.png): "Answer matches a stated figure" Passed,
  and "One defensible answer" Failed again, this time with solver answers: "did not reach your gold \"45%\". Both
  answered \"55%\"." Both solvers used the first half. Two things follow. The percentage form clears the
  stated-figure advisory, since a calculation is needed whichever period is picked. And an event whose own label
  names the other period ("first-half results", announced in the second half) draws both form solvers to that
  other period, which the platform scores as a second defensible answer, not as a trap that worked: do not use a
  dating event that carries the decoy period's name. Rev 3 went back to a plainly dated outside event (result
  pending). My reading: look at the Checks panel before spending a difficulty run on any derived gold.
- 2026-10-12 (aq-02933 q04 rev 4, user screenshots tasks/aq-02933/notes/platform-feedback/
  q04-r4-checks-2026-10-12-list.png and -question.png; the Question box shows rev 4 word for word): "One
  defensible answer" Failed, "Both answered "83.57%"" against the gold 67.45%. The list's fifth member is
  given only in prose outside the table (Georgia). "Across every State with a 2019 hospice total from CMS"
  did not clear; the neighbouring "Wherever CMS gives a State's 2019 hospice total" (rev 3) had cleared and
  measured Low 0/5, Medium 4/5. So a completeness word ("every") is not a stated counting rule for this
  check; a word about where the members may sit was. A wording softened after a Between-levels result should
  be screened here before a difficulty run. Rev 5 named the scope ("whose 2019 hospice total
  appears in CMS's hospice notice"), ran and was submitted at Medium (Low 0/5, Medium 1/5), so the block did
  not recur (its Checks panel was not captured); the difficulty page still showed "may be too vague" beside
  "You can submit now". For a member outside a complete-looking table the repair for this block is the
  structural scope, not a stronger or weaker cue word. The solvers' reasoning is not shown by this check.
- 2026-10-11 (aq-02933 q04 rev 0, user screenshot tasks/aq-02933/notes/platform-feedback/q04-r0-checks-2026-10-11.png,
  transcript beside it; no version id visible): "One defensible answer" Failed with a critique of the reasoning, no
  solver answers: "the reasoning excludes California from the HHA co-location States by arguing Doc 6 only mentions Los
  Angeles County in a different context, but Doc 6 does discuss California in the context of HHA enrollment increases.
  The exclusion of California is not clearly supported by the documents". The question summed 2019 hospice totals in
  States CMS "does not name for home health agencies sharing an address" (gold 1,503 = Arizona 152 + California 1,130 +
  Georgia 221; 373 if California counts as named). Doc 6's shared-address passage lists five States without California,
  so the gold followed the text; the block came from asking for a negative about the one State the document discusses
  most. Same capture, advisories: "No single passage" ("Doc 5 on its own may give enough to compute the answer": every
  number was in Doc 5, Doc 6 only filtered), "Answer matches a stated figure" (a sum of printed rows; "say in the
  question to compute it"), "Each description fits one thing" (listed four table States for "2019 hospice totals", not
  the fifth, which the document gives in prose, and listed the named States for the "does not name" description). Rev 1
  leaves California out in the question and asks the named States' share (67.45%); form result pending.

- 2026-10-10 (aq-02743 q02 rev 0, user screenshot tasks/aq-02743/verdicts/AQ-02743_q02-r0_form-checks_2026-10-10.png,
  transcript beside it): a block with no solver answers quoted. "One defensible answer" Failed: "The reference answer
  of 354 days depends on the assumption that the DOJ compliance date of April 26, 2027 governs over the HHS date of
  May 11, 2027. The documents do not establish that the earlier DOJ date is the one the county must 'first meet';
  both rules apply to overlapping entities, and the documents do not resolve which date is controlling." The question
  asked how many days after one agency's rule took effect a body bound by two agencies' rules "must ... first meet"
  the standard; the gold took the earlier of the two dates, a step no document states. Same page, advisories: "No
  single passage gives the answer: Doc 4 on its own may give enough" (the one-rule reading) and "Answer matches a
  stated figure: Doc 4 states 11; your answer has 354" (day numbers of quoted dates against a computed day count).
  The wording had survived a quick test first. Lessons: the check treats an unstated combining rule (the earlier of
  two rules' deadlines) as an assumption even when ordinary logic forces it, so put it in the question ("does any
  federal rule first require it"); and a quick-test survival on such wording may be the easier solver taking the
  one-rule reading (author's inference, no trace seen). A sibling wording with the condition stated ("before any
  federal rule required it", q03 rev 0) then went through a difficulty run whose page said "You can submit now.";
  its Checks list was not captured. It measured Easy, Low 3/5: the stated condition left a clean route, as this
  note's rule expects (see [[docket-local-solver-calibration]], 2026-10-11).

- 2026-10-09 (aq-02405 q02 rev 0, user screenshot tasks/aq-02405/runs/q02-r0-form-2026-10-09/): "One defensible answer"
  Failed: two solvers "did not reach your [gold] ... and "cannot be determined"". The question asked where 27 CFR
  478.96's seven-day delay would sit once two proposals were "all finalized as written" (gold (d)(4): Doc 5 rewrites the
  whole section, Doc 4 re-letters (c) and (d)). Doc 4 never says its 478.96 instructions amend Doc 5's version; only the
  quoted words match, so the order of the two proposals was an inference. Rev 1 moved to 478.124(c)(5), where Doc 4's
  footnote 37 names Doc 5's rewritten text as the base. Rev 1 was blocked too: "Both answered "27 CFR
  478.124(c)(5)(iii)"", Doc 5's printed position (the trap), with the advisory "This passage in Doc 5 may answer the
  question on its own." Hook retired after the one repair.
- 2026-10-09 (aq-02405 q01 rev 0, user screenshot of the full Checks; tasks/aq-02405/runs/q01-r0-form-2026-10-09/):
  "One defensible answer" Failed: "This question is too vague to submit: two independent solvers, working from the
  documents alone, did not reach your gold "$48.05"." The visible text named no solver answers. Gold = two 2026
  proposals' per-application savings for one paper Form 1 filer revalued at $26.10 (Doc 6 $18 + $17 + 0.25 h, Doc 3
  0.25 h); the question said only "Recomputing ATF's 2026 savings estimates", and Doc 6 prints its own "combined
  (rounded) savings of $42" for exactly that filer. The same capture's advisory "No single passage gives the answer:
  Doc 6 on its own may give enough to compute the answer" points to the one-proposal reading. Rev 1 states "all of
  ATF's 2026 proposals' savings"; its form result is pending. The same capture failed "Question in your own words" (the
  question was Claude-written; the user rewords) and could not run "Needs the documents" (retry).
- 2026-10-09 (aq-02157 q04 Runs 1-3): the difficulty page's own advisory "This question may be too vague: several
  solvers agreed on an answer that is not your gold ... Tighten the question so only one answer fits, or check the
  gold." appeared on all three runs, including Run 3's pass ("In band — Medium tier", "You can submit now."). There it
  listed only trap answers (£0.5, the IA's average-pack duty; £0.6, the consultation's figure as the start), not a
  second reading, and it did not block. On Runs 1-2 the agreed answer was the literal answer to the user's paraphrase:
  read the solvers' quoted question before treating the advisory as ambiguity in the saved wording.
- 2026-10-06, aq-01321 q02 (the user's rewording, never run locally): gold 20.26%; both form
  solvers answered 20.05% from the same-window prose "$3.9 billion in R&D and SG&A"; the advisory
  listed "R&D and SG&A (Doc 9, prose)". Narrowed to the income-statement lines, it cleared the form
  and passed at the Easy tier (user report).
- 2026-10-06, aq-01428 q01 rev 1: gold about €1.3 billion; both answered €1.40 billion, the raised
  guidance printed in the release that reports the event, under the anchor "In the month ..., how
  much ... was its guidance expecting" (the form box also held a stray precision sentence); orange:
  "Doc 1 states €1.4 ... Use it, or say in the question to compute it from the other figures."
  Local solvers A and B matched with high confidence. Rev 2 ("the guidance then in force") was handed
  over; no form result recorded.
- 2026-10-06, aq-01431 old q01 rev 1 (question removed in the 2026-10-08 rebuild; record in commit
  30c3f7e): gold $1.65 trillion; both answered 3.00 trillion dollars from Doc 7's grouped "$4.8
  trillion" once the exact label was dropped ("largest single ESG issue"); the advisory listed
  $4.8T, $1.8T and $1.7T (Doc 7, prose). A and B matched and rejected 3.00 ("conflicts with
  'single'"); review block risk 5-10%. Rev 0, with the exact label, had cleared the form; its
  difficulty run was "Between levels" (low model 4/5 on 3.00).
- 2026-10-08, aq-01650 q01 rev 0: gold 9.2 percentage points; both answered 13.7 from Doc 5's Table
  2 "Financial literacy" mean 15.2 ("Descriptive statistics for complete cases", N 15,228) instead
  of the weighted Table 5 means over all 23,788 non-students. The paper calls the 15,228 "the final
  usable number of complete cases", and the question's coined "non-student respondents" (no
  document uses the word) fits both samples. Orange: "average share of questions answered correctly
  — 2 matches: 1.414 (Doc 2, prose), 15.2 (Doc 5, table)", never Table 5. A and B matched and
  rejected 13.7; review block risk 10-15%; the declared Failure mode 1 predicted 13.7 exactly.
  Rev 1 added "all" ("all non-student respondents"). Its Question box (user screenshot, same day) showed
  two orange advisories, each listing one thing only ("Japan's 2016 Financial Literacy Survey": two Doc 5
  mentions of the same survey; "households in the 2015 China Household Finance Survey": Doc 2's survey and
  its own 1.414), and rev 0's advisory that matched the decoy 15.2 was gone. Rev 1's "One defensible
  answer" result was not yet run or shown; review block risk about 25%.
  A user-edited wording with the condition stated outright (rev 1 plus ", including those with missing
  background information,") cleared the form, since its difficulty run executed, but ended "Answer not supported":
  the high model still took 13.7 in 3 of 3 every-document attempts because it never found the gold's input
  (a decomposition table's header cell). Stating the separating condition clears the block; it does not make
  a hard-to-find gold input reachable. See reference/platform-quality-checks.md.
- 2026-10-08, aq-01543 q01 (form state with the question, gold and documents of revs 1-8; reasoning box
  not shown; user screenshots in tasks/aq-01543/runs/q01-platform-unbound-2026-10-08/): the red "Working
  the question from the documents does not give this answer ..." message above, with no solver answers.
  The gold, 22.8 percentage points, needs Bulgaria's 2024 coal share built as baseload "(coal, nuclear)"
  minus 41.6% nuclear, while Doc 1 prints coal at 27.6% for "September 2024 to August 2025", a window
  starting in the asked year, so "In 2024" was the only separating word. Local Opus solvers matched 22.8
  in all 16 runs over revs 1-8, each naming and rejecting the 28.6 route. Rev 9 states "In calendar year
  2024" (rev 0's wording, dropped at rev 1 because an auditor said it flagged the trap). Rev 9's Quick
  test (user report, same day, no screenshot): "Too easy. Solver got it". Stating the condition made the
  built gold reachable but left the derivation as the only route, and the low model took it. No fair
  wording sits between the two states, so q01 was dropped. The same thing happened to this bundle's q02
  ("with the world": Too easy) and to aq-01321 q02 (cleared, then Easy).
- 2026-10-08, aq-02086 q02 rev 0 (list answer, no printed decoy; raw in tasks/aq-02086/runs/q02-r0-...-platform/):
  "Which hazards in the ... annexed examples ... fell outside the law's first phase?" with a gold naming the two
  scenarios ("Rodents entering through the kitchen wall, and a faulty window handle that may snap"). Both form solvers
  answered in HHSRS hazard types: "Entry by intruders, water supply, and domestic hygiene, pests and refuse" (took the
  emergency water-supply decoy) and "Domestic hygiene, pests and refuse; entry by intruders (as a significant
  hazard)." (right in substance). Different answers, still blocked, so the check needs a solver to match the gold's
  wording, not merely agree. Cause: "Which hazards" invited the category as the answer unit. Rev 1 asks "Which ...
  examples ... were not yet covered" and the gold names each example with its type label; form result pending.
  Lesson: write the gold in every unit the question's noun allows (instance plus category label).
- Cleared the form, with the words excluding the decoy and the documents needed to apply them:
  aq-00964 q01 ("then-current", Medium), aq-00745 q09 ("in force when", High), aq-01322 q01
  (edition trap, Medium), aq-01431 old q01 rev 0 (exact label). aq-01278 q02 ("On that same basis")
  cleared with the "This question may be too vague" advisory, passed at Medium, and was then
  returned by the platform reviewer for the same ambiguity.
- 2026-10-10 (aq-02673 q04 rev 0, difficulty Run 1, Version d599f9): "Too hard", Low 0/5 · Medium 0/5 · High 0/5, with
  "This question may be too vague". The question asked how much more of the western Atlantic bluefin TAC the United
  States was allocated for 2026 than 2025; the gold (168.84) counted 2025's 25 mt bycatch set-aside because another
  document says it was drawn from that TAC, while 2026's 62.5 mt is not. All 15 attempts gave the plain baseline
  difference (193.84), which one document prints as a pair. One High attempt quoted the deciding sentence, derived the
  gold twice, called it "a stretch" and chose "the simplest reading"; three Medium attempts misread the old set-aside as
  eastern too. So a counting rule that only the documents reveal is not a trap the solvers fall into and climb out of:
  they treat the printed pair as the intended answer. State the counting rule in the question ("counting any ...
  allocation drawn from that TAC") and leave to the documents only which items meet it. The Coach's fix (ask for the
  baseline quota difference) would have made a one-document lookup; do not adopt a rewording that removes a ticked
  document's role. Rev 1 (the clause "counting any longline bycatch allocation drawn from that TAC" added) was then
  too easy at the quick test (user report, 2026-10-10 15:43, no capture): a clause that names both the item and the
  test to apply to it hands over the whole inference. Rule unstated = every solver on the printed pair; rule stated
  with item and test named = too easy. Rev 2 tries a scope word that names neither ("in total"), with a stronger
  alternate ("whatever fishery the tonnage was reserved for") for the same quick-test pass; results pending.
- 2026-10-10 (aq-02673, results of the midpoints): "in total" (q04 rev 2, Run 2, Version 5d3970) was Between
  levels, Low 0/5 · Medium 0/5 · High 4/5; "whatever fishery the tonnage was reserved for" (q05, Run 3, Version
  1ee802) was In band - Medium tier, Low 0/5 · Medium 1/5, and the page still showed "This question may be too
  vague" beside "You can submit now". So the advisory tracks solver agreement on a wrong answer, not the gate.
