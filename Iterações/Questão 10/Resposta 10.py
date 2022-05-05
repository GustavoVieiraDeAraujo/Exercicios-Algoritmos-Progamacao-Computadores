def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

x = int(input())
acumulador = 0
cont = 0

while x > 0:
    if par(x) == True and x != 0:
        acumulador += x
        cont += 1
        x= int(input())
    else:
        x = int(input())
if cont != 0:
    media_par = acumulador/cont
    print(media_par)
else :
    print("0.0")


