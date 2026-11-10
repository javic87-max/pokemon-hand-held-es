from vt import *
from run_all import pairs
import sys
src,dst=sys.argv[1],sys.argv[2]
for name,X in pairs:
    r=per_module(src,dst,X)
    vts=[x for x in r if x[1]=="VT"]
    show=vts if vts else r
    ds=sorted(set(x[2] for x in show))
    print(f"{name:16s} {X:08X}: "+("UNIFORM %+#x" % ds[0] if len(ds)==1 else "")+"  | "+"; ".join(f"ov{x[0]}:{x[1]}{x[2]:+#x}" for x in show), flush=True)
