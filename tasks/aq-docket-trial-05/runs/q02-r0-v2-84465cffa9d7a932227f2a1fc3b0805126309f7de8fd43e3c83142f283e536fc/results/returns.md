# q02 rev 0 - raw returns (tested_sha256 84465cffa9d7a932227f2a1fc3b0805126309f7de8fd43e3c83142f283e536fc)

Fresh non-fork agents, 2026-10-06. Blind solvers and the auditor received only the workspace
root, their own packet path and the question verbatim; the closed-book solver received only the
question. Returns copied from the task notifications (tables kept as returned).

## Solver A (blind-solver, solver-1 packet)

**answer:** 9 (1 count in Lt. Hill's suit and 8 in Sgt. Worsley's suit)

**confidence:** high

**path:**
1. **The lieutenant's suit (D03, Hill v. Maryland Department of State Police, JRR-25-2281, entered Sept. 17, 2026).**
   - He is identified as "an African American lieutenant who has served with Defendant Maryland Department of State Police."
   - The complaint has four counts: Title VII discrimination (I), hostile work environment (II), retaliation (III) and the Maryland Fair Employment Practices Act (IV).
   - The ruling: "the Court will grant MDSP's Motion to Dismiss Counts I, II, and IV, and will deny the Motion as to Count III." It also says "dismiss Lt. Hill's Complaint as to Counts I, II, and IV without prejudice," and leave to amend was denied.
   - Count III is still pending, so this suit contributes **1**.
2. **The sergeant's suit (D04, Worsley v. Rinaldo et al., MJM-25-3696, opinion dated Sept. 18, 2026, filed 09/21/26).**
   - "Plaintiff, a BPD Sergeant." "Plaintiff alleges twelve counts total." The last three are mislabeled "Count XI, Count X, and a second Count XI."
   - Which motions were filed: BPD, the City and the two State's Attorney defendants (Bates and Trostle) moved to dismiss all claims against them. "the Officer Defendants moved to dismiss Plaintiff's civil conspiracy claim" only.
   - The conclusion says:
     - "All claims asserted against the State's Attorney Defendants are dismissed without prejudice."
     - "Counts IV, V, VI, VII, VIII, and 'X' are dismissed without prejudice as to the City and BPD."
     - "The count for civil conspiracy is dismissed with prejudice as to all defendants."
     - Count IX: "the City and BPD are not immune from the state constitutional claims asserted in Count IX."
   - Count by count:

