# Independent review, q02 rev 0 (2026-10-08)

Role: question-review (fresh context; frozen fields, corpus, raw returns and floor output).
tested_sha256: d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07

Raw return (verbatim):

q02 (rev 0; tested_sha256: d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07)

**Records.** All the fingerprint-bound checks hold. The only fix needed is in the Targeted failure modes, which sit outside the fingerprint, so no re-test follows from it.
- `docket_agent.py report` recomputes the same hash from the current file: no mechanical failures, source_gaps [] (4f53cda1…).
- snapshot.json fields match q02.md.
- Every record carries rev 0 and this hash, and so does every raw return: A, B, closed-book, audit and both probes.
- The probe packets in runs\q02-r0-alt-m6 are sha256-identical copies of the originals, minus Doc 7 (docs/_10) in solver-1 and minus Doc 6 (docs/_8) in solver-2. Their ids are renumbered.
- The question text is identical in all six packets.
- Floor: 0 FAIL, 2 WARN. The origin WARN is accurate; the sibling WARN is intended.
- No platform record exists.

**gold_verified: yes.** I recomputed it with a Decimal script from these passages:
- Doc 7 l.63-64: the $100 automatic payment goes to the No Bankruptcy Group only.
- Doc 7 l.66: "Approximately $2,882,000.00"; each payment is own points over all claimants' points.
- Doc 7 l.73: 3 points vs 1.
- Doc 7 footnotes 2-3: both groups are defined by the April 22, 2025 report.
- Doc 6 l.47: 920 eliminated, list of 57,233.
- Doc 6 l.49: 20,891, "PACER or Thomson Reuters".
- Doc 6 l.61: 36,317.

The calculation is 3×20,891 + 36,317 = 98,990, then 2,882,000 / 98,990 = 29.11405, which is 29.1 under half-up, half-even and half-down.

Every other route from stated figures also gives 29.1:

| Route | Result |
| --- | --- |
| Aged = 57,233 − 20,891 | 29.1067 |
| No Bankruptcy = 57,233 − 36,317 | 29.0920 |
| Two test records removed | 29.1146 / 29.1158 |
| Fund residual using 20,891 × $100 (2,882,900) | 29.1231 |

Margins: the answer holds for any reserve from 2,875,660 to 2,885,558, or any point total from 98,868 to 99,208. That allows the No Bankruptcy count to move −40/+72 or the Aged count −122/+218.

Wrong routes, all off the gold:

| Route | Result |
| --- | --- |
| March split | 28.096 |
| 920 removed from the no-record group | 28.9 |
| 920 removed from the aged group | 28.4 |
| March shares scaled to 57,233 (not in the lever checks) | 28.5 |
| April no-record + March aged (not in the lever checks) | 29.2 |
| March no-record + April aged (not in the lever checks) | 28.0 |
| 21,000 implied by the reserve, with 36,317 | 29.018 |
| 21,000 implied by the reserve, with 36,233 | 29.043 |
| Rebuilt reserve 2,872,000 | 29.013 |
| Head count | 50.4 |
| 3-point claimant | 87.3 |
| Printed estimate | $350 |

**outcome: A: match; B: match.** Both answered 29.1 with high confidence from Doc 7 and Doc 6. Both rejected the March, reserve-implied and rebuilt routes on document grounds. Their context held git-status file names only, so neither is contaminated. Neither mentions $350; only the auditor lists it.

**closed-book: misses.** It answered "unknown" after guessing the Ramirez case. The source is a July 2026 ruling.

**necessity**
- Doc 7 (D03) is the bundle's only "$" text: the reserve, the automatic payment, the points, the formula and the April-report definitions.
  - Clark in Doc 4 has no money terms and is never "preliminarily approved".
  - Probe without Doc 7: unforced "not answerable"; forced $137.6 (p 0.005).
- Doc 6 (D07) alone holds 20,891 and 36,317.
  - Doc 5 only lists the April report as an exhibit.
  - Doc 4's June 2022 ratios give $33.1 or $33.7.
  - Doc 7's ~21,000 would need an Aged count of 35,868-36,208, and no remaining figure supplies one.
  - Probe without Doc 6: unforced "not answerable"; forced $33.1 (p 0.02).
- No smaller source set exists.

**shortcut: clear.** The verified shortest route is Doc 7 l.63-75 plus footnotes 2-3, then Doc 6 l.47/49/61, then one division.
- No passage prints a per-point or full-participation value.
- The capture overview (l.70) gives Doc 6's March split plus 57,233. For Doc 7 (l.77) it lists the fund pieces but not $2,882,000 or $350. That invites the residual rebuild, which "the court's figure" rules out.

