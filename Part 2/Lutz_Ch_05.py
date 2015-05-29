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

print(1j * 1J)
print(2 + 1j * 3)
print((2 + 1j) * 3)


## PG 151 Hex, Octal, Binary: Literals and conversions

print(0o1, 0o20, 0o377)             # Octal literals: Base 8, digits 0-7
print(0x01, 0x10, 0xFF)             # Hex literals: Base 16, digits 0-9/A-F
print(0b1, 0b10000, 0b11111111)     # Binary literals: Base 2, digits 0-1

print(0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0)))    # How hex/binary map to decimal
print(0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)))
print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))

print(oct(64), hex(64), bin(64))    # Numbers -> digit strings

print(64, 0o100, 0x40, 0b1000000)
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b1000000', 2))

print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))

print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x, %x. %X' % (64, 64, 255, 255))

print(0o1, 0o20, 0o377)

x = 1                   # 1 decimal is 0001 in bits
print(x << 2)           # Shift left 2 bits: 0100
print(x | 2)            # Bitwise OR (either bit=1): 0011
print(x & 1)            # Bitwise AND (both bits=1: 0001

X = 0b0001              # Binary literals
print(X << 2)           # Shift left
print(bin(X << 2))      # Binary digits string
print(bin(X | 0b010))   # Bitwise OR: either
print(bin(X & 0b1))     # Bitwise AND: both

X = 0xFF                # Hex literals
print(bin(X))
print(X ^ 0b10101010)   # Bitwise XOR: either but not both
print(bin(X ^ 0b10101010))
print(int('01010101', 2))   # Digits=>number: string to int per base
print(hex(85))              # Number=>digits: Hex digit string

X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)
# print(bin(256), (256).bit_length(), len(bin(256) - 2))


import math

print(math.pi, math.e)                      # Common constants
print(math.sin(2 * math.pi / 180))          # Sine, tangent, cosine
print(math.sqrt(144), math.sqrt(2))         # Square root
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)        # Exponential power
print(abs(-42.0), sum((1, 2, 3, 4)))        # Absolute value, summation
print(min(3, 1, 2, 4), max(3, 1, 2, 4))     # Minimum, Maximum

print(math.floor(2.567), math.floor(-2.567))    # Floor (next-lower integer)
print(math.trunc(2.567), math.trunc(-2.567))    # Truncate (drop decimal digits)
print(int(2.567), int(-2.567))                  # Truncate (integer conversion)
print(round(2.567), round(2.467), round(2.567, 2))  # Round
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))       # Round for display

print((1 / 3.0), round(1 / 3.0, 2), ('%.2f' % (1 / 3.0)))

print(math.sqrt(144))           # Module
print(144 ** .5)                # expression
print(pow(144, .5))             # Built-in
print(math.sqrt(1234567890))    # Larger numbers


import random

print(random.random())          # Random floats, integers, choices, shuffles
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of life']))
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of life']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)
random.shuffle(suits)
print(['clubs', 'diamonds', 'hearts', 'spades'])

## PG 157 Decimals
print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.30'))

import decimal

print(decimal.Decimal(1) / decimal.Decimal(7))      # Default: 28 digits
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))      # Fixed precision
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))

print(1999 + 1.33)     # This has more digits in memory than displayed
decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)

decimal.getcontext().prec = 28
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


## PG 160 fractions

from fractions import Fraction
x = Fraction(1, 3)                  # Numerator, Denominator
y = Fraction(4, 6)                  # Simplified to 2, 3 by gcd

print(x)
print(y)

print(x + y)                        # results are exact numerator, denominator
print(x - y)
print(x * y)

print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))
a = 1 / 3.0                         # Only as accurate as floating-point hardware
b = 4 / 6.0                        # Can lose precision over many calculations

print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)

print(0.1 + 0.1 + 0.1 - 0.3)        # Should be zero, close but no exact

print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print(1 / 3)
print(Fraction(1, 3))
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))

print((1 / 3) + (6 / 12))
print(Fraction(6, 12))
print(Fraction(1, 3) + Fraction(6, 12))
print(decimal.Decimal(str(1 / 3)) + decimal.Decimal(str(6 / 12)))
print(1000.0 / 1234567890)
print(Fraction(1000, 1234567890))

