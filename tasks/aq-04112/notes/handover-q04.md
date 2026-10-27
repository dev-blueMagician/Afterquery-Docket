# aq-04112 q04 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04112 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 ca843e5c3c94945af18ec57b1dc5aadf2c7545da0798456181b7140977dfff96: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 2, D02 = Doc 3, D03 = Doc 1.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which organisations, if any, sent written evidence but no witness to the Commons inquiry into food and farming labour shortages, yet were named at its hearings of 26 October and 9 November 2021? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
Association of Labour Providers, Kernock Park Plants, Royal College of Veterinary Surgeons
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, the list of published written evidence at the end of the report): the report lists every organisation and person that sent the inquiry written evidence. The Association of Labour Providers, Kernock Park Plants, the Royal College of Veterinary Surgeons and the Department for Environment, Food and Rural Affairs are all on it.
Step 2. Source input (Doc 2 and Doc 3, the witness lists at the head of each hearing): nine bodies on that list sent witnesses to these two hearings: the National Farmers Union, the British Poultry Council, the National Pig Association, the British Meat Processors Association, the British Veterinary Association and the Food and Drink Federation on 26 October, and UKHospitality, the British Retail Consortium and the Cold Chain Federation on 9 November. They sent a witness, so they are out.
Step 3. Source input and decoy (Doc 1, the report's list of witnesses, which covers every hearing of the inquiry; Doc 2 and Doc 3): the Department for Environment, Food and Rural Affairs sent its Secretary of State and a Director-General to a later hearing. It is named at both hearings, as "DEFRA" and "Defra", and the Chair of the second says its Secretary of State is coming in, but it sent a witness to the inquiry, so it is out too.
Step 4. Source input (Doc 2, the hearing of 26 October 2021, Mrs Murray's question to the first panel): she has "Kernock Plants" in her constituency, a large family business. That is Kernock Park Plants under a short form of its name; no other Kernock appears in any of the documents. In.
Step 5. Source input (Doc 2, the same hearing, Dr Hudson's question to the second panel): he names the Royal College of Veterinary Surgeons in full. In.
Step 6. Source input (Doc 3, the hearing of 9 November 2021, Ian Byrne's question to the first panel): he quotes the Association of Labour Providers on the factors driving labour shortages. In.
Step 7. Decoys left out (Doc 1, Doc 2 and Doc 3): a place or an unnamed group names no organisation. Derek Jarman's "Cornish and Lincolnshire daffodil market" does not name Lincolnshire County Council, and the Chair's "some Northern Irish companies" does not name the Northern Ireland Pork and Bacon Forum, though both sent written evidence. No other organisation on the list that sent no witness is named at either hearing.
Step 8. Final answer (Doc 1, Doc 2 and Doc 3): Association of Labour Providers, Kernock Park Plants, Royal College of Veterinary Surgeons.
```

### Answer components

Component 1

```text
Association of Labour Providers
```

Component 2

```text
Kernock Park Plants
```

Component 3

```text
Royal College of Veterinary Surgeons
```

### Evidence

Evidence 1: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. Association of Labour Providers (local note: Published written evidence, opening line)

```text
The following written evidence was received and can be viewed on the inquiry publications page of the Committee
```

Evidence 2: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. Association of Labour Providers (local note: Published written evidence, the Association's entry)

```text
Association of Labour Providers (LS0088)
```

Evidence 3: document Doc 1 (ukc_1497_report_9580.txt), proves component 2. Kernock Park Plants (local note: Published written evidence, Kernock's entry)

```text
Kernock Park Plants (LS0004)
```

Evidence 4: document Doc 1 (ukc_1497_report_9580.txt), proves component 3. Royal College of Veterinary Surgeons (local note: Published written evidence, the Royal College's entry)

```text
Royal College of Veterinary Surgeons (LS0009)
```

Evidence 5: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. Association of Labour Providers (local note: Published written evidence, Defra's entry)

```text
Department for Environment, Food and Rural Affairs (LS0063)
```

Evidence 6: document Doc 2 (ukc_1497_oral_2900.txt), proves component 2. Kernock Park Plants (local note: witness list at the head of the transcript, first panel)

```text
I: Tom Bradshaw, Vice-President, National Farmers Union; Graeme Dear, Chair, British Poultry Council; Derek Jarman, Chair Designate, British Protected Ornamentals Association; and Charlie Dewhirst, Policy Adviser, National Pig Association.
```

Evidence 7: document Doc 2 (ukc_1497_oral_2900.txt), proves component 3. Royal College of Veterinary Surgeons (local note: witness list at the head of the transcript, second panel)

```text
II: Nick Allen, Chief Executive Officer, British Meat Processors Association; James Russell, Senior Vice-President, British Veterinary Association; and Ian Wright, Chief Executive Officer, Food and Drink Federation.
```

Evidence 8: document Doc 3 (ukc_1497_oral_2977.txt), proves component 1. Association of Labour Providers (local note: witness list at the head of the transcript, first panel)

```text
I: Kate Nicholls OBE, Chief Executive Officer, UKHospitality; Andrew Opie, Director of Food and Sustainability, British Retail Consortium; Tom Southall, Policy Director, Cold Chain Federation.
```

Evidence 9: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. Association of Labour Providers (local note: Witnesses, opening line)

```text
The following witnesses gave evidence.
```

Evidence 10: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. Association of Labour Providers (local note: Witnesses, the later hearing with Defra)

```text
The Rt Hon George Eustice MP, Secretary of State, Department for Environment, Food and Rural Affairs; David Kennedy, Director-General, Food, Farming and Bio-Security, Department for Environment, Food and Rural Affairs
```

Evidence 11: document Doc 2 (ukc_1497_oral_2900.txt), proves component 2. Kernock Park Plants (local note: Q17, Charlie Dewhirst, Defra named)

```text
We have been having crisis meetings with DEFRA since February
```

Evidence 12: document Doc 3 (ukc_1497_oral_2977.txt), proves component 1. Association of Labour Providers (local note: the Chair, closing the first panel, Defra named)

```text
We have the Secretary of State for Defra coming in, which is great
```

Evidence 13: document Doc 2 (ukc_1497_oral_2900.txt), proves component 2. Kernock Park Plants (local note: Q18, Mrs Murray)

```text
Mrs Murray: I have one last part to that question, Chair. I do understand, Derek. I have Kernock Plants in my constituency. It is a quite large family going concern.
```

Evidence 14: document Doc 2 (ukc_1497_oral_2900.txt), proves component 3. Royal College of Veterinary Surgeons (local note: Q97, Dr Hudson)

```text
Dr Hudson: You have touched on the fact that the Royal College of Veterinary Surgeons has been trying to look at that.
```

Evidence 15: document Doc 3 (ukc_1497_oral_2977.txt), proves component 1. Association of Labour Providers (local note: Q117, Ian Byrne)

```text
Ian Byrne: It is good to see you physically and not virtually. The Association of Labour Providers gives a number of factors that are driving labour shortages in the food supply chain.
```

Evidence 16: document Doc 2 (ukc_1497_oral_2900.txt), proves component 2. Kernock Park Plants (local note: Q31, Derek Jarman, left out)

```text
the Cornish and Lincolnshire daffodil market is early
```

Evidence 17: document Doc 1 (ukc_1497_report_9580.txt), proves component 2. Kernock Park Plants (local note: Published written evidence, left out)

```text
Lincolnshire County Council (LS0051)
```

Evidence 18: document Doc 3 (ukc_1497_oral_2977.txt), proves component 1. Association of Labour Providers (local note: Q142, the Chair, left out)

```text
We took some evidence privately from some Northern Irish companies
```

Evidence 19: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. Association of Labour Providers (local note: Published written evidence, left out)

```text
Northern Ireland Pork and Bacon Forum (LS0065)
```

### Necessary documents

- Tick Doc 1 (ukc_1497_report_9580.txt), role: Answer component
- Tick Doc 2 (ukc_1497_oral_2900.txt), role: Answer component
- Tick Doc 3 (ukc_1497_oral_2977.txt), role: Answer component

Leave unticked: none

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 2 calls Kernock Park Plants "Kernock Plants"; exact matching drops it (two names). Wrong jurisdiction or scope: Doc 1's witness list shows Defra testifying later; checking only these hearings' panels keeps Defra (four names). The gold matches the short name and tests witnesses inquiry-wide.
```

(48 / 50 words.)
