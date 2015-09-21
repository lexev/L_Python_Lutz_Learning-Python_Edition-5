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

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c)

items = ["aaa", 111, (4, 5), 2.01]      # A set of objects
tests = [(4, 5), 3.14]                  # Keys to search for

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found!")

for key in tests:
    if key in items:
        print(key, "way found")
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