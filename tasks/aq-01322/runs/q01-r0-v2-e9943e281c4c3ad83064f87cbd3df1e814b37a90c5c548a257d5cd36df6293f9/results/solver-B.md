# q01 rev 0 - blind solver B (fresh blind-solver, packet solver-2), 2026-10-06

Raw return as received:

**answer:** Flat. The guidance in effect when U.S. Consulting Services was divested in April 2026 projected fiscal 2026 adjusted operating income growth of about 0% for "Other", measured against fiscal 2025 actuals of $352M. That guidance was issued February 4, 2026.

**confidence:** high

**path:**
1. **When the divestiture happened (D05, Q3 FY26 release, Aug 5, 2026).** Line 81 says Other includes "MWI Animal Health, Profarma, U.S. Consulting Services (which was divested in April 2026), and certain components of PharmaLex." Line 95 refers to "the April 2026 divestiture of U.S. Consulting Services." Footnotes at lines 269 and 393 repeat "divested in April 2026."
2. **Which group it belonged to.** It was in "Other", which is not a reportable segment. D01 line 81 says "other businesses for which the Company is exploring strategic alternatives have been grouped together in Other. These businesses include … U.S. Consulting Services." D06 line 121 says the same.
3. **The fiscal 2026 guidance for Other adjusted operating income, in date order:**
   - Nov 5, 2025 (D06 line 138): "|Other(1)|1% to 4% decline|$352M|"
   - Feb 4, 2026 (D01 line 114): "|Other(2)|Flat|$352M|". The reason given at line 103 is "improved results in Other as certain depreciable assets have been fully impaired as of December 31, 2025."
   - May 6, 2026 (D03 line 123): "|Other(2)|High-single digit growth|$352M|". Line 112 says this reflects "MWI now being accounted for as 'held for sale'."
   - Aug 5, 2026 (D05 line 118): "|Other(2)|~10% growth|$352M|"
4. **Which guidance was current in April 2026.** April falls between the February 4 and May 6 releases. D03 line 17 says EPS guidance was "raised from the previous range of $17.45 to $17.75," which is exactly the February range (D01 line 13: "Reaffirmed at $17.45 to $17.75"). So the packet shows no guidance change between Feb 4 and May 6, and the February guidance ("Flat") was in effect at the divestiture.
5. **Row check.** In D01, the line 110 entry for Other ("1% to 5% growth") is revenue guidance, not operating income. The adjusted operating income rows are lines 111–114, and Other's is "Flat." Flat means roughly 0% growth on the $352M base.

**minimal_documents:** D05 and D01 are both required.
- D05 is the only document that dates the divestiture (D01 says only "classified as held for sale", and D03 doesn't mention the divestiture).
- D01 is the only document with the "Flat" figure.
- D03 is optional. It confirms the February guidance stayed in place until May 6.

**readings:**
- **First guidance issued after the divestiture (May 6, D03):** "High-single digit growth." This is weaker, because that guidance didn't exist yet in April.
- **Anchor on the held-for-sale classification instead of completion:** the business was held for sale by Dec 31, 2025 (D01 line 47), when the November 5 guidance was current, giving "1% to 4% decline." This is weak, because "divested" normally means the sale was completed.
- **Guidance in the release that first disclosed the divestiture (Aug 5, D05):** "~10% growth." This is weak, because it wasn't current at the time of the divestiture.

**gaps:**
- The packet doesn't give the exact day in April 2026, and it contains no standalone announcement of the divestiture. Since every April date falls between the February 4 and May 6 releases, the missing day doesn't change the answer.
- D03 (May 6) says nothing about the April divestiture, even though it was issued afterwards.
- D05 refers to a "previous range of $17.70 to $17.90". No release in the packet contains it, so it was set between May 6 and Aug 5. That is after April and doesn't affect the answer.
- The sources are text files only, with no PDFs or layout files. So the bolding that the footnotes say marks updated guidance can't be seen.
- **Coverage:**
  - Fully read: D01 lines 1–130, D03 lines 1–140, D05 lines 1–140, D06 lines 1–185 and the manifest.
  - Searched only: D02, D04 (fiscal 2025 releases) and the later table/reconciliation sections of D01, D03, D05 and D06, using searches for Consulting, divest/sold, held for sale/strategic alternatives, April/previous range/reaffirm, and Other rows/Flat.

**contaminated:** no. I did not open `question.txt` or any notes.

Files used, all under `D:\Dev\Docket\tasks\aq-01322\runs\q01-r0-v2-e9943e281c4c3ad83064f87cbd3df1e814b37a90c5c548a257d5cd36df6293f9\solver-2\text\`:
- `D01.txt`
- `D03.txt`
- `D05.txt`
- `D06.txt`
- `manifest.json`
