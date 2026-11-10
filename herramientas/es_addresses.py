"""Aplica a games/bw_es.lua las direcciones de las ROMs espanolas (medidas con port.py/vt.py/forced.py).

Marca de ROM espanola en todo el fichero: `DELTA < -0x20` (en ingles DELTA solo vale 0 o -0x20).
"""
import sys
LUA = sys.argv[1] if len(sys.argv) > 1 else r"C:/Users/caspi/Documents/ds access/Lua/games/bw_es.lua"
E70 = "(DELTA < -0x20 and -0x0C or 0)"
R = [
    # ── deteccion: el cargador pasa "white"/"black"; aqui se mira si la ROM es espanola ──
    ('local DELTA    = (GAME == "black") and -0x20 or 0   -- data / ARM9 globals / most overlays\n'
     'local D_OV204  = (GAME == "black") and -0x40 or 0   -- ov89/203/204 (intro cutscene overlay)\n'
     'local D_OV88VT = (GAME == "black") and -0x54 or 0   -- ov88 title/gender vtable block (non-uniform; measured)',
     '-- ES (2026-11-08): ROMs espanolas IRAS (Blanco) / IRBS (Negro). Deltas MEDIDOS offline comparando el ARM9 y\n'
     '-- los overlays descomprimidos de las cuatro ROMs; el mismo metodo reproduce todos los valores Black de aqui.\n'
     '--   * Las dos ROMs espanolas comparten base: ARM9 globals, heap y casi todos los overlays = White -0x60,\n'
     '--     asi que DELTA = -0x60 en ambas y `DELTA < -0x20` es la marca "ROM espanola" en todo el fichero.\n'
     '--   * Solo difieren en lo que ya difiere entre Black y White: ov88 (titulo) y ov203/204 (intro).\n'
     '--   * Excepciones medidas, marcadas "ES:" donde se usan: ov070 parte alta -0x6C, ov010 parte alta -0x70,\n'
     '--     ov111 -0x80, ov131/170/194/215 -0x40, ov021 W-0x5C (Blanco) / W-0x54 (Negro).\n'
     'local ROM_ES = (function()\n'
     '\tlocal ok, code = pcall(function()\n'
     '\t\tlocal c = {}\n'
     '\t\tfor i = 0, 3 do c[i + 1] = string.char(memory.read_u8(0x0C + i, "ROM")) end\n'
     '\t\treturn table.concat(c)\n'
     '\tend)\n'
     '\treturn ok and (code == "IRAS" or code == "IRBS")\n'
     'end)()\n'
     'local DELTA    = ROM_ES and -0x60 or ((GAME == "black") and -0x20 or 0)   -- data / ARM9 globals / most overlays\n'
     'local D_OV204  = ROM_ES and ((GAME == "black") and -0x80 or -0x60) or ((GAME == "black") and -0x40 or 0)   -- ov89/203/204\n'
     'local D_OV88VT = ROM_ES and ((GAME == "black") and -0x94 or -0x60) or ((GAME == "black") and -0x54 or 0)   -- ov88 vtables'),
    ('local reg = { SHOP_CB = 0x021588FD + DELTA, REPORT_CB = 0x02161711 + DELTA }',
     'local reg = { SHOP_CB = 0x021588FD + DELTA, REPORT_CB = 0x02161711 + DELTA + (DELTA < -0x20 and -0x10 or 0) }   -- ES: ov010 aqui -0x70'),
    ('name_child_vtable = 0x021F55A0 + DELTA,', 'name_child_vtable = 0x021F55A0 + DELTA + (DELTA < -0x20 and 0x20 or 0),   -- ES: ov194 -0x40'),
    ('boxapp_vtable     = 0x021EF7AC + DELTA,', 'boxapp_vtable     = 0x021EF7AC + DELTA + (DELTA < -0x20 and 0x20 or 0),   -- ES: ov170 -0x40'),
    ('egghatch_vtable   = 0x021F7138 + DELTA,', 'egghatch_vtable   = 0x021F7138 + DELTA + (DELTA < -0x20 and 0x20 or 0),   -- ES: ov215 -0x40'),
    ('local BOX_VT = 0x021EF7AC + DELTA', 'local BOX_VT = 0x021EF7AC + DELTA + (DELTA < -0x20 and 0x20 or 0)   -- ES: ov170 -0x40'),
    ('\t\tbase = base + DELTA\n\t\tlocal rows = {}', '\t\tbase = base + DELTA + (DELTA < -0x20 and 0x20 or 0)   -- ES: ov170 -0x40\n\t\tlocal rows = {}'),
    ('local CREDITS_VT = (GAME == "black") and 0x021BAB24 or 0x021BAB50',
     'local CREDITS_VT = (GAME == "black") and (0x021BAB24 + (DELTA < -0x20 and -0x40 or 0)) or (0x021BAB50 + (DELTA < -0x20 and -0x60 or 0))   -- ES: medido'),
    ('local HOF_VT     = (GAME == "black") and 0x021B800C or 0x021B802C',
     'local HOF_VT     = (GAME == "black") and (0x021B800C + (DELTA < -0x20 and -0x40 or 0)) or (0x021B802C + (DELTA < -0x20 and -0x60 or 0))   -- ES: medido'),
    ('local SAVE_VT = (GAME == "black") and 0x021B9E54 or 0x021B9E74',
     'local SAVE_VT = (GAME == "black") and (0x021B9E54 + (DELTA < -0x20 and -0x40 or 0)) or (0x021B9E74 + (DELTA < -0x20 and -0x60 or 0))   -- ES: medido'),
    ('local m = u8(((GAME == "black") and 0x021D35A8 or 0x021D35C0) + tid)',
     'local m = u8(((GAME == "black") and (0x021D35A8 + (DELTA < -0x20 and -0x3C or 0)) or (0x021D35C0 + (DELTA < -0x20 and -0x5C or 0))) + tid)   -- ES: ov021 medido'),
    ('record = 0x02171554 + DELTA + index * 10', 'record = 0x02171554 + DELTA + (DELTA < -0x20 and -0x10 or 0) + index * 10   -- ES: ov010 -0x70'),
    ('record = (DELTA == 0 and 0x021DB84C or 0x021DB834) + position * 8',
     'record = ((GAME == "white") and (0x021DB84C + (DELTA < -0x20 and -0x5C or 0)) or (0x021DB834 + (DELTA < -0x20 and -0x3C or 0))) + position * 8   -- ES: ov021 medido; por GAME, no por DELTA'),
    ('local OUTER_VT  = 0x02172634 + DELTA ', 'local OUTER_VT  = 0x02172634 + DELTA + (DELTA < -0x20 and -0x10 or 0)   -- ES: -0x70\n\t\t--'),
    ('local MAIN_DESC = 0x0217261C + DELTA ', 'local MAIN_DESC = 0x0217261C + DELTA + (DELTA < -0x20 and -0x10 or 0)   -- ES: -0x70\n\t\t--'),
    ('local BADGE_DESC = 0x021C894C + DELTA ', 'local BADGE_DESC = 0x021C894C + DELTA + (DELTA < -0x20 and -0x20 or 0)   -- ES: ov111 -0x80\n\t\t--'),
    ('local PSTAT_VT = 0x021DC820 + DELTA ', 'local PSTAT_VT = 0x021DC820 + DELTA + (DELTA < -0x20 and 0x20 or 0)   -- ES: ov131 -0x40\n\t--'),
    ('local BAG_VT    = 0x021BB98C + DELTA ', f'local BAG_VT    = 0x021BB98C + DELTA + {E70}   -- ES: ov070 -0x6C desde 0x021B7889\n\t--'),
    ('QTY_INPUT, QTY = 0x021B7889 + DELTA, 0x7F4', f'QTY_INPUT, QTY = 0x021B7889 + DELTA + {E70}, 0x7F4'),
    ('local SELL_QTY = 0x021B7A9D + DELTA\n', f'local SELL_QTY = 0x021B7A9D + DELTA + {E70}\n'),
    ('[0x021B7BA1 + DELTA] = true }', f'[0x021B7BA1 + DELTA + {E70}] = true }}'),
    ('\t\tMSG_SCREEN[a + DELTA] = true\n', '\t\tMSG_SCREEN[a + DELTA + ((DELTA < -0x20 and a >= 0x021B7889) and -0x0C or 0)] = true   -- ES: ov070 parte alta -0x6C\n'),
    # ── menu de opciones: celdas en el heap de la app; en ES se buscan si la direccion fija falla ──
    ('local function opt_cell(i) return u8(OPT_CELL0 + i * OPT_STRIDE) end\n',
     'local function opt_cell(i) return u8((reg.opt_cell0 or OPT_CELL0) + i * OPT_STRIDE) end\n'),
    ('\tlocal c = u8(OPT_BTN_CUR)\n', '\tlocal c = u8(OPT_BTN_CUR + ((reg.opt_cell0 or OPT_CELL0) - OPT_CELL0))   -- ES: se mueve con las celdas\n'),
    # ── nombres con tilde o ene: se pliegan a ASCII como la e acentuada ──
    ('\t\tif c == 0xE9 then out[#out+1] = "e"\n\t\telseif c >= 0x20 and c < 0x7F then out[#out+1] = string.char(c)\n\t\telse return nil end',
     '\t\tif c == 0xE9 then out[#out+1] = "e"\n\t\telseif c >= 0x20 and c < 0x7F then out[#out+1] = string.char(c)\n'
     '\t\t-- ES: nombres con tilde o eñe daban nil; se pliegan a ASCII igual que la é de arriba.\n'
     '\t\telseif c >= 0xC0 and c <= 0xFF then\n'
     '\t\t\tout[#out+1] = ("AAAAAAACEEEEIIIIDNOOOOOxOUUUUYTsaaaaaaaceeeeiiiidnooooo/ouuuuyty"):sub(c - 0xBF, c - 0xBF)\n'
     '\t\telse return nil end'),
]

