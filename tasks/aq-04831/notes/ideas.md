# aq-04831 - lean candidate sketches

Current target: medium (user, 2026-10-14: "there is no slot for Easy Tier for this bundle, we should target medium and
high"). Page at capture: Hard 0/5 · Medium 0/1 · Easy 0/0, quick tests 0 of 15. Medium has one slot and every captured
run on 2026-10-14 started at the High level, so sketches are audited against the medium and the high solver. Measured
platform success pending. Origin of every sketch: claude.

Round 1, 2026-10-14. Sketch only: no question file, prepare or form until the user reports a quick-test survivor; a
survivor's sentence and short answer go into the question file word for word.

Search behind this round: the caller read all eight texts in full; two independent question-author agents searched the
whole bundle (author A from the climate papers D07, D04, D01, D03; author B from D08, D05, D06, D02). All three found no
design with a step that no word in the question points at, and all three named the same best fair design (i01).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: hazards in D01's VaR data (seven, endnote 5) absent from D04's (five): cyclone wind, surface (flash) flooding | Readings still possible: three to five items if renamed hazards (extreme wind, soil subsidence, forest fire) are taken as new; surface (flash) flooding only if D04's mention of cyclones (l.22) is taken as coverage, rejected by "(other than cyclones)"; cyclone wind only if D04's "floods" is taken as covering flash flooding. Delete-and-guess: neither list recoverable without its document; closed book not reached. Screen clean, 21 words. Unpointed steps: 0 | QUICK-TEST FAILED (user, 2026-10-14: "too easy", no panel): taken as answered by the easier solver; route unread (no capture); dropped |
| A-i02 | hooks.md (author A) | current high-risk dwelling share, 4% (D01, 2020) minus 3 1/2% (D04) = 0.5 ppt | delete-and-guess fails: D04 alone prints 3 1/2% now and +0.5% of properties into high risk by 2050 | dropped, not offered |
| B-i01 | hooks.md (author B) | coal share of commodity exports since 2015, 14% / (2/3) = 21% | delete-and-guess fails on D08 by recall (~14-15% coal share gives 21-22%); 0 unpointed | dropped, not offered |
| B-i02 | hooks.md (author B) | Bowen Basin share of 2017/18 coal exports, 380 / 3 -> 130 Mt | delete-and-guess fails on D08 (380 Mt widely reported); 0 unpointed | dropped, not offered |

Not offered (reasons in hooks.md): h2-h11 and both authors' other hooks (contrived combinations, single-document
features, recallable inputs, rounded "around" bases, or D01 restating D04's parameters).

Round 1 result (user, 2026-10-14, no panel): i01 "too easy". No fair untested sketch remains. Considered after the
result and not offered: h12, the number of dwellings high-risk in 2020 (D01's ~4% times the stock implied by D04's
"0.5 per cent (or 74,000 properties)", ~592,000 -> 600,000 to the nearest hundred thousand): a product of two "around"
figures the documents never connect, with D04's "currently" 3 1/2% as a second share (518,000 -> 500,000), and the
"how many" itself sends any solver to the one share-and-count pair in the bundle (no unpointed step). Release
recommended to the user 2026-10-14; 14 of 15 quick tests and 15 of 15 difficulty runs unspent.
