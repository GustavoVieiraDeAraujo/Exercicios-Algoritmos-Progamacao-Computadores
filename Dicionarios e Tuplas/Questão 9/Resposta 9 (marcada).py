x,y=input().split()

numero_alunos=int(x)
numero_duplas=int(y)

nome_alunos=input().split()

dic_duplas={}
indice=1
for nome in nome_alunos:
    while indice < numero_alunos:
        p = nome_alunos.index(nome)
        juncao = nome+" "+nome_alunos[p+indice]
        dic_duplas[juncao]=0
        indice+=1
    indice=1
    numero_alunos-=1

hist=[]
temp={}
for i in range(numero_duplas):
    entrada=input()
    hist.append(entrada)
    dupla=entrada.split()
    for chave in dic_duplas:
        if dupla[0] in chave:
            dic_duplas[chave]+=1
        elif dupla[1] in chave:
            dic_duplas[chave]+=1

for l in hist:
    temp[l]=dic_duplas[l]
    

dic_final={}
for chave in temp.items():
    for elemento in chave:
        for teste in elemento.split():
            if teste in dic_final:
                pass
            else:
                dic_final[teste]=chave[1]
        break

ordemAlfabetica=sorted(dic_final) 

for unidade in ordemAlfabetica:
    print(f"{unidade} possui {dic_final[unidade]} amigos")
