x = int(input())
y = [int(i) for i in input().split()]
w=[]
u = 1
while x > 0:
    w.append(u)
    u+=1
    x-=1

for elemento_1 in w:
    if elemento_1 in y:
        pass
    else:
        for elemento_2 in y:
            z =  y.count(elemento_2)
            if z > 1:
                print(str(elemento_2)+" "+str(elemento_1))
                break