# q01 rev 7 - independent review (fresh question-review subagent), 2026-10-08

Input: root, slug, question id, revision, fingerprint, target, source-gap hash, paths to the frozen snapshot, the
question file, the six raw returns of this fingerprint, the rev 6 review and the v4 emulator (both modes); four focused
requests (one-decimal intermediates against the gold and clarity, v4 in both modes, the six returns and the solvers'
wrong sensitivity remarks, failure-mode and lever-check truth). No writer conversation. Agent id af8fea8910866f145
(46 tool calls). Raw return below, unchanged except for this header.

q01 (rev 7; tested_sha256: 8f3d3a8eca736a2bb0d563f616066c226ad2baa1e533d1bcb8d417772e272512)

**Bottom line:** verdict ready for local checks. Every check holds on this exact content. The form's reaction to the rev 7 reasoning is still pending, and so is a platform difficulty pass at Medium, so the status should stay checked.

**gold_verified: yes.** I recomputed it with Decimal from the docs/ originals.
- Nuclear: 0.416 × 37,963 = 15,792.608
- Coal: 28,460 − 15,792.608 = 12,667.392, which is 33.367732% of production
- Gap: 56.2 − 33.367732 = 22.832268, which is 22.8 under both half-up and half-even rounding.

The rev 7 route checks out with its one-decimal intermediates:
- 0.562 × 37,963 = 21,335.206, written as 21,335.2
- 21,335.2 − 12,667.4 = 8,667.8 exactly
- 8,667.8 / 37,963 = 22.832231%, written as 22.83%, which rounds to 22.8.

Rounding the intermediates moves the result by about 0.00004 points, which is immaterial. Step 8's claim holds: shortfall divided by production = 0.562 − coal/production, which is the percentage-point gap.

The four evidence quotes are verbatim and occur once each in docs/; the curly apostrophe is included. Rev 7 differs from rev 6 only in the text of Steps 6–8: the other fingerprinted fields are identical between the snapshots, and the current file's fingerprint equals 8f3d3a8e…. The route reads clearly. Step 6's noun phrase is dense, but the calculation right after it fixes its meaning, and Step 8 states the equivalence outright. Rounding 22.83% to 22.8 is left implicit, as in revs 4–6. Writing "22.8" in the reasoning would be flagged, since no document prints it, so this is a reasonable trade-off and a low risk for "Reasoning reaches the answer".

**outcome: A: match; B: match.** Both answered 22.8 from the printed 41.6%. I re-ran audit_transcript.py on all six agents:
- A 14 calls, B 12, shortcut 17, closed-book 1, probes 12 and 16.
- Every agent stayed inside its own packet, and closed-book made only its hand-back call.
- question.txt equals the question in all four packets.

Both solvers' side remarks on sensitivity are wrong. The gap equals the nuclear share minus 18.76773, so 22.8 holds for a nuclear share from 41.5177% up to, but not including, 41.6177%.
- A gives a lower bound of 41.568; the true bound is 41.518.
- B has the direction inverted: 41.55–41.58% gives 22.78–22.81, not 22.9, and 41.65% gives 22.88, which rounds to 22.9.

The records annotate both remarks correctly, and neither affects the match.

**closed-book: misses.** It answered about 28.6 (Poland about 57.1% minus Bulgaria about 28.5%), with low confidence. Its "contaminated: yes" covers only git-status file names and the working-directory path, with no answer content. It equals FM1's wrong value only through recall.

**necessity:**
- **Doc 1 / D02** is the only source of Bulgaria's 2024 inputs (text L10, L11, L13). D13 names Bulgaria twice (L23 trade, L40 BRUA) with no figures. The probe without D02 said not answerable; its forced guess was 28.2 (p 0.05).
- **Doc 2 / D11** is the only document naming Poland (56.2%, L13). The probe without D11 said not answerable; its forced guess was 23.6 (p 0.15).
- No smaller set exists.
- The stated residual still applies: a model that recalls Poland at 56.118–56.218% reaches the gold without Doc 2.
- New and negligible: the FM2 wrong nuclear share combined with a recalled Poland share of 57.34–57.44% also gives 22.8. Every local recall was 57.0–57.1%.

**shortcut: clear.** The verified shortest route is the D11 L13 lookup, plus the three D02 inputs, plus arithmetic. My grep of docs/ and text/ found no 22.8, 22,8, 33.37, 33.4%, 21,335, 8,667, 12,667 or 15,792 anywhere. The difficulty risk is the direct Poland lookup, which is not a shortcut.

