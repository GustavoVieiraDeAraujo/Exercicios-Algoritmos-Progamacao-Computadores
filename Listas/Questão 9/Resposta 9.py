tamanho = int(input())
lista = [int(numero) for numero in input().split()]
lista.sort()
soma = 0

for elemento in lista:
    if soma == 42:
        break
    posicaoElemento = lista.index(elemento)
    acumulador = 1
    while soma != 42:
        if acumulador == tamanho:
            tamanho -= 1
            break
        soma = elemento + lista[posicaoElemento+acumulador]
        acumulador += 1
        if soma == 42:
            break

if soma == 42:
    print("sim")
else:
    print("nao")    
