import os
import shutil

# Test case for reading a file
def test_read_file():
    text = 'This is a test file'
    with open('test.txt', 'w') as file:
        file.write(text)
    try:
        with open('test.txt', 'r') as file:
            if file.read() == text:
                result = 'File read successfully'
            else:
                result = 'File read failed,  Content mismatch'
    except FileNotFoundError:
        result = 'File not found'
    os.remove('test.txt')
    return result

# Test case for writing to a file
def test_write_file():
    text = 'This is a sample text'
    try:
        with open('test.txt', 'w') as file:
            file.write(text)
        result = 'File written successfully'
    except:
        result = 'Error occurred while writing to file'
    os.remove('test.txt')
    return result

# Test case for copying a file
def test_copy_file():
    with open('test.txt', 'w') as file:
        file.write('This is a test file')
    try:
        with open('test.txt', 'r') as source_file:
            with open('copy.txt', 'w') as target_file:
                target_file.write(source_file.read())
        result = 'File copied successfully'
    except FileNotFoundError:
        result = 'File not found'
    except:
        result = 'Error occurred while copying file'
    os.remove('test.txt')
    os.remove('copy.txt')
    return result

# Test case for moving a file
def test_move_file():
    with open('test.txt', 'w') as file:
        file.write('This is a test file')
    try:
        shutil.move('test.txt', 'move.txt')
        result = 'File moved successfully'
    except FileNotFoundError:
        result = 'File not found'
    except Exception as e:
        result = str(e)
        result += 'Error occurred while moving file'
    os.remove('move.txt')
    return result

# Run the test cases
print(test_read_file())
print(test_write_file())
print(test_copy_file())
print(test_move_file())