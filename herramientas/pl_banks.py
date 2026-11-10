"""Bloques [banco] = { [n]="..." } de PM.text: se traduce por su banco declarado. Va despues de pl_names.py."""
import re, collections
from pl_text import banks, norm
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
E=banks('CPUE');S=banks('CPUS')
def conv(s):
    s=re.sub(r"\{[0-9A-F]{4}:(\d+)(?:,\d+)*\}",r"{\1}",s)
    s=re.sub(r"\{[0-9A-F]{4}:\}","",s).replace("\n"," ")
    return re.sub(r"\s+"," ",s).strip()
L=open(LUA,encoding="utf-8").read().split("\n")
head=re.compile(r"^\t\t\[(\d+)\] = \{\s*(?:--\s*(.*))?$")
ent=re.compile(r'\[(\d+)\]\s*=\s*"([^"\n]*)"')
bank=None;c=collections.Counter();names={}
for i,l in enumerate(L):
    m=head.match(l)
    if m: bank=int(m.group(1)); names[bank]=m.group(2); continue
    if bank is None: continue
    if l.startswith("\t\t}"): bank=None; continue
    if bank>=len(E) or l.lstrip().startswith("--"): continue
    code,sep,com=l.partition(" --")
    b=bank
    def rep(mm):
        j,t=int(mm.group(1)),mm.group(2)
        if j>=len(E[b]): return mm.group(0)
        for src,dst in ((norm(E[b][j]),norm(S[b][j])),(conv(E[b][j]),conv(S[b][j]))):
            if t==src and dst and dst!=src and "·" not in dst:
                c[b]+=1; return '[%d] = "%s"'%(j,dst.replace("\\","").replace('"',"'"))
        return mm.group(0)
    L[i]=ent.sub(rep,code)+sep+com
open(LUA,"w",encoding="utf-8",newline="").write("\n".join(L))
print(sum(c.values()),[(b,names.get(b),n) for b,n in c.most_common(25)])
print("bancos declarados",len(names),[ (b,names[b]) for b in sorted(names) if b>=700])
s=open(LUA,encoding="utf-8").read()
for a,b in [('local CARD_COLORS={"red","cobalt blue","bronze","silver","gold","black"}','local CARD_COLORS={"roja","azul cobalto","bronce","plata","oro","negra"}'),
            ('"TRAINER CARD, level "..rank','"Ficha de entrenador, nivel "..rank')]:
    print(s.count(a)); s=s.replace(a,b)
open(LUA,"w",encoding="utf-8",newline="").write(s)
