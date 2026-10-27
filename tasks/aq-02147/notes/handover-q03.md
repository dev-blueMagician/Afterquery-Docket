# aq-02147 q03 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02147 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 ea5426d5a79a040885e55af63a8e3804c7440f04eb9dd5fe6682079ec8d34ae3: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D05 = Doc 3.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At the median saving per retained employee, how many retentions a year would offset an 80% rate's rise over current SSP costs?
```

### Number of asks

1 ask

### Gold answer

```text
52,500 employees
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 2, Annex A, Table 3): the 2021 response estimates what employers gain for each individual retained in work, as productivity plus replacement costs avoided. The total is £4,700 (lower), £8,000 (median) and £11,000 (upper) per employee.

Step 2. Source fact (Doc 3, paragraph 32 and Table 2): employers' total annual SSP costs are £0.65 billion under the current system and £1.07 billion under the 80% earnings illustration.

Step 3. Calculation (from Step 2; Doc 2 and Doc 3): rise over current SSP costs at an 80% rate, in billions of pounds: 1.07 - 0.65 = 0.42.

Step 4. Calculation (from Steps 1 and 3; Doc 2 and Doc 3): retentions a year needed to offset that rise, dividing billions of pounds by the median saving in thousands of pounds, so the result is in millions of employees: 0.42 / 8 = 0.0525 million retained employees a year.
```

### Answer components

Component 1

```text
52,500
```

### Evidence

Evidence 1: document Doc 2 (Government-response-Health-is-everyones-business.txt), proves component 1. 52,500 (local note: L808, Annex A, benefits to employers)

```text
could save employers between £5,000 and £11,000, on average, for each employee they prevent from falling out of work
```

Evidence 2: document Doc 2 (Government-response-Health-is-everyones-business.txt), proves component 1. 52,500 (local note: L853, Annex A)

```text
Table 3: Societal benefits of retaining an individual in work (£)
```

Evidence 3: document Doc 2 (Government-response-Health-is-everyones-business.txt), proves component 1. 52,500 (local note: L855, Table 3 header)

```text
|Employer benefits|Lower|Median|Upper|
```

Evidence 4: document Doc 2 (Government-response-Health-is-everyones-business.txt), proves component 1. 52,500 (local note: L859, Table 3 total)

```text
|Total|£4,700|£8,000|£11,000|
```

Evidence 5: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. 52,500 (local note: L167, Table 2 title)

```text
Table 2 – Comparison of Illustrations on Impact on Business
```

Evidence 6: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. 52,500 (local note: L169, Table 2 header)

```text
||Current system|60% earnings|70% earnings|80% earnings|
```

Evidence 7: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. 52,500 (local note: L171, Table 2 totals)

```text
|Total costs|£0.65 billion|£1.04 billion|£1.06 billion|£1.07 billion|
```

### Necessary documents

- Tick Doc 2 (Government-response-Health-is-everyones-business.txt), role: Answer component
- Tick Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), role: Answer component

Leave unticked: Doc 1 (Health-is-everyones-business-proposals-to-reduce-ill.txt), Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), Doc 5 (Government-response-Making-Work-Pay-Strengthening-Statutory.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Doc 3's own retention figure, an average £30,614 per lost employee, gives 13,719; Doc 2's Table 3 median is £8,000. Dividing the 80% rate's full £1.07 billion instead of its £0.42 billion rise over the current £0.65 billion gives 133,750.
```

(40 / 50 words.)
