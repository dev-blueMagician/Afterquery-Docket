# Quick-test batch, round 3 (2026-10-06)

Target: easy (user: "actually in trial, it's okay if accept in even Low tier"). Paste each pair
into a sketch slot (question plus short answer) and quick-test all three together. A quick test is
one low-model answer: a miss is a good sign, not a tier pass. Please send back each verdict line
and the low model's answer as shown. Only sketches the low model misses get the full write-up and
checks before the single submission.

Local status: each question had one fresh blind solve that matched the gold with high confidence,
and one closed-book attempt that could not answer (unknown). Removal probes and reviews come after
the quick test, for the survivors only.

## S1 (i11) loading-matrix entries

Question:
How many more entries did the loading matrix of the brain spatial-factor study's tissue-section model have than the loading matrix of the autoimmune subtype study's selected model?

Gold answer:
17,312 entries

Why it may be missed: the brain paper puts spots, not genes, in its loadings (3,592 spots x 7
factors = 25,144); the autoimmune loadings are genes x factors (979 x 8 = 7,832). Wrong routes:
genes as rows (94,634), training spots only (14,512), the paper's "approximately p + Gq" parameter
count (24,013).

## S2 (i15) two BIC outcomes

Question:
The battery ageing study and the autoimmune subtype study both relied on BIC. What ridge hyper-parameter value did the battery study's algorithm reach at convergence when fitting all retained cells together, and by exactly how much was the autoimmune study's selected-model BIC below that of its alternative module construction?

Gold answer:
0.0002 and 248,685

Why it may be missed: the only λ in the battery paper's running text, 0.00067, belongs to one
cell's fit; the joint fit's 0.0002 is only in a figure caption. The autoimmune paper's prose says
"∆BIC ≈ 250,000"; the exact table difference is 1,280,292 - 1,031,607 = 248,685.

## S3 (i10) gene trimming with a threshold of 20

Question:
The autoimmune subtype study and the brain spatial-factor study each discarded genes with a threshold of 20: the first dropped genes in undersized modules when building its selected model's modules, the second dropped genes expressed in too few tissue spots. How many more genes did the second rule discard than the first?

Gold answer:
16,879 genes

Why it may be missed: the module-size rule acts on the 3000 genes left by the MAD ranking, a
figure printed only in the appendix (3000 - 979 = 2,021); the brain filter removed 33,538 - 14,638
= 18,900. Wrong routes: 9,671 - 979 (10,208), the WGCNA grey-module 4 genes (18,896).
