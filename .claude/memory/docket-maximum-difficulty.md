---
name: docket-maximum-difficulty
description: "The user wants maximum-level questions only, judged against the Docket platform's reviewer model (the 'high model'), not our Claude solver; ready requires the gate's Q13 (D1-D7 met in the documents and the blind solves' paths, a closed-book miss, review difficulty 'maximum'); a local wrong-lever miss is a bonus, not a requirement."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-04
  originSessionId: 9e8d8c8c-aa4d-457b-a7c1-04fe73680640
  modified: 2026-10-05T10:40:46.141Z
---

> **Frozen history (2026-10-14).** Measured mostly against the Low and Medium solvers. The current
> design rules are in [hard-playbook.md](reference/hard-playbook.md); where this note differs, the
> playbook wins. Open this note only for a specific case it records.

## Superseded policy

The latest user instruction (2026-10-05) makes Easy the minimum target. Read
[docket-redesign-v2.md](docket-redesign-v2.md) and WORKFLOW.md. The following rule is preserved
as historical calibration; it no longer governs new-question acceptance.

## Historical rule

`ready` means maximum difficulty, not survival, and the yardstick is the Docket platform's
reviewer model (the "high model" of its feedback), which only the platform runs. Our Opus 5.5
blind solver is not that model and not the target. A question is ready when it passes the gate's
Q1-Q12 and Q13:
- built to beat the reviewer model: D1-D7 hold in the documents and in both blind solves' paths
  (bundle-only deciding fact; no shortcut passage; the natural path leads to a decoy; the
  deciding fact sits away from the decoy; easy to verify; lean wording; every lever counts and
  the answer cannot be guessed), on one or two levers (first choice: mentions it vs does it,
  does the hedge apply, match then exclude), with at most two conditions in the wording. A decoy
  disproved beside itself is no decoy, and D4 is never bought at the cost of one defensible
  answer;
- fair: two fresh blind solves reach the key or miss only on the lever, with no `ambiguous` or
  `not-answerable`, and the closed-book solve misses;
- the review rates difficulty `maximum`;
- the platform's difficulty check on that exact wording reached the High tier without ending
  "Too easy". The check is a ladder: the low model gets five attempts, then the medium and high
  models, and it stops at "Too easy" once a tier's solvers reach the answer too often. Surviving
  the low model is the minimum bar; the user's bar is the high model. A local `maximum` is only
  a prediction: report it as "passes the local gate", never as maximum difficulty, until the
  platform has spoken.
A blind-solve `match` is the fairness proof, not a failure; a `wrong-lever` is a welcome bonus,
not a requirement. A failed D-check means below maximum: status `checked`. Harden through the
evidence, never by stacking conditions. The platform's verdict is the measurement: log it and
recalibrate. After three sketch rounds with nothing to write up, tell the user what the bundle
supports.

**Why:** on 2026-10-04 (aq-docket-trial-03), after the Coach explained that a quick test's
"survived" is only the minimum bar, the user said: "no, I don't want survived level. I want
maximum level. plz update gate". Later that day: "You need to update gate to design the best
Q/A, The difficulty must be maximized so that even the best models cannot solve it", then "not
maximum model. if high model can't solve, it's good design for Q/A", then "I mean the high model
is not the claude model. it's the Docket platform reviewer model."

**How to apply:** the gate card (`reference/question-gate.md`: Q13, "Maximum difficulty: the
platform's reviewer model cannot solve it", and "Designing for the reviewer model" with D1-D7,
hardening moves and the stop rule), `/docket-check` (rev-tagged records; sketches judged by
their path), `question-review` (difficulty rated from D1-D7 and the paths) and the floor
(`ready` needs this revision's two blind solves, a closed-book miss and a review with
`difficulty: maximum`) all carry this. See also [[docket-local-solver-calibration]] and
[[docket-general-knowledge-check]].
Before the first sketch round, scan the documents for named entities and lists they share. The
three most effective levers need one set of items that spans documents: claims that mention or
do, hedged or firm statements, items to match and then exclude. If the only shared entities are
agencies, programs and dates, those levers have no cross-document form. Tell the user then,
rather than after three numeric rounds.

