__author__ = 'rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 9: Tuples, Files, and Everything Else
############################################

print((1, 2) + (3, 4))
print((1, 2) * 4)
T = (1, 2, 3, 4)
print(T[0], T[1:3])

x = (40)            # An integer!
print(x)

y = (40,)           # A tuple containing an integer
print(y)

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)                   # Make a list from a tuple's items
tmp.sort()                      # Sort the list
print(tmp)                      # Make a tuple from the list's items

T = tuple(tmp)                  # Make a tuple from the list's items
print(T)

print(sorted(T))                # Or use the sorted built-in, and save two steps

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)

T = (1, 2, 3, 2, 4, 2)          # Tuple methods in 2.6, 3.0 and later
print(T.index(2))               # Offset of first appearance of 2
print(T.index(2, 2))            # Offset appearance after offset 2
print(T.count(2))               # How many 2s are there?

T = (1, [2, 3], 4)              # Cannot change tuple itself
T[1][0] = 'spam'                # can change mutable inside
print(T)

bob = ('Bob', 40.5, ['dev', 'mgr'])     # Tuple record
print(bob)
print(bob[0], bob[2])                   # Access by position

bob = dict(name='bob', age=40.5, jobs=['dev', 'mgr'])  # Dictionary record
print(bob)
print(bob['name'], bob['jobs'])         # Access by key
print(tuple(bob.values()))              # Values to tuple
print(list(bob.items()))                # Items to tuple list

from collections import namedtuple                  # Import extension type

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])    # Make a generated class
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])     # A named-tuple record
print(bob)

print(bob[0], bob[2])                   # Access by position
print(bob.name, bob.jobs)               # Access by attribute

O = bob._asdict()                       # Dictionary-lie form
print(O['name'], O['jobs'])             # Access by key too
print(O)

bob = Rec('Bob', 40.5, ['dev', 'mgr'])  # For both tuples and named tuples
name, age, jobs = bob
print(name, jobs)
print(age)

for x in bob:
    print(x)

bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
job, name, age = bob.values()
print(name, job)                        # Dict equivalent
print(age)

for x in bob:                           # Step through keys, index values
    print(bob[x])
for x in bob.values():                  # Step through values view
    print(x)

myfile = open('myfile.txt', 'w')        # Open for text output: create/empty
myfile.write('hello text file\n')       # Write a line of text: string
myfile.write('goodbye text file\n')     # Flush output buffers to disk
myfile.close()

myfile = open('myfile.txt')             # Open for text input: 'r' is default
print(myfile.readline())                # Read the lines back
print(myfile.readline())
print(myfile.readline())

open('myfile.txt').read()               # Read all at once into string
print(open('myfile.txt').read())        # User-friendly display

for line in open('myfile.txt'):         # Use file iterators, no reads
    print(line, end='')

data = open('data.bin', 'rb').read()    # Open binary file: rb=read binary
print(data)                             # bytes string  holds binary data
print(data[4:8])                        # Act like strings
print(data[4:8][0])                     # But really are small 8-bit integers
print(bin(data[4:8][0]))                # Python 3.X/2.6+ bin() function

X, Y, Z = 43, 44, 45                    # Native python objects
S = 'Spam'                              # Must be strings to store in file
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')           # Create output text file
F.write(S + '\n')                       # Terminate lines with \n
F.write('%s, %s, %s\n' % (X, Y, Z))     # Convert numbers to strings
F.write(str(L) + '$' + str(D) + '\n')   # Convert and separate with $
F.close()

chars = open('datafile.txt').read()     # Raw string display
print(chars)

F = open('datafile.txt')                # Open again
line = F.readline()                     # Read one line
print(line)
print(line.strip())                     # Remove end-of-file line
line = F.readline()                     # Next line from file
print(line)                             # It's a string here
parts = line.split(',')                 # Split (parse) on commas
print(parts)

print(int(parts[1]))                    # Convert from string on int
numbers = [int(P) for P in parts]       # Convert all in list at once
print(numbers)

line = F.readline()
print(line)
parts = line.split('$')                # Split (parse) on $
print(parts)
print(eval(parts[0]))                  # Convert to any object type
objects = [eval(P) for P in parts]     # Do same for all in list
print(objects)

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')

