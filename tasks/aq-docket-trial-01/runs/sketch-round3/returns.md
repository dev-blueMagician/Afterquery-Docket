# Sketch round 3: preliminary screen returns (2026-10-06)

Sketch-stage evidence only, not final check records. Each blind solve is a fresh blind-solver
agent given only the workspace root, a packet path from q03's prepared run
(q03-r2-v2-987c25e3..., same corpus bytes; the scope guard allows only that packet's text/ and
docs/) and the sketch question verbatim. Closed-book agents received only the question. Returns
copied verbatim from the task notifications.

## i10 closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: I can't place either study well enough from memory. The autoimmune subtype study is probably a module-based analysis, perhaps a WGCNA-style setup with a minimum module size of 20. The brain spatial-factor study is probably a Visium-type spatial factorization that dropped genes found in fewer than 20 spots. However, I don't remember how many genes either rule discarded, and those two counts are needed to compute the difference. Any number I gave would be a guess.
contaminated: no

## i11 closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: I can't place either study from memory. The answer depends on numbers specific to each document: how many features (for example, genes) and how many factors or components each model used. The loading matrix has features × factors entries, so the answer would be the brain model's count minus the autoimmune model's count. I don't know those figures for either study, so any number I gave would be a blind guess. As instructed, I used no tools.
contaminated: no

## i13 closed-book (closed-book-solver)

answer: unknown

confidence: low

basis: The question needs two exact figures from two specific papers. One is the ridge hyper-parameter value the battery ageing study's algorithm reached at convergence for its full repeated-measurements model. The other is how far the autoimmune subtype study's selected-model BIC fell below the BIC of its alternative module construction. I don't remember either paper or these numbers, and nothing in the question lets me work them out. Any number I gave would be invented. I made no tool calls.

contaminated: no. No project instructions, memory, document excerpts, hints, bundle metadata or earlier results were present. The only extra context was an automatically attached account email, which has nothing to do with the question.

## i12 blind solve (blind-solver, q03 run's shortcut packet)

I found the answer: the later range spans **3** more pages.

answer: 3

confidence: high

path:
1. **The book.** The only 2011 publication on mixtures cited in more than one paper is the edited book "Mixtures: Estimation and Applications" (2011). Each of two papers cites a different chapter of it, with a different page range.
2. **D01** (docs/arxiv_2601_21106v3.txt), text/D01.txt line 507, in the references: "Frühwirth-Schnatter, S. (2011). Dealing with label switching under model uncertainty. Mixtures: estimation and applications, pages 213–239." The extraction prints the name as "Fr ̈uhwirth". The in-text citation at line 449 reads "Frühwirth-Schnatter (2011) shows identification methods for finite mixture model". The same text is at docs/arxiv_2601_21106v3.txt line 505.
3. **D02** (docs/arxiv_2606_16460v3.txt), text/D02.txt line 679: "Geoffrey J McLachlan, Jangsun Baek, and Suren I Rathnayake. Mixtures of factor analysers for the analysis of high-dimensional data. Mixtures: Estimation and Applications, pages 189–212, 2011." The in-text citation at line 33 reads "[... Baek et al., 2009, McLachlan et al., 2011]". The same text is at docs/arxiv_2606_16460v3.txt line 677.
4. **Which range begins later.** 213–239 (D01) starts after 189–212 (D02). The two ranges are back to back (212 is followed by 213), which fits two consecutive chapters of one book.
5. **Calculation, counting both end pages.**
   - Later range: 239 − 213 + 1 = 27 pages.
   - Other range: 212 − 189 + 1 = 24 pages.
   - 27 − 24 = **3**.

   Simple subtraction without the +1 gives the same result: (239 − 213) − (212 − 189) = 26 − 23 = 3.
