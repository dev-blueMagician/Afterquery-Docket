# aq-03120 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03120 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 3, difficulty_target medium, origin claude.
- tested_sha256 4bfe9546bbda147612c4de36dc0f8104234516140054913b484dae40c644c579: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3, D04 = Doc 4.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On Kiwibank's reported figures, what percentage of its 2023 financial-year home lending growth came in the half when ANZ piloted Simple Switch, to the nearest percent?
```

### Number of asks

1 ask

### Gold answer

```text
45%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, its answer on what prompts or hinders switching): ANZ launched its Simple Switch pilot in April 2023 and ran it for six weeks, so the whole pilot falls between April and mid-June 2023.

Step 2. Source input (Doc 4, its paragraph on Kiwibank's growth and the footnote to it): Kiwibank grew its home lending book by $0.6b during the first half of its 2023 financial year. The footnote gives the source as Kiwibank's half-year results for the six months to the end of December 2022.

Step 3. Inference (Doc 2 and Doc 4): a first half that ends in December 2022 means Kiwibank's 2023 financial year runs from July 2022 to June 2023, so its second half is January to June 2023. The April 2023 pilot falls in that second half, not in the first half whose growth Doc 4 prints.

Step 4. Source input (Doc 3, its paragraph on Kiwibank's results): for the whole of that financial year, which ASB calls FY23, Kiwibank reported home lending growth of $1.1 billion.

Step 5. Calculation (Doc 3 and Doc 4): no document prints the second-half growth, so it is the full-year growth less the first-half growth, in billions of dollars: 1.1 - 0.6 = 0.5

Step 6. Final answer (Doc 2, Doc 3 and Doc 4): the second half's part of the full year's growth, as a percentage to the nearest percent: 0.5 / 1.1 = 45%
```

### Answer components

Component 1

```text
45%
```

### Evidence

Evidence 1: document Doc 2 (nzcc_banking_r1_issues_anz_submission_on_market_study_into_personal_ban.txt), proves component 1. 45% (local note: answer to questions 21 and 22, paragraph 123)

```text
In April 2023 we launched a pilot, Simple Switch
```

Evidence 2: document Doc 2 (nzcc_banking_r1_issues_anz_submission_on_market_study_into_personal_ban.txt), proves component 1. 45% (local note: answer to questions 21 and 22, paragraph 123)

```text
The pilot was carried out over six weeks
```

Evidence 3: document Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), proves component 1. 45% (local note: paragraph 2.6(c)

```text
the bank grew its home lending book by $0.6b (1.5 x the banking system) during the first half [of FY23]
```

Evidence 4: document Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), proves component 1. 45% (local note: footnote 7)

```text
Kiwibank half-year results for the six months to 31 December 2022
```

Evidence 5: document Doc 3 (nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt), proves component 1. 45% (local note: paragraph 9.15)

```text
Kiwibank announced its best results in the history of the bank for FY23
```

Evidence 6: document Doc 3 (nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt), proves component 1. 45% (local note: paragraph 9.15)

```text
Home lending growth of $1.1 billion, (or 1.5x market)
```

### Necessary documents

- Tick Doc 2 (nzcc_banking_r1_issues_anz_submission_on_market_study_into_personal_ban.txt), role: Used to identify
- Tick Doc 3 (nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt), role: Answer component
- Tick Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), role: Answer component

Leave unticked: Doc 1 (nzcc_banking_r1_issues_aera_submission_on_market_study_into_personal_ba.txt), Doc 5 (nzcc_banking_r1_issues_consumer_nz_submission_on_market_study_into_pers.txt), Doc 6 (nzcc_banking_r1_issues_federated_farmers_of_nz_submission_on_market_stu.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Figure that must be computed: Doc 2 dates ANZ's pilot to April 2023, the second half of Kiwibank's July-to-June year (Doc 4's footnote). Second-half growth is unprinted: Doc 3's full-year $1.1 billion minus Doc 4's $0.6b, 45% of the year. A careless solver uses the printed first half: 55%.
```

(49 / 50 words.)
