# Current bundle checkpoint

- Goal and user constraints: user 2026-10-06: "work on AQ-01320 ... difficulty_target to at least medium". New work uses difficulty_target: medium.
- Verification target / measured platform tier: medium / pending (no platform result).
- Platform page (capture 2026-10-06 11:38): slots Hard 0/2 · Medium 0/3 · Easy 0/1; 9 submissions left; quick tests 0 of 10; difficulty runs 8 of 8.
- Bundle: 12 earnings-release 8-K exhibits, three per company. Capture AQ-01320_2026-10-06_1138.txt (.txt format, sha256 3ba30293...), "12 of 12 read in full", no gaps; split with docket-e1's .txt support; map complete (notes/doc-map.md, all read in full).
- Id map (local -> platform): D01=Doc 5 CMG 1Q26, D02=Doc 6 CMG 2Q26, D03=Doc 4 CMG 4Q/FY25, D04=Doc 10 DRI FQ2 (Dec 18 2025), D05=Doc 11 DRI FQ3 (Mar 19 2026), D06=Doc 12 DRI FQ4/FY26 (Jun 25 2026), D07=Doc 8 WEN 1Q26, D08=Doc 9 WEN 2Q26, D09=Doc 7 WEN 4Q/FY25, D10=Doc 2 YUM 1Q26, D11=Doc 3 YUM 2Q26, D12=Doc 1 YUM 4Q/FY25.
- Phase: handed over 2026-10-06 (quick-test batch + q01 rev 2 form fields); awaiting user's platform results.
- Questions:
  - q01 rev 2 (checked; origin claude; target medium): Darden FY2026 outlook as it stood when Q4 began (D04 reported EPS 10.62-10.82, midpoint 10.72) vs actual 10.44 -> -$0.28; decoy D05's own later outlook -$0.01; adjusted routes +$0.04/+$0.02. Run q01-r2-v2-a97d3ba0...: A match, B match (high), closed-book misses (-$0.08 guess), audit clear; review ready, medium (marginal): Too easy ~15-20%, Easy ~40-45%, Medium ~25%, High ~8-10%, Too hard ~5%. Status checked. Floor 0 FAIL, 2 WARN (origin; D05 quoted not listed, explained). Rev 0 review: revise (form mechanics); rev 1 review: ready, medium (marginal) ~25% Medium / ~50% Easy.
- Sketches (notes/ideas.md): i04 Darden ETR sibling (-0.4 pp; closed-book guessed -0.5; submit at most one of q01/i04). i02 Yum Pizza Hut reorganization tax benefits $202M (Easy-leaning; closed-book unknown). i03 dropped (closed-book reached 25.3%). Author fallbacks A-i04 Chipotlane share, A-i05 Bahama Breeze count (Too-easy leaning).
- Verdict on bundle: caller, independent author and both reviews agree only Darden's outlook editions support a fair Medium mechanism (Wendy's editions identical; Chipotle qualitative; Yum no annual outlook).
- Rounds used: 1 sketch round (caller + author); q01 revisions: 2 (rev 1 signed wording + reasoning fix; rev 2 decoy lines removed).
- Next action (after hand-over): record the user's quick-test / difficulty-check words verbatim under q01 Feedback log and Blind solve; hand-over said: quick-test q01 (and optionally i04, i02); if q01 survives, run the difficulty check on q01 exactly as frozen; Save passage for the Doc 10 table row; mark only Doc 10 and Doc 12.
- Runtime: Claude Code, Opus 5.5; fresh subagents via Agent tool (blind roles omitClaudeMd).
