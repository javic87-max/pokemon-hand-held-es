"""Arranca main.lua fuera de BizHawk con la API simulada (memoria a cero) y cuenta fotogramas.

Detecta errores de ejecucion al cargar y en los primeros fotogramas. Uso: smoke.py IRAS|IRBS|IRAO [frames]
"""
import sys, os, lupa.lua54 as L

code = sys.argv[1] if len(sys.argv) > 1 else "IRAS"
frames = int(sys.argv[2]) if len(sys.argv) > 2 else 300
os.chdir(r"C:/Users/caspi/Documents/ds access/Lua")
lua = L.LuaRuntime()
lua.execute(r'''
local CODE, FRAMES = ...
local said = {}
local function any() return setmetatable({}, { __index = function() return function() return 0 end end }) end
memory = { read_u8 = function(a, dom) if dom == "ROM" and a >= 0x0C and a <= 0x0F then return CODE:byte(a - 0x0B) end return 0 end,
           read_u16_le = function() return 0 end, read_u32_le = function() return 0 end }
mainmemory = { read_u8 = function() return 0 end, read_u16_le = function() return 0 end, read_u32_le = function() return 0 end,
               read_s16_le = function() return 0 end, write_u8 = function() end, write_u16_le = function() end,
               write_u32_le = function() end,
               read_bytes_as_array = function(a, n) local t = {} for i = 1, n do t[i] = 0 end return t end,
               readbyterange = function(a, n) local t = {} for i = 0, n - 1 do t[i] = 0 end return t end }
gameinfo = { getromname = function() return "test" end, getromhash = function() return "" end }
console = { log = function(...) print("[console]", ...) end, writeline = function(...) print("[console]", ...) end, clear = function() end }
input = { get = function() return {} end, getmouse = function() return {} end }
joypad = { get = function() return {} end, set = function() end, setfrommnemonicstr = function() end, getimmediate = function() return {} end }
local n = 0
emu = { frameadvance = function() n = n + 1; if n >= FRAMES then error("__SMOKE_DONE__", 0) end end,
        framecount = function() return n end, getsystemid = function() return "NDS" end, yield = function() end }
client = any(); gui = any(); event = any(); comm = any(); savestate = any(); movie = any(); bizstring = any(); userdata = any()
forms = any(); tastudio = any(); nds = any()
bit = { band = function(a, b) return a & b end, bor = function(a, b) return a | b end, rshift = function(a, b) return a >> b end, lshift = function(a, b) return a << b end }
SMOKE_SAID = said
''', code, frames)
# speech: core/speech.lua probably uses comm/luanet; patch by preloading a fake if needed
src = open("main.lua", encoding="utf-8").read()
try:
    lua.execute(src)
    print("main.lua returned without running its loop")
except L.LuaError as e:
    msg = str(e)
    print("RESULT:", "OK (" + str(frames) + " frames)" if "__SMOKE_DONE__" in msg else "ERROR: " + msg[:2000])
