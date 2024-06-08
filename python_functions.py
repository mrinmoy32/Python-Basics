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
print(round(abs(float(input("Enter a whole positive number: ")))))

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

welcome(title="Mr.", first="Mrinmoy", last="pal")