6. **Other 2011 items ruled out.** None of these is cited by two papers or matches the description:
   - Ng et al. 2011, "The EM algorithm", Handbook of Computational Statistics, pp. 139–172: only in D02, and it is about the EM algorithm, not mixtures.
   - Liu and Yang 2011, Annals of Statistics, 39(4):2074–2102: only in D01, and it is about model selection.
   - Cojocaru et al. 2011, Maedica 6(4):330: only in D02, and it is about lupus.

minimal_documents: D01 + D02. Both are needed because each gives one of the two ranges, and no other document cites this book, so neither can be replaced.

readings:
- Counting pages with or without the +1 gives the same answer, 3.
- "One 2011 publication" could be read as a single chapter rather than the book. The two cited chapters have different titles and authors, so only the book is shared, and the answer stays 3.
- Reading "begins later" as the paper's posting date: D02 (2606.16460) is a later arXiv posting than D01 (2601.21106), so the later range would be 189–212, which is 3 pages shorter, not longer. That makes it a strained reading and doesn't change the size of the gap.

gaps:
- **Search coverage.** I searched all six text files (D01–D06) for:
  - "2011" (also "20 11", "20-11")
  - "mixture" / "mixtures:" and hyphen-split forms like "mix- tures"
  - "Estimation and Applications", "Mengersen", "Titterington", "Wiley"
  - the cited authors' names (Frühwirth, McLachlan, Baek, Rathnayake)

  D03–D06 had no matches for 2011, mixtures, the book title or these authors.
- **Reading coverage.** I did not read any document from start to finish, only the decisive reference lines and their context. I checked those two lines against the docs/ source files and they match.
- **Format.** The manifest marks all six documents as plain text with no page numbers, and there are no PDFs or layout files, so there were no PDF pages to inspect. The only extraction flaw is the misplaced umlaut in "Frühwirth", which doesn't affect the answer.

contaminated: no. I received only the workspace root, the packet path and the question; no answer, reasoning or source hint leaked.

## i10 blind solve (blind-solver, q03 run's solver-1 packet)

**answer:** 16,879 more genes. The brain study's spot filter discarded 18,900 genes, and the autoimmune study's module-size rule discarded 2,021.

**confidence:** high

**path:**
1. The two studies are D02 (docs/arxiv_2606_16460v3.txt), "Module-structured mixture factor models for molecular subtype discovery…" on rheumatoid arthritis and lupus, and D05 (docs/arxiv_2608_25172v1.txt), "Spatially orthogonal factor models…" with a "human brain spatial transcriptomics case study" from the DLPFC region.
2. **D02, first rule.** Appendix A (text/D02.txt lines 723–725) says: "the top 3000 genes ranked by MAD were retained… The dendrogram was cut at r0 = 0.3, and modules containing fewer than 20 genes were removed. This resulted in 979 genes grouped into 19 modules… The selected model had K = 9 and q = 8."
   - Table 4 (line 585) confirms the selected model: "MAD-based model 9 8 … 19 979".
   - Section 5.1 (line 439) repeats it: "979 highly variable genes organized into 19 co-expression modules."
   - Genes dropped by the module-size rule: 3000 − 979 = **2,021**.
3. **D05, second rule.** Section 6 (text/D05.txt line 783) says the section "contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features… low-expression filtering applied to retain genes with positive expression in at least 20 spots… The low-expression filtering retains 14,638 genes."
   - Appendix 10 (line 1055) repeats both figures: "full-gene analysis (33,538 genes)… filtered analysis (14,638 genes)."
   - Genes dropped by the spot filter: 33,538 − 14,638 = **18,900**.
4. **Difference:** 18,900 − 2,021 = **16,879**. Check: 16,879 + 2,021 = 18,900.
5. The key strings match the original docs/ source files (D02 source lines 721–723 and 575; D05 source line 781). Both sources are plain text, not PDFs, so there were no PDF pages to inspect.

**minimal_documents:** D02 and D05. Neither can be replaced. A search for "at least 20 / fewer than 20 / minimum module / module size / spots" across all of text/ matched only these two documents.

