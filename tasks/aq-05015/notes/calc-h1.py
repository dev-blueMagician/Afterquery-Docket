# Independent check of the cost-of-materials reclassification hook (aq-05015).
# Inputs typed from tasks/aq-05015/text (line numbers in comments).

# As first reported (old presentation: excise taxes inside cost of materials)
old = {
    "Q4_2024": 27926,   # D02:104
    "FY_2024": 116516,  # D02:104
    "Q1_2025": 27548,   # D03:99
    "Q2_2025": 26332,   # D04:98
    "H1_2025": 53880,   # D04:98
    "Q3_2025": 27958,   # D05:97
    "9M_2025": 81838,   # D05:97
}
# New presentation (taxes other than income taxes on their own line)
new = {
    "Q4_2024": 26409, "FY_2024": 110616,            # D06:103 comparatives
    "Q4_2025": 24238, "FY_2025": 101096,            # D06:103
    "Q1_2025": 26048, "Q1_2026": 26185,             # D07:103
    "Q2_2025": 24678, "H1_2025": 50726,             # D08:96 comparatives
    "Q2_2026": 35130, "H1_2026": 61315,             # D08:96
}
tax = {
    "Q4_2024": 1517, "FY_2024": 5900, "Q4_2025": 1740, "FY_2025": 6720,  # D06:105
    "Q1_2025": 1500, "Q1_2026": 1721,                                     # D07:105
    "Q2_2025": 1654, "H1_2025": 3154, "Q2_2026": 1648, "H1_2026": 3369,   # D08:98
}

# 1. Proof of the reclassification: old = new + taxes wherever both exist
for k in ["Q4_2024", "FY_2024", "Q1_2025", "Q2_2025", "H1_2025"]:
    assert old[k] == new[k] + tax[k], k
    print(f"{k}: old {old[k]} = new {new[k]} + taxes {tax[k]}")

# 2. Q3 2025 on the new presentation (never printed)
q3_new_a = new["FY_2025"] - new["Q4_2025"] - new["H1_2025"]
q3_tax = tax["FY_2025"] - tax["Q4_2025"] - tax["H1_2025"]
q3_new_b = old["Q3_2025"] - q3_tax
assert q3_new_a == q3_new_b
print("Q3 2025 new:", q3_new_a, "Q3 2025 taxes:", q3_tax)
# consistency of 9M old vs FY new + taxes
assert old["9M_2025"] + new["Q4_2025"] + tax["Q4_2025"] == new["FY_2025"] + tax["FY_2025"]

# 3. Twelve months ended June 30, 2026
ttm_gold = new["FY_2025"] - new["H1_2025"] + new["H1_2026"]
ttm_quarters = q3_new_a + new["Q4_2025"] + new["Q1_2026"] + new["Q2_2026"]
assert ttm_gold == ttm_quarters
assert new["H1_2026"] == new["Q1_2026"] + new["Q2_2026"]
ttm_trap_q3old = old["Q3_2025"] + new["Q4_2025"] + new["Q1_2026"] + new["Q2_2026"]
ttm_trap_h1old = new["FY_2025"] - old["H1_2025"] + new["H1_2026"]
ttm_oldbasis = ttm_gold + q3_tax + tax["Q4_2025"] + tax["Q1_2026"] + tax["Q2_2026"]
print("TTM gold:", ttm_gold, "| trap Q3 as first reported:", ttm_trap_q3old,
      "| trap H1 2025 as first reported:", ttm_trap_h1old, "| all-old basis:", ttm_oldbasis)

# 4. Second half of 2025
h2_gold = new["FY_2025"] - new["H1_2025"]
assert h2_gold == q3_new_a + new["Q4_2025"]
h2_trap_q3old = old["Q3_2025"] + new["Q4_2025"]
h2_trap_h1old = new["FY_2025"] - old["H1_2025"]
h2_oldbasis = old["Q3_2025"] + new["Q4_2025"] + tax["Q4_2025"]
print("H2 gold:", h2_gold, "| trap Q3 old + Q4:", h2_trap_q3old,
      "| trap FY - H1 old:", h2_trap_h1old, "| all-old basis:", h2_oldbasis)
