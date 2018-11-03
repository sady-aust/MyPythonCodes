k = int(input())

arr = str(input()).split(" ")

mySet = set(arr)

groupMemberSize = int(len(arr) / k)

isfound = False;
for i in mySet:
    count = 0

    for j in range(len(arr)):
        if i == arr[j]:
            count += 1

    if count < k or count > k:
        print(i)
        isfound = True
        break

if not isfound:
    print("NO")