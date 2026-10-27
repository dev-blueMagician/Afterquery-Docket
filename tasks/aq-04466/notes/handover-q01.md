# aq-04466 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04466 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target hard, origin claude.
- tested_sha256 a1d9fbf12724dffe96dbe923b8dea1b8295db951b476d49cdcfb36702e872a63: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 2, D14 = Doc 15.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which submitters, if any, back a proposal from CAMAC's 2014 discussion paper while naming CAMAC as its source? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
Allens, Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association)
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Allens' answer on compliance plans): Allens sets out the three reform options in CAMAC's 2014 discussion paper and says "We would support adopting Option 3 proposed in the 2014 CAMAC Discussion Paper", the option that subsumes compliance into risk management with no compliance plan. Allens backs a proposal from that paper and names CAMAC as its source (component c1).

Step 2. Source input (Doc 2, Allens' answer on the definition of liquid assets): Allens says the consultation paper "also refers to the 2014 CAMAC Discussion Paper", in which "CAMAC suggested" a more objective test of liquidity: an asset that can reasonably be expected to be realised for its book value within seven business days. Allens argues against that test.

Step 3. Source input (Doc 15, the Joint Associations' answer on the definition of liquid assets): the Joint Associations recommend that "the objective test of liquidity as suggested by the Corporations and Markets Authority Committee (CAMAC) should be adopted": liquid assets are money, bank accepted bills and assets that can reasonably be expected to be realised for their book value within seven business days. They name CAMAC as the source and give no year.

Step 4. Combination (Doc 2 and Doc 15): the test the Joint Associations back is the one Allens places in CAMAC's 2014 discussion paper (the same objective test, realisation at book value within seven business days). So the Joint Associations also back a proposal from that paper and name CAMAC as its source (component c2).

Step 5. Exclusions, from the other submissions that cite CAMAC: AIMA and AIOFP back recommendations of a different CAMAC publication, its earlier report on managed investment schemes. AIMA's own proposal to reconsider compliance plans resembles Option 3 but names no CAMAC source. Allens' agreement with a recommendation of that earlier report on limited liability does not count; its endorsement from the discussion paper is Option 3.

Decoy: ASCF quotes the same seven-business-day test as "the CAMAC suggestion" but opposes it, so it names CAMAC without backing the proposal.

Final answer, in alphabetical order (Doc 2 and Doc 15): Allens, Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association).
```

### Answer components

Component 1

```text
Allens
```

Component 2

```text
Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association)
```

### Evidence

Evidence 1: document Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), proves component 1. Allens (local note: answer 10, l483; Doc 2)

```text
We would support adopting Option 3 proposed in the 2014 CAMAC Discussion Paper
```

Evidence 2: document Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), proves component 1. Allens (local note: answer 10, l474; Doc 2)

```text
subsume compliance into risk management (no requirement for a compliance plan
```

Evidence 3: document Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), proves component 2. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: answer 17, l631; Doc 2)

```text
The Consultation Paper also refers to the 2014 CAMAC Discussion Paper
```

Evidence 4: document Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), proves component 2. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: answer 17, l631; Doc 2)

```text
CAMAC suggested it may be useful to introduce a clearer or more objective test for liquidity (such as an asset that can reasonably be expected to be realised for its book value within 7 business days)
```

Evidence 5: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 2. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: answer 17, l237; Doc 15)

```text
The Joint Associations recommend that the objective test of liquidity as suggested by the Corporations and Markets Authority Committee (CAMAC) should be adopted
```

Evidence 6: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 2. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: answer 17, l239; Doc 15)

```text
liquid assets as money, bank accepted bills and assets that can reasonably be expected to be realised for their book value within 7 business days
```

Evidence 7: document Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), proves component 2. Joint Associations (CA ANZ, CPA Australia, IPA, SMSF Association) (local note: opening paragraph, l10; Doc 15)

```text
Chartered Accountants Australia & New Zealand (CA ANZ), CPA Australia, the Institute of Public Accountants and the SMSF Association (the Joint Associations)
```

### Necessary documents

- Tick Doc 2 (autreas_managed_investment_schemes_c2023_404702_allens.txt), role: Answer component
- Tick Doc 15 (autreas_managed_investment_schemes_c2023_404702_caanz_cpa_ipa_smsfa.txt), role: Answer component

Leave unticked: Doc 1 (autreas_managed_investment_schemes_c2023_404702_cp_ventures_and_saltwater_fund.txt), Doc 3 (autreas_managed_investment_schemes_c2023_404702_aima.txt), Doc 4 (autreas_managed_investment_schemes_c2023_404702_angas_securities_ltd.txt), Doc 5 (autreas_managed_investment_schemes_c2023_404702_angel_loop.txt), Doc 6 (autreas_managed_investment_schemes_c2023_404702_archangel_ventures.txt), Doc 7 (autreas_managed_investment_schemes_c2023_404702_arnold_bloch_leibler_and_euphem.txt), Doc 8 (autreas_managed_investment_schemes_c2023_404702_aiofp.txt), Doc 9 (autreas_managed_investment_schemes_c2023_404702_aussie_angels.txt), Doc 10 (autreas_managed_investment_schemes_c2023_404702_afca.txt), Doc 11 (autreas_managed_investment_schemes_c2023_404702_ascf.txt), Doc 12 (autreas_managed_investment_schemes_c2023_404702_bell_potter.txt), Doc 13 (autreas_managed_investment_schemes_c2023_404702_boardroom.txt), Doc 14 (autreas_managed_investment_schemes_c2023_404702_brisbane_angels.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter, Entity resolution

Leave unticked: Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 15 adopts CAMAC's seven-business-day liquidity test without saying which CAMAC paper proposed it; only Doc 2's liquid-assets answer places it in the 2014 discussion paper. Counting only explicit 2014 citations gives Allens alone and misses the Joint Associations.
```

(42 / 50 words.)
