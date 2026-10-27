"""Author arithmetic for aq-06007 sketches i01 and i02 (inputs as printed; see the sketches)."""

# i01: three-year permit goal (50%, Doc 11 L124 / Doc 10 L224) measured from 2021-22,
# applied to applications industry lodged (Doc 2 Table 3, "Industry applications").
goal_share = 0.50
ind_fy2022 = 77_141   # FY2022 = 2021-22 (Doc 2 L394)
ind_fy2025 = 94_088   # FY2025 = 2024-25 (Doc 2 L397)
target = goal_share * ind_fy2022
fall = (ind_fy2025 - target) / ind_fy2025 * 100
print(f"i01 gold: target {target:,.1f}; required fall {fall:.4f}% -> {fall:.1f}%")

# Lures for i01
ata_2122, ata_2425 = 143_000, 196_629       # Doc 11's "permit applications" (= Doc 2 NHVR cases)
cases_fy2022, cases_fy2025 = 143_951, 196_629
ind_fy2021 = 69_891                          # FY2021 misread as 2021-22
consent_fy2022, consent_fy2025 = 233_843, 318_027
for label, base, now in [("ATA series", ata_2122, ata_2425),
                         ("NHVR cases", cases_fy2022, cases_fy2025),
                         ("consent requests", consent_fy2022, consent_fy2025),
                         ("FY2021 as base", ind_fy2021, ind_fy2025)]:
    t = goal_share * base
    print(f"i01 lure {label}: {(now - t) / now * 100:.1f}%")
print(f"i01 alt base (fall as share of 2021-22): {(ind_fy2025 - target) / ind_fy2022 * 100:.1f}%")

# i02: output gap between the 2029 and 2024 shortfalls of the IRU 2024 report,
# valued at the NHVR's GVA per driver (Doc 2 L491).
gva = 184_000
iru_2024 = 28_000     # Doc 10 L360/L782, Doc 5 L73
iru_2029 = 78_000     # Doc 2 L493 (fn 16 IRU), Doc 10 L360/L782, Doc 15 L50
gap = (iru_2029 - iru_2024) * gva
print(f"i02 gold: {(iru_2029 - iru_2024):,} drivers x ${gva:,} = ${gap:,} -> ${gap / 1e9:.1f} billion")
nhvr_now = 26_000     # Doc 2 L481, fn 10 NatRoad (2024)
lure = (iru_2029 - nhvr_now) * gva
print(f"i02 lure (NHVR's 26,000 base): ${lure:,} -> ${lure / 1e9:.1f} billion; printed 14.4 - 4.8 = {14.4 - 4.8:.1f}")
print(f"i02 check of Doc 2's printed products: 26,000 x 184,000 = {26_000 * gva:,}; 78,000 x 184,000 = {78_000 * gva:,}")
