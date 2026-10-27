from decimal import Decimal as D, ROUND_HALF_UP
def r(x, q='0.01'): return x.quantize(D(q), rounding=ROUND_HALF_UP)
def eps(dv, m, s, tax=D('0.22')): return dv*m*(1-tax)/s
dv = D('128.3')-D('103.2')
rows = [
 ('gold: 2Q26 margin incl TEC 25.51, 2Q26 diluted 529', eps(dv,D('25.51'),D('529'))),
 ('2Q26 basic shares 526', eps(dv,D('25.51'),D('526'))),
 ('6M26 diluted 532', eps(dv,D('25.51'),D('532'))),
 ('2Q25 diluted 546', eps(dv,D('25.51'),D('546'))),
 ('2Q25 margin 14.94, 2Q26 shares', eps(dv,D('14.94'),D('529'))),
 ('2Q25 margin 14.94, 2Q25 shares 546', eps(dv,D('14.94'),D('546'))),
 ('margin excl TEC 26.26', eps(dv,D('26.26'),D('529'))),
 ('margin excl DD&A and TEC 36.07', eps(dv,D('36.07'),D('529'))),
 ('operating income per Boe 27.50', eps(dv,D('27.50'),D('529'))),
 ('no tax', eps(dv,D('25.51'),D('529'),D('0'))),
 ('effective tax 21.7% (FY25)', eps(dv,D('25.51'),D('529'),D('0.217'))),
 ('avg margin (25.51+14.94)/2', eps(dv,(D('25.51')+D('14.94'))/2,D('529'))),
 ('1Q25->1Q26: (124.5-98.1) x 18.11 / 535', eps(D('124.5')-D('98.1'),D('18.11'),D('535'))),
 ('3Q25->? (closing) not answerable', None),
]
for n,v in rows:
    print(f"{n:52s}", '-' if v is None else f"{v:.5f} -> {r(v)}")
# 1Q25->1Q26 stepwise EOG rounding
cm = (D('124.5')-D('98.1'))*D('18.11'); print('1Q25->1Q26 stepwise', cm, r(cm,'1'), r(r(cm,'1')*D('0.22'),'1'), (r(cm,'1')-r(r(cm,'1')*D('0.22'),'1'))/535)
# sequential printed effects
seq = {'2Q25->3Q25 (D05)':D('0.32'),'4Q25->1Q26 (D06)':D('-0.11'),'1Q26->2Q26 (D07)':D('0.14')}
q4 = eps(D('128.7')-D('119.7'),D('6.70'),D('539'))
print('self-computed 3Q25->4Q25:', r(q4,'0.0001'), '->', r(q4))
print('chain sum printed only:', sum(seq.values()), ' with 4Q25 step:', sum(seq.values())+r(q4))
# rounding of 25.51: underlying 3274/128.3 and with rebuilt volume
print('margin from $ totals 3274/128.3 =', r(D(3274)/D('128.3'),'0.0001'), ' 3274/128.3464 =', r(D(3274)/D('128.3464'),'0.0001'))
print('gold with 25.518 margin:', r(eps(dv,D(3274)/D('128.3'),D('529')),'0.00001'))
