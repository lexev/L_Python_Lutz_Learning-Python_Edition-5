__author__ = 'rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 8: Lists and Dictionaries
############################################

print(len([1, 2, 3]))  # Length
print([1, 2, 3] + [4, 5, 6])  # Concatenation
print(['Ni!'] * 4)  # Repetition

print(str([1, 2]) + "34")  # Same as "[1, 2] + "34"
print([1, 2] + list("34"))  # Same as [1, 2] + ["3", "4"]

print(3 in [1, 2, 3])  # Membership
for x in [1, 2, 3]:  # iteration
    print(x, end='')

res = [c * 4 for c in 'SPAM']  # List comprehensions
print(res)

res = []
for c in 'SPAM':  # List comprehension equivalent
    res.append(c * 4)
print(res)

print(list(map(abs, [-1, -2, 0, 1, 2])))  # Map a function across a sequence

L = ['spam', 'Spam', 'SPAM!']
print(L[2])  # Offsets start at zero
print(L[-2])  # Negative: count from the right
print(L[1:])  # Slicing fetches sections

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][1])

L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'  # Index assignment
print(L)

L[0:2] = ['eat', 'more']  # Slice assignmentL delete+insert
print(L)  # Replaces items: 0, 1

L = [1, 2, 3]
print(L)
L[1:2] = [4, 5]  # Replacement/insertion
print(L)
L[1:1] = [6, 7]  # Insertion (replace nothing)
print(L)
L[1:2] = []  # Deletion (insert nothing)
print(L)

L = [1]
L[:0] = [2, 3, 4]  # Insert at :0, an empty slice at the front
print(L)
L[len(L):] = [5, 6, 7]  # Insert all at len(L); an empty slice at the end
print(L)
L.extend([8, 9, 10])  # Insert all at the end, named method
print(L)

L = ['abc', 'ABD', 'aBe']  # Sort with mixed case
L.sort()
print(L)

L = ['abc', 'ABD', 'aBe']  # Normalize lowercase
L.sort(key=str.lower)
print(L)

L = ['abc', 'ABD', 'aBe']  # Change the sort order
L.sort(key=str.lower, reverse=True)
print(L)

L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))  # Sorting built-in

L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], reverse=True))  # Pre-transform items: differs!

L = [1, 2]
L.extend([3, 4, 5])  # Add many items at end (like in-place +)
print(L)

print(L.pop())  # Delete and return last item(by default: -1
print(L)

L.reverse()  # In-place reversal method
print(L)

print(list(reversed(L)))  # Reversal built-in with result (iterator)

L = []
L.append(1)  # Push onto stack
L.append(2)
print(L)
L.pop()  # Pop off stack
print(L)

L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))  # Index of an object (search/find)

L.insert(1, 'toast')  # Insert at position
print(L)

L.remove('eggs')  # Delete by value
print(L)

print(L.pop(1))  # Delete by position
print(L)

print(L.count('spam'))  # Number of occurrences

L = ['spam', 'eggs', 'ham', 'toast']
del L[0]  # Delete an entire section
print(L)
del L[1:]  # Delete an entire section
print(L)

L = ['Already', 'got', 'one']
L[1:] = []
print(L)
L[0] = []
print(L)


## 250 Dictionaries

D = {'spam': 2, 'ham': 1, 'eggs': 3}  # Make a dictionary
print(D['spam'])  # Fetch a value by key
print(D)

print(len(D))  # Number of entries in a dictionary
print('ham' in D)  # Key membership test alternative
print(list(D.keys()))  # Create a new list of D's keys

print(D)
D['ham'] = ['grill', 'bake', 'fry']  # Change entry (value=list)
print(D)
del D['eggs']  # Delete entry
print(D)
D['brunch'] = 'Bacon'  # Add new entry

D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.items()))
print(list(D.keys()))

print(D.get('spam'))  # A key that is there
print(D.get('toast'))  # A key that is missing
print(D.get('toast', 88))

print(D)
D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)

print(D.pop('muffin'))  # Delete and return from a key
print(D.pop('toast'))
print(D)

L = ['aa', 'bb', 'cc', 'dd']
print(L.pop())  # Delete and return from end
print(L.pop(1))  # Delete and return from a specific position
print(L)

table = {'1975': 'Holy Grail',
         '1979': 'Life of Brian',
         '1983': 'Meaning of Life'}
year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])

table = {'Holy Grail': '1975',
         'Life of Brian': '1979',
         'The Meaning of Life': '1983'}
print(table['Holy Grail'])
print(list(table.items()))
print([title for (title, year) in table.items() if year == '1975'])

K = 'Holy Grail'
print(table[K])

V = '1975'
print([key for (key, value) in table.items() if value == V])
print([key for key in table.keys() if table[key] == V])

D = {}
D[99] = 'spam'
print(D[99])
print(D)

table = {1975: 'Holy Grail',
         1979: 'Life pf Brian',
         1983: 'The Meaning of Life'}
print(table[1975])
print(list(table.items()))

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2
Y = 3
Z = 4
print(Matrix[(X, Y, Z)])

