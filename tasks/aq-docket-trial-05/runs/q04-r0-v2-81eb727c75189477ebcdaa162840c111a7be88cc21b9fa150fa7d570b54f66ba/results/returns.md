# q04 rev 0 - raw returns (tested_sha256 81eb727c75189477ebcdaa162840c111a7be88cc21b9fa150fa7d570b54f66ba)

Fresh non-fork agents, 2026-10-06. Blind solvers and the auditor received only the workspace
root, their own packet path and the question verbatim; the closed-book solver received only the
question. Returns copied from the task notifications.

## Solver A (blind-solver, solver-1 packet)

**answer:** Two state police forces were held shielded:
1. **Maryland Department of State Police (MDSP)**: in Hill v. MDSP (D. Md., No. JRR-25-2281, decided Sept. 17, 2026), its state-law employment-discrimination claims (Count IV) were held barred.
2. **New Mexico State Police**: in Langworthy v. New Mexico State Police (D.N.M., No. 1:23-cv-684-DHU-JFR), the case was dismissed for lack of jurisdiction on Eleventh Amendment grounds.

**confidence:** high

**path:**
1. D03, Hill v. Maryland Department of State Police (D. Md.), pages 34-35. Count IV (Maryland Fair Employment Practices Act). "Lt. Hill appears to concede— and the Court agrees—that MFEPA claims are barred by Maryland's Eleventh Amendment sovereign immunity." "Accordingly, the Court will dismiss Count IV for lack of subject-matter jurisdiction." A holding by a federal court; the agency is the state's trooper force ("Black troopers in [MDSP]"). The immunity covered only Count IV; Count III survived.
2. D05, an order in Langworthy v. Alcon (D.N.M., Sept. 18, 2026), page 13, lists the plaintiff's earlier cases "in this District." Item (i): "Langworthy v. New Mexico State Police, 1:23-cv-684-DHU-JFR (filed 8/17/2023; terminated 9/20/2023) (dismissed for lack of subject-matterjurisdiction due to Eleventh Amendment immunity)." The holding was made by a federal court (District of New Mexico); D05 reports it secondhand.
3. Both quotes match the docs/ sources (uscourts_mdd_1_25_cv_02281_0.txt lines 501-503; uscourts_nmd_1_24_cv_01291_6.txt line 209).

Excluded candidates: D04 (Baltimore Police Department): a city force; the court found it "has failed to establish… that it is entitled to state sovereign immunity," and that discussion concerned Maryland common-law immunity, not the Eleventh Amendment; the only Eleventh Amendment ruling in D04 protected State's Attorney Bates. D02 and D06 cite Will v. Mich. Dep't of State Police only for the "person" rule. D07: "Connecticut State Trooper" only in a counsel case name; D07's Eleventh Amendment ruling concerns a county probate court. D01: a community college's governing board. D02, D08, D09: prison and corrections officials. D06: the Suffolk County Supreme Court, its judges and a court clerk. D10: Puerto Rico and its veterans' office, decided on Rooker-Feldman, no immunity ruling. Sheriffs in D05 (Colfax and Camden County): county bodies, no immunity holding.

**minimal_documents:** D03 and D05. Each is the only source for its agency, and no other document can replace either one.

**readings:**
- If only rulings made in the opinions themselves count, leaving out a prior case that a later order merely describes, the answer is the Maryland Department of State Police alone. Not favoured: the question asks what "a federal court" held.
- If Will v. Michigan Dep't of State Police were counted, the Michigan Department of State Police would be added. Not supported: the packet cites Will only for the § 1983 "person" rule.
- Counting the Baltimore Police Department is not defensible: the court denied it immunity, and the immunity at issue was Maryland common-law immunity.

**gaps:**
- The New Mexico State Police holding comes only from D05's one-line parenthetical summary; the 2023 dismissal order itself is not in the packet.
- Plain text, no PDFs.
- D03, D04, D05 and D10 read in full; D01, D02, D06, D07, D08, D09 searched (Eleventh Amendment, sovereign immunity, arm of the state; state police, police, trooper, patrol, highway patrol; Department of Public Safety, sheriff, Bureau of Investigation, marshal, ranger, Policía) with matching passages read in context.

**contaminated:** no

## Solver B (blind-solver, solver-2 packet)

**answer:** Two: the Maryland Department of State Police (MDSP) and the New Mexico State Police.

**confidence:** high

**path:**
1. D03 (D. Md., Hill v. Maryland Department of State Police, No. JRR-25-2281, filed 09/17/26). MDSP is the only defendant. At line 193, MDSP argues the Maryland Fair Employment Practices Act claims in Count IV "are barred by sovereign immunity." At lines 503-505 (pp. 34-35): "Lt. Hill appears to concede— and the Court agrees—that MFEPA claims are barred by Maryland's Eleventh Amendment sovereign immunity… Accordingly, the Court will dismiss Count IV for lack of subject-matter jurisdiction." This immunity ruling covers only Count IV; the Title VII counts were decided on the merits (I and II dismissed, III proceeds). The ruling partly rests on Hill's concession, but the court still makes it.
2. D05 (D.N.M., Langworthy v. Alcon, order to show cause, filed 09/18/26). In a list of the plaintiff's earlier cases "in this District," line 211: "(i) Langworthy v. New Mexico State Police, 1:23-cv-684-DHU-JFR (filed 8/17/2023; terminated 9/20/2023) (dismissed for lack of subject-matterjurisdiction due to Eleventh Amendment immunity)." A federal district court dismissing a suit against the New Mexico State Police on Eleventh Amendment grounds.
3. Both passages match the docs/ sources (docs line 501 for D03, docs line 209 for D05).

