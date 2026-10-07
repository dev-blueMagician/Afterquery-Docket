# Hand-over: q04 rev 0 (checked; local review ready, Too easy about 65%; q05 preferred)

Written in the style of aq-docket-trial-02 q01 and aq-docket-trial-06 q02 (user request,
2026-10-06). Fingerprint ced2e12b09a10904dcce43687b70c32c04f9668e1b03291d9458fc7ced840014.
Paste each block into its own field. Doc numbers equal the task page's Doc 1-6.

## Question

Measured against the genes each step started from, by how many percentage points did the share kept by the brain spatial-factor study's low-expression filter exceed the share kept by the autoimmune subtype study's removal of undersized modules for its selected model? Give one decimal place.

## Gold answer

11.0 percentage points

## Step-by-step reasoning

1. Doc 2: Appendix A says that "the top 3000 genes ranked by MAD were retained", that hierarchical clustering was then applied and the dendrogram cut, that modules with fewer than 20 genes were then dropped ("20 genes were removed"), and that "This resulted in 979 genes grouped into 19 modules"; "The selected model had K = 9 and q = 8". So the removal of undersized modules started from 3000 genes and kept 979.
2. Doc 2: the share kept by that step is 979 / 3000 = 32.63%.
3. Doc 5: the analysed tissue section "contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features", the low-expression filter keeps genes "with positive expression in at least 20 spots", and "The low-expression filtering retains 14,638 genes."
4. Doc 5: the share kept by the filter is 14,638 / 33,538 = 43.65%.
5. Doc 5 and Doc 2: the brain filter's share exceeds the autoimmune step's share by 100 × 14,638 / 33,538 - 100 × 979 / 3000 = 11.0 percentage points (to one decimal place).
6. Decoy, Doc 2: the main text gives only the 9,671 measured genes and the 979 in the final analysis set; 979 / 9,671 = 10.12% is the share left after both the MAD ranking and the module removal, not the share kept by the module removal alone.
7. Decoy, Doc 2: the WGCNA comparison also used a minimum module size of 20 genes and excluded the 4 genes assigned to the grey module, but its modules were not the ones the selected model used; 975 / 979 = 99.59% belongs to that comparison.

## Documents, tags, components

- Necessary documents: Doc 2, Doc 5
- Reasoning tags: Cross-document join; Unit normalization; Conditional filter
- Component: 11.0 percentage points

## Passages to save on the page (Save passage)

- Doc 2, Appendix A: "For the autoimmune disease dataset, the top 3000 genes ranked by MAD were retained."
- Doc 2, Appendix A: "20 genes were removed. This resulted in 979 genes grouped into 19 modules."
- Doc 2, Appendix A: "The selected model had K = 9 and q = 8."
- Doc 5, Section 6: "contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features"
- Doc 5, Section 6: "retain genes with positive expression in at least 20 spots"
- Doc 5, Section 6: "The low-expression filtering retains 14,638 genes."

## Notes

- Origin: written by Claude (origin claude). Ticking "I wrote this question myself" is your call.
- Quick test first (question plus gold answer). It shares inputs with sketch S3 (i10); test q04
  in place of S3.
