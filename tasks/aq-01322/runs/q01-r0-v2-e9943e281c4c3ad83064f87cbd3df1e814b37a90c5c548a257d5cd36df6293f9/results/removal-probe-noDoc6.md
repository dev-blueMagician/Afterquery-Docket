# q01 rev 0 - local removal probe without D05 (platform Doc 6), 2026-10-06

Design evidence, not a blind solve. Fresh blind-solver on packet runs/q01-r0-probe-m2/solver-1:
a byte copy of the rev 0 solver-1 packet minus D05, remaining ids renumbered contiguously
(probe D01-D04 unchanged, probe D05 = D06), neutral run name, bound with docket_agent.bind_scope.
Prompt: root, packet, verbatim question, plus a forced best answer with probability.

Raw return as received (probe ids):

answer: **Flat** (roughly 0% growth on the FY2025 base of $352M) for "Other", the group that held U.S. Consulting Services. This is a forced best guess, because the packet never says the sale closed. Probability it is correct: about 0.5.

confidence: low

path:
1. **Which group held the business.**
   - D05 line 121 (Nov 5, 2025): "Other… will consist of businesses for which the Company has begun to explore strategic alternatives and includes MWI Animal Health, Profarma, U.S. Consulting Services and the other components of PharmaLex."
   - D01 line 81 and D03 line 86 say the same: "These businesses include MWI Animal Health, Profarma, U.S. Consulting Services, and certain components of PharmaLex."
2. **The only divestiture-type event for this business.** It is in the quarter ended Dec 31, 2025, reported Feb 4, 2026.
   - D01 line 47: "a $249.5 million impairment of assets related to its U.S. Consulting Services business that is classified as held for sale."
   - D01 lines 204 and 244: "Impairment of assets held for sale, including goodwill, related to its U.S. Consulting Services business."
3. **Guidance in the same release.**
   - D01 line 103 ties the change for Other to that event: "improved results in Other as certain depreciable assets have been fully impaired as of December 31, 2025."
   - D01 line 114, in the adjusted operating income table: "Other(2) | Flat | $352M".
4. **How the guidance for Other moved over time.**

   | Release | Location | Other adjusted operating income guidance |
   |---|---|---|
   | Nov 5, 2025 | D05 line 138 | "1% to 4% decline" |
   | Feb 4, 2026 | D01 line 114 | "Flat" |
   | May 6, 2026 | D03 line 123 | "High-single digit growth" |

   D03 line 112 says the May change was "as a result of MWI now being accounted for as 'held for sale'". That concerns MWI, not U.S. Consulting.
5. **Why D01 is the chosen anchor.** It is the only document that describes a sale step for U.S. Consulting Services. I read "divested" as that held-for-sale classification and impairment, and took the guidance current when it was disclosed.

minimal_documents: D01 alone covers group membership, the event and "Flat". D03 alone supports reading (a) below; D05 plus D01 support reading (b).

readings:
- **(a) High-single digit growth (D03).** "Divested" in its ordinary sense means the sale closed. The packet suggests the business was still owned on May 6, 2026:
  - D03 still lists it in Other.
  - The Q2 commentary (D03 line 102) still cites "lower operating income at our consulting services businesses."
  - No completed sale appears in D01's or D03's highlights.

  If the sale closed between May 6, 2026 and the next guidance update, the guidance in force would be "High-single digit growth." Roughly 0.3.
- **(b) 1% to 4% decline (D05).** If "then-current" means the guidance in force when the held-for-sale classification happened (Oct–Dec 2025), that is D05's figure. The Feb 4 update came after the event. Roughly 0.15.

gaps:
- No packet document gives the closing date, buyer or completion of the U.S. Consulting Services sale. The question's starting assumption is not established by the packet.
- There is no Q3 FY2026 or later release, and no 10-Q.
- D01, D03 and D05 were read in full. D02 and D04 (FY2025 Q2 and Q3 releases) were read for lines 1–150 and searched; they contain only FY2025 guidance and nothing on U.S. Consulting.
- The docs/ and text/ copies have the same counts for "consulting" and "divest", so nothing was lost in extraction. Bold markers showing which guidance figures were updated are not preserved.

contaminated: no

Files:
- D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-probe-m2\solver-1\text\D01.txt
- D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-probe-m2\solver-1\text\D03.txt
- D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-probe-m2\solver-1\text\D05.txt

Caller note: the forced answer equals the gold (Flat, p 0.5) through the held-for-sale reading of
"divested", anchored on D01's own tie between Other's guidance change and the U.S. Consulting
impairment. The platform's document check (high model without Doc 6) could reach the same answer,
so Doc 6 would read as not needed. Rev 1 rewords the anchor to "completed the divestiture".
