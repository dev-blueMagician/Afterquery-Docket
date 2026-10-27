# Removal probe return: sketch i32 without Doc 3 (D03)

- Date: 2026-10-09
- Sketch: notes/sketches/i32.md (question verbatim in probe.json); no fingerprint (sketch stage)
- Packet: tasks/aq-02208/runs/i32-sk-alt-w2/solver-1 (Doc 1 -> D01, Doc 2 -> D02, Doc 4 -> D03, Doc 5 -> D04, Doc 6 -> D05; neutral headers)
- Role: blind-solver (fresh context, question only)

Summary of the raw return (full text in the session transcript):
- answer: 60 MHz (2025-2110 launch uplink band, 85 MHz, from D02 L229 "proposed uplink operations" and Doc 5's Federal-band directions, minus the 2026 proposal's 25 MHz).
- confidence: medium; main risk whether 2360-2395 also counts.
- readings: (b) 95 MHz if 2360-2395 counts (Doc 4 L155 "telemetry and associated telecommand"), judged weaker because the packet "never gives the direction of the Part 26 allocation in that band"; (c) 10; (d) 185 (all three bands, rejected: 2200-2290 is space-to-Earth); (e) 50 or 30 (seek-comment bands, rejected).
- gaps: "The packet has no Part 26 or Sec. 2.106 rule text giving the direction of the 2360-2395 MHz launch allocation. That fact would settle reading (b)."
- contaminated: no.
- forced best guess: 60 MHz, p 0.75, source documents; 95 at about 0.15.
