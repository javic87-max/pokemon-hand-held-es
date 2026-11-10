# Pokémon Hand Held en español

Adaptación al español de **Pokémon Hand Held**, el mod de accesibilidad creado por **Amethyst** que permite jugar a los Pokémon de Nintendo DS con lector de pantalla en el emulador BizHawk.

El mod original funciona con las ROMs en inglés. Este proyecto hace que funcione con las **ROMs españolas** y que todo lo que dice salga en español.

Es un proyecto derivado (fork) del mod de Amethyst. No lo sustituye: hace falta el mod original instalado.

## Juegos

| Juego | Código de la ROM | Estado |
|---|---|---|
| Pokémon Edición Blanca | IRAS | En pruebas, se puede jugar |
| Pokémon Edición Negra | IRBS | En pruebas, se puede jugar |
| Pokémon Platino | CPUS | **Experimental**: se está probando |

Las ROMs inglesas siguen funcionando igual que con el mod original.

## Qué hace

- **Direcciones de memoria:** las ROMs españolas guardan muchas cosas en sitios distintos a las inglesas. Se han medido comparando el código de las ROMs inglesas y españolas.
- **Textos:** las listas que el mod lleva escritas en inglés se han sustituido por el texto oficial de la ROM española: ataques, Pokémon, objetos, habilidades, lugares, Pokédex y otras.
- **Etiquetas propias del mod:** menús, guiado, lista de navegación, contadores («2 de 3») y demás, traducidas a mano.

## Instalación

1. Instala el mod original de Amethyst, en la versión para la que está hecho este proyecto (con soporte de Platino, Diamante y Perla).
2. Haz una copia de tus partidas, en la carpeta `NDS\SaveRAM` del emulador, y de tu `Lua\main.lua`.
3. Copia la carpeta `Lua` de este proyecto dentro de la carpeta del emulador y acepta sobrescribir. Cambia `main.lua` y añade `games\bw_es.lua` y `games\platinum_es.lua`.
4. Abre tu ROM española y carga `main.lua` en la consola de Lua, como con las versiones inglesas.

No se incluye ninguna ROM. Necesitas tus propias copias.

Si actualizas el mod original, se sobrescribirá `main.lua` y las ROMs españolas dejarán de reconocerse hasta adaptar el proyecto a la versión nueva.

## Contenido

- `Lua/main.lua`: el cargador del mod original con las ROMs españolas añadidas.
- `Lua/games/bw_es.lua`: Blanco y Negro en español, hecho a partir de `games/bw.lua` del mod original.
- `Lua/games/platinum_es.lua`: Platino en español, hecho a partir de `games/platinum.lua` del mod original.
- `herramientas/`: los scripts de Python usados para medir las direcciones y traducir los textos. Ver abajo.

## Herramientas

Sirven para rehacer los archivos españoles cuando sale una versión nueva del mod original. Necesitan Python 3, los paquetes de `requirements.txt` y las ROMs inglesas y españolas. Las rutas de las ROMs y del mod están escritas dentro de los scripts y hay que ajustarlas a cada equipo.

- **Medir direcciones:** `port.py`, `vt.py`, `lit.py`, `forced.py` (Blanco y Negro) y `pl_addresses.py`, `pl_states.py` (Platino).
- **Extraer textos de la ROM:** `text.py` (Blanco y Negro) y `pl_text.py` (Platino).
- **Traducir:** `translate.py`, `places.py`, `labels.py`, `phrases.py`, `npcs.py`, `small.py`, `bw_small2.py` (Blanco y Negro) y `pl_translate.py`, `pl_sent.py`, `pl_labels.py`, `pl_final.py`, `pl_intro.py`, `pl_small.py`, `pl_names.py`, `pl_banks.py`, `pl_status.py` (Platino).
- **Comprobar:** `luacheck.py` (sintaxis) y `smoke.py` (arranca el mod fuera del emulador con una ROM simulada).

Los datos que estos scripts extraen de las ROMs no se guardan en el repositorio.

## Problemas conocidos

- Las descripciones de la tecla D (cómo es un Pokémon o un personaje) siguen en inglés.
- En Platino, el mensaje de la fuente del gimnasio de Ciudad Vetusta no se lee. Pasa también en el mod original en inglés.
- En Platino, el sonido podía trabarse tras mucho rato de juego. Se ha añadido un vaciado automático de la consola de Lua que lo mejora; sigue en observación.

## Créditos

- **Amethyst**: creó Pokémon Hand Held, el mod de accesibilidad original. Todo el funcionamiento del mod es su trabajo.
- **Randal**: primera adaptación del mod a la ROM española de Pokémon Negro.
- **javic87-max**: adaptación a las ROMs españolas de Blanco, Negro y Platino, pruebas y coordinación.
- Las descripciones de la carpeta `descriptions` del mod original tienen su propia licencia Creative Commons; consulta su `README.md`.

Pokémon es una marca de Nintendo, Creatures Inc. y GAME FREAK inc.
