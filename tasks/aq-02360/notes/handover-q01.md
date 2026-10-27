# aq-02360 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02360 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 ac260ba11adf232c61a21515648d18e9cb630e0a656698370f3350b21f3c5192: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 2, D02 = Doc 1.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
From 1 April 2022, which paragraph of alpha's rules on transfer payments to other schemes cited which Pension Schemes Act 1993 subsection? Give them in that order.
```

### Number of asks

2 asks

### Gold answer

```text
Regulation 142(4), section 95(2)
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 1, Annex E, draft regulation 5): under the heading "Amendment of regulation 142 (transfer of payments made to other schemes or pension arrangements)", the draft reads "In regulation 142(4), for “95(2)” substitute “95(2A)”." So the paragraph of alpha's transfer-payment rule that cross-refers to the Pension Schemes Act 1993 is regulation 142(4), and before any change it cited section 95(2).
Step 2. Source fact (Doc 1, paragraph 3.3): the change was proposed as an "amendment to regulation 142 to correct a cross reference to the wrong subsection" of the Pension Schemes Act 1993.
Step 3. Source fact (Doc 1, Annex E, draft regulation 1(2)): "These Regulations come into force on 1st April 2022". Had draft regulation 5 been made, regulation 142(4) would have cited the substitute subsection from that date.
Step 4. Source fact (Doc 2, Cabinet Office response on the technical amendments): "Cabinet Office has decided not to proceed with the amendment of regulation 142 to update a cross-referencing error". The 2022 amendments therefore left regulation 142(4) unchanged.
Step 5. Conclusion (Doc 1 and Doc 2): from 1 April 2022 regulation 142(4) still cited section 95(2) of the Pension Schemes Act 1993.
Decoy: 95(2A), the substitute subsection in Doc 1's draft regulation 5, never took effect, because Doc 2 records that the amendment of regulation 142 was not made.
```

### Answer components

Component 1

```text
Regulation 142(4)
```

Component 2

```text
Section 95(2)
```

### Evidence

Evidence 1: document Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), proves component 1. Regulation 142(4) (local note: Annex E, draft regulation 5 heading)

```text
Amendment of regulation 142 (transfer of payments made to other schemes or pension arrangements)
```

Evidence 2: document Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), proves component 1. Regulation 142(4) (local note: Annex E, draft regulation 5)

```text
In regulation 142(4), for “95(2)” substitute “95(2A)”.
```

Evidence 3: document Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), proves component 2. Section 95(2) (local note: Annex E, draft regulation 5)

```text
In regulation 142(4), for “95(2)” substitute “95(2A)”.
```

Evidence 4: document Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), proves component 2. Section 95(2) (local note: Annex E, draft regulation 1(2)

```text
These Regulations come into force on 1st April 2022
```

Evidence 5: document Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), proves component 2. Section 95(2) (local note: paragraph 3.3)

```text
amendment to regulation 142 to correct a cross reference to the wrong subsection
```

Evidence 6: document Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), proves component 2. Section 95(2) (local note: paragraph 4.61)

```text
Cabinet Office has decided not to proceed with the amendment of regulation 142
```

### Necessary documents

- Tick Doc 1 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service.txt), role: Answer component
- Tick Doc 2 (Civil-Service-Pension-Scheme-2015-remedy-and-civil-service-2.txt), role: Answer component

Leave unticked: Doc 3 (Civil-Service-Pensions-2015-Remedy-McCloud-consultation.txt), Doc 4 (Civil-Service-Pensions-2015-Remedy-consultation-response.txt), Doc 5 (Consultation-on-reform-of-the-Civil-Service-Compensation.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Superseded date or version: Doc 1's draft regulation 5 would change regulation 142(4)'s cross-reference from 95(2) to 95(2A) from 1 April 2022. A careless solver assumes the draft took effect and answers section 95(2A). Doc 2 paragraph 4.61 says the amendment was not made, so 142(4) still cited 95(2).
```

(49 / 50 words.)
