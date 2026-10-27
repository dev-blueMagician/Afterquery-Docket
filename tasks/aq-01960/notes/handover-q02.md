# aq-01960 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01960 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 3, difficulty_target medium, origin claude.
- tested_sha256 34bf7b1e09c31429c30af53baed24524378a091896bae9780c75d699270d22ce: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D10 = Doc 10, D11 = Doc 11, D12 = Doc 12, D13 = Doc 13, D14 = Doc 14.
- Floor: 0 FAIL, 4 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: 5 documents listed; the form's reasoning usually covers 2-4, only those the answer relies on
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how many million dollars did KLA's GAAP gross profit for fiscal 2026 (ended June 30, 2026) exceed the sum of the gross profits implied by the revenue and GAAP gross margin guidance it issued for each of that year's four quarters, multiplying the two midpoints for each quarter? Round to the nearest million dollars.
```

### Number of asks

1 ask

### Gold answer

```text
$250 million
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 10, guidance for the first quarter of fiscal 2026 ending in September): total revenues are expected at $3.15 billion +/- $150 million and GAAP gross margin at 60.7% +/- 1.0%, so the midpoints are $3.15 billion and 60.7%.

Step 2. Calculation (from Step 1; Doc 10): implied first-quarter gross profit in billions of dollars = 3.15 × 60.7% = 1.91205.

Step 3. Source fact (Doc 11, guidance for the second quarter of fiscal 2026 ending in December): total revenues $3.225 billion +/- $150 million and GAAP gross margin 60.8% +/- 1.0%.

Step 4. Calculation (from Step 3; Doc 11): implied second-quarter gross profit in billions of dollars = 3.225 × 60.8% = 1.9608.

Step 5. Source fact (Doc 12, guidance for the third quarter of fiscal 2026 ending in March): total revenues $3.35 billion +/- $150 million and GAAP gross margin 60.62% +/- 1.00%.

Step 6. Calculation (from Step 5; Doc 12): implied third-quarter gross profit in billions of dollars = 3.35 × 60.62% = 2.03077.

Step 7. Source fact (Doc 13, guidance for the fourth quarter of fiscal 2026 ending in June): total revenues $3.575 billion +/- $200 million and GAAP gross margin 60.72% +/- 1.00%.

Step 8. Calculation (from Step 7; Doc 13): implied fourth-quarter gross profit in billions of dollars = 3.575 × 60.72% = 2.17074.

Step 9. Calculation (Steps 2, 4, 6 and 8 results; Docs 10 to 13): sum of the implied gross profits in billions of dollars = 1.91205 + 1.9608 + 2.03077 + 2.17074 = 8.07436.

Step 10. Source fact (Doc 14, statement of operations, twelve months ended June 30, 2026, in thousands): total revenues 13,579,476 and costs of revenues 5,255,060.

Step 11. Calculation (from Step 10; Doc 14): fiscal 2026 GAAP gross profit = 13,579,476 - 5,255,060 = 8,324,416 thousand dollars.

