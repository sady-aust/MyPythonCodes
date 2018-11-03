n = int(input())
eng = set(input().split(" "))

b = int(input())
french = set(input().split(" "))

print(len(eng.symmetric_difference(french)))