import port, struct, difflib
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from port import M
eb,ed=M('CPUE')[73]; sb,sd=M('CPUS')[73]
print(hex(eb),len(ed),hex(sb),len(sd))
he=struct.unpack(f"<{len(ed)//2}H",ed[:len(ed)&~1]); hs=struct.unpack(f"<{len(sd)//2}H",sd[:len(sd)&~1])
sm=difflib.SequenceMatcher(None,he,hs,autojunk=False)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag!='equal':
        print(tag,hex(eb+i1*2),hex(eb+i2*2),'->',hex(sb+j1*2),hex(sb+j2*2),' EN',' '.join('%04x'%x for x in he[i1:min(i2,i1+14)]),' ES',' '.join('%04x'%x for x in hs[j1:min(j2,j1+14)]))
# la funcion del circulo: buscar 2 movs con 0x80 / 0x64 cerca
def find(h,b):
    for i,x in enumerate(h):
        if x&0xF8FF==0x2080 or x&0xFF00 in (0x2080,) :
            for k in range(i-12,i+12):
                if 0<=k<len(h) and (h[k]&0x00FF)==0x64 and (h[k]&0xF800)==0x2000: print(hex(b+i*2),'%04x'%x,hex(b+k*2),'%04x'%h[k])
print('EN');find(he,eb);print('ES');find(hs,sb)
