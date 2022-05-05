entrada = input()
listaDaEntrada = entrada.split()
print(listaDaEntrada)

for palavra in listaDaEntrada:
    if len(palavra)> 6:
        print(palavra)
