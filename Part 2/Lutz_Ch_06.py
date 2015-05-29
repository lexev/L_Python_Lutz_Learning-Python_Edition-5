__author__ = 'rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 6: The Dynamic Typing Interlude
############################################

### PG 186 Test your knowedge

### 1. Consider the following three statements. Do they change the value for A?
###     a = "spam"
###     b = A
###     b = "shrubbery"
""" No: A still prints as "spam". When B is assigned to the string "shrubbery", all that
    Happens is that the variable B is reset to point to the new string object. A and B
    initially share (i.e. reference/ point to) the same single string object "spam", but
    two names are never linked together in python. Thus, setting B to a different object
    has no effect on A. The same would be true if the last statement here were B = B +
    'shrubbery', by the way--the concatenation would make a new object fot its result,
    which would then be assigned to B only. We can never overwrite a string (or number, or
    tuple) in place because strings are immutable.
"""

### 2. Consider these three statements. Do they change the value of A?
###     A = ["spam"]
###     B = A
###     B[0] = "shrubbery"
""" Yes: A now prints as ["shrubbery"]. Technically, we haven't really changed either A or
    B; instead, we've changed part of the object they both reference (point to) by
    overwriting that object in place through the variable B. Because A references the same
    object as B, the update is reflected in A as well.
"""

### 3. How about these-- is A changed now?
###     A = ["spam"]
###     B = A[:]
###     B[0] = "shrubbery"
""" No: A still prints as ["spam"]. The in-place assignment through B has no effect this time
    because the slice expression made a copy of the list object before it was assigned to B.
    After the second assignment statement, there are two different list objects that have the
    same value (in Python, we say they are ==, but no is). The third statement changes the
    value of the list object pointed to by B, but not pointed to by A.
"""