**readings:**
- **WGCNA model instead of the selected model.** D02 line 575 also uses "minimum module size … 20 genes" for its WGCNA comparison, with "4 genes assigned to the grey module" excluded (line 577). That would give 18,900 − 4 = 18,896. The WGCNA model (K = 4, q = 6) was not selected; the selected K = 9, q = 8 model uses the MAD-based modules. So the question's wording points to 16,879.
- **Counting from D02's raw genes.** Starting from all 9,671 genes would also count the MAD screening step: 9,671 − 979 = 8,692, giving a difference of 10,208. That step is not the undersized-module rule, so this reading doesn't fit the question.
- **Possible second removal criterion in D02.** Section 5.1 (line 437) says "Small or weakly defined clusters are removed." Appendix A states only the fewer-than-20-genes rule and attributes the 3000 → 979 drop to it, so 2,021 stands. If some unstated "weakly defined" criterion existed, the module-size rule alone would account for fewer genes. The packet gives no such criterion or figure.

**gaps:**
- D02 reports only the number of genes left (979), not the number removed; 2,021 is derived by subtraction. The same applies to D05 (18,900 is derived).
- Coverage: I read D02 and D05 only in the relevant sections (methods, data, model selection, WGCNA comparison, appendices), not end to end. For D01, D03, D04 and D06 I read only the first 30 lines plus the targeted searches. Those are a leukemia clustering paper, an order-statistics paper, a battery-ageing paper and a null-space SVD paper, none relevant to this question.

**contaminated:** no. I received only the workspace root, the packet path and the question. No answer, reasoning or source hint was supplied.

## i13 blind solve (blind-solver, q03 run's solver-1 packet)

I read D04 (battery) and D02 (autoimmune) in full. The battery model reached λ = 0.0002 at convergence, and the autoimmune study's selected model had a BIC 248,685 lower than the alternative.

answer: λ = 0.0002 at convergence for the full repeated-measurements model. The selected (MAD-based) model's BIC was exactly 248,685 below the WGCNA-based model's BIC (1,280,292 − 1,031,607). The paper rounds this to "∆BIC ≈ 250,000".

confidence: high

path:
1. **Battery study is D04** (`docs/arxiv_2608_19879v1.txt`), "A Repeated Measurements Approach to SoH Battery Modelling…".
   - Line 121 says λ is the ridge hyper-parameter and is chosen using BIC: "introducing a ridge regression term … of the form λθ Tθ into (7). When combined with an appropriate information theoretic measure, such as BIC [xiv], the hyperparameter, λ, can be optimally determined at each iteration".
2. **D04 value for the full model.**
   - Line 379: "Figure 7 presents the residuals for the training data for the full nonlinear repeated measurements model. The RIGLS algorithm converged after just 2-iterations."
   - Figure 7 caption (text line 385; docs line 383): "Training residuals for the full nonlinear repeated measurements model … At convergence 𝜆 = 0.0002. The RIGLS algorithm converged after just two iterations."
   - The original docs/ file gives the same text.
3. **Values I excluded from D04.** These are per-cell level-1 power-law fits, not the full model:
   - Fig. 5, cell 8: "λ = 0.00067"
   - Fig. 6, cell 3: "λ = 0.00048"
4. **Autoimmune study is D02** (`docs/arxiv_2606_16460v3.txt`), RA/SLE dataset GSE45291.
   - §5.2, line 447: "the minimum BIC is attained at K = 9 and q = 8."
   - Appendix A, line 725: "The selected model had K = 9 and q = 8." This is the MAD-HC module construction.
5. **D02 alternative module construction** (§5.5, line 579; Table 4, lines 585–587):
   - Text: "The MAD-based model achieved its optimum at K = 9 and q = 8, with a log-likelihood of −504,975.3 and a BIC of 1,031,607. In contrast, the WGCNA-based model … K = 4 and q = 6 … a much higher BIC (1,280,292). The large difference in BIC (∆BIC ≈ 250,000)…"
   - Table rows: "MAD-based model 9 8 −504,975.3 1,031,607 19 979" and "WGCNA-based model 4 6 −630,297.4 1,280,292 3 975".
   - The original docs/ file has the same rows.
