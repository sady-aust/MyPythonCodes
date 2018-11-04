# print(list(zip([1,2,3,4,5,6],'HACKE')))
nx = input().split(" ")

myList = list()
for i in range(int(nx[1])):
    numbers = input().split(" ")
    myList.append(numbers)


for i in range(int(nx[0])):
    total = 0
    for j in range(int(nx[1])):
        total += float(myList[j][i])
    print(total/int(nx[1]))