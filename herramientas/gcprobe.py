import sys, os, re, lupa.lua54 as L
code=sys.argv[1]
os.chdir(r"C:/Users/caspi/Documents/ds access/Lua")
src=open(r"C:/Users/caspi/rom_analysis/smoke.py",encoding="utf-8").read()
m=re.search(r"lua\.execute\(r'''(.*?)''', code, frames\)",src,re.S)
pre=m.group(1).replace("if n >= FRAMES then error(\"__SMOKE_DONE__\", 0) end","""
 if n==2 or n==200 or n==FRAMES then
  local kb=collectgarbage("count"); local t=os.clock(); collectgarbage("collect"); local d=os.clock()-t
  print(string.format("frame %d: heap antes %.0f KB, despues %.0f KB, GC completo %.0f ms", n, kb, collectgarbage("count"), d*1000))
 end
 if n>=FRAMES then error("__SMOKE_DONE__",0) end""")
lua=L.LuaRuntime(); lua.execute(pre,code,400)
try: lua.execute(open("main.lua",encoding="utf-8").read())
except L.LuaError as e: print("fin", str(e)[:100])
