import port, struct, difflib, re
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from port import M
def H(k):
    b,d=M(k)[73]; return b,struct.unpack(f"<{len(d)//2}H",d[:len(d)&~1])
def table(b,h,fn):
    i=(fn-b)//2
    for k in range(i,i+40):
        if h[k]&0xFF00==0x2800 or (h[k]&0xF800)==0x2800 and h[k]&0xFF>30:
            n=h[k]&0xFF
            # "add r0,pc / ldrh / ... " tabla justo despues, alineada
            for t in range(k,k+16):
                if h[t+1]<0x2000 and h[t+2]<0x2000 and h[t+3]<0x2000 and h[t+1]%2==0 and h[t+2]%2==0 and h[t+1]<h[t+2]+0x100:
                    return n,t+1
def sig(h,i):
    o=[]
    for x in h[i:i+10]:
        if x&0xF800 in (0xF000,0xF800): o.append(0xF000)
        elif x&0xF800==0x2000: o.append(x&0xF800)          # movs rN,#imm (estado siguiente)
        elif x&0xF800==0x4800: o.append(0x4800)            # ldr literal
        else: o.append(x)
    return tuple(o)
for k,fn in (('CPUE',0x021D2318),('CPUS',0x021D25B4)):
    b,h=H(k); r=table(b,h,fn); print(k,hex(fn),r,hex(b+r[1]*2) if r else None)
eb,eh=H('CPUE'); sb,sh=H('CPUS'); en,et=table(eb,eh,0x021D2318); sn,st=table(sb,sh,0x021D25B4)
E=[sig(eh,et+eh[et+s]//2) for s in range(en+1)]; S=[sig(sh,st+sh[st+s]//2) for s in range(sn+1)]
m={}
for tag,a,b_,c,d in difflib.SequenceMatcher(None,E,S,autojunk=False).get_opcodes():
    if tag=='equal':
        for x in range(b_-a): m[a+x]=c+x
    else: print(tag,list(range(a,b_)),'->',list(range(c,d)))
import json; json.dump(m,open('pl_ov73_states.json','w')); print(len(E),len(S),len(m))
L=open(r"C:/Users/caspi/Documents/ds access/Lua/games/platinum.lua",encoding="utf-8").read().split("\n")
for i,l in enumerate(L[4490:4565],4491):
    for nm,v in re.findall(r"(ST_[A-Z0-9_]+)\s*=\s*(\d+)",l.split("--")[0]): print(i,nm,v,'->',m.get(int(v),'?'))
