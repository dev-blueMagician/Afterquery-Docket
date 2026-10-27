# Sketch i05 input recall tests (design evidence, not check records), 2026-10-07

Two fresh closed-book-solver subagents, question only, no tools (transcripts: one SubagentHandback call each).
Purpose: before writing up i05 (South Korea's in-operation reactor capacity, a 23-row Table 2 sum of 23,500 MWe in
D15, divided by Koeberg's 1,830 MW in D14 -> 12.84), measure whether a strong model recalls either input exactly,
which would let the platform's Document check reach the gold without that document.

## "What is the combined electricity generating capacity, in megawatts, of the two reactors at South Africa's Koeberg nuclear power station?"

answer: 1,860 MW (net, from two units of about 930 MW each). The gross or installed figure is about 1,940 MW (2 x 970 MW).
confidence: medium
basis: From memory. Reuters and Bloomberg usually call it "the 1,860 MW Koeberg plant." The IAEA's reactor database (PRIS) lists each Framatome PWR unit at about 930 MWe net and 970 MWe gross. Eskom quotes 1,940 MW installed. The only real doubt is whether the question wants net or gross capacity.
contaminated: Partly. The session came with an automatic git-status snapshot listing file names from an unrelated task (aq-00949) and workspace instruction and memory files, plus the user's email address. None of it mentions Koeberg or bears on this answer. I did not read any project instructions, memory contents or documents, and I called no tools other than this hand-off.

Caller: D14 prints 1,830 MW. With a recalled 1,860 or 1,940 MW the ratio is 12.63 or 12.11, not 12.84 (at one
decimal 12.6 or 12.1, not 12.8). Recall alone does not replace D14.

## "As of September 2025, what was the combined capacity, in megawatts electric, of South Korea's nuclear power reactors that were in operation (not counting units that were offline awaiting a licence decision, under construction, or permanently shut down)?"

answer: about 23,350 MWe (net) across 23 operating reactors. This excludes Kori 2, 3 and 4, which were offline awaiting licence decisions; Saeul 3–4 and Shin Hanul 3–4, which were under construction; and Kori 1 and Wolsong 1, which are permanently shut down.
confidence: low
basis: From memory, with no documents. I added up approximate net ratings I recall from PRIS and WNA: 12 OPR1000 units at about 995 each (about 11,945), Saeul 1–2 at 1,416 each, Shin Hanul 1–2 at 1,340 each, Hanbit 1–2 at about 996 and 993, Hanul 1–2 at about 960 each, and Wolsong 2–4 at about 650–669 each. Some per-unit figures are shaky, and some totals I half-remember point lower, so the true figure could be anywhere from about 23,100 to 23,450. If the source uses Korea's gross nameplate ratings instead, the total would be 26,050 − 2,550 (Kori 2–4) = 23,500 MW.
contaminated: no. Only the auto-attached git status and working directory were present, showing file names from an unrelated task and nothing about this question.

Caller: the recalled unit list, the three offline Kori units and the gross nameplate total match D15's Table 2
exactly: 26,050 - 2,550 = 23,500 MWe is D15's in-operation sum. A model without D15 that chooses the nameplate
basis reaches 23,500 / 1,830 = 12.84, the gold, at any precision; the net basis gives 23,350 / 1,830 = 12.76
(12.8 at one decimal, also the one-decimal gold). The question was not asked of this model, so this is a recall
risk for the Document check on Doc 4, not a measured reach.
