# Hand-over: q05 rev 1 (checked; local review ready, Easy marginal)

Written in the style of aq-docket-trial-02 q01 (a part that must be carved out using a fact stated
elsewhere) and aq-docket-trial-06 q02 (a remainder printed only in a footnote or appendix), user
request 2026-10-06. Fingerprint f73ebf6033c08e869c72efe94c2f14f2323d143643c92c3524ee7c573107f6e4.
Paste each block into its own field. Doc numbers equal the task page's Doc 1-6.

## Question

Measured against all the genes each study had expression data for, what is the share discarded by the brain spatial-factor study's low-expression filter divided by the share discarded when the autoimmune subtype study removed undersized modules for its selected model? Give one decimal place.

## Gold answer

2.7 times

## Step-by-step reasoning

1. Doc 2: the autoimmune dataset has "raw expression measurements available for 9,671 genes".
2. Doc 2: Appendix A says that "the top 3000 genes ranked by MAD were retained", that their dendrogram was cut, that modules with fewer than 20 genes were then dropped ("20 genes were removed"), and that "This resulted in 979 genes grouped into 19 modules"; "The selected model had K = 9 and q = 8". So the removal of undersized modules took the 3000 retained genes down to 979.
3. Doc 2: the genes discarded by that removal number 3000 - 979 = 2,021.
4. Doc 2: as a share of the 9,671 genes with expression data, 2,021 / 9,671 = 20.898%.
5. Doc 5: the analysed tissue section "contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features", the low-expression filter keeps genes "with positive expression in at least 20 spots", and "The low-expression filtering retains 14,638 genes."
6. Doc 5: the genes discarded by the filter number 33,538 - 14,638 = 18,900.
7. Doc 5: as a share of the 33,538 genes with expression data, 18,900 / 33,538 = 56.354%.
8. Doc 5 and Doc 2: the brain share divided by the autoimmune share is 56.354 / 20.898 = 2.7 (to one decimal place).
9. Decoy, Doc 2: the main text gives only the 9,671 genes and the 979 in the final analysis set; 9,671 - 979 = 8,692 also counts the genes the MAD ranking had already dropped, so it overstates the module removal.
10. Decoy, Doc 2: measuring the module removal against the 3000 genes it started from gives 2,021 / 3000 = 67.37%, a different base from the question's.

## Documents, tags, components

- Necessary documents: Doc 2, Doc 5
- Reasoning tags: Cross-document join; Unit normalization; Conditional filter
- Component: 2.7 times

## Passages to save on the page (Save passage)

- Doc 2, Section 5.1: "with raw expression measurements available for 9,671 genes"
- Doc 2, Appendix A: "For the autoimmune disease dataset, the top 3000 genes ranked by MAD were retained."
- Doc 2, Appendix A: "20 genes were removed. This resulted in 979 genes grouped into 19 modules."
- Doc 2, Appendix A: "The selected model had K = 9 and q = 8."
- Doc 5, Section 6: "contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features"
- Doc 5, Section 6: "retain genes with positive expression in at least 20 spots"
- Doc 5, Section 6: "The low-expression filtering retains 14,638 genes."

## Notes

- Origin: written by Claude (origin claude). Ticking "I wrote this question myself" is your call.
- Quick test first (question plus gold answer). q04, q05 and sketch S3 (i10) share inputs: submit
  at most one of them.
- Local checks on this exact content: two fresh blind solves 2.7 (high), shortcut audit clear,
  closed-book unknown, removal probes without Doc 2 (11.3) and without Doc 5 (3.0) both miss,
  independent review ready (Too easy about 50%, Easy about 40%, Low 0/5 about 10%).
- If the form flags a reasoning number, paste the panel text back: any edit needs a new
  fingerprint and fresh checks before submitting.
