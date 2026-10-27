# aq-03423 - lean candidate sketches

Current target: medium, Hard welcome (user, 2026-10-12: "there is no slot for Easy Tier for this bundle, we
should target medium and high"). Hooks are in notes/hooks.md; facts and checks are in the linked sketches.

## Round 1 (2026-10-12): unproductive

| ID | Sketch | Hook | Result |
| --- | --- | --- | --- |
| i01 -> q01 | [sketches/i01.md](sketches/i01.md) | h1: two largest operators' fixed broadband share, 71% (Doc 8 + Doc 7), beside Chorus's printed 80% | quick test "too easy" (user: "both too easy for quick test"; no panel or trace, route unread); dropped |
| i02 -> q02 | [sketches/i02.md](sketches/i02.md) | h2: 10GB plan against 25GB plan per included gigabyte over a first year, $1.60 more (Doc 1 + Doc 7) | quick test "too easy" (same message); dropped |
| i03 | [sketches/i03.md](sketches/i03.md) | h3: capital per planned RCG site, $433,000 | no result reported; a plain three-document retrieval, not pursued |
| i04 | [sketches/i04.md](sketches/i04.md) | h4: termination-rate cuts, smaller by 0.4 points | no result reported; not pursued |
| i05 | [sketches/i05.md](sketches/i05.md) | h5: equal 2100MHz split, Spark 156.7 MHz | no result reported; the rule is named in the question, not pursued |

What round 1 shows, without a trace: the easier solver was not held by a printed look-alike figure whose
source the question rules out (q01), nor by a four-step calculation with a time-limited offer and a
neighbouring operator's price (q02). Both were written up in full before the screen; round 2 is sketches only.

## Round 2 (2026-10-12): one survivor

Different dependencies from round 1: an input no document prints that has to be derived before the obvious
calculation and that the wording does not ask for (i06, i07), a claim whose sign reverses against another
document's table (i09), a ranking split across two documents (i10), and a membership count (i08).

| ID | Sketch | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i06 | [sketches/i06.md](sketches/i06.md) | h11: connections added in 2017 against the 2016 MVNO base, 13.5 times (Doc 1 + Doc 5) | 14.2 applies 5.1% to the 2017 level, though it is growth "on the previous year"; 14.8 uses Vocus's own 21,000. Each document holds one input only | quick test "too easy" (user: "only last one survived"; no panel, route unread); dropped |
| i07 | [sketches/i07.md](sketches/i07.md) | h11: MVNO subscribers as a share of 2016 connections, 0.38% (Doc 1 + Doc 5) | 0.36% uses the 2017 connection count for a 2016 share | quick test "too easy" (same message); dropped; hook h11 retired |
| i08 | [sketches/i08.md](sketches/i08.md) | h6: questions none of Vocus, WISPA NZ and Speedchecker set out and answer, 11, lowest Q8 (Doc 9 + Doc 10 + Doc 11) | Read by printed question numbers; read by substance the count changes. About the papers, not the market | survived the quick test (same message, the last of the five); promoted to q03 with "set out to answer" in place of "set out and answer" |
| i09 | [sketches/i09.md](sketches/i09.md) | h12: 2degrees' $129 plan against the benchmark row, 130% dearer than Australia and 35% cheaper than the OECD average (Doc 1 + Doc 7) | Printed 17% and -67% belong to the benchmarked 65 | quick test "too easy" (same message); dropped |
| i10 | [sketches/i10.md](sketches/i10.md) | h13: mobile second on perceived competitiveness, fourth on switching (Doc 7 + Doc 1) | Same five sectors in both documents | quick test "too easy" (same message); dropped |

All five pass the mechanical sketch screen (quotes found, two or more documents). That screen proves neither
uniqueness nor difficulty.

Rejected in round 2 without a sketch: the $534 exit charge in Doc 7 fn 8, which equals half of twelve payments
on Telstra's A$89 plan in Doc 1 (the footnote can be read as two separate examples, so applying its 50% rule to
that plan is unsupported); 2degrees' list of bands where it is at a disadvantage against Doc 1's holdings (the
Commission gives no 2300MHz or 2600MHz figure for 2degrees or Vodafone); the 250 towers 2degrees co-locates on
against RBI1's 154 new sites (a bound the documents never draw); Covec's model re-run with another document's
input (a constructed scenario); a handset bought and unlocked at once (constructed, and each rule is one plain
sentence).

