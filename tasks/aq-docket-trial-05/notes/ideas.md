# aq-docket-trial-05 - lean candidate sketches

Current target: medium (user, 2026-10-06: "at least Medium", one attempt); measured platform success pending.
Design basis (memory, measured): Medium = Low 0/5 then Medium 1-3/5; the only proven route is a
same-label wrong value that only close reading rules out (aq-00964 q01, aq-00745 q09). Low 0/5 with
Medium 4-5/5 is undocumented, so the trap should also catch the medium model sometimes. This bundle
holds ten unrelated rulings: earlier sketches on it (memory) were all solved locally, and the two
platform quick tests already used (q01 federal-claim survivors, q02 with-prejudice jurisdiction
dismissals) were "Too easy". So each sketch below rests on an internal trap in one ruling plus a
second ruling for necessity. The strongest internal trap (hooks h7: Hill's list ranks) has no
legitimate second source and is held.

Round 1 (2026-10-06, origin claude; all six passed the mechanical screen with no FAIL/WARN):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1: count-by-defendant matrix; conclusion says counts dismissed "as to the City and BPD" | Counts still pending against anyone after the rulings, Maryland lieutenant + Baltimore sergeant. Gold 9 (1 + 8) | D03 L471, L521; D04 L67-79, L477 | Mentions it vs does it; aggregation. Decoy 6 (conclusion-only reading) | intro L41 loose wording | screen pass; local solve pending |
| i02 | h2: buried prior-case parenthetical | State police forces held shielded by the Eleventh Amendment. Gold MDSP, New Mexico State Police | D03 L503-505; D05 L211; D04 L169 | Bury one list item late; decoys BPD, Will (Michigan) | DPSCS (Pense) wording | screen pass; local solve pending |
| i03 | h3: claims-to-defendants inference | Individual prison-medical defendants with every claim dismissed with prejudice. Gold Lock, Money, Huner | D09 L89-95, L171; D08 L267; D02 L259 | Match then exclude; decoys Lasher, Weber, Edwards | Wellpath kept out by "individual" | screen pass; local solve pending |
| i04 | h4: chronology inside a prior-case list; buried prior suit | Federal suits filed before the current suits: New Mexico woman, New York woman. Gold 3 and 1 | D05 L209-239; D06 L145, L161 | Temporal alignment; bury one item. Decoys 10 ("eleven"), 0 | anchor on filing, not removal | screen pass; local solve pending |
| i05 | h5: footnote fact vs refused request | Plaintiffs who had appointed lawyers. Gold Resper, Cora | D02 L27; D10 L81-83; D07 L275 | Mentions it vs does it; decoy Mulvilhill | Hill/Worsley representation unstated | screen pass; closed-book unknown; local solve pending |
| i06 | h6: judge in two roles across two list items; hedge decoy | Plaintiffs who sued a judge who had ruled against them. Gold Hernandez, Langworthy | D06 L103, L117; D05 L225, L239; D07 L173-177 | Who belongs where; does the hedge apply; decoy Mulvilhill | L103 vs L123 judgment dates | written up as q01 rev 0 (prepared for packets); local solve pending |

Sketch-stage results (runs/sketch-round1/returns.md): fresh Opus solves matched all six with high
confidence; closed-book screens missed all six. i04 dropped: its solver showed the documents list only
one district's cases over three years and one alleged prior action, so "how many earlier federal
suits" is not pinned. i05 held: a court-appointed-only reading gives Resper alone.

Round 1b (same day): i07 replaces i05 as a sharper who-belongs-where variant of i06 (judges sued by a
litigant they had dismissed or entered judgment against: Gonzales, Liccione; decoys Leo, Urias,
Khalsa, Johnson, Modelewski, Fields, Crandall). Written up as q05; its shortcut audit returned
ambiguous (case-number initials "DHU" plausibly make Urias a third answer), so q05 is dropped.

Promotion: i06 -> q01 rev 1, i01 -> q02, i03 -> q03, i02 -> q04, i07 -> q05 (dropped). Full checks
for q01-q04: two matching fresh solves, closed-book miss and clear audit each; reviews pending.
Quick-test wording equals the final wording of each question file.

Reviews (2026-10-06): q01 revise, Easy most likely, Medium about one in five or less; q02, q03 and
q04 revise, Too easy most likely (items print the qualifying facts; decoys ruled out in their own
passage; q04's "bury late" claim was wrong because item (i) is first). Fairness otherwise met.

Round 2 (independent question-author, fresh context, all ten rulings read): no sketches returned.
Finding: no fair Medium design exists in this bundle. The only untied same-label trap is Hill's list
ranks (h7, single document). Every other same-label value is ruled out in its own sentence or
footnote, or the ruling contradicts itself (Cora reconsiderations and finality dates; Howard letter
dates; Hernandez judgment dates), or it has no counterpart in another ruling. Cross-document groups
(two Maryland officers, two Pennsylvania prisoners, two New York suits against judges, three
prison-medical suits) all print the deciding fact per item.

Decision: q01 rev 2 (same question and answer; reasoning timing, step 4 wording and Doc 3 listing
fixed) is the hand-over candidate, with a full fresh re-check; quick-test before the single attempt.
Rev 2 re-check (run c2f7f4c3...): solvers A and B match with high confidence, closed-book misses,
audit clear (difficulty risk: union of two per-document findings). Review: ready for fairness,
difficulty easy (Easy ~55%, Too easy ~25%, Medium ~15%, higher ~5%). Rev 3 adds the evidence
quotes the review asked for (Hernandez naming the justices; the two Langworthy case names); fresh
checks on run 50c87d6e...: A and B match, closed-book misses, audit clear, review ready for
fairness, difficulty easy (Too easy ~30%, Easy ~50-55%, Medium ~10-15%). Handed over as checked;
quick test pending.
Round 3 (user, 2026-10-06: "can you make QA like Trial 2's q01 or Trial 6's q02"): numeric
sketches whose answer no document prints, derived over three or more dependent steps through a
carve-out, definition or footnoted remainder, with a printed same-label decoy. Two fresh
question-authors with split scopes: (a) paired comparisons across natural frames (two Maryland
officers, two Pennsylvania prisoners, two New York judge suits, three prison-medical suits);
(b) bridges and same-label chronologies (Cora's three notifications, Hill's ranks, Langworthy's
dated list, Hernandez's original vs amended complaint).
Author (b) returned no fair sketch (all ten texts read in full; script matched shared dates and
places, all coincidences). Near-misses: i08 state-police suits filing-to-ruling, Hill 430 vs NM
item (i) 34, 396 days (fair but trapless, Too easy; decoys excluded by the word "suit"); i11
Langworthy removal vs Hernandez original complaint pending spans, 107 days (forced pairing; removal
trap tied in the same parenthetical); i09 Cora first to third notification, 414 days (single
document, L313 states the August 16, 2024 notice outright); i10 Rule 4(m) bridge into Hill's filing
(general knowledge, three answers via weekend/holiday roll-forward, overview exposes inputs).
Internal contradictions found: D09 L77 "June 31, 2023"; D08 L61 letter dated after its reply;
D03 L103 vs L223 Butler appointment dates; D10 L169/L171 vs L213/L315 reconsiderations.
Author (a) (all ten texts read): one fair numeric sketch, i12 (its i01): share of judges among
the individuals sued by the two pro se New York plaintiffs who sued state-court judges, 5 / 17 =
29.4% (D06 L43-L65 groups hide two individuals among the "Bank Defendants" and a court among the
"Judicial Defendants"; D07 L101 names Ricki and Peter before the summons list; D07 L155 "Judge
Randall" misspelling); wrong routes 33.3% (four ways), 36.4%, 23.1%, 31.3%; author estimate Too
easy ~50%, Easy ~40%, Medium ~10% (traps tied in the list sentences). Near-misses: i13 counts
dismissed as to every defendant in the two Maryland officers' suits, 7 (complement of q02, Too
easy); i14 days between the two Pennsylvania grievances, 373 (Richards's grievance one week before
his September 20, 2023 visit; decoy 366 sits in the same sentence; arbitrary pairing; Howard also
had an undated 2022 grievance); i15 share of prison-medical individuals still facing a claim, 50%
(30% defensible: D02 never rules on Mace and Akintade).
Decision: i12 promoted to q06 (screen clean), the only fair numeric design. q06 rev 0 (run
c87a0c48...): A and B match (high), closed-book misses, audit clear, review ready for fairness,
difficulty easy (Too easy ~50%, Easy ~40%, Medium ~5-10%): every trap is settled in its own
sentence and no document prints a figure a quick reader might take. Review: quick-test q01 first,
then q06; never submit both (q06's premise reveals q01's decoy).

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Platform quick tests (low model only, user-run) are the next screen.
