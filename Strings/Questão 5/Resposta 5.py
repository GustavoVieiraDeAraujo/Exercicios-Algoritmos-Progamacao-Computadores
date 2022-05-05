x = input()
Maisucula = 0
Minuscula = 0

for caractere in x:
    if caractere.isupper():
        Maisucula += 1
    else:
        Minuscula += 1

if Maisucula > Minuscula:
    print(x.upper())
else:
    print(x.lower())
