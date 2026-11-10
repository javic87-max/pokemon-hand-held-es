import port, struct
port.ROMS['CPUS']="Pokemon Platino.nds"; port.ROMS['CPUE']="3541 - Pokemon - Platinum Version (USA).nds"
from port import M
def H(k):
    b,d=M(k)[73]; return b,struct.unpack(f"<{len(d)//2}H",d[:len(d)&~1])
eb,eh=H('CPUE'); sb,sh=H('CPUS'); et=2779; st=2857
for e,s in [(47,48),(67,68),(22,22),(27,27),(27,28),(26,26)]:
    ei=et+eh[et+e]//2; si=st+sh[st+s]//2
    print(e,s,hex(eb+ei*2),hex(sb+si*2)); print(' EN',' '.join('%04x'%x for x in eh[ei:ei+18])); print(' ES',' '.join('%04x'%x for x in sh[si:si+18]))
# escritura del genero en ambas: buscar offsets de str con constante igual
