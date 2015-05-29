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
