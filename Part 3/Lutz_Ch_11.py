__author__ = 'rolando'

############################################
#### Part 3: Statements and Syntax PG 319-469
###  CH 11: Assignments, Expressions, and prints
############################################

nudge = 1                   # Basic assignment
wink = 2
A, B = nudge, wink          # Tuple assignment
print(A, B)                 # Like A = nudge; B = wink
[C, D] = [nudge, wink]      # List assignment
print(C, D)

nudge = 1
wink = 2
nudge, wink = wink, nudge   # Tuples: swap values
print(nudge, wink)          # Like T = nudge, nudge = wink;wink = T

[a, b, c] = (1, 2, 3)       # Assign tuple of values to list names
print(a, c)
print(b)
(a, b, c) = "ABC"           # Assign string of characters to a tuple
print(a, c)
print(b)

string = "SPAM"
a, b, c, d = string         # Same number on both sides
print(a, d)
print(b, c)
# a, b, c = string            # Error if not

a, b, c = string[0], string[1], string[2:]      # Index and slice
print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]       # Slice and concatenate
print(a, b, c)

a, b, = string[:2]                              # Same, but simpler
c = string[2:]
print(a, b, c)

(a, b), c = string[:2], string[2:]              # Nested sequences
print(a, b, c)

((a, b), c) = ('SP', 'AM')                      # Paired by shape and position
print(a, b, c)

red, green, blue = range(3)
print(red, blue)
print(green)

print(list(range(3)))                           # list() required in Python 3.X

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
# a, b = seq
a, *b = seq
print(a)
print(b)

*a, b = seq
print(a)
print(b)

a, *b, c = seq
print(a)
print(b)
print(c)

a, b, *c = seq
print(a)
print(b)
print(c)

a, *b = 'spam'
print(a, b)

a, *b, c = 'spam'
print(a, b, c)

a, *b, c = range(4)
print(a, b, c)

S = 'spam'
print(S[0], S[1:])          # Slices are type-specific, *assignment always returns a list
print(S[0], S[1:3], S[3])

L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

seq = [1, 2, 3, 4]

a, b, c, *d = seq
print(a, b, c, d)

a, b, c, d, *e = seq
print(a, b, c, d, e)

a, b, *e, c, d = seq
print(a, b, c, d, e)

# a, b*, c, d* = seq
# a, b = seq
# *a = seq
*a, = seq
print(a)

print(seq)

a, *b = seq                     # first, rest
print(a, b)

a, b = seq[0], seq[1:]          # first, rest: traditional
print(a, b)

*a, b = seq                     # rest, last
print(a, b)

a, b = seq[:-1], seq[-1]        # rest, last: traditional
print(a, b)

a = b = c = 'spam'
print(a, b, c)

c = 'spam'
b = c
a = b
print(a, b, c)

a = b = 0
print(a, b)
a = b + 1
print(a, b)

a = b = []
b.append(42)
print(a, b)

a = []
b = []
b.append(42)
print(a, b)

a, b = [], []
print(a, b)

x = 1
x = x + 1
print(x)

x += 1
print(x)

S = 'spam'
S += 'SPAM'
print(S)

L = [1, 2]
L = L + [3]         # Concatenate, slower
print(L)
L.append(4)         # Faster, but in place
print(L)

L = L + [5, 6]      # Concatenate, slower
print(L)
L.extend([7, 8])    # Faster, but in place
print(L)

L += [9, 10]        # Mapped to L.extend([9, 10])
L = []
L += 'spam'         # += and extend allow any sequence, but + does not!
print(L)

L = [1, 2]
M = L               # L and M reference the same object
print(M)
M = L + [3, 4]      # Changes L but not M
print(M, L)

L = [1, 2]
L.append(3)         # Append is an in-place change
print(L)

L = L.append(4)     # But append returns None, not L
print(L)

print()             # Display a blank line
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)

print(x, y, z, sep='')      # Suppress separator
print(x, y, z, sep=', ')    # Custom separator

print(x, y, z, end='')      # Suppress the line break
print(x, y, x, end='')      # Two prints, same output line
print(x, y, z)
print(x, y, z, end='...\n')     # Custom line end

print(x, y, x, sep='...', end='!\n')        # Multiple keywords
print(x, y, z, end='!\n', sep='...')

print(x, y, z, sep='...', file=open('data.txt', 'w'))       # print to a file
print(x, y, z)              # Back to stdout
print(open('data.txt').read())                              # Display file text

text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)
print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))

import sys

sys.stdout.write('hello world\n')

temp = sys.stdout                       # Save for restoring later
sys.stdout = open('log.txt', 'a')       # Redirect prints to a file
print('spam')                           # Prints go to file, not here
print(1, 2, 3)
sys.stdout.close()                      # Flush output to disk
sys.stdout = temp                       # Restore original stream

print('back here')                      # Prints show up here again
print(open('log.txt').read())           # Result of earlier prints

log = open('log.txt', 'w')
print(1, 2, 3, file=log)
print(4, 5, 6, file = log)
log.close()
print(7, 8, 9)
print(open('log.txt').read())

sys.stderr.write(('Bad! * 8' + '\n'))
print('Bad!' * 8, file=sys.stderr)

X = 1                                               # Print: the easy way
Y = 2
print(X, Y)
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')      # Print: the hard way
print(X, Y, file=open('temp1', 'w'))                # Redirect text to file
open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n')      # Send to file automatically
print(open('temp1', 'rb').read())                    # Binary mode for bytes
print(open('temp2', 'rb').read())

print('spam')
print('spam', 'ham', 'eggs')


### Test you knowledge PG 370

### 1.  Name three ways that you can assign three variables to the same value.
""" You can use multiple-target assignments (A = B = C = 0), sequence assignment
    (A, B, C, = 0, 0, 0), or multiple assignment statements on three separate lines
    (A = 0, B = 0, C = 0). With the latter technique, as introduced in Ch 10, you can
    also string the three separate statements together on the same line by separating them
    with semicolons (A = 0;, B = 0; C = 0)
"""

### 2. Why might you need to care when assigning three variables to a mutable object?
""" If all three reference the same object, changing them in place from one will affect the
    others. This is true only for in-place changes to mutable objects like lists and
    dictionaries, for immutable object such as numbers and strings, this issue is irrelevant
"""

### 3. What is wrong with saying: L = L.sort()
""" The list sort method is like append in that it makes in-place changes to the subject
    list -- it returns None, not the list it changes. The assignment back to L sets L to
    None, not ot the sorted list. A newer built-in function, sorted, sorts any sequence
    and returns a new list with the sorting result; because this is not an in-place change,
    its result can be meaningfully assigned to a name.
"""

### 4. How might you use the print operation to send text to an external file?
""" To print to a file for a single print operation, you can use 3.X's print(X, file=F)
    call form, use 2X's extend print >> file, X statement form, or assign sys.stdout to
    a manually opened file before the print and restore the original after. You can also
    redirect all of a program's printed text to a file with special syntax in the system
    shell, but this is outside Python's scope.
"""