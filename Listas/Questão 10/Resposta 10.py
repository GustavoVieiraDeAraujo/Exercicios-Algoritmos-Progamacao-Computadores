x = int(input())
listaJ = []
total = 0

while x > 0:
    entrada_1 = input()
    lista_1 = entrada_1.split()
    listaJ.append(lista_1)
    x-=1

y = int(input())
listaF= []

while y > 0:
    entrada_2= input()
    lista_2 = entrada_2.split()
    listaF.append(lista_2)
    y-=1

for elemento_1 in listaJ:
    pagar = 0
    z = elemento_1[0]
    for elemento_2 in listaF:
        if z in elemento_2:
            pagar = float(elemento_1[1])*float(elemento_2[1])
            total += pagar
            break
    if pagar == 0:
        print(z+" esta em falta")

print(f"{total:.2f}")


       