"""Author arithmetic check for aq-05747 sketches i01 and i02 (inputs as printed; $ millions, %)."""

# i01: largest single impairment charge recorded in fiscal 2025
impairments_2025 = {
    # Asset Impairments sections (Doc 3 L514-516; Doc 1 L495-497)
    "BODYARMOR trademark, Q4 (Doc 3)": 960,
    "LatAm trademark, Q2 (Doc 1)": 31,
    "LatAm trademark, Q4 (Doc 3: FY 44 - Q4 13 = 31 earlier)": 13,
    "APAC trademark and PP&E, Q4 (Doc 3)": 41,
    "LatAm equity investee OTTI, Q2 (Doc 1)": 40,
    "LatAm JV OTTI, Q1 (Doc 1 six months / Doc 4)": 25,
    # Transaction Gains/Losses, Q4 2025 (Doc 3 L528); called "the previously recorded
    # impairment charge" by Doc 5 L500 (reduction of 66 > Q1 2026's 10, Doc 4 L404)
    "Africa bottling held for sale, Q4 (Doc 3)": 1274,
}
asset_impairment_rows = {k: v for k, v in impairments_2025.items() if "Africa" not in k}
assert sum(asset_impairment_rows.values()) == 1110          # Doc 3 FY table, income before taxes
assert 960 + 13 + 41 == 1014                                 # Doc 3 Q4 table
gold_i01 = max(impairments_2025.values())
lure_i01 = max(asset_impairment_rows.values())
print("i01 gold (largest single impairment charge, $M):", gold_i01)     # 1274
print("i01 lure (Asset Impairments account only):", lure_i01)          # 960
# reading checks
print("  net of 2026 revisions (recorded in 2026, rejected by 'recorded in fiscal 2025'):", 1274 + 10 - 66)
print("  Doc 5 three vs six months consistent with Q1 2026 +10:", 66 - 56 == 10)

# i02: like-for-like comparable currency neutral EPS growth, July 2025 vs July 2026 outlooks
exp_2025 = 8.0                     # Doc 1 L209 "approximately 8%" (comparable currency neutral EPS)
comp_eps_2026 = (9.0, 10.0)        # Doc 5 L203 comparable EPS growth range
fx_2026 = 3.0                      # Doc 5 L203 "Approx. 3% currency tailwind" (included)
ad_2026 = -1.0                     # Doc 5 L203 "Approx. 1% headwind from acquisitions and divestitures"
ex_ad_2026 = (7.0, 8.0)            # Doc 5 L202 comparable currency neutral EPS excluding A&D
ccn_2026 = tuple(x - fx_2026 for x in comp_eps_2026)                 # route 1
ccn_2026_b = tuple(x + ad_2026 for x in ex_ad_2026)                  # route 2
assert ccn_2026 == ccn_2026_b == (6.0, 7.0)
mid = sum(ccn_2026) / 2
print("i02 implied 2026 comparable currency neutral EPS growth:", ccn_2026, "midpoint", mid)
print("i02 gold (points below July 2025's ~8%):", exp_2025 - mid)            # 1.5
print("i02 lure (printed ex-A&D 7-8%, midpoint 7.5):", exp_2025 - sum(ex_ad_2026) / 2)   # 0.5
# wrong editions / inputs
print("  April outlook (Doc 4: comparable 8-9%):", exp_2025 - ((8 - 3) + (9 - 3)) / 2)   # 2.5
print("  February outlook (Doc 3: comparable 7-8%):", exp_2025 - ((7 - 3) + (8 - 3)) / 2) # 3.5
print("  2025 actual 9% (Doc 3) instead of July 2025 expectation:", 9.0 - mid)           # 2.5
# FY2025 consistency: ~8% comparable currency neutral minus ~5% currency = ~3% comparable EPS
assert 8 - 5 == 3
