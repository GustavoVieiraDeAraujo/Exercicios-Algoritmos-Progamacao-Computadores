p1 = input()
d1 = {}

for caractere in p1:
    if caractere in d1:
        d1[caractere] += 1
    else:
        d1[caractere] = 1

print(d1)