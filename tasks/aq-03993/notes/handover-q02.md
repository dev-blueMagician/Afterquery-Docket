# aq-03993 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03993 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 dd07a6e731e23ad7347aa4a16649789b8b9f24b71c41d09ff160c678258577b2: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 4, D04 = Doc 1.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 75. Doc 1 prints it first at character 33,332, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many BBC-funded local democracy reporters does the evidence place on the staff of organisations that sent a witness to the committee's hearings?
```

### Number of asks

1 ask

### Gold answer

```text
77 reporters
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, list of witnesses): among the witnesses the report lists "David Higgerson, Chief Audience Officer, Reach plc" and "David Floyd, Director, Social Spider CIC".
Step 2. Source input (Doc 1, section "The Local Democracy Reporter Service"): the BBC pays these reporters' salaries and they "are allocated to local news providers". In the latest allocation Reach "Plc took 75".
Step 3. Source input (Doc 4, David Floyd): he says the "Local Democracy Reporter scheme funds posts" and adds "we have two of them and it is great". Social Spider therefore has 2 of these reporters. Doc 1 gives no figure for Social Spider.
Step 4. Source input (Doc 4, Dr Rupa Huq to the last panel): "I think the Liverpool Echo was a Reach plc title". The Echo's editor, Maria Breslin, also gave evidence, but her paper's reporters are already inside Reach's figure and no separate number is given for them.
Step 5. Not counted (Doc 1 and Doc 4): the BBC pays for the reporters but they sit with the news providers, not on its own staff. Matt Abbott says of the Independent Community News Network "I think our members employ perhaps a dozen Local Democracy Reporters themselves", which puts them on the members' staff, not the network's. Newsquest and JPI Media, the other publishers in the allocation sentence of Doc 1, sent no witness, and neither did Notts TV, the only television provider with a contract.
Step 6. Calculation (Doc 1 and Doc 4): 75 + 2 = 77 reporters.
Step 7. Final answer (Doc 1 and Doc 4): 77 reporters.
```

### Answer components

Component 1

```text
77 reporters
```

### Evidence

Evidence 1: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. 77 reporters (local note: Witnesses, 28 June 2022)

```text
David Higgerson, Chief Audience Officer, Reach plc
```

Evidence 2: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. 77 reporters (local note: Witnesses, 7 July 2022)

```text
David Floyd, Director, Social Spider CIC
```

Evidence 3: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. 77 reporters (local note: para 30)

```text
The BBC funds the salaries of 165 journalists, who are allocated to local news providers
```

Evidence 4: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. 77 reporters (local note: para 33, before the page's footnotes)

```text
Of the 165 reporters allocated in July 2021, Reach
```

Evidence 5: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. 77 reporters (local note: para 33, after the page's footnotes)

```text
Plc took 75, Newsquest 28.5, and JPI Media (now National World) 35.5.
```

Evidence 6: document Doc 4 (ukc_6536_oral_10571.txt), proves component 1. 77 reporters (local note: Q255, David Floyd)

```text
the Local Democracy Reporter scheme funds posts
```

Evidence 7: document Doc 4 (ukc_6536_oral_10571.txt), proves component 1. 77 reporters (local note: Q255, David Floyd)

```text
we have two of them and it is great
```

Evidence 8: document Doc 4 (ukc_6536_oral_10571.txt), proves component 1. 77 reporters (local note: Q268, Dr Rupa Huq)

```text
I think the Liverpool Echo was a Reach plc title that had a donation drive
```

Evidence 9: document Doc 4 (ukc_6536_oral_10571.txt), proves component 1. 77 reporters (local note: Q271, Matt Abbott, not counted)

```text
I think our members employ perhaps a dozen Local Democracy Reporters themselves
```

Evidence 10: document Doc 1 (ukc_6536_report_33635.txt), proves component 1. 77 reporters (local note: para 64, not counted)

```text
Notts TV qualified in the latest round of contract allocations, though it was the only TV news provider to do so.
```

### Necessary documents

- Tick Doc 1 (ukc_6536_report_33635.txt), role: Answer component
- Tick Doc 4 (ukc_6536_oral_10571.txt), role: Answer component

Leave unticked: Doc 2 (ukc_6536_oral_10244.txt), Doc 3 (ukc_6536_oral_10505.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 1's allocation sentence gives Reach 75 reporters, and Reach is the only publisher there that sent a witness, so 75 looks complete. It is one part. In Doc 4 David Floyd says Social Spider has two such posts. Careless answer 75; the total is 77.
```

(49 / 50 words.)
