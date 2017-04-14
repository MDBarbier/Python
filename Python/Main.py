import Dice
import sys

#----------- Functions
def roll():
    dieToRoll = input("OK, what kind?")
    result = Dice.rolldie(dieToRoll)

    if result == "Unrecognized type":
        print("Sorry that's not a die I know.")
    else:
        print("You rolled a " + str(result) + " on your " + dieToRoll.upper())

def dice():

    success = roll()

    another = True

    while another:
        anotherAnswer = input("Again?")

        if anotherAnswer.lower() == "exit":
            exit()
        elif anotherAnswer.lower() == "true" or anotherAnswer.lower() == "yes" or anotherAnswer.lower() == "y":
            another = True
        else:
            another = False

        if another:
            roll()

def exit():
    print ("Execution finished, press any key to exit.")
    sys.exit()
#---------------------

#---------- Instance variable declarations
name = ""
command = ""
myname = "AIv1"
#-----------------------------------------

#---------- main loop

print("Welcome.")
name = input("What is your name?")

if not name:
    name = "anonymous"

if name == "anonymous":
    print("Well as you didn't tell me your name I'll just call you Bob. Ok, Bob?")
else:
    print("Hello " + name)

print("My name is " + myname + ".")

while command != "exit":

    command = input("What would you like to do?").lower()

    if command == "exit":
        continue
    elif command == "dice":
        dice()
    else:
        print("Sorry I don't understand the command \"" + command + "\"")


exit()

#--------------------
