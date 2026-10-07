# q01 rev 0, shortcut auditor (fresh shortcut-auditor agent, shortcut packet), 2026-10-06

Input: workspace root, packet path runs/q01-r0-v2-a3bea189.../shortcut, question verbatim.
Return copied verbatim from the task notification.

**answer:** $1.65 trillion. Climate change/carbon had $3.45T and military/weapons, the second-ranked issue, had $1.8T, so 3.45 − 1.80 = 1.65.

**verdict:** clear

**shortest_path:**
1. A search for "US SIF" finds only two documents with US SIF figures on individual ESG issues: D12 and D07. D10 mentions US SIF only as a source of fund-ownership data.
2. D12, line 24 (line 22 in the original docs file): "According to US SIF Foundation, of the $8.4 trillion AUM in funds that consider ESG factors in their investment decision-making, $3.45 trillion address climate change/carbon and $1.23 trillion apply fossil fuel divestment policies." Its footnote 4 gives the source as "US SIF Foundation, 2022 Report on US Sustainable Investing Trends Executive Summary, 4".
3. D07, line 45 (line 43 in the original): "According to US SIF, attention to climate change and fossil fuel divestment is by far the most significant of the ESG claims made by asset managers, addressed in funds with a combined $4.8 trillion in AUM. The next largest ESG categories, military/weapons and tobacco, are addressed in funds with $1.8 trillion and $1.7 trillion in AUM, respectively."
   - Same period: D07 line 24 says "at the beginning of 2022, $8.4 trillion", which is the same base D12 uses.
4. Ranking: climate change/carbon 3.45 > military/weapons 1.8 > tobacco 1.7 > fossil fuel divestment 1.23. Military/weapons is second whether climate change/carbon stands alone or is combined with fossil fuel divestment as D07 does.
5. 3.45 − 1.80 = **1.65**.

**sufficient_documents:** D07 and D12 together. Neither works alone, and no other document can stand in for either.
- D12 gives the $3.45T figure but no ranking.
- D07 gives the ranking and the $1.8T figure, but only a combined climate-plus-fossil-fuel total, not climate change/carbon on its own.

**searches:**
- **Terms searched:**
  - Names: "US SIF|USSIF|SIF Foundation|Forum for Sustainable"
  - Topics: "climate change/carbon|carbon", "trillion", "military|weapon|tobacco|human rights|board diversity|anti-corruption|labor", "Trends|ussif.org|divestment"
  - Numbers that could be the answer or its inputs: "3.45|1.65|1.23|4.68|4.8/1.8/1.7/8.4 trillion"
  - Ranking language: "ranked|second-largest|next largest|most significant|ESG criteria|ESG issue|specific ESG"
  - Every "$N billion/trillion" amount in all 12 documents.
- **Read in full:** D07 and D12.
- **Checked and ruled out:**
  - D10's US SIF mentions (lines 59, 348, 355, 618, 784, 796, 839, 1178, 1200) are ownership data with no issue-level figures.
  - D10's hits on 1.23, 3.45 and 1.65 (lines 1076, 1130, 1140) are coincidences inside regression t-statistics.
  - The other "trillion" lines in D01, D03, D05, D06, D08 and D11 are trade groups' own assets under management. D02's $1.7T is unrelated climate financing.
- **Original sources:** both key passages match the files in docs/ exactly.
- **Shortcut attacks:**
  - No document states the difference.
  - Neither document alone is enough.
  - The question's wording gives nothing away: "climate change/carbon" is D12's exact label, but the second-ranked issue has to come from D07.

**readings/gaps:**
- **3.00 (rejected):** a D07-only reader might use the combined $4.8T as "climate change/carbon" (4.8 − 1.8). But that total includes fossil fuel divestment, and the question uses D12's separate $3.45T label.
- **2.22 (rejected):** a D12-only reader might assume fossil fuel divestment ($1.23T) is second (3.45 − 1.23). D07 shows military/weapons ($1.8T) and tobacco ($1.7T) are both larger.
- **The sources disagree slightly:** D07's "combined $4.8 trillion" doesn't match D12's 3.45 + 1.23 = 4.68 (which would round to 4.7). This doesn't change the answer.
- **Precision:** D07 gives $1.8T to only one decimal place, so the two-decimal answer assumes exactly 1.80. If the underlying figure were anywhere from $1.75T to $1.85T, the true difference could be anywhere from 1.60 to 1.70. 1.65 is the only answer the packet supports.
- **Difficulty risk:** this is a simple two-document lookup. One "US SIF" search surfaces both inputs and the subtraction is trivial. The 2.22 and 3.00 traps are what make the question discriminating.
- **Unread:** D01–D06 and D08–D11 were not read in full, but the keyword and dollar-amount searches covered them. The files are plain text, so there are no extraction gaps.

**Files:**
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r0-v2-a3bea189a69e113dbd4e7b5c5fe40eb57ca4a273af31df5ad5a837cad09b8535\shortcut\text\D12.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r0-v2-a3bea189a69e113dbd4e7b5c5fe40eb57ca4a273af31df5ad5a837cad09b8535\shortcut\text\D07.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r0-v2-a3bea189a69e113dbd4e7b5c5fe40eb57ca4a273af31df5ad5a837cad09b8535\shortcut\docs\sec_esg_disclosures_advisers_funds_s71722-458951-1174494.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r0-v2-a3bea189a69e113dbd4e7b5c5fe40eb57ca4a273af31df5ad5a837cad09b8535\shortcut\docs\sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt
