# q01 rev 0 - independent review (fresh question-review subagent), 2026-10-06

Raw return as received:

q01 (rev 0; tested_sha256: bf6318cc663cb6fd13da9637862badbeae2227dd95fa338b3a75d1bbcf2f62c4)

Binding: docket_agent.py report recomputes the fingerprint from the current fields and corpus; equal to the snapshot's; all six raw returns cite it. Floor 0 FAIL, 1 WARN (origin: claude, expected). Lever-check notes are not part of the fingerprint.

gold_verified: yes (recounted with a script). D10 L91 is one paragraph under the "Pressure selling" heading (L71 "The banned practices fall into the following themes.") naming seven behaviours. D09 chapter 3 maps them to banned practices 14 (L577), 24 (L679; 31 at L739 also arguable), 27 (L703), 28 (L711), 26 (L695), 30 (L729), 32 (L759); banned practice N = Schedule 20 paragraph N (L573; fn38 L1589; D08 L63, L159). The offences list (L1387-L1391) covers all of Schedule 20; its marker points to fn112 (L1885), and fn39 (L1593) agrees: paragraphs 12, 13 and 30 are not criminal offences. Only the children's item falls in that set: 7 − 1 = 6. Alternative counts: 7 without the footnote; 5 on the five-example reading; 6 if "ordered" maps to 31; 5 using the old 2008 numbering (fn38 rules it out); 6 under the 2008 law itself.

outcome: A: match; B: match (fresh, high confidence, seven minus practice 30; both considered and rejected 5, 7 (any offence) and the practice-31 mapping; the only leak was the harness git status, no answer content). Two uncontaminated matches.

closed-book: misses ("All of them" = 7 ≠ 6); its stated basis recalled the deciding law (children's appeals civil-only), which matters for necessity.

necessity:
- D10 (Doc 11): the only source of which behaviours the guide counts as pressure selling (D09 L95 names the group with no members; D08 only the refusal-to-leave example; D04, D06, D07, D11 and the US documents silent). Probe without it could not answer and guessed 5 (p 0.25). Unflagged risk: D09's run of practices 26-32 (seven items) minus 30 also gives 6, so that rebuild coincides with the gold; the lever checks cite only the 14, 24, 26-32 rebuild (8).
- D09 (Doc 9): the only source of criminal status, the 12/13/30 exclusion and paragraph numbers (remaining documents: civil fines only D10 L57; enforcement without offence status D11; an unrelated 2013-Regulations offence D08 L91). Indispensable inside the bundle, but recalled law reaches 6.
- No smaller valid source set exists.

shortcut: clear. Shortest verified route: D10 L91 (seven items) → fn39 or fn112 ({12, 13, 30}) → practice 30 at L729 (three passages, two documents, one subtraction). No passage or capture overview text prints the count or pairs these behaviours with offence status; "criminal offence" finds inputs, not the answer. The recall route is a necessity risk, not a demonstrated shortcut (the no-D09 probe, asked without forcing, said it could not answer).

source_assessment: no recorded source gaps; intake all 11 complete and matching. D09 L103-L105 alt text (two categories of prohibited practice; platform shows the same text) and misnumbered markers 116-119 (defences/penalties, not fn39/fn112): no effect on premises, gold, exclusions, uniqueness, necessity or shortcuts.

difficulty: easy (local suitability, below the Medium target). Odds: Too easy ~30%, Easy ~50%, Medium ~12%, Hard ~4%, Too hard / answer not supported ~4%. Separately ~30% chance the document check flags a document (D09 ~20-30%, D10 ~10%), plus ~5% closed-book risk.

verdict: ready (local; status checked until the platform confirms; quick test before spending a difficulty run — 8 runs left, each result final for its version).

findings:
1. Universe: seven is the only defensible count (one paragraph under one theme heading; the second sentence keeps the prohibition form "You mustn't"; other themes also span several "You mustn't" sentences, L79; counting five drops part of the theme; all four Opus readers counted seven). Weak eight-item reading: the guide's "pretend that a special offer will finish soon" (L79), which D09's practice 7 example calls pressure (L481), gives 7 — weak because the guide files it under misleading claims. Residual flag risk ~5-10%. Optional cheap fix before any platform run: tie the count explicitly to the guide's whole pressure-selling theme.
2. "For breaching the banned practice involved" excludes the any-offence reading (without it, D09 L1399-L1407 make aggressive practices and misleading actions offences → 7). "Prosecuted" excludes the civil-action reading (fn39: all banned practices "can attract civil action"). D09 uses "prosecution" only in its offences chapter.
3. D09 on the platform: moderate risk; a reviewer note is appropriate (recalled 2008/2024 law gives the same answer for pressure selling, so no wording removes the risk). The fallback note is factually accurate (only D09 states criminal status and the paragraph-30 exclusion, confirmed by search). Do not enter it in advance (any edit clears it).
4. D10 coincidence: record that the 26-32 rebuild gives the gold. If D10 is flagged, the true note fact is that Doc 11 alone sets the theme's membership (e.g. it places the correspondence duty under after-sales care, L95).
5. Form-number rule: Steps 1-3 comply (every numeral 12, 13, 14, 20, 24, 26-28, 30, 32, 39, 112 printed in Doc 9; Step 1 none). Step 4 cites no document, so its "= 6" passes only because "6" appears elsewhere ("6 April 2025"). The unlabelled final line "6 + 1 = 7" could lead "Reasoning reaches the answer" to read 7 as the conclusion. Optional fix: cite Doc 11 and Doc 9 in Step 4 and label the last line as the wrong route citing Doc 9 (reasoning is fingerprinted: new prepare and fresh checks).
6. Tier lean: towards Easy/Too easy — fn112 marked on the very line that states the offence rule, fn39 restates it, both plain sentences; searching "criminal offence" (the natural next step from "prosecuted") lands on both; trivial practice-30 mapping; the wording signals an exception; legal recall can supply the exclusion; "one lookup plus one operation" profile (aq-00949 q03 Low 5/5). Towards Medium — the offences list is a rule-shaped decoy (7) in the reader's path with the exclusion ~500 lines away; the five-example reading (5) is a second wrong route; Medium needs the low model to stop at the offences list every time. Open Easy slot (0/1) if the user accepts Easy.
7. Lever-check corrections: "prosecut" also at D09 L1417; the 26-32 rebuild coincides with the gold; probe packets were renumbered copies with changed header lines, not byte copies.
8. Set: q02 different documents and mechanism, no giveaway; i06 shares the fn112 exclusion (keep out); i08 shares the D10-theme-to-paragraph mapping (prefer not to pair with q01).

Platform-only checks still unknown: Restricted names, Original question (local overlap 0.16, longest shared run 2 words), own-words checks.
