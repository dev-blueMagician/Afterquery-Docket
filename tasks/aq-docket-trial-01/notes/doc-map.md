# aq-docket-trial-01 - document map

Written once by `bundle-mapper` from `text/` (and `docs/` for flattened tables and scans).
It is for navigation, like the form's bundle overview: where things are, not what to ask.
Questions quote the documents, never this map.

Line numbers are `text/Dnn.txt` lines (each text file has a 2-line header, so `docs/` line =
text line - 2, verified for D01). Quotes are short and verbatim from `text/`.

## Bundle

- What it is: six unrelated statistics/methods preprints (arXiv stat.ME, stat.AP, math.ST; printed
  dates 5 Aug - 9 Sep 2026, one undated). Topics: Bayesian nonparametric clustering of leukemia
  transcriptomics (D01); module-structured mixture factor model for RA/SLE transcriptomics (D02);
  independence of order statistics and rank indicators / censoring (D03); repeated-measurements
  battery state-of-health model (D04); spatially orthogonal factor model for spatial transcriptomics
  and NDVI remote sensing (D05); null-space SVD error analysis (D06). No document cites or responds to
  another bundle document. No fiscal periods anywhere.
- Documents: 6; ids from `text/manifest.json`; local Dnn = platform Doc n (caller report): D01 =
  arxiv_2601_21106v3, D02 = arxiv_2606_16460v3, D03 = arxiv_2608_05428v1, D04 = arxiv_2608_19879v1,
  D05 = arxiv_2608_25172v1, D06 = arxiv_2608_30374v1.
- Gaps (no unread text; every line of D01-D06 inspected). Source-level gaps, all unresolved because
  no rendered original exists (docs/ are the same plain text):
  - Missing table body: D04 Table 2 test plan (caption only, text 261 / docs 259).
  - Figure-only values (no numbers in text): D01 Figs 1-2 (simulation boxplots) and Fig. 5 panels b-c
    (competitor cluster counts and ARI); D02 Fig. 1 (∆BIC grid; K/q grid bounds never stated) and
    Fig. 2a (module-effect heat map; only prose-quoted α values available); D03 Figs 1-2; D04 Figs
    1-9; D05 Figs 1-23 (incl. top-10 gene lists Figs 6-9 and all simulation errors); D06 Figs 1-6.
  - Flattened tables with unresolved cells: D05 Tables 1-2 (HBB/IGKC factor occurrences; column
    assignment unrecoverable); D06 Table 5 (single run with merged exponents; map parse assumes d.dd
    mantissas); D03 Tables 1-2 (formula exponents lost); D01 Table 1 (legible but split).
  - Referenced but absent: D01 Supplementary material S1-S10 (Negative-binomial simulations, S7
    timings, S8 competitor settings, S9 single-cell application, S10 simulation details).
  - Not inspected by this mapper (outside the bundle folder): the capture's bundle-overview text,
    if any; overview exposure must be checked separately.
