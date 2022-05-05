entrada_1 = int(input())
bilhete =[int(i) for i in input().split()]
dic ={}

for i in range(0,entrada_1):
    entrada_2 = input()
    p1=entrada_2.split("-")
    p2=p1[1].split()
    dic[p1[0]]=[int(i) for i in p2]
contador = 0
for chave in dic.items():
    if chave[1] == bilhete:
        print("deu bom!")
        print(chave[0])
        contador+=1
        break
if contador == 0:
    print("não foi dessa vez /:")
    



