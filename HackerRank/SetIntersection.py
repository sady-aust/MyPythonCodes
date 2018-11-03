n = int(input())
english = set(input().split(" "))

b = int(input())
french = set(input().split(" "))

print(len(english.intersection(french)))