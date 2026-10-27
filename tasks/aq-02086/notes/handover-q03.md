# aq-02086 q03 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02086 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 28a06f796dbfd45077f778c3022338b886ed65ea53ce2dac8b2755f3e5e29674: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 2, D04 = Doc 3.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Responses from registered providers to the Awaab's Law consultation equalled what percentage of all registered providers in operation, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
15.4%
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 3, breakdown of consultation responses by type of respondent): 113 responses came from local authority registered providers and 140 from private registered providers of social housing. The table lists other local authorities and other social landlords as not registered providers, and arms-length and tenant management organisations as separate types.

Step 2. Source fact (Doc 3, scope of the document): social landlords are registered providers of social housing, which can be local authority landlords or private registered providers.

Step 3. Source fact (Doc 2, familiarisation costs): there are 234 large and 1,162 small private registered providers in the sector, and 163 large and 86 small local authority registered providers in operation.

Step 4. Calculation (Doc 3), responses from registered providers: 113 + 140 = 253 responses.

Step 5. Calculation (Doc 2), private registered providers: 234 + 1,162 = 1,396 providers.

Step 6. Calculation (Doc 2), local authority registered providers: 163 + 86 = 249 providers.

Step 7. Calculation (Doc 2), all registered providers: 1,396 + 249 = 1,645 providers.

Step 8. Calculation (Doc 2 and Doc 3), responses as a share of providers: 253 / 1,645 = 15.4% (to one decimal place).
```

### Answer components

Component 1

```text
15.4%
```

### Evidence

Evidence 1: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. 15.4% (local note: L101, respondent table)

```text
Local authority registered provider|113|11%
```

Evidence 2: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. 15.4% (local note: L103, respondent table)

```text
Private registered provider of social housing|140|14%
```

Evidence 3: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. 15.4% (local note: L130, scope)

```text
refers to registered providers of social housing. This could include a local authority landlord or private registered provider of social housing
```

Evidence 4: document Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), proves component 1. 15.4% (local note: L454, familiarisation costs)

```text
At present there are 234 large PRPs (with a stock volume of greater than 1,000 social dwellings) and 1,162 small PRPs (1,000 social dwellings or fewer) in the sector.
```

Evidence 5: document Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), proves component 1. 15.4% (local note: L454, familiarisation costs)

```text
Using the same thresholds, there are 163 large local authority registered providers (LARPs) and 86 small LARPs in operation across the sector.
```

### Necessary documents

- Tick Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), role: Answer component
- Tick Doc 3 (Awaabs-Law-government-response.txt), role: Answer component

Leave unticked: Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), Doc 5 (Response-to-the-consultation-on-a-Decent-Homes-Standard-in.txt)

### Reasoning tags

Tick: Cross-document join, Entity resolution, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Wrong kind of entity

How a careless solver fails: Wrong members in a list

#### Failure mode 3

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Doc 2 splits providers into large and small; counting only large gives 63.7%. Doc 3 lists ALMOs, TMOs and other social landlords beside registered providers; adding them gives 16.7%. Doc 3's 11% and 14% are shares of responses (25%). Gold: 253 / 1,645 = 15.4%.
```

(45 / 50 words.)
