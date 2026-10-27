# aq-03120 q02 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03120 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 e0d20bd4982d08dc83e3396ad5f4816f4f70ff5a21006aa59096f178839bd31b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D04 = Doc 4.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN precision: the answer is a rate or decimal; state the precision in the question
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How much did Kiwibank's home lending book grow in the half of its financial year that last ended before its owner announced a $225 million capital injection?
```

### Number of asks

1 ask

### Gold answer

```text
$0.5 billion
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 4, its paragraph on Kiwibank's growth and the footnotes to it): Kiwibank's owner, Kiwi Group Capital, announced its $225 million investment in the bank on 1 August 2023. The date is given in the two footnote citations for that announcement.

Step 2. Source input (Doc 4, the same paragraph and its footnote on the half-year results): Kiwibank grew its home lending book by $0.6b during the first half of its 2023 financial year. The footnote gives the source as Kiwibank's half-year results for the six months to the end of December 2022.

Step 3. Inference (Doc 4): a first half that ends in December 2022 means Kiwibank's financial halves end in December and June, and its 2023 financial year ran from July 2022 to June 2023. The half that last ended before 1 August 2023 is therefore January to June 2023, the second half of that year, not the first half whose growth Doc 4 prints.

Step 4. Source input (Doc 3, its paragraph on Kiwibank's results): for the whole of that financial year, which ASB calls FY23, Kiwibank reported home lending growth of $1.1 billion.

Step 5. Calculation (Doc 3 and Doc 4): no document prints the second-half growth, so it is the full-year growth less the first-half growth, in billions of dollars: 1.1 - 0.6 = 0.5

Step 6. Final answer (Doc 3 and Doc 4): in the half of its financial year that last ended before the injection was announced, Kiwibank's home lending book grew by about $0.5 billion.
```

### Answer components

Component 1

```text
$0.5 billion
```

### Evidence

Evidence 1: document Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), proves component 1. $0.5 billion (local note: footnote 4)

```text
(1 August 2023). Kiwi Group Capital invests $225 million into Kiwibank to accelerate growth
```

Evidence 2: document Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), proves component 1. $0.5 billion (local note: footnote 5)

```text
(1 August 2023). Kiwibank owner to invest $225m in growing bank's home loan business
```

Evidence 3: document Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), proves component 1. $0.5 billion (local note: paragraph 2.6(c)

```text
the bank grew its home lending book by $0.6b (1.5 x the banking system) during the first half [of FY23]
```

Evidence 4: document Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), proves component 1. $0.5 billion (local note: footnote 7)

```text
Kiwibank half-year results for the six months to 31 December 2022
```

Evidence 5: document Doc 3 (nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt), proves component 1. $0.5 billion (local note: paragraph 9.15)

```text
Kiwibank announced its best results in the history of the bank for FY23
```

Evidence 6: document Doc 3 (nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt), proves component 1. $0.5 billion (local note: paragraph 9.15)

```text
Home lending growth of $1.1 billion, (or 1.5x market)
```

### Necessary documents

- Tick Doc 3 (nzcc_banking_r1_issues_asb_submission_on_market_study_into_personal_ban.txt), role: Answer component
- Tick Doc 4 (nzcc_banking_r1_issues_bnz_submission_on_market_study_into_personal_ban.txt), role: Answer component

Leave unticked: Doc 1 (nzcc_banking_r1_issues_aera_submission_on_market_study_into_personal_ba.txt), Doc 2 (nzcc_banking_r1_issues_anz_submission_on_market_study_into_personal_ban.txt), Doc 5 (nzcc_banking_r1_issues_consumer_nz_submission_on_market_study_into_pers.txt), Doc 6 (nzcc_banking_r1_issues_federated_farmers_of_nz_submission_on_market_stu.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Figure that must be computed: Doc 4 prints growth only for the half to 31 December 2022, $0.6b. The half that last ended before the 1 August 2023 injection ended in June 2023 and is unprinted: Doc 3's full-year $1.1 billion minus $0.6b. Careless solvers report $0.6 billion.
```

(48 / 50 words.)
