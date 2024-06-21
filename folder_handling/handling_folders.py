import os

# Define parent directory and directory name
parent_dir = "C:\\Python_BootCamp\\Python-Basics\\folder_handling"
dir_name = "new_folder"

# Create a new folder
new_folder_path = os.path.join(parent_dir, dir_name)
os.mkdir(new_folder_path)

# Check if a folder exists
existing_folder_path = os.path.join(parent_dir, dir_name)
if os.path.exists(existing_folder_path):
    print("Folder exists")
else:
    print("Folder does not exist")

# Rename a folder
renamed_folder_path = os.path.join(parent_dir, "renamed_folder")
os.rename(existing_folder_path, renamed_folder_path)

# Delete a folder
# os.rmdir(renamed_folder_path)

# List all folders in a directory
folders = [f for f in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, f))]
print(folders)