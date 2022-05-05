n = int(input())
x = 0

while n != 1 and n!=0:
    if n % 2 != 0:
        for i in range(1,n+1):
            y=n-x
            if y == 1:
                print(1)
                n -= 2
                x=0
                break
            else:
                print(f"{y} ", end="")
                x+=2
    elif n% 2 ==0:
        for i in range(1, n+1):
            y = n-x
            if y == 0:
                print(0)
                n -= 2
                x = 0
                break
            else:
                print(f"{y} ", end="")
                x += 2

if n == 1:
    print("1")
else:
    print("0")