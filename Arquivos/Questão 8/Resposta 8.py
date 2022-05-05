import os

x = input()
x = x.split()[-1]
tuplas =[]

if os.path.isfile(x):
    print("da pra abrir")
    with open(x) as file:
        for line in file:
            nome,y= line.strip("\n").split()
            numero = int(y)
            tuplas.append((nome,numero))
    tuplas.sort(key=lambda x: x[1], reverse=True)
    for tupla in tuplas:
        print(tupla)
else:
    print("nao da pra abrir")