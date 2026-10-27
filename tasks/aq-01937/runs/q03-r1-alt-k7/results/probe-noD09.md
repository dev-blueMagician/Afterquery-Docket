# q03 rev 1 removal probe, left out: D09 (Doc 9) - packet q03-r1-alt-k7/solver-1 (renumbered: D10->D09), 2026-10-08
Question identical to rev 1 (tested_sha256 993076f2a58c67f3f234ea9ca851b4cd79a01733398a02ccf2428d51fec31b03).
Agent id a099a2e8c80a16ea6. Transcript audit (audit_transcript2.py): 23 tool call(s) (Glob, Grep, Read, handback), all inside the packet (clean).
Verbatim return follows.

answer: cannot be determined. The packet has 2Q25 GAAP FX trading services revenue on the basis where other fee revenue is $127M ($393M, D09). It has no 1Q25 figure on that basis. The only 1Q25 figure, $362M (D05/D06), uses the original basis, under which 2Q25 FX was $431M.

forced best guess: 8.6%, about 30% probability. Calculation: (393 − 362)/362 = 8.56%. This assumes the reclassification left 1Q25 FX unchanged, which the packet does not support. 2Q25 FX was cut by $38M under the new basis, so the true like-for-like figure is more plausibly about 19–21%.

confidence: high that the documents do not settle it.

path:
1. D09 (2Q26 release, 16 Jul 2026), revenue table, text\D09.txt lines 216–226. The original docs\stt_ex991_2026-07-16.txt lines 221–231 match.
   - Columns are "2Q26 1Q26 2Q25".
   - "Other fee revenue 138 107 127"
   - "Foreign exchange trading services 494 435 393"
   - "Total fee revenue $3,188 $2,960 $2,719"
   - Footnote, lines 93 and 255: "GAAP FX trading services revenue of $393 million in 2Q25 included a notable item … $3 million … adjusted 2Q25 FX trading services of $390 million."
   - D09 has no 1Q25 column and no six-month or year-to-date data. A search for 1Q25, "March 31, 2025", "six months" and YTD found nothing.
   - Its only "recast" note (line 374) is about Software services ARR, not revenue lines.
2. D06 (2Q25 release), text\D06.txt lines 250–261, columns 2Q25 / 1Q25 / 2Q24:
   - "Foreign exchange trading services 431 362 336 19.1 28.3"
   - "Other fee revenue 66 32 48"
   - "Lending related and other fees 61 67 62"
   - "Front office software and data 169 158 152"
   - "Management fees 562 562 511"
   - Total fee revenue $2,719 (2Q25) and $2,570 (1Q25).
   - D07 (lines 204 and 209: FX "416 431 374", other fee revenue "79 66 125") and D08 (lines 208–219) still use this original basis.
   - D05 line 252 gives 1Q25 FX "362".
3. Matching the two versions of 2Q25 (total fee revenue is $2,719M in both):
   - Other fee revenue: 66 + 61 (lending related and other fees) = 127.
   - Software services: 169, equal to front office software and data.
   - Management fees: 562 → 600 (+38).
   - FX trading services: 431 → 393 (−38).
   - Servicing fees (1,304) and securities finance (126) are unchanged.
   - So the new basis moved $38M of 2Q25 FX revenue into management fees. The 1Q25 amount moved is not disclosed anywhere in the packet. The 1Q26 release, which would show restated 1Q25 figures, is not included.
4. Calculations:
   - Original basis: (431 − 362)/362 = 19.06%, which rounds to 19.1% (printed in D06).
   - Mixed bases: (393 − 362)/362 = 8.56%, rounds to 8.6%.
   - If $38M was also moved in 1Q25: 69/324 = 21.3%.
   - If the 1Q25 shift was proportional (×393/431): 19.1%.

minimal_documents: D09 + D06. D06 gives the 1Q25 figure of $362M and shows 2Q25 FX changing from $431M to $393M. Alternative: D09 + D07 + D05. For the 8.6% guess alone: D09 + D05, or D09 + D06.

readings:
- (a) Original basis, the printed 19.1%. This contradicts the $127M clue, because under the original basis other fee revenue was $66M.
- (b) Mixed bases: 8.6%.
- (c) Excluding notable items, mixed: (390 − 362)/362 = 7.7%. The word "GAAP" in the question rules this out.
- (d) Assumed restatement of 1Q25: 21.3% (same dollar shift) or 19.1% (proportional shift).

gaps:
- Missing fact: 1Q25 FX trading services revenue on the new basis, which would appear in the 1Q26 release or a recast exhibit.
- Coverage:
  - D09: read in full; revenue table checked against the original.
  - D06: lines 1–330 read.
  - D05: lines 60–284 read.
  - D08: lines 60–259 read.
  - D04 (2025 SSGA presentation): read in full; not relevant.
  - D01 (2024 UBS presentation): read through its end at about line 42; not relevant.
  - D02, D03, D07: covered only by targeted searches.
- There are no PDFs or layout files; all documents are .txt. Text extraction matched the original for D09.

contaminated: no. The automatically attached context included a git status listing file names from an unrelated task (aq-00949). It contained no answer, reasoning or source hint for this question. I could not check from inside the session how I was invoked.

Key files:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-alt-k7\solver-1\text\D09.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-alt-k7\solver-1\text\D06.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-alt-k7\solver-1\text\D05.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01937\runs\q03-r1-alt-k7\solver-1\docs\stt_ex991_2026-07-16.txt
