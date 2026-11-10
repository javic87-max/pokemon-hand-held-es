"""Nombres de personajes/roles y frases sueltas de Platino. Va despues de pl_small.py."""
import re
from pl_text import banks, norm
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
CH={"Rowan":"Serbal","Prof. Rowan":"Prof. Serbal","Roark":"Roco","Maylene":"Brega","Wake":"Mananti","Byron":"Acerón","Candice":"Inverna","Volkner":"Lectro","Aaron":"Alecrán","Bertha":"Gaia","Flint":"Fausto","Lucian":"Delos","Cyrus":"Helio","Mars":"Venus","Jupiter":"Ceres","Saturn":"Saturno","Charon":"Plutón","Looker":"Handsome"}
E=banks('CPUE');S=banks('CPUS')
bad=[]
for en,es in CH.items():
    tot=hit=0
    for b,bk in enumerate(E):
        for j,x in enumerate(bk):
            if re.search(r"\b%s\b"%re.escape(en),x):
                tot+=1; hit+=bool(re.search(r"(?<!\w)%s(?!\w)"%re.escape(es),S[b][j],re.I))
    print(en,es,hit,tot)
    if tot and hit/tot<0.5: bad.append(en)
print("DUDOSOS",bad)
for k in bad: CH.pop(k)
RO={"Mom":"Mamá","Breeder":"Criapokémon","Attendant":"Encargado","Team Galactic":"Equipo Galaxia","Cashier":"Cajero","Woman":"Mujer","Receptionist":"Recepcionista","Professor":"Profesor","Old woman":"Anciana","Old man":"Anciano","Nurse":"Enfermera","Mystery man":"Hombre misterioso","Mossy rock":"Roca musgosa","Icy rock":"Roca helada","Man":"Hombre","Little girl":"Niña","Gym guide":"Guía del gimnasio","Expert":"Experto","Deliveryman":"Repartidor","Child":"Niño","Butler":"Mayordomo","Briefcase":"Maletín","Book":"Libro","Beauty":"Modelo","Berry patch":"Parcela de bayas","Door":"Puerta","Snowball":"Bola de nieve","Vent":"Rejilla","Post":"Poste"}
M=dict(RO);M.update(CH)
s=open(LUA,encoding="utf-8").read()
L=s.split("\n");n=0
for i,l in enumerate(L):
    if l.lstrip().startswith("--"): continue
    code,sep,com=l.partition(" --")
    def rp(m):
        global n
        if m.group(1) in M: n+=1; return '="%s"'%M[m.group(1)]
        return m.group(0)
    L[i]=re.sub(r'(?<![=~<>])="([^"\n]*)"',rp,code)+sep+com
s="\n".join(L)
for a,b in [('"Recalculating. "','"Recalculando. "'),('"I can\'t route to " .. (pf.name or "destino") .. " yet"','"Todavía no encuentro ruta hasta " .. (pf.name or "destino")'),('say("I can\'t route to "','say("Todavía no encuentro ruta hasta "'),('"Badge case closed"','"Estuche de medallas cerrado"'),('"Badge case open"','"Estuche de medallas abierto"'),('"Capsule edge, "','"Borde de la cápsula, "'),('"Covered by another seal. Move that seal first."','"Tapado por otro sello. Mueve antes ese sello."')]:
    s=s.replace(a,b)
al=", ".join('["%s"] = "%s"'%(v,k) for k,v in M.items() if k in CH or k=="Mom")
a="\t\t[\"Thorton\"]=215, [\"Volkner\"]=133, [\"Wake\"]=128,\n\t}\n"
assert s.count(a)==1
s=s.replace(a,a+"\tfor es, en in pairs({ %s }) do STORY_OWNER[es] = STORY_OWNER[en] end   -- ES: story_name da el nombre traducido\n"%al)
a2="do TRAINER_KEY.story[es] = TRAINER_KEY.story[en] end"
assert s.count(a2)==1
k=s.index(a2)+len(a2)
s=s[:k]+"\n\tfor es, en in pairs({ %s }) do TRAINER_KEY.story[es] = TRAINER_KEY.story[en] end"%al+s[k:]
open(LUA,"w",encoding="utf-8",newline="").write(s);print("cambios",n)
