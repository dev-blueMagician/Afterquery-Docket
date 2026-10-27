# aq-04045 q03 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-04045 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 4b2660455595a724be24895b9d526ec9b1af16242646ae41bc1a919a8d64c0c5: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D07 = Doc 7.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 71. Doc 3 prints it first at character 36,522, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 48. Doc 3 prints it first at character 36,690, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 7 doesn't mention 57. expected false alarm: Doc 7 prints it at character 61,753, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 2: Doc 7 doesn't mention 40. Doc 7 prints it first at character 45,724, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how many percentage points did the share of satellite telecommunications providers with 1,500 or fewer employees change between the FCC's earliest and latest year-end counts? Give the sign, to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
+2.6 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, the satellite telecommunications paragraph of its regulatory flexibility analysis): as of December 31, 2020, 71 providers reported providing satellite telecommunications services, and the FCC estimates that about 48 of them were at or below the employee limit the question names.

Step 2. Source input (Doc 7, the same paragraph of its regulatory flexibility analysis): at the end of 2023 there were 57 such providers, and about 40 of them were at or below that limit.

Step 3. Period check (Doc 3 and Doc 7): the end of 2020 is the earliest year-end, and the end of 2023 the latest, for which the documents give this count, so the change runs from the figures in Doc 3 to the figures in Doc 7.

Step 4. Calculation (Doc 3 and Doc 7): the change is the later share, 40 of 57, less the earlier share, 48 of 71. To round only once, both shares are put over one denominator. Numerator of the later share: 40 × 71 = 2,840

Step 5. Calculation (Doc 3 and Doc 7): numerator of the earlier share over the same denominator: 48 × 57 = 2,736

Step 6. Calculation (Doc 3 and Doc 7): difference of the numerators: 2,840 − 2,736 = 104

Step 7. Calculation (Doc 3 and Doc 7): the shared denominator: 57 × 71 = 4,047

Step 8. Final answer (Doc 3 and Doc 7): the change in the share, as a percentage of all providers and to one decimal place: 104 / 4,047 = 2.6%. The later share is the larger, so the sign is plus, and because both shares are percentages of all providers the change is in percentage points.
```

### Answer components

Component 1

```text
+2.6 percentage points
```

### Evidence

Evidence 1: document Doc 3 (fr_2024_17093.txt), proves component 1. +2.6 percentage points (local note: FRFA, Satellite Telecommunications)

```text
based on Commission data in the 2021 Universal Service Monitoring Report, as of December 31, 2020, there were 71 providers that reported they were engaged in the provision of satellite telecommunications services
```

Evidence 2: document Doc 3 (fr_2024_17093.txt), proves component 1. +2.6 percentage points (local note: FRFA, Satellite Telecommunications)

```text
the Commission estimates that approximately 48 providers have 1,500 or fewer employees
```

Evidence 3: document Doc 7 (fr_2025_16375.txt), proves component 1. +2.6 percentage points (local note: FRFA, para 58)

```text
based on Commission data in the 2024 Universal Service Monitoring Report, as of December 31, 2023, there were 57 providers that reported they were engaged in the provision of satellite telecommunications services
```

Evidence 4: document Doc 7 (fr_2025_16375.txt), proves component 1. +2.6 percentage points (local note: FRFA, para 58)

```text
the Commission estimates that approximately 40 providers have 1,500 or fewer employees
```

### Necessary documents

- Tick Doc 3 (fr_2024_17093.txt), role: Answer component
- Tick Doc 7 (fr_2025_16375.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_03506.txt), Doc 2 (fr_2024_16348.txt), Doc 4 (fr_2024_23975.txt), Doc 5 (fr_2025_03993.txt), Doc 6 (fr_2025_12579.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong year or edition: Doc 2 prints the year-end 2021 count three times; the earliest count, year-end 2020, appears once, in Doc 3. Starting from Doc 2's 42 of 65 gives a 5.6-point rise to Doc 7's 40 of 57. Doc 3's 48 of 71 gives +2.6.
```

(47 / 50 words.)
