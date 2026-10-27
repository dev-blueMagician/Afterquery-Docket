# aq-02483 q02 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02483 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 5a9f9e391119666fd1246d1fcc1a971dcd53ac5c893152d3d1e1b693aed9b64b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D06 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
To the nearest week, how far apart were Wisconsin's deadline for CCR landfills' initial-permitting submittals and Wyoming's for existing CCR impoundments' permit applications?
```

### Number of asks

1 ask

### Gold answer

```text
28 weeks
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Permit Requirements and Permitting Process): "Existing CCR surface impoundments must submit a new permit application within 12 months of the effective date of the State rule." Doc 2 places Wyoming's State CCR rules in Solid Waste Rules chapter 18.
Step 2. Source input (Doc 2, Wyoming CCR Regulations): "chapter 18 became effective on August 19, 2022".
Step 3. Derived (Doc 2): 12 months after August 19, 2022 is August 19, 2023, Wyoming's deadline for existing CCR impoundments' permit applications.
Step 4. Source input (Doc 6 and Doc 2, deadlines compared): Doc 6 (Wisconsin CCR Permits) states that under Wisconsin's revised CCR landfill regulations "the six CCR landfills were required to submit a plan of operation modification for initial permitting by February 1, 2023". That Wisconsin deadline falls before Wyoming's August 19, 2023 deadline from Step 3.
Step 5. Calculation (Doc 2 and Doc 6): 7 * 28 = 196 days, so 28 weeks after February 1, 2023 is August 16, 2023.
Step 6. Calculation (Doc 2 and Doc 6): from August 16 to August 19, 2023: 19 - 16 = 3 days.
Step 7. Calculation (Doc 2 and Doc 6): 196 + 3 = 199 days between February 1 and August 19, 2023, that is 28 weeks and 3 days.
Step 8. Final answer (Doc 2 and Doc 6): 3 days is less than half a week, so to the nearest week the two deadlines are 28 weeks apart.
```

### Answer components

Component 1

```text
28
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_16801.txt), proves component 1. 28 (local note: Permit Requirements and Permitting Process, L202)

```text
Existing CCR surface impoundments must submit a new permit application within 12 months of the effective date of the State rule.
```

Evidence 2: document Doc 2 (fr_2025_16801.txt), proves component 1. 28 (local note: Permit Required, L198)

```text
required to comply with State CCR rules found at Wyoming Administrative Rules, Environmental Quality, Solid Waste Rules (SWR) chapter 18
```

Evidence 3: document Doc 2 (fr_2025_16801.txt), proves component 1. 28 (local note: Wyoming CCR Regulations, L278)

```text
chapter 18 became effective on August 19, 2022
```

Evidence 4: document Doc 6 (fr_2026_18552.txt), proves component 1. 28 (local note: Wisconsin CCR Permits, L456)

```text
the six CCR landfills were required to submit a plan of operation modification for initial permitting by February 1, 2023
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 6 (fr_2026_18552.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 3 (fr_2026_08662.txt), Doc 4 (fr_2026_11312.txt), Doc 5 (fr_2026_14118.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 2 dates Wyoming's chapter 18 to August 19, 2022; taking that as the impoundments' deadline puts it 24 weeks before Wisconsin's February 1, 2023 (Doc 6). Doc 2's rule allows 12 months, to August 19, 2023: 199 days, 28 weeks after.
```

(44 / 50 words.)
