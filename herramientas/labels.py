"""Etiquetas de menu traducidas a mano (con el texto oficial de la ROM espanola como referencia)."""
LUA = r"C:/Users/caspi/Documents/ds access/Lua/main_es.lua"
import os; LUA = os.environ.get("LUA_FILE", LUA)

R = [
    # Si / No del guardado
    ('(yn == 0 and "Yes" or "No") .. ", " .. (yn + 1) .. " of 2"',
     '(yn == 0 and "Sí" or "No") .. ", " .. (yn + 1) .. " de 2"'),
    # Regalo Misterioso (bank 80)
    ('main  = { "RECEIVE GIFT", "CHECK THE CARD ALBUM", "INFO", "QUIT" }',
     'main  = { "Recibir regalo", "Ver álbum de tarjetas", "Información", "Salir" }'),
    ('meth  = { "GET VIA WIRELESS", "GET VIA NINTENDO WFC", "GET VIA INFRARED", "BACK" }',
     'meth  = { "Recibir por comunicación inalámbrica", "Recibir por CWF de Nintendo", "Recibir por infrarrojos", "Atrás" }'),
    ('info  = { "ABOUT MYSTERY GIFT", "ABOUT THE CARD ALBUM", "WHEN THE ALBUM IS FULL", "BACK" }',
     'info  = { "Sobre los regalos misteriosos", "Sobre el álbum de tarjetas", "Cuando el álbum está lleno", "Atrás" }'),
    ('back  = "BACK",   -- bank 80[149]', 'back  = "Salir",   -- bank 80[149]'),
    # Pokedex (banks 276/277/234)
    ("MODE = { [0] = 'UNOVA POKÉDEX', [1] = 'NATIONAL POKÉDEX' }",
     "MODE = { [0] = 'Pokédex de Teselia', [1] = 'Pokédex Nacional' }"),
    ("SEEN = 'SEEN', OBTAINED = 'OBTAINED', RESULTS = 'SEARCH RESULTS'",
     "SEEN = 'Avistados', OBTAINED = 'Atrapados', RESULTS = 'Resultados'"),
    ("UNSEEN = 'not seen'", "UNSEEN = 'no avistado'"),
    ("TAB = { [1] = 'INFO', [2] = 'AREA', [3] = 'CRY', [4] = 'FORMS' }",
     "TAB = { [1] = 'Información', [2] = 'Área', [3] = 'Grito', [4] = 'Forma' }"),
    ("COMPARE = 'COMPARE', FORMSEEN = 'FORMS SEEN', SHINYSEEN = 'SHINY SEEN'",
     "COMPARE = 'Formas comparadas', FORMSEEN = 'Formas avistadas', SHINYSEEN = 'Variocolores avistados'"),
    ("SEASON = { [0] = 'Spring', [1] = 'Summer', [2] = 'Autumn', [3] = 'Winter' }",
     "SEASON = { [0] = 'Primavera', [1] = 'Verano', [2] = 'Otoño', [3] = 'Invierno' }"),
    ("SCOPE = { [0] = 'National Pokédex: Search Mode', [1] = 'Unova Pokédex: Search Mode' }",
     "SCOPE = { [0] = 'Búsqueda en Pokédex Nacional', [1] = 'Búsqueda en Pokédex de Teselia' }"),
    ("CTRL = { 'ORDER', 'NAME', 'TYPE', 'COLOR', 'FORM', 'START', '' }",
     "CTRL = { 'Ordenación', 'Nombre', 'Tipo', 'Color', 'Silueta', 'Buscar', '' }"),
    ("ORDER = { 'Number', 'A to Z', 'Heavy to Light', 'Light to Heavy', 'Tall to Short', 'Short to Tall' }",
     "ORDER = { 'Por número', 'De la A a la Z', 'De pesado a ligero', 'De ligero a pesado', 'De alto a bajo', 'De bajo a alto' }"),
    ("TYPE = { 'Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark' }",
     "TYPE = { 'Normal', 'Lucha', 'Volador', 'Veneno', 'Tierra', 'Roca', 'Bicho', 'Fantasma', 'Acero', 'Fuego', 'Agua', 'Planta', 'Eléctrico', 'Psíquico', 'Hielo', 'Dragón', 'Siniestro' }"),
    ("COLOR = { 'Red', 'Blue', 'Yellow', 'Green', 'Black', 'Brown', 'Purple', 'Gray', 'White', 'Pink' }",
     "COLOR = { 'Rojo', 'Azul', 'Amarillo', 'Verde', 'Negro', 'Marrón', 'Morado', 'Gris', 'Blanco', 'Rosa' }"),
    ("FOUND = 'Pokémon found!', NOTFOUND = 'No Pokémon found...'",
     "FOUND = '¡Se han obtenido resultados!', NOTFOUND = 'No se ha encontrado ningún Pokémon.'"),
    ("PROMPT = { [4] = 'Please enter the search criteria.', [10] = 'Please enter the order.', [13] = 'Please enter the first letter in the name.',",
     "PROMPT = { [4] = 'Introduce los criterios de búsqueda.', [10] = 'Introduce el criterio de ordenación.', [13] = 'Introduce la inicial del nombre.',"),
    ("[16] = 'Please enter the type.', [19] = 'Please enter the color.', [22] = 'Please enter the form.' }",
     "[16] = 'Introduce el tipo de Pokémon.', [19] = 'Introduce el color del Pokémon.', [22] = 'Introduce una silueta.' }"),
    ("local LAB_HT, LAB_WT = 'HT', 'WT'", "local LAB_HT, LAB_WT = 'Altura', 'Peso'"),
    ("local BTN_YES, BTN_NO = 'YES', 'NO'", "local BTN_YES, BTN_NO = 'Sí', 'No'"),
    # Eleccion de inicial
    ('local PSEL_OPTION = { "Yes", "No" }', 'local PSEL_OPTION = { "Sí", "No" }'),
    # Subida de nivel (bank 157)
    ('local LVUP_LBL = { "MAX HP", "ATTACK", "DEFENSE", "SP. ATK", "SP. DEF", "SPEED" }',
     'local LVUP_LBL = { "PS máximos", "Ataque", "Defensa", "Ataque especial", "Defensa especial", "Velocidad" }'),
    # Equipo
    ('[9]="Choose a Pokémon.", [11]="Move to where?", [12]="Give to which Pokémon?",',
     '[9]="Elige un Pokémon.", [11]="¿Mover a qué posición?", [12]="¿Dar a qué Pokémon?",'),
    ('[13]="Use on which Pokémon?", [14]="Teach which Pokémon?",',
     '[13]="¿Con qué Pokémon lo usas?", [14]="¿Enseñar a qué Pokémon?",'),
    ('[16]="Deposit which Pokémon?", [19]="Do what with an item?",',
     '[16]="¿Qué Pokémon quieres dejar?", [19]="¿Qué quieres hacer con un objeto?",'),
    ('[163]="Please select an Egg." }', '[163]="Elige un Huevo." }'),
    # Datos del Pokemon (bank 158)
    ('item = "Item",', 'item = "Objeto",'), ('none = "None",', 'none = "Ninguno",'),
    ('dexno = "Dex No.",', 'dexno = "Número de Pokédex",'), ('name = "Name",', 'name = "Nombre",'),
    ('type = "Type",', 'type = "Tipo",'), ('ot = "OT",', 'ot = "Entrenador original",'),
    ('idno = "ID No.",', 'idno = "Número de ID",'), ('exp = "Exp. Points",', 'exp = "Puntos de experiencia",'),
    ('tonext = "To Next Lv.",', 'tonext = "Hasta el siguiente nivel",'), ('hp = "HP",', 'hp = "PS",'),
    ('atk = "Attack",', 'atk = "Ataque",'), ('def = "Defense",', 'def = "Defensa",'),
    ('spatk = "Sp. Atk",', 'spatk = "Ataque especial",'), ('spdef = "Sp. Def",', 'spdef = "Defensa especial",'),
    ('speed = "Speed",', 'speed = "Velocidad",'), ('ability = "Ability",', 'ability = "Habilidad",'),
    ('power = "POWER",', 'power = "Potencia",'), ('accuracy = "ACCURACY",', 'accuracy = "Precisión",'),
    ('category = "CATEGORY",', 'category = "Categoría",'),
    # Mochila (banks 55 y 3)
    ('local POCKETS   = { [0] = "ITEMS", [1] = "MEDICINE", [2] = "TMs & HMs", [3] = "BERRIES", [4] = "KEY ITEMS" }',
     'local POCKETS   = { [0] = "Objetos", [1] = "Botiquín", [2] = "MT y MO", [3] = "Bayas", [4] = "Objetos clave" }'),
    ('local ACTIONS = { [0] = "USE", [1] = "WALK", [2] = "CHECK", [3] = "TRASH", [4] = "REGISTER",',
     'local ACTIONS = { [0] = "Usar", [1] = "Bajarme", [2] = "Ver", [3] = "Tirar", [4] = "Asignar",'),
    ('[5] = "DESELECT", [6] = "GIVE", [7] = "CONFIRM", [8] = "CANCEL" }',
     '[5] = "Anular", [6] = "Dar", [7] = "Vale", [8] = "Salir" }'),
    ('local YESNO_ROW = { [0] = "YES", [1] = "NO" }', 'local YESNO_ROW = { [0] = "Sí", [1] = "No" }'),
    # Opciones (bank 29)
    ('{ name = "Text Speed",     base = 0, vals = { "Slow", "Mid", "Fast" }, desc = "You can choose from three different text-scrolling speeds." },',
     '{ name = "Velocidad del texto", base = 0, vals = { "Lenta", "Media", "Rápida" }, desc = "Elige entre los tres niveles de velocidad del texto." },'),
    ('{ name = "Battle Scene",   base = 3, vals = { "On", "Off" },           desc = "You can choose whether to view move animations." },',
     '{ name = "Animación de batalla", base = 3, vals = { "Ver", "No ver" }, desc = "Muestra o desactiva las animaciones durante los combates." },'),
    ('{ name = "Battle Style",   base = 5, vals = { "Shift", "Set" },        desc = "You can choose to switch Pokemon when an opponent\'s Pokemon faints." },',
     '{ name = "Tipo de combate", base = 5, vals = { "Cambiar", "Fijo" },   desc = "Configura las reglas que se aplican en los combates." },'),
    ('{ name = "Sound",          base = 7, vals = { "Stereo", "Mono" },      desc = "You can choose the way the game sounds." },',
     '{ name = "Sonido",         base = 7, vals = { "Estéreo", "Mono" },     desc = "Configura el sonido como estéreo o mono." },'),
    ('{ name = "Save Before IR", base = 9, vals = { "Save", "No Save" },     desc = "You can choose to save the game before C-Gear launches infrared." },',
     '{ name = "Guardado antes de infrarrojos", base = 9, vals = { "Sí", "No" }, desc = "Activa o desactiva el guardado previo a la comunicación por infrarrojos." },'),
    ('local BTN = { [0] = "Confirm", [1] = "Quit" }', 'local BTN = { [0] = "Vale", [1] = "Salir" }'),
    ('say(row.name .. ", " .. row.vals[v + 1] .. ", " .. row.desc .. " " .. r .. " of " .. #ROWS)',
     'say(row.name .. ", " .. row.vals[v + 1] .. ", " .. row.desc .. " " .. r .. " de " .. #ROWS)'),
    # Combate
    ('local LABELS = { [0] = "Fight", [1] = "Bag", [2] = "Pokémon", [3] = "Run" }',
     'local LABELS = { [0] = "Luchar", [1] = "Mochila", [2] = "Pokémon", [3] = "Huir" }'),
    ('local line = (LABELS[c] or ("Option " .. c)) .. ", " .. pos .. " of " .. total',
     'local line = (LABELS[c] or ("Opción " .. c)) .. ", " .. pos .. " de " .. total'),
    ('local TYPE_NAMES = {[0]="Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark"}',
     'local TYPE_NAMES = {[0]="Normal","Lucha","Volador","Veneno","Tierra","Roca","Bicho","Fantasma","Acero","Fuego","Agua","Planta","Eléctrico","Psíquico","Hielo","Dragón","Siniestro"}'),
    ('local CATS = { [0] = "HP/PP RESTORE", [1] = "STATUS RESTORE", [2] = "POKÉ BALLS", [3] = "BATTLE ITEMS" }',
     'local CATS = { [0] = "Restaurar PS y PP", [1] = "Curación de estados", [2] = "Poké Balls", [3] = "Objetos de combate" }'),
    ('local L_LASTITEM, L_USE = "LAST USED ITEM", "USE"', 'local L_LASTITEM, L_USE = "Último objeto usado", "Usar"'),
    ('local B233 = { [2] = "FORGET", [3] = "KEEP OLD MOVES!" }',
     'local B233 = { [2] = "Olvidar un movimiento antiguo", [3] = "Conservar movimientos antiguos" }'),
    ('local B16 = { [1] = "RUN", [5] = "USE NEXT POKÉMON", [6] = "SWITCH POKÉMON",',
     'local B16 = { [1] = "Huir", [5] = "Usar otro Pokémon", [6] = "Cambiar Pokémon",'),
    ('[7] = "KEEP BATTLING", [8] = "YES", [9] = "NO" }', '[7] = "Seguir luchando", [8] = "Sí", [9] = "No" }'),
]

src = open(LUA, encoding="utf-8").read()
missing = []
for a, b in R:
    n = src.count(a)
    if n != 1:
        missing.append((n, a[:90])); continue
    src = src.replace(a, b)
open(LUA, "w", encoding="utf-8", newline="").write(src)
print("aplicadas", len(R) - len(missing), "de", len(R))
for n, a in missing: print("  NO", n, a)
