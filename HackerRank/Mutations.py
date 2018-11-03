myString = input();
arr = input().split(" ")

charList = list(myString)
charList[int (arr[0])] = arr[1]

ans = ""
for c in charList:
    ans +=c

print(ans)

