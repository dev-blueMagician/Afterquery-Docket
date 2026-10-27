# aq-04466 q03 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04466 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 4c34f7f899eccf15e64adb3f75719dd94cc79458468c114a6318f0181c38cdd1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 3, D04 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many years separate the earliest and the latest CAMAC publications that the submissions cite?
```

### Number of asks

1 ask

### Gold answer

```text
14 years
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, AIMA's footnote 5, attached to its answer on statutory limited liability for scheme members): AIMA cites a paper by its web address, "camac_liability_of_members_of_mis_march_2000.pdf", page 7: a CAMAC paper on the liability of scheme members, dated March 2000 by its file name. No submission cites an earlier CAMAC publication.

Step 2. Source input (Doc 2, Allens' table of collapses and reviews, and its answer on compliance plans): Allens lists the "CAMAC Report on Managed Investment Schemes (2012)" and the "CAMAC Discussion Paper on The establishment and operation of MISs (2014)", and backs Option 3 of the 2014 discussion paper. No submission cites a later CAMAC publication; the other citations are to the 2012 report or to CAMAC's undated liquidity suggestion.

Step 3. Calculation (Doc 2 and Doc 3): 2014 - 2000 = 14 years.

Decoy: the folder name in the web address is the date the file was posted, not the paper's date. Without the footnote, the earliest publication named in the text is the 2012 report, which understates the span.

Step 4. Final answer (Doc 3 and Doc 2): 14 years.
```

### Answer components

Component 1

```text
14 years
```

### Evidence

Evidence 1: document Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), proves component 1. 14 years (local note: footnote 5; Doc 3)

```text
https://treasury.gov.au/sites/default/files/2019-12/camac_liability_of_members_of_mis_march_2000.pdf p 7.
```

Evidence 2: document Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), proves component 1. 14 years (local note: table of collapses and reviews; Doc 2)

```text
CAMAC Discussion Paper on The establishment and operation of MISs (2014)
```

Evidence 3: document Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), proves component 1. 14 years (local note: answer on compliance plans; Doc 2)

```text
We would support adopting Option 3 proposed in the 2014 CAMAC Discussion Paper
```

Evidence 4: document Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), proves component 1. 14 years (local note: footnote 6; Doc 3)

```text
CAMAC MIS Report July 2012 p 199.
```

### Necessary documents

- Tick Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), role: Answer component
- Tick Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), role: Answer component

Leave unticked: Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), Doc 4 (autreas_managed_investment_schemes_c2023_404702_angas_securities_ltd.txt), Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), Doc 6 (autreas_managed_investment_schemes_c2023_404702_archangel_ventures.txt), Doc 7 (autreas_managed_investment_schemes_c2023_404702_arnold_bloch_leibler_and_euphem.txt), Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), Doc 9 (autreas_managed_investment_schemes_c2023_404702_aussie_angels.txt), Doc 10 (autreas_managed_investment_schemes_c2023_404702_afca.txt), Doc 11 (autreas_managed_investment_schemes_c2023_404702_ascf.txt), Doc 12 (autreas_managed_investment_schemes_c2023_404702_bell_potter.txt), Doc 13 (autreas_managed_investment_schemes_c2023_404702_boardroom.txt), Doc 14 (autreas_managed_investment_schemes_c2023_404702_brisbane_angels.txt), Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Document convention: Doc 3 cites CAMAC's March 2000 paper only by its web address in footnote 5. A solver reading only named citations takes the 2012 report as the earliest and answers 2 years; the file name dates the paper to 2000, giving 14.
```

(44 / 50 words.)
