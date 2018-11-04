# import itertools
# # print(list(itertools.combinations_with_replacement('12345',2)))
# #
# A = [1, 2,3]
# print(list(itertools.combinations(A,2)))

import itertools

myIn = input().split(" ")
myList = list(myIn[0])
myList.sort()

ansList = list(itertools.combinations_with_replacement(myList,int(myIn[1])))

for aItem in ansList:
    ans = ""
    for c in aItem:
        ans +=c
    print(ans)
