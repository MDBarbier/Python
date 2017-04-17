import Dice
import sys
import xml.etree.cElementTree as ET
from pathlib import Path

#----------- Functions
def pokerdice():

    input("OK, you roll your dice first. Press any key to roll.")
    roll1 = Dice.rolldie("d6")
    roll2 = Dice.rolldie("d6")
    roll3 = Dice.rolldie("d6")
    roll4 = Dice.rolldie("d6")
    roll5 = Dice.rolldie("d6")
    print("You rolled " + str(roll1) + " , " + str(roll2) + " , " + str(roll3) + " , " + str(roll4) + " , " + str(roll5) + ".")

    roll6 = Dice.rolldie("D6")
    roll7 = Dice.rolldie("D6")
    roll8 = Dice.rolldie("D6")
    roll9 = Dice.rolldie("D6")
    roll10 = Dice.rolldie("D6")
    print("I rolled " + str(roll6) + " , " + str(roll7) + " , " + str(roll8) + " , " + str(roll9) + " , " + str(roll10) + ".")



def exit():
    input("Execution finished, press any key to exit. ")
    sys.exit()


def setup():

    my_file = Path("C:\\Users\\matt-dev\\Documents\\GitHub\\Misc\\Python\\playerdata.xml")

    if my_file.is_file():
        return
        #file exists
    else:
        root = ET.Element("root")
        tree = ET.ElementTree(root)

        players = ET.SubElement(root, "players")

        ET.SubElement(players, "player", name="AI").text = "AI"

        tree.write("playerdata.xml")


def addPlayer(value):

    tree = ET.parse("playerdata.xml")

    players = tree.find("players")

    for p in players:
        if p.text == value:
            return False

    newElement = ET.SubElement(players, "player", name=value).text = value
    tree.write('playerdata.xml')
    return True
#---------------------

#---------- Instance variable declarations
name = ""
command = ""
#-----------------------------------------

#---------- main loop

setup()

print("Welcome to Poker Dice.")
name = input("What is your name? ")

if not name:
    name = "anonymous"

if name.upper() == "AI":
    print("You can't be called AI, that's my name!")
    name = "anonymous"

if name == "anonymous":
    print("Well as you didn't tell me your name I'll just call you anon.")
    print("By the way, did you know you're the most prolific poet in the history of mankind. Fun fact for you.")
else:
    name = name.title()
    print("Hello " + name)
    result = addPlayer(name)
    if not result:
        print("Welcome back.")
    else:
        print("This is your first time, enjoy!")

#loop until user does not want to play anymore
while command != "no":

    command = input("Shall we play Poker Dice? ").lower()

    if command.lower() == "no":
        continue
    elif command.lower() == "yes":
        pokerdice()
    else:
        print("Sorry I don't understand the command \"" + command + "\"")


exit()

#--------------------
