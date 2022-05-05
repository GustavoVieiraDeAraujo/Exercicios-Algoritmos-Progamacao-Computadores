def valid_triangle(a,b,c):
    if a>=b+c or b>=c+a or c>=a+b :
        print("invalido")
    else :
        print("valido")