import pickle
pickle.dump(D, F)                       # Pickle any object to a file
F.close()

F = open('datafile.pkl', 'rb')          # Load any object from file
E = pickle.load(F)
print(E)

print(open('datafile.pkl', 'rb').read())    # Format is prone to change!

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age = 40.5)
print(rec)

import json
S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)
print(O == rec)

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())

F = open('data.bin', 'wb')              # Open binary output file

import struct

data = struct.pack('>i4sh', 7, b'spam', 8)  # make packed binary data
print(data)
F.write(data)                               # write byte string
F.close()

F = open('data.bin', 'rb')
data = F.read()                             # Get packed binary data
print(data)
values = struct.unpack('>i4sh', data)       # Convert to Python object
print(values)

L = ['abc', [(1, 2), ([3], 4)], 5]
print(L[1])
print(L[1][1])
print(L[1][1][0])
print(L[1][1][0][0])

X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}

X[1] = 'surprise'                           # Changes all three references!
print(L)
print(D)

L = [1, 2, 3]
D = {'a': 1, 'b': 2}

A = L[:]                                    # Instead of A = L (or list(L))
B = D.copy()                                # Instead of B = D (ditto for sets)
A[1] = 'Ni'
B['c'] = 'spam'
print(L, D)
print(A, B)
X = [1, 2, 3]
L = ['a', X[:], 'b']                        # Embed copies of X;s object
D = {'x': X[:], 'y': 2}
print(L)
print(D)

L1 = [1, ('a', 3)]                          # Same value, unique objects
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)                   # Equivalent?, Same object?

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)

S1 = 'a longer string'
S2 = 'a longer string'
print(S1 == S2, S1 is S2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)

print(11 == '11')                   # Equality does not convert non-numbers
# print(11 >= '11')                   # 2.X compares by type name string: int str
print(['11', '22'].sort())
# print([11, '11'].sort()
print(11 > 9.123)                           # Mixed numbers convert to highest type
print(str(11) >= '11', 11 >= int('11'))     # Manual conversion force issue

D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
print(D1 == D2)                             # Dictionary equalityL 2.X + 3.X
# print(D1 < D2)                              # Dictionary magnitude: 2.X only

print(list(D1.items()))
print(sorted(D1.items()))
print(sorted(D1.items()) < sorted(D2.items()))  # Magnitude test 3.X
print(sorted(D1.items()) < sorted(D2.items()))

print(bool(1))
print(bool('spam'))
print(bool({}))

print(type([1]) == type([]))                # Compare to type of another list
print(type([1]) == list)                    # Compare to list type name
isinstance([1], list)                       # Test of list or customization therof

import types

def f():
    pass

print(type(f) == types.FunctionType)        # types has names for other types

L = [1, 2, 3]
M = ['X', L, 'Y']
print(L)
print(M)
L[1] = 0
print(M)

L = [1, 2, 3]
M = ['X', L[:], 'Y']
L[1] = 0
print(L)
print(M)

L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print(L)
print(X)
print(Y)

L[1] = 0
print(X)
print(Y)

L = [4, 5, 6]
Y = [list(L)] * 4
L[1] = 0
print(Y)

Y[0][1] = 99
print(Y)

L = [4, 5, 6]
Y = [list(L) for i in range(4)]
print(Y)
Y[0][1] = 99
print(Y)

L = ['grail']               # Append reference ot same object
L.append(L)                 # Generates cycle in object [...]
print(L)

T = (1, 2, 3)
# T[2] = 4            # Error
T = T[:2] + (4,)


### Test Your Knowledge

### 1. How can you determine how large a tuple is? WHy is the tool located where it is?
""" The built-in function len function returns the length (number of contained items) for
    any container object in Python, including tuples. It is a built-in function instead
    of a type method because it applies to many different objects. In general, built-in
    functions and expressions may span many object types; methods are specific to a single
    object type, though some may ne available on more than one type (index, for example,
    works on lists and tuples).
"""

