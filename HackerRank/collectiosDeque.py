# from collections import deque
#
# d = deque()
# d.append(1)
# print(d)
# d.appendleft(2)
# print(d)
# d.clear()
# print(d)
# d.extend('1')
# d.extend('2')
# d.extendleft('23')
# print(d)
# print(d.count('2'))
# print(d.pop())
# print(d.popleft())
# print(d)

from collections import deque
n = int(input())

myDeque = deque()

for i in range(n):
    op = input().split(" ")
    if op[0].__eq__("append"):
        myDeque.append(int(op[1]))
    elif op[0].__eq__("pop"):
        myDeque.pop()

    elif op[0].__eq__("popleft"):
        myDeque.popleft()

    elif op[0].__eq__("appendleft"):
        myDeque.appendleft(int(op[1]))
ans =""
for i in range(myDeque.__len__()):
    ans += str(myDeque[i])+" "
print(ans.strip())