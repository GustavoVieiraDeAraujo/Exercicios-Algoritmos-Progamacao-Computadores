senha = input()

if any(x.isupper() for x in senha):
    if any(x.islower() for x in senha):
        if any(x.isnumeric() for x in senha):
            if len(senha)>=6 and len(senha)<=32:
                if any(x.isspace() for x in senha):
                    print("Senha invalida.")
                elif senha.isalnum():
                    print("Senha valida.")
                else:
                    print("Senha invalida.")
            else:
                print("Senha invalida.")    
        else:
            print("Senha invalida.")
    else:
        print("Senha invalida.")
else:
    print("Senha invalida.")

