def achiles(distancia):
    if distancia <= 0.5:
        print("Foi decidido o empate.")
        return 0
    else:
        print(f'Aquiles se aproximou um pouco, mas a tartaruga ainda está {distancia} metros na frente.')
        return achiles(distancia/2)