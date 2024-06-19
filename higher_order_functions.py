#-------------------Walrus Operator-------------------
# The walrus operator is a new feature in Python 3.8 that allows you to assign values to variables as part of an expression.
# It is denoted by the := operator.
# The walrus operator is useful when you want to assign a value to a variable and use that value in an expression.

# # Without walrus operator
# name = input("Enter your name: ")
# if len(name) > 0:
#     print(f"Hello, {name}")
# else:
#     print("Name cannot be empty")

# # # With walrus operator
# if (name := input("Enter your name: ")):
#     print(f"Hello, {name}")
# else:
#     print("Name cannot be empty")

print(happy := True) # True 
# In the above example, the walrus operator is used to assign the value of input("Enter your name: ") to the variable name and use it in the if condition.
# This makes the code more concise and readable.

#-------------------Assign function to a variable-------------------
# In Python, functions are first-class objects, which means they can be assigned to variables, passed as arguments to other functions, and returned from other functions.

def greet(name):
    return f"Hello, {name}"

print(greet)
greeting = greet # greeting gets the same memory location as greet to keep a reference to the function
print(greeting("Alice")) # Hello, Alice

#Another example
out = print # Assign the print function to the variable out
out("Hello, World!") # Hello, World!

#-------------------Higer Order Functions-------------------
# A higher-order function is a function that takes one or more functions as arguments or returns a function as its result.
# Higher-order functions are used to abstract and encapsulate common patterns in code.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def apply_operation(operation, a, b):
    return operation(a, b)

result = apply_operation(add, 5, 3)
print(result) # 8

result = apply_operation(subtract, 5, 3)
print(result) # 2

#-------------------Lambda Functions-------------------
# Lambda functions, also known as anonymous functions, are small, inline functions that are defined using the lambda keyword.
# Lambda functions can take any number of arguments but can only have one expression.
# Lambda functions are often used as arguments to higher-order functions or in situations where a small function is needed for a short period of time.

# Syntax: lambda arguments: expression

# Example 1: Lambda function with one argument
square = lambda x: x**2
print(square(5)) # 25

# Example 2: Lambda function with multiple arguments
volume = lambda l, w, h: l * w * h
print(volume(2, 3, 4)) # 24

# Example 3: Using lambda function as an argument to a higher-order function
def apply_operation(operation, a, b):
    return operation(a, b)

result = apply_operation(lambda x, y: x + y, 5, 3)
print(result) # 8

age_check = lambda age: "Adult" if age >= 18 else "Minor"
print(age_check(18))

#-------------------Sorting iterables-------------------
# Using sort() method for lists. Syntax list.sort(key=None, reverse=False)
# and sorted() function for all iterables. Syntax sorted(iterable, key=None, reverse=False)

# The sort() method is used to sort lists in-place.
# The sort() method modifies the original list and does not return a new list.

# Syntax: list.sort(key=None, reverse=False)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort() # Sort the numbers in ascending order
print(numbers) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]