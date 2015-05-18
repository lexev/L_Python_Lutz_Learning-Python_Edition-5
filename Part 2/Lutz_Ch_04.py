__author__ = 'Rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 4: Intro Python Object Types PG 90
############################################

###	PG 97 Numbers

print(123 + 222)    # Integer addition
print(1.5 * 4)      # Floating-point multiplication
print(2 ** 100)     # 2 to the power of 100, again

print(len(str(2 ** 1000000)))   # How many digits are in this really big number


import math

print(math.pi)
print(math.sqrt(85))


import random

print(random.random())
print(random.choice([1, 2, 3, 4]))


### PG 99 Strings

S = "Spam"          # Make a 4-character string, and assign it to the name S
print(len(S))       # Find the Length
print(S[0])         # First item in S, indexing by zero-based position
print(S[1])         # The Second item from the left

print(S[-1])        # The last item from the end
print(S[-2])        # The second-to-last item from the end
print(S[len(S) - 1])    # Negative indexing the hard way

print(S[1:3])       # Slice of S from offsets 1 through 2 (not 3)
print(S[1:])        # Everything past the first (1:len(S))
print(S[0:3])       # Everything but the last
print(S[:3])        # Same as S[0:3]
print(S[:-1])       # Everything but the last again, but simpler (0:-1)
print(S[:])         # All of S as a top-level copy (0:len(S))

print(S + "xyz")    # Concatenation
print(S * 8)        # Repetition
print(S)            # S does not change


### PG 101 immutability

# S[0] = "z"          # Immutable objects cannot be changed
S = "z" + S[1:]     # But we can run expressions to make new objects
print(S)

S = "shrubbery"     # Assign new s
L = list(S)         # Expand into list
print(S)
print(L)
L[1] = 'c'          # Change it in place
''.join(L)          # Join with empty delimiter

B = bytearray(b"spam")  # A bytes/list hybrid
B.extend(b"eggs")
print(B)                # B[i] = ord(c)  works here too
print(B.decode())       # Translate to normal string


### PG 102 Type-Specific Methods

S = "Spam"
print(S.find("pa"))             # Find the offset of a substring in S
print(S.replace("pa", "XYZ"))   # Replace occurrences of a string in S with another
print(S)                        # Replace method creates new str, doesn't change old one

line = "aaa,bbb.ccccc,dd"
print(line.split(","))          # Split on a delimiter into a list of sub-strings

S = "spam"
print(S.upper())                # Upper-case conversion
print(S.lower())                # Lower-case conversion
print(S.isalpha())              # Content tests: isalpha, isdigit, etc.

line = "aaa,bbb,ccccc,dd\n"
print(line)
print(line.rstrip())                    # Remove trailing whitespace characters
print(line.rstrip().split(","))         # Combine the two operations

print("%s, eggs, and %s" % ("spam", "SPAM!"))       # Formatting expression
print('{}, eggs, and {}'.format("spam", "SPAM!"))   # Formatting method

print("{:,.2f}".format(296999.2567))    # Separators, decimal digits
print("%2f | %+05d" % (3.14159, - 42))  # Digits, padding, signs

print(S + "NI!")
print(S.__add__("NI!"))


### PG 105 Other ways to Code Strings

S = "A\nB\tC"           # \n is end-of-line, \t is tab
print(S)
print(len(S))           # Each stands for just one character
ord("\n")               # \n is a byte with the binary value 10 in ASCII

S = "A\0B\0C"           # \0, a binary zero byte, does not terminate string
print(S)
print(len(S))

msg = """
aaaaaaaaaaaaa
bbb'''bbbbbbbbbb""bbbbbbb'bbbb
ccccccccccccc
"""
print(msg)


### PG 106 Unicode strings

print("sp\xc4m")        # normal str strings are Unicode text
print(b"a\x01c")        # bytes stings are byte-based data
print(u"sp\u00c4m")

print('spam')                   # Characters may be 1, 2 or 4 bytes in memory
print("spam".encode("utf8"))    # Encoded to 4 bytes in UTF-8 files
print("spam".encode("utf16"))   # Encoded to 10 bytes in UTF-16

print("sp\xc4\u00c4\U000000c4m")

print("\u00A3", "\u00A3".encode("latin1"), b"\xA3".decode("latin1"))

print(u"x" + "y")
print("x" + b"y".decode())      # Bytes and Str cannot be combined in 3.X
print("x".encode() + b"y")      # Without explicit conversion


import re

match = re.match("Hello[ \t]*(.*)world", "Hello     Python world")
print(match.group(1))

match = re.match("[/:](.*)[/:](.*)[/:](.*)", "/usr/home:lumberjack")
print(match.groups())
print(re.split("[/:]", "/usr/home/lumberjack"))


### PG 109 Lists

L = [123, "spam", 1.23]     # A list of three different-type objects
print(len(L))               # Number of items in the list

print(L[0])                 # Indexing by position
print(L[:1])                # Slicing a list returns a new list
print(L + [4, 5, 6])        # Concat/repeat makes new lists too
print(L * 2)                # But the original list is unchanged

