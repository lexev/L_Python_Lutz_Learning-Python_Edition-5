__author__ = 'rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 7: String Fundamentals
############################################

title = "Meaning " 'of' " Life"  # Implicit Concatenation
print(title)

print('knight\'s', "knight\"s")  # Escape sequence

s = 'a\nb\tc'
print(s)
print(len(s))

s = 'a\0b\0c'
print(s)
print(len(s))

s = '\001\002\x03'
print(s)
print(len(s))

S = "s\tp\na\x00m"
print(S)
print(len(S))

x = "C:\py\code"  # Keeps \ literally (and displays it as \\)
print(x)

path = r'C:\new\text.dat'
print(path)
print(len(path))

mantra = """Always look
   on the bright
side of life"""
print(mantra)

menu = """spam      # comments here added to string!
    eggs            # ditto
    """
print(menu)

menu = (
    "spam\n"    # comments here ignored
    "eggs\n"    # but newlines not automatic
)
print(menu)

print(len('abc'))           # Length: number of items
print('abc' + 'def')        # Concatenation: a new string
print('Ni!' * 4)            # Repetition

myjob = "hacker"
for c in myjob:
    print(c, end=' ')   # Step through items, print each (3.X form)
print("k" in myjob)                 # Found
print("z" in myjob)                 # Not found
print('spam' in 'abcspamdef')       # Substring search, no position returned

S = 'spam'
print(S[0], S[-2])                  # Indexing from front or end
print(S[1:3], S[1:], S[:-1])        # Slicing: extract a section

S = 'abcdefghijklmnop'
print(S[1:10:2])                    # Skipping items
print(S[::2])
print(S[::-1])                      # Reversing items

S = 'abcedfg'
print(S[5:1:-1])                    # Bounds roles differ

print('spam'[1:3])                  # Slicing Syntax
print('spam'[slice(1, 3)])          # Slice object with index syntax + object
print('spam'[::-1])
print('spam'[slice(None, None, -1)])

print(int("42"), str(42))           # Convert from/to string
print(repr(42))                     # Convert to as-code string

print(str('spam'), repr('spam'))

S = "42"
I = 1
# print(S + I)
print(int(S) + I)                   # Force addition
print(S + str(I))                   # Force concatenation

print(str(3.1415), float("1.5"))
text = "1.234E-10"
print(float(text))                  # Show more digits before 2.7 and 3.1

print(ord('s'))
print(chr(115))
S = '5'
S = chr(ord(S) + 1)
print(S)
S = chr(ord(S) + 1)
print(S)
print(int('5'))
print(ord('5') - ord('0'))

B = '1101'                          # Convert binary digits to integer with ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

print(int('1101', 2))               # Convert binary to integer: Built-in
print(bin(13))                      # Convert integer to binary: Built-in

S = 'spam'
# S[0] = 'x'
S = S + 'SPAM!'
print(S)
S = S[:4] + "Burger" + S[-1]
print(S)

S = 'splot'
S = S.replace('pl', 'pamal')
print(S)

print('That is %d %s bird!' % (1, 'dead'))          # Format expression: all pythons
print('That is {0} {1} bird!'.format(1, 'dead'))    # Format method in 2.6, 2.7, 3.X

S = 'spam'
result = S.find('pa')               # Call the find method to look for 'pa' in string S
print(result)

S = 'spammy'
S = S[:3] + 'xx' + S[5:]        # Slice sections from s
print(S)

S = 'spammy'
S = S.replace('mm', 'xx')       # Replace all mm with xx in S
print(S)
print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')          # search for position
print(where)                    # occurs at offset 4
S = S[:where] + 'EGGS' + S[(where + 4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))        # Replace all
print(S.replace('SPAM', 'EGGS', 1))     # Replace one

S = 'spammy'
L = list(S)
print(L)

L[3] = 'x'
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)

line = 'bob,hacker,40'
print(line.split(','))
line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))
line = "The knights who say Ni!\n"
print(line)
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))

