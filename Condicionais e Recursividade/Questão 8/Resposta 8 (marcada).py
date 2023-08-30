def jogadas(a,b):
    if a==b:
        print("0")
    elif a>b:
        diferença=a-b
        x=diferença//10
        y=diferença%10
        if y==0:
             print(x)
        else:
             print(x+1)
    else:
        diferença=b-a
        x=diferença//10
        y=diferença%10
        if y==0:
             print(x)
        else:
             print(x+1)
             