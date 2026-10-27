# aq-03707 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03707 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin user+claude.
- tested_sha256 f87a8c375913c55af3183756c4b9981fcd072db5a8b1a94039ef5a9d0c504962: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D03 = Doc 11, D08 = Doc 1, D12 = Doc 8.
- Floor: 0 FAIL, 8 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D03: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN form-numbers: Step 1: Doc 1 doesn't mention 12.8%. Doc 1 prints it first at character 22,280, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 1 doesn't mention 13.1%. Doc 1 prints it first at character 22,308, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 8 doesn't mention 77.8%. expected false alarm: Doc 8 prints it at character 95,419, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 5: Docs 8 and 11 don't mention 77.8. expected false alarm: Doc 8 prints it at character 95,419, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
  - WARN precision: the answer is a rate or decimal; state the precision in the question
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin user+claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What margin did the Foodstuffs co-operative with the higher ROACE in the Commission’s final report earn over the years covered by that ROACE, using a measure that Foodstuffs’ profitability consultant considers comparable across companies and that does not make any adjustments for leasing or gearing?
```

### Number of asks

1 ask

### Gold answer

```text
22.2%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, the final report's profitability finding): the return on average capital employed (ROACE), averaged across the same five years for each retailer, is 12.8% for Foodstuffs SI and 13.1% for Foodstuffs NI. Doc 1 names these co-operatives in full as Foodstuffs South Island and Foodstuffs North Island, so Foodstuffs North Island has the higher ROACE.

Step 2. Source input (Doc 11, the summary of its comparison of margins): only the gross profit margin and the EBITDAR margin can be benchmarked across firms without an adjustment for the degree of renting or leverage. The NPAT margin is affected by how a firm is financed and cannot be benchmarked without an adjustment.

Step 3. Source input (Doc 8, the paragraph on exchange rates in its price analysis): cost of goods sold is 77.8% of revenue for FSNI, the abbreviation Doc 8 gives for Foodstuffs North Island, measured on a whole of business basis for the same five years as the ROACE. Doc 8 prints no gross profit margin and no EBITDAR margin for FSNI. The margin it does print for FSNI is an NPAT margin, which Step 2 rules out, and the only gross profit margin it prints belongs to Woolworths NZ. No document gives the figures an EBITDAR margin would need.

Step 4. Source input (Doc 11, the profit and loss rows of Table 1): gross profit is sales less cost of goods sold, so the gross profit margin is the share of revenue left after cost of goods sold.

Step 5. Calculation (Doc 8 and Doc 11): 100 − 77.8 = 22.2

Step 6. Final answer (Doc 1, Doc 8 and Doc 11): the gross profit margin of Foodstuffs North Island over those years was 22.2 per cent of revenue, the only margin of a kind the consultant accepts that the documents give for it.
```

### Answer components

Component 1

```text
22.2%
```

### Evidence

Evidence 1: document Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), proves component 1. 22.2% (local note: profitability finding, l172; Doc 1)

```text
12.8% for Foodstuffs SI and 13.1% for Foodstuffs NI
```

Evidence 2: document Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), proves component 1. 22.2% (local note: profitability finding, l172; Doc 1)

```text
averaged across 2015 to 2019
```

Evidence 3: document Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), proves component 1. 22.2% (local note: industry overview, l83; Doc 1)

```text
Foodstuffs North Island (Foodstuffs NI) and Foodstuffs South Island (Foodstuffs SI)
```

Evidence 4: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 22.2% (local note: para 11, l187; Doc 11)

```text
only the gross profit margin and EBITDAR margin can be benchmarked across firms without having to make an adjustment for the degree of renting or leverage
```

Evidence 5: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 22.2% (local note: para 10e, l185; Doc 11)

```text
margin will be affected by the extent of equity vs. debt / lease finance employed by the firm, and so also cannot be benchmarked across firms unless an adjustment is made
```

Evidence 6: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 22.2% (local note: Table 1, l114; Doc 11)

```text
[3] Cost of goods sold
```

Evidence 7: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 22.2% (local note: Table 1, l115; Doc 11)

```text
[4] Gross Profit
```

Evidence 8: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 22.2% (local note: Table 1, l138; Doc 11)

```text
[25] Gross profit margin (%)
```

Evidence 9: document Doc 8 (nzcc_grocery_r3_postconf_nz_food_and_grocery_council_post_conference_subm.txt), proves component 1. 22.2% (local note: para 4.19, l702; Doc 8)

```text
Cost of Goods Sold: 77.8% for FSNI and 77.6% for FSSI (measured on a WOB basis for the period 2015 to 2019)
```

Evidence 10: document Doc 8 (nzcc_grocery_r3_postconf_nz_food_and_grocery_council_post_conference_subm.txt), proves component 1. 22.2% (local note: footnote 1, l55; Doc 8)

```text
Foodstuffs North Island (FSNI) and Foodstuffs South Island (FSSI)
```

Evidence 11: document Doc 8 (nzcc_grocery_r3_postconf_nz_food_and_grocery_council_post_conference_subm.txt), proves component 1. 22.2% (local note: para 4.17, l690; Doc 8)

```text
FSNI submitted its NPAT margin is 4%
```

Evidence 12: document Doc 8 (nzcc_grocery_r3_postconf_nz_food_and_grocery_council_post_conference_subm.txt), proves component 1. 22.2% (local note: footnote 111, l719; Doc 8)

```text
gross profit margin was 24.4%
```

### Necessary documents

- Tick Doc 8 (nzcc_grocery_r3_postconf_nz_food_and_grocery_council_post_conference_subm.txt), role: Answer component
- Tick Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), role: Used to identify
- Tick Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), role: Exclusion / condition source

  Reviewer note:

```text
Doc 11 says which kinds of margin compare across firms; it rules out Foodstuffs North Island's 4% NPAT margin, which Doc 8 prints whether or not Doc 11 is read.
```

Leave unticked: Doc 2 (nzcc_grocery_r3_postconf_consumer_nz_post_conference_submission_on_market.txt), Doc 3 (nzcc_grocery_r3_postconf_coriolis_ltd_post_conference_submission_on_marke.txt), Doc 4 (nzcc_grocery_r3_postconf_kore_hiakai_zero_hunger_collective_post_conferen.txt), Doc 5 (nzcc_grocery_r3_postconf_monopoly_watch_post_conference_submission_on_mar.txt), Doc 6 (nzcc_grocery_r3_postconf_ngati_porou_holding_company_ltd_post_conference_.txt), Doc 7 (nzcc_grocery_r3_postconf_northelia_post_conference_submission_on_market_s.txt), Doc 9 (nzcc_grocery_r3_postconf_nz_initiative_post_conference_submission_on_mark.txt), Doc 10 (nzcc_grocery_r3_postconf_frugl_post_conference_submission_on_market_study.txt), Doc 12 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi_e77297.txt), Doc 13 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi_446b21.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Look-alike company

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 8's margins paragraph prints Foodstuffs North Island's NPAT margin, 4%, a kind Doc 11's margin summary rules out. Look-alike company: Doc 8's cost-share sentence also gives Foodstuffs South Island's 77.6%, which yields 22.4%. The gold uses the higher-ROACE co-operative's own 77.8%: 22.2%.
```

(45 / 50 words.)