### 2. Write an expression that changes the first item in a tuple. (4, 5, 6) should become
###     (1, 5, 6) in the process.
""" Because they are immutable, you can'r really change tuples in place, but you can
    generate a new tuple with the desire value. Given T = (4, 5, 6), you can change the
    first item by making a new tuple from its parts by slicing and concatenating:
    T = (1,) + T[1:]. (Recall that single-item tuples require a trailing comma.) You
    could also convert the tuple to a list, change it in place, and convert it back to a
    tuple, but this is more expensive and is rarely required in practice--simply use a list
    if you know that the object will require in-place changes.
"""

### 3. What is the default for the processing mode argument in a file open call?
""" The default for the processing mode argument in a file open call is 'r', for reading
    text input. For input text files, simply pass in the external file's name.
"""

### 4. What module might you use to store Python object in a file without converting
###     them to string yourself?
""" The pickle module can be used to store Python objects in a file without explicitly
    converting them to strings. The struct module is related, but it assumes the data is
    to be in packed binary format in the file, json similarly converts a limited set of
    Python objects to and from string per line in JSON format
"""

### 5. How might one go about copying all parts of a nested structure at once?
""" Import the copy module and call all parts of nested structure X. This is also rarely
    seen in practice; references are usually the desired behavior, and shallow copies
    usually suffice for most copies.
"""
### 6. When does python consider an object true?
""" An object is considered true if it is either a nonzero number or a nonempty collection
    object. The built-on words True and False are essntially predefined to have the same
    meanings as integer 1 and 0 respectively.
"""

### Exercises

### 2.1
print(2 ** 16)
print(2 / 5, 2 / 5.0)

print("spam" + "eggs")
S = "ham"
print("eggs" + S)
print(S * 5)
print(S[:0])
print("green %s and %s" % ("eggs", S))
print("green {0} and {1}".format('eggs', S))

print(('x',)[0])
print(('x', 'y')[1])

L = [1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print(L[2], L[3])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))

print({'a': 1, 'b': 2}['b'])
D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 0
print(D['x'] + D['w'])
D[(1, 2, 3)] = 4
print(list(D.keys()), list(D.values()), (1, 2, 3) in D)
print(D)
print([[]], ["", [], (), {}, None])


### 2.2

L = [0, 1, 2, 3]

# a
# print(L[4])
# print(L[-1000:100]
print(L[1:3])
print(L[3:1])
print(L)
L[3:1] = '?'
print(L[3:1])
print(L)
# L[-1000:100] = 9
# print(L[-1000:100])
# print(L)


### 2.3

L = [0, 1, 2, 3]
L[2] = []
print(L)
L[2:3] = []
print(L)


# 2.4

X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X)
print(Y)


# 2.5

D = {}
D[1] = 'a'
D[2] = 'b'
print(D)

D[(1, 2, 3)] = 'c'
print(D)


# 2.6

D = {'a': 1, 'b': 2, 'c': 3}
print(D)
# print(D['d'])
D['d'] = 'spam'
print(D)

# 2.7

# a. Error
# print(2 + 'a')
# print([2] + 2)
# print({2} + 2)
# print([2] + (2,))
# print('a' + {'b': 2})
# b. No
# print({'a': 1} + {'b': 2})
# c. Yes, No
L = [1, 2]
L.append(3)
L.append('a')
print(L)
# 'a'.append('b')
# d.
print('a' + 'b')
print('abcde'[0:2])
print(['a', 'b'] + ['c', 'd'])
print(['a', 'b', 'c', 'd', 'e'][0:2])


# 2.8

S = 'spam'
print(S[0][0][0][0][0])
L = ['s', 'p', 'a', 'm']
print(L[0][0][0][0][0])


# 2.9

S = 'spam'
S1 = S[:1] + 'l' + S[2:]
print(S1)
S2 = S[0] + '1' + S[2] + S[3]
print(S2)


# 2.10

D = {'name': dict(first='Johnny', middle='B', last='Goode'),
     'age': 22,
     'job': 'Soft Engr/Manager',
     'address': '77 Tulsa Rd',
     'email': 'jbg@gmail.org',
     'phone': '666-9876'}

# 2.11

file = open('myfile.txt', 'w')
file.write('Hello file world\n')
file.close()

file = open('myfile.txt', 'r')
text = file.read()
print(text)
