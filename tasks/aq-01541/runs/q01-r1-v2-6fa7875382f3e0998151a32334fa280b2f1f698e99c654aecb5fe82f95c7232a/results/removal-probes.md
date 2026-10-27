# Removal probes, q01 rev 1 (2026-10-08)

Packets: runs/q01-r0-alt-k3/solver-1 (prepared packet minus docs/uscourts_paed_2_22_cv_00048_10.txt = Doc 7,
ids renumbered D01-D06) and runs/q01-r0-alt-k3/solver-2 (minus docs/uscourts_paed_2_22_cv_00048_8.txt = Doc 6).
The q01 question text is unchanged from rev 0, so the rev 0 probe packets were reused with fresh contexts.
tested_sha256 (question fields): 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a

## Without Doc 7 (D03), raw return (verbatim; probe ids are renumbered)

answer: not answerable. The packet has no preliminarily approved settlement in Brooks v. Trans Union. It gives no automatic-payment group, no money set aside for valid-claim payments, no settlement class size and no rule for splitting claim payments.

Forced best guess, kept separate from the answer above: **36.5%**. I put about a 12% chance on it being right.

confidence: high that the packet cannot answer the question.

path:
1. What was asked: the percentage, to one decimal place, of the claim-payment money that would go to members who also get an automatic payment, assuming every class member files a valid claim. Working this out needs four things: the settlement terms, how many members get the automatic payment, the total class size, and whether each valid claim gets an equal share.
2. What the packet covers (text/manifest.json): all six documents are filings in E.D. Pa. case 2:22-cv-00048 (Brooks v. Trans Union):
   - D01: Doc 105, sealing memorandum, 7/30/24
   - D02: Doc 106, sealing order and Appendix A, 7/30/24
   - D03: Doc 114, ruling on Trans Union's expert (Rule 702), 8/1/24
   - D04: Doc 116, class certification memorandum, 8/1/24
   - D05: Doc 154, sealing memorandum, 10/29/25
   - D06: Doc 157, denial of decertification, 12/2/25
3. Searches across text/ and docs/: I searched for settle, automatic, claim form, valid claim, preliminar, net settlement, pro rata, cy pres, distribution, payment, dollar amounts, million, dollar and approv.
   - The only real settlement is the 2003 Clark settlement (D04 pp. 2–3): "In December 2003, Trans Union and Clark reached a class action settlement agreement, which provided that, after May 31, 2004: Trans Union will not disseminate … Credit Reports … that contain on Joint Accounts any reference to bankruptcy … unless …". It only limits future reporting, it is not described as preliminarily approved, and it has no payment terms.
   - The other hits are unrelated: "is not settled" (D06 p. 16, about burden of proof), "payment of the reasonable expenses" (D06 p. 7, Rule 37 sanctions), and the "preliminary" phrases in D01, D03, D04 and D05, none of which concern a settlement.
4. Latest status in the packet: D06 p. 6 says "On the eve of the parties' second scheduled mediation, Trans Union moved for decertification on July 31, 2025". Footnote 3 says the parties were "intending to participate in private mediation". D06 p. 29 says "Trans Union's motion for decertification is denied". No settlement appears anywhere in the packet.
5. Class counts that the forced guess relies on (D06 pp. 4–5):
   - March 2025 search: "22,212 SSNs that had no bankruptcy records returned, and 35,941 SSNs that had one or more bankruptcy filings that predated the applicable consumer report by more than ten years". These add to 58,153.
   - After the Thomson Reuters search: "elimination of 920 individuals … resulting in a class list of 57,233 individuals" (58,153 − 920 = 57,233).
   - "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters"
   - "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years"
   - 20,891 + 36,317 = 57,208, which is 25 short of 57,233. D06 does not explain the gap.

How I got the guess: I assumed every valid claim gets an equal share and that the automatic payment goes to the 20,891 members with no bankruptcy record at all, since theirs is the clearest inaccuracy. Then 20,891 / 57,233 = 0.36502, which is 36.5%. Using 57,208 as the total gives 0.36518, also 36.5%.

minimal_documents: none of the six documents is enough. D06 alone supplies the counts used in the forced guess. No other packet document could replace the missing settlement filing.

readings:
- If "Trans Union's settlement" means the 2003 Clark settlement: still not answerable, because it has no payment terms and is not described as preliminarily approved.
- If the automatic payment instead goes to the older-than-ten-years bankruptcy group: 36,317 / 57,233 = 63.45%, which rounds to 63.5%. Using 57,208 as the total also gives 63.5%.
- Using the March 2025 counts from before the Thomson Reuters search: 22,212 / 58,153 = 38.2%, or 35,941 / 58,153 = 61.8%.
- If claim payments are weighted (for example 2:1 in favour of the automatic group), the result changes entirely: 41,782 / 78,099 = 53.5%.

gaps:
- The settlement filing itself is missing. The docs/ files are numbered _0, _1, _2, _4, _6 and _8. Numbers _3, _5 and _7 are missing, and nothing comes after _8, so the settlement filing is probably outside this packet.
- Unknown: the settlement class size, which members get the automatic payment, how the claim fund is split, and whether the class list changed after the extra expert reports the court allowed in December 2025.
- Coverage: I read all six text/ files in full. I checked the docs/ source files by search only, and they give the same hits. The packet contains no PDFs (manifest method "text", pages null). I did not read question.txt, as the instructions require.

