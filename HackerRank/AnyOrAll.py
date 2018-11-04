# print(any([5 < 6, 6 < 5]))
# print(all([5 < 6, 6 > 5]))

# str = 'Bangladesh'
# print(str[::-1])
def isPalindrome(number):
    numberS = str(number)
    revS = number[::-1]

    return numberS.__eq__(revS)


n = int(input())

numbers = input().split(" ")

intNumbers = list()

for i in numbers:
    intNumbers.append(int(i))

if all(i > 0 for i in intNumbers):
    isAnyIntegerPlaindrome = False
    for j in numbers:
        if isPalindrome(j):
            isAnyIntegerPlaindrome = True
            break
    print(isAnyIntegerPlaindrome)


else:
    print("False")
