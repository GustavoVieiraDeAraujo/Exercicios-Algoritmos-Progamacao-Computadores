l1=[]
l2=[]
l3=[]
x = 0

for i in range(0,10):
    entrada = int(input())
    l1.append(entrada)

for i in range(0,5):
    tuple_1 = (l1[x], l1[5+x])
    l2.append(tuple_1)
    x+=1

for tupla in l2:
    media = sum(tupla)/len(tupla)
    l3.append(media)

print(l2)
print(l3)