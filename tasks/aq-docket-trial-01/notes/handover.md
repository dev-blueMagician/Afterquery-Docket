# aq-docket-trial-01 hand-over (2026-10-06)

Written for the person filling in the Trial 1 platform form. Doc numbers below are the platform's
(they match the local D01-D06 ids). Paste every field exactly as written.

## Status in one paragraph

Both questions below are fair and fully checked locally: two fresh blind solves matched, a
closed-book attempt missed, a shortcut audit was clear and independent reviews verified the gold.
Neither is a dependable Medium. The independent reviews predict the Easy band for both. The
platform has not measured either one. Use the form's quick tests (low model, 0 of 10 used) before
spending the single submission.

## Quick-test plan

1. Quick-test **Q-A** first, with exactly the question and answer below.
   - If the low model answers 13,853, a Low 0/5 result (needed for Medium) becomes unlikely.
   - If it answers 2,807 or 2,407 (spots counted as observations), the trap worked once. That is
     weak evidence only: earlier bundles survived a quick test and still came back "Too easy".
2. Quick-test **Q-B** second as the fallback.
3. Paste the quick-test lines back verbatim before submitting, so they can be recorded and the
   choice made on evidence.

## Q-A (recommended first): q03 rev 2, tested_sha256 987c25e3...

**Question**

How many more observations did the brain spatial-factor study's model have in its main tissue analysis than the autoimmune subtype study's mixture factor model had?

**Gold answer**

13,853 observations

**Step-by-step reasoning**

1. Doc 5: the paper uses "the term ‘observations’ for the rows of Y", and in its spatial transcriptomics analysis each row is a gene ("each gene, corresponding to a row of Y"); it sets aside counting a spot as an observation ("we do not use this terminology here"). Its main tissue analysis is the filtered one, where "The low-expression filtering retains 14,638 genes", so that model had 14,638 observations.
2. Doc 2: its data matrix has one row per sample ("n and p are the number of samples and genes, respectively"), and its observations are those samples ("The posterior probability that observation i belongs to cluster k"); the dataset "contains a total of 785 samples".
3. Doc 5 and Doc 2: 14,638 - 785 = 13,853 more observations.
4. Decoys: counting Doc 5's in-tissue spots as observations, or taking its full-gene or highly-variable-gene analysis instead of the main one, gives a different number; Doc 2's genes are its variables, not its observations.

**Necessary documents:** Doc 2, Doc 5

**Reasoning tags:** Cross-document join; Entity resolution

**Passages to save (verbatim)**

- Doc 5: "we will use the term ‘observations’ for the rows of Y and spatial locations for the columns"
- Doc 5: "‘observation’ may refer to a spatial location together with its vector of measurements across all genes / features; we do not use this terminology here"
- Doc 5: "In the spatial transcriptomics analysis, each gene, corresponding to a row of Y"
- Doc 5: "The low-expression filtering retains 14,638 genes."
- Doc 5: "We treat the filtered analysis as our main analysis"
- Doc 2: "n and p are the number of samples and genes, respectively"
- Doc 2: "denote the cluster indicator for sample i"
- Doc 2: "The posterior probability that observation i belongs to cluster k"
- Doc 2: "It contains a total of 785 samples"

**Known risks**

- Predicted Easy (Medium or above about one in ten). The spot decoy rests on field convention, and
  the paper's own definition sentence contains the question's keyword.
- If several attempts agree on 2,807, the platform may add a "too vague" warning. The defence is the
  paper's explicit definition and its disclaimer about the spot meaning.
- Step 3 cites two documents because neither prints both numbers; check the form's reasoning panel
  after pasting.

## Q-B (fallback): q01 rev 0, tested_sha256 604695ce...

**Question**

When the leukemia clustering study benchmarked its sparse Dirichlet process mixture model against other clustering methods, how many more iterations did that benchmark run take than the battery ageing study's regularised algorithm needed to converge for its full repeated-measurements model?

**Gold answer**

9 iterations

**Step-by-step reasoning**

1. Doc 1: in the benchmark against other clustering methods, the runtime panel ("a) Runtime (in seconds)") lists "Sparse DPMM: 65", and the text says Sparse DPMM is slower at "∼ 5.91 seconds per iteration". Iterations in that run: 65 / 5.91 = 11 (to the nearest whole iteration).
2. Doc 4: for the full repeated-measurements model, "The RIGLS algorithm converged after just 2-iterations" (the Figure 7 caption repeats "converged after just two iterations"). Difference: 11 - 2 = 9 iterations.
3. Decoys in Doc 4 and Doc 1: Doc 4's "In our experience convergence occurs after roughly 3-5 iterations" describes the method in general, not this fit, which took 2. Doc 1's "1000 MCMC iterations" belong to the comparison slice sampler on simulated data, not to the leukemia benchmark.

**Necessary documents:** Doc 1, Doc 4

**Reasoning tags:** Cross-document join; Unit normalization

**Passages to save (verbatim)**

- Doc 1: "Sparse DPMM: 65"
- Doc 1: "a) Runtime (in seconds)"
- Doc 1: "Sparse DPMM is significantly slower (∼ 5.91 seconds per iteration)"
- Doc 4: "The RIGLS algorithm converged after just 2-iterations."
- Doc 4: "The RIGLS algorithm converged after just two iterations."

**Known risks**

- Predicted Easy, with "Too easy" a real risk: the only hurdle is one division (65 / 5.91).
- Step 2's "11" passes the form's number check only because Doc 4 happens to print "11" elsewhere.
- The Doc 4 overview prints "2 iterations to convergence" (an input, not the answer).

## Before you submit

- Both questions were written by Claude (origin: claude). The form's "I wrote this question
  myself." box cannot be ticked truthfully for them; that decision, and the platform's AI-use
  terms, are yours.
- The local export tool accepts only user-origin questions, so no export sheet was generated.
- Status is "checked" (locally checked, platform pending), not "ready".
