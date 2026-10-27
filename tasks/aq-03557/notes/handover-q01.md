# aq-03557 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03557 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin user+claude.
- tested_sha256 114f324f94a54e12d54cca42851d4d249f827dc0d4f5408a4b32b75b972080dd: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 3, D09 = Doc 7.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin user+claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
With the number of stores Woolworths provides, how many supermarkets trade under banners that any retailer's submission says have no loyalty programme?
```

### Number of asks

1 ask

### Gold answer

```text
376 supermarkets
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, answer on loyalty programmes): Woolworths says Foodstuffs' PAK'nSAVE and Four Square banners do not offer loyalty programmes, and that SuperValue stores have no banner-wide programme. It says the same of Chemist Warehouse, but it describes that chain as a pharmacy retailer, not a supermarket, so Chemist Warehouse stores are left out.

Step 2. Source input (Doc 3, answer on loyalty programmes): Foodstuffs South Island says PAK'nSAVE has no loyalty scheme, that Four Square and Raeward Fresh do not operate loyalty schemes, and that by its understanding FreshChoice and SuperValue do not either. Taking both submissions, the supermarket banners said to have no programme are PAK'nSAVE, Four Square, SuperValue, FreshChoice and Raeward Fresh.

Step 3. Source input (Doc 7, executive summary): Woolworths counts 56 PAK'nSAVE supermarkets and 245 Four Square supermarkets. It gives SuperValue and FreshChoice together as 71 supermarkets.

Step 4. Source input (Doc 7, list of other supermarkets): Raeward Fresh is listed with four retail stores, written as a word. That is 4 stores.

Step 5. Calculation (Doc 3 and Doc 7): 56 + 245 = 301 for PAK'nSAVE and Four Square.

Step 6. Calculation (Doc 3 and Doc 7): 301 + 71 = 372 with SuperValue and FreshChoice. The 71 is added whole because Doc 3 says neither of those banners runs a scheme.

Step 7. Calculation (Doc 3 and Doc 7): 372 + 4 = 376 supermarkets with Raeward Fresh. This is the answer.
```

### Answer components

Component 1

```text
376 supermarkets
```

### Evidence

Evidence 1: document Doc 7 (nzcc_grocery_r1_issues_woolworths_new_zealand_submission_on_retail_groc.txt), proves component 1. 376 supermarkets (local note: executive summary, L31)

```text
56 PAK’nSAVE, 138 New World, and 245 Four Square individually owner-operated supermarkets
```

Evidence 2: document Doc 7 (nzcc_grocery_r1_issues_woolworths_new_zealand_submission_on_retail_groc.txt), proves component 1. 376 supermarkets (local note: executive summary, L20)

```text
We are also the franchisor for 71 SuperValue and FreshChoice supermarkets
```

Evidence 3: document Doc 7 (nzcc_grocery_r1_issues_woolworths_new_zealand_submission_on_retail_groc.txt), proves component 1. 376 supermarkets (local note: other supermarkets, L284)

```text
Raeward Fresh (with four retail stores across Christchurch, Nelson, and Queenstown)
```

Evidence 4: document Doc 7 (nzcc_grocery_r1_issues_woolworths_new_zealand_submission_on_retail_groc.txt), proves component 1. 376 supermarkets (local note: answer on loyalty programmes, L1435)

```text
Four Square banners do not offer loyalty programmes, nor does Chemist Warehouse
```

Evidence 5: document Doc 7 (nzcc_grocery_r1_issues_woolworths_new_zealand_submission_on_retail_groc.txt), proves component 1. 376 supermarkets (local note: answer on loyalty programmes, L1437)

```text
There are not any banner-wide loyalty programmes at SuperValue stores
```

Evidence 6: document Doc 3 (nzcc_grocery_r1_issues_foodstuffs_south_island_submission_on_retail_gro.txt), proves component 1. 376 supermarkets (local note: answer on loyalty programmes, L558)

```text
Four Square and Raeward Fresh also do not operate loyalty schemes.
```

Evidence 7: document Doc 3 (nzcc_grocery_r1_issues_foodstuffs_south_island_submission_on_retail_gro.txt), proves component 1. 376 supermarkets (local note: answer on loyalty programmes, L559)

```text
It is our understanding that FreshChoice and SuperValue do not operate loyalty schemes.
```

### Necessary documents

- Tick Doc 7 (nzcc_grocery_r1_issues_woolworths_new_zealand_submission_on_retail_groc.txt), role: Answer component
- Tick Doc 3 (nzcc_grocery_r1_issues_foodstuffs_south_island_submission_on_retail_gro.txt), role: Answer component

Leave unticked: Doc 1 (nzcc_grocery_r1_issues_consumer_nz_submission_on_retail_grocery_market_.txt), Doc 2 (nzcc_grocery_r1_issues_foodstuffs_north_island_submission_on_retail_gro.txt), Doc 4 (nzcc_grocery_r1_issues_t_and_g_fresh_submission_on_retail_grocery_marke.txt), Doc 5 (nzcc_grocery_r1_issues_the_warehouse_group_submission_on_retail_grocery.txt), Doc 6 (nzcc_grocery_r1_issues_united_fresh_submission_on_retail_grocery_market.txt), Doc 8 (nzcc_grocery_r1_issues_woolworths_new_zealand_limited_submission_on_ret.txt), Doc 9 (nzcc_grocery_r1_issues_foodstuffs_north_island_comments_on_submissions_.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Wrong kind of entity

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Linking across documents: Raeward Fresh's lack of a scheme is only in Doc 3, its four stores only in Doc 7; omitting it gives 372. Wrong kind of entity: Doc 7 also names Chemist Warehouse, a pharmacy chain with 16 stores; adding it gives 392. Gold: 376.
```

(47 / 50 words.)
