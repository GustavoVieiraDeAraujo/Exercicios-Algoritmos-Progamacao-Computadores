a,b,c,d,e = input().split()

lap = int(a)
ipa = int(b)
dia = int(c)
pag = int(d)
dis = int(e)

valor = lap * 1500 + ipa * 1000;

if ((lap + ipa) > 3):
    valor -= 500
    
if (pag == 0):
    if (dia <= 15):
        valor = valor * 0.90
    else:
        valor = valor * 0.95
elif (pag == 1):
    if (dia <= 15):
        valor = valor * 1.08
    else:
        valor = valor * 1.10
        
if dis > 50:
    valor += 200
else:
    valor += 100

print(f'{valor:.2f}')