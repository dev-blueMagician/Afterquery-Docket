# aq-03950 q01 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03950 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 9e00cc4c1c62eb5ba3ce662ea6a3f35d3cf606aa2bb749e152ccd97779dc383d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 3, D02 = Doc 2, D03 = Doc 4, D04 = Doc 5, D05 = Doc 6, D06 = Doc 7, D07 = Doc 1.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D02 or D01: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN documents: D03: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN documents: D04: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN documents: 7 documents listed; the form's reasoning usually covers 2-4, only those the answer relies on
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many witnesses listed in the Welsh Affairs Committee's tourism report gave evidence at hearings attended by Rob Roberts MP?
```

### Number of asks

1 ask

### Gold answer

```text
9 witnesses
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 6, header): the transcript of the hearing on 20 July 2022 names Rob Roberts among the members present.
Step 2. Source input (Doc 7, header and Q234): the transcript of the hearing on 1 February 2023 names Rob Roberts among the members present. This transcript is the second panel of that hearing only, and Roberts refers in it to what "the last panel" said, so he was there for both panels.
Step 3. Source input (Doc 2, Doc 3, Doc 4 and Doc 5, headers): the members present on 20 April 2022, 25 May 2022 and 15 June 2022 do not include Rob Roberts, so the witnesses heard on those days are left out. The Roberts who speaks on 15 June 2022 is Ian Roberts of Portmeirion, a witness.
Step 4. Source input (Doc 1, witness list): under 20 July 2022 the report lists Anthony Pickles, Annette Pritchard and Dorothy Yen. That is 3 witnesses.
Step 5. Source input (Doc 1, witness list): under 1 February 2023 the report lists Vaughan Gething, Jason Thomas and Heledd Owen of the Welsh Government, and then Stuart Andrew, Duncan Parish and Patricia Yates. That is 6 witnesses. The first three have no transcript among the documents; only the report's list names them all.
Step 6. Calculation from Steps 4 and 5 (Doc 1, Doc 6 and Doc 7): 3 + 6 = 9 witnesses at the hearings Rob Roberts attended.
Step 7. Final answer (Doc 1, Doc 6 and Doc 7): 9 witnesses.
```

### Answer components

Component 1

```text
9 witnesses
```

### Evidence

Evidence 1: document Doc 6 (ukc_6476_oral_10647.txt), proves component 1. 9 witnesses (local note: header, members present)

```text
Members present: Stephen Crabb (Chair); Wayne David; Ruth Jones; Rob Roberts; Dr Jamie Wallis.
```

Evidence 2: document Doc 7 (ukc_6476_oral_12643.txt), proves component 1. 9 witnesses (local note: header, members present)

```text
Members present: Stephen Crabb (Chair); Simon Baynes; Virginia Crosbie; Wayne David; Geraint Davies; Ruth Jones; Ben Lake; Rob Roberts.
```

Evidence 3: document Doc 7 (ukc_6476_oral_12643.txt), proves component 1. 9 witnesses (local note: Q209, Chair)

```text
We are going to move seamlessly over to our second panel now
```

Evidence 4: document Doc 7 (ukc_6476_oral_12643.txt), proves component 1. 9 witnesses (local note: Q234, Rob Roberts)

```text
In the last panel, we heard about the huge social media presence of the WWE
```

Evidence 5: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. 9 witnesses (local note: Witnesses, date heading)

```text
Wednesday 20 July 2022
```

Evidence 6: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. 9 witnesses (local note: Witnesses, 20 July 2022)

```text
Anthony Pickles, Former Head of Tourism Affairs, VisitBritain; Professor Annette Pritchard, Professor of Tourism Management, Leeds Beckett University; Professor Dorothy A. Yen, Professor in Marketing, Brunel Business School, Brunel University London
```

Evidence 7: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. 9 witnesses (local note: Witnesses, date heading)

```text
Wednesday 1 February 2023
```

Evidence 8: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. 9 witnesses (local note: Witnesses, 1 February 2023, first panel)

```text
Vaughan Gething MS, Minister for Economy, Welsh Government; Jason Thomas, Director of Culture, Sport and Tourism, Welsh Government; Heledd Owen, Deputy Director of Marketing, Welsh Government
```

Evidence 9: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. 9 witnesses (local note: Witnesses, 1 February 2023, second panel)

```text
Rt Hon Stuart Andrew MP, Minister for Sport, Tourism and Civil Society, Department for Digital, Culture, Media and Sport; Duncan Parish, Deputy Director for Tourism and Cultural Diplomacy, Department for Digital, Culture, Media and Sport; Patricia Yates, Chief Executive, VisitBritain/VisitEngland
```

Evidence 10: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. 9 witnesses (local note: para 6)

```text
held five oral evidence hearings
```

Evidence 11: document Doc 2 (ukc_6476_oral_10125.txt), proves component 1. 9 witnesses (local note: header, members present, 20 April 2022)

```text
Members present: Stephen Crabb (Chair); Geraint Davies; Ruth Jones; Ben Lake; Robin Millar; Beth Winter.
```

Evidence 12: document Doc 3 (ukc_6476_oral_10124.txt), proves component 1. 9 witnesses (local note: header, members present, 20 April 2022)

```text
Members present: Stephen Crabb (Chair); Geraint Davies; Ruth Jones; Ben Lake; Robin Millar; Beth Winter.
```

Evidence 13: document Doc 4 (ukc_6476_oral_10335.txt), proves component 1. 9 witnesses (local note: header, members present, 25 May 2022)

```text
Members present: Stephen Crabb (Chair); Ruth Jones; Ben Lake; Robin Millar.
```

Evidence 14: document Doc 5 (ukc_6476_oral_10428.txt), proves component 1. 9 witnesses (local note: header, members present, 15 June 2022)

```text
Members present: Stephen Crabb (Chair); Ruth Jones; Ben Lake; Robin Millar; Beth Winter.
```

Evidence 15: document Doc 5 (ukc_6476_oral_10428.txt), proves component 1. 9 witnesses (local note: header, witnesses)

```text
Ian Roberts, Finance Director, Portmeirion Cymru
```

### Necessary documents

- Tick Doc 1 (ukc_6476_report_40824.txt), role: Answer component
- Tick Doc 6 (ukc_6476_oral_10647.txt), role: Answer component
- Tick Doc 7 (ukc_6476_oral_12643.txt), role: Answer component
- Tick Doc 2 (ukc_6476_oral_10125.txt), role: Exclusion / condition source; also tick Doc 3 (ukc_6476_oral_10124.txt) and choose it in Doc 2's "or..." box

  Reviewer note:

```text
Members present on 20 April 2022 do not include Rob Roberts, so the six witnesses the report lists for that day are not counted.
```
- Tick Doc 4 (ukc_6476_oral_10335.txt), role: Exclusion / condition source

  Reviewer note:

```text
Members present on 25 May 2022 do not include Rob Roberts, so the five witnesses the report lists for that day are not counted.
```
- Tick Doc 5 (ukc_6476_oral_10428.txt), role: Exclusion / condition source

  Reviewer note:

```text
Members present on 15 June 2022 do not include Rob Roberts (Ian Roberts is a witness), so that day's four listed witnesses are not counted.
```

Leave unticked: none

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 7 is only the second panel of the 1 February 2023 hearing, so its header names a part, three of that day's six witnesses. Adding the transcript headers gives 6. The total needs Doc 1's witness list, which adds the Welsh Government panel: 9.
```

(48 / 50 words.)
