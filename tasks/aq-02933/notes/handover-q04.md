# aq-02933 q04 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-02933 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 5, difficulty_target medium, origin claude.
- tested_sha256 d6a2c4caa1dabf3c2476fb3ac9602a0955e49a4b9163ef10885a0d80467603a4: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 6, D06 = Doc 5.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 221. Doc 5 prints it first at character 45,920, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Across every State whose 2019 hospice total appears in CMS's hospice notice, leaving California out, what percentage of those hospices were in States CMS names for home health agencies sharing an address? Two decimal places.
```

### Number of asks

1 ask

### Gold answer

```text
67.45%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, Table 1, "Number of Enrolled Hospices in CY 2019 and CY 2023"): leaving California out as the question says, the table's CY 2019 totals are Arizona 152, Nevada 55 and Texas 718.

Step 2. Source input (Doc 5, section II.C): outside the table, CMS gives one more State's total for that year: Georgia had 221 hospices in CY 2019. No other State has a 2019 hospice total. Nevada's other 2019 figure counts new enrollments.

Step 3. Source input (Doc 6, section II.B): CMS found numerous HHAs operating out of a single, common practice location in Ohio, and adds that similar situations have been seen in Texas, Michigan, North Carolina and Nevada.

Step 4. Matching (Doc 5 and Doc 6): of the States in Steps 1 and 2, Doc 6 names Texas and Nevada. Arizona and Georgia do not appear in Doc 6. Ohio, Michigan and North Carolina have no hospice total.

Step 5. Calculation (Doc 5 and Doc 6): hospices in the named States, Texas and Nevada: 718 + 55 = 773.

Step 6. Calculation (Doc 5 and Doc 6): hospices in the other States, Arizona and Georgia: 152 + 221 = 373.

Step 7. Calculation (Doc 5 and Doc 6): all the hospices counted: 773 + 373 = 1,146.

Step 8. Final answer (Doc 5 and Doc 6): share in the named States, to two decimal places: 773 / 1,146 = 67.45%.
```

### Answer components

Component 1

```text
67.45%
```

### Evidence

Evidence 1: document Doc 5 (fr_2026_09718.txt), proves component 1. 67.45% (local note: Table 1 title, offset 15,561)

```text
Table 1--Number of Enrolled Hospices in CY 2019 and CY 2023
```

Evidence 2: document Doc 5 (fr_2026_09718.txt), proves component 1. 67.45% (local note: Table 1, Arizona row, offset 15,889)

```text
Arizona......................................................... 152 311 105
```

Evidence 3: document Doc 5 (fr_2026_09718.txt), proves component 1. 67.45% (local note: Table 1, Nevada row, offset 16,047)

```text
Nevada.......................................................... 55 138 151
```

Evidence 4: document Doc 5 (fr_2026_09718.txt), proves component 1. 67.45% (local note: Table 1, Texas row, offset 16,123)

```text
Texas........................................................... 718 1,081 51
```

Evidence 5: document Doc 5 (fr_2026_09718.txt), proves component 1. 67.45% (local note: section II.C, Georgia, offset 45,838)

```text
In Georgia, there have been sharp increases in the number of hospices there--from 221 in CY 2019 to 273 in CY 2025, or a 24 percent rise
```

Evidence 6: document Doc 6 (fr_2026_09717.txt), proves component 1. 67.45% (local note: section II.B, offset 18,479)

```text
CMS has recently detected several situations in Ohio where numerous HHAs are operating out of a single, common practice location
```

Evidence 7: document Doc 6 (fr_2026_09717.txt), proves component 1. 67.45% (local note: section II.B, offset 18,838)

```text
Similar situations have been seen in Texas, Michigan, North Carolina, and Nevada.
```

### Necessary documents

- Tick Doc 6 (fr_2026_09717.txt), role: Used to identify
- Tick Doc 5 (fr_2026_09718.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_08676.txt), Doc 2 (fr_2025_15492.txt), Doc 3 (fr_2026_03971.txt), Doc 4 (fr_2026_04653.txt), Doc 7 (fr_2026_17622.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 5's Table 1 holds only part of the States with a 2019 total; Georgia's 221 is in the text of section II.C. Taking the table's three non-California States as the whole base gives 773 of 925, 83.57%. The gold's base is 1,146: 67.45%.
```

(47 / 50 words.)
