# Removal probe: q03 rev 0 without D07 (Doc 1, ATP v. Oriental Export) — packet q01-r0-alt-n5/solver-2 (rebuilt for q03), fresh blind-solver agent, 2026-10-08

tested_sha256 (q03 rev 0): 66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2
Packet: copy of the frozen q03 solver-1 packet without D07; remaining ids D01-D07 (old D01, D02, D03, D04, D05, D06, D08), originals renamed opinion_01-07 (runs/probe-plan-q03.json).
Prompt: workspace root, packet path, verbatim question, plus "First give the answer you would give from this packet (it may be "cannot be determined"). Then give a forced best guess at the complete answer, with your probability that it is exactly right."

Raw return:

answer: From this packet: **the UK Office of Communications (Ofcom)**. It is the only defendant in the packet that qualifies. But the question covers eight rulings and the packet has only seven (D01–D07), so whether the list is complete cannot be determined. Forced best guess at the complete answer: Ofcom alone, with about a 0.45 probability that this is exactly right. The main risk is the missing eighth ruling.

confidence: high that Ofcom qualifies; low that it is the complete list.

path:
1. D03 (4chan Community Support LLC v. UK Office of Communications, D.D.C. No. 25-2880, filed 09/15/26). The caption names one defendant, "THE UK OFFICE OF COMMUNICATIONS a/k/a OFCOM" (lines 16-21).
   - Line 97: "Ofcom also argues that the Court should dismiss the complaint on the grounds of forum non conveniens and international comity… The Court addresses only Ofcom's first argument and concludes that it lacks subject-matter jurisdiction."
   - Footnote 3, line 218: "Ofcom has raised other non-merits grounds for dismissal, such as forum non conveniens."
   - Line 250: "Ofcom's motion to dismiss is granted and the complaint is dismissed for lack of subject-matter jurisdiction" (FSIA immunity). It asked for forum non conveniens and was dismissed on another ground, so it qualifies.
2. D04 (Bagga v. Royal Caribbean Cruises Ltd., S.D. Fla., 09/14/26). The cruise line asked for a forum non conveniens dismissal (line 35) and got one on that same ground. Line 121: "we dismiss Bagga's Complaint under the doctrine of forum non conveniens." Excluded.
3. D02 (Nada v. UAE, D.D.C., 09/15/26). The UAE was dismissed for lack of subject-matter jurisdiction; Alp, Diligence, Brero, Badal, Cavin and Besson for lack of personal jurisdiction; Vidino for failure to state a claim (line 564). The opinion's only forum non conveniens mention is about a cited case, Azima: "The D.C. Circuit later reversed on forum non conveniens grounds" (line 321). The motions are described only as "a variety of grounds" (line 117), and none is said to have sought forum non conveniens dismissal. Excluded on the text.
4. D06 (Sethmar v. DUAL North America et al., D. Kan., filed 09/14/26). The defendants moved to transfer under 28 U.S.C. § 1404(a) based on a forum-selection clause, not to dismiss (line 60). Every motion was denied (line 260) and no one was dismissed. Excluded.
5. D05 (Shenzhen En De Chuang v. Lewis Machining, M.D. Ga., 09/11/26). This is a consent judgment. The only forum non conveniens mention is the plaintiffs waiving that defense (lines 53, 165). Excluded.
6. D07 (Deaton v. Johnson, N.D. Tex., 09/14/26). Forum non conveniens appears only in a description of the Chick Kam Choo case (line 81). The defendants' earlier request was a venue transfer in the District of Rhode Island (line 42). This ruling denies their motion to reopen. Excluded.
7. D01 (Megalomedia v. Philadelphia Indemnity, 5th Cir., 09/14/26). An insurance appeal that affirms the judgment. Forum non conveniens appears only as a citation to Gulf Oil v. Gilbert (line 513), and no party is dismissed. Excluded.

minimal_documents: D03 is enough to show Ofcom qualifies. D04 and D06 rule out the nearest look-alikes; D02, D05, D07 and D01 rule out the rest. Proving the list is complete would need all eight rulings, and one is missing. I found no other document that could stand in for D03.

readings:
- If seeking to enforce a forum-selection clause counts as asking for forum non conveniens: DUAL, Chaucer and Houston (D06) asked for a transfer rather than dismissal and were not dismissed, and Royal Caribbean (D04) was dismissed on forum non conveniens itself. The answer is still Ofcom.
- A very loose reading might count the D07 Johnson-firm ("JLF") defendants, since they sought a venue transfer and the claims were later dismissed on res judicata. That is not a forum non conveniens dismissal request, and the dismissal came in a 2024 order, not this ruling. Rejected.
- If the D02 defendants raised forum non conveniens in briefs the opinion doesn't describe, they might qualify. The packet doesn't support that.

gaps:
- The question says eight rulings; the packet has seven, so one ruling was never available and could add a qualifying defendant.
- All files are text extractions (manifest method "text", no PDF pages), so there was no original PDF to check.
- I read D02–D07 in full. D01 I read in part (lines 1-119, 425-439, 500-519, 580-604) and covered the rest with keyword searches for forum non conveniens, dismiss, venue, forum and transfer, which turned up only citation-level hits.

contaminated: no. The automatically attached git status listed unrelated file paths from other tasks, but nothing about this question, its answer or its sources. I read only this packet's text/ and docs/ folders.

Files: D:\Agents\Docket\tasks\aq-01540\runs\q01-r0-alt-n5\solver-2\text\D03.txt (decisive), plus D02.txt, D04.txt and D06.txt in the same folder (for the exclusions).

Caller note: unforced "cannot be determined" (seven-ruling answer Ofcom alone); forced Ofcom alone, p 0.45. Both differ from the gold. Result: misses.
