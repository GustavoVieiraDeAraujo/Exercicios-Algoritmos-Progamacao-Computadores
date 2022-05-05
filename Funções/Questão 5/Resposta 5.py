def concatenar(x,y):
    print(x+""+y)
def repetir(x,z):
    print(x*z)
def ambos(x,y,z):
    concatenar(x,y)
    repetir(x,z)
    print((x+""+y)*z)

x,y,k =input().split()
z =int(k)

ambos(x,y,z)