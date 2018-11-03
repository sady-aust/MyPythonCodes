
def solve(s):
    ans = ""

    for i in range(len(s)):
        if i == 0:
            ans += s[i].capitalize()
        elif s[i-1]==' ':
            ans += s[i].capitalize()
        else:
            ans+=s[i]

    return ans

print(solve("asn"))