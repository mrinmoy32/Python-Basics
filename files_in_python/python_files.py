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

# copy using shutil module
import shutil
import datetime

# copyfile: Copies the contents of the source file to the destination file. If the destination file already exists, it will be overwritten.
shutil.copyfile('text.txt', 'copy2.txt') # src, dest

# copy: Copies the source file to the destination file or directory. If the destination is a directory, the source file will be copied with the same name to the destination directory.
shutil.copy('text.txt', 'copy3.txt')

# copy2: Copies the source file to the destination file or directory. It preserves more metadata of the source file, such as timestamps and permissions, compared to the copy function.
shutil.copy2('text.txt', 'copy4.txt')

#### NOT SO IMPORTANT AT THIS MOMENT####
# Get file metadata
file_path = 'copy4.txt'  # Replace with the actual file path
file_stats = os.stat(file_path)

# Access different file metadata
file_size = file_stats.st_size
file_creation_time = file_stats.st_ctime
file_modification_time = file_stats.st_mtime

# Print file metadata
print(f"File Size: {file_size} bytes")
# Convert creation time to datetime object
creation_time = datetime.datetime.fromtimestamp(file_creation_time)

# Convert creation time to IST
creation_time_ist = creation_time.astimezone(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

# Print creation time in IST
print(f"Creation Time: {creation_time_ist}")
print(f"Modification Time: {file_modification_time}")
############

# move a file
try:
    shutil.move('copy4.txt', 'C:\\Python_BootCamp\\Python-Basics\\files_in_python\\temp_folder\\copy4.txt') # src, dest
except FileNotFoundError:
    print('File not found while moving')
except:
    print('Error occurred while moving file')

# move a file using os
source = 'copy3.txt'
destination = 'C:\\Python_BootCamp\\Python-Basics\\files_in_python\\temp_folder\\copy3.txt'
try:
    if os.path.exists(destination):
        print('File already exists')
    else:
        os.replace(source, destination) 
        # os.rename(source, destination) # both replace and rename can be used
        print(source + ' moved successfully')
except FileNotFoundError:
    print('File not found while moving')
except Exception as e:
    print(e)
    print('Error occurred while moving file')

# we can also move folders using shutil.move() and os.replace() or os.rename() methods
source = 'move_folder'
destination = 'C:\\Python_BootCamp\\Python-Basics\\files_in_python\\temp_folder\\move_folder'
shutil.move(source , destination) # src, dest

source = 'move_folder2'
destination = 'C:\\Python_BootCamp\\Python-Basics\\files_in_python\\temp_folder\\move_folder2'
os.replace(source, destination) # src, dest

# delete a file
file_path = 'temp_folder\\copy3.txt'
try:
    os.remove(file_path)
    print(file_path + ' File deleted successfully')
except FileNotFoundError:
    print('File not found while deleting')
