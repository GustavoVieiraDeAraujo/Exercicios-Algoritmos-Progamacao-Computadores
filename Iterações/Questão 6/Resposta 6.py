x = int(input())
inverso = 0

if x < 0:
    numero = abs(x)
    while(numero != 0):
        temp = numero%10
        inverso = inverso * 10 + temp
        numero = numero // 10
    print(-inverso)

if x>0:
    numero = x
    while(numero != 0):
         temp = numero % 10
         inverso = inverso * 10 + temp
         numero = numero // 10
    print(inverso)






    