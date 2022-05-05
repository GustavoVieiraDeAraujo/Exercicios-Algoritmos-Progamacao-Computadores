dubstep = input()

x = dubstep.split("WUB")
while "" in x:
    x.remove("")

if len(x) == 1:
    y="".join(x)
    print(y)
else:
    y=" ".join(x)
    print(y)