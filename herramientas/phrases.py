"""Frases propias del script: solo se cambian literales exactos en lineas que hablan o concatenan."""
import re, sys
LUA = r"C:/Users/caspi/Documents/ds access/Lua/main_es.lua"
import os; LUA = os.environ.get("LUA_FILE", LUA)
P = {
    " of ": " de ", " of 2": " de 2", " of 4": " de 4", " of 5": " de 5",
    "empty": "vacío", "Pocket ": "Bolsillo ", "Option ": "Opción ", "Button ": "Botón ", "page ": "página ",
    "Can't reach ": "No se puede llegar a ", " from here": " desde aquí", "Recalculating. ": "Recalculando. ",
    "You're there": "Has llegado", "This area is too dark to see in.": "Esta zona está demasiado oscura para ver.",
    "Pathfinding off": "Guiado desactivado", "You cannot fly there": "No puedes volar ahí",
    "Arrived at ": "Has llegado a ", "Nothing nearby": "No hay nada cerca", "No Pokemon there.": "No hay ningún Pokémon ahí.",
    "Nowhere to fly to yet": "Todavía no hay ningún sitio al que volar", "Can't resume the path": "No se puede retomar la ruta",
    "Nothing is selected": "No hay nada seleccionado", "Open the nav list first, then press p": "Abre primero la lista de navegación y luego pulsa P",
    "I can't route to ": "No encuentro ruta hasta ", "As close as I can get to ": "Lo más cerca que puedo llegar de ",
    "Can't read the map here": "No puedo leer el mapa aquí", "Can't read the boulders here": "No puedo leer las rocas aquí",
    "Step off here": "Bájate aquí", "Bottom of the shaft": "Fondo del pozo", "Wall closed": "Pared cerrada",
    "Pushed back": "Empujado hacia atrás", "Do what with ": "¿Qué hacer con ", "Lv. ": "Nivel ", " nature": " de naturaleza",
    "To ": "Hacia ", "Wait": "Espera", "The screen would not close": "La pantalla no se cerró",
    "The cursor would not move": "El cursor no se movió", "It would not accept": "No lo aceptó",
    "There is no ring to put it back on": "No hay ningún hueco donde volver a ponerlo",
}
src = open(LUA, encoding="utf-8").read().split("\n")
lit = re.compile(r'"([^"\n]*)"')
changed = 0
for i, l in enumerate(src):
    if l.lstrip().startswith("--"): continue
    code, sep, com = l.partition(" --")
    if "say(" not in code and ".." not in code: continue
    def rep(m):
        global changed
        if m.group(1) in P:
            changed += 1; return '"%s"' % P[m.group(1)]
        return m.group(0)
    new = lit.sub(rep, code)
    if new != code:
        if "-v" in sys.argv: print(i + 1, new.strip()[:150])
        src[i] = new + sep + com
open(LUA, "w", encoding="utf-8", newline="").write("\n".join(src))
print("cambiados", changed)
