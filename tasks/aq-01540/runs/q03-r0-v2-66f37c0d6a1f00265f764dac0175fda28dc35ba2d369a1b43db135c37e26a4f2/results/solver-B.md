# q03 rev 0 blind solver B (fresh blind-solver agent, packet solver-2, 2026-10-08)

tested_sha256: 66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2
Prompt: workspace root, packet path, verbatim question only.

Raw return:

answer: Ofcom (the UK Office of Communications, in D03) and OEC USA, Inc. (in D07)
confidence: high for Ofcom; medium-high for OEC USA (see readings)

path:
1. All eight rulings fall in the window: D01 (5th Cir.) filed 09/14/2026; D02 filed 09/15/26; D03 filed and dated 09/15/26; D04 entered 09/14/2026; D05 filed 09/11/26; D06 filed 09/14/26 (dated Sept. 11); D07 filed 09/11/26; D08 filed 09/14/26.
2. D03 (4chan v. Ofcom, D.D.C. 25-cv-2880). Ofcom is the only defendant. Line 97: "Ofcom also argues that the Court should dismiss the complaint on the grounds of forum non conveniens and international comity. Id. at 23, 25. The Court addresses only Ofcom's first argument and concludes that it lacks subject-matter jurisdiction." Line 250: "Ofcom's motion to dismiss is granted and the complaint is dismissed for lack of subject-matter jurisdiction" (immunity under the Foreign Sovereign Immunities Act, FSIA). So Ofcom asked for an FNC dismissal and got a different ground. It qualifies.
3. D07 (ATP v. Oriental Export Corp., S.D. Ohio 2:25-cv-1239). Line 25: "the Motion to Dismiss filed by Defendants Oriental Export Corporation ('OEC India') and OEC USA, Inc." Line 83: "Defendants now move to dismiss ... under ... 12(b)(2) and 12(b)(6), as well as the doctrine of forum non conveniens." Line 210: "Defendants next argue that the Court should dismiss this case pursuant to the doctrine of forum non conveniens." Line 449: "The Motion is GRANTED as to OEC USA's request for dismissal under Rule 12(b)(2), and OEC USA is DISMISSED without prejudice." OEC USA joined the FNC request and was dismissed for lack of personal jurisdiction. It qualifies.
4. Exclusions, checked one by one:
   - OEC India (D07): its FNC request was denied (line 451), and it stays in the case. Only Count IX and some damages were dismissed under 12(b)(6), so it was not dismissed from the case.
   - RCCL (D04): it asked for FNC dismissal and got it. Line 121: "we dismiss Bagga's Complaint under the doctrine of forum non conveniens." Same ground, so excluded.
   - D02 defendants (UAE; the Alp defendants Alp, Diligence, Brero, Badal and Cavin; Besson; Vidino): all were dismissed, on subject-matter jurisdiction, personal jurisdiction or 12(b)(6). But the opinion never says any of them asked for FNC dismissal. Its only FNC mention (line 321) describes the Azima appeal: "The D.C. Circuit later reversed on forum non conveniens grounds." The UAE's "other legal grounds" (line 167) are not specified.
   - D06 (DUAL, Chaucer, Houston): they moved to transfer under §1404(a), not to dismiss for FNC. The transfer motion and DUAL's 12(b)(6) motion were both denied, and nobody was dismissed.
   - D05: in a consent judgment, the plaintiffs waived an FNC defense. The defendant, Lewis Machining, never moved on FNC.
   - D08: FNC appears only in the discussion of Chick Kam Choo. The defendants asked to reopen the case and for an injunction.
   - D01: an insurance-coverage appeal. FNC appears only in a citation, "Gulf Oil ... (forum non conveniens)" (line 513).

minimal_documents: D03 and D07 are enough to identify both qualifying defendants. Ruling out everyone else takes the other six: D04 is the main contrast (FNC granted), and D02 is the main distractor (dismissed on other grounds, no FNC request shown). No replacement source in the packet covers D03 or D07.

readings:
- The D07 conclusion phrases the request as "OEC India's request for dismissal under the doctrine of forum non conveniens" (line 451). If the FNC request is credited only to OEC India, the answer is Ofcom alone. I prefer the joint-movant reading because lines 25, 83 and 210 attribute the motion and the FNC argument to both "Defendants." The court's later per-defendant wording reflects that OEC USA had already been dismissed (line 284).
- If "dismissed" were stretched to cover partial claim dismissals, OEC India might be added (Count IX was dismissed under Rule 9(b)/12(b)(6)). That is strained, because OEC India remains a party.
- If one assumed the D02 foreign defendants raised FNC among their "variety of grounds," they would be added. The text does not support that.

gaps:
- I did not read D01 in full (I read lines 1–60 and 495–524). I did not read every line of D02 (I read 1–180, 160–179, 310–330 and 400–570). Both were covered by case-insensitive searches for "forum non conveniens", "non conveniens", "veniens", "forum", "convenien", "comity", "alternative forum", "Gulf Oil" and "Piper". D01 had one FNC hit and D02 one, each explained above.
- D03, D04, D05, D06, D07 and D08 were read in full.
- The sources are text files (method "text"), so there were no PDF pages to inspect. I saw no extraction problems that matter here.
- D03 line 97 says "Defendants move" (plural), but the caption lists a single defendant. This looks like a drafting slip and does not change the answer.
- I did not read question.txt.

contaminated: no. Only the packet path and the question were provided. The environment's git status listed unrelated task files but no answer or reasoning for this question.
