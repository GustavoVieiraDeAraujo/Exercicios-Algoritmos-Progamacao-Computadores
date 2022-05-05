def ritmoMedio(h,m,s,d):
    ConversãoHparaS=h*3600
    ConversãoMparaS=m*60
    TotalDeSegundos=s+ConversãoHparaS+ConversãoMparaS
    RitmoMedioEmSegundos=int(TotalDeSegundos/d)
    mediaMinutos=int(RitmoMedioEmSegundos/60)
    mediaSegundos=RitmoMedioEmSegundos%60
    print(f"{mediaMinutos:02d}:{mediaSegundos:02d} min/km")