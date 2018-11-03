a = int(input())
myset = set(input().split(" "))

n = int(input())

for i in range(n):
    op = input().split(" ")
    if op[0].__eq__("intersection_update"):
        demoSet = set(input().split(" "))
        myset.intersection_update(demoSet)
    elif op[0].__eq__("update"):
        demoSet = set(input().split(" "))
        myset.update(demoSet)
    elif op[0].__eq__("symmetric_difference_update"):
        demoSet = set(input().split(" "))
        myset.symmetric_difference_update(demoSet)
    elif op[0].__eq__("difference_update"):
        demoSet = set(input().split(" "))
        myset.difference_update(demoSet)

total = 0
for i in myset:
    total += int(i)

print(total)

