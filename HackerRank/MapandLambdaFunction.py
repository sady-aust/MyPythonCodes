# print(list(map(len,['sady','rupok'])))
# print(list(map(int, ['1', '2'])))

# sum = lambda a,b,c:a+b+c
#
# print(sum(1,2,5))


cube = lambda a:a*a*a

fib = [0,1,1]

n = int(input())

if n == 0:
    print(list())
elif n == 1:
    print(list(map(cube,[0])))
elif n == 2:
    print(list(map(cube, [0,1])))
elif n == 3:
    print(list(map(cube, [0, 1,1])))

elif(n>3):
    for i in range(3,n):
        fib.append(fib[i-1]+fib[i-2])

    print(list(map(cube,fib)))