- Extraction spot-checks (page counts not applicable - text sources; printed page numerals: D01 18,
  D02 15, D03 20, D04 17, D05 53, D06 31): text/ line = docs/ line + 2 for every document checked.
  Table checks: D01 Fig. 5 runtime row; D02 Table 1 pipe rows and Table 4 row; D03 Table 3 S4 rows;
  D04 Table 1 peak-current row and Table 2 caption; D05 Tables 1-2 rows; D06 Table 3 row 4 and Table
  5 line - all identical to docs. Footnote/detail checks: D01 author asterisk has no footnote text in
  either file; D02 corresponding-author footnote (27) and D03 corresponding-author footnote (21)
  present; D04/D05/D06 have no footnotes (checked e-mail lines / declarations instead). Character
  normalisation: D04 docs uses math-italic letters (e.g. "𝑄𝑘") rendered as ASCII in text/; D01 docs
  "Thi´ebaut" vs text "Thi ́ebaut". Markdown pipe-table rows: D02 457-461, D03 737-744 and 752-759,
  D06 1172-1177 (blank header rows; platform shows them without pipes). ```text fences (capture
  artefacts): D03 153-157, 793-796; D05 171-174, 526-529; D06 1015-1018.
- Provenance: notes/intake.json schema 1, capture_sha256 342b8839...a55ad; all six entries
  "incomplete": false, "gap_characters": 0, "matches_capture": true, captured_sha256 =
  source_sha256 = manifest sha256 for each. Caller report: capture
  AQ-DOCKET-TRIAL-01_2026-10-06_0110.md, "6 of 6 captured in full (320,513 characters)". Manifest
  chars sum to 321,862 (42,043 + 56,522 + 43,739 + 32,539 + 87,867 + 59,152); the counting basis of
  the two totals is not stated. No recovered-source history in intake.json.

## D01 - Scalable Dirichlet Process Mixture Models with Unknown Concentration and Adaptive Covariance for High-Dimensional Clustering Applied to Leukemia Transcriptomics

- Source: docs/arxiv_2601_21106v3.txt -> text/D01.txt, 585 lines, 42,043 chars, method "text", no
  page markers. Printed page numerals survive as stray tokens (p.1 at line 19 ... p.18 at line 585);
  main text pp.1-13, references pp.14-17 (lines 455-571), Appendix A.1 p.18 (lines 575-583).
- Written by: Annesh Pal, Aguirre Mimoun, Rodolphe Thiébaut and Boris P. Hejblum (line 11; text
  renders "Thi ́ebaut", docs "Thi´ebaut"). The "∗" after Hejblum has no footnote text anywhere; no
  affiliation block. Institutions appear only in Acknowledgments (line 453).
- Type, date, edition: arXiv preprint, stamp "arXiv:2601.21106v3 [stat.ME] 9 Sep 2026" embedded
  mid-sentence at line 19. Version 3; no v1/v2 date and no change log printed.
- Period covered: not applicable (methods paper; no fiscal/calendar periods). Cited years 1956-2025.
- Entities and aliases: DPMM = "Dirichlet process mixture models" (13); NPMM = "bayesian
  nonparametric mixture models" (21); VI/CVI = (collapsed) variational inference (25, 113); MCMC
  (13); ELBO "Evidence lower bound" (155); VLL "variational log likelihood" (207); KLmean (213-221);
  ARI "adjusted Rand index" (227; line 403 spells "ajusted"); Sparse DPMM = model M7 ("we call M7 as
  the Sparse DPMM", 247); MLL "mixed lineage leukemia gene, now renamed KMT2A" (267); ALL, AML (37);
  HDDC (Bouveyron et al. 2007), sNNclust/SNN (Ertoz 2002), Leiden ("an upgrade of Louvain", 401-403),
  DBSCAN, HDBSCAN, K-means; NPflow (MCMC slice sampler, Hejblum et al. 2019; 35, 263); vimixr R
  package (13, 37, 261, 579).
- Datasets and designs (main vs secondary):
  - MAIN real data: leukemia gene expression of Armstrong et al. (2002) as filtered by De Souto et al.
    (2008): "a filtered set of d = 2194 expressed genes for clustering N = 72 leukemia samples into
    ALL-MLL-AML sub-types" (273); "Affymetrix data" (271); abstract "72 samples and 2,194 gene
    expressions" (13); intro "2, 194 genes and 72 samples" (37). Download URL ".../armstrong-2002-v2/"
    (581). Per-subtype counts are NOT stated in prose; the Fig. 4b cluster-label row (391) reads as
    digit blocks of 24 / 20 / 28 under the column header "ALL MLL AML" (313) - figure text only,
    visually unverified.
  - Secondary real data (not in bundle): single-cell transcriptomics, "HSC-myeloid differentiation
    axis" (439-441), details only in Supplementary S9.
  - Simulation 1: "N = 100 multivariate Gaussian variables of dimension d = 2 ... Ktrue = 2 clusters,
    where both clusters share the same covariance" over "100 simulation runs", models M1-M8 (227;
    Fig. 1, 229-245).
  - Simulation 2: "increasing dimension to d = 100 ... Ktrue ∈ {4, 6, 8, 10}", models M6-M8 (247;
    Fig. 2, 249-257). N and run count not restated for this design.
  - Timing design: "N = 100, d = 100 Gaussian data with K = 2"; "With 1000 MCMC iterations, the slice
    sampler often has not converged yet" (263).
  - Negative-binomial simulations / sensitivity analyses: named in abstract (13) and intro (35);
    details only in supplementary material (not in bundle).
- Tables: Table 1 (lines 79-109, flattened; caption 109): eight covariance parameterizations M1-M8,
  columns Model / Assumption / Parameterization / Cluster-specific / Prior. M1 Known σI; M2 Known Σ;
  M3 Unknown σI, σ~Γ(g1,g2); M4 Unknown Σ, IW(ν0,V0); M5 Unknown Σ^-1 = LL^t (Cholesky); M6 Σk
  IW; M7 Σk, off-diagonal precision Lap(0,c0), diagonal Γ(a0,b0); M8 Σk, off-diagonal N(c0, 10^-6).
  "global ... (M3, M4, M5), whereas cluster-specific ... (M6, M7, M8)" (109). No numeric tables.
- Numeric results (prose and figure text):
  - Leukemia, strong/empirical-Bayes prior: "Kpost = 3 with ARI score of 0.92" (273);
    "a0 = b0 = 28.9076" (273); "k0 = N +1 = 73" (297); best of random initialisations by VLL (297).
  - Leukemia, weaker prior "a0 = b0 = 10 instead of 28.9076": "Kpost = 4 with ARI score 0.86" (297);
    4th cluster "with one sample replacing a labelled AML sub-type" (297).
  - PCA axes: "PC 1 (16.57%)", "PC 2 (5.58%)" (277-279, repeated 289-291, 303-305).
  - Fig. 5 runtime panel, seconds (409-413): DBSCAN 0.03; HDDC (k-means) 0.14; HDBSCAN 0.04;
    Leiden 0.01; sNNclust 0.05; K-means 0.02; HDDC (random) 0.13; "Sparse DPMM: 65". Prose:
    "Sparse DPMM is significantly slower (∼ 5.91 seconds per iteration)" (403). Iteration count not
    printed (Fig. 5 says iterations "are indicated with mini-bars", 435).
  - Fig. 5 panels b (estimated cluster numbers) and c (ARI) for the seven competitors: chart only, no
    values in text -> unresolved visual (see Gaps).
  - Scaling: "computations scale linearly with the sample size and quadratically with the dimension"
    (263); vs slice sampler "timings that are three orders of magnitude less" (263).
  - Fig. 1/Fig. 2 (simulations): boxplots only, no numeric values in text (231-257).
- Lists: competitor methods (six named at 37: Kmeans, DBSCAN, HDBSCAN, shared nearest neighbourhood,
  Leiden, HDDC; Fig. 5 splits HDDC into "HDDC (random)" and "HDDC (k-means)", giving 7 competitors +
  Sparse DPMM, 409-429). Heat-map marker genes (313-389): ALL markers incl. CD22, CD24; MLL markers
  incl. PROML1, FLT3, ADAM10; AML markers incl. DF, CTSD, BSG (cited in prose at 297).
- Forecasts, guidance, deadlines, effective dates: not applicable.
- Operative definitions, rules, conditions:
  - Collapsed prior p0(zn|α), Eq. (1) (115-129); mean-field q factorisation (143-149); truncation at
    k = K (149, Ishwaran and James 2001); coordinate ascent "ensures guarantee of convergence" (151).
  - Innovation: "updating α based on the number of non-empty clusters t < K only, contrary to the
    mean-field VI implementation from Blei and Jordan (2006)" (177).
  - Model selection: random initialisations chosen by VLL (207-211); G0/hyper-parameter choice by
    KLmean (213-221); "Standard model selection criteria like BIC fall short in this setting due to
    unknown cluster number (Liu and Yang, 2011)" (221); ELBO and VLL "subjects to numerical artifacts"
    (221).
  - "all eight parameterizations and prior choices guarantee that covariance matrices always remain
    semi-definite positive" (109).
  - Consistency condition (cited): consistency "guaranteed as long as the concentration parameter α is
    not fixed but data-driven" (23, Ascolani et al. 2023).
  - Label switching handled by ordering clusters "in decreasing proportions" (447-449).
  - Limitation: hyper-prior on a0 = b0 not used because the Gamma conjugate prior "does not have a
    closed form (Miller, 1980)" (445).
- Hedged claims: "thus appears to capture this biological reality of MLL heterogeneity rather than
  representing a technical artifact" (399; "appears" governs the main claim); "suggesting
  lymphoblastic features" (297; inference from CD22/CD24); M3 good "but only because the data were
  indeed generated accordng to this model" (227-245; qualifier on the M3 result); "Such global
  covariance structures (M3- M5) can prove inadequate for clusters with heterogeneous covariances"
  (245); "M7 slightly better than M8" (247); future work "could be updated simultaneously" / "This can
  provide insights" (441).
- Rounded prose beside exact figures: "three orders of magnitude" (263) has no printed timings in
  main text (S7 only). "∼ 5.91 seconds per iteration" (403) vs Fig. 5 total 65 s.
- Amendments or contradictions (internal, neutral): which labelled subtype the extra-cluster sample
  belongs to/resembles is described differently: abstract "one Mixed Lineage Leukemia outlier sample"
  (13); results "one sample replacing a labelled AML sub-type" (297); "intermediate between ALL and
  MLL" (399); discussion "more numerical proximity towards AML subtype, but ... more biological
  proximity towards ALL subtype" (437). No precedence stated.
- Dates, funding, software, repositories: v3 9 Sep 2026 (19). Funding (453): University of
  Bordeaux's Digital Public Health Graduate School, "PIA 3 through the Agence Nationale de la
  Recherche (Ref: 17-EURE-0019)"; PEPR SN project SMATCH "(Ref: 22-PESN0003)"; computing: MCIA
  (Mésocentre de Calcul Intensif Aquitain) of Université de Bordeaux and Université de Pau et des
  Pays de l'Adour. Software: vimixr on CRAN (579, "with all 8 parameterizations", 261); NPflow
  (263); Zenodo "https://doi.org/10.5281/zenodo.18405687" (583); data URL schlieplab.org (581).
- References (455-571), alphabetical, author-year. Of cross-paper interest: Armstrong et al. (2002)
  Nature genetics 30(1):41-47 (463); De Souto et al. (2008) BMC bioinformatics (491); Bishop and
  Nasrabadi (2006) PRML (471); Blei and Jordan (2006) (473); Blei, Kucukelbir, McAuliffe (2017) (475);
  Bouveyron, Girard, Schmid (2007) HDDC (481; described as estimating GMM parameters "using EM
  iterations", 401); Biernacki, Celeux, Govaert (2002) ICL (469); MacQueen (1967) (539); Ferguson
  (1973) (503); Escobar and West (1995) (495); Neal (2000) (547); Jordan et al. (1999) (527);
  Kurihara, Welling, Teh (2007) (531); Gershman and Blei (2012) (513); Liu and Yang (2011) (533).
  No Tipping and Bishop, McLachlan, Dempster/EM or Lee & Seung citation in D01.
- Referenced but absent: Supplementary material S1-S10 (cited throughout, e.g. 29, 109, 211, 245,
  263, 403, 441) is not in the bundle.
- Coverage: FULL. Read ledger: 1-200, 200-399, 400-585 (all lines inspected). Spot-checks vs docs/:
  title/author line (docs 9), Fig. 4b label row (docs 389), Fig. 5 runtime row (docs 411), "5.91"
  (docs 401) and acknowledgments ref (docs 451) all match.

## D02 - Module-structured mixture factor models for molecular subtype discovery in transcriptomic data

- Source: docs/arxiv_2606_16460v3.txt -> text/D02.txt, 727 lines, 56,522 chars, method "text", no
  page markers; printed page numerals 2-15 (e.g. "2" end of line 47, "15" line 727); running header
  (paper title) repeated at each page top (e.g. 29, 49, 111, 469).
- Written by: Jinran Wu (1, corresponding, "jinran.wu@uq.edu.au", line 27), Geoffrey J. McLachlan (1),
  Saumyadipta Pyne (2,3) (line 5). Affiliations (9): 1 "School of Mathematics and Physics, The
  University of Queensland, QLD, Australia"; 2 "Department of Statistics and Applied Probability,
  University of California, Santa Barbara, CA, USA"; 3 "Health Analytics Network, MD, USA". Author
  contributions (623).
- Type, date, edition: arXiv preprint, stamp "arXiv:2606.16460v3 [stat.AP] 19 Aug 2026" (27). Version
  3; no earlier-version dates and no change log printed.
- Period covered: not applicable. Data-collection dates not stated. Cited years 1993-2026
  (Patino-Martinez et al. 2026, line 659).
- Entities and aliases: RA "rheumatoid arthritis", SLE "systemic lupus erythematosus" (27); MFA
  "Mixtures of factor analyzers" (33); ECM "Expectation–Conditional Maximization" (15; Section 4);
  WGCNA "weighted gene co-expression network analysis" (31); MAD "median absolute deviation" (51);
  MAD-HC (577, 581; MAD screening + hierarchical clustering - expansion not spelled out);
  "MSD-MFM-ECM framework" (577; acronym never expanded); HPO "Human Phenotype Ontology" (39); ADEx
  "Autoimmune Diseases Explorer" (431); GO, KEGG (491); BIC/∆BIC (443-445).
- Datasets and designs (single real dataset, no simulations):
  - MAIN: "entry GSE45291 ... obtained from the ADEx database" (431): "a total of 785 samples,
    including 493 RA samples and 292 SLE samples, with raw expression measurements available for
    9,671 genes" (431). Disease labels "not used at any stage of model fitting, model selection, or
    subtype inference" (433).
  - Preprocessing chain: genes standardised to mean zero, unit variance (47-49, 435); MAD screen
    (51-57); Appendix A: "the top 3000 genes ranked by MAD were retained" (723); average-linkage HC on
    d = sqrt(1 - corr) (61-65); "cut at r0 = 0.3, and modules containing fewer than 20 genes were
    removed. This resulted in 979 genes grouped into 19 modules" (723-725). Main text repeats "979
    highly variable genes organized into 19 co-expression modules" (439) without the 3000 / r0 /
    20-gene settings.
  - Secondary analysis (5.5, 573-603): WGCNA modules "using the same set of pre-selected genes" (577):
    signed network, "default value of β = 6", "minimum module size was set to 20 genes", "merging
    threshold was set to 0.25", Pearson, reassignment and kME filtering disabled, grey module excluded
    (575); "WGCNA resulted in only 3 modules after excluding 4 genes assigned to the grey module"
    (577). Which pre-selected set (3000 or 979) is not said; Table 4 genes 975 = 979 - 4 (map
    arithmetic).
  - No simulation study, no replicate counts.
- Tables (all in text; units are sample counts, gene counts, log-likelihood, BIC):
  - Table 1 (453-461), MARKDOWN PIPE TABLE (header row blank; "Disease | 1 ... 9"): RA 15, 0, 0, 0,
    149, 66, 228, 0, 35; SLE 0, 9, 114, 113, 0, 0, 0, 56, 0 (clusters 1-9). Hand sums: RA 493, SLE
    292, total 785 (match 431). Platform shows these rows without pipes.
  - Table 2 (503-549): 19 modules, columns Module / Size / Mapped genes / themes. Sizes 250, 105, 70,
    28, 23, 50, 22, 66, 27, 20, 69, 53, 34, 24, 24, 22, 35, 33, 24 (hand sum 979); mapped 243, 100, 67,
    28, 23, 47, 22, 57, 25, 20, 65, 52, 33, 24, 22, 21, 34, 33, 23 (hand sum 939; total not printed).
    Theme rows for modules 1, 17, 19 wrap onto a second line (507-509, 541-543, 547-549).
  - Table 3 (561-571): HPO terms for modules 9, 10, 15, 17 only (splenomegaly appears in rows 9 and
    15; EBV viremia in rows 15 and 17).
  - Table 4 (581-587): "MAD-based model 9 8 −504,975.3 1,031,607 19 979"; "WGCNA-based model 4 6
    −630,297.4 1,280,292 3 975" (columns Model K q log-likelihood BIC Modules Genes).
  - Table 5 (593-599): WGCNA clusters 1-4: RA 73, 46, 223, 151; SLE 25, 5, 137, 125 (hand sums RA 493,
    SLE 292; cluster sizes 98, 51, 360, 276).
- Numeric results in prose: minimum BIC "at K = 9 and q = 8" (447, repeated 451, 579, 725); WGCNA
  "K = 4 and q = 6" (579); "∆BIC ≈ 250,000" (579) vs Table 4 exact difference 1,280,292 - 1,031,607
  = 248,685 (map arithmetic); cluster sizes "Cluster 7 with n = 228 and Cluster 5 with n = 149 ...
  Cluster 2 with n = 9 and Cluster 1 with n = 15" (485); module effects (Fig. 2a values quoted in
  prose only): Cluster 2 Module 14 α = −1.51; Cluster 3 "Modules 12-14 α = −1.15, −1.04" (three
  modules, two values, 477); Cluster 5 Module 9 α = 0.92, Module 18 α = 1.08; Cluster 7 Module 9 α
  = 1.09 (479); Cluster 6 Module 9 α = −3.35, Modules 3 and 11 α = 1.68 and 2.71 (481, repeated 483,
  497); Cluster 1 Modules 8-9 α = 0.98, 0.87 (481); Cluster 3 Module 11 α = 1.26 (481). Fig. 1 (∆BIC
  grid) and Fig. 2 (heat map "rounded to two decimal places", 473) have no values in text; grid
  bounds for K and q are never stated.
- Rounded/ranged prose: RA clusters 5 and 7 "effect sizes typically between 0.6 and 1.1" over
  "Modules 5, 8, 9, and 15-18" (477-479) vs "α values typically ranging from 0.5 to 1.1" over
  "Modules 4, 5, and 12" (495). SLE negative signatures "particularly across Modules 3-6 and Modules
  10-15" (475) vs "including Modules 2, 9, 15, and 17" (493). "almost exclusively populated by SLE
  samples" (451, 485) and "primarily composed of RA samples" (451) beside Table 1 zeros and "This
  complete separation" (451).
- Lists: 19 modules (Table 2); RA clusters "1, 5, 6, 7, and 9", SLE clusters "2, 3, 4, and 8" (451,
  485, 493); HPO modules 9, 10, 15, 17 (Table 3).
- Forecasts, guidance, deadlines: not applicable.
- Operative definitions, rules, conditions: model Eqs. (1)-(9) (91-139); "B = SMH" (107);
  identifiability "∥hg∥2 = 1" (113) and Remark 1 constraint Σk πk αkg = 0 (123); common covariance
  "Σ = BB⊤ + D" shared across clusters (121; "Unlike conventional mixtures of factor analyzers that
  allow cluster-specific covariance structures, the proposed model employs a common
  module-structured covariance representation across clusters", 37); Remark 2: loadings reduced from
  "pq free loading parameters" to "approximately p + Gq" (159); ECM E-step/CM-steps 1-6 (161-393);
  ψ "bound ... below by a small positive constant to prevent degeneracy" (389-393); initialisation by
  K-means "with multiple random starts" on module means, s_j = 1, random unit h_g (395-421); BIC
  "smaller values indicating a better trade-off" and ∆BIC definition (443-445). Module construction
  "agnostic" to procedure (77).
- Hedged claims: "may be inadequately captured" (35, about conventional MFA); "suggesting a
  dysregulated or reprogrammed molecular state" (481); "suggesting shared molecular components" (483);
  "suggests that the inferred subgroups reflect biologically meaningful molecular programs rather
  than artefacts" (487); "suggesting enhanced biosynthetic and regulatory activity" (495); "suggests
  potential strategies for patient stratification" (501); WGCNA "suggesting that the reduced number
  of modules leads to a significant loss of information" (579); "these results suggest that the
  coarse module structure produced by WGCNA limits" (603); "may reflect clinically meaningful
  variation" (615). Unhedged: "indicating that the WGCNA-derived modules fail to capture meaningful
  disease heterogeneity" (591).
- Amendments or contradictions (internal, neutral): intro "a comparative analysis of multiple
  module-based methods" (39) vs Section 5.5 comparing two constructions (MAD-HC vs WGCNA, 577). Range
  and module-set differences listed above (475/493, 477-479/495).
- Dates, funding, software, repositories: v3 19 Aug 2026 (27); "supported by the Australian Research
  Council [DP230101671]" (629); "Financial Disclosure None reported" (633); no conflicts (637); code
  "https://github.com/wujrtudou/structured_MFA.git" (717-719, URL split over two lines).
- References (639-713), order of citation, full author names. Of cross-paper interest: McLachlan,
  Do, Ambroise 2004 (665); McLachlan, Lee, Rathnayake 2019 (667); McLachlan, Peel, Bean 2003 (669);
  McLachlan and Peel 2000 "Mixtures of factor analyzers" (671); Baek, McLachlan, Flack "Mixtures of
  factor analyzers with common factor loadings" 2009 (675-677); McLachlan, Baek, Rathnayake 2011 in
  "Mixtures: Estimation and Applications, pages 189–212" (679); Meng and Rubin 1993 ECM (685-687);
  McLachlan and Krishnan 2008 "The EM algorithm and extensions" (689); Ng, Krishnan, McLachlan 2011
  (691); Langfelder and Horvath 2008 WGCNA (663); Tibshirani et al. 1999 (683). No Tipping and Bishop,
  Armstrong et al., Dempster et al. or ARI in D02.
- Coverage: FULL. Read ledger: 1-160, 160-359, 359-508, 503-622, 621-727 (all lines). Spot-checks vs
  docs/: Table 1 pipe rows (docs 457-458), Table 4 row (docs 583), grant (docs 627), Appendix A
  r0/3000 line (docs 721) match.

## D03 - Characterizations of independence between order statistics and rank indicators

- Source: docs/arxiv_2608_05428v1.txt -> text/D03.txt, 878 lines, 43,739 chars, method "text", no
  page markers; printed page numerals 1-20 ("1" at line 23 ... "20" at line 878). Two Markdown
  ```text fences wrap prose (153-157, 793-796; present in docs at 151-155, 791-794) - capture
  artefacts, not content.
