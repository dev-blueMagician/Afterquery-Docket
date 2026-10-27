# aq-02147 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02147 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 9563e169f47dcc7565b1747a064b23d05669f64c62677d033e0699d5bfa419fb: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 4, D03 = Doc 5, D05 = Doc 3.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Using the 2024 sick-pay consultation's figures, in which week would its break-even point fall at the median rate employee respondents suggested?
```

### Number of asks

1 ask

### Gold answer

```text
Week 12
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 5, Impact on Employees): respondents answering as employees or members of the public ("employees") put forward a median percentage rate of 90%.

Step 2. Source fact (Doc 3, paragraph 27 and Table 1): the consultation's break-even point is the time it takes an employee earning £123 a week and working five days a week to be entitled to less SSP under the percentage rate than under their current entitlement. Table 1 gives 2, 3 and 4 weeks for the 60%, 70% and 80% illustrations.

Step 3. Source fact (Doc 3, paragraphs 11, 14, 22 and 25): current entitlement is the flat rate of £116.75 a week, not paid for the first 3 qualifying days (waiting days). Under the reform the employee gets the lower of the percentage of earnings and the flat rate, paid from the first day of sickness absence.

Step 4. Calculation (from Steps 1 and 2; Doc 3 and Doc 5): weekly SSP at the median rate: 123 * 90% = 110.7 pounds. This is below the £116.75 flat rate, so the percentage rate applies.

Step 5. Calculation (from Step 3; Doc 3 and Doc 5): current SSP per qualifying day in a five-day week: 116.75 / 5 = 23.35 pounds.

Step 6. Calculation (from Steps 3 and 5; Doc 3 and Doc 5): current SSP withheld for the 3 waiting days: 23.35 * 3 = 70.05 pounds. Paying from the first day gives the median rate this head start.

Step 7. Calculation (from Steps 3 and 4; Doc 3 and Doc 5): weekly shortfall of the median rate against the flat rate: 116.75 - 110.7 = 6.05 pounds.

Step 8. Calculation (from Steps 6 and 7; Doc 3 and Doc 5): shortfall over 11 weeks: 6.05 * 11 = 66.55 pounds. This is less than the 70.05 head start, so after week 11 the employee is still ahead in total.

Step 9. Calculation (from Steps 6 and 7; Doc 3 and Doc 5): shortfall over 12 weeks: 6.05 * 12 = 72.6 pounds. This exceeds the 70.05 head start, so the employee falls behind in total during week 12, which is where the break-even point falls.
```

### Answer components

Component 1

```text
Week 12
```

### Evidence

Evidence 1: document Doc 5 (Government-response-Making-Work-Pay-Strengthening-Statutory.txt), proves component 1. Week 12 (local note: L151, Impact on Employees)

```text
Employees were generally supportive of a high percentage rate, with a median response of 90%.
```

Evidence 2: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. Week 12 (local note: L143, paragraph 27)

```text
the amount of time it takes for an employee earning £123 per week working five days per week to be entitled to less SSP under the percentage rate compared to their current entitlement
```

Evidence 3: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. Week 12 (local note: L105, paragraph 14)

```text
Currently, SSP is not payable for the first 3 qualifying days
```

Evidence 4: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. Week 12 (local note: L190, Your Views)

```text
The government is not consulting on what the SSP flat (currently £116.75 per week) rate should be.
```

Evidence 5: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. Week 12 (local note: L127, paragraph 22)

```text
an employee is entitled to a certain percentage of their average weekly earnings or the current SSP flat rate, whichever is lower
```

Evidence 6: document Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), proves component 1. Week 12 (local note: L95, paragraph 11)

```text
removing the waiting period so that SSP is paid from the first day of sickness absence
```

Evidence 7: document Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), proves component 1. Week 12 (local note: L409, Appendix, case study 1)

```text
Case study 1: Employee works 5 days per week, and earns £123 per week
```

### Necessary documents

- Tick Doc 5 (Government-response-Making-Work-Pay-Strengthening-Statutory.txt), role: Answer component
- Tick Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt), role: Answer component; also tick Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt) and choose it in Doc 3's "or..." box

Leave unticked: Doc 1 (Health-is-everyones-business-proposals-to-reduce-ill.txt), Doc 2 (Government-response-Health-is-everyones-business.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 3

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 3's Table 1 prints break-even weeks 2, 3 and 4 for 60-80%; extending that pattern gives 5. Doc 5 also prints employers' 50% median (week 2) and the April 2025 £118.75 flat rate (week 9). The gold uses 90%, £116.75 and three waiting days: week 12.
```

(47 / 50 words.)
