# aq-02220 q03 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02220 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 a2a2ee666a51f665773b6e66cfc9cd091815dbbef9208eada757266d4166c20e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 4, D02 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many TWh of England's projected 2050 heat demand would heat networks supply at their most recently stated 2050 share, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
87.8 TWh
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 4, Introduction): Doc 4 is the latest document, the government's response to the zoning consultation held between 18 December 2023 and 26 February 2024. It says the Warm Homes Plan targets heat networks meeting 7% (27TWh) of England's heat demand by 2035, with heat networks expected to provide a fifth of all heat by 2050. This is the most recently stated 2050 share; the earlier documents cite only the older Climate Change Committee estimate of what heat networks could provide across the UK.

Step 2. Source fact (Doc 2, Results of the deployment analysis): the impact assessment gives the total heat demand for England, taken from the Opportunity Areas for District Heating Networks study, as 439 TWh in 2050. No other document projects England's heat demand for 2050.

Step 3. Calculation (from Steps 1 and 2; Doc 4 and Doc 2): a fifth of England's projected 2050 heat demand: 439 / 5 = 87.8 TWh.
```

### Answer components

Component 1

```text
87.8 TWh
```

### Evidence

Evidence 1: document Doc 4 (Heat-network-zoning-consultation-2023-summary-of-government.txt), proves component 1. 87.8 TWh (local note: L18, Introduction)

```text
In the Warm Homes Plan we are setting a target to more than double the amount of heat demand met via heat networks in England to 7% (27TWh) by 2035 with them expected to provide a fifth of all heat by 2050
```

Evidence 2: document Doc 4 (Heat-network-zoning-consultation-2023-summary-of-government.txt), proves component 1. 87.8 TWh (local note: L22, Introduction)

```text
A public consultation was held between 18 December 2023 and 26 February 2024 on further proposals for heat network zoning
```

Evidence 3: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. 87.8 TWh (local note: L1495, paragraph 89)

```text
The total heat demand for England, presented in Opportunity Areas for District Heating Networks in the UK3, is estimated to be 439 TWh in 2050
```

### Necessary documents

- Tick Doc 4 (Heat-network-zoning-consultation-2023-summary-of-government.txt), role: Answer component
- Tick Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), role: Answer component

Leave unticked: Doc 1 (Proposals-for-heat-network-zoning-consultation-2021.txt), Doc 3 (Proposals-for-heat-network-zoning-government-response.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Doc 4, the latest, expects heat networks to provide a fifth of all heat by 2050: a fifth of Doc 2's 439 TWh is 87.8. The Climate Change Committee's older 18% UK estimate (Docs 1-3) gives 79.0; Doc 2's 31.2 TWh is only zoning's additional part, not the total.
```

(49 / 50 words.)
