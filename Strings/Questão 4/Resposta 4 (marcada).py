def tem_letra_maiúscula(string):
    for caractere in string:
        if caractere.isupper():
            return True
            break
    return False