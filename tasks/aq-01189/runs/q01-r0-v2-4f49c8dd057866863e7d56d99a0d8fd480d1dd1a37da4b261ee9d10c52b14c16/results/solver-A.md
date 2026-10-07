# q01 rev 0 - blind solver A (fresh blind-solver context, packet solver-1)

Date: 2026-10-05. tested_sha256: 4f49c8dd057866863e7d56d99a0d8fd480d1dd1a37da4b261ee9d10c52b14c16
Task message: workspace root, packet path solver-1, exact question text only.

Raw return (verbatim):

answer: **47.0%** (493 million pounds sold in 1H 2026 ÷ 1,050 million pounds projected for full-year 2026)

confidence: high

path:
1. **When the stake was raised (D04, 2Q 2026 release, filed 2026-07-23).**
   - Line 921: "In May 2026, FCX increased its ownership interest in Cerro Verde from 55.08% to 55.66%."
   - Line 39 confirms it happened in the quarter: "During second-quarter 2026, FCX purchased 2.0 million shares of Cerro Verde common stock in the open market for $107 million…"
   - The footnotes at lines 457 and 511 agree: "prior to May 2026 it was 55.08%."
   - The cash flow statement at line 717 shows "Acquisition of additional ownership interest in Cerro Verde | (107)".
2. **The projection in force in May 2026 (D03, 1Q 2026 release, dated April 23, 2026, line 227).** "Copper sales from South America operations are expected to approximate 1.05 billion pounds for the year 2026." No later projection existed until D04 on July 23, 2026, which is after May. D03 says nothing about a planned Cerro Verde purchase.
3. **South America copper sales in the first six months of 2026 (D04).**
   - The South America operating table, line 205, reads "Sales|245|265|493|540". The columns are 2Q26, 2Q25, 6M26 and 6M25, so 6M26 is 493.
   - The selected operating data table, line 485, reads "Total South America|507|539|493||540||". The 493 is the 2026 six-month sales figure; it splits into Cerro Verde 398 and El Abra 95.
   - The product revenues schedule, line 1423, also gives "Copper sales (millions of recoverable pounds)|493".
   - Cross-check: Q1 sales of 248 (D03 lines 209 and 431) plus Q2 sales of 245 (D04 line 431) equal 493.
4. **Same basis.** Both figures are consolidated South America volumes in millions of recoverable pounds. D03 line 227 calls them "FCX's consolidated copper sales volumes from South America operations."
5. **Calculation.** 493 ÷ 1,050 = 0.469524, or 46.952%, which rounds to **47.0%**.
6. I checked the key lines (the 1.05 and 1.0 billion projections, "Total South America" 248 and 493, and the May 2026 sentence) against the original files in docs/, and they match. These sources are .txt files, not PDFs, so there were no page images to check.

minimal_documents: D03 + D04.
- D03 is the only source for the 1.05 billion pound projection that was current in May 2026. D04 does not repeat the April South America estimate; its "April 2026 estimate" mentions are consolidated only.
- D04 is the only source for the May 2026 timing and the six-month total of 493. You could rebuild 493 from D03's 248 plus D04's 245, but D04 is needed either way.
- D01 and D02 (BHP) contain no Freeport, FCX or Cerro Verde references and can be dropped.

readings:
- **Disclosure date instead of transaction date: 49.3%.** If "at the time it raised" is taken to mean the July 23, 2026 release that reported the increase, the projection is D04 line 221: "expected to approximate 1.0 billion pounds for the year 2026." That gives 493 ÷ 1,000 = 49.3%. This is weaker, because the stake was raised in May, before the July projection existed.
- **FCX's net share instead of consolidated figures:** this doesn't work. The projection is only given on a consolidated basis, so there is no matching net figure to divide by.

gaps:
- The documents don't give an exact day in May for the purchase. Any May date falls between the April 23 and July 23 releases, so the answer doesn't change.
- I did not read everything in full. I read D03 lines 1–240 and 410–440, and D04 lines 1–240, 415–514, 700–729, 905–944 and 1405–1429. The rest of the D03/D04 schedules I covered only through targeted searches (Cerro Verde, South America, 1.05, 1.0 billion, April 2026, 493). I covered D01 and D02 only by searching for Freeport, FCX and Cerro Verde, with no matches.

contaminated: no. I received only the workspace root, the packet path and the question. I did not read question.txt or any notes or metadata.

Files read (as reported by the solver): solver-1\text\D03.txt, solver-1\text\D04.txt, solver-1\docs\ (both Freeport originals)
