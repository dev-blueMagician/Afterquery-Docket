# aq-02626 q04 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02626 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 c18fded5e2b2310412fede8109d4cf7b9e358f3375a24c919523a55542a0221b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D04 = Doc 4.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many coal-ash surface impoundments are in States where EPA proposes approving the State's own version of the definition "contains both CCR and liquids"?
```

### Number of asks

1 ask

### Gold answer

```text
24 surface impoundments
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, Virginia Partial Program): for the terms the 2024 Legacy Rule changed for all units, "EPA is approving the State's version of the following requirements", and that list includes "Contains both CCR and liquids". Virginia qualifies.
Step 2. Source input (Doc 3, Virginia CCR Units and Resources): Virginia's disposal units include "18 surface impoundments".
Step 3. Source input (Doc 4, Louisiana Partial Program): "EPA is approving the State's version of these requirements", and that list also includes "Contains both CCR and liquids". Louisiana qualifies.
Step 4. Source input (Doc 4, Louisiana CCR Units and Resources): Louisiana's disposal units include "6 surface impoundments".
Step 5. Decoy check: Alabama's proposal (Doc 5) prints the same definition entry, but in its list of amendments that "are not being approved"; Wisconsin's approved list (Doc 6) carries the related definitions of infiltration and liquids but not this one; Wyoming (Doc 2) seeks approval of no Legacy Rule amendment. The impoundments in those three States are not counted.
Step 6. Final answer (Doc 3 and Doc 4): impoundments in the two qualifying States: 18 + 6 = 24.
```

### Answer components

Component 1

```text
24
```

### Evidence

Evidence 1: document Doc 3 (fr_2026_08662.txt), proves component 1. 24 (local note: Virginia Partial Program, L246)

```text
Therefore, EPA is approving the State's version of the following requirements:
```

Evidence 2: document Doc 3 (fr_2026_08662.txt), proves component 1. 24 (local note: Virginia Partial Program, L255)

```text
Contains both CCR and liquids
```

Evidence 3: document Doc 3 (fr_2026_08662.txt), proves component 1. 24 (local note: Virginia CCR Units and Resources, L226)

```text
VADEQ has identified 25 disposal units that are currently or have been used for disposal of CCR wastes (7 landfills and 18 surface impoundments) at 8 facilities in Virginia.
```

Evidence 4: document Doc 4 (fr_2026_11312.txt), proves component 1. 24 (local note: Louisiana Partial Program, L316)

```text
Therefore, EPA is approving the State's version of these requirements:
```

Evidence 5: document Doc 4 (fr_2026_11312.txt), proves component 1. 24 (local note: Louisiana Partial Program, L325)

```text
Contains both CCR and liquids
```

Evidence 6: document Doc 4 (fr_2026_11312.txt), proves component 1. 24 (local note: Louisiana CCR Units and Resources, L290)

```text
LDEQ has identified 9 disposal units that are currently or have been used for disposal of CCR wastes (3 landfills and 6 surface impoundments) at 4 facilities in Louisiana.
```

### Necessary documents

- Tick Doc 3 (fr_2026_08662.txt), role: Answer component
- Tick Doc 4 (fr_2026_11312.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 2 (fr_2025_16801.txt), Doc 5 (fr_2026_14118.txt), Doc 6 (fr_2026_18552.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 5 prints the same definition entry for Alabama, but in its list of amendments "not being approved"; a solver matching the phrase adds Alabama's 13 impoundments and answers 37. Only Virginia's and Louisiana's lists approve the State's version: 18 + 6 = 24.
```

(48 / 50 words.)
