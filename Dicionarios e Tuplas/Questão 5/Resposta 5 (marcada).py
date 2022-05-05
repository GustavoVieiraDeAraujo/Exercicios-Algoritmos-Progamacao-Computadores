tamanho= int(input())
entrada_1= input().split()
d1 = {}
x=0

for numero in entrada_1:
    d1[x]=numero
    x+=1

perguntas=int(input())
while perguntas>0:
    x,y=input().split()
    if x == "1":
        contador = 0
        for chave in d1.items():
            if y in chave:
                contador+=1
        if contador == 0:
            print("-1")
        else:
            print(contador)
        perguntas-=1
    elif x == "2":
        contador = 0
        for chave in d1.items():
            if y in chave:
                print(chave[0])
                contador+= 1
                perguntas-=1
                break
        if contador == 0:
            print("-1")
        






