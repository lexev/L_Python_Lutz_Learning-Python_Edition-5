__author__ = 'rolano'

############################################
#### Part 3: Statements and Syntax PG 319-469
###  CH 10: Introducing Python Statements
############################################


while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    try:
        print(int(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')


while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)

print('bye')

### Test Your Knowledge PG 336

### 1. What three things are required on a C-like language but omitted in Python?
""" C-like language require parentheses around the tests in some statements, semi-colons
    at the end of each statement, and braces around a nested block of code.
"""

### 2. How is a statement normally terminated in Python?
""" The end of a line terminates the statement that appears on that line. Alternatively,
    if more than one statement appears on the same line, they can be terminated with
    semicolons; similarly, if a statement spans many lines, you must terminate it by closing
    a bracketed syntactic pair.
"""

### 3. How are the statements in a nested block of code normally associated in Python?
""" The statements in a nested block are all indented the same number of tabs or spaces.
"""

### 4. How can you make a single statement span multiple lines?
""" You can make a statement span many lines by enclosing part of it in parentheses, square
    brackets, or curly brackets; the statement ends when Python sees a line that contains the
    closing part of tha pair.
"""

### 5. How can you code a compound statement on a single line?
""" The body of a compound statement can be move to the header line after the colon, but
    only ff the body consists of only non-compound statements.
"""

### 6. Is there any valid reason to type a semicolon at the end of a statement in Python?
""" Only when you need tp squeeze more than one statement onto a single line of code.
    Even then, this only works if all statements are non-compound, and it's discouraged
    because it can lead to code that is difficult to read.
"""

### 7. What is a try statement for?
""" The try statement is used to catch and recover from exceptions (errors) in a Python
    script. It's usually an alternative to manually checking for errors in you code.
"""

### 8. What is the most common coding mistake among Python beginners?
""" Forgetting to type colon characters at the end of the header line in a compound
    statement is the most common beginner's mistake. If you're new to Python and haven't
    made it yet, you will soo.
"""
