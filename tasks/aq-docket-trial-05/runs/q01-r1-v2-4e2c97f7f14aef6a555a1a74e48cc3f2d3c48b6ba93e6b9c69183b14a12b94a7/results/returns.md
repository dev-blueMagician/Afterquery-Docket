# q01 rev 1 - raw returns (tested_sha256 4e2c97f7f14aef6a555a1a74e48cc3f2d3c48b6ba93e6b9c69183b14a12b94a7)

Fresh non-fork agents, 2026-10-06. Blind solvers and the auditor received only the workspace
root, their own packet path and the question verbatim; the closed-book solver received only the
question. Returns copied from the task notifications.

## Solver A (blind-solver, solver-1 packet)

I found two plaintiffs: Veronica Hernandez and Geneva Langworthy.

answer: Veronica Hernandez; Geneva Langworthy

confidence: high

path:
1. Hernandez (D06, E.D.N.Y. 2:25-cv-2057). She sued judges: line 55, p.2, the defendants include "the Honorable Justice John J. Leo, the Honorable Justice Maureen T. Liccione, the Honorable Justice Christopher Modelewski, and the Honorable Justice Aletha V. Fields (collectively, with the Suffolk County Supreme Court, the 'Judicial Defendants')". Leo ruled against her: line 117, p.5, "Justice John J. Leo presided over these proceedings, issued rulings adverse to Hernandez". Liccione ruled against her: line 103, p.4, "a debt collection action … in which Justice Liccione entered a judgment against Hernandez on July 9, 2025"; line 475, p.24 adds that Liccione "permitted a default judgment to be entered against Hernandez". Timing: line 161, p.7, the original complaint was filed April 11, 2025 and already named Leo and Liccione; line 201, p.8, the amended complaint of November 14, 2025 added Modelewski and Fields. The amended complaint also asks the court to vacate Leo's September 26, 2025 decision (line 69). So the July 9 judgment and the September 26 decision both came before the November 14 amended complaint, which still named Leo and Liccione.
2. Langworthy (D05, D.N.M. 1:24-cv-1291). The defendant in this case is a deputy, not a judge, but the order lists her other lawsuits. A judge ruled against her: line 225, p.14, "(vi) Langworthy v. Colfax County, et al., 1:25-cv-18-WJ-JHR (KK) (filed 1/8/2025; terminated 3/18/2025) (dismissed by Chief District Judge Kenneth J. Gonzales for failure to state a claim for relief (Doc. 28))". She then sued that judge: line 239, p.15, "(xi) Langworthy v. Gonzales, et al., 1:25-cv-433-REB-SBP (filed 5/6/25 …) (alleging that Plaintiff was denied access to the courts by Chief District Judge Kenneth J. Gonzales, District Judge David Urias, and Magistrate Judge Kirtan Khalsa)". Order of events: the dismissal (by 3/18/2025) came 49 days before the suit against Gonzales (5/6/2025): 13 + 30 + 6 days.
3. Excluded: D07, Mulvilhill: she named Judge Crandall, but the document never says he ruled against her. Lines 173-177, pp.10-11: "Plaintiff makes no specific claims against Judge Crandall… Presumably, Judge Crandall was somehow involved in the court proceedings… though Plaintiff does not state so or explain how." D10, Cora: he sued Veteran's Solicitor Montañez-Allman, who signed the agency Resolution that gave him no damages ("The Resolution was signed by Solicitor Montañez-Allman", line 125); an agency official, not a judge; the Puerto Rico appellate judges who ruled against Cora were not sued. D04: the defendants include prosecutors (Bates and Trostle), not judges. D01, D02, D03, D08, D09: no judge is a defendant. Cited precedents (e.g., Collins v. W. Hartford Police Dep't, Falco, Gristina v. Merchan) are not parties in these documents; not counted.

minimal_documents: D05 and D06. Each is the only source for one of the two plaintiffs, and no other document can replace either.

