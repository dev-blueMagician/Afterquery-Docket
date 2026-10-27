# aq-docket-trial-06 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-docket-trial-06 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 41de64e9233b6f77a521d83e04222edfdfe9e3571323784a74d84e31be1a6ed1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D02 = Doc 2, D05 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How many more credit unions did the United States have at the end of 2002 than it had banks on September 30, 2005?
```

### Number of asks

1 ask

### Gold answer

```text
2,361 more credit unions
```

### Step-by-step reasoning

```text
1. Doc 2: as of December 2002, 9,688 credit unions were federally insured, and 214 state-chartered credit unions lacked federal deposit insurance (212 privately insured plus two uninsured ones, in Idaho and New Hampshire). Federally chartered credit unions must be federally insured, so these two groups are all credit unions: 9,688 + 214 = 9,902 credit unions.
2. Doc 5: as of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks: 1,846 + 5,695 = 7,541 banks.
3. Doc 2 and Doc 5: 9,902 - 7,541 = 2,361 more credit unions than banks.
4. Wrong routes: counting only the federally insured credit unions, or adding only the privately insured ones and leaving out the two uninsured credit unions named in a footnote, gives a smaller difference; counting one bank charter type gives a larger one.
```

### Answer components

Component 1

```text
2,361
```

### Evidence

Evidence 1: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 2,361 (local note: Background, text line 231)

```text
As of December 2002, 9,688 credit unions were federally insured
```

Evidence 2: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 2,361 (local note: Background, text line 231)

```text
credit unions that are federally chartered must be federally insured
```

Evidence 3: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 2,361 (local note: Background, text line 233)

```text
As of December 2002, 212 credit unions
```

Evidence 4: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 2,361 (local note: footnote 8, text line 239)

```text
we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire
```

Evidence 5: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 2,361 (local note: Appendix I footnote 2, text line 1179)

```text
As of December 2002, 214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured
```

Evidence 6: document Doc 5 (gaoreports_gao_06_387.txt), proves component 1. 2,361 (local note: Background, text line 191)

```text
As of September 30, 2005, there were 1,846 federally chartered banks and 5,695 state-chartered banks
```

### Necessary documents

- Tick Doc 2 (gaoreports_gao_03_971.txt), role: Answer component
- Tick Doc 5 (gaoreports_gao_06_387.txt), role: Answer component

Leave unticked: Doc 1 (gaoreports_gao_01_819t.txt), Doc 3 (gaoreports_gao_04_412t.txt), Doc 4 (gaoreports_gao_04_684.txt), Doc 6 (gaoreports_gao_08_148r.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 2's background gives two insured groups of credit unions as December 2002 counts: "As of December 2002, 9,688 credit unions were federally insured" and, two sentences later, "As of December 2002, 212 credit unions" about 2 percent of all credit unions "chose to purchase private deposit insurance". The two credit unions with no deposit insurance at all appear only in footnote 8 ("we identified two uninsured credit unions, one was located in Idaho and the other was located in New Hampshire") and in Appendix I ("214 state- chartered credit unions lacked federal deposit insurance, and all but two were privately insured"). Nothing in the question points at uninsured credit unions.
```

The wrong answer a careless solver gives:

```text
2,359 more credit unions. The solver adds the two printed insured groups as if together they were every U.S. credit union, 9,688 + 212 = 9,900, takes the banks from Doc 5 (1,846 federally chartered plus 5,695 state-chartered = 7,541), and subtracts: 9,900 - 7,541 = 2,359.
```

Why the correct answer avoids it:

```text
Doc 2 says federally chartered credit unions must be federally insured, so every credit union outside the 9,688 is state-chartered, and Appendix I counts 214 state-chartered credit unions without federal deposit insurance in December 2002, all but two of them privately insured; footnote 8 names the two uninsured ones in Idaho and New Hampshire. All U.S. credit unions were therefore 9,688 + 214 = 9,902, and 9,902 - 7,541 = 2,361.
```

(229 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 2's background prints the largest credit-union figure in the bundle, "As of December 2002, 9,688 credit unions were federally insured, with about 81 million members and $483 billion in deposits", right after "Almost all (98 percent) credit unions are federally insured". The task page's overview for Doc 2 also lists "9,688 federally insured credit unions as of December 2002" among its key figures. It reads like the national credit-union count, but it covers only the federally insured credit unions.
```

The wrong answer a careless solver gives:

```text
2,147 more credit unions. The solver takes 9,688 as the number of U.S. credit unions and subtracts Doc 5's 7,541 banks: 9,688 - 7,541 = 2,147. A solver who instead scales up the rounded 98 percent share gets 9,688 / 0.98 = 9,886 credit unions and 2,345.
```

Why the correct answer avoids it:

```text
The question asks how many credit unions the United States had, not how many were federally insured. The same background goes on to count the 212 privately insured credit unions, "about 2 percent of all credit unions", and Appendix I adds the two with no deposit insurance, 214 credit unions lacking federal insurance in all. So 9,688 + 214 = 9,902 credit unions, and the difference from the 7,541 banks is 2,361.
```

(199 words across the three boxes; the form needs at least 150.)
