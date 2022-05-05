nome = input()
lista = []
while nome != "EOF":
    lista.append(nome)
    lista.sort()
    nome = input()

print(len(lista))
print(lista)