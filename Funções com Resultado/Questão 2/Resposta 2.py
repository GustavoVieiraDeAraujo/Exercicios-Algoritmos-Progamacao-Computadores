def calculaValores(a,b):
    print("Sou a função de calcular. Calculando...")
    return a+b

def repassaValores(a,b):
    print("Aqui é a função de repassar! Estou repassando a e b!")
    soma=calculaValores(a,b)
    print("Tenho o resultado! Retornando!")
    return print(soma)

a=int(input())
b=int(input())
repassaValores(a,b)