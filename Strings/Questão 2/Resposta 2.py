x=int(input())
while x > 0:
    palavra = input()
    y=len(palavra)
    if y > 10:
        print(palavra[0]+str(y-2)+palavra[-1])
        x-=1
    else:
        print(palavra)
        x-=1