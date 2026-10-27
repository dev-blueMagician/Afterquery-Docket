# aq-02933 q03 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02933 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 04ea99cc6f0ab842020f6be6133faafa412ba69dc288b323c0a3e147fdb1f55e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 6, D06 = Doc 5.
- Floor: 0 FAIL, 8 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 6 doesn't mention 485. Doc 6 prints it first at character 36,942, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 6 doesn't mention 361. Doc 6 prints it first at character 36,949, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 6 doesn't mention 2,269. Doc 6 prints it first at character 36,980, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 6 doesn't mention 1,893. Doc 6 prints it first at character 36,989, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 221. Doc 5 prints it first at character 45,920, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 273. Doc 5 prints it first at character 45,938, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 5 doesn't mention 188. Doc 5 prints it first at character 45,213, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
From 2019 to 2025, across States with CMS-reported enrolled totals for both years, by how many did the home health agencies lost exceed the hospices gained?
```

### Number of asks

1 ask

### Gold answer

```text
315 providers
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, footnote to section II.C): between 2019 and 2025 the number of enrolled HHAs in Michigan dropped from 485 to 361, and in Texas from 2,269 to 1,893. Doc 6 gives no other State's HHA totals for both years.

Step 2. Source input (Doc 5, section II.C): enrolled hospices in Georgia rose from 221 in CY 2019 to 273 in CY 2025. Enrolled Nevada hospices stood at 188 in CY 2025. The figure printed beside it, 138, is Nevada's total for CY 2023, not CY 2019.

Step 3. Source input (Doc 5, Table 1): Nevada's enrolled hospices in CY 2019 numbered 55. Arizona, California and Texas have totals for CY 2019 and CY 2023 only, and Table 2's CY 2025 column counts newly enrolling hospices, so no other State has hospice totals for both years.

Step 4. Calculation (Doc 5 and Doc 6): HHAs lost in Michigan: 485 - 361 = 124.

Step 5. Calculation (Doc 5 and Doc 6): HHAs lost in Texas: 2,269 - 1,893 = 376.

Step 6. Calculation (Doc 5 and Doc 6): HHAs lost in all: 124 + 376 = 500.

Step 7. Calculation (Doc 5 and Doc 6): hospices gained in Georgia: 273 - 221 = 52.

Step 8. Calculation (Doc 5 and Doc 6): hospices gained in Nevada: 188 - 55 = 133.

Step 9. Calculation (Doc 5 and Doc 6): hospices gained in all: 52 + 133 = 185.

Step 10. Final answer (Doc 5 and Doc 6): HHAs lost beyond hospices gained: 500 - 185 = 315.
```

### Answer components

Component 1

```text
315 providers
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_09717.txt), proves component 1. 315 providers (local note: footnote 23, offset 36,866)

```text
Between 2019 and 2025, the number of enrolled HHAs in Michigan dropped from 485 to 361 (over 25 percent) and from 2,269 to 1,893 in Texas (roughly 17 percent).
```

Evidence 2: document Doc 5 (fr_2026_09718.txt), proves component 1. 315 providers (local note: section II.C, Georgia, offset 45,838)

```text
In Georgia, there have been sharp increases in the number of hospices there--from 221 in CY 2019 to 273 in CY 2025, or a 24 percent rise
```

Evidence 3: document Doc 5 (fr_2026_09718.txt), proves component 1. 315 providers (local note: section II.C, Nevada, offset 45,069)

```text
The total number of enrolled Nevada hospices continues to rise at a rate well beyond that of the beneficiary population--from 138 in CY 2023 to 188 in CY 2025, or 36 percent.
```

Evidence 4: document Doc 5 (fr_2026_09718.txt), proves component 1. 315 providers (local note: Table 1 title, offset 15,561)

```text
Table 1--Number of Enrolled Hospices in CY 2019 and CY 2023
```

Evidence 5: document Doc 5 (fr_2026_09718.txt), proves component 1. 315 providers (local note: Table 1, Nevada row, offset 16,047)

```text
Nevada.......................................................... 55 138 151
```

### Necessary documents

- Tick Doc 6 (fr_2026_09717.txt), role: Answer component
- Tick Doc 5 (fr_2026_09718.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_08676.txt), Doc 2 (fr_2025_15492.txt), Doc 3 (fr_2026_03971.txt), Doc 4 (fr_2026_04653.txt), Doc 7 (fr_2026_17622.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Wrong year: Doc 5 prints Nevada's hospices as 138 in CY 2023 to 188 in CY 2025, beside Georgia's 2019-to-2025 pair; that pair gives gains of 102 and an answer of 398. The gold takes Nevada's CY 2019 total, 55, from Table 1: gains 185, answer 315.
```

(47 / 50 words.)
