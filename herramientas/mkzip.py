import zipfile, re
DOC=r"C:/Users/caspi/Documents/"; base=r"C:/Users/caspi/Documents/ds access/Lua/"
old=DOC+"pokemon blanco y negro accesibles.zip"; out=DOC+"pokemon blanco y negro accesibles v2.zip"; R="pokemon blanco y negro accesibles/"
with zipfile.ZipFile(old) as z: txt=z.read(R+"LEEME.txt").decode("utf-8-sig").replace("\r\n","\n")
a="Versión de prueba\n"; assert txt.count(a)==1
txt=txt.replace(a,"Versión de prueba 2\n\nNovedades de la versión 2:\n- Las descripciones de habilidades que seguían en inglés ya salen en español.\n- El tiempo de juego se dice en español (horas y minutos).\n- Corregidos algunos nombres de lugares y notas de los datos del Pokémon que seguían en inglés.\n")
m=open(base+"main.lua",encoding="utf-8").read()
m=re.sub(r'\tCPUS = \{[^\n]*\n','',m); m=re.sub(r'\n\tif n:find\("platino",\s+1, true\) then claim\("CPUS"\) end','',m)
assert "CPUS" not in m and "platino" not in m
open("dist/main_v2.lua","w",encoding="utf-8",newline="").write(m)
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    z.writestr(R+"LEEME.txt",txt.replace("\n","\r\n").encode("utf-8-sig"))
    z.writestr(R+"Lua/main.lua",m.encode("utf-8"))
    z.write(base+"games/bw_es.lua",R+"Lua/games/bw_es.lua")
with zipfile.ZipFile(out) as z:
    print(z.testzip()); [print(i.filename,i.file_size) for i in z.infolist()]
    t=z.read(R+"LEEME.txt").decode("utf-8-sig"); print(t[:300]); print(t[t.find("Créditos"):])
    print(z.read(R+"Lua/games/bw_es.lua")==open(base+"games/bw_es.lua","rb").read())