**source_assessment:** there are no recorded gaps. source_gaps is [] and sha 4f53cda1… matches the report. D02 L44's monthly-production chart caption ("Jan 2024 to Dec 2024") has no data in the original or in the platform text. Its effect on each dimension:
- **Premises:** they rest on the prose at L10, L11 and L13.
- **Gold:** monthly totals could only re-sum to the printed 37,963 GWh, with no coal or nuclear split.
- **Exclusions:** the 27.6% and 27% figures are dated in prose.
- **Uniqueness:** a totals-only chart can't give a second 2024 coal share.
- **Necessity:** Bulgaria's data stays in D02 either way.
- **Shortcut:** the chart can't print the gap.

The chart is also invisible to platform solvers.

**difficulty: medium (marginal).** This is local suitability only. Nothing the solver sees has changed since rev 1. A printed lookup, a three-figure derivation and same-document period decoys make Easy the likeliest single tier, as earlier reviews also found, and this bundle has no Easy slot.

**verdict: ready.**

**failure_modes:** The section is byte-identical to the rev 6 snapshot, and the current file equals the rev 7 snapshot.
- **FM1 is real.** Docs L16 is the Energy chapter's tenth paragraph, eight after the production paragraph (L8). The recomputed wrong answer is 56.2 − 27.6 = 28.6, which overstates the gap by 5.77 points ("almost six" is true). "Out-of-range period / Uses the wrong period or date" fits.
- **FM2 is real.** L11 is the fifth paragraph and opens "To support its energy needs". 74.9677 − 40.38 = 34.5877, and 56.2 − 34.5877 = 21.6123, which is 21.6. "Two numeric shares" is true. "Figure that must be computed / Uses the wrong period or date" fits.
- No trap repeats, and the wording rules out neither.
- Both documents are correctly "Answer component" in the hand-over.

Every lever-check value recomputes: 28.6, 29.2, 21.2, 21.6, −18.8, 37.3, 27.1, 22.6 and 36.6. The early-rounding cases do too: 15.8 TWh gives 22.9, 12.7 TWh gives 22.7, and 38.0 TWh gives 22.9.

**findings:**

1. **Form check (v4).** Default and --strict both print nothing for rev 7. Strict mode on rev 6 reproduces exactly the two exposures (21,335.206 and 8,667.806), so the mode does what it claims. Each new calculation follows a colon, has one "=", and reuses earlier "=" results token for token. Step 6 has the accepted shape of Step 3, and Step 8 that of Step 5.
2. **Remaining exposure (low).** 8,667.8 in Step 7 is the only result that is not exact in floats: 21335.2 − 12667.4 = 8667.800000000001.
   - It passes both modes, because each allows rounding at one decimal.
   - It would be flagged only by a check that demands exact float equality for subtraction while rounding "%" and percent-of results.
   - The bundle's records don't exclude such a check: every accepted ± result in aq-01543 is float-exact.
   - The only counter-precedent is aq-01320 q01's "10.44 - 10.72 = -0.28", which is inexact in floats and was accepted. It isn't clean evidence: "0.28" is absent from its cited Docs 10 and 12, but "28" occurs in Doc 12, which a significant-digit match would accept.
   - The paste will settle it. Revising beforehand isn't warranted.
3. **Records are accurate.** That covers the Blind solve, closed-book, probe and audit lines, the Lever checks' rev 7 computation, the Feedback log and the answered WARNs. check_questions gives 0 FAIL and 2 WARN, both explained. The report fingerprint and source-gap hash match. notes/handover-q01.md carries rev 7's Steps 6–8.
4. **State at hand-over:** the Poland recall risk, the pending form reaction (naming 8,667.8), and the Easy-tier risk.
5. **Not checked:**
   - Original question, Not a duplicate, Restricted names and the token window.
   - The "Answer matches a stated figure" advisory.
   - Whether the form number-checks the failure-mode boxes, which hold unprinted values such as 74.97%, 34.59% and 21.61%.
6. **No workspace writes.** I ran Bash only for read-only checks: python -B and Decimal/float arithmetic.

Paths:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\questions\q01.md
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\notes\helpers\form_check_v4.py
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r7-v2-8f3d3a8eca736a2bb0d563f616066c226ad2baa1e533d1bcb8d417772e272512\snapshot.json
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r7-alt-s4\results\probes.md
