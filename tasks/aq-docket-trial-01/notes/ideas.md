# aq-docket-trial-01 - lean candidate sketches

Current target: easy (user, 2026-10-06, after both write-ups failed the quick test: "actually in
trial, it's okay if accept in even Low tier"); originally medium ("at least Medium", one attempt).
Measured platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Design basis (memory, measured): Medium = Low 0/5 then Medium 1-3/5 (aq-00964 q01). The low model
takes the salient, same-label value; medium/high resolve one clean trap most of the time (aq-00745
q08: medium/high passed the closing-day trap 9/10). Ambiguous wording sends every tier wrong (Too
hard). So each sketch carries one trap whose correct value needs reasoning that label matching
does not supply, with wording pinned for one defensible answer. Bundle limits: six unrelated
papers, so the cross-document step is arithmetic over analogous quantities.

Round 1 (2026-10-06, origin claude; all five passed the mechanical screen, no FAIL/WARN):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1: count never printed; runtime label + time per iteration | Leukemia benchmark run's iterations minus battery full-model iterations. Gold 9 (65/5.91 = 10.998 -> 11; 11 - 2) | D01 413 "Sparse DPMM: 65", 431 "Runtime (in seconds)", 403 "∼ 5.91 seconds per iteration"; D04 379/385 "converged after just 2-iterations" | Calculate across documents; unit normalization (seconds to iterations). Decoys: D04 "roughly 3-5 iterations" (351) -> 6-8; D01 slice sampler "1000 MCMC iterations" (263) -> 998 | "∼" approximate (only integer 11 within rounding); several random initialisations possible (total unchanged) | screen pass; lead; promote to q01 |
| i02 | h2: appendix-only ranking cut vs main-text "979 highly variable genes" | Autoimmune MAD cut share minus brain HVG share. Gold 22.1 pp (31.0206 - 8.9451) | D02 431 (9,671), 723 (top 3000 by MAD); D05 783 (33,538; top 3,000 HVGs) | Bury one item late; calculate across documents; state the rounding. Decoy 979 -> 1.2 pp | 979 also "pre-selected genes" (577): wording must name the ranking cut | screen pass; quick-test probe |
| i03 | h3: full-model λ only in Fig. 7 caption; Results text gives cell 8's 0.00067 first | λ at convergence (full model) and clusters of BIC-selected autoimmune model. Gold 0.0002 and 9 clusters | D04 121 (BIC tunes λ), 385; D02 447 | Same label, different scope; two parallel asks. Decoys 0.00067, 0.00048; WGCNA K = 4 | parallel lookups, weak combination | screen pass; quick-test probe |
| i04 | h4: benchmark used empirical Bayes = strong prior run; headline highlights weaker-prior extra cluster | Clusters: leukemia benchmark configuration and autoimmune BIC model. Gold 3 and 9 | D01 403, 273, 297; D02 447 | Right configuration. Decoys 4 (weaker prior; "instead of 28.9076 ... Kpost = 4"), WGCNA 4 | benchmark count figure-only (Fig. 5b); inferred from Sec. 3.2 | screen pass; quick-test probe |
| i05 | definition applied across papers: spatial paper's "observations" are rows = genes | Observations, brain main analysis minus autoimmune model. Gold 13,853 (14,638 - 785) | D05 29, 31, 783; D02 175, 431 | Entity resolution; calculate across documents. Decoys: spots 2,807; full genes 32,753; HVG 2,215 | "as each paper defines them" signposts; D02 has no formal definition | screen pass; quick-test probe |

Round 1b (same day): i04's anchor lands next to its right value (label matching solves it), so it was
re-anchored as i06 on the sensitivity check, whose own sentence carries the decoy; i02 was reworded
as i07 so the natural search ("screen") lands on the paragraph ending "979 highly variable genes".

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i06 | h4 re-anchored: "the prior hyper-parameters that its sensitivity check replaced" | Autoimmune main K minus leukemia Kpost under the replaced prior. Gold 6 (9 - 3) | D01 297 ("instead of 28.9076 ... Kpost = 4"), 273 (strong/EB, Kpost = 3); D02 447 | Right configuration; calculate across documents. Decoys 5 (sensitivity run), 1 (WGCNA) | "replaced" must be read as the swapped-out setting; link 28.9076 -> Kpost 3 is inferred across sentences | screen pass; promoted to q02 |
| i07 | h2 re-anchored on "screen" | Shares passing the MAD screen and kept in the HVG analysis. Gold 31.0% and 8.9% | D02 431, 723; D05 783 | Bury one item late; state the rounding. Decoy 10.1% (979) | 979 also "pre-selected genes" (577) | screen pass; quick-test probe |

Sketch-stage local screens (raw: runs/sketch-round1/returns.md; preliminary, not final records):
fresh Opus blind solves matched every sketch with high confidence and named every planned decoy
(i02 22.1; i03 0.0002 and 9; i04 3, 9; i05 13,853; i06 6; i07 31.0%, 8.9%). Closed-book screens:
i02 unknown, i03 unknown, i04 "4 and 3" (guess), i05 unknown, i06 "1" (guess), i07 "25.0%; 10.0%"
(guess): all miss. The local solver is the fairness check; it does not measure the platform tiers.

Round 2 (after the q01 review predicted Easy: "none of these wrong values carries the asked label
and is excluded only by a deciding fact"):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i08 | figure crossing documents (3,000) as a bridge into the brain study's three analyses | Sill of the brain analysis with as many genes as passed the autoimmune screen. Gold 100 | D02 435, 723; D05 783, 815 | Who belongs where; bury one item late. Decoys 979 (no match) and 500 (two of three analyses) | removal: guessable without D02 | local match; closed-book unknown; removal probe without D02 guessed 100 at about 0.8: dropped |
| i09 | i05 without the definitional signpost: "observations" = rows = genes in the spatial paper | Observations, brain main analysis minus autoimmune model. Gold 13,853 | D05 29, 31, 783; D02 47, 175, 431 | Entity resolution; calculate across documents. Ordinary-usage decoy: spots 2,807 | a model check might call "observations" ambiguous; defended by the paper's explicit definition and disclaimer | two local matches (high), closed-book unknown; promoted to q03 draft |

Removal probes (runs/sketch-round1/removal-probes.md): q01 without D04 not answerable (guess 5,
p 0.10, gold 9); q02 without D01 guessed the gold 6 at p 0.3 (three labelled subtypes); i08 without
D02 guessed the gold 100 at p 0.8; i07 without D05 guessed 6.0% (gold 8.9%, listed as an
alternative), p 0.10.

Platform quick tests (2026-10-06, user screenshot; one low-model answer each): q03 (i09) "Too easy —
solver got it" (14,638 - 785); q01 (i01) "Too easy — solver got it" (65 / 5.91 about 11, minus 2).
Coach (notes/feedback-coach-2026-10-06.md): both are "two lookups and one subtraction"; the guide's
"Calculate across documents" lever: "One lookup plus one operation is usually solved"; the wording
picked each figure, so no decoy forced a second look; q01 also rests on approximate inputs (chart
65, "∼ 5.91") and Doc 4's "roughly 3-5 iterations". Suggested: scatter the pieces, restated
figures, three or more dependent steps.

Round 3 (target easy; origin claude; all four passed the mechanical screen, no FAIL/WARN):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i10 | parallel gene trimming with a threshold of 20; module-size rule acts on the appendix-only 3000 | Spot rule's removals minus module-size rule's removals. Gold 16,879 (18,900 - 2,021) | D05 783 (33,538; at least 20 spots; 14,638); D02 723-725 (3000 by MAD; fewer than 20 genes removed; 979) | Calculate across documents (three subtractions); bury one item late. Decoys 10,208 (9,671 base), 18,896 (WGCNA grey 4), 28,517 (HVG) | 5.5 "19 gene modules from 979 genes"; overview prints 3000 and 979 | screen pass; blind solve 16,879 (high, named the 18,896 and 10,208 readings); closed-book unknown; quick-test |
| i11 | loadings oriented differently: spots x factors (brain) vs genes x factors (autoimmune) | Loading-matrix entries, brain tissue model minus autoimmune selected model. Gold 17,312 (25,144 - 7,832) | D05 29, 31, 470, 783, 815; D02 105, 439, 447 | Entity resolution; unit normalization; calculate across documents. Decoys 94,634 (genes as rows), 14,512 (training spots), 24,013 (p + Gq) | "entries" vs free parameters; Doc 5 overview prints "m spatial locations" | screen pass; blind solve 17,312 (high, rejected 14,512, 94,634, 24,992 and p + Gq); closed-book unknown; quick-test |
| i12 | the one work cited by two papers: chapters of one 2011 book | Pages of the later-starting range minus the earlier. Gold 3 (27 - 24; exclusive also 3) | D01 507 (pp. 213-239); D02 679 (pp. 189-212) | Who belongs where (citation); scatter the pieces. Decoy: D02 Handbook chapter 2011 pp. 139-172 | trivia risk; closed-book recall of page ranges | screen pass; blind solve 3 (high, by search in about a minute); closed-book recalled the book, "Frühwirth-Schnatter, pp. 213–239" and "McLachlan et al., pp. 189–212, would give 3": dropped (closed-book) |
| i13 | two BIC outcomes beside same-topic wrong values | Full-model λ at convergence and exact ∆BIC. Gold 0.0002 and 248,685 | D04 385 (121); D02 585, 587 | Same label, different scope (λ 0.00067 in text); exact table vs rounded prose (≈ 250,000) | two parallel asks joined only by BIC | screen pass; blind solve 0.0002 and 248,685 (high); closed-book unknown; superseded by i14 (the words "exactly" and "full repeated-measurements model" selected each figure, the Coach's objection) |
| i14 | i13 reworded: "when fitting all retained cells together"; "by how much" | Same gold 0.0002 and 248,685 | as i13 | as i13 | "all retained cells" must not be read as the level-1 σ² sentence | screen pass; blind solve 0.0002 and 248,685 (high), but listed the prose ≈ 250,000 as a second reading of "by how much": superseded by i15 |
| i15 | i14's λ wording with i13's "by exactly how much" (one clear answer) | Same gold 0.0002 and 248,685 | as i13 | as i13 | two parallel asks | screen pass; halves solved in i13/i14; quick-test |

Round 4 (user, 2026-10-06: "can you make QA like Trial 2's q01 or Trial 6's q02"). Those two share
a percentage at a stated precision built from figures no passage prints, where an exclusion or a
remainder stated in a note, footnote or appendix changes the base, with a wrong-scope figure in
reach. The bundle has no shared entity for a trial-06-style bridge, so the cross-document part
stays arithmetic over a real parallel (both transcriptomic papers trim genes with a threshold of 20).

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i16 | i10 as shares: the autoimmune step's base (3000) is a remainder printed only in Appendix A | Brain filter's kept share minus the autoimmune module removal's kept share, one decimal. Gold 11.0 pp (43.646 - 32.633) | D02 723-725 (3000, 979; K = 9, q = 8); D05 783 (33,538; 14,638) | Scatter the pieces; calculate across documents. Wrong routes 33.5 (9,671 base), 12.6 (MAD step), -55.9 (WGCNA), -23.7 (HVG) | two decimals split 11.01/11.02, so one decimal; overview prints 3000 and 979 | screen pass; promoted to q04 (A/B 11.0 high, audit clear, closed-book unknown, probes 10.0 and 22.4; review ready, Too easy about 65%: "genes each step started from" signposts the base and "exceed" disarms the negative routes) |
| i17 | q04 without the signposts: both shares against all genes with expression data, so the module step's discards (3000 - 979) must be separated from the MAD ranking's (match, then exclude) | Brain discarded share divided by autoimmune module-step discarded share, two decimals. Gold 2.70 (56.354 / 20.898) | D02 431 (9,671), 723-725; D05 783 | Match, then exclude; calculate across documents. Wrong routes 0.63 (all 8,692 removals), 0.82 (MAD step), 0.84 (step-local base), 2.09 (brain kept share) | percentage-point difference rejected (35.46 exact, 35.45 from two-decimal shares, 35.4 under half-even); ratio 2.6967 at two decimals sat 0.0017 above 2.695 (whole-percent shares give 2.67), so rev 1 asks one decimal, stable at 2.7 on every reasonable rounding path | written up as q05; rev 0 (2.70) passed A/B, audit, closed-book and probes but sat 0.0017 above a rounding line; rev 1 at one decimal (2.7) passed A/B, audit, closed-book and probes; review running |

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
