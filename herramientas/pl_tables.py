import re, collections
from pl_text import banks, norm
E=banks('CPUE'); S=banks('CPUS')
print('sin mapa ES', sum(s.count("·") for b in S for s in b), 'EN', sum(s.count("·") for b in E for s in b), 'total', sum(len(s) for b in S for s in b))
ix=collections.defaultdict(list)
for b,bk in enumerate(E):
    for j,s in enumerate(bk):
        if norm(s): ix[norm(s)].append((b,j))
L=open(r"C:/Users/caspi/Documents/ds access/Lua/games/platinum.lua",encoding="utf-8").read().split("\n")
pat=re.compile(r'"([^"\n]{1,})"|\'([^\'\n]{1,})\'|\[==\[(.*?)\]==\]')
n=hit=0; big=[]
for i,l in enumerate(L,1):
    if l.lstrip().startswith("--") or re.search(r'[\u3040-\uD7FF]',l): continue
    code=l.split(" --")[0]
    for m in pat.finditer(code):
        t=next(g for g in m.groups() if g is not None)
        for sep in ("\1","|",",",None):
            if sep is None or t.count(sep)>=4: break
        items=t.split(sep) if sep else [t]
        got=sum(1 for x in items if norm(x) in ix); n+=len(items); hit+=got
        if len(items)>=8: big.append((i,len(items),sep,got))
print('literales',n,'en banco',hit); print('listas grandes',big[:60])
