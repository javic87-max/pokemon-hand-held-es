"""Lista los literales cortos de main_es.lua que coinciden con algun texto del juego (ingles)."""
import re, collections, sys
from text import banks
from translate import IDX, norm, ES, LUA

src = open(LUA, encoding="utf-8").read().split("\n")
pat = re.compile(r'"([^"\n]{1,60})"|\'([^\'\n]{1,60})\'')
found = collections.Counter(); where = collections.defaultdict(list)
for i, l in enumerate(src, 1):
    code = l.split("--")[0] if not l.lstrip().startswith("--") else ""
    for m in pat.finditer(code):
        s = m.group(1) if m.group(1) is not None else m.group(2)
        if norm(s) in IDX and not s.isdigit():
            found[s] += 1; where[s].append(i)
for s, n in sorted(found.items(), key=lambda x: where[x[0]][0]):
    b, j = IDX[norm(s)][0]
    print(f"{where[s][:4]} {s!r} -> {norm(ES[b][j])!r} (bank {b})")
