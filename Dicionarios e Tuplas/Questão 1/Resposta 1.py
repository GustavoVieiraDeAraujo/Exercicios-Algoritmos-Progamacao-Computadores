p1 = input()
p2 = input()
l1 = []
l2 = []

for caractere_1 in p1:
    l1.append(caractere_1)
    l1.sort()

for caractere_2 in p2:
    l2.append(caractere_2)
    l2.sort()

if l1 == l2:
    print("True")
else:
    print("False")


