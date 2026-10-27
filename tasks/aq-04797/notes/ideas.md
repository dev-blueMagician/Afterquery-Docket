# aq-04797 - lean candidate sketches

Current target: medium (user 2026-10-14: no Easy slot, "target medium and high"); measured platform
success pending. Page at capture: quick tests 0 of 15 used, up to 5 sketch slots; slots Hard 0/5 ·
Medium 0/1 · Easy 1/0, so a difficulty check may start at the Medium or the High level. Origin of all
sketches: claude (i05 from an independent question-author run, adopted after re-verification).
Quick test round 1 (user, 2026-10-14, verbatim): "i05, i01, i02 survived, others not tested".

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i05 | [i05](sketches/i05.md) | h5: cells ending CV charge at or below B0005's C/100; PANASONIC NCA (Doc 7 Methods, 0.03 A on 3.03 Ah) is the late member; B0018 (1.35 Ah) out | Open: NASA-only reading (B0006, B0007). Docs 1 and 7 each supply a member; delete-and-guess passes | survived; q01 rev 0 Run 1 (2026-10-14): "Too easy", Low — · Medium — · High 3/3; q01 dropped, hook retired for the high model (notes/feedback-index.md F1) |
| i01 | [i01](sketches/i01.md) | h1: R² on cells each model never saw, Doc 6 0.977 - Doc 5 pre-fine-tuning 0.959 = 0.018 (Doc 5 fine-tuned on its own test cells) | Open: Doc 5's headline 0.977 (answer 0.000); "the model" read as the final network only. Docs 5 and 6 each supply a figure | survived; q02 rev 0 Run 2 (2026-10-14): "Too easy", Low — · Medium — · High 3/3; q02 dropped, hook retired for the high model (feedback-index F2) |
| i02 | [i02](sketches/i02.md) | h2: nominal capacity of NASA cells Doc 1 models and Doc 4 does not, 3.35 Ah (B0007 late in Doc 4) | Open: Doc 4 read as B0005 only (5.35); B0018 at 2 Ah (4.00). Doc 4 is an exclusion source | survived; not written up. Not recommended for a High-level run: its deciding step (B0007 in Doc 4 section 3.4) is a sweep for a cell ID, the kind q01's run showed the high model clears |
| i03 | [i03](sketches/i03.md) | h3: MAE in amp-hours, B0005 / CX2 = 1.08 (ranking flips from percent) | Open: Doc 4's "MAE (%)" as a relative error | not tested; every step named by the question; not recommended for a High-level run |
| i04 | [i04](sketches/i04.md) | h4: Doc 4 B0005 0.7462 - Doc 6 per-cell mean 0.4254 = 0.32 (printed 0.561 is per dataset) | Open: Doc 6's held-out-cell test (0.608) as the scope | not tested; every step named by the question; not recommended for a High-level run |

Withdrawn 2026-10-14: i06, i05 with ", if any," after "cells" (same hook as q01, which the high model
solved 3 of 3).
Set review: q01 (Docs 1, 7) and q02 (Docs 5, 6) share no passage. i02 and q01 share Doc 1 line 65;
i03 and i04 share Doc 4 Table 2 and Doc 6's MAEs; i04 and q02 both turn on Doc 6's held-out results.
Independent authors (2026-10-14): A (results/protocols) found nothing outside h1-h4; B (definitions/rules)
found i05 and nothing else with an unpointed step. Rejected families: notes/hooks.md.
