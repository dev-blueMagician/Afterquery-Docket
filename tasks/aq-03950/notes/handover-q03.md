# aq-03950 q03 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03950 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 864acc277ec1e127bce87277b7ea23abf6aaaa7d75395dcf016081251a13395e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 3, D03 = Doc 4, D05 = Doc 6, D07 = Doc 1.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D01: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which witnesses who gave oral evidence remotely in 2022, if any, had also sent the committee written evidence, personally or through their organisation? List them in any order.
```

### Number of asks

1 ask

### Gold answer

```text
Louise Miles-Payne, Dorothy Yen
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, published written evidence): the report lists the written evidence it received. Five entries are a 2022 witness or the body one spoke for: FSB Wales, Fiona Stewart of the Green Man Festival, UK Theatre, the Welsh Sports Association, and Professor Dorothy Yen with two Brunel colleagues.
Step 2. Source input (Doc 1, witness list): the witnesses for those entries are Gwyneth Sweatman of FSB Wales on 20 April 2022, Fiona Stewart, Louise Miles-Payne ("Director, Creu Cymru and Board Member, UK Theatre") and Matthew Williams of the Welsh Sports Association on 25 May 2022, and Dorothy Yen on 20 July 2022. These five are the only candidates.
Step 3. Source input (Doc 4, Q51): on 25 May 2022 the Chair says the committee is "joined in the Committee room by Matthew Williams", is "also joined by Fiona Stewart", and is "joined virtually by" Graeme Farrow, Camilla King and Louise Miles-Payne. Miles-Payne gave evidence remotely (first component). Williams and Stewart are not among those who joined virtually, so they are left out.
Step 4. Source input (Doc 6, Q143): on 20 July 2022 the Chair says the committee is "joined virtually by" Professor Annette Pritchard and Professor Dorothy Yen. Yen gave evidence remotely (second component). Doc 6's own header lists no written evidence; Doc 1's list shows her paper, and at Q174 Pritchard mentions "her evidence submission".
Step 5. Source input (Doc 3, Q1): on 20 April 2022 the Chair says the panel is "joined by David Chapman" and Gwyneth Sweatman and "joined remotely by Suzy Davies". Sweatman was not remote, so she is left out, although the transcript carries the line "[This evidence was taken by video conference]".
Decoy: Gwyneth Sweatman, Fiona Stewart and Matthew Williams each sent written evidence, personally or through their body, but none of them gave oral evidence remotely. Annette Pritchard joined virtually beside Dorothy Yen but sent no written evidence.
Step 6. Final answer (Doc 1, Doc 4 and Doc 6): Louise Miles-Payne, Dorothy Yen.
```

### Answer components

Component 1

```text
Louise Miles-Payne
```

Component 2

```text
Dorothy Yen
```

### Evidence

Evidence 1: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. Louise Miles-Payne (local note: Published written evidence)

```text
UK Theatre (TOU0011)
```

Evidence 2: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. Louise Miles-Payne (local note: Witnesses, 25 May 2022)

```text
Louise Miles-Payne, Director, Creu Cymru and Board Member, UK Theatre
```

Evidence 3: document Doc 4 (ukc_6476_oral_10335.txt), proves component 1. Louise Miles-Payne (local note: Q51, Chair)

```text
We are joined virtually by Graeme Farrow from the Wales Millennium Centre, by Camilla King from the Llangollen International Musical Eisteddfod, and by Louise Miles-Payne, Director of Creu Cymru and a board member of UK Theatre
```

Evidence 4: document Doc 4 (ukc_6476_oral_10335.txt), proves component 1. Louise Miles-Payne (local note: header)

```text
Written evidence from witnesses:
```

Evidence 5: document Doc 4 (ukc_6476_oral_10335.txt), proves component 1. Louise Miles-Payne (local note: Q51, Chair)

```text
We are joined in the Committee room by Matthew Williams from the Welsh Sports Association. We are also joined by Fiona Stewart from the Green Man Festival.
```

Evidence 6: document Doc 1 (ukc_6476_report_40824.txt), proves component 2. Dorothy Yen (local note: Published written evidence)

```text
Professor Dorothy Yen, Professor in Marketing, Dr Ana Canhoto, Reader in Marketing, and Dr Liyuan Wei, Senior Lecturer in Marketing, Brunel University London (TOU0005)
```

Evidence 7: document Doc 6 (ukc_6476_oral_10647.txt), proves component 2. Dorothy Yen (local note: Q143, Chair)

```text
We are joined virtually by Professor Annette Pritchard, professor of tourism management at Leeds Beckett University and Professor Dorothy Yen
```

Evidence 8: document Doc 6 (ukc_6476_oral_10647.txt), proves component 2. Dorothy Yen (local note: Q174, Professor Pritchard)

```text
what Professor Dorothy has talked about in her evidence submission
```

Evidence 9: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. Louise Miles-Payne (local note: Published written evidence)

```text
FSB Wales (TOU0009)
```

Evidence 10: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. Louise Miles-Payne (local note: Published written evidence)

```text
Fiona Stewart, Managing Director, Green Man Festival (TOU0010)
```

Evidence 11: document Doc 1 (ukc_6476_report_40824.txt), proves component 1. Louise Miles-Payne (local note: Published written evidence)

```text
Welsh Sports Association (TOU0015)
```

Evidence 12: document Doc 3 (ukc_6476_oral_10124.txt), proves component 1. Louise Miles-Payne (local note: Q1, Chair)

```text
On panel 1 we are joined by David Chapman, who is the Executive Director for Wales for UK Hospitality, and Gwyneth Sweatman, Head of Communications for the Federation of Small Businesses in Wales, and we are joined remotely by Suzy Davies, who is the Chair of the Wales Tourism Alliance.
```

Evidence 13: document Doc 3 (ukc_6476_oral_10124.txt), proves component 1. Louise Miles-Payne (local note: header)

```text
[This evidence was taken by video conference]
```

### Necessary documents

- Tick Doc 1 (ukc_6476_report_40824.txt), role: Answer component
- Tick Doc 4 (ukc_6476_oral_10335.txt), role: Answer component
- Tick Doc 6 (ukc_6476_oral_10647.txt), role: Answer component
- Tick Doc 3 (ukc_6476_oral_10124.txt), role: Exclusion / condition source

  Reviewer note:

```text
The Chair's opening words place Gwyneth Sweatman in the room. FSB Wales sent written evidence (Doc 1), so without this she could not be ruled out.
```

Leave unticked: Doc 2 (ukc_6476_oral_10125.txt), Doc 5 (ukc_6476_oral_10428.txt), Doc 7 (ukc_6476_oral_12643.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Document convention: Doc 3 is headed "taken by video conference", yet its Chair places Gwyneth Sweatman in the room; trusting the heading adds her. Linking across documents: Doc 6's header lists no written evidence; only Doc 1's list shows Dorothy Yen's paper. Missing it leaves Louise Miles-Payne alone.
```

(48 / 50 words.)
