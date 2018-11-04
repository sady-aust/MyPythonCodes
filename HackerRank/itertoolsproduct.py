# import itertools
# print(list(itertools.product([1, 2, 3], repeat=3)))
# print(list(itertools.product([1, 2, 3], [3,4])))
#
# A =[
#     [1, 2, 3], [3, 4, 5]
# ]
# print(list(itertools.product(*A)))
#
# B = [[1, 2, 3], [3, 4, 5], [7, 8]]
# print(list(itertools.product(*B)))


import itertools

a = input().split(" ")
b = input().split(" ")

aList = []
bList = []

for i in a:
    aList.append(int(i))

for i in b:
    bList.append(int(i))



print(*itertools.product(aList, bList))
