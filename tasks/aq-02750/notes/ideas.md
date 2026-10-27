# aq-02750 - lean candidate sketches

Current target: medium, Hard welcome (user, 2026-10-10: "there is no slot for Easy Tier for this bundle, we
should target medium and high"); measured platform success pending. Round 1 result (user chat, 2026-10-10,
"three of them too easy to pass quick test", no panel or trace): q01 rev 0, q02 rev 0 and q03 rev 0 are taken
as the three; i07 and i05 are not known to have been tested. Hooks are in notes/hooks.md. Origin of
every sketch here: claude (Claude Code, claude-opus-5-5). Round 2 of at most three.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | sketches/i01.md | h1: the order in force when a U.S. aid worker's positive test was announced (July 10, D06 only) is the June order (D05); the rise between its two DRC counts, 91 and 837, is 819.8% | Competing: 123.8% (D06's own pair) and 130.5% (D07's) fail "in force when"; "more than 800 percent" fails "to one decimal"; 919.8% is not a rise. D06: the event, D06 only. D05: 91, D05 only (D06 restates 837 alone) | promoted to q01 rev 0 (30 words). Quick test: too easy (user chat, 2026-10-10). Replaced by i07 as q01 rev 1 |
| i02 | sketches/i02.md | h2: the order in force when Uganda declared its outbreak over (July 28, D07 only) is the July order (D06), whose comment period closed July 31 (D06 only): 3 days | Competing: 0 days (July 13 + the "15-day" label, from D07 alone) fails against D06's printed deadline; 35 days (D07's own deadline) and 15 days (the order's end) fail "comment period ... on the order then in force". D07: the event. D06: the deadline | promoted to q02 rev 0 (22 words, "comment deadline for the ... order then in force"). Quick test: too easy (user chat, 2026-10-10). Rev 1, the one focused repair, drops the status cue: "When Uganda declared its Ebola outbreak over, how many days remained to comment on CDC's entry-suspension order?" (17 words, same gold). Quick test: too easy again (user chat, 2026-10-10). Hook h2 retired, q02 dropped |
| i06 | sketches/i06.md | h10 (independent author B's b01, re-verified by the caller): commenters asked for lawful permanent residents to be allowed back on the June 21 order (answered in D06); that order's deadline is July 10 (D05 only); the rule that ended the exemption is D04, comments by June 26 (D04 only): 14 days | Competing: 35 (D06's own July 31) fails "that order's comment deadline"; 10 (June 21 + 15) fails against D05's printed date; 18 (Amended Order, June 22) fails "rule". D04 and D05 each supply an operand; D06 identifies the order, D07 only by elimination, so they are declared alternatives | promoted to q03 rev 0 (32 words). Quick test: too easy (user chat, 2026-10-10). Dropped: the identifying fact has to be stated in the question and both deadlines are first-line DATES entries, so there is nothing to repair |
| i07 | this row | h1 with another anchor, same gold as i01. "By what percentage, to one decimal, did DRC's confirmed cases rise between the two counts in CDC's entry-suspension order in force when CDC raised its outbreak response to Level 1, its highest?" Gold 819.8% | The escalation is reported in D06 L178 and D07 L163 and dated only by their footnote, "CDC, Internal Decision Memo, June 26, 2026"; D05 (June 21) does not report it, D06 (July 13) does, so the June order was in force. Risks: the date is a footnote citation, not a stated event date; "26" first appears past character 26,000 in D06 and D07, so the form would probably show a false alarm on it. Both later orders carry the event (identifying role "D06 or D07"), which removes q01's document-check weakness | promoted to q01 rev 1 as the one focused repair for q01's quick-test result. Quick test: too easy again (user chat, 2026-10-10). Hook h1 retired, q01 dropped |
| i03 | this row | h3, same event as i02. "When Uganda declared its Ebola outbreak over, CDC's entry-suspension order then in force cited two dated DRC confirmed-case counts. How many cases a day separate them, to one decimal?" Gold 38.4 = (1,873 - 837) / 27 days (June 15 to July 12, both dates in D06 L125) | Competing: 90.6 or 87.3 (D07's own pair) fail "then in force"; 37.0 (D05's 837 with D07's restated "July 13") is not the July order's own dating; inclusive counting (28 days) also gives 37.0, so the elapsed-day convention carries weight. D06: the July 12 date, D06 only. D07: the event | not offered. Besides sharing q02's event: 1,036 / 27 does not terminate, so the form's number check would flag the final step whatever the wording, and independent author A dropped the daily-rate family for the July 12 / July 13 conflict |
| i04 | this row | h4. "From the as-of date of the DRC confirmed-case count in CDC's July 2026 entry-suspension order to that of its August order's count, how many cases were added per day, to one decimal?" Gold 87.3 = (4,318 - 1,873) / 28 days (July 12, D06, to August 9, D07) | Competing: 90.6 (27 days, from D07's restatement "On July 13, 2026, when the last Order was issued, DRC reported 1,873") fails "as-of date ... in CDC's July order". Risk: D07's sentence is a document statement that the count stood at 1,873 on July 13, so a reviewer could call 27 days defensible. D06: July 12. D07: 4,318 and August 9 | not offered: same two defects as i03 (non-terminating quotient; a reviewer could call 27 days defensible) |
| i05 | this row | h5. "If the HHS Secretary makes no finding and nothing extends it, how many days after CDC's August 2026 Ebola order is due to end does the rule letting CDC bar permanent residents lapse?" Gold 77 days (May 27, 2026 + six months = November 27; D07's order ends September 11) | Competing: 72 days (six months from the May 22 effective date) fails D04's "six months from the publication". D04: the expiry clause and publication date. D07: September 11 | quick test only: one plain-sentence rule and a date gap, the shape measured too easy elsewhere (aq-02626 q01, aq-02631 q03). Both independent authors returned the same sketch as their second choice (a02, b02) and both ranked it "hold". Coincidence noted by author B: May 27 to August 12 is also 77 days |

Not sketched, with the reason (details in hooks.md): h6 (travel-notice dates that D05 and D06 give
differently: a paragraph diff that asks about the accounts, not the world); h7 (D01's fiscal-year rows
selected by an event year: the bundle never defines the fiscal year, and without that trap it is a one-step
bridge); h8 (whether the 2025 public-health bar reaches the 2026 outbreak: a legal judgment, and the
"contagion period" is printed nowhere); h9 (the one-year slip in the Security Bars effective date: D03 alone).

Design notes (author checks, not model validations):

- Every candidate is built on the same property of the series: D06 and D07 each report dated events that
  fell while the previous order was in force, and each restates only part of that order. Values the later
  edition does not restate (91; the July 31 deadline; the July 12 as-of date) carry necessity.
- Anchors are stated by status ("in force when", "then in force"), not by what the later document says about
  the event. Workspace evidence: a soft anchor made the later edition's value defensible and the gold "not
  supported" (aq-02706 q02 rev 0, aq-01333 q01 rev 1); a day-level cue was too easy (aq-01333 q01 rev 2).
- All inputs sit within the first 20,000 characters of their documents (D05 L125 at 18,784; D06 L125 at
  17,874; D07 L125 at 16,922), so the form's number check should find every figure.
- Known limit: this is one mechanism family. The same layout has measured Easy (aq-01333 q01, aq-02706 q02),
  Medium (aq-00964 q01, aq-01322 q01) and Hard (aq-00745 q09) on other bundles; nothing local predicts which.
  q02 adds a lure that does not depend on the edition choice (the 15-day label).

Ambiguity: competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

Independent authors (2026-10-10, two question-author agents, fresh contexts, no access to these notes):

- Author A (whole bundle, told nothing of the caller's ideas): first choice a01 = i02 exactly (Uganda's July 28
  declaration, the July order's July 31 deadline, 3 days; wrong routes 35 and 0); second a02 = i05 (77 days),
  held. It found no asymmetric-rule or multi-step-total design: "The three orders share every rule", and
  D01-D03 share no figures across documents.
- Author B (told to avoid the case-count series and look at D01-D03, the two groups' links and the orders'
  non-count content): first choice b01 = i06 (14 days), second b02 = i05 again, held. It found nothing fair
  in D01-D03 as a chain or in the D03-to-CDC link (reasons recorded in hooks.md h7-h9 and its report).
- Reading: two authors and the caller converge on one usable property of this bundle, a later order that
  reports or answers something belonging to the previous order without restating that order's printed
  deadline or counts. q02 and q03 are the two forms of it in which every ticked document supplies an operand
  or is a declared alternative; q01 is the form in which one document only selects the edition.

Round 2 (2026-10-10), after the round 1 quick-test report:

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i08 | sketches/i08.md | h11: one batch of comments run through CDC's two comment procedures. "On June 25, 2026, CDC received 30 letters and 18 portal comments on its interim quarantine rule and 21 letters on its June 21 Ebola entry order; on July 10 it received 22 more portal comments on each. How many met CDC's requirements on method and timing?" Gold 61 (18 + 21 + 22) | Competing: 113 or 91 (the order's mail rule carried to the rule), 83 (rule's June 26 deadline missed), 39 (order's deadline taken as June 21 + 15 days), 40 (portal-only carried to the order). D04: portal only, June 26. D05: mail accepted, July 10 (D06/D07 give only the 15-day label for that order) | Quick test: survived (user chat, 2026-10-10, "i08 survived"; one draw, no trace). Promoted to q04 rev 0, wording unchanged. Difficulty Run 1 (Version b8861d): "Between levels", Low 0/5 · Medium 5/5. Rev 1 (gold 52) checked, difficulty check pending |
| i10 | sketches/i10.md | h12: postmark rule (EOIR) against receipt rule (CDC). "A letter takes four days to arrive. Counting from Federal Register publication, how many more days did someone commenting by post have to mail a timely comment on EOIR's December 2024 interim rule than on CDC's June 2026 Ebola order?" Gold 20 days (31 - 11) | Competing: 16 (both rules treated alike), 12 (swapped). D02: postmark rule and dates. D05: receipt rule (D06/D07 could stand in) | not tested (user, 2026-10-10: "rest not tested"). Held; same documents' comment procedures as q04, so it is an alternative, not a second question for the same tier |

Round 2 design notes:

- What round 1 measured: the easier solver dates an event, picks the order by its printed term and reads a
  printed deadline or count from it, across two or three documents, and follows a content-based identification
  too. Printed inputs plus one subtraction or division do not stop it here.
- q01 rev 1 and q02 rev 1 are each one focused repair inside the same family (an event with no dated
  sentence; no status cue). If either is too easy again the family is retired; no further rewording.
- i08 and i10 change the dependency: no edition choice, but rules that differ between two look-alike
  procedures, applied to one stated case. Nothing else of that kind exists in the bundle (the three orders
  share every rule; D01-D03 have no parallel numeric rules).
- i09 (days from the June order's replacement to the interim rule's expiry) was considered and rejected: no
  document says the July order ended the June order's own term, so "replaced on July 13" is not a document
  fact. i05 (77 days from the August order's scheduled end) does not depend on it and stays available.
- If q01 rev 1, q02 rev 1, i08, i10 and i05 are all too easy: report that no fair Medium design was found and
  recommend release. A third round has no distinct mechanism left to try.

Round 2 quick-test results (user chat, 2026-10-10, verbatim "q01 q02 too easy to pass quick test. i08 survived. rest
not tested"; no panel or trace):

- q01 rev 1 and q02 rev 1: too easy. Five designs of the event-to-edition family have now been solved by the
  easier solver on this bundle, with firm and soft anchors, dated and footnote-dated events, two and three
  documents. The family is closed here.
- i08: survived, and is written up unchanged as q04. This is the first candidate on the bundle that the easier
  solver missed, and the only one without an edition choice: its work is applying two procedures' different
  rules to five groups and adding what is left. Which group the solver got wrong is unknown (no trace).
- i10 and i05: not tested.

Difficulty Run 1 on q04 rev 0 (2026-10-10, raw verdicts/AQ-02750_difficulty_2026-10-10_2058.txt):

- Platform: "Between levels", Low 0/5 · Medium 5/5 · High not run; closed-book needed the documents (18).
- Traces: every low attempt answered 91. Each applied both deadlines correctly, the July 10 boundary included,
  and counted the 30 letters on the rule; the low model recites the rule's submission methods from a blended
  memory of the look-alike ADDRESSES blocks (the orders' "portal or mail", once the EOIR rule's postmark text).
  Every medium attempt answered 61, quoting Doc 4's "all comments must be submitted electronically".
- Reading: one step separates the two solvers and it is all-or-nothing by level. Printed deadlines, a boundary
  day and the 15-day label cost neither level anything, and the easier solver had already cleared
  order-in-force lookups five times on this bundle, so more printed-date groups would not move the medium
  model.
- Rev 1: the rule side is kept as measured. The order side becomes one batch per order (22, 21 and 12 on the
  June, July and August orders), each arriving 19 days after that order was issued. The deadlines fall 19, 18
  and 20 days after issue because the notices were published 4, 3 and 5 days after issue, so the same lag is
  just in time, a day late and a day early: three date additions across three documents, none of them
  printed. Gold 52. The batches differ in size so that leaving out the wrong one cannot give the gold. Doc 6
  only rules a batch out and is entered as an Exclusion / condition source.
- If rev 1 is again Between levels with the medium model at 4 or 5 of 5: no Medium form of this hook is left
  and the bundle should be released or tried for Hard only. If the medium model drops to 0 of 5, the High
  result decides.

Quick test of q04 rev 1 (user chat, 2026-10-11, verbatim "too easy to pass quick test"; no panel or trace):

- The easier solver reached 52, so in that draw it excluded the rule's letters and worked the three arrival
  dates. Rev 0 had stopped it six draws out of six with the same rule-side wording.
- The one low-side difference between rev 0 and rev 1 is the group of valid letters on the June order, which
  rev 1 dropped to save words. With that group present a letter reads as an ordinary accepted comment; without
  it, "letters" stands against "portal comments" and invites a check. Inference from seven draws and one
  trace, not a measured cause.
- Rev 2 (gold 70, 60 words): restores "21 letters on its June 21 Ebola entry order" and keeps a derived order
  side, now one batch per order timed 20 days after comments closed on the prior order (June 22, July 10,
  July 31), which makes every ticked document an answer component and leaves no result hanging on a one-day
  count.
- Honest expectation: the derived dates did not stop the easier solver, so they are unlikely to split the
  medium model. The likeliest results are Between levels again (if the restored group brings the low model
  back to 0 of 5) or Easy (if it does not). Stop rule: one more too-easy quick test, or one more Between
  levels with the medium model at 4 or 5 of 5, and release is recommended. Nothing else in the bundle has
  shown a way to split the medium model.

Difficulty Runs 2 and 3 (capture verdicts/AQ-02750_difficulty_2026-10-11_1820.txt, read 2026-10-11):

- Run 2 = rev 1, "Too easy", Low 4/5 (52 four times; one 82 with the rule's letters counted). This is the
  result reported in chat as a quick test.
- Run 3 = rev 2, "A marked document may not be needed", Low 3/5 (70 three times; 100 and 69, both with the
  rule's letters counted). Document check: needed Doc 4 (52) and Doc 6 (51), reached 70 without Doc 5 and
  without Doc 7. No Medium or High attempts ran.
- Mechanism, from the high model's own working: with an order's notice missing it uses "a 15-day comment
  period" from the order's date (July 6, July 28, "~August 27+"). A printed deadline matters only to a batch
  that falls after that date and on or before the printed one. Rev 2 had one such batch (July 30).
- Low-model record on this hook: rev 0 0/5 (explicit dates), rev 1 4/5, rev 2 3/5 (derived dates). Every
  wrong scored attempt in all three runs counted the rule's letters; no scored attempt was lost on dates.
- Rev 3 (gold 89, 56 words, Docs 4-6): "22 and 19 portal comments reached its June and July orders, each 18
  days after that order was issued" gives July 9 (fallback July 6, printed July 10) and July 31 (fallback
  July 28, printed July 31). Lags tried on paper: 16-18 days put June and July inside their windows; none
  also puts August outside a guessed deadline, so the August order and Doc 7 are out. 17 and 16 fail the
  form's number check in Docs 5 and 6 or leave one day of margin; 18 passes.
- Cost of the repair: every later batch now counts, so timing excludes nothing in the gold; the 30 letters
  are the only exclusion. Timing still decides the answer under the 15-day reading (48, 67 or 70).
- Stop rule: a second Document-check failure or a Too easy result on rev 3 ends this hook. Target question
  still open with the user: the form shows "Easy 0/1"; rev 2's low count was inside the ready range.

Difficulty Run 4 (capture verdicts/AQ-02750_difficulty_2026-10-11_2048.txt, read 2026-10-11):

- Run 4 = q04 rev 3, "In band — Easy tier", Low 2/5, "You can submit now". Document check: Docs 4, 5 and 6
  each needed twice (62, 67, 70, the values worked out beforehand). Wrong low attempts: 119, 119, 100, all
  with the rule's letters counted.
- Low-model record on this hook: 0/5, 4/5, 3/5, 2/5. Nothing has split the medium model. The pass is at
  Easy, below the medium target the user set.
- Premise weakness found in the traces, missed at sketch time and through four revisions: the question
  states the receipts as fact while Doc 6 L43 and Doc 7 L41 give the real counts for the same orders (five,
  none). One low attempt used that record to drop a batch.
- q05 = q04 rev 3 with the Question as a supposition (60 words, gold 89, target easy). Alternative to q04,
  never a second submission. It needs its own run; q04's pass does not carry over.

Round 3 (2026-10-11), after the user confirmed q05 was quick-test too easy and that no Easy slot is left
("must be medium or high"):

- Closed: the comment-procedure hook (h11). Its measured range is Between levels to Too easy with one Easy
  pass; the medium model was 5 of 5 on the only run that reached it. q05 dropped; q04's Easy pass unusable.
- Considered and not sketched in this round, with the reason: travel-notice dates that the June order gives
  differently from the later orders (h6: May 15 against May 18, May 26 against May 27): the later account is
  in both D06 and D07, so neither is needed, and no August-only fact joins it naturally. Travel-notice levels
  by province with "the remainder of DRC" as a grouped item: D07's footnotes 13-15 give the whole history.
  Commenter requests and CDC's answers: each order's answers are complete in that order. Sections amended by
  DHS's proposal and EOIR's rule minus the withdrawn ones: D02's cross-references name DHS's three sections,
  and the one exclusion is guessable. Postmark against receipt (i10) and the rule's lapse (i05): two-lookup
  arithmetic of the kind the low model has solved here seven times.
- i11 (sketches/i11.md, hook h13, D02 + D03): "Which sections of 8 CFR parts 1003, 1208 and 1235 are amended
  by either EOIR's December 2024 interim rule on bars in fear reviews or the provisions of the 2020 Security
  Bars rule that survived the December 2025 partial withdrawal?" Gold: 8 CFR 1003.42, 1208.13, 1208.16,
  1208.31, 1208.33 and 1208.35. Eight candidates, six in. Built on the two shapes that have measured Medium
  elsewhere (a late member beside a statement that seems to exclude it; membership decided item by item
  across two documents). Screen: eligible, no failures; warnings only on section numbers first printed
  past character 20,000 (matters for the reasoning field at write-up). Quick test pending; sketch only.
- Stop rule: if i11 is quick-test too easy, no fourth round; release the bundle.
- 2026-10-11: no quick test left (user). i11 written up as q06 rev 0 with "List them in any order." added and the
  answer comma-separated; first measurement will be the difficulty check. Stop rule now reads: Too easy or Easy
  on q06 ends the bundle.

Quick test of q06 rev 1 (user chat, 2026-10-12, verbatim "too easy for quick test"; no panel or trace):

- The easier solver reached the six sections in one draw. Route unread. q06 dropped; hook h13 closed.
- Tally for the bundle: eleven versions in four families (order in force at an event, date gaps, comment
  procedures with a supposition form, list membership across two rulemakings). Quick tests: seven too
  easy, one survived (i08). Difficulty runs on that survivor: Between levels, Too easy, a document not
  needed, Easy. No result at Medium or above, and the medium model missed nothing in the one run that reached
  it.
- Stop rule reached. No fourth round: every further idea examined in round 3 failed on document necessity or
  was arithmetic of the kind the easier solver has already solved here. Recommendation to the user: release
  the bundle.
