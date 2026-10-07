# q01 rev 0 independent review (question-review agent, fresh context), 2026-10-06

Input: frozen fields (questions/q01.md), prepared run, tested_sha256 604695ce..., target medium,
raw returns (results/returns.md). Return copied verbatim from the task notification.

q01 (rev 0; tested_sha256: 604695ceac0f43ad3983b6d199cb01e630307ff984d5d6eb7cc8a23ae6b28336)

**gold_verified: yes.** I rebuilt the answer from the original texts.
- **Leukemia side (D01):**
  - Line 403: "Figure 5 shows that Sparse DPMM is significantly slower (∼ 5.91 seconds per iteration)".
  - Fig. 5 runtime label, line 413: "Sparse DPMM: 65". The panel label is "a) Runtime (in seconds)" (431), and the caption (435) says iterations "are indicated with mini-bars".
  - 65 / 5.91 = 10.9983. Allowing for rounding in both printed figures (64.5–65.5 s, 5.905–5.915 s), the range is 10.90–11.09. 10 or 12 iterations would mean 6.50 or 5.42 s per iteration, and 65/11 = 5.909 rounds to the printed 5.91. So the run took 11 iterations.
  - The run may cover several random initialisations (297). The total is still 11.
- **Battery side (D04):** "The RIGLS algorithm converged after just 2-iterations." (379), for "the full nonlinear repeated measurements model". The Fig. 7 caption (385) repeats it.
- **Result:** 11 − 2 = 9. Every premise in the question is true.
- **Alternatives ruled out:**
  - D04's "roughly 3-5 iterations" (351) is the authors' general experience, not this fit; it would give 6–8.
  - D01's "1000 MCMC iterations" (263) belong to the slice sampler on simulated data; they would give 998.
  - Reading 65 as an iteration count gives 63; rounding 10.998 down to 10 gives 8. Neither is defensible.
- The count is worked out, not printed. That is fair here because the paper links the two numbers: it attributes the per-iteration time to Figure 5.

**outcome: A: match; B: match.** Both were fresh, uncontaminated runs on separate packets. Both did 65/5.91 → 11, then 11 − 2 = 9, and both named and rejected the 6–8 and 998 readings. That is two supported matches.

**closed-book: misses.** The answer was "unknown" at low confidence, which is not equivalent to 9, and 9 has no obvious default value a model would guess.

**necessity:**
- **D01** is the only source of the 65 s runtime and the ∼5.91 s per iteration. Searching D02, D03, D05 and D06 found no DPMM, Dirichlet, leukemia, vimixr or 5.91. D05's 38.51/88.92/18.51 s are runtimes for a different model with no iteration counts. D01 cannot be replaced.
- **D04** is the only source of the 2-iteration count. No other document mentions RIGLS or batteries, and D01's "fewer iterations in higher dimensions" gives no number. D04 cannot be replaced.
- No rounded figure elsewhere approximates either input, and no smaller document set works.
- Caveat: the task page's overview for Doc 4 prints "2 iterations to convergence" (see finding 3).

**shortcut: clear.** I checked the auditor's route line by line (D01 403 + 413/431/435 → 11; D04 379/385 → 2). My own searches of all six texts found no passage that prints 11 iterations, 9, or the difference. The Doc 1 overview prints no runtime; the Doc 4 overview prints only the input. Searching finds the inputs, not the answer.

**source_assessment:** prepare and report list no source gaps. The capture is 6/6 complete with no gap characters.
- D01's text matches the original apart from the header line.
- D04's text differs only by Unicode normalization (all 196 changed lines are explained by it).
- All five evidence quotes appear word for word in the originals, the extracted texts and the capture.
- Two things are missing from the original .txt files themselves, so platform solvers lack them too. These are content limits, not gaps:
  - **Fig. 5 graphics** (the mini-bars and panels b/c). Premises are unaffected. The gold has to be calculated rather than read, but the calculation can only give 11. Exclusions don't apply. The only uniqueness risk is that the unseen mini-bars might differ, which doesn't matter for answering from the bundle. Necessity and shortcut are unaffected.
  - **Supplementary S1–S10**, which D01 cites. Same assessment.

