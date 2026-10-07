# Platform Coach analyses, 2026-10-06 (pasted by the user)

Source: the user pasted two "Ask the Coach why" results after both drafts failed the quick test
("Too easy — solver got it"). Verbatim below. The first concerns q01 (iterations, gold 9), the
second q03 (observations, gold 13,853). Same message from the user: "actually in trial, it's okay
if accept in even Low tier. but failed in quick test. is there any good idea?"

## Coach on q01

The result says the low model reached your answer. Here is what the run data and the documents show about why.

**The question is two lookups and one subtraction.** The leukemia study's iteration count comes from dividing the Sparse DPMM runtime of 65 seconds (period not stated in Doc 1; Doc 1, Figure 5, panel a) by the stated per-iteration cost of ~5.91 seconds (period not stated in Doc 1; Doc 1, Section 3.2.1), giving approximately 11. The battery study's RIGLS convergence count of 2 iterations (period not stated in Doc 4; Doc 4, Section 2.4) is stated directly. The answer is 11 − 2 = 9. The guide's "Calculate across documents" lever says: "One lookup plus one operation is usually solved." Your draft is one lookup (2, stated), one derived figure (65 ÷ 5.91 ≈ 11), and one subtraction — that is the solved pattern.

**The numbers are easy to find.** Both the 65-second runtime (period not stated in Doc 1; Doc 1, Figure 5, panel a) and the 5.91-seconds-per-iteration figure (period not stated in Doc 1; Doc 1, Section 3.2.1) appear in the same section of Doc 1, and the "2-iterations" figure (period not stated in Doc 4; Doc 4, Section 2.4) appears in a single sentence in Doc 4. A reader does not need to align periods, resolve entities, or filter among decoys.

**Two things to flag on the draft itself:**

1. **The answer rests on approximations, not a stated figure (R9/PIN1).** The 65 (period not stated in Doc 1; Doc 1, Figure 5, panel a) is read from a chart bar, and the 5.91 (period not stated in Doc 1; Doc 1, Section 3.2.1) is preceded by "~" in the text ("∼ 5.91 seconds per iteration"; period not stated in Doc 1; Doc 1, Section 3.2.1). The documents never state an iteration count for the leukemia benchmark — it is derived by division. Your reference answer of exactly "9 iterations" depends on 65 ÷ 5.91 ≈ 11 being exact, but both inputs are approximate.

2. **Possible ambiguity in the battery study's iteration count.** Doc 4 states "The RIGLS algorithm converged after just 2-iterations" (period not stated in Doc 4; Doc 4, Section 2.4) but also says "convergence occurs after roughly 3-5 iterations" (period not stated in Doc 4; Doc 4, Section 2.2). Your question says "its full repeated-measurements model," which points toward the 2-iteration figure, but a reader could land on the other range.

To make this harder, the guide's levers that build difficulty from the evidence (rather than from stacking conditions) include "Scatter the pieces," "Restated figures," and "Calculate across documents" with three or more dependent steps. Your current draft has the pieces in the same sections of their documents and only one operation after the lookups.

## Coach on q03

**The question is two lookups and one subtraction.** The brain study states its main (filtered) analysis retains 14,638 genes (period not stated in Doc 5; Doc 5, Section 6) — and in that model, genes are the "observations" (rows of Y). The autoimmune study states its dataset comprises 785 samples (period not stated in Doc 2; Doc 2, Section 5.1) — and in that model, samples are the observations (rows of X). The answer is 14,638 − 785 = 13,853. The guide's "Calculate across documents" lever says: "One lookup plus one operation is usually solved." Your draft is exactly that — two direct lookups from two documents, then one subtraction.

**Both numbers are prominently stated.** The 14,638 figure appears in a single sentence in Doc 5, Section 6: "The low-expression filtering retains 14,638 genes." (period not stated in Doc 5; Doc 5, Section 6) The 785 figure appears in a single sentence in Doc 2, Section 5.1: "It contains a total of 785 samples." (period not stated in Doc 2; Doc 2, Section 5.1) Neither requires interpretation, alignment, or filtering — a model finds each number on the first pass through the relevant section and subtracts.

**No decoy or distractor forces a second look.** The brain study also mentions 3,592 spots, 33,538 genes (full set), and 3,000 HVGs (period not stated in Doc 5; Doc 5, Section 6), and the autoimmune study mentions 979 retained genes and 9,671 total genes (period not stated in Doc 2; Doc 2, Section 5.1). But the question says "main tissue analysis," which points directly at the filtered set (14,638), and "mixture factor model," which points at the sample count (785). A reader does not need to reject any of the alternative figures — the question's wording selects the right one immediately.

## Lessons recorded

- The platform guide's "Calculate across documents" lever now reads (quoted by the Coach): "One lookup
  plus one operation is usually solved." It recommends three or more dependent steps, scattered
  pieces, and a "Restated figures" lever that the local instruction.md does not list.
- Inputs derived from a chart value and a "∼" figure were flagged as approximations (R9/PIN1).
- A decoy only counts if the question's wording does not already select the right figure.
