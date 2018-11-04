import math
import cmath
num = complex(input())

r = math.sqrt((num.real*num.real)+(num.imag*num.imag))

p = cmath.phase(complex(num.real,num.imag))

print(r)
print(p)