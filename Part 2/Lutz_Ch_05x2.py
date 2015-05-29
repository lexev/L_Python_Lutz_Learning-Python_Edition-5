__author__ = 'rolando'
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)                     # Order matters in sequences
print(set(L1) == set(L2))           # Order-neural equality
print(sorted(L1) == sorted(L2))     # Similar but results ordered

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print('bob' in engineers)           # Is bob an engineer?
print(engineers & managers)         # Who is both engineer and manager?
print(engineers | managers)         # All people in either category
print(engineers - managers)         # Engineers who are not managers
print(managers - engineers)         # Managers who are no engineers
print(engineers > managers)         # Are all managers engineers? (superset)


### PG 171 Booleans

print(type(True))
print(isinstance(True, int))
print(True == 1)                    # Same value
print(True is 1)                    # but a different object: see the next chapter
print(True or False)                # Same as: 1 or 2
print(True + 4)

## Test your knowledge

### 1 What is the value of the expression 2 * (3 + 4) in python?
""" 14
"""

### 2. What is the value of the expression 2 * 3 + 4 in python?
""" 10
"""

### 3. What is the value of the expression 2 + 3 * 4 in python?
""" 14
"""

### 4. What tools can you use to find a number's square root, as well as its square?
""" Functions for obtaining the square root, as well as pi, tangents, and more, are available
    in the imported math module. To fin a number's square, use either the exponent expression
    X ** w or the built-in function pow(X, 2). Either of theses last two can also compute
    the square root when a power of 0.5 (e.g., X ** .5).
"""

### 5. What is the type of the result of the expression 1 + 2.0 + 3?
""" The result will be a floating-point number: the integers are converted up to floating
    point, the most comp;ex type in the expression, and floating-point math is used to
    evaluate it.
"""

### 6. How can you truncate and round a floating-point number?
""" The int(N) and math.trunc(N) functions truncate, and the round(N, digits) function rounds
    We can also compute the floor with math.floor(N) and reound for display with string
    formatting operations.
    """

### 7. How can you convert an integer to a floating-point number?
""" The float(I) function converts an integer to a floating point, mixing an integer with a
    floating-point within an expression will result in a conversion as well. In some sense,
    Python 3.X / division converts too-- it always returns a floating-point result that
    includes the remainder, even if both operands are integers.
"""

### 8. How would you display an integer in octal, hexadecimal, or binary notation?
""" The oct(I) and hex(I) built-in functions return the octal and hexadeciml string forms
    for an integer. The bin(I) call also returns a number's binary digits string in Pythons
    2.6, 3.0, and later. The % string formatting expresion and format string method also
    provide targets for such conversions.
"""

### 9. How might you convert an octal, hexadecimal, o binary string to a plain integer?
""" The int(S, base) function can be used to convert from octal and hexadecimal strings
    to normal integers (pass in 8, 16, or 2 for the base). The eval(S) function can be used
    for this purpose too, but it's more expensive to run and can have security issues.
    Note that integers are always stored in binary form in computer memory, these are just
    display string format conversions.
"""
