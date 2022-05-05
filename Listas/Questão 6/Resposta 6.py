listaDaEntrada =[int(numero) for numero in input().split()]
x = sorted(listaDaEntrada)
soma = 0

while listaDaEntrada != x :
    for elemento in listaDaEntrada:
        if elemento == listaDaEntrada[-1]:
            break
        if elemento > listaDaEntrada[listaDaEntrada.index(elemento)+1]:
            z = listaDaEntrada[listaDaEntrada.index(elemento)+1]
            listaDaEntrada[listaDaEntrada.index(elemento)+1]= elemento
            listaDaEntrada[listaDaEntrada.index(elemento)]=z 
            soma += 1
        else:
            soma += 0

print(soma)