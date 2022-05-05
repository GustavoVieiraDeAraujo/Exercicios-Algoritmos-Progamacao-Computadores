quantJogadores = int(input())
listaJogadores=[int(numero) for numero in input().split()]
listaJogadores.sort()

x = quantJogadores - 11
titulares = listaJogadores[x:quantJogadores]
pontosTitulares = sum(titulares)
reservas = listaJogadores[:x]
pontosReservas = sum(reservas)

diferenca = pontosTitulares - pontosReservas

print(diferenca)