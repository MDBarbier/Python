import os
import shutil

# Specify the directory paths to the vaults you want to iterate through
vaultTwoDir = "D:\\Github\\Obsidian"

# List to hold file paths
filePaths2 = []


def IterateDirectory(directory, filePaths):
    for filename in os.listdir(directory):
        # Check if the current item is a file
        if os.path.isfile(
            os.path.join(directory, filename)
        ) and filename.lower().endswith((".png", ".jpg", ".gif")):
            # Process the file
            filePaths.append(os.path.join(directory, filename))
    return filePaths


def CreateImageDir(directory):
    if not os.path.exists(directory + "\\Images"):
        os.makedirs(directory + "\\Images")
    # else:
    # print("Folder already exists!")
    return directory + "\\Images"


def MoveFiles(filePaths, destinationDir):
    for filePath in filePaths:
        if os.path.exists(destinationDir + filePath.split("\\")[-1]):
            print("File already exists: " + filePath)
        else:
            # print("Pretending to move file: " + filePath)
            # print ("To: " + destinationDir)
            resultantPath = shutil.move(filePath, destinationDir)
            print("Moved file to: {}".format(resultantPath))


# Get the file paths for files to move for both vaults
filePaths2 = IterateDirectory(vaultTwoDir, filePaths2)

# Create a directory to store the images if it doesn't exist
CreateImageDir(vaultTwoDir)

# Move the files to the new directory for both vaults
MoveFiles(filePaths2, vaultTwoDir + "\\Images")
