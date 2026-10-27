# aq-06835 q02 hand-over

Generated 2026-10-19 by `python tools/check_questions.py tasks/aq-06835 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 2f3bf1c94fcf6fe0ed6ad5f50973b76bac62b0ee94c9d3e4ba2e09da11d07e49: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 3, D06 = Doc 1.
- Floor: 0 FAIL, 11 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 4,679. Doc 1 prints it first at character 22,690, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 16,391. Doc 1 prints it first at character 28,087, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 3,934. Doc 3 prints it first at character 23,481, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 7,779. Doc 3 prints it first at character 28,716, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 5: Doc 1 doesn't mention 4,679. Doc 1 prints it first at character 22,690, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 6: Doc 3 doesn't mention 3,934. Doc 3 prints it first at character 23,481, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 3 doesn't mention 7,779. Doc 3 prints it first at character 28,716, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN period: names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; confirm the period is pinned (rule 9b)
  - WARN sibling: six words shared with q01: 'give the percentage to two decimal'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
For Stryker's 2025 quarter with the lowest adjusted gross profit margin, what was its reported operating income margin? Give the percentage to two decimal places.
```

### Number of asks

1 ask

### Gold answer

```text
18.74%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, consolidated statements of earnings, three months and full year ended December 31, 2025): net sales 7,171 (fourth quarter) and 25,116 (full year); operating income 1,804 (fourth quarter) and 4,889 (full year) ($ millions).
Step 2. Source input (Doc 1, reconciliation of non-GAAP measures, three months and full year 2025): adjusted gross profit 4,679 (fourth quarter) and 16,391 (full year) ($ millions).
Step 3. Source input (Doc 3, consolidated statements of earnings, three and six months ended June 30, 2025): net sales 6,022 (second quarter) and 11,888 (six months); operating income 1,950 (six months) ($ millions).
Step 4. Source input (Doc 3, reconciliation of non-GAAP measures, three and six months 2025): adjusted gross profit 3,934 (second quarter) and 7,779 (six months) ($ millions).
Step 5. Calculation (Doc 1): fourth-quarter 2025 adjusted gross profit margin = 4,679 / 7,171 = 65.25%.
Step 6. Calculation (Doc 3): second-quarter 2025 adjusted gross profit margin = 3,934 / 6,022 = 65.33%.
Step 7. Calculation (Doc 3): first-half 2025 adjusted gross profit margin = 7,779 / 11,888 = 65.44%.
Step 8. Calculation (Doc 1 and Doc 3): third-quarter 2025 adjusted gross profit, full year less fourth quarter less first half = 16,391 - 4,679 - 7,779 = 3,933 ($ millions).
Step 9. Calculation (Doc 1 and Doc 3): third-quarter 2025 net sales = 25,116 - 7,171 - 11,888 = 6,057 ($ millions).
Step 10. Calculation (Doc 1 and Doc 3): third-quarter 2025 adjusted gross profit margin = 3,933 / 6,057 = 64.93%.
Step 11. Comparison (Doc 1 and Doc 3): the second quarter's 65.33% is below the first-half 65.44%, so the first quarter's margin is above 65.44%. The third quarter's 64.93% is below that, below the second quarter's 65.33% and below the fourth quarter's 65.25%, so the third quarter of 2025 has the lowest adjusted gross profit margin.
Step 12. Calculation (Doc 1 and Doc 3): third-quarter 2025 operating income as reported = 4,889 - 1,804 - 1,950 = 1,135 ($ millions).
Step 13. Calculation (Doc 1 and Doc 3): third-quarter 2025 reported operating income margin = 1,135 / 6,057 = 18.74%, rounded as the question asks.
```

### Answer components

Component 1

```text
18.74%
```

### Evidence

Evidence 1: document Doc 1 (stryker-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-29.txt), proves component 1. 18.74% (local note: consolidated statements of earnings, three months and full year 2025 and 2024)

```text
|Net sales|$7,171|$6,436|11.4%|$25,116|$22,595|11.2%|
```

Evidence 2: document Doc 1 (stryker-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-29.txt), proves component 1. 18.74% (local note: same statements)

```text
|Operating income|$1,804|$581|210.5%|$4,889|$3,689|32.5%|
```

Evidence 3: document Doc 1 (stryker-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-29.txt), proves component 1. 18.74% (local note: reconciliation of non-GAAP measures, three months 2025)

```text
|Adjusted|$4,679|$2,135|$380|$2,164|$(107)|$331|$1,726|16.1%|$4.47|
```

Evidence 4: document Doc 1 (stryker-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-29.txt), proves component 1. 18.74% (local note: reconciliation of non-GAAP measures, full year 2025)

```text
|Adjusted|$16,391|$8,221|$1,567|$6,603|$(402)|$934|$5,267|15.1%|$13.63|
```

Evidence 5: document Doc 3 (stryker-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-30.txt), proves component 1. 18.74% (local note: consolidated statements of earnings, three and six months 2026 and 2025)

```text
|Net sales|$6,589|$6,022|9.4%|$12,609|$11,888|6.1%|
```

Evidence 6: document Doc 3 (stryker-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-30.txt), proves component 1. 18.74% (local note: same statements)

```text
|Operating income|$1,659|$1,113|49.1%|$2,595|$1,950|33.1%|
```

Evidence 7: document Doc 3 (stryker-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-30.txt), proves component 1. 18.74% (local note: reconciliation of non-GAAP measures, three months 2025)

```text
|Adjusted|$3,934|$1,993|$396|$1,545|$(106)|$228|$1,211|15.9%|$3.13|
```

Evidence 8: document Doc 3 (stryker-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-30.txt), proves component 1. 18.74% (local note: reconciliation of non-GAAP measures, six months 2025)

```text
|Adjusted|$7,779|$4,101|$789|$2,889|$(179)|$402|$2,308|14.9%|$5.97|
```

### Necessary documents

- Tick Doc 1 (stryker-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-29.txt), role: Answer component
- Tick Doc 3 (stryker-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-30.txt), role: Answer component

Leave unticked: Doc 2 (stryker-corporation-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-30.txt), Doc 4 (zimmer-biomet-holdings-inc-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), Doc 5 (zimmer-biomet-holdings-inc-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-28.txt), Doc 6 (zimmer-biomet-holdings-inc-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), Doc 7 (edwards-lifesciences-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), Doc 8 (edwards-lifesciences-corporation-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-23.txt), Doc 9 (edwards-lifesciences-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-23.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 1 prints a 65.2% fourth-quarter 2025 adjusted gross profit margin, the lowest any release prints for 2025, so a careless solver picks the fourth quarter and answers 25.16%. The third quarter, printed nowhere, is full year less first half (Doc 3) less fourth quarter: 64.93%, lower, so 18.74%.
```

(49 / 50 words.)
