import math

listaDaEntrada =[int(numero) for numero in input().split()]
media = sum(listaDaEntrada)/len(listaDaEntrada)
acumulador = 0 

for elemento in listaDaEntrada:
    operacao_1 = (elemento - media)**2
    acumulador += operacao_1

print(f"{media:.1f}")
print(f"{math.sqrt(acumulador/len(listaDaEntrada)):.1f}")