print(line)
print(line.find('Ni') != -1)
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))
print(line[-len(sub):] == sub)

S = 'a+b+c+'
x = S.replace('+', 'spam')
print(x)

print('That is %d %s bird!' % (1, 'dead'))                  # Format Expression
exclamation = 'Ni!'
print('The knight who says %s!' % exclamation)              # String substitution
print('%d %s %g you' % (1, 'spam', 4.0))
print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))          # All types match a %s target

x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)

x = 1.23456789
print(x)
print('%e | %f | %g' % (x, x, x))
print('%E' % x)
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print('%s' % x, str(x))
print('%f, %.2f, %.*f' % (1 / 3.0, 1 / 3.0, 4, 1 / 3.0))

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}                 # Build up values to substitute
print(reply % values)                               # Perform substitutions

food = 'spam'
qty = 10
print(vars())

print('%(qty)d more %(food)s' % vars())             # Variables are keys in words

template = '{0}, {1} and {2}'                       # By position
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'             # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'                # By both
print(template.format('spam', motto='spam', food='eggs'))

template = '{}, {} and {}'                          # By relative position
print(template.format('spam', 'ham', 'eggs'))              # new in 3.1 and 2.7

template = '%s, %s and %s'
print(template % ('spam', 'ham', 'eggs'))

template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))

print('{motto}, {0} and {food}'.format(42, motto=3.14, food='eggs'))

X = '{motto}, {0} and {food}'.format(43, motto=3.14, food=[1, 2])
print(X)

print(X.split(' and '))

Y = X.replace('and', 'but under no circumstances')
print(Y)

import sys

print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

somelist = list('SPAM')
print(somelist)

print('first={0[0]}, third={0[2]}'.format(somelist))
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))  # fails in fmt
parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))

print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:<10}'.format('spa,', 123.4567))
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{:10} = {:10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{.platform:>10} = {[kind]:>10}'.format(sys, dict(kind='laptop')))

print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))      # Hex, octal, binary
print(bin(255), int('11111111', 2), 0b11111111)         # Other to/from binary
print(hex(255), int('FF', 16), 0xFFF)                   # Other to/from hex
print(oct(255), int('377', 8), 0o277)                   # Other to/from octal in 3.X

print('{0:.2f}'.format(1 / 3.0))                        # Parameters hardcoded
print('%.2f' % (1 / 3.0))                               # Ditto for expression
print('{0:.{1}f}'.format(1 / 3.0, 4))                   # Take value from arguments
print('%.*f' % (4, 1 / 3.0))                            # Ditto for expression

print('{0:.2f}'.format(1.2345))                         # String method
print(format(1.2345, '.2f'))                            # Built-in function
print('%.2f' % 1.2345)                                  # Expression

print('%s=%s' % ('spam', 42))                           # Format expression in all 2.X/3.X
print('{0}={1}'.format('spam', 42))                     # Format method in 3.0+ and 2.6+
print('{}={}'.format('spam', 42))                       # With auto-numbering in 3.1+ and 2.7

print('%s, %s and %s' % (3.14, 42, [1, 2]))
print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})
print('My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform))
somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first=%s, last=%s, middle=%s' % parts)

print('%-10s = %10s' % ('spam', 123.4567))
print('%10s = %-10s' % ('spam', 123.4567))
print('%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop'))
print('%e, %.3e, %g' % (3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
print('%x, %o' % (255, 255))

print('My {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'}))
print('My %(kind)-8s runs %(plat)8s)' % dict(kind='laptop', plat=sys.platform))

data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
print('My %(kind)-8s runs %(platform)8s' % data)

print('{0:b}'.format((2 ** 16) - 1))            # Expression (only) binary format code
print(bin((2 ** 16) - 1))                       # But other more general options work too
print('%s' % bin((2 ** 16 - 1)))                 # Usable with method and % expression
print('{}'.format(bin((2 ** 16) - 1)))           # With 2.7/3.1+ relative numbering
print('%s' % bin((2 ** 16) - 1))                # Slice off 0b to get exact equivalent

