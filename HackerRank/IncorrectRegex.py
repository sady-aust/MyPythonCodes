import re
t = int(input())
isValid = False
for i in range(t):
    reg = input()

    try:
        re.compile(reg)
        isValid = True
    except Exception as e:
        isValid = False

    print(isValid)