Candidates excluded: D04, Baltimore Police Department (city department; state sovereign immunity defense denied, lines 169, 199-201; the earlier protection mentioned at line 179 was "state sovereign immunity", not the Eleventh Amendment; the only Eleventh Amendment holding is for State's Attorney Bates). D02 (line 161) and D06 (line 463), Will v. Michigan Dep't of State Police: cited only for official-capacity and "person" rules. D08 footnote 10, Poteat v. Lydon ("PSP employees"): state sovereign immunity, employees, "PSP" never spelled out. D07, Leftridge v. Connecticut State Trooper: counsel citation. D06, Suffolk County Police Department: county department in a separate lawsuit, no immunity ruling. Other Eleventh Amendment holdings cover non-police bodies (D01 college board; D02, D08, D09 prison officials; D06, D07 state courts and judges; D10 Puerto Rico and its veterans' office).

**minimal_documents:** D03 and D05. No other document can stand in for either one.

**readings:**
- Narrow reading (count only rulings the authoring court makes in its own opinion): MDSP alone. Not preferred: the question asks what "a federal court" held, and D05 attributes that dismissal to the D.N.M. federal court.
- Broad reading (any sovereign-immunity protection, or cited precedent): could add BPD, the Michigan Department of State Police, or "PSP"; the packet's wording supports none of these as an Eleventh Amendment holding for a state police force.

**gaps:**
- The 1:23-cv-684 order itself is not in the packet.
- D01, D02, D03, D04, D05 and D07 read in full; D06, D08, D09, D10 read at openings, immunity sections and every police/trooper/patrol match; packet-wide searches for other agency names found nothing further.

**contaminated:** no

## Closed-book (closed-book-solver)

answer: Pennsylvania State Police and New Jersey State Police (a guess)

confidence: low

basis: I don't recall the case or document this question refers to, and the answer depends on that document. The guess rests only on how often federal courts have ruled these two agencies are arms of their states and so protected by Eleventh Amendment immunity. I also considered Will v. Michigan Department of State Police, but that case was decided on whether a state is a "person" under § 1983, not on Eleventh Amendment immunity.

contaminated: no

## Shortcut audit (shortcut-auditor, shortcut packet)

answer: Two forces: the Maryland Department of State Police and the New Mexico State Police.

verdict: clear

shortest_path:
1. Search text/ for "Eleventh Amendment" (hits in all 10 documents), then for "State Police", "Trooper", "Police" and "PSP" (hits in D02, D03, D05, D06, D07 and D08). The fuller police/trooper/patrol search also hit D04 (Baltimore Police Department).
2. D03, Hill v. Maryland Department of State Police (D. Md., No. JRR-25-2281, ECF 20, 09/17/26). Count IV, lines 503-505: "Lt. Hill appears to concede— and the Court agrees—that MFEPA claims are barred by Maryland's Eleventh Amendment sovereign immunity … Accordingly, the Court will dismiss Count IV for lack of subject-matter jurisdiction." Counts I-II dismissed under Rule 12(b)(6), Count III survives; the immunity holding covers only Count IV.
3. D05, Langworthy v. Alcon (D.N.M., 1:24-cv-1291, Doc. 64, 09/18/26), line 211: "(i) Langworthy v. New Mexico State Police, 1:23-cv-684-DHU-JFR (filed 8/17/2023; terminated 9/20/2023) (dismissed for lack of subject-matter jurisdiction due to Eleventh Amendment immunity)."
4. Combining the two documents gives two forces. Neither document gives both.

sufficient_documents: D03 and D05, both required. No other document shows either holding.

searches: "Eleventh Amendment", "State Police", "Trooper", "PSP", "Highway Patrol", "Police" (case-sensitive), "police|trooper|patrol|constab|public safety" (case-insensitive), "arm of the state", "governmental immunity", Puerto Rico police names (Policía, Negociado). Read in full: D01, D02, D03, D05, D10. In part: D04 (lines 1-330 plus every Eleventh Amendment hit), D06 (440-480), D07 (opening, defendant list, 175-195), D08 (1-90, 245-260), D09 (opening). Manifest read; docs/ originals keyword-checked (hit counts matched). question.txt not opened.

readings/gaps:
- Narrower reading (only a holding by the authoring court): Maryland force alone; the question asks what "a federal court" held and D05 states the District of New Mexico dismissal outright, so both count.
- Distractors rejected: D04 BPD (city force; Maryland common-law state sovereign immunity not shown; local governmental immunity for torts; only Eleventh Amendment ruling covers Bates); D02/D06 Michigan State Police (Will citation for "person"/official-capacity rules); D08 fn 10 "PSP employees" (state sovereign immunity for employees on intentional torts; PSP not spelled out); D07 Connecticut trooper (counsel citation).
- Difficulty risk (not a shortcut): a keyword search pairing "State Police" with "Eleventh Amendment" finds both inputs quickly, and D05 has both terms on one line. D03 needs the Count IV passage read. Combining them is simple but genuinely spans two documents.
- Gaps: D06 (92K characters), D07, D08 and D09 not read line by line; keyword searches cover them. No extraction problems.
