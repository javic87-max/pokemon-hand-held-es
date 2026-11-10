"""ES: la introduccion (ov73) tiene un estado mas, el 27; los estados ingleses >= 27 valen +1."""
import re
from pl_text import banks, norm
LUA=r"C:/Users/caspi/Documents/ds access/Lua/games/platinum_es.lua"
s=open(LUA,encoding="utf-8").read(); S=banks('CPUS')
i=s.index("--[[ INTRO_TEXT:BEGIN ]]"); j=s.index("--[[ INTRO_TEXT:END ]]")
b=s[i:j]
b=re.sub(r"\[(\d+)\] = \"",lambda m:'[%d] = "'%(int(m.group(1))+(1 if int(m.group(1))>=27 else 0)),b)
b=b.replace("local ST_PKBL_WAIT_INPUT = 47","local ST_PKBL_WAIT_INPUT = 48   -- ES: un estado mas desde el 27 (medido en ov73)").replace("local ST_GENDR_CHOICE = 67","local ST_GENDR_CHOICE = 68")
L=b.split("\n")
for n,l in enumerate(L):
    for k,e in ((12,2),(14,3)):
        if l.lstrip().startswith('[%d] = "'%k): L[n]=l[:l.index('[')]+'[%d] = "%s",'%(k,norm(S[389][e]).replace('"',"'"))
s=s[:i]+"\n".join(L)+s[j:]
open(LUA,"w",encoding="utf-8",newline="").write(s)
print(re.findall(r"\[(\d+)\] = \"(.{30})",s[i:j+400])[:12]); print(re.findall(r"local ST_\w+ = \d+",s[i:j+400]))
