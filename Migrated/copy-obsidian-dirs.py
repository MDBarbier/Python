import os
import shutil

# Specify the directory paths to the vaults you want to iterate through
vaultOneDir = "/Users/mbarbier/OneDrive - Ordnance Survey/OS Notes" #this is the format for Powershell/Windows
vaultOneDirWSL = "/mnt/c/Users/mbarbier/OneDrive - Ordnance Survey/OS Notes/" #this is format when running in Python/WSL
vaultTwoDir = "/repos/Obsidian/Migrated" #this is the format for Powershell/Windows
vaultTwoDirWSL = "/mnt/c/repos/Obsidian/Migrated" #this is format when running in Python/WSL

# Uncomment these 2 lines if running in WSL/Linux
vaultOneDir = vaultOneDirWSL
vaultTwoDir = vaultTwoDirWSL

# Folders we want to copy
foldersToCopy = ['Tech', 'Architecture', 'Azure']

def CopyDirectory (directory, destinationDir):
    return shutil.copytree(directory, destinationDir, dirs_exist_ok=True)

# Iterate through the list of folders to copy
for folder in foldersToCopy:
    if folder in foldersToCopy:
        print("Found folder: " + folder)
        newPath = CopyDirectory(str(vaultOneDir) + "/" + folder, str(vaultTwoDir) + "/" + folder)
        print("Copied folder to: " + newPath)