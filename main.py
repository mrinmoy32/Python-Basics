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
print("variables-----------")
# string
greet = "Hi, my name is Mrinmoy"
print(greet)
print(5 * "Hi Mrinmoy ") # prints 5 times
num1 = "32"
num2 = "18"
print(2 * int(num1), num1)
print(4 * str(int(num1)+int(num2)))
#To put a " inside string use \"
print("double quote\"")
#multi line string
multiLineStr = '''This is a multiine
string and
this will keep going'''
print(multiLineStr)
# number
year = 2024
temperature = 41.7 
print(temperature, "deg C and", year)
print(type(year), type(temperature))
# List
# A list in Python is an ordered, indexed, "mutable" collection of elements, can have duplicate elements
# allowing for the storage and manipulation of heterogeneous data types.
ages = [19, 27, 21]
print(ages) # [19, 27, 21]
print(ages[1]) # 27
colors = ['red', "green", "blue"]
print(colors)
mixedList = [0, "black", 1.5, "white", ["nested array", -3], True]
print(mixedList)
print(mixedList[3])
singleElementList = [31]
print(singleElementList)
emptyList = []
print(emptyList)
# Tuple
# Python tuples are ordered, indexed collections of elements, similar to lists, but they are "immutable", 
# meaning once created, their contents cannot be changed. Tuples are created using parentheses ().
# Tuples can have duplicate elements 
randomNumbers = (1,0,4,8,6)
print(randomNumbers) # (1, 0, 4, 8, 6)
print(randomNumbers[3]) # 8
tuple_of_strings = ("apple", "banana", "orange", "grape")
print(tuple_of_strings)
mixed_tuple = (1, "apple", True, 3.14)
print(mixed_tuple)
nested_tuple = (("a", "b"), (1, 2, 3), ("x", "y", "z"))
print(nested_tuple)
single_element_tuple = (42,) #need to add a comma to make it work as sigle element tuple
print(single_element_tuple)
tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [True, False])
print(tuple_of_lists)
tuple_of_dicts = ({'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25})
print(tuple_of_dicts)
empty_tuple = ()
print(empty_tuple)
# Set (collection which is unordered, unindexed, mutable. But no duplicate values)
utensils = {"fork", "spoon", "knife"}
for x in utensils:
    print(x)
dishes = {"bowl", "plate", "cup"}
mixed_set = {1, "apple", 3.14, (1, 2)}
print(mixed_set)  # Output: {3.14, 1, (1, 2), 'apple'}
# Dictionaries or Maps
# Python dictionaries, also known as maps or associative arrays in other languages, 
# are unordered collections of key-value pairs. 
# Mutable, Ordered (maintain the insertion order of key-value pairs), Not Indexed, No Duplicate Keys
# Fast because they use hasing
string_to_int_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
int_to_string_dict = {1: "one", 2: "two", 3: "three", 4: "four"}
mixed_dict = {"name": "Alice", "age": 30, "is_student": False, "grades": [85, 92, 78]}
tuple_key_dict = {(1, 2): "value1", (3, 4): "value2", (5, 6): "value3"}
nested_dict = {"person1": {"name": "Alice", "age": 30}, "person2": {"name": "Bob", "age": 25}}
mixed_keys_dict = {1: "one", "two": 2, (3, 4): "three-four"}
dict_with_lists = {"numbers": [1, 2, 3], "letters": ['a', 'b', 'c']}
empty_dict = {}
print(mixed_keys_dict) # {1: 'one', 'two': 2, (3, 4): 'three-four'}
print(mixed_keys_dict[1]) # one
print(mixed_keys_dict['two']) # 2
print(mixed_keys_dict[(3,4)]) # three-four


# Multiple Assignments
name, age, active = "Virat", 35, True
print(name)
print(age)
print(active)

virat = raina = rohit = ashwin = 50
print(virat)
print(raina)
print(rohit)
print(ashwin)

#Arithmetic operations
print("Arithmetic operations-----------")
print("5 + 3 =", 5+3)
print("5 - 3 =", 5-3)
print("5 * 3 =", 5*3)
print("5 / 3 =", 5/3)
print("5 % 3 =", 5%3) #modulo => returns the remainder of division 
print("5 ** 3 =", 5**3) #4 to the power 3 => 4^3
print("5 // 3 =", 5//3) #floor division => returns the quotient of division, rounded to the nearest integer

# Assignment operators
print("Assignment operators-----------")
a = 30
print(a)
a += 3
print(a)
a -= 3
print(a)
a *= 3
print(a)
a /= 3
print(a)

# Comparision operators
print("Comparision operators-----------")
b = (3 > 32) 
print (b)
b = (3 < 32) 
print (b)
b = (3 >= 32) 
print (b)
b = (3 <= 32) 
print (b)
b = (3 == 32) 
print (b)
b = (3 != 32) 
print (b)

# Logical operators
print("Logical operators-----------")
a = True
b = False
print(a and b)
print(a or b)
print(not b)

# TypeCasting 
print("TypeCasting-----------")
a = "3434"
a = int(a)
print(a + 5)

height = 170
print('Height is' , height)
print('Height is ' + str(height))

human = True
print("Are you a human: " + str(human))

print(33)
print(float(33)) #33.0
print(33/11) #Ans: 3.0   division always returns float

#String Methods
name = "virat kohli"
word = "ABcDefG"
numberStr = "1234"
print(len(name)) # length of the sting
print(name.find("h")) # index of h i.e. 8
print(name.capitalize()) # makes the 1st letter capital
print(name.upper())
print(word.lower())
print(numberStr.isdigit()) # True as only digits are there in numberStr
print(name.isalpha()) #False as name contains a space. only alphabets have to be there
print(name.count("i")) #counts number of occurances of i, here it's 2
print(name.replace("i", "a"))

# Accepting user inputs
name = input("What is your name? : ")
print("Name entered is: ", name, "\n It is of Data type:", type(name))
age = input("What is your age? : ")
print("Age entered is: ", age, "\n It is of Data type:", type(age)) #all user inputs are accepted as string only
age = int(age) # we can then cast the input to other data types
print("Now Data type of age is: ", type(age))
height = float(input("How tall are you? : "))
print("Height entered is: ", height, "\n It is of Data type:", type(height))