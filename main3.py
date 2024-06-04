# nested loops 
#(the inner loop will finish all of it's iteration before finishing one iteration of the outer loop)

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="") #end="" prevnts moving to new line
#     print() # print a new line

# Loop control statements
# change a loop execution from it's normal sequance 

# break = used to terminate a loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     # name = input("Enter your name: ")
#     if name != "":
#         break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    # print(i, end="")

for i in range(20):
    if i+1==13:
        pass # does noting, hence 13 won't be printed
    # else:
        # print(i+1)
    
# List methods and 2D list
foods = ["pizza", "burger", "hotdog", "pasta", "pudding"]

foods[1] = "Biryani"
foods.append("ice cream")
foods.remove("hotdog")
foods.pop() #ice cream is popped
foods.insert(0,"cake")
foods.sort()
# foods.clear()
for item in foods:
    print(item)

#Multidimentional List/ Nested List
#2D list = List of lists
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "biryani", "salad"]
dessert = ["cake", "ice cream", ["pastry", "jalebi"]]

food = [drinks, dinner, dessert]
print(food) # [['coffee', 'soda', 'tea'], ['pizza', 'biryani', 'salad'], ['cake', 'ice cream']]
print(food[0]) # ['coffee', 'soda', 'tea']
print(food[0][0]) # coffee
print(food[2][2][0]) # pastry

#tuple methods

player = ("Virat", 35, "male")
print(player.count("Virat"))
print(player.index("male"))

for item in player:
    print(item)
if "Virat" in player:
    print("Virat is here!")

# Set methods
# Set (collection which is unordered, unindexed, mutable. But no duplicate values)
utensils = {"fork", "spoon", "knife"}
utensils.add("Tong")
utensils.remove("spoon")
# utensils.clear()
dishes = {"bowl", "plate", "cup", "knife"}
# utensils.update(dishes) # contents of dishes added in utensils
# for x in utensils:
#     print(x)
dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)
print(dishes.difference(utensils)) #items dishes has but but utensils doesn't
print(utensils.difference(dishes)) #items utensils has but but dishes doesn't

print(utensils.intersection(dishes)) #show only common items

# Dictionary methods
mixed_dict = {"name": "Alice", "age": 30, "is_student": False, "grades": [85, 92, 78]}
print(mixed_dict["name"]) #Alice
# print(mixed_dict["addrerss"]) #KeyError: 'addrerss' key deosn't exist
print(mixed_dict.get('addrerss')) #none
print(mixed_dict.keys())
print(mixed_dict.values())
print(mixed_dict.items())
mixed_dict.update({"yob": 2000})
mixed_dict.update({"is_student": True})
mixed_dict.pop("grades")

# for key in mixed_dict:
#   print(key) # prints the keys
# for key in mixed_dict:
#   print(mixed_dict[key]) # prints the values
# for value in mixed_dict.values(): # loops through the values
#   print(value) # prints the values
for key, value in mixed_dict.items():
  print(key, ":", value)

# index operator []
# gives access to a sequence's element (str, list, tuples)
name = "sachin Tendulkar"

if(name[0].islower()):
    name = name.capitalize()
print(name)
first_name = name[:6].upper()
last_name = name[7:].lower()
print(first_name)
print(last_name)