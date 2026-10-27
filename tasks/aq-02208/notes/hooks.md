# aq-02208 - cross-document hooks

Caller inventory, 2026-10-08 (origin: claude). Target medium (hard where supported); the user
says the bundle has no Easy slot. Locations are `text/Dnn.txt` lines; Doc N = Dnn.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D02 162-220 proposed coordination-request data (group 7 a-d at 195-199); D04 197-295 final registration, coordination and post-coordination lists | Proposed coordination items required of no licensee in the final procedures: distance to nearest aircraft landing area; natural formations/structures shielding the antenna (D02 198-199, absent from every other document) | What changed between versions; match then exclude | Moved, not dropped: elevation of ground and overall height to tip (D04 213-214 fixed/base registration), > 5 MHz explanation (D04 205 single attachment); suborbital-only exemptions (D04 122, still required of orbital launches); "if applicable" items | Long lists; a solver diffing only coordination lists answers four or five items; possible form "too vague" block if both form solvers take the four-item group | sketch i01 |
| h2 | D04 155 three centre frequencies (2,364.5 / 2,370.5 / 2,382.5 MHz, only here); D03 139-140 5 MHz without justification; D03 143-150 / 376-378 mask for > 1 MHz | Edge of the 60 dB zone above the highest historic launch-telemetry frequency at the widest no-justification bandwidth: 2,382.5 + 0.5 x 5 + 1.0 = 2,386.0 MHz | Calculate across documents; apply rule to case | Wrong routes: <= 1 MHz breakpoints (2,388.0), start of zone (2,385.5), another centre frequency | One formula plus one lookup; likely solved by the low model | hold i02 |
| h3 | D02 28 comment deadline Jan 22, 2025; D03 27 effective Apr 7, 2025; D04 296 + header May 2, 2025 (+30 days = June 1, 2025) | Date gaps 75 days / 55 days | Calculate across documents | Adoption Dec 23, 2024 / release Dec 31 / FR Mar 7 as decoys | Plain date gaps measured too easy elsewhere; D04 47 cites the Third R&O's FR date, so "30 days after publication" inference rebuilds Apr 6/7; a 30-day comment period rebuilds Jan 22 | park |
| h4 | D02 77 "at present includes" two bands; D03 27 Apr 7, 2025; anchor dates D02 28 / D04 31 | MHz under part 26 rules in effect on an anchor date (175 vs 210) | Temporal alignment (edition in force) | 210 if the Dec 23, 2024 adoption is taken as effect | Anchor rarely discriminates; effectiveness inferable from FR date; fails Document check | reject |
| h5 | D05 271-274 cost model | Net annual savings from unrounded operands 6,878,592 -> $6.9 million vs printed "at least $6.8 million" | Exact table vs rounded prose | 6.8 printed | Single document | reject (one source) |
| h6 | D01 319/446 $183M (2023 IPD); D06 183 $193,000,000 | Change in UMRA threshold | Same series, right edition | none | Two lookups plus one ratio; public and recallable | reject |
| h7 | D01 726-735 (437.21(b)(1)(i) and (iv) revised); D06 358-363 (only (b)(1)(i) revised again) | Paragraph revised by both FAA rulemakings | Match then exclude | 450.45 (D01) vs 450.47 (D06); (b)(1)(iv), (b)(3) | Citation answer; easy search route | hold (FAA agent may improve) |
| h8 | D03 218 principal launch operators; D01/D04 named commenters | Operators that commented on both agencies' rules | Who belongs where | ULA (Boeing/Lockheed JV) | Commenter lists incomplete (unnamed commenters) | reject (universe) |
| h9 | D01 647 etc. (11 sections, 3 added); anchors before Nov 18, 2024 | Compliance-list count in force on an anchor date (8 vs 11) | Temporal alignment | 11 | Small integer; anchors recallable | hold for FAA agent |
| h10 | D05 233 2312.5 MHz; D04 155 three frequencies | Spacing between Federal launch telemetry frequency in WCS band and 2360-2395 frequencies | Calculate across documents | other WCS frequencies | Contrived, lookup plus subtraction | reject |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.

Two background question-author agents (2026-10-08) search the FCC chain (Docs 2-5) and the FAA chain
plus cross-agency joins (Docs 1, 6 with FCC documents); their sketches are recorded in ideas.md.

FAA/cross-agency author (2026-10-08, origin claude): no fair Medium design; eight candidates dropped.
- Edition windows: Doc 1's rules change only at Nov 18, 2024 (L30) and the Sept 30, 2025 sunset "unless
  public law modifies" (L900, L920). The only other-document event between Doc 1's publication and
  effect is the LCA enactment, printed identically in D02 L71, D03 L25, D04 L53 (no single FCC document
  indispensable; also recallable). Later FCC dates select the current version (no trap); D05 dates fall
  after the sunset (state unknowable); D06 is a proposal. This also sinks h9 and the 440.9(b) idea.
- R1 days from Doc 1's effect to Doc 4's (195): plain gap; June 1, 2025 is a Sunday and Doc 3's own
  Mar 7 + 30 was printed as Monday Apr 7 (D03 L27), so June 2 is also defensible. Avoid Doc 4
  effective-date golds.
