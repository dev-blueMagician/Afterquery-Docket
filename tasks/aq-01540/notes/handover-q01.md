# aq-01540 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01540 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 6f8f40e33cf2ab101a45954cb6df514b0091b51a1fe45140e8a4d6b1ecdd34f7: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D02 = Doc 8, D05 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In eight federal rulings issued September 11-15, 2026, which defendants, if any, did a court say were within its personal jurisdiction even as it dismissed every claim against them? List them in any order.
```

### Number of asks

1 ask

### Gold answer

```text
Lorenzo Vidino and Lewis Machining & Engineering
```

### Step-by-step reasoning

```text
Step 1. Doc 8 (Nada v. United Arab Emirates, D.D.C., September 15, 2026): the court dismisses the UAE for lack of subject-matter jurisdiction and the Alp defendants and Besson for lack of personal jurisdiction. It calls Vidino "the American journalist over whom the Court has personal jurisdiction" and dismisses Count Three, the only claim against him, for failure to state a claim. Vidino qualifies.

Step 2. Doc 2 (the Shenzhen sellers v. Lewis Machining, M.D. Ga., September 11, 2026): the court finds it has "personal jurisdiction over the Parties", and the Parties are the four plaintiffs and defendant Lewis Machining. The consent judgment entered in the same order dismisses with prejudice all claims the plaintiffs asserted against Lewis Machining (Counts I to III). Lewis Machining qualifies.

Step 3. Exclusions. Doc 1: the Ohio court holds OEC India within its personal jurisdiction but dismisses only Count IX, and Counts I to VIII survive. Doc 2: the four Shenzhen plaintiffs are also Parties, but they are plaintiffs, and Counterclaim Counts I and II are adjudged against them. Doc 8, Doc 7 and Doc 1: the UAE, Ofcom, the Alp defendants, Besson and OEC USA lost every claim against them for want of jurisdiction, not despite it. Doc 5: Royal Caribbean won dismissal on forum non conveniens with no statement that the court had personal jurisdiction over it. Doc 4, Doc 3 and Doc 6 dismiss no defendant from the case.

Answer: Lorenzo Vidino and Lewis Machining & Engineering.
```

### Answer components

Component 1

```text
Lorenzo Vidino
```

Component 2

```text
Lewis Machining & Engineering
```

### Evidence

Evidence 1: document Doc 8 (uscourts_dcd_1_24_cv_00206_0.txt), proves component 1. Lorenzo Vidino (local note: Part III, p. 47; l.515)

```text
Defendant Vidino, the American journalist over whom the Court has personal jurisdiction, is charged in only one count
```

Evidence 2: document Doc 8 (uscourts_dcd_1_24_cv_00206_0.txt), proves component 1. Lorenzo Vidino (local note: Part III, p. 50; l.551)

```text
Therefore, the complaint fails to state the only claim against Vidino, and the case against him will be dismissed.
```

Evidence 3: document Doc 2 (uscourts_gamd_7_25_cv_00193_0.txt), proves component 2. Lewis Machining & Engineering (local note: Findings of Infringement, p. 6; l.80)

```text
The Court has subject matter jurisdiction over this matter and personal jurisdiction over the Parties.
```

Evidence 4: document Doc 2 (uscourts_gamd_7_25_cv_00193_0.txt), proves component 2. Lewis Machining & Engineering (local note: Consent Judgment preamble, p. 8; l.118)

```text
Defendant/Counterclaimant Lewis Machining & Engineering, Inc. (Lewis Machining), (collectively, the Parties)
```

Evidence 5: document Doc 2 (uscourts_gamd_7_25_cv_00193_0.txt), proves component 2. Lewis Machining & Engineering (local note: Consent Judgment ¶ 9, p. 10; l.156)

```text
All claims asserted by Plaintiffs in their Complaint for Declaratory Judgment (Doc. 1)
```

Evidence 6: document Doc 2 (uscourts_gamd_7_25_cv_00193_0.txt), proves component 2. Lewis Machining & Engineering (local note: Consent Judgment ¶ 9, p. 10; l.156)

```text
are hereby DISMISSED WITH PREJUDICE, with each Party to bear its own costs and fees
```

### Necessary documents

- Tick Doc 8 (uscourts_dcd_1_24_cv_00206_0.txt), role: Answer component
- Tick Doc 2 (uscourts_gamd_7_25_cv_00193_0.txt), role: Answer component

Leave unticked: Doc 1 (uscourts_ohsd_2_25_cv_01239_1.txt), Doc 3 (uscourts_txnd_4_23_cv_00415_2.txt), Doc 4 (uscourts_ksd_2_26_cv_02326_0.txt), Doc 5 (uscourts_flsd_1_26_cv_20364_0.txt), Doc 6 (uscourts_ca5_23_20570_0.txt), Doc 7 (uscourts_dcd_1_25_cv_02880_0.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter

Leave unticked: Temporal alignment, Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Wrong members in a list

Where the trap sits:

```text
Doc 1, the Ohio opinion on the motion to dismiss by Oriental Export Corporation and OEC USA. Its personal-jurisdiction section opens its analysis with "Upon review, the Court finds that ATP has made a prima facie showing of specific personal jurisdiction over OEC India, but not over OEC USA." It is the one place in the bundle where a court contests and upholds jurisdiction over a defendant. The motion is "GRANTED in part and DENIED in part", and the conclusion dismisses Count IX, the fraudulent-inducement claim, with the word DISMISSED, and limits the damages on four other counts.
```

The wrong answer a careless solver gives:

```text
"Lorenzo Vidino, Lewis Machining & Engineering and OEC India". The solver finds both correct defendants, then also counts OEC India: a court held it within its personal jurisdiction, and the same ruling dismissed a claim against it. It reads "dismissed a claim" as if it were "dismissed every claim".
```

Why the correct answer avoids it:

```text
The question asks for defendants whose every claim was dismissed. Doc 1's conclusion says the motion "is DENIED as to ATP’s breach-of-contract claims (Counts I and II), express-warranty claims (Counts III and IV), and implied-warranty claims (Counts V–VIII)", so eight of nine counts against OEC India go forward. Only Vidino (Doc 8), whose single count was dismissed, and Lewis Machining (Doc 2), whose plaintiffs' claims were all dismissed with prejudice, meet both conditions.
```

(220 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Document convention

How a careless solver fails: Wrong members in a list

Where the trap sits:

```text
Doc 2, the Middle District of Georgia order entering a stipulated consent judgment. The court's finding that it has jurisdiction is a numbered item in a formulaic list: "1. The Court has subject matter jurisdiction over this matter and personal jurisdiction over the Parties." The dismissal sits in paragraph 9 of the stipulated judgment, which dismisses the plaintiffs' claims "WITH PREJUDICE" as part of a settlement, and the defendant is named in that finding only through the defined term "the Parties", which the entered consent judgment defines later.
```

The wrong answer a careless solver gives:

```text
"Lorenzo Vidino". The solver treats the consent judgment as a settlement with no jurisdiction ruling, or never links "the Parties" to the defendant Lewis Machining, and so lists only the Nada defendant whose jurisdiction the D.C. court stated in so many words.
```

Why the correct answer avoids it:

```text
The question asks what the court said, not what was contested. Doc 2's finding 1 is the court's own statement that it has personal jurisdiction over the Parties, the preamble of the consent judgment entered with the same order defines the Parties to include "Lewis Machining & Engineering, Inc. (Lewis Machining)", and paragraph 9 dismisses every claim the plaintiffs brought against it, in the same September 11, 2026 order.
```

(199 words across the three boxes; the form needs at least 150.)
