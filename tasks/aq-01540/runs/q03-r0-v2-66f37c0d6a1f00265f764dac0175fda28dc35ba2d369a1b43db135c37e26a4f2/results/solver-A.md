# q03 rev 0 blind solver A (fresh blind-solver agent, packet solver-1, 2026-10-08)

tested_sha256: 66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2
Prompt: workspace root, packet path, verbatim question only.

Raw return:

answer: Two defendants qualify: OEC USA, Inc. (D07, S.D. Ohio, Advanced Technology Products v. Oriental Export Corp.) and the UK Office of Communications, "Ofcom" (D03, D.D.C., 4chan Community Support v. Ofcom).

confidence: high for Ofcom; medium-high for OEC USA (see readings).

path:
1. D07 (filed 09/11/26), Case 2:25-cv-1239.
   - Line 25: the motion was "filed by Defendants Oriental Export Corporation ("OEC India") and OEC USA, Inc."
   - Line 83: "Defendants now move to dismiss ATP's Complaint under Federal Rules of Civil Procedure 12(b)(2) and 12(b)(6), as well as the doctrine of forum non conveniens."
   - Line 210: "Defendants next argue that the Court should dismiss this case pursuant to the doctrine of forum non conveniens…"
   - Line 449 (conclusion): "The Motion is GRANTED as to OEC USA's request for dismissal under Rule 12(b)(2), and OEC USA is DISMISSED without prejudice." That is lack of personal jurisdiction, not FNC.
   - Line 451: "The Motion is DENIED as to OEC India's request for dismissal under the doctrine of forum non conveniens."
   - OEC India does not qualify. FNC was denied, and only Count IX and some damages were dismissed (line 453), so it stays in the case.
2. D03 (filed 09/15/26), Case 25-2880.
   - Line 97: "Ofcom also argues that the Court should dismiss the complaint on the grounds of forum non conveniens and international comity… The Court addresses only Ofcom's first argument and concludes that it lacks subject-matter jurisdiction."
   - Line 250: "the complaint is dismissed for lack of subject-matter jurisdiction" (FSIA immunity).
   - Ofcom is the sole defendant, so it is out of the case.
3. Exclusions (all eight rulings were checked):
   - D04 (S.D. Fla., 09/14/26): RCCL asked for FNC dismissal and got it. Line 121: "we dismiss Bagga's Complaint under the doctrine of forum non conveniens." That is the same ground, so it is excluded.
   - D02 (D.D.C., 09/15/26): every defendant was dismissed. The UAE went out on FSIA subject-matter jurisdiction; Alp, Diligence, Brero, Badal, Cavin and Besson on personal jurisdiction; Vidino under 12(b)(6) (line 564). But the opinion never says any of them sought FNC dismissal. FNC appears only in a citation describing Azima (line 321: "The D.C. Circuit later reversed on forum non conveniens grounds"). So none can be shown to qualify.
   - D06 (D. Kan., 09/11/26): defendants moved to transfer under §1404(a), not to dismiss on FNC. FNC appears only in the Atlantic Marine footnote (line 74). All motions were denied and nobody was dismissed.
   - D05 (M.D. Ga., 09/11/26): FNC appears only as the plaintiffs' waiver in a consent judgment (lines 53, 165).
   - D01 (5th Cir., 09/14/26): insurance-coverage appeal. FNC appears only in a Gulf Oil citation (line 513).
   - D08 (N.D. Tex., 09/14/26): motion to reopen and for an injunction, denied. FNC appears only in a Chick Kam Choo citation (line 81).
   - A synonym search ("inconvenien", "alternative/adequate/appropriate forum", "comity", Swiss forum) turned up no other FNC-type requests.

minimal_documents: D03 + D07 support the two names. Showing that no one else qualifies needs all eight, most importantly D04, the FNC-granted case that must be excluded. No document repeats another's facts, so there are no alternative sources.

readings:
- Strict attribution: the D07 conclusion and FNC analysis treat the FNC request as "OEC India's request" (lines 225, 451). If only OEC India is treated as the FNC movant, the answer is Ofcom alone. I prefer the joint-motion reading because the body twice says "Defendants" moved and argued for FNC.
- If "dismissed on a different ground" were read to include partial dismissal of claims, OEC India would still fail, because it was not dismissed from the case.
- If FNC-based forum-selection dismissal (D04) were treated as a "different ground" from FNC, the opinion still rests explicitly on FNC, so RCCL stays excluded.

gaps:
- D02 says defendants moved "on a variety of grounds" and the UAE "on other legal grounds" (lines 117, 167) without listing them. The underlying motions are not in the packet, so an unmentioned FNC request by a D02 defendant cannot be ruled out or confirmed. Nothing in the packet supports one.
- Unread parts: D02 lines 61–87 and 171–317, most of D01 after line 40 apart from the FNC context, and D08 after line 83. These were covered by full-text keyword searches, not line-by-line reading.
- No PDFs or layout files exist (the manifest method is "text"), so no page-level check was possible. The extracted text looked complete.
- I did not read question.txt.

contaminated: no
