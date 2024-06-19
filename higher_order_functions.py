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