- Written by: Roberto Vila (1) and Frederico Almeida (∗1, corresponding) (5); affiliation (7):
  "Department of Statistics, University of Brasília, 70910-900, Brasília, Brazil"; e-mails
  "frederico.almeida@unb.br rovig161@gmail.com" (21).
- Type, date, edition: arXiv preprint v1; TWO printed dates: title block "August 7, 2026" (7) and
  stamp "arXiv:2608.05428v1 [math.ST] 5 Aug 2026" (23). No precedence stated. MSC (2020) "60E05,
  60E15, 62N01, 62G30, 62E10" (15).
- Period covered: not applicable. Cited years 1958-2009.
- Entities and aliases: Z observed time, δ event/censoring indicator, Y failure time, C censoring
  time (27); "independent (or non-informative) censoring" (27); PH proportional hazards, PRH
  proportional reversed hazards (29, Table 2); Kd Kolmogorov distance, Wd Wasserstein distance, W∗d
  normalized Wasserstein distance (397-427, 719-721); MC Monte Carlo (697). No people/organisations
  other than authors, CAPES and cited authors.
- Datasets and designs: NO real data ("Data availability No data were used in this study.", 844).
  Monte Carlo design (693-725): "m = 5", Yi failure time, "Cij , for j ∈ {1, 2, 3, 4}" censoring
  times (701); "Yi ∼ Weibull(α, φ), where α > 0 and φ > 0 are the shape and scale parameters"; "Cij ∼
  exp(μj ), where μj > 0 is the rate parameter" (701); right: Ci = min of the four, Zi = min{Yi,Ci};
  left: Ci = max of the four, Zi = max{Yi,Ci} (703-705); "E[Yi] = φ −1Γ(1+ 1/α)" and "E[Cij ] =
  1/μj" (707-709); "R = 100 MC replications" (713); "six scenarios ... α, φ, and μG = P4 j=1 μj" and
  "a fixed sample size of n = 1000" (715). Example 3.1 (geometric, 281-297) and Example 4.1 (discrete
  PRH, 459-489) are analytic, not simulated.
