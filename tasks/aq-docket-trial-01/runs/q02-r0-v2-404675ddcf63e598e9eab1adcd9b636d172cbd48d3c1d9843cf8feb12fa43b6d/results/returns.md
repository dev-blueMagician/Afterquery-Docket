# q02 rev 0 raw returns (tested_sha256 404675ddcf63e598e9eab1adcd9b636d172cbd48d3c1d9843cf8feb12fa43b6d)

Fresh agents dispatched 2026-10-06 by the caller (Claude Code, Opus 5.5) with only the workspace
root, their own packet path and the verbatim question (closed-book: question only). Returns are
copied verbatim from the task notifications.

## Blind solver A (blind-solver, packet solver-1)

answer: **6**. The autoimmune study's main BIC-selected model had 9 clusters; the leukemia study's Sparse DPMM found 3 clusters with the hyper-parameters that the sensitivity check replaced. 9 − 3 = 6.

confidence: high

path:
1. **Autoimmune study (D02, arXiv 2606.16460v3, RA/SLE data):** Section 5.2 (text/D02.txt line 447) says "For the combined RA-SLE dataset, the minimum BIC is attained at K = 9 and q = 8."
   - Three other passages agree. Table 4 (line 585) lists "MAD-based model 9 8 −504,975.3 1,031,607 19 979". Appendix A (line 725) says "The selected model had K = 9 and q = 8."
   - Table 1 (lines 460–461) shows all 9 clusters have samples: 15, 9, 114, 113, 149, 66, 228, 56, 35. These add up to 785, which matches "785 samples" (line 431).
   - This is the "main" model. The WGCNA model ("selected a smaller model with K = 4 and q = 6", line 579) is only a comparison.
2. **Leukemia study (D01, arXiv 2601.21106v3, N = 72 samples, Bayesian Sparse DPMM):** Section 3.2 (line 273) says "For a strong choice of prior hyper-parameters, we obtained Kpost = 3 with ARI score of 0.92 (Figure 3(b)). Following our empirical Bayes approach, we estimated a0 = b0 = 28.9076".
3. **The sensitivity check (D01 line 297, same wording in docs/arxiv_2601_21106v3.txt line 295):** "To check the sensitivity of Sparse DPMM with a weaker prior hyper-parameter, we used a0 = b0 = 10 instead of 28.9076 and clustered the same dataset. For this particular choice, we obtained Kpost = 4 with ARI score 0.86."
   - So the replaced setting is a0 = b0 = 28.9076, called "strong" in contrast to "weaker". The Figure 3(b) caption refers to "Sparse DPMM cluster estimates obtained using strong hyper-parameters". That run gave Kpost = 3.
   - The Discussion supports this: there are "better clustering estimates with empirical Bayes hyper-parameters", and "Even with weaker hyper-parameters" the model adds "a biologically meaningful sub-cluster" (the 4th).
4. **Calculation:** 9 − 3 = 6 more clusters.

minimal_documents: D01 + D02. Both are needed and neither can be swapped out. D03 (order statistics), D04 (battery ageing), D05 (spatial transcriptomics/remote sensing) and D06 (null-space SVD) have no leukemia, autoimmune or comparable clustering results. A search for "leuk" matched only D01, and "autoimmun" matched only D02. Within D02, K = 9 appears in several places (Section 5.2, Section 5.3, Table 4, Appendix A), so any one is enough. In D01, Kpost = 3 appears only at line 273.

readings:
- Using the sensitivity check's own result (a0 = b0 = 10, Kpost = 4) gives 9 − 4 = 5. I rejected this because the question asks about the hyper-parameters the check replaced, not the ones it used.
- Taking D02's WGCNA comparison model (K = 4) as the "BIC-selected model" gives 4 − 3 = 1. I rejected this because the question says "main", and the paper presents the MAD-based K = 9 model as the main one.
- I found no other defensible reading.

gaps:
- No single sentence says the "strong choice" is exactly a0 = b0 = 28.9076. I linked them from "weaker … instead of 28.9076", the order of the sentences, and the Figure 3/4 captions. The link is consistent everywhere and nothing contradicts it.
- Figure 5 (D01 benchmark of cluster counts with empirical Bayes hyper-parameters) is a chart whose bar values were not extracted. The packet has no PDF or layout file (docs/ holds only .txt; text/ has no Dnn.layout.txt), so I couldn't inspect it. It isn't needed for the answer.
- Supplementary material S6.2 is cited but not in the packet.
- I read D01 and D02 in full. For D03–D06 I read only the title/abstract and keyword-search hits. I did not read question.txt.

contaminated: no

## Blind solver B (blind-solver, packet solver-2)

