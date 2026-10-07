# q01 rev 0 - local removal probe without D01 (platform Doc 4), 2026-10-06

Design evidence, not a blind solve. Fresh blind-solver on packet runs/q01-r0-probe-k7/solver-1:
a byte copy of the rev 0 solver-1 packet minus D01, remaining ids renumbered contiguously
(probe D01 = D02, D02 = D03, D03 = D04, D04 = D05, D05 = D06), neutral run name, bound with
docket_agent.bind_scope. Prompt: root, packet, verbatim question, plus "If the packet does not
settle the answer, still commit to a single forced best answer and give your probability (0-1)".

Raw return as received (probe ids):

answer: The guidance in force before the April 2026 sale projected a **decline of 1% to 4%** in fiscal 2026 adjusted operating income for "Other" (fiscal 2025 base: $352M). That works out to roughly $338M–$348M. Forced best answer: −1% to −4%, with probability **≈0.70** that it is correct.

confidence: medium

path:
1. **Date of the sale.** D04 (filed Aug 5, 2026) line 81 says "U.S. Consulting Services (which was divested in April 2026)". Line 95 refers to "the April 2026 divestiture of U.S. Consulting Services", and lines 269 and 393 repeat "which was divested in April 2026".
2. **The group that included it.** D05 line 121 says "Other, which is not considered a reportable segment, will consist of businesses … MWI Animal Health, Profarma, U.S. Consulting Services and the other components of PharmaLex". D02 line 86 and D04 line 81 describe the same group.
3. **The three fiscal 2026 guidance versions in the packet for Other's adjusted operating income:**
   - D05 (Nov 5, 2025), lines 135–138, under "Adjusted operating income | 8% to 10% growth": "|Other(1)|1% to 4% decline|$352M|".
   - D02 (May 6, 2026), line 120: "|Other(2)|High-single digit growth|$352M|". Line 112 says this was an update: "updated operating income expectations in Other as a result of MWI now being accounted for as 'held for sale'".
   - D04 (Aug 5, 2026), line 118: "|Other(2)|~10% growth|$352M|".
4. **Which version was current in April 2026.** April 2026 falls after Nov 5, 2025 and before May 6, 2026. So the May "high-single digit" figure came after the sale and was not yet current. D02 line 17 says EPS guidance was "raised from the previous range of $17.45 to $17.75". That matches D05 line 139, so the EPS guidance had not changed between November and May.
5. **Arithmetic.** $352M × 0.99 = $348.5M and $352M × 0.96 = $337.9M.
6. **Distractor ruled out.** D05 line 134, "Other(1)|0% to 4% growth|$8.2B", is revenue guidance, not operating income.

minimal_documents: D04 + D05. D04 is the only document that dates the sale. D05 is the only fiscal 2026 guidance issued before April 2026. Group membership is in either one. D02 supports the answer by showing the change to Other came after the sale, but nothing else in the packet could replace D04 or D05.

readings:
- **Guidance missing from the packet.** The guidance actually in force in April 2026 was probably a later version than D05, likely from the Q1 FY2026 release (about Feb 2026), which is not in the packet. Two lines in D02 point to it:
  - D02 says the company "narrowed its expectations for interest expense" to "~$485M". That can't be a narrowing of D05's "$315M to $335M".
  - D02 says it expects "an incrementally lower expected share count" of "Under 195.5M", but D05 had "~194M".

  The packet doesn't show whether that version changed Other's operating income guidance. The $249,498K held-for-sale impairment for U.S. Consulting Services appears only in the six-month column (D02 line 237), not the three months ended March 31, 2026. So the business was already held for sale before that release, and a revision there is possible. Because the EPS range stayed the same and D02 links its change to Other only to MWI, the most likely answer is that the −1% to −4% still stood.
- **If "then-current" means the first guidance issued after the sale (D02, May 6, 2026):** high-single-digit growth.
- **If it means the release that first reported the sale as done (D04, Aug 2026):** about 10% growth.

  Both are weaker readings, because neither guidance was in force in April.

gaps:
- No Q1 FY2026 release (about Feb 2026) is in the packet.
- Footnotes in D02 (line 131) and D04 (line 126) say bolded figures mark updates. The bold formatting is lost in both the text/ and docs/ copies, so I can't tell which lines changed.
- No PDF or layout files exist; the manifest lists method "text" with pages null.
- The packet contradicts itself on EPS guidance. D04 line 17 says the previous range was "$17.70 to $17.90", but D02 set it at "$17.65 to $17.90". Either there was another update the packet doesn't record, or one of the documents is wrong.
- Not fully read:
  - D01 and D03 were checked only by search. They contain fiscal 2025 guidance only and no "2026" mentions.
  - Only search hits were read in D02 lines 270–649, D04 lines 161–254 and 280–659, and D05 lines 176 to the end. These are historical tables and reconciliations.

contaminated: no

Files:
- D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-probe-k7\solver-1\text\D05.txt
- D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-probe-k7\solver-1\text\D04.txt
- D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-probe-k7\solver-1\text\D02.txt

Caller note: forced answer "1% to 4% decline" (p 0.70) differs from the gold (Flat): D01 is
needed. The probe inferred the missing February release from D03's "narrowed" interest-expense
wording but could not recover Other's February value.
