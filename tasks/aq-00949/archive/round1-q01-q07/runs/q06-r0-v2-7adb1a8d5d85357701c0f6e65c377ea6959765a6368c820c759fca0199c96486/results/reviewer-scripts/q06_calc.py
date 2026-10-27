from decimal import Decimal as D, ROUND_HALF_UP
def r(x, q='1'): return x.quantize(D(q), rounding=ROUND_HALF_UP)

# MBoed (D07 L161) and days: 1Q=90, 2Q=91, 3Q=92, 4Q=92 (2025, 2026 non-leap)
mboed = {'1Q25':D('1090.4'),'2Q25':D('1134.1'),'3Q25':D('1301.2'),'4Q25':D('1399.0'),'1Q26':D('1383.8'),'2Q26':D('1410.4')}
days  = {'1Q25':90,'2Q25':91,'3Q25':92,'4Q25':92,'1Q26':90,'2Q26':91}
mmboe_printed = {'1Q25':D('98.1'),'2Q25':D('103.2'),'3Q25':D('119.7'),'4Q25':D('128.7'),'1Q26':D('124.5'),'2Q26':D('128.3')}
mmboe_rebuilt = {k: mboed[k]*days[k]/1000 for k in mboed}
print("rebuilt MMBoe:", {k:str(v) for k,v in mmboe_rebuilt.items()})
print("check printed = round(rebuilt,1):", all(r(mmboe_rebuilt[k],'0.1')==mmboe_printed[k] for k in mboed))

def bridge(dv, margin, shares, step_round=True):
    cm = dv*margin
    if step_round:
        cm_r = r(cm); tax = r(cm_r*D('0.22')); ni = cm_r - tax
    else:
        cm_r = cm; tax = cm*D('0.22'); ni = cm - tax
    return cm, cm_r, tax, ni, ni/shares

# Reconcile printed sequential bridges (GAAP margin incl. TEC, later-quarter diluted shares)
printed = [
 ('D02 1Q25 vs 4Q24', None, None, D('20.09'), D('553'), '(54) 12 (42) (0.08)'),
 ('D04 2Q25 vs 1Q25', '2Q25','1Q25', D('14.94'), D('546'), '76 (17) 59 0.11'),
 ('D05 3Q25 vs 2Q25', '3Q25','2Q25', D('13.42'), D('544'), '221 (49) 172 0.32'),
 ('D06 1Q26 vs 4Q25', '1Q26','4Q25', D('18.11'), D('535'), '(76) 17 (59) (0.11)'),
 ('D07 2Q26 vs 1Q26', '2Q26','1Q26', D('25.51'), D('529'), '97 (21) 76 0.14'),
]
for name,a,b,m,s,pr in printed:
    if a is None: continue
    dvp = mmboe_printed[a]-mmboe_printed[b]; dvr = mmboe_rebuilt[a]-mmboe_rebuilt[b]
    p = bridge(dvp,m,s); q = bridge(dvr,m,s)
    print(f"{name}: printed-MMBoe dv={dvp} margin={r(p[0],'0.001')}->{p[1]} tax={p[2]} NI={p[3]} EPS={r(p[4],'0.0001')} | rebuilt dv={r(dvr,'0.0001')} margin={r(q[0],'0.001')}->{q[1]} tax={q[2]} NI={q[3]} EPS={r(q[4],'0.0001')} | printed: {pr}")

print()
# Gold: 2Q25 -> 2Q26 YoY
for label, dv in [('printed MMBoe', mmboe_printed['2Q26']-mmboe_printed['2Q25']), ('rebuilt MBoed x days', mmboe_rebuilt['2Q26']-mmboe_rebuilt['2Q25'])]:
    for sr in (True, False):
        cm, cmr, tax, ni, eps = bridge(dv, D('25.51'), D('529'), sr)
        print(f"{label:22s} step_round={sr}: dv={r(dv,'0.0001')} cm={r(cm,'0.001')} tax={r(tax,'0.001')} NI={r(ni,'0.001')} EPS={r(eps,'0.00001')} -> {r(eps,'0.01')}")
# MBoed rounding band (+-0.05 MBoed each)
lo = (mboed['2Q26']-D('0.05'))*91/1000 - (mboed['2Q25']+D('0.05'))*91/1000
hi = (mboed['2Q26']+D('0.05'))*91/1000 - (mboed['2Q25']-D('0.05'))*91/1000
print("rebuilt dv band:", lo, hi, " EPS band:", r(lo*D('25.51')*D('0.78')/529,'0.00001'), r(hi*D('25.51')*D('0.78')/529,'0.00001'))
# break-even dv for 0.945
print("dv giving exactly 0.945:", r(D('0.945')*529/(D('25.51')*D('0.78')),'0.0001'))
