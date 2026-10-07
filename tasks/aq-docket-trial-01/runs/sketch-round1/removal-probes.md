# Removal probes (2026-10-06)

Each probe is a fresh blind-solver agent given a prepared packet (same corpus bytes), the verbatim
question and an instruction to treat one document as absent and give a forced guess with its
probability. It approximates the platform's own check that re-solves without each marked document.
Returns are abridged to the answer and the stated basis; full text is in the task notifications of
this session (copied below verbatim where shown).

## q01 without D04 (battery paper removed)

answer: Not answerable from D01, D02, D03, D05 and D06. The leukemia benchmark took about 11 iterations (worked out from the paper, not printed), so the answer is 11 − X. X is the number of iterations the battery ageing study's regularised algorithm needed for its full repeated-measurements model. None of the five documents covers that study, so X is unknown. Forced guess: **5 more iterations** (assuming X = 6), probability about 0.10.

Basis of the guess (verbatim): "the question assumes the benchmark took more iterations, so X is below 11. A regularised Newton- or scoring-type fit typically converges in about 4–8 iterations. Picking X = 6 gives 11 − 6 = 5. That is a guess, not evidence, and the probability is about 0.10."

Result: gold 9 not reached. D04 needed in practice.

## q02 without D01 (leukemia paper removed)

answer: not answerable from D02–D06. The autoimmune study's main BIC-selected model has 9 clusters. No remaining document gives the leukemia study's cluster count under its original prior hyper-parameters, so the difference (9 − x) can't be computed. Forced guess: 6, which assumes the leukemia model found 3 clusters. Probability the guess is right: about 0.3.

Prior stated (verbatim): "Clustering of leukemia expression data often recovers about 3 groups (for example ALL-B, ALL-T and AML) or 2 (ALL vs AML). My rough prior on x: 3 about 0.35 (answer 6); 2 about 0.25 (7); 4 about 0.2 (5); 5 or more about 0.15 (4 or fewer). I commit to 6, at about 0.3."

Result: forced guess equals gold 6. D01's contribution is guessable from general knowledge of the dataset's three labelled subtypes (removal-test risk).

## i08 without D02 (autoimmune paper removed)

answer: Not answerable from D01, D03, D04, D05 and D06. ... If forced to guess: prior sill φ̂ = 100, for the 3,000-gene highly-variable-gene (HVG) analysis. I'd put the chance that this guess is right at about 0.8. The only other possible answer is 500.

Basis (verbatim): "the question only works if the autoimmune screen's count equals 3,000, 14,638 or 33,538 exactly. 33,538 is D05's full feature set before any filtering, so a screen is unlikely to 'pass' exactly that many. 14,638 comes from a filter specific to D05's dataset, so an independent study matching it would be an unlikely coincidence. Keeping the top 3,000 variable genes is a common round-number screen, which makes 3,000 the most plausible match."

Result: forced guess equals gold 100 at about 0.8. D02 not needed in practice; i08 dropped.

## i07 without D05 (brain spatial paper removed)

answer (verbatim): **31.0%** for the autoimmune MAD screen; the brain HVG percentage is **not answerable** from D01, D02, D03, D04 and D06. If forced to guess the second value, I would say **6.0%**, with about a **10% chance** of being right.

Basis (verbatim): "It assumes a common default: 2,000 highly variable genes out of 33,538 genes in a 10x Visium human brain dataset (2000 / 33538 = 5.96%, or 6.0%). Other plausible values: 3,000 out of 33,538 gives 8.9%. 2,000 out of 32,285 (mouse) gives 6.2%. Keeping the 'top 10%' outright gives 10.0%."

Result: forced guess 6.0% misses gold 8.9%, but 8.9% was listed among plausible alternatives (the 33,538 total is recalled as the 10x human reference size). D05 needed in practice, with a residual guess risk. The probe also reached 31.0% for the autoimmune half after reading Appendix A, and listed 10.1% (979) as the weaker reading.