L.append("NI")              # Add and object at end of list
print(L)
print(L.pop(2))             # delete and return 3rd item
print(L)                    # "del L[2]" deletes from a list too without returning anything

M = ["bb", "aa", "cc"]
M.sort()
print(M)
M.reverse()
print(M)

M = [[1, 2, 3],                     # A 3 x 3 matrix, as nested lists
     [4, 5, 6],                     # Code can span lines if bracketed
     [7, 8, 9]]
print(M)
print(M[1])                         # Get row 2
print(M[1][2])                      # Get row 2, then get item 3 within the row

col2 = [row[1] for row in M]        # Collect the items in column 2
print(col2)                         # but the matrix is unchanged
print([row[1] + 1 for row in M])    # Add 1 to each item in column 2
print([row[1] for row in M if row[1] % 2 == 0])     # filter out odd items

diag = [M[i][i] for i in [0, 1, 2]]         # Collect a diagonal from matrix
print(diag)

doubles = [c * 2 for c in "spam"]           # Repeat characters in a string
print(doubles)

print(list(range(4)))
print(list(range(-6, 7, 2)))
print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

G = (sum(row) for row in M)         # Create a generator of row sums
print(next(G))                      # Run the iteration protocol next
print(next(G))
print(next(G))

print(list(map(sum, M)))            # Map sum over items in M

print({sum(row) for row in M})              # Create a set of row sums
print({i: sum(M[i]) for i in range(3)})     # Create key/value table with row of sums

print([ord(x) for x in "spaam"])            # List of character ordinals
print({ord(x) for x in "spaam"})            # Sets remove duplicates
print({x: ord(x) for x in "spaam"})         # Dictionary keys are unique
print((ord(x) for x in "spaam"))            # Generator of values


### PG 113 Dictionaries

D = {"food": "spam", "quantity": 4, "color": "pink"}
print(D["food"])                            # Fetch value of key food
D["quantity"] += 1                          # Add 1 tto "quantity" value
print(D)

D = {}
D["name"] = "Bob"                           # Create keys by assignment
D["job"] = "dev"
D["age"] = 40
print(D)
print(D["name"])

bob1 = dict(name="Bob", job="dev", age=40)
print(bob1)
bob2 = dict(zip(["name", "job", "age"], ["Bob", "dev", 40]))
print(bob2)

rec = {"name": {"first": "Bob", "last": "Smith"},
       "jobs": ["dev", "mgr"],
       "age": 40.5}
print(rec)
print(rec["name"])                  # 'name' is a nested dictionary
print(rec["name"]["last"])          # Index the nested dictionary
print(rec["jobs"])                  # 'jobs is a nested list
print(rec["jobs"][-1])              # Index the nested list
rec["jobs"].append("janitor")       # Expand the list
print(rec["jobs"])

rec = 0                             # Now the object's space is reclaimed

D = {"a": 1, "b": 2, "c": 3}
print(D)
D["e"] = 99
print(D)

print("f" in D)
if "f" not in D:
    print("missing")
if "f" not in D:
    print("missing")
    print("no, really")

value = D.get("x", 0)                       # Index but with a default
print(value)
value = D["x"] if "x" in D else 0           # if/else expression form
print(value)

Ks = list(D.keys())                         # Unordered keys list
print(Ks)
Ks.sort()                                   # Sorted keys list

for key in Ks:                              # Iterate through sorted keys
    print(key, "=>", D[key])

for key in sorted(D):
    print(key, "=>", D[key])

for c in "spam":
    print(c.upper())

x = 4
while x > 0:
    print("spam!" * x)
    x -= 1

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares = []
for x in [1, 2, 3, 4, 5]:           # This is what a list comprehension does
    squares.append(x ** 2)          # Both run the iteration protocol internally
print(squares)


### PG 121 Tuples

T = (1, 2, 3, 4)                    # A 4-item tuple
print(len(T))                       # Length
print(T + (5, 6))                   # Concatenation
print(T[0])

T.index(4)                          # Tuple methods: 4 appears at offset 3
T.count(4)                          # 4 appears once

T = (2,) + T[1:]                    # Make a new tuple for a new value
print(T)

T = "spam", 3.0, [11, 22, 33]
print(T)
print(T[1])
print(T[2][1])


### PG 122 Files

f = open("data.txt", "w")           # Make a new file in output mode ("w" is write)
f.write("Hello\n")                  # Write strings of characters into ir
f.write("world\n")                  # It returns the number of items written
f.close()                           # Close to flush output buffers to disk

f = open("data.txt")                # 'r' (read) is the default processing mode
text = f.read()                    # Read entire file into a string
print(text)
print(text.split())

for line in open("data.txt"):
    print(line)


### PG 123 Binary Byte Files

import struct
packed = struct.pack(">i4sh", 7, b"spam", 8)    # Create packed binary data
print(packed)                                   # 10 bytes, not objects or text

file = open("data.bin", "wb")                   # Open binary output file
file.write(packed)                              # Write packed binary data
file.close()

