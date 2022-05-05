n = int(input())
peixe =input()
x = 0

if peixe == "atum":
    while x<n:
        x +=1
        print("Nossa, pesquei um atum gigante!")

elif peixe == "salmão":
    while x<n*2:
        x +=1
        print("Que salmão bonito que pesquei!")
else:
    print("Nem sabia que esse peixe existia")

