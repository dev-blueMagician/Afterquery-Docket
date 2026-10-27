# aq-04466 q04 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04466 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 6dd69215aea64a98ab5b82f09420f621f3098b4b797b91c9de056b70a5a8529e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 8, D06 = Doc 5, D14 = Doc 15.
- Floor: 0 FAIL, 2 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which submitters, if any, rely on Treasury's earlier options paper on wholesale and retail clients? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
AIOFP, Angel Loop, Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association)
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 15, the Joint Associations' answer on the product value test, with its footnote 3): the Joint Associations cite the "Wholesale and Retail Clients Future of Financial Advice Options Paper, January 2011, p.5" for the finding that "the level of $500,000 was considered a low level", in support of raising the test. They rely on the paper (component c3).

Step 2. Source input (Doc 5, Angel Loop's answer on the thresholds, with its footnote 13): Angel Loop "agrees with Treasury's conclusion on the use of s761GA", quotes it, and cites "Wholesale and Retail Clients Future of Financial Advise 2011", the same paper by title and year. Angel Loop relies on the paper (component c2), and its words show the paper is Treasury's.

Step 3. Source input (Doc 8, the AIOFP's answer on the product value test, read with Doc 15): the AIOFP argues that the threshold should rise from $500,000 to $1,000,000 because "A consultation in 2011 asking this exact question identified that $500,000 was too low". It names no paper, but the year, the question and the finding all match the options paper as the Joint Associations describe it (January 2011; $500,000 "a low level"), and no submission mentions any other 2011 consultation on the threshold. The AIOFP relies on the same paper (component c1).

Decoy: Allens refers to a different Treasury options paper, on product rationalisation, and to the Future of Financial Advice reforms; neither is this paper, so Allens does not count.

Final answer, alphabetically by the names the submissions go by (Doc 8, Doc 5 and Doc 15): AIOFP, Angel Loop, Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association).
```

### Answer components

Component 1

```text
AIOFP
```

Component 2

```text
Angel Loop
```

Component 3

```text
Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association)
```

### Evidence

Evidence 1: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 1. AIOFP (local note: answer on the product value test; Doc 15)

```text
As stated in the Wholesale and Retail Clients Future of Financial Advice Options Paper in 20103 the level of $500,000 was considered a low level
```

Evidence 2: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 3. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: answer on the product value test; Doc 15)

```text
As stated in the Wholesale and Retail Clients Future of Financial Advice Options Paper in 20103 the level of $500,000 was considered a low level
```

Evidence 3: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 1. AIOFP (local note: footnote 3; Doc 15)

```text
Wholesale and Retail Clients Future of Financial Advice Options Paper, January 2011, p.5
```

Evidence 4: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 3. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: footnote 3; Doc 15)

```text
Wholesale and Retail Clients Future of Financial Advice Options Paper, January 2011, p.5
```

Evidence 5: document Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), proves component 2. Angel Loop (local note: answer on the thresholds; Doc 5)

```text
Angel Loop agrees with Treasury’s conclusion on the use of s761GA:
```

Evidence 6: document Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), proves component 2. Angel Loop (local note: footnote 13; Doc 5)

```text
Wholesale and Retail Clients Future of Financial Advise 2011
```

Evidence 7: document Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), proves component 1. AIOFP (local note: answer on the product value test; Doc 8)

```text
The financial product threshold should be increased from $500,000 to $1,000,000
```

Evidence 8: document Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), proves component 1. AIOFP (local note: same answer; Doc 8)

```text
A consultation in 2011 asking this exact question identified that $500,000 was too low
```

### Necessary documents

- Tick Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), role: Answer component
- Tick Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), role: Answer component
- Tick Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), role: Answer component

Leave unticked: Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), Doc 4 (autreas_managed_investment_schemes_c2023_404702_angas_securities_ltd.txt), Doc 6 (autreas_managed_investment_schemes_c2023_404702_archangel_ventures.txt), Doc 7 (autreas_managed_investment_schemes_c2023_404702_arnold_bloch_leibler_and_euphem.txt), Doc 9 (autreas_managed_investment_schemes_c2023_404702_aussie_angels.txt), Doc 10 (autreas_managed_investment_schemes_c2023_404702_afca.txt), Doc 11 (autreas_managed_investment_schemes_c2023_404702_ascf.txt), Doc 12 (autreas_managed_investment_schemes_c2023_404702_bell_potter.txt), Doc 13 (autreas_managed_investment_schemes_c2023_404702_boardroom.txt), Doc 14 (autreas_managed_investment_schemes_c2023_404702_brisbane_angels.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 8 never names the paper; its "consultation in 2011" that found $500,000 too low matches Doc 15's January 2011 options paper. Counting only submitters that name it gives Angel Loop, Joint Associations; the gold adds AIOFP.
```

(40 / 50 words.)
