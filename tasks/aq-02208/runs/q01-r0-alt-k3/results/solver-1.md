# Removal probe return: q01 rev 0 without Doc 2 (D02)

- Date: 2026-10-08
- tested_sha256: 3173d78ec01069d506aed5e32ad8ee6c5af2cae8fd6cf28ecbfad251b72c4ddf
- Packet: tasks/aq-02208/runs/q01-r0-alt-k3/solver-1 (Doc 1 -> D01, Doc 3 -> D02, Doc 4 -> D03, Doc 5 -> D04, Doc 6 -> D05; neutral headers)
- Role: blind-solver (fresh context, question only)

Raw return (verbatim):

answer: None. Every coordination-request data item the FCC proposed is still required of at least some licensees under the final procedures. Three items tailored to orbital launches are waived for suborbital launches, but orbital launches still have to supply them ("if applicable"):
- list of objects to achieve orbit
- orbital location (orbit insertion)
- duration of transmission(s), including on/off times

confidence: high (about 0.8–0.85). The main caveat is that the packet does not contain the full list of proposed items (see gaps).

path:
1. D03 is the final procedures: WTB, DA 25-270, 90 FR 18789 (May 2, 2025), "ACTION: Final action". Line 66: "we adopt final licensing and coordination procedures for all three bands". Line 71: "We therefore adopt, as discussed in detail below, the substantial majority of our proposed data requirements, with certain modifications based on record input."
2. What was proposed (D03 lines 114–120). The PN listed what the Commission anticipated: "(1) the specific coordinates of fixed, base, and itinerant stations ... (2) frequency channels; (3) launch trajectories; (4) launch window or planned launch date; and (5) any other technical and operational information (e.g., antenna characteristics, power levels, emission designators)". It then says: "we proposed data requirements for coordination requests in all three bands that include data currently required in the part 87 ... process, the data required in the STA process ... and the aforementioned data points".
3. The only changes to coordination-request items (D03 line 122):
   - Two additions: height AGL to the radiation center, and the tracking arc path.
   - A scoped waiver: "launch operators proposing suborbital launches need not provide the following data tailored for orbital launch operations: (1) list of objects to achieve orbit during launch operation, (2) orbital location (orbit insertion), and (3) duration of transmission(s)..."
4. No cuts were made (D03 line 123): "We therefore do not find it appropriate to adopt commenter suggestions to significantly reduce the data required for coordination requests". ULA's proposed eight-item list and its idea of having data come from suppliers or the FAA were both rejected.
5. The final list says "Space Launch Service licensees shall provide the following data ..." (D03 line 228). It keeps 7d "List of objects to achieve orbit during launch operation, if applicable" (line 267), 7g "Orbital location (orbit insertion), if applicable" (line 270) and 7l "Duration of transmission(s)... if applicable" (line 275). Orbital launches must therefore still provide all three.
6. Each anticipated item maps to the final list:
   - Frequencies: 5 and 7f.
   - Trajectories: 7i–7m.
   - Launch window: 7c.
   - Antenna, power and emission data: items 5 and 6.
   - Station and site coordinates: items 2–4, via the registered details. Itinerant/mobile stations give "geographic coordinates of the transmit location referenced to NAD83" (line 220), and the launch site gives NAD83 coordinates (line 202).
   - Antenna details were only removed from ULS registration: "We therefore require licensees to provide antenna details in frequency coordination requests ... but we decline to adopt our proposal that would require that data also to be submitted for initial station registrations in ULS" (line 87).
7. Candidates I excluded because they are not coordination-request data items:
   - The proposed 96-hour pre-launch notice. It was not adopted, but it is a separate notification (lines 173, 178).
   - The 60-day filing timeframe, which is a timing rule (line 140).
   - The items for registering the launch vehicle itself, which are registration items (lines 92, 96).
   - The justification for bandwidth over 5 MHz. It was proposed for ULS registration and is now a single ULS attachment that is still required of licensees going over 5 MHz (line 106).

minimal_documents: D03 alone. D02 (Third Report and Order, paragraphs 36–37, lines 130–132) only confirms that the PN proposed coordination data requirements and that the Commission "affirm[ed]" them, so it isn't needed. No other document lists coordination-request items.

readings:
- (a) Read loosely as "not required of every licensee": the answer becomes the three orbital-tailored items (objects to achieve orbit; orbital location/orbit insertion; duration of transmissions with on/off times). The question says "of no licensee", so I reject this.
- (b) Ultra-literal split: the final fixed/base station details (D03 lines 206–217) list "Address" but no latitude/longitude. Fixed/base-station lat/long, taken out of anticipated item (1), would then have no explicit final requirement. D03 never says it dropped coordinates, and the itinerant and launch-site coordinates remain, so I give this low weight.
- (c) If the PN put a >5 MHz justification inside the coordination-request emission-bandwidth fields, that per-field justification is gone from coordination requests. It is still required of licensees going over 5 MHz, so it does not qualify under "no licensee".

gaps:
- The December 2024 Licensing and Coordination Comment PN (89 FR 104502), which has the full proposed coordination list, is not in the packet. "None" therefore relies on D03's own account of what it changed being complete.
- Coverage: I read D03 in full. For D02 I read lines 1–199 and 276–375 (rule text) and ran greps. For D01, D04 and D05 (FAA rules and an FCC emergent-space NPRM) I read the headers and ran targeted greps; none of them mention part 26 or space-launch coordination data.
- There is no layout file or PDF; the manifest method is "text".

contaminated: no

Forced best guess (required separately): "None — no proposed coordination-request item was dropped for all licensees; the three orbital-specific items are excused only for suborbital launches." Probability correct: 0.8. The guess comes from the documents (D03), plus the assumption that D03's account of its changes is complete.
