# aq-04466 q05 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-04466 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 8c380edb8fff560b3ba75ac62c121609e29aebc6141850af5fe1eee07346b03d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D10 = Doc 9, D15 = Doc 1.
- Floor: 0 FAIL, 5 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN levers: 'Quiet edit in a re-quoted passage' is not one of the guide's levers (separate them with semicolons)
  - WARN levers: 'Second mention, different words' is not one of the guide's levers (separate them with semicolons)
  - WARN format: say what to answer when nothing qualifies, e.g. 'which ..., if any, ...' (form: answer format stated)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which submitters propose that investors who live outside Australia be able to qualify as wholesale clients by meeting their own country's definition? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
Aussie Angels, CP Ventures, Saltwater Fund
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 9, Aussie Angels' "Other things to consider"): Aussie Angels propose that "non-residents of Australia ought to be considered wholesale clients if they meet their local definitions and certain consent criteria". An investor living abroad would qualify by meeting the definition of their own country, together with consent. Aussie Angels qualify (component c1).

Step 2. Source input (Doc 1, the joint submission of CP Ventures and Saltwater Fund, its list of recommendations): the two funds recommend "Clarification on how to apply foreign investors as sophisticated, ideally as qualifying in their home jurisdiction". In this submission sophisticated investors are the ones wholesale funds are meant for ("restricting MIS funds to sophisticated investors"), so foreign investors would qualify by meeting their home country's test. Both submitters qualify (components c2 and c3).

Decoy: AIMA's general observations contain the passage that Aussie Angels re-quote, but AIMA's condition for non-residents is consent alone ("if they meet certain consent criteria"), with no reference to their own country's definition, so AIMA does not qualify. Aussie Angels' remark that foreign investors are "subject to meeting the thresholds set in Australia" describes the present rules, not a proposal.

Final answer, alphabetically (Doc 9 and Doc 1): Aussie Angels, CP Ventures, Saltwater Fund.
```

### Answer components

Component 1

```text
Aussie Angels
```

Component 2

```text
CP Ventures
```

Component 3

```text
Saltwater Fund
```

### Evidence

Evidence 1: document Doc 9 (autreas_managed_investment_schemes_c2023_404702_aussie_angels.txt), proves component 1. Aussie Angels (local note: Other things to consider; Doc 9)

```text
non-residents of Australia ought to be considered wholesale clients if they meet their local definitions and certain consent criteria
```

Evidence 2: document Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), proves component 2. CP Ventures (local note: We recommend; Doc 1)

```text
Clarification on how to apply foreign investors as sophisticated, ideally as qualifying in their home jurisdiction
```

Evidence 3: document Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), proves component 3. Saltwater Fund (local note: We recommend; Doc 1)

```text
Clarification on how to apply foreign investors as sophisticated, ideally as qualifying in their home jurisdiction
```

Evidence 4: document Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), proves component 3. Saltwater Fund (local note: About CP Ventures and Saltwater Fund; Doc 1)

```text
Both CP Ventures and the Saltwater Fund are wholesale MIS funds
```

Evidence 5: document Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), proves component 2. CP Ventures (local note: on the wholesale tests; Doc 1)

```text
achieve the desired outcome of restricting MIS funds to sophisticated investors
```

### Necessary documents

- Tick Doc 9 (autreas_managed_investment_schemes_c2023_404702_aussie_angels.txt), role: Answer component
- Tick Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), role: Answer component

Leave unticked: Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), Doc 4 (autreas_managed_investment_schemes_c2023_404702_angas_securities_ltd.txt), Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), Doc 6 (autreas_managed_investment_schemes_c2023_404702_archangel_ventures.txt), Doc 7 (autreas_managed_investment_schemes_c2023_404702_arnold_bloch_leibler_and_euphem.txt), Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), Doc 10 (autreas_managed_investment_schemes_c2023_404702_afca.txt), Doc 11 (autreas_managed_investment_schemes_c2023_404702_ascf.txt), Doc 12 (autreas_managed_investment_schemes_c2023_404702_bell_potter.txt), Doc 13 (autreas_managed_investment_schemes_c2023_404702_boardroom.txt), Doc 14 (autreas_managed_investment_schemes_c2023_404702_brisbane_angels.txt), Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 9 re-quotes AIMA's bullet on non-residents but adds "their local definitions"; AIMA's own condition is consent alone. Treating the two copies as one proposal gives AIMA, Aussie Angels, CP Ventures, Saltwater Fund; the gold keeps only submitters tying status to the home country.
```

(47 / 50 words.)
