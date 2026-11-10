import re, collections
import port
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from vt import per_module
from lit import port_lit
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum.lua"
L=open(LUA,encoding="utf-8").read().split("\n")
use={}
for i,l in enumerate(L,1):
    if l.lstrip().startswith("--"): continue
    code,_,com=l.partition("--")
    for x in re.findall(r"0x02[0-9A-Fa-f]{6}",code):
        X=int(x,16)
        if X not in use:
            mm=re.findall(r"(\w+)\s*=\s*"+x,code)
            use[X]=(i,mm[0] if mm else "?",com.strip()[:60])
for X in sorted(use):
    i,nm,com=use[X]
    r=per_module('CPUE','CPUS',X); vts=[x for x in r if x[1]=="VT"]
    if vts: m="VT "+" ".join(f"ov{x[0]}:{x[2]:+#x}" for x in vts)
    else:
        c=collections.defaultdict(list)
        for x in r: c[x[2]].append(x[0])
        m=" | ".join(f"{d:+#x}:{','.join(map(str,v[:6]))}{'+' if len(v)>6 else ''}" for d,v in sorted(c.items()))
    v=port_lit('CPUE','CPUS',X,slack=0).most_common(3)
    print(f"{X:08X} L{i} {nm[:26]} | {m} || lit {[(hex(a-X),n) for a,n in v]} # {com}",flush=True)
