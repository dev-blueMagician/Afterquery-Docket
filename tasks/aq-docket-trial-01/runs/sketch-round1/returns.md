# Sketch round 1: preliminary screen returns (2026-10-06)

Sketch-stage evidence only, not final check records. Each blind solve is a fresh blind-solver
agent given only the workspace root, a packet path from q01's prepared run (same corpus bytes; the
scope guard allows only that packet's text/ and docs/) and the sketch question verbatim. Closed-book
agents received only the question. Returns copied verbatim from the task notifications.

## i02 blind solve (blind-solver, q01 run's shortcut packet)

answer: 22.1

confidence: high

path:
1. Which study is which. D02 (`docs/arxiv_2606_16460v3.txt`) is the autoimmune subtype study. Its title is "Module-structured mixture factor models for molecular subtype discovery in transcriptomic data", and it covers "two autoimmune diseases ... RA and SLE". D05 (`docs/arxiv_2608_25172v1.txt`) is the brain study, with a section titled "Case Study: Spatial transcriptomics from the DLPFC brain region". A search for autoimmune, brain, DLPFC, lupus, rheumatoid and spatial transcriptomics found matches only in D02 (27) and D05 (37).
2. D02, all measured genes. In §5.1 (text line 431): "It contains a total of 785 samples ... with raw expression measurements available for 9,671 genes."
3. D02, genes kept by variability. In §2 (line 55): "The MAD provides a robust measure of marginal variability ... The top p∗ genes with the largest MAD values are retained." Appendix A (line 723) gives the number: "For the autoimmune disease dataset, the top 3000 genes ranked by MAD were retained."
4. D05, all measured genes. In §6 (line 783), section 151675 "contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features." This total is repeated in the full-gene analysis ("retaining all 33,538 genes") and in Appendix 10 (line 1055, "full-gene analysis (33,538 genes)").
5. D05, genes kept by variability. Line 783 describes "a 'highly variable gene' (HVG) analysis selecting the top 3,000 HVGs". The same passage defines them: "HVGs are genes with the highest expression variability across cells or spots." This was one of three analyses, alongside the filtered and full-gene ones, which matches "in at least one analysis".
6. The decisive phrases ("9,671 genes", "top 3000 genes ranked by MAD", "33,538 gene features", "top 3,000 HVGs") match word for word between the docs/ originals and text/.
7. Calculation:
   - Autoimmune share: 3000 / 9671 = 0.3102058, or 31.0206%.
   - Brain share: 3000 / 33538 = 0.0894508, or 8.9451%.
   - Difference: 31.0206 − 8.9451 = 22.0755 percentage points, which rounds to **22.1**. The value is not near a rounding boundary.

minimal_documents: D02 and D05. No other document can stand in for either: D01 is leukemia, D03 is order statistics, D04 is batteries and D06 is null-space SVD.

readings:
- **Brain denominator taken as the filtered set (14,638 genes).** This only works if "measured" means the genes that passed the low-expression filter, or if the HVGs were assumed to be picked from that filtered set. The paper doesn't say which pool the HVGs came from. 3000 / 14638 = 20.4946%, giving a difference of 10.5 points. I rejected this because the question says "all its measured genes", and the paper reports 33,538 measured gene features.
- **Autoimmune kept set taken as the final 979 genes.** 979 / 9671 = 10.1231%, giving a difference of 1.2 points. I rejected this because the 979 came from dropping modules with fewer than 20 genes after the MAD screening. That step was not a ranking by variability; the variability-ranked set kept was 3,000.

gaps:
- D05 does not say whether the top 3,000 HVGs were picked from all 33,538 genes or from the 14,638 filtered genes. This does not change the main reading, because the question fixes the denominator as all measured genes.
- The documents are plain text (the manifest gives `method: "text"` and `pages: null`). There are no PDFs or Dnn.layout.txt files, so no page checks were possible; the decisive numbers appear in running text, not charts.
- Coverage:
  - D02: read lines 1–74, 425–444, 570–619 and 715–728.
  - D05: read lines 1–40, 765–864 and 1050–1089.
  - D01, D03, D04, D06: read only lines 1–40 each.
  - Across all six documents: searched for disease/brain terms, gene counts and variability terms. The rest of the material was not read line by line.

contaminated: no. The input had only the workspace root, packet path and question. I saw no answer, reasoning, hint, project instructions or memory. I can't check the invocation mode (non-fork, omitClaudeMd) from inside the session.

## i02 closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: I can't tell from memory which two studies these are. To answer, I'd need each study's number of top-variability genes kept and its total number of measured genes. Guessing from common defaults, such as the top 2,000 variable genes out of about 33,500 measured in a brain spatial study, would just be making up a figure. No tools were called.
contaminated: no. The only extra context was an account identifier that Claude Code attached automatically. It has nothing to do with the question, and there were no document excerpts, hints, memory, bundle metadata or earlier results.

