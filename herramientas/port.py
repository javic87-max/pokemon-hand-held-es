import sys, pickle, os, collections
import ndspy.rom, ndspy.code, ndspy.codeCompression as cc
D="D:/juegos/juegos pokemon/roms/ds/"
ROMS={'IRAO':"Pokemon - White Version (USA, Europe) (NDSi Enhanced).nds",'IRBO':"5585 - Pokemon - Black Version (USA, Europe) (NDSi Enhanced) [b].nds",'IRAS':"Pokémon Blanco.nds",'IRBS':"Pokemon Negro.nds"}
def load(k):
    cache=f"{k}.pkl"
    if os.path.exists(cache): return pickle.load(open(cache,'rb'))
    r=ndspy.rom.NintendoDSRom.fromFile(D+ROMS[k])
    raw=bytes(r.arm9)
    try: dec=bytes(cc.decompress(raw))
    except Exception as e: print("arm9 dec fail",e); dec=raw

    # arm9 save may re-add things; use sections instead
    data=b''; 
    mods={"arm9":(r.arm9RamAddress, dec)}
    ovs=r.loadArm9Overlays()
    for i,o in ovs.items(): mods[i]=(o.ramAddress, bytes(o.data))
    pickle.dump(mods,open(cache,'wb')); return mods

MODS={}
def M(k):
    if k not in MODS: MODS[k]=load(k)
    return MODS[k]
def candidates(k, addr):
    out=[]
    for mid,(base,data) in M(k).items():
        if base<=addr<base+len(data): out.append(mid)
    return out
def port_in(src, dst, mid, addr, L=20, span=256, step=4):
    sb,sd=M(src)[mid]; db,dd=M(dst)[mid]
    off=addr-sb; votes=collections.Counter()
    for k in range(-span, span+1, step):
        s=off+k
        if s<0 or s+L>len(sd): continue
        w=sd[s:s+L]
        if len(set(w))<4: continue
        p=dd.find(w)
        if p<0 or dd.find(w,p+1)>=0: continue
        votes[(db+p)-(sb+s)]+=1
    return votes
def port(src,dst,addr,mid=None):
    mids=[mid] if mid is not None else candidates(src,addr)
    best=None
    for m in mids:
        v=port_in(src,dst,m,addr)
        if v:
            d,n=v.most_common(1)[0]
            if best is None or n>best[2]: best=(m,d,n,dict(v.most_common(3)))
    return best
if __name__=="__main__":
    src,dst=sys.argv[1],sys.argv[2]
    for a in sys.argv[3:]:
        A=int(a,16); r=port(src,dst,A)
        print(f"{A:08X} ->", "none" if not r else f"{A+r[1]:08X} (mod {r[0]}, delta {r[1]:+#x}, votes {r[3]})")
