# aq-02086 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02086 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 43468c16594d5867a92de4a2e2ecc6d3a31b7dd3f725196fa39eeacac3a6ad4b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 1, D04 = Doc 3.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN format: say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' (form: answer format stated)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which annexed Awaab's Law consultation examples, classed there as emergencies or significant risks, were not yet covered when the law's first phase began? Any order.
```

### Number of asks

1 ask

### Gold answer

```text
Rodents entering via the kitchen wall (domestic hygiene hazard), and a faulty window handle (entry by intruders hazard)
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 1, annex of example hazards): the consultation classes these annexed examples as emergencies: widespread damp and mould with a child struggling to breathe, a broken front door lock that leaves the home insecure (entry by intruders) and a total loss of water supply (water supply). It classes these as significant risks: damp and mould in two rooms with an immunosuppressed occupant, mice or rats entering through the kitchen's external wall (domestic hygiene, pests and refuse) and a faulty external window whose handle may snap (entry by intruders). Its other examples (small mould patches, one broken tap, a loose handrail) are routine and would not trigger Awaab's Law.

Step 2. Source fact (Doc 3, phasing and Annex A): from 27 October 2025, in the first phase, Awaab's Law covers damp and mould hazards that present a significant risk and all emergency hazards. Significant hazards of the domestic hygiene, pests and refuse type are added in 2026; entry by intruders and water supply are added in 2027.

Step 3. Application (Steps 1 and 2; Doc 1 and Doc 3): both damp and mould examples were covered from the first phase. The broken front door lock and the lost water supply were also covered then, because every emergency hazard was in the first phase, even though their hazard types join for significant cases only in 2027. They are the decoys.

Step 4. Application (Steps 1 and 2; Doc 1 and Doc 3): the rodents (significant risk, domestic hygiene, pests and refuse) waited for 2026 and the faulty window handle (significant risk, entry by intruders) for 2027. These two examples were not yet covered when the first phase began.
```

### Answer components

Component 1

```text
Rodents entering via the kitchen wall (domestic hygiene hazard)
```

Component 2

```text
a faulty window handle (entry by intruders hazard)
```

### Evidence

Evidence 1: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 1. Rodents entering via the kitchen wall (domestic hygiene hazard) (local note: L957, annex example of significant risk)

```text
Example of hazard posing a significant risk to residents(Domestic hygiene, pests and refuse)
```

Evidence 2: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 1. Rodents entering via the kitchen wall (domestic hygiene hazard) (local note: L959, annex example)

```text
A social housing resident has reported seeing mice or rats in their property that they believe are entering the property from the external wall in their kitchen.
```

Evidence 3: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. Rodents entering via the kitchen wall (domestic hygiene hazard) (local note: L612, Annex A Phase 2 row)

```text
Structural collapse and falling elements Domestic hygiene, pests and refuse Food safety
```

Evidence 4: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 2. a faulty window handle (entry by intruders hazard) (local note: L965, annex example of significant risk)

```text
Example of hazard posing a significant risk to residents (entry by intruders)
```

Evidence 5: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 2. a faulty window handle (entry by intruders hazard) (local note: L967, annex example)

```text
A resident has reported that one of their external windows is faulty, and whilst it can be secured for the moment, they suspect the handle will snap off and prevent them from being able to lock the window.
```

Evidence 6: document Doc 3 (Awaabs-Law-government-response.txt), proves component 2. a faulty window handle (entry by intruders hazard) (local note: L613, Annex A Phase 3 row)

```text
Volatile organic compounds Entry by intruders Lighting Noise Water supply
```

Evidence 7: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. Rodents entering via the kitchen wall (domestic hygiene hazard) (local note: L176, first phase)

```text
From 27 October 2025, social landlords will have to investigate and take action on all emergency hazards as soon as reasonably practicable and within no longer than 24 hours.
```

Evidence 8: document Doc 3 (Awaabs-Law-government-response.txt), proves component 2. a faulty window handle (entry by intruders hazard) (local note: L176, first phase)

```text
From 27 October 2025, social landlords will have to investigate and take action on all emergency hazards as soon as reasonably practicable and within no longer than 24 hours.
```

### Necessary documents

- Tick Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), role: Answer component
- Tick Doc 3 (Awaabs-Law-government-response.txt), role: Answer component

Leave unticked: Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), Doc 5 (Response-to-the-consultation-on-a-Decent-Homes-Standard-in.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Superseded date or version

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 1's door-lock and water-supply examples are emergencies; Doc 3 puts all emergency hazards in Phase 1, though their types join in 2027, so listing them gives four items. Doc 1 proposed covering every HHSRS hazard at once, giving none. Gold: rodents (2026) and window (2027).
```

(46 / 50 words.)
