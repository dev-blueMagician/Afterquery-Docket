# aq-05747 q02 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-05747 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 06c34c9dcd2d1ff697be00e086eb036afdc301ef592de2567473d6cb57e81d84: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 1, D03 = Doc 5.
- Floor: 0 FAIL, 2 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how many percentage points, to one decimal place, was the midpoint of the 2026 growth in comparable currency neutral EPS implied by Coca-Cola's July 2026 outlook below the 2025 growth in comparable currency neutral EPS it expected in July 2025?
```

### Number of asks

1 ask

### Gold answer

```text
1.5 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, Outlook for full year 2025, release of July 22, 2025): "The company expects to deliver comparable currency neutral EPS (non-GAAP) growth of approximately 8%."
Step 2. Source input (Doc 5, Full Year 2026 Guidance table, Current column, release of July 28, 2026): comparable EPS (non-GAAP) growth of 9% to 10%, which includes an approximate 3% currency tailwind. The table's other EPS row, 7% to 8%, is for comparable currency neutral EPS excluding acquisitions and divestitures, a separate measure.
Step 3. Source input (Doc 5 and Doc 1, definitions): comparable currency neutral EPS is adjusted for currency only, while the measure excluding acquisitions and divestitures is also adjusted for acquisitions and divestitures. Doc 1's 2025 figure is for the measure adjusted for currency only, so the 2026 figure for the same measure is comparable EPS growth less the currency tailwind.
Step 4. Calculation (Doc 1 and Doc 5): low end of the implied 2026 growth in comparable currency neutral EPS: 9 - 3 = 6 (percent).
Step 5. Calculation (Doc 1 and Doc 5): high end: 10 - 3 = 7 (percent).
Step 6. Calculation (Doc 1 and Doc 5): sum of the two ends: 6 + 7 = 13.
Step 7. Calculation (Doc 1 and Doc 5): midpoint of the range: 13 / 2 = 6.5 (percent).
Step 8. Final answer (Doc 1 and Doc 5): 2025 expectation less the 2026 midpoint: 8 - 6.5 = 1.5 percentage points.
```

### Answer components

Component 1

```text
1.5 percentage points
```

### Evidence

Evidence 1: document Doc 1 (the-coca-cola-company-2q-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-07-22.txt), proves component 1. 1.5 percentage points (local note: Outlook, Full Year 2025)

```text
The company expects to deliver comparable currency neutral EPS (non-GAAP) growth of approximately 8%.
```

Evidence 2: document Doc 5 (the-coca-cola-company-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-28.txt), proves component 1. 1.5 percentage points (local note: Full Year 2026 Guidance, Current column, comparable EPS)

```text
9% to 10% growth, which includes: •Approx. 3% currency tailwind
```

Evidence 3: document Doc 5 (the-coca-cola-company-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-28.txt), proves component 1. 1.5 percentage points (local note: Definitions, comparable EPS measures)

```text
Comparable currency neutral EPS (non-GAAP) has been adjusted for the impact of fluctuations in foreign currency exchange rates, and comparable currency neutral EPS excluding acquisitions and divestitures (non-GAAP) has been adjusted for the impact of fluctuations in foreign currency exchange rates and the impact of acquisitions and divestitures
```

### Necessary documents

- Tick Doc 5 (the-coca-cola-company-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-28.txt), role: Answer component
- Tick Doc 1 (the-coca-cola-company-2q-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-07-22.txt), role: Answer component

Leave unticked: Doc 2 (the-coca-cola-company-3q-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2025-10-21.txt), Doc 3 (the-coca-cola-company-4q-and-full-year-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-02-10.txt), Doc 4 (the-coca-cola-company-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-28.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 5's July 2026 table prints 7% to 8% for comparable currency neutral EPS excluding acquisitions and divestitures; using it gives 8 - 7.5 = 0.5. The asked measure, as in Doc 1's 2025 guidance (about 8%), removes only currency: 9-10% less 3% is 6-7%, so 1.5.
```

(49 / 50 words.)