print('{:,d}'.format(999999999999))              # New str format method feature in 3.1/2.7
# print('%s' % commas(999999999999))              # But % is the same with simple 8-line function

print('{name} {job} {name}'.format(name='Bob', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))
D = dict(name='Bob', job='dev')
print('{0[name]} {0[job]} {0[name]}'.format(D))     # Method, key references
print('{name}, {job} {name}'.format(**D))           # Method, dict-to-args
print('%(name)s %(job)s %(name)s' % D)              # Expression, key references

print('The {0} side {1} {2}'.format('bright', 'of', 'life'))
print('The {} side {} {}'.format('bright', 'of', 'life'))
print('The %s side %s %s' % ('bright', 'of', 'life'))

print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))
print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))

print('%.2f' % 1.2345)                  # Single value
print('%.2f %s' % (1.2345, 99))         # Multiple values tuple

print('%s' % 1.23)                      # Single value by itself
print('%s' % (1.23,))                   # Single value that is a tuple
print('%s' % ((1.23,),))                # Single value that is a tuple

print('{0:.2f}'.format(1.2345))             # Single value
print('{0:.2f} {1}'.format(1.2345, 99))     # Multiple values
print('{0}'.format(1.23))                   # Single value, by itself
print('{0}'.format((1.23,)))                # Single value that is a tuple


def myformat(fmt, args):
    return fmt % args

print(myformat('%s %s', (88, 99)))          # Call your function object
print(str.format('{} {}', 88, 99))          # Versus calling the built-in


### PG 137 Test Your Knowledge

### 1. Can the string find method be used to search a list?
""" No because methods are always type-specific; that is, they only work on a single data
    type. Expression like X+Y and built-in functions like len(X) are generic, though,
    may work on a variety of types. In this case, for instance, the in membership
    expression has a similar effect as the string find, but it can be used to search both
    strings and lists. In Python 3.X, there is some attempt to group methods by categories
    (for example, the mutable sequence types list, and bytearray have similar method sets),
    but methods are still more type-specific than other operation sets.
"""

### 2. Can a string slice expression be used on a list?
""" Yes. Unlike methods, expressions are generic and apply to many types. In this case,
    the slice expression is really a sequence operation -- it works on any type of sequence
    object, including strings, lists, and tuples.The only difference is that when you slice
    a list, you get back a new list.
"""

### 3. How would you convert a character to its ASCII integer code? How would you convert
###     the other way. from integer to character?
""" The built-in ord(S) function converts from a one-character string to an integer
    character code; chr(I) converts from the integer code back to a string. Keep in mind,
    though, that these integers are only ASCII codes for text whose characters are drawn
    only from ASCII character set. In the Unicode model, text strings are really sequences
    of unicode point identifying integers, which may fall outside the 7-bit range reserved
    by ASCII
"""

### 4. How might one go about changing a string in Python?
""" Strings cannot be changed; they are immutable. However, you can achieve a similar effect
    by creating a new string--by concatenating, slicing, running formatting expressions, or
    using a method call like replace--andtehn assigning the result back to the original
    variable name.
"""

### 5. Given a string S with the value "s,pa,m", name two ways to extract the two
###     characters in the middle.
""" You can slice the string using S[2:4], or split on the comma and index the string using
    S.split(',')[1].
"""

### 6. How many characters are there in the string "a\nb\x1f\000d"?
""" Six. The string"a\nb\x1f\00d"contains the characters a, newline(\n), b, binary 31
    (a hex escape \x1f), binary 0 (an octal escape \000) and d.
"""

### 7. Why might you use the sting module instead of string method calls?
""" You should never use the string module instead of string object method calls today--
    it's deprecated, and its calls are removed completely in Python 3.X. The only valid
    reason for using string module at all today is for its other tools. such as predefined
    constants. You might also see it appear in what is now very old and dusty Python code
    (and books of misty past -- like the 1990s
"""