- Tables:
  - Table 1 (347-369, flattened formulas): 7 families satisfying Theorem 2 (PH): Exponential (common
    params None), Weibull (Shape β), Rayleigh (None), Gompertz (Shape γ), Lomax (Pareto II) ("Scale
    parameter σ"), Burr XII (Shape c), General Cox PH model (Baseline hazard h0). Remark 1 (369-371):
    "αj = λj/λY for the exponential, Weibull, Rayleigh and Gompertz families, αj = κj/κY for the
    Lomax family, and αj = kj/kY for the Burr XII family".
  - Table 2 (545-565, flattened; exponents lost, e.g. Pareto I hazard renders "θσ t(t − σ)"): 7
    families satisfying Theorem 3 (PRH): Power (Support (0,1)), Beta(θ,1) (Second shape parameter
    fixed at 1), Pareto I (Scale σ), Exponentiated Exponential (Rate λ), Exponentiated Weibull
    (Parameters λ, β), Exponentiated Rayleigh (Parameter λ), General PRH model (Baseline r0).
  - Table 3 (727-759), TWO MARKDOWN PIPE BLOCKS with blank header rows; real column labels are plain
    lines 731-735 / 746-750: Scenario, α, φ, μG, E[Zi|δi=1], E[Zi|δi=0], P(δi=1), Wd, W∗d, Kd.
    Right-censoring (739-744): S1 1.0/0.10/0.10: 5.000, 5.000, 0.500, 0.000, 0.000, 0.000; S2
    1.5/0.10/0.10: 6.236, 4.407, 0.473, 0.341, 0.055, 0.196; S3 0.5/0.10/0.10: 2.918, 6.495, 0.546,
    2.682, 0.413, 0.325; S4 1.0/0.05/0.01: 16.667, 16.667, 0.833, 0.000, 0.000, 0.000; S5
    0.5/0.05/0.05: 5.836, 12.991, 0.546, 2.586, 0.199, 0.325; S6 1.5/0.05/0.20: 6.005, 4.092, 0.131,
    0.394, 0.066, 0.205. Left-censoring (754-759): S1 15.000, 15.000, 0.500, 0.000, 0.000, 0.000; S2
    11.531, 16.236, 0.527, 30.594, 1.884, 0.192; S3 40.514, 12.918, 0.454, 30.934, 0.764, 0.320; S4
    36.667, 116.667, 0.167, 346.532, 2.970, 0.464; S5 81.027, 25.836, 0.454, 57.915, 0.715, 0.320; S6
    19.877, 11.005, 0.869, 32.643, 1.642, 0.360. Three decimals throughout. Platform shows these rows
    without pipes.
  - Figures 1-2 (785, 789): conditional survival curves, chart only, no values in text.
- Numeric prose vs table: right S1/S4 "conditional distributions ... coincide" with distances zero
  (761-769); S2/S6 (α = 1.5) E[Z|δ=1] > E[Z|δ=0] (771-775); S3/S5 (α = 0.5) opposite (775-779);
  left S4 "Kolmogorov distance being the smallest" (791-798); left: "values of W∗ d were lower ...
  decreasing hazard rate, 0 < α < 1, than with an increasing hazard rate, α > 1. In contrast, the
  Kolmogorov distance displayed the opposite pattern" (800) - table: Kd S3 0.320 > S2 0.192 but S5
  0.320 < S6 0.360; "(3, 5) yield identical Kolmogorov distance values" (800; 0.320/0.320 left,
  0.325/0.325 right).
- Operative definitions, theorems, conditions:
  - Theorem 1 (45-61): rank indicator δi; W_k,i(x) = P(δi = 1 | Xi = x); assumes E[W_k,i(Xi)] > 0;
    S∗ = S_k:m "if and only if Z and δi are independent". Props 2.1-2.2 (123-259).
  - Corollary 3.1 multiple right-censoring iff condition (269-279); Theorem 2 PH sufficient
    condition "hCj(t) = αjhY (t)" (303-307); "Theorem 2 applies to any family of absolutely
    continuous distributions that is closed under proportional hazards" (345); Prop 3.1 single
    right-censoring: independence "if and only if there exists a constant α > 0 such that hC(t) =
    αhY (t)" (377-379), α = 1/E[SC(Y)] - 1 (397).
  - Corollary 4.1 left (437-457); Theorem 3 PRH sufficient "rCj (t) = βjrY (t)" (493-499); Prop 4.1
    "for m = 2" iff (581-585), β = [1 − P(δ = 1)]/P(δ = 1) (601).
  - Measures: "Both measures satisfy 0 ⩽ Kd, W∗ d ⩽ 1, and Kd = 0 =⇒ W∗d = 0" (427, right) and
    "Both measures take values in the unit interval, 0 ⩽ Kd, W∗ d ⩽ 1" (689, left).
  - Simulation conclusions: left-censoring "Although setting the Weibull shape parameter to (α = 1)
    is necessary, it is not sufficient ... independence is achieved only when the additional
    condition φ = μG (Scenario 1)" (791); "for the distributions considered here, no combination of
    the scale parameters φ and μG can ensure independence when α ̸= 1" (808); right-censoring "The
    necessary and sufficient condition is that both the failure times Yi and the censoring times Cj
    ... are exponentially distributed" (808); left "independence occurs only when the failure and
    censoring times are independent and identically distributed, which, under the adopted
    parametrization, corresponds to φ = μG" (810).
- Hedged claims: "can be interpreted as a direct consequence of the memoryless property" (765-767);
  "virtually coincide" (769); "potentially more efficient inferential procedures" (29); future work
  "may provide a useful foundation" (832); "deserves further attention" (830).
- Amendments or contradictions (internal, neutral): (a) unit-interval bound for W∗d (427, 689) vs
  left-censoring Table 3 W∗d values 1.884 (S2), 2.970 (S4), 1.642 (S6) (755-759); (b) two dates
  (7 vs 23); (c) general results (Theorem 2/Table 1 families beyond the exponential; Prop 3.1 "if and
  only if" PH) vs Section 5.1 "The necessary and sufficient condition is that both ... are
  exponentially distributed" (808, simulation-scoped) and conclusion "the minimum operator requires
  only proportional hazards structures—and, in the classical case, exponential" (824); (d) line 345
  says αj "is simply the ratio of the corresponding scale (or rate) parameters" while Table 1 lists
  Lomax's σ as the common "Scale parameter" and Remark 1 gives αj = κj/κY; (e) φ called a "scale"
  parameter (701) beside E[Yi] = φ −1Γ(1+ 1/α) (707). No precedence stated for any.
- Dates, funding, software, repositories: "financed in part by CAPES (Finance Code 001)" (838); no
  conflicts (840); ethics not applicable (836); keywords list "R software" (13) but no package, code
  or repository is named anywhere.
- References (846-876): 13 entries (Aalen 1978; Arnold, Balakrishnan, Nagaraja 2008; Balakrishnan
  and Rao 1998; Cox 1972; Cox 1975; David and Nagaraja 2003 "3 edition"; Fleming and Harrington
  1991; Gupta and Gupta 1998; Kalbfleisch and Prentice 2002; Kaplan and Meier 1958; Klein and
  Moeschberger 2006 "2 edition"; Shorack and Wellner 1986; Villani 2009). No overlap with other
  documents' clustering/factor literature.
- Coverage: FULL. Read ledger: 1-180, 180-379, 379-578, 578-747, 746-878 (all lines). Spot-checks
  vs docs/: date line (docs 5), Table 3 S4 rows (docs 740, 755), CAPES (docs 836), fences (docs
  151-155, 791-794) match.

## D04 - A Repeated Measurements Approach to SoH Battery Modelling of Cyclic Aged Data in a Laboratory Environment

- Source: docs/arxiv_2608_19879v1.txt -> text/D04.txt, 635 lines, 32,539 chars, method "text", no
  page markers; printed page numerals 1-17 ("1" line 3 ... "17" line 629). The docs original uses
  math-italic Unicode letters (e.g. docs 249 "𝑄𝑘", "𝑄𝑙𝑜𝑠𝑠") that text/ renders as plain "Qk",
  "Qloss" (251) - quotes containing symbols may not match the platform's characters.
- Written by: M. Cary (1; "m.cary@lboro.ac.uk", 7) and Charles Bokor (2;
  "charlesbokor@outlook.com", 9). Affiliations: 1 "Department of Aeronautical and Automotive
  Engineering, Loughborough University, Loughborough, LE11 3TU, UK" (11-13); 2 "School of
  Engineering, Computing and Mathematics, Oxford Brookes University Oxford OX33 1HX, UK" (17).
- Type, date, edition: preprint (file name says arXiv 2608.19879 v1), but NO arXiv stamp, version
  line or date is printed anywhere in the text. "License: CC-BY 4.0" (31). Latest cited date "Sep
  2022" (ref xi, 613).
- Period covered: not applicable; no calendar dates for the experiments. Ageing time axis in days
  ("in the interval [200,250] days", 411).
- Entities and aliases: SoH "state of health" (27); PLM "power law model" (281-285); RIGLS
  "regularized iterative generalised least squares" (121); FAST-LTS "Least Trimmed Squares" (355,
  Hawkins and Khan [xxi]); BIC [xiv] (121, 517); NCA "Nickel Cobalt Aluminum" (207); BOL, SOC (243);
  EV "electric vehicle" (423); L1/L2, LCI/UCI, LPI/UPI (413). Zülke et al [xvi] (199) vs "A. Aragon
  Zulke" co-author of ref [xi] (613) - same surname, identity not stated. Author "Cary" also cited
  as refs ii, xi, xx.
- Datasets and designs (single laboratory dataset, no simulation):
  - Cells: "The training data comprised SoH profiles for 10 cells" (21); cells drawn from a batch of
    "55 pristine cells" screened by Zülke et al [xvi], "mean nominal capacity of these cells as 4.73
    ± 0.025 [Ah]" at "one third C-rate and 25 [oC]" (199-201); "All test cells were selected randomly
    from this batch" (201).
  - Protocol: "All data were collected at 25 [oC] and a constant discharge current of 2 [A] was
    applied throughout. In contrast, the applied charge current during cycling was varied" (251);
    "After every 50 cycles, a check-up test" (251); Qloss = 100 × (Q0 − Qk)/Q0, Eq. (16) (253-255);
    "The procedure was repeated until failure" (259). Table 2 caption: "The charging current is varied
    from 1 to 5 [A]. Two cells are tested at each condition." (261).
  - Exclusions: "cell 5 was deemed to be an outlier and subsequently excluded from the analysis"
    (289-291, at ai = 3 [A]); FAST-LTS point exclusions: cell 8 "(10.75, 3.80)" (367); cell 3
    "(10.75, 4.01)" and "(490.5, 19.50)" (371). Later "over all 9 cells" (377). Step 1 "fitting each
    individual ageing profile for all 10 cells tested" (327). Observations per cell and total N are
    never printed.
  - Cell-to-current mentions: Cell 1 at 1 [A] (309), Cell 2 at 1 [A] (413), Cell 3 at 2 [A] (383),
    Cell 8 at 4 [A] (367, 373), cell 5 at 3 [A] (289-291).
- Tables: Table 1 "Cell Specification Table" (203-249): NCA cathode; Graphite/Silicon anode; typical
  capacity (4.2 V, C/3 discharge) "4.8 [Ah]"; typical energy "17.4 [Wh]"; nominal voltage "3.62
  [V]"; Vmin 2.5 [V]; Vmax 4.2 [V]; energy density "256 [Wh/kg]; 717 [Wh/L]"; standard charge C/3;
  max charge 1 C; standard discharge C/5; max discharge 2 C; peak discharge (30s, 10s) at 50%SOC and
  BOL "42 [A]/54[A]"; weight "68 [g]"; cylindrical. Table 2 (test plan): CAPTION ONLY (261) - body
  absent in docs original too (docs 259 caption then 2.1 heading) -> missing source content.
  Figures 1-9: captions only (259, 309-313, 317, 341, 373, 383, 385, 413, 417).
- Numeric results: cell 8 "(Ai, Bi ) = (1.383, 1.1011) ... λ = 0.00067, yielding γ = 1.997" (373;
  prose 367 "from 2, for the unregularized fit, to γ = 1.997"); cell 3 "(1.374, 1.1034) ... λ =
  0.00048, yielding γ = 1.998" (383); pooled level-1 variance "σ 2, was 0.00772" (375-377); full
  model "The RIGLS algorithm converged after just 2-iterations. The RMSE for the trained model was
  0.191 [%]" (379; caption 385 adds "At convergence λ = 0.0002" and "two iterations"); level-2
  correlation "C = [ 1 −0.743 −0.743 1 ]" (397); "T 1/2 = diag{0.0374 0.0233}" (403-405); full
  level-2 parameter vector "∈ R12" (305); B-spline "order 4 with a single knot", 5 basis functions
  per parameter (297); m = d + 1 (299).
- Rounded prose beside exact figures: abstract "SoH is accurately predicted to ±0.191% for SoH ∈
  [0,20]" (21) vs body "RMSE for the trained model was 0.191 [%]" (379) / "training RMSE of 0.191 [%]"
  (421) and "Validation data was not available to test the predictive capability of the model for
  previously untried configurations" (379). Iterations: "In our experience convergence occurs after
  roughly 3-5 iterations" (351, general) vs "converged after just 2-iterations" (379, this case).
- Operative definitions, rules, conditions: longitudinal data definition (27); two-stage model
  Eqs. (1)-(2), "Throughout, we will assume Σi = Ini" (53), "ei and bi are independent" (63); first-
  order Taylor approximation about E[bi] = 0 (71-73, Sheiner, Rosenberg and Melmon [ix]); negative
  log-likelihood Eq. (7) (111-119); ridge term λθ^Tθ with BIC-based fixed-point λ, Eq. (8) = (A13)
  (121-127, 561-565); fixed-point Definition and convergence Theorem "|h′(λ)| ≤ k < 1" (131-141),
  error bound Eq. (9) (147-151); delta-method CI/PI Eqs. (10)-(15) (153-195); PLM Eq. (17) "s.t. Ai >
  1, Bi > 0" with i.i.d. N(0, σ2) errors, "all data receives the same weight of unity" (267-275); BIC
  defined "BIC = 2L p(ω, λ, σ2) + γlog(N)" with "γ = trace(S(λ)) denotes the effective number of
  parameters" (517-525); D = M² gives eigenvalues λi² that "cannot be negative ensuring positive
  definite D" (Appendix B, 567-589); FAST-LTS S ∈ [0.5ni, ni] (355-363).
- Hedged claims: second cell-3 outlier "may indicate the cell is entering into a period of rapid
  capacity decay ... If so, this observation is not consistent with the PLM formulation.
  Consequently, this observation should be excluded" (371; hedge on the interpretation, exclusion
  stated firmly); "There appears to be an outlying observation at charging current = 3 [A]" (317,
  Fig. 3 caption) vs firm exclusion of cell 5 (289-291); "the residual pattern suggests the model
  exhibits small systematic errors" (379); "Extensions to time dependent covariate [iii] protocols may
  address the real-world in-service analysis problem" (423); FAST-LTS "may converge to a local rather
  that a global minimum" (361); "To our knowledge, this is the first time" (421).
- Amendments or contradictions (internal, neutral): abstract "aged at various constant discharge and
  charge current cycles" (21) vs body discharge fixed at 2 [A], charge varied (251, 259, 261); 10
  cells (21, 327) vs 9 cells after excluding cell 5 (291, 377); "Differentiating (19) with respect to
  λ" (525) where Eq. (19) is "m = d + 1" (299) and BIC is (A9); unresolved "[refs]" placeholder (27);
  duplicate references i = vii (Lindstrom & Bates 1990) and x = xv (Burden, Faires, Reynolds 1981)
  (593-619). No precedence stated.
- Dates, funding, software, repositories: no funding statement, no software or code repository
  named. Ref xi "Sep 2022" Loughborough conference (613); Zülke et al. "(2021)" (621).
- References (593-635): roman numerals i-xxiii (23 entries, two duplicated). Of cross-paper interest:
  Schwarz (1978) BIC [xiv] (617); Hoerl & Kennard ridge 1970 [xiii] (615); Searle 1982 [xxiii] (635);
  Davidian & Giltinan [iii, v, vi]. No overlap with the clustering/factor-model reference lists.
- Coverage: FULL. Read ledger: 1-170, 170-369, 369-508, 507-636 (all lines). Spot-checks vs docs/:
  protocol paragraph (docs 249), Table 2 caption with no body (docs 259-261), Table 1 peak-current
  row (docs 239-241), σ2 line (docs 375) match apart from math-italic normalisation.

## D05 - Spatially orthogonal factor models for spatial transcriptomics and remote sensing data

- Source: docs/arxiv_2608_25172v1.txt -> text/D05.txt, 1715 lines, 87,867 chars, method "text", no
  page markers; printed page numerals 1-53 ("1" line 9 ... "53" line 1715). Main text pp.1-27,
  references pp.28-32 (921-1049), appendices 10-14 pp.33-53 (1053-1713). ```text fences around
  formula fragments (171-174, 526-529; docs 169-172, 524-527) are capture artefacts.
- Written by: Dan Cunha (1), Lukas M. Weber (2), Mark Friedl (3), Luis Carvalho (1) (5);
  affiliations (5): 1 "Department of Mathematics and Statistics, Boston University"; 2 "Department
  of Biostatistics, Boston University School of Public Health"; 3 "Department of Earth and
  Environment, Boston University". No e-mails, no corresponding-author mark. Name matches in cited
  works (identity not stated): "Weber, L. M." in Maynard et al. (2021) (975) and Weber et al. (2023)
  (1031); "Friedl, M. A." in Zhang et al. (2003) (1043).
- Type, date, edition: arXiv preprint, stamp "arXiv:2608.25172v1 [stat.ME] 25 Aug 2026" (9). v1.
- Period covered: NDVI single-year study "01/08/2022-12/24/2022" and 40-year study "01/08/1982-
  12/24/2022" (887; month/day/year format). AVHRR collecting "since 1981" (875); Pinzon et al.
  (2023) title "gimms-3g+, 1981–2022" (997).
- Entities and aliases: PCA/probabilistic PCA (17, 27-39); SOFM = spatially orthogonal factor model
  (687, 795; acronym first used without expansion at 687); MAP (147); MM-EM
  "minorizationmaximization-within-EM" (79); DLPFC "dorsolateral prefrontal cortex" (83); HVG
  "highly variable gene" (783); Laminae-PCA (807-809, Appendix 12); SpatialPCA (Shang and Zhou 2022),
  MEFISTO (Velten et al. 2022), nonnegative spatial factorization (Townes and Engelhardt 2023),
  GraphPCA (Yang et al. 2024) (797); NDVI, RED, NIR (869-873); AVHRR (875); GIMMS "Global Inventory
  Modeling and Mapping Studies" (877-879); 10x Genomics Visium (773, 779); genes HBB, IGKC, NPY (811).
- Notation/definitions relevant across papers: Y is n×m with rows = "observations" (time points
  for remote sensing; genes for spatial transcriptomics) and columns = spatial locations (29); "we
  will use the term 'observations' for the rows of Y" (29); S := Y′Y/n (37-39); orthogonal spatial
  patterns "maximally different in the sense that their inner product is 0" (51); Laminae-PCA U
  "orthonormal, i.e. U′U = Ik" (1659); pve = tr(V′RV)/tr(R) (1669-1671); Figure 2 caption uses
  per-factor "Proportion variance explained pve = diag(U ′SU)/tr(S)" and "Percent variance explained
  pve = diag(U ′ΣU)/tr(Σ)" (839).
- Datasets and designs (main vs secondary):
  - DLPFC (main case study, Section 6): Maynard et al. (2021) "12 tissue sections from 3 donors"
    (775-777); Visium spots "approximately 55 μm in diameter and spaced approximately 100 μm
    center-to-center, with up to approximately 5,000 spots per tissue section" (779-781). "We analyzed
    section 151675 from this dataset, which contains expression measurements for 3,592 in-tissue
    Visium spots and 33,538 gene features" (783). Three analyses (783): filtered "positive expression
    in at least 20 spots" -> "The low-expression filtering retains 14,638 genes"; full-gene "all
    33,538 genes"; "top 3,000 HVGs". "We treat the filtered analysis as our main analysis ... and
    include the full-gene analysis in the appendix" (783). Normalised, log-transformed, mean-centred
    per gene (783-785).
  - NDVI (Section 7): GIMMS "bi-weekly NDVI global measurements at 1/12 degrees spatial resolution"
    (877); 1-year study "239318 spatial locations and 24 temporal observations" (887); 40-year PCA
    benchmark "984 temporal observations" (887); sub-Saharan conterminous Africa; mean spatial vector
    subtracted (887). Earlier description "a 15-day maximum value composite of daily imagery" (53).
    Map arithmetic: 984/24 = 41 and the dates span 1982-2022 (41 calendar years) while the text says
    "40-year" / "40 years" (887, 895-897) - wording vs count, not a stated conflict.
  - Simulation (Section 5, 717-769): three covariance models "a stationary model, a nonstationary
    model, where the length scales evolve smoothly ... and a shape model, where there is a circle"
    (721); "two spatial domains of 400 and 2500 spatial locations, along with sample sizes (200, 500,
    1000, 5000, 10000). There are two σ 2 ∈ {5, 10}" (721-725); "We take k = 3"; "there are twenty
    replicate simulations"; "maximum spatial lags of 2 and 20, initial length scales λi ∈ {1, 3, 5}
    and sill values φ ∈ {1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000}" (725). Timing study
    (Fig. 1 caption, 767): "run on a single core", "3000 samples/features per dataset and k = 3
    factors". Appendix 14 (1677-1713): Figures 12-23 = 12 figures, models "circular", "stationary",
    "left-to-right", "σ = 10.0" or "σ = 5.0", max lag 20 or 2, ALL "size of spatial domain equal to
    400".
- Tables: Table 1 (851-857, filtered) and Table 2 (859-865, 3000-HVG): occurrence of HBB and IGKC
  in top-10 positive/negative gene lists per factor for SOFM / Laminae / PCA. FLATTENED in text and
  docs original alike (docs 853-863): six column headers but rows read "IGKC Factor 2 Factor 4
  Factor 2" / "HBB Factor 7 Factor 3 Factor 7" (Table 1) and a longer run (Table 2, continuation line
  865 "Factor 5 Factor 6 Factor 7 Factor 4") -> cell-to-column assignment UNRESOLVED (no
  rendered original available). Prose anchors: SOFM filtered Factor 7 has HBB as largest negative
  (825); Laminae-PCA filtered has neither gene (827); SOFM HVG Factor 6 HBB largest positive and
  IGKC largest negative (829); SOFM HVG Factor 7 HBB and IGKC top two negative (831).
  Algorithm 1 (729-763). Figures 1-23 chart/image only.
- Numeric results: DLPFC "k = 7 factors and 400 held-out spots" (815); sill domain "{1, 5, 10, 50,
  100, 500, 1000, 5000}", "φˆ = 500 for the filtered and full-gene analyses, and φˆ = 100 for the
  3000-HVG analysis" (815); length-scale domain "{0.5, 1, 2, 4}" (815-817); "The algorithm ran on 32
  cores in 38.51 seconds for the filtered analysis, 88.92 seconds for the full-gene analysis, and
  18.51 seconds for the 3000-HVG analysis" (819); P-spline knots "rx = ry = 10" with GCV (711); prior
  df "ν which we take to be equal to m" (143). NDVI: "The first component of both models captures
  about 50 percent of the total variance" (891-895); length scales "range from 0 to 3 degrees"
  (893). No numeric simulation errors in text (Fig. 1 only).
- Lists: DLPFC SOFM factor descriptions 1-7 (823-825); Laminae-PCA column order "white matter, layer
  3, layer 1, layer 5, layer 2, layer 6, and layer 4" (847, 1083); Maynard non-laminar genes "HBB,
  IGKC, and NPY" (811) - only HBB and IGKC are tracked afterwards (811-831, Tables 1-2); "Four
  additional immunoglobulin genes" unnamed (829); comparator methods (797).
- Operative definitions, theorems, conditions: Eq. (1) model with orthogonal U (55-59); Proposition 1
  prior (93-139), "conditional prior of U|L, σ2, Σ is a matrix-Fisher-Bingham and conjugate" (139);
  Theorem 1 "for ν ≥ m" MAP U = k eigenvectors of (S + (1/n)Σ) with largest eigenvalues (147-151);
  "The MAP values for L, σ2 are more difficult to prove and we leave this step for potential future
  research" (155); eigendecomposition "cubic computational complexity" in m (79), MM-EM linear (79,
  907); Σ not optimisable directly because "the normalizing constant of this prior is difficult to
  compute" (143, 466); held-out validation (464-689); Laminae-PCA definition (807-809, 1655-1665);
  "no model can perform better than PCA on the empirical covariance matrix S in terms of pve
  (Jolliffe and Cadima, 2016)" (1673; also "PCA serves as an upper bound", 839, 891).
- SpatialPCA comparison (797-799): stationary vs nonstationary prior; SpatialPCA bandwidth
  "Sheather-Jones method ... for datasets with at most 5,000 spatial locations and Silverman's
  rule-of-thumb ... for larger datasets"; "The dense SpatialPCA implementation includes quadratic
  operations in the number of spatial locations, although low-rank approximations and a sparse-kernel
  option are also available" (799).
- Hedged claims: "There are two main approximations made in the Algorithm 1 that may affect the
  study results" then "estimation of U, L, σ2 is not sensitive to these approximations" (727-769);
  "We report the following exploratory findings" (821); "The fourth factor potentially captures a
  non-laminar factor" (823); "appears to correspond primarily to layer 4" (823); Factor 7 "appears to
  be non-laminar" (825); HVG Factor 6 "appears to be non-laminar" (829); length scales "appear
  qualitatively strongest in the first cortical layer" (833); "may contribute to major modes of
  covariation" (841); "Although this Gaussian modeling assumption is an approximation" (785); HVG
  selection "may remove some genes with spatial expression patterns" (783); "PCA may struggle ...
  may prove useful" (887); "To our knowledge ... the first of its kind" (909); "not inconsistent
  with a related model fit to 40 years of data" (911-913).
- Amendments or contradictions (internal, neutral): line 769 "Appendix 14 contains additional
  studies for varying values of σ, spatial domain size, as well as different maximum spatial lags"
  vs every Appendix 14 caption at domain size 400 (1681-1713); Section 5 "σ 2 ∈ {5, 10}" (723-725)
  vs captions "σ = 10.0" / "σ = 5.0"; model names "nonstationary"/"shape" (721) vs "left-to-right"/
  "circular" (1681-1713); simulation sill grid to 50000 (725) vs DLPFC grid to 5000 (815). No
  precedence stated.
- Dates, funding, software, repositories: no funding/acknowledgment statement; code
  "https://github.com/daniel-s-cunha/SOFM" and "pip install sofm" (919).
- References (921-1049), author-year. Of cross-paper interest: Tipping and Bishop (1999)
  "Probabilistic principal component analysis" JRSS-B 61(3):611-622 (1023; cited 29, 37); Pearson
  (1901) (989); Hotelling (1933) (957); James (1964) (967); Muirhead (1982) (981); Hunter and Lange
  (2004) MM (965); Schönemann (1966) (1001); Jolliffe and Cadima (2016) (969); Absil et al. (2008)
  (923); Eilers and Marx (1996, 2003); Craven and Wahba (1978). "Jun, M. and Stein, M. L. (2008)"
  has no venue (971). No McLachlan, Armstrong, Bishop-Nasrabadi or Dempster citations.
- Coverage: FULL. Read ledger: 1-170, 170-399, 399-628, 628-857, 857-1056, 1056-1275, 1275-1504,
  1504-1715 (all lines). Spot-checks vs docs/: Tables 1-2 rows (docs 853-863), fences (docs 169-172,
  524-527), NDVI and section lines (docs 781, 885) match.

## D06 - Compact and Infinite-Order Error Analysis for Null-Space SVD Estimation

- Source: docs/arxiv_2608_30374v1.txt -> text/D06.txt, 1361 lines, 59,152 chars, method "text", no
  page markers; printed page numerals 1-31 ("1" line 21 ... "31" line 1361). ```text fence at
  1015-1018 is a capture artefact. Superscripts are flattened throughout tables (e.g. "2.62 × 101"
  = 2.62 × 10^1; "3.84 × 100" = 3.84 × 10^0).
- Written by: Xin Li, Jonathan Cohen, Rami Puzis (5). No affiliations, e-mails, funding statement,
  acknowledgments or code URL anywhere in the text.
- Type, date, edition: TWO printed dates: "September 1, 2026" (7) and stamp "arXiv:2608.30374v1
  [math.ST] 31 Aug 2026" (21). v1; no precedence stated. Seed "20260803" (1160, 1166) is a random
  seed, not a date statement.
- Period covered: not applicable.
- Entities and aliases / notation: Z = HX ∈ R^{m×τ}, H ∈ R^{m×n}, X ∈ R^{n×τ}, E fixed standardized
  noise, σ noise scale (31-33); r = rank(Z), q0 = m − r (33); "reducing the retained nullity" = q <
  q0 (49); η, ε (51-61); Remp,q / Rgen,q fixed-realization risks vs εemp,q / εgen,q expectations (61);
  W "effective splitting" matrix Λ2 = Q0^T(A2 − A1GA1)Q0 (423-427); ∆rank, δvis, Cvis, σlo, σhi
  (659-671); h⋆ = ∥H∥2, ζ = σ/h⋆ (681); ρq projector radius, ρgen,q risk radius (999-1032); BBP =
  "Baik–Ben Arous–Péché transition" (1283). Unexplained "portfolio template" (461) / "template's"
  (619, 1325). Symbol K reused for series order and for "K = 9 adjacent tail margins" (1187).
- Datasets and designs: NO real data; all numeric work is simulation ("experiment notebooks", 1104):
  - 9.1 compact-formula test: "m = 6, τ = 50, σ = 0.2, random seed 17, and construct Z with rank(Z)
    = 5" (1110); "λSVD = 1.76378905836" (1110).
  - Seed-8 convergence-radius realization (7.1, 9.2, 9.4): "random seed 8, m = 6, n = 1, q0 = 5,
    and τ = 100" (1036; 1132 "m = 6, n = 1, τ = 100"); H vector printed (1036); "set H = H0/∥H0∥F"
    (1132).
  - 9.3 ensemble (separate): "Set m = 7, n = 3, q0 = 4, τ = 100" (1146), "draw H0 with seed 8", "H =
    2H0 ∥H0∥F", "h⋆ = ∥H∥2 = 1.57970420" (1146-1150); "averages over 100,000 independent training
    realizations" (1152); calibration seed 73119 over "0.15 ≤ ζ ≤ 0.45 and 5 ≤ ζ ≤ 10" (1154);
    validation seed 20260803 "121 logarithmically spaced values over 10−2 ≤ ζ ≤ 10" (1160);
    dedicated run "seed 20260803, 3,000,000 independent trials, and ζ = 1" (1166); "a separate
    200,000-trial check" (1185). "This ensemble experiment is separate from the fixed seed-8 study of
    convergence radii" (1146) although its H0 is also drawn with seed 8.
- Tables (all simulation outputs):
  - Table 1 (1060-1064, flattened, sentence split around it): noise level 0.8ρgen,5: orders 20/40/
    80/120 = 1.62 × 10−5, 1.91 × 10−6, 1.17 × 10−11, 1.33 × 10−14; 1.2ρgen,5: 4.92 × 10−2, 2.62 ×
    101, 1.10 × 103, 2.49 × 107.
  - Table 2 (1114-1122): M = (ZZT)+EET: 4.51 × 10−16, 1.47 × 10−14; M = (ZZT)EET: 3.28 × 10−1,
    1.88 × 101; "cond(Q) = 1.31077".
  - Table 3 (1168-1179), MARKDOWN PIPE TABLE with blank header row; labels on plain lines
    1168-1170 (SVD rank; Ê[u^T B u]; Σk=5..7 Ω; Σk=6..7 Ω; Ωi7): rank 1: 0.131298, 0.13838,
    0.07337, 0.01582; rank 2: 0.160640, 0.17201, 0.09029, 0.01820; rank 3: 0.204187, 0.22247,
    0.11585, 0.02148; rank 4: 0.283649, 0.31508, 0.16321, 0.02720. Caption: "at the representative
    middle-noise point σ = ∥H∥2" (1179). Platform shows rows without pipes.
  - Table 4 (1223-1235): q, Re s⋆, Im s⋆, ρq, collision: 5: −1.16405872, −0.43982812, 1.24437996,
    (4, 5); 4: −1.08848353, −0.67174264, 1.27907567, (3, 5); 3: −1.21293931, −0.24914546,
    1.23826299, (2, 3); 2: −0.97696847, −1.00453024, 1.40126671, (0, 5); 1: −0.25176277,
    −1.18001336, 1.20657201, (0, 1).
  - Table 5 (1275-1277), ONE FLATTENED LINE with merged exponents (docs 1275 identical), rows σ =
    1.00, 1.20, 1.26, 1.35, 1.40, 1.50 × columns q = 5, 4, 3, 2, 1. Map parse (assumes d.dd mantissas):
    1.00: 5.56e-14, 6.37e-15, 7.87e-14, 3.24e-15, 3.06e-12; 1.20: 1.99e-4, 9.46e-6, 2.72e-4,
    1.58e-10, 1.07e-2; 1.26: 7.10e-2, 3.39e-3, 9.74e-2, 5.68e-8, 3.84e0; 1.35: 2.89e2, 1.38e1,
    3.97e2, 2.32e-4, 1.56e4; 1.40: 2.31e4, 1.10e3, 3.17e4, 1.86e-2, 1.25e6; 1.50: 9.42e7, 4.49e6,
    1.29e8, 7.57e1, 5.06e9. Platform rendering of this run is ambiguous.
  - Figures 1-6: captions only (1076-1090, 1142, 1156-1158, 1213-1221, 1261-1263).
- Numeric results in prose: "s⋆,5 = −1.16405872 − 0.43982812 i, ρgen,5 = ρ5 = |s⋆,5| = 1.24437996"
  (1048; repeats Table 4 row q = 5 and 1267, 1347); coefficient-fit estimate "ρbgen,5 = 1.24437676"
  from "orders 800–1000" (1058); σ = 2 lies outside ρgen,5 (1060-1064); multiple-nullity check
  "∥εSVD∥2 = 3.33314836 × 10−5, ∥εcompact − εSVD∥2 = 2.19 × 10−16", residual 9.12 × 10−15 (1126);
  projector errors at σ = 10−3 for K = 1, 2, 3, 4, 120: "3.7381×10−7 1.0869×10−10 1.2732×10−13
  1.4551×10−15 1.4536×10−15", "so four orders reach floating-point accuracy" (1134-1140); (β5, β6,
  β7) = (0.702381824, 0.802152806, 2.495465370) (1166); adjacent gaps "(0.029342, 0.043548,
  0.079461)" (1183); "only about 10.1%" ordered pointwise (1185); Hoeffding: "K = 9", "N =
  3,000,000 and α = 0.01, the subtraction radius is 0.002130. The smallest sampled tail margin is
  0.002382, leaving a positive simultaneous lower endpoint 0.000252" (1187-1189); "C2 = 0.024350, C4
  = 0.041545, CH = 0.226569" (1191); δvis = 10−3 measured "[0.3102, 6.0161]" (1193), older fit
  "gives 0.2363", C2 alone "gives 0.3201", with C4 "0.3101" (1195), predicted "[0.3101, 6.1288]"
  with "relative endpoint errors 0.04% and 1.87%" (1197); μ values "(72.2180, 78.9868, 102.1430,
  113.0325, 146.6655)" (1205); at σ = 1.26 full-nullity errors at orders 20/40/80/120 "(0.0546,
  0.0601, 0.0558, 0.0710)" and q = 4 "(0.0346, 0.0192, 0.00754, 0.00342)" (1239-1243); 1024-point
  Cauchy–Fourier on |s| = 0.95ρq (1247-1249); "q = 2 gives the largest radius, ρ2 = 1.40126671"
  (1269, 1347 "q = 2 is optimal among the five tested nullities"); rounded radii "1.206572 ...
  1.238263, 1.244380, and 1.279076" (1279); BBP illustration "c = 6 100 = 0.06, θbZ = s1(Z) √ 100 =
  1.0408844, σBBP = θbZ c 1/4 ≈ 2.10312" vs "ρ5 ≈ 1.24438" (1305-1315).
