# aq-03143 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03143 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 12f43234d2873bbdd1d527ee27df1f65ca4e4e836af43d92116bb0777c8422f9: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 3, D04 = Doc 1.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 6: Doc 1 doesn't mention 317. expected false alarm: Doc 1 prints it at character 86,692, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 9: Doc 3 doesn't mention 52.00. Doc 3 prints it first at character 28,218, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 10: Docs 1 and 3 don't mention 29.25. expected false alarm: Doc 3 prints it at character 91,203, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN precision: the answer is a rate or decimal; state the precision in the question
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Once the final fee changes are in force, what is a firm outside London paid in total for 10 hours' preparation on each of a housing legal help matter opened in 2024 and a new non-asylum immigration one, plus 3 hours attending county court with counsel in each of a new housing and a new discrimination case?
```

### Number of asks

1 ask

### Gold answer

```text
£1,054.25
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, background on how civil legal aid work is paid): legal help is Controlled Work paid by a fixed fee. Under the escape mechanism a matter is paid at hourly rates instead when its claim for the work done, calculated in hourly rates, exceeds the escape threshold, which is a set multiple of the fixed fee.

Step 2. Source input (Doc 3, immediate next steps): the fee increases apply only to new certificates or determinations made after the commencement dates. The housing legal help matter opened in 2024 was determined before any increase, so it stays on the current fee, hourly rate and escape threshold.

Step 3. Source input and calculation (Doc 1, worked example for housing legal help): the current housing legal help fee is £157, based on a non-London hourly rate of £45.95, and the escape threshold is 3 times the fixed fee, in pounds: 3 × 157 = 471

Step 4. Calculation (Doc 1 and Doc 3): the hourly claim on the 2024 housing matter at the current rate, in pounds: 10 × 45.95 = 459.50

Step 5. Comparison (Doc 1 and Doc 3): the claim of 459.50 is below 471, so the 2024 housing matter does not escape and is paid its fixed fee, 157 pounds.

Step 6. Source input and calculation (Doc 1, immigration fixed fees table and the changes made in 2023): the new fixed fee for non-asylum immigration Stage 1 legal help is £317, and since 2023 the escape threshold for immigration legal help cases is twice the fixed fee, in pounds: 2 × 317 = 634

Step 7. Calculation (Doc 1 and Doc 3): the hourly claim on the new immigration matter at the new non-London preparation rate of £65.35, in pounds: 10 × 65.35 = 653.50

Step 8. Comparison (Doc 1 and Doc 3): the claim of 653.50 is above 634, so the immigration matter escapes its fixed fee and is paid its hourly claim, 653.50 pounds.

Step 9. Source input and calculation (Doc 3, decision on attendance fees and the updated rate tables): after the consultation the fee for attendance at court or conference with counsel was raised from 50% to 75% of the preparation rate, and the final table prints one lower-courts rate, £52.00 an hour, with no separate rate outside London. Pay for the new housing case, in pounds: 3 × 52.00 = 156

Step 10. Source input and calculation (Doc 1 and Doc 3, scope of the increase and the current lower-courts attendance rate): the increases do not apply to work in other categories of law, whose licensed work stays in the unchanged table, so the discrimination case is paid the current rate of £29.25 an hour, in pounds: 3 × 29.25 = 87.75

Step 11. Calculation (Doc 1 and Doc 3): the two legal help payments together, in pounds: 157 + 653.50 = 810.50

Step 12. Calculation (Doc 1 and Doc 3): adding the housing attendance, in pounds: 810.50 + 156 = 966.50

Step 13. Final answer (Doc 1 and Doc 3): adding the discrimination attendance, in pounds: 966.50 + 87.75 = 1,054.25
```

### Answer components

Component 1

```text
£1,054.25
```

### Evidence

Evidence 1: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: Chapter One, Background, L293)

```text
Most fixed fees have an escape mechanism whereby providers can be remunerated by hourly rates when the claim for work done (calculated in hourly rates) exceeds the escape threshold, which is two or three times the fixed fee.
```

Evidence 2: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: worked example for housing, L554)

```text
The current fee for Housing legal help work is £157 (Table 1 in the remuneration regulations). This is based on an underlying hourly rate of £45.95/£48.74 (per Table 7(b)).
```

Evidence 3: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: worked example for housing, L556)

```text
The escape threshold remains at three times the fixed fee, meaning the escape threshold is increased to £669.
```

Evidence 4: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: immigration fees, changes made in 2023, L415)

```text
reduction of the escape threshold for legal help cases to twice the value of the fixed fee
```

Evidence 5: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: Annex B, immigration fixed fees, non-asylum Stage 1 legal help row, L1121)

```text
£48.24  35%  £317
```

Evidence 6: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: Chapter One, Proposals, L531)

```text
These fee increases will not apply to work carried out under other categories of law.
```

Evidence 7: document Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), proves component 1. £1,054.25 (local note: footnote 24, L537)

```text
Table 10a is used for remuneration of non-Family licensed work
```

Evidence 8: document Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), proves component 1. £1,054.25 (local note: Chapter 1, immediate next steps, L188)

```text
Fee increases will be applied to all new certificates or determinations made after the specified commencement dates.
```

Evidence 9: document Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), proves component 1. £1,054.25 (local note: Chapter 1, measures taken forward, L165)

```text
up to a minimum hourly rate of £65.35/£69.30 (non-London/London) and uplifting fixed fees by a matching proportional uplift
```

Evidence 10: document Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), proves component 1. £1,054.25 (local note: government response to question 7, L475)

```text
we propose to raise this fee from 50% to 75% of the corresponding preparation and attendance rate
```

Evidence 11: document Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), proves component 1. £1,054.25 (local note: Annex A, table 10(a), label of the lower courts attendance row, L1710)

```text
Lower courts – attendance at court or conference with counsel
```

Evidence 12: document Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), proves component 1. £1,054.25 (local note: Annex A, Schedule 2 rates, attendance at court or conference in the County Court, L1994)

```text
£29.25   78%  1(b), 1(c)  £52.00
```

Evidence 13: document Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), proves component 1. £1,054.25 (local note: Annex A, note on the licensed work tables, L1596)

```text
table 10(a) will remain for non-immigration or housing work
```

### Necessary documents

- Tick Doc 1 (Civil-legal-aid-Towards-a-sustainable-future-consultation.txt), role: Answer component
- Tick Doc 3 (Civil-legal-aid-Towards-a-sustainable-future---consultation.txt), role: Answer component

Leave unticked: Doc 2 (Civil-legal-aid-Towards-a-sustainable-future---impact.txt), Doc 4 (Civil-legal-aid-Towards-a-sustainable-future---response.txt), Doc 5 (Governments-interim-response-to-the-Criminal-Legal-Aid.txt), Doc 6 (Criminal-legal-aid-interim-response-impact-assessment.txt), Doc 7 (Criminal-legal-aid-independent-review-response-consultation.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter, Aggregation

Leave unticked: Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Failure mode 3

Trap: Superseded date or version

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 1 limits the increase to housing and immigration; paying the discrimination case £52.00 gives £1,122.50. Wrong year or edition: Doc 3 keeps the 2024 matter on the old £157; the new £223 gives £1,120.25. Superseded date or version: Doc 1's proposed £34.65 gives £1,002.20.
```

(49 / 50 words.)
