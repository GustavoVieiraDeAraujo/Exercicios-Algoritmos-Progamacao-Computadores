def maiorQue1000(a):
    if a > 1000:
        return print(a)
    else:
        return maiorQue1000(a**2)

x=int(input())
maiorQue1000(x)