t = int(input())

for i in range(t):
    aN = int(input())
    a = set(input().split(" "))

    bN = int(input())
    b = set(input().split(" "))

    if a.issubset(b):
        print("True")
    else:
        print("False")



