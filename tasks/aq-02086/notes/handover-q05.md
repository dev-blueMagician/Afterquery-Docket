# aq-02086 q05 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02086 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 48cea5c5d5063443e4c08f3ae489234fbb16e9e8d6b68572e531bee335367479: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 4, D02 = Doc 1.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By what percentage did the percentage point gap between private and social rented non-decency shrink from 2010 to 2020, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
53.5%
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 4, introduction): the proportion of substandard dwellings in the private rented sector fell from 37.2% in 2010 to 21.0% in 2020.

Step 2. Source fact (Doc 4, background to the Decent Homes Standard): the proportion of social rented homes that do not meet the Standard fell from 39% in 2001 to 13% in 2020.

Step 3. Source fact (Doc 1, introduction): in 2010, 759,000 social rented homes (20%) were non-decent.

Step 4. Calculation (from Steps 1 and 3; Doc 4 and Doc 1), percentage-point gap in 2010: 37.2 - 20 = 17.2 percentage points.

Step 5. Calculation (from Steps 1 and 2; Doc 4), percentage-point gap in 2020: 21.0 - 13 = 8 percentage points.

Step 6. Calculation (from Steps 4 and 5; Doc 4 and Doc 1), narrowing of the gap: 17.2 - 8 = 9.2 percentage points.

Step 7. Calculation (from Steps 4 and 6; Doc 4 and Doc 1), narrowing as a share of the 2010 gap: 9.2 / 17.2 = 53.5% (to one decimal place).
```

### Answer components

Component 1

```text
53.5%
```

### Evidence

Evidence 1: document Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), proves component 1. 53.5% (local note: L235, introduction)

```text
the proportion of substandard dwellings in the private rented sector falling from 37.2% in 2010 to 21.0% in 2020
```

Evidence 2: document Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), proves component 1. 53.5% (local note: L259, Decent Homes Standard background)

```text
the proportion of homes that do not meet the Standard has reduced from 39% in 2001 to 13% in 2020
```

Evidence 3: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 1. 53.5% (local note: L239, introduction)

```text
In 2021, there were 380,000 (10%) non-decent social rented homes, down from 759,000 (20%) in 2010.
```

### Necessary documents

- Tick Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), role: Answer component
- Tick Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), role: Answer component

Leave unticked: Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), Doc 3 (Awaabs-Law-government-response.txt), Doc 5 (Response-to-the-consultation-on-a-Decent-Homes-Standard-in.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Failure mode 2

Trap: Out-of-range period

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 1's 10% social share is for 2021 and Doc 5's for 2023; using either for 2020 gives 36.0%. Doc 4 gives social non-decency for 2001 (39%), not 2010; using it makes the gap widen 9.8 points. Gold: gaps 17.2 and 8.0, shrink 53.5%.
```

(44 / 50 words.)
