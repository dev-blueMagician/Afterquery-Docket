# aq-06809 q01 hand-over

Generated 2026-10-18 by `python tools/check_questions.py tasks/aq-06809 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 70f0d32351b2595f0690a1cdc831abf2522e3131c2c262601bdedc359f320736: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 5, D05 = Doc 3.
- Floor: 0 FAIL, 22 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 17,038. Doc 3 prints it first at character 45,569, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 17,016. Doc 3 prints it first at character 45,560, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 149,338. Doc 3 prints it first at character 45,822, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 3 doesn't mention 152,317. Doc 3 prints it first at character 45,812, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: a chain that mixes operators. one such chain passed on the form and one was flagged in a step that also spelled a number out (aq-02626 q03 Steps 5 and 4): prefer one two-operand calculation per step
  - WARN form-numbers: Step 2: Doc 3 doesn't mention 17,038. Doc 3 prints it first at character 45,569, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 3 doesn't mention 149,338. Doc 3 prints it first at character 45,822, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 3 doesn't mention 17,016. Doc 3 prints it first at character 45,560, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 3 doesn't mention 152,317. Doc 3 prints it first at character 45,812, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 5 doesn't mention 21,160. Doc 5 prints it first at character 40,800, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 5 doesn't mention 21,388. Doc 5 prints it first at character 40,793, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 5 doesn't mention 208,132. Doc 5 prints it first at character 41,388, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 5 doesn't mention 214,192. Doc 5 prints it first at character 41,378, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: a chain that mixes operators. one such chain passed on the form and one was flagged in a step that also spelled a number out (aq-02626 q03 Steps 5 and 4): prefer one two-operand calculation per step
  - WARN form-numbers: Step 4: Doc 5 doesn't mention 21,160. Doc 5 prints it first at character 40,800, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 5 doesn't mention 208,132. Doc 5 prints it first at character 41,388, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 5 doesn't mention 21,388. Doc 5 prints it first at character 40,793, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 5 doesn't mention 214,192. Doc 5 prints it first at character 41,378, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 5: a chain that mixes operators. one such chain passed on the form and one was flagged in a step that also spelled a number out (aq-02626 q03 Steps 5 and 4): prefer one two-operand calculation per step
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What was the difference, in basis points to the nearest basis point, between the declines in KeyCorp's and Huntington's common equity tier 1 ratios from March 31 to June 30, 2026?
```

### Number of asks

1 ask

### Gold answer

```text
6
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, GAAP to Non-GAAP Reconciliations, capital rows): KeyCorp's common equity tier 1 capital was $17,038 million at March 31, 2026 and $17,016 million at June 30, 2026, against risk-weighted assets of $149,338 million and $152,317 million. Doc 3 computes the ratio as this capital over risk-weighted assets and prints it to one decimal, 11.4% and 11.2%.
Step 2. Calculation (Doc 3): fall in KeyCorp's ratio from March 31 to June 30: 17,038 / 149,338 - 17,016 / 152,317 = 0.23758%.
Step 3. Source input (Doc 5, Basel III capital table): Huntington's common equity tier 1 capital was $21,160 million at March 31, 2026 and $21,388 million at June 30, 2026, against risk-weighted assets of $208,132 million and $214,192 million. Doc 5 computes its ratio the same way and prints it to one decimal, 10.2% and 10.0%.
Step 4. Calculation (Doc 5): fall in Huntington's ratio over the same dates: 21,160 / 208,132 - 21,388 / 214,192 = 0.18119%.
Step 5. Calculation (Doc 3 and Doc 5): KeyCorp's fall less Huntington's, from the unrounded ratios: 17,038 / 149,338 - 17,016 / 152,317 - 21,160 / 208,132 + 21,388 / 214,192 = 0.05639%.
Step 6. Final answer (Doc 3 and Doc 5): in basis points, 0.05639% × 10,000 = 5.639, which rounds to 6.
```

### Answer components

Component 1

```text
6
```

### Evidence

Evidence 1: document Doc 3 (key_ex991_2026-07-21.txt), proves component 1. 6 (local note: GAAP to Non-GAAP Reconciliations, columns 6/30/2026, 3/31/2026, 6/30/2025)

```text
Common equity tier 1 (F)|$|17,016 $|17,038 $|16,775
```

Evidence 2: document Doc 3 (key_ex991_2026-07-21.txt), proves component 1. 6 (local note: same table)

```text
Risk-weighted assets (H) (c)|$|152,317 $|149,338 $|143,427
```

Evidence 3: document Doc 3 (key_ex991_2026-07-21.txt), proves component 1. 6 (local note: same table, ratio row)

```text
Common equity tier 1 ratio (F/H) (c) 11.2 % 11.4 % 11.7 %
```

Evidence 4: document Doc 3 (key_ex991_2026-07-21.txt), proves component 1. 6 (local note: table note)

```text
(c)Amounts and ratios as of June 30, 2026 are estimated.
```

Evidence 5: document Doc 5 (hban_ex992_2026-07-23.txt), proves component 1. 6 (local note: Quarterly Capital Under Current Regulatory Standards (Basel III), column dates)

```text
June 30, March 31, December 31, September 30, June 30,
```

Evidence 6: document Doc 5 (hban_ex992_2026-07-23.txt), proves component 1. 6 (local note: same table)

```text
Common equity tier 1 capital|21,388 21,160 17,286 15,924 15,539
```

Evidence 7: document Doc 5 (hban_ex992_2026-07-23.txt), proves component 1. 6 (local note: same table)

```text
Risk-weighted assets (RWA) (1)|$|214,192 $|208,132 $|166,684 $|150,222 $|148,602
```

Evidence 8: document Doc 5 (hban_ex992_2026-07-23.txt), proves component 1. 6 (local note: same table, reconciliation)

```text
CET1 ratio (A/C)|10.0 % 10.2 % 10.4 % 10.6 % 10.5 %
```

### Necessary documents

- Tick Doc 3 (key_ex991_2026-07-21.txt), role: Answer component
- Tick Doc 5 (hban_ex992_2026-07-23.txt), role: Answer component

Leave unticked: Doc 1 (fitb_ex991_2026-07-17.txt), Doc 2 (fitb_ex992_2026-07-17.txt), Doc 4 (hban_ex991_2026-07-23.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Doc 3 prints KeyCorp's CET1 ratio as 11.4% then 11.2% and Doc 5 prints Huntington's as 10.2% then 10.0%: both fall 20 basis points, so a careless solver answers 0. Capital over risk-weighted assets gives falls of 23.76 and 18.12 basis points, a difference of 6.
```

(46 / 50 words.)