print(2.5.as_integer_ratio())         # Float object method

f = 2.5
z = Fraction(*f.as_integer_ratio())     # Convert float->fraction: two args
print(z)                                # Same as Fraction(5, 2)

print(x)
print(x + z)

print(float(x))
print(float(z))
print(float(x + z))
print(17 / 6)
print(Fraction.from_float(1.75))        # Convert float -> fraction: other way
print(Fraction(*1.75.as_integer_ratio()))

print(x)
print(x + 2)                    # Fraction + int -> Fraction
print(x + 2.0)                  # Fraction + float -> Float
print(x + (1. / 3))               # Fraction + float -> Float
print(x + (4. / 3))
print(x + Fraction(4, 3))       # Fraction + Fraction -> Fraction

print(4.0 / 3)
# print(4.0 / 3).as_integer_ratio()

# print(x)
# a = x + Fraction(*(4.0 / 3).as_integer_ratio())
# print(a)
# print(a.limit_denominator(10))

## PG 163 Sets

x = set('abcde')
y = set('bdxyz')

print(x)
print(y)

print(x - y)            # Difference
print(x | y)            # Union
print(x & y)            # Intersection
print(x ^ y)            # Symmetric difference
print(x > y, x < y)     # Superset, subset

print('e' in x)         # Membership
print('e' in 'Camelot', 22 in [11, 22, 33])     # Works with other types as well

z = x.intersection(y)       # Same as x & y
print(z)
z.add('SPAM')               # Insert one item
print(z)
z.update({'X', 'Y'})   # Merge: in-place union
print(z)
z.remove('b')               # Delete one item
print(z)

for item in set('abc'):
    print(item * 3)

S = set([1, 2, 3])
print(S | set([3, 4]))      # Expressions require both to be sets
# print(S | [3, 4])
print(S.union([3, 4]))      # But their methods allow any iterable
print(S.intersection((1, 3, 5)))
print(S.issubset(range(-5, 5)))

print(set([1, 2, 3, 4]))    # Built-in: same as in 2.6
print(set('spam'))          # Add all items in an iterable

print({1, 2, 3, 4})         # Set literals: new in 3.X (and 2.7)
S = {'s', 'p', 'a', 'm'}
S.add('alot')               # Methods work as before
print(S)

S1 = {1, 2, 3, 4}
print(S1 & {1, 3})          # Intersection
print({1, 5, 3, 6} | S1)    # Union
print(S1 - {1, 3, 4})       # Difference
print(S1 > {1, 3})          # Superset

print(S1 - {1, 2, 3, 4})    # Empty sets print differently
print(type({}))             # Because {} is an empty dictionary
S = set()                   # Initialize an empty set
S.add(1.23)
print(S)

print({1, 2, 3} | {3, 4})
# print({1, 2, 3} | [3, 4])
print({1, 2, 3}.union([3, 4]))
print({1, 2, 3}.union({3, 4}))
print({1, 2, 3}.union(set([3, 4])))
print({1, 2, 3}.intersection((1, 3, 5)))
print({1, 2, 3}.issubset(range(-5, 5)))

print(S)
# S.add([1, 2, 3])    # Only immutable objects work in a set
S.add((1, 2, 3))        # NO list or dict, but tuple OK
print(S | {(4, 5, 6), (1, 2, 3)})
print((1, 2, 3) in S)
print((1, 4, 3) in S)
print((4, 5, 6) in S)

print({x ** 2 for x in [1, 2, 3, 4]})       # 3.X/2.7 set comprehension
print({x for x in 'spam'})                  # Same as: set('spam')
print({c * 4 for c in 'spam'})              # Set of collected expression results
print({c * 4 for c in 'spamham'})
S = {c * 4 for c in 'spam'}
print(S | {'mmmm', 'xxxx'})
print(S & {'mmmm', 'xxxx'})

L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
L = list(set(L))                            # Remove duplicates
print(L)
print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))  # But the order may change

print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))
