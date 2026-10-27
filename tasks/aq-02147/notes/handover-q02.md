# aq-02147 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02147 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 b01169fc2400d07e733b9a3c0074ea06a8022f6b263a7ccac3c1ed19a8a50781: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 4, D03 = Doc 5.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In which week of absence would the equality analysis's higher-paid case-study employee first be worse off overall at employers' median suggested rate?
```

### Number of asks

1 ask

### Gold answer

```text
Week 3
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 5, Impact on Employers): across the 275 responses from employers and employer representative groups, the median percentage rate put forward was 50%.

Step 2. Source fact (Doc 4, Appendix, case study 2): the higher-paid case-study employee works 5 days per week and earns £175 per week. The analysis compares cumulative SSP under the new percentage rate with the old entitlement, and at 80% finds this employee always better off.

Step 3. Source fact (Doc 4, paragraphs 1.2, 1.7 and 1.11): SSP is currently a flat £116.75 a week and is not paid for the first 3 qualifying days (waiting days). The reform removes the waiting days and pays the lower of a percentage of earnings and the flat rate.

Step 4. Calculation (from Steps 1 and 2; Doc 4 and Doc 5): weekly SSP at the employers' median rate: 175 * 50% = 87.5 pounds. This is below the £116.75 flat rate, so the percentage rate applies.

Step 5. Calculation (from Step 3; Doc 4 and Doc 5): current SSP per qualifying day in a five-day week: 116.75 / 5 = 23.35 pounds.

Step 6. Calculation (from Steps 3 and 5; Doc 4 and Doc 5): current entitlement in week 1, when 2 of the 5 qualifying days are paid after the 3 waiting days: 23.35 * 2 = 46.7 pounds (the table shows £47).

Step 7. Calculation (from Steps 3 and 6; Doc 4 and Doc 5): current cumulative entitlement after week 2: 46.7 + 116.75 = 163.45 pounds (the table shows £163).

Step 8. Calculation (from Step 4; Doc 4 and Doc 5): cumulative SSP at the median rate after week 2: 87.5 * 2 = 175 pounds. This is more than 163.45, so the employee is still ahead after week 2.

Step 9. Calculation (from Steps 3 and 7; Doc 4 and Doc 5): current cumulative entitlement after week 3: 163.45 + 116.75 = 280.2 pounds (the table shows £280).

Step 10. Calculation (from Step 4; Doc 4 and Doc 5): cumulative SSP at the median rate after week 3: 87.5 * 3 = 262.5 pounds. This is less than 280.2, so the employee is first worse off overall in week 3.
```

### Answer components

Component 1

```text
Week 3
```

### Evidence

Evidence 1: document Doc 5 (Government-response-Making-Work-Pay-Strengthening-Statutory.txt), proves component 1. Week 3 (local note: L105, Impact on Employers)

```text
The median percentage put forward across all employers was 50%
```

Evidence 2: document Doc 5 (Government-response-Making-Work-Pay-Strengthening-Statutory.txt), proves component 1. Week 3 (local note: L103, Impact on Employers)

```text
the distribution of the 275 responses received from employers and employer representative groups
```

Evidence 3: document Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), proves component 1. Week 3 (local note: L428, Appendix, case study 2)

```text
Case study 2: Employee works 5 days per week, and earns £175 per week
```

Evidence 4: document Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), proves component 1. Week 3 (local note: L45, paragraph 1.2)

```text
Currently SSP is paid at a flat rate (currently £116.75 per week).
```

Evidence 5: document Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), proves component 1. Week 3 (local note: L45, paragraph 1.2)

```text
SSP is not payable for the first 3 Qualifying Days of sickness absence (Waiting Days)
```

Evidence 6: document Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), proves component 1. Week 3 (local note: L67, paragraph 1.7)

```text
removing the existing requirements to serve waiting days
```

Evidence 7: document Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), proves component 1. Week 3 (local note: L87, paragraph 1.11)

```text
employees receive either a percentage of their earnings or the flat rate of SSP (currently £116.75) whichever is lower
```

### Necessary documents

- Tick Doc 4 (Equality-Analysis-for-Statutory-Sick-Pay-Reform-Measures-in.txt), role: Answer component
- Tick Doc 5 (Government-response-Making-Work-Pay-Strengthening-Statutory.txt), role: Answer component

Leave unticked: Doc 1 (Health-is-everyones-business-proposals-to-reduce-ill.txt), Doc 2 (Government-response-Health-is-everyones-business.txt), Doc 3 (Making-Work-Pay-Strengthening-Statutory-Sick-Pay.txt)

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

#### Why these are traps (at most 50 words)

```text
Doc 4 says this £175 employee is always better off at 80%, so a careless solver answers never. Doc 5's employees' median, 90%, also leaves the flat rate (never). The gold uses employers' 50%: £87.50 a week, cumulatively £262.50 against £280.20 by week 3.
```

(44 / 50 words.)
