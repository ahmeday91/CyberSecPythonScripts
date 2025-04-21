import os

# example path: windows: "C:\\Windows", mac/linux: "/etc"
directory_path = input("Please enter a directory path: ")

# Build a list of all file and directory names
# in the specified directory
items_in_directory = os.listdir(directory_path)

for item in items_in_directory:
    item_path = os.path.join(directory_path, item)
    if os.path.isdir(item_path):
        print("Directory", item)
    elif os.path.isfile(item_path):
        size = os.path.getsize(item_path)
        print("File", item, "File size: ", size)