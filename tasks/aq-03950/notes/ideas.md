# aq-03950 - lean candidate sketches

Current target: medium or hard (user, 2026-10-13: no Easy slot). Measured platform success pending.
Page state at intake: Hard 0/3 · Medium 0/2 · Easy 0/0; quick tests used 0 of 15; 8 submissions left.
Round 1 (2026-10-13): four sketches, all author-screened and script-screened (0 failures). Quick tests the
same day (user report, no panels): "i01, i04 failed, i02, i03 survived". Quick tests used: 4 of 15 by this
count. No difficulty run yet.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md), written up as [q01](../questions/q01.md) | h1: witnesses at the hearings Rob Roberts MP attended, counted from the report's list. Gold 9 witnesses. | Open reading: witnesses counted from transcript headers (6); the words "listed in the ... report" reject it. Docs 1, 6, 7 each change the count when removed; Docs 2/3, 4, 5 only rule hearings out. | Quick test failed: the easier solver answered it. q01 dropped. Hook h1 closed (scope named: too easy; scope unnamed: an open count). |
| i04 | [sketches/i04.md](sketches/i04.md) | h1, two-member form: Robin Millar's hearings against Rob Roberts's. Gold 6 (15 against 9). | Same open reading (gives 9). Every transcript adds to one of the two counts, so no exclusion-only document. 27 words. A double slip (12 - 6) would also give 6; the two-ask form (9 and 15) avoids that. | Quick test failed: the easier solver answered it. Dropped with i01. |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: witnesses with a role at VisitBritain; Edwards's board seat is stated only by another witness. Gold Pickles, Yates, Edwards. | Open reading: "a role" taken as employment only (Pickles, Yates). Doc 6 necessary; Yates's post from Doc 7 or Doc 1. | Quick test survived. Written up as [q02](../questions/q02.md), rev 0 checked (0 FAIL, 1 WARN), fingerprint cfc8c753...; ", if any," added after the test. Difficulty Run 1 (Version a14913): "In band — Medium tier", Low 0/5 · Medium 2/6. Submitted at Medium (user report 2026-10-13). Frozen; see [feedback-q02.md](feedback-q02.md). |
| i03 | [sketches/i03.md](sketches/i03.md) | h3: witnesses heard remotely in 2022 who had also sent written evidence. Gold Miles-Payne, Yen. | First draft (all hearings, four names) withdrawn by the author: Cadw is a Welsh Government service and the Welsh Government panel's mode is unknown. Open readings: Miles-Payne left out (UK Theatre is her second body); Sweatman added (video-conference line). | Quick test survived. Written up as [q03](../questions/q03.md), rev 0 checked (0 FAIL, 2 WARN), fingerprint 864acc27...; ", if any," added after the test. Next: form Checks, then a difficulty run. |

Held in reserve, not offered: h4 (mean hearings attended by the six MPs who agreed the report, 2.67). It is
fair, but it is a plain tabulation over printed lists, the shape that measured Between levels on aq-03423 q03,
and it shares i01's answer path. Offer it only if the user asks for more sketches.

Rejected with reasons in hooks.md: h5 (report's misattributed quote: one transcript answers it), h6 (campaign
markets: two short lists), h7 (rounded and exact spend give the same ratio), h8 (counterfactual share: method
in the question), h9 (VAT price: two defensible starting points), h10 (page's own period-by-event idea: two
lookups).

Set review: q02 (titles in the report's list plus one answer in Doc 6) and q03 (written-evidence list plus
the Chairs' opening words in Docs 3, 4 and 6) share no answer path, and neither states a fact the other asks
for. Both can be submitted.

A survival at the quick test sets no tier. On aq-03711 a survivor turned out to be an open reading once the
form's "One defensible answer" check ran, so that check comes before any difficulty run here.
