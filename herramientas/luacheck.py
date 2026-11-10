import sys, lupa.lua54 as L
lua=L.LuaRuntime()
for p in sys.argv[1:]:
    src=open(p,encoding='utf-8').read()
    print(p.split('/')[-1], lua.eval('function(s) local f,e=load(s,"x") return f~=nil, e end')(src))
