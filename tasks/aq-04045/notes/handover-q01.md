# aq-04045 q01 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-04045 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 871bb7e96968a4910454fc49461b274d9e538c6bda4536f4102c4b4946205aa1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 6 doesn't mention 964,200. Doc 6 prints it first at character 46,797, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 6 doesn't mention 441,925. Doc 6 prints it first at character 46,967, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What percentage of all space station regulatory fees the FCC assessed for fiscal year 2024 fell on its NGSO-Other category, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
31.5%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, its paragraph on how few units pay space station fees): for FY 2024 there were 11 units of other NGSO space stations, 6 units of less complex NGSO space stations and 16 units of small satellite fee payors.

Step 2. Source input (Doc 6, its paragraph on the current NGSO fee split): for fiscal year 2024 each NGSO-Other payor was assessed $964,200 and each NGSO-Less Complex payor $441,925. The same paragraph says that 80% and 20% of the NGSO share go to these categories after a pro rata amount of the small satellite fees is subtracted from each, so the small satellite fees are paid out of the NGSO share.

Step 3. Source input (Doc 6, its background paragraph on the June 2024 order): the small satellite fee for FY 2024 was $12,215 per license.

Step 4. Calculation (Doc 5 and Doc 6): NGSO-Other fees, in dollars: 11 × 964,200 = 10,606,200

Step 5. Calculation (Doc 5 and Doc 6): NGSO-Less Complex fees, in dollars: 6 × 441,925 = 2,651,550

Step 6. Calculation (Doc 5 and Doc 6): small satellite fees, in dollars: 16 × 12,215 = 195,440

Step 7. Calculation (Doc 5 and Doc 6): the NGSO share is the sum of these fees, in dollars: 10,606,200 + 2,651,550 + 195,440 = 13,453,190

Step 8. Source input (Doc 5, its background paragraph on September 2024 and its later remark on FY 2024): for FY 2024 the Commission allocated 60% of space station regulatory fees to GSO payors and 40% to NGSO payors. No document prints the GSO fee, so the total has to be worked out from the NGSO share.

Step 9. Calculation (Doc 5 and Doc 6): the NGSO share is 40% of all space station regulatory fees, so the total in dollars is 13,453,190 / 40% = 33,632,975

Step 10. Final answer (Doc 5 and Doc 6): NGSO-Other fees as a percentage of that total: 10,606,200 / 33,632,975 = 31.5%
```

### Answer components

Component 1

```text
31.5%
```

### Evidence

Evidence 1: document Doc 5 (fr_2025_03993.txt), proves component 1. 31.5% (local note: III.B.1, para 28)

```text
for FY 2024 there were 16 units of small satellite fee payors, 140 units of GSO space stations, 6 units of
```

Evidence 2: document Doc 5 (fr_2025_03993.txt), proves component 1. 31.5% (local note: III.B.1, para 28)

```text
and 11 units of other NGSO space stations
```

Evidence 3: document Doc 5 (fr_2025_03993.txt), proves component 1. 31.5% (local note: II, para 9)

```text
to 60% of space station regulatory fees being allocated to GSO space station payors and 40% to NGSO space station payors
```

Evidence 4: document Doc 5 (fr_2025_03993.txt), proves component 1. 31.5% (local note: III.B.2, para 34)

```text
that we determined was the case for FY 2024 (that is, 60 percent of space station FTE resources allocated to GSO space station fee payors and 40 percent allocated to NGSO space station fee payors)
```

Evidence 5: document Doc 6 (fr_2025_12579.txt), proves component 1. 31.5% (local note: III.D, para 40)

```text
80% of the share of NGSO space station fees are allocated to the NGSO--Other fee category and 20% to the NGSO--Less Complex fee category, after subtracting a pro rata amount of the total fees assessed for NGSO--Small Satellites from each category
```

Evidence 6: document Doc 6 (fr_2025_12579.txt), proves component 1. 31.5% (local note: III.D, para 40)

```text
For fiscal year 2024, fee payors in the NGSO--Other fee category were assessed fees of $964,200 per unit
```

Evidence 7: document Doc 6 (fr_2025_12579.txt), proves component 1. 31.5% (local note: III.D, para 40)

```text
Payors in the NGSO--Less Complex fee category were assessed per unit fees of $441,925
```

Evidence 8: document Doc 6 (fr_2025_12579.txt), proves component 1. 31.5% (local note: II, para 7)

```text
for FY 2024 at the level set for FY 2023 ($12,215)
```

### Necessary documents

- Tick Doc 5 (fr_2025_03993.txt), role: Answer component
- Tick Doc 6 (fr_2025_12579.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_03506.txt), Doc 2 (fr_2024_16348.txt), Doc 3 (fr_2024_17093.txt), Doc 4 (fr_2024_23975.txt), Doc 7 (fr_2025_16375.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 6's fee paragraph prices only NGSO-Other and Less Complex, but the NGSO share (40% of the total, Doc 5) also holds small satellite fees. Taking those two categories as the whole share gives 32.0%, like 40% x 80%. Counting small satellite fees gives 31.5%.
```

(48 / 50 words.)
