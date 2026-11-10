"""Contadores 'X of Y' y palabras sueltas de Platino. Va despues de pl_intro.py."""
import re
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
L=open(LUA,encoding="utf-8").read().split("\n"); n=0
W={"Yes":"Sí","Blank":"Vacío","Empty":"Vacío",", Empty":", Vacío","Party Pokémon, ":"Pokémon del equipo, ","Seal page ":"Página de sellos ","Previous":"Anterior","Next":"Siguiente"}
for i,l in enumerate(L):
    if l.lstrip().startswith("--"): continue
    code,sep,com=l.partition(" --")
    def rep(m):
        global n
        t=m.group(1)
        if re.fullmatch(r" of ?\d*",t): n+=1; return '"%s"'%t.replace(" of"," de",1)
        if t in W: n+=1; return '"%s"'%W[t]
        return m.group(0)
    L[i]=re.sub(r'"([^"\n]*)"',rep,code)+sep+com
open(LUA,"w",encoding="utf-8",newline="").write("\n".join(L)); print("cambios",n)
