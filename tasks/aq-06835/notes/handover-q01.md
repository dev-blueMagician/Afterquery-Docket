# aq-06835 q01 hand-over

Generated 2026-10-18 by `python tools/check_questions.py tasks/aq-06835 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 81781c91447613e54743d6385b1bc42c0622dd77c51e68f0d3dfe5613bb72da0: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D08 = Doc 6, D09 = Doc 4.
- Floor: 0 FAIL, 12 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 4 doesn't mention 1,623.6. Doc 4 prints it first at character 44,997, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 4 doesn't mention 5,944.1. Doc 4 prints it first at character 45,015, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 4 doesn't mention 72.4%. Doc 4 prints it first at character 45,205, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 6 doesn't mention 3,986.4. Doc 6 prints it first at character 23,227, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 6 doesn't mention 2,867.6. Doc 6 prints it first at character 42,248, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 6 doesn't mention 72.3%. Doc 6 prints it first at character 42,435, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 4 doesn't mention 154.5. Doc 4 prints it first at character 24,019, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 4 doesn't mention 1,098.1. Doc 4 prints it first at character 25,194, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 8: Doc 6 doesn't mention 592.3. Doc 6 prints it first at character 23,640, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN period: names a quarter or fiscal year without 'fiscal'/'calendar'/'ended'; confirm the period is pinned (rule 9b)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
For Zimmer Biomet's 2025 quarter with the highest adjusted gross margin, what was its reported operating profit margin? Give the percentage to two decimal places.
```

### Number of asks

1 ask

### Gold answer

```text
17.55%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 4, reconciliation of gross profit and margin, three months and year ended December 31, 2025): net sales 2,243.8 (fourth quarter) and 8,231.5 (full year); adjusted gross profit 1,623.6 (fourth quarter) and 5,944.1 (full year), in $ millions; the fourth-quarter adjusted gross margin is printed as 72.4%.
Step 2. Source input (Doc 6, reconciliation of gross profit and margin, six months ended June 30, 2025): net sales 3,986.4 and adjusted gross profit 2,867.6 ($ millions); the second-quarter 2025 adjusted gross margin is printed as 72.3%.
Step 3. Calculation (Doc 4 and Doc 6): third-quarter 2025 adjusted gross profit, full year less fourth quarter less first half = 5,944.1 - 1,623.6 - 2,867.6 = 1,452.9 ($ millions).
Step 4. Calculation (Doc 4 and Doc 6): third-quarter 2025 net sales = 8,231.5 - 2,243.8 - 3,986.4 = 2,001.3 ($ millions).
Step 5. Calculation (Doc 4 and Doc 6): third-quarter 2025 adjusted gross margin = 1,452.9 / 2,001.3 = 72.60%.
Step 6. Comparison (Doc 4 and Doc 6): first-half 2025 adjusted gross margin = 2,867.6 / 3,986.4 = 71.93%. The second quarter's printed 72.3% is above that first-half average, so the first quarter's margin is below it. The third quarter's 72.60% is above that average and above the second quarter's 72.3% and the fourth quarter's 72.4%, so the third quarter of 2025 has the highest adjusted gross margin.
Step 7. Source input (Doc 4, reconciliation of operating profit and margin, three months and year ended December 31, 2025): operating profit 154.5 (fourth quarter) and 1,098.1 (full year), in $ millions.
Step 8. Source input (Doc 6, reconciliation of operating profit and margin, six months ended June 30, 2025): operating profit 592.3 ($ millions).
Step 9. Calculation (Doc 4 and Doc 6): third-quarter 2025 operating profit as reported = 1,098.1 - 154.5 - 592.3 = 351.3 ($ millions).
Step 10. Calculation (Doc 4 and Doc 6): third-quarter 2025 reported operating profit margin = 351.3 / 2,001.3 = 17.55%, rounded as the question asks.
```

### Answer components

Component 1

```text
17.55%
```

### Evidence

Evidence 1: document Doc 4 (zimmer-biomet-holdings-inc-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), proves component 1. 17.55% (local note: reconciliation of gross profit and margin, three months and years ended December 31, 2025 and 2024)

```text
|Net Sales|$2,243.8|$2,023.2|$8,231.5|$7,678.6|
```

Evidence 2: document Doc 4 (zimmer-biomet-holdings-inc-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), proves component 1. 17.55% (local note: same table)

```text
|Adjusted gross profit|$1,623.6|$1,442.5|$5,944.1|$5,506.7|
```

Evidence 3: document Doc 4 (zimmer-biomet-holdings-inc-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), proves component 1. 17.55% (local note: same table)

```text
|Adjusted gross margin|72.4%|71.3%|72.2%|71.7%|
```

Evidence 4: document Doc 4 (zimmer-biomet-holdings-inc-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), proves component 1. 17.55% (local note: reconciliation of operating profit and margin, same periods)

```text
|Operating profit|$154.5|$389.0|$1,098.1|$1,285.7|
```

Evidence 5: document Doc 6 (zimmer-biomet-holdings-inc-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 17.55% (local note: reconciliation of gross profit and margin, three and six months ended June 30, 2026 and 2025)

```text
|Net Sales|$2,177.0|$2,077.3|$4,263.7|$3,986.4|
```

Evidence 6: document Doc 6 (zimmer-biomet-holdings-inc-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 17.55% (local note: same table)

```text
|Adjusted gross profit|$1,547.5|$1,502.1|$3,071.4|$2,867.6|
```

Evidence 7: document Doc 6 (zimmer-biomet-holdings-inc-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 17.55% (local note: same table)

```text
|Adjusted gross margin|71.1%|72.3%|72.0%|71.9%|
```

Evidence 8: document Doc 6 (zimmer-biomet-holdings-inc-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), proves component 1. 17.55% (local note: reconciliation of operating profit and margin, same periods)

```text
|Operating profit|$326.1|$300.0|$699.2|$592.3|
```

### Necessary documents

- Tick Doc 4 (zimmer-biomet-holdings-inc-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), role: Answer component
- Tick Doc 6 (zimmer-biomet-holdings-inc-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-08-05.txt), role: Answer component

Leave unticked: Doc 1 (stryker-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-29.txt), Doc 2 (stryker-corporation-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-30.txt), Doc 3 (stryker-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-30.txt), Doc 5 (zimmer-biomet-holdings-inc-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-28.txt), Doc 7 (edwards-lifesciences-corporation-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), Doc 8 (edwards-lifesciences-corporation-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-23.txt), Doc 9 (edwards-lifesciences-corporation-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-23.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 4 prints a 72.4% fourth-quarter 2025 adjusted gross margin, the highest any release prints, so a careless solver picks the fourth quarter and answers 6.89%. The third quarter, printed nowhere, is full year less first half (Doc 6) less fourth quarter: 72.60%, higher, so 17.55%.
```

(46 / 50 words.)
