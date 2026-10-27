# aq-03423 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03423 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 5f25fda0ea48e13730bd649900b696638691b6e3c36adbbca5c1f49f0961e64b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D07 = Doc 8, D08 = Doc 7.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 8 doesn't mention 75. Doc 8 prints it first at character 38,707, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On the Commerce Commission's December 2017 monitoring figures, what share of the fixed broadband market, to the nearest percent, did New Zealand's two largest mobile network operators hold together?
```

### Number of asks

1 ask

### Gold answer

```text
71%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 8, product bundling section): Covec reads the Commerce Commission's most recent monitoring report, its Key Facts edition of December 2017, as showing that the three mobile network operators collectively have 75 per cent of the fixed broadband market.

Step 2. Source input (Doc 8, roaming regulation section): the three operators are Spark, Vodafone and 2degrees, and 2degrees is well behind Spark and Vodafone in subscriber shares. The two largest operators are therefore Spark and Vodafone, and the collective figure also holds the share of the third operator, 2degrees.

Step 3. Source input (Doc 7, footnote to its answer on bundling): on the Commission's annual monitoring report of the same December date, 2degrees' own share of broadband connections was 4 per cent.

Step 4. Calculation (Doc 8 and Doc 7): the two largest operators' share is the three-operator figure less the third operator's share: 75 − 4 = 71. Spark and Vodafone together held that percentage of the fixed broadband market.

Step 5. Check on the printed look-alike (Doc 2): Chorus says the two largest mobile network owners account for 80 per cent of the retail broadband market. Chorus wrote on 30 November 2017, before the December report existed, and gives no source for the figure, so it is not the Commission's December figure and is not used.
```

### Answer components

Component 1

```text
71%
```

### Evidence

Evidence 1: document Doc 8 (nzcc_mobile_r1_issues_two_degrees_covec_mobile_market_development_in_n.txt), proves component 1. 71% (local note: para 81, L307)

```text
the three MNOs collectively have 75% of the fixed broadband market
```

Evidence 2: document Doc 8 (nzcc_mobile_r1_issues_two_degrees_covec_mobile_market_development_in_n.txt), proves component 1. 71% (local note: footnote 14, L316)

```text
Annual Telecommunications Monitoring Report: Key Facts, 20 December 2017
```

Evidence 3: document Doc 8 (nzcc_mobile_r1_issues_two_degrees_covec_mobile_market_development_in_n.txt), proves component 1. 71% (local note: para 48, L211)

```text
2degrees is well behind Spark (incl Skinny) and Vodafone in total subscriber shares
```

Evidence 4: document Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), proves component 1. 71% (local note: footnote 7, L320)

```text
estimated broadband retailer market share by connections was 13% versus 4% for 2degrees: Commerce Commission, 2017 Annual Telecommunications Monitoring Report, 20 December 2017
```

### Necessary documents

- Tick Doc 8 (nzcc_mobile_r1_issues_two_degrees_covec_mobile_market_development_in_n.txt), role: Answer component
- Tick Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), role: Answer component

Leave unticked: Doc 1 (nzcc_mobile_r1_issues_study_of_mobile_telecommunications_markets_in_ne.txt), Doc 2 (nzcc_mobile_r1_issues_chorus_submission_on_terms_of_reference_30_novem.txt), Doc 3 (nzcc_mobile_r1_issues_new_street_research_submission_on_terms_of_refer.txt), Doc 4 (nzcc_mobile_r1_issues_vocus_submission_on_terms_of_reference_30_novemb.txt), Doc 5 (nzcc_mobile_r1_issues_trustpower_analysys_mason_submission_on_terms_of.txt), Doc 6 (nzcc_mobile_r1_issues_bluereach_submission_on_terms_of_reference_6_dec.txt), Doc 9 (nzcc_mobile_r1_issues_vocus_submission_on_the_issues_paper_26_october_.txt), Doc 10 (nzcc_mobile_r1_issues_wispa_nz_submission_on_the_issues_paper_26_octob.txt), Doc 11 (nzcc_mobile_r1_issues_speedchecker_ltd_submission_on_the_issues_paper_.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 8's 75% is all three operators' fixed broadband share; taking it for the two largest gives 75%. Wrong edition: Doc 2's 80%, written 30 November 2017, predates the December report. The gold removes 2degrees' 4% (Doc 7) from 75%: 71%.
```

(44 / 50 words.)