- Exact table vs printed derived values (map arithmetic, neutral): Table 3 column-1 differences
  give 0.029342, 0.043547, 0.079462 vs printed gaps 0.029342, 0.043548, 0.079461 (1183); printed
  4-dp endpoints give a lower relative error of 0.032% vs printed "0.04%" (1197; upper 1.87%
  reproduces); (160) q = 4 order-120 error at σ = 1.26 "0.00342" vs Table 5 parse 3.39 × 10−3 for
  q = 4 at σ = 1.26 (q = 5 matches: 0.0710 vs 7.10 × 10−2). No precedence stated.
- Operative definitions, theorems, conditions: estimator (3) and projector (4) (35-47); Proposition
  1 exact compact representation, requires Q invertible (89-127); Proposition 2 Taylor recursion
  (213-239), first order "is the first-order least-squares expression" (361); Proposition 3 block
  recursion (399-447); Proposition 4 empirical ranking, "Under the Gaussian assumptions of Section
  6.2, suppose also that τ ≥ m. Then W ∼ Wishartq0(τ − n, Iq0)" (475-505); Section 6.2 assumptions
  "H has full column rank ... standard-real-Gaussian entries, and that τ > n + 1" (637);
  "We assume that their displayed remainders hold in L1" (673-677); Proposition 5 "a = 1 + n/(τ − n −
  1)" common leading coefficient, lower crossover (104), "For C4 = 0, this reduces to h⋆ √(δvis/C2)"
  (681-721); Proposition 6 requires "τ ≥ m", common law σ² + ∥H∥F²/m, σhi ≈ h⋆(CH/δvis)^(1/4)
  (791-823); Corollary 1 equal-ranked-equal (855-861); Theorem 1 isotropic exact ranking "suppose τ
  ≥ m" (875-919), "'equal' at the two endpoints means asymptotic equality, not exact equality at a
  finite σ" (929); "The isotropic proof therefore does not establish a universal unequal-spike
  theorem" (939); Proposition 7 overlap criterion (941-955); Observation 1 scope (973); norm
  condition (132) "is a convenient sufficient small-noise check, but it is not the exact convergence
  radius" (983); ρq definition (999-1005); Theorem 2 "Assume the boundary collisions are generic"
  (1009-1020); "ρgen,q ≥ ρq, with equality generically" (1032); "ρq−1 may be greater or smaller than
  ρq; (145) there is no general monotonicity theorem" (1100); BBP condition (1283-1287); "they do
  not yet prove an asymptotic identity" (1303).
