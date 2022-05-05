x=int(input())

for i in range(0,x):
    y =input()
    if y == "0" or y=="1":
        print("0")
    else:
        while y.startswith("0"):
            y = y[1:]
        while y.endswith("0"):
            y = y[:-1]
        print(y.count("0"))