OPT_OLD_HEAD = "local function options_active()\n\tif u8(A.player_control) ~= 1 then return false end\n"
OPT_NEW = '''-- `get(i)` reads cell i; the same test serves the live read and the ES scan below.
function reg.opt_valid(get)
	local n3 = 0
	for _, r in ipairs(OPT_ROWS) do
		local chosen = 0
		for i = r[1], r[1] + r[2] - 1 do
			local b = get(i)
			if b == nil or b > 3 then return false end
			if b == 0 or b == 3 then chosen = chosen + 1 end
			if b == 3 then n3 = n3 + 1 end
		end
		if chosen ~= 1 then return false end   -- each setting row must show exactly one chosen value
	end
	return n3 <= 1                             -- 0 on the Confirm/Quit row, 1 on a setting row
end
-- ES: las celdas viven en el heap de la app, que no se puede medir sin ejecutar el juego; si la direccion
-- fija no pasa la prueba, en ROM espanola se BUSCA el array alrededor de ella (campo desmontado, como mucho
-- una vez cada 45 frames). La direccion encontrada queda en reg.opt_cell0 y se escribe en la consola.
local function options_active()
	if u8(A.player_control) ~= 1 then return false end
	if reg.opt_valid(opt_cell) then return true end
	if DELTA >= -0x20 then return false end
	reg.opt_wait = (reg.opt_wait or 0) - 1
	if reg.opt_wait > 0 then return false end
	reg.opt_wait = 45
	local gs = u32(GAMESYS_PTR)
	if not inram(gs) or u32(gs + 0x20) ~= 0 then return false end
	local lo, span = OPT_CELL0 - 0x8000, 0x10000
	local arr = mainmemory.read_bytes_as_array(lo - MM, span + OPT_NCELLS * OPT_STRIDE)
	local b0 = (arr[0] ~= nil) and 0 or 1
	for off = 0, span - 1, 2 do
		if arr[b0 + off] and arr[b0 + off] <= 3 and
		   reg.opt_valid(function(i) return arr[b0 + off + i * OPT_STRIDE] end) then
			reg.opt_cell0 = lo + off
			console.writeline(string.format("[ES] opciones: celdas en 0x%08X (fija 0x%08X, diferencia %d)",
				lo + off, OPT_CELL0, lo + off - OPT_CELL0))
			return true
		end
	end
	return false
end
'''

src = open(LUA, encoding="utf-8").read()
bad = 0
for a, b in R:
    n = src.count(a)
    if n != 1:
        print("NO", n, a[:90].replace("\n", "\\n")); bad += 1; continue
    src = src.replace(a, b)
# options_active: reemplaza la funcion entera (hasta su "end" de nivel superior)
i = src.find(OPT_OLD_HEAD)
if i < 0:
    print("NO options_active"); bad += 1
else:
    j = src.index("\nend\n", i) + len("\nend\n")
    src = src[:i] + OPT_NEW + src[j:]
open(LUA, "w", encoding="utf-8", newline="").write(src)
print("hecho, fallos:", bad)
