# q01 rev 0 follow-up review (fresh question-review subagent, 2026-10-08)

Scope given: confirm the fingerprint, check every Targeted failure mode claim after the caller's edits, spot-check the
earlier review. Verbatim hand-back (harness indentation removed).

## Verdict: revise

The tested question still holds at this fingerprint. Two small things need fixing before the form is pasted, and neither needs a re-test.

- **Stale hand-over (required):** `notes/handover-q01.md` was written at 02:41, before the 03:23 edit. It still contains every error the earlier review flagged. I did not regenerate it because `--handover` writes the file.
- **One untrue claim in Failure mode 1 (required):** it says the regressions "all report N 23,788", but Table 4 does not print that figure.
- **Optional:** trimming two side routes in Failure mode 2 (finding 3).

q01 (rev 0; tested_sha256: 8766f4397a13e8f501b617e8fd6b1e7c809ca1bc67f170b29c9df0dfa0a22af1)

**Records (scope 1)**
- `check_questions --q q01`: 0 FAIL, 1 WARN. The warning is about the origin field for export, and Lever checks explains it.
- `report` recomputes the fingerprint from the current content and source bytes. It gives 8766f439…, the same as every record.
- The snapshot's form hash (63054dc5…) equals the current one.
- The question, answer, components, reasoning, evidence, necessary documents and the five metadata fields are byte-identical to `snapshot.json`.
- Only Lever checks, Targeted failure modes and the record sections changed, and all of these are outside the fingerprint.
- There are no source gaps (gap hash 4f53cda1…). There is no platform record, and the status is draft.

**gold_verified: yes**
- Japan: (11,658 × 14.719 + 12,130 × 13.480) / 23,788 = 14.08721, which is 56.3488% of 25 questions.
- China: 1.414 / 3 = 47.1333%.
- Difference: 9.2155, which is 9.2 under both rounding rules. Using the distribution's mean of 1.4142 gives 9.2088, also 9.2.
- The counts reconcile:
  - 25,000 − 1,212 = 23,788 = 11,658 + 12,130.
  - 37 + 614 + 4,204 + 3,705 = 8,560 = 23,788 − 15,228.
  - 8,054 + 7,174 = 15,228.
- Inputs: D01 lines 69, 208, 365 and 397; D03 lines 102, 106 and 108.

**outcome: A: match; B: match.** In the raw `returns.md`, both solvers reach 9.2 by weighting the Table 5 means. Each names and rejects 13.7 and 9.3, and the returns carry this fingerprint.

**closed-book: misses.** It answered "about 30.0". It recalled only Japan's published overall rate (about 55.6%) and nothing for the Chinese survey. Its context held file names only.

**necessity: no smaller valid set exists.**
- **D01 (Doc 5)** is the only source for the 2016 survey. My grep finds "Financial Literacy Survey", "Central Council", 23,788, 14.719 and 13.480 only in D01. The other Japanese data are from Osaka University's survey (D04/D05). The probe without D01 answered "cannot be determined", with a forced guess of 8.9 (p 0.07).
- **D03 (Doc 2)** is the only source of a 2015 Chinese literacy level (1.414).
  - D02 pools the 2011–2019 waves (line 164) and reports literacy only as a regression outcome (lines 309, 316–318).
  - D06 uses the 2017/2019 waves with a four-question index (lines 164, 203).
  - The probe without D03 answered "cannot be determined", with a forced guess of 26.3 (p 0.02).
- The probe map matches the records.

**shortcut: clear.** The route is D01 lines 69 → 208 → 365 + 397 (weighting) → D03 line 108 → subtraction. No passage states either share, the pooled mean or the difference. "Non-student" does not appear anywhere in the documents. The route is simple once found, which is a difficulty risk rather than a Guide violation.

**source_assessment.** There is no exact gap label: all seven documents are complete, with 0 gap characters, and match the capture. The papers cite supplements that are not in the bundle: Doc 5's S1/S2 tables (D01 line 601) and Doc 2's Supplementary Table 1 (D03 line 141).
- **Premises:** the survey names, the 25 and 3 items and both populations are all in body text.
- **Gold:** uses only the body tables (D03 Table 1, D01 Table 5).
- **Exclusions:** the "Big 3" subset is ruled out by "each survey's own literacy test" and has no values in the bundle.
- **Uniqueness:** Supplementary Table 1 might hold another 2015 mean, but no solver can see it, so 1.414 stays the only one.
- **Necessity:** no supplement could replace either document.
- **Shortcut:** no supplement text exists that could state the answer.

