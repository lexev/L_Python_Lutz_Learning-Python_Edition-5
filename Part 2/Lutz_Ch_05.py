__author__ = 'Rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 5: Numeric Types PG 133
############################################

print(40 + 3.14)        # Integer to float, float math/result
print(int(3.1415))      # Truncates float to integer
print(float(3))         # Converts integer to float

a = 3
b = 4

print(a + 1, a - 1)     # Addition (3 + 1), subtraction (3 - 1)
print(b * 3, b / 2)     # Multiplication (4 * 3), division (4 / 2)
print(a % 2, b ** 2)    # Modulus (remainder), power(4 ** 2)
print(2 + 4.0, 2.0 ** b)    # Mixed type conversions
print(b / 2 + a)
print(b / (2.0 + a))
print(1 / 2.0)
num = 1 / 3.0
print(num)
print("%e" % num)       # String formatting expression
print("%4.2f" % num)    # Alternate floating point expression
print("{0:4.2f}".format(num))   # String formatting method: Python 2.6, 3.0, and later

print(repr("spam"))
print("spam")

print(1 < 2)            # Less than
print(2.0 >= 1)         # Greater than or equal
print(2.0 == 2.0)       # Equal value
print(2.0 != 2.0)       # Not Equal value

X, Y, Z, = 2, 4, 6

print(X < Y < Z)        # Chained comparisons, range test

print(X < Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)
print(1 == 2 < 3)       # Same as 1 == 2 and 2 < 3, eval to False
print(False < 2)        # Means 0 < 3, which is True

print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))

print(10 / 4)
print(10 / 4.0)
print(10 // 4)
print(10 // 4.0)


import math

print(math.floor(2.5))      # Closest number below value
print(math.floor(-2.5))
print(math.trunc(2.5))      # Truncate fractional part(toward zero)
print(math.trunc(-2.5))

print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)
print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)

print(5 / -2)                   # keep remainder
print(5 // -2)                  # Floor blow result
print(math.trunc(5 / -2))       # Truncate instead of floor

print((5 / 2), (5 / 2.0), (5 / -2.0), (5 / -2))
print((5 // 2), (5 // 2.0), (5 // -2.0), (5 // -2))
print((9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0))
