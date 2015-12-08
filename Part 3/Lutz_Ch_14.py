__author__ = 'rolan_000'

############################################
#### Part 3: Statements and Syntax PG 319-469
###  CH 14: Iterations and Comprehensions
############################################

for x in [1, 2, 3, 4]:
    print(x ** 2, end=' ')
print()

for x in (1, 2, 3, 4,):
    print(x ** 3, end= ' ')
print()

print(open('script2.py').read())

f = open('script2.py')          # Read a four-line script file in this directory
print(f.readline())             # readline loads one line on each call
print(f.readline())
print(f.readline())
print(f.readline())             # Last lines may a a \n or not
print(f.readline())             # returns empty string at end-of-file

f = open('script2.py')          # __next__ loads one line on each call too
print(f.__next__())             # But raises an exception at end-of-file
print(f.__next__())             # use f.nest in 2.X or next(f) in 2.X or 3.X
print(f.__next__())
print(f.__next__())
# print(f.__next__())

for line in open('script2.py'):
    print(line.upper(), end='')

for line in open('script2.py').readlines():
    print(line.upper(), end='')

f = open('script2.py')
while True:
    line = f.readline()
    if not line:
        break
    print(line.upper(), end='')

f = open('script2.py')
print(f.__next__())
print(f.__next__())

f = open('script2.py')
print(next(f))
print(next(f))
print(f.__next__())
