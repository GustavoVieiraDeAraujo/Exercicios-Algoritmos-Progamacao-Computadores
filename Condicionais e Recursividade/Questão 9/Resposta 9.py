def paresDeNumeros(n,m):
    if n<=m :
        print(n,m)
        return paresDeNumeros(n+2,m-1)