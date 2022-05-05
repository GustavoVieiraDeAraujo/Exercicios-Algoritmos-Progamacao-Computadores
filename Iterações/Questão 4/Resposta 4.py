n = int(input())
while n != 42:
    if n < 42:
        print("É maior que isso")
        n = int(input())
    elif n > 42:
        print("Tenta dar uma diminuída")
        n = int(input())
        
print("Você acertou!")