import os

# Method 1: Using raw strings
path = "D:\Github\Obsidian"

# Method 2: Using double backslashes
# path = "D:\\Github\\Obsidian"

# Method 3: Using forward slashes
# path = "D:/Github/Obsidian"

# Method 4: Using os.path.join
# path = os.path.join("D:", "Github", "Obsidian")


# Example function to list contents of the directory
def list_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")


# List contents of the specified path
list_directory_contents(path)
