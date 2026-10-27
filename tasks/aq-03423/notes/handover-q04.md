# aq-03423 q04 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03423 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 7946e5eb80bb16d278946b7d4d59592e42b42320791b2a13e24674a259a76fd7: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D08 = Doc 7, D11 = Doc 10.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Judging by all the submissions to the Commerce Commission's mobile market study together, which of the organisations that made them, if any, had become an MVNO or had tried to? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
Trustpower, Vocus, WISPA NZ
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, 2degrees on Vocus): 2degrees notes that Vocus has a mobile offer and that Vocus says the network operators constrain it. Vocus sells mobile service over another operator's network, so it has become an MVNO. Vocus's own submissions and the issues paper say the same and are not needed for this.

Step 2. Source input (Doc 10, WISPA NZ): WISPA NZ says its members would dearly like to offer an MVNO service and that WISPA has requested negotiations to establish an MVNO from the two largest network operators, without progress. It tried.

Step 3. Source input (Doc 7, 2degrees on Trustpower): Trustpower's own submission, a consultant's report, does not say that Trustpower is seeking an MVNO. 2degrees reports that Trustpower holds a competing MVNO offer from Spark, is considering whether to launch an MVNO with 2degrees or Spark, and that 2degrees has invested in the opportunity. Trustpower was trying to become an MVNO, and only another submitter reports it.

Step 4. Decoy: 2degrees writes about MVNOs more than any other submitter and hosts the largest one, but it is a network operator, like Spark and Vodafone, so it has not become an MVNO or tried to. Chorus, New Street Research, Bluereach and Speedchecker report no MVNO of their own and no attempt at one, and no other submitter reports one for them. Bluereach is building its own network and asks for roaming. Warehouse Mobile, Compass and Kogan are MVNOs named in the papers, but none of them made a submission.

Step 5. Answer, alphabetically: Trustpower, Vocus, WISPA NZ.
```

### Answer components

Component 1

```text
Trustpower
```

Component 2

```text
Vocus
```

Component 3

```text
WISPA NZ
```

### Evidence

Evidence 1: document Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), proves component 1. Trustpower (local note: answer on Q12, L468)

```text
We understand Trustpower has also received a competing MVNO offer from Spark.
```

Evidence 2: document Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), proves component 1. Trustpower (local note: answer on Q12, L468)

```text
2degrees understands Trustpower is considering whether it will launch an MVNO with 2degrees or Spark
```

Evidence 3: document Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), proves component 2. Vocus (local note: answer on Q20, L597)

```text
Vocus claims its mobile offer is constrained by MNOs
```

Evidence 4: document Doc 10 (nzcc_mobile_r1_issues_wispa_nz_submission_on_the_issues_paper_26_octob.txt), proves component 3. WISPA NZ (local note: answer on Q4, L34)

```text
WISPs would dearly like to be able to offer a MVNO service.
```

Evidence 5: document Doc 10 (nzcc_mobile_r1_issues_wispa_nz_submission_on_the_issues_paper_26_octob.txt), proves component 3. WISPA NZ (local note: answer on Q14, L39)

```text
WISPA has requested negotiations to establish a MVNO from the two largest MNOs.
```

### Necessary documents

- Tick Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), role: Answer component
- Tick Doc 10 (nzcc_mobile_r1_issues_wispa_nz_submission_on_the_issues_paper_26_octob.txt), role: Answer component

Leave unticked: Doc 1 (nzcc_mobile_r1_issues_study_of_mobile_telecommunications_markets_in_ne.txt), Doc 2 (nzcc_mobile_r1_issues_chorus_submission_on_terms_of_reference_30_novem.txt), Doc 3 (nzcc_mobile_r1_issues_new_street_research_submission_on_terms_of_refer.txt), Doc 4 (nzcc_mobile_r1_issues_vocus_submission_on_terms_of_reference_30_novemb.txt), Doc 5 (nzcc_mobile_r1_issues_trustpower_analysys_mason_submission_on_terms_of.txt), Doc 6 (nzcc_mobile_r1_issues_bluereach_submission_on_terms_of_reference_6_dec.txt), Doc 8 (nzcc_mobile_r1_issues_two_degrees_covec_mobile_market_development_in_n.txt), Doc 9 (nzcc_mobile_r1_issues_vocus_submission_on_the_issues_paper_26_october_.txt), Doc 11 (nzcc_mobile_r1_issues_speedchecker_ltd_submission_on_the_issues_paper_.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Linking across documents: Trustpower's own submission is silent; only Doc 7's answer on wholesale competition reports its MVNO offers, so reading each submitter's own paper gives Vocus, WISPA NZ. Wrong scope: Doc 1's table of MVNOs adds Compass and Warehouse Mobile, which made no submission. Gold: Trustpower, Vocus, WISPA NZ.
```

(50 / 50 words.)