- R2 ordering five events: only the Mar 25 release flips an order; Doc 3 rebuildable from D04 L47 + 30.
- R3 suborbital exemption on a permitted flight: 14 vs 12 ("if applicable" reentry items); permits =
  suborbital is public knowledge.
- R4 440.17 willful-misconduct paragraph (f)->(g): binary, LCA anchor.
- R5 FAA Order 1050.1F vs 1050.1G: different exclusion categories; binary; recallable.
- R6 comment counts 15 vs 8 + 7: small integer once the ex parte condition is stated.
- R7 FRFA/IRFA statistic changes: boilerplate, one operation; Doc 5 Satellite row misprint (195/332 =
  58.73%, printed 88.69%).
- R8 Doc 6 parts vs Doc 1 human-space-flight sections: overlap {437, 450}, short-list filter.
- Commenter universes incomplete (D01 L118 15 comments; D04 L70 8 + 7).

FCC-chain author (2026-10-08, origin claude): nothing likely to reach Medium beyond h1-h5.
- i11 (kept as a quick-test sketch, notes/sketches/i11.md): transmitter-characteristic items, final list
  a-q (17, D04 L237-253) vs proposed a-l (12, D02 L173-184) = 5 more; decoy 3 (additions Doc 4 discusses,
  L88-89, L122) and 2 (SBE only). Two-list count; shares q01's Doc 2/Doc 4 path.
- i12 dropped: 2320-2345 MHz as a share/enlargement of part 26 spectrum (11.9%); 2360-2395 printed in both
  Doc 3 and Doc 4, so only Doc 5 indispensable; S-band completeness needs outside knowledge.
- Screened out: 2312.5 MHz to the three 2360-2395 frequencies (70.0 MHz; CFR-recallable; the 2200-2290
  "four sub-bands" are unnamed); Doc 4 released on LCA day 180 and Doc 3 released after its own Dec 25
  deadline (single-document); Second Further Notice FR date conflict (Feb 1 vs Feb 2, 2024); FRFA/IRFA
  statistics; 0.5 dB BAS showing (Doc 2 only).
- On h2: Doc 3 L57-58 cites 87.303(d)(1)/US276 by number, so the three centre frequencies may be recalled
  (Doc 4 replaceable); the mask's power term prints as "pY". h2 rejected.
- On h3: Doc 4's +30 days from May 2 is Sunday June 1, 2025; the bundle's printed dates roll to the next
  business day (Doc 3 Mar 7 + 30 = Sun Apr 6, printed Apr 7; Doc 5 Apr 9 + 30 = Sat May 9, printed May 11),
  so June 2 is defensible too; Doc 2's Jan 22 equals its FR date + 30, inferable. h3 rejected.
- On h1 (q01): proposed registration items absent from the final lists (fixed/base station coordinates,
  Doc 2 L134; launch-vehicle launch-site coordinates, Doc 2 L111) are outside "coordination-request items";
  Doc 4 L115 still names fixed/base coordinates as the Commission's expectation. Recorded as a reading risk.

Round 2 author (2026-10-09, origin claude; third independent round): no fair Medium design. The measured Medium
mechanisms (post-event decoy in a later edition; label regrouped across editions; grouped figure split in another
document) have no instance here: shared facts are twin-printed (Docs 2-4, Doc 3/Doc 4), rebuildable (FR + 30 days),
recallable (CFR US100/US276, UMRA, E.O. dates) or already-closed list diffs; Doc 5 shares only band edges.
- i31 (35 MHz with no showing replacing per-launch non-Federal coordination; Doc 2's 0.5 dB showing): dropped, readings
  35/120/0/125 stay defensible (the showing's survival into Doc 4 cannot be shown).
- i32 (launch-vehicle command spectrum under part 26, 85 + 35 = 120, minus the 2026 25 MHz uplink band = 95; decoys 185
  all part 26 bands, 60 Doc 5's own comparison): fair gold, but Doc 3's direction rules may be inferred from D02 L156,
  D02 L229 ("uplink operations") and D04 L155 ("telemetry and associated telecommand"); caller probing Doc 3 and Doc 5
  removal before offering it (runs/i32-sk-alt-w2). Sketch: notes/sketches/i32.md.
- i33 (four launch-telemetry frequencies between 2,300 and 2,395 MHz: 2312.5 + three US276): dropped, twin necessity
  (Doc 3/Doc 4), CFR recall, keyword path.
- Also screened out: transmitter items absent from the whole proposal (3; Doc 4 prose names them, Doc 2 unneeded);
  item count pending at the Third R&O's adoption; Doc 5's "zero" emergent-spectrum line vs part 26's 210 MHz; Doc 3's
  open issues vs Doc 5 (judgment); FAA definitions on Doc 3's crewed flights (outside knowledge); "licensed under
  chapter 509" vs permits (legal judgment); 100 kHz TT&C through the mask; Goldstone 145 km vs 320 km; coordinators a
  three-band launch clears (Doc 4 alone); Doc 2 limits that became mandatory (none; Doc 4 alone); E.O.-to-sunset gap.
