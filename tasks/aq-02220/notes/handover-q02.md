# aq-02220 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02220 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status draft, revision 0, difficulty_target medium, origin claude.
- tested_sha256 9a2b416cec8ce40625eb5806aff73a1fedd2dd1aecd670ea5c496946dc6ed5ce: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 1.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- DRAFT: not locally checked. Use it for a quick test or a look at the form only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At the impact assessment's central assumptions, what would the methodology stages that central government leads in the private-sector-led model cost in total, undiscounted?
```

### Number of asks

1 ask

### Gold answer

```text
£9,500,000
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 1, delivery models for the zoning methodology, model C, Private sector-led): central government would commission and lead both aspects of the zone identification stage, the initial analysis (national mapping, stage 1a) and local refinement (stage 1b); the feasibility stage would then likely be led by the private sector. So the stages central government leads are national mapping and local refinement.

Step 2. Source fact (Doc 2, cost to government of designating zones and Table 6): in the central scenario the methodology is deployed in 200 towns and cities. Stage 1a national mapping costs 5,000 pounds per town or city, 85% of cities go forward to stage 1b, and stage 1b local refinement costs 50,000 pounds per city.

Step 3. Calculation (from Step 2; Doc 2 and Doc 1): national mapping for every town and city: 200 * 5,000 = 1,000,000 pounds.

Step 4. Calculation (from Step 2; Doc 2 and Doc 1): towns and cities going forward to local refinement: 200 * 85% = 170.

Step 5. Calculation (from Steps 2 and 4; Doc 2 and Doc 1): local refinement: 170 * 50,000 = 8,500,000 pounds.

Step 6. Calculation (from Steps 1, 3 and 5; Doc 1 and Doc 2): the two stages central government leads in the private-sector-led model: 1,000,000 + 8,500,000 = 9,500,000 pounds.
```

### Answer components

Component 1

```text
£9,500,000
```

### Evidence

Evidence 1: document Doc 1 (Proposals-for-heat-network-zoning-consultation-2021.txt), proves component 1. £9,500,000 (local note: L672, delivery model C)

```text
C: Private sector-led: Central government would commission and lead both aspects of the zone identification stage (initial analysis for identifying heat network zones and local refinement)
```

Evidence 2: document Doc 1 (Proposals-for-heat-network-zoning-consultation-2021.txt), proves component 1. £9,500,000 (local note: L673, delivery model C)

```text
The feasibility stage would then likely be led by the private sector
```

Evidence 3: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. £9,500,000 (local note: L1079, cost to government of zone designation)

```text
The methodology is assumed to be deployed in 200 towns and cities in the central scenario
```

Evidence 4: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. £9,500,000 (local note: L1083, Table 6)

```text
Table 6 – Central assumptions for the cost to government of designating zones
```

Evidence 5: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. £9,500,000 (local note: L1095-1102, Table 6 stage 1a)

```text
Stage 1a - National mapping Stage 1a/b Cost per town/ city £5,000
```

Evidence 6: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. £9,500,000 (local note: L1104-1107, Table 6)

```text
Proportion of cities going forward to Stage 1b 85%
```

Evidence 7: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. £9,500,000 (local note: L1109-1114, Table 6 stage 1b)

```text
Stage 1b - Local Refinement Cost per city £50,000
```

### Necessary documents

- Tick Doc 1 (Proposals-for-heat-network-zoning-consultation-2021.txt), role: Answer component
- Tick Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), role: Answer component

Leave unticked: Doc 3 (Proposals-for-heat-network-zoning-government-response.txt), Doc 4 (Heat-network-zoning-consultation-2023-summary-of-government.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong kind of entity

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 1's private-sector-led model gives central government local refinement as well as national mapping; giving refinement to councils, as in the local-authority-led model, leaves £1,000,000. Doc 2's Table 6 sends only 85% of 200 towns to refinement; costing all 200 gives £11,000,000. Gold: £9,500,000.
```

(44 / 50 words.)
