# Shortcut auditor (packet shortcut), q01 rev 1 (2026-10-08)

Role: shortcut-auditor, fresh context, input = root, packet path, question text.
tested_sha256: 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a

Raw return (verbatim):

answer: 63.3%

verdict: clear

shortest_path:
1. D03 (Doc. 176, preliminary approval memo, July 6, 2026), text\D03.txt lines 63–73. Only the No Bankruptcy Group (NBG) gets the automatic payment: "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 … Members of the Aged Bankruptcy Group will not receive these automatic payments." "Approximately $2,882,000.00 … is reserved for payments to settlement class members … who submit valid claims." Each payment is the member's points divided by total points, and "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members … one individual pro rata point." Footnotes 2 and 3 tie both groups to "Jonathan Jaffe … April 22, 2025 Supplemental Report."
2. D07 (Doc. 157, decertification memo, Dec 2, 2025), text\D07.txt lines 47–61, gives the counts from that April 2025 report: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters" (NBG), and "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years" (ABG).
3. Calculation: NBG points = 3 × 20,891 = 62,673. ABG points = 36,317. Total = 98,990. NBG share = 62,673 / 98,990 = 0.63312, so 63.3% (about $1.82M of the $2.882M; about $29.11 per point).
4. Cross-check: $2,100,000 / $100 ≈ 21,000 NBG members, which fits 20,891 × $100 = $2,089,100.

sufficient_documents: D03 + D07 together. Neither works alone. D03 has the 3:1 points and identifies the automatic-payment group, but its only group count is the rounded $2.1M reserve and it has no ABG count. D07 has the counts but comes before the settlement, so it has no points structure. No other document gives the April 2025 group counts.

searches: I read the manifest and all of D01–D07 in full (I did not open question.txt). Literal and concept searches: "No Bankruptcy Group", "Aged Bankruptcy Group", "automatic payment", "pro rata", "point", "class list", "percent/%", 20,891, 36,317, 57,233, 22,212, 35,941, "920 individuals", 2,100,000, 2,882,000, 21,000, 98,990, 62,673, and "63.x". I checked the key figures against the docs\ originals and they match the extracted text. No ready-made answer or percentage appears anywhere. D01, D02, D04 and D06 (sealing and Daubert rulings) contain nothing useful. D05 (certification) has only the June 2022 sample.

readings/gaps:
- Using the rounded reserve as the NBG count is the main risk at one decimal. With NBG = 21,000 and ABG = 36,317 the result is 63,000/99,317 = 63.4%. With ABG = 57,233 − 21,000 the result is 63.5%. The exact counts are available and are tied to the group definitions, so 63.3% is preferred.
- The March 2025 counts (22,212 / 35,941) give 66,636/102,577 = 65.0%. They are superseded: the group definitions cite the April 22, 2025 report, which removed 920 people.
- There is an unexplained 25-person gap: 57,233 on the class list versus 20,891 + 36,317 = 57,208. Assigning the gap to either group still gives 63.3% (62,673/99,015 or 62,748/99,065). The two "test subject" records (D07 fn 9) also leave it at 63.3%.
- Wrong readings: counting heads without points gives 20,891/57,208 = 36.5%. Using the June 2022 sample (D05: 270 no-bankruptcy / 311 stale) gives 810/1,121 = 72.3%. The ~$1,000 / ~$350 figures are claims-rate estimates, not a 100%-claim scenario.
- Gaps: the settlement agreement (Doc. 172-2) and Jaffe's April 2025 report are not in the packet. Opt-outs from the 2025 class notice are unknown. Neither changes the result at one decimal on the stated record.
- Difficulty risk: this is a simple two-document join plus a weighted-share calculation. It is not a shortcut, because neither document alone answers the question.
- Contamination: none found. My context had no project instructions, memory, answer key or prior solve outputs. The only extra context was an auto-attached git-status list of file names for an unrelated task (aq-00949), with no content. I cannot verify the invocation mode (non-fork or omitClaudeMd) from inside the session.

Key files:
D:\Agents\Docket\tasks\aq-01541\runs\q01-r1-v2-6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a\shortcut\text\D03.txt
D:\Agents\Docket\tasks\aq-01541\runs\q01-r1-v2-6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a\shortcut\text\D07.txt