6. **Calculation:** 1,280,292 − 1,031,607 = 248,685.
   - Check: 1,031,607 + 248,685 = 1,280,292.

minimal_documents: D04 and D02. No other document covers either study, so there are no substitutes.

readings:
- **Per-cell λ instead of the full model.** If "battery study's λ" meant a level-1 cell fit, the answer would be 0.00067 (cell 8) or 0.00048 (cell 3). The question says "full repeated-measurements model", which rules these out.
- **Rounded difference.** The paper's own figure is "∆BIC ≈ 250,000". The question asks "exactly", so 248,685 applies.
- **Difference in −2 log-likelihood.** This would be 2 × (630,297.4 − 504,975.3) = 250,644.2. It isn't a BIC difference because it leaves out the penalty terms, so it doesn't answer the question.

gaps:
- Figures are not in the text: D02 Fig. 1 (∆BIC grid) and D04 Figs. 2–9. The values needed are in the captions, the main text and Table 4.
- The sources are .txt files, so there are no PDF pages or `.layout.txt` files to check.
- I didn't read D01, D03, D05 or D06 in full. I only searched them by keyword and checked their titles: Dirichlet-process mixtures for leukemia, order statistics, spatial factor models and null-space SVD. D01's only BIC mention is a general remark. D06's "0.0002" is unrelated to either study.

contaminated: no

## i11 blind solve (blind-solver, q03 run's solver-2 packet)

answer: 17,312 more entries. The brain model's loading matrix has 3,592 × 7 = 25,144 entries and the autoimmune model's has 979 × 8 = 7,832.

confidence: high

path:
1. **Which documents.** D05 (`D:\Dev\Docket\tasks\aq-docket-trial-01\runs\q03-r2-v2-987c25e32fae91ba826f09cae16d35fdb76513d4807bdb0b4345130b165bbd51\solver-2\text\D05.txt`, "Spatially orthogonal factor models…") is the brain spatial-factor study. It describes "a human brain spatial transcriptomics case study" from "a postmortem human brain tissue section" of the DLPFC (L7, L83). D02 (`...\solver-2\text\D02.txt`, "Module-structured mixture factor models…") is the autoimmune subtype study (RA and SLE). A search of all six docs for brain, autoimmune, spatial-factor, tissue-section and loading-matrix terms matched only these two.
2. **What D05 means by the loading matrix.** The rows of Y are genes and the columns are "spatial locations." L31 says "W ∈ R m×k is the loadings matrix." L51 says "placing the spatial dimension as loadings and the time/gene dimension as factors." The orthogonal loadings U have the same m × k size; Laminae-PCA uses "Π ∈ {0, 1}(m×k)" (L1657–1659).
3. **D05, m.** L783: "We analyzed section 151675 from this dataset, which contains expression measurements for 3,592 in-tissue Visium spots and 33,538 gene features." Gene filtering removes genes, not spots, so m = 3,592 in all three analyses (filtered, full-gene and HVG).
4. **D05, k.** L815: "The SOFM model was fitted using k = 7 factors and 400 held-out spots chosen at random on the tissue section."
5. **Held-out spots are still in the matrix.** L470: "we still specify the loadings U at all locations… yielding estimation of the loadings U at all locations." So the matrix has 3,592 × 7 = 25,144 entries.
6. **What D02 means by the loading matrix.** L105: "the loading matrix B ∈ R p×q is constrained as B = SMH." H (G×q) is described separately as "module-level loading direction vectors" (L111).
7. **D02, p.** L439: "the final analysis set consists of 979 highly variable genes organized into 19 co-expression modules." Table 4 gives "Genes 979" (L585) and Appendix A (L725) says "979 genes grouped into 19 modules." As a check, the module sizes in Table 2 add up to 979: 250+105+70+28+23+50+22+66+27+20+69+53+34+24+24+22+35+33+24.
8. **D02, selected q.** L447: "the minimum BIC is attained at K = 9 and q = 8." The same values appear at L451, L579, L585 and L725 ("The selected model had K = 9 and q = 8"). So B has 979 × 8 = 7,832 entries.
9. **Calculation.** 25,144 − 7,832 = 17,312. Check: 3,592×7 = 24,500 + 644 = 25,144; 979×8 = 8,000 − 168 = 7,832.

