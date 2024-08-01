import os
import shutil

# Specify the directory paths to the vaults you want to iterate through
vaultOneDir = "/Users/mbarbier/OneDrive - Ordnance Survey/Python" #this is the format for Powershell/Windows
vaultOneDirWSL = "/mnt/c/Users/mbarbier/OneDrive - Ordnance Survey/Python/" #this is format when running in Python/WSL
vaultTwoDir = "/repos/Python/Migrated" #this is the format for Powershell/Windows
vaultTwoDirWSL = "/mnt/c/repos/Python/Migrated" #this is format when running in Python/WSL

# Uncomment these 2 lines if running in WSL/Linux
vaultOneDir = vaultOneDirWSL
vaultTwoDir = vaultTwoDirWSL

# Folders we want to copy
foldersToCopy = ['Tech', 'Architecture', 'Azure']

def CopyFile (src, dest):
    return shutil.copy(src, dest)

def CreateDir (directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

# Create the directories if they don't exist
CreateDir(vaultTwoDir)

# Iterate through the list of folders to copy
for filename in os.listdir(vaultOneDir):
    print("Found file: " + filename)
    newFilePath = CopyFile(vaultOneDir + "/" + filename, vaultTwoDir + "/" + filename)
    print("Copied file to: " + newFilePath)