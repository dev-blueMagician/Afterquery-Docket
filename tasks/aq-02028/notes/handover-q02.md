# aq-02028 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02028 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 c9e651b935eb54e9dc9e6e9fe1cbf6de0da7719814573d17272fdfcd63eb9e6a: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D08 = Doc 8.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Using the whole-port throughput Melbourne's newest container terminal states, how many yearly truck trips would 4 TEU average loads save?
```

### Number of asks

1 ask

### Gold answer

```text
432,000 truck trips
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 1, establishment of VICT at the Port of Melbourne): in 2014 VICT was awarded the concession for the third international container terminal in the Port of Melbourne, while the existing container terminals are at East Swanson and West Swanson Dock; VICT's first vessel was serviced in March 2017. VICT is therefore the port's newest container terminal.

Step 2. Source fact (Doc 1, same section): VICT states that the Port of Melbourne as a whole, not VICT alone, currently services over 2.88 million TEU annually.

Step 3. Source fact (Doc 8, asset utilisation): the Victorian Transport Association puts the current average load at 2.5 TEU per truck trip, gets yearly truck trips by dividing the port's yearly TEU by the load per trip, and also models a load of 4 TEU per vehicle per trip.

Step 4. Calculation (from Steps 2 and 3; Doc 1 and Doc 8), yearly truck trips at the current average load, in millions: 2.88 / 2.5 = 1.152 million trips.

Step 5. Calculation (from Steps 2 and 3; Doc 1 and Doc 8), yearly truck trips at an average load of 4 TEU, in millions: 2.88 / 4 = 0.72 million trips.

Step 6. Calculation (from Steps 4 and 5; Doc 1 and Doc 8), yearly truck trips saved, in millions: 1.152 - 0.72 = 0.432 million trips.
```

### Answer components

Component 1

```text
432,000
```

### Evidence

Evidence 1: document Doc 1 (pcau_maritime_r1_sub007_maritime_logistics.txt), proves component 1. 432,000 (local note: L35, establishment of VICT)

```text
VICT was awarded the concession to design, build and operate the third international container terminal in the Port of Melbourne
```

Evidence 2: document Doc 1 (pcau_maritime_r1_sub007_maritime_logistics.txt), proves component 1. 432,000 (local note: L35, existing terminals)

```text
the existing container terminals at East Swanson and West Swanson Dock
```

Evidence 3: document Doc 1 (pcau_maritime_r1_sub007_maritime_logistics.txt), proves component 1. 432,000 (local note: L40, first vessel)

```text
Our first vessel was serviced in March 2017
```

Evidence 4: document Doc 1 (pcau_maritime_r1_sub007_maritime_logistics.txt), proves component 1. 432,000 (local note: L33, port throughput)

```text
It currently services over 2.88 million Twenty-foot equivalent Units (TEU) annually
```

Evidence 5: document Doc 8 (pcau_maritime_r1_sub024_maritime_logistics.txt), proves component 1. 432,000 (local note: L140, current average load)

```text
the current average is 2.5 TEU
```

Evidence 6: document Doc 8 (pcau_maritime_r1_sub024_maritime_logistics.txt), proves component 1. 432,000 (local note: L147, TEU to truck trips)

```text
handled through Melbourne with a load factor of 2.5 TEU vehicle per trip resulting in approximately 1.2million truck trips pa
```

Evidence 7: document Doc 8 (pcau_maritime_r1_sub024_maritime_logistics.txt), proves component 1. 432,000 (local note: L150, 4 TEU scenario)

```text
Increase the load factor to 4 TEU per vehicle per trip
```

### Necessary documents

- Tick Doc 1 (pcau_maritime_r1_sub007_maritime_logistics.txt), role: Answer component
- Tick Doc 8 (pcau_maritime_r1_sub024_maritime_logistics.txt), role: Answer component

Leave unticked: Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), Doc 3 (pcau_maritime_r1_sub014_maritime_logistics.txt), Doc 4 (pcau_maritime_r1_sub016_maritime_logistics.txt), Doc 5 (pcau_maritime_r1_sub017_maritime_logistics.txt), Doc 6 (pcau_maritime_r1_sub021_maritime_logistics.txt), Doc 7 (pcau_maritime_r1_sub023_maritime_logistics.txt), Doc 9 (pcau_maritime_r1_sub025_maritime_logistics.txt), Doc 10 (pcau_maritime_r1_sub026_maritime_logistics.txt), Doc 11 (pcau_maritime_r1_sub032_maritime_logistics.txt), Doc 12 (pcau_maritime_r1_sub033_maritime_logistics.txt), Doc 13 (pcau_maritime_r1_sub034_maritime_logistics.txt), Doc 14 (pcau_maritime_r1_sub037_maritime_logistics.txt), Doc 15 (pcau_maritime_r1_sub040_maritime_logistics.txt), Doc 16 (pcau_maritime_r1_sub041_maritime_logistics.txt), Doc 17 (pcau_maritime_r1_sub042_maritime_logistics.txt), Doc 18 (pcau_maritime_r1_sub043_maritime_logistics.txt), Doc 19 (pcau_maritime_r1_sub046_maritime_logistics.txt), Doc 20 (pcau_maritime_r1_sub048_maritime_logistics.txt)

### Reasoning tags

Tick: Cross-document join, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Doc 8 prints about 450,000 fewer trips for 4 TEU loads, on VTA's own 3 million TEU, not the newest terminal's figure. Doc 1 gives the port 2.88 million TEU but VICT itself 800,000 TEU (120,000). Correct: 2.88 / 2.5 - 2.88 / 4 = 0.432 million.
```

(47 / 50 words.)
