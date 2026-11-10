"""Traduce tablas numeradas de platinum_es.lua: cada bloque [n]="texto" se asocia al banco donde mas indices coinciden."""
import re, sys, collections
from pl_text import banks, norm
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
E=banks('CPUE'); S=banks('CPUS')
L=open(LUA,encoding="utf-8").read().split("\n")
pat=re.compile(r'\[(\d+)\]\s*=\s*"([^"\n]*)"')
def unesc(t): return t.replace('\\"','"').replace("\'","'").replace("\n"," ")
def conv(s):
    s=re.sub(r"\{[0-9A-F]{4}:(\d+)(?:,\d+)*\}",r"{\1}",s)
    s=re.sub(r"\{[0-9A-F]{4}:\}","",s).replace("\n"," ")
    return re.sub(r"\s+"," ",s).strip()
ix=collections.defaultdict(set)
for b,bk in enumerate(E):
    for j,s in enumerate(bk):
        if norm(s): ix[(j,norm(s))].add(b); ix[(j,conv(s))].add(b)
blocks=[];cur=[];gap=0
for i,l in enumerate(L):
    if not l.lstrip().startswith("--") and pat.search(l.split(" --")[0]) and not re.search(r'[\u3040-\uD7FF]',l):
        if gap>2 and cur: blocks.append(cur);cur=[]
        cur.append(i);gap=0
    else: gap+=99 if "{" in l or "}" in l else 1
if cur: blocks.append(cur)
tot=done=0;weak=[];miss=[]
for bl in blocks:
    v=collections.Counter();ents=[]
    for i in bl:
        for m in pat.finditer(L[i].split(" --")[0]):
            k=(int(m.group(1)),conv(unesc(m.group(2)))); ents.append(k)
            for b in ix.get(k,()): v[b]+=1
    if not v: weak.append((bl[0]+1,len(ents),ents[:2]));continue
    b,n=v.most_common(1)[0]
    if n<max(2,len(ents)*0.5): weak.append((bl[0]+1,len(ents),n,ents[:2]));continue
    for i in bl:
        code,sep,com=L[i].partition(" --")
        count=[0]
        def rep(m):
            j,t=int(m.group(1)),conv(unesc(m.group(2)))
            if j<len(E[b]) and t in (norm(E[b][j]),conv(E[b][j])):
                out=norm(S[b][j]) if t==norm(E[b][j]) else conv(S[b][j])
                if out and "·" not in out:
                    count[0]+=1
                    return '[%d] = "%s"'%(j,out.replace("\\","").replace('"',"'"))
            miss.append((i+1,j,t[:30],b))
            return m.group(0)
        L[i]=pat.sub(rep,code)+sep+com; done+=count[0]
    tot+=len(ents)
print("bloques",len(blocks),"entradas",tot,"traducidas",done);print("flojos",len(weak));print("fallos",len(miss),miss[:30])
if "--write" in sys.argv: open(LUA,"w",encoding="utf-8",newline="").write("\n".join(L));print("escrito")
