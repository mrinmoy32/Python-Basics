# Working with files in python
#File detection
import os
path = "C:\\Users\\mrinm\\OneDrive\\Desktop\\file_for_python.txt" # need \\ in python (escape sequence for \)

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("It is a directory")
else:
    print("That location doesn't exist")