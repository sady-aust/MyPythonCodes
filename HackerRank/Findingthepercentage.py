from decimal import Decimal

mydictionary = {}

n = int(input())

for i in range(n):
    line = input()
    arr = line.split(" ")

    total = 0

    for j in range(1, len(arr)):
        total += Decimal(arr[j])
        #print(total)

    mydictionary[arr[0]] = Decimal(total / (len(arr) - 1))
  #  print(total)

name = input()

print(round(mydictionary.get(name),2))
