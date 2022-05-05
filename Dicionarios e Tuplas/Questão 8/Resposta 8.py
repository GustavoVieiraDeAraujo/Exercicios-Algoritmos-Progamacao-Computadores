def fibonacci(num):
    arr = [0, 1]
    if num == 1:
        print('0')
    elif num == 2:
        print('[0,', '1]')
    else:
        while(len(arr) < num):
            arr.append(0)
        if(num == 0 or num == 1):
            return 1
        else:
            arr[0] = 0
            arr[1] = 1
            for i in range(2, num):
                arr[i] = arr[i-1]+arr[i-2]
            return arr

x = int(input())
posi = [int(i) for i in input().split()]
l1=[]
l2=fibonacci(max(posi))

for elemento in posi:
    l1.append(l2[elemento-1])

print(tuple(l1))

    


