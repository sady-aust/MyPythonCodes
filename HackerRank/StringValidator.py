n = input()

hasAnyAlphanumeric = False
hasAnyAlphabeticalChar = False
hasAnyDegit = False
hasAnyLowerCaseLtr = False
hasAnyUpperCaseLtr = False

for c in n:
    if c.isalnum():
        hasAnyAlphanumeric = True
    if c.isalpha():
        hasAnyAlphabeticalChar = True
    if c.isdigit():
        hasAnyDegit = True
    if c.islower():
        hasAnyLowerCaseLtr = True
    if c.isupper():
        hasAnyUpperCaseLtr = True

print(hasAnyAlphanumeric)
print(hasAnyAlphabeticalChar)
print(hasAnyDegit)
print(hasAnyLowerCaseLtr)
print(hasAnyUpperCaseLtr)