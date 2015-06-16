__author__ = 'rolando'

############################################
#### Part 3: Statements and Syntax PG 319-469
###  CH 12: if Tests and Syntax Rules
############################################


if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')

x = 'killer rabbit'

if x == 'roger':
    print("shave and a haircut")
elif x == 'bugs':
    print("what's up doc?")
else:
    print("Run away! Run away!")

choice = 'ham'
print({'spam':  1.25,
       'ham':   1.99,
       'eggs':  0.99,
       'bacon': 1.10}[choice])

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))

choice = 'bacon'

if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

print(2 < 3, 3 < 3)
print(2 or 3, 3 or 2)
print([] or 3)
print([] or {})

print(2 and 3, 3 and 2)
print([] and {})
print(3 and [])

A = 't' if 'apam' else 'f'          # for strings, non-empty means true
print(A)
A = 't' if '' else 'f'

print(['f', 't'][bool('')])
print(['f', 't'][bool('')])

L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L)))        # Get the values
print([x for x in L if x])          # Comprehensions
print(any(L), all(L))               # Aggregate truth

### 1. How might you code a multi-way branch in Python?
""" An if statement with multiple elif clauses is often the most straightforward way to
    code a multi-way branch, though not necessarily the most consice or flexible.
    Dictionary indexing can often achieve the same result, especially if he dictionary
    contains callable functions coded with def statements or lambda expressions.
"""

### 2. How can you code an if/else statement as an expression in Python?
""" In python 2.5 and later, the expression form Y if X else Z returns Y id X is true, or
    Z otherwise; it's the same as a four=line if statement. The and/or combination
    (((X and Y) or Z)) can work the same way, but its more obscure and requires that the
    Y part be true
"""

### 3. How can you make a single statement span many lines?
""" Wrap up the statement in an open syntactic pair ((), [], or {}), and it can span as many
    lines as you like; the statement ends when Python sees the closing (right) half of the
    pair, and lines 2 and beyond of the statement can begin at any indentation level.
    Backslash continuations work too, but are broadly discouraged in the Python world.
"""

### 4. What do the worlds True and False mean?
""" True and False are just custom versions of the integers1 and 0, respectively, they
    always stand for Boolean true and false values in Python. They are available for use
    in truth tests and variable initialization, and are printed for expression results at
    the interactive prompt. In all there roles, they serve as a more mnemoni and hence
    readable alternative to 1 and 0.
"""