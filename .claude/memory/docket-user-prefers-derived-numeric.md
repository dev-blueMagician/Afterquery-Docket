---
name: docket-user-prefers-derived-numeric
description: "The user asks for questions shaped like trial-02 q01 / trial-06 q02 (numeric answer derived over several steps through a carve-out or footnoted remainder, with a printed decoy) rather than list or filter questions"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 94731214-f590-446c-a9c8-79ae2d81eb16
  modified: 2026-10-06T13:59:07.671Z
---

On 2026-10-06 the user asked twice for this shape. On aq-docket-trial-02 they asked for "another like" q01 with a decimal answer. On aq-docket-trial-05, after a list question (plaintiffs who sued a judge who ruled against them) was handed over, they asked: "can you make QA like Trial 2's q01 or Trial 6's q02". Both models are numeric answers that no document prints:
- trial-02 q01: +7.85%, a percentage change of carved-out segment sales, nine dependent steps; the decoy is the whole segment's printed 7.0%.
- trial-06 q02: 9.8%, a state identified by a detail in one report, plus a footnoted remainder in another.

Neither had a platform result when the user named them (both were pending, and trial-06 q02 had been dropped locally).

Results so far (user reports, 2026-10-06, no tier lines): trial-02 q01 "passed in pipeline" and was accepted; trial-04 q03, built in this shape at the user's request (a set from one edition rebuilt in another, a footnoted $27.8 million remainder under the printed $986.8 million), "passed in pipeline of Docket". The user then asked for "another one" on the same bundle.

**Why:** not stated by the user. Likely reason (inferred): on unrelated-document bundles, list and filter questions kept reviewing Easy or Too easy, and trial-05's two quick-tested list drafts came back "Too easy — solver got it". So the derived-numeric shape looks like the better route to Medium.

**How to apply:** when sketching, look first for derived-numeric designs of this shape. Hand over a list or filter question only when no fair numeric design exists, and say so plainly. Fairness rules still win: one defensible answer, no outside law, and the removal and entity-coincidence checks. See [[docket-local-solver-calibration]] and [[docket-redesign-v2]].

aq-01322 (2026-10-06): offered an edition-trap lookup (q01, reviewed Medium-leaning) and two derived
numerics reviewed Easy-leaning, the user ran the difficulty check first on the derived carve-out q03
(answer 5.2%): "Too easy", Low 4/5. Derived shape alone did not lift a signposted carve-out.

aq-01278 (2026-10-06): q02, a derived Q2 growth rate rebuilt on the basis an earlier release's stated figure
implies (agriculture inside "commercial"), with the later release's narrower printed -2.3% as the answer-shaped
decoy, passed the difficulty check at Medium (Low 0/5, Medium 1/5). Derived shape plus an untied scope decoy
worked where a signposted carve-out did not (aq-01322 q03).
