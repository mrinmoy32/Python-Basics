# Continuation from main.py file
# Math Functions -----------------------
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

# String slicing (create substring from a string) ---------------------
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
website1 = "https://google.com"
website2 = "https://wikipedia.com"
slice = slice(8,-4) #creating a slice object by calling the slice function. eg. slice(start,stop,step) step is optional
print(website1[slice])
print(website2[slice])

#If Statement --------------------
age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

# while loop
# while 1==1:
#     print("I am stuck in an infinite loop!")

name = ""
while len(name)==0:
    name = input("Enter your name: ")

#Another way
subject = None
while not subject:
    subject = input("Enter subject: ")