# aq-02626 q06 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02626 --handover --q q06` from questions/q06.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 8b7ea010d8a2f6709efac5f5270e7c0de6ef761b18e6e7eee969ff326656b3ee: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3, D06 = Doc 6.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 3 doesn't mention 7. Doc 3 prints it first at character 34,796, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 6: Doc 6 doesn't mention 6. Doc 6 prints it first at character 21,982, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q06.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many coal-ash landfills are in States whose CCR-program permits carry no set expiry?
```

### Number of asks

1 ask

### Gold answer

```text
16 landfills
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, Permit Requirements and Permitting Process): in Virginia "The permit is issued for the life of the facility (through termination of postclosure care)", so it has no set expiry. Virginia qualifies.
Step 2. Source input (Doc 3, Virginia CCR Units and Resources): Virginia's disposal units include "7 landfills".
Step 3. Source input (Doc 2, Permit Requirements and Permitting Process): in Wyoming the duration of "CCR landfills renewal permits will be for the operating life of the facility through post-closure", so the permit under the State's coal ash rules has no set expiry. Wyoming qualifies.
Step 4. Source input (Doc 2, Wyoming CCR Units and Resources): Wyoming's disposal units include "3 landfills".
Step 5. Source input (Doc 6, Guidelines for Permitting): in Wisconsin "There is no expiration for an operating license or plan of operation approval". The same passage has the plan of operation "updated every 10 years", which is a plan update, not a permit term. Wisconsin qualifies.
Step 6. Source input (Doc 6, Wisconsin CCR Units and Resources): Wisconsin's units include "6 landfills".
Step 7. Decoy check: Alabama's permit (Doc 5) is tied to the facility's design life but capped at a fixed number of years, and Louisiana's (Doc 4) is issued for a fixed maximum term although the facility must hold a permit for its active life. Both carry a set expiry, so their landfills are not counted.
Step 8. Calculation (Doc 2 and Doc 3): landfills in Virginia and Wyoming: 7 + 3 = 10.
Step 9. Final answer (Doc 2, Doc 3 and Doc 6): adding Wisconsin's landfills: 10 + 6 = 16.
```

### Answer components

Component 1

```text
16
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_08662.txt), proves component 1. 16 (local note: Permit Requirements and Permitting Process, L190)

```text
The permit is issued for the life of the facility (through termination of postclosure care)
```

Evidence 2: document Doc 3 (fr_2026_08662.txt), proves component 1. 16 (local note: Virginia CCR Units and Resources, L226)

```text
VADEQ has identified 25 disposal units that are currently or have been used for disposal of CCR wastes (7 landfills and 18 surface impoundments) at 8 facilities in Virginia.
```

Evidence 3: document Doc 2 (fr_2025_16801.txt), proves component 1. 16 (local note: Permit Requirements and Permitting Process, L204)

```text
The permit duration for new or existing CCR surface impoundments and CCR landfills renewal permits will be for the operating life of the facility through post-closure
```

Evidence 4: document Doc 2 (fr_2025_16801.txt), proves component 1. 16 (local note: Wyoming CCR Units and Resources, L267)

```text
WDEQ has identified 19 disposal units that are currently or have been used for disposal of CCR wastes (3 landfills and 16 surface impoundments) at 4 facilities in Wyoming.
```

Evidence 5: document Doc 6 (fr_2026_18552.txt), proves component 1. 16 (local note: Guidelines for Permitting, L192)

```text
There is no expiration for an operating license or plan of operation approval
```

Evidence 6: document Doc 6 (fr_2026_18552.txt), proves component 1. 16 (local note: Wisconsin CCR Units and Resources, L290)

```text
WDNR has identified 9 CCR units (6 landfills and 3 surface impoundments) at 6 facilities in Wisconsin.
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 3 (fr_2026_08662.txt), role: Answer component
- Tick Doc 6 (fr_2026_18552.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 4 (fr_2026_11312.txt), Doc 5 (fr_2026_14118.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 6 prints a ten-year figure for Wisconsin, but it is the interval for updating a landfill's plan of operation; the licence has "no expiration". Reading it as a permit term drops Wisconsin's 6 landfills and gives 10. The gold counts Virginia 7, Wyoming 3, Wisconsin 6: 16.
```

(50 / 50 words.)
