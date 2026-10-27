# aq-02220 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02220 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 89e95f8b06ac883340b59c53c084c832df7634d2967e621823fb802dcfee2d14: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 4, D02 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Using the impact assessment's heat-network efficiencies, what percentage of the zone emissions benchmark's electricity and gas input is gas, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
40.0%
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 4, Emissions in Heat Network Zones): from 2030 zone heat networks must meet a carbon emissions limit based on a benchmark scenario in which 85% of heat is delivered by low-carbon air source heat pumps using electricity and 15% is supplied by gas boilers.

Step 2. Source fact (Doc 2, Annex 1 Tables 21 and 24): Table 21 lists the heat-network generation technologies, including the Back-up Gas Boiler. Table 24 prints thermal efficiencies in the same order as its technology list, so the Air Source Heat Pump has 321% and the Back-up Gas Boiler, which follows Gas CHP, has 85%.

Step 3. Calculation (from Steps 1 and 2; Doc 4 and Doc 2): each source's energy input is its share of the heat divided by its efficiency. Multiplying both inputs by the two efficiencies keeps their proportions, so the gas term becomes the gas share of heat times the heat pump efficiency: 15% * 321% = 0.4815.

Step 4. Calculation (from Steps 1 and 2; Doc 4 and Doc 2): the electricity term becomes the heat pump share of heat times the boiler efficiency: 85% * 85% = 0.7225.

Step 5. Calculation (from Steps 3 and 4; Doc 4 and Doc 2): both terms together: 0.4815 + 0.7225 = 1.204.

Step 6. Calculation (from Steps 3 and 5; Doc 4 and Doc 2): gas share of the electricity and gas input: 0.4815 / 1.204 = 40.0% (to one decimal place).
```

### Answer components

Component 1

```text
40.0%
```

### Evidence

Evidence 1: document Doc 4 (Heat-network-zoning-consultation-2023-summary-of-government.txt), proves component 1. 40.0% (local note: L116, Emissions in Heat Network Zones)

```text
This will be based on a benchmark scenario assuming 85% of heat is delivered by low-carbon air source heat pumps using electricity and 15% is supplied by gas boilers
```

Evidence 2: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. 40.0% (local note: L2074, Annex 1)

```text
Table 21 – Capital and operating cost per generation technology (heat networks)
```

Evidence 3: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. 40.0% (local note: L2230, Annex 1)

```text
Table 24 - Thermal Efficiency (factual and counterfactual)
```

Evidence 4: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. 40.0% (local note: L2236, Table 24 technology list)

```text
Air Source Heat Pump Ground Source Heat Pump Water Source Heat Pump (WSHP)
```

Evidence 5: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. 40.0% (local note: L2237, Table 24 technology list)

```text
Back-up Gas Boiler Commercial Gas Boiler Domestic Gas Boiler Electric Heater
```

Evidence 6: document Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), proves component 1. 40.0% (local note: L2243-2254, Table 24 values)

```text
Thermal Efficiency (%) 321 284 330 541 690 500 N/A 40 85
```

### Necessary documents

- Tick Doc 4 (Heat-network-zoning-consultation-2023-summary-of-government.txt), role: Answer component
- Tick Doc 2 (Heat-network-zoning-consultation-stage-impact-assessment.txt), role: Answer component

Leave unticked: Doc 1 (Proposals-for-heat-network-zoning-consultation-2021.txt), Doc 3 (Proposals-for-heat-network-zoning-government-response.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Figure that must be computed

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Doc 4's benchmark splits heat: its 15% gas share is not an input share (15.0%). Doc 2's Table 24 efficiencies, air source heat pump 321% and back-up gas boiler 85%, give inputs of 26.480% and 17.647% of heat; rounding those to 26.5 and 17.6 first gives 39.9%. Gold 40.0%.
```

(49 / 50 words.)
