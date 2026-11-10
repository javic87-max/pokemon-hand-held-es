"""Descripciones de habilidades por posicion (banco 183) y horas de juego, en bw_es.lua y main_es.lua."""
import re
from text import banks
from translate import norm
EN,ES=banks("IRAO"),banks("IRAS")
for p in (r"C:/Users/caspi/Documents/ds access/Lua/games/bw_es.lua",r"C:/Users/caspi/Documents/ds access/Lua/main_es.lua"):
    L=open(p,encoding="utf-8").read().split("\n"); c=0
    for i,l in enumerate(L):
        if "local ABILDESC_ = \"" in l:
            a=l.index('"')+1; b=l.rindex('"')
            it=l[a:b].split("|"); out=[]
            for k,x in enumerate(it):
                t=x.replace('\\"','"')
                if k<len(EN[183]) and norm(EN[183][k])==norm(t) and norm(ES[183][k]):
                    out.append(norm(ES[183][k]).replace("\\","").replace('"','\\"')); c+=1
                else: out.append(x)
            L[i]=l[:a]+"|".join(out)+l[b:]
            print(len(it),"traducidas",c,"inglés restante",[x[:40] for x in out if re.search(r"\b(the|The|moves?|Pokémon's|Boosts|Powers|Raises)\b",x)][:6])
    s="\n".join(L)
    for a,b in [('string.format(". %s, %d hours %d minutes"','string.format(". %s, %d horas %d minutos"'),('string.format("%d hours %d minutes"','string.format("%d horas %d minutos"')]:
        print(s.count(a)); s=s.replace(a,b)
    open(p,"w",encoding="utf-8",newline="").write(s)
