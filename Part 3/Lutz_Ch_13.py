__author__ = 'rolando'

############################################
#### Part 3: Statements and Syntax PG 319-469
###  CH 13: while an for loops
############################################

x = 'spam'
while x:  # While is no
    print(x, end=' ')
    x = x[1:]  # Strip the first character off x

a = 0
b = 10
while a < b:  # One way to code counter loops
    print(a, end=' ')
    a += 1

# while True:
#     name = input('Enter name: ')
#     if name == 'stop':
#         break
#     age = input('Enter age: ')
#     print('Hello', name, '=>', int(age) ** 2)

for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')

sum1 = 0
for x in [1, 2, 3, 4]:
    sum1 += x

print(sum1)

prod = 1
for item in [1, 2, 3, 4]:
    prod *= item

print(prod)

S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S:
    print(x, end=' ')

for x in T:
    print(x, end=' ')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

print(list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value)

print(T)
for both in T:
    a, b = both
    print(a, b)

((a, b), c) = ((1, 2), 3)
print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)

a, b, c = (1, 2, 3)
print(a, b, c)

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

a, b, c = (1, 2, 3)
print(a, b, c)

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

a, *b, c = (1, 2, 3, 4)
print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

for alli in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = alli[0], alli[1:3], alli[3]

for allx in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = allx[0], allx[1:3], allx[3]
    print(a, b, c)

items = ["aaa", 111, (4, 5), 2.01]  # A set of objects
tests = [(4, 5), 3.14]  # Keys to search for

for key in tests:  # for all keys
    for item in items:  # for all items
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found!")

for key in tests:
    if key in items:
        print(key, "way found")

for key in tests:  # For all keys
    if key in items:  # Let python check for a match
        print(key, "was found")
    else:
        print(key, "not found!")

seq1 = "spam"
seq2 = "scam"

res = []
for x in seq1:
    if x in seq2:
        res.append(x)

print(res)

print([x for x in seq1 if x in seq2])

print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
res = []  # Start empty
for x in seq1:  # Scan first sentence
    if x in seq2:  # Common item?
        res.append(x)  # Add to result end
print(res)

print([x for x in seq1 if x in seq2])  # Let Python collect results

print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))

print(list(range(-5, 5)))
print(list(range(5, -5, -1)))

for i in range(3):
    print(i, 'Pythons')

X = 'spam'
for item in X:
    print(item, end=' ')

print()
k = 0
while k < len(X):
    print(X[k], end=' ')
    k += 1

print("\n%s" % X)
print(len(X))
print(list(range(len(X))))
for i in range(len(X)):
    print(X[i], end=' ')

print()
for item in X:
    print(item, end=' ')

print()
S = 'spam'

for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')
print()

i1 = 0
while i1 < len(X):
    print(X[i1], end=' ')
    i1 += 1

print()
print(X)
print(len(X))  # Length of string
print(list(range(len(X))))  # All legal offsets into X

for i in range(len(X)):
    print(X[i], end=' ')  # Manual range/len iteration
print()

for item in X:  # Use simple iteration if you can
    print(item, end=' ')
print()

S = 'spam'
for i in range(len(S)):  # For repeat counts 0...3
    S = S[1:] + S[:1]  # Move front item to end
    print(S, end=' ')
print()

for i in range(len(S)):  # For positions 0...3
    X = S[i:] + S[:i]  # Rear part + front part
    print(X, end=' ')
print()

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]
    print(X, end=' ')
print()

S = 'abcdefghijk'
print(list(range(0, len(S), 2)))

for i in range(0, len(S), 2):
    print(S[i], end=' ')
print()

for c in S[::2]:
    print(c, end=' ')
print()

L = [1, 2, 3, 4, 5]
for x in L:
    x += 1  # Changes x, not L
print(L)
print(x)

for i in range(len(L)):
    L[i] += 1
print(L)

i1 = 0
while i1 < len(L):
    L[i1] += 1
    i1 += 1
print(L)

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(T3)

print(list(zip(T1, T2, T3)))  # Three tuples for three arguments

S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2)))  # Truncates at len(shortest)
print(list(map(ord, 'spam')))

res = []
for c in 'spam':
    res.append(ord(c))
print(res)

D1 = {'spam': 1, 'eggs': 3, 'toast': 5}
print(D1)

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

print(list(zip(keys, vals)))

D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D2)

D3 = dict(zip(keys, vals))
print(D3)

print({k: v for (k, v) in zip(keys, vals)})

S = 'spam'
offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1

S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

E = enumerate(S)
print(E)
print(next(E))
print(next(E))
print(next(E))

print([c * i for (i, c) in enumerate(S)])

for (i, l) in enumerate(open('test.txt')):
    print('%s) %s' % (i, l.rstrip()))

import os

F = os.popen('dir')
print(F.readline())         # Read line by line

F = os.popen('dir')
print(F.read(50))           # Read by sized blocks

print(os.popen('dir').readlines()[0])       # Read all lines: index

print(os.popen('dir').read()[:50])          # Read all at once: slice

for line in os.popen('dir'):                # File line iterator loop
    print(line.rstrip())

# print(os.system('systeminfo'))

# for (i, line) in enumerate(os.popen('systeminfo')):
#     if i == 4: break
#     print('%05d) %s' % (i, line.rstrip()))

# for line in os.popen('systeminfo'):
#     parts = line.split(':')
#     if parts and parts[0].lower() == 'system type':
#         print(parts[1].strip())

from urllib.request import urlopen


for line in urlopen('http://home.rmi.net/~lutz'):
    print(line)

### Test Your Knowledge PG 414

### 1. What are the main functional differences between a while and a for?
""" The while loop is a general looping statement but the for is designed to iterate across items
    a sequence or other iterable. Although the while can imitate the for with counter loops, it
    takes more code and might run slower.
"""

### 2. What's the difference between break and continue?
""" The break statement exits a loop immediately (you wind up below the entire while or for loop
    statement), and continue jumps pack to the top of the loop (you wind up positioned just before
    the test in th while loop anf the next item fetch in for).
"""

### 3. When is a loop's else clause executed?
""" The else clause in a while or for loop will be run once as the loop is exiting, if the loop
    exits normally (without running into a break statement). A break exits the loop immediately,
    skipping the else part on the way out (if there is one).
"""

### 4. How can you code a counter-based loop in Python?
""" Counter loops can be coded with a while statement that keeps track of the index manually, or
    with a for loop that uses the range built-in function to generate successive integer offsets.
    Neither is the preferred way to work in Python, if you need to simply step across all items
    in a sequence. Instead, use a simple for loop without range or counters whenever possible;
    i will be easier to code and usually quicker to run."""

### 5. What can range be used for in a for loop?
""" The range built-in can be used in a for to implement a fixed number of repetitions, to scan by
    offsets instead of items at offsets, to skip successive items as you go, and to change a list
    while stepping across it. None of those roles requires range, and most have alternatives --
    scanning actual items, three-limit slices, and list comprehensions are often better solutions
    today (despite the natural inclinations of ex-C programmers to want to count things!)."""