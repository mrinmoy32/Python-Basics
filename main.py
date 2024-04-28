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
# Python dictionaries, also known as maps or associative arrays in other languages, 
# are unordered collections of key-value pairs.
string_to_int_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
int_to_string_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
mixed_dict = {"name": "Alice", "age": 30, "is_student": False, "grades": [85, 92, 78]}
tuple_key_dict = {(1, 2): "value1", (3, 4): "value2", (5, 6): "value3"}
nested_dict = {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}
mixed_keys_dict = {1: "one", "two": 2, (3, 4): "three-four"}
dict_with_lists = {"numbers": [1, 2, 3], "letters": ['a', 'b', 'c']}
empty_dict = {}
