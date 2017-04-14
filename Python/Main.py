import Dice
import sys
import xml.etree.cElementTree as ET
from pathlib import Path

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


def setup():

    my_file = Path("C:\\Users\\matt-dev\\Documents\\GitHub\\Misc\\Python\\data.xml")

    if my_file.is_file():
        return
        #file exists
    else:
        root = ET.Element("root")
        tree = ET.ElementTree(root)

        myself = ET.SubElement(root, "myself")
        users = ET.SubElement(root, "users")

        ET.SubElement(myself, "myname", name="AIv1").text = "AIv1"

        tree.write("data.xml")


def getData(element, entity):

    tree = ET.parse("data.xml")
    root = tree.getroot()
    val = tree.find(entity + "/" + element)
    return val.text

#---------------------

#---------- Instance variable declarations
name = ""
command = ""
#-----------------------------------------

#---------- main loop

setup()

print("Welcome.")
name = input("What is your name?")

if not name:
    name = "anonymous"

if name == "anonymous":
    print("Well as you didn't tell me your name I'll just call you Bob. Ok, Bob?")
else:
    print("Hello " + name)

print("My name is " + getData("myname", "myself") + ".")

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
