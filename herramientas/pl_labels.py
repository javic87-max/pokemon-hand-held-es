"""Etiquetas propias del lector de Platino, a mano. Se ejecuta al final del proceso."""
import re, collections
from pl_text import banks, norm
LUA = r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
s = open(LUA, encoding="utf-8").read()
R = [
    ('"level " .. level }', '"nivel " .. level }'),
    ('return cur .. " of " .. max end', 'return cur .. " de " .. max .. " PS" end'),
    ('.. " percent"', '.. " por ciento"'),
    ('local line = (side == 0 and "Your " or "Enemy ") .. table.concat(parts, ", ")',
     'local line = (side == 0 and "Tu " or "") .. parts[1] .. (side == 0 and "" or " rival") .. (#parts > 1 and (", " .. table.concat(parts, ", ", 2)) or "")'),
    ('local PAGES = { [0] = "upper case", [1] = "lower case", [2] = "others" }', 'local PAGES = { [0] = "Mayúsculas", [1] = "Minúsculas", [2] = "Otros" }'),
    ('[0xE007] = "back", [0xE008] = "OK",', '[0xE007] = "Borrar", [0xE008] = "Vale",'),
    ('announce(name or "blank", landed)', 'announce(name or "vacío", landed)'),
    ('local YESNO = { "Yes", "No" }', 'local YESNO = { "Sí", "No" }'),
    ('local GENDERS = { [0] = "Boy", [1] = "Girl" }', 'local GENDERS = { [0] = "Chico", [1] = "Chica" }'),
    ('.. " hours " .. tonumber(m) .. " minutes"', '.. " horas " .. tonumber(m) .. " minutos"'),
    ('grass="Grass", ground="Ground", cave="Cave floor", floor="Floor",', 'grass="Hierba", ground="Tierra", cave="Suelo de cueva", floor="Suelo",'),
    ('rock="Rocky ground", water="Water", waterfall="Waterfall", puddle="Puddle",', 'rock="Terreno rocoso", water="Agua", waterfall="Cascada", puddle="Charco",'),
    ('shallow="Shallow water", ice="Ice", sand="Sand", snow="Snow", mud="Mud",', 'shallow="Agua poco profunda", ice="Hielo", sand="Arena", snow="Nieve", mud="Barro",'),
    ('bridge="Bridge", ledge="Ledge", stairs="Stairs", door="Door", berries="Berry patch",', 'bridge="Puente", ledge="Saliente", stairs="Escaleras", door="Puerta", berries="Parcela de bayas",'),
    ('"Pokémon Center", "Poké Mart", "Gym", "House", "Room"', '"Centro Pokémon", "Tienda", "Gimnasio", "Casa", "Habitación"'),
    ('if who then return who .. (k == BK.PLAYER_HOUSE and "’s house" or "’s room") end', 'if who then return (k == BK.PLAYER_HOUSE and "Casa de " or "Habitación de ") .. who end'),
    ('say(cur_cat(), true)', 'say(({ Transitions = "Salidas", NPCs = "Personas", Items = "Objetos", HM = "Obstáculos MO", Signs = "Carteles", Objects = "Objetos del entorno", ["Honey trees"] = "Árboles de miel" })[cur_cat()] or cur_cat(), true)'),
    ('[0x54]="Strength", [0x55]="Rock Smash", [0x56]="Cut", surf="Surf", climb="Rock Climb", waterfall="Waterfall",', '[0x54]="Fuerza", [0x55]="Golpe Roca", [0x56]="Corte", surf="Surf", climb="Trepar", waterfall="Cascada",'),
    ('"Person", "Sign", "Item"', '"Persona", "Cartel", "Objeto"'),
    ('PM.spot = { word = "Object", names = { [494] = { [4] = "Machine", [5] = "Machine", [6] = "Machine", [10] = "Button" },', 'PM.spot = { word = "Objeto del entorno", names = { [494] = { [4] = "Máquina", [5] = "Máquina", [6] = "Máquina", [10] = "Botón" },'),
    ('local PFWORD = { [0] = "up", [1] = "down", [2] = "left", [3] = "right" }', 'local PFWORD = { [0] = "arriba", [1] = "abajo", [2] = "izquierda", [3] = "derecha" }'),
    ('local FACEWORD = { [0] = "north", [1] = "south", [2] = "west", [3] = "east" }', 'local FACEWORD = { [0] = "norte", [1] = "sur", [2] = "oeste", [3] = "este" }'),
    ('(de > 0 and "east" or "west")', '(de > 0 and "este" or "oeste")'),
    ('(dn > 0 and "south" or "north")', '(dn > 0 and "sur" or "norte")'),
    ('return d == "" and "here" or d', 'return d == "" and "aquí" or d'),
    ('" for " .. (last-n) .. " tiles"', '" durante " .. (last-n) .. " casillas"'),
    ('"Bicycle slope. Hold " .. table.concat(parts, ", then ") .. " without stopping"', '"Cuesta en bici. Mantén " .. table.concat(parts, ", luego ") .. " sin parar"'),
    ('" up"', '" arriba"'), ('" down"', '" abajo"'), ('" left"', '" izquierda"'), ('" right"', '" derecha"'),
    ('"Arrived at "', '"Has llegado a "'), ('(pf.name or "target")', '(pf.name or "destino")'),
    ('"I can\'t route to " .. (pf.name or "destino") .. " yet"', '"Todavía no encuentro ruta hasta " .. (pf.name or "destino")'),
    ('"Can\'t reach "', '"No se puede llegar a "'), ('" from here"', '" desde aquí"'),
    ('or "continue")', 'or "continúa")'), ('say("Nothing nearby", true)', 'say("No hay nada cerca", true)'),
    ('"Open the nav list first, then press p"', '"Abre primero la lista de navegación y luego pulsa P"'),
    ('"You\'re there"', '"Has llegado"'), ('say("To " ..', 'say("Hacia " ..'),
    ('"This area is too dark to see in."', '"Esta zona está demasiado oscura para ver."'),
    ('"Pathfinding off"', '"Guiado desactivado"'),
    ('cmd = { "FIGHT", "BAG", "POKéMON", "RUN", "CANCEL" }', 'cmd = { "Luchar", "Mochila", "Pokémon", "Huir", "Salir" }'),
    ('stats = { "Max. HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed" }', 'stats = { "PS máximos", "Ataque", "Defensa", "Ataque especial", "Defensa especial", "Velocidad" }'),
    ('"Developed by GAME FREAK inc."', '"Desarrollado por GAME FREAK inc."'), ('"PRESS START"', '"Pulsa Start"'), ('"GAME FREAK presents"', '"GAME FREAK presenta"'),
    ('radar = "Radar", previous = "Previous app", next = "Next app", app = "App",', 'radar = "Radar", previous = "Aplicación anterior", next = "Aplicación siguiente", app = "Aplicación",'),
    ('here = "here", item = WORD_ITEM, none = "No items detected", near = "An item is nearby",', 'here = "aquí", item = WORD_ITEM, none = "No se detectan objetos", near = "Hay un objeto cerca",'),
]
miss = []
for a, b in R:
    if a not in s: miss.append(a[:50])
    s = s.replace(a, b)