- Hedged/scoped claims: "Multiple components must be reported separately; the definition does not
  force a three-regime picture" (671); "The order therefore appears after expectation, not
  pointwise" (1185-1187); "numerical evidence that, for this realization, no plotted scalar risk
  cancels" (1090); "The reported values are therefore algebraic–numerical estimates" (1207); "The
  calibration validates the asymptotic powers ... it is not a parameter-free derivation of C2, C4,
  CH" (1199); "The middle visibility interval is consistent with signal–noise mixing" (1293);
  visibility crossings "are therefore neither the fixed-realization Taylor radius ρq nor an exact
  phase-transition or BBP threshold" (975).
- Amendments or contradictions (internal, neutral): two dates (7 vs 21); "fourth-order corrected
  lower crossover" (713) vs abstract "A sixth-order risk correction improves the lower-crossover
  estimate" (13) and conclusion "The sixth-order low-noise term improves" (1343-1345) (different
  order conventions, ∆rank in ζ vs risk in σ); conclusion calls the overlap study "the seed-8
  experiment" (1343) while 1146 says the ensemble is "separate from the fixed seed-8 study"; 9.4 "For
  the same realization" (1205) follows the m = 7 ensemble text but its five μ values and label 5
  match the m = 6, q0 = 5 realization; the value-pair issues listed above.
