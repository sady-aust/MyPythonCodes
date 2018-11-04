# import itertools
#
# print(list(itertools.permutations([1,2,3])))
# print(list(itertools.permutations([1,2,3], 2)))#print all 2 length permutations
# print(list(itertools.permutations('abc',2)))

import itertools

myIn = input().split(" ")

myList = list(myIn[0])
myList.sort()

allComb = list(itertools.permutations(myList,int(myIn[1])))

for aItem in allComb:
    ans = ""
    for ch in aItem:
        ans += ch
    print(ans)