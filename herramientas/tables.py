import re, collections
from text import banks
E = banks("IRAO"); S = banks("IRAS")
src = open(r"C:/Users/caspi/Documents/ds access/Lua/main_es.lua", encoding="utf-8").read()
lines = src.split("\n")
idx = collections.defaultdict(list)
for b, bk in enumerate(E):
    if not bk: continue
    for j, s in enumerate(bk):
        if s: idx[s].append((b, j))
lit = re.compile(r'"([^"\n]{150,})"')
for ln, l in enumerate(lines, 1):
    if l.lstrip().startswith("--"): continue
    for m in lit.finditer(l):
        t = m.group(1)
        sep = "|" if t.count("|") > t.count(",") else ","
        items = t.split(sep)
        votes = collections.Counter()
        for it in items:
            for b, j in idx.get(it, ()): votes[b] += 1
        nm = re.findall(r'(\w+)\s*=\s*$', l[:m.start()])
        if len(items) > 3:
            print(f"{ln:6d} {nm[0] if nm else '?':14s} n={len(items):5d} sep={sep} banks={votes.most_common(3)}")