**source_assessment:** none needed. The capture is complete: intake shows all seven documents with matches_capture true and 0 gap characters.

**difficulty: easy, marginal toward medium** (local suitability for the Medium target, not a measured tier).
- The March trap is tied: the supersession is in the next sentences, and the governing edition is the latest.
- The $350 is excluded by the premise. The calibration memo rates decoys the wording sidesteps as weak.

**verdict: revise.** The scope is narrow: one Targeted-failure-modes fix (finding 1). No new solves, probes or audit are needed. Finding 3 is a run decision for you, not a wording fix.

**failure_modes**
- **Mode 1 ($350; Look-alike measure / Misapplies a rule or premise; 208 words).**
  - Real: Doc 7 l.75 and l.212 (page 17) print it.
  - Not strictly ruled out by the wording, since the question never mentions estimates. But the premise disarms it: 36,317 × $350 = $12,710,950, 4.4 times the reserve, implying about 8.3% participation.
  - Unobserved locally.
  - "Figure that must be computed" fits at least as well as Look-alike measure. The cause fits.
  - Overclaim: the quoted "from typical claims rates data for similar cases" belongs to the $1,000 sentence. The $350 sentence carries only "(Id.)" and the later "these estimates based on historical data".
- **Mode 2 (March split; Superseded date or version / Uses the wrong period or date; 188 words).**
  - Real, not ruled out by the wording, and 28.1 recomputes. The labels fit.
  - "Later gives the April split" is an inference, but it is supported by "PACER or Thomson Reuters" and footnote 5's "final class list".
  - 58,153 − 920 = 57,233 ✓.
- Each trap is used once.
- Necessary documents are left blank, so both default to Answer component, which matches how each is used.

**Pinning and the rule checks (Q1-Q12, Q14, Q15)**
- Q1-Q12 and Q14 pass.
- "Taking the court's figure…": one reading. Only Doc 7 l.66 sets money aside for valid claims, and the pin excludes the residual 2,872,000 (29.0).
- "Each claimant who gets no automatic payment": one reading. No Bankruptcy members are paid "without the need to submit a claim", so only the Aged group qualifies, and "of it" confines the answer to the reserve.
- "Preliminarily approved settlement" fits only Brooks.
- Rule 10: the question asks about the world, with no "group of/set of" trigger. It is 47 words: below the 60-word warning, slightly over the 20-45 aim.
- The evidence quotes are verbatim, and step numbers follow the form's rule.

**Platform risks**
- "One defensible answer": about 10% that both form solvers take 28.1. Under 2% each for $350 and for 29.0.
- "Answer matches a stated figure" may fire on $350, $100.00 or $2,882,000.00. It is advisory, and the question states the computation.
- "Answer not supported": about 4%.
- Document check: under 5%.
- "Not a duplicate": q01 and q02 have a 0.652 token ratio, so save only one.

**Tier estimate** (my judgment, not a measurement)

| Outcome | Estimate |
| --- | --- |
| Too easy | ~15% |
| Easy | ~45% |
| Medium | ~15% |
| Between levels | ~15% |
| High | ~3% |
| Too hard / not supported | ~7% |

The usable odds are about 18% (range 12-22%), against q01's 15-20%. The $350 converts a few would-be low-model solves into misses. Most of that gain likely lands in "Between levels": medium/high models cleared a comparable tied trap 9/10 (aq-00745 q08).

**If only one can be submitted:** q02, narrowly. The difference is a few points, below what local estimates can resolve. It adds a second printed attractor at no fairness cost, but slightly more advisory exposure. q01 rev 1 is the equally defensible lower-exposure choice.

**findings**
1. **Q15, mode 1 "Where the trap sits":** the quote is attributed to the wrong sentence (Doc 7 l.75). Re-attribute it to the passage that actually covers $350, then re-run the floor only.
2. **Q15, mode 1:** the mode is weak and unobserved (0 of 3 runs produced it). Don't describe it as measured. The label change is optional.
3. **D3/D4/D7:** the trap is tied and lands on the endpoint edition, so the question is Easy-leaning. I found no fair wording change that raises the Medium odds.
4. **Set:** q02 and q03 share the March/April trap and the 20,891 input. Avoid submitting both.
5. Origin WARN accurate. Platform measurement pending.

Files:
- D:\Agents\Docket\tasks\aq-01541\questions\q02.md
- D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\
- D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-alt-m6\
- D:\Agents\Docket\AQ-01541_2026-10-07_0358.txt
