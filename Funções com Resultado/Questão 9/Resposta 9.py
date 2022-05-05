def pattern1(x):
    if x<=0:
        return
    elif x%2 == 0:
        print (x)
        return pattern(x-5)
    elif x%2 != 0:
        print (x)
        return pattern(x-((x+1)//2))
    
def pattern(x):
    pattern1(x)
    print(x)