# aq-03169 - lean candidate sketches

Current target: medium (user, 2026-10-12: no Easy slot, "target medium and high"); measured platform success pending.
Round 2 of 3 (round 1: i01 quick-test too easy, 2026-10-12). Hooks in notes/hooks.md; each sketch file holds its quotes, ambiguity and necessity checks and calculation.
All five passed the mechanical sketch screen (`docket_agent.py screen`, 2026-10-12): structure and quotes only.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h1: years of tender wins, at the rate Deloitte's five-year target assumes, to bring the Big Four within ICAEW's 65-company individual cap; 7 years | Gold sits between the two short cuts (6 by scaling, 8 without the 11 audits already held); 7 on every stated base; D02 and D06 each give a number found nowhere else | promoted to q01. Rev 0 difficulty Run 1 (2026-10-12): "Answerable without the documents", the no-document attempt guessed "7 years" from the rounding instruction; no solver with documents ran. Rev 1 adds a second ask (gold "260 audits and 7 years"); the form passed its blocking checks on it and raised two advisory warnings; "Run again" would not start (P2). Rev 2 rewords the question for the warnings (P3), checked, hand-over rewritten. User, 2026-10-12: "too easy for quick test" (wording not stated). q01 dropped, hook closed (P4) |
| i02 | [i02](sketches/i02.md) | h2: share of the FTSE 250 tenders Deloitte expects that others must win for BDO's 2023 limit; 100% to the nearest ten | 98-101% on every base, so only the nearest ten is safe; short cuts give 90% and 110% | closed with i01: same Deloitte paragraph, same offset, measured too easy |
| i03 | [i03](sketches/i03.md) | h3: audits BDO's limit and ICAEW's cap leave to others, as multiples of Grant Thornton's realistic maximum; 2.2 and 1.8 | Base-free; same-label decoy "10-20% ... within three to four years"; three documents each give one number | not recommended: plain arithmetic, the family the quick test solved; untested |
| i04 | [i04](sketches/i04.md) | h4: first yearly cut at which Nexia's sliding cap is tighter than ICAEW's individual cap allows; 4 | Same answer under both readings of "5% per annum"; look-alike 65 / 65% | not recommended: plain arithmetic, the family the quick test solved; untested |
| i05 | [i05](sketches/i05.md) | h5: Deloitte's and Grant Thornton's auditor-switching rates; 46.4 points | Plain, two lookups | not recommended: plain arithmetic; untested |
| i06 | [i06](sketches/i06.md) | h10: measures Deloitte rates High for costs and Low for benefits whose benefits in Grant Thornton's Annex 2 include auditor independence; tendering and rotation reform, the audit-only split, joint audits | Seven candidates, three qualify; one sits under the merit heading, one qualifies only through "All other benefits of 1 above"; decoys break the link and the all-clients prohibition; D02 and D04 each irreplaceable | user, 2026-10-12: "both of i06 survived, others not tested" (quick test, chat only). Promoted to q02 rev 0 with the explicit wording: difficulty Run 2 "In band — Easy tier", Low 2/5 (P6), below target. q02 rev 1 keeps the two tables and asks two lists whose members sit partly in the annex and partly in the reply; form Checks on rev 1 failed "Short answer" on the gold's format (P7); rev 2 reformats the gold and the tail only: difficulty Run 3 "Between levels", Low 0/5, Medium 4/5 (P8). Rev 3 removed "anywhere in its response": difficulty Run 4 "Answer not supported", Low 0/5, Medium 1/4, high model 0 of 3 with every document (P9). Rev 4 names the scope as "Grant Thornton's response" and changes nothing else: difficulty Run 5 "In band — Hard tier", Low 0/5, Medium 1/7, High 3/6 (P10). Submitted by the user at Hard, 2026-10-13; q02 frozen, later returns in notes/feedback-q02.md |
| i07 | [i07](sketches/i07.md) | h11: Deloitte's ratings of the measure Hermes calls a de facto break-up; Medium, High, Low | Every row reached through "break-up", "prohibit" or "split" is High, Low, High; definition at D05 L67 only | quick-test sketch |
| i08 | [i08](sketches/i08.md) | h12: the one merit-group measure Deloitte rates High/Low, and the country cited as further along; tendering and rotation reform, Poland | Decoy joint audits / France; group condition stated in the question | quick-test sketch, after i06 and i07; shares its first part with i06 |

Round 2 came from two independent authors (fresh context, documents only; neither saw these notes) plus the caller re-reading
both tables line by line. Both authors found h11; one found h10 and the other h12. Their rejected lists are summarised in notes/hooks.md.

Wording a paraphrase of q02 rev 4 must keep: "High for costs and Low for benefits", "Grant Thornton's response" as the thing that says and
warns (not "Grant Thornton" alone, and not "anywhere in its response"), "less concentrated", "reduce or destabilise audit quality"
(both verbs), both asks in this order, "if any", and the word "alphabetically" in the last sentence. Measured scope ladder (P8, P9):
"say anywhere in its response" = Between levels (Medium 4/5); "does Grant Thornton say" = Answer not supported (the high model
answered from the annex table, 0 of 3). No word about where to look may be added. The gold stays a plain comma list.

Historical (q01 dropped): wording a paraphrase of q01 rev 2 had to keep: both asks in this order, "individual cap on each Big Four firm", "the four hold in total",
"years of tender wins", "yearly rate", "Deloitte's five-year market-share target", "within that total", "nearest whole year".
Dropping "of tender wins" lets the one-to-two-year go-live lag in; dropping "individual" lets the collective 60% in; dropping the
first ask brings back the lone "7 years" the closed-book attempt guessed; "in total", "on each Big Four firm" and
"market-share" answer the form's two advisory warnings on rev 1 (P3).

Gold-form rule applied from P1 (notes/feedback-index.md): no sketch here goes forward with a lone whole number under about
twenty, or one of about ten round values, as its answer. i04 ("4 cuts", one of five) and i02 ("100%", one of about ten at
the nearest ten percent) had the same fault; both sketches now carry a first ask with a document-only number (2026-10-12:
i02 "240 audits and 100%", i04 "74.3% and 4 cuts"). i03 (2.2 and 1.8) and i05 (46.4 points) did not need it.

Not sketched, with reasons, in notes/hooks.md (h6-h9 and "Closed for stated reasons").
