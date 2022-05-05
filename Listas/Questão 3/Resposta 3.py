dic = {}
lista = []
nome = "começar"

while nome != "fim":
    nome = input()
    if nome in dic:
        dic[nome]+=1
    else:
        dic[nome]=1

dic.pop("fim")
for key in sorted(dic.keys()):
    x=key+" "+str(dic[key])
    y= x.split()
    lista.append(y)

for lista in lista:
    if int(lista[1]) > 1:
        print(" ".join(lista))
