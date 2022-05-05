def feedback(nota):
    if nota < 26:
        x = 28-nota
        return f"Car@ alun@, revise a materia toda! Nao foi dessa vez, mas nao desista! Rumo aos 28!!! Saldo: -{x}"
    elif nota == 26 or nota == 27:
        x = 28-nota
        return f"Foi quaaaaaaase, vamos estudar mais pra passar semana que vem (: Saldo: -{x}"
    elif nota == 28:
        return f"Mandou bem! Continue estudando que voce vai fechar a prova ;)"
    elif nota >= 29 and nota <= 35:
        x = nota-28
        return f"Mandou bem! Continue estudando que voce vai fechar a prova ;) Saldo: +{x}"
    elif nota >= 36 and nota <= 39:
        x = nota-28
        return f"Excelente!!!! Saldo: +{x}"
    elif nota == 40:
        return "Lendaaaaario!"