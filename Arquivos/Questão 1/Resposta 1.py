with open(input()) as file:
    for line in file:
        contador = 0
        for char in "polystation":
            if char in line:
                contador+=1
        if contador == len("polystation"):
            print("o poderoso polystation ainda vive")

        contador=0
        for char in "nintendomeiaquatro":
            if char in line:
                contador+=1
        if contador == len("nintendomeiaquatro"):
            print("O encanador venceu outra vez")
        