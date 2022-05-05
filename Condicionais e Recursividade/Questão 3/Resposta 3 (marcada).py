x,y,z=input().split()

a=int(x)
b=int(y)
c=int(z)

if c==0 and a>350: 
    valorParcela=a/b
    valorDoDesconto=a%b
    valorAPagar=a-valorDoDesconto
    print("Eba! Você ganhou",valorDoDesconto,"reais de desconto!")
if c==0 and a<350:
    valorParcela=a/b
    valorDoDesconto=a%b
    print("Por favor, pague",valorDoDesconto,"reais para prosseguir com o parcelamento")
if c==1:
    valorParcela=a/b
    valorDoDesconto=a%b
    valorAPagar=a-valorDoDesconto
    print("Eba! Você ganhou",valorDoDesconto,"reais de desconto!")