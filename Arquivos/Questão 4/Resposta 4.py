arq_1,arq_2 = input().split()

with open(arq_1) as file:
    file = file.readlines()
    if len(file) > 1:
        print(f"O arquivo {arq_2} esta quase vazio, mas o {arq_1} nao esta!")
        for line in file:
            print(line.rstrip("\n"))
    elif len(file) == 1:
        print(f"O arquivo {arq_1} esta quase vazio, mas o {arq_2} nao esta!")
        with open(arq_2) as file:
            for line in file:
                print(line.replace("\n", ""))
              