readings:
- Looser reading (naming a judge is enough, or a ruling can be presumed): add Ashley Mulvilhill (D07). The document itself only presumes Crandall was involved.
- Very broad reading (an agency official who decides a case counts as a "judge"): add Captain Richard Cora (D10, for Montañez-Allman's Resolution). That is not the ordinary meaning of "judge."
- Strict reading (only the defendant in the decided case counts): Hernandez only, because Langworthy's suit against a judge is a different case listed in D05.
- Case-number initials: "DHU" and "KG" in the case numbers suggest Judges Urias and Gonzales also decided Langworthy's other dismissed cases, and "(KK)" suggests Magistrate Judge Khalsa was assigned to case (vi). The text does not say this outright, and it would not change the answer.

gaps:
- All ten text files read in full, including the parts of D03 and D04 that the first read cut off.
- The manifest lists only .txt sources (method "text"); no PDFs or layout files.
- docs/ not read separately.
- The exact dates of Leo's earlier adverse rulings are not given. Liccione's earlier default judgment is only implied to predate March 2025.

contaminated: no

## Solver B (blind-solver, solver-2 packet)

**answer:** Veronica Hernandez and Geneva Langworthy

**confidence:** high

**path:**
1. Hernandez (D06, E.D.N.Y. 2:25-cv-2057). Who she sued: Justices John J. Leo, Maureen T. Liccione, Christopher Modelewski and Aletha V. Fields of Suffolk County Supreme Court ("Judicial Defendants"). Rulings against her: Leo "presided over these proceedings, issued rulings adverse to Hernandez" (text/D06.txt line 117); she also asks to vacate "a September 26, 2025 decision rendered by Justice Leo." Liccione "entered a judgment against Hernandez on July 9, 2025" (line 103); line 591 adds that Liccione "improperly ruled in favor of the Pressler Defendants." Modelewski and Fields "granted extensions of time permitting the foreclosure action to proceed" (line 135). Timing: the amended complaint naming all four was filed November 14, 2025, after those rulings. The claims were dismissed, partly on absolute judicial immunity.
2. Langworthy (D05, D.N.M. 1:24-cv-1291). The current case is against a deputy. But the court's list of her earlier cases shows (xi) "Langworthy v. Gonzales, et al., 1:25-cv-433 (filed 5/6/25…) (alleging that Plaintiff was denied access to the courts by Chief District Judge Kenneth J. Gonzales, District Judge David Urias, and Magistrate Judge Kirtan Khalsa)" (line 239). Ruling against her: case (vi), "Langworthy v. Colfax County… (filed 1/8/2025; terminated 3/18/2025) (dismissed by Chief District Judge Kenneth J. Gonzales for failure to state a claim for relief (Doc. 28))" (line 225). Timing: Gonzales dismissed her case by 3/18/2025, and she sued him on 5/6/2025. Both quotes match the source file in docs/.
3. Excluded: Mulvilhill (D07): she asked for a summons against Judge Crandall of the Herkimer County Surrogate Court, but the court says she "makes no specific claims against Judge Crandall" and only guesses he was "somehow involved… though Plaintiff does not state so or explain how." No ruling against her is shown. Cora (D10): he sued Veteran's Solicitor Montañez-Allman, who signed the agency Resolution that gave him no damages; an agency official, not a judge. The "administrative judge" mentioned at line 97 is not a defendant, and no court-of-appeals or Supreme Court judge was sued. Worsley (D04): he sued prosecutors, not judges. D01, D02, D03, D08, D09: no judge is a defendant; every judge-term hit is a signature block, a legal citation, or a non-party mention.

**minimal_documents:** D05 and D06. Both are needed because each supplies a different plaintiff, and no other document can replace either. D07 and D10 matter only for the exclusions.

**readings:**
- Only judges sued in the case being decided: the answer is Hernandez alone, because Langworthy's suit against Gonzales is a separate case reported in D05's list of her past cases.
- Inferred rulings count: Mulvilhill would be added if a ruling against her is assumed from Crandall's presumed role in the Herkimer County proceedings. The document does not support that.
- Agency adjudicators count: Cora would be added if the Solicitor who signed the adverse Resolution counts as a "judge." Ordinary meaning does not support that.
- Other judges Langworthy sued: Urias and Khalsa may also have ruled against her. The judge initials in her case numbers ("DHU", "(KK)") hint at it, but the document doesn't say so explicitly, and it doesn't change the answer. Case (x), against unnamed state "judges, clerks," gives no ruling.

**gaps:**
- All ten text/Dnn.txt files were read in full.
- Of the docs/ source files, only two were spot-checked by search. No layout files or PDFs exist.
- The dates of Leo's earliest adverse rulings, relative to the original April 11, 2025 complaint, aren't stated. The November 2025 amended complaint clearly postdates the rulings, so this doesn't affect the answer.

**contaminated:** no. The question file was not opened, and nothing about the answer leaked.

## Closed-book (closed-book-solver)

answer: Unknown for this specific docket. My best guess from well-known judicial-immunity cases: Joseph Bradley (v. Judge Fisher, who disbarred him); the clergymen in Pierson v. Ray (v. Judge Spencer, who convicted them); the Sparks in Dennis v. Sparks (v. the judge who issued an injunction against them); Richmond Allen and Jesse Nicholson (v. Magistrate Pulliam, who set bail and jailed them); possibly Linda and Leo Sparkman (v. Judge Stump, who approved her sterilization).
confidence: low
basis: The question seems to refer to a specific set of documents that I don't have. The list comes from memory of landmark U.S. judicial-immunity cases, so it may not match the cases this question is about.
contaminated: no

## Shortcut audit (shortcut-auditor, shortcut packet)

answer: Veronica Hernandez (D06) and Geneva Langworthy (D05).

verdict: clear

shortest_path:
1. Find candidates. Searches for "judge", "judicial immunity" and named judges ("Hon.", "Judge/Justice [Name]") return only D05, D06 and D07.
2. D06 (E.D.N.Y. 2:25-cv-2057) includes Hernandez. She named Justices Leo, Liccione, Modelewski and Fields ("state court judges"). Leo: "Justice John J. Leo presided over these proceedings, issued rulings adverse to Hernandez"; she also asks the court to vacate his "September 26, 2025 decision". Liccione: "Justice Liccione entered a judgment against Hernandez on July 9, 2025"; a default judgment had been entered against her before March 2025. Modelewski and Fields "granted extensions of time" to her opponents in the foreclosure case. Her Amended Complaint (Nov 14, 2025) came after all of these rulings.
3. D05 (D.N.M. 1:24-cv-1291) includes Langworthy. This needs two entries from her case list plus a date comparison. Entry (vi): "Langworthy v. Colfax County, et al., 1:25-cv-18 … (filed 1/8/2025; terminated 3/18/2025) (dismissed by Chief District Judge Kenneth J. Gonzales…)". Entry (xi): "Langworthy v. Gonzales, et al., 1:25-cv-433 … (filed 5/6/25…) (alleging that Plaintiff was denied access to the courts by Chief District Judge Kenneth J. Gonzales, District Judge David Urias, and Magistrate Judge Kirtan Khalsa)". 3/18/2025 is before 5/6/2025, so she sued Gonzales after he dismissed her case. Weaker support: the judge initials in her earlier case numbers (DHU, "(KK)") suggest those judges also handled cases she lost; an inference, not needed for the answer.
4. D07 excludes Mulvilhill: "Plaintiff makes no specific claims against Judge Crandall" and "Presumably, Judge Crandall was somehow involved … though Plaintiff does not state so or explain how." No ruling against her is shown.
5. Other documents have no judge defendant: D10 (Commonwealth, P.R. VPO, Veteran's Solicitor, attorneys); D09 ("M.J. Edwards" is a prison health care administrator, not a magistrate judge); D01, D02, D03, D04, D08 (agencies, prison or police officials, prosecutors, medical staff).

sufficient_documents: D05 and D06 together. D07 must be read to exclude it, and the rest were checked to exclude them. No single document gives the whole list.

searches: judge, justice, magistrate, judicial immunity, "sued/naming … judge/court", Hon./Honorable, "Judge/Justice/Commissioner [Name]", hearing officer, ALJ, arbitrator, referee, tribunal, district justice. Read in full: D01, D02, D05, D06, D07, D08, D09, D10. Read in part: D03 and D04 (first 200 lines) with judge-term searches over their full text. Key quotes match docs/.

readings/gaps:
- Broad reading adds Mulvilhill (D07) only if one assumes Crandall presided over the Herkimer matters she lost; the opinion expressly says she doesn't state his role.
- Very broad reading of "judge" adds Cora (D10); the Veteran's Solicitor is not a judge, and the Resolution found in Cora's favor on liability.
- Strict timing for Hernandez: she still qualifies (earlier default judgment, Leo's earlier adverse rulings, Amended Complaint after everything).
- Difficulty risk, not a shortcut: Hernandez is nearly stated outright in D06; Langworthy needs a two-entry join and a date comparison inside D05; the cross-document work is combining D05 and D06 and rejecting the D07 distractor.
- Gaps: analysis sections of D03 and D04 covered by search; no extraction gaps; contamination none.
