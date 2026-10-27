# Removal probe return: sketch i32 without Doc 5 (D05)

- Date: 2026-10-09
- Sketch: notes/sketches/i32.md (question verbatim in probe.json); no fingerprint (sketch stage)
- Packet: tasks/aq-02208/runs/i32-sk-alt-w2/solver-2 (Doc 1 -> D01, Doc 2 -> D02, Doc 3 -> D03, Doc 4 -> D04, Doc 6 -> D05; neutral headers)
- Role: blind-solver (fresh context, question only)

Summary of the raw return (full text in the session transcript):
- answer: not answerable from the packet. FCC side = 120 MHz (D03 para 17: 2025-2110 ground-to-launch vehicle telecommand, 85 MHz; 2200-2290 vehicle-to-ground only, excluded; Sec. 26.3(a)(3) and NG42: 2360-2395 telemetry and telecommand, 35 MHz). No 2026 spacecraft-uplink proposal in the packet, so 120 - X cannot be computed.
- confidence: high (not answerable); high (FCC side 120 MHz).
- minimal_documents: D03 covers the FCC side; "D02 and D04 restate the three bands but cannot replace D03: D02 was issued before the 2360-2395 rules were adopted, and D04 does not restate the 2025-2110 telecommand limit."
- readings: 210 - X if all three bands counted; 85 - X if only the dedicated uplink band.
- contaminated: no.
- forced best guess: 35 MHz (assumed the proposal uses 2025-2110, 120 - 85), p 0.2, source assumption.
