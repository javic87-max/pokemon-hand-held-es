"""Aplica a games/platinum_es.lua las direcciones de la ROM espanola CPUS, medidas contra CPUE."""
import re, collections, shutil
import port
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from port import port_in, candidates
from vt import per_module
from lit import port_lit
BASE=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum.lua"; OUT=BASE.replace("platinum.lua","platinum_es.lua")
FORCE={0x0206AEAC:0xA4,0x02070A24:0x94,0x021E06A8:0x250}          # medido por sus literales y por vecindad
def mod_of(X):
    if 0x021D2500<=X<0x021D2A70 and X in SPEAR or X in SPEAR: return 100
    if X==0x021D4130: return 99
    if X==0x021D46C8: return 100
    if 0x02249960<=X<0x0224C000: return 8
    return None
SPEAR={0x021d3a90,0x021d3ab4,0x021d3e16,0x021d3e46,0x021d2516,0x021d25aa,0x021d25e8,0x021d2696,0x021d293a,0x021d29b8,0x021d2a6c}
L=open(BASE,encoding="utf-8").read().split("\n")
ad=set()
for l in L:
    if not l.lstrip().startswith("--"):
        ad|={int(x,16) for x in re.findall(r"0x02[0-9A-Fa-f]{6}",l.partition("--")[0])}
res={}; how=collections.Counter(); flag=[]
for X in sorted(ad):
    if X in FORCE: res[X]=FORCE[X]; how['fijado']+=1; continue
    m=mod_of(X)
    if m is not None:
        v=port_in('CPUE','CPUS',m,X&~1,L=16,span=48).most_common(1)
        if v: res[X]=v[0][0]; how['modulo']+=1; continue
    lv=[(a-X,n) for a,n in port_lit('CPUE','CPUS',X,slack=0).most_common(3) if abs(a-X)<0x400]
    if lv: res[X]=lv[0][0]; how['literal']+=1; continue
    r=per_module('CPUE','CPUS',X); vts=[x for x in r if x[1]=="VT"]
    ds=collections.Counter(x[2] for x in (vts or r))
    if len(ds)==1: res[X]=next(iter(ds)); how['codigo unico']+=1; continue
    if 0x200 in ds: res[X]=0x200; how['base +0x200']+=1; flag.append(hex(X)); continue
    flag.append(hex(X)+" SIN RESOLVER"); how['SIN']+=1
print(how); print("revisar:",flag); print(collections.Counter(hex(v) for v in res.values()).most_common())
n=0
for i,l in enumerate(L):
    if l.lstrip().startswith("--"): continue
    code,sep,com=l.partition("--")
    def rep(m):
        global n
        X=int(m.group(0),16)
        if X in res and res[X]: n+=1; return "0x%08X"%(X+res[X])
        return m.group(0)
    L[i]=re.sub(r"0x02[0-9A-Fa-f]{6}",rep,code)+sep+com
open(OUT,"w",encoding="utf-8",newline="").write("\n".join(L)); print("reescritas",n)
