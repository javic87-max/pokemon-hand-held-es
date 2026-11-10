import port, struct, collections, ndspy.rom
EN=r"C:/Users/caspi/Documents/ds access/3541 - Pokemon - Platinum Version (USA).nds"
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from port import M, D, ROMS
for k in ('CPUE','CPUS'):
    r=ndspy.rom.NintendoDSRom.fromFile(D+ROMS[k])
    print(k, 'arm9',hex(r.arm9RamAddress),len(r.arm9),'ovl',len(r.loadArm9Overlays()))
    print('  msg',[p for p in ('msgdata/pl_msg.narc','msgdata/msg.narc') if r.filenames.idOf(p) is not None])
E,S=M('CPUE'),M('CPUS')
print('arm9 dec',len(E['arm9'][1]),len(S['arm9'][1]))
c=collections.Counter(); odd=[]
for i in sorted(k for k in E if k!='arm9'):
    d=S[i][0]-E[i][0]; c[d]+=1
    if len(E[i][1])!=len(S[i][1]): odd.append((i,len(S[i][1])-len(E[i][1])))
print('delta base',[(hex(k),v) for k,v in c.most_common()])
print('tam distinto',len(odd),'de',len(E)-1,odd[:30])