## i03 blind solve (blind-solver, q01 run's solver-1 packet)

answer: The battery study's full repeated-measurements model reached a ridge hyper-parameter of **λ = 0.0002** at convergence. The autoimmune study's selected model had **9 clusters** (K = 9, with q = 8 latent factors).

confidence: high

path:
1. D04 is the battery ageing study ("A Repeated Measurements Approach to SoH Battery Modelling of Cyclic Aged Data…", line 5). D02 is the autoimmune subtype study ("Module-structured mixture factor models for molecular subtype discovery…", using RA and SLE data).
2. In D04, λ is the ridge hyper-parameter and it is set with BIC. Line 121: "introducing a ridge regression term … of the form λθ Tθ into (7). When combined with an appropriate information theoretic measure, such as BIC [xiv], the hyperparameter, λ, can be optimally determined at each iteration". Equation (8) gives "λBIC = …".
3. The value for the full model is in the D04 Figure 7 caption (text/D04.txt line 385; docs source line 383 says the same): "Training residuals for the full nonlinear repeated measurements model with cell number as a parameter. The RMSE for these data is 0.191 [%]. At convergence λ = 0.0002. The RIGLS algorithm converged after just two iterations." The body text (line 379) confirms this is the full model ("converged after just 2-iterations… RMSE … 0.191 [%]") but does not give λ.
4. Values excluded: λ = 0.00067 (Fig. 5, line 373) and λ = 0.00048 (Fig. 6, line 383) are for single-cell "Level-1 PLM fit[s]" (cell 8 and cell 3), not the full model.
5. In D02, BIC selects the model. Line 443: "Model selection is carried out using the Bayesian information criterion (BIC)". Line 447: "For the combined RA-SLE dataset, the minimum BIC is attained at K = 9 and q = 8." Line 451: "Using the selected model configuration (K = 9, q = 8)". Appendix A, line 725: "The selected model had K = 9 and q = 8." K is defined at line 81 as "a finite mixture model with K latent clusters", and line 725 calls it "the number of clusters K".
6. Cross-checks: Table 1 (lines 455–461) lists clusters 1–9 and all are non-empty. For example, cluster 2 has 9 SLE samples and cluster 1 has 15 RA samples, which matches 9 clusters. Table 4 (line 585) gives "MAD-based model 9 8 … BIC 1,031,607".
7. No arithmetic is needed. Both values are quoted as printed, and 0.0002 is given to one significant figure in the source.

minimal_documents: D04 + D02. No alternatives exist: D01 (leukemia DPMM), D03 (order statistics), D05 (spatial factor models) and D06 (null-space SVD) are not battery or autoimmune studies. D01's only BIC mention (line 221) says "Standard model selection criteria like BIC fall short", and D05's only hit was the word "cubic".

readings:
- **WGCNA comparison model (K = 4).** D02 Table 4, line 587, also reports a "WGCNA-based model" with "K = 4 and q = 6", chosen by the same BIC grid. This is a comparison variant with a much worse BIC (1,280,292 versus 1,031,607), not the paper's selected model "used for all subsequent analyses" (line 447). Under that reading the answer would be 4, but I consider it the wrong reading.
- **"Clusters are removed" (line 437).** This sentence ("Small or weakly defined clusters are removed…") refers to gene co-expression modules in preprocessing (Appendix: "modules containing fewer than 20 genes were removed"). It does not change the sample-cluster count of 9.
- **Level-1 λ values.** Reading "converged hyper-parameter" as a per-cell Level-1 value would give 0.00067 (cell 8) or 0.00048 (cell 3), but the question asks for the full model, which is 0.0002.
- **Not a ridge parameter.** D02's λ at line 353, "(Ag + λIq) hg = bg", is a multiplier for the unit-norm constraint, not a ridge hyper-parameter, and is irrelevant here.

gaps:
- There are no layout files or PDFs. The manifest gives method "text" with pages null, so the figures could not be checked visually. The D04 Fig. 7 caption reads the same in text/ and docs/.
- Unread sections:
  - D04 lines 30–100 and 200–320 were not read directly, but a whole-file search for λ/lambda/hyper-parameter/BIC found no other λ values.
  - D02 lines 50–395 (model and ECM algorithm) and 504–560 (enrichment tables) were not read directly. Whole-file searches found no other "selected"/K values and no simulation study (the "simulat/synthetic" hits were only "biosynthetic").
  - D01, D03, D05 and D06 were read only in their first 30 lines, plus keyword searches.

contaminated: no

## i03 closed-book (closed-book-solver)

answer: unknown

confidence: low

