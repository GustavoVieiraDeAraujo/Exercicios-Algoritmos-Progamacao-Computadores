def calcular_media(n1, n2, n3):
    nota_final = (n1*1 + n2*2 + n3*3)/6
    print(f'Sua nota final é {nota_final:.2f}')

n1, n2, n3 = map(float, input().split())
calcular_media(n1, n2, n3)