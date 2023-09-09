listaDaEntrada =[int(numero) for numero in input().split()]
soma = 0

n = len(listaDaEntrada)
for i in range(n):
    for j in range(n - i - 1):
        if listaDaEntrada[j] > listaDaEntrada[j+1]:
            listaDaEntrada[j], listaDaEntrada[j+1] = listaDaEntrada[j+1], listaDaEntrada[j]
            soma += 1

print(soma)