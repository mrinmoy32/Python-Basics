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