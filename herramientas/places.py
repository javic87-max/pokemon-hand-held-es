"""Lugares: tablas indexadas por banco (mapdesc = banco 185, placenames = banco 89) y listas de nombres."""
import re
from text import banks
from translate import norm, LUA

EN, ES = banks("IRAO"), banks("IRAS")
src = open(LUA, encoding="utf-8").read().split("\n")


def block(start_pat):
    i = next(k for k, l in enumerate(src) if start_pat in l)
    j = next(k for k in range(i, len(src)) if src[k].strip() == "}")
    return i, j


def by_index(start_pat, bank):
    i, j = block(start_pat); n = 0
    for k in range(i + 1, j):
        def rep(m):
            nonlocal n
            idx, en = int(m.group(1)), m.group(2)
            if idx < len(EN[bank]) and norm(EN[bank][idx]) == en and norm(ES[bank][idx]):
                n += 1
                return '[%d]="%s"' % (idx, norm(ES[bank][idx]).replace('"', "'"))
            return m.group(0)
        src[k] = re.sub(r'\[(\d+)\]="([^"]*)"', rep, src[k])
    print(start_pat, n)


by_index("local mapdesc = {", 185)
by_index("local placenames = {", 89)

# nombres de lugar sueltos (bancos 89/185/90), solo en las tablas de lugares y la lista ZA del Pokedex
names = {}
for b in (89, 90, 185):
    for j, s in enumerate(EN[b]):
        if norm(s) and norm(ES[b][j]): names.setdefault(norm(s), norm(ES[b][j]))
i, j = block("local zone_building = {")
za = [k for k, l in enumerate(src) if "local ZA = (GAME == 'black')" in l][0]
n = 0
for k in list(range(i, j)) + [za, za + 1]:
    code, sep, com = src[k].partition("--")
    def rep(m):
        global n
        q, s = m.group(1), m.group(2)
        mc = re.match(r"(.+) Pokémon Center$", s)
        if s in names: t = names[s]
        elif mc and mc.group(1) in names: t = "Centro Pokémon de " + names[mc.group(1)]
        else: return m.group(0)
        n += 1
        return q + t.replace(q, "") + q
    src[k] = re.sub(r"""(["'])([^"'\n]+)\1""", rep, code) + sep + com
print("zone_building + ZA", n)
open(LUA, "w", encoding="utf-8", newline="").write("\n".join(src))