The bundle is complete as captured; that does not certify the articles themselves as complete.

**difficulty: medium (marginal), as local suitability only.**
- **For Medium:**
  - The gold is printed nowhere and takes about six dependent steps.
  - The paper's only overall mean (15.2) is a decoy that covers a narrower, labelled group.
  - A second weighting trap changes the first decimal.
- **Against Medium:**
  - The decoy is easy to rule out: the 23,788 / 15,228 sentence and the "complete cases" title sit right beside 15.2.
  - Weighting by group size is routine.
- Easy is at least as likely as Medium, and Lever checks records this bundle's Easy slot as full.

**failure_modes**
- **FM1 (Part vs total / Picks the wrong entity or section): the trap is real.**
  - My script gives 15.2 / 25 = 60.8%, and 60.8 − 47.1333 = 13.667, so 13.7.
  - Both labels are on the form's lists and fit. The wording does not rule the trap out, because the complete cases are themselves non-students. The mode has 283 words.
  - The earlier findings are fixed:
    - "begins by … then states" quotes line 208 exactly.
    - Table 2 does follow that paragraph (line 210).
    - "covariate" is replaced by "education, self-rating, income or asset information".
    - The point that literacy is never missing is now an inference. Its premise is true: line 208 lists only those four missing items, and line 251's imputation uses "knowledge" as a predictor.
    - The table row is described accurately (line 216).
  - **Still untrue:** "which all report N 23,788". Tables 3 and 5–9 print 23,788, but Table 4 prints only "N|11,658|12,130" (line 340).
  - "means are the scores" is loose wording but not false.
- **FM2 (Figure that must be computed / Calculation slip): the trap is real.** My recomputations:
  - Unweighted: 14.0995 → 56.398% → 9.2647, so 9.3.
  - Complete-case weights: 14.1353 → 9.4079, so 9.4 (using the 0.529 share gives 9.4084, also 9.4).
  - Rounding the mean to 14.1 first: 9.2667, so 9.3.
  - Gold with 1.4142: 9.2088.
- All of FM2's claims are true:
  - Table 5 is the only table of literacy means for all non-students. Tables 3 and 6–9 give coefficients or contributions, and Tables 8–9's means are for behaviour and attitude.
  - 0.529 is at line 221 and 8,054 / 7,174 at line 233.
  - The "means" fix is applied, and the mode has 218 words.
- The labels fit the main route. The 9.4 and 14.1 side routes belong to other causes, and no run produced them.
- No trap is repeated.

**findings**
1. **Q15, stale hand-over** (`notes/handover-q01.md`). Line 121 still says "and ends" and "sits right after the sentence" and keeps the pipe-quoted row. Line 133 says "lacked a covariate" and "the literacy score itself is observed for everyone". Line 147 says "reports financial literacy for all". This is the unfinished half of the earlier review's finding 1. Regenerate it with `--handover --q q01`, then confirm its failure-mode blocks match the question file.
2. **Q15, FM1 "Why" box:** the "all report N 23,788" claim versus Table 4 (line 340). Fix it before pasting; no re-test is needed.
3. **Q15, FM2 (optional):** trim the 9.4 and 14.1 side routes.
4. **Form check, carried forward:** run the form's free "One defensible answer" check on the exact 42-word question before any difficulty run.
5. **Spot-check (scope 3):** the gold, both matches, the closed-book miss, the shortcut audit, both probes and the two Answer-component roles all still hold at this fingerprint.

## Caller actions (2026-10-08)

- Finding 2 applied: FM1's "Why" box now says the regressions and decomposition "use all 23,788 non-students (11,658 men and 12,130 women)", which Tables 3-9 support (Table 4 prints the two sex counts).
- Finding 3 applied: FM2 declares only the unweighted route (9.3); the 9.4 complete-case-weights and 14.1 early-rounding routes moved to Lever checks as "considered, not declared".
- Finding 1: hand-over regenerated after these edits.
