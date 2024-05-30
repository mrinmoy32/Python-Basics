# nested loops 
#(the inner loop will finish all of it's iteration before finishing one iteration of the outer loop)

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(0,rows):
    for j in range(0,columns):
        print(symbol, end="") #end="" prevnts moving to new line
    print() # print a new line