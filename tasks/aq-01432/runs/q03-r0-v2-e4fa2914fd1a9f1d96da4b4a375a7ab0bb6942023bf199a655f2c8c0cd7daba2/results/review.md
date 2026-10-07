# q03 rev 0 - independent review (fresh question-review subagent), 2026-10-07

Raw return as received (closing file list removed):

Recommendation: ready for q03 (correctness and fairness only). Weak fit for the Medium target (most likely Too easy; Medium ~4%). Two fixes outside the fingerprint; the Doc 9 risk has no fair fix.

q03 (rev 0; tested_sha256: e4fa2914fd1a9f1d96da4b4a375a7ab0bb6942023bf199a655f2c8c0cd7daba2)

gold_verified: yes (rebuilt from the source texts).
- The guide's list: Doc 11 (D10) lists seven behaviours under "Misleading promotional claims" (L77–79), with no "for example" (unlike the theme paragraphs at L75 and L91), so the list is complete.
- Scripted check: all 32 banned practices extracted from Doc 9 (D09 L397–763), each guide clause scored by shared words; five clauses have one clear best match (special offer → 7, cease trading/move premises → 17, free → 23, won a prize → 22, statutory rights → 11); the runners-up are exactly the decoys (21 for the prize clause, 29 for the rights clause).
- The two "bait" terms share no words with Doc 9 ("bait" only in D10 and a US rule title in D02); matched by ordinary meaning: practice 5 is the lure price the trader can't supply (£9 headphones example); practice 6 refuses to show or supply "with the intention of promoting a different product". The guide names two separate practices; 5 and 6 are the only two that begin "invitation to purchase … at a specified price", so a reader treating the terms as one idea still has to place both; dropping 5 would leave a guide item with no practice.
- 22 vs 21: "tell someone they have won a prize" = practice 22's "false impression that the consumer has already won"; Doc 10 (D08) L159 uses the same wording for "paragraph 22"; 21 (a competition not awarding prizes) does not qualify.
- No clause maps to two practices: 20 concerns market or availability information, not an offer deadline; 18 sits in the illegal-products theme; 29 (contractual rights, unanswered correspondence) is filed under after-sales care.
- Practice N = paragraph N: six anchors agree (D09 L573 (13); D09 notes 39 and 112 (12, 13, 30); D08 (22, 27); D04 note 4 (12, 25)).
- Order: script-confirmed ascending 5, 6, 7, 11, 17, 22, 23.

outcome: A: match; B: match (high confidence, separate fresh packets, each packet's question and all 11 texts byte-identical to the snapshot; both rejected 21 for the right reason; only file names from git status seen).

closed-book: misses ("7, 16, 20, 21 and 32", low; wrong set and a wrong single shift; only 7 overlaps).

necessity:
- Doc 11 (D10): only source of the theme's members (Doc 9 L95 names other themes; no document pairs this heading with practices). Without it the probe forced 21, 22, 23 (p 0.12), alternatives also wrong; 11 is an unexpected member and 21 an expected non-member, so a rebuild misses either way. Platform risk ≤ 10%.
- Doc 9 (D09): only source of numbers 5, 6, 7, 11, 17, 23 (D08 fixes only 22; D11 and D04 give 12, 13, 25 in other themes). Locally needed; platform: findings 2–3.
- No smaller set; D08 corroboration only (same CMA207 collection).

shortcut: clear. Shortest route: "misleading promotional claims" → D10 L79 (seven clauses, no numbers) → match each in D09 chapter 3 → sort. No passage pairs a theme with paragraph numbers; the capture's bundle overview names no theme.

source_assessment: no gaps (snapshot none; intake 11/11 complete, zero gap characters; capture "11 of 11 read in full"; all 21 evidence quotes word for word in the capture's own Doc 11 and Doc 9 text).

difficulty: easy (local fit only; below Medium). The question copies the theme heading (one search finds the inputs); five of seven mappings nearly word-for-word; sibling q01 used the same mapping step and was Low 5/5 Too easy; q03's possible misses (adding 21, slipping on a bait term, missing the third sentence's rights item) are scattered single-attempt errors — can produce Easy (Low 1–3/5); Medium needs Low 0/5 (a trap catching every attempt), which this design lacks. Odds: Too easy ~55%, Easy ~37%, Medium ~4%, Between levels / Too hard / Answer not supported ~4%.

verdict: ready (local correctness and fairness only; status at most checked; no platform evidence).

findings:
1. Levers record fix: "Ordered answers" does nothing (ascending numeric order is a format instruction and never changes which items qualify); remove it from the levers field and the lever checks (outside the fingerprint; no re-test). "Who belongs where" decoy 21 works (taking it gives eight items); decoys 20 and 29 are weak.
2. Doc 9 document-check risk ~30–45% if a run reaches the document check. Simulated reader recalling the 2008 numbering with the five anchors (12, 13, 22, 25, 27): 44 consistent arrangements within two moves, five candidate answer sets; the gold results whenever the moved after-sales item sits at positions 9–11 (right after the language item), the natural grouping and the probe's choice. Direct recall of Schedule 20 also gives the gold. The platform does not force a guess (the local probe's unforced answer was "only 22"), but statute recall is easier to volunteer than the aq-01428 outlook values.
3. No fair change lowers the Doc 9 risk: dropping the Act's name opens the old 2008 numbering reading (Doc 9 note 38), and D04/D11's "practice 12 of Schedule 20"/"Banned Practice 12" would still tie the numbers to the Act; any non-numeric Doc 9 fact changes the question family. Mitigation: mark Doc 9 as "Answer component"; enter the prepared reviewer note only if the check flags it (any edit clears it); the note's claim is accurate after a whole-bundle search; whether a note unblocks a flag on an answer-component document has not been observed.
4. Floor WARNs — explanations adequate: origin (accurate; the tick is the user's decision); empty case (not applicable, the theme always has members); list contract (announcing seven would reveal a one-to-one mapping and disarm decoy 21; advisory, expect it on the form); copied phrasing (four hits on the Act's proper name, needed to fix the numbering; hits land on the Act's mentions in D04, D09, D10, D11, not the answer).
5. Form number rule (by hand): Step 1 no numbers; Step 2 numbers (13, 20, 5, 6, 7, 17, 22, 23, 11) printed in Doc 9; Step 3 repeats them citing Doc 11 and Doc 9 — Doc 11 prints none (6 only in "6 April 2025"), so it passes only if the form checks the cited documents together (as in aq-00949 q05); low risk; if revised for another reason, cite Doc 9 alone. Decoy line 21 and 22 in Doc 9.
6. Set: never submit q03 with sketch i08/j03 (shared theme-to-paragraph path; each would reveal how the other's items map); q02 independent (D04/D03); word overlap with all workspace questions ≤ 0.19, longest shared run 3 tokens; 40 words; no rule-10 trigger phrase.
7. Records: fingerprint recomputed from q03.md equals e4fa2914… (post-prepare lever-check edits outside it); both probe packets drop the right original from text/ and docs/; record this review; Q13 pending.
8. Hand-over: quick-test before a difficulty run (7 of 8 left); ask whether Easy is acceptable (one Easy slot; q02 the other Easy-leaning candidate).
9. Not checkable locally: restricted names, Original question / Not a duplicate, token window, form model checks; "One defensible answer" fails only if two solvers both add 21 (~5%); "Needs two or more documents" carries finding 2's risk.
