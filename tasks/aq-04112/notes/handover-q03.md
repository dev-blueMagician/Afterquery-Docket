# aq-04112 q03 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-04112 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 2b2b333b5ce87532cb894fa853451a85db0c412c1fbd16f35d857aa8f7eb354e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 2, D02 = Doc 3.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN world: 'in any order' drew the form's rule-10 advisory as an answer-protocol tail (aq-03736 q02); give a natural order instead ('alphabetically', 'in date order'), or ask for one value
  - WARN single-passage: one passage of D03 holds the answer: '...arlie dewhirst, senior policy adviser, national pig association q1-67 nick allen, chief executive officer, british meat processors association; james...' (rules 2-3)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Judging by all the evidence the committee heard, which witnesses, if any, put a figure on how long it takes to train a new worker? List them in any order.
```

### Number of asks

1 ask

### Gold answer

```text
Charlie Dewhirst, Nick Allen, Tom Southall
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, the Chair's question to the first panel and Charlie Dewhirst's answer): asked how long it takes to train a good butcher, Charlie Dewhirst of the National Pig Association says it is "around 18 months" from scratch to being up to speed, and about six months to make someone relatively competent. That is a figure for training a new worker, so he is in the list.
Step 2. Source input (Doc 2, Nick Allen of the British Meat Processors Association, at the end of his answer on the Government's recent measures): speaking of bringing British recruits in and training them up, he says "It is 18 months once you are trained", and that it is not a course of three or four months. That is a figure for the same training, so he is in the list.
Step 3. Source input (Doc 3, Tom Southall of the Cold Chain Federation, answering the Chair on short-term relief): he says lorry drivers take between six months and a year to train from scratch. That is a figure too, for another trade, so he is in the list.
Step 4. Left out (Doc 2): Ian Wright also says "18 months", but his "18 months to two years" is how long his members expect labour shortages to last, not how long training takes.
Step 5. Left out (Doc 3): Kate Nicholls speaks of a "two-year hiatus" and a "two-year bridge", which is a break in training, not the time it takes to train a worker.
Step 6. Final answer (Doc 2 and Doc 3): Charlie Dewhirst, Nick Allen, Tom Southall.
```

### Answer components

Component 1

```text
Nick Allen
```

Component 2

```text
Charlie Dewhirst
```

Component 3

```text
Tom Southall
```

### Evidence

Evidence 1: document Doc 2 (ukc_1497_oral_2900.txt), proves component 2. Charlie Dewhirst (local note: Q7, the Chair)

```text
On the training of a butcher for the pig industry, how long does it take to train a good butcher?
```

Evidence 2: document Doc 2 (ukc_1497_oral_2900.txt), proves component 2. Charlie Dewhirst (local note: Q7, Charlie Dewhirst)

```text
Charlie Dewhirst: You will get chapter and verse from Nick Allen in your next session. It is around 18 months, I believe, from scratch to being up to speed. You can make them relatively competent around six months, but it isn’t simple.
```

Evidence 3: document Doc 2 (ukc_1497_oral_2900.txt), proves component 1. Nick Allen (local note: Q73, Nick Allen)

```text
Then we need to start working out whether they want us to employ more British people, and how we bring those people in and train them up. It is 18 months once you are trained; it is not a three or four-month course that you can just pull people off the street and put them through.
```

Evidence 4: document Doc 2 (ukc_1497_oral_2900.txt), proves component 1. Nick Allen (local note: Q74, the next question, naming the speaker just heard)

```text
Q74 Julian Sturdy: Thanks a lot, Nick. Ian, did you want to just briefly come in on that as well?
```

Evidence 5: document Doc 3 (ukc_1497_oral_2977.txt), proves component 3. Tom Southall (local note: Q137, Tom Southall)

```text
Tom Southall: I would agree with that. That short-term relief needs to be for a minimum of one year. It takes time to train people up. As I mentioned, we need to do a thorough review of what we can deliver with a domestic workforce. For example, drivers take six to 12 months to train from scratch on average.
```

Evidence 6: document Doc 2 (ukc_1497_oral_2900.txt), proves component 1. Nick Allen (local note: Q74, Ian Wright, left out)

```text
they are expecting labour shortages to continue for the next 18 months to two years
```

Evidence 7: document Doc 3 (ukc_1497_oral_2977.txt), proves component 3. Tom Southall (local note: Q136, Kate Nicholls, left out)

```text
We have had a two-year hiatus. We need a two-year bridge just to get it right before we can restart
```

### Necessary documents

- Tick Doc 2 (ukc_1497_oral_2900.txt), role: Answer component
- Tick Doc 3 (ukc_1497_oral_2977.txt), role: Answer component

Leave unticked: Doc 1 (ukc_1497_report_9580.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter

Leave unticked: Temporal alignment, Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 2 holds two witnesses on a butcher's training time, Charlie Dewhirst and Nick Allen, and the first points to the second. A solver who stops at that hearing answers with two names. Doc 3's Tom Southall gives a lorry driver's training time: three names.
```

(48 / 50 words.)
