# Removal probe without Doc 4 (D05), q03 rev 0 (2026-10-08)

Role: fresh blind-solver; packet tasks/aq-01541/runs/q02-r0-alt-m6/shortcut (byte copy of q03's prepared
solver-1 packet minus docs/uscourts_paed_2_22_cv_00048_4.txt, ids renumbered D01-D06 contiguously: old
D06 -> D05, old D07 -> D06; question.txt is q03's). Input: root, packet path, question text, plus the
request for an unforced answer and a forced best guess with probability.
tested_sha256 (question fields): 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf

Raw return (verbatim; the probe's D03/D04/D05/D06 are the renumbered Doc 7/Doc 3/Doc 5/Doc 6):

answer: not answerable from this packet. Only the first share can be computed: 20,891 / 57,233 = 36.5%. The packet does not give the June 2022 certification-stage count or its split, so the difference cannot be computed.

Forced best guess (separate from the packet answer): 26.5 percentage points. I put about a 5% chance on this being right. It uses the only June 2022 split in the packet (Wodzinski's 50 files, see reading 3), and those files are probably not the group the question means. If the intended figure is in the certification memorandum, my central guess would be a small positive gap (roughly +0 to +6 pp), but no single 0.1-point value there gets more than about 1%.

confidence: high that the packet cannot settle the question; low on the forced guess.

path:
1. When Trans Union moved to decertify. D06 p.6: "Trans Union moved for decertification on July 31, 2025. (See Doc. No. 139.)" D05 p.2 lists Jaffe's April 22, 2025 Supplemental Report (Doc. 139-4) as an exhibit to that motion.
2. The class list at that time. D06 p.4: the Thomson Reuters search "resulted in the elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals." This is consistent with the March 2025 counts: 22,212 + 35,941 = 58,153, and 58,153 − 920 = 57,233.
3. Members with no bankruptcy record found at all. D06 p.4: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters." D06 p.5: "36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years." D03 p.5 n.2 defines the "No Bankruptcy Group" by the April 22, 2025 report as "no locatable public record of a bankruptcy."
4. Share A = 20,891 / 57,233 = 36.502%, which rounds to 36.5%. Using 57,208 (20,891 + 36,317) as the base gives 36.518%, also 36.5%. Note that the two groups add up to 25 fewer than 57,233, and the packet does not explain why.
5. Share B (June 2022 class members at certification) is not in the packet. The only June 2022 numbers are in D04 p.8: Wodzinski "was supplied with 22,141 primary files from June 2022." These were Trans Union internal files, and the court said her sample did not screen for whether a report was sold or whether a government-held record existed (D04 p.14). Every document in the packet cites the certification memorandum (Doc. No. 116) for the certification-stage facts, for example D06 p.2 "(Doc. No. 116 at 6–7)". That memorandum is not in the packet.

minimal_documents: D06 is enough for Share A (D03 confirms the group definition). No document in the packet supplies Share B; it would need Doc. No. 116, the August 1, 2024 class-certification memorandum. I checked the other documents as substitutes: D04 has only Wodzinski's sample, and D01, D02, D03 and D05 have no class-member counts.

readings:
1. Using the sum of the two groups as the denominator: Share A is still 36.5.
2. Using the March 2025 list instead: 22,212 / 58,153 = 38.2%. I rejected this because the April 2025 list replaced it before the motion.
3. Treating Wodzinski's 50 June 2022 files as the comparison group. D04 p.17: "For 24 of the 50 primary files ... she did not locate any secondary files" with a bankruptcy record, and a paralegal "found public bankruptcy filings ... for 19 of the 24." That leaves 5 of 50 with no record found anywhere, or 10.0%, giving 36.5 − 10.0 = 26.5 pp. I did not adopt this because these are "primary files," not class members, and the paralegal matched on name, address and last four SSN digits rather than the nine-digit SSN.
4. Using only the 24 unmatched files: 5 / 24 = 20.8%, giving 15.7 pp. This is weaker still.

gaps:
- Missing: the June 2022 class-member count from the certification stage and how it splits between no record and a record more than ten years old (expected in Doc. No. 116).
- Unexplained 25-person difference between 57,233 and the sum of the two groups.
- Coverage: I read D01 to D06 in full. For the docs/ sources I only searched them to confirm their numbers match the text files. There are no layout files or PDFs in this packet, and I did not read question.txt.

contaminated: no. The automatic git-status context listed file names from an unrelated task (aq-00949) but nothing about this question or its answer.

Packet path: D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-alt-m6\shortcut\text\ (D06.txt, D04.txt, D03.txt)

Caller note: unforced "not answerable"; forced +26.5 pp (p 0.05); central guess a small positive gap. Off the gold (-10.0). Doc 4 is needed.
