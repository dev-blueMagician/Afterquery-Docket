# Sketch round 1: preliminary screen returns (2026-10-06)

Sketch-stage evidence only, not final check records. Each blind solve is a fresh blind-solver
agent given only the workspace root, one packet path from q01 rev 0's prepared run
(q01-r0-v2-3a54fe77..., same corpus bytes; the scope guard allows only that packet's text/ and
docs/) and the sketch question verbatim. Closed-book agents received only the question.
Returns are copied from the task notifications.

## Closed-book screens

### i01 (closed-book-solver)

answer: unknown
confidence: low
basis: My training data ends in June 2026, and the rulings you asked about came in September 2026. I don't recall the suits by the Maryland State Police lieutenant or the Baltimore police sergeant, and I don't know how many counts each one raised. Without that, I can't count which claims survived the motions to dismiss. Any number I gave would be a pure guess.
contaminated: no. Only general environment and account details were attached. Nothing related to the question, such as document excerpts, hints, answer keys or earlier results, was present.

### i03 (closed-book-solver)

answer: unknown
confidence: low
basis: The question points to a specific set of prisoner medical-care lawsuits, but it doesn't name any case, court or filing. Many such suits exist, and nothing I remember ties this question to one of them. I can't identify the defendants whose claims were all dismissed with prejudice without the documents. I made no tool calls.
contaminated: no. The session only had automatic account details and environment details, including the working directory name. None of it was project instructions, memory, an answer key, document excerpts, hints, bundle metadata or earlier results.

### i04 (closed-book-solver)

answer: unknown
confidence: low
basis: These rulings came in September 2026, which is after my June 2026 knowledge cutoff. I have no memory of either plaintiff or how many federal suits each filed before, so any numbers I gave would be made up. No tools were called.
contaminated: no

### i02 (closed-book-solver)

answer: unknown. If a guess is wanted: the Pennsylvania State Police and the New Jersey State Police.
confidence: low
basis: I can't recall the specific ruling. The question points to one particular case or document that wasn't provided. The guess only reflects that federal courts in the Third Circuit often treat these two agencies as arms of the state protected by the Eleventh Amendment. It does not come from any memory of this holding.
contaminated: no. The only context attached was an automatic account email and environment details, with nothing related to the answer. No tools were called.

### i05 (closed-book-solver)

answer: unknown
confidence: low
basis: The question depends on a specific set of case documents or dockets that I was not given. Which plaintiffs got appointed counsel is a detail found only in those records, and general knowledge cannot supply it. I don't recall any widely known set of cases that matches this question.
contaminated: no

## Blind solves

### i02 (blind-solver, solver-2 packet)

answer: The Maryland Department of State Police and the New Mexico State Police.
confidence: high
path (summary): D03 L35 MDSP sole defendant; L503-505 "Lt. Hill appears to concede— and the Court agrees—that MFEPA claims are barred by Maryland's Eleventh Amendment sovereign immunity ... dismiss Count IV for lack of subject-matter jurisdiction". D05 L211 "(i) Langworthy v. New Mexico State Police ... (dismissed for lack of subject-matterjurisdiction due to Eleventh Amendment immunity)". Excluded: BPD (Maryland state-law sovereign immunity, rejected, L199-201; Eleventh Amendment applied only to Bates); Will v. Michigan Dep't of State Police (cited for "person"/official-capacity propositions only); D08 "PSP employees" in a Poteat citation (state sovereign immunity, employees, PSP undefined); D07 Connecticut trooper (counsel citation); D01, D09, D10 immune parties are not police.
minimal_documents: D03 and D05.
readings: narrow (only a ruling in its own opinion) gives MDSP alone; broad (agencies in cited cases) could add Michigan State Police and "PSP", rejected because the citations do not say so.
gaps: the 2023 New Mexico order itself is not in the packet; D03's ruling rests partly on the concession; several documents searched rather than read.
contaminated: no

### i03 (blind-solver, shortcut packet)

answer: Britney Huner (D08); Nurse Supervisor Lock and RNS Money (D09)
confidence: high
path (summary of the verbatim return): only D02, D08, D09 are prisoner medical-care suits (others ruled out by subject). D08: Huner "the claims against her will be dismissed with prejudice"; Letizio's Eighth Amendment claim goes forward; Wellpath is a company. D09: counts 2-3 against "Defendants Edwards, Lock and Money"; official-capacity, declaratory/injunctive, ADA and equal protection claims "dismissed from this action with prejudice"; remaining claim "against Defendants Edwards and Baird", so nothing is left against Lock or Money. D02: official-capacity claims dismissed without prejudice; summary judgment for Weber; Lasher dismissed without prejudice; fn 8 declines with-prejudice dismissal; Mace and Akintade not ruled on.
minimal_documents: D08 and D09 supply the names; D02 needed to exclude its defendants.
readings: summary judgment treated as dismissal still leaves Weber out (official-capacity claims without prejudice); answer unchanged under the other readings tried; misreading to all suits would add Radosta and the Cora defendants.
gaps: only surnames for Lock and Money; D06 read lines 1-300 plus searches.
contaminated: no (did not open question.txt).

