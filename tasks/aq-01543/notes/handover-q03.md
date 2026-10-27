# aq-01543 q03 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01543 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status draft, revision 4, difficulty_target medium, origin claude.
- tested_sha256 808fc8ec44ccd9b9efd92e4f207a0dab5f798e4b35b44a10ed3527ff195b65e7: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D12 = Doc 16, D15 = Doc 4.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- DRAFT: not locally checked. Use it for a quick test or a look at the form only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Taken together, what percentage of the electricity generated in South Korea and in mainland Portugal from January through November 2025 came from renewable sources? Give the percentage to two decimal places.
```

### Number of asks

1 ask

### Gold answer

```text
15.46%
```

### Step-by-step reasoning

```text
Step 1. Doc 4: on a provisional basis for January to November 2025, South Korea's "total generation estimated at 543.6TWh", of which "Renewable generation remained at 57.6TWh".

Step 2. Doc 4: South Korea's total generation in GWh: 543.6 TWh = 543,600 GWh.

Step 3. Doc 4: South Korea's renewable generation in GWh: 57.6 TWh = 57,600 GWh.

Step 4. Doc 16: between January 1 and November 30, 2025, mainland Portugal generated "a total of 44 303 GWh", where a space separates the thousands, so its 44 is in thousands of GWh: 44 TWh = 44,000 GWh.

Step 5. Doc 16: mainland Portugal's total generation: 44,000 + 303 = 44,303 GWh.

Step 6. Doc 16: "75.1 % coming from renewable sources": 75.1% * 44,303 = 33,271.553 GWh.

Step 7. Doc 4 and Doc 16: combined generation: 543,600 + 44,303 = 587,903 GWh.

Step 8. Doc 4 and Doc 16: combined renewable generation: 57,600 + 33,271.553 = 90,871.553 GWh.

Step 9. Doc 4 and Doc 16: 90,871.553 / 587,903 = 15.46%.
```

### Answer components

Component 1

```text
15.46%
```

### Evidence

Evidence 1: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 15.46% (local note: Energy overview, L10)

```text
On a provisional January-November 2025 basis, Korea
```

Evidence 2: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 15.46% (local note: Energy overview, L10)

```text
with total generation estimated at 543.6TWh
```

Evidence 3: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 15.46% (local note: Energy overview, L10)

```text
Renewable generation remained at 57.6TWh, or 10.6%
```

Evidence 4: document Doc 16 (ccg_energy_cleantech_sectors_portugal.txt), proves component 1. 15.46% (local note: Renewable Energy, L17)

```text
between January 1 and November 30, 2025, a total of 44 303 GWh of electricity were generated in Mainland Portugal, with 75.1 % coming from renewable sources
```

### Necessary documents

- Tick Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), role: Answer component
- Tick Doc 16 (ccg_energy_cleantech_sectors_portugal.txt), role: Answer component

Leave unticked: Doc 1 (ccg_energy_cleantech_sectors_bulgaria.txt), Doc 2 (ccg_energy_cleantech_sectors_poland.txt), Doc 3 (ccg_energy_cleantech_sectors_vietnam.txt), Doc 5 (ccg_energy_cleantech_sectors_israel.txt), Doc 6 (ccg_energy_cleantech_sectors_chile.txt), Doc 7 (ccg_energy_cleantech_sectors_angola.txt), Doc 8 (ccg_energy_cleantech_sectors_mauritius.txt), Doc 9 (ccg_energy_cleantech_sectors_germany.txt), Doc 10 (ccg_energy_cleantech_sectors_china.txt), Doc 11 (ccg_energy_cleantech_sectors_united_arab_emirates.txt), Doc 12 (ccg_energy_cleantech_sectors_south_africa.txt), Doc 13 (ccg_energy_cleantech_sectors_mexico.txt), Doc 14 (ccg_energy_cleantech_sectors_united_kingdom.txt), Doc 15 (ccg_energy_cleantech_sectors_uruguay.txt), Doc 17 (ccg_energy_cleantech_sectors_spain.txt), Doc 18 (ccg_energy_cleantech_sectors_finland.txt), Doc 19 (ccg_energy_cleantech_sectors_indonesia.txt), Doc 20 (ccg_energy_cleantech_sectors_romania.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization, Aggregation

Leave unticked: Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 4 prints South Korea's January-November 2025 renewable share (10.6%) and Doc 16 mainland Portugal's (75.1%); averaging them gives 42.85%. Pooling needs generation weights: (57,600 + 33,271.553) / (543,600 + 44,303) GWh = 15.46%.
```

(34 / 50 words.)
