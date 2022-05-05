import math

def printMatriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end="")
        print()

def TwoDSpace(deslocamento,amplitude,espaço):
    matriz = []
    for linha in range(20):
        matriz.append([])

    for coluna in range(40):
        for linha in matriz:
            linha.append(espaço)
            
    for i in range(40):
        j = int(deslocamento-amplitude*math.cos(10*i*math.pi/180))
        if j == 20:
            pass 
        else:
            matriz[j][i] = "*"
    
    printMatriz(matriz)


