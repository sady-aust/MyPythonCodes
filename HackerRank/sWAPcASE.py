s = input()

ans = ""

for c in s:
    if c.islower():
        ans += c.upper()
    elif c.isupper():
        ans += c.lower()
    else:
        ans +=c
print(ans)