**answer:** 6. The autoimmune study's main BIC-selected model had 9 clusters. The leukemia Sparse DPMM found 3 clusters with the hyper-parameters a0 = b0 = 28.9076, which its sensitivity check replaced. 9 − 3 = 6.

**confidence:** high

**path:**
1. **Autoimmune study = D02** (RA/SLE dataset GSE45291, 785 samples). It is the only document that matches "autoimmun".
   - Section 5.2 (text\D02.txt line 447): "For the combined RA-SLE dataset, the minimum BIC is attained at K = 9 and q = 8." The same section says this configuration "is used for all subsequent analyses".
   - Section 5.3 (line 451): "Using the selected model configuration (K = 9, q = 8)…". Table 1 (lines 459–461) shows all 9 clusters have samples:
     - RA: 15, 0, 0, 0, 149, 66, 228, 0, 35
     - SLE: 0, 9, 114, 113, 0, 0, 0, 56, 0
   - Table 4 (line 585) and Appendix A (line 725) say the same: "The selected model had K = 9 and q = 8."
   - The WGCNA-based model with K = 4 (line 579) is a comparison model, not the main one. Its BIC is higher (1,280,292 vs 1,031,607).
2. **Leukemia study = D01** (Sparse DPMM, a collapsed-variational-inference Dirichlet process mixture model, on 72 samples and 2,194 genes). It is the only document that matches "leukemia/leukaemia".
   - Section 3.2 (line 273): "For a strong choice of prior hyper-parameters, we obtained Kpost = 3 with ARI score of 0.92 (Figure 3(b)). Following our empirical Bayes approach, we estimated a0 = b0 = 28.9076".
   - Line 297, the sensitivity check: "To check the sensitivity of Sparse DPMM with a weaker prior hyper-parameter, we used a0 = b0 = 10 instead of 28.9076 and clustered the same dataset. For this particular choice, we obtained Kpost = 4 with ARI score 0.86."
   - So the replaced hyper-parameters are a0 = b0 = 28.9076, the empirical Bayes or "strong" choice. Three statements confirm that "strong" and the empirical Bayes values are the same setting:
     - The Figure 3 caption says "(b) Sparse DPMM cluster estimates obtained using strong hyper-parameters".
     - The Discussion (line 437) says "better clustering estimates with empirical Bayes hyper-parameters… Even with weaker hyper-parameters…".
     - The sensitivity check describes 10 as "weaker", in contrast to the "strong" setting.
   - Under that setting, Kpost = 3.
3. **Calculation:** 9 − 3 = 6 clusters.
4. The decisive sentences also appear in the source files in docs\: arxiv_2601_21106v3.txt lines 271 and 295, and arxiv_2606_16460v3.txt lines 445, 449 and 723.

**minimal_documents:** D01 and D02. No other document can replace either one: D03 is about order statistics, D04 battery state-of-health modelling, D05 spatially orthogonal factor models, and D06 null-space SVD error analysis.

**readings:**
- If "replaced" is misread as the replacement setting (a0 = b0 = 10, Kpost = 4), the answer is 9 − 4 = 5. The sentence "used … 10 instead of 28.9076" shows 28.9076 is the replaced setting, so I reject this reading.
- If the autoimmune model were taken to be the WGCNA comparison model (K = 4), the answer would be 4 − 3 = 1. That model is not the main BIC-selected model, so I reject this too.
- D01 has a separate hyper-parameter sensitivity analysis on negative-binomial simulations, and a single-cell example in the supplement. Neither is "on the leukemia samples", so neither applies.

**gaps:**
- The manifest lists text-only extraction ("pages": null), and there are no Dnn.layout.txt files or original PDFs in the packet. I could not inspect the figures directly: D02 Figure 1 (the ΔBIC grid) and D01 Figures 3 and 5 (Figure 5 has the Sparse DPMM cluster count in the benchmark). The prose and tables state the needed values directly, so this does not affect the answer.
- I read D01 and D02 in full. For D03–D06 I only looked at the titles and ran keyword searches (autoimmune, leukemia/leukaemia, disease-name synonyms, BIC). D04's BIC mentions are about battery-model regularization and are not relevant.

**contaminated:** no

## Closed-book solver (closed-book-solver, question only)

answer: 1

confidence: low

basis: I couldn't identify either study from memory, so this is a guess based on typical numbers. Autoimmune subtype studies that pick their model by BIC often land on about 4 clusters. Bayesian clustering of leukemia samples often finds about 3 clusters (for example, B-ALL, T-ALL and AML). I don't have the details I'd need from the two papers: the cluster count of the autoimmune study's main BIC-selected model, and the count the leukemia model found with its original prior hyper-parameters, before the sensitivity check swapped them out.

