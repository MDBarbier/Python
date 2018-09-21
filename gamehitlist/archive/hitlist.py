#!/user/bin/python3

import functions
import json

functions.new_line(3)

profileName = functions.get_profile()

if (profileName):
    print('Welcome to the gamehitlist application, ' + profileName)
else:
    userName = input('Enter a name for your profile:')
    profileName = functions.create_profile(userName) 
    print('Welcome to the gamehitlist application, ' + profileName)


functions.new_line(3)

# TODO - put main menu rendering into function
print("Main menu")
print("")
print("1. Add new list")
print("2. View list")
print("3. Exit")

userChoice = ""

while userChoice == "" or not userChoice.isdigit():
    userChoice = input("Please choose an option:")


if userChoice == "1":
    #functions.add_list() # TODO create function
    print("adding lists")
    my_json_string = json.dumps({'key1': "val1", 'key2': "val2"})
    functions.create_list("list1", my_json_string)
elif userChoice == "2":
    #functions.view_lists() # TODO create funtion
    print("viewing lists")
elif userChoice == "3":
    print("Exiting program")
    exit()


print('Execution finished, exiting')

