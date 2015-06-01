__author__ = 'rolando'

############################################
#### Part 2: Types and Operations PG 90-315
###  CH 7: String Fundamentals
############################################

title = "Meaning " 'of' " Life"  # Implicit Concatenation
print(title)

print('knight\'s', "knight\"s")  # Escape sequence

s = 'a\nb\tc'
print(s)
print(len(s))

s = 'a\0b\0c'
print(s)
print(len(s))

s = '\001\002\x03'
print(s)
print(len(s))

S = "s\tp\na\x00m"
print(S)
print(len(S))

x = "C:\py\code"  # Keeps \ literally (and displays it as \\)
print(x)

path = r'C:\new\text.dat'
print(path)
print(len(path))

mantra = """Always look
   on the bright
side of life"""
print(mantra)

menu = """spam      # comments here added to string!
    eggs            # ditto
    """
print(menu)

menu = (
    "spam\n"    # comments here ignored
    "eggs\n"    # but newlines not automatic
)
print(menu)

print(len('abc'))           # Length: number of items
print('abc' + 'def')        # Concatenation: a new string
print('Ni!' * 4)            # Repetition

myjob = "hacker"
for c in myjob: print(c, end=' ')   # Step through items, print each (3.X form)
print("k" in myjob)                 # Found
print("z" in myjob)                 # Not found
print('spam' in 'abcspamdef')       # Substring search, no position returned

S = 'spam'
print(S[0], S[-2])                  # Indexing from front or end
print(S[1:3], S[1:], S[:-1])        # Slicing: extract a section

S = 'abcdefghijklmnop'
print(S[1:10:2])                    # Skipping items
print(S[::2])
print(S[::-1])                      # Reversing items

S = 'abcedfg'
print(S[5:1:-1])                    # Bounds roles differ

print('spam'[1:3])                  # Slicing Syntax
print('spam'[slice(1, 3)])          # Slice object with index syntax + object
print('spam'[::-1])
print('spam'[slice(None, None, -1)])

print(int("42"), str(42))           # Convert from/to string
print(repr(42))                     # Convert to as-code string

print(str('spam'), repr('spam'))

S = "42"
I = 1
# print(S + I)
print(int(S) + I)                   # Force addition
print(S + str(I))                   # Force concatenation

print(str(3.1415), float("1.5"))
text = "1.234E-10"
print(float(text))                  # Show more digits before 2.7 and 3.1

print(ord('s'))
print(chr(115))
S = '5'
S = chr(ord(S) + 1)
print(S)
S = chr(ord(S) + 1)
print(S)
print(int('5'))
print(ord('5') - ord('0'))

B = '1101'                          # Convert binary digits to integer with ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

print(int('1101', 2))               # Convert binary to integer: Built-in
print(bin(13))                      # Convert integer to binary: Built-in

S = 'spam'
# S[0] = 'x'
S = S + 'SPAM!'
print(S)
S = S[:4] + "Burger" + S[-1]
print(S)

S = 'splot'
S = S.replace('pl', 'pamal')
print(S)

print('That is %d %s bird!' % (1, 'dead'))          # Format expression: all pythons
print('That is {0} {1} bird!'.format(1, 'dead'))    # Format method in 2.6, 2.7, 3.X

S = 'spam'
result = S.find('pa')               # Call the find method to look for 'pa' in string S
print(result)

S = 'spammy'
S = S[:3] + 'xx' + S[5:]        # Slice sections from s
print(S)

S = 'spammy'
S = S.replace('mm', 'xx')       # Replace all mm with xx in S
print(S)
print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')          # search for position
print(where)                    # occurs at offset 4
S = S[:where] + 'EGGS' + S[(where + 4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))        # Replace all
print(S.replace('SPAM', 'EGGS', 1))     # Replace one

S = 'spammy'
L = list(S)
print(L)

L[3] = 'x'
L[4] = 'x'
print(L)
S = ''.join(L)

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)

line = 'bob,hacker,40'
print(line.split(','))
line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))
line = "The knights who say Ni!\n"
print(line)
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))

print(line)
print(line.find('Ni') != -1)
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))
print(line[-len(sub):] == sub)