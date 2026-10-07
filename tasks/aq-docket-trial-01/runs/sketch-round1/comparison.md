# Comparative design assessment (question-review agent, fresh context), 2026-10-06

Design comparison only, not a fingerprint-bound check record. Input: candidate files q01, q02,
sketches i03, i07, i09, sketch-stage returns and removal probes. Return copied verbatim.

I'd put i09 first and quick-test it before anything else. None of the five looks like a dependable Medium. i09 is the only one whose trap works the way the measured Medium and High passes did, and even it looks about as likely to land Easy as Medium. All tier calls below are local predictions, not platform results.

**Records.** `report` shows q01 rev 0 (`604695ce…`) and q02 rev 0 (`404675dd…`) are current, with no source gaps and no platform records. i03, i07 and i09 are sketches with no fingerprint. I recomputed every gold from the original texts:
- q01: 65/5.91 = 10.998, so 11 (the rounding bounds allow only 10.90–11.09); 11 − 2 = 9.
- q02: 9 − 3 = 6.
- i03: λ = 0.0002 (D04 l.385) and 9 clusters (D02 l.447/725).
- i07: 3000/9671 = 31.02% and 3000/33538 = 8.945%.
- i09: 14,638 − 785 = 13,853.

### q01 (iterations, gold 9)
- **(a) One answer:** low risk. A model check could call the count "not stated", because the figure's iteration bars aren't in the text and the 5.91 is marked "∼". But l.403 ties the 5.91 seconds per iteration to Figure 5, and only 11 fits.
- **(b) Naive route:** none reaches 9 without the division.
- **(c) Removal:** D01 is safe. D04's only input is printed in the Doc 4 overview ("2 iterations to convergence"); I can't tell whether the platform's re-solve sees overviews.
- **(d) Trap:** no wrong value carries the asked label.
  - The 1000 slice-sampler iterations even share the word "benchmarked" (l.35), but "other clustering methods" and "that benchmark run" rule them out.
  - D04's "roughly 3-5" is a general range.
  - The only hurdle is one division.
- **(e) Tier:** Easy, with a real Too-easy risk. Medium needs the low model to miss all five on time ÷ time-per-iteration, which seems unlikely.

### q02 (clusters, gold 6)
- **(a) One answer:** low risk. The link between the "strong choice" and 28.9076 is inferred across sentences, but nothing contradicts it.
- **(b) Naive route:** two easy routes land on 3 without the intended step.
  - The headline Kpost = 3 is the first leukemia result, and the Doc 1 overview lists it first.
  - The leukemia data has three labelled subtypes, ALL, MLL and AML (l.37, l.273).
  - So the correct value is the obvious default, and the decoy only catches a solver who reads the sensitivity sentence and ignores "replaced".
- **(c) Removal:** moderate risk for D01. The removal probe guessed 6 at about 0.3 from the three known subtypes. D02 is safe.
- **(d) Trap:** Kpost = 4 carries the asked label and sits in the anchor sentence. But "replaced" directly paraphrases "instead of", and the WGCNA model's K = 4 is excluded by the question's own word "main".
- **(e) Tier:** Too easy or Easy.

### i03 (λ and clusters)
- **(a) One answer:** low risk. "Selected model" also fits l.579: "the WGCNA-based model selected a smaller model with K = 4".
- **(b) Naive route:** a keyword search lands on the answer.
  - The question's "full repeated-measurements model … at convergence" nearly copies the Figure 7 caption, which prints λ = 0.0002.
  - K = 9 is one sentence and is also in the Doc 2 overview.
- **(c) Removal:** both inputs are unguessable.
- **(d) Trap:** cell 8's 0.00067 sits in a paragraph that opens by naming the full model, so it is a real scope decoy. The caption labels the right value directly, though, and the second ask has no trap at all.
- **(e) Tier:** Too easy. Two unrelated lookups is exactly the "without careful work across the documents" profile.

