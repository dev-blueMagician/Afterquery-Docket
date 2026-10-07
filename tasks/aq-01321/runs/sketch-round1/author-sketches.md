# Independent question-author sketches (other families), raw return, 2026-10-06

Fresh question-author agent (Claude Code, claude-opus-5-5), target medium, told the caller's three
sketches (Microchip inventory, calendar-window revenue, onsemi midpoint claim) and the rejected
families; no files written by the agent. Its ids i05/i06 collide with caller sketches and are
renumbered by the caller: author i05 -> i07 (TI twelve-month R&D+SG&A ratio), author i06 -> i08
(onsemi buybacks over free cash flow). Return summarized with key lines verbatim; full text below.

---

I found no fair Medium mechanism of the measured kind (a later same-label value that only timing rules out) beyond your sketch 1. Every outlook here covers only the next quarter. The only intra-quarter guidance updates (Microchip, D05 L8-12) have no partner edition, and no event in a later release picks out an earlier outlook. Below are the two strongest new designs. Each has a derived answer and a printed, answer-shaped decoy, but I predict both lean Easy, so quick-test them before spending a difficulty run. I used i05/i06 because hooks.md already assigns i04 to h4. Writer origin for both: `claude`. Nothing below is validated.

**id: i05 (caller: i07)**
- difficulty_target: medium
- question (34 words): "For the twelve months ended June 30, 2026, what was Texas Instruments' combined research and development and selling, general and administrative expense divided by its revenue, expressed as a percentage to two decimal places?"
- answer: 20.26%
- facts: D12 = Doc 7 L62 R&D "|Research and development (R&D)|521|491|2,083|1,959|" (Q4 2025, Q4 2024, 2025, 2024; headers L56-58), L63 SG&A 446 / 446 / 1,860 / 1,794. D10 = Doc 8 L62-63 R&D 510 / 517, SG&A 464 / 472 (Q1 2026 / Q1 2025). D11 = Doc 9 L62-63 R&D 535 / 527, SG&A 490 / 485 (Q2 2026 / Q2 2025); L220 twelve-month revenue "$19,453" under L213 "For 12 Months Ended June 30". Decoy D11 L17 "Over the past 12 months we invested $3.9 billion in R&D and SG&A" (D10 L17 and D12 L17 print "$3.9 billion" for their own windows).
- documents: Doc 7, Doc 8, Doc 9 (all three necessary).
- dependency: year 2025 (3,943) minus first half 2025 (2,001) plus first half 2026 (1,999) = 3,941; / 19,453. No document prints a twelve-month R&D or SG&A figure; July-September 2025 has no release. Removal: without Doc 7, 20.05% (Doc 9 prose) or 20.12% (Doc 8 prose rolled forward); without Doc 8, 20.27% (2025 numerator), 20.34% (Q1 2026 = Q1 2025) or 20.05%; without Doc 9, unanswerable.
- selected_levers: Exact table vs rounded prose; State the rounding.
- lever_checks: rounded prose 3,900 / 19,453 = 20.05% (lever bites). One decimal fails (2025-numerator route and Q1-equality guess both round to 20.3); at two decimals the 2025-numerator route is 0.01 from the gold. Other wrong routes: 2025's own ratio 22.30%; twelve months to March 21.30%; with acquisition charges 20.43%; with 2025 restructuring and acquisition charges 21.04%; first half 2026 only 19.43%; Q2 only 18.76%. Revenue rebuilt from rounded quarterly prose still gives 20.26%.
- arithmetic_check: calc1.py (Decimal, half-up). Route A 3,943 - 2,001 + 1,999 = 3,941; Route B July-September 2025 R&D 518, SG&A 457, quarters 975 + 967 + 974 + 1,025 = 3,941; revenue 17,682 - 8,517 + 10,288 = 19,453; 3,941 / 19,453 = 20.2591%.
- shortcut_search: "R&D and SG&A", "Research and development", "Selling, general and administrative", "12 Months", "Trailing" across all 12; only rounded prose twelve-month figures; no ratio printed; overview not checked.
- tags: Cross-document join; Temporal alignment; Aggregation.
- unresolved: TI's 2025 R&D and SG&A were printed in January 2026 (recall risk; run a removal probe without Doc 7). Tier guess: too easy ~25%, Easy ~45%, Medium ~20%.
- draft reasoning: Doc 7 2,083 + 1,860 = 3,943; Docs 8 and 9 first halves 517 + 472 + 527 + 485 = 2,001 (2025) and 510 + 464 + 535 + 490 = 1,999 (2026); 3,943 - 2,001 + 1,999 = 3,941; 3,941 / 19,453 = 20.26%; "$3.9 billion" is rounded, 3,900 / 19,453 = 20.05%.

**id: i06 (caller: i08)**
- difficulty_target: medium
- question (33 words): "Over onsemi's four fiscal quarters ended July 3, 2026, what was the cash it paid to repurchase common stock divided by its free cash flow, expressed as a percentage to one decimal place?"
- answer: 97.7%
- facts: D09 = Doc 10 L253 "|Repurchase of common stock|(450.2)|(325.0)|(204.1)|(1,377.6)|(654.1)|" (headers L227-229). D08 = Doc 12 L232 "(344.8)|(345.7)|(302.3)|(690.5)|(602.4)" (fourth = six months ended July 3, 2026); D08 L370-373 LTM "Free cash flow|$372.4|$485.4|$217.2|$425.4|$1,500.4"; FCF definition L426. Decoys: D08 L21 "Share repurchases of $332 million, bringing year-to-date shareholder returns to approximately 105% of free cash flow"; D07 L19 "approximately 160% of free cash flow"; D09 L25 "returned 100% of our annual free cash flow".
- documents: Doc 10 and Doc 12 (Doc 11 repeats Q4 2025 and Q1 2026; unlisted).
- dependency: 325.0 + 450.2 + 690.5 = 1,465.7; / 1,500.4. Without Doc 10, Doc 11's treasury-stock change gives 339.4 -> 98.6%; without Doc 12, Doc 11's twelve months to April gives 120.5%.
- lever_checks: wrong routes 105% (105.5% computed), 107.5%, 97.1% (2025), 160%, 120.5%, 96.9% ($332M highlight). "Cash it paid" rules out $332M. One decimal forced (97.69 vs 97.71 split at two decimals).
- arithmetic_check: calc2.py 1,465.7 both routes; LTM FCF 1,500.4; 97.687% -> 97.7%.
- unresolved: Q3 2025 buyback ($325M) was a November 2025 headline (recall risk for Doc 10's necessity). Reviewer may query $332M vs cash flow. Tier guess: Easy ~45%, too easy ~30%, Medium ~15%.

**Considered and rejected:** which companies beat the top of their guided range (giveaway or guessable count); ADI's new Empower exclusion (two bases, 39/40 bps split); onsemi accelerated depreciation (D08 contributes only a zero; keyword-searchable); TI CHIPS benefit for Jul-Sep 2025 (public Q3 2025 family); TI H1 2026 FCF ex-CHIPS (caller h7); TI "5-cent benefit" beat (signposted, one lookup and one operation); rankings with Microchip/TI near-ties (13.232% vs 13.223%; 8.002% vs 7.999%); onsemi twelve-month non-GAAP operating margin 19.76% (no printed decoy); Microchip September 2025 quarter (public; D04 L40's 40.6% approximation); onsemi other income/expense sign check (+18.3; on sketch 3's path).

**Hazard:** D02 L328 and D03 L337 print ADI's January 31, 2026 quarter revenue as $3,160,063 while D01 prints $3,160,263, so ADI's twelve-month revenue has two defensible values.