## After round 2: q03 measured

q03 (from i08) drew "Between levels" on its first difficulty run (2026-10-12, Low 0/5 · Medium 5/5; record and
attempt routes in questions/q03.md). All five low attempts gave the lowest question (Q8) and a wrong count (13, 3,
5, 5, 13) after mixing up which document carried which headings; all five medium attempts listed the 47
questions and ticked each respondent's printed numbers. No attempt judged by the substance of an answer. The
lists share the Commission's numbers, so nothing is left for a careful solver to infer; no wording repair
addresses that, and the second conditions examined either state a rule a careful solver applies or shrink the
enumeration that stopped the low solver. q03 dropped, hook h6 retired.

## Round 3 (2026-10-12): one sketch, promoted

| ID | Sketch | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i11 | [sketches/i11.md](sketches/i11.md) | h14: submitters that had become an MVNO or tried to: Trustpower, Vocus, WISPA NZ (Doc 7 + Doc 10); Trustpower's attempt is reported only in 2degrees' response | Own-paper reading (Vocus, WISPA NZ) fails the clause on attempts only another submitter reports; Doc 1 Table 3's MVNOs fail "made submissions". Doc 7 alone carries Trustpower, Doc 10 alone WISPA NZ | promoted to q04. Rev 0 (rule named as a kind) quick-test "too easy" (user, 2026-10-12; no panel). Rev 1, the one focused repair, states the rule as pooled evidence ("Judging by all the submissions ... together"): quick-test "too easy", as was the no-rule wording (user: "both are too easy"). q04 dropped |

Why this hook now: rounds 1 and 2 looked for numeric joins and label counts. The sibling result was recorded in
workspace memory during this session (recipe 6), and this bundle has the same structure in exactly one place. It
is the only relationship found here where a member has to be inferred from another party's paper. Three rounds
are now used; if q04 fails for a reason a single repair cannot address, the supported conclusion is that the
bundle has no further candidate.

q04 repair ladder, taken from the sibling bundle's three measured states (rule named as a kind; pooled-evidence phrase; no rule):
rev 0 used the first and was too easy here. Rev 1 uses the second. The third (no rule) is the same repair in its other form and
can share rev 1's quick-test batch; on the sibling bundle it was blocked by the form's "One defensible answer" check, so it is
the fallback, not the lead. If both are too easy, hook h14 is spent: every relationship found in this bundle has then been
measured (six calculations and this list too easy at the quick test, one count between levels), and the supported
recommendation is to release the bundle.

## Outcome (2026-10-12): no candidate left, release recommended

Three sketch rounds and one difficulty run are used. Every cross-document relationship found has been measured:

| Hook | Mechanism | Measured result |
| --- | --- | --- |
| h1 (q01) | printed look-alike figure, source condition, subtraction | quick test too easy |
| h2 (q02) | time-limited offer priced over a year, neighbouring operator's price | quick test too easy |
| h11 (i06, i07) | base backed out of a growth rate, as a ratio and as a share | quick test too easy, both |
| h12 (i09) | sign that reverses against a benchmark row | quick test too easy |
| h13 (i10) | ranking split across two documents | quick test too easy |
| h6 (i08, q03) | count over three lists with shared printed numbers | quick test survived; difficulty Between levels, Low 0/5 · Medium 5/5 |
| h14 (q04) | list member reported only in another submitter's paper, three wordings | quick test too easy, all three |

Not tested and not recommended: h3-h5 (plain retrieval or a rule named in the question), and the relationships
rejected in hooks.md (h7-h10) and in the round 2 notes above, each for a stated fairness reason.

Unresolved avenues, stated so that nobody mistakes them for candidates: (1) counts that need the bodies of
2degrees' 47 answers read for cross-references or shared answers: they are about the layout of one document and
a careful solver reads them as it read q03's lists; (2) matching the 2017 submitters' requested scope to the
Commission's framework or questions by content: no shared wording, so membership is a judgment; (3) re-running
Covec's fourth-network model with another document's input: a scenario the documents do not set up. None gives
one defensible answer with a step a careful solver must infer.

What the bundle lacks is a rule with an exception, an eligibility test, or two editions of one table: every
measured Medium or Hard result in this workspace rests on one of those.
