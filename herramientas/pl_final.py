import re
from pl_text import banks, norm
import collections
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
s=open(LUA,encoding="utf-8").read()
a='say("Pokemon " .. GAME:gsub("^%l", string.upper) .. " accessibility loader running.")'
assert s.count(a)==1; s=s.replace(a,'say("Accesibilidad de Pokémon Platino en marcha.")')
i=s.index("TRAINER_KEY = {"); j=s.index("\n\t}",i)
blk=s[i:j]; names=re.findall(r'(?:\["([^"]+)"\]|\b([A-Z][A-Za-z]+))\s*=\s*"[a-z-]+"',blk)
E=banks('CPUE');T=banks('CPUS');ix=collections.defaultdict(collections.Counter)
for b,bk in enumerate(E):
    for k,x in enumerate(bk):
        if norm(x) and norm(T[b][k]) and "·" not in T[b][k]: ix[norm(x).upper()][norm(T[b][k])]+=1
al={}
for x,y in names:
    n=x or y
    if n.upper() in ix:
        t=ix[n.upper()].most_common(1)[0][0]
        if t.upper()!=n.upper(): al[t.capitalize() if t.isupper() else t]=n
print(al)
lst=", ".join('["%s"] = "%s"'%(k,v) for k,v in al.items())
k=j+len("\n\t}")
s=s[:k]+'\n\tfor es, en in pairs({ %s }) do TRAINER_KEY.story[es] = TRAINER_KEY.story[en] end   -- ES: la lista dice los nombres en espanol'%lst+s[k:]
open(LUA,"w",encoding="utf-8",newline="").write(s)
