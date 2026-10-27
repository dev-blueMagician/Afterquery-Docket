# aq-02673 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02673 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 236aeb3ba8a5dbac30c9f2dfbd95f61907ae4d450e144f74a3f1505610084650: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D06 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At 26 percent of the lowest total allowable catch under ICCAT's North Atlantic swordfish management procedure, what percentage of 2025 U.S. landings would the U.S. quota be, to the nearest percent?
```

### Number of asks

1 ask

### Gold answer

```text
146%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, North Atlantic swordfish section): the management procedure provides for 11 possible North Atlantic-wide TACs, ranging from 4,764 mt ww to 17,628 mt ww. The lowest is 4,764 mt ww.

Step 2. Source input (Doc 3, same passage): the United States is allocated approximately 26 percent of the TAC, and the document applies that share as a multiplier of 0.26 to a whole-weight TAC; for its highest case it multiplies 17,628 mt ww by 0.26 to give 4,583.3 mt ww.

Step 3. Calculation (Doc 3): U.S. quota at the lowest TAC: 4,764 × 0.26 = 1,238.64 mt ww.

Step 4. Source input (Doc 6, North Atlantic swordfish section): in 2025, U.S. landings of North Atlantic swordfish were 637.7 mt dw. Doc 6 reports no South Atlantic swordfish landings in 2025.

Step 5. Source input (Doc 6 and Doc 3, supplementary information): swordfish weight converts from dressed to whole weight with the factor 1.33.

Step 6. Calculation (Doc 6 and Doc 3): 2025 landings in whole weight: 637.7 × 1.33 = 848.141 mt ww.

Step 7. Calculation (Doc 3 and Doc 6): the quota as a percentage of those landings: 1,238.64 / 848.141 = 146%.
```

### Answer components

Component 1

```text
146%
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_09059.txt), proves component 1. 146% (local note: North Atlantic swordfish section, range of TACs)

```text
11 possible North Atlantic-wide total allowable catches (TACs) that range from 4,764 mt ww to 17,628 mt ww
```

Evidence 2: document Doc 3 (fr_2026_09059.txt), proves component 1. 146% (local note: same passage, U.S. share)

```text
the United States continues to be allocated approximately 26 percent of the TAC
```

Evidence 3: document Doc 3 (fr_2026_09059.txt), proves component 1. 146% (local note: same passage, share applied to a whole-weight TAC)

```text
17,628 mt ww * 0.26 = 4,583.3 mt ww
```

Evidence 4: document Doc 3 (fr_2026_09059.txt), proves component 1. 146% (local note: supplementary information, weight basis)

```text
The conversion factor between dw and ww for swordfish is 1.33
```

Evidence 5: document Doc 6 (fr_2026_16870.txt), proves component 1. 146% (local note: North Atlantic swordfish section, 2025 landings)

```text
In 2025, U.S. landings of North Atlantic swordfish, which include landings and dead discards, were 637.7 mt dw (2,514.9 mt dw less than the 2025 adjusted quota).
```

Evidence 6: document Doc 6 (fr_2026_16870.txt), proves component 1. 146% (local note: South Atlantic swordfish section)

```text
In 2025, there were no landings of South Atlantic swordfish by U.S. fishermen
```

### Necessary documents

- Tick Doc 3 (fr_2026_09059.txt), role: Answer component
- Tick Doc 6 (fr_2026_16870.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_19459.txt), Doc 2 (fr_2025_24264.txt), Doc 4 (fr_2026_09973.txt), Doc 5 (fr_2026_10389.txt), Doc 7 (fr_2026_18031.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 3 states TACs in whole weight, so 26 percent of 4,764 mt ww is 1,238.64 mt ww, while Doc 6 gives 2025 landings as 637.7 mt dw. Dividing them unconverted gives 194%. The gold first converts the landings by 1.33 to 848.141 mt ww.
```

(48 / 50 words.)
