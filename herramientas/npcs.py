"""Nombres de personas/roles en las tablas de navegacion (rango ROLE_SCRIPTS .. fin de la tabla de charlas)."""
import re, os
LUA = os.environ.get("LUA_FILE", r"C:/Users/caspi/Documents/ds access/Lua/main_es.lua")
D={"Shop attendant":"Dependiente","Bianca":"Bel","Team Plasma":"Equipo Plasma","Professor Juniper":"Profesora Encina","Burgh":"Camus","Leader":"Líder","Man":"Hombre","Trainer":"Entrenador","Lenora":"Aloe","Woman":"Mujer","The Riches":"Finolis","Skyla":"Gerania","Waitress":"Camarera","Pokemon":"Pokémon","Clerk":"Dependiente","Brycen":"Junco","Alder":"Mirto","Worker":"Operario","Scientist":"Científico","School Kid":"Escolar","Ranger":"Pokémon Ranger","Psychic":"Médium","Preschooler":"Preescolar","Old man":"Anciano","Elite Four":"Alto Mando","Elesa":"Camila","Backpacker":"Mochilero","Backers":"Hinchas","Ace Trainer":"Entrenador guay","Veteran":"Veterano","Old woman":"Anciana","Mom":"Mamá","Maid":"Criada","Drayden":"Lirio","Clay":"Yakón","Breeder":"Criapokémon","Boy":"Niño","Battle Girl":"Luchadora","Youngster":"Joven","Young woman":"Joven","Waiter":"Camarero","Swimmer":"Nadador","Subway Boss":"Jefe de Metro","Striker":"Delantero","Socialite":"Marquesa","Smasher":"Tenista","Shauntal":"Anís","Roughneck":"Calvo","Rich Boy":"Niño bien","Policeman":"Policía","Pokefan":"Pokéfan","Parasol Lady":"Dama Parasol","Little girl":"Niña","Little Girl":"Niña","Linebacker":"Quarterback","Lady":"Damisela","Infielder":"Pitcher","Hoopster":"Pívot","Hiker":"Montañero","Harlequin":"Arlequín","Gentleman":"Duque","Fisherman":"Pescador","Fennel":"Oryza","Depot Agent":"Ferroviario","Cynthia":"Cintia","Cyclist":"Ciclista","Cilan":"Millo","Caitlin":"Catleya","Black Belt":"Karateka","Attendant":"Encargado","Twins":"Gemelas","Pilot":"Piloto","Nursery Aide":"Seño","Nurse":"Enfermera","Musician":"Cantautor","Motorcyclist":"Motero","Marshal":"Lotto","Looker":"Handsome","Lass":"Chica","Janitor":"Limpiador","Ingo":"Fero","Hooligans":"Pandilleros","Guitarist":"Guitarrista","Grimsley":"Aza","Emmet":"Caril","Dancer":"Breakdancer","Cress":"Maíz","Chili":"Zeo","Cheren's Mom":"Madre de Cheren","Cheren's Dad":"Padre de Cheren","Champion":"Campeón","Biker":"Motorista","Bianca's Mom":"Madre de Bel","Bianca's Dad":"Padre de Bel","Baker":"Pastelera","Artist":"Artista","Cedric":"Didier"}
L=open(LUA,encoding="utf-8").read().split("\n")
a=next(i for i,l in enumerate(L) if "local ROLE_SCRIPTS = {" in l)
b=next(i for i,l in enumerate(L) if "[121]={[1]=(GAME" in l)
b=next(i for i in range(b,len(L)) if L[i].strip()=="}")
n=0
for i in range(a,b+1):
    code,sep,com=L[i].partition("--")
    def rep(m):
        global n
        if m.group(1) in D: n+=1; return '="%s"'%D[m.group(1)]
        return m.group(0)
    L[i]=re.sub(r'="([^"]*)"',rep,code)+sep+com
L[b-0]=L[b]
s="\n".join(L)
s=s.replace('(GAME == "black") and "Drayden" or "Iris"}','(GAME == "black") and "Lirio" or "Iris"}')
open(LUA,"w",encoding="utf-8",newline="").write(s); print("lineas",a+1,b+1,"cambios",n)
for k in D:
    if re.search(r'[=~]= *"%s"'%re.escape(k), s): print("COMPARACION", k)