- References (1353-1359): 3 numbered entries: [1] Kato 1995; [2] Baik, Ben Arous, Péché 2005; [3]
  Benaych-Georges and Nadakuditi 2012. No overlap with any other document's references.
- Coverage: FULL. Read ledger: 1-160, 160-379, 379-608, 608-837, 837-1066, 1066-1235, 1235-1361
  (all lines). Spot-checks vs docs/: Table 3 row 4 (docs 1175), (160) line (docs 1241), Table 5 line
  (docs 1275, identical flattening) match.

## Shared ground (navigation only)

- Entities that appear in more than one document, and where:
  - No shared author, institution, funder, dataset or repository across the six documents.
  - Name matches without stated identity: "Pyne, S." in D01 references (Frühwirth-Schnatter and
    Pyne 2010, D01 509; cited 33) vs D02 author "Saumyadipta Pyne" (D02 5, 623). "Li, X." in D05
    reference Hu et al. 2021 (D05 961) vs D06 author "Xin Li" (D06 5). "C. M. Bishop" in D01 (Bishop
    and Nasrabadi 2006, D01 471) and D05 (Tipping and Bishop 1999, D05 1023) - different works.
  - Same edited volume: "Mixtures: estimation and applications" - D01 Frühwirth-Schnatter (2011)
    pages 213-239 (D01 507) and D02 McLachlan, Baek, Rathnayake (2011) pages 189-212 (D02 679).
  - No reference work is cited by two documents (checked: Tipping and Bishop only D05; Armstrong et
    al. only D01; McLachlan works only D02; Schwarz BIC only D04; Kato/BBP only D06; no Dempster et
    al. anywhere).
