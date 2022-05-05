matriz = []
with open("/etc/passwd") as file:
    for line in file:
        line = [line.rstrip("\n").split(":")]
        matriz.append(line)

entrada = int(input())
print(matriz[entrada-1][0][0])