---
name: docket-user-prefers-derived-numeric
description: "The user prefers a precise numerical gold derived across documents when sources support it; short arithmetic is eligible, and printed inputs must be distinguished from computed values"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 94731214-f590-446c-a9c8-79ae2d81eb16
  modified: 2026-10-08
---

## Current user instruction — 2026-10-08

Prefer questions with a precise numerical gold derived across documents, such as 4.96%, when
the sources support that precision. This is an explicit answer-shape preference. The earlier
inference about aiming for Medium, and the recipe of several steps plus a printed decoy, are
historical rather than requirements. Ordinary short cross-document arithmetic remains eligible;
do not add operations, force a carve-out or invent precision to match an example. Decoys remain
required for which-items questions; apply author checks to other claimed levers without making
a decoy mandatory for every numerical ask.

Each marked necessary document must supply an indispensable input or condition after substitute
searches; a precise answer alone does not establish that dependency. Specify units and final
rounding. In Step-by-Step Reasoning, label printed facts with Doc N, location, value/unit and
scope, then label calculations as derived from those facts or earlier steps. A computed 50 from
5 × 10 is a calculation, not a claim that a document prints 50. Round the final answer once;
see [[docket-form-automated-checks]] for the source-fact/calculation format.

The user examples and historical results below do not guarantee a platform pass or predict a
tier. The current Easy-minimum target and lean platform-validation workflow still govern; this
preference adds no mandatory model diagnostics.

## Historical observations and guidance

- 2026-10-09 (aq-02157 q04): the preferred shape passed at the target: one derived pounds figure across two
  documents (the response's printed £8.46 minus the IA table's floor, £347.86 per 1,000 converted to £6.9572 a pack),
  one decimal stated, gold £1.5: "In band — Medium tier" (Low 0/5, Medium 2/5). See [[docket-local-solver-calibration]].
- 2026-10-09 (aq-02486 q01 rev 2): the preferred shape passed again at the target: the total a news reporter pays two
  agencies for 216 photocopies each under their FOIA proposals, $11.60 (Doc 5 rate and free pages; Doc 7 rate, free pages
  and "$25.00 or less, no fee" rule): "In band — Medium tier" (Low 0/5, Medium 2/5). Its first form, a difference of the
  two charges, was Easy because the missed-rule route gave the negated gold and the grader ignored the sign.
- 2026-10-10 (aq-02564 q02 rev 1): the preferred shape passed a third time at the target: a host's total monthly bill
  for two exchanges' feeds, $2,375, built from two parallel SEC notices (Doc 5 EDGX: 5,000 x 0.10 + 750 + 750; Doc 6
  BYX: 250 + 5,000 x 0.025): "In band — Medium tier" (Low 0/5, Medium 3/5), submitted at Medium. Its one-inference
  form ($1,625) was Easy, Low 2/5; the pass came from four independent steps in one scenario, each wrong route with its
  own total ($875, $1,750, $2,125, $2,387.50). See [[docket-local-solver-calibration]] (recipe 3).

On 2026-10-06 the user asked twice for this shape. On aq-docket-trial-02 they asked for "another like" q01 with a decimal answer. On aq-docket-trial-05, after a list question (plaintiffs who sued a judge who ruled against them) was handed over, they asked: "can you make QA like Trial 2's q01 or Trial 6's q02". Both models are numeric answers that no document prints:
- trial-02 q01: +7.85%, a percentage change of carved-out segment sales, nine dependent steps; the decoy is the whole segment's printed 7.0%.
- trial-06 q02: 9.8%, a state identified by a detail in one report, plus a footnoted remainder in another.

Neither had a platform result when the user named them (both were pending, and trial-06 q02 had been dropped locally).

Results so far (user reports, 2026-10-06, no tier lines): trial-02 q01 "passed in pipeline" and was accepted; trial-04 q03, built in this shape at the user's request (a set from one edition rebuilt in another, a footnoted $27.8 million remainder under the printed $986.8 million), "passed in pipeline of Docket". The user then asked for "another one" on the same bundle.

**Historical inference (superseded above):** the reason was not stated by the user. Likely reason (inferred): on unrelated-document bundles, list and filter questions kept reviewing Easy or Too easy, and trial-05's two quick-tested list drafts came back "Too easy — solver got it". So the derived-numeric shape looked like the better route to Medium.

**Historical application advice (superseded above):** when sketching, look first for derived-numeric designs of this shape. Hand over a list or filter question only when no fair numeric design exists, and say so plainly. Fairness rules still win: one defensible answer, no outside law, and the removal and entity-coincidence checks. See [[docket-local-solver-calibration]] and [[docket-redesign-v2]].

aq-01322 (2026-10-06): offered an edition-trap lookup (q01, reviewed Medium-leaning) and two derived
numerics reviewed Easy-leaning, the user ran the difficulty check first on the derived carve-out q03
(answer 5.2%): "Too easy", Low 4/5. Derived shape alone did not lift a signposted carve-out.

aq-01278 (2026-10-06): q02, a derived Q2 growth rate rebuilt on the basis an earlier release's stated figure
implies (agriculture inside "commercial"), with the later release's narrower printed -2.3% as the answer-shaped
decoy, passed the difficulty check at Medium (Low 0/5, Medium 1/5). Derived shape plus an untied scope decoy
worked where a signposted carve-out did not (aq-01322 q03).
