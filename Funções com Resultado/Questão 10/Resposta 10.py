def collatz(s, n, cont):
    if cont == n:
        return s
    elif s%2 == 0:
        return collatz(s//2,n,cont+1)
    elif s%2 != 0:
        return collatz(((s*3)+1), n, cont+1)