- Data domains and dataset sizes (all documents' own data; no overlap):
  - Bulk/array gene expression: D01 leukemia N = 72 samples, d = 2194 genes (D01 13, 37, 273;
    Affymetrix 271); D02 RA/SLE 785 samples (493 RA, 292 SLE), 9,671 genes raw -> top 3000 by MAD ->
    979 genes in 19 modules (D02 431, 439, 723-725); D02 platform never named.
  - Spatial transcriptomics: D05 DLPFC section 151675, 3,592 spots, 33,538 genes; filtered 14,638;
    3,000 HVGs (D05 783).
  - Single-cell mentions only: D01 S9 (D01 439-441, supplementary, absent); D05 workflow context
    (773, 785, 791).
  - Remote sensing: D05 NDVI 239318 locations x 24 observations (1 year); 984 observations (40-year
    PCA benchmark) (D05 887).
  - Laboratory cells: D04 10 cells (9 after excluding cell 5) (D04 21, 291, 377).
  - No real data: D03 ("No data were used in this study", 844); D06 (simulations only).
  - Same numbers in different roles: "3000" = D02 top-MAD gene count (723), D05 HVG count (783) and
    D05 timing-study size "3000 samples/features" (767). "20" = D02 minimum module size (575, 723-725)
    and D05 minimum spots with positive expression (783). "K = 9" = D02 cluster count (447) and D06
    "K = 9 adjacent tail margins" (1187).
- Simulation designs (located): D01 N = 100, d = 2, Ktrue = 2, 100 runs; d = 100, Ktrue ∈ {4, 6, 8,
  10}; timing N = 100, d = 100, K = 2, 1000 MCMC iterations (227, 247, 263). D03 m = 5, n = 1000, R =
  100, six scenarios (701-715). D05 domains 400/2500, sample sizes 200-10000, σ2 ∈ {5, 10}, k = 3,
  twenty replicates, lags 2/20 (721-725). D06 seeds 17 and 8, m = 6/7, τ = 50/100, 100,000 and
  3,000,000 trials (1110, 1132, 1146-1166).
- Notation crosswalk (same letters, different meanings): samples/rows - D01 N, D02 n, D03 n
  (simulated sample size), D04 M cells and ni per cell (N = Σ ni, 511), D05 n = rows called
  "observations" (genes or time points, 29), D06 τ measurements. Variables/columns - D01 d, D02 p,
  D05 m = spatial locations, D06 m = rows of Z. Latent dimension - D02 q (factors, 8), D05 k (7 or 3),
  D06 q = retained nullity. α - D01 DP concentration, D02 module effects αk,g, D03 Weibull shape and
  PH ratio αj, D04 confidence level, D06 Hoeffding level 0.01. λ - D03 rate, D04 ridge
  hyper-parameter, D05 length scales, D06 eigenvalue.
- Definitions across documents (each located; no common definition is printed):
  - ARI: named only in D01 ("adjusted Rand index (ARI)", 227); no formula anywhere in the bundle.
  - BIC: D01 "Standard model selection criteria like BIC fall short in this setting due to unknown
    cluster number (Liu and Yang, 2011)" (221); D02 BIC "with smaller values indicating a better
    trade-off" and ∆BIC definition, used to pick K and q (443-447, Table 4 583-587); D04 "BIC = 2L
    p(ω, λ, σ2) + γlog(N)" with γ = trace(S(λ)) (517-525), Schwarz [xiv], used to pick the ridge λ
    (121).
  - Cluster: D01 mixture component; "non-empty clusters" count Kpost (177, 227); D02 latent mixture
    component zi ∈ {1..K} (81); D05 clustering only as a downstream step (795).
  - Factor/loading orientation: D02 per-sample latent factor ui ∈ R^q with gene loadings B = SMH
    (93-115); D05 per-row (gene or time point) latent zi with location loadings U, "placing the
    spatial dimension as loadings and the time/gene dimension as factors" (51, 31).
  - Orthogonal: D05 "inner product is 0" (51), U′U = Ik (1659); D06 "orthonormal columns" and
    "orthogonal projector" (33, 43); D02 only unit-norm hg (113); D01 none.
  - Covariance sharing: D01 "global" (common) vs "cluster-specific" (109), "Compared to global
    covariance, cluster-specific covariance structures provide better results overall" (247), "Such
    global covariance structures (M3- M5) can prove inadequate" (245); D02 "employs a common
    module-structured covariance representation across clusters" (37, Σ = BB⊤ + D, 121) with future
    work on "cluster-specific latent dependence" (617).
- Shared method families (located): EM family - D02 ECM (161-421; Meng and Rubin 1993, McLachlan and
  Krishnan 2008, Ng et al. 2011 at 685-691); D05 MM-EM (192-665) and Laminae-PCA "estimated using EM"
  (807-809); D01 mentions HDDC estimating GMM parameters "using EM iterations" (401) but itself uses
  collapsed VI with coordinate ascent (111-201). Variational inference - D01 only. Factor models -
  D02 (MFA), D05 (probabilistic PCA/factor), D01 mentions "latent factor models" (33). PCA - D05
  (core), D01 PCA projection plots "PC 1 (16.57%)", "PC 2 (5.58%)" (277-279). SVD - D05 (Prop. 1,
  Procrustes 266-270), D06 (core); eigendecomposition also D04 Appendix B (567-589). Wishart - D01
  inverse-Wishart priors (33, Table 1 M4/M6), D05 James (1964) Wishart eigendecomposition (89), D06
  Wishart laws (495, 749, 867). Generalised least squares - D04 only (RIGLS, 121). Mixture models -
  D01 (DPMM), D02 (finite Gaussian mixture). Splines - D04 single-knot cubic B-spline (21, 297), D05
  two-dimensional P-splines, rx = ry = 10 (691-713). Cholesky - D01 M5 (Table 1, 245), D04 (89).
  Taylor expansions - D01 (35), D04 (71-73, 153, 427), D06 (core). Monte Carlo - D01 MCMC, D03 MC
  simulation (695-725), D06 MC certificate (1187-1189). Gaussian modelling of expression - D01
  Gaussian kernels with note that "overdispersed count data is better modelled using Negative
  Binomial distributions" (439); D02 standardised expression in a Gaussian mixture (47-49); D05
  log-transformed counts treated as Gaussian, "an approximation (Townes et al., 2019)" (785).
- Spectrum ends: D05 MAP loadings are eigenvectors with the "largest k eigenvalues" of S + (1/n)Σ
  (151); D06 estimates the null space from "the q smallest left singular vectors" (43).
- Runtimes and iteration counts (only D01, D04, D05 report them): D01 Sparse DPMM 65 s (Fig. 5,
  413), "∼ 5.91 seconds per iteration" (403), slice sampler 1000 iterations (263); D04 RIGLS "2"
  iterations (379, 385) vs "roughly 3-5" typical (351); D05 38.51 s / 88.92 s / 18.51 s on 32 cores
  (819), single-core timing study (767). D02, D03, D06 report none.
- Dates and versions: arXiv stamps D03 5 Aug 2026 (v1), D02 19 Aug 2026 (v3), D05 25 Aug 2026 (v1),
  D06 31 Aug 2026 (v1), D01 9 Sep 2026 (v3); D04 has no printed date or version. Title-block dates
  differing from stamps: D03 "August 7, 2026" (7), D06 "September 1, 2026" (7). No document prints a
  change log or earlier-version date; no edition of one paper appears twice.
- Funding/software/repositories by document: D01 ANR 17-EURE-0019, PEPR SN SMATCH 22-PESN0003, MCIA
  computing; vimixr (R, CRAN), NPflow, Zenodo 10.5281/zenodo.18405687. D02 Australian Research
  Council DP230101671; github wujrtudou/structured_MFA. D03 CAPES Finance Code 001; "R software"
  keyword only. D04 none; CC-BY 4.0. D05 none; github daniel-s-cunha/SOFM, "pip install sofm". D06
  none; notebook "seriesCheck2.ipynb" only.
- Issuer vs mentioned organisations: issuers are the author affiliations (D01 none printed; D02
  Queensland / UC Santa Barbara / Health Analytics Network; D03 Brasília; D04 Loughborough / Oxford
  Brookes; D05 Boston University; D06 none). Mentioned-only bodies: D01 University of Bordeaux, ANR,
  MCIA, Université de Pau (453); D02 ADEx database (431); D04 Zülke et al. batch source (199); D05
  10x Genomics (773), GIMMS/AVHRR (875-879), Maynard et al. data (775).
- Actions vs mentions (located): D05 analyses one section (151675) of "12 tissue sections from 3
  donors" (775-783); D05 tracks HBB and IGKC but not NPY of the listed "HBB, IGKC, and NPY" (811); D02
  says alternative module definitions "can be incorporated" (77) but runs only MAD-HC and WGCNA
  (577); D01 single-cell and negative-binomial work only in absent supplements (439-441, 35); D04
  real-world EV data discussed, not analysed (423), and "Validation data was not available" (379);
  D06 inserts its realization "naively" into the BBP normalisation (1305) and states the experiments
  "do not yet prove an asymptotic identity" (1303).
- Exclusion facts (located): D02 disease labels unused in fitting (433), 4 grey-module genes excluded
  (577), modules under 20 genes removed (723-725); D04 cell 5 excluded (289-291) and three FAST-LTS
  points (367, 371); D05 low-expression filter (783) and 400 held-out spots (815); D03 "no
  combination of the scale parameters φ and μG can ensure independence when α ̸= 1" (808).
- Late list members: D05 NPY is the last of three named genes (811); D02 Table 2 module 19 is the
  final row (547-549); D06 Table 4 last row q = 1 has the smallest radius 1.20657201 (1233); D03 Tables
  1-2 end with the general Cox PH / general PRH rows (369, 565); D01 intro competitor list ends with
  HDDC (37), Fig. 5 splits HDDC into random and k-means initialisations (409-413).
- Narrative passages restating tables: D02 5.3 prose (451, 485) restates Table 1; 579 and 725
  restate Table 4/K = 9, q = 8; 589 restates Table 5. D03 761-800 restates Table 3 patterns. D04
  abstract (21), captions (373, 383, 385) and conclusion (421) restate RMSE and fit values. D06 1048,
  1267-1279, 1347 restate Table 4; 1239-1243 overlap Table 5's σ = 1.26 row. D01 abstract (13) and
  intro (37) restate 72 x 2194.
- Forecast/actual-type and predicted/measured pairs (within documents only): D06 predicted
  "[0.3101, 6.1288]" vs measured "[0.3102, 6.0161]" (1193-1197); D04 abstract "predicted to ±0.191%"
  vs training-only RMSE and no validation data (21, 379, 421); D03 stated W∗d bound (427, 689) vs
  left-censoring Table 3 W∗d values above 1 (755-759); D01 Kpost vs known subtypes (273, 297).
- Repeated/changed tables: no cross-document repeats. Within-document pairs over the same sample:
  D02 Table 1 (MAD-HC, 9 clusters) vs Table 5 (WGCNA, 4 clusters) both partition 493 RA + 292 SLE;
  D03 Table 3 right vs left halves share scenario parameters; D06 Table 4 vs repeated prose radii.
- Stated limitations / "cannot" statements: D01 ELBO and VLL "cannot properly discriminate extreme
  values from optimal ones" (221), a0 = b0 hyper-prior lacks closed form (445); D02 "fully
  unstructured covariance modeling is statistically infeasible" (21); D04 marginal integral "does not
  have a closed-form solution" (71), no validation data (379); D05 Σ parameters "we cannot optimize
  these directly" (143), "not possible to store S nor Σ in memory" (192), MAP of L, σ2 left for
  future research (155); D06 "cannot automatically be averaged term by term" (627), "increasing K
  cannot make the Taylor series converge" beyond ρq (1020), Proposition 3 "cannot simply be called
  with an incomplete clean null basis" (1100); D03 independence "is not a strict requirement" (29).
- Documents that cite, amend or respond to another bundle document: none.
