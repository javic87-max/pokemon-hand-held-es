"""Textos de Platino (msgdata/pl_msg.narc): descifrado Gen IV con el mapa de caracteres de platinum.lua."""
import re, struct, pickle, os, ndspy.rom, ndspy.narc
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum.lua"
ROM={'CPUE':r"C:/Users/caspi/Documents/ds access/3541 - Pokemon - Platinum Version (USA).nds",'CPUS':r"D:/juegos/juegos pokemon/roms/ds/Pokemon Platino.nds"}
def charmap():
    src=open(LUA,encoding="utf-8").read(); cm={}
    for m in re.finditer(r'\{\s*(0x[0-9A-Fa-f]{4}),\s*((?:"[^"\n]*"\s*(?:\.\.\s*)?)+)\}',src):
        b=int(m.group(1),16)
        for i,ch in enumerate("".join(re.findall(r'"([^"\n]*)"',m.group(2)))): cm[b+i]=ch
    return cm
CM=charmap()
def chars(codes):
    s=[];i=0;n=len(codes)
    while i<n:
        c=codes[i]
        if c==0xFFFF: break
        if c==0xFFFE and i+2<n:
            cnt=codes[i+2]; s.append("{%04X:%s}"%(codes[i+1],",".join(map(str,codes[i+3:i+3+cnt])))); i+=3+cnt; continue
        if c in (0xE000,0x25BC,0x25BD): s.append("\n")
        elif c==0xF100:
            acc=bits=0;i+=1
            while i<n:
                acc|=codes[i]<<bits;bits+=16;i+=1;stop=False
                while bits>=9:
                    ch=acc&0x1FF;acc>>=9;bits-=9
                    if ch==0x1FF: stop=True;break
                    s.append(CM.get(ch,"·"))
                if stop:break
            continue
        else: s.append(CM.get(c," " if c==0x1DE else "·"))
        i+=1
    return "".join(s)
def dec(b):
    n,seed=struct.unpack_from("<HH",b,0); key=(seed*0x2FD)&0xFFFF; out=[]
    for i in range(n):
        k2=(key*(i+1))&0xFFFF; kk=k2|(k2<<16)
        off,sz=struct.unpack_from("<II",b,4+i*8); off^=kk; sz^=kk
        k=(0x91BD3*(i+1))&0xFFFF; cs=[]
        for j in range(sz):
            cs.append(struct.unpack_from("<H",b,off+j*2)[0]^k); k=(k+0x493D)&0xFFFF
        out.append(chars(cs))
    return out
def banks(k):
    p=f"pltxt_{k}.pkl"
    if os.path.exists(p): return pickle.load(open(p,"rb"))
    r=ndspy.rom.NintendoDSRom.fromFile(ROM[k]); na=ndspy.narc.NARC(r.getFileByName('msgdata/pl_msg.narc'))
    res=[dec(f) for f in na.files]; pickle.dump(res,open(p,"wb")); return res
def norm(s):
    s=re.sub(r"\{[0-9A-F]{4}:[0-9,]*\}","",s).replace("\n"," ")
    return re.sub(r"\s+"," ",s).strip()
