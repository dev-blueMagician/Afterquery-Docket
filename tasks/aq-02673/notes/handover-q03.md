# aq-02673 q03 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02673 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 e59485675f86e79f68a485545147b3c297113d1ffe49e9dfeffece3aa6de3f5f: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D06 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q02: '26 percent of the lowest total'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At 26 percent of the lowest total allowable catch under ICCAT's North Atlantic swordfish management procedure, what percentage of 2025 U.S. landings would the maximum adjusted U.S. quota be, to the nearest percent?
```

### Number of asks

1 ask

### Gold answer

```text
168%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, North Atlantic swordfish section): the management procedure provides for 11 possible North Atlantic-wide TACs, ranging from 4,764 mt ww to 17,628 mt ww. The lowest is 4,764 mt ww.

Step 2. Source input (Doc 3, same passage): the United States is allocated approximately 26 percent of the TAC, and the document applies that share as a multiplier of 0.26 to a whole-weight TAC; for its highest case it multiplies 17,628 mt ww by 0.26 to give 4,583.3 mt ww.

Step 3. Calculation (Doc 3): U.S. baseline quota at the lowest TAC: 4,764 × 0.26 = 1,238.64 mt ww.

Step 4. Source input (Doc 3 and Doc 6, North Atlantic swordfish sections): underharvest may be carried forward up to 15 percent of the baseline quota, and the maximum adjusted quota is the baseline plus that carryover. Doc 3 works its highest case as 3,446.1 mt dw plus 0.15 times 3,446.1 mt dw to give 3,963.0 mt dw.

Step 5. Calculation (Doc 3 and Doc 6): largest carryover at the lowest TAC: 1,238.64 × 0.15 = 185.796 mt ww.

Step 6. Calculation (Doc 3 and Doc 6): maximum adjusted quota at the lowest TAC: 1,238.64 + 185.796 = 1,424.436 mt ww.

Step 7. Source input (Doc 6, North Atlantic swordfish section): in 2025, U.S. landings of North Atlantic swordfish were 637.7 mt dw. Doc 6 reports no South Atlantic swordfish landings in 2025.

Step 8. Source input (Doc 6 and Doc 3, supplementary information): swordfish weight converts from dressed to whole weight with the factor 1.33.

Step 9. Calculation (Doc 6 and Doc 3): 2025 landings in whole weight: 637.7 × 1.33 = 848.141 mt ww.

Step 10. Calculation (Doc 3 and Doc 6): the maximum adjusted quota as a percentage of those landings: 1,424.436 / 848.141 = 168%.
```

### Answer components

Component 1

```text
168%
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_09059.txt), proves component 1. 168% (local note: North Atlantic swordfish section, range of TACs)

```text
11 possible North Atlantic-wide total allowable catches (TACs) that range from 4,764 mt ww to 17,628 mt ww
```

Evidence 2: document Doc 3 (fr_2026_09059.txt), proves component 1. 168% (local note: same passage, U.S. share)

```text
the United States continues to be allocated approximately 26 percent of the TAC
```

Evidence 3: document Doc 3 (fr_2026_09059.txt), proves component 1. 168% (local note: same passage, share applied to a whole-weight TAC)

```text
17,628 mt ww * 0.26 = 4,583.3 mt ww
```

Evidence 4: document Doc 3 (fr_2026_09059.txt), proves component 1. 168% (local note: same passage, carryover limit)

```text
15 percent of the baseline quota from one year to the next
```

Evidence 5: document Doc 3 (fr_2026_09059.txt), proves component 1. 168% (local note: same passage, maximum adjusted quota worked for the highest TAC)

```text
quota would be 3,963.0 mt dw (5,270.8 mt ww) (3,446.1 mt dw + (0.15 * 3,446.1) mt dw)
```

Evidence 6: document Doc 3 (fr_2026_09059.txt), proves component 1. 168% (local note: supplementary information, weight basis)

```text
The conversion factor between dw and ww for swordfish is 1.33
```

Evidence 7: document Doc 6 (fr_2026_16870.txt), proves component 1. 168% (local note: North Atlantic swordfish section, 2025 landings)

```text
In 2025, U.S. landings of North Atlantic swordfish, which include landings and dead discards, were 637.7 mt dw (2,514.9 mt dw less than the 2025 adjusted quota).
```

Evidence 8: document Doc 6 (fr_2026_16870.txt), proves component 1. 168% (local note: same paragraph, carryover limit)

```text
the maximum North Atlantic swordfish underharvest that may be carried forward from one year to the next is 15 percent of the baseline quota
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

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 3's quota at the lowest TAC is whole weight (1,424.436 mt ww with carryover), Doc 6's landings are 637.7 mt dw; dividing unconverted gives 223%. Look-alike measure: taking the baseline quota (1,238.64 mt ww) for the maximum adjusted quota drops the 15 percent carryover: 146%.
```

(49 / 50 words.)
