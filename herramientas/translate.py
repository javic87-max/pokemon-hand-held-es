"""Sustituye en main_es.lua las listas de texto en ingles por el texto de la ROM espanola.

Cada elemento de una lista se busca, normalizado, en los bancos a/0/0/2 de la ROM inglesa (IRAO); si
aparece, se cambia por la cadena de la MISMA posicion en la ROM espanola (IRAS). Lo que no se encuentra
se queda en ingles. Uso: python translate.py [--write]
"""
import re, sys, collections
from text import banks

LUA = r"C:/Users/caspi/Documents/ds access/Lua/main_es.lua"
import os; LUA = os.environ.get("LUA_FILE", LUA)
EN, ES = banks("IRAO"), banks("IRAS")
SKIP_LINES = set()          # se rellena abajo con lineas a no tocar (creditos)


def norm(s):
    s = re.sub(r"\{[0-9A-F]{4}\}", "", s)
    s = s.replace("\n", " ")
    return re.sub(r"\s+", " ", s).strip()


IDX = collections.defaultdict(list)
for b, bk in enumerate(EN):
    if not bk or not ES[b] or len(ES[b]) != len(bk): continue
    for j, s in enumerate(bk):
        n = norm(s)
        if n: IDX[n].append((b, j))


def lua_unescape(s):
    return s.replace("\\'", "'").replace('\\"', '"')


def translate_list(body, sep, quote):
    items = body.split(sep)
    votes = collections.Counter()
    for it in items:
        for b, _ in IDX.get(norm(lua_unescape(it)), ()): votes[b] += 1
    out, hit, conflict = [], 0, 0
    for it in items:
        cands = IDX.get(norm(lua_unescape(it)), ())
        if not cands:
            out.append(it); continue
        b, j = max(cands, key=lambda c: votes[c[0]])
        t = norm(ES[b][j])
        bad = (sep in t) or ("]==]" in t) or (quote and (quote in t or "\\" in t))
        if bad or not t:
            conflict += 1; out.append(it); continue
        out.append(t); hit += 1
    return sep.join(out), hit, conflict, len(items), votes.most_common(2)


def main(write):
    src = open(LUA, encoding="utf-8").read()
    lines = src.split("\n")
    # creditos: el reader los compara con el orden de la secuencia inglesa; no se tocan
    for i, l in enumerate(lines):
        if "Junichi Masuda|2-D Art Director" in l: SKIP_LINES.add(i)
    pat = re.compile(r'"([^"\n]{120,})"|\[==\[(.*?)\]==\]')
    total = 0
    for i, l in enumerate(lines):
        if i in SKIP_LINES or l.lstrip().startswith("--"): continue
        def rep(m):
            nonlocal total
            body = m.group(1) if m.group(1) is not None else m.group(2)
            quote = '"' if m.group(1) is not None else None
            seps = [s for s in ("\\001", "\\1", "|", ",") if body.count(s) >= 4]
            if not seps: return m.group(0)
            sep = seps[0]
            new, hit, conf, n, v = translate_list(body, sep, quote)
            if hit:
                total += hit
                print(f"linea {i+1:6d}: {hit:5d}/{n:5d} traducidos, {conf} conflictos, bancos {v}")
            return ('"%s"' % new) if quote else ("[==[%s]==]" % new)
        lines[i] = pat.sub(rep, l)
    print("total", total)
    if write:
        open(LUA, "w", encoding="utf-8", newline="").write("\n".join(lines))
        print("escrito")


if __name__ == "__main__":
    main("--write" in sys.argv)
