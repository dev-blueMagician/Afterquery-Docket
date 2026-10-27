# Shortcut auditor (packet shortcut), q02 rev 0 (2026-10-08)

Role: shortcut-auditor, fresh context, input = root, packet path, question text.
tested_sha256: d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07

Raw return (verbatim):

answer: about $29.1 for each Aged Bankruptcy Group claimant. These are the claimants who get no automatic payment. The figure is $2,882,000 ÷ 98,990 points = $29.114 per point, and each of them has 1 point.

verdict: clear

shortest_path:
1. D03 (Doc. 176, preliminary-approval memo, July 6, 2026), pages 4–6, gives the settlement terms:
   - "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 … Members of the Aged Bankruptcy Group will not receive these automatic payments."
   - "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims."
   - "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point." Each payment is the member's points divided by the total points of all claimants.
   - Footnotes 2–3 define both groups by Jaffe's April 22, 2025 Supplemental Report.
2. D07 (Doc. 157, decertification memo, Dec. 2, 2025), pages 4–5, gives the group sizes from the April 2025 (Thomson Reuters) run:
   - "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters". This is the No Bankruptcy Group.
   - "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years". This is the Aged Bankruptcy Group.
   - It also gives the class list as "57,233 individuals".
3. Calculation:
   - Total points = 3 × 20,891 + 36,317 = 62,673 + 36,317 = 98,990.
   - $2,882,000 ÷ 98,990 = $29.114 per point.
   - An Aged claimant has 1 point, so gets $29.1.

sufficient_documents: D03 and D07 together; neither is enough alone. D03 has no count for the Aged group or the whole class. Dividing its "approximately $2,100,000" by $100 only gives an estimate of about 21,000 No Bankruptcy members. D07 has none of the settlement terms. No alternative document supplies the group counts.

searches:
- I read all seven text files (D01–D07) in full.
- Grep on docs/ found the key figures in the same source files as the text/ copies (20,891; 36,317; 57,233; 22,212; 35,941; 920; 2,882; 2,100,000).
- Concept searches covered "pro rata", "automatic payment", "No Bankruptcy Group", "Aged Bankruptcy", "valid claim", "class list" and "approximately".
- D01, D02 and D06 are sealing rulings, and D04 is the Daubert ruling. None of them is relevant.
- D05 (certification) has only June 2022 sample figures that could mislead: 270 with no bankruptcy and 311 stale, plus extrapolations.
- No document gives a per-claimant amount for a scenario where everyone claims, so there is no complete-answer lookup.
- I did not open question.txt, notes or any other packet. The session context showed git-status file names from another task (aq-00949), but nothing about this question, so there was no contamination.

readings/gaps:
- Robustness: D07 is inconsistent with itself. 20,891 + 36,317 = 57,208, not the stated 57,233. Every way of combining the April figures still gives $29.1:
  - 20,891 with 57,233 − 20,891 = 36,342 Aged: 99,015 points, $29.107.
  - 57,233 − 36,317 = 20,916 No Bankruptcy with 36,317: 99,065 points, $29.092.
- Weaker readings that give a different answer:
  - Using about 21,000 No Bankruptcy members from the approximate $2.1M reserve gives $29.0 (29.018 with 36,317 Aged, 29.043 with 36,233). This is a rounding risk, but the exact 20,891 sits in the same D07 passage a reader must use anyway.
  - Using the March 2025 counts (22,212 and 35,941) gives 102,577 points and $28.1. That is wrong because the settlement groups are tied to the April report.
  - Working out the valid-claim money yourself as $8,310,000 − $2,770,000 − $308,000 − $50,000 − $210,000 − $2,100,000 gives $2,872,000 and then $29.0. The question's "court's figure" wording rules this out.
  - The $350 figure is the plaintiff's estimate at typical claim rates and is a decoy. Splitting the money equally per head (about $50.4) ignores the points.
- Difficulty risk: this is a simple cross-document join. You match the group definitions to D07's April-report counts, then do a weighted division. It is not a shortcut.
- Gaps: the settlement agreement (Doc. 172-2) and Jaffe's reports are not in the packet, so exact group counts in the agreement itself cannot be checked. There were no extraction gaps; all files were read in full.

Files:
- D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\shortcut\text\D03.txt
- D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-v2-d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07\shortcut\text\D07.txt
