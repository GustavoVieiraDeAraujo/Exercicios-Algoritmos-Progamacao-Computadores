def escada(n):
    if n>0:
        escada(n-1)
        print("#"*n)
    