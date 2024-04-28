print("Hello World")

# single line comment

"""
This is a multi-line comment.
It can span multiple lines.
These lines are not executed as code.
"""

'''This also works
for multiline comment'''

#------------ variables -------------
# string
greet = "Hi, my name is Mrinmoy"
print(greet)
# number
year = 2024
temperature = 41.7 
print(temperature, "deg C and", year)
# List
ages = [19, 27, 21]
print(ages)
colors = ['red', "green", "blue"]
print(colors)
mixedList = [0, "black", 1.5, "white", ["nested array", -3], True]
print(mixedList)
singleElementList = [31]
print(singleElementList)
emptyList = []
print(emptyList)
# Tuple
# Python tuples are ordered collections of elements, similar to lists, but they are immutable, 
# meaning once created, their contents cannot be changed. Tuples are created using parentheses ().
randomNumbers = (1,0,4,8,6)
print(randomNumbers)
tuple_of_strings = ("apple", "banana", "orange", "grape")
print(tuple_of_strings)
mixed_tuple = (1, "apple", True, 3.14)
print(mixed_tuple)
nested_tuple = (("a", "b"), (1, 2, 3), ("x", "y", "z"))
print(nested_tuple)
single_element_tuple = (42,) #need to add a comman to make it work as sigle element tuple
print(single_element_tuple)
tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [True, False])
print(tuple_of_lists)
tuple_of_dicts = ({'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25})
print(tuple_of_dicts)
empty_tuple = ()
print(empty_tuple)
# Dictionaries or Maps
