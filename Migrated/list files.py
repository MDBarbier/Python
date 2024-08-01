import os

# Specify the directory path you want to iterate through
usersDir = "/Users/mbarbier"
ordnanceSurveyDir = usersDir + "/OneDrive - Ordnance Survey"
directory = ordnanceSurveyDir + "/Useful/icons"

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the current item is a file
    if os.path.isfile(os.path.join(directory, filename)):
        # Process the file
        print(filename)
