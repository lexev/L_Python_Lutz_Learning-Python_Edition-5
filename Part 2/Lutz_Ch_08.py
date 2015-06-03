__author__ = 'rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 8: Lists and Dictionaries
############################################

print(len([1, 2, 3]))               # Length
print([1, 2, 3] + [4, 5, 6])        # Concatenation
print(['Ni!'] * 4)                  # Repetition

print(str([1, 2]) + "34")           # Same as "[1, 2] + "34"
print([1, 2] + list("34"))          # Same as [1, 2] + ["3", "4"]

print(3 in [1, 2, 3])               # Membership
for x in [1, 2, 3]:                 # iteration
    print(x, end='')

res = [c * 4 for c in 'SPAM']       # List comprehensions
print(res)

res = []
for c in 'SPAM':                    # List comprehension equivalent
    res.append(c * 4)
print(res)

print(list(map(abs, [-1, -2, 0, 1, 2])))    # Map a function across a sequence

L = ['spam', 'Spam', 'SPAM!']
print(L[2])                         # Offsets start at zero
print(L[-2])                        # Negative: count from the right
print(L[1:])                        # Slicing fetches sections

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][1])

L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'                       # Index assignment
print(L)

L[0:2] = ['eat', 'more']            # Slice assignmentL delete+insert
print(L)                            # Replaces items: 0, 1

L = [1, 2, 3]
print(L)
L[1:2] = [4, 5]                     # Replacement/insertion
print(L)
L[1:1] = [6, 7]                     # Insertion (replace nothing)
print(L)
L[1:2] = []                         # Deletion (insert nothing)
print(L)

L = [1]
L[:0] = [2, 3, 4]                   # Insert at :0, an empty slice at the front
print(L)
L[len(L):] = [5, 6, 7]              # Insert all at len(L); an empty slice at the end
print(L)
L.extend([8, 9, 10])                # Insert all at the end, named method
print(L)

L = ['abc', 'ABD', 'aBe']           # Sort with mixed case
L.sort()
print(L)

L = ['abc', 'ABD', 'aBe']           # Normalize lowercase
L.sort(key=str.lower)
print(L)

L = ['abc', 'ABD', 'aBe']           # Change the sort order
L.sort(key=str.lower, reverse=True)
print(L)

L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))       # Sorting built-in

L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], reverse=True))     # Pre-transform items: differs!

L = [1, 2]
L.extend([3, 4, 5])                 # Add many items at end (like in-place +)
print(L)

print(L.pop())                      # Delete and return last item(by default: -1
print(L)

L.reverse()                         # In-place reversal method
print(L)

print(list(reversed(L)))            # Reversal built-in with result (iterator)

L = []
L.append(1)                         # Push onto stack
L.append(2)
print(L)
L.pop()                             # Pop off stack
print(L)

L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))              # Index of an object (search/find)

L.insert(1, 'toast')                # Insert at position
print(L)

L.remove('eggs')                    # Delete by value
print(L)

print(L.pop(1))                     # Delete by position
print(L)

print(L.count('spam'))              # Number of occurrences

L = ['spam', 'eggs', 'ham', 'toast']
del L[0]                            # Delete an entire section
print(L)
del L[1:]                           # Delete an entire section
print(L)

L = ['Already', 'got', 'one']
L[1:] = []
print(L)
L[0] = []
print(L)


## 250 Dictionaries

D = {'spam': 2, 'ham': 1, 'eggs': 3}        # Make a dictionary
print(D['spam'])                            # Fetch a value by key
print(D)

print(len(D))                               # Number of entries in a dictionary
print('ham' in D)                           # Key membership test alternative
print(list(D.keys()))                       # Create a new list of D's keys

print(D)
D['ham'] = ['grill', 'bake', 'fry']         # Change entry (value=list)
print(D)
del D['eggs']                               # Delete entry
print(D)
D['brunch'] = 'Bacon'                       # Add new entry

D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.items()))
print(list(D.keys()))

print(D.get('spam'))                        # A key that is there
print(D.get('toast'))                       # A key that is missing
print(D.get('toast', 88))

print(D)
D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)

print(D.pop('muffin'))                      # Delete and return from a key
print(D.pop('toast'))
print(D)

L = ['aa', 'bb', 'cc', 'dd']
print(L.pop())                              # Delete and return from end
print(L.pop(1))                             # Delete and return from a specific position
print(L)

table = {'1975': 'Holy Grail',
         '1979': 'Life of Brian',
         '1983': 'Meaning of Life'}
year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])

table = {'Holy Grail':          '1975',
         'Life of Brian':       '1979',
         'The Meaning of Life': '1983'}
print(table['Holy Grail'])
print(list(table.items()))
print([title for (title, year) in table.items() if year == '1975'])

K = 'Holy Grail'
print(table[K])