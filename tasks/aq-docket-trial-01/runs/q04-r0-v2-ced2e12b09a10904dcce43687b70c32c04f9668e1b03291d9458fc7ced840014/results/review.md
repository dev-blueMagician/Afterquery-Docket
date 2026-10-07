# q04 rev 0 bound review (question-review agent, fresh context), 2026-10-06

Input: frozen fields (questions/q04.md rev 0), prepared run, tested_sha256 ced2e12b..., target
easy, rev 0 raw returns (A, B, closed-book, shortcut audit, two removal probes), comparison files
aq-docket-trial-02 q01 and aq-docket-trial-06 q02. Return copied verbatim from the task notification.

q04 (rev 0; tested_sha256: ced2e12b09a10904dcce43687b70c32c04f9668e1b03291d9458fc7ced840014)

**gold_verified: yes.** I recomputed from the original passages with Python Decimal (half-up):
- Brain share: 14,638 / 33,538 = 43.6460% (D05 l.783, repeated at l.1055).
- Autoimmune share: 979 / 3000 = 32.6333% (D02 Appendix A, l.723–725).
- Difference: 11.0127, which is 11.0. It stays 11.0 whatever the rounding order (shares rounded to 0, 1, 2 or 3 decimals first, or truncated).
- Units: percentage points. No other figure is printed for these inputs, so no stated-figure choice can flip the gold.

Premises:
- The step order (Sec. 2 l.67) supports a base of 3000. The dendrogram is "partitioned" into candidate modules, so all 3000 MAD-retained genes enter the size removal, and Appendix A credits the cut plus the size rule with the result "979 genes grouped into 19 modules".
- Table 2's sizes add up to 979, and the smallest module is exactly 20 genes, which fits a "fewer than 20" rule.
- "Selected model" is K = 9, q = 8 (l.447, l.725; Table 4 l.585).
- "Exceed" is true (43.65 > 32.63).

Readings I tested:
- **Sec. 5.1 "Small or weakly defined clusters are removed":** no other rule or count exists, so no different value can be computed. The lever note's "names no other criterion" is a little loose, but the conclusion holds.
- **Sec. 5.5 "19 gene modules from 979 genes":** read as a starting count of 979, it gives 100% and −56.4, which breaks "exceed". Sec. 5.5 does show that WGCNA ran on the 979 "pre-selected genes" (975 = 979 − 4).
- **WGCNA:** 975/979 gives −55.9. A near miss I found that is not listed, 975/3000, gives 11.1. It is still excluded, because WGCNA is not the selected model and never started from 3000.
- **HVG analysis:** −23.7 (3,000/33,538) or −12.1 (3,000/14,638).
- **9,671 base:** 33.5. **MAD-step share (3000/9,671):** 12.6. **Table 2 mapped genes (939):** 12.3.
- Sec. 2's "partition of the retained gene set J∗" is loose notation that can't produce a different number.

Result: 11.0 is the only computable answer.

**outcome: A: match; B: match.** Both returned 11.0 with high confidence, from different packets (solver-1, solver-2), each holding all six documents. Both cited D05 l.783 and D02 Appendix A, rejected the 9,671 and WGCNA routes, and reported no contamination. That gives two supported fresh matches.

**closed-book: misses.** It answered "unknown" and could not identify either paper, with no contamination. The papers date from Aug 2026. 33,538 is a common reference gene count, but without 14,638 a guess cannot hit the 0.1-point window.

**necessity:**
- **D02** is the only source of the autoimmune counts. 3000 appears once in the bundle (Appendix A). D01's 2,194 genes belong to a leukemia study.
- **D05** is the only source of the brain counts, and no other document describes a brain study.
- A bundle-wide search found no repeats, summaries or rounded approximations of either pair. No smaller set works.
- Removal probes, run from neutrally named packets:
  - Without D02 (t5): "not answerable", forced guess 10.0 at p ≈ 0.01.
  - Without D05 (w8): "not answerable", forced guess 22.4 at p ≈ 0.01.
  - Both miss. The manifests' Dnn numbering gap showed which document was missing, but that gap cannot lead to the gold.

**shortcut: clear.** My shortest route matches the auditor's: D05 l.783 (both counts in one paragraph) plus D02 l.723–725 (3000 and 979 in adjacent sentences), then two divisions and a subtraction. No passage prints 32.6, 43.6, 11.0, 2,021 or 18,900. D03's "11.005" and "32.643" are unrelated simulation cells. Search finds the inputs, not the whole answer, so this is ordinary cross-document arithmetic and not a demonstrated violation.