## Evidence and history

- 2026-10-04: instruction given in aq-docket-trial-03 after q01 rev 5 passed every local check
  with all blind solves matching. Gate, commands, agent, workflow, CLAUDE.md and floor updated
  the same day. Existing `ready` questions in every bundle with no recent `wrong-lever` now fail
  the floor's ready check, so set them to `checked` and treat them as below maximum.
- 2026-10-04 (aq-docket-trial-07, seven unrelated BLS Monthly Labor Review articles): three
  sketch rounds (i1-i10) gave no survivor. The articles share only agencies and programs
  (Census Bureau, OMB, BEA, QCEW, CES, CPS/ACS) and two recessions, so every hedge, list and
  claim set sits inside one article. The best fair design, q03, was a bridge with a prose
  decoy: a chart month in one article decides which value to read in another. It matched on
  both blind solves and the closed-book solve missed, so it is `checked`, below maximum. Reported
  to the user per the rule. One bundle; the intake scan above would have flagged it before
  sketching.
- 2026-10-05 (aq-docket-trial-03, DOT agendas plus a 2025 proposal and 2026 final rule): the
  bundle does share item sets: the proposal's three cited meetings against the agendas' rulemakings,
  review findings, and rule components. Five maximum-level sketches used them (i9-i13), with two
  high-model solves each. Every lever was handled: the 'Ancillary Services' title trap, the
  'minimize the SEISNOSE' mention, the 'may have some impact' hedge, statutory vs discretionary
  components, and planned vs published. One sketch's misses came from my own wording, not the lever.
  No survivor, so q01-q03 stay `checked`. Shared item sets are necessary but not sufficient: this
  local solver reads every candidate and also checks the companion documents.