| Count | Claim | Brought against | Result |
|---|---|---|---|
| I | §1983 unlawful seizure | Officers | **Pending** (officers didn't challenge it) |
| II | §1983 malicious prosecution | Officers | **Pending** |
| III | §1983 suppression/fabrication of evidence | Officers, Trostle | Trostle out; **pending** vs. officers |
| IV | Monell (city liability) | BPD, City, Bates | Dismissed against all |
| V | Defamation | Bates, City, BPD | Dismissed against all |
| VI | State-law malicious prosecution | Officers, Trostle, BPD, City | **Pending** vs. officers |
| VII | Intentional infliction of emotional distress | Officers, both prosecutors, BPD, City | **Pending** vs. officers |
| VIII | Breach of contract | BPD, City | Dismissed |
| IX | Maryland Declaration of Rights | Officers, both prosecutors, BPD, City | **Pending** vs. officers, City, BPD |
| 10th ("XI") | Civil conspiracy | All | Dismissed against all |
| 11th ("X") | Negligence / gross negligence | Officers, both prosecutors, BPD, City | **Pending** vs. officers |
| 12th ("XI") | Battery | Rinaldo only | **Pending** |

   - 12 − 4 fully dismissed = **8** pending. This matches the opinion's summary: "remaining constitutional and common-law claims shall proceed against the City, BPD, and the Officer Defendants."
3. **Total:** 1 + 8 = **9**.

I checked the key quoted sentences against the original docs/ files for both cases, and they match the text/ versions.

**minimal_documents:** D03 + D04. No other document in the packet covers either suit, so there are no substitutes. D02's "Sergeant Lisa Lasher" is a prison-case defendant, not a plaintiff. Other keyword hits (D05, D06, D07) are only case citations.

**readings:**
- **Counting by the printed labels in D04:** the pending labels are I, II, III, VI, VII, IX, "X" and the second "XI". That is still 8, so the total is still 9.
- **Counting only counts that survived a motion actually aimed at them:** D03 Count III plus D04 Count IX (against the City and BPD) gives 2. The question asks about counts "pending against at least one defendant," so the counts the officers never challenged belong in the total. I don't think this reading fits the question.
- **Treating "without prejudice" dismissals as still pending:** I don't consider this defensible. Those counts are no longer live, and amendment would need a new filing.

**gaps:**
- The separate implementing orders ("A separate Order follows/will issue") are not in the packet. The answer relies on the dispositions stated in the opinions themselves.
- The packet contains only plain-text documents (no PDFs or layout files), so there were no original pages to check.
- I read D03 and D04 in full. D01, D02 and D05–D10 were checked only by keyword searches, not read.

**contaminated:** no. I did not open question.txt.

## Solver B (blind-solver, solver-2 packet)

answer: 9 counts. That is 1 in Hill v. Maryland Department of State Police (Count III) plus 8 in Worsley v. Rinaldo (Counts I, II, III, VI, VII, IX, the negligence count mislabeled "Count X", and the battery count mislabeled as the second "Count XI").

confidence: high

path:
1. Who the two plaintiffs are. The lieutenant is in D03 (Civ. No. JRR-25-2281): "Plaintiff Duane Hill ('Lt. Hill') is an African American lieutenant who has served with Defendant Maryland Department of State Police", entered 17 September 2026 (filed 09/17/26). The sergeant is in D04 (Civ. No. MJM-25-3696): "Plaintiff, a BPD Sergeant", dated September 18, 2026, filed 09/21/26.
2. D03 counts. Four counts: Title VII discrimination (I), hostile work environment (II), retaliation (III), Maryland Fair Employment Practices Act claims (IV); only defendant MDSP. D03 p.10: "the Court will grant MDSP's Motion to Dismiss Counts I, II, and IV, and will deny the Motion as to Count III." D03 p.36: "dismiss Lt. Hill's Complaint as to Counts I, II, and IV without prejudice." Pending: 1 (Count III).
3. D04 counts. D04 p.3 "Plaintiff alleges twelve counts total"; last three mislabeled "Count XI", "Count X" and a second "Count XI". Motions: BPD, the City and the State's Attorney defendants each moved to dismiss all claims against them; the four officer defendants moved to dismiss only the civil conspiracy count (pp.4-5). Rulings: "All claims asserted against the State's Attorney Defendants are dismissed without prejudice."; "Counts IV, V, VI, VII, VIII, and 'X' are dismissed without prejudice as to the City and BPD."; "The count for civil conspiracy is dismissed with prejudice as to all defendants" (pp.31-32); Count IX survives against the City and BPD: they "are not immune from the state constitutional claims asserted in Count IX" (p.15). Count by count: I pending; II pending; III pending against the officers (Trostle dismissed); IV fully dismissed; V fully dismissed; VI pending against the officers; VII pending against the officers; VIII fully dismissed; IX pending against the officers, BPD and the City; 10th (first "XI", conspiracy) dismissed as to all; 11th ("X", negligence) pending against the officers; 12th (second "XI", battery, Rinaldo only) pending. Pending: 8. Check: 12 − 4 fully dismissed (IV, V, VIII, conspiracy) = 8; matches p.2 "remaining constitutional and common-law claims shall proceed against the City, BPD, and the Officer Defendants."
4. Total: 1 + 8 = 9.

minimal_documents: D03 and D04. Both are needed, and no other document in the packet mentions either case (searched for the names and docket numbers). There are no alternative documents.

readings:
- Counting by printed count labels: if you count Worsley's distinct labels (I-XI, 11 labels) instead of the court's twelve counts, the pending labels are I, II, III, VI, VII, IX, X and XI. Label XI stays pending because of the battery count, so this still gives 8 and a total of 9.
- Counting only counts a motion challenged and that survived: this would leave out I, II and the battery count (none were challenged). That conflicts with "still pending against at least one defendant", so I reject it.
- Treating "without prejudice" dismissals as pending: these are dismissals, not pending claims, so I reject this too.

gaps:
- I read D03 and D04 in full.
- D02 I read only lines 1-30 plus the search hits. It is a prisoner's suit (Resper v. Weber) in which "Sergeant Lisa Lasher" is a defendant, so it is excluded.
- D01 and D05-D10 are from non-Maryland districts and were not read. Case-insensitive searches for sergeant, lieutenant, trooper, Baltimore and Maryland State Police found nothing in them except a "Connecticut State Trooper" case citation in D07.
- All files were extracted as plain text; there are no PDFs to check.
- The separate orders that accompanied each opinion are not in the packet, so the count rests on the opinions' own conclusions.

contaminated: no

## Closed-book (closed-book-solver)

answer: unknown
confidence: low
basis: The rulings happened in September 2026, which is after my knowledge cutoff of June 2026. I have no memory of these two suits (one by a Maryland State Police lieutenant, one by a Baltimore police sergeant), the motions to dismiss, or how many counts survived. Any number I gave would be a guess. I made no tool calls.
contaminated: no. The only extra context was the user's email address and the working-directory name ("D:\Dev\Docket"), which say nothing about the answer. There were no document excerpts, hints, keys or earlier results.

## Shortcut audit (shortcut-auditor, shortcut packet)

answer: **9.** One count is still pending in Hill v. MDSP (the lieutenant) and eight in Worsley v. Rinaldo (the sergeant).

verdict: clear

shortest_path:
1. Find the two suits. A search for "Maryland State Police|Lieutenant|Lt\." matched only D03. A search for "Sergeant|Sgt\.|Baltimore Police" matched D04 and D02. D03 is Duane Hill v. Maryland Department of State Police, JRR-25-2281; Hill "is an African American lieutenant"; entered September 17, 2026. D04 is Larry Worsley v. Officer Louis Rinaldo et al., MJM-25-3696; Worsley is "a BPD Sergeant"; signed September 18, 2026, filed 09/21/26. D02 (Resper v. Weber) doesn't fit: the sergeant there is a defendant and the plaintiff is a prisoner.
2. D03 count. Four counts. "At bottom, the Court will grant MDSP's Motion to Dismiss Counts I, II, and IV, and will deny the Motion as to Count III." MDSP is the only defendant, so 1 count is pending (Count III, Title VII retaliation).
3. D04 count. "Plaintiff alleges twelve counts total." The officer defendants moved to dismiss only the civil conspiracy count. Conclusion: "All claims asserted against the State's Attorney Defendants are dismissed… Counts IV, V, VI, VII, VIII, and 'X' are dismissed without prejudice as to the City and BPD. The count for civil conspiracy is dismissed with prejudice as to all defendants." Matching each count to its defendants:

| Count | Claim | Status |
|---|---|---|
| I | Unlawful seizure (officers) | Pending |
| II | Malicious prosecution / detention (officers) | Pending |
| III | Officers + Trostle | Trostle out; pending vs officers |
| IV | Monell (BPD, City, Bates) | Fully dismissed |
| V | Defamation (Bates, City, BPD) | Fully dismissed |
| VI | State malicious prosecution | Pending vs officers |
| VII | IIED | Pending vs officers |
| VIII | Contract (BPD, City) | Fully dismissed |
| IX | Maryland Declaration of Rights | Pending vs officers, City, BPD (no immunity for state constitutional torts) |
| 10th (first "XI") | Conspiracy | Fully dismissed |
| 11th ("X") | Negligence | Pending vs officers |
| 12th (second "XI") | Battery, Rinaldo only, not challenged | Pending |

   That leaves 12 − 4 = 8 pending counts.
4. Total: 1 + 8 = 9.

sufficient_documents: D03 and D04 are both needed, and there is no alternative. Neither one alone gives the total, and neither states a "remaining counts" figure. D04's summary says only that "remaining constitutional and common-law claims shall proceed against the City, BPD, and the Officer Defendants," with no number. Key passages checked in the docs/ originals; they match the text extraction.

searches: "Maryland State Police|Lieutenant|Lt\."; "Sergeant|Sgt\.|Baltimore Police"; "Baltimore|BPD|trooper|State Police|police department" (case-insensitive); "Worsley|Duane Hill|Hill v\.|Rinaldo|counts? (remain|surviv|proceed)|remaining (counts|claims)"; a scan of case captions. Read: manifest, D03 and D04 in full, start of D02. Not read in full: D01 and D05-D10 (other districts; only unrelated citation hits).

readings/gaps:
- Counting by the complaint's labels gives the same 8 for D04. Two misreadings would change the answer: treating the conclusion's "Counts IV…VIII, X dismissed" as dismissed against everyone, when it says "as to the City and BPD," gives 5 + 1 = 6; using D02 as the sergeant's suit would also differ, but it is ruled out.
- D03 cites Kimbrough v. Mayor & City Council of Balt. (BAH-25-2187) and Smallwood v. Mayor & City Council of Balt.; neither is in the packet or is the sergeant's suit.
- Difficulty risk: the D03 half is a one-sentence lookup and the cross-document step is a simple sum; the real work is the count-by-defendant matching in D04. Not treated as a shortcut.
- Contamination: none.