**source_assessment:** report and intake show no gaps:
- `source_gaps` is [] (sha 4f53cda1…).
- All 6 documents are complete with 0 gap characters, and docs/ hashes match the capture.
- The originals are text captures without figure images. Every fact used (the four counts, the step order at l.67, the selected model at l.447/725, and the decoy figures at l.431, 577, 585–587 and D05 l.783) is running text. Figure-only content therefore cannot affect the premises, gold, exclusions, uniqueness, necessity or shortcut coverage.

**difficulty: easy.** This is a marginal local fit for the Easy target; Too easy is more likely than Easy.
- Only one trap is live: the 9,671 base.
- The question's own "genes each step started from" rules that trap out for a careful reader.
- The question's terms ("undersized modules", "selected model") pull up Appendix A, where 3000 sits next to 979 and next to "The selected model had K = 9 and q = 8."
- The Doc 2 overview prints "top 3000 genes ranked by MAD · 979 genes grouped into 19 modules" (capture l.47). It is unknown whether the platform's solver sees the overview.
- "Exceed" disarms every negative-result route (WGCNA, HVG, Sec. 5.5), so those add no difficulty.
- All inputs are plain sentences. This is the profile the Coach called solved ("one lookup plus one operation"), with one extra division.

Estimated per-attempt success for the Low model: about 75–85%. Tier estimate:

| Platform outcome | Estimate |
| --- | --- |
| Too easy (Low 4–5/5) | ~65% |
| Easy (Low 1–3/5) | ~30% |
| Low 0/5 (moves on to Medium) | ~5% |
| One-answer quick test survives | ~20–25% |
| Platform document check flags a document | ≤5% |
| Closed-book check reaches the gold | <1% |

**verdict: ready** (local only; platform pending).

**findings:**
1. **Gold and uniqueness (Q4, Q9):** independently reproduced as above. Every alternative differs at one decimal and is excluded by the question's terms, by Appendix A or by "exceed". No further check needed.
2. **Form checks (Q5, Q14):**
   - Answer: "11.0 percentage points", 3 words, no semicolon, one component.
   - All 7 evidence quotes (39–90 characters) and the reasoning's inline quotes are verbatim in docs/ and in the capture's platform text, once each.
   - D02's "fewer than\n\n20 genes" paragraph break is the same in both texts, and the quotes split exactly there.
   - Both necessary documents are quoted.
   - My emulation of the number rule found nothing flagged in steps 1–7: every number is printed in the cited document or follows "=".
   - Remaining low risk: step 5's four-operator expression ("100 × 14,638 / 33,538 - 100 × 979 / 3000 = 11.0"). The only recorded "=" result that was flagged came from a compound expression (aq-00949 q04, cause unresolved). The only two-document step on record that passed subtracted two derived values (aq-00949 q05 rev 0). Check the form's warning when pasting. Any edit changes the fingerprint, so re-prepare and re-record before submitting.
3. **Wording (Q3, Q7, Q8, Q10):** 45 words, one ask, no numbers, no em-dashes. Each description fits one study and one step. It asks about the world, not the set. Points, direction and precision are stated. "Low-expression filter" and "selected model" copy the papers' phrases, but they find inputs, not the answer.
4. **Tags (Q6):** Cross-document join and Unit normalization (counts converted to shares) fit. "Conditional filter" describes the papers' filtering, not anything the reader filters. This is advisory only, since two valid tags remain.
5. **Levers (Q11):** "Scatter the pieces" works (two documents, no single passage holds the answer) and "Calculate across documents" works. No which-items, exclusion or rounding lever is claimed, so no decoy is required.
6. **Difficulty risk (D2/D3/D4/D7):** Too easy is the most likely platform result (~65%). Quick-test before spending the single submission, as `notes/session.md` already plans. q04 and sketch S3/i10 share the same inputs and path, so submit at most one of them.
7. **Records:** the report recomputes ced2e12b… from the current file, matching the run folder and every record (rev 0). The floor shows 0 FAIL and 1 WARN (origin claude; export accepts only user). Report authorship separately. The status may become `checked`, not `ready`. Q13, restricted names and duplicate checks remain platform-only and unknown.
