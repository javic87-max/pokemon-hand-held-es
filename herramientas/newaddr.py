from lit import port_lit
from vt import per_module
import sys
for X,src in [(0x02171554,'IRAO'),(0x021ADBD1,'IRAO'),(0x021B81F0,'IRAO'),(0x021DB84C,'IRAO'),(0x021DB834,'IRBO')]:
    for dst in ('IRAS','IRBS','IRBO'):
        if src=='IRBO' and dst!='IRBS': continue
        r=per_module(src,dst,X); vts=[x for x in r if x[1]=="VT"]
        lv=port_lit(src,dst,X,slack=0).most_common(2)
        print(f"{X:08X} {src}->{dst}: VT {[(x[0],hex(x[2])) for x in vts]} lit {[(hex(a),hex(a-X),n) for a,n in lv]}", flush=True)
