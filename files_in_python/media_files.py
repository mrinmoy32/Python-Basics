# To copy binary files (like images, videos, etc.), you should open the files in binary mode ('rb' and 'wb').

source_path = './temp_folder/source_image.jpg'
destination_path = './temp_folder/destination_image.jpg'

# Open the source file in binary read mode and the destination file in binary write mode
with open(source_path, 'rb') as source_file:
    content = source_file.read()  # Read the entire content of the source file

with open(destination_path, 'wb') as destination_file:
    destination_file.write(content)  # Write the content to the destination file

print("File copied successfully!")
