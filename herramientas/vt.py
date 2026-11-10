from port import *
import struct
def rd(data,o): return struct.unpack_from("<I",data,o)[0]
def per_module(src,dst,X):
    out=[]
    for m in candidates(src,X):
        if m not in M(dst): continue
        sb,sd=M(src)[m]; db,dd=M(dst)[m]; o=(X&~1)-sb
        if o+12>len(sd): continue
        ws=[rd(sd,o+4*i) for i in range(3)]
        vt=all(sb<=w<sb+len(sd) and w&1 for w in ws)
        res=None
        if vt:
            ps=[]
            for w in ws:
                v=port_in(src,dst,m,w&~1,L=16,span=64)
                if not v: break
                ps.append(w+v.most_common(1)[0][0])
            if len(ps)==3:
                pat=struct.pack("<3I",*ps); p=dd.find(pat)
                if p>=0 and dd.find(pat,p+1)<0: res=("VT",db+p+(X&1)-X)
        if res is None:
            v=port_in(src,dst,m,X&~1,L=16,span=48)
            if v:
                d,n=v.most_common(1)[0]
                if n>=4: res=("code",d,n)
        if res: out.append((m,)+res)
    return out
if __name__=="__main__":
    src,dst=sys.argv[1],sys.argv[2]
    for a in sys.argv[3:]:
        X=int(a,16)
        r=per_module(src,dst,X)
        vts=[x for x in r if x[1]=="VT"]
        show=vts if vts else r
        print(f"{X:08X}: "+"; ".join(f"ov{x[0]}:{x[1]}{x[2]:+#x}" for x in show))
