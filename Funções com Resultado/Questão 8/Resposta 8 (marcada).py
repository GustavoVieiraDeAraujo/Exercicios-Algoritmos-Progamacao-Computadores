def hh_duracao(a,b,c,d,e,f):
    inicio = a*3600 + b*60 + c
    final = d*3600 + e*60 + f
    duracao = final - inicio
    if duracao <= 0:
        duracao += 24*3600
    horas = duracao // 3600
    minutos = (duracao % 3600) // 60
    segundos = duracao % 60
    return horas, minutos, segundos