minimal_documents: D02 and D05. No other document can replace either one; D01, D03, D04 and D06 cover leukemia clustering, order statistics, battery state of health and null-space SVD.

readings:
- **Training spots only for the brain matrix:** (3,592 − 400) × 7 = 22,344, giving a difference of 14,512. The paper rules this out (step 5).
- **Using H (19 × 8 = 152) as the autoimmune matrix:** the difference would be 25,144 − 152 = 24,992. The paper reserves "the loading matrix" for B.
- **Treating genes × factors as the brain loadings:** for example, the filtered 14,638 × 7 = 102,466 gives 94,634. This contradicts D05's explicit choice to put the spatial dimension in the loadings.
- **Counting free loading parameters (about p + Gq = 1,131 per D02 Remark 2):** this is a parameter count, not a count of matrix entries, so it does not fit the question.
- **Other D05 models (PCA, Laminae-PCA, HVG and full-gene runs):** all use 7 components over the same 3,592 spots, so the answer is still 17,312.

gaps:
- The packet has no `Dnn.layout.txt` files and no PDFs (the extraction method is "text"). I could not view D02's Figure 1 (ΔBIC heatmap), but the selected (K, q) is stated in the text several times.
- Not read in full:
  - **D05:** the derivations (about L90–460 and L477–765), the remote-sensing case study (about L865–915), the references and the proofs (L1089–1650).
  - **D02:** the ECM derivations (L165–425), the HPO table (L551–571) and the references.
  - **D01, D03, D04, D06:** only the first 40 lines plus the search results.
- The decisive figures appear consistently wherever the searches found them (3,592 once; 979, K = 9 and q = 8 several times).

contaminated: no. I received only the workspace root, the packet path and the question, with no answer, reasoning or hints. I cannot confirm from inside the session whether it was launched as a non-fork invocation or with omitClaudeMd. No project instructions or memory content appeared in the context.

## i12 closed-book (closed-book-solver)

answer: 6 pages (a guess)
confidence: low
basis: I don't have the collection, so this rests on two assumptions. I assumed the 2011 work is the Wiley book *Mixtures: Estimation and Applications* (edited by Mengersen, Robert and Titterington). I also assumed the two papers cite different chapters of it. From memory, two commonly cited chapters are Gormley & Murphy, pp. 101–121 (21 pages), and Frühwirth-Schnatter, pp. 213–239 (27 pages), which gives 27 − 21 = 6. Both the chapter page numbers and the choice of chapters are uncertain. A different pair, such as McLachlan et al., pp. 189–212, would give 3.
contaminated: no (the session only had an automatically attached account email and environment details, neither related to the question)

Caller note: the closed-book model recalled the book and both cited chapters' page ranges from
memory and named the gold (3) as the alternative pair. Closed-book risk is real: i12 dropped.

## i14 blind solve (blind-solver, q03 run's solver-2 packet)

