# Removal probe return: q01 rev 2 without Doc 2 (D02)

- Date: 2026-10-08
- tested_sha256: d58f4220f4951db00837f467c9e5b8161d404fe8f100b7535ed07b1d292f4145
- Packet: tasks/aq-02208/runs/q01-r2-alt-m6/solver-1 (Doc 1 -> D01, Doc 3 -> D02, Doc 4 -> D03, Doc 5 -> D04, Doc 6 -> D05; neutral headers)
- Role: blind-solver (fresh context, question only)

Raw return (verbatim):

answer: None. The final procedures still require every FCC-proposed coordination-request data item of at least some licensees. Three items are excused only for suborbital launches, and orbital launches must still provide them ("if applicable"):
- the list of objects to achieve orbit
- the orbital location (orbit insertion)
- the duration of transmissions, including on/off times

confidence: medium. The full list proposed in December 2024 is not in the packet, so this relies on D03's account of the changes being complete.

path:
1. D03 is the WTB final action ("Licensing and Coordination Procedures for the Space Launch Service", DA 25-270, 90 FR 18789, May 2, 2025). Its summary of the proposal (line 114–115): "we proposed in the Licensing and Coordination Comment PN a list of data requirements for frequency coordination requests ... (1) the specific coordinates of fixed, base, and itinerant stations (e.g., latitude and longitude); (2) frequency channels; (3) launch trajectories; (4) launch window or planned launch date; and (5) any other technical and operational information (e.g., antenna characteristics, power levels, emission designators)". Line 120 adds that the proposal "include[s] data currently required in the part 87 ... flight test coordination process, the data required in the STA process ..., and the aforementioned data points".
2. D03 line 122 lists the changes to the coordination-request data. "First, we require ... the height AGL to the antenna radiation center ... and for each fixed and base station the projected space launch tracking arc path" (these are additions). "Second ... launch operators proposing suborbital launches need not provide the following data tailored for orbital launch operations: (1) list of objects to achieve orbit during launch operation, (2) orbital location (orbit insertion), and (3) duration of transmission(s), to include on/off time".
3. D03 line 123: "We therefore do not find it appropriate to adopt commenter suggestions to significantly reduce the data required for coordination requests". Line 71 says D03 adopts "the substantial majority of our proposed data requirements, with certain modifications based on record input."
4. D03 line 87: antenna details were moved, not dropped. "We therefore require licensees to provide antenna details in frequency coordination requests ... but we decline to adopt our proposal that would require that data also to be submitted for initial station registrations in ULS."
5. The final list in D03 Section III.B (lines 228–284) keeps the three orbital items with a qualifier: "d. List of objects to achieve orbit during launch operation, if applicable"; "g. Orbital location (orbit insertion), if applicable"; "l. Duration of transmission(s) ... if applicable". The five anticipated categories also appear: station details (item 3/4), requested frequencies (7.f), trajectory and ground track (7.i, 7.m), launch window (7.c), and antenna/power/emission data (5, 6).
6. Classification: an item excused for suborbital launches is still required of orbital launch licensees, so it is not "required of no licensee." I found no coordination-request data item that D03 drops outright. The candidates I set aside, all in D03, are not coordination-request data items or were never licensee duties:
   - the 96-hour pre-launch notification (lines 173, 178)
   - the 60-day advance submission (lines 136, 139–140)
   - the 15-day reply from SBE coordinators (lines 142, 146)
   - the AFC filing destination (lines 129, 134)
   - AFTRCC's throughput detail for the over-5 MHz justification (line 106; a commenter request about a ULS filing)

minimal_documents: D03 alone. D02 (¶36–37, lines 130–132) only confirms that the December 2024 notice proposed coordination-request data requirements and that the Commission affirmed them; it is not needed. No other packet document can replace D03. D01 and D05 are FAA rules, and D04 is a 2026 FCC NPRM with no part 26 coordination-request content (a grep for "part 26|space launch" found nothing).

readings:
- (a) If the question is read as "not required of every licensee," the answer is the three orbital-tailored items: list of objects to achieve orbit; orbital location (orbit insertion); duration of transmissions including on/off times.
- (b) A hyper-literal reading (low weight): the anticipated item (1) includes coordinates for fixed and base stations. The final fixed/base station details (D03 lines 206–217) list "Address" and ground elevation but no latitude/longitude, and coordination item 4 carries over only those details. On that reading the answer would be "latitude/longitude of fixed and base stations." D03 never says coordinates were dropped, and the address may serve as the location.
- (c) If "items" means procedural proposals, the only licensee-facing proposal not adopted is the 96-hour pre-launch notification. That is a separate notification, not part of a coordination request.

gaps:
- The full proposed coordination-request list (Licensing and Coordination Comment PN, 89 FR 104502, Dec. 23, 2024) is not in the packet. D03 only summarizes the proposal and the changes.
- The manifest shows text only (method "text", pages null), so there was no original PDF to check.
- Coverage:
  - D03: read in full.
  - D02: lines 1–199 and 340–379 plus grep hits; the rest is unread (FRFA and other rule text).
  - D01, D04, D05: headers plus targeted greps only.
  - docs/: not read, per your instruction.

contaminated: no

Forced best guess: "None — no proposed coordination-request item is required of no licensee; the three orbital-only items still apply to orbital launches." The guess comes from the documents (D03). Probability it matches the gold: about 0.70. The main alternative gold would be the three suborbital-excused items (about 0.2).
