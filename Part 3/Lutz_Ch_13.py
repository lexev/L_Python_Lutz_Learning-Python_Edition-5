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
