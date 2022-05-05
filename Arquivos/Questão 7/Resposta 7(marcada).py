prato = input()
dicionarioDoPrato = {}

with open("cardapio.txt") as file:
    for line in file:
        if prato in line.lower().replace("\n", ""):
            dicionarioDoPrato[line.replace("\n", "").split(
                "/")[0]] = line.replace("\n", "").split("/")[1]
if len(dicionarioDoPrato) == 0:
    print("Infelizmente não temos este prato")
else:
    for key in dicionarioDoPrato:
        print(f"{key} {dicionarioDoPrato[key]}")
    print(
        f"Sua conta deu: {sum([float(i) for i in dicionarioDoPrato.values()]):.2f}")

with open("carteira.txt") as file:
    for line in file:
        flag = True
        metodo,valor=line.rstrip("\n").split("/")
        if float(valor) >= sum([float(i) for i in dicionarioDoPrato.values()]):
            if metodo == "Dinheiro":
                print("Vou pagar com dinheiro")
                break
            elif metodo == "Cartão de crédito":
                print("O jeito é pagar com o cartão de crédito")
        else:
            flag =False
    
if flag == False:
    print("Ah não! Vou ter que lavar prato!")