str = input()
test = input()

count = 0;
for i in range(0, len(str) - (len(test)-1)):
    myStr = ""
    for j in range(i, i + len(test)):
        myStr += str[j]
        if myStr == test:
            count += 1
print(count)
