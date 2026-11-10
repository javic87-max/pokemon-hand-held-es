import re
L=open(r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua",encoding="utf-8").read().split("\n")
es=set("el la los las de del en un una y o que por para con se tu su es al lo".split())
skip=re.compile(r"console\.|dbg\(|\bbad\(|\.bad\(|error\(|why\s*=|log\(|string\.find|:find\(|:match\(|:gsub\(|gmatch|why\(|fail\(|reason|screen\(|name = \"")
C={}
for i,l in enumerate(L,1):
    if l.lstrip().startswith("--") or re.search(r'[\u3040-\uD7FF]',l): continue
    code=l.split(" --")[0]
    if skip.search(code): continue
    for t in re.findall(r'"([^"\n]*[A-Za-z][^"\n]*)"',code):
        w=[x.lower() for x in re.findall(r"[A-Za-z]+",t)]
        if re.search(r"[áéíóúñ¿¡ÁÉÍÓÚÑ]",t) or not w or set(w)&es and len(w)<7: continue
        if re.fullmatch(r"[a-z0-9_.\-]+",t) and len(t)>12: continue
        if re.search(r"\.\.|%s\+|%08X|^\)|^ (and|or)\b",t): continue
        C.setdefault(t,[]).append(i)
print(len(C))
for t,v in sorted(C.items(),key=lambda x:x[1][0]): print(v[0],len(v),t[:70])
