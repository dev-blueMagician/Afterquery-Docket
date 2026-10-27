# aq-05015 h4 (i04) and h7 (i05) arithmetic. $ millions. Inputs from tasks/aq-05015/text.

# h4: Diamond Green Diesel 2025 capital investments, outlook vs actual
partner_expected = 110          # D02:795 "DGD's capital investments attributable to the other joint venture member (110)"
dgd_capex_2025 = 71             # D06:809 "DGD 4 52 71 250" (FY 2025 column)
dgd_turnaround_2025 = 99        # D06:816 "of DGD 8 9 99 71"
partner_actual = 85             # D06:823 "(6) (31) (85) (161)"
share = 0.5                     # D02:891 "only 50 percent of DGD's capital investments should be attributed to our net share"
dgd_expected = partner_expected / share
dgd_actual = dgd_capex_2025 + dgd_turnaround_2025
assert dgd_actual == partner_actual / share == 170
print("i04 gold:", dgd_expected - dgd_actual, "| lures: partner shares", partner_expected - partner_actual,
      "| 110 vs 170:", partner_expected - dgd_actual, "| consolidated", 2060 - 1888, "| attributable", 1950 - 1797)

# h7: 2025 capital investments not for sustaining the business
quarters = {"Q1": (660, 582), "Q2": (407, 371), "Q3": (409, 364), "Q4": (412, 368)}  # D03:39, D04:39, D05:40, D06:44
fy_total = 1888                 # D06:818 "Capital investments 412 547 1,888 2,057"
assert sum(t for t, _ in quarters.values()) == fy_total
sustaining = sum(s for _, s in quarters.values())
print("i05 gold:", fy_total - sustaining, "(sustaining", sustaining, ")",
      "| lures: Q4 only", 412 - 368, "| attributable base", 1797 - sustaining,
      "| FY minus Q4 sustaining", fy_total - 368, "| capex lines", 719 + 71 + 6 + 3)
