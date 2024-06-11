# Function (A block of code which is executed only when it is called)

def hello(first_name, last_name, year):
    print("Hello" + " " + first_name + " " + last_name)
    print("Happy New Year!" + " " + str(year))
hello("Mrinmoy", "Pal", 2024)

#return statement (the value or object python sends back to the caller)
def sum(num1, num2):
    return num1 + num2
print(sum(2,3))

# keyword arguments (arguments prceded by an identifier when we pass them to a function
# The order of the arguments doesn't ,atter unlike the positional arguments
# python knows the names of the arguments that our function receives)

def greet(first_name, last_name, year):
    print("Hello" + " " + first_name + " " + last_name)
    print("Happy New Year!" + " " + str(year))
greet(year=2024, last_name="Pal", first_name="Mrinmoy")

# nested function call
print(round(abs(float(-3.3456))))
# print(round(abs(float(input("Enter a whole positive number: ")))))

# Variable Scope
# scope => The region that a variable is recognised
# A variable is only available from inside the region it is created
# A global and locally scoped versions of a varible can be created

name = "Virat"  # globally scoped

def display_name():
    name = "Sachin" # locally scoped
    print(name)

display_name() # Sachin
print(name) # Virat

#Scope chain => LEGB: Local > Enclosing > Global > Built-in 

## *args (parameter that will pack all arguments into a tuple
# useful when a function needs to accept a varying amount of arguments)
def add(num1, num2):
    return num1 + num2
print(add(2,3))

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum(1,2,3,4))

def dispaly_items(*items):
    print(items)
dispaly_items("One", 2, True, None)

## *kwargs (parameter that will pack all arguments into a dictionary
# useful when a function needs to accept a varying amount of arguments)

def welcome(**kwargs):
    print('Hello', end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
    print()

welcome(title="Mr.", first="Mrinmoy", last="pal")

#format method
# The str.format() method is an optional method that gives users more control when displaying the output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format("cow", "moon"))  
print("The {} jumped over the {}".format(animal, item)) # more elegant way. The {} are known as format field
# these format fields work as placeholders for values or variable 
print("The {1} jumped over the {0}".format(animal, item)) #positional argumnets
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #keyword argumnets
print("The {item} jumped over the {item}".format(animal="cow", item="moon")) #keyword argumnets

text = "The {} jumped over the {}"
print(text.format(animal,item))
#lets add some padding
name = "Mrinmoy"
person = "friend"
print("Hi I'm {1}. Nice to meet you {0}".format(person, name))
print("Hi I'm {:10}. Nice to meet you {}".format(name, person)) # 10 spaces to the right
print("Hi I'm {0:>10}. Nice to meet you {1}".format(name, person)) # 
print("Hi I'm {name:<10}. Nice to meet you {person}".format(name="virat", person="Rohit")) # 
print("Hi I'm {0:^10}. Nice to meet you {1}".format(name, person)) # 

#number format
num_pi = 3.14159
print("The number pi is {:.2f}".format(num_pi)) # upto 2 dec place
amount = 58755754543
print("The amount is {:,}".format(amount)) #58,755,754,543
print("The amount is {:b}".format(amount)) #binary representation
print("The amount is {:o}".format(amount)) #octal representation
print("The amount is {:x}".format(amount)) #hex representation
print("The amount is {:e}".format(amount)) #scientific representation

#random module
import random
x = random.randint(1,6) # random num bet 1-6
print(x)
y = random.random() # random float
print(y) 
my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
random.shuffle(cards) # shuffles the list
print(cards)