I found both values in the packet. The battery study's combined fit converged at λ = 0.0002, and the autoimmune study's selected model had a BIC 248,685 lower than the alternative module construction.

    answer: λ = 0.0002 at convergence for the battery model fitted to all 9 retained cells together. The autoimmune study's selected model (MAD-HC modules) had a BIC 248,685 lower than the WGCNA-module model: 1,280,292 − 1,031,607. The paper rounds this gap to "∆BIC ≈ 250,000".
    confidence: high
    path:
     1. D04 is the battery study, "A Repeated Measurements Approach to SoH Battery Modelling of Cyclic Aged Data…" (D04.txt line 5).
        - The ridge term and BIC: "introducing a ridge regression term … λθ Tθ … When combined with … BIC [xiv], the hyperparameter, λ, can be optimally determined at each iteration" (line 121).
     2. Which cells were retained (D04):
        - "cell 5 was deemed to be an outlier and subsequently excluded from the analysis" (lines 289–291).
        - The pooled fit covers "all 9 cells" (line 377).
     3. The combined fit of the retained cells (D04):
        - Line 379: "Figure 7 presents the residuals for the training data for the full nonlinear repeated measurements model. The RIGLS algorithm converged after just 2-iterations."
        - Figure 7 caption (line 385): "Training residuals for the full nonlinear repeated measurements model with cell number as a parameter. The RMSE for these data is 0.191 [%]. At convergence λ = 0.0002."
        - So the value is λ = 0.0002.
     4. Values I excluded (D04): these are fits to single cells, not the combined fit.
        - Cell 8, level-1 fit: "λ = 0.00067 … γ = 1.997" (lines 367 and 373).
        - Cell 3, level-1 fit: "λ = 0.00048, yielding γ = 1.998" (line 383).
     5. D02 is the autoimmune study, "Module-structured mixture factor models…", using RA and SLE data (lines 429–431).
        - "Model selection is carried out using the Bayesian information criterion (BIC), with smaller values indicating a better trade-off" (line 443).
        - The selected model is K = 9, q = 8 (lines 447 and 725).
     6. The alternative module construction is WGCNA (D02 Section 5.5).
        - Line 579: "The MAD-based model achieved its optimum at K = 9 and q = 8, with a log-likelihood of −504,975.3 and a BIC of 1,031,607 … the WGCNA-based model … K = 4 and q = 6 … much higher BIC (1,280,292). The large difference in BIC (∆BIC ≈ 250,000)…"
        - Table 4 (lines 583–587) agrees: "MAD-based model 9 8 −504,975.3 1,031,607 19 979" and "WGCNA-based model 4 6 −630,297.4 1,280,292 3 975".
     7. Calculation: 1,280,292 − 1,031,607 = 248,685.
        - Check: 1,031,607 + 248,685 = 1,280,292.
        - The selected model's BIC is lower, so the requested amount is positive.
    minimal_documents: D04 and D02. No replacements exist: no other document mentions a battery or autoimmune study.
    readings:
     - Reading the BIC gap as the paper's own rounded statement gives about 250,000 instead of the exact 248,685 from Table 4.
     - Reading "fitting all retained cells together" as fits to single cells would give 0.00067 (cell 8) or 0.00048 (cell 3). That doesn't fit the question's wording, so I rejected it.
     - The pooled σ² of 0.00772 is a variance, not the ridge hyper-parameter, so it doesn't apply.
    gaps:
     - The manifest lists all documents as plain text ("method": "text", "pages": null). There are no PDFs or layout files, so I couldn't check original pages.
     - D02 Figure 1 (the ∆BIC grid) is an image with no extracted text. It isn't needed, because Table 4 and line 579 give the BIC values directly.
     - D04's Table 2 test plan has no extracted rows. It isn't needed for this question.
     - Coverage:
       - D04: read in full.
       - D02: lines 425–624 and 711–728, plus targeted searches across the whole file. The rest (mainly method sections and references) was not read in full.
       - D01, D03, D05, D06: checked by keyword searches and their opening lines. They cover leukemia clustering with a Dirichlet process mixture model (D01 says BIC "fall[s] short" there), order statistics, spatial factor models, and null-space SVD. None is a battery or autoimmune study.
    contaminated: no

Caller note: the solver listed the paper's rounded "∆BIC ≈ 250,000" as a second reading of "by how
much". Per the one-clear-answer lesson (a gold that flips between a rounded and an exact stated
figure drew "answered inconsistently"), the quick-test version restores "exactly" from i13 and keeps
i14's "when fitting all retained cells together" (i15).