basis: I don't remember either paper well enough to answer. The question needs two specific facts: the ridge value the battery study's full repeated-measurements model reached at convergence, and the number of clusters in the autoimmune study's chosen model. Guessing either one, such as a typical 3–4 clusters, would be unfounded. I used no tools.

contaminated: no

## i04 blind solve (blind-solver, q01 run's solver-2 packet)

**answer:** 3, 9

**confidence:** high

**path:**
1. **Which hyper-parameters were used in the benchmark.** D01 (text\D01.txt line 403, §3.2.1, the leukemia study's Sparse DPMM model) says the other methods "are compared with Sparse DPMM implementation with empirical Bayes hyper-parameters". The Discussion (line 437) repeats this: "it provides better clustering estimates with empirical Bayes hyper-parameters ... Even with weaker hyper-parameters...".
2. **What those values are.** D01 line 273, §3.2: "Following our empirical Bayes approach, we estimated a0 = b0 = 28.9076". Line 297: "with a weaker prior hyper-parameter, we used a0 = b0 = 10 instead of 28.9076". So 28.9076 is the "strong", non-weaker setting.
3. **Cluster count with those values.** D01 line 273: "For a strong choice of prior hyper-parameters, we obtained Kpost = 3 with ARI score of 0.92 (Figure 3(b))". The Figure 3 caption says "(b) Sparse DPMM cluster estimates obtained using strong hyper-parameters", and its legend shows "Cluster 1 2 3". For contrast, line 297: weaker values gave "Kpost = 4 with ARI score 0.86". **Leukemia count: 3.**
4. **Autoimmune model chosen by BIC.** D02 §5.2 (line 447): "For the combined RA-SLE dataset, the minimum BIC is attained at K = 9 and q = 8." Three other places agree:
   - §5.3 (line 451): "Using the selected model configuration (K = 9, q = 8)".
   - Table 1 (lines 459–461) has clusters 1–9, and the counts add to 785 samples: RA 15+149+66+228+35 = 493; SLE 9+114+113+56 = 292.
   - Appendix A (line 725): "The selected model had K = 9 and q = 8."
   
   Table 4 (line 585): "MAD-based model 9 8 −504,975.3 1,031,607". **Autoimmune count: 9.**

The question asks for the leukemia count first, then the autoimmune count: 3, 9.

**minimal_documents:** D01 and D02, both needed. There are no alternatives: D03 (order statistics), D04 (battery modelling, which uses BIC in another field), D05 (spatial factor models) and D06 (SVD error analysis) don't cover leukemia or autoimmune clustering.

**readings:**
- **Leukemia, if the benchmark used the weaker hyper-parameters (a0 = b0 = 10):** 4. The text contradicts this, since the benchmark says "empirical Bayes", and that value is 28.9076.
- **Autoimmune, if the WGCNA-based variant counts:** 4. D02 line 579 says "the WGCNA-based model selected a smaller model with K = 4 and q = 6". That is the comparison variant, and its BIC is much worse (1,280,292 vs 1,031,607), so BIC still prefers K = 9. This reading would give "3, 4", which I consider weak.

**gaps:**
- The bar values in D01 Figure 5b, which would show the Sparse DPMM cluster count directly in the benchmark, were lost in extraction. Only the axis labels "0 2 4 6" remain. The docs\ copy has the same text, and the packet has no PDF or layout file, so the "3" comes from linking the text in steps 1–3 rather than reading the chart.
- D02 Figure 1 (the ΔBIC grid) was not extracted, but the text states where the minimum is.
- The supplementary sections D01 cites (S6.2, S8) are not in the packet.
- Coverage: I read D01 and D02 in full. For D03, D05 and D06 I read only the titles and abstracts. For D04 I saw only the title and the line numbers of its BIC matches. Searches for leukemia, autoimmune and related disease terms across all six text files matched only D01 and D02.

**contaminated:** no

## i05 blind solve (blind-solver, q01 run's shortcut packet)

**answer:** 13,853. The brain study's main analysis used 14,638 observations (genes) and the autoimmune study's mixture factor model used 785 observations (samples); 14,638 − 785 = 13,853.

**confidence:** high

**path:**
1. **The brain study's definition of an observation.** The brain study is D05 (docs\arxiv_2608_25172v1.txt), on spatially orthogonal factor models applied to brain tissue.
   - §1.1, text line 29: "in spatial transcriptomics rows typically correspond to genes … we will use the term 'observations' for the rows of Y and spatial locations for the columns."
   - The same passage rules out counting spots: "'observation' may refer to a spatial location … we do not use this terminology here."
   - Line 31: "each gene, corresponding to a row of Y, is mean-centered across spatial locations."
2. **The brain study's main tissue analysis.** D05 §6, line 783, covers section 151675, which has "3,592 in-tissue Visium spots and 33,538 gene features."
   - "The low-expression filtering retains 14,638 genes."
   - "We treat the filtered analysis as our main analysis in the results below."
   - Appendix §10, line 1055, confirms it: "the main results shown in Figures 2 and 3 for the filtered analysis (14,638 genes)."
   - Holding out 400 spots removes columns, not rows, so the observation count stays at **14,638**.
3. **The autoimmune study's definition of an observation.** The autoimmune study is D02 (docs\arxiv_2606_16460v3.txt), on module-structured mixture factor models.
   - §2, line 47: "xi … represents the gene expression profile of sample i … n and p are the number of samples and genes."
   - §4.1, line 175: "The posterior probability that observation i belongs to cluster k is rik."
   - So an observation here is a sample.
4. **The autoimmune study's count.**
   - D02 §5.1, line 431: "It contains a total of 785 samples, including 493 RA samples and 292 SLE samples."
   - §5.2, line 443: the model "is fitted to the combined dataset."
   - Table 1 (lines 460–461) adds up to the same total. RA: 15+149+66+228+35 = 493. SLE: 9+114+113+56 = 292. Total **785**.
   - Table 5 (the comparison model) also totals 493 + 292 = 785.
5. **Calculation.** 14,638 − 785 = 13,853. Check: 785 + 13,853 = 14,638.

**minimal_documents:** D02 and D05. No other document can replace either one.
- D01 is a Dirichlet-process clustering paper with no autoimmune or brain data.
- D03 covers order statistics, D04 battery state-of-health, and D06 null-space SVD estimation.

**readings:**
- **Spots as brain observations:** 3,592 − 785 = 2,807, or 2,407 using the 3,192 spots left after the 400 held-out ones. D05 explicitly rejects this definition.
- **The full-gene analysis as the main one:** 33,538 − 785 = 32,753. With the top-3,000 highly variable gene set instead: 3,000 − 785 = 2,215. D05 names the filtered analysis as main, so neither applies.
- **Genes as the autoimmune study's observations:** 14,638 − 979 = 13,659. This contradicts D02's definition.
- None of these matches "as each paper defines them"; the primary answer stands.

**gaps:**
- I read D02 in full.
- I read D05 lines 1–1219 and 1653–1680. The rest (proof algebra in lines 1220–1652 and simulation figure captions in lines 1680–1716) I only searched for gene, spot and observation counts; there were no hits.
- For D03, D04 and D06 I read only the titles and abstract openings. D01 I covered by keyword search.
- The sources are plain text with no PDF page markers or layout files, so there are no PDF pages to inspect. The decisive phrases ("14,638", "total of 785", the definition of observations, "main analysis") also appear in the docs\ originals.

**contaminated:** no

## i05 closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: I can't tell which two papers the question means: the brain spatial-factor study and the autoimmune study with the mixture factor model. The answer depends on observation counts from those specific papers, such as spots or cells in the brain tissue analysis versus patients or samples in the autoimmune model. I don't recall those numbers, and any number I gave would be a guess. I made no tool calls.
contaminated: no (only the standard account and environment context that Claude Code attaches automatically, none of it about the papers)

## i04 closed-book (closed-book-solver)

answer: 4 and 3 (a guess)
confidence: low
basis: I couldn't identify either study from memory, so this answer is not based on recalling the papers. I guessed from typical outcomes. Bayesian nonparametric clustering of leukemia data often lands near the known 3–4 subtypes, and models picked by the Bayesian information criterion in autoimmune studies most often have 3–4 clusters. The answer depends on specific details I don't have: which hyper-parameters the leukemia study used in its benchmark, and which model the autoimmune study's criterion picked.
contaminated: no. The only context attached to this session was unrelated account and workspace metadata. There were no document excerpts, hints, keys or earlier results, and I made no tool calls.


## i06 blind solve (blind-solver, q01 run's solver-1 packet)

I read D01 and D02 in full and took the answer from them: **6**.

answer: 6
confidence: high

path:
1. **Autoimmune study's main BIC-selected model (D02, RA and SLE gene-expression data, GSE45291):**
   - §5.2, text line 447: "The optimal model configuration is selected as the combination of (K, q) that minimizes the BIC and is used for all subsequent analyses. For the combined RA-SLE dataset, the minimum BIC is attained at K = 9 and q = 8."
   - This is confirmed in §5.3 (line 451, "Using the selected model configuration (K = 9, q = 8)"), Table 4 (line 585, "MAD-based model 9 8 −504,975.3 1,031,607 19 979") and Appendix A (line 725, "The selected model had K = 9 and q = 8").
   - Table 1 (lines 459-461) shows all 9 clusters have samples. RA counts are 15+149+66+228+35 = 493, and SLE counts are 9+114+113+56 = 292. Together that is 785, matching the stated totals. So the model has **9 clusters**.
   - "Main" excludes the comparison model built from WGCNA modules. That model's BIC grid search picked K = 4, q = 6 (line 579, "the WGCNA-based model selected a smaller model with K = 4 and q = 6").
2. **Leukemia study's Bayesian model (D01, a Dirichlet-process mixture model called Sparse DPMM, run on N = 72 leukemia samples):**
   - Line 273: "For a strong choice of prior hyper-parameters, we obtained Kpost = 3 with ARI score of 0.92 (Figure 3(b)). Following our empirical Bayes approach, we estimated a0 = b0 = 28.9076"
   - Line 297, the sensitivity check: "To check the sensitivity of Sparse DPMM with a weaker prior hyper-parameter, we used a0 = b0 = 10 instead of 28.9076 and clustered the same dataset. For this particular choice, we obtained Kpost = 4 with ARI score 0.86."
   - The settings that were replaced are therefore a0 = b0 = 28.9076, the "strong" empirical Bayes setting. Three things support Kpost = 3 for that setting:
     - The legend of Figure 3(b) (line 293) reads "Cluster 1 2 3".
     - Line 297 says the weaker setting "identifies an additional 4th cluster".
     - The Discussion (line 437) contrasts "empirical Bayes hyper-parameters" with "weaker hyper-parameters".
   - Kpost is the posterior number of non-empty clusters (line 227). So this model found **3 clusters**.
3. **Calculation:** 9 − 3 = **6**.

minimal_documents: D01 and D02. Neither can be replaced: "autoimmun" appears only in D02 and "leuk" only in D01. D03 (order statistics), D04 (battery ageing; it uses BIC only as a formula), D05 (spatial transcriptomics of brain tissue and remote-sensing data; it mentions "immune" only for gene patterns) and D06 (SVD error analysis) contain neither study.

readings:
- **Replacement values instead of replaced values:** if "hyper-parameters that its sensitivity check replaced" is read as the new values (a0 = b0 = 10), Kpost = 4 and the answer is 9 − 4 = **5**. The wording "that ... replaced" points to the original 28.9076 setting, so 6 is the primary answer.
- **Wrong autoimmune model:** using the WGCNA comparison model (K = 4) instead of the main model gives 4 − 3 = **1**. This conflicts with "main", since the K = 9 model is the one "used for all subsequent analyses".
- **Components vs. occupied clusters:** counting mixture components (K = 9) or non-empty clusters (9) gives the same result.

gaps:
- No single sentence in D01 says "a0 = b0 = 28.9076 gave Kpost = 3". The link runs through "strong", "empirical Bayes", "instead of 28.9076", the "additional 4th cluster" wording and the Figure 3(b) legend, which makes it clear but not literal.
- The packet has no PDFs or layout files; the manifest lists only text sources with "pages": null. I could not look at the original figures. Figure 5(b), the cluster-count chart in D01's benchmark, didn't survive extraction as a number, but the answer doesn't depend on it.
- For D03-D06 I read only the first ~20 lines and ran targeted searches across them, not full reads.
- I did not open the duplicate source copies in docs/ separately.

contaminated: no. I received only the workspace root, packet path and question, and no answer, reasoning or source hint. I can't confirm from inside the session how I was launched (non-fork, omitClaudeMd), but no project instructions appear in my context.

## i07 blind solve (blind-solver, q01 run's solver-2 packet)

**answer:** 31.0%, 8.9%

**confidence:** high

**path:**
1. D02 is the autoimmune subtype study ("Module-structured mixture factor models for molecular subtype discovery…", RA and SLE). How many genes were measured: D02.txt line 431 says "It contains a total of 785 samples… with raw expression measurements available for 9,671 genes."
2. How many genes passed the MAD screen: D02.txt line 723 (Appendix A) says "For the autoimmune disease dataset, the top 3000 genes ranked by MAD were retained." Section 2 (lines 51–57) defines the screen: "The top p∗ genes with the largest MAD values are retained."
3. Calculation for D02: 3000 / 9,671 = 0.31021, which is **31.0%**.
4. D05 is the brain spatial-transcriptomics study (abstract: "human brain spatial transcriptomics case study"; Section 6: "Spatial transcriptomics from the DLPFC brain region"). How many genes were measured: D05.txt line 783 says "section 151675… contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features."
5. How many genes the HVG analysis kept: same line, "a 'highly variable gene' (HVG) analysis selecting the top 3,000 HVGs." The 3000-HVG analysis is also mentioned at lines 815, 819 and 1071.
6. Calculation for D05: 3000 / 33,538 = 0.089451, which is **8.9%**. The hundredths digit is 4, so it rounds down.
7. The same figures appear in the raw docs/ files: arxiv_2606_16460v3.txt lines 429 and 721, and arxiv_2608_25172v1.txt line 781.

**minimal_documents:** D02 and D05. Neither can be replaced. D01 is a leukemia clustering study with no MAD screen or HVG analysis. D03 (order statistics), D04 (battery modelling) and D06 (null-space SVD) contain no matches for genes, transcriptomics, brain or spatial.

**readings:**
- **Second number, other base (20.5%).** If the 3,000 HVGs were taken from the low-expression-filtered set ("The low-expression filtering retains 14,638 genes," line 783), then 3000 / 14,638 = 20.5%. The paper never says the HVGs came from the filtered set. It lists the HVG analysis alongside the filtered and full-gene analyses. Since the question's first part asks about "measured genes," I used the 33,538 measured features.
- **First number, final gene set (10.1%).** The D02 main text calls the final set "979 highly variable genes" (line 439), and 979 / 9,671 = 10.1%. But Appendix A (lines 723–725) shows the 979 genes are what remained after removing modules with fewer than 20 genes. They were not the output of the MAD screen. So 31.0% is the answer to the question as worded.

**gaps:**
- The packet has only text-extracted sources: the manifest says method "text" with pages null, and there are no PDF files. Locations above are therefore line numbers, not page numbers.
- D05 doesn't say which gene set the HVGs were selected from.
- I didn't read D01, D03, D04 or D06 in full. I ruled them out by keyword searches plus their titles and abstracts.

**contaminated:** no

## i07 closed-book (closed-book-solver)

answer: 25.0%; 10.0%
confidence: low
basis: I couldn't identify either study from memory, so these are guesses from common practice. Gene-subtyping studies often keep the top quarter of genes ranked by median absolute deviation. Bioconductor spatial workflows often keep the top 10% of highly variable genes. The actual gene counts from each document are missing.
contaminated: no

## i06 closed-book (closed-book-solver)

answer: 1 (a guess)
confidence: low
basis: I can't pin down either study from memory. This is an inference from typical results, not something I recall. Model-selection criteria like BIC usually pick about 4 subtypes in autoimmune studies. Bayesian clustering of leukemia samples (for example the Golub or Armstrong datasets) often finds 3 groups. I'd need both papers to confirm two numbers: the cluster count of the autoimmune study's main BIC-selected model, and the count the leukemia model found under its original prior settings, before the sensitivity check replaced them.
contaminated: no (only an automatically attached account email was present, which has nothing to do with the question)

## i08 closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: I can't connect this from memory. Answering needs two details from specific documents. The first is how many genes passed the gene screen in the autoimmune subtype study. The second is which tissue analysis in the brain spatial-factor study used that same number of genes, and what prior sill it reported. I don't reliably recall either, so any number I gave would be a guess.
contaminated: no


## i08 blind solve (blind-solver, q01 run's solver-1 packet)

**answer:** 100. In the brain study, the analysis that used the top 3,000 highly variable genes had an estimated prior sill of φ̂ = 100. The value was picked from the candidate set {1, 5, 10, 50, 100, 500, 1000, 5000}.

**confidence:** high

**path:**
1. **Matching the documents.**
   - D05 (`docs/arxiv_2608_25172v1.txt`) is "Spatially orthogonal factor models for spatial transcriptomics and remote sensing data". Its abstract describes a "human brain spatial transcriptomics case study", so it is the brain spatial-factor study.
   - D02 (`docs/arxiv_2606_16460v3.txt`) is "Module-structured mixture factor models for molecular subtype discovery…", covering "two autoimmune diseases" (RA and SLE). It is the autoimmune subtype study.
   - D01 (leukemia), D03 (order statistics), D04 (battery) and D06 (null-space SVD) don't match either description.
2. **The autoimmune study's gene screen (D02).**
   - Line 435: "genes are first screened using the MAD, and only highly variable genes are retained for downstream analysis."
   - Appendix A, line 723: "For the autoimmune disease dataset, the top 3000 genes ranked by MAD were retained."
   - So 3,000 genes passed the screen. A later, separate step dropped small modules, leaving 979 genes (line 725: "modules containing fewer than 20 genes were removed. This resulted in 979 genes grouped into 19 modules"). That step is module pruning, not the screen.
   - A search of D02 found no other screen size.
3. **The brain study's three analyses of section 151675 (D05, line 783).**
   - "a filtered analysis … to retain genes with positive expression in at least 20 spots": 14,638 genes ("The low-expression filtering retains 14,638 genes").
   - "a full-gene analysis retaining all 33,538 genes"
   - "a 'highly variable gene' (HVG) analysis selecting the top 3,000 HVGs"
   - Appendix line 1055 confirms the full-gene count (33,538) and the filtered count (14,638).
   - Only the HVG analysis used 3,000 genes, so it matches the D02 screen exactly.
4. **The sill estimate (D05, line 815).** "the domain of sill values was set to {1, 5, 10, 50, 100, 500, 1000, 5000}, and the estimated sill was φˆ = 500 for the filtered and full-gene analyses, and φˆ = 100 for the 3000-HVG analysis."
5. **Why "prior" sill fits.** D05 treats the sill as a parameter of the prior spatial covariance:
   - Line 683: "Σ depends on a sill parameter φ and length scale parameters"
   - Line 685: "estimating the prior nonstationary spatial covariance matrix … estimate the sill parameter φ"
   - Algorithm line 747: "Σs,λlat,λlon = φˆ · Cs,λlat,λlon"
6. **Arithmetic check.** 3000 = 3,000. It doesn't equal 14,638, 33,538 or 979, so exactly one analysis matches. No other sill value for the HVG analysis appears anywhere in D05; I searched for "sill", "φˆ" and "HVG".

**minimal_documents:** D02 + D05. Both are needed: D02 supplies the 3,000 count and D05 supplies the analysis and its sill. No other document in the packet can stand in for either one.

**readings:**
- **Main reading:** "passed the gene screen" means the MAD screen (3,000 genes). The answer is φ̂ = 100.
- **Alternative reading:** "passed the screen" means the final analysis set of 979 genes. D02 line 439 calls these "979 highly variable genes". No D05 analysis used 979 genes, so this reading has no answer. That supports the main reading, which also uses D02's own word "screened".
- **Near-miss to avoid:** φ̂ = 500 belongs to the filtered (14,638-gene) and full-gene (33,538-gene) analyses, not the one asked about.

**gaps:**
- There are no PDFs or `.layout.txt` files in the packet. `docs/` contains only `.txt` files, so I couldn't check any original pages. The decisive facts are in plain prose sentences, not tables or charts, so extraction loss is unlikely to matter. There is one stray page-number artifact ("The length scale domain 20") on line 815, after the sill sentence.
- What I read:
  - D02: lines 43–82, 429–453, 570–619 and 715–728, plus targeted searches.
  - D05: lines 675–690, 769–863 and 1053–1087, plus searches for sill, φ̂, HVG and gene counts.
  - D01, D03, D04 and D06: only the first 40 lines each (title and abstract), which was enough to rule them out.
- What I didn't read: the rest of D01, D03, D04 and D06; D05's methods, proofs and remote-sensing sections; and D02's model and algorithm sections. These don't bear on the question.

**contaminated:** no. I received only the workspace root, packet path and question. An automatic account context (the user's email) was attached, but it contains nothing about the answer.

## i09 closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: I can't identify either study from memory. "Brain spatial-factor study" and "autoimmune subtype study's mixture factor model" seem to point to particular documents. To answer, I would need the observation count from each study's model: the brain study's main tissue analysis and the autoimmune study's mixture factor model. I don't have those numbers, and guessing a difference would be meaningless.
contaminated: no


## i09 blind solve 2 (blind-solver, q02 run's solver-2 packet)

answer: 13,853 more observations (14,638 − 785)

confidence: high

path:
1. **Which documents.** D05 (text\D05.txt) is the brain spatial-factor study, "Spatially orthogonal factor models for spatial transcriptomics…" (SOFM). It is the only document that mentions "brain", in "6 Case Study: Spatial transcriptomics from the DLPFC brain region" (line 771). D02 (text\D02.txt) is the autoimmune subtype study, "Module-structured mixture factor models for molecular subtype discovery in transcriptomic data". It is the only document that mentions "autoimmune". D01 also uses a mixture model, but its data is leukemia, so it is excluded.
2. **What counts as an observation in D05.** D05 line 29 says: "In this work, in both applied settings, we will use the term 'observations' for the rows of Y". It also says "in spatial transcriptomics rows typically correspond to genes", and it rejects the per-spot meaning: "'observation' may refer to a spatial location … we do not use this terminology here." So observations in D05 are genes.
3. **D05's main tissue analysis.** Line 783 says: "We analyzed section 151675 … 3,592 in-tissue Visium spots and 33,538 gene features", "The low-expression filtering retains 14,638 genes" and "We treat the filtered analysis as our main analysis". The appendix (line 1055) repeats this: "the main results shown in Figures 2 and 3 for the filtered analysis (14,638 genes)". So n = 14,638.
4. **What counts as an observation in D02.** Line 47 says "xi … represents the gene expression profile of sample i … n and p are the number of samples and genes, respectively". So observations in D02 are samples.
5. **D02's sample count.** Line 431 says: "It contains a total of 785 samples, including 493 RA samples and 292 SLE samples". No sample exclusion is mentioned. Filtering applies only to genes: "979 highly variable genes organized into 19 co-expression modules" (line 439).
6. **The counts check out.** The selected model (K = 9, q = 8) has cluster counts in Table 1 (lines 460–461):
   - RA: 15 + 149 + 66 + 228 + 35 = 493
   - SLE: 9 + 114 + 113 + 56 = 292
   - Total: 785

   Table 5 for the WGCNA comparison model also totals 785 (493 + 292).
7. **Calculation.** 14,638 − 785 = 13,853. Check: 785 + 13,853 = 14,638.

minimal_documents: D02 + D05. No substitutes exist: no other document covers either study.

readings:
- **Observations as spots.** This is the common usage in spatial transcriptomics, but D05 explicitly rejects it.
  - 3,592 in-tissue spots − 785 = 2,807
  - Excluding the "400 held-out spots" (line 815): 3,192 − 785 = 2,407
- **A different gene set.** These are not the main analysis.
  - Full-gene analysis: 33,538 − 785 = 32,753
  - 3,000-HVG analysis: 3,000 − 785 = 2,215
- **Primary reading.** Rows are genes and the analysis is the filtered main one, giving 13,853.

gaps:
- No PDFs or Dnn.layout.txt files are in the packet (docs\ holds only .txt files; the manifest says method "text"). The figures I used are all in the prose and appendix text, so no page check was needed.
- I searched all six documents for the key concepts. Parts I did not read line by line:
  - D01, D03, D04 and D06 beyond their opening sections
  - D02 lines 60–424 (model and ECM algorithm)
  - D05 lines 60–760 (theory, algorithm and simulations) and its later appendices
- Searches for samples, simulations and the numbers 785/493/292 in D02, and for the gene counts in D05, found no conflicting figures.

contaminated: no


## i09 blind solve 1 (blind-solver, q02 run's solver-1 packet)

answer: 13,853 more observations (14,638 in the brain study's main analysis minus 785 in the autoimmune model)

confidence: high

path:
1. Which documents. D05 (docs/arxiv_2608_25172v1.txt), "Spatially orthogonal factor models for spatial transcriptomics…", is the brain spatial-factor study. D02 (docs/arxiv_2606_16460v3.txt), "Module-structured mixture factor models for molecular subtype discovery…", is the autoimmune subtype study. Searching all text files for brain/autoimmune/lupus/rheumatoid found matches only in D02 and D05.
2. What D05 counts as an observation. D05 line 29 says: "we will use the term 'observations' for the rows of Y and spatial locations for the columns." It also says "in spatial transcriptomics rows typically correspond to genes" and, about counting spots as observations, "we do not use this terminology here." Line 31 adds "each gene, corresponding to a row of Y." So in the brain study, observations are genes.
3. D05's main tissue analysis. Line 783: "We analyzed section 151675 … 3,592 in-tissue Visium spots and 33,538 gene features … The low-expression filtering retains 14,638 genes … We treat the filtered analysis as our main analysis." Appendix line 1055 agrees: "the main results shown in Figures 2 and 3 for the filtered analysis (14,638 genes)." The 400 held-out spots (line 815) are columns, not rows, so they don't change the observation count. Observations = 14,638.
4. D02's model. Line 431: "It contains a total of 785 samples, including 493 RA samples and 292 SLE samples." In D02, n is the number of samples (line 47), and line 175 refers to "observation i" belonging to a cluster. The model "is fitted to the combined dataset" (line 443). Two tables check the total:
   - Table 1 (selected K=9, q=8 model): RA 15+149+66+228+35 = 493; SLE 9+114+113+56 = 292; total 785.
   - Table 5 (WGCNA-based model): 493 + 292 = 785.
   Observations = 785.
5. Calculation: 14,638 − 785 = 13,853. The key quotes appear identically in the docs/ source copies (D05 docs lines 27, 781, 1053; D02 docs line 429).

minimal_documents: D02 and D05. No alternatives: no other document covers either study.

readings:
- If "main tissue analysis" meant the full-gene analysis: 33,538 − 785 = 32,753. Rejected, because the paper explicitly names the filtered analysis as the main one.
- If spots were counted as observations, which the paper explicitly rules out: 3,592 − 785 = 2,807. Excluding the 400 held-out spots instead gives 3,192 − 785 = 2,407.
- Using D02's 979 genes as its observation count would contradict D02's own definition (observations are samples), so I rejected it.

gaps:
- The packet had no PDF or layout files, so I couldn't look at figures (for example, D02 Figure 2b, cluster sizes). The text tables were enough.
- What I didn't read: D01, D03, D04 and D06 beyond their first ~40 lines, though the keyword search covered them in full. In D02, I skipped lines 120–379 (model and algorithm derivations) and the references. In D05, I skipped the methods, proofs, the phenology case study and the simulation appendix, apart from the search results.

contaminated: no
