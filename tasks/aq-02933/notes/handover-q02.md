# aq-02933 q02 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02933 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 5ee9d6414251abc96db5ecd7f498efc3fe836179ce960e69dff204e486f58a18: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D06 = Doc 5.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 300. Doc 3 prints it first at character 42,385, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 166. Doc 5 prints it first at character 57,975, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At the yearly enrollment paces CMS cites, how many would-be enrollees would six months keep out: medical supply companies plus hospices outside its five outlier States?
```

### Number of asks

1 ask

### Gold answer

```text
383 enrollees
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, section II.F.1): after its yearly figure for medical supply companies enrolling in Medicare, CMS gives the same pace for half a year: 300 over a 6-month period.

Step 2. Source input (Doc 5, section V.C.1): leaving out its outliers, Arizona, California, Georgia, Nevada and Texas, CMS gives new hospice enrollments between CY 2023 and CY 2025 as 166 per year. It prints no six-month figure for hospices.

Step 3. Calculation (Doc 3 and Doc 5): six months is half a year, so the hospice figure for six months is 166 / 2 = 83.

Step 4. Final answer (Doc 3 and Doc 5): medical supply companies and hospices kept out over six months: 300 + 83 = 383.
```

### Answer components

Component 1

```text
383 enrollees
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_03971.txt), proves component 1. 383 enrollees (local note: section II.F.1, offset 42,309)

```text
approximately 600 medical supply companies enroll in Medicare each year (or 300 over a 6-month period)
```

Evidence 2: document Doc 5 (fr_2026_09718.txt), proves component 1. 383 enrollees (local note: section V.C.1, offset 57,790)

```text
Excluding the aforementioned outliers in Arizona, California, Georgia, Nevada, and Texas, between CY 2023 and CY 2025 the combined nationwide number of new enrollments was roughly 500 (166 per year)
```

### Necessary documents

- Tick Doc 3 (fr_2026_03971.txt), role: Answer component
- Tick Doc 5 (fr_2026_09718.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_08676.txt), Doc 2 (fr_2025_15492.txt), Doc 4 (fr_2026_04653.txt), Doc 6 (fr_2026_09717.txt), Doc 7 (fr_2026_17622.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 3 prints a six-month figure, 300, but Doc 5's hospice figure is 166 per year; adding the two printed figures gives 466. The gold halves 166 to 83 for six months and adds 300, giving 383.
```

(40 / 50 words.)
