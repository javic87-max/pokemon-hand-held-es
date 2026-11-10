import sys
R=[
('(LOGO .. ". Developed by GAME FREAK inc.")','(LOGO .. ". Desarrollado por GAME FREAK inc.")'),
('then return "Empty" .. pos, page * 8 + cell end','then return "Vacío" .. pos, page * 8 + cell end'),
('(zs_caught(zs, sp) and ", caught" or ", seen")','(zs_caught(zs, sp) and ", atrapado" or ", avistado")'),
('if not tid then return "Trainer" end','if not tid then return "Entrenador" end'),
('(pf.name or "target")','(pf.name or "destino")'),
('(pf.slide and ". 1 down" or "")','(pf.slide and ". 1 abajo" or "")'),
('local last = step and (". 1 " .. step)','local last = step and (". 1 " .. reg.dir_es(step))'),
('parts[#parts+1] = (-dz) .. " up" elseif dz > 0 then parts[#parts+1] = dz .. " down" end','parts[#parts+1] = (-dz) .. " arriba" elseif dz > 0 then parts[#parts+1] = dz .. " abajo" end'),
('parts[#parts+1] = (-dx) .. " left" elseif dx > 0 then parts[#parts+1] = dx .. " right" end','parts[#parts+1] = (-dx) .. " izquierda" elseif dx > 0 then parts[#parts+1] = dx .. " derecha" end'),
('far = ", " .. table.concat(parts, " and ") end','far = ", " .. table.concat(parts, " y ") end'),
('or ("move " .. id) end','or ("movimiento " .. id) end'),
('return nil, nil, "party " .. (pi + 1) end','return nil, nil, "equipo " .. (pi + 1) end'),
('MENU_WORD[tid] or ("option " .. (i + 1))','MENU_WORD[tid] or ("opción " .. (i + 1))'),
('if pick then bits[#bits + 1] = "picked up" end','if pick then bits[#bits + 1] = "cogido" end'),
('bits[#bits + 1] = box_name(w, b) or ("Box " .. (b + 1))','bits[#bits + 1] = box_name(w, b) or ("Caja " .. (b + 1))'),
('(kind == "prevbox") and "previous box" or "next box"','(kind == "prevbox") and "caja anterior" or "caja siguiente"'),
('local nm = box_name(w, b) or ("Box " .. (b + 1))','local nm = box_name(w, b) or ("Caja " .. (b + 1))'),
('(nm .. ", " .. n .. " Pokemon")','(nm .. ", " .. n .. " Pokémon")'),
('bits[#bits + 1] = "party " .. (idx + 1)','bits[#bits + 1] = "equipo " .. (idx + 1)'),
('bits[#bits + 1] = "row " .. (math.floor(idx / 6) + 1)','bits[#bits + 1] = "fila " .. (math.floor(idx / 6) + 1)'),
('bits[#bits + 1] = "column " .. ((idx % 6) + 1)','bits[#bits + 1] = "columna " .. ((idx % 6) + 1)'),
('if cur == 7 then return "Cancel" end','if cur == 7 then return "Salir" end'),
('line = line .. ", not entered" end','line = line .. ", no inscrito" end'),
('say(l .. ", picked up")','say(l .. ", cogido")'),
('if cur == 6 then return "Cancel" end','if cur == 6 then return "Salir" end'),
('.. ", " .. pos .. " of 6"','.. ", " .. pos .. " de 6"'),
('BML_TXT[69] .. ", 6 of 6" end','BML_TXT[69] .. ", 6 de 6" end'),
('ITEMS[id] or ("Item " .. id)','ITEMS[id] or ("Objeto " .. id)'),
('(L_USE .. ", 1 of 2") or ((c == 1) and "Cancel, 2 of 2" or nil)','(L_USE .. ", 1 de 2") or ((c == 1) and "Salir, 2 de 2" or nil)'),
]
for p in sys.argv[1:]:
    s=open(p,encoding="utf-8").read(); n0=0; miss=[]
    for a,b in R:
        n=s.count(a)
        if n: s=s.replace(a,b); n0+=n
        else: miss.append(a[:45])
    open(p,"w",encoding="utf-8",newline="").write(s)
    print(p.split("/")[-1], "cambios", n0, "no encontrados:", miss)
