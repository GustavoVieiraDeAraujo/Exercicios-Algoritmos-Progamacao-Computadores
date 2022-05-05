def quant_divisores(n, conta, quant):
    if conta <= n:
        if n%conta == 0:
            return quant_divisores(n, conta+1, quant+1)
        elif n%conta != 0:
            return quant_divisores(n, conta+1, quant)
    else:
        return quant