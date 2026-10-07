import re, io
base = "D:/Dev/Docket/tasks/aq-00949/text/"
def load(d): return io.open(base+d+".txt", encoding="utf-8").read()
def ws(s): return re.sub(r'\s+', ' ', s)
def depipe(s):
    s = re.sub(r'^\|\s*-{3}.*$', '', s, flags=re.M)
    return ws(s.replace('|', ' '))
quotes = [
 ('D03', "May 30, 2025"),
 ('D03', "today announced a definitive agreement with Canada Pension Plan Investment Board (CPP) and Encino Energy under which EOG will acquire Encino Acquisition Partners"),
 ('D07', "2Q 2026 1Q 2026 4Q 2025 3Q 2025 2Q 2025"),
 ('D07', "Volume - Million Barrels of Oil Equivalent - (a) 128.3 124.5 128.7 119.7 103.2"),
 ('D07', "Multiplied by: 2Q 2026 Composite Average Margin per Boe (GAAP) (Including Total Exploration Costs)"),
 ('D07', "Composite Average Margin per Boe (including Total Exploration Costs) - [(e) / (a) - (j) / (a)] 25.51"),
 ('D07', "Less: Income Tax Benefit (Provision) Imputed (based on 22%)"),
 ('D07', "2Q 2026 Average Number of Common Shares - Diluted 529"),
]
for d,q in quotes:
    t = load(d)
    raw = q in t; w = ws(q) in ws(t); dp = ws(q) in depipe(t)
    print(f"{d} raw={raw} ws-normalized={w} depiped={dp} :: {q[:70]}")
# reasoning number probe for Doc 7 steps: derived operands
t7 = load('D07'); t3 = load('D03')
for n in ['25.1','640','141','499','529','25.51','22%','103.2','128.3','0.94','0.14','3.8','124.5']:
    hits = [m.start() for m in re.finditer(re.escape(n), t7)]
    exact = [m.start() for m in re.finditer(r'(?<![\d.,])'+re.escape(n)+r'(?![\d])', t7)]
    print(f"D07 '{n}': substring hits={len(hits)} standalone-token hits={len(exact)}")
for n in ['2025','30','3']:
    print(f"D03 '{n}' present:", n in t3)
