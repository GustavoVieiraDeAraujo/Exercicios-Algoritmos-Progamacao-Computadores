litros = int(input())
capacidade = litros
caminho = int(input())
km = 0

while caminho != -1:
    if caminho == 0:
        if litros < 1:
            break
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
        if perdeu > litros:
            break
        litros -= perdeu
        km += 1
        caminho = int(input())


if caminho == -1:
    print("Lar Deivis lar")
else:
    print(km)


