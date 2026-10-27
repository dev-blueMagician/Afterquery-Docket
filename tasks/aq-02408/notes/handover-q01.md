# aq-02408 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02408 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 2e56252faf9b7786a217ca08d35315cfddc14a5b607a87fa8a140657e51b7c8f: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D05 = Doc 5.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D04: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
To the nearest 10 MW, how much Calpine-owned capacity must be divested under DOJ's Constellation-Calpine settlement in relevant markets holding a coal plant covered by EPA's coal-ash deadline proposal?
```

### Number of asks

1 ask

### Gold answer

```text
660 MW
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 5, complaint paragraphs 31 and 33): the relevant geographic markets for Constellation's purchase of Calpine are the region covered by ERCOT and the PJM Coastal Mid-Atlantic area, which includes southeastern Pennsylvania, New Jersey, Delaware, and the eastern shores of Maryland and Virginia.

Step 2. Source fact (Doc 4, section III.B, the ERCOT entry): Coleto Creek, one of the plants EPA's proposed deadline extension covers, falls in the ERCOT market and has a 650 MW coal-fired steam generating unit.

Step 3. Source fact (Doc 4, sections II.A and III.B): the covered plants are in Illinois, Louisiana, Texas, Utah, Ohio, Wyoming and Indiana, and the only ones in PJM are Kincaid, located in Illinois, and Miami Fort, located in Ohio, so no covered plant lies in the PJM Coastal Mid-Atlantic area.

Step 4. Determination (from Steps 1 to 3; Doc 4 and Doc 5): of the two relevant markets, only ERCOT contains a coal plant covered by EPA's proposal, so only the ERCOT divestitures count and the PJM divestitures drop out.

Step 5. Source fact (Doc 5, Competitive Impact Statement, divestiture assets): the ERCOT divestitures are Calpine's Jack A. Fusco plant, a 557 MW combined-cycle natural gas facility, and Calpine's interest in Gregory, a 365 MW combined-cycle natural gas facility of which Calpine owns approximately 28.5%.

Step 6. Calculation (from Step 5; Doc 5 and Doc 4): Calpine-owned capacity at Gregory: 365 * 28.5% = 104.025 MW.

Step 7. Calculation (from Steps 5 and 6; Doc 5 and Doc 4): Calpine-owned capacity divested in ERCOT: 557 + 104.025 = 661.025 MW.

Step 8. Answer (from Step 7; Doc 5 and Doc 4): rounded to the nearest 10 MW, as the question asks, 661.025 MW is six hundred sixty megawatts.
```

### Answer components

Component 1

```text
660 MW
```

### Evidence

Evidence 1: document Doc 5 (fr_2025_23298.txt), proves component 1. 660 MW (local note: complaint para. 31)

```text
The region covered by ERCOT is a relevant geographic market for evaluating the potential competitive impact of Constellation's purchase of Calpine
```

Evidence 2: document Doc 5 (fr_2025_23298.txt), proves component 1. 660 MW (local note: complaint para. 33)

```text
The PJM Coastal Mid-Atlantic geographic area is a distinct area within the PJM region that includes southeastern Pennsylvania, New Jersey, Delaware, and the eastern shores of Maryland and Virginia.
```

Evidence 3: document Doc 4 (fr_2025_21597.txt), proves component 1. 660 MW (local note: section III.B, ERCOT)

```text
3. Electric Reliability Council of Texas (ERCOT) Coleto Creek Power Plant (Coleto Creek) located in Texas.
```

Evidence 4: document Doc 4 (fr_2025_21597.txt), proves component 1. 660 MW (local note: section III.B, Coleto Creek)

```text
associated with the 650 MW coal-fired steam generating unit
```

Evidence 5: document Doc 4 (fr_2025_21597.txt), proves component 1. 660 MW (local note: section II.A, covered plants)

```text
Baldwin Power Station (IL), Big Cajun II Power Plant (LA), Brame Energy Center (LA), Coleto Creek Power Plant (TX), Intermountain Generating Facility (UT), Kincaid Power Station (IL), Miami Fort Power Station (OH), Naughton Power Plant (WY), Newton Power Station (IL), R.M.
```

Evidence 6: document Doc 4 (fr_2025_21597.txt), proves component 1. 660 MW (local note: section II.A, covered plants)

```text
Schahfer Generating Station (IN), and Welsh Power Plant (TX).
```

Evidence 7: document Doc 4 (fr_2025_21597.txt), proves component 1. 660 MW (local note: section III.B, PJM)

```text
Kincaid Power Station (Kincaid) located in Illinois.
```

Evidence 8: document Doc 4 (fr_2025_21597.txt), proves component 1. 660 MW (local note: section III.B, PJM)

```text
Miami Fort Power Station (Miami Fort) located in Ohio.
```

Evidence 9: document Doc 5 (fr_2025_23298.txt), proves component 1. 660 MW (local note: Competitive Impact Statement III.A.1)

```text
Calpine's two ERCOT plants to be divested as part of the ERCOT Divestiture Assets are Jack A. Fusco and Gregory.
```

Evidence 10: document Doc 5 (fr_2025_23298.txt), proves component 1. 660 MW (local note: Competitive Impact Statement III.A.1)

```text
557 MW combined-cycle natural gas facility located in Richmond, Texas.
```

Evidence 11: document Doc 5 (fr_2025_23298.txt), proves component 1. 660 MW (local note: Competitive Impact Statement III.A.1)

```text
Gregory is a 365 MW combined-cycle natural gas facility located in Gregory, Texas. Calpine owns approximately 28.5% of Gregory.
```

### Necessary documents

- Tick Doc 5 (fr_2025_23298.txt), role: Answer component
- Tick Doc 4 (fr_2025_21597.txt), role: Exclusion / condition source

  Reviewer note:

```text
Doc 4 puts EPA's covered coal plants by market: Coleto Creek in ERCOT, the PJM plants in Illinois and Ohio, outside the PJM Coastal Mid-Atlantic market, so PJM divestitures drop out.
```

Leave unticked: Doc 1 (fr_2024_06556.txt), Doc 2 (fr_2024_24879.txt), Doc 3 (fr_2025_12990.txt), Doc 6 (fr_2026_03659.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 4's PJM coal plants are in Illinois and Ohio, outside Doc 5's PJM Coastal Mid-Atlantic market; adding PJM divestitures gives 5,040 MW. Part vs total: Doc 5's Gregory is 365 MW, Calpine owns 28.5%; the whole plant gives 920 MW. Gold: 660 MW.
```

(48 / 50 words.)
