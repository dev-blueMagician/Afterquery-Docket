# q03 rev 0 shortcut audit (fresh shortcut-auditor agent, packet shortcut, 2026-10-08)

tested_sha256: 66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2
Prompt: workspace root, packet path, verbatim question only.

Raw return:

answer: Two defendants qualify: Ofcom (the UK Office of Communications) in D03, and OEC USA, Inc. in D07.

verdict: clear. There is a difficulty risk, but I found no disqualifying shortcut.

shortest_path:
1. I searched text/D01–D08 for "forum non|non conveniens". Every document has at least one hit (D07 13, D04 11, D03 2, D05 2, and 1 each in D01, D02, D06 and D08).
2. **D03** (D.D.C. 25-cv-2880, dated Sept 15, 2026; Ofcom is the only defendant):
   - Line 97: "Ofcom also argues that the Court should dismiss the complaint on the grounds of forum non conveniens and international comity… The Court addresses only Ofcom's first argument and concludes that it lacks subject-matter jurisdiction."
   - Line 250: "Ofcom's motion to dismiss is granted and the complaint is dismissed for lack of subject-matter jurisdiction." The FSIA is the ground, and footnote 3 at line 218 confirms the forum non conveniens argument was never reached.
3. **D07** (S.D. Ohio 2:25-cv-1239, filed 09/11/26):
   - Line 25: the motion was "filed by Defendants Oriental Export Corporation ('OEC India') and OEC USA, Inc."
   - Line 83: "Defendants now move to dismiss… under… 12(b)(2) and 12(b)(6), as well as the doctrine of forum non conveniens."
   - Line 210: "Defendants next argue that the Court should dismiss this case pursuant to the doctrine of forum non conveniens."
   - Line 449: "GRANTED as to OEC USA's request for dismissal under Rule 12(b)(2), and OEC USA is DISMISSED without prejudice."
   - Line 451: the forum non conveniens request was denied as to OEC India, which stays in the case, so OEC India is excluded.
4. Exclusions:
   - **D04**, Royal Caribbean (RCCL): its forum non conveniens request was granted ("we dismiss Bagga's Complaint under the doctrine of forum non conveniens", line 121). It was dismissed on that ground, not a different one.
   - **D02**: the UAE (subject-matter jurisdiction), the Alp defendants and Besson (personal jurisdiction) and Vidino (12(b)(6)) were all dismissed on other grounds. But forum non conveniens appears only in the Azima citation (line 321), and no defendant's request for it is recorded.
   - **D06**: forum non conveniens appears only in an Atlantic Marine quote (line 74). The §1404(a) transfer motion and DUAL's 12(b)(6) motion were both denied, so no defendant was dismissed.
   - **D05**: it appears only as the plaintiffs' waiver in the consent judgment (lines 53 and 165).
   - **D08**: it appears only in the Chick Kam Choo discussion (line 81). The motion to reopen was denied, and the earlier Rhode Island motion was to transfer, not to dismiss.
   - **D01**: it appears only in a Gulf Oil citation (line 513). This is an insurance appeal with no dismissal motions.
5. All eight rulings are dated or filed between Sept 11 and Sept 15, 2026.

sufficient_documents:
- D03 and D07 give the two positives.
- All eight are needed to confirm nothing else qualifies. D04 (forum non conveniens granted) and D02 (dismissed on other grounds, no forum non conveniens request) are the key decoys.
- No single document is enough. The docs/ originals match text/: the counts for "forum non" (32) and "dismiss" (115) are identical.

searches:
- Exact terms: "forum non", "non conveniens", "conveniens", "FNC", "forum-non" and "inconvenient forum" across text/ and docs/; "dismiss" counts in both.
- In D02: "forum|convenien|alternative|comity|abstain". In D07: "Doe|other defendant". In D01: "dismiss|venue|transfer".
- Coverage: I read D02–D08 in full and D01 in targeted parts (header and pages 1–6, lines 495–534, plus the grep hits). I did not read question.txt.

readings/gaps:
- **Narrow reading (weaker):** leave out OEC USA, because the court calls forum non conveniens "OEC India's request" (line 451) and only weighs OEC India's burden. That would make the answer Ofcom alone. I think this is weaker because the opinion twice says "Defendants" (both movants) asked for forum non conveniens dismissal of "this case".
- **D02 gap:** the UAE's motion included unstated "other legal grounds" (line 167), and the motions against the first complaint raised "multiple grounds". The opinion never records a forum non conveniens request. This is unresolved, not proof there was none, so I excluded D02.
- **D01:** only partly read. It is low risk, since it is a coverage appeal with no dismissal motions.
- **Difficulty risk:** searching the question's own term surfaces both qualifying passages, and D03 line 97 nearly answers Ofcom by itself. The work across documents is adding up two independent findings and ruling out decoys, not linking facts between documents.
- **Contamination:** none detected. The injected git status listed only filenames (other tasks and memory files), with no content about this question, its key or earlier solves. No CLAUDE.md or memory content appeared in my context. I can't confirm how I was launched (fork or not, or whether omitClaudeMd was set).

Packet: D:\Agents\Docket\tasks\aq-01540\runs\q03-r0-v2-66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2\shortcut\text\ (D03.txt, D07.txt, D04.txt, D02.txt are the key files)
