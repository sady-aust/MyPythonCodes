s = input()
w = int(input())

i = 0
ans = ""
while i < len(s):
    if len(ans) == w:
        print(ans)
        ans = ""
    else:
        ans += s[i]
        i +=1


if len(ans) > 0:
    print(ans)
