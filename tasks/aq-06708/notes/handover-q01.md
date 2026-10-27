# aq-06708 q01 hand-over

Generated 2026-10-19 by `python tools/check_questions.py tasks/aq-06708 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 a99e6e2df0d8fafe14e925317c9b550ce4c4096c2f1e59a147fd40e2c0c0c65d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D06 = Doc 5, D07 = Doc 7.
- Floor: 0 FAIL, 5 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
  - WARN form-numbers: Step 7: a chain that mixes operators. one such chain passed on the form and one was flagged in a step that also spelled a number out (aq-02626 q03 Steps 5 and 4): prefer one two-operand calculation per step
  - WARN period: names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; confirm the period is pinned (rule 9b)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how many percentage points did Snap's gross margin rise from the third quarter to the fourth quarter of 2025? Answer to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
3.8
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, condensed consolidated statements of operations, three months and year ended December 31, 2025): fourth-quarter 2025 revenue was 1,716,461 and cost of revenue 702,443; cost of revenue for the full year 2025 was 2,669,575 (thousands of dollars).
Step 2. Source input (Doc 5, condensed consolidated statements of operations, six months ended June 30, 2025): first-half 2025 cost of revenue was 1,292,912 (thousands of dollars).
Step 3. Source input (Doc 5, supplemental financial information and business metrics, third-quarter 2025 column): third-quarter 2025 revenue was 1,506,839 (thousands of dollars).
Step 4. Calculation (Doc 7 and Doc 5): no release prints third-quarter 2025 cost of revenue; it is the full year less the fourth quarter less the first half: 2,669,575 - 702,443 - 1,292,912 = 674,220 (thousands of dollars, derived).
Step 5. Calculation (Doc 7): fourth-quarter 2025 cost of revenue as a share of revenue: 702,443 / 1,716,461 = 40.92% (derived); gross margin is the rest of revenue.
Step 6. Calculation (Doc 7 and Doc 5): third-quarter 2025 cost of revenue as a share of revenue: 674,220 / 1,506,839 = 44.74% (derived).
Step 7. Final answer (Doc 7 and Doc 5): gross margin rose by as much as the cost-of-revenue share fell from the third quarter to the fourth: 674,220 / 1,506,839 - 702,443 / 1,716,461 = 3.8% of revenue, a rise of that many percentage points, rounded as the question asks.
```

### Answer components

Component 1

```text
3.8
```

### Evidence

Evidence 1: document Doc 7 (Snap-Inc-Q4-2025-Earnings-Release.txt), proves component 1. 3.8 (local note: l.223, statement of operations, three months and year ended December 31)

```text
|Revenue|$1,716,461|$1,557,283|$5,931,447|$5,361,398|
```

Evidence 2: document Doc 7 (Snap-Inc-Q4-2025-Earnings-Release.txt), proves component 1. 3.8 (local note: l.225, statement of operations)

```text
|Cost of revenue|702,443|671,660|2,669,575|2,474,237|
```

Evidence 3: document Doc 5 (Snap-Inc-Q2-2026-Earnings-Release.txt), proves component 1. 3.8 (local note: l.145, statement of operations, three and six months ended June 30)

```text
|Cost of revenue|667,885|653,333|1,333,126|1,292,912|
```

Evidence 4: document Doc 5 (Snap-Inc-Q2-2026-Earnings-Release.txt), proves component 1. 3.8 (local note: l.311, supplemental table, Q1 2025 to Q2 2026)

```text
|Revenue|$1,363,217|$1,344,930|$1,506,839|$1,716,461|$1,528,791|$1,598,993|
```

### Necessary documents

- Tick Doc 7 (Snap-Inc-Q4-2025-Earnings-Release.txt), role: Answer component
- Tick Doc 5 (Snap-Inc-Q2-2026-Earnings-Release.txt), role: Answer component

Leave unticked: Doc 1 (Pinterest-Q2-2026-Earnings-Release.txt), Doc 2 (Pinterest-Q1-2026-Earnings-Release.txt), Doc 3 (Pinterest-Q4-2025-Earnings-Release.txt), Doc 4 (Pinterest-Q1-2026-Quarterly-Report.txt), Doc 6 (Snap-Inc-Q1-2026-Earnings-Release.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Doc 7's headline says Q4 gross margin was 'up 4 percentage points sequentially', a whole-number rounding, giving 4.0. No release prints Q3 2025 cost of revenue; backing it out (full year less Q4 less Doc 5's first half) gives margins of 55.26% and 59.08%, so 3.8.
```

(46 / 50 words.)
