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

# Sorting in descending order
sorted_numbers = sorted(numbers, reverse=True) # Sort the numbers in descending order
print(sorted_numbers) # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# Sorting a tuple
fruits = ("apple", "banana", "cherry", "date")
sorted_fruits = sorted(fruits)
print(sorted_fruits) # ['apple', 'banana', 'cherry', 'date']

# Sorting a tuple with a custom key
fruits = ("apple", "banana", "cherry", "date")
sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit))
print(sorted_fruits) # ['date', 'apple', 'banana', 'cherry']

# Sorting a dictionary by keys
person = {"name": "Alice", "age": 25, "city": "New York"}
sorted_person = sorted(person)
for key in sorted_person:
    print(key, person[key])

# Sorting a dictionary by values
person = {"name": "Alice", "country": "USA", "city": "New York"}
sorted_person = sorted(person, key=lambda key: person[key])
for key in sorted_person:
    print(key, person[key])

# Sorting a tuple of dictionaries by a specific key
people = (
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
)
sorted_people = sorted(people, key=lambda person: person["age"])
for person in sorted_people:
    print(person["name"], person["age"])

#-------------------Map function-------------------
# The map() function is used to apply a function to each element of an iterable (such as a list, tuple, or dictionary) and returns an object of the map class, that can be converted to a list, tuple, or dictionary.
# The map() function takes two arguments: a function and an iterable.
# The function is applied to each element of the iterable, and the results are returned as a new iterable.

# Syntax: map(function, iterable)

# Example 1: Using map() with a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print((squared_numbers)) # <map object at 0x7f8b1c7b5d30>
print(list(squared_numbers)) # [1, 4, 9, 16, 25]

# Example 2: Using map() with a tuple
fruits = ("apple", "banana", "cherry", "date")
uppercase_fruits = map(lambda fruit: fruit.upper(), fruits)
print(list(uppercase_fruits)) # ['APPLE', 'BANANA', 'CHERRY', 'DATE']
print(tuple(uppercase_fruits)) # ('APPLE', 'BANANA', 'CHERRY', 'DATE')

# Example 3: Using map() with a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
keys = map(lambda key: key.upper(), person.keys())
print(list(keys)) # ['NAME', 'AGE', 'CITY']

# Example 4: Using map() with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sums = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sums)) # [5, 7, 9]

# Example 5: Using map() with a list of tuples
currency_rates = [("USD", 1.0), ("EUR", 0.85), ("GBP", 0.75)]
converted_rates = map(lambda rate: (rate[0], rate[1] * 100), currency_rates)
print(list(converted_rates)) # [('USD', 100.0), ('EUR', 85.0), ('GBP', 75.0)]

#-------------------Filter function-------------------
# The filter() function is used to filter elements from an iterable (such as a list, tuple, or dictionary) based on a condition.
# The filter() function takes two arguments: a function that returns a boolean value (True or False) and an iterable. It returns an object of the filter class, that can be converted to a list, tuple, or dictionary.
# The function is applied to each element of the iterable, and only the elements for which the function returns True are included in the result.

# Syntax: filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda number: number%2 == 0, numbers)
print(set(even_numbers)) # {2, 4, 6, 8, 10}

fruits = ("apple", "banana", "cherry", "date")
def check_long_fruit(fruit):
    return len(fruit) > 5
long_fruits = filter(check_long_fruit, fruits) # without lambda function
print(tuple(long_fruits)) # ('banana', 'cherry')

person = {"name": "Alice", "age": 25, "city": "New York"}
keys_starting_with_a = filter(lambda key: key.startswith("a"), person.keys())
print(list(keys_starting_with_a)) # ['age']

# Using filter() with a list of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 20}
]
adults = filter(lambda person: person["age"] >= 18, people)
for person in adults:
    print(person["name"], person["age"])

#-------------------Reduce function-------------------
# The reduce() function is used to apply a function to the elements of an iterable (such as a list, tuple, or dictionary) cumulatively and returns a single value.
# The reduce() function is part of the functools module in Python.
# The reduce() function takes two arguments: a function that takes two arguments and an iterable.
# The function is applied to the first two elements of the iterable, and then the result is applied to the next element, and so on, until the iterable is exhausted.

# Syntax: reduce(function, iterable)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers) # 15

birds = ("crow", "sparrow", "eagle", "pigeon")
concatenated_birds = reduce(lambda x, y: x + " " + y, birds)
print(concatenated_birds) # crow sparrow eagle pigeon

# Using reduce() with a list of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]
total_age = reduce(lambda acc, person: acc + person["age"], people, 0)
# The rduce function takes 3 arguments: the function, the iterable, and the initial value of the accumulator.
# The 2nd argumnet must be an iterable.
print(total_age) # 75

#-------------------List Comprehensions-------------------
# List comprehensions provide a concise way to create lists in Python.
# List comprehensions are a more readable and efficient way to create lists compared to using loops.
# List comprehensions consist of square brackets containing an expression followed by a for clause, then zero or more for or if clauses.

# Syntax: [expression for item in iterable if condition]

# List comprehensions can be used to create lists, sets, dictionaries, and even nested lists.

# Example 0: Using a list comprehension to create a list of numbers multiplied by 2
multiplied_by_2 = [x*2 for x in range(1, 6)]
print(multiplied_by_2) # [2, 4, 6, 8, 10]

# Example 1: Using a list comprehension to create a list of squares
numbers = (1, 2, 3, 4, 5)    # we can use list, tuple, set, dictionary here as iterable
squared_numbers = [numbers**2 for numbers in numbers]
print(squared_numbers) # [1, 4, 9, 16, 25]

# Example 2: Using a list comprehension with a condition
even_numbers = [number for number in numbers if number%2 == 0]
print(even_numbers) # [2, 4]

# Example 3: Using a list comprehension with multiple conditions
scores = [80, 90, 70, 85, 65]
pass_scores = ["Pass" if score >= 80 else "Fail" for score in scores]
print(pass_scores) # ['Pass', 'Pass', 'Fail', 'Pass', 'Fail']

# Example 4: Using a list comprehension with nested loops
colors = ["red", "green", "blue"]
objects = ["car", "house", "tree"]
color_objects = [(color, object) for color in colors for object in objects]
print(color_objects) # [('red', 'car'), ('red', 'house'), ('red', 'tree'), ('green', 'car'), ('green', 'house'), ('green', 'tree'), ('blue', 'car'), ('blue', 'house'), ('blue', 'tree')]

# Example 5: Using a list comprehension with a function
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(number) for number in numbers]
print(squared_numbers) # [1, 4, 9, 16, 25]

# Example 6: Using a list comprehension with a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
person_items = [f"{key}: {value}" for key, value in person.items()]
print(person_items) # ['name: Alice', 'age: 25', 'city: New York']

# Example 7: Using a list comprehension with a set
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_set = {number**2 for number in numbers}
print(squares_set) # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

# Example 8: Using a list comprehension with a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [number for row in matrix for number in row]
print(flattened_matrix) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#-------------------Tuple Comprehensions-------------------
# Tuple comprehensions are not directly supported in Python.
# However, you can use a generator expression with the tuple() function to create a tuple from the generator.

# Example: Using a generator expression with the tuple() function
numbers = [1, 2, 3, 4, 5]
even_numbers = tuple(number for number in numbers if number%2 == 0)
print(even_numbers) # (2, 4)

# Create a tuple of squares of numbers from 1 to 5
squares_tuple = tuple(x**2 for x in range(1, 6))
print(squares_tuple)  # Output: (1, 4, 9, 16, 25)