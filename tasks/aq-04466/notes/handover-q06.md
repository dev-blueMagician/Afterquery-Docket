# aq-04466 q06 hand-over

Generated 2026-10-15 by `python tools/check_questions.py tasks/aq-04466 --handover --q q06` from questions/q06.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 d1c5580e0e05e0b8b8cf1f92a50f4a20dab0021ba3ffe1af437bb3544dc9a42e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 3, D06 = Doc 5.
- Floor: 0 FAIL, 2 WARN.
  - WARN strong-screen: the strong solver was right in every fresh solve of this exact sentence: likely Too easy at High. Say so with the hand-over; the user decides whether to run it. Never reword or re-screen the sentence to find a miss
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q06.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which submitters, if any, say that firms shy away from classing investors as wholesale clients on the strength of the investors' experience because of the risk to themselves? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
AIMA, Angel Loop
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, AIMA's answer on consent requirements): AIMA describes the sophisticated investor test as requiring engagement between the licensee and the client "in relation to that client's financial products/services experience", so it is the route that classes investors on their experience. AIMA then observes that "some product issuers are reluctant to rely on the sophisticated investor test because of the compliance risk associated with the subjectivity of the assessment criteria": issuers shy away from it because of a risk to themselves. AIMA qualifies (component c1).

Step 2. Source input (Doc 5, Angel Loop's answer on the thresholds): Angel Loop says the test's subjective nature "creates less certainty for AFS Licensees to know whether to accept retail investors based on experience", and that "from experience many AFS Licensees 'would not risk their license' or showed concerns with their ability to obtain insurance". Licensees shy away because of the risk to their own licence and insurance. Angel Loop qualifies (component c2).

Decoy: the Joint Associations describe the risk to accountants who sign certificates of an investor's wealth, not firms avoiding classification on experience, and they report growing use of the wholesale and sophisticated investor regimes. Archangel says there is no clear option for experienced investors but gives no risk to firms as the reason; Arnold Bloch Leibler and Euphemia call the test a reasonable basis; Aussie Angels ask for an education pathway that licensees would accept, without saying why they hold back now; Bell Potter describes its own experience certificate in use. None qualifies.

Final answer, alphabetically (Doc 3 and Doc 5): AIMA, Angel Loop.
```

### Answer components

Component 1

```text
AIMA
```

Component 2

```text
Angel Loop
```

### Evidence

Evidence 1: document Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), proves component 1. AIMA (local note: answer on consent requirements; Doc 3)

```text
in relation to that client’s financial products/services experience
```

Evidence 2: document Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), proves component 1. AIMA (local note: same answer; Doc 3)

```text
Anecdotally, AIMA observes that some product issuers are reluctant to rely on the sophisticated investor test because of the compliance risk associated with the subjectivity of the assessment criteria.
```

Evidence 3: document Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), proves component 2. Angel Loop (local note: answer on the thresholds; Doc 5)

```text
creates less certainty for AFS Licensees to know whether to accept retail investors based on experience
```

Evidence 4: document Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), proves component 2. Angel Loop (local note: same passage; Doc 5)

```text
from experience many AFS Licensees “would not risk their license” or showed concerns with their ability to obtain insurance
```

### Necessary documents

- Tick Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), role: Answer component
- Tick Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), role: Answer component

Leave unticked: Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), Doc 4 (autreas_managed_investment_schemes_c2023_404702_angas_securities_ltd.txt), Doc 6 (autreas_managed_investment_schemes_c2023_404702_archangel_ventures.txt), Doc 7 (autreas_managed_investment_schemes_c2023_404702_arnold_bloch_leibler_and_euphem.txt), Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), Doc 9 (autreas_managed_investment_schemes_c2023_404702_aussie_angels.txt), Doc 10 (autreas_managed_investment_schemes_c2023_404702_afca.txt), Doc 11 (autreas_managed_investment_schemes_c2023_404702_ascf.txt), Doc 12 (autreas_managed_investment_schemes_c2023_404702_bell_potter.txt), Doc 13 (autreas_managed_investment_schemes_c2023_404702_boardroom.txt), Doc 14 (autreas_managed_investment_schemes_c2023_404702_brisbane_angels.txt), Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Document convention: Doc 3 calls the experience-based route "the sophisticated investor test" and ties it to the client's "financial products/services experience" in the same answer. Matching only the word "experience" gives Angel Loop alone; the gold adds AIMA, whose issuers avoid that test for "compliance risk".
```

(46 / 50 words.)
