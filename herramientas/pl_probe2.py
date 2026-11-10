import re, collections, struct, ndspy.rom, ndspy.narc
import port
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from vt import per_module
from port import D, ROMS
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum.lua"
src=open(LUA,encoding="utf-8").read()
code="\n".join(l.split("--")[0] for l in src.split("\n"))
ad=sorted({int(x,16) for x in re.findall(r"0x02[0-9A-Fa-f]{6}",code)})
kinds=collections.Counter(); deltas=collections.Counter(); amb=[]; none=[]
for X in ad:
    r=per_module('CPUE','CPUS',X)
    vts=[x for x in r if x[1]=="VT"]; show=vts or r
    ds=sorted({x[2] for x in show})
    if not ds: kinds['sin medir (memoria temporal o datos)']+=1; none.append(hex(X))
    elif len(ds)==1: kinds['un valor claro']+=1; deltas[hex(ds[0])]+=1
    else: kinds['varios candidatos (hay que fijar el overlay)']+=1; amb.append(hex(X))
print(len(ad),dict(kinds)); print('deltas claros',deltas.most_common(14)); print('sin medir',none[:50])
# textos: descifrado Gen IV
runs=[]
for m in re.finditer(r'\{\s*(0x[0-9A-Fa-f]{4}),\s*((?:"[^"\n]*"\s*(?:\.\.\s*)?)+)\}',src):
    runs.append((int(m.group(1),16),"".join(re.findall(r'"([^"\n]*)"',m.group(2)))))
CM={}
for b,t in runs:
    for i,ch in enumerate(t): CM[b+i]=ch
def dec(b):
    n,seed=struct.unpack_from("<HH",b,0); key=(seed*0x2FD)&0xFFFF; out=[]
    for i in range(n):
        k2=(key*(i+1))&0xFFFF; kk=k2|(k2<<16)
        off,sz=struct.unpack_from("<II",b,4+i*8); off^=kk; sz^=kk
        k=(0x91BD3*(i+1))&0xFFFF; s=[]
        for j in range(sz):
            c=struct.unpack_from("<H",b,off+j*2)[0]^k; k=(k+0x493D)&0xFFFF
            if c==0xFFFF: break
            s.append(CM.get(c,"·"))
        out.append("".join(s))
    return out
B={}
for k in ('CPUE','CPUS'):
    r=ndspy.rom.NintendoDSRom.fromFile(D+ROMS[k]); na=ndspy.narc.NARC(r.getFileByName('msgdata/pl_msg.narc'))
    bs=[]
    for f in na.files:
        try: bs.append(dec(f))
        except Exception: bs.append(None)
    B[k]=bs
E,S=B['CPUE'],B['CPUS']
print('bancos',len(E),len(S),'fallos',sum(x is None for x in E),sum(x is None for x in S),'mismo n entradas',sum(1 for a,b in zip(E,S) if a is not None and b is not None and len(a)==len(b)))
miss=sum(s.count("·") for bk in S if bk for s in bk); tot=sum(len(s) for bk in S if bk for s in bk); print('caracteres sin mapa ES',miss,'de',tot)
for w in ("Pound","POUND","Bulbasaur","BULBASAUR","Stench"):
    for i,bk in enumerate(E):
        if bk and w in bk: j=bk.index(w); print(w,i,j,'->',S[i][j]); break
