# aq-02673 q06 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02673 --handover --q q06` from questions/q06.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 2411231e3c77eaac260ac7482144898276744a12f972357074b75d389736390b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D06 = Doc 6.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: q01 has the same answer; do the two ask for the same fact?
  - WARN sibling: six words shared with q01: '2025 north atlantic swordfish total allowable'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q06.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What percentage of the 2025 North Atlantic swordfish total allowable catch was U.S. underharvest not carried into 2026, both on the same weight basis, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
18.7%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, North Atlantic swordfish section): in 2025, U.S. landings of North Atlantic swordfish were 637.7 mt dw, which is 2,514.9 mt dw less than the 2025 adjusted quota. That shortfall is the 2025 underharvest. Table 1 prints it in the 2026 column as "Underharvest from Previous Year"; the 2,558.3 in the 2025 column is the shortfall of the year before.

Step 2. Source input (Doc 6, same paragraph): the carryover is capped at 15 percent of the baseline quota, so only 440.6 mt dw of the underharvest may be carried forward.

Step 3. Calculation (Doc 6): underharvest not carried into 2026: 2,514.9 - 440.6 = 2,074.3 mt dw.

Step 4. Source input (Doc 3, North Atlantic swordfish section): the North Atlantic-wide TACs are stated in whole weight, ranging from 4,764 mt ww to 17,628 mt ww, and the TAC set for 2025-2027 is 14,769 mt, out of which the United States is allocated 3,907 mt, its baseline quota in whole weight.

Step 5. Source input (Doc 3 and Doc 6, supplementary information): swordfish weight converts from dressed to whole weight with the factor 1.33.

Step 6. Calculation (Doc 6 and Doc 3): the uncarried underharvest in whole weight: 2,074.3 × 1.33 = 2,758.819 mt ww.

Step 7. Calculation (Doc 3 and Doc 6): its share of the 2025 TAC: 2,758.819 / 14,769 = 18.7%.
```

### Answer components

Component 1

```text
18.7%
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_16870.txt), proves component 1. 18.7% (local note: North Atlantic swordfish section, 2025 landings)

```text
In 2025, U.S. landings of North Atlantic swordfish, which include landings and dead discards, were 637.7 mt dw (2,514.9 mt dw less than the 2025 adjusted quota).
```

Evidence 2: document Doc 6 (fr_2026_16870.txt), proves component 1. 18.7% (local note: same paragraph, carryover limit)

```text
This underharvest exceeds the 440.6-mt dw underharvest carryover limit allowed; therefore, only 440.6 mt dw may be carried forward
```

Evidence 3: document Doc 6 (fr_2026_16870.txt), proves component 1. 18.7% (local note: supplementary information, weight basis)

```text
The conversion factor between dw and ww for swordfish is 1.33
```

Evidence 4: document Doc 3 (fr_2026_09059.txt), proves component 1. 18.7% (local note: North Atlantic swordfish section, TAC)

```text
Recommendation 24-10 previously set the TAC for 2025-2027 at 14,769 mt.
```

Evidence 5: document Doc 3 (fr_2026_09059.txt), proves component 1. 18.7% (local note: same passage, TAC weight basis)

```text
11 possible North Atlantic-wide total allowable catches (TACs) that range from 4,764 mt ww to 17,628 mt ww
```

Evidence 6: document Doc 3 (fr_2026_09059.txt), proves component 1. 18.7% (local note: same passage, U.S. allocation)

```text
resulting in a 3,907 mt allocation out of a 14,769 mt TAC
```

### Necessary documents

- Tick Doc 3 (fr_2026_09059.txt), role: Answer component
- Tick Doc 6 (fr_2026_16870.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_19459.txt), Doc 2 (fr_2025_24264.txt), Doc 4 (fr_2026_09973.txt), Doc 5 (fr_2026_10389.txt), Doc 7 (fr_2026_18031.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Rounding, scale or sign

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 6 gives the underharvest in dressed weight, Doc 3's TAC is whole weight; dividing without the 1.33 conversion gives 14.0%. Part vs total: Doc 6's 2,514.9 mt total underharvest includes the 440.6 mt carried forward; using the total gives 22.6%. The gold subtracts, then converts.
```

(49 / 50 words.)
