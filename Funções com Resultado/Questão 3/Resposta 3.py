def divisivel(a,b):
    resto=a%b
    if resto == 0:
        return print("x eh divisivel por y")
    elif resto != 0:
        return print("x nao eh divisivel por y")
    
x=int(input())
y=int(input())

divisivel(x,y)