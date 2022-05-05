a= input()
b= input()
x = 0
y =len(a)

for i in range(0,y):
    if a[x] == b[x]:
        y-=1
        x+=1
    else:
        x+=1

print(y)