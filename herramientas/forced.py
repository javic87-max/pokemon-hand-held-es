from lit import *
import struct
def lit_in(src,dst,m,X,slack=0):
    sb,sd=M(src)[m]; db,dd=M(dst)[m]; res=collections.Counter()
    for o in range(0,len(sd)-3,4):
        w=struct.unpack_from("<I",sd,o)[0]
        if X-slack<=w<=X:
            v=port_in(src,dst,m,sb+o,L=16,span=96)
            if not v: continue
            d,n=v.most_common(1)[0]
            q=o+d-(db-sb)
            if 0<=q<=len(dd)-4: res[X+struct.unpack_from("<I",dd,q)[0]-w-X]+=1
    return res
L=[("gender_live",0x021C03C0,204),("gender_confirm",0x021C0420,204),("OV21_TBL",0x021D35C0,21),
("TM_LIVE",0x021B9A09,72),("PSEL_SPECIES",0x021BC730,223),("LIST_MENU_CB",0x021B017D,21),("YESNO_CB",0x021B00A5,21),
("TGT_ROW1",0x021EFD14,93),("TGT_ROW2",0x021EFD1A,93),("MOVELEARN",0x021F3B8C,93),("SHIFT_HANDLER",0x021D10D9,93),
("BROWSE",0x021B7271,70),("ACTION_INPUT",0x021B6F19,70),("QTY_INPUT",0x021B7889,70),("SELL_QTY",0x021B7A9D,70),
("YN1",0x021B7721,70),("YN2",0x021B7525,70),("YN3",0x021B7BA1,70),("B_6A35",0x021B6A35,70),("B_75A5",0x021B75A5,70),
("B_763D",0x021B763D,70),("B_76A9",0x021B76A9,70),("B_7705",0x021B7705,70),("B_7805",0x021B7805,70),("B_7CA9",0x021B7CA9,70),("B_8F2D",0x021B8F2D,70),
("BOX_38",0x021EF938,170),("BOX_D4",0x021EF9D4,170),("BOX_70",0x021EF970,170),("BOX_0C",0x021EF90C,170),("BOX_30",0x021EFA30,170),("BOX_28",0x021EF928,170),
("REPORT_CB",0x02161711,10),("SHOP_CB",0x021588FD,10),("MAIN_DESC",0x0217261C,10),("DESC_DRAWN",0x02172BC0,10),("PR_3470",0x02172744,10),
("H_MAIN",0x021D6E5C,121),("A_INTRO",0x021DCEE4,121),("MG_VT",0x021DF558,121),("OV93_SIG",0x021B6120,93),("BTL_SYS",0x0220AF40,94),("BPLIST_FN",0x0220F499,198),("BP_4FC",0x0220F4FC,198)]
for dst in sys.argv[1:]:
  print("==",dst)
  for name,X,m in L:
    if m not in M('IRAO') or not (M('IRAO')[m][0]<=X<M('IRAO')[m][0]+len(M('IRAO')[m][1])): 
        cv="(outside module)"
    else:
        v=port_in('IRAO',dst,m,X&~1,L=16,span=48); cv=str(v.most_common(2))
    lv=lit_in('IRAO',dst,m,X)
    print(f"{name:14s} {X:08X} ov{m}: code {cv}  lit {lv.most_common(2)}", flush=True)