if (2, 3, 6) in Matrix:             # Check for key before fetch
    print(Matrix[(2, 3, 6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])        # Try to index
except KeyError:                    # Catch and recover
    print(0)

print(Matrix.get((2, 3, 4), 0))     # Exists: fetch and return
print(Matrix.get((2, 3, 6), 0))     # Doesn't exist, use default arg

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print(rec['name'])

rec = {'name': 'Bob',
       'jobs': ['developer', 'manager'],
       'web': 'www.bobs.org/Bob',
       'home': {'state': 'Overworked', 'zip': 12345}}
print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])

print(dict.fromkeys(['a', 'b'], 0))

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))    # Zip together keys and values
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))       # Make a dict from zip result
print(D)
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

D = {c: c * 4 for c in 'SPAM'}                  # Loop over any iterable
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

D = dict.fromkeys(['a', 'b', 'c'], 0)           # Initialize dict from keys
print(D)

D = {k: 0 for k in ['a', 'b', 'c']}             # Same but with a comprehension
print(D)

D = dict.fromkeys('spam')                       # Other iterables, default value
print(D)

D = {k: None for k in 'spam'}
print(D)

D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()                                    # Makes a view object in 3.X, not a list
print(K)
print(list(K))                                  # Force a real list in 3.X if needed

V = D.values()                                  # Ditto for values and items views
print(V)
print(list(V))

for k in D.keys():
    print(k)                                    # Iterators used automatically in loops

for key in D:                                   # Still no need to call keys() to iterate
    print(key)

D = {'a': 1, 'b': 2, 'c': 3}
print(D)

K = D.keys()
V = D.values()
print(list(K))                                  # Views maintain same order as dictionary
print(list(V))
del D['b']                                      # Chane the dictionary in place
print(D)
print(list(K))                                  # Reflected in any current view objects
print(list(V))                                  # Not true in 2.X! - list detached from dict

print(K, V)
print(K | {'x': 4})

D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & D.keys())          # Intersect key values
print(D.keys() & {'b'})             # Intersect keys and set
print(D.keys() & {'b': 1})          # Intersect keys and dict

D = {'a': 1}
print(list(D.items()))              # Items set-like if hashable
print(D.items() | D.keys())         # Union view and view
print(D.items() | D)                # dict treated same as keys
print(D.items() | {('c', 3), ('d', 4)})     # Set of key/value pairs
print(dict(D.items() | {('c', 3), ('d', 4)}))     # dict accepts iterable sets too

D = {'a': 1, 'b': 2, 'c': 3}
print(D)

Ks = D.keys()                       # Sorting a view object doesn't work
Ks = list(Ks)                       # Force it to be a list and then sort
Ks.sort()
for k in Ks:
    print(k, D[k])                  # 2.X: omit outer paren s in prints

print(D)
Ks = D.keys()                       # Or you can use sorted() on the keys
for k in sorted(Ks):                # sorted() accepts any iterable
    print(k, D[k])                  # sorted() returns its result

print(D)
for k in sorted(D):
    print(k, D[k])                  # Better yet. sort the dict directly

print(D)
print('c' in D)                     # required in 3.X
print('x' in D)                     # preferred in 2.X today
if 'c' in D:                        # Branch on result
    print('present', D['c'])
print(D.get('c'))                   # Fetch with default
print(D.get('x'))
if D.get('c') is not None:
    print('present', D['c'])        # Another option

### PG 272, Test your knowledge

### 1. Name two ways to build a list containing five integer zeros.
""" A literal expression like [0, 0, 0, 0, 0] and a repetition  like [0] * 5 will each
    create a list of five zeroes. In practive, you might also buld one up with L.append(0).
    A list comprehension ([0 for 1 in range(5)]) could work here, too. but this is more
    work than you need to do for this answer
"""

### 2. Name two ways to build a dictionary with two keys, 'a' and 'b', each having
###     an associated value of zero.
""" A literal expression such as {'a': 0, 'b': 0} or a series of assignments like D = {},
    D['a'] = 0, D['b'] = 0 would like the desired dictionary. You can also use the newer
    and simpler-to-code dict(a=0, ,b=0) keyword form, or the more flexible dict([('a', 0),
    ('b', 0)]) key/value sequences form. Or, because all the values are the same, you cn use
    the special form dict.fromkeys('ab', 0). In 3.x and 2.7, you can also use a dictionary
    comprehension: {k:0 for k in 'ab'}, thought again, this may be overkill here.
"""

### 3. Name four operations that change a list object in place
""" The append and extend methods grow a list in place, the sort and reverse methods order
    and reverse lists, the insert method inserts an item at an offset, the remove and pop
    methods delete from a list by value and by position, the del statement deletes an item
    or slice, and index and slice assignment statements replace an item or entire section.
"""

### 4. Name four operations that change a dictionary object in place
""" Dictionaries are primarily changed by assignment to a new or existing key, which
    creates or changes the key's entry in the tab;e. Also the del statement deletes a
    key's entry, the dictionary update method merges one dictionary into another in place,
    D.pop(key) removes a key and returns the value it had.
"""

### 5. Why might you use a dictionary instead of a list?
""" Dictionaries are generally better when data is labled (a record with filed names, for
    example); lists are best suited to collections of unlabeled items (such as all the
    files in a directory). Dictionary lookup is also usually quicker then searching a
    list, though this may vary per program.
"""