contaminated: no. The automatically attached git status listed files from an unrelated task (aq-00949). Nothing about this question's answer, reasoning or sources reached me. No project instructions or memory contents were in my context.

Packet path: D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\solver-1\text\ (D01–D06.txt and manifest.json)

Caller note: unforced "not answerable"; forced 36.5% (p 0.12). Off the gold 63.3%. Its reading "63.5%" (equal shares, aged group as the automatic group) also differs from the gold.

## Without Doc 6 (D07), raw return (verbatim)

answer: Not answerable from this packet. The packet never gives the size of the Aged Bankruptcy Group in the settlement class, or the ratio between the two groups. My estimate is 72.3%, but only if the June 2022 sample split of 270 no-bankruptcy to 311 stale-bankruptcy members holds for the whole class.
Forced best guess: 72.3%. Probability it is right: about 20%.

confidence: high that the packet can't settle the exact figure; low for the 72.3% estimate.

path:
1. The members who also get the automatic payment are the No Bankruptcy Group. D03 (Doc 176, p.5) says: "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim." It also says: "Approximately $2,100,000.00 of the Settlement Fund is reserved to provide No Bankruptcy Group class members with automatic payments" and "Members of the Aged Bankruptcy Group will not receive these automatic payments." So the No Bankruptcy Group has about $2,100,000 ÷ $100 = 21,000 members.
2. The valid-claim money is a fixed pool shared by points. D03 pp.5–6 says: "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims." Payments are split by "dividing the class member's individual pro rata points by the aggregate total." Also: "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members ... one individual pro rata point."
   If everyone claims, the No Bankruptcy Group's share is 3 × (its members) ÷ (3 × its members + Aged Bankruptcy members). The $2,882,000 cancels out, so only the ratio between the two groups matters.
3. That ratio is missing. D03 footnotes 2 and 3 define both groups by Jaffe's "April 22, 2025 Supplemental Report," but no counts are given. D06 only lists that report as sealed exhibit 139-4, with no numbers. D03's expected payments ("approximately $1,000" and "approximately $350") come from "typical claims rates," which aren't stated, so they can't be used to back out the Aged Bankruptcy Group's size.
4. The only composition data in the packet is a sample. D05 (Doc 116, p.12) says: "at least 270 lacked a public record of a bankruptcy action on PACER ... Additionally, 311 individuals had a public record of a bankruptcy that was more than 10 years old in June 2022." On p.27 it gives "270 of 973 ... or 27.7%" and "311 ..., or 32.0%." (The extraction reads "97330" because footnote marker 30 ran into 973.) The court itself only says "If these proportions hold steady."
   Using that split: (3 × 270) ÷ (3 × 270 + 311) = 810 ÷ 1,121 = 72.26%, which rounds to 72.3%. Scaling it to 21,000 gives the same result: 63,000 ÷ (63,000 + 24,189) = 72.26%.

minimal_documents: D03 alone sets up the calculation and shows the missing fact. D03 + D05 are needed for the 72.3% estimate. No other packet document can replace either one: D01, D02 and D06 are sealing rulings, and D04 is the expert-witness ruling.

readings:
- Using D05's rounded percentages (27.7% and 32.0%): 83.1 ÷ 115.1 = 72.2%.
- Using the court's printed three-month totals: No Bankruptcy 270 + 4,736 + 4,741 = 9,747; Aged Bankruptcy 311 + 5,471 + 4,623 = 10,405. That gives 29,241 ÷ 39,646 = 73.8%.
  - The printed March 2021 figures don't match the stated proportions: 14,816 × 27.7% = 4,104 and 14,816 × 32.0% = 4,741.
  - Correcting them to 4,104 and 4,741 gives 72.2%.
- Assuming the two groups are the same size, which nothing in the packet supports: 75.0%.

gaps:
- The settlement-class count for the Aged Bankruptcy Group, or the total class size, is not in the packet. It would probably be in Jaffe's April 22, 2025 report, the settlement papers (Doc 172-1/172-2) or the decertification ruling, and none of these is included.
- The 270 is a lower bound ("at least"), and the June 2022 sample predates the 2025 analysis that defines the groups.
- The $2,100,000 and $2,882,000 figures are both "approximately."
- The sources are text-only (method "text"), so there are no PDF pages to check.
- Coverage: I read text/D01–D06 in full and spot-checked the matching passages in docs/ for D03 and D05; they match.
- Some side inconsistencies don't affect the answer:
  - The fee is called "one-third" in one place and "30 percent" in another.
  - The listed amounts add up to $8,320,000, against a fund of $8,310,000.
  - D02's order is dated "July 2021" but was filed in 2024.

contaminated: no. I did not read question.txt. The automatically attached git status showed only file names from an unrelated task (aq-00949), with no content from this question.

Relevant files:
D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\solver-2\text\D03.txt
D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\solver-2\text\D05.txt
D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\solver-2\docs\uscourts_paed_2_22_cv_00048_10.txt
D:\Agents\Docket\tasks\aq-01541\runs\q01-r0-alt-k3\solver-2\docs\uscourts_paed_2_22_cv_00048_4.txt

Caller note: unforced "not answerable"; forced 72.3% (p 0.20). Off the gold 63.3%.
