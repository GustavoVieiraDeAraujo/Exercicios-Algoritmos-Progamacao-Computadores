def somaDivisores(numero):
    for divisor in range(1, numero):
        if numero % divisor == 0:
            listaDeDivisores.append(divisor)
    
def tresDivisoresPrimos(listaDeDivisores):
    contador_1 = 0
    for divisor in listaDeDivisores:
        if contador_1 == 3:
            return True
        if divisor > 1:
            for i in range(2, divisor):
                if (divisor % i) == 0:
                    break
            else:
                contador_1 += 1
    

def temCinco(numero):
    if "5" in str(numero):
        return True

with open(input()) as file:
    for numero in file:
        contador = 0
        listaDeDivisores=[]
        numero = int(numero.rstrip("\n"))
        somaDivisores(numero)
        if sum(listaDeDivisores) == numero:
            contador+=1
        if tresDivisoresPrimos(listaDeDivisores) == True:
            contador+=1
        if temCinco(numero) == True:
            contador+=1
        if contador >= 2:
            print("ai tanto faz a definicao ahuehuahe")
        if contador == 1:
            if sum(listaDeDivisores) == numero:
                print("A matematica nunca erra")
            if tresDivisoresPrimos(listaDeDivisores) == True:
                print("Isso foi muito especifico Font, ta tudo bem?")
            if temCinco(numero) == True:
                print("Gui ama o numero 5!")
        if contador == 0:
            print("numero tres vezes imperfeito?")
    