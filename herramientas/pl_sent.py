"""Frases completas de platinum_es.lua (3 palabras o mas) que coinciden exactamente con un texto del juego."""
import re, collections, sys
from pl_text import banks, norm
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
E=banks('CPUE');S=banks('CPUS')
ix=collections.defaultdict(collections.Counter)
for b,bk in enumerate(E):
    for j,s in enumerate(bk):
        n=norm(s); t=norm(S[b][j])
        if n and t and "·" not in t: ix[n][t]+=1
L=open(LUA,encoding="utf-8").read().split("\n")
skip=re.compile(r"console\.|dbg\(|\bbad\(|\.bad\(|error\(|why\s*=|log\(|:find\(|:match\(|:gsub\(|gmatch|[=~]=\s*\"")
n=0;amb=0
def unesc(t): return t.replace('\\"','"').replace("\'","'")
for i,l in enumerate(L):
    if l.lstrip().startswith("--") or re.search(r'[\u3040-\uD7FF]',l): continue
    code,sep,com=l.partition(" --")
    if skip.search(code): continue
    def rep(m):
        global n,amb
        t=m.group(1); k=norm(unesc(t))
        if len(k.split())<3 or k not in ix: return m.group(0)
        c=ix[k].most_common(2)
        if len(c)>1 and c[0][1]==c[1][1]: amb+=1
        n+=1; return '"%s"'%c[0][0].replace("\\","").replace('"',"'")
    L[i]=re.sub(r'"([^"\n]*)"',rep,code)+sep+com
print("frases",n,"ambiguas",amb)
if "--write" in sys.argv: open(LUA,"w",encoding="utf-8",newline="").write("\n".join(L))
