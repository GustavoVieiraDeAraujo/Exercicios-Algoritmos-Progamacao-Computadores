def não_possui_a_letra_a(palavra):
    if 'a' in palavra:
        return False
    elif 'á' in palavra:
        return False
    elif 'à' in palavra:
        return False
    elif 'â' in palavra:
        return False
    elif 'a'.upper() in palavra:
        return False
    elif 'á'.upper() in palavra:
        return False
    elif 'à'.upper() in palavra:
        return False
    elif 'â'.upper() in palavra:
        return False
    else:
        return True