### i07 (31.0%, 8.9%)
- **(a) One answer:** two ambiguities change the answer.
  - The main text describes the MAD screen and then "979 highly variable genes" (l.435–439), and later calls them "pre-selected genes" (l.577). Only Appendix A gives the 3000.
  - The brain base is never stated, and D05 doesn't say whether the HVGs came from all 33,538 genes or the 14,638 filtered ones (which gives 20.5%).
- **(b) Naive route:**
  - The Doc 2 overview prints "top 3000 genes ranked by MAD", so the buried appendix fact isn't buried.
  - Four stated counts and two divisions is the shape an earlier platform reviewer returned on this bundle as "too easy".
- **(c) Removal:** D05's half is partly guessable; the removal probe listed 8.9% among its alternatives.
- **(d) Trap:** the 979 decoy works the right way in principle, but because ruling it out is arguable, it reads as ambiguity rather than a trap.
- **(e) Tier:** Easy with a "vague" or "inconsistent" flag, or a reviewer return.

### i09 (observations, gold 13,853)
- **(a) One answer:** this is the main risk, because "observations" has no signpost.
  - D05 l.29 says it uses "observations" for the rows of Y (genes), and adds "we do not use this terminology here" about the spot meaning.
  - D02 uses "observation i" for samples (l.175; n is the number of samples at l.47).
  - That is defensible, but D05 itself admits the spot meaning exists, and subtracting samples from genes may look contrived to a reviewer.
- **(b) Naive route:** the question's "main tissue analysis" is a label route. D05 prints "main analysis" right after "retains 14,638 genes" (l.783) and "main results … (14,638 genes)" (l.1055), so a keyword matcher can reach the gold without resolving the term.
- **(c) Removal:** low risk. Neither 14,638 nor 785 is guessable, the closed-book solve returned "unknown", and no overview prints either count. The Doc 5 overview's "m spatial locations · n observations" is only a mild hint.
- **(d) Trap:** the best fit to the measured mechanism.
  - The everyday spatial-transcriptomics value (3,592 spots, or 3,192 after the 400 held-out spots) carries the asked label.
  - The case-study paragraph itself calls genes "gene features".
  - Only a definition about 750 lines earlier rules the spot count out, so the trap is untied, like aq-00745 q09.
- **(e) Tier:** roughly even between Easy and Medium, with a High tail (which still meets the target) and a small Too-hard tail. All three local solves matched, two of them on this exact wording.

### Ranking and quick tests
**Ranking:** i09, then q01, q02, i07, i03.

**Quick tests:**
- Test i09 first, in its exact final wording.
- If the low model answers 13,853, treat Medium as unlikely.
- If it answers 2,807 or 2,407, that fits the trap working, but a survival is weak evidence: aq-00998 q03 and aq-00949 round 4 survived quick tests and still came out too easy or unseparated.
- Test q01 second as the fallback.
- Don't spend tests on i03 or i07.
- If the form allows retesting identical text (unknown), sample i09 again.

### Wording risks for i09
1. **Unsignposted "observations"** could fail the platform's one-defensible-answer check. The reasoning field should quote both D05 l.29 sentences and D02 l.175 or l.47.
2. **"Main tissue analysis"** opens the label route to 14,638. It can't simply be dropped, because the gene reading needs it to give one answer.
3. **Genes minus samples** may strike a reviewer as contrived, and with one attempt a return is fatal.
4. **"Mixture factor model"** fits both D02 fits. Both use 785 samples, so the answer doesn't change.
5. **Paste it verbatim** onto the form.

Two open points:
- The tier rules you gave don't cover the low model getting 0/5 and then the medium model getting 4–5/5, so that outcome is unknown.
- i09 still needs to be prepared and fully checked before hand-over: two fresh blind solves on the final text, a closed-book solve, a shortcut audit and a review. Its sketch-stage matches used q02's packets and aren't tied to any fingerprint.
