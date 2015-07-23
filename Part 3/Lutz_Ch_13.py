__author__ = 'rolando'

############################################
#### Part 3: Statements and Syntax PG 319-469
###  CH 13: while an for loops
############################################

x = 'spam'
while x:                        # While is no
    print(x, end=' ')
    x = x[1:]                   # Strip the first character off x

a = 0
b = 10
while a < b:                    # One way to code counter loops
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

for allx in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = allx[0], allx[1:3], allx[3]
    print(a, b, c)

items = ["aaa", 111, (4, 5), 2.01]      # A set of objects
tests = [(4, 5), 3.14]                  # Keys to search for

for key in tests:                      # for all keys
    for item in items:                  # for all items
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found!")

for key in tests:                       # For all keys
    if key in items:                    # Let python check for a match
        print(key, "was found")
    else:
        print(key, "not found!")

seq1 = "spam"
seq2 = "scam"

res = []                                # Start empty
for x in seq1:                          # Scan first sentence
    if x in seq2:                       # Common item?
        res.append(x)                   # Add to result end
print(res)

print([x for x in seq1 if x in seq2])   # Let Python collect results

print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))

print(list(range(-5, 5)))
print(list(range(5, -5, -1)))

for i in range(3):
    print(i, 'Pythons')

X = 'spam'
for item in X:
    print(item, end=' ')
print()

i1 = 0
while i1 < len(X):
    print(X[i1], end=' ')
    i1 += 1

print()
print(X)
print(len(X))                           # Length of string
print(list(range(len(X))))              # All legal offsets into X

for i in range(len(X)):
    print(X[i], end=' ')                # Manual range/len iteration
print()

for item in X:                          # Use simple iteration if you can
    print(item, end=' ')
print()

S = 'spam'
for i in range(len(S)):                 # For repeat counts 0...3
    S = S[1:] + S[:1]                   # Move front item to end
    print(S, end=' ')
print()

for i in range(len(S)):                 # For positions 0...3
    X = S[i:] + S[:i]                   # Rear part + front part
    print(X, end=' ')
print()

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L [:i]
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
    x += 1                              # Changes x, not L
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

print(list(zip(T1, T2, T3)))            # Three tuples for three arguments

S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2)))                # Truncates at len(shortest)

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
