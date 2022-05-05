def hh_duracao(a,b,c,d,e,f):
    if a != d:
        horas=24-a+d
        minutos=e-b
        segundos=f-c
        return horas,minutos,segundos
    elif a==d and b==e==0 and c==f==0:
        horas=24
        minutos=0
        segundos=0
        return horas,minutos,segundos
    elif a==d and b>=0 and c>=0 and e>=0 and f>=0:
        horas=d-a
        minutos=e-b
        segundos=f-c
        return horas,minutos,segundos