**difficulty: easy.** This is a local prediction from the design, below the Medium target, not a measured tier. Medium needs the low model to get 0/5 and then the medium model 1–3/5. The ways a weaker solver could go wrong:
1. **Says the benchmark count is unprinted, or guesses** (moderate; the main hurdle). But the per-iteration sentence sits in the section the question describes, it names Figure 5, and the 65 s label is ten lines further on. "Time ÷ time per iteration" is a standard step.
2. **Takes the slice sampler's 1000 iterations → 998** (weak to moderate). It is the only explicit "N iterations" in D01, and the introduction says the model was "benchmarked against an MCMC slice sampler" (35). The question's "against other clustering methods" and "that benchmark run" rule it out.
3. **Uses D04's general 3–5 range → 6–8** (weak). It is a range marked "In our experience", while the question's own words match the 2-iteration sentence.
4. **Rounds down to 10 (→ 8) or treats 65 as a count (→ 63)** (weak).

None of these wrong values carries the asked label and is excluded only by a deciding fact. That was the mechanism behind this workspace's measured Medium and High passes (aq-00964 q01, aq-00745 q09). This question looks more like the derived-value questions that landed in the Easy window (aq-00998 q05, low model 2/5; aq-00949 q04, low model 3/5). My expectation:
- **Easy band:** most likely.
- **Too easy (low model 4–5/5):** a real risk.
- **Medium:** unlikely. Even if the low model went 0/5, a medium model will probably not miss this single division two or more times in five.

**verdict: revise.** I found no fairness or correctness defect. The unresolved finding is that the question does not suit the Medium target.

**findings:**
1. **Target suitability (gate Q13/difficulty), whole design.** The only real trap is one division inside D01, and the wrong values above are each excluded by the question's own wording. Consequence: with one submission attempt, it is not suitable for Medium, and the floor blocks `ready` while the review predicts below target. To verify:
   - Run a platform quick test of this exact wording first (the capture shows 0 of 10 used).
   - If the low model solves it, that rules out Medium. If it misses, that is weak evidence only.
   - Otherwise, switch to a question type where a wrong value carries the asked label and only one deciding fact rules it out.
2. **Reasoning step 2, the form's per-step number rule.** "11 - 2 = 9" sits in a step citing Doc 4, but 11 comes from Doc 1. Doc 4 contains "11" only as a page number (D04 line 381) and in the postcode "LE11" (line 13), so a plain string match passes by accident. A stricter check could flag "Doc 4 doesn't mention 11". Low risk; look at the form after pasting.
3. **Overview exposure.** The Doc 4 overview's "Figures" line prints "2 iterations to convergence". That makes the D04 step cheaper. If the platform's remove-a-document re-solve also shows the overview, it could report "A marked document may not be needed … without document 4". Whether it does is unknown and can't be checked locally.
4. **Platform reviewer risk.** The only cross-document step is subtracting the iteration counts of two unrelated algorithms. The earlier platform review of this bundle ("too easy: it can be answered without careful work across the documents") targeted the same pattern of analogous figures from unrelated papers. This is not a guide violation; it is a risk.
5. **Unprinted count marked "∼".** The derivation is supported and pinned to 11. There is a low risk that a platform model check calls the count "not stated".
6. **No stated precision.** The question doesn't say "whole iterations". Answers like "about 9" or "8.998" should count as equivalent, but a strict grader might differ. Low risk.
7. **Floor:** 0 FAIL, 1 WARN (origin is claude, but export accepts only user). Report this at hand-over and do not change the origin.
8. **Fingerprint.** `report` recomputed 604695ce… from the current file and corpus. All three packets' docs, texts and manifest match the snapshot hashes. The check records were appended after prepare, but the frozen fields are unchanged. A, B, closed-book and audit records are all bound to this fingerprint. There is no platform record yet, so this is locally checked only and nothing has been observed on the platform.
9. **Set overlap.** Sketches i03 (the D04 Fig. 7 caption, line 385) and i04 (the D01 benchmark) reuse q01's passages. Don't promote them together with q01 unless the passages differ.
10. **Process disclosure.** While checking packet hashes I wrote three temporary hash lists to the session scratchpad, which is outside the workspace. I wrote or changed no workspace files.