### i04 (blind-solver, solver-1 packet)

answer: 3, 1
confidence: high
path (summary): D05 list, present case "(filed in state court 11/27/2024; removed 12/23/2024)"; filed before 11/27/2024: (i) 8/17/2023, (ii) 11/13/2023, (iii) 11/20/2023; later items excluded. D06: "in December 2024 ... Hernandez filed a separate federal civil rights action"; before April 11, 2025, so 1.
minimal_documents: D05 and D06.
readings: measured from the 12/23/2024 removal date, 4, 1 (case (v) filed 12/5/2024); ignoring the timing, 10, 1 (contradicts the question).
gaps: D05's list covers only "cases in this District over the past three years", so older suits or suits elsewhere would not appear; D06 rests on Hernandez's allegation and gives no full litigation list.
contaminated: no

### i01 (blind-solver, solver-1 packet)

answer: 9 counts. One survives in Lt. Hill's suit and eight survive in Sgt. Worsley's suit.
confidence: high
path (summary): D03 four counts; L193/L521 Counts I, II, IV dismissed, Count III survives (1). D04 twelve counts with defendants (L67-77); Officers moved only against conspiracy (L79); SA Defendants dismissed (L465); L477 conclusion; L255 Count IX survives against City/BPD. Count by count: I, II, III, VI, VII, IX, 11th (negligence), 12th (battery) pending; IV, V, VIII, 10th (conspiracy) out; 8 + 4 = 12. Total 1 + 8 = 9. Decisive sentences checked against docs/ originals.
minimal_documents: D03 and D04.
readings: by printed labels still 8 (total 9); counting claims inside D03's counts still 1; counting only counts that survived a motion aimed at them gives 2 (rejected: conflicts with "pending against at least one defendant"); treating without-prejudice dismissals as pending gives 15 (rejected).
gaps: implementing orders and later docket activity not in the packet; other eight documents keyword-searched only.
contaminated: no (did not read question.txt).

### i05 (blind-solver, solver-2 packet)

answer: Wayne Resper (D02) and Captain Richard Cora (D10)
confidence: high
path (summary): D02 fn 2 "Plaintiff is now represented by appointed counsel. (ECF Nos. 20, 27.)", L29, fn 3 former pro se status. D10 VPO appointed Pérez-Hernández and Quintana-Román (L81-83), Bandas and Deliz-Hernández (L105), Meléndez-López and Álvarez-Torres (L107); L237 "appointed counsels"; L127 later disclaimer does not undo earlier appointments. D07 excluded: motion for counsel denied (L37, L275). Others: no appointed counsel mentioned (Wagner, Langworthy, Hernandez, Howard, Richards pro se; Hill none; Worsley only union/legal counsel in pay demands).
minimal_documents: D02 and D10; all ten needed to exclude the rest.
readings: only court-appointed lawyers gives Resper only (Cora's were agency-appointed); counting a request would add Mulvilhill (rejected).
gaps: D06 read lines 1-250 and 560-819 plus keyword searches.
contaminated: no

### i06 (blind-solver, shortcut packet)

answer: Veronica Hernandez; Geneva Langworthy
confidence: high
path (summary): D06 Leo "issued rulings adverse to Hernandez" (p. 5); Liccione "entered a judgment against Hernandez on July 9, 2025" (p. 4) and "permitted a default judgment" (p. 24); AC (11/14/2025) postdates these. D05 (vi) "dismissed by Chief District Judge Kenneth J. Gonzales ..." terminated 3/18/2025; (xi) filed 5/6/25 alleging denial of access "by Chief District Judge Kenneth J. Gonzales, ..."; adverse ruling first. Exclusions: D07 Mulvilhill ("Presumably, Judge Crandall was somehow involved ... though Plaintiff does not state so or explain how"); D10 Cora sued an agency head, not a judge; D04 Worsley sued prosecutors; D08 Howard's earlier dismissal came from a court but no judge was sued; D01, D02, D03, D09 name no judge.
minimal_documents: D05 and D06.
readings: broader reading ("sued a judge" connected to proceedings that went against them, no stated ruling by that judge) adds Mulvilhill; very loose reading (agency adjudicators as judges) could add Cora (weak); Urias and Khalsa rulings not stated (answer unchanged).
gaps: D03 read through L230 plus keyword search; all others in full.
contaminated: no (saw question.txt in a listing but did not open it).

### i06 closed-book (closed-book-solver)

answer: unknown. My best guess comes from well-known U.S. judicial-immunity cases: Joseph Bradley (Bradley v. Fisher); Linda and Leo Sparkman (Stump v. Sparkman); the Pierson clergymen (Pierson v. Ray); the Sparks plaintiffs (Dennis v. Sparks); Richmond Allen and Jesse Nicholson (Pulliam v. Allen)
confidence: low
basis: no access to the specific set; guess from memory of famous suits against judges.
contaminated: no

Caller note: the gaps item is a real fairness defect for i04 as worded. "How many other federal
lawsuits had she filed" is not pinned by the documents, which list only cases in one district over
three years and one alleged prior action. i04 needs rescoping or is dropped.