Step 12. Calculation (Steps 9 and 11 results; Docs 10 to 14): 8,324,416 thousand dollars - 8.07436 billion dollars = 250 million dollars (to the nearest million).
```

### Answer components

Component 1

```text
$250 million
```

### Evidence

Evidence 1: document Doc 10 (klac_ex991_2025-07-31.txt), proves component 1. $250 million (local note: L36, First Quarter Fiscal 2026 Guidance)

```text
The following details our guidance for the first quarter of fiscal 2026 ending in September
```

Evidence 2: document Doc 10 (klac_ex991_2025-07-31.txt), proves component 1. $250 million (local note: L37, revenue guidance)

```text
Total revenues is expected to be in a range of $3.15 billion +/- $150 million
```

Evidence 3: document Doc 10 (klac_ex991_2025-07-31.txt), proves component 1. $250 million (local note: L37, GAAP gross margin guidance)

```text
GAAP gross margin is expected to be in a range of 60.7% +/- 1.0%
```

Evidence 4: document Doc 11 (klac_ex991_2025-10-29.txt), proves component 1. $250 million (local note: L37, Second Quarter Fiscal 2026 Guidance)

```text
The following details our guidance for the second quarter of fiscal 2026 ending in December
```

Evidence 5: document Doc 11 (klac_ex991_2025-10-29.txt), proves component 1. $250 million (local note: L38, revenue guidance)

```text
Total revenues are expected to be in a range of $3.225 billion +/- $150 million
```

Evidence 6: document Doc 11 (klac_ex991_2025-10-29.txt), proves component 1. $250 million (local note: L38, GAAP gross margin guidance)

```text
GAAP gross margin is expected to be in a range of 60.8% +/- 1.0%
```

Evidence 7: document Doc 12 (klac_ex991_2026-01-29.txt), proves component 1. $250 million (local note: L38, Third Quarter Fiscal 2026 Guidance)

```text
The following details our guidance for the third quarter of fiscal 2026 ending in March
```

Evidence 8: document Doc 12 (klac_ex991_2026-01-29.txt), proves component 1. $250 million (local note: L39, revenue guidance)

```text
Total revenues are expected to be in a range of $3.35 billion +/- $150 million
```

Evidence 9: document Doc 12 (klac_ex991_2026-01-29.txt), proves component 1. $250 million (local note: L39, GAAP gross margin guidance)

```text
GAAP gross margin is expected to be in a range of 60.62% +/- 1.00%
```

Evidence 10: document Doc 13 (klac_ex991_2026-04-29.txt), proves component 1. $250 million (local note: L38, Fourth Quarter Fiscal 2026 Guidance)

```text
The following details our guidance for the fourth quarter of fiscal 2026 ending in June
```

Evidence 11: document Doc 13 (klac_ex991_2026-04-29.txt), proves component 1. $250 million (local note: L39, revenue guidance)

```text
Total revenues are expected to be in a range of $3.575 billion +/- $200 million
```

Evidence 12: document Doc 13 (klac_ex991_2026-04-29.txt), proves component 1. $250 million (local note: L39, GAAP gross margin guidance)

```text
GAAP gross margin is expected to be in a range of 60.72% +/- 1.00%
```

Evidence 13: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. $250 million (local note: L94, statement of operations columns)

```text
Three Months Ended June 30, Twelve Months Ended June 30,
```

Evidence 14: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. $250 million (local note: L101, statement of operations, third column = twelve months ended June 30, 2026)

```text
Total revenues 3,657,556 3,174,741 13,579,476 12,156,162
```

Evidence 15: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. $250 million (local note: L104, statement of operations)

```text
Costs of revenues 1,413,108 1,207,286 5,255,060 4,751,867
```

### Necessary documents

- Tick Doc 10 (klac_ex991_2025-07-31.txt), role: Answer component
- Tick Doc 11 (klac_ex991_2025-10-29.txt), role: Answer component
- Tick Doc 12 (klac_ex991_2026-01-29.txt), role: Answer component
- Tick Doc 13 (klac_ex991_2026-04-29.txt), role: Answer component
- Tick Doc 14 (klac_ex991_2026-07-28.txt), role: Answer component

Leave unticked: Doc 1 (klac_ex991_2023-04-26.txt), Doc 2 (klac_ex991_2023-07-27.txt), Doc 3 (klac_ex991_2023-10-25.txt), Doc 4 (klac_ex991_2024-01-25.txt), Doc 5 (klac_ex991_2024-04-25.txt), Doc 6 (klac_ex991_2024-07-24.txt), Doc 7 (klac_ex991_2024-10-30.txt), Doc 8 (klac_ex991_2025-01-30.txt), Doc 9 (klac_ex991_2025-04-30.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization, Aggregation

Leave unticked: Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Docs 11 to 14 print next-quarter guidance (Doc 14: September 2026); pairing each fiscal 2026 release with its own block gives -$302 million. Each block also lists non-GAAP margin; using it gives $96 million. The gold pairs Docs 10-13's GAAP guidance with their named quarters.
```

(45 / 50 words.)