- 2026-10-04 (gate update, the user's last three messages above): the earlier gate called our
  Opus 5.5 max blind solver "the high model" and required one of its two solves to miss. Across
  seven bundles it solved every sketch (about fifty, the three most effective levers included),
  so no question could become ready. The gate now targets the platform's reviewer model:
  - the wrong-lever requirement is gone; D1-D7 are checked against the documents and the solves'
    paths, the review records a difficulty rating, and the floor reads rev-tagged records;
  - the design checks come from the platform's own "too easy" explanations, which describe the
    solver's path ("Answered from one passage in Doc 6");
  - questions marked `ready` under older record formats fail the floor until a fresh
    `/docket-check` writes rev-tagged records. At the time these were trial-02 q02 and q03 and
    trial-06 q03, each with only blind-solve matches.
  Whether D1-D7 predict the platform verdict is untested. Record each platform result against
  the D-checks it passed.
- 2026-10-04 (aq-docket-trial-07, redesign under D1-D7): round A gave one write-up (q05, a
  chart-peak bridge between the rail and Midwest manufacturing articles). It had two blind
  matches and a closed-book miss, but the review rated it below maximum because D4 failed: the
  prose decoy sat right after the chart that refutes it. Two other sketches were exposed: the
  closed-book solve guessed a plausible percent (3.0%) and a small count (6 months). Lesson: when
  each data series lives in one document and no document claims anything about another's data,
  D4 cannot hold, because every decoy is refuted inside its own document. Stop there and report.
  Same day, after D4 became a preference: q05 re-rated at rev 0 (solves reused, unchanged text),
  verdict ready, difficulty maximum, with D3 as its main platform risk.
- 2026-10-04 (aq-docket-trial-06, six GAO consumer-protection reports, redesign under D1-D7):
  the intake scan found agencies and laws as the only cross-document sets. One round still
  tested agency roles, and both sketches were hard paths with closed-book misses, so both were
  written up. The review rated both below maximum. q04, five banking regulators minus those GAO
  named unsuited for section 43, was dropped. One search for an agency's name in the other
  report reached the late passage that rules it out (D4). Worse, GAO's reason for that ruling
  (any federal supervisor) applies to the remaining answer items too. The key held only
  because the report never printed their names: a defensible "none" and a rule 10 risk. q05,
  preemption claimants minus the one whose rulings OCC's 2004 rule adopted, stays `checked`.
  Its deciding passage was early in its report, every search for the excluded agency hit it,
  and the exclusion phrase described the answer's other item (Q8). Lesson: with agency sets,
  the deciding fact is printed beside a searchable name. A stated reason then reaches past the
  named items, so D4 and one defensible answer pull against each other. Stopped after one
  round per the intake rule and reported.
- 2026-10-04 (aq-docket-trial-04 q05): first platform result for a question rated under D1-D7. Review: below maximum, D3/D4/D7 failed (lexical bridge to every candidate; each decoy refuted in its own sentence; two lookups plus an intersection), D1 held. Platform quick test (low model): "Too easy — solver got it". The failed checks predicted the verdict; one case.
- 2026-10-04 (gate update, the user's decision in docket-88): D4 became a preference. In the
  redesign it had stopped four bundles (trial-01, -05, -06, -07), all collections of unrelated
  documents where each decoy is refuted inside its own document. In trial-06, forcing it cost
  one defensible answer. It is also the one D-check that comes from our own solver's behaviour,
  not a platform verdict. Asked whether to make D4 a preference, wait for trials 02 and 03, or
  keep it required, the user chose "Make D4 a preference". Maximum now needs D1-D3 and D5-D7;
  D4 is reported either way. The trial-04 q05 result above still stands: it failed D3 and D7 as
  well. Record whether D4 held for each platform result, to learn whether it matters to the
  reviewer model.
- 2026-10-05 (aq-00745: seven Abbott earnings releases plus an Exact Sciences deal release,
  by-laws, a derivative settlement notice and an NEC settlement release): the intake scan found
  item sets only inside the release series, where every figure, footnote and dividend ordinal
  is printed beside its own period or date. The four non-release documents join the releases
  only by dates, and the overview prints those dates. Of 10 designs, three were written up:
  q01 (quarters in which prior-year tax resolutions raised taxes), q02 (dividends declared as
  of the hearing date) and q03 (legal reserve in the quarter the by-laws took effect). Each had
  two blind matches and a closed-book miss. Review rated all three below maximum: D7 every time
  (lookups plus a date or sign step), D2 for the two date bridges the overview prints, and D3
  for q01 and q03. Round 3 was assessed on paper against those checks; nothing passed, so the
  stop rule was applied and reported. Local review only, one bundle. Lesson: when only dates
  join the documents, a date bridge is two lookups (D7) and is usually printed in the overview
  (D2).
- 2026-10-04 (aq-docket-trial-02: ten Colgate-Palmolive earnings releases, a recast segment exhibit and a
  2019 award form): the intake scan found one cross-document item set, the special charges that each
  release's Base Business definition names "as applicable" while only the Corporate notes and
  reconciliations carry amounts. Of four designs (i11-i14), two were exposed: the closed-book solve came
  near on a restructuring-quarter count (8 against 7) and on a division filter (it guessed Latin America).
  Two were hard paths and were written up. q06 asked in which quarters ERISA charges cut operating
  profit (Q1 and Q4 2025). q07 asked which charge types were excluded for 2025 but not in the first half
  of 2026. Each had two blind matches and a closed-book miss. Review rated both below maximum on D7:
  each release prints its own period's adjustments, so the paths were labelled lookups and a set
  difference. q06 rev 1 moved to the pretax effect, where the printed Q4 operating charge of $84 had
  no pretax line. That made the key the Q1 2025 charge, public since April 2025, so D1 failed and the
  closed-book solve came near. Lesson: in an earnings-release series, the post-cutoff facts are printed
  outright, and the two-statement inferences rest on pre-cutoff facts. D1 and D7 pull against each
  other. Local review only, one bundle; reported to the user.
- 2026-10-04 (aq-docket-trial-06 q05, after D4 became a preference): the rev 0 re-rate stayed
  below maximum on Q8 and D7. The exclusion "leaving out any whose determinations another
  regulator's 2004 rule adopted" could only describe OCC's rule, and OCC was an answer item, so
  the wording settled one item and left a two-way pick. Rev 1 dropped the agent: "findings folded
  into a rule issued in 2004". That one condition removes both the adopter (OCC's rules codified
  its own opinions) and the adoptee (OTS precedents on OCC's lists), leaving NCUA. Two blind
  matches; the closed-book solve gave the decoy (OTS and NCUA, what models believe); the review
  rated it maximum, with D4 met only in the letter. Hardening move: when an exclusion names who
  did something, reword it so the condition applies to every candidate the evidence touches. The
  wording then stops pointing at an answer item, and each exclusion fact counts. One question;
  the platform verdict is pending.
- 2026-10-04 (aq-docket-trial-07 q05, calibration): rated maximum locally with D4 not met (after D4
  became a preference), then solved by the platform's low model in the quick test. The Coach
  said "no decoy to trip on": the decoy sat right after the chart that refutes it, and the
  question's wording led straight to the table maximum. This is the first platform result
  against a question that failed only D4. It counts in D4's favour, and it says the local D3
  rating was too generous. One result; reported to docket-88 for the gate.
- 2026-10-04 (gate update, the user's decision in docket-88): D4 restored as required, reversing
  the preference set earlier the same day. Platform evidence now covers it: two of two questions
  that failed D4 were solved by the low model in the quick test (trial-04 q05; trial-07 q05, "no
  decoy to trip on"). Asked whether to require only D4's minimum, restore it fully, or quick-test
  first, the user chose "Restore D4 fully". Maximum needs D1-D7 again. The gate, reviewer and
  check command now say a decoy disproved beside itself is no decoy. Re-reviewed with D4
  required: the questions made ready while it was a preference, trial-05 q04 ("decoy ruled out
  beside it") and trial-06 q05 ("D4 met only in the letter"). Lesson: relaxing a check because
  only the local solver supported it was premature. Wait for a platform result before removing a
  check that targets decoys.
- 2026-10-04 (aq-docket-trial-06 q05, after D4 became required again): rev 1 was re-reviewed with
  no new solves and fell to below maximum. Its deciding fact (OCC's lists took in OTS rulings)
  is printed at OTS's first mention in the second report, so a search for the name the first
  report supplies lands on it. The excluded item's first mention in the other document was its
  refutation. In agency-set bundles, check where each candidate is first named in the document
  that excludes it. A late fact under a heavily repeated name (NCUA 86 times in one report) is
  the remaining D4 route. There it is usually an agency's position, which models infer (D1).
  Stopped and reported. Platform verdict: none yet.
- 2026-10-04 (aq-docket-trial-07 q06, after D4 was required again): the Coach's suggested lever, an
  exact table figure against rounded prose ("contracted by over 17 percent"), did not fix the
  structure. The rounded figure sits two lines after the chart that refutes it (D4 fails), and
  the path is four named cells plus arithmetic (D7 fails). Review verdict: drop. Bundle stopped
  and reported: this structure cannot reach maximum.
- 2026-10-05 (aq-00745, round 3 after the user asked to "re check, you must find best option"):
  two write-ups copied the peak-bridge shape (a series peak that no sentence prints decides which
  value to read). q04: the quarter with the largest deferred-tax adjustment, then its GAAP rate.
  q05: the 2025 quarter with the largest COVID share of Diagnostics, then its growth. Both were
  fair, both closed-book solves missed, and both were rated below maximum:
  - the question's own wording ("calendar quarter", "share") excluded each decoy;
  - the peaks sat at the series edges, the latest quarter and the first one;
  - every quarter's figure is printed beside its period.
  Lesson: a decoy works only if the wording admits it. Year-to-date or level figures that the
  question's unit word rules out are not decoys. A peak at the first or last period is an
  edition shortcut. Local review, one bundle; consistent with the platform's low-model solve of
  trial-07 q05.
- 2026-10-04 (aq-docket-trial-03 redesign, three DOT agenda editions plus a UDP proposal/final
  pair): three sketch rounds, four write-ups, one at maximum. q04 reached it with D4 required. The
  question named the middle edition and asked about that edition's own date, and that edition
  printed one proposal (AK09) only as a projected month. Only the last edition, under a new title
  and stage, dated it before the middle edition appeared, and no sentence joins the two facts.
  The failures:
  - q05 bridged a 2026 rule's environmental exclusion into a plan's part range. The proposal
    prints the same sentence, and models know the citation, so it failed Q2 and D1.
  - q06 took the union of two editions' early-2023 proposals. Naming both editions removed the
    one-edition decoys, and each date sat in its item's own row, so it failed D3, D4 and D7.
  - q07 asked about the same lever "a year after" the first edition. That points straight to
    the last edition, and the excluded items were famous rules, so it failed D2, D3 and D7.
  Lesson for agenda series: the projected-vs-published lever works only when the question's
  time anchor is the named edition itself. Anchoring on a later date hands the reader the right
  edition. Local review, one bundle; platform verdict pending.
- 2026-10-04 (aq-docket-trial-03 q04, platform quick test pasted by the user in docket-88):
  "Too easy — solver got it". The low model listed the three rulemakings in order: "Of those,
  only three had already published their NPRMs by the time that agenda appeared (Feb. 9,
  2024)". The user's words: "hey, you told me it's maximum. but in platform it's too easy".
  The local gate had rated q04 maximum with D4 required, and docket-88 reported it to the user
  as clearing the full gate, which overstated a prediction. Two weaknesses the local review
  passed:
  - The deciding date sat in another agenda, but under the same RIN (2120-AK09). A model holding
    every document links a shared identifier at once, so this was a direct link, not a bridge.
  - Read at face value, the middle edition's projected NPRM 12/00/23 already falls before the
    February 2024 agenda. That naive route lands on the key, so the decoy pointed the wrong way.
  The public December 2023 NPRM (a D1 risk docket-15 flagged) may also have helped.
  Changes:
  - `ready` now needs a platform quick test that survived, and the floor enforces it.
  - D3 now works out the answer under each naive reading, and none may equal the key.
  - D4 now fails when the item carries a shared identifier across documents.
  Platform results so far: every local "maximum" tested (trial-07 q05, trial-03 q04) and every
  below-maximum one (trial-04 q05) was solved by the low model.
- 2026-10-05 (gate update in docket-88, from aq-00745 q01's verdict; the user: "You can check
  aq-00745's verdict. based on that, check if needed to update design gate"). The verdict
  confirmed the gate's prediction: local review had rated q01 below maximum (D3, D4, D7), and
  the platform said "Too easy", low model 5/5. It also showed two things the gate lacked:
  - The difficulty check is a ladder: "Low 5/5 · Medium — · High —". The low model gets five
    attempts, and the medium and high models run only if it fails often enough.
  - The five saved tracks (tasks/aq-00745/verdict/) show the low model's method. It works
    through every release, reads each quarter's own note, reconciles full-year and year-to-date
    totals with the quarters, drops prior-period comparatives, and settles the window plainly.
  Changes:
  - `ready` now needs the check to reach the High tier without ending "Too easy". The tier line
    is recorded verbatim, and the floor rejects a tier line with no High count.
  - Q3 now says the platform matches meaning, not tokens.
  - D7 now calls a filter over per-item printed statuses a lookup filter, and asks for at least
    one answer item that qualifies only through two statements.
  - The gate lists cumulative totals and comparatives as non-decoys.
