n = int(input())
eng = set(input().split(" "))

b = int(input())
french = set(input().split(" "))

ans = eng.union(french)

print(len(ans))
