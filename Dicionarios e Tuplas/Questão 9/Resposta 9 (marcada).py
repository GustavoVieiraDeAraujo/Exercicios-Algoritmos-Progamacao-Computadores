x,y=input().split()

numero_alunos=int(x)
numero_duplas=int(y)

nome_alunos=input().split()

parent = {nome: nome for nome in nome_alunos}

def find(a):
    while parent[a] != a:
        a = parent[a]
    return a

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb

for i in range(numero_duplas):
    entrada = input()
    dupla = entrada.split()
    union(dupla[0], dupla[1])

from collections import Counter
tamanho_componente = Counter(find(nome) for nome in nome_alunos)

ordemAlfabetica = sorted(nome_alunos)

for unidade in ordemAlfabetica:
    print(f"{unidade} possui {tamanho_componente[find(unidade)] - 1} amigos")
