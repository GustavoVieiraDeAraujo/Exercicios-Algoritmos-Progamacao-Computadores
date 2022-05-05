def verLinhas(matriz):
    for linha in matriz:
        temp = "".join(linha)
        if "wally" in temp:
            pcoluna = temp.index("wally")+1
            plinha = matriz.index(linha)+1
            print(f"{plinha} {pcoluna} horizontal")
            return True
    return False
    
def verColunas(matriz):
    pcoluna = 0
    while True:
        temp = ""
        for linha in matriz:
            temp+=linha[pcoluna]
        if "wally" in temp:
            plinha = temp.index("wally")+1
            pcoluna +=1
            print(f"{plinha} {pcoluna} vertical")
            return
        else:
            pcoluna+=1
        
matriz=[]
with open(input()) as file:
    for line in file:
        linha =[]
        line = line.rstrip("\n")
        for caractere in line:
            linha.append(caractere)
        matriz.append(linha)

if verLinhas(matriz) == True:
    pass
else:
    verColunas(matriz)
