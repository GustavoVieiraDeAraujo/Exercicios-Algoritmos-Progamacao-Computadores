def imprimeTermos(n):
    if n>0 and n%2 == 0 :
        print(n)
        return imprimeTermos(n-2)
    elif n>=0 and n%2 != 0:
        print(n)
        return imprimeTermos(n-2)
    else:
        print("0")