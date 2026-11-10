import ndspy.rom, ndspy.narc, struct, pickle, os
from port import D, ROMS
def dec_file(b):
    nsec,nent,secsz,unk=struct.unpack_from("<HHII",b,0)
    so=struct.unpack_from("<I",b,12)[0]
    out=[]
    for e in range(nent):
        off,ln,_=struct.unpack_from("<IHH",b,so+4+e*8)
        enc=struct.unpack_from(f"<{ln}H",b,so+off)
        if not enc: out.append(""); continue
        key=enc[-1]^0xFFFF; dec=[0]*ln
        for i in range(ln-1,-1,-1):
            dec[i]=enc[i]^key; key=((key>>3)|(key<<13))&0xFFFF
        s=[]; i=0
        while i<ln:
            c=dec[i]
            if c==0xFFFF: break
            if c==0xFFFE: s.append("\n")
            elif c==0xF000:
                n=dec[i+2] if i+2<ln else 0; s.append("{%04X}"%dec[i+1]); i+=3+n; continue
            elif c==0xF100:
                # 9-bit compressed
                acc=bits=0; i+=1
                while i<ln:
                    acc|=dec[i]<<bits; bits+=16; i+=1; stop=False
                    while bits>=9:
                        ch=acc&0x1FF; acc>>=9; bits-=9
                        if ch==0x1FF: stop=True; break
                        s.append(chr(ch))
                    if stop: break
                continue
            else: s.append(chr(c))
            i+=1
        out.append("".join(s))
    return out
def banks(k, path="a/0/0/2"):
    cache=f"txt_{k}_{path.replace('/','')}.pkl"
    if os.path.exists(cache): return pickle.load(open(cache,"rb"))
    r=ndspy.rom.NintendoDSRom.fromFile(D+ROMS[k])
    n=ndspy.narc.NARC(r.getFileByName(path))
    res=[]
    for f in n.files:
        try: res.append(dec_file(f))
        except Exception as e: res.append(None)
    pickle.dump(res,open(cache,"wb")); return res
if __name__=="__main__":
    import sys
    for k in ("IRAO","IRAS","IRBS"):
        b=banks(k); print(k,len(b))
    e=banks("IRAO"); s=banks("IRAS")
    for i,bk in enumerate(e):
        if bk and len(bk)>2 and bk[1] in ("Pound","POUND","Bulbasaur","BULBASAUR","Stench","Hardy","Master Ball"):
            print(i, bk[1:4], "|", s[i][1:4])