data = open("data.bin", "rb").read()            # Open/read binary data file
print(data)                                     # 10 bytes unaltered
print(data[4:8])                                # Slice bytes in the middle
print(list(data))                               # A sequence of 8-bit bytes
print(struct.unpack(">i4sh", data))             # Unpack into objects again


### PG 124 Unicode Text Files
S = "sp\xc4m"                                   # Non-ASCII Unicode text
print(S)                                        # Sequence of characters
print(S[2])
file = open("unidata.txt", "w", encoding="utf-8")
file.write(S)
file.close()

text = open("unidata.txt", encoding="utf-8").read()     # Read/decode UTF-8 text
print(text)
print(len(text))

raw = open("unidata.txt", "rb").read()                  # Read raw encoded bytes
print(raw)
print(len(raw))

print(text.encode("utf-8"))         # Manual encode to bytes
print(raw.decode("utf-8"))          # Manual decode to string

print(text.encode("latin-1"))
print(text.encode("utf-16"))
print(len(text.encode("latin-1")), len(text.encode("utf-16")))

X = set("spam")                 # Make a set out of a sequence
Y = {"h", "a", "m"}             # Make a set with literals
print(X, Y)

print(X & Y)                    # Intersection
print(X | Y)                    # Union
print(X - Y)                    # Difference
print(X > Y)                    # Superset

print({n ** 2 for n in [1, 2, 3, 4]})   # Set comprehension

print(list({1, 2, 1, 3, 1}))        # Filter out duplicates
print(set("spam") - set("ham"))     # Finding differences in collections
print(set("spam") == set("asmp"))   # Order-neutral equality tests

print("p" in set("spam"), "p" in "spam", "ham" in ["eggs", "spam", "ham"])

print(1 / 3)
print((2 / 3) + (1 / 2))


import decimal                      # Decimals:fixed precision

d = decimal.Decimal("3.141")
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))


from fractions import Fraction  # Fractions: numerator+denominator
f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))

print(1 > 2, 1 < 2)             # Booleans
print(bool("spam"))             # Object's Boolean value

X = None                        # None placeholder
print(X)
L = [None] * 100                # Initialize a list of 100 Nones
print(L)

print(type(L))                  # types are classes
print(type(type(L)))            # Even types are objects

if type([]) == type(L):         # Type testing
    print("yes")

if type(L) == list:             # Using the type name
    print("yes")

if isinstance(L, list):         # Object-oriented tests
    print("yes")


### PG 129 User-Defined Classes

class Worker:

    def __init__(self, name, pay):      # Initialize when created
        self.name = name                # self is the new object
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker("Bob Smith", 50000)    # Make two instances
sue = Worker("Sue Jones", 60000)    # Each has name and pay attrs
print(bob.last_name())
print(sue.last_name())
sue.give_raise(.10)
print(sue.pay())

### 1. Name four of Python's core data types.
""" Numbers, strings, lists, dictionaries, tuples, files, and sets are generally considered
    to be the core object (data) types. Types, None, Booleans, are sometimes classified this
    way as well. There are multiple number types (integer, floating point, complex, fraction,
    and decimal) and multiple string types (simple strings, and Unicode strings in Python 2.X,
    and text strings and byte strings in Python 3.X
"""

### 2. Why are they called "core" data types?
""" They are known as "core" types because they are a part of the Python language itself and
    are always available; to create other objects, you generally must call functions in
    imported modules. Most of the core types have specific syntax for generating the objects:
    'spam' for example, is an expression that makes a string and determines the set of
    operations that can be applied to it. Because of this core types are hardwired into
    Python's syntax. In contrast, you must call the built-in open function to create a file
    object (even though this is usually considered a core type too).
"""

### 3. What does "immutable" mean, and which of the three of Python's core types are considered immutable
""" An "immutable" object is an object that cannot be changed after it is created. Numbers,
    strings, and tuples in Python fall into this category. While you cannot change an immutable
    object in place, you can always make a new one by running an expression. Bytearrays in recent
    Pythons offer mutability for text, but they are not normal strings, and only apply directly to
    text if it's a simple 8-bit kind (e.g. ASCII)
"""

### 4. What does "sequence" mean, and which three types fall into this category?
""" A "sequence" is a positionally ordered collection of objects. Strings, lists, and tuples are
    all sequences in Python. They share common sequence  operations, such as indexing, concatenation,
    slicing, but also have type-specific method calls. A related term, "iterable", means either a
    physical sequence, or virtual one that produces items upon request.
"""

### 5. What does "mapping" mean, and which core type is a mapping
""" The term "mapping" denotes an object that maps keys to associated values. Python's dictionary is the
    only mapping type in the core type set. Mappings do not maintain any left-to-right positional ordering
    they support access to data stored by key, plus type-specific method calls.
"""

### 6. What is "polymorphism", and why should you care?
""" "Polymorphism" means that the meaning of an operation (like a+) depends on the objects being operated on.
    This turns out to be a key idea (perhaps the key idea) behind using python as well -- not constraining code
    to specific types makes that code automatically applicable to many types.
"""
