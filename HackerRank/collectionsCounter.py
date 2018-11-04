# import collections
# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(collections.Counter(myList))
#
# print(collections.Counter(myList).items())
#
# print(collections.Counter(myList).keys())
# print(collections.Counter(myList).values())

import collections

x = int(input())
shoeSize = input().split(" ")

myMap = collections.Counter(shoeSize)

n = int(input())

shoes = myMap.keys()

total = 0
for i in range(n):
    q = input().split(" ")
    if shoes.__contains__(q[0]):
        if myMap.get(q[0])>0:
            total += int(q[1])
            myMap[q[0]] = myMap.get(q[0])-1


print(total)