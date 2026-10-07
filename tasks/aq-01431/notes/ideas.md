# aq-01431 - lean candidate sketches

Current target: medium (user, 2026-10-06: "you should do difficulty_target to at least medium"); measured platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Round 1 (2026-10-06): caller hooks h1-h9 plus two independent question-author runs (A: independent;
B: from hooks.md, derived-numeric focus). Both authors concluded the bundle has no strong Medium
mechanism (no dated forecast series, ICI asset figures are snapshots not values in force, rule 10
bars author-name answers, most qualitative levers resolve inside one letter). Raw author returns:
runs/sketch-round1/author-sketches.md. All origin: claude.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1 US SIF single-issue ranking (author A-i01) | "In the US SIF Foundation's 2022 figures on ESG fund assets, by how many trillion dollars did the assets addressing the largest single ESG issue exceed those addressing the second-largest single issue?" -> $1.65 trillion | D12 l24 (climate change/carbon 3.45; fossil fuel divestment 1.23); D07 l45 (grouped climate + fossil "combined $4.8 trillion", "by far the most significant"; military/weapons 1.8, tobacco 1.7 "next largest") | Scatter; carve-out + ranking. Decoys 2.22 (fossil as runner-up), 3.00 (4.8 - 1.8), 1.75 (tobacco) | D07 l45 undated (2022 inferred from l23-24); 4.8 vs 4.68 conflict (gold avoids 4.8); "single" signposts the split | screen pass; blind match (1.65, decoys 3.0 and 2.22 rejected); closed-book miss (about 1); kept as q01's sibling phrasing for a quick-test comparison only |
| i02 | h1 variant naming the top issue (caller) | "In the US SIF Foundation's 2022 figures, by how many trillion dollars did assets in funds addressing climate change/carbon exceed assets in funds addressing the ESG issue that ranked second by fund assets?" -> $1.65 trillion | as i01 | Decoy sits in the named input's own sentence (D12 fossil 1.23 -> 2.22); grouped and single rankings both give military/weapons | sibling of i01: never submit both | PROMOTED to q01 (rev 0: A/B match, audit clear, closed-book miss, removal probes 3.00/2.22; review ready, difficulty easy, Medium 6-8%) |
| i03 | h6 reopening -> next MFA letter (author B-i02) | "In 2023 the SEC reopened public comment on its proposed cybersecurity risk-management rules for investment advisers and funds. How many days after that reopening did Managed Funds Association next file a comment letter on the proposal?" -> 68 days | D01 l56 fn 6 (Mar. 15, 2023); D05 l681-690 (June 22, 2023; May 22, 2023; Apr. 11, 2022, newest first) | Temporal alignment; conditional filter. Decoys 99, 128, 371 | appendix completeness (world vs set); reopened deadline may be public | DROPPED: closed-book reached 68 (reopening date + reopened deadline recalled); blind match |
| i04 | securities-loan proposal FR date -> Global PSSL meeting (author A-i03) | "How many days after the SEC's proposed rule on reporting of securities loans was published in the Federal Register did representatives of Global PSSL meet with SEC staff about it?" -> 85 days | D01 l105 (86 FR 69,802, Dec. 8, 2021); D04 l7 (November 1, 2022) + l21 ("3rd March this year") | Scatter; date gap with year inference. Decoys 30, 114, 86 | FR date may be recalled (D01 removal risk) | HELD: blind match 85; closed-book missed (34) but recalled Dec 8, 2021, so the platform document check would likely find D01 not needed; Too-easy profile |
| i05 | climate rule FR-to-FR (author B-i01) | "How many days after the SEC's proposed climate-related disclosure rules for public companies appeared in the Federal Register did the final rules appear there?" -> 717 days | D01 l107 (87 FR 21,334, April 11, 2022); D11 l125 (89 FR 21,668, Mar. 28, 2024) | Scatter; calculate across documents. Decoys 716, 738, 695, 724, 745 | famous rule: general-knowledge risk | DROPPED: closed-book reached 717 (both FR dates recalled); blind match |

Not promoted (author/caller evidence): ICI combined-asset growth (A-i02, B-i04; two labelled
lookups + routine arithmetic, Too easy ~65-75%); agenda forecast vs adoption (11 months; famous
date, decoy ruled out by "climate"); Market Data Infrastructure release-to-FR gap (121 days; two
lookups, public adoption date); tailored shareholder reports (812 days; public dates); climate-rule
petitions count (good remainder trap but single-document D11); joint trade letter signatories
(Chamber vs CCMC identity, guessable, who-cites-whom); equity-proposal count 3 vs 4 (about the
letters); IM Director (Birdthistle/Greiner known from memory); Diversity Washing internals
(single document).

Arithmetic (caller script, 2026-10-06): 3.45 - 1.8 = 1.65; 3.45 - 1.23 = 2.22; 4.8 - 1.8 = 3.00;
3.45 - 1.7 = 1.75. Mar 15 -> May 22, 2023 = 68 days (June 22: 99; July 21: 128). Dec 8, 2021 ->
Mar 3, 2022 = 85 days. Apr 11, 2022 -> Mar 28, 2024 = 717 days (2024 leap year).

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
