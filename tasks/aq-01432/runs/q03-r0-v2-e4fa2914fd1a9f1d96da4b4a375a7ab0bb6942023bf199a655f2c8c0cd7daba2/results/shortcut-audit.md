# q03 rev 0 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-07

Raw return as received:

answer: 5, 6, 7, 11, 17, 22, 23

verdict: clear

shortest_path:
1. The brief guide is D10 ("a short guide to the unfair commercial practices guidance"), the only packet document with the heading "Misleading promotional claims" (D10 L77–79): "You must not use bait advertising or bait and switch or pretend that a special offer will finish soon, or that you are about to cease trading or move premises, when this is not true. You mustn't say a product is free when in fact it isn't, or tell someone they have won a prize if that's not true. You mustn't pretend that consumers' statutory rights are a distinctive part of your offer." → seven practices, no paragraph numbers.
2. D09 (CMA207, ch. 3, L397–763) lists "Banned practice 1" to "Banned practice 32" and says "Schedule 20 to the DMCC Act lists 32 banned commercial practices". Banned practice N = paragraph N: BP13 "paragraph 13 of Schedule 20"; fn39 "paragraphs 12, 13 and 30 of Schedule 20" not criminal = the hidden-advertising, reviews and children practices (BP12, BP13, BP30); D08 "paragraph 27" (refusing to leave, BP27) and "paragraph 22" (false impression of having won a prize, BP22); fn38 warns the old CPUTRs Schedule 1 list "has been rearranged and therefore the numbers... differ".
3. Mapping: bait advertising → BP5; bait and switch → BP6 ("with the intention of promoting a different product"); special offer finishing soon → BP7; statutory rights as distinctive → BP11; cease trading or move premises → BP17; prize not really won → BP22 (D08 confirms paragraph 22); "free" → BP23.
4. Ascending: 5, 6, 7, 11, 17, 22, 23.

sufficient_documents: D10 + D09 minimal (D08 only confirms paragraph 22 and the numbering). No single document gives the whole answer (D10 theme without numbers; D09 numbers without themes).

searches: "Schedule 20"; "paragraph \d+"; "banned practice"; bait / switch / closing down / cease trading / statutory rights / distinctive; "promotional claim" / "themes"; the other D10 theme names; patterns for lists of practice numbers. Read manifest.json; D10 and D08 in full; D09 L1–110, L370–770, L1460–1620, L1806–1817; matching lines from D04 and D11 (D11 gives BP12, 13, 25, consistent). No document groups the D10 themes with paragraph numbers — no whole-answer lookup. question.txt not read; git status file names only — no contamination.

readings/gaps:
- Alternative: adding 21 ("Claiming to offer a competition or prize promotion without awarding the prizes described") — weaker (D10's "tell someone they have won a prize if that's not true" matches BP22; D08 ties that wording to paragraph 22).
- Main trap (difficulty risk, not a shortcut): old CPUTRs numbering from memory gives 5, 6, 7, 10, 15, 20, 31 — wrong; D09 fn38 warns about this.
- D09 never uses "bait advertising" or "bait and switch"; BP5/BP6 matched by the standard meaning, which BP6's description and example fit closely.
- D01–D07, D11 not read in full (FTC/US material; D04 paragraph 13 only; D06, D07 reviews and endorsements); keyword searches found no conflicting theme lists. docs/ same as text/.
