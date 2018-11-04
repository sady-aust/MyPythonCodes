A = set(input().split(" "))

n = int(input())

isAll = True

for i in range(n):
    otherSet = set(input().split())

    if otherSet.issubset(A):
        count = 0

        for j in A:
            if not otherSet.__contains__(j):
                count += 1

        if count == 0:
            isAll = False

    else:
        isAll = False

print(isAll)
