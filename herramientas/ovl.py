import sys, ndspy.rom
D="D:/juegos/juegos pokemon/roms/ds/"
roms={'IRAO':"Pokemon - White Version (USA, Europe) (NDSi Enhanced).nds",'IRBO':"5585 - Pokemon - Black Version (USA, Europe) (NDSi Enhanced) [b].nds",'IRAS':"Pokémon Blanco.nds",'IRBS':"Pokemon Negro.nds"}
ov={}
for k,f in roms.items():
    r=ndspy.rom.NintendoDSRom.fromFile(D+f)
    ov[k]={i:(o.ramAddress,o.ramSize) for i,o in r.loadArm9Overlays().items()} if False else {i:(e.ramAddress,e.ramSize) for i,e in __import__('ndspy.code',fromlist=['x']).loadOverlayTable(r.arm9OverlayTable, lambda a,b:b'').items()}
    print(k, hex(r.arm9RamAddress), len(r.arm9))
ids=sorted(ov['IRAO'])
for i in ids:
    a=ov['IRAO'][i][0]
    row=[f"{i:3d} W {a:08X}"]
    for k in ('IRBO','IRAS','IRBS'):
        b=ov[k].get(i,(0,0))[0]; row.append(f"{k} {b-a:+#06x}")
    print("  ".join(row))
