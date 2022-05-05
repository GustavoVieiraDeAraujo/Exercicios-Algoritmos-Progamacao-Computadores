e1 = input()
e2 = input()

l1 = e1.split()
l2 = e2.split()

d1 = {}
x=0

for i in range(0,len(l1)):
    d1[l1[x]]=l2[x]
    x+=1

print(d1)