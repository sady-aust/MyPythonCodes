# n = input()
# lis = n.split(" ")
# newList = list(map(int, lis))
# print(newList)

# list = [1,5,6,6]
# myset = set(list)
#
# print(myset)

# a = {2, 4, 5, 9}
# b = {2, 4, 11, 12}
#
# print(a.difference(b) ==a.difference(b))

m = input()
mlis = input().split(" ")
mList = list(map(int,mlis))

n = input()
nlis = input().split(" ")
nList = list(map(int,nlis))

mSet = set(mList)
nSet = set(nList)

a = mSet.difference(nSet)
b = nSet.difference(mSet)

aList = list(a)
bList = list(b)

for i in range(len(bList)):
    aList.append(bList[i])

aList.sort()

for i in range(len(aList)):
    print(aList[i])