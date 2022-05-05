entrada = input()
intervalo = input()
listaEntrada = entrada.split()
listaIntervalo = intervalo.split()
novoIntervalo = []
x = int(listaIntervalo[0])


while x != int(listaIntervalo[1]) :
    novoIntervalo.append(str(x))
    x+=1
novoIntervalo.append(str(listaIntervalo[1]))

y = []
for caractere in listaEntrada:
    if caractere in novoIntervalo:
        y.append(caractere)
        listaEntrada[listaEntrada.index(caractere)]=""

print([int(i) for i in y])
while "" in listaEntrada:
    listaEntrada.remove("")
print([int(i) for i in listaEntrada])
