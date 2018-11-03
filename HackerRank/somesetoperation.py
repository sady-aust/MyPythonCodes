n = int(input())
nlis = input().split(" ")
nset = set(map(int, nlis))

noOp = int(input())

for i in range(noOp):
    operation = input()
    if operation.__eq__("pop"):
        nset.pop()
    else:
        opArr = operation.split(" ")
        if opArr[0].__eq__("remove"):
            nset.remove(int(opArr[1]))
        elif opArr[0].__eq__("discard"):
            nset.discard(int(opArr[1]))

print(sum(nset))