contaminated: no

## Shortcut auditor (shortcut-auditor, packet shortcut)

answer: **6**. The autoimmune study's main BIC-selected model has K = 9 clusters. The leukemia study's model found Kpost = 3 clusters with the hyper-parameters (a0 = b0 = 28.9076) that its sensitivity check replaced. 9 − 3 = 6.

verdict: clear

shortest_path:
1. A search for "autoimmun" matches only D02 (Wu, McLachlan, Pyne: a mixture factor model on RA and SLE samples). Section 5.2 says: "For the combined RA-SLE dataset, the minimum BIC is attained at K = 9 and q = 8." The same value appears in Table 4 ("MAD-based model 9 8 −504,975.3 1,031,607 19 979"), in Appendix A ("The selected model had K = 9 and q = 8") and in Table 1, which lists clusters 1–9. So K = 9.
2. A search for "leukemia" matches only D01 (Pal et al., Sparse DPMM on 72 leukemia samples and 2,194 genes). Section 3.2 says: "For a strong choice of prior hyper-parameters, we obtained Kpost = 3 with ARI score of 0.92 (Figure 3(b)). Following our empirical Bayes approach, we estimated a0 = b0 = 28.9076 … To check the sensitivity of Sparse DPMM with a weaker prior hyper-parameter, we used a0 = b0 = 10 instead of 28.9076 … we obtained Kpost = 4 with ARI score 0.86." The values that were replaced are 28.9076, the strong/empirical Bayes setting, so Kpost = 3. The caption of Figure 3(b) ties the 3-cluster result to the "strong hyper-parameters."
3. 9 − 3 = 6.

sufficient_documents: D01 and D02 are both required, and nothing else can stand in for either. Neither document cites the other, and no single document has both values. Paths:
- D:\Dev\Docket\tasks\aq-docket-trial-01\runs\q02-r0-v2-404675ddcf63e598e9eab1adcd9b636d172cbd48d3c1d9843cf8feb12fa43b6d\shortcut\text\D01.txt
- D:\Dev\Docket\tasks\aq-docket-trial-01\runs\q02-r0-v2-404675ddcf63e598e9eab1adcd9b636d172cbd48d3c1d9843cf8feb12fa43b6d\shortcut\text\D02.txt

searches:
- **Literal and concept terms:** leuk(a)emia, autoimmun, BIC, hyper-parameter, sensitivity, Kpost, 28.9076, Armstrong, vimixr, Sparse DPMM, Hejblum, McLachlan, mixture factor, Dirichlet process, lupus, rheumatoid, SLE, GSE45291, "number of clusters", K = 9, K = 3, "minimum BIC".
- **Read in full:** D01 and D02.
- **Other documents:** I read the headers of D03–D06 and ran targeted searches on them. They cover order statistics (D03), battery state-of-health modelling (D04, where BIC and hyper-parameter refer to a regression λ), spatial factor models (D05) and null-space SVD (D06). D06's "K = 9" counts tail margins and is unrelated.
- **docs/ originals:** I also searched these. The key terms appear only in the two arXiv files behind D01 and D02.
- **Contamination:** none. I had only the packet path and the question, with no project instructions, notes, gold answer or prior outputs.
- **Shortcut attacks:** Every attack failed. There is no summary or ranking that gives the whole answer, no single sufficient document, and nothing in the wording that hands over the answer.

readings/gaps:
- **Distractor readings:**
  - 9 − 4 = **5** uses the result from the replacement (weaker, a0 = b0 = 10) prior instead of the prior that was replaced. The wording "instead of 28.9076" rules this out.
  - 4 − 3 = **1** uses D02's WGCNA comparison model (K = 4, q = 6), which is not the main model. The paper selects the MAD-based K = 9 model "for all subsequent analyses."
  - 4 − 4 = **0** combines both distractors.
  - Reading the leukemia side as the three labelled subtypes (ALL, MLL, AML) still gives 3, so the answer stays 6.
  - q = 8 and k0 = 73 are a latent dimension and a hyper-parameter, not cluster counts.
- **Difficulty risk:** this is a simple two-document subtraction with both inputs stated plainly in prose. What makes it non-trivial is telling the replaced prior from the replacement and the main model from the WGCNA one. This is a difficulty concern, not a shortcut.
- **Extraction gaps:**
  - Figures can't be read from the text, including D02's Figure 1 (ΔBIC grid) and D01's Figure 5 (estimated clusters per benchmarked method). The prose is unambiguous, so they aren't needed.
  - The manifest lists only text extraction (method "text"), so there are no page images to check.
  - I didn't read D03–D06 in full, but searches show they are off-topic.
