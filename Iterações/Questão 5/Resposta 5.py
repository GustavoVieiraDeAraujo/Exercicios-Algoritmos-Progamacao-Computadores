def primo(n):
    total = 0
    for i in range(1,n+1):
        if n % i == 0:
            total += 1
        else:
            total += 0
    if total == 2:
        return True
    else: 
        return False

x = int(input())
numero = 0
acumulador = 1
cont = 0

while cont < x:
    if primo(numero) == True:
        acumulador *= numero
        numero += 1
        cont += 1
    else:
        numero += 1

print(acumulador)



