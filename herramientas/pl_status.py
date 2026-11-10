"""Estados, formas, concursos, medallas y marcas de Platino. Va despues de pl_banks.py."""
import re
from pl_text import banks, norm
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
E=banks('CPUE');S=banks('CPUS')
def es(w):
    for b,bk in enumerate(E):
        for j,x in enumerate(bk):
            if norm(x)==w and norm(S[b][j])!=w: return norm(S[b][j])
BD=["Coal Badge","Forest Badge","Cobble Badge","Fen Badge","Relic Badge","Mine Badge","Icicle Badge","Beacon Badge"]
fallback=dict(zip(BD,["Medalla Lignito","Medalla Bosque","Medalla Adoquín","Medalla Ciénaga","Medalla Reliquia","Medalla Mina","Medalla Carámbano","Medalla Faro"]))
got={b:es(b) for b in BD}; print(got)
bn=", ".join('"%s"'%(got[b] or fallback[b]) for b in BD).replace(", ",",")
s=open(LUA,encoding="utf-8").read()
R=[('{[0]="Pokérus", "paralysed", "frozen", "asleep", "poisoned", "burned", "fainted"}','{[0]="Pokérus", "paralizado", "congelado", "dormido", "envenenado", "quemado", "debilitado"}'),
('{[0]="Cool", "Beauty", "Cute", "Smart", "Tough"}','{[0]="Carisma", "Belleza", "Dulzura", "Ingenio", "Dureza"}'),
('{[0]="None", "Four legs", "Two legs without a tail", "Two legs with a tail",','{[0]="Ninguna", "Cuatro patas", "Dos patas sin cola", "Dos patas con cola",'),
('"Serpentine", "Multiple wings", "Two wings", "Insect body", "Head and base", "Head and arms",','"Serpentina", "Varias alas", "Dos alas", "Cuerpo de insecto", "Cabeza y base", "Cabeza y brazos",'),
('"Head and legs", "Tentacles", "Fins", "Head only", "Multiple bodies"}','"Cabeza y patas", "Tentáculos", "Aletas", "Solo cabeza", "Varios cuerpos"}'),
('{"Coal Badge","Forest Badge","Cobble Badge","Fen Badge","Relic Badge","Mine Badge","Icicle Badge","Beacon Badge"}','{'+bn+'}'),
('local marks={"Circle","Triangle","Square","Heart","Star","Diamond"}','local marks={"Círculo","Triángulo","Cuadrado","Corazón","Estrella","Rombo"}'),
('local labels={"All","Held item",table.unpack(marks)}','local labels={"Todos","Objeto equipado",table.unpack(marks)}')]
for a,b in R:
    print(s.count(a)); s=s.replace(a,b)
open(LUA,"w",encoding="utf-8",newline="").write(s)
