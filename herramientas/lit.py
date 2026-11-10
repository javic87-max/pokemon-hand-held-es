from port import *
import struct
IDX={}
def words(k):
    if k in IDX: return IDX[k]
    d={}
    for mid,(base,data) in M(k).items():
        n=len(data)//4
        arr=struct.unpack_from(f"<{n}I",data,0)
        for i,w in enumerate(arr):
            if 0x02000000<=w<0x02400000: d.setdefault(w,[]).append((mid,i*4))
    IDX[k]=d; return d
def port_lit(src,dst,X,slack=0x400):
    W=words(src); votes=collections.Counter(); 
    for w in range(X-slack, X+1):
        for (mid,pos) in W.get(w,()):
            if mid not in M(dst): continue
            sb,sd=M(src)[mid]; db,dd=M(dst)[mid]
            v=port_in(src,dst,mid,sb+pos,L=16,span=96)
            if not v: continue
            dlt,n=v.most_common(1)[0]
            if n<3: continue
            q=pos+dlt-(db-sb)
            if q<0 or q+4>len(dd): continue
            w2=struct.unpack_from("<I",dd,q)[0]
            votes[(X+(w2-w))]+=1 if w!=X else 3
        if votes and w==X: pass
    return votes
if __name__=="__main__":
    src,dst=sys.argv[1],sys.argv[2]
    for a in sys.argv[3:]:
        X=int(a,16); v=port_lit(src,dst,X)
        top=v.most_common(3)
        print(f"{X:08X} -> " + ", ".join(f"{t:08X}({t-X:+#x})x{n}" for t,n in top))
