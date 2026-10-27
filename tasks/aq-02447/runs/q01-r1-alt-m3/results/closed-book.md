# Closed-book probe, q01 rev 1

- Date: 2026-10-09
- Question (verbatim): How many distinct five-character ECCNs named in the 2026 UAE rule's § 742.6(a)(6)(iii)(B) were absent from the January 2023 Macau rule's § 742.6(a)(6)?
- Agent: fresh closed-book-solver (claude-opus-5-5), question only, no tools.
- Bound to: q01 rev 1, tested_sha256 0ffd9a958e8f87a92868fffa693ccf66aba0eaa768e2cbacc1aef69a19a891c6

## Return (as delivered, which the harness had reformatted; kept word for word apart from the shortened contamination note)

answer: unknown
confidence: low
basis: I can't recall the wording of § 742.6(a)(6)(iii)(B) in the 2026 UAE rule. I partly recall the January 2023 rule that extended the October 2022 advanced computing and semiconductor controls to Macau. Its § 742.6(a)(6) probably named 3A090, 4A090, 3B090, 3D001, 3E001, 4D001, 4D090, 4E001, 4A994 (as 4A994.l) and the base ECCNs of the .z items (3A001, 4A003, 4A004, 4A005, 5A002, 5A004, 5A992, 5D002, 5D992). Of the ECCNs created after 2023, 4E091 (AI model weights, added in 2025) is the most likely to be missing from the 2023 list. Some technology ECCNs, such as 5E002, might also be missing. I can't confirm any of this without the two documents.
contaminated: minor (harness git status and email; no document text, answers or hints).
forced_guess: 2, forced_probability: 0.2, basis: The 2023 list probably already covered most advanced computing ECCNs, so only one or two later additions such as 4E091 are likely missing from it.
