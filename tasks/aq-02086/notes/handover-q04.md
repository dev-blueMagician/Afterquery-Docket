# aq-02086 q04 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02086 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 ac7582aa7207872459660aa34f55eca91592fc432f6a8a6d968626c49c17bd55: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 1, D04 = Doc 3.
- Floor: 0 FAIL, 4 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN format: say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' (form: answer format stated)
  - WARN single-passage: one passage of D02 holds the answer: '...ed fuel gas 10. volatile organic compounds 11. crowding and space 12. entry by intruders 13. lighting 14. noise 15. domestic hygiene, pests and refuse 16. foo...' (rules 2-3)
  - WARN single-passage: one passage of D04 holds the answer: '...ducts lead radiation un-combusted fuel gas volatile organic compounds entry by intruders lighting noise water supply flames, hot surfaces and materials collis...' (rules 2-3)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which hazard types had an emergency or significant-risk example in the Awaab's Law consultation's annex that the law's first phase missed? Any order.
```

### Number of asks

1 ask

### Gold answer

```text
"Entry by intruders", "Domestic hygiene, pests and refuse"
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 1, annex of example hazards): the annex classes as emergencies widespread damp and mould with a child struggling to breathe, a broken front door lock that leaves the home insecure (entry by intruders) and a total loss of water supply (water supply). It classes as significant risks damp and mould in two rooms with an immunosuppressed occupant, mice or rats entering through the kitchen's external wall (domestic hygiene, pests and refuse) and a faulty external window whose handle may snap (entry by intruders). Its remaining examples are routine and would not trigger Awaab's Law.

Step 2. Source fact (Doc 3, phasing and Annex A): from 27 October 2025, in the first phase, Awaab's Law covers damp and mould hazards that present a significant risk and all emergency hazards. Significant hazards of the domestic hygiene, pests and refuse type are added in 2026; entry by intruders and water supply are added in 2027.

Step 3. Application (Steps 1 and 2; Doc 1 and Doc 3): damp and mould had no missed example, since both of its examples were covered from the first phase. Decoy: water supply had none either. Its only emergency or significant-risk example, the lost water supply, is an emergency and so was covered from the first phase, although the type joins for significant cases only in 2027.

Step 4. Application (Steps 1 and 2; Doc 1 and Doc 3): entry by intruders had a missed example, the faulty window handle (significant risk, added in 2027), even though its broken front door lock example was an emergency and covered. Domestic hygiene, pests and refuse had a missed example, the rodents (significant risk, added in 2026). These are the two hazard types.
```

### Answer components

Component 1

```text
Entry by intruders
```

Component 2

```text
Domestic hygiene, pests and refuse
```

### Evidence

Evidence 1: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 1. Entry by intruders (local note: L965, annex example of significant risk)

```text
Example of hazard posing a significant risk to residents (entry by intruders)
```

Evidence 2: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 1. Entry by intruders (local note: L967, annex example)

```text
A resident has reported that one of their external windows is faulty, and whilst it can be secured for the moment, they suspect the handle will snap off and prevent them from being able to lock the window.
```

Evidence 3: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. Entry by intruders (local note: L613, Annex A Phase 3 row)

```text
Volatile organic compounds Entry by intruders Lighting Noise Water supply
```

Evidence 4: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 2. Domestic hygiene, pests and refuse (local note: L957, annex example of significant risk)

```text
Example of hazard posing a significant risk to residents(Domestic hygiene, pests and refuse)
```

Evidence 5: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 2. Domestic hygiene, pests and refuse (local note: L959, annex example)

```text
A social housing resident has reported seeing mice or rats in their property that they believe are entering the property from the external wall in their kitchen.
```

Evidence 6: document Doc 3 (Awaabs-Law-government-response.txt), proves component 2. Domestic hygiene, pests and refuse (local note: L612, Annex A Phase 2 row)

```text
Structural collapse and falling elements Domestic hygiene, pests and refuse Food safety
```

Evidence 7: document Doc 3 (Awaabs-Law-government-response.txt), proves component 1. Entry by intruders (local note: L176, first phase)

```text
From 27 October 2025, social landlords will have to investigate and take action on all emergency hazards as soon as reasonably practicable and within no longer than 24 hours.
```

Evidence 8: document Doc 3 (Awaabs-Law-government-response.txt), proves component 2. Domestic hygiene, pests and refuse (local note: L176, first phase)

```text
From 27 October 2025, social landlords will have to investigate and take action on all emergency hazards as soon as reasonably practicable and within no longer than 24 hours.
```

### Necessary documents

- Tick Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), role: Answer component
- Tick Doc 3 (Awaabs-Law-government-response.txt), role: Answer component

Leave unticked: Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), Doc 5 (Response-to-the-consultation-on-a-Decent-Homes-Standard-in.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Superseded date or version

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 1's water-supply example is an emergency, which Doc 3's first phase covers, so adding water supply gives three types. Entry by intruders stays: its window example is significant. Doc 1 proposed covering all hazards at once, giving none. Gold: entry by intruders and domestic hygiene.
```

(46 / 50 words.)
