# aq-02626 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02626 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 eaf8ef1c02a2dcb090e0262fad5fd9e7bd0989b6669a73b765628265053c532a: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 3, D05 = Doc 5.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 5 doesn't mention 1,069,479. Doc 5 prints it first at character 54,400, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 5 doesn't mention 1,069,479. Doc 5 prints it first at character 54,400, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 4: Doc 3 doesn't mention 571,396.00. Doc 3 prints it first at character 44,480, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 6: Doc 3 doesn't mention 571,396.00. Doc 3 prints it first at character 44,480, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Per facility holding a State-issued coal-ash permit, how much more STAG funding had Alabama been awarded than Virginia had received, to the nearest dollar?
```

### Number of asks

1 ask

### Gold answer

```text
$62,260
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, Alabama CCR Units and Resources): "ADEM has been awarded a total of $1,069,479 from EPA's CCR State and Tribal Assistance Grants (STAG) funding." The same paragraph also prints a larger total that adds an amount EPA only "anticipates ADEM will be awarded"; that money is not yet awarded and is left out.
Step 2. Source input (Doc 5, Alabama's Permits Issued Under the State CCR Regulations): ADEM "issued permits for the following CCR facilities", a list numbered (1) to (8), from the James H. Miller Electric Generating Plant to the TVA Colbert Plant. Alabama therefore has 8 facilities holding State coal-ash permits; the units paragraph gives no facility count.
Step 3. Calculation (Doc 5): Alabama's awarded funding per permitted facility, in dollars: 1,069,479 / 8 = 133,684.875.
Step 4. Source input (Doc 3, Virginia CCR Units and Resources): VADEQ identified its disposal units "at 8 facilities in Virginia" and "has received $571,396.00 in funding to develop its CCR permit program", after applying for STAG funding.
Step 5. Source input (Doc 3, Virginia's Permits Issued Under the Commonwealth CCR Regulations): "VADEQ issued permits to the owners and/or operators of all CCR units in the Commonwealth", so all 8 Virginia facilities hold State permits.
Step 6. Calculation (Doc 3): Virginia's funding per permitted facility, in dollars: 571,396.00 / 8 = 71,424.5.
Step 7. Final answer (Doc 3 and Doc 5): Alabama's excess per permitted facility, in dollars: 133,684.875 - 71,424.5 = 62,260.375. To the nearest dollar the fraction drops, giving the gold answer.
```

### Answer components

Component 1

```text
$62,260
```

### Evidence

Evidence 1: document Doc 5 (fr_2026_14118.txt), proves component 1. $62,260 (local note: Alabama CCR Units and Resources, L276)

```text
ADEM has been awarded a total of $1,069,479 from EPA's CCR State and Tribal Assistance Grants (STAG) funding.
```

Evidence 2: document Doc 5 (fr_2026_14118.txt), proves component 1. $62,260 (local note: Alabama CCR Units and Resources, L276)

```text
EPA anticipates ADEM will be awarded an additional $203,390 in the upcoming round of funding, for a total of $1,272,869.
```

Evidence 3: document Doc 5 (fr_2026_14118.txt), proves component 1. $62,260 (local note: Alabama's Permits Issued Under the State CCR Regulations, L397)

```text
Subsequently, ADEM issued permits for the following CCR facilities: (1) The James H. Miller Electric Generating Plant (Permit #37-51, issued December 18, 2020); (2) Greene County Electric Generating Plant (Permit #32-03, issued December 18, 2020);
```

Evidence 4: document Doc 5 (fr_2026_14118.txt), proves component 1. $62,260 (local note: Alabama's Permits Issued Under the State CCR Regulations, L398)

```text
(7) Plant Gorgas (Permit #64-12, issued February 28, 2022); and (8) TVA Colbert Plant (Permit #17-11, issued October 25, 2022).
```

Evidence 5: document Doc 3 (fr_2026_08662.txt), proves component 1. $62,260 (local note: Virginia CCR Units and Resources, L226)

```text
VADEQ has identified 25 disposal units that are currently or have been used for disposal of CCR wastes (7 landfills and 18 surface impoundments) at 8 facilities in Virginia.
```

Evidence 6: document Doc 3 (fr_2026_08662.txt), proves component 1. $62,260 (local note: Virginia CCR Units and Resources, L226)

```text
In total, VADEQ has received $571,396.00 in funding to develop its CCR permit program.
```

Evidence 7: document Doc 3 (fr_2026_08662.txt), proves component 1. $62,260 (local note: Virginia's Permits Issued Under the Commonwealth CCR Regulations, L329)

```text
Subsequently, VADEQ issued permits to the owners and/or operators of all CCR units in the Commonwealth.
```

### Necessary documents

- Tick Doc 3 (fr_2026_08662.txt), role: Answer component
- Tick Doc 5 (fr_2026_14118.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt), Doc 2 (fr_2025_16801.txt), Doc 4 (fr_2026_11312.txt), Doc 6 (fr_2026_18552.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 5's resources paragraph prints $1,272,869 beside the $1,069,479 awarded; that larger total adds $203,390 EPA only anticipates. Taking it gives $159,109 per facility and $87,684 more than Virginia. The gold uses the awarded figure over Doc 5's eight permitted facilities: $62,260.
```

(44 / 50 words.)
