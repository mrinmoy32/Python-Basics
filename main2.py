# Continuation from main.py file
# Math Functions
import math #importing the math module
pi = 3.14
neg = - 32
x,y,z = 1,2,-3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(neg))
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x,y,z))
print(min(x,y,z))

# String slicing (create substring from a string)
# using indexing[] -> [start:stop:step]
name = "Virat Kohli"
first_name = name[0:5] #Also print((name[:5])) would work
last_name = name[6:11] # print((name[4:])) would work
print(first_name)
print(last_name)
# lets use optional step (step is 1 by default)
funky_name = name[::2]
print(funky_name)
reversed_name = name[::-1] # to reverse a string in python
print(reversed_name)

# using slice()