for en, es in {"asleep": "dormido", "badly poisoned": "gravemente envenenado", "poisoned": "envenenado", "burned": "quemado", "frozen": "congelado", "paralysed": "paralizado"}.items():
    s = re.sub(r'(return |= )"%s"' % en, r'\1"%s"' % es, s, count=2)
TY = {"NORMAL": "Normal", "FIGHTING": "Lucha", "FLYING": "Volador", "POISON": "Veneno", "GROUND": "Tierra", "ROCK": "Roca", "BUG": "Bicho", "GHOST": "Fantasma", "STEEL": "Acero", "FIRE": "Fuego", "WATER": "Agua", "GRASS": "Planta", "ELECTRIC": "Eléctrico", "PSYCHIC": "Psíquico", "ICE": "Hielo", "DRAGON": "Dragón", "DARK": "Siniestro"}
FL = {"2F": "Planta 2", "3F": "Planta 3", "4F": "Planta 4", "1F": "Planta 1", "B1F": "Sótano 1", "B2F": "Sótano 2"}
L = s.split("\n")
for i, l in enumerate(L):
    if l.lstrip().startswith('types = { [0] = "NORMAL"'):
        for en, es in TY.items(): L[i] = L[i].replace('"%s"' % en, '"%s"' % es)
    if "NAV_FLOOR = {" in l:
        for en, es in FL.items(): L[i] = L[i].replace('="%s"' % en, '="%s"' % es)
# nombres sueltos de personas y clases en las tablas de navegacion: la traduccion dominante del juego
E = banks('CPUE'); T = banks('CPUS'); ix = collections.defaultdict(collections.Counter)
for b, bk in enumerate(E):
    for j, x in enumerate(bk):
        if norm(x) and norm(T[b][j]) and "·" not in T[b][j]: ix[norm(x)][norm(T[b][j])] += 1
a = next(i for i, l in enumerate(L) if "NAV_FLOOR = {" in l); z = min(a + 450, len(L)); n = 0
for i in range(a, z):
    if L[i].lstrip().startswith("--"): continue
    code, sep, com = L[i].partition(" --")
    def rp(m):
        global n
        t = m.group(1)
        if t in ix and not re.fullmatch(r"[a-z_]+", t):
            n += 1
            return '="%s"' % ix[t].most_common(1)[0][0].replace('"', "'")
        return m.group(0)
    L[i] = re.sub(r'\s*=\s*"([^"\n]*)"', rp, code) + sep + com
open(LUA, "w", encoding="utf-8", newline="").write("\n".join(L))
print("no encontrados", miss, "npc", n)
