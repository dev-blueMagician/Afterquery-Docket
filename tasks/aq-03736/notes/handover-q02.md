# aq-03736 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03736 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 0316bb7a9a5901a3a0fabd63827c44413a834975d197764694150847b0af5126: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D02 = Doc 3.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which guidance, if any, does the adopted due diligence directive require the Commission to issue where the articles of the Commission's original proposal had merely allowed it to? List the items in any order.
```

### Number of asks

1 ask

### Gold answer

```text
Guidelines on fulfilling due diligence obligations, guidance on the fitness of industry or multi-stakeholder initiatives
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, article headed "Guidelines"): to support companies and Member State authorities on how companies should fulfil their due diligence obligations, the Commission "shall issue guidelines". This is a duty.
Step 2. Source input (Doc 3, article headed "Accompanying measures"): the Commission "shall issue guidance setting out fitness criteria and a methodology for companies to assess the fitness of industry and multi-stakeholder initiatives". The next paragraph requires the same for "the fitness of third-party verifiers", with guidance on monitoring their verification. All of these are duties.
Step 3. Source input (Doc 3, article headed "Model contractual clauses"): the Commission "shall adopt guidance about voluntary model contractual clauses". Also a duty. Steps 1 to 3 are all the guidance the adopted directive's articles require the Commission to issue.
Step 4. Source input (Doc 1, article headed "Guidelines"): in the proposal the Commission "may issue guidelines, including for specific sectors or specific adverse impacts". That was a permission, so the guidelines qualify (first component).
Step 5. Source input (Doc 1, article headed "Accompanying measures"): the Commission "may issue guidance for assessing the fitness of industry schemes and multi-stakeholder initiatives". That was a permission too, so this guidance qualifies (second component). The proposal's articles say nothing about guidance on third-party verifiers, so that guidance was not something the proposal had allowed and it does not qualify.
Step 6. Source input (Doc 1, article headed "Model contractual clauses"): the proposal already said the Commission "shall adopt guidance about voluntary model contract clauses". It was a duty from the start, so it does not qualify.
Decoy: the guidance on third-party verifiers sits in a sentence that mirrors the one on industry and multi-stakeholder initiatives, but the proposal has no such sentence. The guidance on model contractual clauses is required in both texts.
Step 7. Final answer (Doc 1 and Doc 3): two items moved from a permission in the proposal's articles to a duty in the adopted directive: the guidelines on fulfilling due diligence obligations, and the guidance on the fitness of industry or multi-stakeholder initiatives.
```

### Answer components

Component 1

```text
Guidelines on fulfilling due diligence obligations
```

Component 2

```text
guidance on the fitness of industry or multi-stakeholder initiatives
```

### Evidence

Evidence 1: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 1. Guidelines on fulfilling due diligence obligations (local note: Article 19(1), L677)

```text
shall issue guidelines, including general guidelines and sector-specific guidelines or guidelines for specific adverse impacts
```

Evidence 2: document Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), proves component 1. Guidelines on fulfilling due diligence obligations (local note: Article 13, L835)

```text
may issue guidelines, including for specific sectors or specific adverse impacts
```

Evidence 3: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 2. guidance on the fitness of industry or multi-stakeholder initiatives (local note: Article 20(4), L719)

```text
The Commission, in collaboration with Member States, shall issue guidance setting out fitness criteria and a methodology for companies to assess the fitness of industry and multi-stakeholder initiatives.
```

Evidence 4: document Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), proves component 2. guidance on the fitness of industry or multi-stakeholder initiatives (local note: Article 14(4), L847)

```text
The Commission, in collaboration with Member States, may issue guidance for assessing the fitness of industry schemes and multi-stakeholder initiatives.
```

Evidence 5: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 2. guidance on the fitness of industry or multi-stakeholder initiatives (local note: Article 20(5), L723)

```text
shall issue guidance setting out fitness criteria and a methodology for companies to assess the fitness of third-party verifiers
```

Evidence 6: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 1. Guidelines on fulfilling due diligence obligations (local note: Article 18, L671)

```text
shall adopt guidance about voluntary model contractual clauses
```

Evidence 7: document Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), proves component 1. Guidelines on fulfilling due diligence obligations (local note: Article 12, L829)

```text
the Commission shall adopt guidance about voluntary model contract clauses
```

### Necessary documents

- Tick Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), role: Answer component
- Tick Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), role: Answer component

Leave unticked: Doc 2 (swd-2022-43-executive-summary-of-the-impact-assessment-report-accompanying-the-csdd-proposal.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter

Leave unticked: Temporal alignment, Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 3's Accompanying measures article requires fitness guidance twice, for initiatives and for third-party verifiers; Doc 1 allows only the first. Listing Doc 3's guidance duties unchecked adds verifiers and model clauses, four items. Matching each to Doc 1's wording leaves the two.
```

(46 / 50 words.)
