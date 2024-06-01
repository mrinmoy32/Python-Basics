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