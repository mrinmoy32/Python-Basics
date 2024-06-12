# Working with files in python
#File detection
import os
path = "C:\\Users\\mrinm\\OneDrive\\Desktop\\file_for_python.txt" # need \\ in python (escape sequence for \)

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path): # we can also
        print("It is a directory")
else:
    print("That location doesn't exist")

# create a file

try:
    with open('example.txt', 'w') as file: # in place of 'example.txt' you can use any file path(C:\\Users\\user\\Desktop\\example.txt)
        print('Empty file','example.txt', 'created successfully. Will write to this file later')
except:
    print('Error occurred while creating file')

# write to a file

text = "This is a sample text file. Have a nice day!"
try:
    with open('text.txt', 'w') as file: # in place of 'text.txt' you can use any file path(C:\\Users\\user\\Desktop\\text.txt)
        file.write(text)
        print('text.txt', 'File written successfully')
except:
    print('Error occurred while writing to file')

# now write example.txt

text = "This is a example text file. Thanks!"
try:
    with open('example.txt', 'w') as file: # in place of 'text.txt' you can use any file path(C:\\Users\\user\\Desktop\\example.txt)
        file.write(text)
        print('example.txt', 'File written successfully')
except:
    print('Error occurred while writing to file')

# read a file

try:
    with open('example.txt', 'r') as file: # in place of 'example.txt' you can use any file path(C:\\Users\\user\\Desktop\\example.txt)
        print(file.read())
        print(file.closed) # check if file is closed
except FileNotFoundError:
    print('File not found while reading')

# copy a file

try:
    with open('text.txt', 'r') as source_file:
        with open('C:\\Python_BootCamp\\Python-Basics\\files_in_python\\temp_folder\\copy.txt', 'w') as target_file: # in place of 'copy.txt' you can use any file path(C:\\Users\\user\\Desktop\\copy.txt)
            target_file.write(source_file.read())
    print('File copied successfully')
except FileNotFoundError:
    print('File not found while copying')
except:
    print('Error occurred while copying file')