litros = int(input())
capacidade = litros
caminho = int(input())
km = 0

while caminho != -1 and litros >= 0:
    if caminho == 0:
        litros -= 1
        km += 1
        caminho = int(input())
    elif caminho == 1:
        querEncher = int(input())
        if querEncher > capacidade-litros:
            litros =capacidade
            km+=1
            caminho = int(input())
        else:
            litros += querEncher
            km += 1
            caminho = int(input())
    elif caminho == 2:
        perdeu = int(input())
        litros -= perdeu
        km += 1
        caminho = int(input())
    
    
if litros == 0:
    print(km)
elif litros == -1:
    print(km-1)
elif caminho == -1:
    print("Lar Deivis lar")


